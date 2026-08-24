# Diogo Ribeiro

**Lead Data Scientist · AI Engineer · Professor · Mathematical Engineer**  
Working between the United Kingdom and Portugal · Python (typed, NumPy-first) · production AI + reproducible research

<div align="center">
  <img src="https://img.shields.io/badge/Home-1F6FEB?style=for-the-badge" alt="Home (current page)" />
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/PROJECTS.md"><img src="https://img.shields.io/badge/Projects-30363D?style=for-the-badge" alt="Projects" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/METHODS.md"><img src="https://img.shields.io/badge/Methods-30363D?style=for-the-badge" alt="Methods" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/RESEARCH.md"><img src="https://img.shields.io/badge/Research-30363D?style=for-the-badge" alt="Research" /></a>
  <a href="https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/TEACHING.md"><img src="https://img.shields.io/badge/Teaching-30363D?style=for-the-badge" alt="Teaching" /></a>
</div>

> "Knowledge is knowing a tomato is a fruit; wisdom is not putting it in a fruit salad."
> — Miles Kington

I build production systems that turn complex data into reliable decisions, and reproducible research pipelines that turn open data into auditable evidence. My work spans end-to-end AI systems (LLMs, RAG, agents, and MCP tooling), forecasting and anomaly detection, reliability under distribution shift, and a growing body of econometric and dynamical-systems research on inequality, wealth, and public finance — including audits of what published figures and official statistics actually measure. When a method I need is missing from the Python ecosystem, I build it, test it against the reference implementation, and publish it. Across all of it the constants are the same: lean models, robust software practice, and results you can reproduce and defend.

<p align="center">
  <img src="data_has_a_better_idea.png"
       alt="Poster with the phrase 'Data has a better idea'"
       title="Data has a better idea"
       width="75%" />
</p>

---

## What I Work On

- **Production AI & LLM systems**  
  RAG pipelines, agentic workflows, MCP servers, structured outputs, evaluation loops, and audit-friendly narrative reporting — plus parameter-efficient fine-tuning (LoRA/QLoRA) judged on execution-grounded accuracy rather than text similarity, and guardrails for PII redaction and prompt injection. Designed for reliability, observability, and CI from the start.
- **Data science & statistical modelling**  
  The full toolkit: supervised and unsupervised learning, causal inference and experimentation, survival analysis, Bayesian modelling, and robust/heavy-tailed statistics.  
  With a working emphasis on the parts most people skip — uncertainty quantification and calibration, class imbalance, cost-sensitive decision thresholds, power analysis and variance reduction, interpretability and fairness, leakage and drift checks, and honest model selection under real-world noise.
- **Forecasting, anomaly detection & reliability under shift**  
  Classical and foundation-model time series (SARIMAX/Prophet through Chronos and masked-patch transformers), conformal prediction intervals, change-point and rare-event detection, extreme-value methods for pre-failure signals, and drift monitoring for operational and sensor-driven systems — extending into selective prediction, where a model with poor source–target overlap abstains instead of guessing.
- **Econometrics & reproducible policy research**  
  Panel and causal models, event studies, synthetic control, configurational methods (csQCA/fsQCA), and Monte Carlo simulation over open economic data (Eurostat, OECD, AMECO, WID, INE/PORDATA, FRED) — including replication and extension of published results under explicit provenance labels, and methodological audits that separate accounting boundaries, cash flows, and actuarial liabilities before any number is called a deficit or a subsidy.
- **Optimisation & decision systems**  
  Turning forecasts into decisions: MILP unit commitment for hybrid power systems, perishable inventory and replenishment policy, project scheduling under financial and fuzzy uncertainty, and cost-weighted operating thresholds.
- **Dynamical systems & scientific computing**  
  Attractor dynamics, dynamical-systems econometrics, extreme-value and large-deviation methods, physics-informed neural networks and PDE solvers, neural operators for geophysical fields, and exact algorithmic solvers.
- **Data & ML engineering**  
  Contract-linked ingestion, dataset curation, streaming and lakehouse patterns, and reproducible project scaffolding.

→ Full stack and model families on the **[Methods](https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/METHODS.md)** tab.

---

## Current Focus

