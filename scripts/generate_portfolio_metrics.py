"""Generate evidence-based portfolio metrics for the profile statistics page.

The generator audits the repositories listed in FEATURED.md using the GitHub
Contents API. Mechanical metrics are discovered from repository structure.
Semantic metrics that cannot be inferred safely from filenames are maintained
in an explicit, reviewable manifest below.
"""

from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Final
from xml.sax.saxutils import escape

OWNER: Final[str] = "DiogoRibeiro7"
FEATURED_PATH: Final[Path] = Path("FEATURED.md")
OUTPUT_PATH: Final[Path] = Path("assets/portfolio-evidence.svg")
API_ROOT: Final[str] = "https://api.github.com"

# These classifications require scientific judgement and are therefore
# explicit rather than guessed from filenames.
REAL_DATA_OR_EMPIRICAL: Final[frozenset[str]] = frozenset(
    {
        "qwen-text2sql-lab",
        "clinic-forecasting-platform",
        "transaction-risk-lakehouse",
        "oisst-fourier-neural-operator",
        "portugal-public-pension-financing",
        "short-rate-anomaly-regimes",
    }
)

RESEARCH_SOFTWARE_OR_METHOD_PACKAGE: Final[frozenset[str]] = frozenset(
    {
        "genSurvPy",
        "setqca-python",
        "behavioral-sensing-research",
        "bmssp",
    }
)


@dataclass(frozen=True)
class RepoEvidence:
    """Mechanical quality signals found in one flagship repository."""

    name: str
    has_ci: bool
    has_tests: bool
    has_docs: bool
    has_citation: bool
    has_reproducibility_assets: bool


def _headers() -> dict[str, str]:
    """Return GitHub API request headers, using the Actions token when present."""
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "diogoribeiro7-profile-metrics",
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
        if exc.code == 404:
            return []
        raise RuntimeError(f"GitHub API request failed: {url} ({exc.code})") from exc


def _contents(repo: str, path: str = "") -> list[dict[str, object]]:
    """Return directory entries from one repository path."""
    suffix = f"/{path}" if path else ""
    payload = _get_json(f"{API_ROOT}/repos/{OWNER}/{repo}/contents{suffix}")
    if not isinstance(payload, list):
        return []
    return [item for item in payload if isinstance(item, dict)]


def _names(entries: list[dict[str, object]]) -> set[str]:
    """Return entry names with runtime type validation."""
    result: set[str] = set()
    for item in entries:
        name = item.get("name")
        if isinstance(name, str):
            result.add(name)
    return result


def _featured_repos() -> list[str]:
    """Parse public GitHub repository names from the flagship table."""
    text = FEATURED_PATH.read_text(encoding="utf-8")
    matches = re.findall(r"https://github\.com/DiogoRibeiro7/([^/)#]+)", text)
    excluded = {"diogoribeiro7"}
    repos = list(dict.fromkeys(repo for repo in matches if repo not in excluded))
    if len(repos) != 12:
        raise ValueError(f"Expected 12 flagship repositories, found {len(repos)}: {repos}")
    return repos


def _audit_repo(repo: str) -> RepoEvidence:
    """Audit mechanically verifiable repository-level evidence."""
    root = _names(_contents(repo))
    github = _names(_contents(repo, ".github")) if ".github" in root else set()
    workflows = _contents(repo, ".github/workflows") if "workflows" in github else []

    docs_markers = {"docs", "mkdocs.yml", "mkdocs.yaml", "docs.yml", "docs.yaml"}
    test_markers = {"tests", "test", "pytest.ini", "tox.ini"}
    citation_markers = {"CITATION.cff", ".zenodo.json"}
    reproducibility_markers = {
        "experiments",
        "artifacts",
        "results",
        "reports",
        "notebooks",
        "data",
        "data_sources",
        "config",
        "configs",
    }

    return RepoEvidence(
        name=repo,
        has_ci=bool(workflows),
        has_tests=bool(root & test_markers),
        has_docs=bool(root & docs_markers),
        has_citation=bool(root & citation_markers),
        has_reproducibility_assets=bool(root & reproducibility_markers),
    )


