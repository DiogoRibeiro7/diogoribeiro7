from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "portfolio.json"
PAGES = [
    "README.md",
    "FEATURED.md",
    "PROJECTS.md",
    "METHODS.md",
    "RESEARCH.md",
    "OUTPUTS.md",
    "CASE_STUDIES.md",
    "TEACHING.md",
    "PYPI.md",
    "STATISTICS.md",
]
MATURITY_START = "<!-- maturity:start -->"
MATURITY_END = "<!-- maturity:end -->"
NAV_PATTERN = re.compile(
    r'<div align="center">\n(?=(?:(?!</div>)[\s\S])*img\.shields\.io/badge/Home-).*?</div>\n*',
    re.DOTALL,
)
FEATURED_REPO_PATTERN = re.compile(r"https://github\.com/DiogoRibeiro7/([^/)#]+)")


def load_manifest() -> dict:
    """Load the canonical portfolio manifest."""
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def nav_html(current: str, manifest: dict) -> str:
    """Render the canonical navigation badges for one page."""
    chunks = ['<div align="center">']
    for label, target in manifest["navigation"]:
        active = target == current
        colour = "1F6FEB" if active else "30363D"
        logo = "&logo=pypi&logoColor=white" if label == "PyPI" else ""
        alt = f"{label} (current page)" if active else label
        badge_label = label.replace(" ", "%20")
        img = f'<img src="https://img.shields.io/badge/{badge_label}-{colour}?style=for-the-badge{logo}" alt="{alt}" />'
        if active:
            chunks.append(f"  {img}")
        else:
            chunks.append(
                f'  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/{target}">{img}</a>'
            )
    chunks.append("</div>")
    return "\n".join(chunks)


def replace_nav(text: str, current: str, manifest: dict) -> str:
    """Replace the navigation block without regenerating human-edited page content."""
    replacement = nav_html(current, manifest)
    cleaned = NAV_PATTERN.sub("", text)

    if current == "README.md":
        anchor = "Statistical modelling, production AI, decision systems, and reproducible research · Python-first"
        if anchor not in cleaned:
            raise ValueError("README navigation anchor not found")
        before, after = cleaned.split(anchor, 1)
        return before + anchor + "\n\n" + replacement + after.lstrip("\n")

    return replacement + "\n\n---\n\n" + cleaned.lstrip("\n- ")


def project_url(repo: str, path: str | None = None, ref: str = "main") -> str:
    """Build a repository or subpath URL."""
    base = f"https://github.com/DiogoRibeiro7/{repo}"
    return f"{base}/tree/{ref}/{path}" if path else base


def maturity_legend(manifest: dict) -> str:
    """Render the project-maturity legend."""
    values = sorted({p["maturity"] for p in manifest["projects"]})
    rows = "\n".join(f"- **{value}**" for value in values)
    return (
        f"{MATURITY_START}\n"
        "## Maturity labels\n\n"
        "Project maturity is kept separate from topic. A production-style system, an empirical study, a published package and an active research programme are not interchangeable signals. The manifest currently uses:\n\n"
        f"{rows}\n"
        f"{MATURITY_END}"
    )


def inject_maturity_legend(text: str, manifest: dict) -> str:
    """Insert or refresh the generated maturity legend."""
    block = maturity_legend(manifest)
    pattern = re.compile(
        re.escape(MATURITY_START) + r".*?" + re.escape(MATURITY_END), re.DOTALL
    )
    if pattern.search(text):
        return pattern.sub(block, text, count=1)
    heading = re.search(r"^# .+$", text, re.MULTILINE)
    if not heading:
        return text + "\n\n" + block + "\n"
    pos = heading.end()
    return text[:pos] + "\n\n" + block + text[pos:]


def featured_repos() -> list[str]:
    """Return the twelve human-curated repositories listed on FEATURED.md."""
    text = (ROOT / "FEATURED.md").read_text(encoding="utf-8")
    excluded = {"diogoribeiro7"}
    matches = FEATURED_REPO_PATTERN.findall(text)
    return list(dict.fromkeys(repo for repo in matches if repo not in excluded))


