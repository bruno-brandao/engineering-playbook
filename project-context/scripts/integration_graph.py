"""Cross-repo integration graph generator."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _load_manifest(manifest_path: Path) -> list[dict[str, Any]]:
    if not manifest_path.is_file():
        return []
    return json.loads(manifest_path.read_text(encoding="utf-8")).get("nodes", [])


def _collect_repo_hints(repo_path: Path, engineering_dir: Path) -> dict[str, Any]:
    profile_path = engineering_dir / "repo-profile.yaml"
    hints: list[str] = []
    name = repo_path.name
    stack: list[str] = []

    if profile_path.is_file():
        import yaml

        profile = yaml.safe_load(profile_path.read_text(encoding="utf-8")) or {}
        hints = profile.get("integration_hints", [])
        stack = profile.get("stack", [])
        name = profile.get("name", name)

    manifest_nodes = _load_manifest(engineering_dir / "kb" / "manifest.json")
    external: set[str] = set()
    for node in manifest_nodes:
        for kw in node.get("keywords", []):
            if re.search(r"\[DW\]|SAP|TicketLog|Http", kw, re.I):
                external.add(kw)
        for tag in node.get("tags", []):
            if tag in ("integration", "client", "sap", "dw"):
                external.add(tag)

    return {
        "name": name,
        "stack": stack,
        "integration_hints": hints,
        "manifest_nodes": manifest_nodes,
        "external_refs": sorted(external),
    }


def generate_integration_graph(
    project_map: dict[str, Any],
    project_dir: Path,
    repo_paths: dict[str, Path],
) -> str:
    repos_data: list[dict[str, Any]] = []
    all_nodes: list[dict[str, Any]] = []

    for repo_cfg in project_map.get("repos", []):
        name = repo_cfg["name"]
        status = repo_cfg.get("status", "active")
        local = repo_cfg.get("local_path")
        repo_path = repo_paths.get(name)
        if not repo_path and local:
            candidate = (project_dir / local).resolve()
            if candidate.is_dir():
                repo_path = candidate
        if not repo_path:
            continue

        eng = repo_path / ".engineering"
        info = _collect_repo_hints(repo_path, eng)
        info["status"] = status
        info["reference_branch"] = repo_cfg.get("reference_branch", "main")
        repos_data.append(info)
        all_nodes.extend(info["manifest_nodes"])

    lines = [
        "# Integration Graph",
        "",
        f"> Gerado em {datetime.now(timezone.utc).isoformat()}",
        "",
        "## Repos",
        "",
        "| Repo | Status | Stack | Integrações |",
        "| --- | --- | --- | --- |",
    ]

    for r in repos_data:
        stack = ", ".join(r.get("stack", [])) or "—"
        hints = ", ".join(r.get("integration_hints", [])) or "—"
        lines.append(f"| {r['name']} | {r['status']} | {stack} | {hints} |")

    lines.extend(["", "## Grafo (WikiLinks)", ""])

    for r in repos_data:
        lines.append(f"### {r['name']}")
        nodes = r.get("manifest_nodes", [])
        if not nodes:
            lines.append("_Sem nós KB indexados._")
            lines.append("")
            continue
        for node in nodes[:20]:
            nid = node.get("id", "")
            links = node.get("wikilinks", [])
            link_str = ", ".join(f"[[{l}]]" for l in links[:5]) if links else "—"
            lines.append(f"- [[{nid}]] → {link_str}")
        lines.append("")

    lines.extend(["## Dependências externas detectadas", ""])
    externals: set[str] = set()
    for r in repos_data:
        externals.update(r.get("external_refs", []))
        externals.update(r.get("integration_hints", []))

    dw_views = [e for e in externals if "dw" in e.lower() or "sap" in e.lower()]
    if dw_views:
        for ext in sorted(dw_views):
            lines.append(f"- [[DW_{ext}]] — referência externa (view/API)")
    else:
        lines.append("_Nenhuma dependência externa detectada automaticamente._")

    lines.extend(["", "## Cross-repo", ""])
    repo_names = [r["name"] for r in repos_data if r["status"] == "active"]
    if len(repo_names) > 1:
        lines.append("Repos ativos no projeto:")
        for a in repo_names:
            others = [b for b in repo_names if b != a]
            lines.append(f"- **{a}** pode integrar com: {', '.join(others)}")
    else:
        lines.append("_Projeto mono-repo ou apenas um repo ativo._")

    return "\n".join(lines) + "\n"
