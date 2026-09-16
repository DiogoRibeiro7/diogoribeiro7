<div align="center">
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/README.md"><img src="https://img.shields.io/badge/Home-30363D?style=for-the-badge" alt="Home" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/FEATURED.md"><img src="https://img.shields.io/badge/Featured-30363D?style=for-the-badge" alt="Featured" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/PROJECTS.md"><img src="https://img.shields.io/badge/Projects-30363D?style=for-the-badge" alt="Projects" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/METHODS.md"><img src="https://img.shields.io/badge/Methods-30363D?style=for-the-badge" alt="Methods" /></a>
  <img src="https://img.shields.io/badge/Research-1F6FEB?style=for-the-badge" alt="Research (current page)" />
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/OUTPUTS.md"><img src="https://img.shields.io/badge/Outputs-30363D?style=for-the-badge" alt="Outputs" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/CASE_STUDIES.md"><img src="https://img.shields.io/badge/Case%20Studies-30363D?style=for-the-badge" alt="Case Studies" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/TEACHING.md"><img src="https://img.shields.io/badge/Teaching-30363D?style=for-the-badge" alt="Teaching" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/PYPI.md"><img src="https://img.shields.io/badge/PyPI-30363D?style=for-the-badge&logo=pypi&logoColor=white" alt="PyPI" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/STATISTICS.md"><img src="https://img.shields.io/badge/Statistics-30363D?style=for-the-badge" alt="Statistics" /></a>
</div>

---

# Research Programme

I work on research problems where the difficult part is usually not fitting one more model. It is defining the object being measured, separating competing explanations, designing falsifiable checks, and leaving enough evidence that somebody else can reproduce or challenge the result.

The table below lists the public research threads I would point a technical reviewer to first. Broader interests come later; public inspectability comes first.

## Current focus