- Production RAG and agentic systems with evaluation, observability, and CI baked in — including MCP-exposed data agents and parameter-efficient fine-tuning benchmarked on execution accuracy
- Portuguese public finance under audit: the general-government balance by subsector since 1977, how the public pension promise (CGA, Social Security, and transferred banking-sector liabilities) was actually financed, and a methodological audit of the 2026 pension reform report
- What official statistics measure: which population figure a published GDP-per-capita index is really divided by, how growth and productivity transmit into real wages, and what the Portuguese salary distribution looks like when fitted rather than averaged
- Reproducible econometric research on inequality, wealth concentration, and public policy — including dynamical-systems models of rentier equilibria and crisis dynamics
- Portuguese and European economic history: minimum wages against productivity and inflation since 1974, the public-debt interest burden, and external growth linkages in 1960–1973
- Configurational methods in Python — a native, typed csQCA/fsQCA implementation validated against the reference R package, and a survey-design-aware fsQCA study of firm innovation across the EU-27
- Replication-grade empirical work: rebuilding published results with provenance labels, frozen artifacts, and adversarial release gates rather than transcribed tables
- Reliability under distribution shift: conformal coverage with explicit abstention, survival-model drift monitoring on replayable telemetry, and cost-weighted operating thresholds
- Environmental and energy exposure: urban heat island exposure in Porto and Lisbon, refining capacity and fuel-price transmission, and neural-operator forecasting of real sea-surface temperature fields
- Reusable research infrastructure: contract-linked ETL, GitHub Actions tooling, and reproducibility contracts across multi-paper programmes

---

## Flagship Work

Eight projects that cover the range. The full catalogue — around 70 curated repositories across AI, ML engineering, deep learning, data engineering, statistics, economics, optimisation, algorithms, and tooling — is on the **[Projects](https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/PROJECTS.md)** tab.

