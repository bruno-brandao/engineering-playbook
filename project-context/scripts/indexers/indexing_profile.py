"""Indexing tiers for KB generation — minimal, standard, full."""

from __future__ import annotations

from dataclasses import dataclass, field
from fnmatch import fnmatch
from typing import Any

PROFILE_MINIMAL = frozenset(
    {"controllers", "repositories", "handlers", "jobs", "clients"}
)
PROFILE_STANDARD = PROFILE_MINIMAL | frozenset(
    {"services", "validators", "mappers", "domain_entities"}
)
PROFILE_FULL = PROFILE_STANDARD | frozenset({"all_classes"})

PROFILES: dict[str, frozenset[str]] = {
    "minimal": PROFILE_MINIMAL,
    "standard": PROFILE_STANDARD,
    "full": PROFILE_FULL,
}

DEFAULT_PROFILE = "standard"

DEFAULT_EXCLUDE_GLOBS = [
    "**/Migrations/**",
    "**/*.Designer.cs",
    "**/*Dto.cs",
    "**/*DTO.cs",
    "**/*Request.cs",
    "**/*Response.cs",
    "**/*Options.cs",
    "**/*Config.cs",
    "**/*Configuration.cs",
    "**/*Settings.cs",
]

DOMAIN_FOLDER_MARKERS = frozenset(
    {"domain", "domains", "entities", "entity", "models", "model", "aggregates", "valueobjects"}
)

ENTITY_EXCLUDE_SUFFIXES = (
    "Dto",
    "DTO",
    "Request",
    "Response",
    "Options",
    "Config",
    "Configuration",
    "Settings",
    "Profile",
    "Controller",
    "Repository",
    "Handler",
    "Client",
    "Job",
    "Worker",
    "Service",
    "Validator",
    "Mapper",
    "BackgroundService",
)

ORCHESTRATION_SUFFIXES = (
    "Controller",
    "Repository",
    "Handler",
    "CommandHandler",
    "QueryHandler",
    "Client",
    "Job",
    "Worker",
    "BackgroundService",
)


@dataclass
class IndexingConfig:
    profile: str = DEFAULT_PROFILE
    include: frozenset[str] = field(default_factory=lambda: PROFILE_STANDARD)
    exclude_globs: list[str] = field(default_factory=lambda: list(DEFAULT_EXCLUDE_GLOBS))

    def includes(self, category: str) -> bool:
        return category in self.include or "all_classes" in self.include


def resolve_indexing_config(
    repo_cfg: dict[str, Any],
    project_map: dict[str, Any] | None = None,
) -> IndexingConfig:
    """Merge project default_indexing with per-repo indexing block."""
    project_defaults = (project_map or {}).get("default_indexing") or {}
    repo_indexing = repo_cfg.get("indexing") or {}

    profile = repo_indexing.get("profile") or project_defaults.get("profile") or DEFAULT_PROFILE
    if profile not in PROFILES:
        profile = DEFAULT_PROFILE

    exclude = list(DEFAULT_EXCLUDE_GLOBS)
    for extra in project_defaults.get("exclude_globs") or []:
        if extra not in exclude:
            exclude.append(extra)
    for extra in repo_indexing.get("exclude_globs") or []:
        if extra not in exclude:
            exclude.append(extra)

    include_override = repo_indexing.get("include") or project_defaults.get("include")
    include = frozenset(include_override) if include_override else PROFILES[profile]

    return IndexingConfig(profile=profile, include=include, exclude_globs=exclude)


def path_matches_glob(rel_path: str, pattern: str) -> bool:
    normalized = rel_path.replace("\\", "/")
    if pattern.startswith("**/"):
        return fnmatch(normalized, pattern) or fnmatch(normalized.split("/")[-1], pattern[3:])
    return fnmatch(normalized, pattern)


def should_skip_file(rel_path: str, config: IndexingConfig) -> bool:
    for pattern in config.exclude_globs:
        if path_matches_glob(rel_path, pattern):
            return True
    if "Migrations" in rel_path or ".Designer.cs" in rel_path:
        return True
    return False


def is_domain_entity_file(rel_path: str) -> bool:
    parts = {p.lower() for p in rel_path.replace("\\", "/").split("/")[:-1]}
    return bool(parts & DOMAIN_FOLDER_MARKERS)


def is_entity_symbol(symbol: str) -> bool:
    if symbol.startswith("I") and len(symbol) > 1 and symbol[1].isupper():
        return False
    return not any(symbol.endswith(suffix) for suffix in ENTITY_EXCLUDE_SUFFIXES)


def is_orchestration_symbol(symbol: str) -> bool:
    return any(symbol.endswith(suffix) for suffix in ORCHESTRATION_SUFFIXES)
