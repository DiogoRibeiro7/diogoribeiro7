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

## Selected Work: From Problems to Tools

The mathematical formulation is the bridge between a practical problem and a useful software tool. These public projects illustrate what was modelled, what was built, and what that implementation makes possible. They are not presented as independent measurements of the commercial results from my industry career.

| Problem | Mathematical approach | Tool developed | Contribution |
| :-- | :-- | :-- | :-- |
| Feedback is unstructured and difficult to interrogate reliably | Retrieval relevance, grounded answer evaluation, and explicit quality and failure criteria | [feedback-intelligence-agent](https://github.com/DiogoRibeiro7/feedback-intelligence-agent): retrieval and guarded-generation service with FastAPI and observability | Makes feedback searchable through answers that can be checked against retrieved evidence. |
| Demand forecasts must support staffing decisions | Rolling-origin validation, probabilistic forecasts, conformal uncertainty and constrained resource allocation | [clinic-forecasting-platform](https://github.com/DiogoRibeiro7/clinic-forecasting-platform): forecasting, staffing optimisation, serving and monitoring | Connects predictive uncertainty to inspectable operational staffing decisions. |
| Housing changes and local-accommodation pressure are difficult to distinguish from spatial effects | Parish-level measurement, spatial autocorrelation, robust regression and sensitivity to influential observations | [lisbon-spatial-dynamics](https://github.com/DiogoRibeiro7/lisbon-spatial-dynamics): official-data spatial analysis pipeline | Makes associations and their limitations inspectable without asserting unsupported causality. |
| Population drift may be mistaken for model failure | Distribution comparisons, sample-size-aware thresholds, calibration and Monte Carlo experiments | [population-resemblance](https://github.com/DiogoRibeiro7/population-resemblance): statistical monitoring toolkit | Distinguishes evidence of changing populations from conclusions about model performance. |
| Tabular data errors are difficult to explain and audit | Pattern consistency, mixed-type constraints and interpretable anomaly evidence | [DataConsistencyChecker](https://github.com/DiogoRibeiro7/DataConsistencyChecker): explainable consistency-checking software | Connects flagged records to the checks and expectations they violate. |
| Survival-model evaluations need controlled ground truth | Event-history distributions, censoring, multistate processes and known-truth simulation | [genSurvPy](https://github.com/DiogoRibeiro7/genSurvPy): survival simulation library | Enables reproducible method comparisons where the data-generating mechanism is known. |
| Structural changes in time series require different detection assumptions | Bayesian, kernel, state-space, offline and online change detection | [ChangePointLab](https://github.com/DiogoRibeiro7/ChangePointLab): unified changepoint toolkit | Makes alternative change-detection methods accessible through a common research interface. |
| Scientific models must satisfy differential-equation constraints | Physics-informed optimisation, PDE residuals, boundary conditions and numerical benchmarks | [PINNLab](https://github.com/DiogoRibeiro7/pinn): PyTorch toolkit for forward and inverse PDE problems | Provides a testable framework for exploring neural approximations to constrained scientific problems. |

For a broader technical cross-section, see [Featured](FEATURED.md). For end-to-end accounts of constraints, methods and outcomes, see [Case Studies](CASE_STUDIES.md).

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
