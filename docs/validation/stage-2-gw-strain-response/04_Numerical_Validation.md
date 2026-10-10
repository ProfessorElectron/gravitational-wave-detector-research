# Stage 2 Numerical Validation & Verification Record — GW Strain → Differential Arm Response

**Status:** Complete for Steps 10 and 12. Part II (pre-implementation, Step 10)
and Part III (controlled implementation update and post-implementation
revalidation, Step 12) are both executed and recorded. This document is the
computational evidence record for Stage 2. It is evidence, not a derivation,
not a literature review, and not a repeat of the code audit.

**Document ID:** `S2` — test identifiers carry the prefix `S2-` (S2-T1 …
S2-T10, S2-T9S) so they cannot be confused with the Stage 1 tests T1–T13 in
`numerical_validation.md`.

---

## 1. Purpose, Scope and Position in the Stage 2 Workflow

### 1.1 Purpose

$$
\boxed{\text{implemented}\neq\text{validated}\neq\text{physically justified}}
$$

This document establishes whether the repository implementation of the
Stage 2 chain

$$
h(t)\;\rightarrow\;\Delta L_\mathrm{arm}(t)\;\rightarrow\;\Delta\phi(t)\;\rightarrow\;I_\mathrm{bright}(t)
$$

numerically reproduces the frozen analytical relations established in the
earlier Stage 2 documents, to the precision available in IEEE 754 double
precision. It also records the controlled implementation update (Step 12)
that exposed the individual arm perturbations $\delta L_x,\delta L_y$, and the
re-run of the frozen tests after that update.

### 1.2 Relationship to the Other Stage 2 Documents

| Document | Question it answers |
|---|---|
| Document 1 — Analytical Model | What physics was derived, and from what assumptions? |
| Document 2 — Literature Validation | What external evidence supports it? |
| Document 3 — Code Implementation & Physics Mapping Audit | What does the repository actually implement? |
| **Document 4 — this record** | Does the implementation numerically reproduce the frozen analytical relations, before and after the Step 12 update? |
| Document 5 — Limitations & Master Conclusion | What has been established overall, and where does Stage 2 stop? |

Derivations are in Document 1, literature evidence in Document 2, and the code
audit and gap register in Document 3. This document refers to them and does not
repeat them.

### 1.3 Scope Boundary

**In scope:** the baseline Stage 2 mapping $\Delta L_\mathrm{arm}=hL_0$ and its
decomposition $\delta L_x=+\tfrac12 hL_0$, $\delta L_y=-\tfrac12 hL_0$; strain
linearity; arm-length scaling; sign convention; zero-strain limit; time-series
response; the Stage 2 → Stage 1 interface; the long-wavelength regime of the
test parameters.

**Out of scope** (consistent with Documents 1, 3 and 5): finite-arm transfer
function $C(f)$, cavity dynamics, TDI, antenna patterns $F_{+},F_{\times}$,
general polarization, network response, physical noise, and real data.
The Stage 1 optical relation is used as a frozen input; Stage 1 is not
re-validated here. Only the bright port is exercised, because the repository
implements only the bright port (Stage 1 literature validation shows that
gravitational-wave detectors read out at the dark port; that distinction does
not change any test below).

---

## 2. Validation Method and Conventions

### 2.1 Validation Chain

$$
\text{analytical expectation}\rightarrow\text{implementation output}\rightarrow\text{numerical error}\rightarrow\text{tolerance}\rightarrow\text{status}
$$

A test whose required quantity does not exist in the implementation is not a
failure. It is recorded as `NOT EXECUTABLE / BLOCKED BY IMPLEMENTATION GAP`.

### 2.2 Status Vocabulary

| Status | Meaning |
|---|---|
| **PASS** | Measured error is within the stated tolerance. |
| **PASS — WITH NUMERICAL-RESOLUTION LIMITATION** | Passes, but the physical signal is below float64 resolution; the limitation travels with the result. |
| **FAIL** | Measured error exceeds the stated tolerance. |
| **NOT EXECUTABLE / BLOCKED BY IMPLEMENTATION GAP** | The required quantity is absent from the implementation. |
| **OUT OF SCOPE** | Outside the frozen Stage 2 baseline. |
| **REQUIRES CLARIFICATION** | The criterion is not yet defined. |

### 2.3 Input Provenance Classes

Every numerical input is classified, so that no convenient test value is
mistaken for a physical requirement:

- **Frozen project parameter** — inherited from the frozen Stage 1 model.
- **Previously used example** — taken from the repository's existing
  simulation scripts.
- **Methodological test choice** — chosen here for reproducibility.

### 2.4 Evidence Strength of the Tests

Not all tests carry the same evidentiary weight. Four levels are used:

| Level | Meaning |
|---|---|
| **L1 — Independent analytical check** | The implementation (or a parameter set) is compared with a reference obtained by a different mathematical route. |
| **L2 — Implementation/formula self-consistency** | Reference and implementation perform algebraically identical operations; agreement (including exactly zero error) shows the computational expressions agree, not that the physics has been independently confirmed. |
| **L3 — Numerical-resolution validation** | The test places the response in a regime where float64 can resolve it. |
| **L4 — Auxiliary diagnostic** | Supporting information that does not decide a test result on its own merit. |

Section 9 assigns each test to a level.

### 2.5 Historical Preservation

The pre-implementation results (Part II) are frozen. The post-implementation
results (Part III) are a new record and do not overwrite them.

---

## 3. Frozen Analytical References

Extraction only; derivations are in Document 1.

