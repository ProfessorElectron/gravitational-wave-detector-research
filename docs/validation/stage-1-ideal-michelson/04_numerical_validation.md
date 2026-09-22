# Phase 1 Numerical Validation — Ideal Michelson Interferometer

**Status:** Complete. This document is the computational evidence record for
Phase 1: it establishes whether `src/interferometer.py`, together with an
independently constructed field-level reference model, numerically
reproduces the frozen analytical predictions of `analytical_model.md`. It
is evidence, not a fourth derivation and not a repeat of the code audit.

---

## 1. Purpose and Scope

### 1.1 Purpose

$$
\boxed{\text{implemented}\neq\text{validated}\neq\text{physically justified}}
$$

`analytical_model.md` establishes what was derived. `literature_validation.md`
establishes that it is externally supported. `code_and_simulation_audit.md`
establishes what the repository implements. This document establishes the
remaining leg: whether the implementation numerically *reproduces* the
frozen analytical predictions, to the precision available in double-precision
arithmetic. The tests do not determine the physics model — they test its
computational implementation against a baseline that was already fixed
before any test was run.

### 1.2 Validation Boundary

**In scope:** the ideal two-arm Michelson interferometer — differential
arm-length response, round-trip optical path difference, optical phase
difference, the 50:50 beamsplitter, bright-port response, dark-port
complementary response, field-level recombination, power conservation,
periodicity and symmetry, and numerical fringe structure.

**Explicitly excluded**, consistent with `analytical_model.md` §1.2 and
`literature_validation.md` §6.5: GW strain → displacement, polarization and
antenna response, operating-point linearization, physical detector noise,
PSD/ASD modelling, sensitivity, matched filtering/SNR, and public GW data.

### 1.3 Relationship to Earlier Phase 1 Work

$$
\text{Independent analytical derivation}
\rightarrow
\text{Assumptions and conventions}
\rightarrow
\text{Literature validation}
\rightarrow
\text{Frozen Phase 1 analytical model}
\rightarrow
\text{Code implementation}
\rightarrow
\text{Numerical validation (this document)}
$$

Conventions and assumptions are integrated into `analytical_model.md` (§3,
§18) rather than existing as a separate file; this document cites those
sections directly.

---

## 2. Validated Analytical Reference Model

Extraction only — full derivations live in `analytical_model.md`.

| # | Relation | Source |
|---|---|---|
| 2.1 | $\Delta L_\mathrm{arm}=L_x-L_y$ | `analytical_model.md` §4 |
| 2.2 | $\Delta L_\mathrm{rt}=2\Delta L_\mathrm{arm}$ | `analytical_model.md` §5 |
| 2.3 | $\Delta\phi=\dfrac{2\pi}{\lambda}\Delta L_\mathrm{rt}=\dfrac{4\pi}{\lambda}\Delta L_\mathrm{arm}$ | `analytical_model.md` §6 |
| 2.4 | $B=\dfrac{1}{\sqrt2}\begin{pmatrix}1&i\\i&1\end{pmatrix}$ | `analytical_model.md` §7.1 |
| 2.5 | $I_\mathrm{bright}=\dfrac{I_0}{2}(1+\cos\Delta\phi)$ | `analytical_model.md` §9 |
| 2.6 | $I_\mathrm{dark}=\dfrac{I_0}{2}(1-\cos\Delta\phi)$ | `analytical_model.md` §9 |
| 2.7 | $I_\mathrm{bright}+I_\mathrm{dark}=I_0$ | `analytical_model.md` §9 |
| 2.8 | $I(\Delta L+\lambda/2)=I(\Delta L)$; $I(+\Delta L)=I(-\Delta L)$ | `analytical_model.md` §13–§14 |

---

## 3. Numerical Validation Methodology

### 3.1 Validation Philosophy

Code is evidence to be tested against the baseline in Section 2 — it is not
itself the source of physical truth. Every test below compares a computed
value against a value predicted independently of that computation.

### 3.2 Test Classification

| Test | Classification |
|---|---|
| T1 | Core |
| T2 | Core consistency (no independent round-trip function exists — see §5.2) |
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

### 3.3 Numerical Precision and Tolerance

