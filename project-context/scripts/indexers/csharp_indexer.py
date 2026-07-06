"""Lightweight C# indexer using regex (Roslyn CLI optional for deep analysis)."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from indexers.indexing_profile import (
    DEFAULT_PROFILE,
    IndexingConfig,
    is_domain_entity_file,
    is_entity_symbol,
    is_orchestration_symbol,
    resolve_indexing_config,
    should_skip_file,
)

__all__ = [
    "KBNode",
    "index_csharp_files",
    "merge_roslyn_output",
    "resolve_indexing_config",
    "run_roslyn_cli",
]


@dataclass
class KBNode:
    id: str
    path: str
    title: str
    tags: list[str]
    tipo: str
    namespace: str
    source_file: str
    source_hash: str
    keywords: list[str] = field(default_factory=list)
    wikilinks: list[str] = field(default_factory=list)
    contrato: str = ""
    dependencias: str = ""
    fluxo_marcos: str = ""
    efeitos_colaterais: str = ""
    saidas_http: str = ""
    content: str = ""


HANDLER_RE = re.compile(
    r"class\s+(\w+(?:CommandHandler|QueryHandler|Handler))\s*(?::\s*[\w<>,\s]+)?\s*\{",
    re.MULTILINE,
)
JOB_RE = re.compile(r"class\s+(\w+(?:Job|Worker|BackgroundService))\s*(?::\s*[\w<>,\s]+)?\s*\{")
CONTROLLER_RE = re.compile(r"class\s+(\w+Controller)\s*(?::\s*[\w<>,\s]+)?\s*\{")
REPO_RE = re.compile(r"(?:interface|class)\s+(I?\w+Repository)\s*(?::\s*[\w<>,\s]+)?\s*\{")
CLIENT_RE = re.compile(r"(?:interface|class)\s+(I?\w+Client)\s*(?::\s*[\w<>,\s]+)?\s*\{")
SERVICE_RE = re.compile(r"class\s+(\w+Service)\s*(?::\s*[\w<>,\s]+)?\s*\{")
VALIDATOR_RE = re.compile(r"class\s+(\w+Validator)\s*(?::\s*[\w<>,\s]+)?\s*\{")
MAPPER_RE = re.compile(r"class\s+(\w+Mapper)\s*(?::\s*[\w<>,\s]+)?\s*\{")
CLASS_RE = re.compile(
    r"(?:public\s+|internal\s+|protected\s+)?(?:partial\s+|sealed\s+|abstract\s+|static\s+)*"
    r"class\s+(\w+)\s*(?::\s*[\w<>,\s]+)?\s*\{",
    re.MULTILINE,
)
NAMESPACE_RE = re.compile(r"namespace\s+([\w.]+)")
DEP_RE = re.compile(r"(?:private|protected|public)\s+readonly\s+(\w+)\s+(_\w+)\s*;")
METHOD_CALL_RE = re.compile(r"await\s+(\w+)\.(\w+)\s*\(")
HTTP_ATTR_RE = re.compile(r'\[Http(?:Get|Post|Put|Delete|Patch)\("([^"]+)"\)\]')
PUBLIC_PROP_RE = re.compile(
    r"public\s+(?:virtual\s+|override\s+|required\s+)?[\w<>,\?\[\]\s]+\s+(\w+)\s*\{"
)

SKIP_PATH_PARTS = {".git", "bin", "obj", "node_modules"}

PATTERN_RULES: list[tuple[str, re.Pattern[str], str, str]] = [
    ("handlers", HANDLER_RE, "handler", "cqrs"),
    ("jobs", JOB_RE, "job", "batch"),
    ("controllers", CONTROLLER_RE, "controller", "api"),
    ("repositories", REPO_RE, "repository", "persistence"),
    ("clients", CLIENT_RE, "client", "integration"),
    ("services", SERVICE_RE, "service", "domain"),
    ("validators", VALIDATOR_RE, "validator", "validation"),
    ("mappers", MAPPER_RE, "mapper", "infra"),
]


def _file_hash(content: str) -> str:
    return hashlib.sha256(content.encode()).hexdigest()[:16]


def _make_id(repo_name: str, symbol: str) -> str:
    safe_repo = re.sub(r"[^a-zA-Z0-9]+", "_", repo_name)
    return f"{safe_repo}_{symbol}"


def _extract_namespace(content: str) -> str:
    m = NAMESPACE_RE.search(content)
    return m.group(1) if m else ""


def _extract_keywords(symbol: str, namespace: str, content: str, rel_path: str) -> list[str]:
    keywords: list[str] = [symbol]
    if namespace:
        keywords.extend(namespace.split("."))
    for part in Path(rel_path).parts[:-1]:
        if part.lower() not in SKIP_PATH_PARTS:
            keywords.append(part)
    keywords.extend(PUBLIC_PROP_RE.findall(content)[:12])
    keywords.extend(re.findall(r'"([^"]{4,40})"', content)[:8])
    return list(dict.fromkeys(keywords))[:20]


def _extract_dependencies(content: str, repo_name: str) -> tuple[str, list[str]]:
    lines: list[str] = []
    wikilinks: list[str] = []
    for type_name, field_name in DEP_RE.findall(content):
        dep_id = _make_id(repo_name, type_name)
        wikilinks.append(dep_id)
        category = _categorize_dep(type_name)
        lines.append(f"- [{category}] [[{dep_id}]] ({field_name})")
    return "\n".join(lines) if lines else "_Nenhuma dependência explícita detectada._", wikilinks


def _categorize_dep(type_name: str) -> str:
    lower = type_name.lower()
    if "repository" in lower:
        return "Banco de Dados"
    if "client" in lower:
        return "Integração API"
    if "service" in lower:
        return "Domínio"
    if "mapper" in lower:
        return "Infra"
    if "unitofwork" in lower or "context" in lower:
        return "Infra"
    return "Dependência"


def _extract_flow(content: str) -> str:
    lines: list[str] = []
    for match in METHOD_CALL_RE.finditer(content):
        var, method = match.groups()
        lines.append(f"- Código executa: `{var}.{method}()`")
    if "SaveChanges" in content:
        lines.append("- Persistência confirmada via `SaveChanges` _(inferido)_")
    return "\n".join(lines[:25]) if lines else "_Fluxo não detectado automaticamente._"


def _extract_http(content: str, repo_name: str) -> tuple[str, list[str]]:
    lines: list[str] = []
    wikilinks: list[str] = []
    routes = HTTP_ATTR_RE.findall(content)
    for client in CLIENT_RE.findall(content):
        cid = _make_id(repo_name, client if isinstance(client, str) else client[0])
        wikilinks.append(cid)
    if routes:
        lines.append(f"- Rotas HTTP detectadas: `{', '.join(routes)}`")
    return "\n".join(lines) if lines else "_Nenhuma saída HTTP detectada._", wikilinks


def _build_node(
    repo_name: str,
    symbol: str,
    tipo: str,
    tags: list[str],
    source_file: Path,
    content: str,
    source_commit: str,
    reference_branch: str,
    kb_domain: str,
) -> KBNode:
    rel = source_file.as_posix()
    node_id = _make_id(repo_name, symbol)
    ns = _extract_namespace(content)
    deps_text, dep_links = _extract_dependencies(content, repo_name)
    http_text, http_links = _extract_http(content, repo_name)
    flow = _extract_flow(content)
    keywords = _extract_keywords(symbol, ns, content, rel)
    wikilinks = list(dict.fromkeys(dep_links + http_links))

    md = _render_markdown(
        node_id=node_id,
        title=symbol,
        tags=tags + [kb_domain],
        kb_domain=kb_domain,
        tipo=tipo,
        namespace=ns,
        source_commit=source_commit,
        reference_branch=reference_branch,
        source_file=rel,
        source_hash=_file_hash(content),
        wikilinks=wikilinks,
        contrato=f"- **Tipo:** `{tipo}`\n- **Arquivo:** `{rel}`",
        dependencias=deps_text,
        fluxo_marcos=flow,
        efeitos_colaterais="- Persistência via SaveChanges _(inferido)_" if "SaveChanges" in content else "_Não detectado._",
        saidas_http=http_text,
    )

    return KBNode(
        id=node_id,
        path=f"kb/nodes/{node_id}.md",
        title=symbol,
        tags=tags + [kb_domain],
        tipo=tipo,
        namespace=ns,
        source_file=rel,
        source_hash=_file_hash(content),
        keywords=keywords,
        wikilinks=wikilinks,
        contrato=f"- **Tipo:** `{tipo}`\n- **Arquivo:** `{rel}`",
        dependencias=deps_text,
        fluxo_marcos=flow,
        efeitos_colaterais="- Persistência via SaveChanges _(inferido)_" if "SaveChanges" in content else "_Não detectado._",
        saidas_http=http_text,
        content=md,
    )


def _render_markdown(**kwargs: Any) -> str:
    wikilinks_yaml = ", ".join(kwargs["wikilinks"]) if kwargs["wikilinks"] else ""
    tags_yaml = ", ".join(kwargs["tags"])
    now = datetime.now(timezone.utc).isoformat()
    return f"""---