def render_pypi(manifest: dict) -> str:
    """Render the generated PyPI page."""
    packages = [p for p in manifest["projects"] if p.get("pypi")]
    body = [
        nav_html("PYPI.md", manifest),
        "",
        "---",
        "",
        "# PyPI Packages",
        "",
        f"**Current audited inventory: {len(packages)} published packages.**",
        "",
    ]
    for p in packages:
        pkg = p["pypi"]
        body.extend(
            [
                f'## [`{pkg}`](https://pypi.org/project/{pkg}/)',
                "",
                f'[![PyPI](https://img.shields.io/pypi/v/{pkg}?label=PyPI)](https://pypi.org/project/{pkg}/) [![Python](https://img.shields.io/pypi/pyversions/{pkg})](https://pypi.org/project/{pkg}/)',
                "",
                p["summary"],
                "",
                "```bash",
                f"pip install {pkg}",
                "```",
                "",
                f'**Source:** [DiogoRibeiro7/{p["repo"]}]({project_url(p["repo"])})  ',
                f'**Maturity:** {p["maturity"]}',
                "",
            ]
        )
    body.extend(
        [
            "---",
            "",
            "## Verification",
            "",
            "The manifest records only packages with evidence of an actual PyPI release. Repositories that merely contain packaging or release scaffolding are not counted.",
        ]
    )
    return "\n".join(body) + "\n"


def render_outputs(manifest: dict) -> str:
    """Render the generated outputs index."""
    groups: dict[str, list[dict]] = {}
    for item in manifest["outputs"]:
        groups.setdefault(item["type"], []).append(item)
    body = [
        nav_html("OUTPUTS.md", manifest),
        "",
        "---",
        "",
        "# Outputs",
        "",
        f'**{len(manifest["outputs"])} substantial public artifacts are indexed here.**',
        "",
        "This is the broad output index, not a second Featured page. It includes published research software, paper/research programmes, empirical and replication studies, and decision/engineering artifacts that have a substantial inspectable result.",
        "",
    ]
    for kind, items in groups.items():
        body.extend([f"## {kind}", ""])
        for item in items:
            url = project_url(item["repo"], item.get("path"), item.get("ref", "main"))
            suffix = []
            if item.get("pypi"):
                suffix.append(f'[PyPI](https://pypi.org/project/{item["pypi"]}/)')
            if item.get("doi"):
                suffix.append("DOI/archive metadata")
            meta = " · ".join(suffix)
            description = item.get("summary", "")
            tail = f" — {description}" if description else ""
            if meta:
                tail += f" *({meta})*"
            body.append(f'- **[{item["title"]}]({url})**{tail}')
        body.append("")
    return "\n".join(body) + "\n"


def render_case_studies(manifest: dict) -> str:
    """Render the generated case-studies page."""
    groups: dict[str, list[dict]] = {}
    for case in manifest["case_studies"]:
        groups.setdefault(case.get("domain", "Other"), []).append(case)
    body = [
        nav_html("CASE_STUDIES.md", manifest),
        "",
        "---",
        "",
        "# Case Studies",
        "",
        f'**{len(manifest["case_studies"])} end-to-end cases across {len(groups)} domains.**',
        "",
        "Case studies are selective, but they are drawn from the full portfolio rather than only the flagship list. Each case has to show a genuine chain from problem and constraints through method to an inspectable outcome or decision.",
        "",
    ]
    for domain, cases in groups.items():
        body.extend([f"## {domain}", ""])
        for case in cases:
            repo = case["repo"]
            url = project_url(repo, case.get("path"), case.get("ref", "main"))
            title = case.get("title", repo)
            body.extend(
                [
                    f'### [{title}]({url})',
                    "",
                    f'**Problem.** {case["problem"]}',
                    "",
                    f'**Constraints.** {case["constraints"]}',
                    "",
                    f'**Method.** {case["method"]}',
                    "",
                    f'**Outcome.** {case["outcome"]}',
                    "",
                ]
            )
    return "\n".join(body) + "\n"