All tests were executed in IEEE 754 double precision. Observed discrepancies
across the two independently run environments (§12) range from exactly
$0$ to $\sim2.78\times10^{-16}$ for ordinary floating-point roundoff, down
to $\sim10^{-22}$–$10^{-33}$ at points where a quantity is analytically
exactly zero. One outlier is expected and pre-explained here: **T5** shows
a discrepancy of $\approx5.77\times10^{-10}$ at $\Delta L=\lambda/8$,
several orders larger than ordinary roundoff. This is attributed to the
floating-point representation of $\lambda/8$ as an arm-length value
*before* the trigonometric evaluation, not to an implementation error — it
reproduced to three significant figures across both independent runs
($5.773\times10^{-10}$ and the originally recorded $5.77\times10^{-10}$),
which is itself evidence that it is a deterministic representation artifact
rather than noise. No test claims exact bitwise equality; all pass/fail
decisions use explicit, stated tolerances.

### 3.4 Reproducibility

Recorded in full in Section 12.

---

## 4. Test Results Overview

| Test | Validation Target | Classification | Result |
|---|---|---|---|
| T1 | Differential arm length | Core | PASS |
| T2 | Round-trip factor | Core consistency | PASS |
| T3 | Phase difference | Core | PASS |
| T4 | Bright-port intensity | Core | PASS |
| T5 | End-to-end chain | Core | PASS |
| T6 | Periodicity + symmetry | Core structural | PASS |
| T7 | Fringe spacing | Core numerical | PASS |
| T8 | Intensity bounds | Supplementary sanity | PASS |
| T9 | Equal-arm point | Supporting | PASS |
| T10 | 50:50 beamsplitter | Core field-level | PASS |
| T11 | Field-level recombination | Strong independent reference | PASS |
| T12 | Bright + dark energy conservation | Core conservation | PASS |
| T13 | Dark-port known answers | Complementary output | PASS |

**T1–T13 passed in both independently executed environments (§12). No
physics-driven modification to the Phase 1 implementation was required.**

---

## 5. Detailed Validation Tests

Expected/Obtained/Error fields below hold multiple test cases per test
where the underlying test has more than one case; this mirrors how each
test was actually structured and executed.

### 5.1 T1 — Differential Arm-Length Validation

**Objective:** verify $\Delta L_\mathrm{arm}=L_x-L_y$ (§2.1), including
sign, not merely magnitude.

**Reference:** `analytical_model.md` §4.

**Method:** direct evaluation of `differential_arm_length(Lx, Ly)` against
independently computed expected values.

| Case | $L_x$ (m) | $L_y$ (m) | Expected | Obtained | Abs. error |
|---|---|---|---|---|---|
| Equal arms | 1.0 | 1.0 | 0 | 0 | 0 |
| X longer | 1.0000001 | 1.0 | $1.0\times10^{-7}$ | $1.0000000005838672\times10^{-7}$ | $5.84\times10^{-17}$ |
| Y longer | 1.0 | 1.0000001 | $-1.0\times10^{-7}$ | $-1.0000000005838672\times10^{-7}$ | $5.84\times10^{-17}$ |
| Ordinary unequal | 1.2 | 0.8 | 0.4 | 0.3999999999999999 | $1.11\times10^{-16}$ |

**Result:** PASS. **Interpretation:** confirms the full-difference
convention with correct sign in all four cases; establishes nothing about
the round-trip or phase relations, which are separate tests.

### 5.2 T2 — Round-Trip Optical Path Difference and Factor of 2

**Objective:** verify $\Delta L_\mathrm{rt}=2\Delta L_\mathrm{arm}$ (§2.2)
and its consistency with $\Delta\phi=\frac{2\pi}{\lambda}\Delta L_\mathrm{rt}$.

**Reference:** `analytical_model.md` §5.

**Method:** `src/interferometer.py` has no separate round-trip function —
`phase_difference()` folds the factor of 2 directly into $4\pi/\lambda$
(`code_and_simulation_audit.md` §5.2). This test therefore computes
$\Delta L_\mathrm{rt}=2\Delta L_\mathrm{arm}$ and its phase independently in
two steps, and compares the result against `phase_difference()`'s single-step
output — a cross-formulation consistency check, not a test of a separate
implementation.

