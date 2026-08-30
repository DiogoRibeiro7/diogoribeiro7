<div align="center">
  <a href="https://github.com/DiogoRibeiro7"><img src="https://img.shields.io/badge/Home-30363D?style=for-the-badge" alt="Home" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/FEATURED.md"><img src="https://img.shields.io/badge/Featured-30363D?style=for-the-badge" alt="Featured" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/PROJECTS.md"><img src="https://img.shields.io/badge/Projects-30363D?style=for-the-badge" alt="Projects" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/METHODS.md"><img src="https://img.shields.io/badge/Methods-30363D?style=for-the-badge" alt="Methods" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/RESEARCH.md"><img src="https://img.shields.io/badge/Research-30363D?style=for-the-badge" alt="Research" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/OUTPUTS.md"><img src="https://img.shields.io/badge/Outputs-30363D?style=for-the-badge" alt="Outputs" /></a>
  <img src="https://img.shields.io/badge/Case%20Studies-1F6FEB?style=for-the-badge" alt="Case Studies (current page)" />
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/TEACHING.md"><img src="https://img.shields.io/badge/Teaching-30363D?style=for-the-badge" alt="Teaching" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/PYPI.md"><img src="https://img.shields.io/badge/PyPI-30363D?style=for-the-badge&logo=pypi&logoColor=white" alt="PyPI" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/STATISTICS.md"><img src="https://img.shields.io/badge/Statistics-30363D?style=for-the-badge" alt="Statistics" /></a>
</div>

---

# Case Studies

A small set of end-to-end examples showing the problem, constraints, method and resulting decision or system. These are deliberately more selective than the project catalogue.

## [feedback-intelligence-agent](https://github.com/DiogoRibeiro7/feedback-intelligence-agent)

**Problem.** Turn unstructured customer feedback into traceable, queryable evidence.

**Constraints.** Ground answers in retrieved evidence, measure retrieval quality, expose latency/cost and support production serving.

**Method.** RAG pipeline with FastAPI, evaluation, observability and CI.

**Outcome.** A production-style feedback intelligence system whose answer quality can be tested rather than asserted.

## [clinic-forecasting-platform](https://github.com/DiogoRibeiro7/clinic-forecasting-platform)

**Problem.** Forecast healthcare demand while supporting staffing decisions under uncertainty.

**Constraints.** Temporal leakage, multiple forecasting families, uncertainty intervals and production monitoring.

**Method.** Rolling-origin benchmark across thirteen models with conformal intervals and serving.

**Outcome.** A full forecast-to-operation workflow rather than a single accuracy leaderboard.

## [oisst-fourier-neural-operator](https://github.com/DiogoRibeiro7/oisst-fourier-neural-operator)

**Problem.** Test whether an FNO materially improves seven-day SST field forecasts over persistence.

**Constraints.** Real NOAA data, spatial scale dependence and the need for a strong trivial baseline.

**Method.** Controlled operator-learning experiment with spatial-scale diagnostics.

**Outcome.** A falsifiable scientific-ML comparison centred on where the complex model actually earns its place.

## [energy-system-simulator](https://github.com/DiogoRibeiro7/energy-system-simulator)

**Problem.** Choose feasible electricity dispatch under intertemporal physical and economic constraints.

**Constraints.** Unit commitment, ramping, minimum up/down time, storage, hydro, imports and demand response.

**Method.** Explicit optimisation rather than a learned surrogate.

**Outcome.** A decision system that produces operational schedules and exposes the constraints driving them.

## [portugal-public-pension-financing](https://github.com/DiogoRibeiro7/portugal-public-pension-financing)

**Problem.** Determine how Portugal's public pension promise was financed across institutional regimes.

**Constraints.** Legal changes, accounting consolidation, transfers, actuarial liabilities and historical comparability.

**Method.** Auditable legal/accounting data model with explicit measurement boundaries.

**Outcome.** A research framework where definitions and provenance are part of the estimand rather than preprocessing details.

---

This page is generated from `data/portfolio.json`; it is intentionally limited to a handful of cases with a clear problem-to-outcome chain.
