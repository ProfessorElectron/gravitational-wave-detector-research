# Gravitational-Wave Detector Research — Master Plan

**Status:** Governing roadmap for the complete research and development workflow.

## Contents

1. [Project Purpose](#1-project-purpose)
2. [How to Read This Repository](#2-how-to-read-this-repository)
3. [Research Philosophy](#3-research-philosophy)
4. [Overall Research Workflow](#4-overall-research-workflow)
5. [Stage-by-Stage Research Plan](#5-stage-by-stage-research-plan)
6. [Standard Research Method for Every Stage](#6-standard-research-method-for-every-stage)
7. [Stage Validation Documentation](#7-stage-validation-documentation)
8. [Stage-to-Repository Mapping](#8-stage-to-repository-mapping)
9. [Current Repository Architecture](#9-current-repository-architecture)
10. [Current Project Status](#10-current-project-status)
11. [Scope Boundaries and Future Extensions](#11-scope-boundaries-and-future-extensions)
12. [Explicitly Removed Original Objectives](#12-explicitly-removed-original-objectives)
13. [How the Stages Connect](#13-how-the-stages-connect)
14. [Definition of a Completed Stage](#14-definition-of-a-completed-stage)
15. [Final Project Outcome](#15-final-project-outcome)

---

## 1. Project Purpose

This project develops a **progressively validated computational model of gravitational-wave interferometric detection**.

The goal is not simply to build an interferometer simulation. The project progressively establishes the physical and computational chain from a gravitational-wave signal to detector output, noise, spectral sensitivity, signal recovery, and comparison with real gravitational-wave data.

The overall modelling chain is:

```text
GW source
   ↓
h₊(t), h×(t)
   ↓
Detector antenna response
   ↓
h_det(t)
   ↓
Differential arm response
   ↓
ΔL(t)
   ↓
Optical phase response
   ↓
Δφ(t)
   ↓
Operating-point/readout model
   ↓
Detector output
   ↓
┌───────────────┬────────────────┐
│     Signal    │      Noise     │
│               │                │
│               │  Physical noise│
│               │       ↓        │
│               │     PSD/ASD    │
└───────┬───────┴───────┬────────┘
        │               │
        └───────┬───────┘
                ↓
       Signal processing
                ↓
        SNR / recovery
                ↓
      Sensitivity assessment
                ↓
      Real-data comparison
                ↓
       Integrated research
```

The project therefore combines three connected kinds of work:

1. **Physics** — establish what the detector model should represent.
2. **Computational implementation** — implement those relationships as reproducible code and simulations.
3. **Validation and documentation** — demonstrate that the implementation agrees with the established model within its stated assumptions and limitations.

The governing principle throughout the repository is:

```text
physics
→ derivation
→ literature support
→ assumptions / conventions
→ implementation
→ numerical validation
→ documentation
```

A central distinction must always be maintained:

> **Implemented ≠ validated ≠ physically justified.**

A piece of code may already exist while its underlying physics has not yet been fully researched or validated. Likewise, a mathematically correct implementation may still represent only a simplified approximation of a real detector.

---

## 2. How to Read This Repository

This document is the **map of the project**. It is not intended to contain every derivation, literature argument, code inspection, or numerical test.

The repository is organized so that different documents answer different questions:

* **`MASTER_PLAN.md`** — Where is the project going, and what are the major stages?
* **`README.md`** — How should a new visitor enter and navigate the repository?
* **`src/`** — What computational models are implemented?
* **`simulations/`** — What demonstrations and experiments are being run?
* **`tests/`** — What automated or controlled checks exist?
* **`docs/design/`** — How are implementation-level components designed?
* **`docs/validation/`** — Why is a model considered physically and numerically defensible?
* **`data/`** — What external/public data are used?
* **`results/`** — What outputs are produced from simulations and validation?
* **`papers/`** — What is the final research-level synthesis?

The detailed scientific work should therefore remain in the appropriate stage documents rather than being duplicated here.

---

## 3. Research Philosophy

The project follows a **progressive validation strategy**.

A later stage should build on an earlier stage whose relevant foundation has already been established. This does not mean that code cannot be developed early. In practice, implementation may overlap between stages.

For example, the repository may already contain noise or spectral-analysis code while the corresponding physics is still being researched.

Therefore:

```text
Existing code
      ≠
Completed research stage
```

A stage becomes complete only when its scientific basis, implementation relationship, numerical behaviour, and limitations have been documented sufficiently to support the next part of the project.

The project also deliberately separates:

* idealized physics from realistic detector physics,
* toy models from physical noise models,
* mathematical derivation from code implementation,
* numerical validation from literature validation,
* and the simplified detector model from the full complexity of instruments such as Advanced LIGO.

---

## 4. Overall Research Workflow

The project is divided into **nine major stages**:

```text
Stage 1  — Ideal Michelson Physics
Stage 2  — GW Strain Response
Stage 3  — Polarization & Antenna Response
Stage 4  — Operating Point & Readout
Stage 5  — Physical Noise Models
Stage 6  — PSD / ASD / Sensitivity
Stage 7  — Signal Processing & Recovery
Stage 8  — Public GW Data Validation
Stage 9  — Integrated Model & Final Research Study
```

Conceptually, these stages follow the physical dependency chain.

Implementation may overlap, but scientific conclusions from later stages should not silently be treated as established simply because corresponding code already exists.

---

## 5. Stage-by-Stage Research Plan

### Stage 1 — Ideal Michelson Physics

#### Purpose

Establish the foundational optical physics of the simplified Michelson interferometer.

This stage provides the baseline from which the later gravitational-wave response and detector readout are developed.

#### Major work

The stage establishes the closed-form relationships involving:

* differential arm length,
* round-trip optical path difference,
* optical phase difference,
* beam-splitter transformation,
* field recombination,
* bright-port and dark-port behaviour,
* interference,
* periodicity and symmetry.

The detailed derivation and literature validation belong in the Stage 1 validation documents rather than in this master plan.

#### Existing implementation

The foundational implementation is primarily associated with:

```text
src/interferometer.py
```

The repository also contains illustrative Stage 1 simulations.

#### Boundary

Stage 1 establishes the **ideal interferometer optics**. It does not attempt to include the complete gravitational-wave coupling, physical detector noise, realistic LIGO optical configuration, or advanced signal processing.

The boundary between the ideal Michelson model and the GW strain response is explicitly preserved as the Stage 1/Stage 2 interface.

---

### Stage 2 — GW Strain Response

#### Purpose

Establish how a gravitational wave produces a differential response in the interferometer arms.

The simplified relationship is represented conceptually as:

```text
GW strain h(t)
      ↓
Differential arm response ΔL(t)
```

with the commonly used simplified relationship:

```text
ΔL(t) ≈ h(t)L₀
```

under the assumptions established by the research.

#### Major research topics

* gravitational-wave strain,
* metric perturbation,
* TT gauge,
* `h₊` and `h×`,
* proper distance,
* differential arm response,
* equal-arm approximations,
* long-wavelength approximation,
* finite-arm effects,
* displacement versus strain.

#### Existing implementation

```text
src/gravitational_wave.py
simulations/gravitational_wave_injection.py
```

The existing strain model is a simplified waveform/toy model. Stage 2 determines the physical justification and validity range of the relationship implemented by that model.

#### Main output

A defensible and documented **strain-to-detector-arm-response model** that can serve as the foundation for later detector-response stages.

---

### Stage 3 — Polarization & Antenna Response

#### Purpose

Extend the detector model from a simplified scalar strain input to the directional and polarization-dependent response of an interferometric detector.

The target detector response is represented conceptually as:

```text
h_det(t) = F₊h₊(t) + F×h×(t)
```

where the antenna factors depend on source direction, detector geometry, and polarization.

#### Major research topics

* tensor GW polarizations,
* propagation direction,
* detector orientation,
* polarization angle,
* antenna-pattern functions,
* sky location,
* detector response,
* maximum-response geometries,
* null-response geometries.

#### Implementation

The implementation architecture should be decided **after establishing the physics**, rather than assuming in advance whether the functionality belongs in:

```text
src/gravitational_wave.py
```

or a separate detector-response module.

#### Validation

Special geometries with known expected responses should provide controlled validation cases.

---

### Stage 4 — Operating Point & Readout

#### Purpose

Establish how the simplified interferometer is operated and how small changes in phase are converted into a measurable output.

#### Major topics

* bright and dark ports,
* antisymmetric-port readout,
* operating point,
* phase response,
* linearization,
* small-signal response,
* `dI/dφ`,
* simplified control/locking concepts,
* relationship between the ideal optical model and detector readout.

The local response can be represented conceptually as:

```text
ΔI ≈ (dI/dφ)|φ₀ · Δφ
```

#### Existing implementation

```text
simulations/operating_point.py
```

Additional simulations may connect the operating-point model with the simplified detector output.

#### Scope boundary

This project does **not** automatically become a full Advanced LIGO optical/control simulation at this stage.

Fabry–Pérot arm cavities, power recycling, signal recycling, detailed control loops, optical losses, mode mismatch, and other realistic detector subsystems remain outside the current simplified model unless explicitly introduced as future extensions.

The real detector is used as physical context and comparison, not as an implicit requirement to reproduce the entire instrument.

---

### Stage 5 — Physical Noise Models

#### Purpose

Move from simplified measurement noise toward physically motivated, frequency-dependent detector noise models.

The fundamental method for each noise source is:

```text
Physical origin
      ↓
Mathematical model
      ↓
Frequency dependence
      ↓
Units
      ↓
Approximation / regime
      ↓
Implementation
      ↓
Numerical validation
```

#### Major candidate noise categories

**Quantum**

* shot noise,
* radiation-pressure noise.

**Mechanical**

* seismic noise,
* suspension noise,
* coating thermal noise,
* substrate thermal noise.

**Gravity-gradient**

* Newtonian noise.

**Laser**

* frequency noise,
* intensity noise.

**Optical/readout**

* photodetector/readout contributions,
* scattered-light effects.

**Environmental**

* residual-gas refractive-index fluctuations.

#### Existing implementation

```text
src/noise.py
src/physical_noise.py

simulations/noisy_detector.py
simulations/noise_spectrum.py
simulations/physical_noise_budget.py
simulations/seismic_noise.py
simulations/seismic_strain_budget.py
```

The simple Gaussian model in `src/noise.py` is treated as a **controlled toy noise model**, not automatically as a representation of physical detector noise.

The physical-noise architecture is documented separately in:

```text
docs/design/physical_noise_architecture.md
```

---

### Stage 6 — PSD / ASD / Sensitivity

#### Purpose

Establish that the spectral-analysis machinery correctly represents detector noise and signal content in the frequency domain.

#### Major topics

* Fourier-transform conventions,
* one-sided and two-sided PSD,
* PSD normalization,
* ASD,
* windowing,
* coherent gain,
* periodograms,
* Welch averaging,
* frequency resolution,
* sampling rate,
* Nyquist frequency,
* units,
* strain calibration,
* combining independent noise sources.

Core relationships include:

```text
ASD(f) = √PSD(f)

S_total(f) = Σ Sᵢ(f)

ASD_total(f) = √S_total(f)
```

The final sensitivity representation is a frequency-dependent strain sensitivity such as:

```text
√S_h(f)
```

with units of:

```text
1 / √Hz
```

#### Existing implementation

```text
src/spectral_analysis.py
```

with simulations including:

```text
simulations/frequency_analysis.py
simulations/noise_spectrum.py
simulations/welch_analysis.py
```

This stage validates not merely whether the code produces a spectrum, but whether the estimator, normalization, units, and statistical interpretation are appropriate.

---

### Stage 7 — Signal Processing & Recovery

#### Purpose

Develop the signal-analysis layer that turns noisy detector output into a recoverable GW signal.

The existing repository contains an RMS-based SNR implementation, but this is treated as a simplified starting point rather than the final gravitational-wave search methodology.

#### Major topics

* filtering,
* Fourier-domain processing,
* whitening,
* matched filtering,
* templates,
* frequency-domain SNR,
* detection statistics,
* signal recovery,
* relationship between noise spectrum and detectability.

A target frequency-domain SNR framework is represented by:

```text
ρ² = 4 ∫ |h̃(f)|² / S_n(f) df
```

#### Existing implementation

```text
src/signal_analysis.py
simulations/snr_analysis.py
```

The stage progressively determines how far the implementation should move from controlled toy analysis toward a physically meaningful GW signal-recovery framework.

---

### Stage 8 — Public GW Data Validation

#### Purpose

Test the developed computational framework against publicly available gravitational-wave data.

This stage is not intended to reproduce the complete LIGO/Virgo/KAGRA production analysis pipeline.

Instead, it asks whether the simplified research model behaves consistently when compared with real detector observations.

#### Major validation questions

* Does the observed/simulated signal morphology behave consistently?
* Does the frequency-domain representation behave as expected?
* Do relevant noise characteristics resemble those represented by the model?
* Can injected signals be recovered?
* Does matched filtering provide the expected improvement?
* Are the model's simplifying assumptions reasonable within the selected comparison?
* Where does the simplified model diverge from real detector behaviour?

#### Repository areas

```text
data/
analysis/
results/
```

are expected to become increasingly important here.

The real-data comparison should also provide evidence for the limitations of the simplified model rather than being treated only as a demonstration.

---

### Stage 9 — Integrated Model & Final Research Study

#### Purpose

Connect the validated components into one coherent computational detector model and synthesize the entire research process.

The integrated chain is:

```text
GW source
   ↓
h₊(t), h×(t)
   ↓
Antenna response
   ↓
h_det(t)
   ↓
Differential arm response
   ↓
ΔL(t)
   ↓
Δφ(t)
   ↓
Operating-point/readout model
   ↓
Detector output
   ↓
Signal + physical noise
   ↓
PSD / ASD
   ↓
Signal processing
   ↓
SNR / recovery
   ↓
Sensitivity
   ↓
Real-data comparison
```

#### Final research work

The final stage should:

* connect the validated modules,
* identify the assumptions inherited from earlier stages,
* identify where the model remains simplified,
* evaluate the behaviour of the integrated framework,
* consolidate numerical and literature evidence,
* and present the resulting research conclusions and limitations.

#### Final output

The Stage 9 capstone belongs in:

```text
papers/final_research_report.md
```

rather than in the per-stage validation folders.

---

## 6. Standard Research Method for Every Stage

Every stage uses the same broad research cycle.

### A — Define the physics question

Identify exactly what physical or computational question the stage is intended to answer.

### B — Independent understanding / derivation

Where practical, establish the mathematical relationship independently before relying on implementation or literature.

### C — Literature validation

Compare the formulation against authoritative sources such as:

* peer-reviewed gravitational-wave literature,
* LIGO and other detector technical documentation,
* established textbooks,
* detector reviews,
* relevant methodological references.

### D — Assumptions and conventions

Explicitly record:

* approximations,
* idealizations,
* geometry,
* coordinate/gauge conventions where relevant,
* operating regime,
* frequency range,
* units,
* normalization,
* sign conventions,
* neglected physical effects.

### E — Code and simulation audit

Determine whether the existing implementation actually corresponds to the established model.

The audit distinguishes:

* **A — Agreement**
* **B — Scope limitation**
* **C — Genuine discrepancy**

### F — Numerical validation

Construct controlled tests with known or independently derived expected behaviour.

The purpose is not merely to show that code executes, but to establish numerical agreement with the validated reference model.

### G — Documentation

Record the established model, evidence, assumptions, validation results, and limitations.

### H — Implementation changes

Only after the above work should the implementation be modified or extended based on the findings.

This workflow is intended to prevent the repository from becoming a collection of equations and simulations whose physical validity has not been established.

---

## 7. Stage Validation Documentation

Each research-validation stage from Stage 1 through Stage 8 has a dedicated folder under:

```text
docs/validation/
```

The standard structure is:

```text
README.md
analytical_model.md
literature_validation.md
code_and_simulation_audit.md
numerical_validation.md
limitations_and_conclusion.md
```

The five core documents serve different purposes.

| Document                        | Main purpose                                                                                 |
| -------------------------------- | ---------------------------------------------------------------------------------------------- |
| `analytical_model.md`           | Establish the mathematical/physical reference model                                          |
| `literature_validation.md`      | Establish literature support for the model and resolve convention or formulation differences |
| `code_and_simulation_audit.md`  | Compare the validated model with the implementation and simulations                          |
| `numerical_validation.md`       | Demonstrate numerical agreement using controlled tests                                       |
| `limitations_and_conclusion.md` | Synthesize the stage's validity boundary and determine whether the stage can be closed       |

An optional stage `README.md` provides navigation and a concise stage overview.

The same documentation philosophy is carried forward from Stage 1 rather than inventing a different validation structure for every later stage.

---

## 8. Stage-to-Repository Mapping

The validation folders are organized as:

```text
docs/validation/
├── stage-1-ideal-michelson/
├── stage-2-gw-strain-response/
├── stage-3-polarization-antenna/
├── stage-4-operating-point-readout/
├── stage-5-physical-noise-models/
├── stage-6-psd-asd-sensitivity/
├── stage-7-signal-processing-recovery/
└── stage-8-public-data-validation/
```

Stage 9 is the integrated research/capstone stage and therefore culminates in:

```text
papers/final_research_report.md
```

The repository is thus divided by responsibility rather than putting all research material into one large document.

---

## 9. Current Repository Architecture

The major repository areas are:

```text
gravitational-wave-detector-research/
│
├── README.md
├── MASTER_PLAN.md
├── requirements.txt
│
├── src/
│
├── simulations/
│
├── tests/
│
├── analysis/
│
├── data/
│
├── results/
│
├── docs/
│   ├── design/
│   └── validation/
│
└── papers/
```

**Ownership:** `src/`, `simulations/`, `tests/`, and `docs/design/` are implementation
— maintained by whoever owns the code. `docs/validation/` and this Master Plan are
the research-validation record, maintained by the documentation author independently
of the codebase. Neither side edits the other's folders.

### `src/`

Contains the reusable computational models and core implementation.

Examples include:

```text
interferometer.py
gravitational_wave.py
noise.py
physical_noise.py
spectral_analysis.py
signal_analysis.py
```

### `simulations/`

Contains executable demonstrations and controlled simulations associated with the different stages.

### `tests/`

Contains automated or controlled software checks. Numerical validation documents should reference reproducible tests rather than treating plots alone as validation evidence.

### `analysis/`

Contains higher-level or post-processing analysis, particularly relevant as the project approaches public-data validation and integration.

### `data/`

Stores relevant datasets, particularly as Stage 8 begins.

### `results/`

Stores outputs from simulations, numerical validation, spectral analysis, noise budgets, and later integrated studies.

### `docs/design/`

Contains implementation-facing design documentation.

### `docs/validation/`

Contains the research-validation audit trail.

### `papers/`

Contains publication-facing or final research outputs.

---

## 10. Current Project Status

The existence of code in a stage does not mean that the stage is scientifically closed.

**Legend:** ✅ Complete/Closed — 🟢 Active/current — 🟡 Preliminary/partial — 🔴 Not started/future

| Stage                                        | Status                | Meaning                                                                                                                                                                          |
| --------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Ideal Michelson Physics**                | ✅ Complete (CLOSED)   | All five Stage 1 validation documents are complete (`analytical_model.md`, `literature_validation.md`, `code_and_simulation_audit.md`, `numerical_validation.md`, `limitations_and_conclusion.md`); Stage 1 meets the closure criteria in §14 |
| **2. GW Strain Response**                     | 🟢 Active (current)    | Preliminary implementation exists (`src/gravitational_wave.py`, `simulations/gravitational_wave_injection.py`); independent derivation, literature validation, code audit, and numerical validation now underway |
| **3. Polarization & Antenna Response**        | 🔴 Not started         | Major physics and implementation work remains                                                                                                                                   |
| **4. Operating Point & Readout**              | 🟡 Preliminary         | Operating-point simulation exists; physical validation remains                                                                                                                  |
| **5. Physical Noise Models**                  | 🟡 Partial implementation | Significant implementation exists; source-by-source physical validation remains                                                                                             |
| **6. PSD / ASD / Sensitivity**                | 🟡 Partial implementation | Spectral machinery exists; mathematical/statistical validation remains                                                                                                       |
| **7. Signal Processing & Recovery**           | 🟡 Preliminary         | Basic SNR functionality exists; more physically meaningful signal processing remains                                                                                            |
| **8. Public GW Data Validation**              | 🔴 Future              | Begins after sufficient maturity of the preceding model                                                                                                                         |
| **9. Integrated Model & Final Research Study** | 🔴 Future              | Final integration and research synthesis                                                                                                                                        |

This status is intentionally separate from the implementation inventory.

---

## 11. Scope Boundaries and Future Extensions

The current project focuses on a **progressively validated simplified ground-based interferometric detector model**.

Several topics may be physically relevant to real gravitational-wave detectors without being part of the current core implementation.

These include:

* full Fabry–Pérot arm-cavity modelling,
* power recycling,
* signal recycling,
* detailed control and locking systems,
* realistic optical losses,
* beam imperfections and mode mismatch,
* detailed detector calibration,
* complete Advanced LIGO optical configuration,
* full production gravitational-wave search pipelines.

These should not be silently introduced merely because real detectors contain them.

They can instead appear as:

1. physical context,
2. limitations of the simplified model,
3. future extensions,
4. or dedicated research stages if the project scope is formally expanded.

---

## 12. Explicitly Removed Original Objectives

The project's original roadmap contained additional objectives that are no longer part of the active nine-stage workflow.

### Tabletop Michelson prototype

A tabletop experimental Michelson project was previously included as a later phase.

It is **not part of the current active research workflow**.

### LISA / space-based detector study

A conceptual space-based/LISA-like extension was also part of the original roadmap.

It is likewise **not part of the current core workflow**.

Neither should be presented in the README or master plan as an active project objective unless the scope is explicitly reintroduced.

---

## 13. How the Stages Connect

The dependency structure can be viewed at three levels.

### Physics foundation

```text
Stage 1
Ideal Michelson
      ↓
Stage 2
GW strain response
      ↓
Stage 3
Polarization / antenna response
      ↓
Stage 4
Operating point / readout
```

These stages establish what the detector measures and how the GW signal becomes an observable detector response.

### Detector realism

```text
Stage 4
Readout
   ↓
Stage 5
Physical noise
   ↓
Stage 6
PSD / ASD / sensitivity
```

These stages establish how the ideal signal is affected by realistic frequency-dependent detector noise and how detector sensitivity is represented.

### Data analysis and research validation

```text
Stage 6
Sensitivity
   ↓
Stage 7
Signal processing / recovery
   ↓
Stage 8
Public-data validation
   ↓
Stage 9
Integrated model / final study
```

These stages establish whether the computational detector model can support meaningful signal analysis and comparison with real observations.

---

## 14. Definition of a Completed Stage

A stage is considered **CLOSED** only when its required scientific and computational evidence has been assembled.

At minimum, this means:

```text
Physics question defined
        ↓
Model/derivation established
        ↓
Literature support established
        ↓
Assumptions and conventions recorded
        ↓
Implementation audited
        ↓
Numerical behaviour validated
        ↓
Limitations documented
        ↓
Stage conclusion established
```

The existence of functioning code, plots, or preliminary simulations alone is therefore not sufficient to close a stage.

A closed stage should provide a defensible foundation for the work that follows.

---

## 15. Final Project Outcome

The intended outcome is not merely a collection of independent simulations.

The final repository should provide a traceable chain showing:

```text
What physics was assumed
        ↓
Why that physics was chosen
        ↓
What literature supports it
        ↓
How it was mathematically formulated
        ↓
How it was implemented
        ↓
How the implementation was tested
        ↓
Where the model is valid
        ↓
Where the model is simplified
        ↓
How the components behave together
        ↓
How the model compares with real GW data
```

The completed project should therefore function as both:

1. a **reproducible computational research framework**, and
2. a **documented validation record** explaining the scientific basis and limitations of that framework.

The detailed scientific evidence belongs in the stage documentation; this Master Plan exists to make the entire journey visible and navigable.