| Case | $\Delta L_\mathrm{arm}$ (m) | Expected phase (rad) | Obtained phase (rad) | Abs. error |
|---|---|---|---|---|
| Positive | $+1\times10^{-9}$ | $+0.011810498697706$ | $+0.011810498697706$ | $0$ |
| Negative | $-1\times10^{-9}$ | $-0.011810498697706$ | $-0.011810498697706$ | $0$ |

**Result:** PASS. **Interpretation:** confirms the double-pass factor of 2
is neither omitted nor double-counted, and that the sign convention from T1
is preserved through the phase relation. Does not independently validate a
standalone round-trip function, since none exists.

### 5.3 T3 — Phase-Difference Known-Answer Validation

**Objective:** verify $\Delta\phi=\frac{4\pi}{\lambda}\Delta L_\mathrm{arm}$
(§2.3) against physically known phase values, avoiding circular validation
against the production formula itself.

**Reference:** `analytical_model.md` §6. $\lambda=1064$ nm throughout.

| $\Delta L_\mathrm{arm}$ | Expected $\Delta\phi$ | Obtained $\Delta\phi$ | Abs. error |
|---|---|---|---|
| $0$ | $0$ | $0$ | $0$ |
| $\lambda/8$ | $\pi/2$ | $1.5707963267948966$ | $0$ |
| $\lambda/4$ | $\pi$ | $3.1415926535897931$ | $0$ |
| $\lambda/2$ | $2\pi$ | $6.2831853071795862$ | $0$ |
| $-\lambda/4$ | $-\pi$ | $-3.1415926535897931$ | $0$ |

Additional property checks: $\phi(-x)=-\phi(x)$ — PASS; $\phi(2x)=2\phi(x)$
— PASS.

**Result:** PASS. **Interpretation:** the primary cases are derived from
independently known physical phase conditions ($\lambda/8\to\pi/2$, etc.),
not from re-evaluating the production equation, which is what makes this a
genuine known-answer test rather than a tautology.

### 5.4 T4 — Bright-Port Intensity and Interference Conditions

**Objective:** verify $I_\mathrm{bright}=\frac{I_0}{2}(1+\cos\Delta\phi)$
(§2.5) and reproduce constructive, destructive, and intermediate
interference. $\lambda=1064$ nm, $I_0=1$.

| $\Delta L_\mathrm{arm}$ | Expected $I_\mathrm{bright}$ | Obtained | Abs. error |
|---|---|---|---|
| $0$ | $1$ | $1.000000000000000$ | $0$ |
| $\lambda/8$ | $0.5$ | $0.500000000000000$ | $0$ |
| $\lambda/4$ | $0$ | $0.000000000000000$ | $0$ |
| $\lambda/2$ | $1$ | $1.000000000000000$ | $0$ |
| $-\lambda/4$ | $0$ | $0.000000000000000$ | $0$ |

**Result:** PASS. **Interpretation:** constructive ($\Delta\phi=2\pi n$),
destructive ($\Delta\phi=(2n+1)\pi$), and intermediate ($\Delta\phi=\pi/2$)
conditions are all reproduced exactly by `photodetector_intensity()`.

### 5.5 T5 — End-to-End Implementation Chain

**Objective:** verify the composed chain
$L_x,L_y\to\texttt{differential\_arm\_length()}\to\texttt{phase\_difference()}\to\texttt{photodetector\_intensity()}$
via `intensity_from_arm_lengths()`.

**Reference:** `analytical_model.md` §10.

| $\Delta L_\mathrm{arm}$ | Expected $I$ | Obtained | Abs. error |
|---|---|---|---|
| $0$ | $1.0$ | $1.000000000000$ | $0$ |
| $\lambda/8$ | $0.5$ | $0.500000000577303$ | $5.77\times10^{-10}$ |
| $\lambda/4$ | $0$ | $0.000000000000$ | $0$ |
| $\lambda/2$ | $1.0$ | $1.000000000000$ | $0$ |
| $-\lambda/4$ | $0$ | $0.000000000000$ | $0$ |

**Result:** PASS. **Interpretation:** the individually validated relations
(T1, T3, T4) are also correctly composed in the actual repository
implementation. The $\lambda/8$ discrepancy is the pre-explained
floating-point representation artifact (§3.3), not a physics or
implementation error.

