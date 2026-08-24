<div align="center">
  <a href="https://github.com/DiogoRibeiro7"><img src="https://img.shields.io/badge/Home-30363D?style=for-the-badge" alt="Home" /></a>
  <img src="https://img.shields.io/badge/Projects-1F6FEB?style=for-the-badge" alt="Projects (current page)" />
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/METHODS.md"><img src="https://img.shields.io/badge/Methods-30363D?style=for-the-badge" alt="Methods" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/RESEARCH.md"><img src="https://img.shields.io/badge/Research-30363D?style=for-the-badge" alt="Research" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/TEACHING.md"><img src="https://img.shields.io/badge/Teaching-30363D?style=for-the-badge" alt="Teaching" /></a>
</div>

---

# Selected Work

A curated slice of recent work, grouped by the kind of problem it solves. Linked entries are public repositories; entries marked *(private)* are active but not published, and are listed so the picture is complete. Full public list at [github.com/DiogoRibeiro7](https://github.com/DiogoRibeiro7?tab=repositories).

- [Production AI & LLM Systems](#production-ai--llm-systems)
- [ML Engineering & MLOps](#ml-engineering--mlops)
- [Deep Learning & Scientific Computing](#deep-learning--scientific-computing)
- [Data Engineering & Streaming](#data-engineering--streaming)
- [Statistical & Applied Data Science](#statistical--applied-data-science)
- [Optimisation & Decision Systems](#optimisation--decision-systems)
- [Economics, Finance & Policy Research](#economics-finance--policy-research)
- [Mathematical Methods & Algorithms](#mathematical-methods--algorithms)
- [Developer Tooling](#developer-tooling)
- [Live Dashboards](#live-dashboards)

---

## Production AI & LLM Systems

- **[feedback-intelligence-agent](https://github.com/DiogoRibeiro7/feedback-intelligence-agent)** — Production-style RAG system: a customer feedback intelligence agent with FastAPI, evaluation, observability, and CI.
- **[ragops-lab](https://github.com/DiogoRibeiro7/ragops-lab)** — Evaluation-first RAG and LLMOps platform for production-grade document QA: tracing, regression testing, and cost-aware experimentation.
- **[hf-data-agent](https://github.com/DiogoRibeiro7/hf-data-agent)** — Internal data agent where a UI, an HTTP API, local and remote MCP, and Slack all funnel into one Agent API, grounding an open-source Hugging Face model in a company knowledge base while pulling fresh numbers from the data platform.
- **[genai-rag-engineering](https://github.com/DiogoRibeiro7/genai-rag-engineering)** — Standalone RAG and LLM engineering primitives: chunking, prompt registry, retrieval and reranking, guardrails with PII redaction and prompt-injection checks, judge helpers, and cost/latency/trace telemetry — with a deterministic fake client so CI runs offline without API keys.
- **[qwen-text2sql-lab](https://github.com/DiogoRibeiro7/qwen-text2sql-lab)** — Controlled LoRA/QLoRA adaptation study on Qwen3.5-4B for text-to-SQL, asking how much data and adapter capacity fine-tuning actually needs before it beats the base model. Scored on execution accuracy against the target database; string equality is kept only as a secondary diagnostic.
- **rag-showcase** *(private)* — End-to-end RAG Q&A reshaped from prototype into a production FastAPI service on Azure (pgvector, Azure OpenAI, Bicep, GitHub Actions).
- **[ai-incident-analysis-agent](https://github.com/DiogoRibeiro7/ai-incident-analysis-agent)** — Incident analysis agent over logs and metrics with anomaly detection, correlation, root-cause analysis, and LLM-assisted reporting.
- **[agentic-qa-lab](https://github.com/DiogoRibeiro7/agentic-qa-lab)** — Autonomous UI/game-testing agent: vision-language reasoning, browser control, action planning, failure recovery, and evaluation.
- **[llm-etl-and-evaluation](https://github.com/DiogoRibeiro7/llm-etl-and-evaluation)** — ETL + evaluation harness for structured LLM outputs: schema-guided prompting, tolerant parsing, validation, and an error taxonomy.
- **rag-eval-framework** *(private)* — Framework for evaluating RAG answer quality, relevance, and retrieval metrics.
- **[huggingface-finetuning-lab](https://github.com/DiogoRibeiro7/huggingface-finetuning-lab)** — HuggingFace fine-tuning and NLP experimentation lab.
- **[ds-workspace-mcp](https://github.com/DiogoRibeiro7/ds-workspace-mcp)** — Model Context Protocol server for safely inspecting and profiling local analytical datasets.
- **[linear-algebra-tutor](https://github.com/DiogoRibeiro7/linear-algebra-tutor)** — RAG-driven Socratic tutoring system (FastAPI, React, Claude) built for ESMAD students.
- **[portuNLP](https://github.com/DiogoRibeiro7/portuNLP)** — Python library for Portuguese NLP: normalization, tokenization, preprocessing, and spaCy-backed analysis.

## ML Engineering & MLOps

- **[fastapi-ml-platform](https://github.com/DiogoRibeiro7/fastapi-ml-platform)** — Production-style FastAPI service for real-time fraud-risk scoring with ML inference, drift monitoring, and observability.
- **[clinic-forecasting-platform](https://github.com/DiogoRibeiro7/clinic-forecasting-platform)** — Healthcare demand-forecasting and staffing platform: a 13-model benchmark (SARIMAX, Prophet, gradient boosting, Nixtla, Chronos) with conformal intervals, rolling-origin backtesting, FastAPI serving, and monitoring.
- **[sensor-intelligence-platform](https://github.com/DiogoRibeiro7/sensor-intelligence-platform)** — Production-style time-series ML platform: forecasting, anomaly detection, drift monitoring, and predictive maintenance behind a FastAPI inference service.
- **[enterprise-ml-platform](https://github.com/DiogoRibeiro7/enterprise-ml-platform)** — Reference implementation of a production ML platform: reproducible training, versioned features, a model registry with alias-based promotion, an HTTP serving layer, and controlled SageMaker deployment — with an explicit statement of which parts are tested and which are scaffolding.
- **ml-portfolio-showcase** *(private)* — End-to-end ML engineering: FinBERT fine-tuning with production MLOps on AWS (SageMaker, MWAA, Athena), Docker deployment, monitoring, and automated retraining.
- **feature-store-lab** *(private)* — Local feature-store workbench for point-in-time pipelines, offline/online serving parity, and training-serving skew detection.
- **time-series-foundation-models** *(private)* — Time-series foundation models in PyTorch for masked patch modelling, forecasting, and anomaly detection.
- **research-to-product-ml-template** *(private)* — Reusable template for turning ML research papers into tested packages, benchmark suites, APIs, and product-oriented reports.
- **survdrift** *(private)* — Survival-model drift monitoring on replayed Backblaze drive telemetry: idempotent ingestion, explicit censoring semantics, a model registry, FastAPI serving with prediction logging, matured-outcome monitoring, and Kubernetes rollout/rollback.
- **shiftguard** *(private)* — Overlap-aware conformal prediction and selective risk control under covariate shift: hold a target coverage guarantee, detect poor source–target overlap, and abstain when the evidence stops supporting a prediction.

## Deep Learning & Scientific Computing

Architecture research and numerical solvers, run as reproducible experiments rather than one-off notebooks.

- **[modern-neural-networks-agent-repo](https://github.com/DiogoRibeiro7/modern-neural-networks-agent-repo)** — Research lab for neural-network mechanisms beyond conventional MLPs and Transformers: eleven architecture tracks under one shared experimental contract, 987 validated experiment records, and reports regenerated from those records — with no aggregate leaderboard, by design.
- **[anomaly-transformer-lab](https://github.com/DiogoRibeiro7/anomaly-transformer-lab)** — Compact PyTorch implementation of the Anomaly Transformer (series-vs-prior association discrepancy) for unsupervised time-series anomaly detection, with sparse-attention ablations and robust reconstruction losses.
- **[pinn](https://github.com/DiogoRibeiro7/pinn)** — Modular PyTorch Physics-Informed Neural Networks for PDEs, with advanced sampling strategies, error analysis, and visualisation.
- **[pinn-rk](https://github.com/DiogoRibeiro7/pinn-rk)** — Runge–Kutta Physics-Informed Neural Networks with time-discrete losses (Gauss, Radau, Lobatto).
- **[torch-namo-optim](https://github.com/DiogoRibeiro7/torch-namo-optim)** — Production-ready PyTorch implementations of the NAMO and NAMO-D orthogonalised-momentum optimisers.
- **[oisst-fourier-neural-operator](https://github.com/DiogoRibeiro7/oisst-fourier-neural-operator)** — Fourier Neural Operator study on NOAA OISST sea-surface temperature over the Northeast Atlantic, asking the narrow version of the question: when does an FNO beat persistence at 7-day-ahead field forecasting, and at which spatial scales? Positioned explicitly as an empirical forecasting study, not a claim to have learned the governing equations.
- **[navier-stokes-solvers](https://github.com/DiogoRibeiro7/navier-stokes-solvers)** — 2D incompressible Navier–Stokes solvers (Newton–Raphson finite difference and Fourier spectral) with adaptive time stepping, convergence analysis, and turbulence diagnostics.

## Data Engineering & Streaming

- **[llm-data-platform](https://github.com/DiogoRibeiro7/llm-data-platform)** — Python monorepo for the LLM data lifecycle: contract-linked ingestion, dataset curation, and observability.
- **[transaction-risk-lakehouse](https://github.com/DiogoRibeiro7/transaction-risk-lakehouse)** — Production-style PySpark lakehouse for transaction-risk modelling, fraud detection, and temporal model validation.
- **[iceberg-lakehouse-portfolio](https://github.com/DiogoRibeiro7/iceberg-lakehouse-portfolio)** — Apache Iceberg lakehouse engineering with Spark, MinIO, and Nessie.
- **[pyflink-fraud-detection-streaming](https://github.com/DiogoRibeiro7/pyflink-fraud-detection-streaming)** — PyFlink streaming fraud detection with stateful features and explainable risk scoring.
- **[carbon-transition-duckdb-lab](https://github.com/DiogoRibeiro7/carbon-transition-duckdb-lab)** — Local DuckDB lakehouse for climate and energy-transition analytics with transparent risk scoring and forecasting.
- **online-concept-drift-electricity-market** *(private)* — Online concept-drift monitoring for electricity-market streaming data with adaptive retraining and alerting.
- **displacement-risk-lab-dynamodb** *(private)* — DynamoDB-based lab for public-data ingestion, scoring, and reproducible analytics workflows.

## Statistical & Applied Data Science

Breadth across the core methods — causal, survival, Bayesian, calibration, and interpretability — with reproducible experiments.

- **[setqca](https://github.com/DiogoRibeiro7/setqca-python)** — Native, typed Python implementation of crisp-set and fuzzy-set Qualitative Comparative Analysis with exact Boolean minimisation — not an R wrapper. Conservative, parsimonious, and intermediate solutions match the reference R `QCA` package on the canonical Lipset datasets, with the one divergence documented on the validation page; on PyPI (0.2.x alpha), with docs and a DOI.
- **[scania-aps-cost](https://github.com/DiogoRibeiro7/scania-aps-cost)** — Cost-sensitive learning on the UCI *APS Failure at Scania Trucks* data: regularisation, imbalance handling, calibration, representation learning, and threshold choice all evaluated against an explicit 10×FP + 500×FN maintenance cost rather than accuracy.
- **[experimentation-toolkit](https://github.com/DiogoRibeiro7/experimentation-toolkit)** — Focused A/B testing utilities: two-proportion and Welch tests, bootstrap intervals, sample-size and power calculations, sample-ratio-mismatch checks, CUPED variance reduction, and small bandit helpers.
- **[applied-unsupervised-learning](https://github.com/DiogoRibeiro7/applied-unsupervised-learning)** — Unsupervised learning treated as a full modelling workflow rather than a tour of algorithms: representation learning, clustering, anomaly detection, topic discovery, model selection, and stability analysis — with the results that did *not* flatter the method reported alongside the ones that did.
- **[causal-uplift-marketing-campaign](https://github.com/DiogoRibeiro7/causal-uplift-marketing-campaign)** — Causal uplift toolkit for incremental treatment-effect evaluation and campaign modelling.
- **[customer-analytics](https://github.com/DiogoRibeiro7/customer-analytics)** — Churn, segmentation, retention, and uplift in one place: feature engineering, model orchestration, evaluation, and a production wrapper with lightweight MLOps helpers.
- **[effectbridge](https://github.com/DiogoRibeiro7/effectbridge)** — Test (un)confoundedness by comparing an RCT-like effect to the same estimand from observational data (IPW/AIPW, bootstrap CIs, transportability weighting).
- **[genSurvPy](https://github.com/DiogoRibeiro7/genSurvPy)** — Python package for simulating survival data under a range of models (inspired by R's genSurv).
- **probml-lab** *(private)* — Probabilistic machine-learning lab covering Bayesian modelling and inference workflows.
- **calibrated-ml-lab** *(private)* — ML calibration and uncertainty-quantification toolkit.
- **[csp_forecast_package](https://github.com/DiogoRibeiro7/csp_forecast_package)** — Training-free probabilistic forecasting with Conformal Seasonal Pools: quantiles, prediction intervals, and rolling-origin backtesting.
- **interpretable-stroke-risk-screening** *(private)* — Transparent stroke-risk screening with actionable risk groups and fairness-aware evaluation.
- **[PSOD](https://github.com/DiogoRibeiro7/PSOD)** — Pseudo-Supervised Outlier Detection: ensemble regression prediction errors as outlier scores for mixed-type tabular data.

## Optimisation & Decision Systems

Models that end in a decision — a dispatch schedule, an order quantity, an operating threshold — not just a metric.

- **[energy-system-simulator](https://github.com/DiogoRibeiro7/energy-system-simulator)** — Optimisation-based simulator for hybrid electricity systems: thermal unit commitment with ramp limits and minimum up/down times, battery and pumped storage, reservoir and run-of-river hydro, demand response, imports, and distribution constraints — explicit physics and economics rather than learned surrogates.
- **[perishable-inventory-decision-lab](https://github.com/DiogoRibeiro7/perishable-inventory-decision-lab)** — Probabilistic demand forecasting and perishable inventory simulation: censored-demand separation, leakage-safe features, calibrated quantile forecasts, and replenishment-policy evaluation across the full decision loop.
- **[rcpsp_cf_ivfth](https://github.com/DiogoRibeiro7/rcpsp_cf_ivfth)** — Multi-mode project scheduling under financial constraints and fuzzy uncertainty, with loans and resource limits (Python/Pyomo).

## Economics, Finance & Policy Research

Reproducible research programmes built on open data, with validation, econometric models, and policy-facing outputs.

- **[portugal-public-pension-financing](https://github.com/DiogoRibeiro7/portugal-public-pension-financing)** — How the public pension promise was actually financed, tracing CGA, Social Security, and the 2009–2012 transfer of banking-sector liabilities through the legal sequence that produced them. Separates legal obligations, cash accounting, consolidated flows, actuarial liabilities, and counterfactual financing regimes before any balance is read as a deficit, a surplus, or a subsidy.
- **[portugal-fiscal-balance](https://github.com/DiogoRibeiro7/portugal-fiscal-balance)** — How Portugal's general-government balance is formed across Central Government, Regional and Local Government, and Social Security Funds, 1977–2025 — restricted by design to accounting, statistical, and economic analysis, with no inference of intent or responsibility.
- **portugal-pension-boundaries** *(private)* — Methodological audit of the 2026 Portuguese pension reform report across all nineteen chapters: accounting boundaries, a claim registry, and a systematic inference, tax-treatment, and validation-provenance protocol. The founding case is the report's treatment of post-2005 public-worker contributions in the RGSS/CGA comparison.
- **[portugal-gdp-bayesian-revision](https://github.com/DiogoRibeiro7/portugal-gdp-bayesian-revision)** — Portugal has two official population figures for 2025 that differ by 5.6%. Before asking what INE's revision does to GDP per capita, this asks the prior question of fact: which population is the published index actually divided by?
- **[gdp-wage-transmission](https://github.com/DiogoRibeiro7/gdp-wage-transmission)** — How growth and labour productivity transmit into real wages, how fast, and whether the relationship has changed — Portugal first, built from the start to support cross-country robustness checks, with a frozen reference audit.
- **[pt-salary-gamma-distribution](https://github.com/DiogoRibeiro7/pt-salary-gamma-distribution)** — Monthly earnings in Portugal from the GEP/MTSSS *Quadros de Pessoal* grouped tables. Does not assume the Gamma family fits; tests it against alternative positive-support models on the grouped data the workbooks actually publish.
- **poverty_neoliberalism_research_program** *(private)* — Agent-first scaffold for a ten-paper empirical programme on poverty, wages, taxes, and asset power in the US and UK since 1950, sharing one pipeline and reproducibility contract across all papers.
- **eu_economy_decision_lab** *(private)* — Policy-facing framework for diagnosing the European economy (growth, wage-productivity gaps, fiscal stance, inequality) producing reproducible country scorecards and a Portugal-vs-EU brief.
- **wealth_rentier_dynamics** *(private)* — Modelling modern inequality as ownership and rent extraction: a dynamical system tending toward a rentier equilibrium, tested against WID, OECD, Eurostat, and ECB data.
- **il_supply_side_policy_tests** *(private)* — Econometric tests of supply-side liberalisation using event studies, synthetic control (Portugal 2011–2015), and OECD/EU panel models.
- **portugal_swf_sim** *(private)* — Monte Carlo stress-testing framework for a Portuguese sovereign/strategic fund, modelling debt paths, pension coverage, and downside risk across six scenarios.
- **housing_future_work_etl** *(private)* — Auditable municipality-year ETL and econometric platform extending a Portuguese housing-price paper into a multi-year panel (PORDATA/INE + GEO API PT) with spatial and causal models.
- **[portugal-minimum-wage-inflation](https://github.com/DiogoRibeiro7/portugal-minimum-wage-inflation)** — Minimum wages, productivity, and consumer prices in Portugal since 1974: long-run growth accounting plus an exposure-based pass-through design across regions and industries, including the Madeira/Azores differentiation.
- **[portugal-public-debt-interest](https://github.com/DiogoRibeiro7/portugal-public-debt-interest)** — Portugal's general-government interest burden in euros and as a share of GDP (Eurostat ESA 2010, with an optional AMECO extension), supporting two papers off one shared measurement layer with a byte-identical regression test as the contract between them.
- **[portugal-external-growth-1960-1973](https://github.com/DiogoRibeiro7/portugal-external-growth-1960-1973)** — Data pipeline weighing colonial against European economic linkages in Portuguese growth, 1960–1973: historical trade classifications, territorial definitions, and cross-checks — deliberately code and data only, no narrative until the pipeline is stable.
- **[short-rate-anomaly-regimes](https://github.com/DiogoRibeiro7/short-rate-anomaly-regimes)** — Replication and extension of Maio and Santa-Clara on short-rate innovations and equity anomalies: every table and figure generated from frozen artifacts, with provenance labels, an adversarial release gate, and a test that fails when a committed table stops matching its source.
- **[europe-fsqca-innovation](https://github.com/DiogoRibeiro7/europe-fsqca-innovation)** — Survey-design-aware fsQCA of configurational pathways to firm innovation across the EU-27, asking whether capability configurations travel between Northern/Western, Southern, and Central/Eastern Europe — with a readiness gate that refuses to run a template design.
- **economic-pressure-democracy-europe** *(private)* — Political data science on economic pressure, institutional decay, and anti-system voting in Europe.
- **[portugal-refining-resilience](https://github.com/DiogoRibeiro7/portugal-refining-resilience)** — Portugal's petroleum-product system around two events: the Sines hydrocracker entering production in 2013 and the end of refining at Matosinhos in 2021. Does not assume closure raised pump prices — it separates and tests four candidate mechanisms.
- **[porto-lisbon-uhi-exposure](https://github.com/DiogoRibeiro7/porto-lisbon-uhi-exposure)** — Urban heat island exposure rebuilt from Eurostat GISCO census grids, Urban Audit boundaries, the EEA/Copernicus UrbClim model, and OpenStreetMap green cover, to answer two separate questions: what makes cells hot, and who lives in them.
- **[city-wage-cost-global](https://github.com/DiogoRibeiro7/city-wage-cost-global)** — Does the higher nominal income in big, expensive cities survive adjustment for what it costs to live there? Tested across US, UK, and EU cities on public data, with all notebooks executed end to end and the findings read off committed outputs.
- **[us-gdp-regime-1920](https://github.com/DiogoRibeiro7/us-gdp-regime-1920)** / **[pt_gdp_regime_repo](https://github.com/DiogoRibeiro7/pt_gdp_regime_repo)** — Reproducible analyses of US and Portuguese real-GDP trends and growth regimes.

## Mathematical Methods & Algorithms

- **[bmssp](https://github.com/DiogoRibeiro7/bmssp)** ⭐ — Deterministic Single-Source Shortest Paths solver for directed graphs with non-negative weights, using a BMSSP-style divide-and-conquer design (typed, tested).
- **[min_ratio_cycle](https://github.com/DiogoRibeiro7/min_ratio_cycle)** — Lawler-style parametric search with NumPy-accelerated negative-cycle detection and an exact Stern–Brocot mode.
- **[dynamical_systems_econometrics](https://github.com/DiogoRibeiro7/dynamical_systems_econometrics)** — Toolkit for simulation and econometric analysis of dynamical systems, including extreme-value and return-time workflows.
- **[heavytails](https://github.com/DiogoRibeiro7/heavytails)** — Pure-Python library of heavy-tailed distributions (Pareto, Burr, LogNormal, …) built from first principles.
- **[drl-cox](https://github.com/DiogoRibeiro7/drl-cox)** — Distributionally robust Cox regression with Wasserstein ambiguity sets, with baselines and reproducible experiments.
- **[sml_diffusions_paper](https://github.com/DiogoRibeiro7/sml_diffusions_paper)** — Dimensional asymptotics of Euler-based simulated likelihood for multidimensional diffusions: two manuscripts, the code that generates every number in them, and the machinery that keeps the two in agreement.
- **[dynamical-evt-pdm](https://github.com/DiogoRibeiro7/dynamical-evt-pdm)** — Regime-conditioned dynamical extreme-value theory for predictive maintenance: extremal indices, declustering, recurrence near periodic states, and lagged multivariate extremes turned into event-level alarms with measurable lead time.

## Developer Tooling

- **[smart-todo-action](https://github.com/DiogoRibeiro7/smart-todo-action)** — GitHub Action that turns inline TODO/FIXME/BUG comments into issues, with labels, metadata parsing, and semantic enrichment.
- **[git-actions-collection](https://github.com/DiogoRibeiro7/git-actions-collection)** — Curated library of reusable GitHub Actions, workflows, and composite helpers shared across projects.
- **[repo-task-tracker](https://github.com/DiogoRibeiro7/repo-task-tracker)** — GitHub Action that syncs `tracker.json` tasks to issues and a central project board across repositories.
- **[article-reminders](https://github.com/DiogoRibeiro7/article-reminders)** — Scheduled GitHub Action that syncs one reminder issue per unfinished article across tracked repos.

## Live Dashboards

- **[Portugal Economic Indicators Dashboard](https://portugal-econ-dashboard.vercel.app/)** — Macroeconomic dashboard for Portugal with historical context across GDP, inflation, labour markets, external balance, and public finances.
- **[NASDAQ Stock Analytics Dashboard](https://nasdaq-dashboard-sigma.vercel.app/)** — Focused analytics for a selected set of NASDAQ stocks: prices, returns, volatility, and technical indicators.

---

<div align="center">
  <a href="https://github.com/DiogoRibeiro7"><img src="https://img.shields.io/badge/%E2%86%90%20Back%20to%20profile-30363D?style=for-the-badge" alt="Back to profile" /></a>
</div>
