"""Obsidian vault linker — symlinks project-context KB into a single vault folder."""

from __future__ import annotations

import json
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ENGINEERING_DIR = ".engineering"


@dataclass
class ScannedRepo:
    name: str
    repo_path: Path
    indexed_commit_sha: str | None
    last_sync: str | None
    node_count: int


def _load_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _has_kb(repo_path: Path) -> bool:
    eng = repo_path / ENGINEERING_DIR
    manifest = eng / "kb" / "manifest.json"
    nodes_dir = eng / "kb" / "nodes"
    if manifest.is_file():
        return True
    if nodes_dir.is_dir() and any(nodes_dir.glob("*.md")):
        return True
    return False


def _count_nodes(repo_path: Path) -> int:
    nodes_dir = repo_path / ENGINEERING_DIR / "kb" / "nodes"
    if not nodes_dir.is_dir():
        return 0
    return sum(1 for _ in nodes_dir.glob("*.md"))


def resolve_scanned_repos(
    project_map: dict[str, Any],
    project_dir: Path,
    resolve_repo_path,
    *,
    repo_filter: str | None = None,
) -> list[ScannedRepo]:
    """Repos with local clone, KB artifacts, and a completed scan."""
    scan_state = _load_json(project_dir / "scan-state.json")
    central_repos: dict[str, Any] = scan_state.get("repos", {})

    scanned: list[ScannedRepo] = []

    for repo_cfg in project_map.get("repos", []):
        name = repo_cfg["name"]
        if repo_filter and name != repo_filter:
            continue

        repo_path = resolve_repo_path(project_dir, repo_cfg)
        if not repo_path:
            continue
        if not _has_kb(repo_path):
            continue

        central = central_repos.get(name, {})
        repo_sync = _load_json(repo_path / ENGINEERING_DIR / "sync-state.json")
        indexed = central.get("indexed_commit_sha") or repo_sync.get("indexed_commit_sha")
        last_sync = central.get("last_sync") or _last_sync_from_history(repo_sync)

        if not indexed:
            continue

        scanned.append(
            ScannedRepo(
                name=name,
                repo_path=repo_path,
                indexed_commit_sha=indexed,
                last_sync=last_sync,
                node_count=_count_nodes(repo_path),
            )
        )

    return scanned


def _last_sync_from_history(sync_state: dict[str, Any]) -> str | None:
    history = sync_state.get("sync_history") or []
    if not history:
        return None
    return history[-1].get("at")


def _remove_path(path: Path) -> None:
    if not path.exists() and not path.is_symlink():
        return
    if path.is_symlink():
        path.unlink()
        return
    if path.is_dir():
        if sys.platform == "win32":
            import subprocess

            subprocess.run(["cmd", "/c", "rmdir", str(path)], check=False)
            if path.exists():
                shutil.rmtree(path)
        else:
            shutil.rmtree(path)
        return
    path.unlink()


def _link_or_copy(source: Path, dest: Path, *, copy: bool, force: bool) -> str:
    source = source.resolve()
    if not source.exists():
        raise FileNotFoundError(source)

    if dest.exists() or dest.is_symlink():
        if not force:
            return "skipped"
        _remove_path(dest)

    dest.parent.mkdir(parents=True, exist_ok=True)

    if copy:
        if source.is_dir():
            shutil.copytree(source, dest)
        else:
            shutil.copy2(source, dest)
        return "copied"

    if sys.platform == "win32":
        return _link_windows(source, dest)

    dest.symlink_to(source, target_is_directory=source.is_dir())
    return "linked"