### 5.6 T6 — Periodicity and Symmetry

**Reference:** `analytical_model.md` §13–§14 (§2.8). $\lambda=1064$ nm.

#### 5.6.1 Periodicity: $I(\Delta L+\lambda/2)=I(\Delta L)$

| $\Delta L/\lambda$ | $I(\Delta L)$ | $I(\Delta L+\lambda/2)$ | Difference |
|---|---|---|---|
| $-0.37$ | $0.468604740235$ | $0.468604740235$ | $2.78\times10^{-16}$ |
| $-0.10$ | $0.654508497187$ | $0.654508497187$ | $1.11\times10^{-16}$ |
| $0$ | $1.000000000000$ | $1.000000000000$ | $0$ |
| $0.13$ | $0.468604740235$ | $0.468604740235$ | $2.22\times10^{-16}$ |
| $0.49$ | $0.996057350657$ | $0.996057350657$ | $1.11\times10^{-16}$ |

#### 5.6.2 Symmetry: $I(+\Delta L)=I(-\Delta L)$

| $\Delta L/\lambda$ | $I(+\Delta L)$ | $I(-\Delta L)$ | Difference |
|---|---|---|---|
| $-0.37$ | $0.468604740235$ | $0.468604740235$ | $0$ |
| $-0.10$ | $0.654508497187$ | $0.654508497187$ | $0$ |
| $0$ | $1.000000000000$ | $1.000000000000$ | $0$ |
| $0.13$ | $0.468604740235$ | $0.468604740235$ | $0$ |
| $0.49$ | $0.996057350657$ | $0.996057350657$ | $0$ |

**Result:** PASS. **Interpretation:** confirms the fringe period is
$\lambda/2$ and the response is even in $\Delta L$, both at floating-point
precision.

### 5.7 T7 — Numerical Fringe-Spacing Validation

**Objective:** verify $\Delta L_\mathrm{period}=\lambda/2$ (§2.8) directly
from the swept intensity pattern. $\lambda=1064$ nm; predicted spacing
$532$ nm.

**Method:** `photodetector_intensity()` swept over
$\Delta L\in[-2\lambda,2\lambda]$; fringe maxima located via sub-grid
parabolic interpolation around each detected local maximum.

| Quantity | Value |
|---|---|
| Fringe maxima detected | 7 |
| Expected spacing | $5.320000\times10^{-7}$ m |
| Measured mean spacing | $5.320000\times10^{-7}$ m |
| Max deviation | $1.06\times10^{-22}$ m |

**Result:** PASS. **Interpretation:** reproduces the analytically predicted
periodicity numerically. This measures the sweep's own output against the
same formula already established in T3/T6/§2.3, not an independently
constructed reference — the extremely small residual reflects that, and
should not be read as a stronger check than T10–T13.

### 5.8 T8 — Intensity Bounds

**Objective:** verify $0\le I_\mathrm{bright}\le I_0$ across several input
intensities. **Explicitly a supplementary sanity check, not an independent
physics validation.**

| $I_0$ | Min obtained | Max obtained | Bounds |
|---|---|---|---|
| $0$ | $0$ | $0$ | $[0,0]$ |
| $1$ | $0$ | $1$ | $[0,1]$ |
| $2.5$ | $0$ | $2.5$ | $[0,2.5]$ |
| $10$ | $0$ | $10$ | $[0,10]$ |

**Result:** PASS. **Interpretation:** the implementation produces no
negative or over-bound intensities across the tested range; does not by
itself establish the interference equations.

### 5.9 T9 — Equal-Arm Operating Point

**Objective:** verify the equal-arm condition
$L_x=L_y\Rightarrow\Delta L=0\Rightarrow\Delta\phi=0\Rightarrow
I_\mathrm{bright}=I_0,\ I_\mathrm{dark}=0$. $L_x=L_y=1$ m, $\lambda=1064$ nm.

| Quantity | Value |
|---|---|
| $\Delta L$ | $0$ |
| $\Delta\phi$ | $0$ |
| $I_\mathrm{bright}$ | $1.000000000000$ |
| $I_\mathrm{dark}$ (via conservation, not repository code) | $0.000000000000$ |
| $I_\mathrm{bright}+I_\mathrm{dark}$ | $1.000000000000$ |

