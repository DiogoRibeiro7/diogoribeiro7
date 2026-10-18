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

## From Economic Problems to Mathematical Tools

My work starts with problems that have operational or economic consequences: resources being allocated inefficiently, forecasts that do not support decisions, unreliable information, avoidable process costs, and risks that are poorly understood. Mathematics provides a way to express these problems precisely. Software turns those formulations into tools that can be used, evaluated and improved.

The value of a model is therefore not the algorithm itself, but the decision or process it enables:

- **Costs, waste and scarce resources.** Forecasting and constrained optimisation connect uncertain demand to staffing, inventory, scheduling and resource-allocation decisions. The economic question is not simply whether a forecast is accurate, but whether using it leads to a better decision under real constraints.
- **Commercial and operational risk.** Probabilistic modelling, calibration and explicit loss functions make the consequences of different errors visible. Decision thresholds should reflect the costs of false alarms, missed events and unnecessary intervention.
- **Productivity and analytical infrastructure.** Data integration, validation and automation reduce manual reconciliation and make information more consistent and usable. The purpose is to support more reliable decisions and free effort for higher-value work.
- **Measurement of economic effects.** Statistics, econometrics and causal inference help distinguish correlations from effects that could justify a business or policy decision. Assumptions, counterfactuals and uncertainty matter because acting on the wrong conclusion has a cost.
- **Reliable operational monitoring.** Statistical change detection and evidence-quality rules help distinguish genuine events from noise and unreliable observations, avoiding decisions driven by misleading signals.

### Manufacturing, supply chain and industrial operations — Grupo Piedade

At Grupo Piedade, I worked across production management, demand planning, materials, warehousing, logistics and customer-service operations. The objective was to turn operational uncertainty into practical planning tools, not simply to improve a model score.

- **Demand forecasting and production planning.** Developed statistical and predictive models for demand across 60 products and 80 international customers. Forecasts informed capacity planning, production scheduling, material requirements and responses to customer orders, connecting time-series modelling with operational decisions.
- **Inventory and logistics analytics.** Built tools to study stock coverage, delivery lead times, forecast-versus-actual demand and logistics costs, supporting purchasing, replenishment, warehousing and dispatch decisions. Moving reporting and data management from spreadsheets into SQL made operational information more consistent and reusable.
- **Manufacturing process and quality.** Used deterministic and stochastic mathematical models of heat transfer, including partial differential equations, to study thermal behaviour during cork disinfection. The contribution was to understand process variability and its implications for production conditions and quality assurance, rather than treating process settings as arbitrary constants.

Reported outcomes from that professional work include a 12% improvement in forecast accuracy, a 40% reduction in inventory days, approximately €500K less inventory value, 25% less obsolete inventory and an 18% reduction in logistics costs. These are historical industry results; the underlying commercial data and measurement baselines are not published in this repository.

The work illustrates the connection between mathematical modelling, tools used by operational teams, and business decisions with economic consequences.

In each case, the work follows a common sequence: **define the economic or operational objective, formulate the mathematical problem, build the appropriate tool, and evaluate the decisions it supports**. A technically sophisticated implementation is not automatically valuable; its contribution must be judged in the context of the problem it addresses.

My earlier work in behavioural sensing and wireless-signal inference is one application of this approach, not its defining industry. Some commercial systems and measurements remain proprietary. The public projects below demonstrate related methods and software without implying that they reproduce employer systems or their reported business outcomes.

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
