"""Stack detection from repository artifacts."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


@dataclass
class StackDetectionResult:
    stacks: list[str] = field(default_factory=list)
    patterns: dict[str, str] = field(default_factory=dict)
    folder_structure: dict[str, str] = field(default_factory=dict)
    integration_hints: list[str] = field(default_factory=list)
    signals: list[str] = field(default_factory=list)


STACK_SIGNALS: list[tuple[str, str, callable[[Path], bool]]] = [
    ("dotnet", "*.csproj", lambda r: _glob_exists(r, "*.csproj") or _glob_exists(r, "*.sln")),
    ("node", "package.json", lambda r: (r / "package.json").is_file()),
    ("azure-functions", "host.json", lambda r: (r / "host.json").is_file()),
    ("python", "pyproject.toml", lambda r: (r / "pyproject.toml").is_file() or (r / "requirements.txt").is_file()),
    ("go", "go.mod", lambda r: (r / "go.mod").is_file()),
    ("docker", "Dockerfile", lambda r: (r / "Dockerfile").is_file() or (r / "docker-compose.yml").is_file()),
    ("sql", "migrations", lambda r: (r / "migrations").is_dir() or bool(list(r.rglob("*.sql")))),
]

PATTERN_FOLDERS: dict[str, str] = {
    "Domain": "clean-architecture / DDD",
    "Application": "clean-architecture / CQRS",
    "Infrastructure": "clean-architecture",
    "Handlers": "CQRS handlers",
    "Commands": "CQRS commands",
    "Queries": "CQRS queries",
    "Controllers": "REST API",
    "src/features": "feature folders",
    "src/components": "frontend components",
    "Pages": "Blazor / Razor pages",
    "Jobs": "batch / scheduled jobs",
    "Services": "service layer",
}

INTEGRATION_PATTERNS: list[tuple[str, str]] = [
    ("HttpClient", "http-client"),
    ("IHttpClientFactory", "http-client-factory"),
    ("ConnectionStrings", "database"),
    ("ServiceBus", "azure-service-bus"),
    ("[DW].", "data-warehouse-view"),
    ("VWImobilizados", "dw-view-sap"),
    ("SAP", "sap-integration"),
]


def _glob_exists(root: Path, pattern: str) -> bool:
    return any(root.rglob(pattern))


def _walk_limited(root: Path, max_depth: int = 4) -> Iterable[Path]:
    root = root.resolve()
    for dirpath, dirnames, _ in os.walk(root):
        depth = len(Path(dirpath).relative_to(root).parts)
        if depth >= max_depth:
            dirnames.clear()
            continue
        yield Path(dirpath)


def detect_stack(repo_path: Path) -> StackDetectionResult:
    result = StackDetectionResult()
    if not repo_path.is_dir():
        return result

    for stack, signal, check in STACK_SIGNALS:
        if check(repo_path):
            result.stacks.append(stack)
            result.signals.append(signal)

    for folder, meaning in PATTERN_FOLDERS.items():
        if (repo_path / folder).is_dir():
            result.folder_structure[folder] = meaning

    for sub in _walk_limited(repo_path):
        rel = sub.relative_to(repo_path)
        parts = rel.parts
        if len(parts) >= 2:
            key = "/".join(parts[:2])
            if key not in result.folder_structure and parts[0] in ("src", "app", "lib"):
                result.folder_structure[key] = "source tree"

    patterns_found: list[str] = []
    if "Handlers" in result.folder_structure or "Commands" in result.folder_structure:
        patterns_found.append("CQRS")
    if "Domain" in result.folder_structure:
        patterns_found.append("Clean Architecture")
    if "Controllers" in result.folder_structure:
        patterns_found.append("REST API")
    if "Jobs" in result.folder_structure:
        patterns_found.append("Batch Jobs")
    if "node" in result.stacks and "src/components" in result.folder_structure:
        patterns_found.append("SPA Frontend")

    dominant = ", ".join(patterns_found) if patterns_found else "Não identificado"
    recommended = _recommended_pattern(result.stacks, patterns_found)
    result.patterns = {"dominant": dominant, "recommended": recommended}

    result.integration_hints = _scan_integrations(repo_path)
    return result


def _recommended_pattern(stacks: list[str], patterns: list[str]) -> str:
    if "CQRS" in patterns:
        return "Manter CQRS — Commands/Queries/Handlers"
    if "dotnet" in stacks:
        return "Clean Architecture (Domain / Application / Infrastructure)"
    if "node" in stacks:
        return "Feature folders ou camadas (routes / services / models)"
    if "python" in stacks:
        return "Modular packages com separação domain / infra"
    return "Clean Architecture conforme stack detectada"


def _scan_integrations(repo_path: Path, max_files: int = 200) -> list[str]:
    hints: set[str] = set()
    count = 0
    skip_dirs = {".git", "node_modules", "bin", "obj", ".engineering", "dist", "build"}

    for dirpath, dirnames, filenames in os.walk(repo_path):
        dirnames[:] = [d for d in dirnames if d not in skip_dirs]
        for name in filenames:
            if count >= max_files:
                break
            ext = Path(name).suffix.lower()
            if ext not in (".cs", ".ts", ".js", ".json", ".yaml", ".yml", ".sql", ".config"):
                continue
            count += 1
            try:
                text = (Path(dirpath) / name).read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            for needle, hint in INTEGRATION_PATTERNS:
                if needle in text:
                    hints.add(hint)
        if count >= max_files:
            break

    return sorted(hints)


def compute_quality_score(repo_path: Path, detection: StackDetectionResult) -> tuple[int, str]:
    score = 50
    if (repo_path / "README.md").is_file():
        score += 10
    if (repo_path / ".editorconfig").is_file():
        score += 10
    if any((repo_path / d).is_dir() for d in ("tests", "test", "__tests__", "Tests")):
        score += 15
    if detection.folder_structure:
        score += min(15, len(detection.folder_structure) * 3)
    if detection.patterns.get("dominant") != "Não identificado":
        score += 10
    score = min(100, score)

    if score < 40:
        debt = "high"
    elif score < 70:
        debt = "medium"
    else:
        debt = "low"
    return score, debt
