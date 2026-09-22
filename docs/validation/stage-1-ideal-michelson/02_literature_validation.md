# Literature Validation — Ideal Michelson Interferometer (Phase 1)

**Status:** Complete. This document is the literature-validation evidence
record for the Phase 1 analytical model (`analytical_model.md`). It is an
audit trail, not a second derivation and not a general literature review.

---

## 1. Purpose and Validation Scope

### 1.1 Purpose of the Literature Validation

This document establishes whether the independently derived Phase 1 optical
model of the ideal two-arm Michelson interferometer is supported by
authoritative gravitational-wave and interferometry literature. It does not
re-derive the physics — that is the role of `analytical_model.md` — and it
does not attempt a general survey of interferometry literature. Its sole
purpose is to check the project's own formulations against external sources,
claim by claim, and to record what was found.

This is an evidence/audit record. Content decisions throughout are grounded
exclusively in the uploaded source material (33 primary and supporting
documents plus two subsequently identified sources; see Section 9).

### 1.2 Relationship to the Phase 1 Analytical Model

The formulation under test is the completed Phase 1 analytical chain:

$$
L_x, L_y \rightarrow \Delta L_\mathrm{arm} \rightarrow \Delta L_\mathrm{rt}
\rightarrow \Delta\phi \rightarrow \text{field recombination} \rightarrow
I_\mathrm{bright}, I_\mathrm{dark}.
$$

This chain was derived independently of the repository's existing code
(`analytical_model.md` §20). The present document checks that chain against
literature; it does not check the repository's implementation, which is a
separate, later audit step.

The Phase 1 scope is the ideal two-arm Michelson interferometer only.
Fabry–Pérot cavities, power/signal recycling, realistic operating-point
control, physical noise, PSD/ASD, sensitivity, and general antenna response
are explicitly outside this document's scope (see Section 6 for the full
boundary treatment).

### 1.3 Validation Questions

For each of the ten physics claims examined, this document answers:

1. Is the project's independent formulation supported by the literature?
2. Where two or more sources appear to disagree, is the disagreement a
   genuine physical contradiction, or a difference of notation, sign
   convention, or definition?
3. What explicit assumptions does the claim require to hold?
4. Does the claim belong to the core Phase 1 optical model, or to the
   Phase 1/Phase 2 boundary (i.e., the gravitational-wave coupling)?

---

## 2. Physics Claims Under Literature Validation

This is an index only; full evidence is in Section 4.

| # | Claim | Scope |
|---|---|---|
| 2.1 | Physical Differential Arm Length ($\Delta L_\mathrm{arm} = L_x - L_y$) | Core Phase 1 |
| 2.2 | Round-Trip Optical Path Difference ($\Delta L_\mathrm{rt} = 2\Delta L_\mathrm{arm}$) | Core Phase 1 |
| 2.3 | Differential Optical Phase ($\Delta\phi = \tfrac{4\pi}{\lambda}\Delta L_\mathrm{arm}$) | Core Phase 1 |
| 2.4 | 50:50 Beamsplitter Transformation ($B$ matrix) | Core Phase 1 |
| 2.5 | Field-Level Recombination | Core Phase 1 |
| 2.6 | Bright-Port Intensity ($I_\mathrm{bright}$) | Core Phase 1 |
| 2.7 | Dark-Port Intensity ($I_\mathrm{dark}$) | Core Phase 1 |
| 2.8 | Constructive and Destructive Interference | Core Phase 1 |
| 2.9 | Periodicity and Symmetry | Core Phase 1 |
| 2.10 | GW Strain-to-Differential-Length Relation ($\Delta L_\mathrm{arm}(t) = h(t)L_0$) | Phase 1/Phase 2 boundary |

### 2.11 Core Phase 1 Claims vs. Boundary Claim

Claims 1–9 constitute the closed, self-contained optical model: they involve
only geometric arm lengths, optical wavelength, and the beamsplitter
convention. Claim 10 is different in kind — it couples general-relativistic
metric strain to mechanical arm displacement, and is therefore treated
throughout this document as an interface to the subsequent GW-response work
rather than as a tenth core optical result. Full boundary reasoning is in
Section 6.

---

## 3. Literature-Validation Method

### 3.1 Claim-by-Claim Validation Approach

Evidence was assessed claim by claim rather than treating the literature
corpus as one undifferentiated authority. For each claim, sources were
checked individually for what they actually verify, not merely for whether
they mention the general topic.

### 3.2 Evidence Chain

The audit logic applied to every claim is:

$$
\text{independent formulation} \rightarrow \text{literature formulation}
\rightarrow \text{source evidence} \rightarrow \text{assumptions/conventions}
\rightarrow \text{notation mapping} \rightarrow \text{conflict assessment}
\rightarrow \text{final status}.
$$

### 3.3 Source Roles and Evidence Use

Sources are classified, per claim, by the role they play:

- **Primary supporting evidence** — the source most directly establishes the
  claim in matching or near-matching notation.
- **Independent confirmation** — an unrelated source reaches the same result.
- **Convention comparison** — the source uses a different convention
  (half-difference arm length, Fresnel beamsplitter phase, etc.) that must
  be reconciled rather than treated as disagreement.
- **Supplementary evidence** — the source touches the claim tangentially
  (e.g., a space-based interferometry paper confirming a general relation
  also used in ground-based detectors).

A given source's role can differ from claim to claim; no source is assigned
one fixed role across the whole document.

### 3.4 Treatment of Notation and Conventions

Mathematically different-looking equations from different sources cannot be
compared until their definitions are aligned. The most consequential
recurring alignment needed throughout this document is the full-difference
vs. half-difference arm-length convention (Section 5.1).

### 3.5 Treatment of Apparent Conflicts

An apparent disagreement between sources is classified as exactly one of:
physical contradiction, notation difference, sign convention, port-label
convention, or assumption difference. No genuine physical contradiction was
identified among the claims examined in this document (Section 5.6).

### 3.6 Validation Status Categories

Three statuses are used throughout, matching those actually produced by the
research process (no additional categories are introduced):

- **VERIFIED** — the claim is supported by the literature with no additional
  assumptions beyond the model's own stated idealizations.
- **VERIFIED WITH EXPLICIT ASSUMPTIONS** — the claim is supported, but only
  under specific, stated physical assumptions (e.g., normal retroreflection,
  ideal 50:50 splitting).
- **CONVENTION/DEFINITION DEPENDENT** — the claim's validity depends on which
  of two or more equally legitimate conventions is adopted (e.g., which port
  is labeled "bright").

---

## 4. Claim-by-Claim Literature Evidence

