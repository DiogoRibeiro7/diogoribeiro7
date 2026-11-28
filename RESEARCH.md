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

The hard part is rarely fitting one more model: it is defining what is measured, identifying which assumptions make a claim possible, separating competing explanations, and leaving evidence others can reproduce or challenge. Areas: statistical methodology, causal inference and econometrics, time series and monitoring, behavioural sensing, spatial and policy analysis, scientific ML, research software.

Status below describes current activity, not publication. A repository, manuscript, software release, preprint and peer-reviewed paper are different evidence; none implies another. Some implementations stay private while a manuscript is in preparation. Novelty has to be established against the literature, not inferred from breadth. Public artifacts are indexed in [Outputs](OUTPUTS.md).

## Current focus

| Programme | Research question | Status |
| :-- | :-- | :-- |
| **Causal inference and policy evaluation**: [minimum-wage pass-through](https://github.com/DiogoRibeiro7/portugal-minimum-wage-inflation), [GDP–wage transmission](https://github.com/DiogoRibeiro7/gdp-wage-transmission), [causal uplift](https://github.com/DiogoRibeiro7/causal-uplift-marketing-campaign), [effectbridge](https://github.com/DiogoRibeiro7/effectbridge) | How to build causal claims when assignment is non-random and identifying assumptions are fragile, and keep them apart from predictive performance. | Active methodological thread |
| **[Failure-aware behavioural sensing](https://github.com/DiogoRibeiro7/behavioral-sensing-research)** | How can a sensing system tell sensor failure, missing evidence, occupancy ambiguity and real behavioural change apart before alerting? | Active research programme |
| **[Population drift](https://github.com/DiogoRibeiro7/population-resemblance)** · **[ChangePointLab](https://github.com/DiogoRibeiro7/ChangePointLab)** | How to detect, calibrate and interpret gradual shift and abrupt change without calling every discrepancy a model failure. | Active methods programme |
| **[Survival discrimination vs calibration](https://github.com/DiogoRibeiro7/genSurvPy/tree/develop/research/discrimination-not-calibration)** | When do ranking, probability accuracy, censoring and misspecification tell different stories about survival models? | Active simulation study |
| **[Lisbon spatial dynamics](https://github.com/DiogoRibeiro7/lisbon-spatial-dynamics)** | How are housing-value changes associated with local-accommodation pressure across parishes, and how sensitive is that to spatial dependence and small-sample influence? | Active empirical programme |
| **[Portuguese public pension financing](https://github.com/DiogoRibeiro7/portugal-public-pension-financing)** | How were pension promises financed across Social Security, CGA and transferred sectoral liabilities, and which accounting boundaries matter? | Active research programme |
| **[GDP–wage transmission](https://github.com/DiogoRibeiro7/gdp-wage-transmission)** | How do growth and productivity transmit into real wages, and where do structural breaks change that? | Active research programme |
| **[Portugal fiscal balance](https://github.com/DiogoRibeiro7/portugal-fiscal-balance)** | What does the general-government balance look like with Central, Regional/Local and Social Security subsectors separated consistently since 1977? | Empirical study |
| **[European innovation configurations](https://github.com/DiogoRibeiro7/europe-fsqca-innovation)** | Which firm and institutional conditions combine with innovation across the EU-27? | Empirical study |
| **[FNO vs persistence on NOAA OISST](https://github.com/DiogoRibeiro7/oisst-fourier-neural-operator)** | At what spatial scales does a Fourier Neural Operator earn its complexity over baselines? | Empirical study |

Software behind these: [genSurvPy](https://github.com/DiogoRibeiro7/genSurvPy), [setqca](https://github.com/DiogoRibeiro7/setqca-python), [ChangePointLab](https://github.com/DiogoRibeiro7/ChangePointLab), [population-resemblance](https://github.com/DiogoRibeiro7/population-resemblance), [DataConsistencyChecker](https://github.com/DiogoRibeiro7/DataConsistencyChecker). Released artifacts: [Outputs](OUTPUTS.md), [PyPI](PYPI.md). Modelling choices: [Methods](METHODS.md).

## Standards

1. Define the estimand before the estimator; identification before estimation.
2. Build the strongest simple baseline first.
3. Match validation to the data-generating process.
4. Treat falsification (placebos, negative controls, known-truth simulation, broken assumptions) as part of the result.
5. Show uncertainty: calibration, intervals, censoring, missingness, overlap, regime instability.
6. Keep provenance inspectable: sources, transformations, configurations, seeds, checksums.
7. Label replication, extension, association, prediction and causal evidence as different claims.

## Infrastructure

Projects keep the chain explicit: source and provenance → validated data contract → estimand and assumptions → experiment → diagnostics, falsification and uncertainty → frozen machine-readable outputs → human interpretation. That means typed pipelines, tests for invariants, CI, fixed configurations and seed-controlled simulation.

The **[data registry](https://github.com/DiogoRibeiro7/data)** holds canonical and external datasets with provenance, licensing, metadata, SHA-256 integrity checks, immutable consumer references and quarantine for material that does not meet the contract.

## Collaboration

I look for questions that are falsifiable and where reproducibility matters: causal and econometric research, policy evaluation, method validation, survival and longitudinal modelling, time-series reliability, spatial analysis, scientific ML, forecast-to-decision systems, production-AI evaluation. Send the question, available data, constraints, identification assumptions and what would count as convincing evidence.

**Contact:** [Email](mailto:dfr@esmad.ipp.pt) · [LinkedIn](https://www.linkedin.com/in/diogo-ribeiro-9094604a/) · [Website](https://diogoribeiro7.github.io) · [ORCID](https://orcid.org/0009-0001-2022-7072)

---

<div align="center">
  <a href="https://github.com/DiogoRibeiro7"><img src="https://img.shields.io/badge/%E2%86%90%20Back%20to%20profile-30363D?style=for-the-badge" alt="Back to profile" /></a>
</div>