def generated_files(manifest: dict) -> dict[str, str]:
    """Return pages whose substantive content is generated from the manifest.

    FEATURED.md is deliberately absent: its reviewer-oriented selection and order
    are human-curated. Automation only normalizes its navigation and validates
    that the twelve listed repositories belong to the canonical project inventory.
    """
    return {
        "PYPI.md": render_pypi(manifest),
        "OUTPUTS.md": render_outputs(manifest),
        "CASE_STUDIES.md": render_case_studies(manifest),
    }


def write_generated(manifest: dict) -> None:
    """Refresh generated pages and canonical navigation."""
    for path, content in generated_files(manifest).items():
        (ROOT / path).write_text(content, encoding="utf-8")
    for path in PAGES:
        file_path = ROOT / path
        if not file_path.exists():
            continue
        text = file_path.read_text(encoding="utf-8")
        updated = replace_nav(text, path, manifest)
        if path == "PROJECTS.md":
            updated = inject_maturity_legend(updated, manifest)
        file_path.write_text(updated, encoding="utf-8")


def check(manifest: dict) -> list[str]:
    """Validate the profile publishing contract."""
    errors: list[str] = []
    nav_targets = [target for _, target in manifest["navigation"]]
    if len(nav_targets) != len(set(nav_targets)):
        errors.append("navigation targets are not unique")
    for target in nav_targets:
        if not (ROOT / target).exists():
            errors.append(f"navigation target missing: {target}")

    manifest_repos = {p["repo"] for p in manifest["projects"]}
    curated_featured = featured_repos()
    if len(curated_featured) != 12:
        errors.append(f"expected 12 human-curated featured repositories, found {len(curated_featured)}")
    unknown_featured = sorted(set(curated_featured) - manifest_repos)
    if unknown_featured:
        errors.append(f"featured repositories missing from manifest: {unknown_featured}")

    pypi_names = [p["pypi"] for p in manifest["projects"] if p.get("pypi")]
    if len(pypi_names) != len(set(pypi_names)):
        errors.append("duplicate PyPI package names")
    repos = [p["repo"] for p in manifest["projects"]]
    if len(repos) != len(set(repos)):
        errors.append("duplicate project repositories")
    maturities = {p.get("maturity") for p in manifest["projects"]}
    if None in maturities or "" in maturities:
        errors.append("all projects must have a maturity label")
    output_keys = [(item["repo"], item.get("path"), item["title"]) for item in manifest["outputs"]]
    if len(output_keys) != len(set(output_keys)):
        errors.append("duplicate output entries")
    case_titles = [case.get("title", case["repo"]) for case in manifest["case_studies"]]
    if len(case_titles) != len(set(case_titles)):
        errors.append("duplicate case-study titles")

    for path, expected in generated_files(manifest).items():
        actual_path = ROOT / path
        if actual_path.exists() and actual_path.read_text(encoding="utf-8") != expected:
            errors.append(f"generated file is stale: {path}")

    canonical_nav = {path: nav_html(path, manifest) for path in PAGES}
    for path in PAGES:
        fp = ROOT / path
        if not fp.exists():
            continue
        text = fp.read_text(encoding="utf-8")
        nav_blocks = NAV_PATTERN.findall(text)
        if len(nav_blocks) != 1:
            errors.append(f"expected exactly one navigation block in {path}, found {len(nav_blocks)}")
            continue
        if canonical_nav[path] not in text:
            errors.append(f"navigation is stale: {path}")
        if path == "README.md":
            title_pos = text.find("# Diogo Ribeiro")
            nav_pos = text.find(canonical_nav[path])
            if title_pos < 0 or nav_pos < title_pos:
                errors.append("README navigation must appear below the profile title")
        elif not text.startswith(canonical_nav[path]):
            errors.append(f"navigation must be first on secondary page: {path}")

    projects_text = (ROOT / "PROJECTS.md").read_text(encoding="utf-8")
    if MATURITY_START not in projects_text or MATURITY_END not in projects_text:
        errors.append("PROJECTS.md maturity legend is missing")
    return errors


def main() -> int:
    """Generate or validate the profile publishing system."""
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["generate", "check"])
    args = parser.parse_args()
    manifest = load_manifest()
    if args.command == "generate":
        write_generated(manifest)
        return 0
    errors = check(manifest)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Profile manifest and generated pages are consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
