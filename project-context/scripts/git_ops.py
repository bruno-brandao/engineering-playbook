"""Git operations for branch sync and verification."""

from __future__ import annotations

import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal


VerifyStatus = Literal[
    "aligned",
    "ref_stale",
    "branch_delta",
    "doc_ahead",
    "divergent",
    "branch_not_found",
    "not_indexed",
]


@dataclass
class GitCommit:
    sha: str
    date: str | None = None


@dataclass
class DiffEntry:
    status: str
    path: str


@dataclass
class VerifyResult:
    status: VerifyStatus
    reference_branch: str
    working_branch: str
    indexed_commit_sha: str | None
    remote_head_sha: str | None
    merge_base_sha: str | None = None
    kb_ahead_files: list[str] = field(default_factory=list)
    branch_unique_files: list[str] = field(default_factory=list)
    commits_behind: int = 0
    message: str = ""


class GitError(Exception):
    pass


def _run_git(repo: Path, *args: str, check: bool = True) -> str:
    cmd = ["git", "-C", str(repo), *args]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=check)
    except subprocess.CalledProcessError as e:
        raise GitError(e.stderr.strip() or str(e)) from e
    return result.stdout.strip()


def fetch(repo: Path, branch: str) -> None:
    _run_git(repo, "fetch", "origin", branch, check=False)


def branch_exists(repo: Path, branch: str) -> bool:
    try:
        _run_git(repo, "rev-parse", "--verify", branch)
        return True
    except GitError:
        try:
            _run_git(repo, "rev-parse", "--verify", f"origin/{branch}")
            return True
        except GitError:
            return False


def resolve_ref(repo: Path, branch: str) -> str:
    for ref in (branch, f"origin/{branch}"):
        try:
            return _run_git(repo, "rev-parse", ref)
        except GitError:
            continue
    raise GitError(f"Branch não encontrada: {branch}")


def get_commit_date(repo: Path, sha: str) -> str | None:
    try:
        return _run_git(repo, "show", "-s", "--format=%cI", sha)
    except GitError:
        return None


def merge_base(repo: Path, ref_a: str, ref_b: str) -> str:
    return _run_git(repo, "merge-base", ref_a, ref_b)


def is_ancestor(repo: Path, ancestor: str, descendant: str) -> bool:
    try:
        _run_git(repo, "merge-base", "--is-ancestor", ancestor, descendant)
        return True
    except GitError:
        return False


def count_commits(repo: Path, from_sha: str, to_sha: str) -> int:
    if from_sha == to_sha:
        return 0
    try:
        out = _run_git(repo, "rev-list", "--count", f"{from_sha}..{to_sha}")
        return int(out)
    except GitError:
        return 0


def diff_name_status(repo: Path, from_sha: str, to_sha: str) -> list[DiffEntry]:
    if from_sha == to_sha:
        return []
    try:
        out = _run_git(repo, "diff", "--name-status", f"{from_sha}..{to_sha}")
    except GitError:
        return []
    entries: list[DiffEntry] = []
    for line in out.splitlines():
        parts = line.split("\t", 1)
        if len(parts) == 2:
            entries.append(DiffEntry(status=parts[0], path=parts[1]))
    return entries


def diff_changed_files(repo: Path, from_sha: str, to_sha: str) -> list[str]:
    return [e.path for e in diff_name_status(repo, from_sha, to_sha)]


def log_oneline(repo: Path, from_sha: str, to_sha: str, limit: int = 20) -> list[str]:
    if from_sha == to_sha:
        return []
    try:
        out = _run_git(
            repo,
            "log",
            f"{from_sha}..{to_sha}",
            f"--oneline",
            f"-{limit}",
        )
        return out.splitlines() if out else []
    except GitError:
        return []


def verify_branch_alignment(
    repo: Path,
    working_branch: str,
    reference_branch: str,
    indexed_commit_sha: str | None,
) -> VerifyResult:
    if not branch_exists(repo, working_branch):
        return VerifyResult(
            status="branch_not_found",
            reference_branch=reference_branch,
            working_branch=working_branch,
            indexed_commit_sha=indexed_commit_sha,
            remote_head_sha=None,
            message=f"Branch '{working_branch}' não encontrada.",
        )

    if not indexed_commit_sha:
        return VerifyResult(
            status="not_indexed",
            reference_branch=reference_branch,
            working_branch=working_branch,
            indexed_commit_sha=None,
            remote_head_sha=resolve_ref(repo, working_branch),
            message="Repositório ainda não indexado. Execute scan init ou scan sync.",
        )

    fetch(repo, working_branch)
    fetch(repo, reference_branch)

    working_sha = resolve_ref(repo, working_branch)
    ref_head_sha = resolve_ref(repo, reference_branch)

    if working_branch == reference_branch or working_sha == ref_head_sha:
        if indexed_commit_sha == working_sha:
            return VerifyResult(
                status="aligned",
                reference_branch=reference_branch,
                working_branch=working_branch,
                indexed_commit_sha=indexed_commit_sha,
                remote_head_sha=working_sha,
                message="Documentação alinhada com HEAD da branch.",
            )
        commits_behind = count_commits(repo, indexed_commit_sha, working_sha)
        return VerifyResult(
            status="ref_stale",
            reference_branch=reference_branch,
            working_branch=working_branch,
            indexed_commit_sha=indexed_commit_sha,
            remote_head_sha=working_sha,
            commits_behind=commits_behind,
            message=f"KB atrás do HEAD em {commits_behind} commit(s). Execute scan sync.",
        )

    base = merge_base(repo, working_sha, ref_head_sha)
    kb_ahead = diff_changed_files(repo, working_sha, indexed_commit_sha)
    branch_unique = diff_changed_files(repo, base, working_sha)

    kb_ahead_set = set(kb_ahead)
    branch_unique_set = set(branch_unique)

    if not kb_ahead_set and not branch_unique_set:
        if indexed_commit_sha == working_sha or is_ancestor(repo, indexed_commit_sha, working_sha):
            return VerifyResult(
                status="aligned",
                reference_branch=reference_branch,
                working_branch=working_branch,
                indexed_commit_sha=indexed_commit_sha,
                remote_head_sha=working_sha,
                merge_base_sha=base,
                message="Feature branch alinhada com KB.",
            )

    if kb_ahead_set and branch_unique_set:
        return VerifyResult(
            status="divergent",
            reference_branch=reference_branch,
            working_branch=working_branch,
            indexed_commit_sha=indexed_commit_sha,
            remote_head_sha=working_sha,
            merge_base_sha=base,
            kb_ahead_files=sorted(kb_ahead_set),
            branch_unique_files=sorted(branch_unique_set),
            message="KB à frente da branch E branch tem alterações únicas não indexadas.",
        )

    if kb_ahead_set:
        return VerifyResult(
            status="doc_ahead",
            reference_branch=reference_branch,
            working_branch=working_branch,
            indexed_commit_sha=indexed_commit_sha,
            remote_head_sha=working_sha,
            merge_base_sha=base,
            kb_ahead_files=sorted(kb_ahead_set),
            message="KB indexada em commit mais novo; branch precisa merge/rebase da ref.",
        )

    return VerifyResult(
        status="branch_delta",
        reference_branch=reference_branch,
        working_branch=working_branch,
        indexed_commit_sha=indexed_commit_sha,
        remote_head_sha=working_sha,
        merge_base_sha=base,
        branch_unique_files=sorted(branch_unique_set),
        message="Feature branch tem alterações não indexadas na KB.",
    )
