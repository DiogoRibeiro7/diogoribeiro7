<div align="center">
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/README.md"><img src="https://img.shields.io/badge/Home-30363D?style=for-the-badge" alt="Home" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/FEATURED.md"><img src="https://img.shields.io/badge/Featured-30363D?style=for-the-badge" alt="Featured" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/PROJECTS.md"><img src="https://img.shields.io/badge/Projects-30363D?style=for-the-badge" alt="Projects" /></a>
  <img src="https://img.shields.io/badge/Methods-1F6FEB?style=for-the-badge" alt="Methods (current page)" />
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/RESEARCH.md"><img src="https://img.shields.io/badge/Research-30363D?style=for-the-badge" alt="Research" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/OUTPUTS.md"><img src="https://img.shields.io/badge/Outputs-30363D?style=for-the-badge" alt="Outputs" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/CASE_STUDIES.md"><img src="https://img.shields.io/badge/Case%20Studies-30363D?style=for-the-badge" alt="Case Studies" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/TEACHING.md"><img src="https://img.shields.io/badge/Teaching-30363D?style=for-the-badge" alt="Teaching" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/PYPI.md"><img src="https://img.shields.io/badge/PyPI-30363D?style=for-the-badge&logo=pypi&logoColor=white" alt="PyPI" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/STATISTICS.md"><img src="https://img.shields.io/badge/Statistics-30363D?style=for-the-badge" alt="Statistics" /></a>
</div>

---

# Methods

I do not start from a preferred algorithm. I start from the question, the data-generating process, the decision that follows from the estimate, and the failure modes that would make the result misleading.

My default sequence is:

1. define the estimand or decision target;
2. establish the simplest defensible baseline;
3. choose validation that matches the data-generating process;
4. quantify uncertainty, calibration and failure modes;
5. add complexity only when it improves the decision or the scientific claim;
6. make the result reproducible enough that another person can inspect the chain.

The sections below map common problem types to the modelling approaches I usually consider, the checks I care about, and public work where those choices are visible.

---

## Problem → method → evidence

