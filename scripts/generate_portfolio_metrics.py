"""Generate evidence-based flagship metrics for the profile Statistics page."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Final
from urllib.parse import quote
from xml.sax.saxutils import escape

from check_external_inventory import get

OWNER: Final[str] = "DiogoRibeiro7"
FEATURED_PATH: Final[Path] = Path("FEATURED.md")
MANIFEST_PATH: Final[Path] = Path("data/portfolio.json")
STATISTICS_PATH: Final[Path] = Path("STATISTICS.md")
OUTPUT_PATH: Final[Path] = Path("assets/portfolio-evidence.svg")
REPRODUCIBILITY_PATH: Final[Path] = Path("data/flagship_reproducibility.json")
API_ROOT: Final[str] = "https://api.github.com"
CONTROLS_START: Final[str] = "<!-- statistics:controls:start -->"
CONTROLS_END: Final[str] = "<!-- statistics:controls:end -->"
REPRO_START: Final[str] = "<!-- statistics:reproducibility-index:start -->"
REPRO_END: Final[str] = "<!-- statistics:reproducibility-index:end -->"


@dataclass(frozen=True)
class RepoEvidence:
    """Mechanical quality signals found in one flagship repository."""

    name: str
    has_ci: bool
    has_tests: bool
    has_docs: bool
    has_citation: bool
    has_reproducibility_assets: bool
    reproducibility_path: str | None = None
    reproducibility_kind: str | None = None
    reproducibility_note: str | None = None


@dataclass(frozen=True)
class AuditResult:
    """Complete flagship audit used by both Markdown and SVG outputs."""

    repositories: tuple[str, ...]
    evidence: tuple[RepoEvidence, ...]
    real_data_count: int
    research_software_count: int

    @property
    def total(self) -> int:
        return len(self.repositories)


def _get_json(url: str) -> object:
    """Fetch JSON using the shared, bounded public-API retry policy."""
    status, payload = get(url, attempts=4)
    if status != 200:
        raise RuntimeError(f"Unexpected HTTP {status} for {url}")
    return json.loads(payload.decode("utf-8"))


def _tree_files(repo: str) -> set[str]:
    """Return nonempty tracked files from the complete main-branch tree.

    One API request replaces shallow directory-name checks. Reject truncated
    responses rather than silently undercounting large repositories.
    """
    payload = _get_json(f"{API_ROOT}/repos/{OWNER}/{repo}/git/trees/main?recursive=1")
    if not isinstance(payload, dict) or not isinstance(payload.get("tree"), list):
        raise TypeError(f"Git tree for {repo} must contain a tree array")
    if payload.get("truncated") is not False:
        raise ValueError(f"Git tree for {repo} is truncated or lacks truncation metadata")

    result: set[str] = set()
    for entry in payload["tree"]:
        if not isinstance(entry, dict):
            raise TypeError(f"Git tree for {repo} contains an invalid entry")
        path = entry.get("path")
        size = entry.get("size")
        if entry.get("type") != "blob":
            continue
        if not isinstance(path, str) or not isinstance(size, int) or size < 0:
            raise TypeError(f"Git tree for {repo} contains invalid file metadata")
        if size > 0:
            result.add(path)
    return result


@dataclass(frozen=True)
class ReproductionReference:
    """Curated reference to one specific artifact; not proof of reproducibility."""

    path: str
    kind: str
    note: str


def _reproducibility_catalog() -> dict[str, ReproductionReference]:
    """Read and validate source-linked evidence declared for featured projects."""
    payload: Any = json.loads(REPRODUCIBILITY_PATH.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or payload.get("version") != 1:
        raise ValueError("Reproducibility catalog must have version 1")
    rows = payload.get("evidence")
    if not isinstance(rows, list):
        raise TypeError("Reproducibility catalog requires an evidence array")

    result: dict[str, ReproductionReference] = {}
    for row in rows:
        if not isinstance(row, dict):
            raise TypeError("Reproducibility catalog entries must be objects")
        repo = row.get("repo")
        path = row.get("path")
        kind = row.get("kind")
        note = row.get("note")
        if not all(isinstance(value, str) and value.strip() for value in (repo, path, kind, note)):
            raise ValueError("Every reproducibility reference needs repo, path, kind and note")
        if not re.fullmatch(r"[A-Za-z0-9_.-]+", repo):
            raise ValueError(f"Invalid reproducibility repository identifier: {repo}")
        if path.startswith("/") or any(part in ("", ".", "..") for part in path.split("/")):
            raise ValueError(f"Invalid reproducibility evidence path: {repo}/{path}")
        if repo in result:
            raise ValueError(f"Duplicate reproducibility reference: {repo}")
        result[repo] = ReproductionReference(path=path, kind=kind, note=note)
    return result


def _featured_repos() -> list[str]:
    """Parse the twelve curated repositories from FEATURED.md."""
    text = FEATURED_PATH.read_text(encoding="utf-8")
    matches = re.findall(r"https://github\.com/DiogoRibeiro7/([^/)#]+)", text)
    repos = list(dict.fromkeys(repo for repo in matches if repo != "diogoribeiro7"))
    if len(repos) != 12:
        raise ValueError(f"Expected 12 flagship repositories, found {len(repos)}: {repos}")
    return repos


def _project_metadata() -> dict[str, dict[str, Any]]:
    """Load semantic project classifications from the canonical manifest."""
    payload: object = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or not isinstance(payload.get("projects"), list):
        raise TypeError("Portfolio manifest must contain a projects list.")

    metadata: dict[str, dict[str, Any]] = {}
    for project in payload["projects"]:
        if not isinstance(project, dict) or not isinstance(project.get("repo"), str):
            raise TypeError("Every manifest project must be an object with a string repo field.")
        metadata[project["repo"]] = project
    return metadata


def _audit_repo(repo: str, reference: ReproductionReference | None = None) -> RepoEvidence:
    """Audit actual tracked files and optionally verify one curated evidence link."""
    files = _tree_files(repo)
    root = {path.split("/", 1)[0] for path in files}
    docs_markers = {"docs", "mkdocs.yml", "mkdocs.yaml", "docs.yml", "docs.yaml"}
    test_markers = {"tests", "test", "pytest.ini", "tox.ini"}
    citation_markers = {"CITATION.cff", ".zenodo.json"}

    if reference is not None and reference.path not in files:
        raise ValueError(
            f"Curated reproducibility artifact missing: {repo}/{reference.path}"
        )

    return RepoEvidence(
        name=repo,
        has_ci=any(
            path.startswith(".github/workflows/") and path.endswith((".yml", ".yaml"))
            for path in files
        ),
        has_tests=bool(root & test_markers),
        has_docs=bool(root & docs_markers),
        has_citation=bool(root & citation_markers),
        has_reproducibility_assets=reference is not None,
        reproducibility_path=reference.path if reference else None,
        reproducibility_kind=reference.kind if reference else None,
        reproducibility_note=reference.note if reference else None,
    )

def audit() -> AuditResult:
    """Run the full structural and semantic audit over the curated flagship set."""
    repos = _featured_repos()
    metadata = _project_metadata()
    missing = [repo for repo in repos if repo not in metadata]
    if missing:
        raise ValueError(f"Featured repositories missing from canonical manifest: {missing}")

    catalog = _reproducibility_catalog()
    extra_repos = sorted(set(catalog) - set(repos))
    if extra_repos:
        raise ValueError(f"Reproducibility references outside Featured: {extra_repos}")

    evidence = tuple(_audit_repo(repo, catalog.get(repo)) for repo in repos)
    real_data_count = sum(bool(metadata[repo].get("real_data")) for repo in repos)
    research_software_count = sum(bool(metadata[repo].get("research_software")) for repo in repos)
    return AuditResult(tuple(repos), evidence, real_data_count, research_software_count)


def _coverage(count: int, total: int) -> str:
    """Format a count and percentage for Markdown."""
    return f"{count} / {total} ({100 * count / total:.0f}%)"


def _metric(label: str, count: int, total: int, note: str) -> tuple[str, str, str]:
    """Format one metric tuple for SVG rendering."""
    return label, f"{count}/{total} · {100 * count / total:.0f}%", note


def _metrics(result: AuditResult) -> list[tuple[str, int, str]]:
    """Return all dashboard metrics from one audit result."""
    evidence = result.evidence
    return [
        ("CI-backed", sum(item.has_ci for item in evidence), "GitHub Actions workflow present"),
        ("Automated tests", sum(item.has_tests for item in evidence), "tests/test/pytest/tox marker present"),
        ("Dedicated documentation", sum(item.has_docs for item in evidence), "docs directory or docs config present"),
        ("Citable / archived", sum(item.has_citation for item in evidence), "CITATION.cff or Zenodo metadata present"),
        (
            "Reproducibility assets",
            sum(item.has_reproducibility_assets for item in evidence),
            "curated, source-linked artifact verified in main",
        ),
        (
            "Real-data / empirical",
            result.real_data_count,
            "canonical manifest classification for the curated flagship set",
        ),
        (
            "Research software / methods",
            result.research_software_count,
            "canonical manifest classification for the curated flagship set",
        ),
    ]


def _render_svg(result: AuditResult) -> str:
    """Render the dark/light-compatible flagship evidence dashboard."""
    metrics = [_metric(label, count, result.total, note) for label, count, note in _metrics(result)]
    width = 900
    card_w = 420
    card_h = 104
    gap = 20
    rows = (len(metrics) + 1) // 2
    height = 90 + rows * (card_h + gap) + 42

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">Flagship portfolio evidence metrics</title>',
        f'<desc id="desc">Evidence metrics computed across {result.total} flagship repositories.</desc>',
        '<style>',
        'text{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:#c9d1d9}',
        '.title{font-size:24px;font-weight:700}.sub{font-size:13px;fill:#8b949e}',
        '.card{fill:#161b22;stroke:#30363d;stroke-width:1}.label{font-size:14px;font-weight:600}',
        '.value{font-size:24px;font-weight:700;fill:#58a6ff}.note{font-size:11px;fill:#8b949e}',
        '@media (prefers-color-scheme: light){text{fill:#24292f}.sub,.note{fill:#57606a}'
        '.card{fill:#f6f8fa;stroke:#d0d7de}.value{fill:#0969da}}',
        '</style>',
        '<text x="24" y="34" class="title">Flagship portfolio evidence</text>',
        f'<text x="24" y="58" class="sub">Audited across {result.total} featured repositories · structural signals, not popularity metrics</text>',
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
        f'<text x="24" y="{height - 18}" class="sub">Generated from FEATURED.md + GitHub repository structure + canonical manifest classifications.</text>'
    )
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def _render_controls_table(result: AuditResult) -> str:
    """Render the Statistics-page engineering-control table from the same audit."""
    evidence = result.evidence
    rows = [
        CONTROLS_START,
        "| Control | Coverage |",
        "| :-- | --: |",
        f'| CI workflow present | **{_coverage(sum(item.has_ci for item in evidence), result.total)}** |',
        f'| Automated-test marker present | **{_coverage(sum(item.has_tests for item in evidence), result.total)}** |',
        f'| Dedicated documentation | **{_coverage(sum(item.has_docs for item in evidence), result.total)}** |',
        f'| Citation / archive metadata | **{_coverage(sum(item.has_citation for item in evidence), result.total)}** |',
        f'| Reproducibility-style assets | **{_coverage(sum(item.has_reproducibility_assets for item in evidence), result.total)}** |',
        CONTROLS_END,
    ]
    return "\n".join(rows)


def _replace_block(text: str, replacement: str, start: str, end: str) -> str:
    """Replace exactly one bounded generated Markdown block."""
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    matches = pattern.findall(text)
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one block ({start}); found {len(matches)}")
    return pattern.sub(lambda _: replacement, text, count=1)


def _replace_controls(text: str, replacement: str) -> str:
    """Preserve the public function used by offline regression tests."""
    return _replace_block(text, replacement, CONTROLS_START, CONTROLS_END)


def _render_reproducibility_index(result: AuditResult) -> str:
    """Render per-repository, source-linked evidence without grading scientific quality."""
    rows = [
        REPRO_START,
        "| Flagship repository | Reference artifact | What it demonstrates / requires |",
        "| :-- | :-- | :-- |",
    ]
    for item in result.evidence:
        repository_link = f"https://github.com/{OWNER}/{quote(item.name)}"
        if item.reproducibility_path is None:
            rows.append(f"| [{item.name}]({repository_link}) | Not yet curated | — |")
            continue
        artifact_url = (
            f"{repository_link}/blob/main/"
            f"{quote(item.reproducibility_path, safe='/')}"
        )
        label = (item.reproducibility_kind or "Evidence artifact").replace("|", r"\|")
        note = (item.reproducibility_note or "").replace("|", r"\|")
        rows.append(
            f"| [{item.name}]({repository_link}) | [{label}]({artifact_url}) | {note} |"
        )
    rows.append(REPRO_END)
    return "\n".join(rows)


def _expected_statistics(result: AuditResult) -> str:
    """Return Statistics Markdown with both generated evidence tables refreshed."""
    current = STATISTICS_PATH.read_text(encoding="utf-8")
    updated = _replace_controls(current, _render_controls_table(result))
    return _replace_block(
        updated, _render_reproducibility_index(result), REPRO_START, REPRO_END
    )


def generate(result: AuditResult) -> None:
    """Write both audit-derived outputs."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(_render_svg(result), encoding="utf-8")
    STATISTICS_PATH.write_text(_expected_statistics(result), encoding="utf-8")


def check(result: AuditResult) -> int:
    """Fail when either committed audit-derived output is stale."""
    errors: list[str] = []
    if not OUTPUT_PATH.exists():
        errors.append(f"{OUTPUT_PATH} is missing; run this script with 'generate'")
    elif OUTPUT_PATH.read_text(encoding="utf-8") != _render_svg(result):
        errors.append("assets/portfolio-evidence.svg is stale")
    if STATISTICS_PATH.read_text(encoding="utf-8") != _expected_statistics(result):
        errors.append("STATISTICS.md flagship controls or evidence index is stale")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Flagship engineering controls are synchronized with the current audit.")
    return 0


def main() -> int:
    """Generate audit outputs or verify their committed state."""
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("generate", "check"), nargs="?", default="generate")
    args = parser.parse_args()
    result = audit()
    if args.command == "generate":
        generate(result)
        return 0
    return check(result)


if __name__ == "__main__":
    raise SystemExit(main())
