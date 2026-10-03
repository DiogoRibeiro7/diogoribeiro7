# Diogo Ribeiro (@DiogoRibeiro7)

**Lead Data Scientist · Researcher · Invited Assistant Professor**  
**Statistical ML · Time Series · Causal Inference · Applied AI · Research Software**  
[Technical writing, research notes, and open-source software](https://diogoribeiro7.github.io)

Statistical modelling, production AI, decision systems, and reproducible research · Python-first

<div align="center">
  <img src="assets/links/nav-home-active.svg" alt="Home (current page)" width="96" height="40" />
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/FEATURED.md"><img src="assets/links/nav-featured.svg" alt="Featured" width="116" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/PROJECTS.md"><img src="assets/links/nav-projects.svg" alt="Projects" width="112" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/METHODS.md"><img src="assets/links/nav-methods.svg" alt="Methods" width="112" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/RESEARCH.md"><img src="assets/links/nav-research.svg" alt="Research" width="120" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/STATISTICS.md"><img src="assets/links/nav-evidence.svg" alt="Evidence" width="120" height="40" /></a>
</div>

I build data and AI systems where the difficult part starts before and after model fitting: defining the estimand, choosing the decision rule, validating uncertainty, detecting distribution shift, and making the whole chain reproducible.

My default is not “use more ML.” It is to start from the problem, the evidence, and the decision being supported; establish strong statistical or mathematical baselines; and add complexity only when it earns its place empirically.

## What I Work On

My work spans statistical machine learning, time series, forecasting, causal inference, optimisation, behavioural sensing, research software, data engineering, and applied AI. Across those areas, I care most about four things:

- **Decision-aware modelling** — evaluate a model by the decisions it supports, not only by an aggregate predictive score.
- **Uncertainty and failure modes** — calibration, missingness, drift, censoring, abstention, leakage, and operating thresholds are part of the model.
- **Reproducible evidence** — typed code, tests, CI, frozen configurations, provenance, and machine-readable outputs are part of the research contract.
- **Methods that remain inspectable** — prefer the least complicated model that answers the question well and make the resulting claim auditable.

## Portfolio at a Glance

<!-- readme:portfolio-snapshot:start -->
| Evidence | Current scope |
| :-- | --: |
| Manifest-backed public projects | **43** |
| Substantial outputs | **39** |
| Published PyPI packages | **11** |
| Case studies | **13 across 11 domains** |
| Real-data / empirical projects | **25 / 43 (58%)** |
| Curated flagship repositories | **12** |
<!-- readme:portfolio-snapshot:end -->

These figures are generated from the same canonical portfolio data used by [Statistics](STATISTICS.md), so the front page and the detailed evidence page share one source of truth.

**Selected professional delivery outcomes:** 80% reduction in reporting costs · 30% reduction in analytics processing time · €500K reduction in inventory value through forecasting and operational optimisation.

---

## Selected Work

| Project | Focus | What to inspect |
| :-- | :-- | :-- |
| **[feedback-intelligence-agent](https://github.com/DiogoRibeiro7/feedback-intelligence-agent)** | Production AI / RAG | Guarded generation, retrieval evaluation, FastAPI serving, observability, and CI. |
| **[clinic-forecasting-platform](https://github.com/DiogoRibeiro7/clinic-forecasting-platform)** | Forecasting → decisions | Rolling-origin evaluation, conformal uncertainty, hierarchical forecasting, staffing optimisation, serving, and monitoring. |
| **[lisbon-spatial-dynamics](https://github.com/DiogoRibeiro7/lisbon-spatial-dynamics)** | Spatial analysis / urban economics | Official public data, parish-level housing change, local-accommodation pressure, spatial statistics, and regression. |
| **[population-resemblance](https://github.com/DiogoRibeiro7/population-resemblance)** | Drift / statistical monitoring | Population Resemblance Statistic, sample-size-aware thresholds, PSI and discrete KS benchmarks, and Monte Carlo simulation. |
| **[DataConsistencyChecker](https://github.com/DiogoRibeiro7/DataConsistencyChecker)** | Data quality / anomaly detection | Interpretable pattern discovery, outlier scoring, explanations, mixed data types, and synthetic validation examples. |
| **[genSurvPy](https://github.com/DiogoRibeiro7/genSurvPy)** | Statistical research software | Known-truth survival simulation, multiple model families, multistate simulation, typed APIs, and published releases. |
| **[ChangePointLab](https://github.com/DiogoRibeiro7/ChangePointLab)** | Time series / changepoints | Offline, online, Bayesian, kernel, state-space, and point-process change detection. |
| **[pinn](https://github.com/DiogoRibeiro7/pinn)** | Scientific machine learning | Typed PyTorch PINNs for forward and inverse PDEs, exact-solution benchmarks, adaptive sampling, and reproducible experiments. |

→ **[Featured](FEATURED.md)** gives the curated reviewer cross-section. **[Projects](PROJECTS.md)** contains the broader catalogue.

---

## Current Focus

- **Failure-aware behavioural sensing** — separating sensor failure, missing evidence, occupancy ambiguity, and genuine behavioural change before an alert is allowed to mean anything. The public programme lives in [behavioral-sensing-research](https://github.com/DiogoRibeiro7/behavioral-sensing-research).
- **Forecast → decision systems** — probabilistic forecasts evaluated by downstream decisions, constraints, and operating cost rather than forecasting metrics alone.
- **Causal inference and econometrics** — identification, counterfactual construction, synthetic control, difference-in-differences, treatment-effect estimation, and reproducible policy analysis.
- **Statistical monitoring and change detection** — population drift, changepoints, calibration, and the distinction between data-quality failures and real distributional change.
- **Research data infrastructure** — provenance, metadata validation, integrity checks, and reproducible dataset registries in [data](https://github.com/DiogoRibeiro7/data).
- **Research and teaching infrastructure** — reusable LaTeX/Beamer material in [academic-presentations](https://github.com/DiogoRibeiro7/academic-presentations), alongside open-source tooling across GitHub and [GitLab](https://gitlab.com/DiogoRibeiro7).

→ More active research threads on **[Research](RESEARCH.md#current-focus)**.

---

## How I Work

- **Model the question before the algorithm.** Define the estimand, failure modes, constraints, and decision rule first.
- **Use strong baselines.** Classical statistical and mathematical models are often the right starting point; complexity has to earn its place empirically.
- **Validate in the regime that matters.** Temporal splits, rolling-origin evaluation, realistic missingness, censoring, imbalance, and deployment constraints matter more than convenient random splits.
- **Treat reliability as part of modelling.** Calibration, uncertainty, leakage, missingness, drift, abstention, and operating thresholds belong in the design, not in an appendix.
- **Make claims reproducible.** Typed code, tests, CI, frozen configurations, provenance, and machine-readable outputs are part of the research and engineering contract.

---

## Explore by Question

| If you want to inspect… | Start here |
| :-- | :-- |
| The strongest cross-section of the portfolio | **[Featured](FEATURED.md)** |
| End-to-end problem → constraints → method → outcome reasoning | **[Case Studies](CASE_STUDIES.md)** |
| Modelling methods, statistical tools, and engineering stack | **[Methods](METHODS.md)** |
| Active research programmes and reproducibility standards | **[Research](RESEARCH.md)** |
| Rust packages for statistics, numerical methods, and validation | **[Rust](RUST.md)** |
| Citable software, studies, and released packages | **[Outputs](OUTPUTS.md)** · **[PyPI](PYPI.md)** |
| Full catalogue breadth and quantitative portfolio evidence | **[Projects](PROJECTS.md)** · **[Statistics](STATISTICS.md)** |
| University teaching and supporting material | **[Teaching](TEACHING.md)** |

---

## Professional and Academic Work

I am a data scientist and researcher with more than 15 years of experience across software, statistical modelling, machine learning, and data-intensive research. I have led data-science work in health technology and currently teach as an **Invited Assistant Professor at the Faculty of Media Arts and Design, Technical University of Porto (FMAD–UTP)**.

I am particularly interested in remote senior, lead, and principal-level work where statistical reasoning, engineering quality, and decision-making under uncertainty matter. I also collaborate on research, technical mentoring, and open-source scientific software.

For collaboration or professional enquiries, a short note describing the problem, constraints, and expected outcome is the best starting point. Longer-form technical writing and research notes live on my **[website](https://diogoribeiro7.github.io)**.

<div align="center">
  <a href="mailto:diogo.debastos.ribeiro@gmail.com">
    <img src="assets/links/email.svg" alt="Email Diogo Ribeiro" width="120" height="40" />
  </a>
  <a href="https://www.linkedin.com/in/diogo-ribeiro-9094604a/">
    <img src="assets/links/linkedin.svg" alt="LinkedIn profile" width="118" height="40" />
  </a>
  <a href="https://diogoribeiro7.github.io">
    <img src="assets/links/website.svg" alt="Personal website" width="118" height="40" />
  </a>
  <a href="https://orcid.org/0009-0001-2022-7072">
    <img src="assets/links/orcid.svg" alt="ORCID researcher profile" width="104" height="40" />
  </a>
  <a href="https://gitlab.com/DiogoRibeiro7">
    <img src="assets/links/gitlab.svg" alt="GitLab profile" width="104" height="40" />
  </a>
</div>