- **[feedback-intelligence-agent](https://github.com/DiogoRibeiro7/feedback-intelligence-agent)** — Production-style RAG system: a customer feedback intelligence agent with FastAPI, evaluation, observability, and CI.
- **[ragops-lab](https://github.com/DiogoRibeiro7/ragops-lab)** — Evaluation-first RAG and LLMOps platform for production-grade document QA: tracing, regression testing, and cost-aware experimentation.
- **[hf-data-agent](https://github.com/DiogoRibeiro7/hf-data-agent)** — Internal data agent where UI, HTTP, local and remote MCP, and Slack all funnel into one Agent API, grounding an open-source Hugging Face model in a company knowledge base while pulling live numbers from the data platform.
- **[clinic-forecasting-platform](https://github.com/DiogoRibeiro7/clinic-forecasting-platform)** — Healthcare demand-forecasting and staffing platform: a 13-model benchmark (SARIMAX, Prophet, gradient boosting, Nixtla, Chronos) with conformal intervals, rolling-origin backtesting, and FastAPI serving.
- **[transaction-risk-lakehouse](https://github.com/DiogoRibeiro7/transaction-risk-lakehouse)** — Production-style PySpark lakehouse for transaction-risk modelling, fraud detection, and temporal model validation.
- **[setqca](https://github.com/DiogoRibeiro7/setqca-python)** — Native, typed Python implementation of crisp-set and fuzzy-set QCA with exact Boolean minimisation — not an R wrapper. Conservative, parsimonious, and intermediate solutions match the reference R `QCA` package on the canonical Lipset datasets, with the single divergence documented rather than hidden; published on PyPI with a DOI.
- **[portugal-public-pension-financing](https://github.com/DiogoRibeiro7/portugal-public-pension-financing)** — How the public pension promise was financed over time, tracing CGA, Social Security, and the 2009–2012 transfer of banking-sector liabilities through the actual legal sequence — distinguishing legal obligations, cash accounting, consolidated flows, and actuarial liabilities before calling any balance a deficit, a surplus, or a subsidy.
- **[bmssp](https://github.com/DiogoRibeiro7/bmssp)** ⭐ — Deterministic Single-Source Shortest Paths solver for directed graphs with non-negative weights, using a BMSSP-style divide-and-conquer design (typed, tested).

**Live dashboards:** [Portugal Economic Indicators](https://portugal-econ-dashboard.vercel.app/) · [NASDAQ Stock Analytics](https://nasdaq-dashboard-sigma.vercel.app/)

---

## Research, Collaboration & Teaching

I research inequality and political economy, public finance and official statistics, applied econometrics and empirical finance, configurational methods, dynamical systems, production AI, time series and anomaly detection, and survival analysis — mostly organised as multi-paper programmes with a shared pipeline and reproducibility contract. I teach mathematics and data subjects at ESMAD (Instituto Politécnico do Porto) and run seminars on MLOps, streaming analytics, experimentation, and forecasting.

→ **[Research & Collaboration](https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/RESEARCH.md)** for research themes and what I am open to working on.  
→ **[Teaching](https://github.com/DiogoRibeiro7/diogoribeiro7/blob/main/TEACHING.md)** for courses, workshops, and course repositories.

When reaching out, include a short note on your use case, constraints, and timeline so we can assess fit quickly.

---

## GitHub Stats

### 2026 Highlights (public + private work)

- **Production AI:** shipped RAG and agent systems (`feedback-intelligence-agent`, `ragops-lab`, `ai-incident-analysis-agent`, `hf-data-agent`) — with evaluation, tracing, observability, and CI treated as first-class, and MCP as a first-class entrypoint alongside HTTP and Slack.
- **LLM engineering beyond retrieval:** ran a controlled LoRA/QLoRA adaptation study on Qwen3.5-4B scored by execution accuracy against a live database rather than string overlap (`qwen-text2sql-lab`), and extracted offline-testable RAG engineering primitives — guardrails, PII redaction, injection checks, judge and telemetry helpers — into a standalone package (`genai-rag-engineering`).
- **ML & data engineering:** built serving, MLOps, and lakehouse/streaming platforms (`fastapi-ml-platform`, `feature-store-lab`, `transaction-risk-lakehouse`, `pyflink-fraud-detection-streaming`, `llm-data-platform`) spanning inference, drift monitoring, feature parity, and contract-linked ingestion.
- **Research programmes at scale:** launched a cluster of reproducible econometric and dynamical-systems projects on inequality, wealth, and policy, several sharing a single pipeline and reproducibility contract across many papers — extended this half into Portuguese economic history and public finance (`portugal-minimum-wage-inflation`, `portugal-public-debt-interest`, `portugal-external-growth-1960-1973`), replication-grade empirical asset pricing (`short-rate-anomaly-regimes`), and methodological work on simulated-likelihood asymptotics for multidimensional diffusions (`sml_diffusions_paper`).
- **Public finance and official statistics under audit:** opened a Portuguese fiscal cluster that takes definitions as the object of study — the general-government balance by subsector 1977–2025 (`portugal-fiscal-balance`), the financing history of the pension promise (`portugal-public-pension-financing`), a chapter-by-chapter audit of the 2026 pension reform report (`portugal-pension-boundaries`), which of two official population figures a GDP-per-capita index is actually divided by (`portugal-gdp-bayesian-revision`), and growth-to-wage transmission and salary distributions (`gdp-wage-transmission`, `pt-salary-gamma-distribution`).
- **Reliability under distribution shift:** built systems that decline to answer when the evidence runs out — overlap-aware conformal prediction with explicit abstention (`shiftguard`), survival-model drift monitoring on replayable Backblaze telemetry with rollout and rollback controls (`survdrift`), and cost-weighted maintenance thresholds (`scania-aps-cost`).
- **Published research software:** `setqca` on PyPI — a native csQCA/fsQCA implementation validated against the reference R package — alongside `gen_surv` and typed, tested solvers and libraries (`bmssp`, `min_ratio_cycle`, `heavytails`, `dynamical_systems_econometrics`), with a growing set of repositories archived under Zenodo DOIs.
- **Decision & optimisation systems:** built simulators and policy layers that end in a decision, not a metric (`energy-system-simulator` unit commitment, `perishable-inventory-decision-lab` replenishment policy, `experimentation-toolkit` power, CUPED and sample-ratio checks for experiment design).
- **Scientific & deep-learning research:** ran reproducible architecture, PDE, and operator labs with baselines, ablations, and audited claims (`modern-neural-networks-agent-repo`, `anomaly-transformer-lab`, `pinn`, `pinn-rk`, `torch-namo-optim`, `oisst-fourier-neural-operator`) — the last asking the narrow, falsifiable question of when a Fourier Neural Operator actually beats persistence on real NOAA sea-surface temperatures, and at which spatial scales.
- **Environment & energy exposure:** measured who is exposed and what cools them — urban heat island exposure across Porto and Lisbon population grids, where green cover correlates negatively with modelled UHI intensity in both cities (`porto-lisbon-uhi-exposure`) — alongside refining capacity, fuel-trade dependence, and price transmission (`portugal-refining-resilience`).
- **Reusable infrastructure:** built developer tooling (`smart-todo-action`, `git-actions-collection`, `repo-task-tracker`, `article-reminders`) to keep a large, multi-repo research output reproducible and maintainable.

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
