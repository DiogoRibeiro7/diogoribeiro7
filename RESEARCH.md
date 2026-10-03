<div align="center">
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/README.md"><img src="assets/links/nav-home.svg" alt="Home" width="96" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/FEATURED.md"><img src="assets/links/nav-featured.svg" alt="Featured" width="116" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/PROJECTS.md"><img src="assets/links/nav-projects.svg" alt="Projects" width="112" height="40" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/METHODS.md"><img src="assets/links/nav-methods.svg" alt="Methods" width="112" height="40" /></a>
  <img src="assets/links/nav-research-active.svg" alt="Research (current page)" width="120" height="40" />
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/STATISTICS.md"><img src="assets/links/nav-evidence.svg" alt="Evidence" width="120" height="40" /></a>
</div>

---

# Research Programme

I work on problems where the difficult part is usually not fitting one more model. It is defining what is being measured, identifying which assumptions make the claim possible, separating competing explanations, and leaving enough evidence that somebody else can reproduce or challenge the result.

The research programme spans statistical methodology, causal inference and econometrics, time series and monitoring, behavioural sensing, spatial and policy analysis, scientific machine learning, and research software. The common standard is narrower: the question must be falsifiable, the evidence traceable, and the model no more complicated than the claim requires.

## Current focus

| Programme | Research question | Evidence now | Status |
| :-- | :-- | :-- | :-- |
| **Causal inference and policy evaluation** | How should causal claims be built when treatment assignment is non-random, identifying assumptions are fragile, and estimator performance can look good even when the design is wrong? | Public evidence spans [minimum-wage pass-through](https://github.com/DiogoRibeiro7/portugal-minimum-wage-inflation), [GDP–wage transmission](https://github.com/DiogoRibeiro7/gdp-wage-transmission), [causal uplift](https://github.com/DiogoRibeiro7/causal-uplift-marketing-campaign), and [effect comparability](https://github.com/DiogoRibeiro7/effectbridge), with identification assumptions, counterfactual design, robustness checks, and sensitivity analysis kept separate from predictive performance. | Active methodological thread |
| **[Failure-aware behavioural sensing](https://github.com/DiogoRibeiro7/behavioral-sensing-research)** | How can a sensing system distinguish sensor failure, missing evidence, occupancy ambiguity, and genuine behavioural change before raising an alert? | Explicit missing-evidence semantics, uncertainty-aware fusion, abstention logic, reproducible simulation, and paper-oriented artifacts. | Active research programme |
| **[Population drift and structural change](https://github.com/DiogoRibeiro7/population-resemblance)** · **[ChangePointLab](https://github.com/DiogoRibeiro7/ChangePointLab)** | How should gradual population shift and abrupt structural change be detected, calibrated, and interpreted without turning every discrepancy into a model-failure claim? | Population Resemblance Statistic with sample-size-aware thresholds, PSI/KS benchmarks, Monte Carlo calibration, plus offline, online, Bayesian, kernel, and state-space changepoint methods. | Active methods programme |
| **[Survival discrimination vs calibration](https://github.com/DiogoRibeiro7/genSurvPy/tree/develop/research/discrimination-not-calibration)** | When do ranking metrics, probability accuracy, censoring, and model misspecification tell different stories about survival-model quality? | Known-truth simulation built on `genSurvPy`, multiple data-generating families, calibration/discrimination comparisons, and reproducible experiments. | Active simulation study |
| **[Lisbon spatial dynamics](https://github.com/DiogoRibeiro7/lisbon-spatial-dynamics)** | How are changes in housing values associated with local-accommodation pressure across Lisbon's parishes, and how sensitive are those associations to spatial dependence, registry completeness, and small-sample influence? | Official Portuguese sources, parish-level panels, Moran/LISA diagnostics, robust regression, leave-one-parish-out sensitivity, provenance records, and explicit limits on causal interpretation. | Active empirical programme |
| **[Portuguese public pension financing](https://github.com/DiogoRibeiro7/portugal-public-pension-financing)** | How were pension promises financed across Social Security, CGA, and transferred sectoral liabilities, and which accounting boundaries matter? | Legal, accounting, and actuarial reconstruction with explicit institutional boundaries and reproducible source handling. | Active research programme |
| **[GDP–wage transmission](https://github.com/DiogoRibeiro7/gdp-wage-transmission)** | How do growth and productivity transmit into real wages over time, and where do structural breaks or state changes alter that relationship? | Long-run empirical pipeline, structural-break analysis, ECM/state-space work, and reproducible country-level evidence. | Active research programme |
| **[Portugal fiscal balance](https://github.com/DiogoRibeiro7/portugal-fiscal-balance)** | What does the general-government balance look like once Central, Regional/Local, and Social Security subsectors are separated consistently over time? | Reproducible official-statistics pipeline with explicit accounting boundaries and subsector decomposition from 1977 onward. | Empirical study |
| **[European innovation configurations](https://github.com/DiogoRibeiro7/europe-fsqca-innovation)** | Which combinations of firm and institutional conditions are associated with innovation across the EU-27? | Survey-design-aware fsQCA, explicit calibration, configurational inference, and a native Python implementation path through `setqca`. | Empirical study |
| **[FNO vs persistence on NOAA OISST](https://github.com/DiogoRibeiro7/oisst-fourier-neural-operator)** | At what spatial scales does a Fourier Neural Operator earn its complexity over persistence and classical baselines? | Real NOAA sea-surface-temperature data, explicit baselines, controlled evaluation, and reproducible empirical comparisons. | Empirical study |

---

## Research standards

My research workflow is organised around rules that are meant to survive contact with reviewers, collaborators, and future reruns.

1. **Define the estimand before choosing the estimator.** Target populations, measurement boundaries, time windows, treatment definitions, and decision variables are part of the model.
2. **Identification comes before estimation.** A sophisticated estimator cannot repair a design that does not support the causal or structural claim being made.
3. **Build the strongest simple baseline first.** More complex models matter only when they improve the quantity the study actually cares about.
4. **Match validation to the data-generating process.** Time, groups, censoring, spatial dependence, treatment assignment, and repeated measurements must survive into the validation design.
5. **Treat falsification as part of the result.** Placebos, negative controls, sensitivity analyses, known-truth simulation, alternative specifications, and deliberately broken assumptions are useful evidence.
6. **Represent uncertainty explicitly.** Calibration, interval quality, censoring, missingness, weak overlap, spatial uncertainty, and regime instability should be visible in the final claim.
7. **Keep provenance inspectable.** Data sources, transformations, configurations, seeds, checksums, and generated artifacts should be traceable rather than reconstructed from prose.
8. **Distinguish replication, extension, association, prediction, and causal evidence.** These are different claims and should be labelled as such.

---

## Recurring research themes

- **Causal inference and econometrics** — potential outcomes, panel designs, DiD and event studies, synthetic control, RDD, IV, doubly robust estimation, causal ML, negative controls, and sensitivity analysis.
- **Public finance and official statistics** — accounting boundaries, fiscal subsectors, pension financing, debt-service burdens, denominator audits, and reproducible use of administrative statistics.
- **Spatial and urban analysis** — small-area measurement, spatial autocorrelation, neighbourhood heterogeneity, registry completeness, robust regression, and uncertainty about geographic assignment.
- **Statistical reliability and monitoring** — calibration, uncertainty, missing evidence, population drift, changepoints, selective prediction, and known-truth simulation.
- **Applied econometrics and economic history** — long-run transmission, structural breaks, historical reconstruction, counterfactual design, and open-data provenance.
- **Configurational methods** — csQCA/fsQCA, calibration, Boolean minimisation, and multi-country comparative designs.
- **Time series and dynamical systems** — state-space models, change points, rare events, regime shifts, nonlinear dynamics, and forecast-to-decision evaluation.
- **Scientific machine learning** — physics-informed models, neural operators, and controlled comparisons against classical numerical or statistical baselines.
- **Production AI evaluation** — retrieval quality, grounded generation, execution-based evaluation, observability, and regression testing for LLM systems.
- **Decision systems** — connecting forecasts or risk estimates to constrained optimisation, operating thresholds, costs, and measurable downstream decisions.

---

## Research infrastructure

I prefer research programmes to one-off notebooks. A typical project keeps the evidence chain explicit:

```text
source + provenance
        ↓
validated data contract
        ↓
estimand / identification / mathematical assumptions
        ↓
statistical or computational experiment
        ↓
diagnostics + falsification + uncertainty
        ↓
frozen machine-readable outputs
        ↓
human interpretation
```

That means typed pipelines where they help, tests for transformations and invariants, CI, fixed experiment configurations, deterministic or seed-controlled simulations, and a clear separation between generated evidence and hand-written interpretation.

The **[data registry](https://github.com/DiogoRibeiro7/data)** now provides a reusable layer for canonical datasets and external sources: provenance, licensing, metadata, SHA-256 integrity checks, immutable consumer references, and quarantine for historical material that does not yet satisfy the canonical contract.

Public research-software examples include [genSurvPy](https://github.com/DiogoRibeiro7/genSurvPy), [setqca](https://github.com/DiogoRibeiro7/setqca-python), [ChangePointLab](https://github.com/DiogoRibeiro7/ChangePointLab), [population-resemblance](https://github.com/DiogoRibeiro7/population-resemblance), and [DataConsistencyChecker](https://github.com/DiogoRibeiro7/DataConsistencyChecker). They are not treated as detached libraries: each exists to make a statistical or empirical workflow easier to inspect, test, or reproduce.

For released software and citable artifacts, see **[Outputs](OUTPUTS.md)** and **[PyPI](PYPI.md)**. For modelling choices and validation logic, see **[Methods](METHODS.md)**. Longer-form notes and essays live on my **[website](https://diogoribeiro7.github.io)**.

---

## Collaboration

I am most interested in collaborations where the technical question is clear enough to be falsifiable and important enough that reproducibility matters. Typical fits include causal and econometric research, policy evaluation, statistical method validation, survival and longitudinal modelling, time-series reliability, spatial analysis, scientific ML, configurational methods, forecast-to-decision systems, and evaluation of production AI systems.

The best starting point is a short description of the research question, available data, constraints, identification assumptions where relevant, and what would count as convincing evidence.

**Contact:** [Email](mailto:diogo.debastos.ribeiro@gmail.com) · [LinkedIn](https://www.linkedin.com/in/diogo-ribeiro-9094604a/) · [Website](https://diogoribeiro7.github.io) · [ORCID](https://orcid.org/0009-0001-2022-7072)

---

<div align="center">
  <a href="https://github.com/DiogoRibeiro7"><img src="https://img.shields.io/badge/%E2%86%90%20Back%20to%20profile-30363D?style=for-the-badge" alt="Back to profile" /></a>
</div>