| # | Relation | Source |
|---|---|---|
| 3.1 | $\delta L_x=+\tfrac12 hL_0$ | Document 1 (individual-arm response) |
| 3.2 | $\delta L_y=-\tfrac12 hL_0$ | Document 1 |
| 3.3 | $\Delta L_\mathrm{arm}=\delta L_x-\delta L_y=hL_0$; $\Delta L_\mathrm{arm}(t)=h(t)L_0$ | Document 1 |
| 3.4 | $\Delta L_\mathrm{arm}\equiv L_x-L_y$ (full-difference convention) | Stage 1 / Document 1 |
| 3.5 | $\Delta\phi=\dfrac{4\pi}{\lambda}\Delta L_\mathrm{arm}=\dfrac{4\pi L_0}{\lambda}h$ | Stage 1 / Document 1 (interface) |
| 3.6 | $I_\mathrm{bright}=\dfrac{I_0}{2}\left[1+\cos\Delta\phi\right]$ — exact cosine form is the primary T9 reference | Stage 1 |
| 3.7 | $\Delta I\equiv I_0-I_\mathrm{bright}=I_0\sin^2(\Delta\phi/2)$ — numerically stable equivalent form | identity from 3.6 |
| 3.8 | LWA: $f\ll f^*\equiv c/(2\pi L_0)$ | Document 1 |

Validity conditions: weak field $|h|\ll1$, TT gauge, aligned $+$ polarization,
equal nominal arm lengths, long-wavelength regime.

---

## 4. Implementation Under Test

### 4.1 Files

| File | Role |
|---|---|
| `src/gravitational_wave.py` | `sinusoidal_strain(time, amplitude, frequency, phase)`; after Step 12 also `arm_perturbations`, `differential_arm_perturbation` |
| `simulations/gravitational_wave_injection.py` | Runner: $h(t)\to\Delta L(t)\to\Delta\phi(t)\to I(t)$ with plots |
| `src/interferometer.py` | Frozen Stage 1 optics: `phase_difference`, `photodetector_intensity` (unchanged throughout) |
| `validation/stage2_numerical_validation.py` | The test script that produced every result in this record |

### 4.2 Pre-Implementation State

The runner computed the differential displacement directly as
`differential_displacement = arm_length * strain`. No variable for
$\delta L_x$ or $\delta L_y$ existed anywhere in the implementation
(Document 3, Finding F-01).

### 4.3 Gap Register (from Document 3)

| ID | Title | Relevance to this record |
|---|---|---|
| F-01 | Individual-arm implementation gap | Blocked S2-T1/T2; resolved by Step 12 (Part III) |
| F-02 | Float64 cancellation in the proposed T6 auxiliary test | Test rejected (Appendix B); drives the Step 12 design rule |
| F-03 | Finite sampling grid in T8 | Mean and FFT bin are diagnostics only |
| F-04 | Float64 resolution in T9 | Limitation attached to S2-T9; S2-T9S added |
| Disc. 1–3 | Direct $L_0h$ product; pre-projected scalar strain; uncalled helper `differential_arm_length()` | Implementation choices with no effect on numerical output |
| Disc. 4 | Sinc transfer function omitted | See §4.4 |

### 4.4 Note on Discrepancy 4 (finite-arm factor)

At $L_0=1$ m and $f=100$ Hz, $x=\omega L_0/c=f/f^*\approx2.1\times10^{-6}$ and
$1-\mathrm{sinc}(x)\approx x^2/6\approx7.3\times10^{-13}$. This is a
**physical** truncation of the baseline model, not a numerical error. It is
larger than the numerical tolerance $10^{-14}$ used below, which causes no
conflict: every test compares the implementation with the **LWA baseline**
$\Delta L=hL_0$, not with a finite-arm model. The two quantities must not be
compared with each other.

### 4.5 Test-Access Limitation

The runner's computation sits inside a plotting function and cannot be
called separately. The script therefore (a) calls the real `src` functions and
(b) in pre-implementation mode reproduces the runner's inline expression
`arm_length * strain` verbatim. See Finding F-05.

---

## 5. Controlled Numerical Inputs and Provenance

| Parameter | Value | Classification |
|---|---:|---|
| Strain amplitude $A$ | $10^{-21}$ | Previously used example |
| GW frequency $f$ | 100 Hz | Previously used example |
| Arm length $L_0$ | 1 m | Previously used example |
| Initial phase $\phi_0$ | 0 | Methodological |
| Duration $T$ | 0.1 s | Methodological |
| Samples $N$ | 10 000 (`np.linspace`, both endpoints included) | Methodological |
| Wavelength $\lambda$ | 1064 nm | Frozen Stage 1 |
| Input intensity $I_0$ | 1 | Frozen Stage 1 |
| S2-T4 amplitudes | $\{1,2,5\}\times10^{-21}$ | Methodological |
| S2-T5 arm lengths | $\{1,4,10\}$ m | Methodological (not detector scales; literature detector scales are 4 km and 10 km) |
| S2-T9S strain | $10^{-7}$ at $L_0=1$ m | Methodological |

None of the methodological values is claimed to be a physical requirement.
The weak-field condition $|h|\ll1$ is satisfied by every strain used.

---

## 6. Error Metrics and Tolerances

### 6.1 Principle

**Physics** fixes the expected relationship. **Numerical analysis** sets the
scale of plausible floating-point error (float64 machine epsilon
$\epsilon_\mathrm{mach}=2^{-52}\approx2.22\times10^{-16}$). **Methodology**
selects the acceptance threshold. Every tolerance below is a
**methodological numerical-analysis acceptance criterion**. None is
derived from General Relativity, none is a universal or machine-independent
bound on floating-point error, and none was tightened because the
implementation happened to produce zero error.

### 6.2 Tolerance Table

Tolerances for S2-T3 to S2-T10 are those of the Step 10 tolerance audit.

