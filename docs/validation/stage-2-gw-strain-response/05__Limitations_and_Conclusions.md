# Stage 2 Model Boundaries, Limitations and Master Conclusion — GW Strain → Differential Arm Response

**Status:** Complete, **with the items listed in Section 16 (ten open; one, OI-5, closed at the level of printed runner output)**. This is
**Document 5** of the Stage 2 process. It consolidates Step 6 (freeze the
baseline and separate corrections), Step 9 (boundary with general detector
response) and Step 11 (final Stage 2 validation record). It is a synthesis and
audit record: it introduces no new physics, runs no tests, and does not edit
Documents 1–4.

Where information is missing, unverified or contradictory across the project
records, this document says so at the point of use and collects every such item
in Section 16. Nothing missing has been filled in silently.

---

## 1. Purpose, Scope and Position

### 1.1 Purpose

This document answers four questions:

1. What exactly is the frozen Stage 2 baseline, and where does it stop being valid? (Part I)
2. What is separated from the baseline as a correction, and what is deferred to later stages? (Part I)
3. What limitations, across physics, implementation, numerics and evidence, apply to the Stage 2 result? (Part II)
4. What has Stage 2 established, what has it not, and can every claim be traced to its derivation, evidence or test? (Part III)

### 1.2 Position in the Stage 2 Document Set

| Document | Question it answers |
|---|---|
| 1 — Analytical Model (`analytical_model`) | What physics was derived, and from what assumptions? |
| 2 — Literature Validation & Consistency Audit | What external evidence supports it? |
| 3 — Code and Simulation Audit | What does the repository implement? |
| 4 — Numerical Validation & Verification Record (`S2_Numerical_Validation`) | Does the implementation reproduce the frozen analytical relations, before and after the Step 12 update? |
| **5 — this document** | What are the model boundaries and limitations, and what is the master conclusion? |

### 1.3 Step Numbering

This document uses the current 12-step plan. The older research records used
different labels. Where this document draws on them, they are named:
the closure record the notebook files under "Step 6" is labelled "Step 5
Closure Decision" inside its own text; the scope-control record for
general detector response, labelled "Step 7" in the older notebook, is
Step 9 here.

### 1.4 Terminology

"Stage" is the project term. The Stage 1 documents use "Phase 1" for the same
ideal-Michelson stage.

---

## 2. Source Records and Reconciliation Conventions

### 2.1 Records Used

Documents 1–3 as supplied; Document 4 as written in this project; the
completed Step 6 record; the completed Step 9 record; the Stage 2 step plan;
the Stage 1 `analytical_model`, `literature_validation` and `numerical_validation`
records; and the notebook's answer on stage boundaries (Section 7).

### 2.2 Precedence Rule

Where an older step record and a later document disagree, the later document is
treated as the controlling statement and the difference is listed in Appendix B.
Documents 1–4 are not edited here.

### 2.3 Identifier Collision

Document 3 numbers its findings F1–F9. Document 4 numbers its findings
F-01 to F-06 (F-01 to F-04 come from the gap register). The two sets are
different findings. This document prefixes every reference: **D3-F1 … D3-F9**
and **D4-F-01 … D4-F-06**.

### 2.4 Evidence Levels

Document 4 classifies evidence as L1 (independent analytical check),
L2 (implementation/formula self-consistency), L3 (numerical-resolution
validation) and L4 (auxiliary diagnostic). Those levels are used here.

---

# Part I — Model Boundaries (Steps 6 and 9)

## 3. The Frozen Baseline Model (Step 6)

$$
\boxed{\Delta L_\mathrm{arm}(t)=h(t)\,L_0}
$$

where $\Delta L_\mathrm{arm}\equiv L_x-L_y=\delta L_x-\delta L_y$ is the
differential proper arm-length perturbation, $L_0$ is the nominal unperturbed
arm length ($L_{x,0}=L_{y,0}=L_0$), and $h(t)\equiv h_+(t)\equiv h_\mathrm{det}(t)$
is the working scalar strain of the aligned baseline (Document 1 §4.6).

**Individual arms:** $\delta L_x=+\tfrac12hL_0$, $\delta L_y=-\tfrac12hL_0$
(Document 1 §7).
**Interface to Stage 1:** $\Delta\phi(t)=(4\pi L_0/\lambda_0)\,h(t)$
(Document 1 §10.3), with the frozen Stage 1 relations beyond it.
**Frozen register:** Document 1 §13.2 (F1–F5).

**Derived configuration:** plane wave from overhead ($\theta=0$), propagating
along $+z$; pure plus polarization ($h_\times=0$) aligned with the arms
($\phi=\psi=0$); orthogonal ($90^\circ$) arms of equal nominal length.

**Strength of the statement.** The baseline is **valid to first order in $h$,
under the stated conditions**. This is Document 2's closure wording
(§9.3). The earlier Step 5/6 records describe the result as "exact" and as
established "without unresolved analytical gaps"; those phrases are not carried
forward (Appendix B).