### 4.1 Claim 1 — Physical Differential Arm Length

**4.1.1 Project Formulation**

$$\Delta L_\mathrm{arm} = L_x - L_y$$

**4.1.2 Literature Formulations**

- Bond et al.: $\Delta L = L_N - L_E$ (full-difference)
- Martynov et al.: $L = L_\parallel - L_\perp$ (full-difference)
- Abbott et al. (2016): $\Delta L(t) = \delta L_x - \delta L_y$ (full-difference)
- Cahillane & Mansell: $\Delta L = (L_x - L_y)/2$ (half-difference)
- Dooley, Grote & van den Brand: $\Delta L = L_y - L_x$ (reversed sign)

**4.1.3 Supporting Evidence**

| Source | Location | Support type |
|---|---|---|
| Bond et al. (2017) | §5.2, Eq. (5.10), p. 45 | Direct — confirmed verbatim: "The light power on the main photo detector (PD) changes when the difference between the arm length $\Delta L = L_X - L_Y$ changes." |
| Martynov et al. (2016) | §II, p. 3 | Direct |
| Abbott et al. (2016) | §I, p. 3 | Direct |
| Cahillane & Mansell (2021) | App. A.1, p. 24 | Direct, after half-difference conversion |
| Dooley, Grote & van den Brand (2021) | §2.1, p. 7 | Direct, after sign-reversal conversion |

**4.1.4 Assumptions and Conventions**

Physical-model assumptions: arms strictly orthogonal ($90°$); arm lengths
measured from the physical center of the 50:50 beamsplitter to the
high-reflectivity mirror faces. Source assumption: macroscopic unperturbed
arm lengths approximately equal ($L_x \approx L_y = L_0$). Formulation
assumption: fixed coordinate mapping, $L_x$ = inline/North arm,
$L_y$ = perpendicular/East arm.

**4.1.5 Notation Mapping**

$L_N \to L_x$, $L_E \to L_y$; $L_\parallel \to L_x$, $L_\perp \to L_y$;
$\Delta L_\text{half} = \Delta L_\mathrm{arm}/2$;
$\Delta L_\text{reversed} = -\Delta L_\mathrm{arm}$.

**4.1.6 Apparent Conflict**

Three distinct-looking definitions: full-difference, half-difference, and
reversed-sign.

**4.1.7 Resolution**

Pure variable-definition choice, not a physical contradiction. The absolute
physical distance between test-mass faces, $|L_x - L_y|$, is invariant
across all three conventions.

**4.1.8 Literature Status**

✅ **VERIFIED**

**4.1.9 Phase Scope**

Phase 1 — core.

**4.1.10 Limitations**

Valid only for static or quasi-static geometric physical lengths of
orthogonal arms; does not itself address time-dependence (introduced later,
Claim 10).

---

### 4.2 Claim 2 — Round-Trip Optical Path Difference

**4.2.1 Project Formulation**

$$\Delta L_\mathrm{rt} = 2\Delta L_\mathrm{arm}$$

**4.2.2 Literature Formulations**

- Dooley, Grote & van den Brand: $T_{\mathrm{rt}\pm} = \frac{2L}{c}(1 \pm h/2)$, $\Delta T_\mathrm{rt} = 2Lh/c$
- Freise (FINESSE Manual, as cited): $\Delta L' = 2\Delta L$ (optical path vs. physical displacement)
- Cahillane & Mansell: phase exponents $e^{i2kL_x}$, $e^{i2kL_y}$ (round-trip factor kept inline)

**4.2.3 Supporting Evidence**

| Source | Location | Support type |
|---|---|---|
| Dooley, Grote & van den Brand (2021) | §2.1, Eqs. (1)–(2), p. 7 | Direct — round-trip transit-time doubling |
| Freise (FINESSE Manual, LIGO-T1300431, "FINESSE 1.0," June 2013) | §3.6.1, Eq. (3.150), p. 65–69 | Source identity now confirmed — the primary manual (not the earlier-checked companion arXiv note, 1306.2973) was located and fetched during this audit. §3.3.1 and §3.4.4 (Eq. 3.36) were directly confirmed verbatim (see Claims 4–5 below); §3.6.1 itself was not reached within the fetched portion of the document and its specific $\Delta L' = 2\Delta L$ excerpt remains unconfirmed. Narrower residual traceability item — the relation is independently confirmed by Dooley et al. and Cahillane & Mansell regardless. |
| Cahillane & Mansell (2021) | App. A.1, Eqs. (A1)–(A2), p. 23 | Direct — double-pass phase accumulation |

**4.2.4 Assumptions and Conventions**

Physical-model assumptions: normal retroreflection ($180°$ reflection along
the incoming axis); collinear incoming/returning beam paths. Source
assumption: vacuum propagation ($n \approx 1$). Formulation assumption:
introduction of the explicit standalone variable $\Delta L_\mathrm{rt}$,
which literature does not define as a separate named quantity — the
round-trip factor of 2 is instead kept inline within phase exponents
($2kL_x$) or transit times ($2L/c$).

**4.2.5 Notation Mapping**

$c\,\Delta T_\mathrm{rt} \to \Delta L_\mathrm{rt}$; $\Delta L' \to \Delta L_\mathrm{rt}$.

**4.2.6 Apparent Conflict / Definition Issue**

No standalone literature equation "$\Delta L_\mathrm{rt} = 2\Delta L_\mathrm{arm}$"
exists verbatim; this is a project-introduced shorthand.

**4.2.7 Resolution**

Convention/notation difference only — the physical content (double-pass
propagation gives a factor of 2) is established consistently across all
three sources; only the choice to name it as a standalone variable is the
project's own.

**4.2.8 Literature Status**

🟡 **VERIFIED WITH EXPLICIT ASSUMPTIONS**

**4.2.9 Phase Scope**

Phase 1 — core.

**4.2.10 Limitations**

Assumes normal incidence on end test masses and uniform refractive index
($n=1$) along both arm vacuum paths; does not address arm-cavity buildup
(explicitly out of Phase 1 scope).

---

### 4.3 Claim 3 — Differential Optical Phase

**4.3.1 Project Formulation**

$$\Delta\phi = \frac{2\pi}{\lambda}\Delta L_\mathrm{rt} = \frac{4\pi}{\lambda}\Delta L_\mathrm{arm} = 2k\Delta L_\mathrm{arm}$$

**4.3.2 Literature Formulations**

