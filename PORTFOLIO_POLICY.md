# Portfolio Policy

This repository distinguishes between the **canonical public portfolio**, the broader **curated catalogue**, and the complete set of repositories on the account.

The distinction is intentional. Repository count is not used as a proxy for seniority, scientific quality, engineering maturity, or professional impact.

## Portfolio layers

| Layer | Purpose | Source of truth |
| :-- | :-- | :-- |
| **Canonical public portfolio** | Serious reviewer-facing work with explicit evidence metadata | `data/portfolio.json` |
| **Featured projects** | Human-curated 12-project cross-section for fast review | `FEATURED.md` |
| **Curated catalogue** | Broader public technical and research breadth | `PROJECTS.md` |
| **Outputs** | Inspectable artifacts produced by canonical projects | manifest `outputs` records |
| **Case studies** | End-to-end problem → constraints → method → outcome evidence | manifest `case_studies` records |
| **Full account** | Every public repository, including experiments, teaching utilities, historical work and small tools | GitHub profile |

## Canonical inclusion criteria

A project belongs in the canonical public portfolio when it satisfies all of the following:

1. **Publicly inspectable.** An external reviewer can access the repository and the evidence linked from the profile without credentials.
2. **Substantive technical or research content.** The repository demonstrates a method, system, empirical study, research programme, decision workflow, or reusable software artifact rather than only configuration or scaffolding.
3. **Clear evidence state.** The project can be assigned a meaningful maturity label such as empirical study, research software, published software, decision system, or production-style system.
4. **Inspectable reasoning or engineering.** The repository exposes enough implementation, methodology, documentation, validation, or results for a reviewer to understand what was done.
5. **Stable enough to cite.** The repository is not merely a temporary scratchpad, abandoned experiment, or placeholder.
6. **Non-redundant portfolio signal.** It adds evidence not already represented more clearly by another canonical project.

A project does **not** need to be large, popular, or production deployed. It does need to make a credible, inspectable claim.

## What stays outside the canonical denominator

The following may still appear in `PROJECTS.md`, Teaching, or other profile pages without entering the canonical manifest:

- teaching repositories whose main purpose is course delivery rather than portfolio evidence;
- small developer utilities and workflow helpers;
- historical repositories retained for reference;
- exploratory notebooks and proof-of-concept work;
- repositories that substantially duplicate stronger canonical evidence;
- private repositories;
- projects whose public surface is incomplete or requires credentials;
- repositories that contain scaffolding but not yet enough implemented evidence.

These exclusions are not negative judgements. They simply answer a different question from the canonical portfolio.

## Public visibility rule

Anything counted in the canonical portfolio, Outputs, Case Studies, Featured, or another reviewer-facing evidence section must be publicly accessible.

Private GitHub or GitLab repositories may inform current work, but they are not presented as public evidence until their visibility changes and the repository passes the same inclusion rules.

The external-inventory check validates linked same-owner GitHub and GitLab repositories where supported.

## Maturity labels

Maturity and topic are separate dimensions.

A project can be technically strong without being production software, and an empirical study should not be presented as equivalent to a released package.

Current maturity labels are generated from the manifest and may include:

- **published software**
- **research software**
- **production-style system**
- **empirical study**
- **replication study**
- **research programme**
- **research portfolio**
- **decision system**
- **decision study**

New labels should be added only when an existing label cannot describe the evidence state without distortion.

## Output policy

An output is an inspectable artifact produced by a canonical project. Examples include:

- released research software;
- a reproducible empirical study;
- a paper-oriented research programme;
- a decision or engineering artifact.

Outputs are not required to map one-to-one with repositories. One repository may legitimately produce multiple distinct outputs when each is independently inspectable.

## Case-study policy

Case studies are selective and should demonstrate end-to-end reasoning.

A useful case study contains:

- a concrete problem;
- material constraints;
- the method or design choice;
- an outcome that shows what was learned, built, or decided.

Case studies are not repository summaries. They exist to expose judgement.

## Featured-project policy

`FEATURED.md` is a human-curated reviewer route, not an automated top-12 list.

The selection should preserve a useful cross-section of:

- system and production engineering;
- statistical or research software;
- empirical research;
- decision modelling;
- uncertainty, monitoring, or failure-aware work.

Popularity, recency, or stars are not selection criteria by themselves.

## Updating the portfolio

When adding a canonical project:

1. verify that it is public;
2. add its metadata to `data/portfolio.json`;
3. add output or case-study records only when justified;
4. update generator routing when a genuinely new domain requires it;
5. let the maintenance workflow regenerate derived pages and assets;
6. confirm the integrity workflow passes;
7. update `FEATURED.md` only when the new project improves the reviewer cross-section.

Avoid manually editing generated counts.

## Denominator discipline

Different profile pages intentionally answer different questions with different populations.

Examples:

- canonical projects measure serious public portfolio breadth;
- Outputs measure artifact depth;
- Case Studies measure end-to-end reasoning;
- Featured measures a deliberately small reviewer sample;
- `PROJECTS.md` topic counts measure broader catalogue composition;
- GitHub stars measure attention only.

These denominators should remain separate rather than being collapsed into one headline number.