## 4. Validity Domain

### 4.1 Conditions

The baseline holds when all of the following hold together (Document 2 §6.1,
Document 1 §14):

1. Weak field, $|h|\ll1$.
2. Long-wavelength regime, $f_\mathrm{gw}\ll f^*\equiv c/(2\pi L_0)$.
3. Overhead incidence with aligned plus polarization.
4. Orthogonal arms of equal nominal length.
5. TT gauge as the frame of derivation.
6. Subtraction order $\Delta L\equiv L_x-L_y$ (a convention; the reversed order gives $-hL_0$).

**Physical condition versus project criterion.** $f_\mathrm{gw}\ll f^*$ is the
physical long-wavelength condition. $f_\mathrm{gw}\le0.1f^*$ is a
**project-adopted operational criterion**, not a physical law. The two are not
mixed in this document. The earlier "if and only if" wording combined them and
is superseded (Appendix B).

**Wavelength form.** Because $f^*=c/(2\pi L_0)$, the condition $f\ll f^*$ is
equivalent to the *reduced* wavelength $\lambda_\mathrm{gw}/2\pi\gg L_0$.
Writing it as $\lambda_\mathrm{gw}\gg L_0$ with the full wavelength differs by a
factor $2\pi$; the operational limit $f\le0.1f^*$ corresponds to
$\lambda_\mathrm{gw}\approx63\,L_0$. Some earlier records use the two forms
interchangeably.

### 4.2 Characteristic Frequencies

| Detector | $L_0$ | $f^*=c/2\pi L_0$ | $0.1f^*$ | $f_\mathrm{FSR}=c/2L_0=\pi f^*$ |
|---|---|---|---|---|
| Advanced LIGO | 4 km | 11.93 kHz | 1.19 kHz | 37.5 kHz |
| Einstein Telescope | 10 km | 4.77 kHz | 477 Hz | 15.0 kHz |
| Einstein Telescope (2L option) | 15 km | 3.18 kHz | 318 Hz | 10.0 kHz |
| Repository toy model | 1 m | 47.71 MHz | 4.77 MHz | 150 MHz |
| LISA | $2.5\times10^{6}$ km | 19.1 mHz | 1.9 mHz | 60 mHz |

Values for 4 km, 10 km and 1 m are from Document 2 §6.3. The 15 km and LISA rows
are from the Step 6 record and were recomputed here from $f^*=c/(2\pi L_0)$; the
Advanced LIGO band (10 Hz–1 kHz) lies below $0.1f^*$ for 4 km arms. Document 1
§9.1 states the 4 km operational limit as 1.2 kHz; the correct rounding of
$0.1\times11.93$ kHz is **1.19 kHz** (Document 2 §6.3); see OI-7.

### 4.3 Baseline Assumption Inventory

The canonical inventory is Document 2 §5.1 (eleven assumptions or conventions
plus two boundary definitions). Document 1 §14 lists eight assumptions A1–A8
for the derivation; they are a subset organised by role. The Step 6 record
quotes "29 uploaded literature sources"; see OI-9.

## 5. Corrections Kept Separate from the Baseline

**Scope rule (Step 6).** Corrections must remain distinguishable from the
baseline. The baseline equation is not replaced by a correction model unless
the evidence establishes that the baseline lies outside its stated validity
regime. Nothing in Documents 1–4 invokes a correction to replace the baseline.

| Correction | Form | Applies when | Status in Stage 2 |
|---|---|---|---|
| Finite-arm transit response | $C(f)=\mathrm{sinc}(\omega L_0/c)\,e^{-i\omega L_0/c}$, so $\Delta L_\mathrm{arm}(f)=C(f)\,h(f)L_0$ | $f\gtrsim0.1f^*$ (Document 1 §15) | Named, not developed. $C\to1$ as $f\to0$, restoring the baseline |
| Arm-cavity storage | single-pole response, $K_-(f)\approx1/(1+if/f_p)$ | Resonant arm cavities | Excluded. Document 2 §6.2 gives $f_p\approx f^*T_\mathrm{ITM}/4$ |
| Power/signal recycling, detuning, Schnupp asymmetry | transfer functions | Recycled configurations | Excluded |
| Readout and photodetector response | DC offset, homodyne beating, output mode cleaner, photodiode electronics | Realistic readout | Excluded; bright port used |
| Non-orthogonal arms | factor $\sin\zeta$ ($\sqrt3/2$ at $60^\circ$) | $\zeta\neq90^\circ$ | Named, not derived |
| Space-based TDI | delay-line transfer functions | LISA-type detectors | Outside Stage 2 |
| Nonlinear metric terms | $\Delta L_\mathrm{arm}=L_0(h+h^3/8+\dots)$ | Strong field | Relative correction $h^2/8\sim10^{-43}$ at $|h|\sim10^{-21}$ (Document 1 §12) |
| Explicit light-travel-time calculation | full round-trip photon-time derivation | Beyond quasi-static | Not performed (Document 1 §15) |