| Test | Quantity | Error metric | Tolerance | Basis and qualification |
|---|---|---|---|---|
| S2-T1, S2-T2 | $\delta L_{x},\delta L_y$ | max relative error | $\le10^{-14}$ | Same criterion as S2-T3; introduced for the post-implementation run |
| S2-T3 | $\Delta L(t)$ | max relative error over nonzero points; max absolute error reported | $\le10^{-14}$ | Float64 array multiplication; about 45× above $\epsilon_\mathrm{mach}$ |
| S2-T4 | peak ratio | relative ratio error | $\le10^{-14}$ | Scaling of float64 values; the ratio for $5\times$ is exact only to a few $\epsilon_\mathrm{mach}$ |
| S2-T5 | peak ratio | relative ratio error | $\le10^{-14}$ | As above |
| S2-T6 | $\Delta L(\pm h)$ | exact sign match; exact antisymmetry $\Delta L(-h)=-\Delta L(h)$; relative error | sign and antisymmetry exact; relative $\le10^{-14}$ | IEEE 754 preserves the sign bit under multiplication. The exact-antisymmetry check is a criterion of the script, in addition to the audit's sign check |
| S2-T7 | $\Delta L,\ \Delta\phi,\ I-I_0$ at $h=0$ | **absolute** error | $\le10^{-32}$ m, $\le10^{-32}$ rad, $\le10^{-14}$ | Relative error against an expected zero is undefined. $10^{-32}$ is a conservative floor above an expected *exact* zero; it is not derived from $\epsilon_\mathrm{mach}$ |
| S2-T8 | $\Delta L(t)$ | max absolute error over all samples (primary); relative error at near-peak samples (secondary) | $\le10^{-35}$ m; $\le10^{-14}$ | Time-series bound set by double-precision `sin`. See §6.4 |
| S2-T9 | $\Delta\phi(t)$; $I(t)$ | relative phase error; absolute intensity error | $\le10^{-14}$; $\le10^{-14}$ | The intensity criterion is vacuous at $h=10^{-21}$: the physical signal ($3.5\times10^{-29}$) is 15 orders of magnitude below the tolerance |
| S2-T9S | $\Delta\phi$; $I$; $\Delta I$ vs $I_0\sin^2(\Delta\phi/2)$ | relative / absolute / absolute | $\le10^{-14}$ each | **Extension of the T9 values.** Not covered by the original audit; see §6.3 |
| S2-T10 | $f/f^*$ for every configuration executed | inequality | $\le0.1$ | The factor 0.1 is a project-adopted operational criterion, not a fundamental boundary |

### 6.3 Tolerance Selection for S2-T9S

A tolerance of $10^{-14}$ is used for the supplementary S2-T9S numerical
comparisons. This value is a methodological numerical acceptance criterion,
not a physics-derived requirement. It is supported by the observed
discrepancies of order $10^{-16}$ in the tested float64 calculations
($1.1\times10^{-16}$ and $1.7\times10^{-16}$ in the two execution
environments, Section 18), about two orders of magnitude of margin. It is a
criterion for numerical consistency in the validation environments used, not
a universal bound on floating-point error. The project has not tested other
platforms or other threshold values experimentally.

### 6.4 Near-Peak Diagnostic in S2-T8

Samples satisfying $|\Delta L|\ge0.99\,\max|\Delta L|$ (900 of 10 000 samples)
are treated as near-peak samples. The threshold 0.99 is a methodological
data-selection choice with no physical meaning and is not a physical
definition of a waveform peak. The finite time grid does not contain the exact
sine maximum (Finding F-03), which is why a threshold rule is used. In the
executed script the near-peak criterion is evaluated together with the
all-samples absolute error when assigning the S2-T8 status. Because both
errors are exactly zero in every run, changing 0.99 to another value would
alter only the sample count and could not change the recorded result. The
primary S2-T8 comparison is over the complete time series.

---

## 7. Test Matrix

| Test | Quantity | Analytical reference | Pre-implementation | Post-implementation |
|---|---|---|---|---|
| S2-T1 | $\delta L_x$ | $+\tfrac12 hL_0$ | BLOCKED | executed |
| S2-T2 | $\delta L_y$ | $-\tfrac12 hL_0$ | BLOCKED | executed |
| S2-T3 | $\Delta L$ | $hL_0$ | executed | re-run |
| S2-T4 | $\Delta L$ vs $h$ | $\Delta L\propto h$ | executed | re-run |
| S2-T5 | $\Delta L$ vs $L_0$ | $\Delta L\propto L_0$ | executed | re-run |
| S2-T6 | sign | $h\to-h\Rightarrow\Delta L\to-\Delta L$ | executed | re-run |
| S2-T7 | zero input | $h=0\Rightarrow\Delta L=0,\ \Delta\phi=0,\ I=I_0$ | executed | re-run |
| S2-T8 | time series | $\Delta L(t)=h(t)L_0$ | executed | re-run |
| S2-T9 | Stage 2 → Stage 1 chain at $h=10^{-21}$ | exact cosine law | executed | re-run |
| S2-T9S | same chain at $h=10^{-7}$ | exact cosine law; stable $\Delta I$ form | executed | re-run |
| S2-T10 | regime | $f\ll f^*$; $f/f^*\le0.1$ | executed | re-run |

---

# Part II — Pre-Implementation Validation (Step 10)

All results in this part were produced with the **unmodified** implementation.

## 8. Test Results

Environment 1 (Windows 11, Python 3.12.10, NumPy 2.5.3) is the primary record.
Environment 2 (Linux, Python 3.12.3, NumPy 2.4.4) gave the same status for every
test; the only differences are in informational values and are listed in
Section 18.

### 8.1 S2-T1 and S2-T2 — Individual Arm Responses

