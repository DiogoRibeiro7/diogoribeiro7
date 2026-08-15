<div align="center">
  <a href="https://github.com/DiogoRibeiro7"><img src="https://img.shields.io/badge/Home-30363D?style=for-the-badge" alt="Home" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/PROJECTS.md"><img src="https://img.shields.io/badge/Projects-30363D?style=for-the-badge" alt="Projects" /></a>
  <img src="https://img.shields.io/badge/Methods-1F6FEB?style=for-the-badge" alt="Methods (current page)" />
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/RESEARCH.md"><img src="https://img.shields.io/badge/Research-30363D?style=for-the-badge" alt="Research" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/TEACHING.md"><img src="https://img.shields.io/badge/Teaching-30363D?style=for-the-badge" alt="Teaching" /></a>
</div>

---

# Skills & Modelling Toolbox

The tools I build with, and the model families I reach for. I choose for interpretability and calibration first, then accuracy — and I benchmark rather than assume.

- [Technical Skills](#technical-skills)
- [Modelling Toolbox](#modelling-toolbox)

---

## Technical Skills

- **Programming** — Python (typed, NumPy-first), SQL, R, TypeScript, Bash/Zsh, C, Fortran
- **AI / LLM** — RAG, agent orchestration, structured outputs, evaluation harnesses; HuggingFace fine-tuning; prompt contracts and audit trails
- **ML / Data** — NumPy, Pandas, Polars, FireDucks; scikit-learn, XGBoost/LightGBM; PyTorch, TensorFlow; Statsmodels, PyMC, Pyomo
- **Research packaging** — Publishing methods as installable, documented libraries (PyPI, Poetry) with Zenodo DOIs, validation against reference implementations, and release gates
- **Data Eng & Streaming** — Apache Kafka, Flink, Spark, Databricks; Arrow/Parquet; Apache Iceberg (lakehouse)
- **Cloud & Storage** — AWS S3, DynamoDB; PostgreSQL/PostGIS, MySQL, SQLite; MongoDB, InfluxDB, TimescaleDB
- **DevEx & CI/CD** — Docker; GitHub Actions (incl. custom/composite actions), Jenkins; Poetry; pre-commit (ruff, mypy, pytest-cov); semantic versioning
- **Testing & Quality** — pytest, coverage, property-based tests (hypothesis); static typing; security linting (bandit)

---

## Modelling Toolbox

The model families I reach for, organised by task.

- **Regression** — OLS/GLS, regularised linear (Ridge, Lasso, Elastic Net), GLMs (Poisson, Negative Binomial, Gamma, logistic) and IRLS, robust/M-estimators, quantile regression, GAMs/splines, mixed-effects (MixedLM), gradient boosting (XGBoost/LightGBM/CatBoost), Gaussian processes, and Bayesian regression (PyMC).
- **Classification** — Logistic regression, regularised linear models, SVM, k-NN, decision trees, random forests, gradient-boosted trees, naïve Bayes, and neural nets — with explicit attention to class imbalance (resampling, cost-sensitive learning), probability calibration, and threshold/decision analysis.
- **Unsupervised learning** — Clustering (k-means, hierarchical, DBSCAN/HDBSCAN, GMMs, fuzzy c-means); dimensionality reduction and manifold learning (PCA, SVD, t-SNE, UMAP); anomaly/outlier detection (Isolation Forest, LOF, One-Class SVM, autoencoders, and my own [PSOD](https://github.com/DiogoRibeiro7/PSOD)); density estimation; and topological methods (persistent homology).
- **Time series & forecasting** — ARIMA/SARIMAX, ETS/Prophet, state-space and structural models, singular spectrum analysis, global gradient-boosting, and foundation models (Chronos, Nixtla, masked-patch transformers), with conformal prediction intervals and rolling-origin backtesting.
- **Survival & event history** — Kaplan–Meier, Cox PH (incl. [distributionally robust](https://github.com/DiogoRibeiro7/drl-cox)), parametric AFT models, and count/actuarial regression.
- **Causal & experimentation** — Uplift/heterogeneous treatment effects, IPW/AIPW, difference-in-differences, synthetic control, event studies, and A/B testing (power, variance reduction, SRM checks).
- **Configurational & comparative** — Crisp-set and fuzzy-set QCA: calibration anchors, truth tables, consistency and coverage, and exact Boolean minimisation across conservative, parsimonious, and intermediate solutions — implemented natively in Python in my [setqca](https://github.com/DiogoRibeiro7/setqca-python) package and checked against the reference R implementation.
- **Optimisation & decision modelling** — MILP unit commitment and dispatch, inventory and replenishment policy under censored demand, project scheduling with financial and fuzzy constraints (Pyomo), and cost-weighted threshold optimisation where false positives and false negatives carry different prices.
- **Deep learning & scientific ML** — Modern architectures beyond MLPs and Transformers (including association-discrepancy anomaly detection and gated convolutional heads), physics-informed neural networks (including Runge–Kutta time-discrete formulations), custom optimisers, and spectral / finite-difference PDE solvers.
- **Probabilistic & Bayesian** — Hierarchical models, MCMC (PyMC), conformal prediction, and uncertainty quantification / calibration throughout.

Working code for most of these lives in [Projects](https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/PROJECTS.md).

---

<div align="center">
  <a href="https://github.com/DiogoRibeiro7"><img src="https://img.shields.io/badge/%E2%86%90%20Back%20to%20profile-30363D?style=for-the-badge" alt="Back to profile" /></a>
</div>
