# Code & Simulation Audit — Ideal Michelson Interferometer (Phase 1)

**Status:** Complete. This document audits the repository's implementation and
simulation use against the frozen Phase 1 physics baseline established in
`analytical_model.md` and literature-validated in `literature_validation.md`.
It is a comparison/audit record, not a third derivation and not a second
literature review.

---

## 1. Purpose and Scope

### 1.1 Purpose

This document determines whether the repository's existing code and
simulations correctly correspond to the independently established and
literature-validated Phase 1 analytical model, identifies implementation
and simulation-level assumptions that are additional to that model, and
distinguishes Phase 1 material from later-stage material.

The project's governing principle applies throughout:

$$
\boxed{\text{implemented}\neq\text{validated}\neq\text{physically justified}}
$$

`analytical_model.md` establishes what was derived. `literature_validation.md`
establishes that the derivation is externally supported. This document
establishes whether the repository implements what those two documents
validated — nothing more.

### 1.2 In scope

* `src/interferometer.py`, compared function-by-function against the frozen
  Phase 1 equations.
* Every file under `simulations/`, inventoried and classified by which
  Master Plan stage it belongs to.
* Every other module under `src/`, inventoried and classified (but not
  compared against the Phase 1 baseline, since none of them implement
  Phase 1 physics).
* Assumptions introduced by the implementation or simulations that are
  additional to the assumptions already stated in `analytical_model.md` §18.
* The relationship between this audit's findings and the numerical evidence
  in the finalized T1–T13 validation record.

### 1.3 Out of scope

