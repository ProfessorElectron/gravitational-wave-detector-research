# Code and Simulation Audit — GW Strain → Differential Arm Response (Stage 2)

**Status:** Draft for repository commit. All content is complete except the
repository commit hash and per-line locators, which are entered in Section 13.
This document is an inspection-and-comparison audit record. It is not a
derivation, not a literature review, and not a numerical validation: no code
was executed and no test results are reported here.

---

## 1. Purpose and Scope

### 1.1 Purpose

This document establishes what the repository code currently implements for
the Stage 2 relationship

$$
h(t) \rightarrow \Delta L_\mathrm{arm}(t) = h(t)L_0,
$$

and compares that implementation, item by item, with the frozen Stage 2
baseline (Document 1, validated by Document 2). It answers one question:

> Does the repository implement the established h(t) → ΔL_arm(t) relationship
> within the baseline's stated assumptions and validity regime?

### 1.2 Audited Files

| # | File | Role |
|---|---|---|
| 1 | `src/gravitational_wave.py` | Strain model: `sinusoidal_strain()` |
| 2 | `src/interferometer.py` | Optical functions (Stage 1): `differential_arm_length()`, `phase_difference()`, `photodetector_intensity()`, `intensity_from_arm_lengths()` |
| 3 | `simulations/gravitational_wave_injection.py` | Stage 2 injection runner: `run_gravitational_wave_injection()` |
| 4 | `simulations/interferometer.py` | Stage 1 baseline fringe-sweep runner: `run_basic_sweep()` (inventoried for completeness; outside the Stage 2 comparison) |

### 1.3 Relationship to Other Documents

- **Document 1 (analytical model)** defines the baseline audited here.
- **Document 2 (literature validation and consistency audit)** supports that
  baseline against external sources.
- **This document (Document 3)** checks the code against the baseline.
- **Numerical validation** is a separate, later stage. It executes tests
  against the code. Section 10 hands off to it; this document does not perform
  it.

### 1.4 Out of Scope

Physical correctness of the baseline (Documents 1–2); execution of any test;
proposed code modifications; finite-arm, cavity, recycling, readout, noise and
network physics (Stage 3 onward).

---

## 2. Baseline Under Audit

Frozen Stage 2 specification (Document 1, Step 5 synthesis):

| Item | Baseline |
|---|---|
| Equation | ΔL_arm(t) = h(t)L₀ |
| Strain | Pre-projected scalar h(t) ≡ h₊(t) |
| Arm length | Common nominal L₀ = L_x,0 = L_y,0 |
| Sign | ΔL_arm ≡ L_x − L_y = δL_x − δL_y = +h(t)L₀ |
| Normalization | δL_x = +½hL₀, δL_y = −½hL₀; net factor 1.0 |
| Geometry | Orthogonal arms (ζ = 90°) |
| Polarization / alignment | Pure plus (h× = 0), φ = ψ = 0 ⇒ F₊ = 1, F× = 0 |
| Incidence | Overhead, θ = 0 |
| Approximation | Long-wavelength: f_GW ≪ f* ≡ c/(2πL₀) |
| Adopted regime | f_GW ≤ 0.1 f* (project-adopted criterion) |
| Excluded | Finite-arm factor C(f), Fabry–Pérot pole K₋(f), recycling, homodyne/DC readout, non-orthogonal geometry, network statistics |

The optical stages consumed after ΔL_arm come from the Stage 1 frozen results:
Δφ = 4πΔL_arm/λ and the bright-port intensity I_bright = (I₀/2)(1 + cos Δφ).

---

## 3. Audit Method and Evidence Chain

$$
\text{baseline} \rightarrow \text{code inventory} \rightarrow \text{item-by-item comparison}
\rightarrow \text{assumptions/conventions} \rightarrow \text{scope check}
\rightarrow \text{status}.
$$

Evidence is read directly from the four source files. Locators are given as
file and function/statement; per-line numbers are added in Section 13.

### 3.1 Status Categories

- **MATCH** — the code implements the baseline item directly and explicitly.
- **EQUIVALENT** — different construction, identical net result.
- **MATCH UNDER STATED ASSUMPTIONS** — agrees with the baseline only because
  of an assumption the code does not represent explicitly.