**Size of the finite-arm correction.** The amplitude departure of $C(f)$ from 1
is about $x^2/6$ and the phase departure about $x$, with $x=\omega L_0/c=f/f^*$.

| Case | $x=f/f^*$ | Amplitude departure $\approx x^2/6$ | Phase departure $\approx x$ |
|---|---|---|---|
| Repository toy model (1 m, 100 Hz) | $2.1\times10^{-6}$ | $7.3\times10^{-13}$ | $2.1\times10^{-6}$ rad |
| Advanced LIGO at its operational limit (0.1 $f^*$) | 0.1 | $1.7\times10^{-3}$ | 0.1 rad |

The second row is computed here from the stated expansion; it is an
order-of-magnitude statement, not a detector model.

**Numerical tolerances versus this physical error.** The $7.3\times10^{-13}$
departure is a *physical* truncation of the baseline model. The numerical
tolerance $10^{-14}$ used in Document 4 is an *arithmetic* acceptance
criterion. They are different quantities and are not compared with each other:
every Document 4 test compares the implementation with the baseline, not with a
finite-arm model.

**Cavity-pole values.** The Step 6 record quotes $f_p\approx350$–$450$ Hz and
$f_p\approx42$ Hz. Document 2 (§7.6) replaced $f^*T/2$ by $f^*T/4$ and removed
the 80–350 Hz range; the origin of the quoted values and of
$T_\mathrm{ITM}=0.014$ is Traceability Pending (OI-10). They are not carried
forward as validated numbers.

## 6. Boundary with General Detector Response (Step 9)

### 6.1 Reduction to the Baseline

The general detector-projected strain is
$h_\mathrm{det}=F_+(\theta,\phi,\psi)h_++F_\times(\theta,\phi,\psi)h_\times
=d^{ij}h^\mathrm{TT}_{ij}$ with $d^{ij}=\tfrac12(\hat e_x^i\hat e_x^j-\hat e_y^i\hat e_y^j)$.
At the aligned baseline ($\theta=\phi=\psi=0$, $h_\times=0$) it gives
$F_+=1$, $F_\times=0$ and $h_\mathrm{det}=h_+\equiv h(t)$. This is the
exact reduction used to define the working scalar strain. The general
antenna-pattern expressions are not reproduced here; the Step 9 record writes
them without the factor of 2 in the $\phi$ and $\psi$ arguments, which does not
affect the baseline values but should not be copied as the general form
(Appendix B).

### 6.2 Inherited, Simplified, Deferred

| Element | Status in Stage 2 | Reason |
|---|---|---|
| Working scalar strain $h(t)$ | **Inherited** (primary input) | Entry point of the proper-distance integration |
| Plus polarization $h_+$ | **Inherited**, identified with $h(t)$ | Sole active mode at the aligned baseline |
| Cross polarization $h_\times$ | **Simplified** (set to 0) | Non-zero only for misaligned or general waves |
| Sky position $(\theta,\phi)$ | **Simplified** (overhead, $\theta=0$) | Off-axis incidence introduces $F_+<1$ |
| Polarization angle $\psi$ | **Simplified** ($\psi=0$) | Rotation mixes $h_+$ and $h_\times$ |
| Antenna patterns $F_+,F_\times$ | **Simplified** (collapsed to 1 and 0) | General functions deferred |
| 3D detector tensor contraction | **Simplified** (scalar reduction implicit) | Needed for arbitrary geometry |
| Non-orthogonal geometry | **Deferred** | $\sin\zeta$ factor; at $60^\circ$ the unscaled baseline overestimates the response by $1/\sin60^\circ-1\approx15.5\%$ |
| General polarization projection | **Deferred** | $F_+h_++F_\times h_\times$ |
| Network statistics, Fisher-matrix estimation | **Deferred** | Post-projection data analysis |

The implementation makes the same simplifications by construction: the
repository takes a pre-projected scalar strain and contains no sky coordinates,
polarization angle, cross polarization or detector tensor (Document 3 §6.6,
D3-F3).

## 7. Later-Stage Assignment of Excluded Items

### 7.1 What Each Source Says

The project records do not agree on where every excluded item lands, and the
Master Plan itself was not supplied for this document.

