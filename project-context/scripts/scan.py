#!/usr/bin/env python3
"""Dev Context Platform — scan CLI."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PLAYBOOK_ROOT = SCRIPT_DIR.parent.parent
PROJECTS_DIR = PLAYBOOK_ROOT / "project-context" / "projects"

sys.path.insert(0, str(SCRIPT_DIR))

import yaml
from ado_client import list_repos
from detectors.stack_detector import compute_quality_score, detect_stack
from git_ops import (
    GitError,
    count_commits,
    diff_changed_files,
    diff_name_status,
    fetch,
    get_commit_date,
    log_oneline,
    resolve_ref,
    verify_branch_alignment,
)
from indexers.csharp_indexer import index_csharp_files, merge_roslyn_output, run_roslyn_cli
from indexers.indexing_profile import resolve_indexing_config
from integration_graph import generate_integration_graph
from vault_link import build_vault


ENGINEERING_DIR = ".engineering"


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load_yaml(path: Path) -> dict:
    if not path.is_file():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def _save_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")


def _load_json(path: Path) -> dict:
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _save_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def project_dir_for(name: str) -> Path:
    return PROJECTS_DIR / name


def load_project_map(project: str) -> dict:
    path = project_dir_for(project) / "project-map.yaml"
    if not path.is_file():
        raise SystemExit(f"project-map não encontrado: {path}\nExecute: scan init --project {project}")
    return _load_yaml(path)


def resolve_repo_path(project_dir: Path, repo_cfg: dict) -> Path | None:
    local = repo_cfg.get("local_path")
    if local:
        p = Path(local)
        if not p.is_absolute():
            p = (project_dir / local).resolve()
        if p.is_dir():
            return p
    name = repo_cfg["name"]
    candidates = [
        project_dir.parent / name,
        PLAYBOOK_ROOT.parent / name,
        Path.cwd() / name,
    ]
    for c in candidates:
        if c.is_dir() and (c / ".git").is_dir():
            return c.resolve()
    return None


def write_repo_profile(
    eng_dir: Path,
    repo_name: str,
    detection,
    quality_score: int,
    debt_level: str,
    source_commit: str,
    reference_branch: str,
    indexer_available: bool,
    indexing_profile: str = "standard",
) -> None:
    profile = {
        "name": repo_name,
        "stack": detection.stacks,
        "quality_score": quality_score,
        "debt_level": debt_level,
        "patterns": detection.patterns,
        "folder_structure": detection.folder_structure,
        "integration_hints": detection.integration_hints,
        "indexer_available": indexer_available,
        "indexing_profile": indexing_profile,
        "last_scan_at": _now_iso(),
        "source_commit": source_commit,
        "reference_branch": reference_branch,
    }
    _save_yaml(eng_dir / "repo-profile.yaml", profile)

    readme_tpl = (PLAYBOOK_ROOT / "project-context" / "templates" / "README.engineering.md").read_text(
        encoding="utf-8"
    )
    folder_lines = "\n".join(f"- `{k}` — {v}" for k, v in detection.folder_structure.items()) or "_Não detectada._"
    hints_lines = "\n".join(f"- {h}" for h in detection.integration_hints) or "_Nenhuma._"
    indexer_status = "Disponível (C#)" if indexer_available else "Scan leve apenas — indexer profundo indisponível para stack"
    readme = readme_tpl.format(
        repo_name=repo_name,
        stack_list=", ".join(detection.stacks) or "Não detectada",
        dominant_pattern=detection.patterns.get("dominant", ""),
        recommended_pattern=detection.patterns.get("recommended", ""),
        quality_score=quality_score,
        debt_level=debt_level,
        folder_structure=folder_lines,
        integration_hints=hints_lines,
        indexer_status=indexer_status,
        reference_branch=reference_branch,
        source_commit=source_commit[:12] if source_commit else "—",
        last_scan_at=_now_iso(),
    )
    (eng_dir / "README.engineering.md").write_text(readme, encoding="utf-8")


def write_manifest(
    eng_dir: Path,
    nodes,
    source_commit: str,
    reference_branch: str,
    indexing_profile: str = "standard",
) -> None:
    manifest = {
        "version": "1",
        "generated_at": _now_iso(),
        "reference_branch": reference_branch,
        "source_commit": source_commit,
        "indexing_profile": indexing_profile,
        "nodes": [
            {
                "id": n.id,
                "path": n.path,
                "tags": n.tags,
                "keywords": n.keywords[:20],
                "wikilinks": n.wikilinks,
                "tipo": n.tipo,
                "source_file": n.source_file,
                "source_commit": source_commit,
                "reference_branch": reference_branch,
            }
            for n in nodes
        ],
        "broken_wikilinks": _find_broken_wikilinks(nodes),
    }
    _save_json(eng_dir / "kb" / "manifest.json", manifest)


def _find_broken_wikilinks(nodes) -> list[str]:
    ids = {n.id for n in nodes}
    broken: set[str] = set()
    for n in nodes:
        for link in n.wikilinks:
            if link not in ids:
                broken.add(link)
    return sorted(broken)


def write_kb_nodes(eng_dir: Path, nodes, *, full_replace: bool = False) -> None:
    nodes_dir = eng_dir / "kb" / "nodes"
    nodes_dir.mkdir(parents=True, exist_ok=True)
    if full_replace:
        keep_ids = {n.id for n in nodes}
        for stale in nodes_dir.glob("*.md"):
            if stale.stem not in keep_ids:
                stale.unlink()
    for n in nodes:
        (nodes_dir / f"{n.id}.md").write_text(n.content, encoding="utf-8")


def update_sync_state(
    eng_dir: Path,
    reference_branch: str,
    indexed_sha: str,
    previous_sha: str | None,
    trigger: str,
    files_changed: int = 0,
    nodes_updated: int = 0,
    nodes_removed: int = 0,
    working_branch: str | None = None,
    remote_head: str | None = None,
) -> dict:
    state_path = eng_dir / "sync-state.json"
    state = _load_json(state_path)
    history = state.get("sync_history", [])

    from_sha = previous_sha or state.get("indexed_commit_sha") or indexed_sha
    commits_count = 0
    if previous_sha and previous_sha != indexed_sha:
        commits_count = 1

    history.append(
        {
            "at": _now_iso(),
            "from_sha": from_sha,
            "to_sha": indexed_sha,
            "commits_count": commits_count,
            "files_changed": files_changed,
            "nodes_updated": nodes_updated,
            "nodes_removed": nodes_removed,
            "trigger": trigger,
        }
    )
    history = history[-50:]

    remote_head = remote_head or indexed_sha
    is_stale = remote_head != indexed_sha

    new_state = {
        "reference_branch": reference_branch,
        "working_branch": working_branch,
        "indexed_commit_sha": indexed_sha,
        "indexed_commit_date": get_commit_date(Path(eng_dir).parent, indexed_sha) if indexed_sha else None,
        "previous_commit_sha": previous_sha,
        "sync_history": history,
        "staleness": {
            "is_stale": is_stale,
            "remote_head_sha": remote_head,
            "commits_behind": 0 if not is_stale else 1,
        },
    }
    _save_json(state_path, new_state)
    return new_state


def scan_repo(
    repo_path: Path,
    repo_cfg: dict,
    *,
    project_map: dict | None = None,
    force: bool = False,
    dry_run: bool = False,
    branch: str | None = None,
    trigger: str = "manual",
    incremental_from: str | None = None,
) -> dict:
    repo_name = repo_cfg["name"]
    status = repo_cfg.get("status", "active")
    reference_branch = branch or repo_cfg.get("reference_branch", "main")
    eng_dir = repo_path / ENGINEERING_DIR

    if status in ("legacy", "discontinued") and not force:
        return {"repo": repo_name, "skipped": True, "reason": f"status={status}"}

    if not (repo_path / ".git").is_dir():
        return {"repo": repo_name, "skipped": True, "reason": "not a git repo"}

    try:
        fetch(repo_path, reference_branch)
        head_sha = resolve_ref(repo_path, reference_branch)
    except GitError as e:
        return {"repo": repo_name, "skipped": True, "reason": str(e)}

    state = _load_json(eng_dir / "sync-state.json")
    indexed_sha = state.get("indexed_commit_sha")
    sync_branch = branch or reference_branch

    if not force and indexed_sha == head_sha and not incremental_from:
        return {"repo": repo_name, "skipped": True, "reason": "already up to date", "commit": head_sha}

    changed_files: list[str] = []
    if incremental_from and indexed_sha and not force:
        changed_files = diff_changed_files(repo_path, indexed_sha, head_sha)
        if not changed_files and indexed_sha == head_sha:
            return {"repo": repo_name, "skipped": True, "reason": "already up to date"}

    if dry_run:
        logs = log_oneline(repo_path, indexed_sha or head_sha, head_sha) if indexed_sha else []
        return {
            "repo": repo_name,
            "dry_run": True,
            "from": indexed_sha,
            "to": head_sha,
            "commits": logs,
            "files": changed_files or ["__full_scan__"],
        }

    detection = detect_stack(repo_path)
    quality_score, debt_level = compute_quality_score(repo_path, detection)
    indexer_available = "dotnet" in detection.stacks
    indexing = resolve_indexing_config(repo_cfg, project_map)

    eng_dir.mkdir(parents=True, exist_ok=True)

    nodes = []
    full_scan = not (changed_files and indexed_sha)
    if indexer_available:
        files_to_index = changed_files if changed_files and indexed_sha else None
        if files_to_index:
            cs_files = [f for f in files_to_index if f.endswith(".cs")]
            new_nodes = index_csharp_files(
                repo_path,
                repo_name,
                head_sha,
                sync_branch,
                files=cs_files or None,
                indexing=indexing,
            )
            existing_manifest = _load_json(eng_dir / "kb" / "manifest.json")
            # Remove nodes for deleted source files from delta
            removed_sources = {
                e.path for e in diff_name_status(repo_path, indexed_sha, head_sha)
                if e.status.startswith("D") and e.path.endswith(".cs")
            }
            kept_nodes = [
                n for n in existing_manifest.get("nodes", [])
                if n.get("source_file") not in removed_sources
            ]
            # Reload existing node files for kept entries
            nodes_dir = eng_dir / "kb" / "nodes"
            from indexers.csharp_indexer import KBNode
            for entry in kept_nodes:
                node_path = eng_dir / entry.get("path", f"kb/nodes/{entry['id']}.md")
                if node_path.is_file() and entry["source_file"] not in {n.source_file for n in new_nodes}:
                    content = node_path.read_text(encoding="utf-8")
                    nodes.append(
                        KBNode(
                            id=entry["id"],
                            path=entry.get("path", f"kb/nodes/{entry['id']}.md"),
                            title=entry["id"].split("_", 1)[-1],
                            tags=entry.get("tags", []),
                            tipo=entry.get("tipo", ""),
                            namespace="",
                            source_file=entry.get("source_file", ""),
                            source_hash="",
                            keywords=entry.get("keywords", []),
                            wikilinks=entry.get("wikilinks", []),
                            content=content,
                        )
                    )
            nodes.extend(new_nodes)
            roslyn_out = eng_dir / "kb" / ".roslyn-output.json"
            if run_roslyn_cli(repo_path, roslyn_out):
                nodes = merge_roslyn_output(nodes, roslyn_out, repo_name)
        else:
            full_scan = True
            nodes = index_csharp_files(
                repo_path,
                repo_name,
                head_sha,
                sync_branch,
                indexing=indexing,
            )
            roslyn_out = eng_dir / "kb" / ".roslyn-output.json"
            if run_roslyn_cli(repo_path, roslyn_out):
                nodes = merge_roslyn_output(nodes, roslyn_out, repo_name)

    write_repo_profile(
        eng_dir, repo_name, detection, quality_score, debt_level,
        head_sha, sync_branch, indexer_available, indexing.profile,
    )
    if nodes:
        write_kb_nodes(eng_dir, nodes, full_replace=full_scan)
        write_manifest(eng_dir, nodes, head_sha, sync_branch, indexing.profile)

    files_changed = len(changed_files) if changed_files else 0
    update_sync_state(
        eng_dir,
        reference_branch=repo_cfg.get("reference_branch", "main"),
        indexed_sha=head_sha,
        previous_sha=indexed_sha,
        trigger=trigger,
        files_changed=files_changed,
        nodes_updated=len(nodes),
        working_branch=branch,
        remote_head=head_sha,
    )

    return {
        "repo": repo_name,
        "commit": head_sha,
        "branch": sync_branch,
        "nodes": len(nodes),
        "indexing_profile": indexing.profile,
        "quality_score": quality_score,
        "files_changed": files_changed,
    }


def update_central_scan_state(project: str, results: list[dict]) -> None:
    central = project_dir_for(project) / "scan-state.json"
    data = _load_json(central)
    data["updated_at"] = _now_iso()
    data["repos"] = data.get("repos", {})

    for r in results:
        if r.get("skipped"):
            continue
        name = r["repo"]
        repo_path = None
        pmap = load_project_map(project)
        for cfg in pmap.get("repos", []):
            if cfg["name"] == name:
                repo_path = resolve_repo_path(project_dir_for(project), cfg)
                break
        if repo_path:
            state = _load_json(repo_path / ENGINEERING_DIR / "sync-state.json")
            data["repos"][name] = {
                "indexed_commit_sha": state.get("indexed_commit_sha"),
                "reference_branch": state.get("reference_branch"),
                "staleness": state.get("staleness"),
                "last_sync": _now_iso(),
            }
    _save_json(central, data)


def cmd_init(args: argparse.Namespace) -> int:
    project = args.project
    pdir = project_dir_for(project)
    pmap_path = pdir / "project-map.yaml"

    if args.discover_ado and not pmap_path.is_file():
        org = args.organization or "aguiabranca"
        try:
            ado_repos = list_repos(org, project)
        except RuntimeError as e:
            print(f"AVISO: não foi possível listar repos ADO: {e}", file=sys.stderr)
            ado_repos = []

        pmap = {
            "project": project,
            "organization": org,
            "default_reference_branch": "main",
            "default_indexing": {"profile": "standard"},
            "updated_at": _now_iso(),
            "repos": [
                {
                    "name": r.name,
                    "status": "active",
                    "reference_branch": r.default_branch,
                    "ado_url": r.url,
                    "stack": [],
                    "description": "",
                }
                for r in ado_repos
            ],
        }
        _save_yaml(pmap_path, pmap)
        print(f"Criado {pmap_path} com {len(ado_repos)} repos do ADO.")
    elif not pmap_path.is_file():
        tpl = (PLAYBOOK_ROOT / "project-context" / "templates" / "project-map.yaml").read_text(encoding="utf-8")
        pmap_path.parent.mkdir(parents=True, exist_ok=True)
        pmap_path.write_text(tpl.replace("SeuProjeto", project), encoding="utf-8")
        print(f"Criado template em {pmap_path} — edite repos antes de continuar.")
        return 0

    pmap = load_project_map(project)
    results = []
    for repo_cfg in pmap.get("repos", []):
        if args.repo and repo_cfg["name"] != args.repo:
            continue
        repo_path = resolve_repo_path(pdir, repo_cfg)
        if not repo_path:
            print(f"AVISO: caminho não encontrado para {repo_cfg['name']}", file=sys.stderr)
            continue
        print(f"Init {repo_cfg['name']} @ {repo_path}")
        results.append(scan_repo(repo_path, repo_cfg, project_map=pmap, force=True, trigger="manual"))

    update_central_scan_state(project, results)
    _regenerate_integration_graph(project)
    for r in results:
        print(json.dumps(r, indent=2))
    return 0


def cmd_sync(args: argparse.Namespace) -> int:
    project = args.project
    pmap = load_project_map(project)
    pdir = project_dir_for(project)
    results = []

    for repo_cfg in pmap.get("repos", []):
        if args.repo and repo_cfg["name"] != args.repo:
            continue
        repo_path = resolve_repo_path(pdir, repo_cfg)
        if not repo_path:
            print(f"AVISO: caminho não encontrado para {repo_cfg['name']}", file=sys.stderr)
            continue

        state = _load_json(repo_path / ENGINEERING_DIR / "sync-state.json")
        indexed = state.get("indexed_commit_sha")

        print(f"Sync {repo_cfg['name']} @ {repo_path}")
        results.append(
            scan_repo(
                repo_path,
                repo_cfg,
                project_map=pmap,
                force=args.force,
                dry_run=args.dry_run,
                branch=args.branch,
                trigger=args.trigger,
                incremental_from=indexed,
            )
        )

    if not args.dry_run:
        update_central_scan_state(project, results)
        _regenerate_integration_graph(project)

    for r in results:
        print(json.dumps(r, indent=2))
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    project = args.project
    pmap = load_project_map(project)
    pdir = project_dir_for(project)

    print(f"{'Repo':<30} {'Ref branch':<15} {'Indexed':<12} {'Stale':<8} {'Behind'}")
    print("-" * 80)

    for repo_cfg in pmap.get("repos", []):
        if args.repo and repo_cfg["name"] != args.repo:
            continue
        repo_path = resolve_repo_path(pdir, repo_cfg)
        name = repo_cfg["name"]
        ref = repo_cfg.get("reference_branch", "main")

        if not repo_path or not (repo_path / ".git").is_dir():
            print(f"{name:<30} {'—':<15} {'—':<12} {'?':<8} —")
            continue

        state = _load_json(repo_path / ENGINEERING_DIR / "sync-state.json")
        indexed = (state.get("indexed_commit_sha") or "—")[:12]
        stale = state.get("staleness", {}).get("is_stale", True)
        behind = state.get("staleness", {}).get("commits_behind", "?")

        try:
            fetch(repo_path, ref)
            head = resolve_ref(repo_path, ref)
            if state.get("indexed_commit_sha"):
                behind = count_commits(repo_path, state["indexed_commit_sha"], head)
                stale = behind > 0
        except GitError:
            pass

        print(f"{name:<30} {ref:<15} {indexed:<12} {str(stale):<8} {behind}")

    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    project = args.project
    branch = args.branch
    if not branch:
        print("Erro: --branch é obrigatório para verify", file=sys.stderr)
        return 1

    pmap = load_project_map(project)
    pdir = project_dir_for(project)
    exit_code = 0

    for repo_cfg in pmap.get("repos", []):
        if args.repo and repo_cfg["name"] != args.repo:
            continue
        repo_path = resolve_repo_path(pdir, repo_cfg)
        if not repo_path:
            continue

        ref = repo_cfg.get("reference_branch", "main")
        state = _load_json(repo_path / ENGINEERING_DIR / "sync-state.json")
        indexed = state.get("indexed_commit_sha")

        try:
            result = verify_branch_alignment(repo_path, branch, ref, indexed)
        except GitError as e:
            print(json.dumps({"repo": repo_cfg["name"], "error": str(e)}, indent=2))
            exit_code = 1
            continue

        payload = {
            "repo": repo_cfg["name"],
            "status": result.status,
            "reference_branch": result.reference_branch,
            "working_branch": result.working_branch,
            "indexed_commit_sha": result.indexed_commit_sha,
            "remote_head_sha": result.remote_head_sha,
            "merge_base_sha": result.merge_base_sha,
            "kb_ahead_files": result.kb_ahead_files,
            "branch_unique_files": result.branch_unique_files,
            "commits_behind": result.commits_behind,
            "message": result.message,
        }
        print(json.dumps(payload, indent=2, ensure_ascii=False))

        if result.status in ("ref_stale", "divergent", "branch_not_found", "not_indexed"):
            exit_code = 1

    return exit_code


def cmd_vault_link(args: argparse.Namespace) -> int:
    project = args.project
    pmap = load_project_map(project)
    pdir = project_dir_for(project)
    result = build_vault(
        project,
        pdir,
        pmap,
        resolve_repo_path,
        output_dir=args.output,
        repo_filter=args.repo,
        copy=args.copy,
        force=args.force,
        dry_run=args.dry_run,
    )

    if result.get("error"):
        print(result["error"], file=sys.stderr)
        return 1

    print(json.dumps(result, indent=2, ensure_ascii=False))

    if not args.dry_run:
        print(f"\nVault pronto: {result['vault_dir']}")
        print("Abra esta pasta como vault no Obsidian (Graph view + WikiLinks).")

    return 0


def _regenerate_integration_graph(project: str) -> None:
    pmap = load_project_map(project)
    pdir = project_dir_for(project)
    repo_paths = {}
    for cfg in pmap.get("repos", []):
        p = resolve_repo_path(pdir, cfg)
        if p:
            repo_paths[cfg["name"]] = p
    md = generate_integration_graph(pmap, pdir, repo_paths)
    out = pdir / "integration-graph.md"
    out.write_text(md, encoding="utf-8")
    print(f"Atualizado {out}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Dev Context Platform — scan CLI")
    parser.add_argument("--playbook-root", type=Path, default=PLAYBOOK_ROOT)
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init", help="Primeiro scan full + project-map")
    p_init.add_argument("--project", required=True)
    p_init.add_argument("--repo", help="Limitar a um repo")
    p_init.add_argument("--organization", help="Organização ADO para discover")
    p_init.add_argument("--discover-ado", action="store_true", help="Listar repos do Azure DevOps")

    p_sync = sub.add_parser("sync", help="Sync incremental na branch de referência")
    p_sync.add_argument("--project", required=True)
    p_sync.add_argument("--repo")
    p_sync.add_argument("--branch", help="Branch alternativa (feature branch)")
    p_sync.add_argument("--force", action="store_true")
    p_sync.add_argument("--dry-run", action="store_true")
    p_sync.add_argument("--trigger", default="manual", choices=["manual", "ci", "scheduled"])

    p_status = sub.add_parser("status", help="Staleness por repo")
    p_status.add_argument("--project", required=True)
    p_status.add_argument("--repo")

    p_verify = sub.add_parser("verify", help="Validar alinhamento KB vs branch de trabalho")
    p_verify.add_argument("--project", required=True)
    p_verify.add_argument("--branch", required=True)
    p_verify.add_argument("--repo")

    p_vault = sub.add_parser("vault-link", help="Montar vault Obsidian com symlinks da KB escaneada")
    p_vault.add_argument("--project", required=True)
    p_vault.add_argument("--repo", help="Limitar a um repo")
    p_vault.add_argument("--output", type=Path, help="Pasta do vault (default: projects/{projeto}/vault)")
    p_vault.add_argument("--copy", action="store_true", help="Copiar arquivos em vez de symlinks")
    p_vault.add_argument("--force", action="store_true", help="Recriar links existentes")
    p_vault.add_argument("--dry-run", action="store_true", help="Simular sem criar links")

    args = parser.parse_args()
    handlers = {
        "init": cmd_init,
        "sync": cmd_sync,
        "status": cmd_status,
        "verify": cmd_verify,
        "vault-link": cmd_vault_link,
    }
    return handlers[args.command](args)


if __name__ == "__main__":
    raise SystemExit(main())
