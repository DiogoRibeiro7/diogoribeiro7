<div align="center">
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/README.md"><img src="assets/links/nav-home.svg" alt="Home" width="96" height="40" /></a>
  <img src="assets/links/nav-featured-active.svg" alt="Featured (current page)" width="116" height="40" />
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/PROJECTS.md"><img src="assets/links/nav-projects.svg" alt="Projects" width="112" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/METHODS.md"><img src="assets/links/nav-methods.svg" alt="Methods" width="112" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/RESEARCH.md"><img src="assets/links/nav-research.svg" alt="Research" width="120" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/STATISTICS.md"><img src="assets/links/nav-evidence.svg" alt="Evidence" width="120" height="40" /></a>
</div>

---

# Featured Projects

Twelve repositories selected for reviewers who want evidence quickly. This is not a ranking of the full portfolio; it is a deliberately mixed cross-section of production systems, statistical and research software, empirical studies, and decision-oriented modelling.

The selection is designed to answer three different questions: can the work operate as a system, are the methods inspectable and tested, and does the modelling remain tied to evidence and decisions?

## Choose a reviewer route

| If you want to assess… | Start with |
| :-- | :-- |
| **Production and system design** | [feedback-intelligence-agent](https://github.com/DiogoRibeiro7/feedback-intelligence-agent) · [clinic-forecasting-platform](https://github.com/DiogoRibeiro7/clinic-forecasting-platform) · [transaction-risk-lakehouse](https://github.com/DiogoRibeiro7/transaction-risk-lakehouse) |
| **Statistical and research software** | [genSurvPy](https://github.com/DiogoRibeiro7/genSurvPy) · [setqca](https://github.com/DiogoRibeiro7/setqca-python) · [ChangePointLab](https://github.com/DiogoRibeiro7/ChangePointLab) · [population-resemblance](https://github.com/DiogoRibeiro7/population-resemblance) · [DataConsistencyChecker](https://github.com/DiogoRibeiro7/DataConsistencyChecker) |
| **Empirical research and decision modelling** | [behavioral-sensing-research](https://github.com/DiogoRibeiro7/behavioral-sensing-research) · [oisst-fourier-neural-operator](https://github.com/DiogoRibeiro7/oisst-fourier-neural-operator) · [lisbon-spatial-dynamics](https://github.com/DiogoRibeiro7/lisbon-spatial-dynamics) · [energy-system-simulator](https://github.com/DiogoRibeiro7/energy-system-simulator) |

The maturity label is descriptive, not promotional. A production-style system, published package, empirical study, decision system, research toolkit, and active research programme are different kinds of evidence.

---

## Production and systems

| Project | Maturity | Evidence to inspect |
| :-- | :-- | :-- |
| **[feedback-intelligence-agent](https://github.com/DiogoRibeiro7/feedback-intelligence-agent)** | production-style system | End-to-end RAG service design: retrieval evaluation, guarded generation, FastAPI serving, observability, and CI rather than a notebook-only demonstration. |
| **[clinic-forecasting-platform](https://github.com/DiogoRibeiro7/clinic-forecasting-platform)** | production-style system | Rolling-origin forecasting, conformal uncertainty, hierarchy, staffing optimisation, serving, monitoring, and model operations connect predictive work to an explicit operational decision. |
| **[transaction-risk-lakehouse](https://github.com/DiogoRibeiro7/transaction-risk-lakehouse)** | production-style system | PySpark/lakehouse engineering combined with temporal validation, graph-derived features, cost-sensitive decisions, streaming scoring, and drift monitoring. |

---

## Statistical and research software

| Project | Maturity | Evidence to inspect |
| :-- | :-- | :-- |
| **[genSurvPy](https://github.com/DiogoRibeiro7/genSurvPy)** | published software | Known-truth survival simulation with multiple event-history families, a general multistate engine, typed APIs, reproducible validation, and a published package. |
| **[setqca](https://github.com/DiogoRibeiro7/setqca-python)** | published software | Native typed Python csQCA/fsQCA, exact Boolean minimisation, and explicit validation against the reference R implementation. |
| **[ChangePointLab](https://github.com/DiogoRibeiro7/ChangePointLab)** | published software | A common API across PELT, BOCPD, E-Divisive, HSMM, kernel, and seasonal changepoint methods, with tests, documentation, citation metadata, and archived releases. |
| **[population-resemblance](https://github.com/DiogoRibeiro7/population-resemblance)** | research software | Population-drift monitoring with the Population Resemblance Statistic, sample-size-aware decision thresholds, PSI and discrete-KS comparisons, calibration diagnostics, and Monte Carlo simulation. |
| **[DataConsistencyChecker](https://github.com/DiogoRibeiro7/DataConsistencyChecker)** | research software | 158 explainable checks for patterns and exceptions in tabular data, mixed-type support, structured reports, row-level anomaly explanations, CLI integration, and CI-backed documentation. |

---

## Empirical research and decision modelling

| Project | Maturity | Evidence to inspect |
| :-- | :-- | :-- |
| **[behavioral-sensing-research](https://github.com/DiogoRibeiro7/behavioral-sensing-research)** | research programme | Failure-aware multimodal sensing that separates sensor failure, missing evidence, occupancy ambiguity, and behavioural change before inference or alerting. |
| **[oisst-fourier-neural-operator](https://github.com/DiogoRibeiro7/oisst-fourier-neural-operator)** | empirical study | NOAA SST experiment asking when a Fourier Neural Operator actually beats persistence and classical baselines, rather than assuming neural operators win by default. |
| **[lisbon-spatial-dynamics](https://github.com/DiogoRibeiro7/lisbon-spatial-dynamics)** | empirical study | Official Portuguese data, parish-level housing change, local-accommodation pressure, spatial autocorrelation, robust regression, sensitivity analysis, and explicit limits on causal interpretation. |
| **[energy-system-simulator](https://github.com/DiogoRibeiro7/energy-system-simulator)** | decision system | Explicit unit-commitment, storage, hydro, imports, and demand-response optimisation under operational constraints, where the output is a feasible decision rather than a prediction alone. |

---

## What this selection is designed to show

Across the twelve repositories, the recurring pattern is the ability to move between:

- statistical formulation, calibration, and known-truth validation;
- production-oriented engineering and operational constraints;
- time-series monitoring, changepoints, and distribution shift;
- strong baselines and justified model complexity;
- empirical work with explicit measurement and identification limits;
- uncertainty, failure modes, and decision rules;
- reproducible research artifacts and maintainable software.

For end-to-end narratives, continue to **[Case Studies](CASE_STUDIES.md)**. For the complete curated catalogue, use **[Projects](PROJECTS.md)**. Published packages are collected on **[PyPI](PYPI.md)**, and substantial software/research artifacts on **[Outputs](OUTPUTS.md)**.