**Result:** PASS. **Interpretation:** confirms the equal-arm bright-fringe
operating point. $I_\mathrm{dark}$ here is obtained via the conservation
relation $I_0-I_\mathrm{bright}$, since no dark-port function exists in the
repository (`code_and_simulation_audit.md` §5.4) — not an independent
dark-port measurement. Operating-point linearization near this point is
Stage 4 and is explicitly not tested here.

### 5.10 T10 — 50:50 Beamsplitter Validation

**Objective:** validate the beamsplitter convention $B$ (§2.4) — unitarity,
50:50 splitting, power conservation, relative phase. **Independent of
repository code**: no beamsplitter function exists in `src/interferometer.py`
(`code_and_simulation_audit.md` §5.4), so this validates the analytical
matrix directly, using $E_\mathrm{in}=\binom{1}{0}$.

#### 5.10.1 Unitarity ($B^\dagger B=I$)

Max deviation from identity: $2.22\times10^{-16}$. PASS.

#### 5.10.2 50:50 Power Splitting

$I_1=0.500000000000$, $I_2=0.500000000000$. PASS.

#### 5.10.3 Energy Conservation

$I_1+I_2=1.000000000000$, error $2.22\times10^{-16}$. PASS.

#### 5.10.4 Relative Phase

$\arg(E_2)-\arg(E_1)=1.5707963267948966$ rad, expected $\pi/2$. PASS.

**Result:** PASS. **Interpretation:** the frozen beamsplitter convention is
numerically lossless, exactly 50:50, and carries the correct $\pi/2$ phase
convention, independent of any repository implementation.

### 5.11 T11 — Field-Level Recombination Validation

**Objective:** starting from $B$, propagate both arm fields through their
round trips, recombine, and compare the resulting powers against the
frozen scalar predictions
$I_\mathrm{dark}=I_\mathrm{in}\sin^2(\Delta\phi/2)$,
$I_\mathrm{bright}=I_\mathrm{in}\cos^2(\Delta\phi/2)$. Deliberately
independent of `src/interferometer.py`.

| $\Delta L_\mathrm{arm}$ | $I_\mathrm{dark}$ (expected / obtained) | $I_\mathrm{bright}$ (expected / obtained) |
|---|---|---|
| $0$ | $0$ / $0$ | $1$ / $1$ |
| $\lambda/8$ | $0.5$ / $0.5$ | $0.5$ / $0.5$ |
| $\lambda/4$ | $1$ / $1$ | $0$ / $3.75\times10^{-33}$ |
| $\lambda/2$ | $0$ / $1.50\times10^{-32}$ | $1$ / $1$ |
| $-\lambda/4$ | $1$ / $1$ | $0$ / $3.75\times10^{-33}$ |

Non-special case $\Delta L=0.137\lambda$ ($\Delta\phi=1.7215927742$ rad):
expected $I_\mathrm{dark}=0.5751127945603786$,
$I_\mathrm{bright}=0.4248872054396214$; obtained
$I_\mathrm{dark}=0.5751127945603784$, $I_\mathrm{bright}=0.4248872054396212$;
max discrepancy $1.67\times10^{-16}$.

**Result:** PASS. **Interpretation:** the field-level calculation
reproduces the frozen scalar predictions from first principles — beamsplitter
$\to$ arm propagation $\to$ recombination $\to$ bright/dark intensities —
without using `photodetector_intensity()` at all. This is a substantially
stronger check than comparing the existing code against a restatement of
its own formula, which is why it is classified as "strong independent
reference" rather than merely "core."

### 5.12 T12 — Bright + Dark Power Conservation

**Objective:** verify $I_\mathrm{bright}+I_\mathrm{dark}=I_0$ (§2.7) using
the field-level model from T11, across both special and non-special phase
values.

