<div align="center">
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/README.md"><img src="https://img.shields.io/badge/Home-30363D?style=for-the-badge" alt="Home" /></a>
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

**13 end-to-end cases across 11 domains.**

Case studies are selective, but they are drawn from the full portfolio rather than only the flagship list. Each case has to show a genuine chain from problem and constraints through method to an inspectable outcome or decision.

## Production AI

### [Feedback intelligence agent](https://github.com/DiogoRibeiro7/feedback-intelligence-agent)

**Problem.** Turn unstructured customer feedback into traceable, queryable evidence.

**Constraints.** Ground answers in retrieved evidence, measure retrieval quality, expose latency/cost and support production serving.

**Method.** RAG pipeline with FastAPI, evaluation, observability and CI.

**Outcome.** A production-style feedback intelligence system whose answer quality can be tested rather than asserted.

## LLM adaptation

### [Qwen text-to-SQL adaptation](https://github.com/DiogoRibeiro7/qwen-text2sql-lab)

**Problem.** Determine whether parameter-efficient fine-tuning actually improves text-to-SQL execution.

**Constraints.** Avoid string-match evaluation, control data volume and adapter capacity, and compare against the untouched base model.

**Method.** Controlled LoRA/QLoRA experiments scored by execution accuracy against the target database.

**Outcome.** A falsifiable model-adaptation study showing where fine-tuning earns its cost.

## Forecasting & MLOps

### [Clinic forecasting platform](https://github.com/DiogoRibeiro7/clinic-forecasting-platform)

**Problem.** Forecast healthcare demand while supporting staffing decisions under uncertainty.

**Constraints.** Temporal leakage, multiple forecasting families, uncertainty intervals and production monitoring.

**Method.** Rolling-origin benchmark across thirteen models with conformal intervals and serving.

**Outcome.** A full forecast-to-operation workflow rather than a single accuracy leaderboard.

## Data engineering

### [Transaction risk lakehouse](https://github.com/DiogoRibeiro7/transaction-risk-lakehouse)

**Problem.** Build a reproducible risk/fraud modelling pipeline on transaction data.

**Constraints.** Large-scale processing, temporal validation and separation between data-engineering and modelling concerns.

**Method.** PySpark lakehouse with temporal model evaluation and production-style data contracts.

**Outcome.** An end-to-end risk platform where model evidence is tied to the data pipeline that produced it.

## Scientific ML

### [FNO versus persistence on NOAA OISST](https://github.com/DiogoRibeiro7/oisst-fourier-neural-operator)

**Problem.** Test whether an FNO materially improves seven-day SST field forecasts over persistence.

**Constraints.** Real NOAA data, spatial scale dependence and the need for a strong trivial baseline.

**Method.** Controlled operator-learning experiment with spatial-scale diagnostics.

**Outcome.** A falsifiable scientific-ML comparison centred on where the complex model actually earns its place.

## Optimisation

### [Energy-system dispatch](https://github.com/DiogoRibeiro7/energy-system-simulator)

**Problem.** Choose feasible electricity dispatch under intertemporal physical and economic constraints.

**Constraints.** Unit commitment, ramping, minimum up/down time, storage, hydro, imports and demand response.

**Method.** Explicit optimisation rather than a learned surrogate.

**Outcome.** A decision system that produces operational schedules and exposes the constraints driving them.

## Decision science

### [Perishable inventory replenishment](https://github.com/DiogoRibeiro7/perishable-inventory-decision-lab)

**Problem.** Convert uncertain demand forecasts into replenishment decisions for perishable goods.

**Constraints.** Censoring, spoilage, leakage-safe forecasting and asymmetric inventory costs.

**Method.** Calibrated probabilistic forecasting coupled to inventory simulation and policy comparison.

**Outcome.** Forecast quality is judged through the downstream replenishment policy rather than forecast error alone.

## Industrial ML

### [Scania APS maintenance decisions](https://github.com/DiogoRibeiro7/scania-aps-cost)

**Problem.** Detect costly truck failures without optimising the wrong classification metric.

**Constraints.** Extreme class imbalance and a 10×FP + 500×FN maintenance-cost structure.

**Method.** Calibration, imbalance handling, representation learning and threshold selection against explicit cost.

**Outcome.** Model selection becomes an operating-cost decision rather than an accuracy contest.

## Mobility decision systems

### [Probabilistic taxi fleet allocation](https://github.com/DiogoRibeiro7/ds-projects-portfolio/tree/main/projects/mobility_demand_optimization)

**Problem.** Allocate a finite taxi fleet spatially under uncertain hourly demand.

**Constraints.** Real geography, fleet conservation, policy-dependent state propagation and trip-duration availability.

**Method.** Probabilistic count forecasting feeding constrained allocation and rolling fleet-state simulation.

**Outcome.** Forecasts are evaluated by service level, regret and operating cost, exposing when better uncertainty modelling does not imply a better decision policy.

## Public finance

### [Portuguese public pension financing](https://github.com/DiogoRibeiro7/portugal-public-pension-financing)

**Problem.** Determine how Portugal's public pension promise was financed across institutional regimes.

**Constraints.** Legal changes, accounting consolidation, transfers, actuarial liabilities and historical comparability.

**Method.** Auditable legal/accounting data model with explicit measurement boundaries.

**Outcome.** A research framework where definitions and provenance are part of the estimand rather than preprocessing details.

### [Portugal general-government balance](https://github.com/DiogoRibeiro7/portugal-fiscal-balance)

**Problem.** Measure how the general-government balance is formed across institutional subsectors over time.

**Constraints.** Changing statistical definitions, intra-government transfers and long historical coverage.

**Method.** Subsector accounting reconstruction with explicit consolidation rules and source provenance.

**Outcome.** A reproducible decomposition of the balance without inferring political intent from accounting aggregates.

## Labour economics

### [Minimum wage and price pass-through](https://github.com/DiogoRibeiro7/portugal-minimum-wage-inflation)

**Problem.** Estimate how minimum-wage changes interact with productivity and consumer prices in Portugal.

**Constraints.** Long-run structural change, regional/industry exposure and the Madeira/Azores differentiation.

**Method.** Growth accounting plus exposure-based pass-through designs.

**Outcome.** A research design that separates national co-movement from heterogeneous exposure to policy changes.

### [GDP–wage transmission](https://github.com/DiogoRibeiro7/gdp-wage-transmission)

**Problem.** Estimate how growth and productivity transmit into real wages and whether that relationship changes.

**Constraints.** Non-stationarity, measurement mismatch, structural breaks and time-varying transmission.

**Method.** ECM, state-space modelling, break analysis and cross-country robustness checks.

**Outcome.** A layered estimate of long-run and evolving wage transmission rather than a single correlation.