| Item | Step 9 record | Documents 2 and 3; Step 6 record | Notebook stage-boundary answer | Stage 1 `numerical_validation` §8 |
|---|---|---|---|---|
| Antenna patterns, sky position, $\psi$, $h_\times$, general polarization projection | Stage 3 | not assigned | not mentioned in its Stage 3 description (optical response) | Stage 3: polarization/antenna response |
| Non-orthogonal arm geometry | Stage 3 | Stage 3 (configuration extension) | Stage 3 | not assigned |
| Finite-arm $C(f)$, arm-cavity dynamics, recycling, Schnupp asymmetry | not addressed | Stage 3 | Stage 3 | not assigned |
| DC readout, homodyne, output mode cleaner, photodiode | not addressed | Stage 4 | Stage 4 | Stage 4: operating-point linear response (compatible in part) |
| Detector-network statistics, Fisher-matrix estimation | **Stage 3** | **Stage 4** | **Stage 4** | Stage 7: SNR and signal recovery (this item not named) |
| Physical noise, PSD/ASD, sensitivity, SNR, public data, integrated model | not addressed | not addressed | Stages 5–9 "not defined in the available record" | Stages 5–9 named: noise; PSD/ASD/sensitivity; SNR/signal recovery; public data; integrated model |

### 7.2 Reading of the Conflict

- **Network statistics:** Stage 3 (Step 9) against Stage 4 (Documents 2 and 3,
  Step 6, notebook) against a later stage if the Stage 1 list is the Master
  Plan. This is a genuine conflict.
- **Stage 3 content:** the Stage 2 packages describe Stage 3 as optical and
  cavity response and configuration extensions. The Step 9 record and the
  Stage 2 plan (Steps 0 and 9) describe Stage 3 as general polarization and
  antenna-pattern projection. The records are not shown to be in conflict
  (Stage 3 could contain both), but they have never been reconciled against the
  Master Plan.
- **Stages 5–9:** the notebook answer says they are undefined in its record,
  while the Stage 1 numerical-validation record lists them. These are not
  contradictory; they are different records.

### 7.3 Treatment in This Document

Stage numbers for the deferred items are therefore reported as stated in each
source (§7.1) and are **not** adopted as a single frozen assignment. What Stage
2 does establish is the **exclusion**: every item in §§5–6 is outside the
frozen baseline, whichever later stage receives it. See OI-1.

---

# Part II — Limitations

## 8. Consolidated Limitations Register

Each limitation appears once. Classes: **P** physical/model scope, **I**
implementation, **N** numerical, **E** evidence/traceability.

| ID | Limitation | Class | Source | Status |
|---|---|---|---|---|
| L-01 | Result is first order in $h$; nonlinear terms not treated beyond the $h^2/8$ magnitude note | P | Doc 1 §12, §15 | Accepted limitation |
| L-02 | Finite-arm response $C(f)$ omitted; baseline valid for $f\ll f^*$ (operationally $\le0.1f^*$) | P | Doc 1 §15; Doc 2 claims 9–10 | Accepted; correction named in §5 |
| L-03 | Aligned-geometry special case: overhead incidence, plus polarization, $\phi=\psi=0$ | P | Doc 1 A3–A4; Doc 2 claim 4 | Accepted; general response deferred (§6) |
| L-04 | Orthogonal arms of equal nominal length; static asymmetry offsets excluded | P | Doc 1 A5–A6 | Accepted |
| L-05 | TT-gauge derivation only; no step-by-step transformation to Fermi-normal coordinates in the sources | P/E | Step 6 record §6 | Open (OI-8) |
| L-06 | No arm cavities, recycling or readout physics | P | Doc 1 §15; Doc 3 §7 | Accepted; deferred |
| L-07 | Bright port only. GW detectors read out at the dark port; the repository has no dark-port function | P/I | Stage 1 Claim 6; D3-F5, D3-F8 | Accepted scope observation |
| L-08 | Time dependence rests on a quasi-static argument, not a general time-dependent optical derivation | P | Doc 1 §9.2 | Accepted |
| L-09 | No explicit light-travel-time calculation | P | Doc 1 §15 | Accepted |
| L-10 | Implementation takes a pre-projected scalar strain; no antenna patterns, sky position, or polarization components | I | D3-F3; gap register Disc. 2 | Accepted; deferred (§6) |
| L-11 | The code does not document or guard its assumptions (long-wavelength regime, equal arms, orthogonality, sign convention) | I | D3-F2 | **Open** (OI-11); not changed by Step 12 |
| L-12 | Input validation partial: `arm_length` and `strain_amplitude` unchecked | I | D3-F9 | Open, minor |
| L-13 | Toy parameters ($L_0=1$ m) are not detector-scale; peak $\Delta\phi\approx1.18\times10^{-14}$ rad against $\approx4.7\times10^{-11}$ rad at 4 km for $h=10^{-21}$ | I | D3-F6; Doc 1 §10.6 | Accepted scope observation |
| L-14 | Helper `differential_arm_length()` is not used by the Stage 2 runner | I | Gap register Disc. 3 | Accepted; no numerical effect |
| L-15 | Individual arm perturbations $\delta L_x,\delta L_y$ were not exposed | I | D4-F-01 | **Resolved** by Step 12; S2-T1 and S2-T2 now PASS (Doc 4 §14) |
| L-16 | At $h=10^{-21}$ the bright-port modulation ($3.5\times10^{-29}$ at 1 m; $\approx5.6\times10^{-22}$ at 4 km) is below float64 spacing near unity; at equal arms the response is quadratic in $\Delta\phi$ | N | D4-F-04; D3-F5 | Accepted; S2-T9 carries the limitation; S2-T9S confirms the chain at a resolvable strain |
| L-17 | A $10^{-21}$ m difference cannot be recovered from two $\approx1$ m float64 values | N | D4-F-02 | Accepted; auxiliary T6 construction rejected; Step 12 design rule |
| L-18 | Endpoint-inclusive time grid: spacing $0.1/9999$ s, effective rate 99 990 Hz | N | D3-F4; D4-F-03 | Accepted; pointwise comparison is primary |
| L-19 | Tests S2-T1 to S2-T8 are self-consistency checks (Level 2), not independent confirmation of the physics | N | Doc 4 §9 | Accepted |
| L-20 | Tolerances are methodological numerical criteria, checked in two environments only | N | Doc 4 §6, §18 | Accepted |
| L-21 | The three-line runner edit made in Step 12 is not exercised by the validation script | N/I | D4-F-06 | **Closed at printed-output level** by the before/after runner comparison (Doc 4 §14.3); residual: four-digit precision, plots not compared, environment not recorded (OI-5) |
| L-22 | Textbook-level references have no locators (MTW, Maggiore, Schutz, Saulson, others) | E | Doc 2 §10.2 | **Open** (OI-6) |
| L-23 | No formal source-selection document | E | Doc 2 §10.3 | Accepted |
| L-24 | Repository commit hash and per-line locators not yet entered | E | Doc 3 §13; Doc 4 §18 | **Open** (OI-3) |