def _metric(label: str, count: int, total: int, note: str) -> tuple[str, str, str]:
    """Format one metric tuple for rendering."""
    pct = 100.0 * count / total
    return label, f"{count}/{total} · {pct:.0f}%", note


def _render_svg(metrics: list[tuple[str, str, str]], total: int) -> str:
    """Render a compact dark/light-compatible SVG metrics dashboard."""
    width = 900
    card_w = 420
    card_h = 104
    gap = 20
    rows = (len(metrics) + 1) // 2
    height = 90 + rows * (card_h + gap) + 42

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">Flagship portfolio evidence metrics</title>',
        f'<desc id="desc">Evidence metrics computed across {total} flagship repositories.</desc>',
        '<style>',
        'text{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:#c9d1d9}',
        '.title{font-size:24px;font-weight:700}.sub{font-size:13px;fill:#8b949e}',
        '.card{fill:#161b22;stroke:#30363d;stroke-width:1}.label{font-size:14px;font-weight:600}',
        '.value{font-size:24px;font-weight:700;fill:#58a6ff}.note{font-size:11px;fill:#8b949e}',
        '</style>',
        '<rect width="100%" height="100%" rx="12" fill="#0d1117"/>',
        '<text x="24" y="34" class="title">Flagship portfolio evidence</text>',
        f'<text x="24" y="58" class="sub">Audited across {total} featured repositories · structural signals, not popularity metrics</text>',
    ]

    for index, (label, value, note) in enumerate(metrics):
        col = index % 2
        row = index // 2
        x = 24 + col * (card_w + gap)
        y = 78 + row * (card_h + gap)
        parts.extend(
            [
                f'<rect x="{x}" y="{y}" width="{card_w}" height="{card_h}" rx="10" class="card"/>',
                f'<text x="{x + 18}" y="{y + 27}" class="label">{escape(label)}</text>',
                f'<text x="{x + 18}" y="{y + 59}" class="value">{escape(value)}</text>',
                f'<text x="{x + 18}" y="{y + 82}" class="note">{escape(note)}</text>',
            ]
        )

    parts.append(
        f'<text x="24" y="{height - 18}" class="sub">Generated from FEATURED.md + GitHub repository structure. Semantic classifications are explicit in scripts/generate_portfolio_metrics.py.</text>'
    )
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main() -> None:
    """Audit the flagship set and write the portfolio evidence SVG."""
    repos = _featured_repos()
    evidence = [_audit_repo(repo) for repo in repos]
    total = len(evidence)

    metrics = [
        _metric("CI-backed", sum(item.has_ci for item in evidence), total, "GitHub Actions workflow present"),
        _metric("Automated tests", sum(item.has_tests for item in evidence), total, "tests/test/pytest/tox marker present"),
        _metric("Dedicated documentation", sum(item.has_docs for item in evidence), total, "docs directory or docs config present"),
        _metric("Citable / archived", sum(item.has_citation for item in evidence), total, "CITATION.cff or Zenodo metadata present"),
        _metric(
            "Reproducibility assets",
            sum(item.has_reproducibility_assets for item in evidence),
            total,
            "experiments/results/data/config-style artifacts present",
        ),
        _metric(
            "Real-data / empirical",
            len(REAL_DATA_OR_EMPIRICAL & set(repos)),
            total,
            "explicit curated classification; never inferred from filenames",
        ),
        _metric(
            "Research software / methods",
            len(RESEARCH_SOFTWARE_OR_METHOD_PACKAGE & set(repos)),
            total,
            "explicit flagship classification",
        ),
    ]

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(_render_svg(metrics, total), encoding="utf-8")


if __name__ == "__main__":
    main()