| Problem | Default modelling direction | Reliability checks | Public evidence |
| :-- | :-- | :-- | :-- |
| **Probabilistic forecasting** | Classical time-series and state-space baselines first; global ML or foundation models only when they earn the additional complexity | rolling-origin evaluation, interval calibration, leakage checks, regime sensitivity, decision-level validation | [clinic-forecasting-platform](https://github.com/DiogoRibeiro7/clinic-forecasting-platform), [csp_forecast_package](https://github.com/DiogoRibeiro7/csp_forecast_package), [ds-projects-portfolio](https://github.com/DiogoRibeiro7/ds-projects-portfolio) |
| **Risk classification under asymmetric costs** | Calibrated probabilistic models and explicit operating thresholds rather than accuracy-first classification | temporal validation, class imbalance, calibration, cost curves, drift and threshold stability | [transaction-risk-lakehouse](https://github.com/DiogoRibeiro7/transaction-risk-lakehouse), [scania-aps-cost](https://github.com/DiogoRibeiro7/scania-aps-cost), [fastapi-ml-platform](https://github.com/DiogoRibeiro7/fastapi-ml-platform) |
| **Survival and event-history modelling** | Kaplan–Meier and Cox as structural baselines, then parametric, multistate or robust alternatives when the estimand requires them | censoring assumptions, calibration versus discrimination, known-truth simulation, model misspecification | [genSurvPy](https://github.com/DiogoRibeiro7/genSurvPy), [drl-cox](https://github.com/DiogoRibeiro7/drl-cox) |
| **Causal and policy questions** | Identification strategy before estimator; panel, event-study, synthetic-control or weighting methods chosen from design constraints | pre-trends, overlap, placebo and falsification tests, sensitivity to specification and measurement definitions | [portugal-minimum-wage-inflation](https://github.com/DiogoRibeiro7/portugal-minimum-wage-inflation), [gdp-wage-transmission](https://github.com/DiogoRibeiro7/gdp-wage-transmission), [causal-uplift-marketing-campaign](https://github.com/DiogoRibeiro7/causal-uplift-marketing-campaign) |
| **Configurational / comparative inference** | csQCA or fsQCA when conjunctural causation and equifinality are part of the question | calibration sensitivity, consistency and coverage, exact minimisation, cross-checks against reference implementations | [setqca](https://github.com/DiogoRibeiro7/setqca-python), [europe-fsqca-innovation](https://github.com/DiogoRibeiro7/europe-fsqca-innovation) |
| **Anomaly, change and failure detection** | Robust statistical or change-point methods first; representation learning only when the signal structure justifies it | false-alarm control, rare-event behaviour, contamination robustness, shift sensitivity, abstention | [anomalybench](https://github.com/DiogoRibeiro7/anomalybench), [behavioral-sensing-research](https://github.com/DiogoRibeiro7/behavioral-sensing-research), [PSOD](https://github.com/DiogoRibeiro7/PSOD) |
| **RAG / LLM systems** | Retrieval quality and task-grounded evaluation before prompt complexity or agent orchestration | groundedness, retrieval recall, execution accuracy, regression suites, prompt injection and PII controls, tracing and cost | [feedback-intelligence-agent](https://github.com/DiogoRibeiro7/feedback-intelligence-agent), [ragops-lab](https://github.com/DiogoRibeiro7/ragops-lab), [qwen-text2sql-lab](https://github.com/DiogoRibeiro7/qwen-text2sql-lab) |
| **Optimisation and decision systems** | Separate prediction from policy; formulate the actual constraints and objective explicitly | feasibility, sensitivity to forecasts and costs, scenario stress tests, out-of-sample decision quality | [energy-system-simulator](https://github.com/DiogoRibeiro7/energy-system-simulator), [perishable-inventory-decision-lab](https://github.com/DiogoRibeiro7/perishable-inventory-decision-lab), [rcpsp_cf_ivfth](https://github.com/DiogoRibeiro7/rcpsp_cf_ivfth) |
| **Scientific machine learning** | Exact or numerical baseline first; neural approximations only when they solve a real computational or inverse problem | known-solution benchmarks, discretisation error, convergence, sensitivity to sampling and optimisation | [pinn](https://github.com/DiogoRibeiro7/pinn), [pinn-rk](https://github.com/DiogoRibeiro7/pinn-rk), [oisst-fourier-neural-operator](https://github.com/DiogoRibeiro7/oisst-fourier-neural-operator) |
| **Research software and statistical methods** | Explicit mathematical contract, typed API, reference tests and reproducible release process | deterministic fixtures, property tests, cross-implementation validation, package metadata and release gates | [genSurvPy](https://github.com/DiogoRibeiro7/genSurvPy), [setqca](https://github.com/DiogoRibeiro7/setqca-python), [industrialstats](https://github.com/DiogoRibeiro7/industrialstats), [heavytails](https://github.com/DiogoRibeiro7/heavytails) |

---

## How I choose models

### Start with the estimand

Before fitting anything, I want to know what quantity the model is supposed to estimate or what decision it is meant to support. A ranking problem, a calibrated probability problem and a resource-allocation problem can all use the same input data and still require different models, losses and validation.

### Match validation to the data-generating process

Random cross-validation is not a default when time, groups, censoring or treatment assignment matter. I use blocked, grouped, nested or rolling-origin designs when those structures are part of the problem. For simulation studies, I prefer known-truth designs that let bias, coverage and failure probability be measured directly.

### Prefer interpretable structure when performance is comparable

Linear, generalized linear, state-space, survival, rule-based and optimisation models remain strong defaults when their assumptions are defensible. More complex models need to demonstrate an empirical gain that matters to the final decision, not just a better benchmark score.

### Treat uncertainty as part of the model

Prediction intervals, posterior uncertainty, conformal coverage, calibration, decision thresholds and abstention are not presentation layers. They determine what the system is allowed to claim or do.

### Make failure visible

I care about leakage, missing evidence, distribution shift, contamination, weak overlap, unstable thresholds, bad calibration and external-service failure. In production systems, observability and structured failure modes matter as much as the central model.

---

## Reliability toolkit

| Reliability question | Typical checks |
| :-- | :-- |
| **Can the validation be trusted?** | leakage-safe pipelines, grouped or temporal splits, nested CV, rolling-origin backtests, frozen test sets |
| **Are probabilities meaningful?** | reliability curves, Brier/log loss, Platt or isotonic calibration, interval coverage, calibration by subgroup |
| **Does the result survive shift?** | PSI, KS, MMD, regime analysis, sensitivity grids, source–target overlap checks |
| **Does class imbalance distort the conclusion?** | PR curves, class weighting, resampling audits, cost-sensitive metrics, threshold curves |
| **Is the model actually helping the decision?** | explicit utility or cost functions, optimisation downstream of forecasts, policy simulation, scenario stress tests |
| **Can someone reproduce the claim?** | typed code, frozen configurations, tests, CI, provenance, machine-readable outputs, package/release metadata |

---

## Engineering principles

The same modelling discipline carries into software:

- typed Python where practical;
- explicit interfaces between data, model, decision and reporting layers;
- reproducible environments and dependency management;
- `pytest`, static typing and linting in CI;
- structured outputs rather than fragile free text when systems integrate with other systems;
- observability, retries, timeouts and failure semantics for production services;
- versioned artifacts and release gates for research software.

Common tools include Python, SQL, R, C/C++, Fortran, NumPy, Pandas, Polars, scikit-learn, Statsmodels, PyMC, PyTorch, TensorFlow, Pyomo, Spark, Flink, Kafka, FastAPI, PostgreSQL/PostGIS, MongoDB, AWS services, Docker, Poetry and GitHub Actions.

---

<details>
<summary><strong>Technical reference — model families and methods</strong></summary>

<br>

### Supervised learning

OLS/GLS, Ridge, Lasso, Elastic Net, GLMs, robust regression, quantile regression, GAMs and splines, mixed-effects models, Gaussian processes, Bayesian regression, logistic regression, SVMs, k-NN, trees, random forests, gradient boosting, CatBoost/XGBoost/LightGBM and neural networks.

### Unsupervised and representation learning

k-means, hierarchical clustering, DBSCAN/HDBSCAN, Gaussian mixtures, fuzzy c-means, PCA/SVD, t-SNE, UMAP, density estimation, Isolation Forest, LOF, One-Class SVM, autoencoders and persistent-homology methods.

### Time series and event data

ARIMA/SARIMAX, ETS, Prophet, state-space and structural models, singular spectrum analysis, global gradient-boosting models, foundation models such as Chronos, conformal intervals, change-point detection, Kaplan–Meier, Cox PH, parametric AFT and multistate survival models.

### Causal, comparative and experimental methods

IPW/AIPW, uplift and heterogeneous-treatment-effect models, difference-in-differences, event studies, synthetic control, A/B testing, power analysis, variance reduction, csQCA/fsQCA and exact Boolean minimisation.

### Optimisation and decision modelling

MILP, unit commitment and dispatch, inventory and replenishment policy, project scheduling, fuzzy constraints, cost-weighted threshold optimisation and scenario analysis.

### Deep learning, LLMs and scientific ML

Transformers, recurrent and convolutional sequence models, LoRA/QLoRA, RAG, reranking, structured generation, agent/tool orchestration, LLM evaluation, PINNs, Runge–Kutta PINNs, neural operators, finite-difference and spectral PDE methods.

### Robustness, calibration and monitoring

Conformal prediction, Bayesian uncertainty, Platt and isotonic calibration, leakage audits, drift detection, class-imbalance methods, cost curves, selective prediction and abstention, SHAP, permutation importance, PDP/ICE and counterfactual explanations.

</details>

---

Working examples are indexed in **[Featured](FEATURED.md)**, **[Case Studies](CASE_STUDIES.md)** and the broader **[Projects](PROJECTS.md)** catalogue.

<div align="center">
  <a href="https://github.com/DiogoRibeiro7"><img src="https://img.shields.io/badge/%E2%86%90%20Back%20to%20profile-30363D?style=for-the-badge" alt="Back to profile" /></a>
</div>
