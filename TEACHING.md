<div align="center">
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/README.md"><img src="assets/links/nav-home.svg" alt="Home" width="96" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/FEATURED.md"><img src="assets/links/nav-featured.svg" alt="Featured" width="116" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/PROJECTS.md"><img src="assets/links/nav-projects.svg" alt="Projects" width="112" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/METHODS.md"><img src="assets/links/nav-methods.svg" alt="Methods" width="112" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/RESEARCH.md"><img src="assets/links/nav-research.svg" alt="Research" width="120" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/STATISTICS.md"><img src="assets/links/nav-evidence.svg" alt="Evidence" width="120" height="40" /></a>
  <img src="assets/links/nav-teaching-active.svg" alt="Teaching (current page)" width="120" height="40" />
</div>

---

# Teaching & Course Design

I teach mathematics and data subjects at the **Faculty of Media Arts and Design, Technical University of Porto (FMAD–UTP)**. My teaching work follows the same principles as my research and engineering work: make assumptions explicit, connect theory to executable evidence, and build material that can be reused, tested, reviewed, and improved rather than disappearing with one semester.

The public teaching portfolio now has two complementary layers:

- **course repositories** — exercises, notebooks, datasets, tests, submission workflows, and reference implementations;
- **[academic-presentations](https://github.com/DiogoRibeiro7/academic-presentations)** — a source-first library of reusable LaTeX/Beamer material across statistics, machine learning, causal inference, Bayesian methods, time series, and production data science.

## Current teaching areas

| Course / activity | Main focus | Public evidence |
| :-- | :-- | :-- |
| **Mathematics I** | Logic, sets, rigorous reasoning, differential and integral calculus, and the transition from symbolic work to computational intuition. | [calculus-with-python](https://github.com/DiogoRibeiro7/calculus-with-python) · [esmad_public](https://github.com/DiogoRibeiro7/esmad_public) |
| **Mathematics II / Linear Algebra & Analytic Geometry** | Matrices, linear systems, vector spaces, linear maps, determinants, geometry, numerical stability, and links to data analysis. | [linear-algebra-with-python](https://github.com/DiogoRibeiro7/linear-algebra-with-python) · [linear-algebra-tutor](https://github.com/DiogoRibeiro7/linear-algebra-tutor) |
| **NoSQL Databases** | Document modelling, CRUD, indexing, aggregation, replication, performance, and modern MongoDB features. | [nosql-databases-labs](https://github.com/DiogoRibeiro7/nosql-databases-labs) |
| **Data science & statistical methods** | Statistical modelling, experimentation, causal inference, Bayesian methods, time series, optimisation, interpretability, and production data science. | [academic-presentations](https://github.com/DiogoRibeiro7/academic-presentations) |
| **Project supervision** | Problem formulation, technical reasoning, evidence, reproducibility, implementation choices, and communication. | Supervision and assessment work spans multiple projects rather than one repository. |

The repositories are not decorative companions to the courses. Where appropriate, they contain executable exercises, validation code, assessment structure, reproducible environments, and documentation intended to remain useful beyond a single cohort.

---

## Academic presentations

**[academic-presentations](https://github.com/DiogoRibeiro7/academic-presentations)** is the main reusable presentation layer for advanced technical teaching.

It currently contains **20 active compiled course decks plus additional standalone tracks**, built around a shared FMAD–UTP Beamer system and CI-validated LaTeX sources.

The catalogue spans:

- statistical learning theory and feature engineering;
- PCA and optimisation for data science;
- deep learning and reinforcement learning;
- MCMC and Bayesian machine learning;
- causal inference and A/B testing;
- time-series forecasting;
- explainable AI and interpretability;
- AI agents and production data science;
- object-oriented programming and streaming pipelines;
- capstone and applied data-science material;
- software testing and engineering practice.

Many modules combine presentations with code, exercises, learning objectives, prerequisites, assessment material, and reproducible build rules. Compiled artifacts are produced through CI while source remains version controlled.

→ **[Browse the slide previews](https://diogoribeiro7.github.io/academic-presentations/)**

---

## Teaching artifacts worth inspecting

| Artifact | What it contains | What it demonstrates |
| :-- | :-- | :-- |
| **[Academic Presentations](https://github.com/DiogoRibeiro7/academic-presentations)** | Reusable LaTeX/Beamer course decks, exercises, rubrics, code, shared FMAD–UTP presentation infrastructure, and CI-validated builds across statistics, ML, Bayesian methods, causal inference, time series, and production data science. | A maintainable curriculum layer where advanced technical material is treated as versioned source rather than isolated slide files. |
| **[Linear Algebra with Python](https://github.com/DiogoRibeiro7/linear-algebra-with-python)** | Practical assignments, lesson notebooks, exercise/solution material, tested implementations, PR-based student submissions, grading structure, release history, and a Zenodo DOI. | A mathematics course treated as maintained software and reproducible teaching material. |
| **[NoSQL Databases Labs](https://github.com/DiogoRibeiro7/nosql-databases-labs)** | Labs on modelling, queries, aggregation, replication and modern MongoDB features; datasets, automated tests, CI, validation scripts, performance expectations, and self-paced paths. | Hands-on database teaching with engineering-quality feedback and reproducible environments. |
| **[Calculus with Python](https://github.com/DiogoRibeiro7/calculus-with-python)** | Guided notebooks on functions, numerical differentiation and integration, visual demonstrations, tested numerical helpers, a CLI, and symbolic extensions. | Using computation to expose approximation error and mathematical structure rather than replacing the mathematics. |
| **[Linear Algebra Tutor](https://github.com/DiogoRibeiro7/linear-algebra-tutor)** | A RAG-driven Socratic tutoring system built around linear-algebra learning material. | An experiment in augmenting teaching with retrieval and guided questioning while keeping course material as the source of truth. |
| **[esmad_public](https://github.com/DiogoRibeiro7/esmad_public)** | Long-lived open mathematics material including linear algebra, Python-and-mathematics examples, numerical-integration utilities, and geometric visualisations. | Continuity of open teaching material across multiple mathematical topics and academic years. |

---

## How I design technical teaching

- **Start from the mathematical or statistical object.** Tools come after definitions, assumptions, and the reasoning the student should be able to reproduce.
- **Theory should survive execution.** Mathematical statements are paired with code, numerical examples, counterexamples, or experiments when that improves understanding.
- **Assessment should reveal reasoning.** Assignments focus on method, evidence, interpretation, and reproducibility rather than only the final numeric answer.
- **Separate learning goals from tooling.** Git, CI, notebooks, LaTeX, Python, R, databases, or LLM systems are used when they serve the concept being taught.
- **Automation should improve feedback, not replace judgement.** Validation scripts catch structural mistakes quickly; conceptual and mathematical assessment remains a human task.
- **Teach uncertainty and failure, not only the happy path.** Calibration, diagnostics, assumptions, counterexamples, data-quality problems, and model failure are part of the curriculum.
- **Open material compounds.** Course repositories and presentation sources can be reviewed, cited, extended, and improved across cohorts instead of being rebuilt from private files.

---

## From classroom to research practice

I use teaching material to make the reasoning behind research and production work explicit. The same ideas recur across the portfolio:

| Teaching concept | Research / engineering connection |
| :-- | :-- |
| Linear algebra and optimisation | numerical methods, dimensionality reduction, scientific ML, constrained decision systems |
| Probability and statistical modelling | uncertainty, calibration, forecasting, survival analysis, monitoring |
| Causal inference and experimentation | identification, counterfactuals, DiD, synthetic control, A/B testing, sensitivity analysis |
| Time series | state-space models, changepoints, forecasting, rolling validation, regime change |
| Data engineering | provenance, reproducible pipelines, contracts, validation, streaming systems |
| Software testing | research-software validation, CI, reproducible releases, regression tests |
| AI systems | retrieval evaluation, observability, guardrails, execution-based testing, cost and latency |

This is intentional: students should see technical ideas as parts of a coherent reasoning system rather than unrelated modules.

---

## Seminars, mentoring & supervision

Shorter sessions and supervision work typically connect a mathematical or statistical idea to an operational workflow. Topics include statistical modelling and experimentation, causal inference, forecasting and anomaly detection, Bayesian methods, data science and MLOps, graph analytics, sensor systems, scientific ML, and reliable LLM/RAG evaluation.

For guest lectures, workshops, course collaboration, mentoring, or supervision enquiries: [Email](mailto:diogo.debastos.ribeiro@gmail.com) · [LinkedIn](https://www.linkedin.com/in/diogo-ribeiro-9094604a/) · [Website](https://diogoribeiro7.github.io) · [ORCID](https://orcid.org/0009-0001-2022-7072).

---

<div align="center">
  <a href="https://github.com/DiogoRibeiro7"><img src="https://img.shields.io/badge/%E2%86%90%20Back%20to%20profile-30363D?style=for-the-badge" alt="Back to profile" /></a>
</div>