* Re-deriving any physics relation (that is `analytical_model.md`'s role).
* Re-arguing literature support for any claim (that is
  `literature_validation.md`'s role).
* Adding new numerical tests (T1–T13 are treated as final).
* Proposing or making code changes, unless a genuine discrepancy is found
  (none was — see Section 11.3).
* Assessing the *physical adequacy* of Stage 2, 4, 5, 6, or 7 material —
  e.g. whether the sinusoidal strain model is a defensible approximation, or
  whether the toy Gaussian noise model should eventually be replaced. The
  Master Plan assigns that evaluation to each stage's own future document
  (Stage 2 → `docs/gw_detector_response.md`; Stage 6 →
  `docs/sensitivity_analysis.md`; other stages not yet assigned a document).
  Sections 6 and 8 of this audit classify later-stage material; they do not
  evaluate it.

### 1.4 Relationship to the preceding documents

Conventions and assumptions are not a separate document — they are
integrated into `analytical_model.md` (§3 for definitions/conventions, §18
for idealizations). This audit cites those sections directly rather than
restating them. Literature status labels (VERIFIED /
VERIFIED WITH EXPLICIT ASSUMPTIONS / CONVENTION-DEFINITION DEPENDENT) are
cited from `literature_validation.md` §7 where relevant to an implementation
finding, never re-derived.

---

## 2. Audit Methodology

### 2.1 Method flow

This document's section order mirrors the audit method directly:

$$
\text{Validated physics baseline (§3)}
\rightarrow
\text{Repository inventory (§4)}
\rightarrow
\text{Code comparison (§5)}
\rightarrow
\text{Simulation inspection (§6)}
\rightarrow
\text{Mapping (§7)}
\rightarrow
\text{Phase-boundary classification (§8)}
\rightarrow
\text{Additional assumptions (§9)}
\rightarrow
\text{Numerical-validation linkage (§10)}
\rightarrow
\text{Findings (§11)}
\rightarrow
\text{Conclusion (§12)}
$$

The validated physics determines what the code should implement; the code
is evidence to be audited against that baseline, not a source of physical
truth.

### 2.2 Finding classification scheme

Every comparison in Section 5, and the consolidated findings in Section 11,
are classified into exactly one of three categories:

* **A — Agreement.** The implementation matches the validated physics.
* **B — Scope limitation.** The physics is established (analytically and/or
  in the literature), but the repository does not currently implement that
  part. This is not an error.
* **C — Genuine discrepancy.** The implementation conflicts with the
  validated physics. Only this category creates an automatic, evidence-based
  reason to modify the code.

---

## 3. Validated Physics Baseline

This section extracts the frozen Phase 1 results for comparison purposes
only. Derivations live in `analytical_model.md`; literature support lives
in `literature_validation.md`.

### 3.1 Frozen equation table

| Physics element | Frozen result | Source |
|---|---|---|
| Differential arm length | $\Delta L_\mathrm{arm}=L_x-L_y$ | `analytical_model.md` §4, §17.2 |
| Round-trip optical path | $\Delta L_\mathrm{rt}=2\Delta L_\mathrm{arm}$ | `analytical_model.md` §5, §17.2 |
| Differential optical phase | $\Delta\phi=\dfrac{4\pi}{\lambda}\Delta L_\mathrm{arm}=2k\Delta L_\mathrm{arm}$ | `analytical_model.md` §6, §17.2 |
| Beamsplitter matrix | $B=\dfrac{1}{\sqrt2}\begin{pmatrix}1&i\\i&1\end{pmatrix}$ | `analytical_model.md` §7.1 |
| Bright-port intensity | $I_\mathrm{bright}=\dfrac{I_0}{2}(1+\cos\Delta\phi)$ | `analytical_model.md` §9, §17.2 |
| Dark-port intensity | $I_\mathrm{dark}=\dfrac{I_0}{2}(1-\cos\Delta\phi)$ | `analytical_model.md` §9, §17.2 |
| Conservation | $I_\mathrm{bright}+I_\mathrm{dark}=I_0$ | `analytical_model.md` §9, §17.2 |
| Periodicity | $\Delta L_\mathrm{period}=\lambda/2$ | `analytical_model.md` §13, §17.2 |
| Complete chain | $L_x,L_y\rightarrow\Delta L_\mathrm{arm}\rightarrow\Delta L_\mathrm{rt}\rightarrow\Delta\phi\rightarrow I_\mathrm{bright},I_\mathrm{dark}$ | `analytical_model.md` §10 |

### 3.2 Beamsplitter convention

The field-level derivation (`analytical_model.md` §7–§8) applies the same
matrix $B$ for both the initial split and the recombination pass (the
reciprocal-beamsplitter assumption, stated in §18.2). $I_\mathrm{bright}$
and $I_\mathrm{dark}$ are *derived consequences* of this field-level
convention, not independently asserted formulas.

### 3.3 Phase 1 / Phase 2 boundary

$\Delta L_\mathrm{arm}(t)=h(t)L_0$ (`analytical_model.md` §16;
`literature_validation.md` Claim 10, status VERIFIED WITH EXPLICIT
ASSUMPTIONS) is the interface to the Stage 2 GW-response work. It is not
part of the core Phase 1 optical derivation, and this audit does not treat
its implementation as a Phase 1 requirement (see §6.2, §8).

### 3.4 Bright- vs. dark-port literature status

`literature_validation.md` §7 rates the bright-port relation (Claim 6) as
**CONVENTION/DEFINITION DEPENDENT** — correct as a formula, but not the port
gravitational-wave detectors actually read out. The dark-port relation
(Claim 7) is rated **VERIFIED WITH EXPLICIT ASSUMPTIONS** and is identified
as the operationally relevant channel. This distinction is directly
relevant to §5.3–§5.4 below: the repository implements the port that
literature marks as convention-dependent and operationally secondary, and
does not implement the port marked as the actual GW-readout channel. This
is recorded as a scope observation, not reargued here.

---

## 4. Repository Implementation Overview

### 4.1 Repository snapshot

The audited material is the uploaded repository archive
`gravitational-wave-detector-research-main`. No version-control metadata
(`.git/`) is present in the supplied archive, so no commit hash can be cited
for traceability; this audit refers to the archive as supplied. The
repository does not contain a `tests/` directory — the T1–T13 numerical
validation record exists as an external document, not as a checked-in,
automated regression suite.

### 4.2 File inventory

**`src/` modules**

| Module | Role | Stage |
|---|---|---|
| `interferometer.py` | Ideal Michelson optical response ($\Delta L\to\Delta\phi\to I$) | Stage 1 (Phase 1) |
| `gravitational_wave.py` | Sinusoidal strain $h(t)$ toy model | Stage 2 |
| `noise.py` | Additive Gaussian toy measurement noise | Stage 5 (toy) |
| `physical_noise.py` | Frequency-dependent physical noise models; PSD/ASD/strain conversions | Stage 5 (physical) / Stage 6 (unit conversion) |
| `signal_analysis.py` | RMS / RMS-SNR utilities | Stage 7 |
| `spectral_analysis.py` | FFT / periodogram PSD / ASD / Welch utilities | Stage 6 |
| *(none)* | Polarization / antenna-pattern response | Stage 3 — **not yet implemented** |
| *(none)* | Public GW-data validation | Stage 8 — **not yet implemented** |
| *(none)* | Integrated detector model | Stage 9 — **not yet implemented** |

**`simulations/` files** (12 total)

| Simulation | Stage(s) | Treatment |
|---|---|---|
| `basic_interferometer.py` | 1 | Full inspection — §6.1 |
| `time_dependent_interferometer.py` | 1 (application) | Full inspection — §6.1 |
| `gravitational_wave_injection.py` | 2 | Classification — §6.2 |
| `operating_point.py` | 2 + 4 | Classification — §6.2 |
| `noisy_detector.py` | 2 + 5 (toy) | Classification — §6.2 |
| `frequency_analysis.py` | 2 + 5 (toy) + 6 | Classification — §6.2 |
| `noise_spectrum.py` | 2 + 5 (toy) + 6 | Classification — §6.2 |
| `welch_analysis.py` | 2 + 5 (toy) + 6 | Classification — §6.2 |
| `snr_analysis.py` | 2 + 5 (toy) + 7 | Classification — §6.2 |
| `physical_noise_budget.py` | 5 (physical) | Classification — §6.3 |
| `seismic_noise.py` | 5 (physical) | Classification — §6.3 |
| `seismic_strain_budget.py` | 5 (physical) | Classification — §6.3 |

### 4.3 Cross-reference: physical noise architecture

The repository already contains `docs/physical_noise_architecture.md`
("Milestone 8A"), which defines the contract that `src/physical_noise.py`
implements (common frequency grid, PSD/ASD units, domain conversions). This
is noted here as context for the Stage 5/6 inventory rows above; its content
is not imported or re-evaluated by this audit, since Stage 5/6 adequacy is
out of scope per §1.3.

### 4.4 Implementation chain diagram

$$
L_x,L_y
\xrightarrow{\texttt{differential\_arm\_length()}}
\Delta L
\xrightarrow{\texttt{phase\_difference()}}
\Delta\phi
\xrightarrow{\texttt{photodetector\_intensity()}}
I_\mathrm{bright}
$$

with `intensity_from_arm_lengths()` composing all three in a single call.

---

## 5. Code Comparison

Scoped explicitly to `src/interferometer.py`, the only module implementing
Phase 1 physics. The other five `src/` modules are inventoried in §4.2 and
phase-tagged in §8, not compared against the Phase 1 baseline here, since
no Phase 1 baseline applies to their content.

### 5.1 Differential arm length

**Baseline:** $\Delta L_\mathrm{arm}=L_x-L_y$ (§3.1;
`literature_validation.md` Claim 1, VERIFIED).

**Code:**

```python
def differential_arm_length(length_x: float, length_y: float) -> float:
    """Return the arm-length difference Lx - Ly in meters."""
    return length_x - length_y
```

**Finding:** Exact match — full-difference convention, correct sign, no
half-difference substitution.

**Numerical evidence:** T1 (four cases including equal arms, X-longer,
Y-longer, ordinary unequal; max observed absolute error $\approx1.11\times10^{-16}$ m,
floating-point roundoff).

**Category: A**

### 5.2 Phase difference

**Baseline:** $\Delta\phi=\dfrac{4\pi}{\lambda}\Delta L_\mathrm{arm}$ (§3.1;
`literature_validation.md` Claim 3, VERIFIED; Claim 2, round-trip factor,
VERIFIED WITH EXPLICIT ASSUMPTIONS).

**Code:**

```python
def phase_difference(
    differential_length: float | np.ndarray,
    wavelength: float,
) -> float | np.ndarray:
    """Return the round-trip phase difference in radians."""
    if wavelength <= 0:
        raise ValueError("wavelength must be positive")
    return 4.0 * np.pi * differential_length / wavelength
```

**Finding:** The round-trip factor of 2 is folded directly into the
$4\pi/\lambda$ coefficient rather than exposed as a separate
$\Delta L_\mathrm{rt}$ quantity or function. This matches the fact,
established in `literature_validation.md` §4.2.4, that no source defines a
standalone $\Delta L_\mathrm{rt}$ variable either — the factor is kept
inline in every source examined. The explicit `wavelength <= 0` check is an
implementation-level input-validation choice, additional to the physics
model (§9).

**Numerical evidence:** T2 (cross-formulation consistency check — explicitly
qualified in the validation record as *not* an independent test of a
separate round-trip function, since none exists; agreement to
$\sim1.7\times10^{-18}$ rad) and T3 (known-answer phase values at
$0,\lambda/8,\lambda/4,\lambda/2,-\lambda/4$, all exact to displayed
precision, including odd-symmetry and phase-doubling checks).

**Category: A**, with the T2 methodological qualification carried forward
as a caveat on the strength of that particular piece of evidence, not as a
discrepancy.

### 5.3 Bright-port intensity

**Baseline:** $I_\mathrm{bright}=\dfrac{I_0}{2}(1+\cos\Delta\phi)$ (§3.1;
`literature_validation.md` Claim 6, CONVENTION/DEFINITION DEPENDENT).

**Code:**

```python
def photodetector_intensity(
    phase: float | np.ndarray,
    input_intensity: float = 1.0,
) -> float | np.ndarray:
    """Return ideal bright-port Michelson intensity."""
    if input_intensity < 0:
        raise ValueError("input_intensity must be non-negative")
    return 0.5 * input_intensity * (1.0 + np.cos(phase))
```

**Finding:** Exact match. The function's own docstring correctly scopes
itself as "bright-port" — the implementation does not claim to be a general
detector-readout function, which is consistent with the convention caveat
in §3.4.

**Numerical evidence:** T4 (known-answer constructive/destructive/
intermediate cases, all exact), T5 (end-to-end chain), T8 (intensity bounds
sanity check across $I_0=0,1,2.5,10$), T9 (equal-arm operating point).

**Category: A**

### 5.4 Dark-port / field-level beamsplitter model

**Baseline:** beamsplitter matrix $B$ and
$I_\mathrm{dark}=\dfrac{I_0}{2}(1-\cos\Delta\phi)$ (§3.1–§3.2;
`literature_validation.md` Claim 7, VERIFIED WITH EXPLICIT ASSUMPTIONS —
the actual GW-readout channel).

**Code:** none. A search of the entire repository for `dark`,
`antisymmetric`, `beamsplitter`, and `unitary` returns zero matches in any
`src/` or `simulations/` file.

**Finding:** The field-level beamsplitter model and the dark-port response
have no corresponding implementation anywhere in the repository. This is
not a case of the function existing elsewhere and not being wired in —
there is no beamsplitter representation in the codebase at all. T10–T13
validate the analytical model independently of the repository, exactly as
their own methodology notes state ("There is no beamsplitter function there
to compare against... this is a genuine numerical validation of the
analytical beamsplitter model rather than a code-self-consistency test").

**Numerical evidence:** T10 (unitarity, 50:50 split, power conservation,
$\pi/2$ relative phase — all PASS, independent of the repository), T11
(field-level recombination, known-answer cases plus the non-special case
$\Delta L=0.137\lambda$, max discrepancy $5.55\times10^{-16}$), T12
(bright+dark conservation across six phase values, max deviation
$4.44\times10^{-16}$), T13 (dark-port known-answer cases at
$\Delta\phi=0,\pi,\pi/2,-\pi$).

**Category: B — scope limitation.** The physics is analytically established
and independently numerically validated; the repository does not implement
it.

### 5.5 Complete implementation chain

**Baseline:** $L_x,L_y\rightarrow\Delta L_\mathrm{arm}\rightarrow\Delta L_\mathrm{rt}\rightarrow\Delta\phi\rightarrow I_\mathrm{bright}$
(§3.1).

**Code:**

```python
def intensity_from_arm_lengths(
    length_x: float,
    length_y: float,
    wavelength: float,
    input_intensity: float = 1.0,
) -> float:
    """Calculate detector intensity directly from Michelson arm lengths."""
    return float(photodetector_intensity(
        phase_difference(differential_arm_length(length_x, length_y), wavelength),
        input_intensity,
    ))
```

**Finding:** Correctly composes the three validated functions in the
correct order.

**Numerical evidence:** T5 (end-to-end chain; the one non-zero discrepancy,
$5.77\times10^{-10}$ at $\Delta L=\lambda/8$, is attributed in the
validation record to floating-point representation of $\lambda/8$ as an
arm-length value before the trigonometric evaluation, and is negligible at
double precision).

**Category: A**

### 5.6 Scope summary

| Physics element | Implemented? | Category |
|---|---|---|
| $\Delta L_\mathrm{arm}=L_x-L_y$ | Yes — `differential_arm_length()` | A |
| $\Delta L_\mathrm{rt}=2\Delta L_\mathrm{arm}$ | Folded into `phase_difference()`, no standalone function | A (T2 caveat) |
| $\Delta\phi=4\pi\Delta L_\mathrm{arm}/\lambda$ | Yes — `phase_difference()` | A |
| Beamsplitter matrix $B$ | No | B |
| Field-level recombination | No | B |
| $I_\mathrm{bright}$ | Yes — `photodetector_intensity()` | A |
| $I_\mathrm{dark}$ | No | B |
| Complete chain | Yes — `intensity_from_arm_lengths()` | A |

The repository implements exactly and only the bright-port scalar path of
the Phase 1 model. The field-level derivation exists solely as an
analytical/numerical reference (§3.2, T10–T13); it has never been
repository code.

---

## 6. Simulation Inspection

### 6.1 Phase 1 simulations (full inspection)

**`basic_interferometer.py`**

Imports all four Phase 1 functions
(`differential_arm_length`, `phase_difference`, `photodetector_intensity`,
`intensity_from_arm_lengths`). Runs an equal-arm baseline
($L_x=L_y=1.0$ m, $\lambda=1064$ nm) and a 2000-point sweep of
$\Delta L\in[-2\lambda,2\lambda]$, producing the fringe plot
(`results/basic_interferometer_fringe.png`).

*Finding:* Directly and correctly exercises the frozen chain
$\Delta L\to\Delta\phi\to I$. Consistent with T1, T3, T4, T6, T7.
**Category: A.**

**`time_dependent_interferometer.py`**

Imports `phase_difference` and `photodetector_intensity` only — it injects
an artificial sinusoidal displacement
(`differential_displacement = amplitude * sin(2π·frequency·t)`, amplitude
$10^{-9}$ m, frequency 100 Hz) directly, with no strain or GW model
involved.

*Finding:* This is a Phase 1 *application*, not later-stage physics — the
chain $\Delta L(t)\to\Delta\phi(t)\to I(t)$ applies the already-validated
static formulas at each time sample; $\Delta L(t)$ is an arbitrary
externally specified time series, not one derived from strain. The
resulting local-quadratic/frequency-doubling behavior near the equal-arm
bright point is a property of composing the validated static formula, not a
new physics claim requiring separate validation.
**Category: A.**

### 6.2 Later-stage simulations reusing `phase_difference()` (classification only)

Per §1.3, this subsection classifies; it does not evaluate physical
adequacy.

| Simulation | Uses `phase_difference()` | Uses `photodetector_intensity()` | Other modules used | Stage(s) |
|---|---|---|---|---|
| `gravitational_wave_injection.py` | Yes | Yes | `gravitational_wave.sinusoidal_strain` | 2 |
| `operating_point.py` | Yes | Yes | `gravitational_wave.sinusoidal_strain` | 2 + 4 |
| `noisy_detector.py` | Yes | Yes | `gravitational_wave.sinusoidal_strain`, `noise.add_gaussian_noise` (toy) | 2 + 5 (toy) |
| `frequency_analysis.py` | Yes | No | `gravitational_wave.sinusoidal_strain`, `noise.add_gaussian_noise` (toy), `spectral_analysis` | 2 + 5 (toy) + 6 |
| `noise_spectrum.py` | Yes | No | `gravitational_wave.sinusoidal_strain`, `noise.add_gaussian_noise` (toy), `spectral_analysis.welch_amplitude_spectral_density` | 2 + 5 (toy) + 6 |
| `welch_analysis.py` | Yes | No | `gravitational_wave.sinusoidal_strain`, `noise.add_gaussian_noise` (toy), `spectral_analysis` | 2 + 5 (toy) + 6 |
| `snr_analysis.py` | Yes | No | `gravitational_wave.sinusoidal_strain`, `noise.add_gaussian_noise` (toy), `signal_analysis.rms_snr` | 2 + 5 (toy) + 7 |

**Observations (classification, not evaluation):**

* `gravitational_wave_injection.py` computes
  `differential_displacement = arm_length * strain`, i.e. exactly
  $\Delta L(t)=h(t)L_0$ (§3.3). This confirms the Stage 2 classification and
  matches the Master Plan's own instruction that this relationship belongs
  to Stage 2, not Phase 1.
* `operating_point.py` layers a static phase offset
  ($\phi_0\in\{0,\pi/4,\pi/2\}$) on top of the Stage 2 strain-induced phase
  before calling `photodetector_intensity()` — a Stage 4 concept applied on
  top of Stage 2 input.
* Four simulations (`frequency_analysis.py`, `noise_spectrum.py`,
  `welch_analysis.py`, `snr_analysis.py`) call `phase_difference()` but not
  `photodetector_intensity()` — they analyze the strain-induced phase signal
  directly rather than carrying it through the full optical intensity
  readout. This is recorded as a structural observation, not a defect,
  since it is outside Phase 1 scope either way.
* All five noise-adjacent simulations in this group
  (`noisy_detector.py`, `frequency_analysis.py`, `noise_spectrum.py`,
  `welch_analysis.py`, `snr_analysis.py`) use `noise.add_gaussian_noise`
  (the toy model) rather than `physical_noise.py` (the physically-motivated
  model) — see §9.
* `gravitational_wave_injection.py` and `operating_point.py` both use
  `arm_length = 1.0` m, a simplified value rather than a realistic
  kilometer-scale detector arm — a simulation-level parameter choice (§9).

Because the Phase 1 function `phase_difference()` (and, where used,
`photodetector_intensity()`) is correctly reused as a building block inside
these later-stage pipelines, this is expected behavior, not a Phase 1
boundary violation. These seven simulations are recorded here for
inventory and traceability; no Category A/B/C finding applies to them at
the Phase 1 level, since they are not part of the Phase 1 baseline being
audited.

### 6.3 Simulations with no Phase 1 dependency (classification only)

`physical_noise_budget.py`, `seismic_noise.py`, and
`seismic_strain_budget.py` import exclusively from `src.physical_noise`;
none references `src.interferometer` in any form.

*Finding:* Stage 5 (physical noise) / Stage 6 (unit conversion), with no
Phase 1 linkage whatsoever. Recorded for inventory completeness only.

---

## 7. Physics ↔ Code ↔ Simulation Mapping

| Physics | Analytical result | Code | Simulation(s) | Numerical evidence | Category |
|---|---|---|---|---|---|
| Differential arm length | $\Delta L=L_x-L_y$ | `differential_arm_length()` | `basic_interferometer.py` | T1 | A |
| Round-trip path | $\Delta L_\mathrm{rt}=2\Delta L$ | folded into `phase_difference()` | — | T2 | A |
| Phase difference | $\Delta\phi=4\pi\Delta L/\lambda$ | `phase_difference()` | `basic_interferometer.py`, `time_dependent_interferometer.py`, all Stage 2 reuse (§6.2) | T3, T6, T7 | A |
| Bright-port intensity | $I_0(1+\cos\Delta\phi)/2$ | `photodetector_intensity()` | `basic_interferometer.py`, `time_dependent_interferometer.py`, `gravitational_wave_injection.py`, `operating_point.py`, `noisy_detector.py` | T4, T5, T8, T9 | A |
| Complete chain | $\Delta L\to\Delta\phi\to I$ | `intensity_from_arm_lengths()` | `basic_interferometer.py` | T5 | A |
| Beamsplitter matrix | $B$ | — none | — | T10 | B |
| Field recombination | $E_\mathrm{dark},E_\mathrm{bright}$ | — none | — | T11 | B |
| Dark port | $I_0(1-\cos\Delta\phi)/2$ | — none | — | T12, T13 | B |
| GW strain $\to\Delta L$ | $\Delta L(t)=h(t)L_0$ | `gravitational_wave.py` | `gravitational_wave_injection.py` | — | Stage 2, out of Phase 1 scope |

---

## 8. Phase-Boundary Classification

This section assigns each repository element to a Master Plan stage; per
§1.3, it does not assess whether that stage's physics is adequate.

* **Stage 1 (Phase 1):** `src/interferometer.py`; `basic_interferometer.py`;
  `time_dependent_interferometer.py`.
* **Stage 2:** `src/gravitational_wave.py`;
  `gravitational_wave_injection.py`, and as a component within
  `operating_point.py`, `noisy_detector.py`, `frequency_analysis.py`,
  `noise_spectrum.py`, `welch_analysis.py`, `snr_analysis.py`.
* **Stage 3:** no repository code.
* **Stage 4:** `operating_point.py` (layered on Stage 2 within the same
  file).
* **Stage 5 (toy):** `src/noise.py`; used within `noisy_detector.py`,
  `frequency_analysis.py`, `noise_spectrum.py`, `welch_analysis.py`,
  `snr_analysis.py`.
* **Stage 5 (physical):** `src/physical_noise.py`;
  `physical_noise_budget.py`, `seismic_noise.py`,
  `seismic_strain_budget.py`.
* **Stage 6:** `src/spectral_analysis.py`; `frequency_analysis.py`,
  `noise_spectrum.py`, `welch_analysis.py`; `src/physical_noise.py`'s
  ASD/PSD and unit-conversion functions also touch this stage.
* **Stage 7:** `src/signal_analysis.py`; `snr_analysis.py`.
* **Stage 8:** no repository code.
* **Stage 9:** no repository code.

The Master Plan itself draws the toy-vs-physical noise distinction used
above: `src/noise.py`'s Gaussian model is explicitly characterized as "a
controlled toy measurement-noise model, not automatically ... a physical
detector noise model," with the physically-motivated modelling assigned to
`src/physical_noise.py`. This audit cites that characterization rather than
independently assessing it, consistent with §1.3.

No simulation misattributes later-stage physics to Phase 1, and no Phase 1
simulation introduces later-stage physics. Stages 3, 8, and 9 have no
repository code yet, which is expected at this point in the project and is
recorded here for completeness rather than as a finding.

---

## 9. Additional Assumptions Introduced

Assumptions already listed in `analytical_model.md` §18 (monochromatic
input, lossless beamsplitter, perfect mirrors, static arm lengths for the
core derivation, etc.) are not repeated here. This section lists only
assumptions introduced by the implementation or simulations that are
additional to that list.

* **Implementation-level input validation.** `phase_difference()` raises
  `ValueError` for `wavelength <= 0`; `photodetector_intensity()` raises
  `ValueError` for `input_intensity < 0`. The analytical model states
  positive wavelength and non-negative intensity as physical idealizations
  (§18) but does not specify runtime-validation behavior — this is a code-
  level defensive choice, not a physics claim.
* **Simulation-level numerical parameters.** All Phase 1 and Stage 2
  simulations consistently use $\lambda=1064$ nm, matching the parameter
  used throughout the T1–T13 validation record. `gravitational_wave_injection.py`
  and `operating_point.py` use `arm_length = 1.0` m — a simplified value,
  not a realistic kilometer-scale detector arm. Strain amplitude
  ($10^{-21}$), GW frequency (100 Hz), duration (0.1 s), and sample count
  (10,000) are simulation-specific choices with no counterpart in the
  Phase 1 analytical model.
* **Toy vs. physical noise choice.** Five Stage 2+ simulations
  (`noisy_detector.py`, `frequency_analysis.py`, `noise_spectrum.py`,
  `welch_analysis.py`, `snr_analysis.py`) use the toy Gaussian model
  (`src/noise.py`) rather than the physically-motivated model
  (`src/physical_noise.py`). This is a simulation-layer simplification the
  Master Plan itself already flags (§8, Stage 5 discussion).
* **Deliberate architectural deferral.** `src/gravitational_wave.py`'s own
  docstring states that converting strain into detector arm displacement is
  kept in the simulation layer "for now, so the validation chain stays
  explicit" — a stated design choice, not an omission.
* **No automated regression suite.** The repository contains no `tests/`
  directory; T1–T13 exist only as the supplied validation record. This is a
  repository-traceability observation (§4.1), not a physics or
  implementation assumption.

---

## 10. Relationship to Numerical Validation

### 10.1 Evidence linkage

| Test | Validates | Supports | Result |
|---|---|---|---|
| T1 | $\Delta L=L_x-L_y$ | §5.1 | PASS |
| T2 | Round-trip factor of 2 | §5.2 | PASS |
| T3 | $\Delta\phi=4\pi\Delta L/\lambda$ | §5.2 | PASS |
| T4 | Bright-port intensity | §5.3 | PASS |
| T5 | End-to-end chain | §5.5 | PASS |
| T6 | Periodicity + symmetry | §5.2, §5.3 | PASS |
| T7 | Numerical fringe spacing | §5.2, §6.1 | PASS |
| T8 | Intensity bounds | §5.3 | PASS |
| T9 | Equal-arm operating point | §5.3, §5.6 | PASS |
| T10 | 50:50 beamsplitter | §5.4 | PASS |
| T11 | Field-level recombination | §5.4 | PASS |
| T12 | Bright + dark conservation | §5.4, §5.6 | PASS |
| T13 | Dark-port known-answer | §5.4 | PASS |

### 10.2 Methodological classification

The finalized validation record itself classifies the strength of each
test; this audit cites that classification rather than re-deriving it:

| Test | Role |
|---|---|
| T1 | Core |
| T2 | Core consistency (cross-formulation check — no independent round-trip function exists) |
| T3 | Core |
| T4 | Core |
| T5 | Core |
| T6 | Core structural |
| T7 | Core numerical |
| T8 | Supplementary sanity check |
| T9 | Supporting |
| T10 | Core field-level (independent of repository code) |
| T11 | Strong independent reference |
| T12 | Core conservation |
| T13 | Complementary output |

All calculations were performed in double precision; discrepancies at the
$10^{-16}$–$10^{-18}$ level (and, in one fringe-spacing case,
$10^{-22}$) are floating-point roundoff, not physics or implementation
issues, consistent with the tolerance policy stated in the validation
record.

---

## 11. Audit Findings

### 11.1 Category A — Agreement

* $\Delta L_\mathrm{arm}=L_x-L_y$ — `differential_arm_length()` (§5.1).
* $\Delta\phi=4\pi\Delta L_\mathrm{arm}/\lambda$, including the round-trip
  factor — `phase_difference()` (§5.2).
* $I_\mathrm{bright}=\dfrac{I_0}{2}(1+\cos\Delta\phi)$ —
  `photodetector_intensity()` (§5.3).
* The complete chain $L_x,L_y\to\Delta L\to\Delta\phi\to I_\mathrm{bright}$ —
  `intensity_from_arm_lengths()` (§5.5).
* `basic_interferometer.py` and `time_dependent_interferometer.py` apply
  this chain correctly and entirely within Phase 1 scope (§6.1).

### 11.2 Category B — Scope limitations

* The beamsplitter matrix $B$ and the field-level derivation have no
  repository implementation (§5.4).
* The dark-port response $I_\mathrm{dark}$ has no repository implementation,
  despite being the operationally relevant GW-readout channel per
  `literature_validation.md` Claim 7 (§3.4, §5.4).
* No repository code exists yet for Stage 3 (polarization/antenna
  response), Stage 8 (public-data validation), or Stage 9 (integrated
  model) — expected at this point in the project (§4.2, §8).

### 11.3 Category C — Genuine discrepancies

None identified. No case was found in which the repository's Phase 1
implementation conflicts with the frozen analytical model or the
literature-validated physics.

---

## 12. Conclusion

* **Does the code implement the frozen Phase 1 model?** Yes, for the
  bright-port scalar path (§5.1–§5.3, §5.5). The field-level/dark-port half
  of the frozen model has no implementation (§5.4, Category B).
* **Do the simulations use that model consistently?** Yes.
  `basic_interferometer.py` and `time_dependent_interferometer.py` apply it
  directly and correctly (§6.1); the seven Stage 2+ simulations correctly
  reuse `phase_difference()` (and, in three cases, `photodetector_intensity()`)
  as a building block within later-stage pipelines, without misrepresenting
  later-stage physics as Phase 1 (§6.2).
* **Which simulations belong to Phase 1?** `basic_interferometer.py`,
  `time_dependent_interferometer.py`.
* **Which introduce later-stage physics?** The remaining ten, spanning
  Stages 2, 4, 5, 6, and 7 as tabulated in §8.
* **What additional assumptions are introduced?** Enumerated in §9 — all
  are implementation- or simulation-level choices; none alter or contradict
  the Phase 1 physics itself.
* **Are there genuine discrepancies?** No (§11.3).
* **Is code modification required?** No.

This document establishes that "implemented" and "matches validated
physics" both hold for the Phase 1 bright-port path; "physically justified"
was already established by `literature_validation.md`. The dark-port/
field-level result remains physically justified and numerically validated
(T10–T13) but not implemented — a scope status, to be revisited only if the
repository's Phase 1 module is later extended, which is a decision outside
this audit's remit.

Per the documentation workflow, the next document is
`limitations_and_conclusion.md`, which defines the overall Phase 1 validity
boundary using the findings of `analytical_model.md`,
`literature_validation.md`, this audit, and the numerical validation
record together.
