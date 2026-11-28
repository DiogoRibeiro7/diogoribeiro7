<div align="center">
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/README.md"><img src="assets/links/nav-home.svg" alt="Home" width="96" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/FEATURED.md"><img src="assets/links/nav-featured.svg" alt="Featured" width="116" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/PROJECTS.md"><img src="assets/links/nav-projects.svg" alt="Projects" width="112" height="40" /></a>
  <img src="assets/links/nav-methods-active.svg" alt="Methods (current page)" width="112" height="40" />
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/RESEARCH.md"><img src="assets/links/nav-research.svg" alt="Research" width="120" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/STATISTICS.md"><img src="assets/links/nav-evidence.svg" alt="Evidence" width="120" height="40" /></a>
</div>

---

# Methods

I start from the question, the data-generating process, the decision that follows from the estimate, and the failure modes that would make the result misleading, not from a preferred algorithm.

1. Define the estimand or decision target; for causal questions, state identification assumptions before the estimator.
2. Establish the simplest defensible baseline.
3. Choose validation that matches the data-generating process (time, groups, censoring, space, assignment).
4. Quantify uncertainty, calibration and failure modes.
5. Add complexity only if it improves the decision or the scientific claim.
6. Make the chain reproducible.

## Problem → method → evidence

| Problem | Approach and checks | Public evidence |
| :-- | :-- | :-- |
| **Probabilistic forecasting** | Classical and state-space baselines first; global ML or foundation models only if they earn it. Checks: rolling-origin evaluation, interval calibration, leakage, decision-level validation. | [clinic-forecasting-platform](https://github.com/DiogoRibeiro7/clinic-forecasting-platform), [csp_forecast_package](https://github.com/DiogoRibeiro7/csp_forecast_package), [ds-projects-portfolio](https://github.com/DiogoRibeiro7/ds-projects-portfolio) |
| **Risk classification, asymmetric costs** | Calibrated probabilities and explicit thresholds, not accuracy-first. Checks: temporal validation, imbalance, cost curves, threshold stability. | [transaction-risk-lakehouse](https://github.com/DiogoRibeiro7/transaction-risk-lakehouse), [scania-aps-cost](https://github.com/DiogoRibeiro7/scania-aps-cost), [fastapi-ml-platform](https://github.com/DiogoRibeiro7/fastapi-ml-platform) |
| **Survival and event history** | Kaplan–Meier and Cox as baselines; parametric or multistate when the estimand needs it. Checks: censoring assumptions, calibration vs discrimination, known-truth simulation. | [genSurvPy](https://github.com/DiogoRibeiro7/genSurvPy), [drl-cox](https://github.com/DiogoRibeiro7/drl-cox) |
| **Causal and policy questions** | Identification before estimation: DiD, synthetic control, RDD, IV, matching or doubly robust, chosen from the assignment mechanism. Checks: parallel trends, overlap, instruments, placebo and negative controls. | [portugal-minimum-wage-inflation](https://github.com/DiogoRibeiro7/portugal-minimum-wage-inflation), [gdp-wage-transmission](https://github.com/DiogoRibeiro7/gdp-wage-transmission), [effectbridge](https://github.com/DiogoRibeiro7/effectbridge), [causal-uplift-marketing-campaign](https://github.com/DiogoRibeiro7/causal-uplift-marketing-campaign) |
| **Configurational inference** | csQCA or fsQCA when conjunctural causation matters. Checks: calibration sensitivity, consistency and coverage, reference-implementation cross-checks. | [setqca](https://github.com/DiogoRibeiro7/setqca-python), [europe-fsqca-innovation](https://github.com/DiogoRibeiro7/europe-fsqca-innovation) |
| **Drift, changepoints, failure detection** | Separate gradual shift, abrupt change, anomalies and missing evidence before choosing a detector. Checks: threshold calibration, false alarms, sample-size sensitivity, abstention. | [population-resemblance](https://github.com/DiogoRibeiro7/population-resemblance), [ChangePointLab](https://github.com/DiogoRibeiro7/ChangePointLab), [behavioral-sensing-research](https://github.com/DiogoRibeiro7/behavioral-sensing-research), [anomalybench](https://github.com/DiogoRibeiro7/anomalybench) |
| **RAG and LLM systems** | Retrieval quality and task-grounded evaluation before prompt or agent complexity. Checks: groundedness, recall, regression suites, injection and PII controls, tracing and cost. | [feedback-intelligence-agent](https://github.com/DiogoRibeiro7/feedback-intelligence-agent), [ragops-lab](https://github.com/DiogoRibeiro7/ragops-lab), [qwen-text2sql-lab](https://github.com/DiogoRibeiro7/qwen-text2sql-lab) |
| **Optimisation and decisions** | Separate prediction from policy; state constraints and objective explicitly. Checks: feasibility, sensitivity to forecasts and costs, stress tests. | [energy-system-simulator](https://github.com/DiogoRibeiro7/energy-system-simulator), [perishable-inventory-decision-lab](https://github.com/DiogoRibeiro7/perishable-inventory-decision-lab), [rcpsp_cf_ivfth](https://github.com/DiogoRibeiro7/rcpsp_cf_ivfth) |
| **Scientific machine learning** | Exact or numerical baseline first; neural approximation only for a real computational or inverse problem. Checks: known-solution benchmarks, discretisation error, convergence. | [pinn](https://github.com/DiogoRibeiro7/pinn), [pinn-rk](https://github.com/DiogoRibeiro7/pinn-rk), [oisst-fourier-neural-operator](https://github.com/DiogoRibeiro7/oisst-fourier-neural-operator) |
| **Spatial and small-area analysis** | Validated geography first; descriptive spatial statistics before regression or causal reading. Checks: boundary consistency, autocorrelation, influence, leave-one-area-out. | [lisbon-spatial-dynamics](https://github.com/DiogoRibeiro7/lisbon-spatial-dynamics) |
| **Data quality and research data** | Data contracts, provenance and interpretable consistency checks before modelling. Checks: schema validation, checksums, lineage, duplicates, quarantine of unverified material. | [DataConsistencyChecker](https://github.com/DiogoRibeiro7/DataConsistencyChecker), [data](https://github.com/DiogoRibeiro7/data) |
| **Research software** | Explicit mathematical contract, typed API, reference tests, reproducible releases. Checks: property tests, known-truth simulation, cross-implementation validation, release gates. | [genSurvPy](https://github.com/DiogoRibeiro7/genSurvPy), [setqca](https://github.com/DiogoRibeiro7/setqca-python), [ChangePointLab](https://github.com/DiogoRibeiro7/ChangePointLab), [population-resemblance](https://github.com/DiogoRibeiro7/population-resemblance), [DataConsistencyChecker](https://github.com/DiogoRibeiro7/DataConsistencyChecker) |

## Principles

- **Prediction is not intervention.** A conditional distribution, a treatment effect and an optimal action need different targets and evaluation; predictive accuracy cannot identify counterfactuals.
- **Respect dependence.** Use blocked, grouped, nested or rolling-origin validation when time, groups, censoring or space matter; prefer known-truth simulation for method studies.
- **Prefer interpretable structure at comparable performance.** Complex models must show a gain that matters to the decision.
- **Uncertainty is part of the model.** Intervals, calibration, thresholds and abstention determine what a system may claim or do.
- **Make failure visible.** Leakage, missing evidence, shift, weak overlap, unstable thresholds and service failures.

## Engineering

Typed Python, explicit interfaces between data, model, decision and reporting, reproducible environments, `pytest`/typing/linting in CI, structured outputs, observability and failure semantics for services, versioned artifacts and release gates for research software.

Common tools include Python, SQL, R, C/C++, Fortran, NumPy, Pandas, Polars, scikit-learn, Statsmodels, PyMC, PyTorch, TensorFlow, Pyomo, Spark, Flink, Kafka, FastAPI, PostgreSQL/PostGIS, MongoDB, AWS services, Docker, Poetry, GitHub Actions and GitLab CI.

---

<details>
<summary><strong>Technical reference — model families and methods</strong></summary>

<br>

### Supervised learning

OLS/GLS, Ridge, Lasso, Elastic Net, GLMs, robust regression, quantile regression, GAMs and splines, mixed-effects models, Gaussian processes, Bayesian regression, logistic regression, SVMs, k-NN, trees, random forests, gradient boosting, CatBoost/XGBoost/LightGBM and neural networks.

### Unsupervised and representation learning

k-means, hierarchical clustering, DBSCAN/HDBSCAN, Gaussian mixtures, fuzzy c-means, PCA/SVD, t-SNE, UMAP, density estimation, Isolation Forest, LOF, One-Class SVM, autoencoders and persistent-homology methods.

### Time series and event data

ARIMA/SARIMAX, ETS, state-space and structural models, singular spectrum analysis, Gaussian processes, global gradient-boosting models, foundation models such as Chronos, conformal intervals, PELT, BOCPD, kernel and nonparametric changepoint methods, Kaplan–Meier, Cox PH, parametric AFT and multistate survival models.

### Causal, comparative and experimental methods

potential outcomes and explicit estimands, matching, IPW/AIPW, outcome regression, heterogeneous-treatment-effect models, difference-in-differences, event studies, synthetic control, RDD, IV/2SLS, interrupted time series, A/B testing, CUPED, power analysis, variance reduction, csQCA/fsQCA and exact Boolean minimisation.

### Optimisation and decision modelling

MILP, unit commitment and dispatch, inventory and replenishment policy, project scheduling, fuzzy constraints, cost-weighted threshold optimisation and scenario analysis.

### Deep learning, LLMs and scientific ML

Transformers, recurrent and convolutional sequence models, LoRA/QLoRA, RAG, reranking, structured generation, agent/tool orchestration, LLM evaluation, PINNs, Runge–Kutta PINNs, neural operators, finite-difference and spectral PDE methods.

### Spatial, robustness, calibration and monitoring

Moran's I and LISA, robust and influence-aware regression, spatial sensitivity analysis, conformal prediction, Bayesian uncertainty, Platt and isotonic calibration, leakage audits, PRS/PSI/KS drift diagnostics, changepoint detection, class-imbalance methods, cost curves, selective prediction and abstention, SHAP, permutation importance, PDP/ICE and counterfactual explanations.

### Data quality and research-data controls

Typed or schema-validated inputs, metadata contracts, provenance records, SHA-256 integrity checks, deterministic transformations, lineage, duplicate detection, interpretable consistency checks, explicit canonical/external/legacy data states and immutable references for reproducible consumers.

</details>

---

Examples: **[Featured](FEATURED.md)** · **[Case Studies](CASE_STUDIES.md)** · **[Projects](PROJECTS.md)**

<div align="center">
  <a href="https://github.com/DiogoRibeiro7"><img src="https://img.shields.io/badge/%E2%86%90%20Back%20to%20profile-30363D?style=for-the-badge" alt="Back to profile" /></a>
</div>
