## Diogo Ribeiro
**Lead Data Scientist • AI Engineer • Professor • Mathematical Engineer — working between the United Kingdom and Portugal**

> "Knowledge is knowing a tomato is a fruit; wisdom is not putting it in a fruit salad."
> — Miles Kington

I build production systems that turn complex data into reliable decisions, and reproducible research pipelines that turn open data into auditable evidence. My work spans end-to-end AI systems (LLMs, RAG, and agents), forecasting and anomaly detection, and a growing body of econometric and dynamical-systems research on inequality, wealth, and public policy. Across all of it the constants are the same: lean models, robust software practice, and results you can reproduce and defend.

<p align="center">
  <img src="data_has_a_better_idea.png"
       alt="Poster with the phrase 'Data has a better idea'"
       title="Data has a better idea"
       width="75%" />
</p>

---

## Quick Navigation

- [What I Work On](#what-i-work-on)
- [Technical Skills](#technical-skills)
- [Modelling Toolbox](#modelling-toolbox)
- [Current Focus](#current-focus)
- [Selected Work](#selected-work)
  - [Production AI & LLM Systems](#production-ai--llm-systems)
  - [ML Engineering & MLOps](#ml-engineering--mlops)
  - [Data Engineering & Streaming](#data-engineering--streaming)
  - [Statistical & Applied Data Science](#statistical--applied-data-science)
  - [Economics, Inequality & Policy Research](#economics-inequality--policy-research)
  - [Mathematical Methods & Algorithms](#mathematical-methods--algorithms)
  - [Live Dashboards](#live-dashboards)
- [Research Interests](#research-interests)
- [Collaboration Interests](#collaboration-interests)
- [Teaching](#teaching)
- [GitHub Stats](#github-stats)
- [Let's Connect and Collaborate](#lets-connect-and-collaborate)

---

## What I Work On

- **Production AI & LLM systems**  
  RAG pipelines, agentic workflows, structured outputs, evaluation loops, and audit-friendly narrative reporting — designed for reliability, observability, and CI from the start.
- **Data science & statistical modelling**  
  The full toolkit — supervised and unsupervised learning, causal inference and experimentation (uplift, synthetic control, RCT-vs-observational tests), survival and event-history analysis, Bayesian and probabilistic modelling, and robust/heavy-tailed statistics. With a working emphasis on the parts most people skip: uncertainty quantification and calibration, class imbalance, interpretability and fairness, leakage and drift checks, and honest model selection under real-world noise.
- **Forecasting & anomaly detection**  
  Classical and foundation-model time series (SARIMAX/Prophet through Chronos and masked-patch transformers), conformal prediction intervals, change-point and rare-event detection, and drift monitoring for operational and sensor-driven systems.
- **Econometrics & reproducible policy research**  
  Panel and causal models, event studies, synthetic control, and Monte Carlo simulation over open economic data (Eurostat, OECD, AMECO, WID, INE/PORDATA, FRED).
- **Dynamical systems & mathematical modelling**  
  Attractor dynamics, dynamical-systems econometrics, extreme-value and rare-event methods, and exact algorithmic solvers.
- **Data & ML engineering**  
  Contract-linked ingestion, dataset curation, streaming and lakehouse patterns, and reproducible project scaffolding.

---

## Technical Skills

- **Programming** — Python (typed, NumPy-first), SQL, R, TypeScript, Bash/Zsh, C, Fortran
- **AI / LLM** — RAG, agent orchestration, structured outputs, evaluation harnesses; HuggingFace fine-tuning; prompt contracts and audit trails
- **ML / Data** — NumPy, Pandas, Polars, FireDucks; scikit-learn, XGBoost/LightGBM; PyTorch, TensorFlow; Statsmodels, PyMC, Pyomo  
  _Focus:_ time series, anomaly detection, GLMs/IRLS, robust and Bayesian statistics, causal inference
- **Data Eng & Streaming** — Apache Kafka, Flink, Spark, Databricks; Arrow/Parquet; Apache Iceberg (lakehouse)
- **Cloud & Storage** — AWS S3, DynamoDB; PostgreSQL/PostGIS, MySQL, SQLite; MongoDB, InfluxDB, TimescaleDB
- **DevEx & CI/CD** — Docker; GitHub Actions (incl. custom/composite actions), Jenkins; Poetry; pre-commit (ruff, mypy, pytest-cov); semantic versioning
- **Testing & Quality** — pytest, coverage, property-based tests (hypothesis); static typing; security linting (bandit)

---

## Modelling Toolbox

The model families I reach for, organised by task. I choose for interpretability and calibration first, then accuracy — and I benchmark rather than assume.

- **Regression** — OLS/GLS, regularised linear (Ridge, Lasso, Elastic Net), GLMs (Poisson, Negative Binomial, Gamma, logistic) and IRLS, robust/M-estimators, quantile regression, GAMs/splines, mixed-effects (MixedLM), gradient boosting (XGBoost/LightGBM/CatBoost), Gaussian processes, and Bayesian regression (PyMC).
- **Classification** — Logistic regression, regularised linear models, SVM, k-NN, decision trees, random forests, gradient-boosted trees, naïve Bayes, and neural nets — with explicit attention to class imbalance (resampling, cost-sensitive learning), probability calibration, and threshold/decision analysis.
- **Unsupervised learning** — Clustering (k-means, hierarchical, DBSCAN/HDBSCAN, GMMs, fuzzy c-means); dimensionality reduction and manifold learning (PCA, SVD, t-SNE, UMAP); anomaly/outlier detection (Isolation Forest, LOF, One-Class SVM, autoencoders, and my own PSOD); density estimation; and topological methods (persistent homology).
- **Time series & forecasting** — ARIMA/SARIMAX, ETS/Prophet, state-space and structural models, singular spectrum analysis, global gradient-boosting, and foundation models (Chronos, Nixtla, masked-patch transformers), with conformal prediction intervals and rolling-origin backtesting.
- **Survival & event history** — Kaplan–Meier, Cox PH (incl. distributionally robust), parametric AFT models, and count/actuarial regression.
- **Causal & experimentation** — Uplift/heterogeneous treatment effects, IPW/AIPW, difference-in-differences, synthetic control, event studies, and A/B testing (power, variance reduction, SRM checks).
- **Probabilistic & Bayesian** — Hierarchical models, MCMC (PyMC), conformal prediction, and uncertainty quantification / calibration throughout.

---

## Current Focus

- Production RAG and agentic systems with evaluation, observability, and CI baked in
- Reproducible econometric research programs on inequality, wealth concentration, and public policy
- Dynamical-systems models of rentier equilibria, crisis dynamics, and wealth attractors
- Robust forecasting, anomaly detection, and drift control for operational data
- Reusable research infrastructure: contract-linked ETL, GitHub Actions tooling, and reproducibility contracts across multi-paper programmes

---

## Selected Work

A curated slice of recent public repositories. Full list at [github.com/DiogoRibeiro7](https://github.com/DiogoRibeiro7?tab=repositories).

### Production AI & LLM Systems

- **[feedback-intelligence-agent](https://github.com/DiogoRibeiro7/feedback-intelligence-agent)** — Production-style RAG system: a customer feedback intelligence agent with FastAPI, evaluation, observability, and CI.
- **[ragops-lab](https://github.com/DiogoRibeiro7/ragops-lab)** — Evaluation-first RAG and LLMOps platform for production-grade document QA: tracing, regression testing, and cost-aware experimentation.
- **[rag-showcase](https://github.com/DiogoRibeiro7/rag-showcase)** — End-to-end RAG Q&A reshaped from prototype into a production FastAPI service on Azure (pgvector, Azure OpenAI, Bicep, GitHub Actions).
- **[ai-incident-analysis-agent](https://github.com/DiogoRibeiro7/ai-incident-analysis-agent)** — Incident analysis agent over logs and metrics with anomaly detection, correlation, root-cause analysis, and LLM-assisted reporting.
- **[agentic-qa-lab](https://github.com/DiogoRibeiro7/agentic-qa-lab)** — Autonomous UI/game-testing agent: vision-language reasoning, browser control, action planning, failure recovery, and evaluation.
- **[llm-etl-and-evaluation](https://github.com/DiogoRibeiro7/llm-etl-and-evaluation)** — ETL + evaluation harness for structured LLM outputs: schema-guided prompting, tolerant parsing, validation, and an error taxonomy.
- **[rag-eval-framework](https://github.com/DiogoRibeiro7/rag-eval-framework)** — Framework for evaluating RAG answer quality, relevance, and retrieval metrics.
- **[huggingface-finetuning-lab](https://github.com/DiogoRibeiro7/huggingface-finetuning-lab)** — HuggingFace fine-tuning and NLP experimentation lab.
- **[ds-workspace-mcp](https://github.com/DiogoRibeiro7/ds-workspace-mcp)** — Model Context Protocol server for safely inspecting and profiling local analytical datasets.
- **[linear-algebra-tutor](https://github.com/DiogoRibeiro7/linear-algebra-tutor)** — RAG-driven Socratic tutoring system (FastAPI, React, Claude) built for ESMAD students.
- **[portuNLP](https://github.com/DiogoRibeiro7/portuNLP)** — Python library for Portuguese NLP: normalization, tokenization, preprocessing, and spaCy-backed analysis.

### ML Engineering & MLOps

- **[fastapi-ml-platform](https://github.com/DiogoRibeiro7/fastapi-ml-platform)** — Production-style FastAPI service for real-time fraud-risk scoring with ML inference, drift monitoring, and observability.
- **[clinic-forecasting-platform](https://github.com/DiogoRibeiro7/clinic-forecasting-platform)** — Healthcare demand-forecasting and staffing platform: a 13-model benchmark (SARIMAX, Prophet, gradient boosting, Nixtla, Chronos) with conformal intervals, rolling-origin backtesting, FastAPI serving, and monitoring.
- **[sensor-intelligence-platform](https://github.com/DiogoRibeiro7/sensor-intelligence-platform)** — Production-style time-series ML platform: forecasting, anomaly detection, drift monitoring, and predictive maintenance behind a FastAPI inference service.
- **[ml-portfolio-showcase](https://github.com/DiogoRibeiro7/ml-portfolio-showcase)** — End-to-end ML engineering: FinBERT fine-tuning with production MLOps on AWS (SageMaker, MWAA, Athena), Docker deployment, monitoring, and automated retraining.
- **[feature-store-lab](https://github.com/DiogoRibeiro7/feature-store-lab)** — Local feature-store workbench for point-in-time pipelines, offline/online serving parity, and training-serving skew detection.
- **[time-series-foundation-models](https://github.com/DiogoRibeiro7/time-series-foundation-models)** — Time-series foundation models in PyTorch for masked patch modelling, forecasting, and anomaly detection.
- **[research-to-product-ml-template](https://github.com/DiogoRibeiro7/research-to-product-ml-template)** — Reusable template for turning ML research papers into tested packages, benchmark suites, APIs, and product-oriented reports.

### Data Engineering & Streaming

- **[llm-data-platform](https://github.com/DiogoRibeiro7/llm-data-platform)** — Python monorepo for the LLM data lifecycle: contract-linked ingestion, dataset curation, and observability.
- **[transaction-risk-lakehouse](https://github.com/DiogoRibeiro7/transaction-risk-lakehouse)** — Production-style PySpark lakehouse for transaction-risk modelling, fraud detection, and temporal model validation.
- **[iceberg-lakehouse-portfolio](https://github.com/DiogoRibeiro7/iceberg-lakehouse-portfolio)** — Apache Iceberg lakehouse engineering with Spark, MinIO, and Nessie.
- **[pyflink-fraud-detection-streaming](https://github.com/DiogoRibeiro7/pyflink-fraud-detection-streaming)** — PyFlink streaming fraud detection with stateful features and explainable risk scoring.
- **[carbon-transition-duckdb-lab](https://github.com/DiogoRibeiro7/carbon-transition-duckdb-lab)** — Local DuckDB lakehouse for climate and energy-transition analytics with transparent risk scoring and forecasting.
- **[online-concept-drift-electricity-market](https://github.com/DiogoRibeiro7/online-concept-drift-electricity-market)** — Online concept-drift monitoring for electricity-market streaming data with adaptive retraining and alerting.
- **[displacement-risk-lab-dynamodb](https://github.com/DiogoRibeiro7/displacement-risk-lab-dynamodb)** — DynamoDB-based lab for public-data ingestion, scoring, and reproducible analytics workflows.

### Statistical & Applied Data Science

Breadth across the core methods — causal, survival, Bayesian, calibration, and interpretability — with reproducible experiments.

- **[causal-uplift-marketing-campaign](https://github.com/DiogoRibeiro7/causal-uplift-marketing-campaign)** — Causal uplift toolkit for incremental treatment-effect evaluation and campaign modelling.
- **[effectbridge](https://github.com/DiogoRibeiro7/effectbridge)** — Test (un)confoundedness by comparing an RCT-like effect to the same estimand from observational data (IPW/AIPW, bootstrap CIs, transportability weighting).
- **[genSurvPy](https://github.com/DiogoRibeiro7/genSurvPy)** — Python package for simulating survival data under a range of models (inspired by R's genSurv).
- **[probml-lab](https://github.com/DiogoRibeiro7/probml-lab)** — Probabilistic machine-learning lab covering Bayesian modelling and inference workflows.
- **[calibrated-ml-lab](https://github.com/DiogoRibeiro7/calibrated-ml-lab)** — ML calibration and uncertainty-quantification toolkit.
- **[csp_forecast_package](https://github.com/DiogoRibeiro7/csp_forecast_package)** — Training-free probabilistic forecasting with Conformal Seasonal Pools: quantiles, prediction intervals, and rolling-origin backtesting.
- **[interpretable-stroke-risk-screening](https://github.com/DiogoRibeiro7/interpretable-stroke-risk-screening)** — Transparent stroke-risk screening with actionable risk groups and fairness-aware evaluation.
- **[PSOD](https://github.com/DiogoRibeiro7/PSOD)** — Pseudo-Supervised Outlier Detection: ensemble regression prediction errors as outlier scores for mixed-type tabular data.

### Economics, Inequality & Policy Research

Reproducible research programmes built on open data, with validation, econometric models, and policy-facing outputs.

- **[poverty_neoliberalism_research_program](https://github.com/DiogoRibeiro7/poverty_neoliberalism_research_program)** — Agent-first scaffold for a ten-paper empirical programme on poverty, wages, taxes, and asset power in the US and UK since 1950, sharing one pipeline and reproducibility contract across all papers.
- **[eu_economy_decision_lab](https://github.com/DiogoRibeiro7/eu_economy_decision_lab)** — Policy-facing framework for diagnosing the European economy (growth, wage-productivity gaps, fiscal stance, inequality) producing reproducible country scorecards and a Portugal-vs-EU brief.
- **[wealth_rentier_dynamics](https://github.com/DiogoRibeiro7/wealth_rentier_dynamics)** — Modelling modern inequality as ownership and rent extraction: a dynamical system tending toward a rentier equilibrium, tested against WID, OECD, Eurostat, and ECB data.
- **[il_supply_side_policy_tests](https://github.com/DiogoRibeiro7/il_supply_side_policy_tests)** — Econometric tests of supply-side liberalisation using event studies, synthetic control (Portugal 2011–2015), and OECD/EU panel models.
- **[portugal_swf_sim](https://github.com/DiogoRibeiro7/portugal_swf_sim)** — Monte Carlo stress-testing framework for a Portuguese sovereign/strategic fund, modelling debt paths, pension coverage, and downside risk across six scenarios.
- **[housing_future_work_etl](https://github.com/DiogoRibeiro7/housing_future_work_etl)** — Auditable municipality-year ETL and econometric platform extending a Portuguese housing-price paper into a multi-year panel (PORDATA/INE + GEO API PT) with spatial and causal models.
- **[economic-pressure-democracy-europe](https://github.com/DiogoRibeiro7/economic-pressure-democracy-europe)** — Political data science on economic pressure, institutional decay, and anti-system voting in Europe.
- **[us-gdp-regime-1920](https://github.com/DiogoRibeiro7/us-gdp-regime-1920)** / **[pt_gdp_regime_repo](https://github.com/DiogoRibeiro7/pt_gdp_regime_repo)** — Reproducible analyses of US and Portuguese real-GDP trends and growth regimes.

### Mathematical Methods & Algorithms

- **[bmssp](https://github.com/DiogoRibeiro7/bmssp)** ⭐ — Deterministic Single-Source Shortest Paths solver for directed graphs with non-negative weights, using a BMSSP-style divide-and-conquer design (typed, tested).
- **[min_ratio_cycle](https://github.com/DiogoRibeiro7/min_ratio_cycle)** — Lawler-style parametric search with NumPy-accelerated negative-cycle detection and an exact Stern–Brocot mode.
- **[dynamical_systems_econometrics](https://github.com/DiogoRibeiro7/dynamical_systems_econometrics)** — Toolkit for simulation and econometric analysis of dynamical systems, including extreme-value and return-time workflows.
- **[heavytails](https://github.com/DiogoRibeiro7/heavytails)** — Pure-Python library of heavy-tailed distributions (Pareto, Burr, LogNormal, …) built from first principles.
- **[drl-cox](https://github.com/DiogoRibeiro7/drl-cox)** — Distributionally robust Cox regression with Wasserstein ambiguity sets, with baselines and reproducible experiments.

### Developer Tooling

- **[smart-todo-action](https://github.com/DiogoRibeiro7/smart-todo-action)** — GitHub Action that turns inline TODO/FIXME/BUG comments into issues, with labels, metadata parsing, and semantic enrichment.
- **[git-actions-collection](https://github.com/DiogoRibeiro7/git-actions-collection)** — Curated library of reusable GitHub Actions, workflows, and composite helpers shared across projects.
- **[article-reminders](https://github.com/DiogoRibeiro7/article-reminders)** — Scheduled GitHub Action that syncs one reminder issue per unfinished article across tracked repos.

### Live Dashboards

- **[Portugal Economic Indicators Dashboard](https://portugal-econ-dashboard.vercel.app/)** — Macroeconomic dashboard for Portugal with historical context across GDP, inflation, labour markets, external balance, and public finances.
- **[NASDAQ Stock Analytics Dashboard](https://nasdaq-dashboard-sigma.vercel.app/)** — Focused analytics for a selected set of NASDAQ stocks: prices, returns, volatility, and technical indicators.

---

## Research Interests

- **Inequality & Political Economy** — Wealth concentration, rentier dynamics, distributional metrics, and policy simulation under counterfactuals
- **Applied Econometrics** — Panel models, synthetic control, event studies, structural breaks, and causal inference on open data
- **Dynamical Systems** — Attractor dynamics, crisis and contagion models, extreme-value methods, and rare-event simulation
- **Production AI** — Reliable RAG and agent systems, evaluation, and audit-friendly LLM reporting
- **Time Series & Anomaly Detection** — Robust monitoring, drift, and change-point detection in operational and sensor-driven systems
- **Health & Survival Analysis** — Robust survival modelling, simulation workflows, and interpretable clinical analytics

---

## Collaboration Interests

I welcome collaboration with researchers, technical teams, and product groups on high-impact analytical problems, particularly:

- Production RAG, agentic systems, and evaluation/observability for LLM applications
- Reproducible econometric and policy research on inequality, wealth, and public finance
- Robust time-series modelling and anomaly detection in operational environments
- Dynamical-systems modelling and rare-event simulation
- Translating mathematically rigorous methods into maintainable team workflows

When reaching out, include a short note on your use case, constraints, and timeline so we can assess fit quickly.

---

## Teaching

<details>
<summary>Teaching is a core part of how I contribute — translating mathematical and technical ideas into material teams and students can apply in practice. (click to expand)</summary>

### Teaching @ESMAD (Instituto Politécnico do Porto)

- **Introduction to Logic & Set Theory** — Logic (prop/FO), sets, induction, and differential & integral calculus, with an emphasis on rigorous reasoning and the transition from discrete foundations to continuous mathematics.
- **Linear Algebra & Analytic Geometry** — Vector spaces and linear maps; matrices and determinants; eigenvalues, diagonalisation, orthogonality and least squares; SVD and PCA; numerical stability; applications to optimisation and data science. ([course repo](https://github.com/DiogoRibeiro7/linear-algebra-with-python))
- **NoSQL & MongoDB** — Document-oriented modelling, indexing and aggregation, query patterns, and practical work with real datasets. ([labs](https://github.com/DiogoRibeiro7/nosql-databases-labs))
- **NLP & LLM mini-workshops** — Prompt design, evaluation, lightweight retrieval, structured outputs, and report generation, with attention to reliability in production.

### Seminars & Workshops

- **Data Science & MLOps** — End-to-end ML pipelines, feature engineering for time series, evaluation under drift, CI/CD, and reproducible research practices.
- **Sensors & Dashboards** — IoT ingestion (MQTT/Kafka), time-series storage (InfluxDB/Parquet), streaming analytics (Flink), and dashboards (Grafana/Plotly/Dash) with alerting and anomaly detection.
- **Statistical Modelling & Experimentation** — Experimental design, power analysis, variance reduction, SRM diagnostics, and translating results into decisions.
- **Graph Analytics & Network Science** — Centrality, community detection, temporal networks, and diffusion processes.
- **Time Series, Forecasting & Anomaly Detection** — Decomposition, baselines, adaptive thresholds, and change-point detection for operational systems.

</details>

---

## GitHub Stats

### 2026 Highlights (public + private work)

- **Production AI:** shipped RAG and agent systems (`feedback-intelligence-agent`, `ragops-lab`, `ai-incident-analysis-agent`) — with evaluation, tracing, observability, and CI treated as first-class.
- **ML & data engineering:** built serving, MLOps, and lakehouse/streaming platforms (`fastapi-ml-platform`, `feature-store-lab`, `transaction-risk-lakehouse`, `pyflink-fraud-detection-streaming`, `llm-data-platform`) spanning inference, drift monitoring, feature parity, and contract-linked ingestion.
- **Research programmes at scale:** launched a cluster of reproducible econometric and dynamical-systems projects on inequality, wealth, and policy, several sharing a single pipeline and reproducibility contract across many papers.
- **Algorithms & methods:** released and refined typed, tested solvers and libraries (`bmssp`, `min_ratio_cycle`, `heavytails`, `dynamical_systems_econometrics`).
- **Reusable infrastructure:** built developer tooling (`smart-todo-action`, `git-actions-collection`, `article-reminders`) to keep a large, multi-repo research output reproducible and maintainable.

Contribution activity across public and private work:

<p align="center">
  <a href="https://user-badge.committers.top/portugal_private/DiogoRibeiro7">
    <img src="https://user-badge.committers.top/portugal_private/DiogoRibeiro7.svg" alt="committers.top badge"/>
  </a>
</p>

<div align="center">
  <a href="https://github.com/ryo-ma/github-profile-trophy">
    <img src="https://trophy.benkou.dev/?username=DiogoRibeiro7&column=3&no-frame=true&theme=algolia" alt="Trophy" />
  </a>
</div>

---

## Let's Connect and Collaborate

<div align="center">
  <a href="https://medium.com/@neverforget-1975">
    <img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white" alt="Medium" />
  </a>
  <a href="https://dev.to/diogoribeiro7">
    <img src="https://img.shields.io/badge/dev.to-0A0A0A?style=for-the-badge&logo=dev.to&logoColor=white" alt="Dev.to" />
  </a>
  <a href="https://www.linkedin.com/in/diogo-ribeiro-9094604a/">
    <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="mailto:diogo.debastos.ribeiro@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?logo=gmail&logoColor=white" alt="Email">
  </a>
</div>
