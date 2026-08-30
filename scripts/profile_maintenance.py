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


def load_manifest() -> dict:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def nav_html(current: str, manifest: dict) -> str:
    chunks = ['<div align="center">']
    for label, target in manifest["navigation"]:
        active = target == current
        colour = "1F6FEB" if active else "30363D"
        logo = "&logo=pypi&logoColor=white" if label == "PyPI" else ""
        alt = f"{label} (current page)" if active else label
        img = f'<img src="https://img.shields.io/badge/{label.replace(" ", "%20")}-{colour}?style=for-the-badge{logo}" alt="{alt}" />'
        if active:
            chunks.append(f"  {img}")
        else:
            chunks.append(
                f'  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/{target}">{img}</a>'
            )
    chunks.append("</div>")
    return "\n".join(chunks)


def replace_nav(text: str, current: str, manifest: dict) -> str:
    replacement = nav_html(current, manifest)
    pattern = re.compile(r'^<div align="center">\n.*?</div>', re.DOTALL)
    if pattern.search(text):
        return pattern.sub(replacement, text, count=1)
    return replacement + "\n\n---\n\n" + text.lstrip()


def project_url(repo: str, path: str | None = None) -> str:
    base = f"https://github.com/DiogoRibeiro7/{repo}"
    return f"{base}/tree/main/{path}" if path else base


def render_featured(manifest: dict) -> str:
    rows = []
    for p in manifest["projects"]:
        if not p.get("featured"):
            continue
        rows.append(
            f'| **[{p["title"]}]({project_url(p["repo"])})** | {p["category"]} | {p["maturity"]} | {p["summary"]} |'
        )
    return (
        nav_html("FEATURED.md", manifest)
        + "\n\n---\n\n# Featured Projects\n\n"
        + "A short list for reviewers who want the strongest cross-section of the portfolio without browsing the full catalogue. Maturity is explicit so finished software, production-style systems, empirical studies and active research programmes are not presented as the same thing.\n\n"
        + "| Project | Area | Maturity | Why inspect it |\n| :-- | :-- | :-- | :-- |\n"
        + "\n".join(rows)
        + "\n\n---\n\nThe broader catalogue remains on **[Projects](PROJECTS.md)**. Published Python software is collected on **[PyPI](PYPI.md)**, while papers, software releases and other citable artifacts are collected on **[Outputs](OUTPUTS.md)**.\n"
    )


def render_pypi(manifest: dict) -> str:
    packages = [p for p in manifest["projects"] if p.get("pypi")]
    body = [nav_html("PYPI.md", manifest), "", "---", "", "# PyPI Packages", "", f"**Current audited inventory: {len(packages)} published packages.**", ""]
    for p in packages:
        pkg = p["pypi"]
        body.extend([
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
        ])
    body.extend([
        "---",
        "",
        "## Verification",
        "",
        "The manifest records only packages with evidence of an actual PyPI release. Repositories that merely contain packaging or release scaffolding are not counted.",
    ])
    return "\n".join(body) + "\n"


def render_outputs(manifest: dict) -> str:
    groups: dict[str, list[dict]] = {}
    for item in manifest["outputs"]:
        groups.setdefault(item["type"], []).append(item)
    body = [nav_html("OUTPUTS.md", manifest), "", "---", "", "# Outputs", "", "Citable and reviewable outputs: research software, paper programmes, empirical studies and archived releases. This page is intentionally about artifacts that can be inspected or cited, not activity counts.", ""]
    for kind, items in groups.items():
        body.extend([f"## {kind}", ""])
        for item in items:
            url = project_url(item["repo"], item.get("path"))
            suffix = []
            if item.get("pypi"):
                suffix.append(f'[PyPI](https://pypi.org/project/{item["pypi"]}/)')
            if item.get("doi"):
                suffix.append("DOI/archive metadata in repository")
            extra = " · ".join(suffix)
            body.append(f'- **[{item["title"]}]({url})**' + (f" — {extra}" if extra else ""))
        body.append("")
    return "\n".join(body) + "\n"


def render_case_studies(manifest: dict) -> str:
    body = [nav_html("CASE_STUDIES.md", manifest), "", "---", "", "# Case Studies", "", "A small set of end-to-end examples showing the problem, constraints, method and resulting decision or system. These are deliberately more selective than the project catalogue.", ""]
    for case in manifest["case_studies"]:
        repo = case["repo"]
        body.extend([
            f'## [{repo}]({project_url(repo)})',
            "",
            f'**Problem.** {case["problem"]}',
            "",
            f'**Constraints.** {case["constraints"]}',
            "",
            f'**Method.** {case["method"]}',
            "",
            f'**Outcome.** {case["outcome"]}',
            "",
        ])
    return "\n".join(body) + "\n"


def generated_files(manifest: dict) -> dict[str, str]:
    return {
        "FEATURED.md": render_featured(manifest),
        "PYPI.md": render_pypi(manifest),
        "OUTPUTS.md": render_outputs(manifest),
        "CASE_STUDIES.md": render_case_studies(manifest),
    }


def write_generated(manifest: dict) -> None:
    for path, content in generated_files(manifest).items():
        (ROOT / path).write_text(content, encoding="utf-8")
    for path in PAGES:
        file_path = ROOT / path
        if not file_path.exists():
            continue
        text = file_path.read_text(encoding="utf-8")
        updated = replace_nav(text, path, manifest)
        file_path.write_text(updated, encoding="utf-8")


def check(manifest: dict) -> list[str]:
    errors: list[str] = []
    nav_targets = [target for _, target in manifest["navigation"]]
    if len(nav_targets) != len(set(nav_targets)):
        errors.append("navigation targets are not unique")
    for target in nav_targets:
        if not (ROOT / target).exists():
            errors.append(f"navigation target missing: {target}")
    featured = [p for p in manifest["projects"] if p.get("featured")]
    if len(featured) != 12:
        errors.append(f"expected 12 featured projects, found {len(featured)}")
    pypi_names = [p["pypi"] for p in manifest["projects"] if p.get("pypi")]
    if len(pypi_names) != len(set(pypi_names)):
        errors.append("duplicate PyPI package names")
    repos = [p["repo"] for p in manifest["projects"]]
    if len(repos) != len(set(repos)):
        errors.append("duplicate project repositories")
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
        if not text.startswith(canonical_nav[path]):
            errors.append(f"navigation is stale: {path}")
    return errors


def main() -> int:
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