- **ASSUMED, NOT REPRESENTED** — the baseline item has no representation in
  the code; the code's result is consistent with it only if the assumption
  holds.
- **CONSISTENT (OUT OF SCOPE)** — excluded by the baseline and omitted by the
  code.

No category implies numerical confirmation. That belongs to the next stage.

---

## 4. Code Inventory

### 4.1 `src/gravitational_wave.py`

`sinusoidal_strain(time, amplitude, frequency, phase=0.0)` returns
`amplitude * np.sin(2.0 * np.pi * frequency * time + phase)`, accepting a
scalar or a NumPy array for `time`. It raises `ValueError` if
`frequency < 0`. The module docstring states that converting strain into arm
displacement "belongs in the simulation layer for now". No arm length, sky
angle, polarization or antenna-pattern quantity appears in this module.

### 4.2 `src/interferometer.py`

| Function | Behaviour | Validation |
|---|---|---|
| `differential_arm_length(length_x, length_y)` | Returns `length_x - length_y` (m) | None |
| `phase_difference(differential_length, wavelength)` | Returns `4.0 * np.pi * differential_length / wavelength` (rad); docstring states the round-trip factor of 2 | `wavelength <= 0` → `ValueError` |
| `photodetector_intensity(phase, input_intensity=1.0)` | Returns `0.5 * input_intensity * (1.0 + np.cos(phase))`; docstring states "ideal bright-port" | `input_intensity < 0` → `ValueError` |
| `intensity_from_arm_lengths(length_x, length_y, wavelength, input_intensity=1.0)` | Composes the three functions above and returns a float | Inherited |

No dark-port function exists in the module.

### 4.3 `simulations/gravitational_wave_injection.py`

`run_gravitational_wave_injection(show_plots=True)` defines, as local
constants: `wavelength = 1064e-9`, `input_intensity = 1.0`,
`arm_length = 1.0`, `strain_amplitude = 1e-21`, `gw_frequency = 100.0`,
`duration = 0.1`, `sample_count = 10_000`. Its computation is:

```
time = np.linspace(0.0, duration, sample_count)
strain = sinusoidal_strain(time, strain_amplitude, gw_frequency)
differential_displacement = arm_length * strain
phase = phase_difference(differential_displacement, wavelength)
intensity = photodetector_intensity(phase, input_intensity)
intensity_change = intensity - input_intensity
peak_phase_shift = np.max(np.abs(phase))
small_angle_intensity_change = 0.25 * input_intensity * peak_phase_shift**2
```

It prints peak ΔL, peak phase shift, the range of `intensity_change`, and the
analytic small-angle estimate; saves four PNG plots to `results/`
(`gw_injection_strain.png`, `gw_injection_displacement.png`,
`gw_injection_phase.png`, `gw_injection_intensity.png`); and returns the four
paths. The helper `_save_time_series_plot()` produces the first three plots;
the intensity plot is built inline with `ticklabel_format(style="plain",
useOffset=False)`. `show_plots=True` calls `plt.show()`.

`differential_displacement = arm_length * strain` is the only statement in the
repository that implements the Stage 2 relationship. No individual arm
variable (δL_x, δL_y, L_x, L_y) exists in this runner.

### 4.4 `simulations/interferometer.py` (Stage 1 baseline script)

`run_basic_sweep()` uses `differential_arm_length`, `phase_difference`,
`intensity_from_arm_lengths` and `photodetector_intensity` for equal arms
(L_x = L_y = 1.0 m) and a ±2λ differential-displacement sweep over 2000
points, saves `results/basic_interferometer_fringe.png`, and calls
`plt.show()` unconditionally. It is the Stage 1 optical baseline and does not
contain any strain or GW quantity.

### 4.5 Execution Flow (Stage 2 runner)

```
time (linspace) → strain = sinusoidal_strain(...)           [h(t)]
               → differential_displacement = arm_length * strain   [ΔL_arm(t)]
               → phase = phase_difference(...)               [Δφ(t) = 4πΔL/λ]
               → intensity = photodetector_intensity(...)    [I_bright(t)]
               → four plots saved to results/
```