- Dooley et al.: $\Delta\phi_\mathrm{rt} = 2kLh$
- Bond et al.: $S = P_0\cos^2(k\Delta L)$, i.e. $\Delta\phi = 2k\Delta L$
- Thorne (1995): $\Delta\Phi \sim 100 \times 4\pi\Delta L/\lambda$ (Eq. 4, §3.5; the factor 100 is a LIGO-specific cavity-storage multiplier and is not part of the base relation)
- Jaranowski & Królak: $\Delta\phi(t) = 4\pi\nu_0 L h(t)$ ($c=1$ units)
- Cahillane & Mansell: field phase argument $2k\Delta L_\text{half}$

**4.3.3 Supporting Evidence**

| Source | Location | Support type |
|---|---|---|
| Dooley, Grote & van den Brand | §2.1, Eq. (3), p. 8 | Direct |
| Bond et al. | §5.2, Eq. (5.12), p. 46 | Direct |
| Thorne (1995, arXiv:gr-qc/9506086) | §3.1 Eq. (2) and §3.5 Eq. (4) | Direct — verified against the primary source during this audit; both the base phase relation and the underlying $4\pi\Delta L/\lambda$ scaling are confirmed verbatim |
| Jaranowski & Królak | §2.2, p. 7 | Direct |
| Cahillane & Mansell | App. A.1, Eq. (A5), p. 24 | Direct, after half-difference conversion |

**4.3.4 Assumptions and Conventions**

Physical-model assumption: monochromatic, highly coherent laser light;
plane-wave propagation. Source assumption: constant wavenumber
$k = 2\pi/\lambda$. Formulation assumption: standardizing all literature
expressions into full-difference notation.

**4.3.5 Full- vs Half-Difference Mapping**

Full-difference sources write $\Delta\phi = 2k\Delta L_\text{full} = 4\pi\Delta L_\mathrm{arm}/\lambda$.
Half-difference sources write the field phase as $2k\Delta L_\text{half}$,
which substituting $\Delta L_\text{half} = \Delta L_\mathrm{arm}/2$ gives
$k\Delta L_\mathrm{arm} = \Delta\phi/2$ — algebraically identical once the
substitution is made.

**4.3.6 Apparent Factor-of-Two Conflict**

$\Delta\phi = 2k\Delta L$ (Bond et al.) appears to differ from
$\Delta\phi = 4k\Delta L$ (half-difference reading of Cahillane & Mansell).

**4.3.7 Resolution**

Entirely explained by whether $\Delta L$ denotes $L_x - L_y$ or
$(L_x-L_y)/2$; not a physical disagreement.

**4.3.8 LWA Boundary**

Per the analytical model (§6.2), the Long-Wavelength Approximation is **not
required** for this purely wave-optical phase relation. This is the model's
own explicit statement, and this document uses that wording — not the
stronger, less-qualified "dynamically exact" phrasing that appeared in
earlier research-history drafts — since the analytical model itself only
establishes that LWA is unnecessary here, not that the relation is exact
under all possible physical conditions.

**4.3.9 Literature Status**

✅ **VERIFIED**

**4.3.10 Phase Scope**

Phase 1 — core.

**4.3.11 Limitations**

Does not include Fabry–Pérot cavity optical buildup or frequency-dependent
transfer functions; assumes zero laser linewidth/frequency jitter.

---

### 4.4 Claim 4 — 50:50 Beamsplitter Transformation

**4.4.1 Project Formulation**

$$B = \frac{1}{\sqrt2}\begin{pmatrix}1 & i \\ i & 1\end{pmatrix}$$

**4.4.2 Literature Formulations**

- Bond et al.: energy-conservation constraint $\tfrac12(\varphi_{r1}+\varphi_{r2}) - \varphi_t = (2N+1)\pi/2$, adopting $\varphi_r=0$, $\varphi_t=\pi/2$
- Freise (FINESSE Manual, as cited): matrix with reflection $\eta_0$, transmission $i\eta_1$
- Cahillane & Mansell: Fresnel $\pm$ convention, $B_\text{Fresnel} = \tfrac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$

**4.4.3 Supporting Evidence**

| Source | Location | Support type |
|---|---|---|
| Bond et al. | §2.4, Eqs. (2.25) & (2.29), p. 19 | Direct — derives the full energy-conservation constraint verbatim: "the phase change upon transmission $\varphi_t$ should be the same in both directions... we write $\varphi_{r1}$ for the reflection at the front and $\varphi_{r2}$ for the reflection at the back," resolving to $\varphi_t = \pi/2, \varphi_r = 0$. Confirmed against the primary Springer/Living Reviews source during this audit. |
| Freise (FINESSE Manual, LIGO-T1300431) | §3.3.1, p. 31; §3.4.4, Eq. (3.36), p. 40 | Direct — confirmed verbatim during this audit against the primary manual. §3.3.1: "the phase is not changed upon reflection; instead, the phase changes by π/2 at every transmission." §3.4.4, Eq. (3.36): $\text{Out}_1 = r\,\text{In}_1 + it\,\text{In}_2$, $\text{Out}_2 = r\,\text{In}_2 + it\,\text{In}_1$. |
| Cahillane & Mansell | App. A.1, Eqs. (A1)–(A7), p. 24 | Direct — convention comparison |

**4.4.4 Assumptions and Conventions**

Physical-model assumption: lossless 50:50 power splitting ($R=T=0.5$).
Source assumption: reciprocal, unitary, energy-conserving two-port optical
component. Formulation assumption: selection of the symmetric phase
convention ($\varphi_t = \pi/2$, giving the factor $i$), rather than the
Fresnel convention.

**4.4.5 Symmetric vs Fresnel Convention**

Symmetric: $B = \tfrac{1}{\sqrt2}\begin{pmatrix}1&i\\i&1\end{pmatrix}$.
Fresnel: $B_\text{Fresnel} = \tfrac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$,
with a $-1$ (180°) phase flip on back-surface reflection instead of a
$\pi/2$ transmission phase.

**4.4.6 Apparent Matrix/Port Conflict**

The two conventions assign the bright/dark output labels to opposite ports.

**4.4.7 Resolution**

Convention choice, not contradiction: both matrices are unitary, both
conserve total energy ($I_1+I_2=I_\text{in}$), and both produce the same
$\sin^2$/$\cos^2$ functional forms for the two output intensities — only
the port *labels* swap.

**4.4.8 Literature Status**

🟡 **VERIFIED WITH EXPLICIT ASSUMPTIONS**

**4.4.9 Phase Scope**

Phase 1 — core.

**4.4.10 Limitations**

Assumes ideal 50:50 power splitting and zero substrate loss or wavefront
distortion; does not model coating absorption or scattering.

---

### 4.5 Claim 5 — Field-Level Recombination