**Reference:** $\delta L_x=+\tfrac12hL_0$; $\delta L_y=-\tfrac12hL_0$.
**Implementation:** no explicit $\delta L_x$ or $\delta L_y$ exists.
**Result:** `NOT EXECUTABLE / BLOCKED BY IMPLEMENTATION GAP` (both). No tolerance
is assigned.
**Interpretation:** the analytical relations are not shown to be wrong; the
implementation simply does not expose the quantities needed to test them. A
passing S2-T3 cannot be used to claim that S2-T1 and S2-T2 passed.

### 8.2 S2-T3 — Differential Arm Response

Reference $\Delta L=hL_0$; expected peak $10^{-21}$ m.

| Quantity | Value |
|---|---|
| Max relative error | 0 |
| Max absolute error | 0 m |
| Sampled peak $\lvert\Delta L\rvert$ | $1.000000\times10^{-21}$ m |

**Result:** PASS. **Interpretation (L2):** reference and implementation perform
the same multiplication, so zero error shows agreement of the expressions, not
extraordinary precision and not an independent confirmation of the physics.

### 8.3 S2-T4 — Strain Linearity

| $A$ | Sampled peak (m) | Ratio | Expected | Ratio error |
|---:|---:|---:|---:|---:|
| $1\times10^{-21}$ | $1.000000\times10^{-21}$ | 1 | 1 | 0 |
| $2\times10^{-21}$ | $2.000000\times10^{-21}$ | 2.000000000000000 | 2 | 0 |
| $5\times10^{-21}$ | $5.000000\times10^{-21}$ | 5.000000000000000 | 5 | 0 |

**Result:** PASS. The grid is a methodological choice, not a physical one; the
physical requirement is only $|h|\ll1$.

### 8.4 S2-T5 — Arm-Length Scaling

| $L_0$ (m) | Sampled peak (m) | Ratio | Expected | Ratio error |
|---:|---:|---:|---:|---:|
| 1 | $1.000000\times10^{-21}$ | 1 | 1 | 0 |
| 4 | $4.000000\times10^{-21}$ | 4.000000000000000 | 4 | 0 |
| 10 | $1.000000\times10^{-20}$ | 10.000000000000000 | 10 | 0 |

**Result:** PASS. The 1/4/10 m grid is a table-top test grid and is not a
detector configuration.

### 8.5 S2-T6 — Sign Consistency

$\Delta L(+10^{-21})=+1.000000\times10^{-21}$ m;
$\Delta L(-10^{-21})=-1.000000\times10^{-21}$ m. Sign match: true. Exact
antisymmetry: true. Relative error 0.

**Result:** PASS (direct sign test). The auxiliary arm-length subtraction
$(1+0.5\times10^{-21})-(1-0.5\times10^{-21})$ is rejected as numerically
unresolvable (Finding F-02, Appendix B) and is not executed. The convention
$\Delta L=L_x-L_y$ is not redefined to accommodate any test.

### 8.6 S2-T7 — Zero-Strain Response

| Quantity | Absolute error | Tolerance |
|---|---:|---:|
| $\Delta L$ | 0 m | $10^{-32}$ m |
| $\Delta\phi$ | 0 rad | $10^{-32}$ rad |
| $I-I_0$ | 0 | $10^{-14}$ |

**Result:** PASS. Absolute error is used because relative error against an
expected zero is undefined.

### 8.7 S2-T8 — Time-Dependent Response

| Quantity | Value |
|---|---|
| Samples | 10 000 |
| Max absolute error (all samples) | 0 m (tolerance $10^{-35}$ m) |
| Near-peak relative error | 0 (tolerance $10^{-14}$; 900 samples) |
| Sampled mean, informational | $-4.815\times10^{-39}$ m |
| FFT peak bin, informational | 99.990 Hz |

**Result:** PASS. The sampled mean and the FFT bin are Level 4 diagnostics; the
`np.linspace` grid includes both endpoints, so neither is mathematically
required to equal exactly 0 or exactly 100 Hz (Finding F-03). The test
validates the implemented time-series mapping; it does not validate propagation
delay, cavity response, memory, finite-arm response, or control dynamics.

### 8.8 S2-T9 — Stage 2 → Stage 1 Integration at $h=10^{-21}$

| Quantity | Value |
|---|---|
| Phase relative error | 0 (tolerance $10^{-14}$) |
| Sampled peak phase | $1.181050\times10^{-14}$ rad (nominal $4\pi L_0A/\lambda$: $1.181050\times10^{-14}$) |
| Intensity absolute error | 0 (tolerance $10^{-14}$) |
| Expected peak $\Delta I$ (stable form) | $3.487\times10^{-29}$ |
| Implementation $I_0-\min I$ | 0 |

**Result:** **PASS — WITH NUMERICAL-RESOLUTION LIMITATION.**
The phase is reproduced. The physical intensity modulation exists
($3.487\times10^{-29}$) but is far below the float64 spacing near unity
($\approx2.2\times10^{-16}$), so the implementation returns exactly $1.0$.
A numerical intensity of $1.0$ is therefore **not** evidence that the physical
modulation is zero. The intensity tolerance of $10^{-14}$ is 15 orders of
magnitude larger than the signal and cannot detect it; the experiment does not
resolve the $10^{-29}$ modulation.

### 8.9 S2-T9S — Supplementary Method-Resolution Test at $h=10^{-7}$

| Quantity | Value |
|---|---|
| Peak phase | 1.181050 rad |
| Max $\Delta I$ (implementation) | 0.310023 |
| Phase relative error | 0 (tolerance $10^{-14}$) |
| Intensity absolute error | 0 (tolerance $10^{-14}$) |
| $\Delta I$ vs $I_0\sin^2(\Delta\phi/2)$, absolute error | $1.665\times10^{-16}$ (tolerance $10^{-14}$) |
| Signal resolvable in float64 | true |

