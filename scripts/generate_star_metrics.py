"""Generate the most-starred public repository table for the profile Statistics page."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Final

OWNER: Final[str] = "DiogoRibeiro7"
TOP_N: Final[int] = 10
STATISTICS_PATH: Final[Path] = Path("STATISTICS.md")
API_ROOT: Final[str] = "https://api.github.com"
STARS_START: Final[str] = "<!-- statistics:stars:start -->"
STARS_END: Final[str] = "<!-- statistics:stars:end -->"

ROW_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"^\| \[(?P<name>[^\]]+)\]\(https://github\.com/" + OWNER + r"/(?P<repo>[^)]+)\) \| \*\*(?P<stars>\d+)\*\* \|$"
)
FOOTNOTE_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"^_Top (?P<top>\d+) of (?P<total>\d+) public non-fork repositories · "
    r"counts fetched (?P<date>\d{4}-\d{2}-\d{2}) · ties broken alphabetically\._$"
)


@dataclass(frozen=True)
class Repository:
    """One public repository and its current star count."""

    name: str
    stars: int


def _headers() -> dict[str, str]:
    """Return GitHub API request headers, using the Actions token when present."""
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "diogoribeiro7-profile-stars",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def _get_json(url: str) -> object:
    """Fetch and decode a GitHub API JSON response."""
    request = urllib.request.Request(url, headers=_headers())
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"GitHub API request failed: {url} ({exc.code})") from exc


def fetch_repositories() -> list[Repository]:
    """Return every public, non-fork repository owned by the account."""
    repositories: list[Repository] = []
    page = 1
    while True:
        payload = _get_json(f"{API_ROOT}/users/{OWNER}/repos?per_page=100&type=owner&page={page}")
        if not isinstance(payload, list):
            raise TypeError("GitHub repository listing must be a JSON array.")
        if not payload:
            break
        for item in payload:
            if not isinstance(item, dict):
                raise TypeError("Every repository entry must be a JSON object.")
            if item.get("fork") or item.get("private"):
                continue
            name = item.get("name")
            stars = item.get("stargazers_count")
            if not isinstance(name, str) or not isinstance(stars, int):
                raise TypeError(f"Repository entry is missing a usable name or star count: {item!r}")
            repositories.append(Repository(name, stars))
        page += 1
    if not repositories:
        raise ValueError("GitHub returned no public repositories for the account.")
    return repositories


def top_repositories(repositories: list[Repository]) -> list[Repository]:
    """Return the most-starred repositories, breaking ties alphabetically."""
    ordered = sorted(repositories, key=lambda repo: (-repo.stars, repo.name.lower()))
    return ordered[:TOP_N]


def render_table(top: list[Repository], total: int, fetched_on: dt.date) -> str:
    """Render the generated most-starred repository block."""
    if len(top) != TOP_N:
        raise ValueError(f"Expected {TOP_N} repositories to render, got {len(top)}.")
    rows = [STARS_START, "| Repository | Stars |", "| :-- | --: |"]
    rows.extend(
        f"| [{repo.name}](https://github.com/{OWNER}/{repo.name}) | **{repo.stars}** |" for repo in top
    )
    rows.append("")
    rows.append(
        f"_Top {TOP_N} of {total} public non-fork repositories · "
        f"counts fetched {fetched_on.isoformat()} · ties broken alphabetically._"
    )
    rows.append(STARS_END)
    return "\n".join(rows)


def _replace_stars(text: str, replacement: str) -> str:
    """Replace exactly one generated most-starred block."""
    pattern = re.compile(re.escape(STARS_START) + r".*?" + re.escape(STARS_END), re.DOTALL)
    matches = pattern.findall(text)
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one most-starred block; found {len(matches)}.")
    return pattern.sub(lambda _: replacement, text, count=1)


def _extract_block(text: str) -> list[str]:
    """Return the committed most-starred block as individual lines."""
    pattern = re.compile(re.escape(STARS_START) + r".*?" + re.escape(STARS_END), re.DOTALL)
    matches = pattern.findall(text)
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one most-starred block; found {len(matches)}.")
    return matches[0].splitlines()


def generate() -> None:
    """Fetch live star counts and rewrite the committed table."""
    repositories = fetch_repositories()
    table = render_table(top_repositories(repositories), len(repositories), dt.date.today())
    STATISTICS_PATH.write_text(_replace_stars(STATISTICS_PATH.read_text(encoding="utf-8"), table), encoding="utf-8")


def check() -> int:
    """Validate the committed table offline.

    Star counts drift continuously, so this verifies the block's structure and
    ordering rules rather than comparing against live values, which would make
    pull-request CI fail whenever somebody stars a repository.
    """
    errors: list[str] = []
    lines = _extract_block(STATISTICS_PATH.read_text(encoding="utf-8"))

    if lines[1:3] != ["| Repository | Stars |", "| :-- | --: |"]:
        errors.append("most-starred block does not start with the expected table header")

    entries: list[Repository] = []
    for line in lines[3:]:
        match = ROW_PATTERN.match(line)
        if match is None:
            continue
        if match.group("name") != match.group("repo"):
            errors.append(f"row label and repository link disagree: {line}")
        entries.append(Repository(match.group("name"), int(match.group("stars"))))

    if len(entries) != TOP_N:
        errors.append(f"expected {TOP_N} repository rows, found {len(entries)}")

    expected_order = sorted(entries, key=lambda repo: (-repo.stars, repo.name.lower()))
    if entries != expected_order:
        errors.append("rows are not ordered by descending stars, then repository name")

    footnote = FOOTNOTE_PATTERN.match(lines[-2]) if len(lines) >= 2 else None
    if footnote is None:
        errors.append("most-starred block is missing its denominator and fetch-date footnote")
    else:
        if int(footnote.group("top")) != TOP_N:
            errors.append(f"footnote claims a top {footnote.group('top')} but {TOP_N} rows are published")
        if int(footnote.group("total")) < TOP_N:
            errors.append("footnote denominator is smaller than the number of published rows")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"Most-starred repository table is well-formed ({TOP_N} rows, correctly ordered).")
    return 0


def main() -> int:
    """Refresh the most-starred table, or verify its committed state."""
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("generate", "check"), nargs="?", default="generate")
    args = parser.parse_args()
    if args.command == "generate":
        generate()
        return 0
    return check()


if __name__ == "__main__":
    raise SystemExit(main())