tags: [{tags_yaml}]
kb_domain: {kwargs['kb_domain']}
tipo: {kwargs['tipo']}
namespace: {kwargs['namespace']}
ultima_sincronizacao: {now}
reference_branch: {kwargs['reference_branch']}
source_commit: {kwargs['source_commit']}
source_file: {kwargs['source_file']}
source_hash: {kwargs['source_hash']}
wikilinks_out: [{wikilinks_yaml}]
---

# {kwargs['title']}

## Contrato

{kwargs['contrato']}

## Dependências (grafo)

{kwargs['dependencias']}

## Fluxo (marcos)

{kwargs['fluxo_marcos']}

## Efeitos colaterais

{kwargs['efeitos_colaterais']}

## Saídas HTTP (clients)

{kwargs['saidas_http']}
"""


def _collect_symbols(
    content: str,
    rel_path: str,
    config: IndexingConfig,
) -> list[tuple[str, str, str]]:
    """Return list of (symbol, tipo, tag) for one source file."""
    found: dict[str, tuple[str, str]] = {}

    for category, pattern, tipo, tag in PATTERN_RULES:
        if not config.includes(category):
            continue
        for match in pattern.finditer(content):
            symbol = match.group(1)
            if category == "services" and symbol.endswith("BackgroundService"):
                continue
            found.setdefault(symbol, (tipo, tag))

    if config.includes("domain_entities") and is_domain_entity_file(rel_path):
        for match in CLASS_RE.finditer(content):
            symbol = match.group(1)
            if not is_entity_symbol(symbol) or is_orchestration_symbol(symbol):
                continue
            found.setdefault(symbol, ("entity", "domain"))

    if config.includes("all_classes"):
        for match in CLASS_RE.finditer(content):
            symbol = match.group(1)
            if symbol in found:
                continue
            if symbol.endswith("BackgroundService"):
                found.setdefault(symbol, ("job", "batch"))
            elif is_orchestration_symbol(symbol):
                for category, pattern, tipo, tag in PATTERN_RULES:
                    if pattern.search(f"class {symbol}"):
                        found.setdefault(symbol, (tipo, tag))
                        break
            else:
                found.setdefault(symbol, ("class", "code"))

    return [(symbol, tipo, tag) for symbol, (tipo, tag) in found.items()]


def index_csharp_files(
    repo_path: Path,
    repo_name: str,
    source_commit: str,
    reference_branch: str,
    files: list[str] | None = None,
    kb_domain: str | None = None,
    indexing: IndexingConfig | None = None,
) -> list[KBNode]:
    kb_domain = kb_domain or repo_name.replace("-", "_")
    config = indexing or IndexingConfig(profile=DEFAULT_PROFILE)
    nodes: list[KBNode] = []
    cs_files = [repo_path / f for f in files] if files else list(repo_path.rglob("*.cs"))

    for cs in cs_files:
        if any(part in SKIP_PATH_PARTS for part in cs.parts):
            continue
        try:
            rel = cs.relative_to(repo_path).as_posix()
        except ValueError:
            continue
        if should_skip_file(rel, config):
            continue
        try:
            content = cs.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue

        for symbol, tipo, tag in _collect_symbols(content, rel, config):
            nodes.append(
                _build_node(
                    repo_name=repo_name,
                    symbol=symbol,
                    tipo=tipo,
                    tags=[tag, tipo, kb_domain],
                    source_file=cs.relative_to(repo_path),
                    content=content,
                    source_commit=source_commit,
                    reference_branch=reference_branch,
                    kb_domain=kb_domain,
                )
            )
    return nodes


def run_roslyn_cli(repo_path: Path, output_json: Path) -> bool:
    """Invoke optional Roslyn CLI if built. Returns True if output produced."""
    cli_dir = Path(__file__).parent / "roslyn" / "RoslynIndexer"
    project = cli_dir / "RoslynIndexer.csproj"
    if not project.exists():
        return False
    try:
        subprocess.run(
            ["dotnet", "run", "--project", str(project), "--", str(repo_path), str(output_json)],
            check=True,
            capture_output=True,
            text=True,
        )
        return output_json.is_file()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def merge_roslyn_output(nodes: list[KBNode], roslyn_json: Path, repo_name: str) -> list[KBNode]:
    if not roslyn_json.is_file():
        return nodes
    data = json.loads(roslyn_json.read_text(encoding="utf-8"))
    by_file: dict[str, dict] = {item["source_file"]: item for item in data.get("symbols", [])}
    for node in nodes:
        extra = by_file.get(node.source_file, {})
        if extra.get("methods"):
            node.fluxo_marcos = "\n".join(f"- Código executa: `{m}`" for m in extra["methods"][:30])
    return nodes