| $\Delta\phi$ | $I_\mathrm{dark}$ | $I_\mathrm{bright}$ | Sum | Error |
|---|---|---|---|---|
| $0$ | $0.0000000000$ | $1.0000000000$ | $1.000000000000$ | $4.44\times10^{-16}$ |
| $\pi/2$ | $0.5000000000$ | $0.5000000000$ | $1.000000000000$ | $3.33\times10^{-16}$ |
| $\pi$ | $1.0000000000$ | $0.0000000000$ | $1.000000000000$ | $4.44\times10^{-16}$ |
| $1.234$ | $0.3347674460$ | $0.6652325540$ | $1.000000000000$ | $4.44\times10^{-16}$ |
| $2.7$ | $0.9520360710$ | $0.0479639290$ | $1.000000000000$ | $3.33\times10^{-16}$ |
| $-0.8$ | $0.1516466453$ | $0.8483533547$ | $1.000000000000$ | $4.44\times10^{-16}$ |

**Result:** PASS. **Interpretation:** the ideal lossless model correctly
distributes power between the two complementary output ports across every
tested phase, not just the special cases.

### 5.13 T13 — Dark-Port Known-Answer Validation

**Objective:** verify $I_\mathrm{dark}=\frac{I_0}{2}(1-\cos\Delta\phi)$
(§2.6) at known phase values, cross-checked against the T11 field-level
model.

| $\Delta\phi$ | Expected | Analytical relation | Field-level model |
|---|---|---|---|
| $0$ | $0$ | $0.000000000000$ | $0.000000000000$ |
| $\pi$ | $1$ | $1.000000000000$ | $1.000000000000$ |
| $\pi/2$ | $0.5$ | $0.500000000000$ | $0.500000000000$ |
| $-\pi$ | $1$ | $1.000000000000$ | $1.000000000000$ |

**Result:** PASS. **Interpretation:** the dark-port response is
analytically established and numerically validated, even though no
dark-port function exists in `src/interferometer.py`
(`code_and_simulation_audit.md` §5.4) — this test cross-checks the
analytical relation against the independent field-level model, not against
repository code.

---

## 6. Cross-Test Validation Summary

### 6.1 Mathematical Consistency

T1–T3, T6, T7 together confirm that the implementation reproduces
$L_x-L_y$, the round-trip factor of 2, the phase relation, periodicity, and
symmetry.

### 6.2 Optical Consistency

T10–T13 confirm 50:50 beamsplitter behavior, the field-level phase
relations, bright/dark interference, and power conservation. **These
results come from the independently constructed field-level reference
model written for this validation, not from any repository implementation**
— `code_and_simulation_audit.md` §5.4 confirms no beamsplitter or dark-port
code exists anywhere in the repository.

### 6.3 Implementation Consistency

T1, T3, T4, T5 confirm that the source-level computational chain — the
**bright-port scalar path only** (`differential_arm_length()`,
`phase_difference()`, `photodetector_intensity()`,
`intensity_from_arm_lengths()`) — reproduces the frozen analytical response.

### 6.4 Numerical Consistency

Observed discrepancies across both independently run environments (§12)
are consistent with double-precision floating-point roundoff and the
pre-explained T5 representation artifact (§3.3); none indicate a physics or
implementation defect.

---

## 7. Relationship to Repository Code and Simulations

This section connects the validation to the repository without repeating
the code audit.

**Source implementation:** `src/interferometer.py`.
**Relevant simulation:** `simulations/basic_interferometer.py`.
**Phase 1 time-dependent application:** `simulations/time_dependent_interferometer.py`,
which applies $\Delta L(t)\to\Delta\phi(t)\to I(t)$ within the ideal optical
model tested above.

The full code-to-simulation comparison, including the ten later-stage
simulations, is `code_and_simulation_audit.md`'s responsibility, not this
document's.

---

## 8. Phase-Boundary Checks

Tested relationships belong to Stage 1 (Phase 1) only:
$\Delta L\to\Delta\phi\to I$, at both the scalar and field level.

Explicitly not covered by this validation, consistent with
`code_and_simulation_audit.md` §8:

* **Stage 2:** $h\to\Delta L$.
* **Stage 3:** polarization/antenna response — no repository code exists.
* **Stage 4:** operating-point linear response.
* **Stage 5:** physical detector noise (toy and physical models).
* **Stage 6:** PSD/ASD/sensitivity.
* **Stage 7:** SNR/signal recovery.
* **Stage 8:** public-data validation — no repository code exists.
* **Stage 9:** integrated detector model — no repository code exists.