**4.5.1 Project Formulation**

$$
E_\mathrm{dark} = iE_\mathrm{in}e^{i\phi_\mathrm{av}}\sin\!\left(\frac{\Delta\phi}{2}\right), \qquad
E_\mathrm{bright} = iE_\mathrm{in}e^{i\phi_\mathrm{av}}\cos\!\left(\frac{\Delta\phi}{2}\right)
$$

derived by applying $B$ twice: once to split the input field, once to
recombine the returning arm fields.

**4.5.2 Literature Formulations**

- Bond et al.: $E_S = i\,2rt\,E_0\,e^{i2k\bar L}\cos(k\Delta L)$
- Freise (FINESSE Manual, as cited): $E_S = \tfrac{i}{\sqrt2}E_\mathrm{in}(1-\ldots)$
- Cahillane & Mansell: $E_\text{as} = -iE_\mathrm{in}e^{i2kL}\sin(2k\Delta L)$

**4.5.3 Supporting Evidence**

| Source | Location | Support type |
|---|---|---|
| Bond et al. | §2.4, Eq. (2.16); §5.2, Eqs. (5.9)–(5.12), pp. 45–46 | Direct |
| Freise (FINESSE Manual, LIGO-T1300431) | §3.6.1, Eq. (3.146), p. 66 | Source identity confirmed (as in 4.2.3); this specific equation was not reached within the fetched portion of the document. The beamsplitter matrix it builds on (Eq. 3.36, §3.4.4) is directly confirmed. |
| Cahillane & Mansell | App. A.1, Eqs. (A3)–(A5), p. 24 | Direct, convention-shifted |

**4.5.4 Assumptions and Conventions**

Physical-model assumptions: ideal 50:50 splitting; equal returning arm
field amplitudes ($E_x = E_y$); lossless retroreflection. Formulation:
reapplication of the same matrix $B$ on both the initial split and the
recombination pass (the reciprocal-beamsplitter assumption, stated
explicitly in `analytical_model.md` §18.2).

**4.5.5 Field/Port Convention Mapping**

Under the symmetric convention, Port 1 is the dark port
($\propto \sin(\Delta\phi/2)$) and Port 2 is the bright port
($\propto \cos(\Delta\phi/2)$).

**4.5.6 Apparent Conflict**

Recombined-field expressions differ in phase factors between the symmetric
and Fresnel conventions.

**4.5.7 Resolution**

Caused entirely by which beamsplitter phase convention is adopted (Claim 4);
resolved identically to 4.4.7.

**4.5.8 Literature Status**

🟡 **VERIFIED WITH EXPLICIT ASSUMPTIONS**

**4.5.9 Phase Scope**

Phase 1 — core.

**4.5.10 Limitations**

Requires perfect spatial mode overlap at recombination; a contrast defect
occurs if beam profiles or amplitudes differ between arms — outside Phase 1
scope.

---

### 4.6 Claim 6 — Bright-Port Intensity

**4.6.1 Project Formulation**

$$I_\mathrm{bright} = I_0\cos^2\!\left(\frac{\Delta\phi}{2}\right) = \frac{I_0}{2}(1+\cos\Delta\phi)$$

**4.6.2 Literature Formulations**

- Bond et al.: $S = P_0\cos^2(k\Delta L)$
- Libbrecht & Black: $V_\text{det} = \tfrac{V_0}{2}(1+\cos(2kx))$
- Dooley et al.: $P_{AS} = P_0\cos^2(k\Delta L)$ (under their port-naming convention)

**4.6.3 Supporting Evidence**

| Source | Location | Support type |
|---|---|---|
| Bond et al. | §5.2, Eq. (5.12), p. 46 | Direct |
| Libbrecht & Black | §II.A, Eq. (1), p. 411 | Direct — photodetector-voltage proxy |
| Dooley, Grote & van den Brand | §2.1.1, Eq. (7), p. 9 | Direct, under their own naming |

**4.6.4 Assumptions and Conventions**

Physical-model assumptions: ideal 50:50 splitting, equal returning beam
amplitudes, perfect spatial mode-matching. Formulation assumption: reflected/
transmitted port designated bright under the symmetric convention.

**4.6.5 Port-Label Convention**

The plus-sign form is specific to whichever port a given source's convention
labels as bright/symmetric.

**4.6.6 Apparent Sign/Port Conflict**

None between sources on the mathematical form; the issue is one of
*applicability*, addressed in 4.6.7.

**4.6.7 Resolution**

No conflict in the formula itself. The relevant caveat is that gravitational-
wave detectors do not read out at this port operationally (see Claim 7).

**4.6.8 Literature Status**

⚠️ **CONVENTION/DEFINITION DEPENDENT**

**4.6.9 Phase Scope**

Phase 1 — core.

**4.6.10 Limitations**

Does not represent the primary GW signal-readout channel; GW detectors
operate on the dark fringe (Claim 7), not the bright fringe.

---

### 4.7 Claim 7 — Dark-Port Intensity

**4.7.1 Project Formulation**

$$I_\mathrm{dark} = I_0\sin^2\!\left(\frac{\Delta\phi}{2}\right) = \frac{I_0}{2}(1-\cos\Delta\phi)$$

**4.7.2 Literature Formulations**

- Cahillane & Mansell: $P_\text{as} = P_\text{in}\sin^2(2k\Delta L) = \tfrac{P_\text{in}}{2}(1-\cos(4k\Delta L))$
- LIGO Scientific Collaboration (2009): qualitative dark-fringe operation
- Hild et al.: DC-readout dark-fringe offset

**4.7.3 Supporting Evidence**

| Source | Location | Support type |
|---|---|---|
| Cahillane & Mansell | App. A.1, Eq. (A7), p. 24 | Direct |
| LIGO Scientific Collaboration (2009) | §4.1, p. 3 | Direct — verbatim: "un-modulated light interferes destructively at the antisymmetric (AS) port — the dark fringe condition" |
| Abbott et al. (2016) | §I, p. 3 | Independent confirmation — output photodetector records dark-fringe variations |
| Bond et al. | §5.4, pp. 48–50 | Independent confirmation — operating on dark fringe |
| Hild et al. | §2, p. 2 | Independent confirmation — DC-readout dark-fringe offset |
| Dupletsa, Iacovelli, Korobko et al. (Einstein Telescope, arXiv:2607.27311) | as cited | Supplementary — next-generation ground-detector context for dark-fringe/readout operation, identity confirmed during this audit; specific passage content not independently re-verified beyond identity confirmation |

**4.7.4 Assumptions and Conventions**