**Result:** PASS. **Interpretation (L3):** with an $O(1)$ phase the optical
chain produces a numerically resolvable response and agrees with the exact
cosine law and with the independent stable form. This confirms that the optical
implementation behaves consistently for a resolvable perturbation. It does
**not** demonstrate direct resolution of the $h=10^{-21}$ intensity
modulation, and it does not replace the S2-T9 result, which keeps its
limitation. $h=10^{-7}$ satisfies the weak-field condition and is a
methodological test strain, not a physical expectation.

### 8.10 S2-T10 — Approximation-Regime Validation

| Configuration | $L_0$ (m) | $f^*$ (Hz) | $f/f^*$ |
|---|---:|---:|---:|
| Baseline (S2-T3, T4, T6–T9, T9S) | 1 | $4.7713\times10^{7}$ | $2.096\times10^{-6}$ |
| S2-T5 | 4 | $1.1928\times10^{7}$ | $8.383\times10^{-6}$ |
| S2-T5 | 10 | $4.7713\times10^{6}$ | $2.096\times10^{-5}$ |

**Result:** PASS. All executed configurations satisfy $f/f^*\le0.1$ by more than
four orders of magnitude. The 0.1 factor is a project-adopted operational
criterion, not a fundamental boundary of General Relativity. This is not a
finite-arm transfer-function validation.

## 9. Evidence Strength: What Each Test Can and Cannot Detect

| Test | Level | Can detect | Cannot detect |
|---|---|---|---|
| S2-T1, S2-T2 (post) | L2 | wrong factor, sign or wiring in the arm functions relative to the frozen expression | an error in the physics of $\pm\tfrac12$ itself (Documents 1–2) |
| S2-T3 | L2 | a coding change that breaks $\Delta L=hL_0$ | an incorrect baseline relation |
| S2-T4, S2-T5 | L2 | loss of linearity or of $L_0$ proportionality in the code | nonlinear physics at larger $h$ |
| S2-T6 | L2 | a sign-convention reversal | — |
| S2-T7 | L2 | a nonzero offset at $h=0$ | — |
| S2-T8 | L2 (L4 for mean, FFT, near-peak) | sample-wise errors in the time series | detector dynamics |
| S2-T9 | L2, with an L3 limitation | an error in the displacement-to-phase factor | the $10^{-29}$ intensity modulation |
| S2-T9S | L3 (its $\Delta I$ comparison with $I_0\sin^2(\Delta\phi/2)$ is an independent formula check, L1 within the optical relation) | an error in the optical chain at a resolvable signal | behavior at $h=10^{-21}$ |
| S2-T10 | L1 (parameter admissibility against the analytical LWA condition) | test parameters outside the LWA regime | finite-arm response |

No test in this document independently validates the physical relation
$h\rightarrow\Delta L$; that evidence belongs to Documents 1 and 2. Exact zero
errors in S2-T1 to S2-T8 are Level 2 self-consistency and must not be read as
evidence of extraordinary numerical precision.

## 10. Findings and Numerical Limitations

| ID | Finding | Classification | Effect |
|---|---|---|---|
| F-01 | $\delta L_x,\delta L_y$ not exposed | Implementation gap | S2-T1, S2-T2 blocked; resolved in Part III |
| F-02 | A $10^{-21}$ m difference cannot be recovered by subtracting two $\approx1$ m float64 values | Numerical limitation | Auxiliary T6 construction rejected; design rule for Step 12 |
| F-03 | The `linspace` grid includes both endpoints, so the sample interval is not exactly 10 µs | Numerical limitation | Mean and FFT bin are diagnostics only |
| F-04 | At $h=10^{-21}$, $\Delta I\approx3.5\times10^{-29}$ is below float64 resolution near 1 | Numerical limitation | Limitation attached to S2-T9; S2-T9S added |
| F-05 | The runner's computation is inside a plotting function and cannot be called separately; in pre-implementation mode the script reproduces its expression `arm_length * strain` | Test-access limitation (new in this record) | S2-T3 to S2-T9 exercise `src` functions and a verbatim copy of the runner's expression, not the runner itself |
| F-06 | The three-line runner edit made in Step 12 is not exercised by the validation script | Test-access limitation (new in this record) | Closed at the level of printed runner output by the before/after runner comparison in §14.3; residual limits are stated there |

## 11. Pre-Implementation Conclusion and Frozen Historical Record

The pre-implementation validation established the baseline state of the Stage 2
implementation. S2-T1 and S2-T2 could not be executed, because the
implementation did not contain explicit individual-arm perturbations
($\delta L_x$, $\delta L_y$). All executable tests, S2-T3 through S2-T10, passed.
S2-T9 passed with the documented float64 numerical-resolution limitation.
S2-T9S confirmed that the optical chain is numerically consistent at a larger,
resolvable test strain; it did not resolve the $h=10^{-21}$ modulation.
**Overall pre-implementation result: no failures.**

**Frozen historical statuses:** S2-T1 BLOCKED · S2-T2 BLOCKED · S2-T3 PASS ·
S2-T4 PASS · S2-T5 PASS · S2-T6 PASS (direct sign test; auxiliary construction
rejected) · S2-T7 PASS · S2-T8 PASS · S2-T9 PASS with float64-resolution
limitation · S2-T9S PASS · S2-T10 PASS.

---

# Part III — Controlled Implementation Update and Revalidation (Step 12)

## 12. Requirement and Gap Traceability

The Step 12 rule is that no implementation change precedes the physical
requirement and its validation test. The sequence for this update was:

$$
\text{physics}\rightarrow\text{derivation}\rightarrow\text{literature}\rightarrow\text{assumptions}\rightarrow\text{code audit}\rightarrow\text{numerical validation}\rightarrow\text{documented gap (F-01)}\rightarrow\text{update}\rightarrow\text{re-run}
$$