## 9. Document 3 Expectations Against Document 4 Outcomes

Document 3 was a static audit and recorded expectations for the numerical stage
(Document 3 §10.2). Document 4 can be compared with them.

| Document 3 expectation | Document 4 outcome |
|---|---|
| Computed intensity exactly 1.0; intensity change exactly 0 (D3-F5) | Confirmed: implementation $I_0-\min I=0$ against an expected $3.487\times10^{-29}$ |
| FFT bin nearest 100 Hz centred near 99.99 Hz | Confirmed: 99.990 Hz |
| A $10^{-14}$ relative tolerance on a sampled peak "expected not to hold" | **Not borne out in Document 4.** Document 4 compares the implementation with a reference at the same samples, so the sampled-peak shortfall does not enter; the expectation concerned a differently constructed test |
| Nearest sample to the 0.005 s zero crossing has $|\Delta L|\approx3\times10^{-25}$ m | Not tested: no Document 4 test evaluates that sample |
| h → ΔL could not be called on its own (D3-F1) | Resolved by Step 12 for the physics module; the runner still contains the statements inline |

## 10. What the Evidence Levels Establish

Document 4 §9 assigns each test to a level. In summary:

- **No test in Document 4 independently validates the physical relation
  $h\to\Delta L$.** That evidence is Documents 1 and 2. Document 4 shows that the
  implementation reproduces the frozen expressions.
- The only checks with independent mathematical content are the
  $\Delta I$-versus-$I_0\sin^2(\Delta\phi/2)$ comparison in S2-T9S and the
  parameter-admissibility check S2-T10.
- Exact zero errors are expected by construction for S2-T1 to S2-T8; they are
  not evidence of unlimited numerical precision.

---

# Part III — Master Conclusion (Step 11)

## 11. Traceability Matrix

Each row traces one Step 11 item to its derivation, literature support, code
audit and numerical evidence. "—" means that layer is not applicable.