Physical-model assumptions: ideal 50:50 splitting, equal returning field
amplitudes, 100% spatial/polarization mode-matching, operation near the dark
fringe. Formulation: antisymmetric port designated dark for GW readout,
minus sign.

**4.7.5 Dark/Antisymmetric-Port Convention**

The minus-sign form is invariant across both the symmetric and Fresnel
beamsplitter conventions for whichever port is physically antisymmetric.

**4.7.6 Apparent Sign/Port Conflict**

Same underlying issue as Claim 6 — resolved identically.

**4.7.7 Resolution**

The minus-sign intensity is confirmed as the correct GW-readout formula
independent of beamsplitter phase-convention choice.

**4.7.8 Literature Status**

🟡 **VERIFIED WITH EXPLICIT ASSUMPTIONS**

**4.7.9 Phase Scope**

Phase 1 — core.

**4.7.10 Limitations**

Assumes ideal destructive interference (zero contrast defect); ignores DC
homodyne offset tuning and higher-order spatial-mode carrier leakage, both
of which are real-detector effects outside Phase 1 scope.

---

### 4.8 Claim 8 — Constructive and Destructive Interference

**4.8.1 Project Formulation**

$$
\Delta\phi = 0 \implies I_\mathrm{dark}=0,\ I_\mathrm{bright}=I_0; \qquad
\Delta\phi = \pi \implies I_\mathrm{dark}=I_0,\ I_\mathrm{bright}=0
$$

**4.8.2 Literature Formulations**

- Bond et al.: "At $0°$ the Michelson is on a bright fringe and at $90°$ on a dark fringe."
- LIGO Scientific Collaboration (2009): dark-fringe/full-power-return description

**4.8.3 Supporting Evidence**

| Source | Location | Support type |
|---|---|---|
| Bond et al. | §5.3, pp. 46–48 | Direct |
| LIGO Scientific Collaboration (2009) | §4.1, p. 3 | Direct |
| Cahillane & Mansell | App. A.1, p. 24 | Independent confirmation |

**4.8.4 Assumptions and Conventions**

Physical-model assumptions: monochromatic light, equal returning beam
amplitudes, zero differential loss between arms.

**4.8.5 Phase/Arm-Length Mapping**

Tuning $0° \implies k\Delta L = 0 \implies \Delta\phi = 0$; tuning
$90° \implies k\Delta L = \pi/2 \implies \Delta\phi = \pi$.

**4.8.6 Apparent Conflict**

None.

**4.8.7 Resolution**

Not applicable.

**4.8.8 Literature Status**

✅ **VERIFIED**

**4.8.9 Phase Scope**

Phase 1 — core.

**4.8.10 Limitations**

Assumes perfect destructive cancellation (zero loss/asymmetry between arms);
real detectors never reach exactly $I_\mathrm{dark}=0$.

---

### 4.9 Claim 9 — Periodicity and Symmetry

**4.9.1 Project Formulation**

$$
I(\Delta\phi + 2\pi) = I(\Delta\phi), \qquad I(\Delta\phi) = I(-\Delta\phi)
$$

corresponding to a differential-arm-length period of $\lambda/2$.

**4.9.2 Literature Formulations**

- Bond et al.: "displacement of one mirror by $\Delta x = \lambda/2$ re-creates exactly the same condition"; power varies as $\cos^2$
- Libbrecht & Black: $\cos(2kx)$ periodicity

**4.9.3 Supporting Evidence**

| Source | Location | Support type |
|---|---|---|
| Bond et al. | §2.5, Fig. 12; §5.6.2, pp. 20, 55 | Direct |
| Libbrecht & Black | §II.A, p. 411 | Independent confirmation |

**4.9.4 Assumptions and Conventions**

Physical-model assumptions: monochromatic laser light; spatial coherence.

**4.9.5 Phase/Length Period Mapping**

$\Delta x = \lambda/2 \implies 2k\Delta x = 2(2\pi/\lambda)(\lambda/2) = 2\pi$.

**4.9.6 Apparent Conflict**

None.

**4.9.7 Resolution**

Not applicable.

**4.9.8 Literature Status**

✅ **VERIFIED**

**4.9.9 Phase Scope**

Phase 1 — core.

**4.9.10 Limitations**

Valid for a single-frequency carrier field only; multi-frequency/modulated
fields (outside Phase 1 scope) can break the simple periodicity.

---

### 4.10 Claim 10 — GW Strain-to-Differential-Length Relation

**4.10.1 Boundary Formulation**

$$
\Delta L_\mathrm{arm}(t) = h(t)L_0, \qquad h(t) \equiv F_+h_+(t) + F_\times h_\times(t)
$$

**4.10.2 Literature Formulations**

- Abbott et al. (2016): $\Delta L(t) = \delta L_x - \delta L_y = h(t)L$
- Cahillane & Mansell: $\Delta L_x = h_+L_x/2$, $\Delta L_y = -h_+L_y/2$, $\Delta L = h_+L$
- Thorne (1995): $\Delta L(t)/L = F_+h_+(t) + F_\times h_\times(t) \equiv h(t)$
- Martynov et al.: $L(f) = L_\parallel - L_\perp = h(f)L_0$

**4.10.3 Supporting Evidence**

| Source | Location | Support type |
|---|---|---|
| Abbott et al. (2016) | §I, p. 3 | Direct |
| Cahillane & Mansell | §2, Eqs. (8)–(10), pp. 2–3 | Direct — individual arm distortion and differential combination |
| Thorne (1995, arXiv:gr-qc/9506086) | §3.1, Eq. (2) | Direct — verified against the primary source during this audit; this is the exact formulation the project adopts |
| Martynov et al. | §II, p. 3 | Direct, frequency-domain form |
| Ni (2024, arXiv:2409.00927), incl. Passage 969 (§7.2, TDI/equal-arm-length context) | as cited | Supplementary — space-based generalized-Michelson/TDI context for the equal-arm-length approximation underlying this relation; source identity and general section content confirmed during this audit |

Two passage citations from an earlier research-history draft (883, 898, 900,
attributed to Arun et al., "New Horizons for Fundamental Physics with LISA,"
arXiv:2205.01597) were checked against the primary source during this audit
and found **not** to support this claim: the cited passages are reference-
list entries in a paper whose body content addresses tests of general
relativity and dark-matter constraints with LISA, not detector strain
response or antenna-pattern formulas. These citations have been removed from
this claim's evidence; they are noted here only so the correction is
traceable.

**4.10.4 Explicit Assumptions**