**Requirement:** the implementation must expose $\delta L_x=+\tfrac12hL_0$ and
$\delta L_y=-\tfrac12hL_0$ as separate quantities and form
$\Delta L_\mathrm{arm}=\delta L_x-\delta L_y$ from them, so that S2-T1 and
S2-T2 become executable.

**Numerical design rule (from F-02):** the perturbations must never be added to
the nominal arm length ($L_0+\delta L$) before the difference is formed. At
$10^{-21}$ m next to 1 m, both sums round to $L_0$ and the difference becomes
zero in float64.

## 13. Specification of the Update

| File | Change |
|---|---|
| `src/gravitational_wave.py` | Add `arm_perturbations` and `differential_arm_perturbation`; update the module docstring (the former statement that arm conversion "belongs in the simulation layer" no longer holds) |
| `simulations/gravitational_wave_injection.py` | Extend the import; replace one line with two |
| `src/interferometer.py` | **No change** |

New functions (appended after `sinusoidal_strain`, which is unchanged):

```python
def arm_perturbations(
    strain: float | np.ndarray,
    arm_length: float,
) -> tuple[float | np.ndarray, float | np.ndarray]:
    """Return individual arm perturbations (delta_Lx, delta_Ly) in metres."""
    delta_Lx = 0.5 * strain * arm_length
    delta_Ly = -0.5 * strain * arm_length
    return delta_Lx, delta_Ly


def differential_arm_perturbation(
    delta_Lx: float | np.ndarray,
    delta_Ly: float | np.ndarray,
) -> float | np.ndarray:
    """Return the differential displacement delta_Lx - delta_Ly in metres."""
    return delta_Lx - delta_Ly
```

Runner import (replacing the single import of `sinusoidal_strain`):

```python
from src.gravitational_wave import (  # noqa: E402
    arm_perturbations,
    differential_arm_perturbation,
    sinusoidal_strain,
)
```

Runner line (replacing `differential_displacement = arm_length * strain`):

```python
    delta_Lx, delta_Ly = arm_perturbations(strain, arm_length)
    differential_displacement = differential_arm_perturbation(delta_Lx, delta_Ly)
```

**Not changed:** the Stage 1 optical equations, photodetector physics, any
finite-arm transfer function, cavity-pole modeling, sinc damping, and all
plotting and printing.

## 14. Post-Implementation Revalidation

The same script was re-run unchanged. It detects the new functions and switches
to post-implementation mode. The tolerances of Section 6 apply.

### 14.1 S2-T1 and S2-T2 (new executions)

| Test | Quantity | Max relative error | Max absolute error | Peak |
|---|---|---:|---:|---:|
| S2-T1 | $\delta L_x$ vs $+\tfrac12 hL_0$ | 0 | 0 m | $5.000000\times10^{-22}$ m |
| S2-T2 | $\delta L_y$ vs $-\tfrac12 hL_0$ | 0 | 0 m | $5.000000\times10^{-22}$ m |

**Result:** PASS (both). Informational diagnostics (Level 4):
$\max\lvert\delta L_x+\delta L_y\rvert=0$; $\delta L_x-\delta L_y$ is
bitwise equal to $L_0h$; the relative difference from the proper-distance form
$L_0(\sqrt{1\pm h}-1)$, evaluated in the stable form $L_0h/(\sqrt{1\pm h}+1)$,
is 0 to the printed precision. The two forms differ analytically: for the individual
arms by a relative $h/4\approx2.5\times10^{-22}$ (from the $-h^2/8$ term of
$\sqrt{1\pm h}$), and for the differential combination only by a relative
$h^2/8\sim10^{-43}$ (Document 1, higher-order note). Both are far below float64
resolution, so a zero difference is expected and does not test those terms.
**Interpretation (L2):** the exact agreement is expected by construction:
multiplication by $0.5$ is exact in binary floating point, so
$(0.5hL_0)-(-0.5hL_0)$ equals $hL_0$ exactly. The tests confirm that the new
functions implement the frozen expressions with the correct signs and
antisymmetry. They are not an independent confirmation of the factor
$\tfrac12$, which is established in Documents 1 and 2.

### 14.2 S2-T3 to S2-T10 (regression)

All results were identical in status and in every recorded error to the
pre-implementation values in Section 8: S2-T3 to S2-T8 PASS with zero error;
S2-T9 PASS with the same float64 limitation (expected $\Delta I=3.487\times10^{-29}$,
implementation $I_0-\min I=0$); S2-T9S PASS (max $\Delta I=0.310023$,
$\Delta I$-vs-stable-form error $1.665\times10^{-16}$); S2-T10 PASS with
unchanged $f/f^*$ values.

### 14.3 Runner Comparison (F-06)

The validation script exercises the `src` functions but not the runner. To
check the runner edit itself, the runner was executed twice and its printed
output compared:

- **Before the update:** the original `simulations/gravitational_wave_injection.py`
  with the unmodified `src/gravitational_wave.py`.
- **After the update:** the patched copy
  `simulations/gravitational_wave_injection_patched.py`, which calls
  `arm_perturbations()` and `differential_arm_perturbation()`.

| Printed line | Before | After |
|---|---|---|
| Laser wavelength | $1.064\times10^{-6}$ m | $1.064\times10^{-6}$ m |
| Arm length | 1.000 m | 1.000 m |
| Strain amplitude | $1.000\times10^{-21}$ | $1.000\times10^{-21}$ |
| GW frequency | 100.0 Hz | 100.0 Hz |
| Peak $\Delta L$ | $1.000\times10^{-21}$ m | $1.000\times10^{-21}$ m |
| Peak phase shift | $1.181\times10^{-14}$ rad | $1.181\times10^{-14}$ rad |
| Intensity change range | 0 to 0 | 0 to 0 |
| Small-angle estimate | $\sim3.487\times10^{-29}$ | $\sim3.487\times10^{-29}$ |
| Plots saved | four | four |

