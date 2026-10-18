# Diogo Ribeiro (@DiogoRibeiro7)

**Lead Data Scientist · Statistical Modelling & Research · Invited Assistant Professor**  
**Statistical ML · Time Series · Causal Inference · Applied AI · Research Software**  

20 years in software, statistical modelling and data science · Technical leadership, decision systems and reproducible research

<div align="center">
  <img src="assets/links/nav-home-active.svg" alt="Home (current page)" width="96" height="40" />
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/FEATURED.md"><img src="assets/links/nav-featured.svg" alt="Featured" width="116" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/PROJECTS.md"><img src="assets/links/nav-projects.svg" alt="Projects" width="112" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/METHODS.md"><img src="assets/links/nav-methods.svg" alt="Methods" width="112" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/RESEARCH.md"><img src="assets/links/nav-research.svg" alt="Research" width="120" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/STATISTICS.md"><img src="assets/links/nav-evidence.svg" alt="Evidence" width="120" height="40" /></a>
</div>

Over 20 years working across software engineering, statistical modelling and data science, I have designed and led work that connects analytical methods to operational decisions. My focus is on problems where defining the estimand, choosing a decision rule, quantifying uncertainty and maintaining reproducible evidence matter as much as model fitting.

My default is not “use more ML.” It is to start from the problem, the evidence, and the decision being supported; establish strong statistical or mathematical baselines; and add complexity only when it earns its place empirically.

## Start Here

Different readers can inspect different kinds of evidence without having to work through the entire repository catalogue.