Physical-model assumption: equal nominal arm lengths ($L_x=L_y=L_0$). Source
assumption: transverse-traceless gauge in general relativity; quadrupolar
metric perturbation $h_{\mu\nu}$. Formulation assumptions: overhead GW
propagation ($\theta=0$); perfect $+$-polarization alignment with the
detector arms ($F_+=1$, $F_\times=0$). Approximation: the Long-Wavelength
Approximation, $\lambda_\mathrm{GW} \gg L_0$, i.e.
$f_\mathrm{GW} \ll f_* = c/(2\pi L_0)$ ($\sim 12$ kHz for 4 km arms).

**4.10.5 Detector-Projected vs Incident Strain**

Aligned case: $h(t) = h_+(t)$. General sky coordinates:
$h(t) \equiv F_+(\theta,\phi,\psi)h_+(t) + F_\times(\theta,\phi,\psi)h_\times(t)$.
The physical differential displacement $\Delta L_\mathrm{arm}(t)$ is
invariant regardless of which interpretation is used.

**4.10.6 Apparent Formulation Conflict**

A single arm's displacement is $\Delta L_x = \tfrac12 hL_0$; the full
$hL_0$ factor in the *differential* relation is recovered only by
subtracting the orthogonal arm's opposite-sign displacement:
$\Delta L_x - \Delta L_y = \tfrac12 hL_0 - (-\tfrac12 hL_0) = hL_0$.

**4.10.7 Resolution**

Not a conflict — a step in the derivation that must be shown explicitly, per
4.10.6.

**4.10.8 Literature Status**

🟡 **VERIFIED WITH EXPLICIT ASSUMPTIONS**

**4.10.9 Phase 1/Phase 2 Boundary**

This claim couples general-relativistic metric strain to mechanical arm
displacement. It is the interface between the Phase 1 optical model and the
subsequent GW-response stages (Master Plan Stage 2), and is not treated as
part of the core Phase 1 optical derivation (`analytical_model.md` §16).

**4.10.10 Limitations**

Per the analytical-model's own wording (§16, and confirmed in this audit —
see Section 5.4 below), the Long-Wavelength Approximation is required *here*,
unlike in Claim 3. Breaks down at high GW frequencies
($f_\mathrm{GW} \geq f_*$), where a frequency-dependent sinc transfer
function is required — explicitly deferred to Phase 2.

---

## 5. Apparent Conflicts and Their Resolution

### 5.1 Full-Difference vs Half-Difference Notation

LIGO technical literature (Cahillane & Mansell) defines
$\Delta L \equiv (L_x-L_y)/2$; the project and most other sources use the
full difference $L_x - L_y$. Substituting the half-difference definition
into half-difference equations reproduces the project's full-difference
results exactly (Sections 4.1, 4.3). **Classification: notation/definition
difference, not a physical contradiction.**

### 5.2 Bright-Port vs Dark-Port Identification

Early evaluation of $I = \tfrac{I_0}{2}(1+\cos\Delta\phi)$ as *the*
Michelson output was incomplete. Gravitational-wave detectors specifically
read out at the antisymmetric (dark) port to suppress common-mode laser
noise (Section 4.7). **Classification: scope/applicability refinement, not
a contradiction between sources.**

### 5.3 Beamsplitter Phase and Two-Pass Matrix Convention

Symmetric ($\varphi_t=\pi/2$) and Fresnel ($-1$ back-reflection phase flip)
conventions produce matrices that swap which physical port is labeled bright
vs. dark, but both conserve total energy and produce identical functional
forms for the two output intensities (Section 4.4). **Classification:
convention difference.**

### 5.4 LWA vs Optical Phase Accumulation

Per the analytical model (§6.2) and confirmed against Thorne (1995) directly
during this audit, the Long-Wavelength Approximation is not required for the
purely optical phase relation (Claim 3), because that relation depends only
on the specified differential path length, not on how that path length
arose. The LWA is required specifically for the GW strain-to-length coupling
(Claim 10), which converts a time-varying metric perturbation into a
mechanical displacement under a quasi-static assumption. **Classification:
scope boundary between two distinct physical relations, correctly kept
separate.**

### 5.5 Incident vs Detector-Projected Strain

A single arm experiences half the strain effect ($\Delta L_x = \tfrac12 hL_0$);
the full differential factor $hL_0$ requires combining both arms'
opposite-sign displacements (Section 4.10.6). **Classification: derivation
step, not a conflict.**

### 5.6 Status of Resolved vs Convention-Dependent Differences

Across all ten claims examined in this document, **no genuine physical or
mathematical contradiction was identified.** Every apparent disagreement
resolved to one of: full- vs half-difference notation, coordinate sign
convention, beamsplitter phase-convention/port-labeling choice, or an
assumption difference (e.g., LWA applicability). This is a statement about
the specific sources examined during this audit, not a claim that all
possible GW-detector literature is mutually consistent in every regard.

### 5.7 Research-History Corrections and Superseded Interpretations

Four interpretive corrections were made in the course of this audit and are
recorded here so the reasoning is not lost from the final synthesis:

1. **Bright-port focus → explicit dark-port distinction.** Early evaluation
   of the bright-port intensity as the primary Michelson output was
   corrected once the literature (LIGO Scientific Collaboration, Cahillane &
   Mansell, Hild et al.) established that GW detectors operate on the dark
   fringe specifically to suppress common-mode laser noise.
2. **LWA mis-association → boundary separation.** The Long-Wavelength
   Approximation was initially discussed loosely in connection with the
   optical phase relation (Claim 3); it was subsequently and correctly
   restricted to the strain-to-length coupling (Claim 10) only, per 5.4.
3. **Apparent factor-of-two concern → notation mapping.** What initially
   looked like a factor-of-two discrepancy between $2k\Delta L$ and
   $4k\Delta L$ forms across sources was resolved as the full/half-difference
   convention issue (5.1), not a computational error.
4. **Repeated-$B$ uncertainty → explicit two-pass derivation.** Whether
   applying the same beamsplitter matrix $B$ on both the initial split and
   the recombination pass was internally consistent was resolved by explicit
   matrix multiplication (`analytical_model.md` §8.4), confirming unitarity
   and energy conservation.

---

## 6. Phase 1 / Phase 2 Boundary

### 6.1 Core Phase 1 Optical Model

Claims 1–9 constitute the complete, self-contained ideal-Michelson optical
model: differential arm length → round-trip path → optical phase →
beamsplitter transformation → field recombination → bright/dark intensity →
interference conditions → periodicity/symmetry.

### 6.2 GW Strain-to-Length Relation as Boundary Input

Claim 10 is retained in this document only as the interface to the
subsequent GW-response stage — it establishes what a gravitational wave
*does* to the arm lengths that Claims 1–9 then process optically. It is not
part of the core Phase 1 optical derivation.

