<div align="center">
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/README.md"><img src="assets/links/nav-home.svg" alt="Home" width="96" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/FEATURED.md"><img src="assets/links/nav-featured.svg" alt="Featured" width="116" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/PROJECTS.md"><img src="assets/links/nav-projects.svg" alt="Projects" width="112" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/METHODS.md"><img src="assets/links/nav-methods.svg" alt="Methods" width="112" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/RESEARCH.md"><img src="assets/links/nav-research.svg" alt="Research" width="120" height="40" /></a>
  <img src="assets/links/nav-evidence-active.svg" alt="Evidence (current page)" width="120" height="40" />
</div>

---

# Statistics

A concise view of public project evidence, engineering controls, professional outcomes and portfolio composition.

## Portfolio at a Glance

<!-- statistics:snapshot:start -->
| Portfolio signal | Current value |
| :-- | --: |
| Manifest-backed public projects | **43** |
| Substantial outputs | **39** |
| Case studies | **16 across 14 domains** |
| Published PyPI packages | **11** |
| Real-data / empirical projects | **25 / 43 (58%)** |
| Research software / methods | **17 / 43 (40%)** |
| Curated flagship repositories | **12** |
| Curated catalogue entries | **71** |
<!-- statistics:snapshot:end -->

These figures describe distinct populations; definitions and collection methods are documented in [Methodology and Data Sources](#methodology-and-data-sources).

<!-- statistics:denominator:start -->
The primary public-project denominator is the **43 projects** in [`data/portfolio.json`](data/portfolio.json).
<!-- statistics:denominator:end -->

<p align="center">
  <img src="assets/portfolio-overview.svg" alt="Portfolio-wide evidence dashboard showing project count, outputs, case studies, empirical work, research software, PyPI packages and maturity mix" width="100%" />
</p>

<details>
<summary>Metric definitions (expanded audit table)</summary>

<!-- statistics:depth:start -->
| Measure | Current scope | What it means |
| :-- | --: | :-- |
| Manifest-backed public projects | **43** | Projects with explicit category, maturity and evidence metadata |
| Substantial outputs | **39** | Published software, research programmes, empirical/replication studies, and decision/engineering artifacts |
| Published PyPI packages | **11** | Verified package releases, not merely package-ready repositories |
| Real-data / empirical projects | **25 / 43 (58%)** | Explicitly classified in the manifest |
| Research software / methods | **17 / 43 (40%)** | Explicitly classified libraries, methods and research tooling |
| Case studies | **16 across 14 domains** | End-to-end problem → constraints → method → outcome narratives |
| Curated flagship projects | **12** | Reviewer-oriented subset; deliberately not used as the portfolio denominator |
<!-- statistics:depth:end -->

</details>

## Research and Engineering Evidence

### Output composition

<!-- statistics:outputs-intro:start -->
The **39 outputs** currently break down into:
<!-- statistics:outputs-intro:end -->

<!-- statistics:outputs:start -->
| Output class | Count |
| :-- | --: |
| Published research software | **11** |
| Research and paper programmes | **5** |
| Empirical and replication studies | **10** |
| Decision and engineering artifacts | **13** |
<!-- statistics:outputs:end -->

This is an artifact count, not a repository count: a repository can legitimately produce more than one inspectable output.

The **11 PyPI packages** and **11 published research-software outputs** are separate measures, even though their current totals happen to match. The PyPI figure counts projects with recorded package releases; the output figure counts records classified as published research software in the curated output inventory. For example, **DataExcept** is included in the PyPI total, while its output is classified under decision and engineering artifacts. **ChangePointLab** is included as a published research-software output with archive metadata, but has no PyPI package recorded in the manifest. Neither category requires a software DOI or implies that unrelated preprint-stage code must be made public.

---

## Delivered Impact

Self-reported industry outcomes, separate from public repository metrics. Commercial baselines and measurement records are not published here.

| Delivered outcome | Result |
| :-- | --: |
| Reporting cost reduction | **80%** |
| Analytics processing-time reduction | **30%** |
| Inventory-value reduction through forecasting and operational optimisation | **€500K** |

---

### Flagship engineering controls

**Denominator:** the **12 projects in [`FEATURED.md`](FEATURED.md)**. This smaller set is used only for repository-structure auditing, where a consistent manual/automated check is useful.

<p align="center">
  <img src="assets/portfolio-evidence.svg" alt="Engineering-control audit for twelve flagship repositories covering CI, tests, documentation, citation metadata and reproducibility assets" width="100%" />
</p>

Current structural evidence across those 12 flagships:

<!-- statistics:controls:start -->
| Control | Coverage |
| :-- | --: |
| CI workflow present | **12 / 12 (100%)** |
| Automated-test marker present | **12 / 12 (100%)** |
| Dedicated documentation | **12 / 12 (100%)** |
| Citation / archive metadata | **11 / 12 (92%)** |
| Reproducibility-style assets | **12 / 12 (100%)** |
<!-- statistics:controls:end -->

These are structural controls, not claims that every project is scientifically valid or production-ready. The reproducibility row now counts a curated, nonempty tracked artifact in each flagship repository; it does not assert that the artifact was executed successfully, that all inputs are available, or that a paper was replicated independently.

<details>
<summary><strong>Reproducibility evidence index — 12 inspectable artifacts</strong></summary>

The following references identify one concrete artifact per flagship repository and describe its scope or dependencies. A source file, notebook, configuration, or fixture is evidence of an inspectable reproducibility pathway, not a successful independent rerun.

<!-- statistics:reproducibility-index:start -->
| Flagship repository | Reference artifact | What it demonstrates / requires |
| :-- | :-- | :-- |
| [feedback-intelligence-agent](https://github.com/DiogoRibeiro7/feedback-intelligence-agent) | [RAG benchmarking script](https://github.com/DiogoRibeiro7/feedback-intelligence-agent/blob/main/scripts/benchmark.py) | Local retrieval/evaluation driver; example dataset and provider configuration determine the run |
| [clinic-forecasting-platform](https://github.com/DiogoRibeiro7/clinic-forecasting-platform) | [Hybrid-policy benchmark](https://github.com/DiogoRibeiro7/clinic-forecasting-platform/blob/main/scripts/run_hybrid_policy_benchmark.py) | Synthetic-data staffing experiment with separately documented decision and coverage limits |
| [transaction-risk-lakehouse](https://github.com/DiogoRibeiro7/transaction-risk-lakehouse) | [Spark model benchmark](https://github.com/DiogoRibeiro7/transaction-risk-lakehouse/blob/main/src/transaction_risk/experiments/benchmark.py) | Temporal risk-model evaluation implementation; demo data and local Spark required |
| [genSurvPy](https://github.com/DiogoRibeiro7/genSurvPy) | [Study reproduction entrypoint](https://github.com/DiogoRibeiro7/genSurvPy/blob/main/research/discrimination-not-calibration/scripts/reproduce.py) | Pilot and locked-production orchestration for simulation, aggregation, tables and figures |
| [setqca-python](https://github.com/DiogoRibeiro7/setqca-python) | [R reference fixture generator](https://github.com/DiogoRibeiro7/setqca-python/blob/main/validation/r/generate_fixtures.R) | Cross-language parity fixtures; R QCA and jsonlite required when regenerating |
| [ChangePointLab](https://github.com/DiogoRibeiro7/ChangePointLab) | [Reproduction notebook](https://github.com/DiogoRibeiro7/ChangePointLab/blob/main/docs/notebooks/within_period_reproduction.ipynb) | Method comparison/reproduction notebook; execution depends on notebook environment |
| [population-resemblance](https://github.com/DiogoRibeiro7/population-resemblance) | [Published-table reproduction](https://github.com/DiogoRibeiro7/population-resemblance/blob/main/examples/reproduce_table2.py) | Deterministic verification of selected PRS calibration values and tolerances |
| [DataConsistencyChecker](https://github.com/DiogoRibeiro7/DataConsistencyChecker) | [OpenML-backed demonstration](https://github.com/DiogoRibeiro7/DataConsistencyChecker/blob/main/Demo%20Notebooks/Demo_Clear_Issues.ipynb) | Executable notebook demonstrating pattern checks; downloads the hypothyroid dataset from OpenML |
| [behavioral-sensing-research](https://github.com/DiogoRibeiro7/behavioral-sensing-research) | [Sensing simulation runner](https://github.com/DiogoRibeiro7/behavioral-sensing-research/blob/main/scripts/run_phase1_recoverable_gap.py) | Phase-one recoverable-information experiment; protocol and artifact assumptions documented in repository |
| [oisst-fourier-neural-operator](https://github.com/DiogoRibeiro7/oisst-fourier-neural-operator) | [NOAA baseline notebook](https://github.com/DiogoRibeiro7/oisst-fourier-neural-operator/blob/main/notebooks/05_baselines.ipynb) | Empirical SST forecasting baseline; NOAA data preparation and experiment environment required |
| [lisbon-spatial-dynamics](https://github.com/DiogoRibeiro7/lisbon-spatial-dynamics) | [Spatial sensitivity analysis](https://github.com/DiogoRibeiro7/lisbon-spatial-dynamics/blob/main/scripts/analyse_housing_spatial_sensitivity.py) | Geographic robustness procedure; official-data inputs and configured boundaries required |
| [energy-system-simulator](https://github.com/DiogoRibeiro7/energy-system-simulator) | [Storage-value experiment](https://github.com/DiogoRibeiro7/energy-system-simulator/blob/main/experiments/storage_value/scripts/run_experiment.py) | Configuration-backed power-system experiment with local input data |
<!-- statistics:reproducibility-index:end -->

</details>

---

## Technology and Research Distribution

### Programming languages across the full GitHub inventory

<p align="center">
  <img src="assets/language-radar.svg" alt="Radar of the six leading GitHub primary-language classifications across 504 owned public and private repositories" width="100%" />
</p>

GitHub Linguist assigns one primary language to each of the **504 owned repositories**, including private repositories. Jupyter Notebook is classified separately from Python. This is a repository count, not a measure of proficiency or lines of code.

| GitHub primary-language classification | Public | Private | Total |
| :-- | --: | --: | --: |
| Python | 122 | 189 | **311** |
| Jupyter Notebook | 58 | 30 | **88** |
| R | 16 | 10 | **26** |
| TeX | 7 | 12 | **19** |
| TypeScript | 9 | 6 | **15** |
| Rust | 6 | 2 | **8** |
| Other / unclassified | 22 | 15 | **37** |
| **Total** | **240** | **264** | **504** |

The [aggregate language snapshot](data/repository_language_snapshot.json) records counts only, without private repository identifiers. Refresh requirements are documented in [Methodology and Data Sources](#methodology-and-data-sources).

### Public portfolio topic composition

<!-- statistics:topic-intro:start -->
**Denominator:** the **71 curated entries in [`PROJECTS.md`](PROJECTS.md)**. Unlike the manifest dashboard above, this measures breadth of the catalogue rather than the maturity or evidential strength of each project.
<!-- statistics:topic-intro:end -->

<p align="center">
  <img src="assets/topic-statistics.svg" alt="Bar chart showing the distribution of curated project entries across technical and research topics" width="100%" />
</p>

Topic counts describe catalogue composition, not project quality or proficiency.

---

## Methodology and Data Sources

The [Portfolio Policy](PORTFOLIO_POLICY.md) documents inclusion rules. Account inventory counts and language classifications use the authenticated, dated [visibility](data/repository_visibility_snapshot.json) and [language](data/repository_language_snapshot.json) snapshots. The inventory includes archived repositories and publishes aggregate private counts only; anonymous visitors cannot independently verify private counts.

| Account visibility (29 October 2026) | Repositories | Archived |
| :-- | --: | --: |
| Public | **240** | 5 |
| Private | **264** | 1 |
| **Total** | **504** | **6** |

The snapshot is point-in-time ownership metadata, not a measure of quality, experience, deployed systems or scientific validity. The [refresh script](scripts/refresh_repository_inventory.py) and [weekly workflow](.github/workflows/repository-inventory.yml) update aggregates when a `PROFILE_INVENTORY_TOKEN` with read-only Metadata access to owned repositories is configured; otherwise the checked-in snapshot remains dated.

<!-- statistics:boundaries:start -->
| Question | Denominator |
| :-- | :-- |
| What does the serious public portfolio contain? | **43 manifest-backed public projects** |
| What inspectable artifacts has it produced? | **39 output records** |
| What can a reviewer inspect end-to-end? | **16 case studies across 14 domains** |
| How strong are repository controls on the curated front page? | **12 flagship repositories** |
| Where is the broad catalogue concentrated? | **71 PROJECTS.md entries** |
<!-- statistics:boundaries:end -->

Professional delivery figures are self-reported and cannot be independently reproduced from these repositories. Engineering controls indicate tracked artifacts, not independently successful reruns. Popularity metrics are attention signals only.

---

## GitHub Activity and Reach

These are reach signals, not evidence of research quality or engineering reliability.

<p align="center">
  <img src="assets/star-metrics.svg" alt="Bar chart of star counts for the ten most-starred public repositories" width="100%" />
</p>

<!-- statistics:stars:start -->
| Repository | Stars |
| :-- | --: |
| [bmssp](https://github.com/DiogoRibeiro7/bmssp) | **26** |
| [esmad_public](https://github.com/DiogoRibeiro7/esmad_public) | **7** |
| [genSurvPy](https://github.com/DiogoRibeiro7/genSurvPy) | **7** |
| [min_ratio_cycle](https://github.com/DiogoRibeiro7/min_ratio_cycle) | **6** |
| [heavytails](https://github.com/DiogoRibeiro7/heavytails) | **4** |
| [Medium-Blog](https://github.com/DiogoRibeiro7/Medium-Blog) | **4** |
| [causal-uplift-marketing-campaign](https://github.com/DiogoRibeiro7/causal-uplift-marketing-campaign) | **3** |
| [fastapi-ml-platform](https://github.com/DiogoRibeiro7/fastapi-ml-platform) | **3** |
| [nosql-databases-labs](https://github.com/DiogoRibeiro7/nosql-databases-labs) | **3** |
| [smart-todo-action](https://github.com/DiogoRibeiro7/smart-todo-action) | **3** |

_Top 10 of 228 public non-fork repositories · counts fetched 2026-10-22 · ties broken alphabetically._
<!-- statistics:stars:end -->


