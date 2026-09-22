# GW Detector Research — Documentation Repository

This directory contains the research and validation documentation for the
gravitational-wave detector modelling project.

The documentation records how the detector model is developed and validated,
from foundational interferometer physics through gravitational-wave response,
detector noise, spectral analysis, and signal recovery, to public-data
comparison and final integration.

**Start here:** [`MASTER_PLAN.md`](../../MASTER_PLAN.md) — the governing
roadmap for the complete project. This README is a short navigation guide to
the documentation repository.

---

## What this repository contains

The documentation is organized around the project's nine research stages:

```text
Stage 1 → Ideal Michelson Physics
Stage 2 → GW Strain Response
Stage 3 → Polarization & Antenna Response
Stage 4 → Operating Point & Readout
Stage 5 → Physical Noise Models
Stage 6 → PSD / ASD / Sensitivity
Stage 7 → Signal Processing & Recovery
Stage 8 → Public GW Data Validation
Stage 9 → Integrated Model & Final Research Study
```

Stages 1–8 have dedicated validation folders under `docs/validation/`. Stage 9
is the integrated capstone and is documented through the final research
output in `papers/`.

The stages are conceptually sequential, although implementation may overlap
between them.

---

## How the validation work is organized

Each validation stage follows the same overall research cycle:

```text
Physics question
      ↓
Independent derivation
      ↓
Literature support
      ↓
Assumptions & conventions
      ↓
Code / simulation audit
      ↓
Numerical validation
      ↓
Limitations & conclusion
```

The standard documentation set is:

```text
stage-N-<name>/
├── README.md
├── analytical_model.md
├── literature_validation.md
├── code_and_simulation_audit.md
├── numerical_validation.md
└── limitations_and_conclusion.md
```

The detailed purpose and required structure of these documents are defined in
[`MASTER_PLAN.md`](../../MASTER_PLAN.md) §7.

A stage is considered CLOSED only after its required validation work has been
completed and its conclusion establishes the stage's validity boundary.

---

## Stage Index

| Stage | Topic | Documentation |
|---|---|---|
| 1 | Ideal Michelson Physics | [`stage-1-ideal-michelson/`](stage-1-ideal-michelson/) |
| 2 | GW Strain Response | [`stage-2-gw-strain-response/`](stage-2-gw-strain-response/) |
| 3 | Polarization & Antenna Response | [`stage-3-polarization-antenna/`](stage-3-polarization-antenna/) |
| 4 | Operating Point & Readout | [`stage-4-operating-point-readout/`](stage-4-operating-point-readout/) |
| 5 | Physical Noise Models | [`stage-5-physical-noise-models/`](stage-5-physical-noise-models/) |
| 6 | PSD / ASD / Sensitivity | [`stage-6-psd-asd-sensitivity/`](stage-6-psd-asd-sensitivity/) |
| 7 | Signal Processing & Recovery | [`stage-7-signal-processing-recovery/`](stage-7-signal-processing-recovery/) |
| 8 | Public GW Data Validation | [`stage-8-public-data-validation/`](stage-8-public-data-validation/) |
| 9 | Integrated Model & Final Research Study | [`papers/final_research_report.md`](../../papers/final_research_report.md) |

For the authoritative stage descriptions, scope, dependencies, and current
status, see [`MASTER_PLAN.md`](../../MASTER_PLAN.md) §§4–10 and §13.

---

## Relationship to the rest of the project

This documentation repository is one part of the larger project:

```text
src/                  → computational models
simulations/          → simulations and demonstrations
tests/                → software / numerical checks
docs/design/          → implementation-facing design specifications
docs/validation/      → research and physics validation
data/                 → datasets
analysis/             → higher-level analysis
results/              → generated research outputs
papers/               → final research synthesis
```

The validation documentation does not replace the implementation or design
documentation. Its purpose is to establish the scientific basis, evidence,
implementation relationship, numerical behaviour, and limitations of the
models.

A useful distinction throughout the project is:

> **Implemented ≠ validated ≠ physically justified.**

---

## Adding or advancing a stage

When work moves to a new stage:

1. Follow the stage scope and dependencies in `MASTER_PLAN.md`.
2. Use the established validation-document structure.
3. Keep derivations, literature evidence, code audits, and numerical results
   in their appropriate documents rather than duplicating them in this
   README.
4. Update the stage status in `MASTER_PLAN.md` §10 when it changes.
5. Mark a stage CLOSED only when its final validation/conclusion document
   supports closure.

The detailed conventions and classification vocabularies are maintained
centrally in [`MASTER_PLAN.md`](../../MASTER_PLAN.md) §6.

---

## Ownership

`docs/validation/` and this README contain the project's research-validation
record.

Implementation is maintained separately in:

```text
src/
simulations/
tests/
docs/design/
```

The final integrated research output belongs in:

```text
papers/
```