**Result:** the printed output is identical before and after. This is
consistent with the script result that $\delta L_x-\delta L_y$ is bitwise equal
to $L_0h$ (§14.1), and it shows that the edited runner still produces the same
peak $\Delta L$, peak phase and intensity behavior, including the float64
limitation on the intensity change (F-04).

**Limits of this check.** The printed values have four significant digits, so
the comparison does not by itself establish bit-level equality of the runner's
arrays. The saved plots were not compared. The operating system, Python and
NumPy versions of these two runs were not recorded. The post-update run used a
separate patched copy of the runner, not an in-place edit of the original file;
whether the repository's original runner has since been edited in place is not
recorded here.

## 15. Before → After and Traceability

### 15.1 Before → After

| Test | Pre-implementation | Post-implementation |
|---|---|---|
| S2-T1 | BLOCKED | PASS |
| S2-T2 | BLOCKED | PASS |
| S2-T3 | PASS | PASS |
| S2-T4 | PASS | PASS |
| S2-T5 | PASS | PASS |
| S2-T6 | PASS | PASS |
| S2-T7 | PASS | PASS |
| S2-T8 | PASS | PASS |
| S2-T9 | PASS (float64 limitation) | PASS (same limitation) |
| S2-T9S | PASS | PASS |
| S2-T10 | PASS | PASS |

### 15.2 Requirement → Change → Test → Result

| Requirement | Change | Affected tests | Post-change result |
|---|---|---|---|
| Expose $\delta L_x$ (F-01) | `arm_perturbations()` | S2-T1 | PASS |
| Expose $\delta L_y$ (F-01) | `arm_perturbations()` | S2-T2 | PASS |
| Form $\Delta L=\delta L_x-\delta L_y$ without $L_0+\delta L$ (F-02) | `differential_arm_perturbation()` | S2-T3, S2-T8 (and downstream S2-T4 to S2-T7, S2-T9, S2-T9S) | PASS; output bit-identical to the pre-change $L_0h$ |
| Leave Stage 1 optics untouched | none | S2-T9, S2-T9S | PASS; unchanged |
| Runner uses the new functions | three-line runner edit | runner before/after comparison (§14.3); not exercised by the script (F-06) | printed output identical before and after (to the printed precision) |

---

# Part IV — Closure

## 16. Overall Numerical-Validation Conclusion

The post-implementation validation confirms that the Stage 2 individual-arm
response has been implemented. S2-T1 and S2-T2, previously blocked by the
implementation gap, are now executable and both PASS. The implemented arm
perturbations satisfy the expected antisymmetry
($\max\lvert\delta L_x+\delta L_y\rvert=0$), and their differential response is
bitwise equal to $L_0h$. All previously executable tests, S2-T3 through S2-T10,
continue to PASS. S2-T9 retains the documented float64 numerical-resolution
limitation, while S2-T9S confirms the optical chain at a resolvable test
strain. **Overall post-implementation result: no failures.**

**Established:** the implemented Stage 2 mapping, in both its pre- and
post-update form, reproduces $\Delta L_\mathrm{arm}(t)=h(t)L_0$, its
decomposition into $\delta L_x=+\tfrac12hL_0$ and $\delta L_y=-\tfrac12hL_0$,
linearity in $h$, proportionality to $L_0$, the sign convention, the
zero-strain limit, and the Stage 2 → Stage 1 phase interface, within the
stated tolerances and under the stated assumptions; all test parameters lie in
the LWA regime.

**Not established:** independent numerical confirmation of the physics of the
mapping (Level 2 limitation, §9); direct resolution of the $10^{-29}$ intensity
modulation at $h=10^{-21}$ (S2-T9S does not provide this); bit-level or
plot-level equality of the runner's outputs (§14.3 compares printed values to
four significant digits only); and anything outside the frozen baseline (§17).

## 17. Limitations and Boundaries

- **Evidence strength.** Tests S2-T1 to S2-T8 are self-consistency checks
  (Level 2). The independent physical evidence is in Documents 1 and 2.
- **Float64 resolution at the physical baseline.** At $L_0=1$ m, the
  $h=10^{-21}$ bright-port modulation is $\approx3.5\times10^{-29}$. For
  reference, at $L_0=4$ km the phase scale is $\approx4.7\times10^{-11}$ rad
  and the quadratic modulation $\Delta\phi^2/4\approx5.6\times10^{-22}$, which
  is also far below float64 spacing near unity. At equal arms the bright-port
  response is quadratic in $\Delta\phi$; linearization about an operating point
  belongs to a later stage.
- **Tolerances.** All tolerances are methodological numerical criteria (§6.1).
  They were validated on two execution environments only.
- **Auxiliary diagnostics.** The mean, the FFT bin, the near-peak threshold
  and the proper-distance comparison are Level 4 information.
- **Test access.** The script exercises the `src` functions and, before the
  update, a verbatim copy of the runner's expression (F-05). It does not execute
  the edited runner lines. F-06 was addressed by running the runner before and
  after the update and comparing the printed lines (§14.3); that comparison has
  four-digit precision, did not compare plots, and used a separate patched copy
  of the runner.
- **Bright port only,** a single physical baseline ($A=10^{-21}$, $f=100$ Hz,
  $L_0=1$ m) and table-top arm lengths.
- **Not validated:** finite-arm transfer function, cavity dynamics, TDI,
  antenna patterns and general polarization, network response, noise, and
  real data. These are outside the frozen Stage 2 baseline. This record is not
  experimental validation, and the master synthesis belongs to Document 5.

## 18. Reproducibility and Traceability