| # | Item | Derivation | Literature (Doc 2) | Code audit (Doc 3) | Numerical (Doc 4) |
|---|---|---|---|---|---|
| 1 | Stage 2 objective | Doc 1 §1.1 | — | Doc 3 §1.1 | Doc 4 §1.1 |
| 2 | Scope and interface | Doc 1 §1.2–§1.4 | §1.3, §8 | Doc 3 §1 | Doc 4 §1.3 |
| 3 | Definition of $h(t)$ | Doc 1 §4.1–§4.6 | Claims 1–5 | §6.6 | §3 |
| 4 | Analytical derivation | Doc 1 §5–§8 | Claims 6–7 | §6.1 | S2-T3 |
| 5 | Individual arm responses | Doc 1 §6.3, §7 | Claim 6 | §6.2 (bypassed, EQUIVALENT) | S2-T1, S2-T2 (BLOCKED → PASS) |
| 6 | Differential response | Doc 1 §8 | Claims 7–8 | §6.1, §6.3 | S2-T3, S2-T6 |
| 7 | Literature verification | — | §4, §9 | — | — |
| 8 | Assumptions | Doc 1 §14 | §5.1–§5.2 | §6.5–§6.6 | — |
| 9 | Validity regime | Doc 1 §9 | §6; Claim 9 | §6.7 | S2-T10 |
| 10 | Baseline model | Doc 1 §13 (F1–F5) | §9.3 | §2 | Part II |
| 11 | Corrections and exclusions | Doc 1 §15 | §8 | §7 | Doc 4 §1.3 |
| 12 | Implementation audit | — | — | §4–§9, §12 | — |
| 13 | Stage 2 → Stage 1 interface | Doc 1 §10 | Claim 12 | §6.8 | S2-T9, S2-T9S |
| 14 | Numerical validation | — | — | — | Doc 4 §8, §14 |
| 15 | Implementation gaps | — | — | §9 (D3-F1–F9) | Doc 4 §4.3, §10, §12 (D4-F-01–F-06) |
| 16 | Numerical limitations | — | — | — | Doc 4 §10, §17 |
| 17 | Reproducibility | — | — | §13 (hash and locators pending) | Doc 4 §18 (hash pending) |
| 18 | Final validated scope | §13 below | | | |
| 19 | Remaining unresolved items | §16 below | | | |

**Literature status of the core claims (Doc 2 §9.1):** claims 1, 2, 3 and 9
VERIFIED; claims 4, 5, 6, 7, 10, 11 and 12 VERIFIED WITH EXPLICIT ASSUMPTIONS;
claim 8 (subtraction order) CONVENTION/DEFINITION DEPENDENT.

## 12. Evidence Chain Summary

$$
\text{derivation (Doc 1)}\rightarrow\text{literature (Doc 2)}\rightarrow\text{code audit (Doc 3)}\rightarrow\text{numerical validation (Doc 4)}\rightarrow\text{boundaries and limitations (this document)}
$$

The code audit found no genuine discrepancy between the repository and the
baseline (Doc 3 §12). The numerical record found no failures before or after
the Step 12 update (Doc 4 §11, §16).

## 13. Validated Scope — What Stage 2 Has Established

Under the stated assumptions, the following are established:

1. The relation $\Delta L_\mathrm{arm}(t)=L_x-L_y=h(t)L_0$ is derived from the weak-field TT-gauge metric (Document 1) and is literature-supported, valid to first order in $h$ (Document 2).
2. The individual-arm responses $\delta L_x=+\tfrac12hL_0$ and $\delta L_y=-\tfrac12hL_0$ and their antisymmetry, with no factor of 2 missing or double counted (Documents 1 and 2).
3. The Stage 2 → Stage 1 interface $\Delta\phi=(4\pi L_0/\lambda_0)h$ (Documents 1 and 2); static gain $\approx4.724\times10^{10}$ rad per unit strain at 4 km and 1064 nm (Document 1 §10.6).
4. The repository implements the baseline relation with net normalization 1, positive sign, consistent units and a static long-wavelength form inside the baseline's regime for its parameters ($f/f^*\approx2.1\times10^{-6}$) (Document 3).
5. The implementation reproduces the frozen relations numerically within the stated tolerances: S2-T3 to S2-T10 PASS before and after the update; S2-T1 and S2-T2 BLOCKED before and PASS after; S2-T9 carries a float64-resolution limitation; S2-T9S confirms the optical chain at a resolvable strain (Document 4).
6. The baseline is separated from every named correction and from general detector response (Sections 5 and 6).

## 14. What Stage 2 Has Not Established

1. **Independent numerical confirmation of the physics.** Document 4's tests are Level 2 (self-consistency); the independent evidence is Documents 1 and 2.
2. **Direct float64 resolution of the $h=10^{-21}$ intensity modulation.** S2-T9S does not provide it.
3. **Bit-level or plot-level equality of the edited runner's outputs.** Document 4 §14.3 shows identical printed output before and after the edit, to four significant digits (OI-5).
4. **Any finite-arm, cavity, recycling, readout, antenna-pattern or network effect.** These are excluded from the baseline (§§5–6).
5. **Agreement with real detector data.** Stage 2 is an analytical, literature and implementation record, not empirical validation.
6. **A single reconciled later-stage assignment of the excluded items** (OI-1).

## 15. Stage 2 Completion Criteria

The plan lists thirteen criteria. Status here is assessed against the evidence
in Documents 1–4 and this document.