| Reader | Start with | What to evaluate |
| :-- | :-- | :-- |
| **Technical recruiters and hiring teams** | [Featured Projects](FEATURED.md) · [Case Studies](CASE_STUDIES.md) | System architecture, modelling decisions, technical leadership and the boundaries of demonstrated results. |
| **Research collaborators and scientific reviewers** | [Research](RESEARCH.md) · [Methods](METHODS.md) · [Outputs](OUTPUTS.md) | Research questions, identification assumptions, known-truth validation, methodological limits and available artifacts. |
| **Senior consulting clients** | [Case Studies](CASE_STUDIES.md) · [Methods](METHODS.md) · [Professional impact](STATISTICS.md#delivered-impact) | Problem formulation, operational constraints, decisions supported, and clearly identified professional outcomes. |

---

## Industry Systems and Problem-Solving

My professional work includes internal systems developed for operational use, distinct from the public research and engineering repositories below. The underlying employer code and commercial data are not published here.

| Operational problem | Mathematical and engineering approach | Tool or system developed | What it enabled |
| :-- | :-- | :-- | :-- |
| Distinguishing genuine behavioural changes from unreliable sensor readings | Time-series change detection, sensor evidence quality, missingness and uncertainty-aware decision rules | Behavioural sensing and alerting logic combining in-home signals | Helped separate changes in observed behaviour from missing or ambiguous evidence before alerts were raised |
| Turning heterogeneous home and wearable measurements into usable information | Event-time validation, data consistency, signal processing and integration of multiple sources | Sensor-data ingestion and analytical pipelines | Produced structured observations for downstream monitoring and analysis |
| Explaining longitudinal patterns to care and product users | Statistical summaries, time-dependent interpretation and controlled natural-language generation | Automated weekly reporting workflows | Translated analytical results into recurring, interpretable reports |
| Estimating activity and location from indirect wireless signals | Received-signal-strength analysis, probabilistic modelling and spatial uncertainty | RSSI-based localisation and activity-inference components | Supported inference from imperfect sensor observations instead of relying on deterministic thresholds alone |

### Mathematical decisions behind the systems

Two examples illustrate why implementing a model is not the same as solving the operational problem.

**Behavioural sensing — when does an observed change justify an alert?** A change in a sensor signal is not necessarily a change in behaviour: missing observations, unreliable readings and uncertain occupancy can produce similar patterns. The modelling task therefore includes defining usable evidence, distinguishing observation quality from behavioural change, and deciding when uncertainty warrants withholding a behavioural conclusion. The key trade-off is between generating more alerts and making alerts sufficiently defensible for downstream care decisions. This is a decision-system problem, not merely a changepoint-detection problem.

**RSSI-based inference — what can an indirect radio signal tell us about location?** Received signal strength varies with obstacles, device placement and the surrounding environment. A fixed signal-to-location mapping would obscure uncertainty and environmental variation. Probabilistic spatial modelling, including Gaussian-process approaches, provides a way to represent the relationship between signal strength and location together with uncertainty. The engineering challenge is to make those estimates usable within a sensing pipeline while retaining their limitations, rather than presenting an inferred location as a direct observation.

These descriptions focus on the mathematical and engineering considerations behind the work. They do not disclose proprietary model specifications, assert an unverified production comparison, or claim that a particular choice achieved a measured improvement.

These descriptions concern the purpose and design of professional systems, not open-source releases or independently reproducible claims about employer outcomes. For publicly inspectable implementations of related ideas, see the projects below.

---

## Selected Work: Problems, Mathematics and Tools

The mathematical formulation connects a real problem with a working tool. These projects show what was built and what it makes possible—not independently measured commercial outcomes.

### [Feedback intelligence agent](https://github.com/DiogoRibeiro7/feedback-intelligence-agent)
- **Problem:** Customer feedback is difficult to search and interpret reliably.
- **Mathematics:** Retrieval relevance, grounded-answer evaluation, quality and failure criteria.
- **Tool and contribution:** A guarded RAG service with FastAPI and observability, enabling answers to be inspected against retrieved evidence.

### [Clinic forecasting platform](https://github.com/DiogoRibeiro7/clinic-forecasting-platform)
- **Problem:** Uncertain healthcare demand must inform staffing.
- **Mathematics:** Rolling-origin evaluation, probabilistic forecasts, conformal intervals and resource constraints.
- **Tool and contribution:** A forecasting and staffing-optimisation platform that connects uncertainty to operational decisions.

### [Lisbon spatial dynamics](https://github.com/DiogoRibeiro7/lisbon-spatial-dynamics)
- **Problem:** Housing-value changes and local-accommodation pressure may be confounded by geography.
- **Mathematics:** Spatial autocorrelation, robust regression and influence sensitivity.
- **Tool and contribution:** An official-data analysis pipeline that exposes associations and their limits without claiming causality.

### [Population resemblance](https://github.com/DiogoRibeiro7/population-resemblance)
- **Problem:** Population shift can be mistaken for predictive-model failure.
- **Mathematics:** Distribution comparison, sample-size-aware thresholds and Monte Carlo calibration.
- **Tool and contribution:** A statistical monitoring toolkit that separates evidence of drift from claims about model performance.

### [DataConsistencyChecker](https://github.com/DiogoRibeiro7/DataConsistencyChecker)
- **Problem:** Data-quality failures need explanations rather than opaque scores.
- **Mathematics:** Pattern consistency, mixed-type constraints and interpretable anomaly evidence.
- **Tool and contribution:** A consistency-checking library that links unusual records to violated expectations.

### [genSurvPy](https://github.com/DiogoRibeiro7/genSurvPy)
- **Problem:** Survival estimators require validation against controlled ground truth.
- **Mathematics:** Event-history simulation, censoring and multistate processes.
- **Tool and contribution:** A simulation library for reproducible method comparisons with known generating mechanisms.

### [ChangePointLab](https://github.com/DiogoRibeiro7/ChangePointLab)
- **Problem:** Structural changes in time series require distinct detection assumptions.
- **Mathematics:** Bayesian, kernel, state-space, offline and online changepoint methods.
- **Tool and contribution:** A unified toolkit for comparing detection approaches through a shared interface.

### [PINNLab](https://github.com/DiogoRibeiro7/pinn)
- **Problem:** Scientific model approximations must respect differential-equation constraints.
- **Mathematics:** PDE residuals, boundary conditions and physics-informed optimisation.
- **Tool and contribution:** A PyTorch framework for evaluating neural approaches to forward and inverse PDE problems.

See [Featured](FEATURED.md) for more projects and [Case Studies](CASE_STUDIES.md) for detailed problem-to-outcome narratives.

---

## Portfolio at a Glance

<!-- readme:portfolio-snapshot:start -->
| Evidence | Current scope |
| :-- | --: |
| Manifest-backed public projects | **43** |
| Substantial outputs | **39** |
| Published PyPI packages | **11** |
| Case studies | **16 across 14 domains** |
| Real-data / empirical projects | **25 / 43 (58%)** |
| Curated flagship repositories | **12** |
<!-- readme:portfolio-snapshot:end -->

These figures are generated from the same canonical portfolio data used by [Statistics](STATISTICS.md), so the front page and the detailed evidence page share one source of truth.

**Reported outcomes from professional delivery:** 80% reduction in reporting costs · 30% reduction in analytics processing time · €500K reduction in inventory value through forecasting and operational optimisation. These figures refer to industry work, not measured results from the public GitHub projects; underlying commercial baselines are not published here.

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

My work spans statistical modelling, time series, causal inference, optimisation, behavioural sensing, data engineering and applied AI. The common discipline is to:

- **Define the question and decision first.** Specify the estimand, constraints, assumptions and consequences of a wrong decision before choosing an algorithm.
- **Earn model complexity through evidence.** Start from mathematical and statistical baselines; compare alternatives using validation that respects time, grouping, censoring and other data-generating structure.
- **Make uncertainty and failure explicit.** Evaluate calibration, missing evidence, drift, leakage, abstention and operating thresholds, not only aggregate scores.
- **Keep the result inspectable.** Use tests, provenance, frozen configurations and reproducible outputs, with enough detail to examine the claim and its limitations.

The detailed reasoning, methods and supporting projects are in [Methods](METHODS.md) and [Case Studies](CASE_STUDIES.md).

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
| What qualifies for the canonical portfolio and why | **[Portfolio Policy](PORTFOLIO_POLICY.md)** |
| University teaching and supporting material | **[Teaching](TEACHING.md)** |

---

## Professional and Academic Work

My background combines mathematics, software engineering and statistical research. I have led data-science work in health technology, including sensor-based behavioural analysis, time-series modelling and decision-support systems. Alongside industry work, I teach as an **Invited Assistant Professor at the Faculty of Media Arts and Design, Technical University of Porto (FMAD–UTP)**.

I am particularly interested in remote senior, lead, and principal-level work where statistical reasoning, engineering quality, and decision-making under uncertainty matter. I also collaborate on research, technical mentoring, and open-source scientific software.

For collaboration or professional enquiries, a short note describing the problem, constraints, and expected outcome is the best starting point. Longer-form technical writing and research notes live on my **[website](https://diogoribeiro7.github.io)** and **[Medium](https://medium.com/@diogo-ribeiro-1975)**.

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
  <a href="https://medium.com/@diogo-ribeiro-1975">
    <img src="assets/links/medium.svg" alt="Medium writing profile" width="104" height="40" />
  </a>
  <a href="https://orcid.org/0009-0001-2022-7072">
    <img src="assets/links/orcid.svg" alt="ORCID researcher profile" width="104" height="40" />
  </a>
  <a href="https://gitlab.com/DiogoRibeiro7">
    <img src="assets/links/gitlab.svg" alt="GitLab profile" width="104" height="40" />
  </a>
</div>