### 4.6 Not Represented in the Audited Code

Tensor strain h_ij, h₊ and h× as separate quantities; sky angles (θ, φ) and
polarization angle ψ; antenna patterns F₊, F×; individual arm responses
δL_x(t), δL_y(t); arm opening angle; finite-arm transit factor C(f);
Fabry–Pérot and recycling cavities; dark-port output, DC offset or homodyne
readout; noise.

---

## 5. Physics-to-Code Mapping Table

| Baseline item | Code | Status | Locator |
|---|---|---|---|
| Pre-projected scalar h(t) | `sinusoidal_strain()` returns a scalar waveform | MATCH UNDER STATED ASSUMPTIONS | `src/gravitational_wave.py` |
| ΔL_arm = h(t)L₀ | `arm_length * strain` | MATCH | injection runner, `differential_displacement` |
| Net factor 1.0 (±½ split) | Multiplier 1.0; arms not instantiated | EQUIVALENT | injection runner |
| Sign +hL₀ | Positive product; helper `length_x - length_y` | MATCH | injection runner; `differential_arm_length()` |
| Units (h dimensionless, L₀ and ΔL in m) | As stated in variables, prints, docstrings | MATCH | injection runner; `src/interferometer.py` |
| Equal nominal arms | Single scalar `arm_length` | MATCH UNDER STATED ASSUMPTIONS | injection runner |
| Orthogonal arms (ζ = 90°) | No arm angle in code | ASSUMED, NOT REPRESENTED | — |
| Plus polarization, F₊ = 1, F× = 0 | No polarization or antenna quantity | ASSUMED, NOT REPRESENTED | — |
| Overhead incidence θ = 0 | No sky-angle quantity | ASSUMED, NOT REPRESENTED | — |
| Long-wavelength regime | Static multiplication; f/f* ≈ 2.1 × 10⁻⁶ for the runner's parameters | MATCH (within regime) | injection runner |
| Finite-arm factor C(f) | Omitted | CONSISTENT (OUT OF SCOPE) | — |
| Fabry–Pérot pole K₋(f) | Omitted | CONSISTENT (OUT OF SCOPE) | — |
| Recycling cavities | Omitted | CONSISTENT (OUT OF SCOPE) | — |
| Homodyne / DC readout | Bright port only; no offset | CONSISTENT (OUT OF SCOPE) | `photodetector_intensity()` |
| Non-orthogonal geometry | Omitted | CONSISTENT (OUT OF SCOPE) | — |
| Network statistics | Omitted | CONSISTENT (OUT OF SCOPE) | — |
| Stage 1: Δφ = 4πΔL/λ | `phase_difference()` | MATCH | `src/interferometer.py` |
| Stage 1: I_bright = (I₀/2)(1 + cos Δφ) | `photodetector_intensity()` | MATCH (bright port) | `src/interferometer.py` |
| Stage 1: I_dark = (I₀/2)(1 − cos Δφ) | Not implemented | NOT IMPLEMENTED (consistent with Stage 1 record) | — |

---

## 6. Claim-by-Claim Comparison

### 6.1 Strain-to-Differential-Displacement Equation

**Baseline:** ΔL_arm(t) = h(t)L₀.
**Code:** `differential_displacement = arm_length * strain`, with `strain`
from `sinusoidal_strain()` and `arm_length = 1.0`.
**Result:** MATCH. The statement is algebraically identical to the baseline.
**Note:** The relation exists only as this one inline statement in the runner
(see Finding F1).

### 6.2 Normalization and the ½ Factor

**Baseline:** δL_x = +½hL₀, δL_y = −½hL₀, so δL_x − δL_y = hL₀.
**Code:** No individual arm quantity is computed; the net multiplier is 1.0.
**Result:** EQUIVALENT. The ½ factors are not instantiated, and the net
differential equals the baseline's net by the identity ½ − (−½) = 1. The
code therefore cannot expose a single-arm error, because there is no
single-arm variable to inspect.

### 6.3 Sign Convention