This prevents any later-stage repository functionality from being read as
part of the Phase 1 numerical validation.

---

## 9. Limitations of the Numerical Validation

These tests do not validate: realistic optical losses; beam imperfections
or mode mismatch; physical detector noise; GW strain coupling; polarization
or antenna response; operating-point control/readout; PSD/ASD or
sensitivity; matched filtering. They do not constitute experimental
validation against real interferometer data.

**Not tested because outside Phase 1 scope** (§8) is distinct from **not
tested despite being required for Phase 1** — for the defined Phase 1
scope, the required numerical checks (§2.1–§2.8) have all been covered.

---

## 10. Validation Findings

### 10.1 Agreement

* $\Delta L_\mathrm{arm}=L_x-L_y$, including sign (T1).
* The round-trip factor of 2 is correctly incorporated into the phase
  relation (T2, with its consistency-check qualification).
* $\Delta\phi=4\pi\Delta L_\mathrm{arm}/\lambda$ (T3).
* $I_\mathrm{bright}=\frac{I_0}{2}(1+\cos\Delta\phi)$, including
  constructive/destructive/intermediate conditions (T4).
* The complete bright-port scalar chain is internally consistent (T5).
* Periodicity ($\lambda/2$) and symmetry hold at floating-point precision
  (T6, T7).
* **The bright-port scalar response is directly exposed in
  `src/interferometer.py` and numerically validated (T1–T5, T8, T9).**

### 10.2 Scope Limitations

* The complementary dark-port response is analytically established
  (`analytical_model.md` §9) and numerically validated (T11, T13) against
  the independent field-level model, but is not separately exposed as
  repository code.
* The beamsplitter matrix and field-level recombination (T10, T11, T12)
  validate the analytical model, not any repository implementation — none
  exists (`code_and_simulation_audit.md` §5.4).
* Later-stage GW coupling, operating-point, noise, PSD/ASD, and SNR
  functionality is outside the basic interferometer module and outside this
  validation's scope (§8).

### 10.3 Genuine Discrepancies

None identified. No numerical evidence in T1–T13 conflicts with the frozen
Phase 1 analytical model.

---

## 11. Overall Validation Conclusion

T1–T13 passed in two independently executed environments (§12). The
implementation is numerically consistent with the established Phase 1
ideal Michelson model:

* The bright-port scalar chain in `src/interferometer.py` reproduces the
  frozen analytical predictions (T1–T5, T8, T9).
* The independently constructed field-level beamsplitter and recombination
  model reproduces the frozen bright/dark predictions and satisfies power
  conservation (T10–T13), supporting the analytical model itself rather
  than testing repository code, since no beamsplitter/dark-port code
  exists.
* No physics-driven source modification was required.

Phase 1 numerical validation is therefore closed. This evidence was already
used as the basis for `code_and_simulation_audit.md`, which asks a
different question — whether the repository implementation and simulations
correspond to, and appropriately use, this validated physics baseline. The
next document in the Phase 1 sequence is `limitations_and_conclusion.md`.

---

## 12. Reproducibility / Traceability

**Repository:** `gravitational-wave-detector-research-main`.
**Commit hash:** not yet available. Phase 1 documentation (this document,
`analytical_model.md`, `literature_validation.md`, and
`code_and_simulation_audit.md`) and the validation script below are to be
captured together in a single Phase 1 closing commit; this section will be
updated with that hash once it exists.
**Source file under test:** `src/interferometer.py`.
**Validation script:** `validation/phase1_numerical_validation.py`.
**Run command:** `PYTHONPATH=. python3 validation/phase1_numerical_validation.py`.
**Numerical parameters:** $\lambda=1064$ nm throughout; per-test parameters
given in Section 5.

This validation was executed independently in two environments, with
identical PASS/FAIL outcomes:

| | Environment 1 | Environment 2 |
|---|---|---|
| Python | 3.12.3 | 3.12.10 |
| NumPy | 2.4.4 | 2.5.3 |
| OS | Linux | Windows 11 |
| Result | T1–T13 ALL PASS | T1–T13 ALL PASS |

Agreement across two different patch versions, two different NumPy
versions, and two different operating systems is itself evidence that the
T1–T13 results are not an artifact of any single environment.