def _link_windows(source: Path, dest: Path) -> str:
    import subprocess

    if source.is_dir():
        result = subprocess.run(
            ["cmd", "/c", "mklink", "/J", str(dest), str(source)],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            return "junction"
        raise OSError(result.stderr.strip() or f"mklink /J falhou: {dest}")

    result = subprocess.run(
        ["cmd", "/c", "mklink", "/H", str(dest), str(source)],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        return "hardlink"

    shutil.copy2(source, dest)
    return "copied"


def _write_vault_readme(vault_dir: Path, project: str, repos: list[ScannedRepo]) -> None:
    lines = [
        f"# DCP Vault — {project}",
        "",
        f"> Gerado em {datetime.now(timezone.utc).isoformat()}",
        "",
        "Vault Obsidian para a Dev Context Platform. Abra **esta pasta** como vault no Obsidian.",
        "",
        "## Repos linkados",
        "",
        "| Repo | Commit indexado | Nós KB |",
        "| --- | --- | --- |",
    ]
    for r in repos:
        sha = (r.indexed_commit_sha or "—")[:12]
        lines.append(f"| {r.name} | `{sha}` | {r.node_count} |")

    lines.extend(
        [
            "",
            "## Navegação",
            "",
            "- [[integration-graph]] — visão cross-repo",
            "- `repos/{nome}/kb/nodes/` — notas KB por repositório",
            "",
            "## Atualizar",
            "",
            "```powershell",
            f".\\project-context\\scripts\\dcp.ps1 sync --project {project}",
            f".\\project-context\\scripts\\dcp.ps1 vault-link --project {project} --force",
            "```",
            "",
            "_Links simbólicos apontam para `.engineering/` nos clones locais — rode `vault-link` após sync._",
            "",
        ]
    )
    (vault_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")


def build_vault(
    project: str,
    project_dir: Path,
    project_map: dict[str, Any],
    resolve_repo_path,
    *,
    output_dir: Path | None = None,
    repo_filter: str | None = None,
    copy: bool = False,
    force: bool = False,
    dry_run: bool = False,
) -> dict[str, Any]:
    vault_dir = (output_dir or (project_dir / "vault")).resolve()
    repos = resolve_scanned_repos(
        project_map, project_dir, resolve_repo_path, repo_filter=repo_filter
    )

    if not repos:
        return {
            "project": project,
            "vault_dir": str(vault_dir),
            "repos": [],
            "actions": [],
            "error": "Nenhum repo escaneado com KB encontrado. Execute: dcp sync --project " + project,
        }

    project_links = [
        ("_project/integration-graph.md", project_dir / "integration-graph.md"),
        ("_project/project-map.yaml", project_dir / "project-map.yaml"),
        ("_project/scan-state.json", project_dir / "scan-state.json"),
    ]

    repo_links: list[tuple[str, Path, Path]] = []
    for repo in repos:
        eng = repo.repo_path / ENGINEERING_DIR
        prefix = f"repos/{repo.name}"
        repo_links.extend(
            [
                (f"{prefix}/repo-profile.yaml", eng / "repo-profile.yaml"),
                (f"{prefix}/README.engineering.md", eng / "README.engineering.md"),
                (f"{prefix}/sync-state.json", eng / "sync-state.json"),
                (f"{prefix}/kb/manifest.json", eng / "kb" / "manifest.json"),
                (f"{prefix}/kb/nodes", eng / "kb" / "nodes"),
            ]
        )

    actions: list[dict[str, str]] = []

    if dry_run:
        for rel, src in project_links:
            if src.is_file():
                actions.append({"path": rel, "source": str(src), "action": "would-link"})
        for rel, src in repo_links:
            if src.exists():
                actions.append({"path": rel, "source": str(src), "action": "would-link"})
        actions.append({"path": "README.md", "action": "would-write"})
        return {
            "project": project,
            "vault_dir": str(vault_dir),
            "repos": [r.name for r in repos],
            "actions": actions,
        }

    vault_dir.mkdir(parents=True, exist_ok=True)

    for rel, src in project_links:
        if not src.is_file():
            continue
        dest = vault_dir / rel
        action = _link_or_copy(src, dest, copy=copy, force=force)
        actions.append({"path": rel, "source": str(src), "action": action})

    for rel, src in repo_links:
        if not src.exists():
            continue
        dest = vault_dir / rel
        action = _link_or_copy(src, dest, copy=copy, force=force)
        actions.append({"path": rel, "source": str(src), "action": action})

    _write_vault_readme(vault_dir, project, repos)
    actions.append({"path": "README.md", "action": "written"})

    return {
        "project": project,
        "vault_dir": str(vault_dir),
        "repos": [
            {
                "name": r.name,
                "indexed_commit_sha": r.indexed_commit_sha,
                "node_count": r.node_count,
            }
            for r in repos
        ],
        "actions": actions,
    }