### 6.3 General Detector Response Outside Phase 1

The angular antenna-pattern functions $F_+(\theta,\phi,\psi)$ and
$F_\times(\theta,\phi,\psi)$ are stated in general form (Claim 10) but their
full derivation belongs to the Phase 2 detector-response stage and is not
expanded here.

### 6.4 High-Frequency/Finite-Arm Response Outside Phase 1

The LWA breakdown at $f_\mathrm{GW} \geq f_*$ is flagged in the literature
(Dooley et al.; Cahillane & Mansell) but the corresponding frequency-
dependent sinc transfer function is explicitly deferred to Phase 2, not
incorporated into the frozen Phase 1 equations.

### 6.5 Later Detector Physics Explicitly Excluded

Fabry–Pérot arm cavities; power recycling; signal recycling; realistic
detector operating-point control; physical detector noise; PSD/ASD
modeling; detector sensitivity; realistic optical losses; beam
imperfections/mode mismatch; calibration.

---

## 7. Literature Validation Results

### 7.1 Claim Status Summary

| Claim | Formulation | Final Status | Scope |
|---|---|---|---|
| 1 | $\Delta L_\mathrm{arm}=L_x-L_y$ | VERIFIED | Phase 1 |
| 2 | $\Delta L_\mathrm{rt}=2\Delta L_\mathrm{arm}$ | VERIFIED WITH EXPLICIT ASSUMPTIONS | Phase 1 |
| 3 | $\Delta\phi=\tfrac{4\pi}{\lambda}\Delta L_\mathrm{arm}$ | VERIFIED | Phase 1 |
| 4 | Beamsplitter matrix $B$ | VERIFIED WITH EXPLICIT ASSUMPTIONS | Phase 1 |
| 5 | Field recombination | VERIFIED WITH EXPLICIT ASSUMPTIONS | Phase 1 |
| 6 | $I_\mathrm{bright}=\tfrac{I_0}{2}(1+\cos\Delta\phi)$ | CONVENTION/DEFINITION DEPENDENT | Phase 1 |
| 7 | $I_\mathrm{dark}=\tfrac{I_0}{2}(1-\cos\Delta\phi)$ | VERIFIED WITH EXPLICIT ASSUMPTIONS | Phase 1 |
| 8 | Constructive/destructive interference | VERIFIED | Phase 1 |
| 9 | Periodicity and symmetry | VERIFIED | Phase 1 |
| 10 | $\Delta L_\mathrm{arm}(t)=h(t)L_0$ | VERIFIED WITH EXPLICIT ASSUMPTIONS | Phase 1/2 boundary |

This table is the canonical, authoritative Claim Status Summary for this
document; label discrepancies between earlier research-history drafts for
Claims 4–7 were audited and resolved as wording-only, with one substantive
clarification (Claim 6's index shift, resolved to CONVENTION/DEFINITION
DEPENDENT as the final canonical label).

### 7.2 Fully Supported Claims

Claims 1, 3, 8, and 9 are VERIFIED with no additional explicit assumptions
beyond the model's own stated idealizations.

### 7.3 Claims Requiring Explicit Assumptions

Claims 2, 4, 5, 7, and 10 are VERIFIED WITH EXPLICIT ASSUMPTIONS — each
requires specific, stated physical conditions (normal retroreflection;
ideal 50:50 splitting; equal returning amplitudes; dark-fringe operation;
the Long-Wavelength Approximation and related conditions, respectively).

### 7.4 Convention-Dependent Claims

Claim 6 is CONVENTION/DEFINITION DEPENDENT: its plus-sign form is
mathematically correct but applies to the bright port, which is not the
primary GW readout channel. Claims 4 and 7 also carry convention dependence
(beamsplitter phase choice; port labeling) but are otherwise fully
supported once a convention is fixed.

### 7.5 Overall Phase 1 Literature-Validation Result and Closure/Handoff

The core ideal-Michelson claim set (Claims 1–9) has authoritative literature
support. All identified apparent discrepancies across sources were
investigated and resolved as notation, sign-convention, port-labeling, or
assumption differences — no genuine physical contradiction was found among
the sources examined (Section 5.6). The boundary claim (10) is supported
under its explicitly stated assumptions and is correctly scoped as an
interface to Phase 2 rather than a core optical result.

**This establishes a literature-supported physics foundation for the Phase 1
ideal Michelson model.** The result of this document is the reference from
which the subsequent code-and-simulation audit and numerical-validation
stages (`numerical_validation.md`, tests T10–T13)
proceed. This document does not itself perform or describe that later
validation work.

---

## 8. Limitations of the Literature Validation

### 8.1 Underlying Evidence Availability

Source names, sections, equation numbers, and page references are available
for essentially all citations. Verbatim excerpt text was independently
confirmed against primary sources for the large majority of claims during
this and a subsequent audit pass — notably Bond et al. for Claim 4, Thorne
(1995) for Claims 3 and 10, and, on a second pass, the primary FINESSE
Manual itself (LIGO-T1300431, "FINESSE 1.0," Freise, June 2013 — located
directly, correcting an earlier mismatch with a shorter companion arXiv
note, 1306.2973). The manual's §3.3.1 (beamsplitter phase convention) and
§3.4.4, Eq. (3.36) (mirror/beamsplitter coupling matrix) are now confirmed
verbatim and support Claims 4 and 5 directly.