| # | Criterion | Evidence | Status |
|---|---|---|---|
| 1 | Strain input physically defined | Doc 1 §4; Doc 2 claims 1–5 | Met |
| 2 | Strain-to-arm relationship analytically derived | Doc 1 §5–§8 | Met |
| 3 | Individual and differential responses established | Doc 1 §7–§8; Doc 4 S2-T1 to S2-T3 | Met |
| 4 | Model literature-verified | Doc 2 §9 | Met (textbook locators pending, OI-6) |
| 5 | Assumptions and validity conditions explicit | Doc 1 §9, §14; Doc 2 §5–§6; §4 here | Met |
| 6 | Baseline and corrections separated | §3, §5 here; Doc 1 §13, §15 | Met |
| 7 | Implementation audited against the validated model | Doc 3 | Met (Doc 3 predates Steps 10 and 12, OI-4) |
| 8 | Stage 2 → Stage 1 interface established | Doc 1 §10; Doc 2 claim 12; Doc 4 S2-T9, S2-T9S | Met |
| 9 | Boundaries with general detector response explicit | §6 here | Met in substance; later-stage assignment unresolved (OI-1) |
| 10 | Executable numerical tests performed with documented tolerances | Doc 4 | Met |
| 11 | Implementation gaps and numerical limitations recorded | §8 here; Doc 3 §9; Doc 4 §10 | Met |
| 12 | Final record reproducible and traceable | §11 here; Doc 4 §18 | Met in structure; commit hashes and locators pending (OI-3) |
| 13 | Subsequent implementation changes separately revalidated | Doc 4 Part III | Met; the runner's printed output was compared before and after the edit (Doc 4 §14.3), at printed precision (OI-5) |

## 16. Open Items

These are the points the available records leave missing, unverified or
contradictory. OI-5 is shown for completeness and is closed at the level of
printed runner output.

| ID | Open item | Detail | Needed to close |
|---|---|---|---|
| OI-1 | Later-stage assignment of excluded items | Sources disagree on network statistics (Stage 3 or 4), and on whether Stage 3 contains antenna response, optical response, or both (§7). The Master Plan stage table was not supplied | The Master Plan's Stage 3–9 table, and where finite-arm, cavity, geometry, readout and network items belong |
| OI-2 | "Step 5D" | The older Step 5C record offered a unified response model combining the sinc factor, cavity pole and recycling. **No record of its execution was provided** and nothing in Documents 1–4 depends on it. This document treats it as not executed, which is unconfirmed | Confirmation from the research notebook |
| OI-3 | Commit hash and locators | Document 3 §13 and Document 4 §18 both leave the commit hash to be entered; Document 3 per-line locators are pending | One closing commit and its hash |
| OI-4 | Document 3 status | The supplied file is labelled "Draft for repository commit". It predates Steps 10 and 12; its D3-F1 and §10.2 are superseded by Document 4 | A final version, or an explicit note in Document 3 |
| OI-5 | Runner edit (closed at printed-output level) | The runner was run before and after the Step 12 edit and the printed output was identical (Doc 4 §14.3). Residual: four significant digits only, plots not compared, environment of the two runs not recorded, post-update run used a separate patched copy | Optional: compare saved arrays or plots, and record the environment |
| OI-6 | References without locators | MTW, Maggiore, Schutz, Saulson, the Advanced LIGO review (except Eq. (A9)), the Advanced LIGO sensitivity paper, the Einstein Telescope design study and others (Doc 2 §10.2) | Section, page or equation locators |
| OI-7 | Rounding mismatch | Document 1 §9.1 gives the 4 km operational limit as 1.2 kHz; the correct value is 1.19 kHz (Doc 2 §6.3) | Correct Document 1 |
| OI-8 | Frame-invariance proof | Sources note TT-gauge and Fermi-normal derivations agree but give no step-by-step transformation (Step 6 record §6) | A source with the transformation, or acceptance as a stated gap |
| OI-9 | Source count | Step 5/6 records cite "29 uploaded literature sources"; Document 2's reference list has 14 entries, 7 with locators | The final source inventory |
| OI-10 | Cavity-pole numbers | The origin of the 350–450 Hz and 42 Hz values and of $T_\mathrm{ITM}=0.014$ is Traceability Pending (Doc 2 §10.2) | A locator |
| OI-11 | Assumptions not documented or guarded in code | D3-F2: nothing in the code states or checks the long-wavelength regime, equal arms, orthogonality, sign convention. Step 12 did not change this | A project decision on code comments or guards |

## 17. Overall Conclusion and Handoff

**Conclusion.** The Stage 2 relation $\Delta L_\mathrm{arm}(t)=h(t)L_0$, with
$\delta L_x=+\tfrac12hL_0$ and $\delta L_y=-\tfrac12hL_0$, is derived,
literature-supported and implemented in the repository, valid **to first order
in $h$ under the stated conditions**: weak field, long-wavelength regime
($f\ll f^*$; operationally $f\le0.1f^*$), overhead incidence with aligned plus
polarization, and orthogonal arms of equal nominal length. The implementation
reproduces the frozen relations in the numerical record, before and after the
controlled Step 12 update, with no failures. All of this holds for an
idealised, static, linearised, aligned-geometry model. It is not empirical
validation, and it does not model a real detector.