**Repository:** `gravitational-wave-detector-research`.
**Commit hash:** not yet available. The Stage 2 documents, the patched
`src/gravitational_wave.py`, the edited runner and the validation script are to
be captured together in one closing commit; this section will be updated with
that hash.
**Script:** `validation/stage2_numerical_validation.py`.
**Run command:** `PYTHONPATH=. python3 validation/stage2_numerical_validation.py`.
**Mode selection:** automatic. Pre-implementation mode when
`arm_perturbations` is absent from `src.gravitational_wave`; post-implementation
mode when it is present. The original `src/gravitational_wave.py` was
preserved for the pre-implementation run.

| | Environment 1 | Environment 2 |
|---|---|---|
| Python | 3.12.10 | 3.12.3 |
| NumPy | 2.5.3 | 2.4.4 |
| OS | Windows 11 | Linux |
| Pre-implementation run | S2-T1/T2 BLOCKED; all others PASS | same |
| Post-implementation run | S2-T1 to S2-T10 and S2-T9S PASS | same |

Environment 2 was executed in a separate sandbox using the repository module
sources as provided (`src/interferometer.py` and the original and patched
`src/gravitational_wave.py`). The runner was not part of it.

Differences between environments are confined to informational values and one
error that remained far inside its tolerance:

| Quantity | Environment 1 | Environment 2 |
|---|---:|---:|
| Sampled mean of $\Delta L$ (S2-T8, informational) | $-4.815\times10^{-39}$ m | $-9.630\times10^{-39}$ m |
| S2-T9S $\Delta I$ vs stable form, absolute error | $1.665\times10^{-16}$ | $1.110\times10^{-16}$ |

Every PASS/FAIL status, and every other recorded error, was identical in the
two environments.

## 19. Source Provenance

Inputs to this record: the Stage 2 step plan (Steps 10 and 12); the frozen
Step 10 numerical framework and the pre-implementation numerical record; the
Step 10 tolerance audit; the Step 10 input-provenance analysis; the Document 3
gap register; the Stage 1 `analytical_model.md`, `literature_validation.md` and
`numerical_validation.md` (format and conventions); the repository sources
quoted in Sections 4 and 13; and the raw outputs of
`validation/stage2_numerical_validation.py` in both execution environments.

---

## Appendix A — Constants and Derived Scales

| Quantity | Value |
|---|---|
| Float64 machine epsilon $2^{-52}$ | $2.22\times10^{-16}$ |
| $\Delta\phi_\mathrm{max}=4\pi L_0A/\lambda$ ($L_0=1$ m, $A=10^{-21}$, 1064 nm) | $1.18105\times10^{-14}$ rad |
| $\Delta I_\mathrm{max}\approx\Delta\phi_\mathrm{max}^2/4$ | $3.487\times10^{-29}$ |
| $f^*$ at $L_0=1$, 4, 10 m | $4.7713\times10^{7}$, $1.1928\times10^{7}$, $4.7713\times10^{6}$ Hz |
| $f/f^*$ at $f=100$ Hz, $L_0=1$, 4, 10 m | $2.096\times10^{-6}$, $8.383\times10^{-6}$, $2.096\times10^{-5}$ |
| $1-\mathrm{sinc}(f/f^*)$ at the baseline (physical, §4.4) | $\approx7.3\times10^{-13}$ |
| S2-T9S phase at $h=10^{-7}$, $L_0=1$ m | 1.181050 rad |

## Appendix B — Rejected and Superseded Constructions

1. **S2-T6 auxiliary subtraction** $(1+0.5\times10^{-21})-(1-0.5\times10^{-21})$.
   Evaluates to 0 in float64 because both operands equal 1.0 (Finding F-02).
   Rejected as a numerically unresolvable test; never used as a PASS/FAIL
   criterion. The implementation was not modified to accommodate it. The
   tolerance audit listed this construction among the T6 quantities; the final
   Step 10 record supersedes it.
2. **Earlier validation plan** (Step 7 Run 3: T1–T7 and M1–M3). Superseded by
   the final S2-T1 to S2-T10 set.
3. **Stable form as an implementation measurement.** $I_0\sin^2(\Delta\phi/2)$
   gives a reliable *expected* value at $h=10^{-21}$. It does not make the
   implementation's intensity resolvable, because `photodetector_intensity()`
   still returns exactly 1.0 there. The only test that exercises the
   implementation at a resolvable signal is S2-T9S.

## Appendix C — Frozen Methodological Decisions

1. The S2-T9S tolerance of $10^{-14}$ is retained as a methodological numerical
   acceptance criterion (§6.3). It is not physics-derived and is not claimed to
   be a machine-independent floating-point bound.
2. The S2-T8 near-peak criterion $|\Delta L|\ge0.99\max|\Delta L|$ is retained as
   an auxiliary data-analysis diagnostic with no physical status (§6.4). The
   primary S2-T8 comparison covers the complete time series.
3. S2-T9S ($h=10^{-7}$) is retained. Its success demonstrates numerical
   consistency of the optical response for a resolvable perturbation. It does
   not demonstrate direct float64 resolution of the $h=10^{-21}$ modulation.
4. Exact zero errors in tests whose reference and implementation perform
   algebraically identical operations are interpreted as implementation/formula
   self-consistency, not as independent numerical validation or unlimited
   precision.

## Appendix D — Traceability to Other Stage 2 Documents

| This record | Depends on |
|---|---|
| §3 frozen references | Document 1 (derivation, individual-arm response, interface) |
| §3, §9 evidence boundaries | Document 2 (literature verification and validity domain) |
| §4, §10, §12 gap register and findings | Document 3 (code audit and gap register) |
| §16, §17 limitations | feeds Document 5 (limitations and master conclusion) |

---

*End of document. This record is the numerical-validation input to the Stage 2
limitations and master conclusion.*