One narrower item remains outstanding: §3.6.1 of the same manual (Eq. 3.150,
$\Delta L' = 2\Delta L$, and Eq. 3.146 — the specific equations underlying
Claims 2 and 5's round-trip optical path and field-recombination citations)
was not reached within the portion of the document retrieved during this
audit. This does not affect either claim's status: both are independently
supported by Dooley et al. and Cahillane & Mansell (Claim 2) and by the
now-confirmed beamsplitter matrix itself (Claim 5).

### 8.2 Search Methodology & Source Selection

No formal, standalone search-methodology or source-selection-criteria
document exists in the project workspace. Source selection was conducted
via an exhaustive, claim-driven filter applied directly across a 35-document
uploaded corpus: a document was included in the primary evidence inventory
if and only if it provided an explicit mathematical, optical, or physical
formulation supporting one of the ten Phase 1 claims, or contributed
directly to resolving a convention/notation conflict. Sources focused on
educational/museum exhibits, software/data-analysis pipelines unrelated to
core optics, or specialized noise-budget material without core Michelson
relations were scanned but excluded from the final evidence inventory.

### 8.3 Source-Selection/Authority Documentation

Source roles (primary, independent confirmation, convention comparison,
supplementary) were assigned per claim based on the content actually found,
per Section 3.3. No separate, pre-registered authority ranking of sources
exists beyond this claim-by-claim assessment.

### 8.4 Bibliographic Completeness

Full bibliographic metadata (author lists, journal/arXiv identifiers,
publication years, DOIs where available) was obtained and confirmed for all
primary sources during this audit; see Section 9.

### 8.5 Limits of Convention Reconciliation

This document resolves the convention differences actually encountered
among the sources examined (full/half-difference arm length; symmetric/
Fresnel beamsplitter phase; bright/dark port labeling). It does not
establish universal equivalence for every possible arm-length or
beamsplitter-phase convention that might appear elsewhere in the broader GW
literature.

### 8.6 Scope of the Validation Result

This document validates the defined ideal Phase 1 optical model — a
minimal, lossless, single-frequency, two-arm Michelson interferometer — not
a complete real gravitational-wave detector. The analytical model's own
stated idealizations (`analytical_model.md` §18) remain in force throughout;
this document adds literature support for those idealized relations, not a
claim that real detectors behave exactly as modeled.

### 8.7 Evidence-Traceability Limitation

Where a source is cited by name, section, and equation number but the
verbatim excerpt was not independently re-confirmed during this final audit
pass (see 8.1), that is noted explicitly at the claim level (Sections
4.2.3, 4.4.3, 4.5.3) rather than left implicit. Synthesis conclusions in
this document are not a substitute for reading the original sources, and
readers requiring full excerpt-level traceability should consult the
primary documents directly.

---

## 9. References

### 9.1 Primary Literature Sources

1. Bond, C., Brown, D., Freise, A., & Strain, K. A. (2016/2017). *Interferometer techniques for gravitational-wave detection.* Living Reviews in Relativity, 19(3), 1–217. DOI: 10.1007/s41114-016-0002-8. (Original 2010 edition: DOI 10.12942/lrr-2010-1.)
2. Cahillane, C., & Mansell, G. (2021). *Review of the Advanced LIGO gravitational wave observatories leading to observing run four.* Preprints, 1(0), 1–33. LIGO document LIGO-P2100298.
3. Dooley, K. L., Grote, H., & van den Brand, J. (2021). *Terrestrial Laser Interferometers.* arXiv:2103.01740 [physics.ins-det].
4. Abbott, B. P., et al. (LIGO Scientific Collaboration and Virgo Collaboration). (2016). *Observation of Gravitational Waves from a Binary Black Hole Merger.* Physical Review Letters, 116(6), 061102. DOI: 10.1103/PhysRevLett.116.061102. arXiv:1602.03838 [gr-qc].
5. Thorne, K. S. (1995). *Gravitational Waves.* In *Proceedings of the Snowmass 95 Summer Study on Particle and Nuclear Astrophysics and Cosmology*, eds. E. W. Kolb and R. Peccei. arXiv:gr-qc/9506086.
6. Freise, A. (2013). *FINESSE 1.0 — Frequency domain INterferomEter Simulation SoftwarE: Mathematical description of light beams and optical components.* LIGO Document LIGO-T1300431. www.gwoptics.org/finesse. (Distinct from: Bond, C., Brown, D., & Freise, A. (2013). *Finesse, Frequency domain INterferomEter Simulation SoftwarE.* arXiv:1306.2973 [physics.comp-ph] — a shorter companion software-announcement paper, not the technical manual; checked and found non-matching earlier in this audit.)
7. Martynov, D. V., Hall, E. D., et al. (2016). *The Sensitivity of the Advanced LIGO Detectors at the Beginning of Gravitational Wave Astronomy.* Physical Review D, 93(11), 112004. DOI: 10.1103/PhysRevD.93.112004. arXiv:1604.00439 [astro-ph.IM]. LIGO document LIGO-P1500248.
8. Jaranowski, P., & Królak, A. (2012). *GW data analysis and formalism.* Living Reviews review article/update publication.
9. LIGO Scientific Collaboration. (2009). *LIGO: The Laser Interferometer Gravitational-Wave Observatory.* Reports on Progress in Physics, 72(7), 076901. DOI: 10.1088/0034-4885/72/7/076901. arXiv:0711.3041 [gr-qc]. LIGO document P070082-v4.
10. Libbrecht, K. G., & Black, E. D. (2015). *A basic Michelson laser interferometer for the undergraduate teaching laboratory demonstrating picometer sensitivity.* American Journal of Physics, 83(5), 409–417. DOI: 10.1119/1.4901972.
11. Hild, S., Grote, H., Degallaix, J., Chelkowski, S., Danzmann, K., Freise, A., Hewitson, M., Hough, J., Lück, H., Prijatelj, M., Strain, K. A., Smith, J. R., & Willke, B. (2009). *DC-readout of a signal-recycled gravitational wave detector.* Classical and Quantum Gravity, 26(5), 055012. DOI: 10.1088/0264-9381/26/5/055012. arXiv:0811.3242 [gr-qc].
12. Wanner, G., Shah, S., Staab, M., Wegener, H., & Paczkowski, S. (2024). *In-Depth Modeling of Tilt-To-Length Coupling in LISA's Interferometers and TDI Michelson Observables.* arXiv:2403.06526 [astro-ph.IM].
13. Ni, W.-T. (2024). *Space gravitational wave detection: progress and outlook.* Scientia Sinica Physica, Mechanica & Astronomica, 54(7), 270402. DOI: 10.1360/SSPMA-2024-0186. English translation: arXiv:2409.00927.
14. Pitkin, M., Reid, S., Rowan, S., & Hough, J. (2011). *Gravitational wave detection by interferometry (ground and space).* Living Reviews in Relativity, 14, lrr-2011-5. DOI: 10.12942/lrr-2011-5.
15. Dupletsa, U., Iacovelli, F., Korobko, M., Sequino, V., et al. (2026). *Assessing the Impact of Instrumental Requirements on the Scientific Performance of the Einstein Telescope.* arXiv:2607.27311 [astro-ph.IM].

### 9.2 Supporting/Comparison Sources

16. Arun, K. G., et al. (2022). *New Horizons for Fundamental Physics with LISA.* arXiv:2205.01597 [gr-qc]. — Checked and confirmed real; **not used as evidentiary support for Claim 10** in this document, as its content (tests of GR, black-hole physics, dark matter) does not substantiate the strain-response formulas it was earlier cited for. Retained here only as a corrected reference.

---

*End of document. This literature-validation record is the reference for
the subsequent code-and-simulation audit and numerical-validation stages.*