**Baseline:** ΔL_arm ≡ L_x − L_y = +h(t)L₀.
**Code:** The Stage 2 runner uses a positive product. `differential_arm_length`
returns `length_x - length_y`, matching the Stage 1 definition, but the Stage 2
runner does not call it.
**Result:** MATCH. In the Stage 2 path the positive sign holds by construction
of the product rather than through a subtraction of two arm lengths.

### 6.4 Units and Dimensional Consistency

**Baseline:** h dimensionless; L₀ and ΔL_arm in meters; Δφ in radians.
**Code:** `strain_amplitude = 1e-21` (dimensionless), `arm_length = 1.0` (m),
`wavelength = 1064e-9` (m), `phase_difference` returns radians, intensity is
normalized.
**Result:** MATCH. Each operation is dimensionally consistent: [m] = [m] ×
[1], [rad] = [m]/[m], and intensity is normalized.

### 6.5 Equal-Arm and Orthogonal-Arm Assumptions

**Equal arms.** A single scalar `arm_length` enforces L_x,0 = L_y,0. This is
MATCH UNDER STATED ASSUMPTIONS: the code cannot represent unequal nominal arms
at all.
**Orthogonal arms.** No arm angle or geometry factor exists anywhere in the
audited files. The ΔL = hL₀ relation is orthogonal-arm physics, and the code
reproduces it only because it uses the orthogonal-arm form of the relation.
This is ASSUMED, NOT REPRESENTED.

### 6.6 Polarization, Alignment and Incidence

**Baseline:** h× = 0, φ = ψ = 0, θ = 0 ⇒ F₊ = 1, F× = 0, h_det = h₊ ≡ h.
**Code:** `sinusoidal_strain()` generates the pre-projected scalar h(t)
directly. None of the sky or polarization quantities appears.
**Result:** ASSUMED, NOT REPRESENTED. The code corresponds to the aligned,
overhead, plus-polarized special case and cannot represent any other
configuration.

### 6.7 Long-Wavelength Approximation

**Baseline:** valid for f_GW ≪ f* = c/(2πL₀); adopted regime f_GW ≤ 0.1 f*.
**Code:** static multiplication, with no frequency-dependent factor.
**Audit calculation** (from the runner's parameters and the baseline's own
definitions): for L₀ = 1.0 m, f* = c/(2π · 1 m) ≈ 47.7 MHz; for
f_GW = 100 Hz, f_GW/f* ≈ 2.1 × 10⁻⁶, which satisfies the adopted criterion
f_GW ≤ 0.1 f*. With x = ωL₀/c = f_GW/f*, the baseline's omitted finite-arm
factor C(f) = sinc(x)e^{−ix} departs from unity in amplitude by about x²/6
≈ 7 × 10⁻¹³ and in phase by about x ≈ 2 × 10⁻⁶ rad.
**Result:** MATCH (within regime). Omitting C(f) is consistent with the
baseline boundary for these parameters. The conclusion holds for the runner's
specific L₀ and f_GW; the code itself contains no check or guard for the
regime (Finding F2).

### 6.8 Stage 1 Optical Chain Consumed by the Stage 2 Runner

`phase_difference()` implements Δφ = 4πΔL/λ and
`photodetector_intensity()` implements I_bright = (I₀/2)(1 + cos Δφ),
both as frozen in Stage 1 (Claims 3 and 6). The Stage 1 literature record
classifies the bright-port formula as CONVENTION/DEFINITION DEPENDENT,
because gravitational-wave detectors read out at the dark port. The Stage 2
runner reads out the bright port. This is a scope observation, not a
discrepancy (Finding F5).

---

## 7. Model Boundary Audit

| Effect | Stage 2 status | Code status | Evaluation |
|---|---|---|---|
| Static strain scaling ΔL = L₀h | Included (core baseline) | Implemented | Within baseline |
| Finite-arm transit factor C(f) | Excluded (Stage 3) | Omitted | Consistent |
| Fabry–Pérot cavity pole K₋(f) | Excluded (Stage 3) | Omitted | Consistent |
| Recycling cavities | Excluded (Stage 3) | Omitted | Consistent |
| Homodyne / DC readout offset | Excluded (Stage 4) | Omitted; bright port used | Consistent |
| Non-orthogonal geometry (ζ = 60°) | Excluded (Stage 3 extension) | Omitted | Consistent |
| Detector network statistics | Excluded (Stage 4) | Omitted | Consistent |

