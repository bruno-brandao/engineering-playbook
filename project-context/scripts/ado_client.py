"""Azure DevOps repository listing (read-only)."""

from __future__ import annotations

import json
import os
import subprocess
import urllib.error
import urllib.request
from dataclasses import dataclass


@dataclass
class AdoRepo:
    name: str
    url: str
    default_branch: str = "main"
    remote_url: str = ""


def list_repos_ado(organization: str, project: str, pat: str | None = None) -> list[AdoRepo]:
    pat = pat or os.environ.get("AZURE_DEVOPS_EXT_PAT") or os.environ.get("ADO_PAT")
    url = (
        f"https://dev.azure.com/{organization}/{project}/"
        f"_apis/git/repositories?api-version=7.1"
    )
    headers = {"Accept": "application/json"}
    if pat:
        import base64

        token = base64.b64encode(f":{pat}".encode()).decode()
        headers["Authorization"] = f"Basic {token}"

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"ADO API error {e.code}: {e.reason}") from e

    repos: list[AdoRepo] = []
    for item in data.get("value", []):
        default = item.get("defaultBranch", "refs/heads/main")
        branch = default.replace("refs/heads/", "") if default else "main"
        repos.append(
            AdoRepo(
                name=item["name"],
                url=item.get("webUrl", ""),
                default_branch=branch,
                remote_url=item.get("remoteUrl", ""),
            )
        )
    return repos


def list_repos_az_cli(organization: str, project: str) -> list[AdoRepo]:
    cmd = [
        "az",
        "repos",
        "list",
        "--organization",
        f"https://dev.azure.com/{organization}",
        "--project",
        project,
        "-o",
        "json",
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        raise RuntimeError(f"az repos list failed: {e}") from e

    repos: list[AdoRepo] = []
    for item in data:
        default = item.get("defaultBranch", "refs/heads/main")
        branch = default.replace("refs/heads/", "") if default else "main"
        repos.append(
            AdoRepo(
                name=item["name"],
                url=item.get("webUrl", ""),
                default_branch=branch,
                remote_url=item.get("remoteUrl", ""),
            )
        )
    return repos


def list_repos(organization: str, project: str) -> list[AdoRepo]:
    try:
        return list_repos_az_cli(organization, project)
    except RuntimeError:
        return list_repos_ado(organization, project)