| Programme | Research question | Evidence now | Status |
| :-- | :-- | :-- | :-- |
| **[Failure-aware behavioural sensing](https://github.com/DiogoRibeiro7/behavioral-sensing-research)** | How can a sensing system distinguish sensor failure, missing evidence, occupancy ambiguity and genuine behavioural change before raising an alert? | Explicit missing-evidence semantics, uncertainty-aware fusion, abstention logic, reproducible simulation and paper-oriented artifacts. | Active research programme |
| **[Survival discrimination vs calibration](https://github.com/DiogoRibeiro7/genSurvPy/tree/develop/research/discrimination-not-calibration)** | When do ranking metrics, probability accuracy, censoring and model misspecification tell different stories about survival-model quality? | Known-truth simulation built on `genSurvPy`, multiple data-generating families, calibration/discrimination comparisons and reproducible experiments. | Active simulation study |
| **[Portuguese public pension financing](https://github.com/DiogoRibeiro7/portugal-public-pension-financing)** | How were pension promises actually financed across Social Security, CGA and transferred sectoral liabilities, and which accounting boundaries matter? | Legal, accounting and actuarial reconstruction with explicit institutional boundaries and reproducible source handling. | Active research programme |
| **[GDP–wage transmission](https://github.com/DiogoRibeiro7/gdp-wage-transmission)** | How do growth and productivity transmit into real wages over time, and where do structural breaks or state changes alter that relationship? | Long-run empirical pipeline, structural-break analysis, ECM/state-space work and reproducible country-level evidence. | Active research programme |
| **[Portugal fiscal balance](https://github.com/DiogoRibeiro7/portugal-fiscal-balance)** | What does the general-government balance look like once Central, Regional/Local and Social Security subsectors are separated consistently over time? | Reproducible official-statistics pipeline with explicit accounting boundaries and subsector decomposition from 1977 onward. | Empirical study |
| **[Short-rate anomaly regimes](https://github.com/DiogoRibeiro7/short-rate-anomaly-regimes)** | Do published short-rate innovation effects survive replication and regime-sensitive re-analysis? | Frozen artifacts, provenance checks, replication labels, regime analysis and reproducible empirical outputs. | Replication study |
| **[European innovation configurations](https://github.com/DiogoRibeiro7/europe-fsqca-innovation)** | Which combinations of firm and institutional conditions are associated with innovation across the EU-27? | Survey-design-aware fsQCA, explicit calibration, configurational inference and a native Python implementation path through `setqca`. | Empirical study |
| **[FNO vs persistence on NOAA OISST](https://github.com/DiogoRibeiro7/oisst-fourier-neural-operator)** | At what spatial scales does a Fourier Neural Operator earn its complexity over persistence and classical baselines? | Real NOAA sea-surface-temperature data, explicit baselines, controlled evaluation and reproducible empirical comparisons. | Empirical study |

---

## Research standards

My research workflow is organised around a small set of rules that are meant to survive contact with reviewers, collaborators and future reruns.

1. **Define the estimand before choosing the model.** Measurement boundaries, target populations, time windows and decision variables are part of the research design.
2. **Build the strongest simple baseline first.** More complex models only matter if they improve the quantity the study actually cares about.
3. **Separate identification from prediction.** Good predictive performance does not by itself establish a causal, structural or policy claim.
4. **Treat falsification as part of the result.** Placebo tests, sensitivity analyses, known-truth simulation, alternative specifications and adversarial checks are not optional decoration.
5. **Represent uncertainty explicitly.** Calibration, interval quality, censoring, missingness, instability and regime uncertainty should be visible in the final claim.
6. **Keep provenance inspectable.** Data sources, transformations, configurations, seeds and generated artifacts should be traceable rather than reconstructed from prose.
7. **Distinguish replication, extension and new evidence.** Reproducing a pattern, matching a published table and extending a study are different claims and should be labelled accordingly.

---

## Recurring research themes

These are the broader problem families behind the active programmes above.

- **Public finance and official statistics** — accounting boundaries, fiscal subsectors, pension financing, debt-service burdens and denominator audits.
- **Applied econometrics and economic history** — long-run transmission, structural breaks, event studies, synthetic controls, historical reconstruction and open-data provenance.
- **Statistical reliability** — calibration, uncertainty, missing evidence, distribution shift, selective prediction and known-truth simulation.
- **Configurational methods** — csQCA/fsQCA, calibration, Boolean minimisation and multi-country comparative designs.
- **Time series and dynamical systems** — state-space models, change points, rare events, regime shifts and nonlinear dynamics.
- **Scientific machine learning** — physics-informed models, neural operators and controlled comparisons against classical numerical or statistical baselines.
- **Production AI evaluation** — retrieval quality, grounded generation, execution-based evaluation, observability and regression testing for LLM systems.
- **Decision systems** — connecting forecasts or risk estimates to constrained optimisation, operating thresholds and measurable downstream decisions.

---

## Research infrastructure

I prefer research programmes to one-off notebooks. A typical project has four layers:


dataset provenance → validated transformations → statistical or computational experiment → frozen outputs


That usually means typed pipelines, tests for transformations, CI, fixed experiment configurations, machine-readable result artifacts and a clear separation between generated outputs and hand-written interpretation.

Public examples include [genSurvPy](https://github.com/DiogoRibeiro7/genSurvPy), [setqca](https://github.com/DiogoRibeiro7/setqca-python), [behavioral-sensing-research](https://github.com/DiogoRibeiro7/behavioral-sensing-research), [portugal-public-pension-financing](https://github.com/DiogoRibeiro7/portugal-public-pension-financing), and [short-rate-anomaly-regimes](https://github.com/DiogoRibeiro7/short-rate-anomaly-regimes).

For released software and citable artifacts, see **[Outputs](OUTPUTS.md)** and **[PyPI](PYPI.md)**. For the modelling choices behind the work, see **[Methods](METHODS.md)**.

---

## Collaboration

I am most interested in collaborations where the technical problem is clear enough to be falsifiable and important enough that reproducibility matters. Typical fits include reproducible econometric or policy research, statistical method validation, survival and longitudinal modelling, time-series reliability, scientific ML, configurational methods, forecast-to-decision systems, and evaluation of production AI systems.

The best starting point is a short description of the research question, available data, constraints, and what would count as convincing evidence.

**Contact:** [diogo.debastos.ribeiro@gmail.com](mailto:diogo.debastos.ribeiro@gmail.com) · [LinkedIn](https://www.linkedin.com/in/diogo-ribeiro-9094604a/)

---

<div align="center">
  <a href="https://github.com/DiogoRibeiro7"><img src="https://img.shields.io/badge/%E2%86%90%20Back%20to%20profile-30363D?style=for-the-badge" alt="Back to profile" /></a>
</div>