Stage 2 is complete **with the open items of Section 16**. None of them
changes the baseline result. OI-1 affects how the later-stage boundary is
documented; OI-3, OI-4 and OI-6 affect traceability. OI-5 was closed at the
level of printed runner output.

**Handoff.** The frozen outputs available to later work are:
$\Delta L_\mathrm{arm}(t)=h(t)L_0$ under the Section 4 conditions;
$\Delta\phi(t)=(4\pi L_0/\lambda_0)h(t)$; the correction forms of Section 5
(named, not developed); and the simplifications of Section 6 that the general
response must lift. Which later stage receives each excluded item is
unresolved (OI-1).

---

## Appendix A — Constants and Derived Scales

| Quantity | Value |
|---|---|
| $f^*$, 1 m / 4 km / 10 km / 15 km | 47.71 MHz / 11.93 kHz / 4.77 kHz / 3.18 kHz |
| $f_\mathrm{FSR}=\pi f^*$, 4 km | 37.5 kHz |
| $f/f^*$ at 100 Hz, 1 m | $2.1\times10^{-6}$ |
| $1-\mathrm{sinc}(x)\approx x^2/6$ at $x=2.1\times10^{-6}$ | $7.3\times10^{-13}$ |
| Static gain, 4 km, 1064 nm | $4.724\times10^{10}$ rad per unit strain |
| $\Delta\phi$ at $h=10^{-21}$: 4 km / 1 m | $4.72\times10^{-11}$ rad / $1.18105\times10^{-14}$ rad |
| Bright-port modulation $\Delta\phi^2/4$ at $h=10^{-21}$: 4 km / 1 m | $5.6\times10^{-22}$ / $3.49\times10^{-29}$ |
| Float64 spacing near 1 | $2.22\times10^{-16}$ |
| $1/\sin60^\circ-1$ | 15.47 % |

## Appendix B — Superseded and Corrected Statements

| Earlier statement | Where | Treatment here |
|---|---|---|
| "$f^*\approx37.5$ kHz for 4 km arms" | Step 6 record (validity table) | Incorrect: 37.5 kHz is the free spectral range. $f^*=11.93$ kHz |
| $1-\mathrm{sinc}\approx2.2\times10^{-12}$ and "exact to 1 part in $10^{11}$" | Earlier code-audit validation record | Arithmetic slip ($x^2/2$ used for $x^2/6$). Correct value $7.3\times10^{-13}$ (Doc 2 §6.3; Doc 3 §6.7) |
| Baseline "exact", "100% verified", "without unresolved analytical gaps"; "if and only if" mixing the physical and operational criteria | Step 5/6 records | Replaced by "valid to first order in $h$ under the stated conditions" (Doc 2 §7.6) |
| $\lambda_\mathrm{gw}\gg L_0$ and $f\ll f^*$ called equivalent | Step 5/6 records | They differ by $2\pi$ (§4.1) |
| "Stage 2 is now completely closed" after the validity step | Step 5 record | Stage 2 closure is decided by the thirteen criteria (§15) |
| Next stage as "integrate into the optical readout model" | Step 5 record | That integration is Step 8, already done |
| "Unresolved issues: none"; "physically justified: Yes" | Earlier code-audit validation record | The individual-arm gap (D4-F-01) was found later and resolved by Step 12 |
| Cavity pole $f^*T/2$; range 80–350 Hz | Earlier packages | $f^*T/4$; range removed (Doc 2 §7.6) |
| General $F_+,F_\times$ written without the factor 2 in the $\phi$, $\psi$ arguments | Step 9 record | Not reproduced; baseline values $F_+=1$, $F_\times=0$ unaffected |
| "Eight explicit assumptions" (nine listed) | Step 9 record | Doc 2 §5.1 inventory is canonical |
| "Fully supported … mathematically rigorous" | Step 9 record | Replaced by the Doc 2 status vocabulary |
| Network statistics assigned to Stage 3 | Step 9 record | Conflicts with the other sources; see §7 and OI-1 |
| Proper-distance diagnostic "differs only at $O(h^2)$, about $10^{-21}$" | First version of Document 4 | Corrected in Document 4: $h/4\approx2.5\times10^{-22}$ for the individual arms; $h^2/8\sim10^{-43}$ for the differential |

## Appendix C — Document Map and Provenance

| Item | Location |
|---|---|
| Analytical model | Document 1 |
| Literature validation | Document 2 |
| Code and simulation audit | Document 3 |
| Numerical validation and verification | `S2_Numerical_Validation.md`; script `validation/stage2_numerical_validation.py` |
| This record | `S2_Limitations_and_Conclusions.md` |

This record draws on Documents 1–4, the Step 6 and Step 9 records, the Stage 2
plan, the Stage 1 records, and the notebook's stage-boundary answer, as listed
in §2.1. Where those sources conflict or are silent, the conflict or gap is
stated in the text and in Section 16.

---

*End of document. With Documents 1–4 it forms the Stage 2 record.*
