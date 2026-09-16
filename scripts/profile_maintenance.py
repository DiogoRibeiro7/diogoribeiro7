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

CASE_STUDY_ROUTES = {
    "System reliability & production": {
        "Production AI",
        "Forecasting & MLOps",
        "Data engineering",
    },
    "Model selection & falsification": {
        "LLM adaptation",
        "Scientific ML",
        "Industrial ML",
    },
    "Forecast-to-decision systems": {
        "Optimisation",
        "Decision science",
        "Mobility decision systems",
    },
    "Measurement & inference": {
        "Public finance",
        "Labour economics",
    },
}

OUTPUT_TYPE_PURPOSE = {
    "Published research software": (
        "Installable methods and research tooling with inspectable release evidence."
    ),
    "Research and paper programmes": (
        "Active research questions with public code, data pipelines or manuscript evidence."
    ),
    "Empirical and replication studies": (
        "Falsifiable analyses built around real data, explicit baselines and provenance."
    ),
    "Decision and engineering artifacts": (
        "Systems where modelling is connected to serving, operations or an explicit decision rule."
    ),
}


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


def output_evidence(item: dict) -> str:
    """Summarise concrete public evidence attached to an output record."""
    signals: list[str] = []
    if item.get("pypi"):
        signals.append(f'[PyPI](https://pypi.org/project/{item["pypi"]}/)')
    if item.get("doi"):
        signals.append("DOI/archive metadata")
    if item.get("path"):
        signals.append("dedicated research path")
    if not signals:
        signals.append("repository artifact")
    return " · ".join(signals)


def render_outputs(manifest: dict) -> str:
    """Render outputs as an evidence index rather than a flat artifact list."""
    groups: dict[str, list[dict]] = {}
    for item in manifest["outputs"]:
        groups.setdefault(item["type"], []).append(item)

    projects = {project["repo"]: project for project in manifest["projects"]}
    unknown_output_repos = sorted(
        {item["repo"] for item in manifest["outputs"]} - set(projects)
    )
    if unknown_output_repos:
        raise ValueError(
            f"Output repositories missing project metadata: {unknown_output_repos}"
        )

    body = [
        nav_html("OUTPUTS.md", manifest),
        "",
        "---",
        "",
        "# Outputs",
        "",
        f'**{len(manifest["outputs"])} substantial public artifacts are indexed here.**',
        "",
        "This page answers a narrower question than Projects: **what inspectable thing did the work produce?** Output class, repository maturity and release evidence are kept separate so a published package, an empirical study, an active research programme and a production-style system are not presented as equivalent signals.",
        "",
        "## Evidence index",
        "",
        "| Output class | Count | What to inspect |",
        "| :-- | --: | :-- |",
    ]

    for kind, items in groups.items():
        purpose = OUTPUT_TYPE_PURPOSE.get(
            kind, "Inspectable public artifacts in this output class."
        )
        body.append(f"| **{kind}** | **{len(items)}** | {purpose} |")

    body.extend(
        [
            "",
            "The sections below remain generated from `data/portfolio.json`. Maturity comes from the corresponding project record; release signals come from the output record itself.",
            "",
        ]
    )

    for kind, items in groups.items():
        body.extend(
            [
                f"## {kind}",
                "",
                OUTPUT_TYPE_PURPOSE.get(
                    kind, "Inspectable public artifacts in this output class."
                ),
                "",
                "| Artifact | Repository maturity | Public evidence | What it demonstrates |",
                "| :-- | :-- | :-- | :-- |",
            ]
        )
        for item in items:
            project = projects[item["repo"]]
            url = project_url(item["repo"], item.get("path"), item.get("ref", "main"))
            evidence = output_evidence(item)
            description = item.get("summary", "")
            body.append(
                f'| **[{item["title"]}]({url})** | {project["maturity"]} | {evidence} | {description} |'
            )
        body.append("")

    body.extend(
        [
            "---",
            "",
            "For a shorter reviewer-oriented cross-section, start with **[Featured](FEATURED.md)**. For end-to-end reasoning from problem to outcome, use **[Case Studies](CASE_STUDIES.md)**. Published Python packages are collected separately on **[PyPI](PYPI.md)**.",
        ]
    )
    return "\n".join(body) + "\n"


def case_study_route(domain: str) -> str:
    """Map a case-study domain to a reviewer-oriented reasoning route."""
    matches = [route for route, domains in CASE_STUDY_ROUTES.items() if domain in domains]
    if len(matches) != 1:
        raise ValueError(f"Case-study domain must map to exactly one reviewer route: {domain!r}")
    return matches[0]


def render_case_studies(manifest: dict) -> str:
    """Render case studies by recurring reasoning pattern rather than sparse domain headings."""
    cases = manifest["case_studies"]
    routes: dict[str, list[dict]] = {route: [] for route in CASE_STUDY_ROUTES}
    domains = {case.get("domain", "Other") for case in cases}

    for case in cases:
        routes[case_study_route(case.get("domain", "Other"))].append(case)

    body = [
        nav_html("CASE_STUDIES.md", manifest),
        "",
        "---",
        "",
        "# Case Studies",
        "",
        f'**{len(cases)} end-to-end cases across {len(domains)} domains, organised into four reviewer routes.**',
        "",
        "These cases are selective. They are grouped by the kind of judgement they demonstrate rather than by application domain, so recurring patterns are easier to compare across the portfolio.",
        "",
        "| Reviewer route | What it demonstrates |",
        "| :-- | :-- |",
        "| **System reliability & production** | Whether the data, model, serving and monitoring chain can be trusted together. |",
        "| **Model selection & falsification** | Whether complexity earns its place against strong baselines and decision-relevant evaluation. |",
        "| **Forecast-to-decision systems** | Whether predictive uncertainty is carried through to an explicit operational decision. |",
        "| **Measurement & inference** | Whether definitions, identification and provenance support the claim being made. |",
        "",
    ]

    for route, route_cases in routes.items():
        body.extend([f"## {route}", ""])
        for case in route_cases:
            repo = case["repo"]
            url = project_url(repo, case.get("path"), case.get("ref", "main"))
            title = case.get("title", repo)
            body.extend(
                [
                    f"### [{title}]({url})",
                    "",
                    f'**Domain.** {case.get("domain", "Other")}',
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
    unknown_output_repos = sorted(
        {item["repo"] for item in manifest["outputs"]} - set(repos)
    )
    if unknown_output_repos:
        errors.append(f"output repositories missing from project inventory: {unknown_output_repos}")
    case_titles = [case.get("title", case["repo"]) for case in manifest["case_studies"]]
    if len(case_titles) != len(set(case_titles)):
        errors.append("duplicate case-study titles")
    case_domains = {case.get("domain", "Other") for case in manifest["case_studies"]}
    mapped_domains = set().union(*CASE_STUDY_ROUTES.values())
    unknown_case_domains = sorted(case_domains - mapped_domains)
    if unknown_case_domains:
        errors.append(f"case-study domains missing reviewer routes: {unknown_case_domains}")

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
