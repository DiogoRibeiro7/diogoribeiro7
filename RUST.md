# Rust Packages

A small collection of Rust libraries focused on statistical computing, numerical methods, and reliable data-science infrastructure.

All packages are currently pre-1.0 and should be treated as evolving research or engineering software.

## Packages

| Package | Version | Focus | Repository |
| :-- | :--: | :-- | :-- |
| **copula-core** | `0.2.0` | Copula modelling, simulation, and dependence analysis for statistical and risk applications. | **[DiogoRibeiro7/copula-core](https://github.com/DiogoRibeiro7/copula-core)** |
| **uncertain-numerics** | `0.1.0` | Probabilistic numerical methods with explicit uncertainty over computational quantities. | **[DiogoRibeiro7/uncertain-numerics](https://github.com/DiogoRibeiro7/uncertain-numerics)** |
| **modelguard** | `0.1.0` | Rust-native model and data validation for tabular data-science workflows, including metrics and drift-oriented tooling. | **[DiogoRibeiro7/modelguard-rs](https://github.com/DiogoRibeiro7/modelguard-rs)** |

## Why Rust Here

These packages target parts of scientific and statistical software where correctness, predictable performance, explicit APIs, and strong compile-time guarantees matter. The goal is not to replace Python as the main modelling environment, but to use Rust where a reusable numerical or validation core benefits from stricter invariants and lower-level control.

## Package Notes

### copula-core

`copula-core` provides foundations for copula-based dependence modelling and simulation. Its current scope includes statistical dependence analysis, sampling, optional parameter estimation, serialization support, tests, property-based testing, and benchmarking.

### uncertain-numerics

`uncertain-numerics` explores numerical computation in which uncertainty about the numerical result is represented explicitly. The project is aimed at probabilistic numerical methods, with Bayesian quadrature and Gaussian-process-based numerical inference as natural extensions of the core design.

### modelguard

`modelguard` is a Rust-native validation layer for data-science workflows. It is designed around tabular validation and model-facing checks, with optional integrations for Arrow, DataFusion, Parquet, Polars, JSON, and command-line use.

---

← **[Back to profile](README.md)** · **[Projects](PROJECTS.md)** · **[Methods](METHODS.md)** · **[Outputs](OUTPUTS.md)**