---

## 8. Toy-Model Evaluation

**What it represents.** A monochromatic scalar strain, h(t) = A sin(2πft)
with A = 1.0 × 10⁻²¹, f = 100 Hz, φ = 0, T = 0.1 s, N = 10,000, under the
aligned, overhead, plus-polarized, long-wavelength baseline.

**What it can exercise.** The linear mapping h → ΔL_arm, array handling,
Δφ = 4πΔL/λ and the bright-port intensity expression.

**What it cannot exercise.** Broadband or chirp waveforms, off-axis sky
projection, cross polarization, noise, cavity storage, finite-arm cancellation
at high frequency, dark-port readout.

**Sampling grid.** `np.linspace(0.0, 0.1, 10_000)` includes the endpoint, so
the sample spacing is 0.1/9999 s ≈ 1.0001 × 10⁻⁵ s and the effective sampling
rate is 9999/0.1 = 99,990 Hz. It is not exactly 100 kHz (Finding F4).

**Parameter scale.** L₀ = 1.0 m gives a static gain
4πL₀/λ ≈ 1.18 × 10⁷ rad per unit strain, versus ≈ 4.72 × 10¹⁰ rad per unit
strain for 4 km at 1064 nm. The relation is linear, so the toy value does not
alter its form; it does mean the runner's peak Δφ (≈ 1.18 × 10⁻¹⁴ rad) is not
detector-scale.

**Compatibility with the baseline.** The sinusoid introduces no additional
physical assumption that changes the strain-to-displacement scaling.

---

## 9. Findings and Discrepancies

**Genuine discrepancies between the code and the Stage 2 baseline: none.** The
findings below are structural, documentary or scope observations. Each is
classified.

| ID | Finding | Classification |
|---|---|---|
| F1 | The h → ΔL relation is one inline statement in the runner. `gravitational_wave.py` states that this conversion "belongs in the simulation layer for now". There is no importable function for it. | Design observation |
| F2 | The code does not document the baseline assumptions. LWA validity, equal arms, orthogonality, F₊ = 1, θ = 0 and the sign convention appear in neither comments nor guards. | Documentation observation |
| F3 | Orthogonal arms, polarization alignment and overhead incidence are not represented in the code. | Assumption, not representation; corrects the stronger wording of an earlier comparison draft |
| F4 | The sampling grid is endpoint-inclusive: effective sampling rate 99,990 Hz, not 100 kHz. | Correction to the earlier code-inventory draft |
| F5 | The runner reads out the bright port at Δφ_peak ≈ 1.18 × 10⁻¹⁴ rad. Because 1 − cos(Δφ) ≈ 7 × 10⁻²⁹ is far below the float64 resolution of 1.0, `intensity` is expected to equal exactly 1.0 and `intensity_change` exactly 0.0. The runner's analytic small-angle estimate is computed separately. | Scope/readout observation (expectation from floating-point arithmetic; not executed here) |
| F6 | Toy parameters are not detector-scale (L₀ = 1 m). | Scope observation |
| F7 | The earlier code-inventory draft omitted `intensity_change`, the small-angle estimate, and the partial input validation (frequency, wavelength, input intensity). They are recorded in Section 4. | Audit-record correction |
| F8 | No dark-port function exists, consistent with the Stage 1 record. | Scope observation |
| F9 | Input validation is partial: `arm_length` and `strain_amplitude` are unchecked. | Minor observation |

---

## 10. Phase Boundary and Hand-off to Numerical Validation

### 10.1 What This Document Establishes

What the four files implement, and how that corresponds to the Stage 2
baseline. It establishes no numerical result.

### 10.2 What the Next Stage Must Address

The numerical validation plan (Step 7 Run 3: T1–T7, M1–M3) specifies tests
that have not been executed. Reading the code against that plan gives the
following inputs for that stage. They are expectations from the code and the
sampling grid, to be confirmed or refuted there.

1. **Importability (F1).** The h → ΔL statement cannot be called on its own. A
   test must either re-evaluate the expression or run the runner; the choice
   of whether to refactor is a project decision not made here.
2. **Grid-aware test points.** Because the grid spacing is 0.1/9999 s, the
   times 0.0025 s and 0.005 s used in T3 and T6 are not sample points
   (0.0025 s falls at index ≈ 249.975, 0.005 s at ≈ 499.95). The nearest
   sample to the zero crossing at 0.005 s is offset by about 5 × 10⁻⁷ s, so
   |ΔL| there is expected near 3 × 10⁻²⁵ m, not below 10⁻³² m.
3. **Peak-based checks (T2, T7).** The nearest sample to the first peak
   (0.0025 s) is offset by about 2.5 × 10⁻⁷ s, so the sampled peak is
   expected to sit about 1.2 × 10⁻⁸ below A·L₀ in relative terms. A 10⁻¹⁴
   relative tolerance on a sampled peak is expected not to hold.
4. **T7 intensity check (F5).** The plan's intensity target of
   ≈ 3.49 × 10⁻²⁹ is below float64 resolution; the computed intensity change
   is expected to be exactly 0.0.
5. **FFT peak (T6).** With N = 10,000 samples at 99,990 Hz the bin spacing is
   ≈ 9.999 Hz, so the bin nearest 100 Hz is centered at ≈ 99.99 Hz.
6. **Test numbering.** Stage 1 numerical validation already uses T10–T13. A
   prefix (for example `S2-T1`) would avoid ambiguity in the repository.

---

## 11. Limitations

- Static inspection only. No code was run, and no output value in this
  document comes from execution; values quoted from the runner's print
  statements come from the source, not from a run.
- The comparison is with the Stage 2 baseline as frozen in Document 1; it does
  not re-evaluate the baseline's physics.
- A match here shows that the code implements the relation. It does not show
  agreement with real detector data.
- The toy sinusoid is a single-frequency test vector, not an astrophysical
  waveform.
- Locators in this version are function/statement level (Section 13).

---

## 12. Final Audit Statement

The repository implements the Stage 2 baseline relation
ΔL_arm(t) = h(t)L₀ directly, with net normalization 1.0, positive sign
(+h(t)L₀), consistent units, and a static long-wavelength form that sits
within the baseline's regime for the runner's parameters (f_GW/f* ≈ 2.1 × 10⁻⁶).

- **What agrees:** the equation, net normalization, sign, units, and the
  Stage 1 optical functions it feeds.
- **What agrees only under stated assumptions:** the pre-projected scalar
  strain, equal arms, orthogonal arms, F₊ = 1, F× = 0 and θ = 0, none of which
  the code represents explicitly.
- **What differs by construction:** individual arm perturbations are bypassed
  (EQUIVALENT).
- **What lies outside the Stage 2 boundary:** finite-arm factor, cavities,
  recycling, dark-port and homodyne readout, non-orthogonal geometry, network
  statistics.
- **Genuine discrepancies:** none.
- **Open for the next stage:** numerical confirmation, including the grid and
  floating-point points in Section 10.2.

---

## 13. Reproducibility Appendix

### 13.1 Audited Revision

- Repository commit hash: `<to be entered>`
- Files: `src/gravitational_wave.py`, `src/interferometer.py`,
  `simulations/gravitational_wave_injection.py`,
  `simulations/interferometer.py`

### 13.2 Locators

Per-line locators are to be added from the repository at the commit above.
Until then, locators are given by file and function/statement as in
Sections 4–6.

---

## 14. References

- Stage 2 Document 1 — analytical model (frozen baseline).
- Stage 2 Document 2 — literature validation and consistency audit.
- Stage 1 `analytical_model.md` and `literature_validation.md` (frozen Stage 1
  optical results consumed by the code).
- Step 7 Run 3 — numerical validation plan (hand-off only; not executed).

---

*End of document. This audit is the reference for the Stage 2 numerical
validation stage.*
