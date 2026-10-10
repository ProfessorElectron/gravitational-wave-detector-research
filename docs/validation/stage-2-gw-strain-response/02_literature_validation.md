# Literature Validation & Consistency Audit — Stage 2 (GW Strain → Differential Arm Response)

**Status:** Complete. This is **Document 2** of the Stage 2 process. It is the
literature-validation evidence record for the Stage 2 analytical model
(Document 1, `gw_detector_response` analytical model). It is an audit trail,
not a second derivation and not a general literature review.

**Terminology note:** this project's terminology is "Stage". The Stage 1
documents (`analytical_model`, `literature_validation`) use the word "Phase 1"
internally; "Stage 1" and "Phase 1" refer to the same ideal-Michelson model.

---

## 1. Purpose, Scope and Relationships

### 1.1 Purpose

This document checks the independently derived Stage 2 relation

$$
\Delta L_\mathrm{arm}(t) = h(t)\,L_0
$$

and the derivation chain beneath it against General Relativity and detector
literature, claim by claim, and records what was found. Content decisions are
grounded exclusively in the uploaded Step 4 and Step 5 packages, the Stage 1
literature-validation record, and the Stage 1 analytical model. No physics is
introduced from outside those materials.

### 1.2 Chain under test

$$
g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu}\;\rightarrow\;\text{TT gauge}\;\rightarrow\;
h_\mathrm{det}=F_+h_++F_\times h_\times\;\rightarrow\;
\delta L_x,\ \delta L_y\;\rightarrow\;\Delta L_\mathrm{arm}=hL_0\;\rightarrow\;
\Delta\phi=\frac{4\pi L_0}{\lambda_0}h .
$$

The last arrow is the Stage 2 → Stage 1 interface. The optical chain after
$\Delta L_\mathrm{arm}$ was validated in the Stage 1 literature record and is
not re-validated here.

### 1.3 Relationship to other documents

| Document | Relationship |
|---|---|
| Document 1 (Stage 2 analytical model) | The formulation under test. |
| Stage 1 `literature_validation.md` | Already audits $\Delta L_\mathrm{arm}=L_x-L_y$ (Claim 1), the phase relation (Claim 3) and the boundary relation $\Delta L_\mathrm{arm}=hL_0$ (Claim 10). This document **cites** those results where the relation is the same, and **adds** evidence only where Stage 2 introduces something new or where doubt exists (see §3.6). |
| Document 3 (Code Implementation & Physics Mapping Audit) | Later step. This document does not check the repository code (`src/gravitational_wave.py`, `simulations/gravitational_wave_injection.py`). |

### 1.4 Validation questions

For each claim: (1) is the Stage 2 formulation supported by the literature;
(2) is any apparent disagreement a physical contradiction or a notation, sign,
or assumption difference; (3) which assumptions must hold; (4) is the claim
core Stage 2, a boundary item, or a Stage 3/4 extension.

---

## 2. Claims Under Validation

| # | Claim | Scope tag |
|---|---|---|
| 1 | Weak-field linearization $g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu}$ | Core |
| 2 | TT gauge and test-mass coordinate fixity | Core |
| 3 | Tensor polarization modes $h_+,h_\times$ | Core |
| 4 | Detector tensor $d^{ij}$ and antenna patterns ($F_+=1$, $F_\times=0$ at the aligned geometry) | Core |
| 5 | Scalar shorthand $h(t)\equiv h_+(t)\equiv h_\mathrm{det}(t)$ | Core (conditional) |
| 6 | Proper-distance integral and binomial expansion → $\delta L_x=+\tfrac12hL_0$, $\delta L_y=-\tfrac12hL_0$ | Core |
| 7 | Differential combination → $\Delta L_\mathrm{arm}=hL_0$ | Core |
| 8 | Subtraction-order sign convention | Core (convention) |
| 9 | Long-Wavelength Approximation and $f^*=c/(2\pi L_0)$ | Core (validity boundary) |
| 10 | Free spectral range $f_\mathrm{FSR}$ and finite-arm response $C(f)$ | Boundary |
| 11 | Cavity pole $f_p$ | Extension (Stage 3) |
| 12 | Stage 2 → Stage 1 interface $\Delta\phi=(4\pi L_0/\lambda_0)h$ and factor-of-2 audit | Core (interface) |

---

## 3. Method

### 3.1 Evidence chain

independent formulation → literature formulation → source evidence →
assumptions/conventions → notation mapping → conflict assessment → final status.

### 3.2 Source roles

Per claim, a source is classified as primary supporting evidence, independent
confirmation, convention comparison, or supplementary evidence. A source's
role may differ between claims.

### 3.3 Status categories (Stage 1 three-tier scheme)

- **VERIFIED** — supported with no assumptions beyond the model's own stated idealizations.
- **VERIFIED WITH EXPLICIT ASSUMPTIONS** — supported only under specific stated conditions.
- **CONVENTION/DEFINITION DEPENDENT** — validity depends on which of several legitimate conventions is adopted.

Scope (core / boundary / extension) is recorded as a **separate tag** and is
not an evidence level.

**Mapping from Step 4 labels:**

| Step 4 label | Stage 1 tier used here |
|---|---|
| Directly supported by literature | VERIFIED (or VERIFIED WITH EXPLICIT ASSUMPTIONS where the claim carries explicit conditions — noted per claim) |
| Supported under stated assumptions | VERIFIED WITH EXPLICIT ASSUMPTIONS |
| Derived from literature-supported results | Tier set by the conditions of the derivation; "derived" is noted in the claim text |
| Convention-dependent | CONVENTION/DEFINITION DEPENDENT |
| Relegated to advanced extensions / "Move to Extension" | Scope tag **Extension**, not an evidence tier |

### 3.4 Locator policy

No section, page, or equation number is invented. A general reference (MTW,
Maggiore, Schutz, Saulson, Advanced LIGO review, Einstein Telescope design
study) that appears in the source packages without an explicit locator is
recorded as **"Traceability Pending"**. Locators that appear in the Stage 1
literature record are reused as recorded there.

### 3.5 Treatment of apparent conflicts

Each apparent disagreement is classified as exactly one of: physical
contradiction, notation difference, sign convention, port/label convention, or
assumption difference. No physical contradiction was identified (§7.7).

### 3.6 Reuse of Stage 1 evidence

Where a Stage 2 claim is the same relation already audited in Stage 1, it is
cited to the Stage 1 record. Because the relation $\Delta L_\mathrm{arm}=hL_0$
is the subject of this stage, Claim 6 and Claim 7 additionally carry the
Stage 2-specific evidence (per-arm factors, binomial origin, detector tensor)
rather than relying on the Stage 1 citation alone.

---

## 4. Claim-by-Claim Literature Evidence

### 4.1 Claim 1 — Weak-field linearization

**Formulation:** $g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu}$, $|h_{\mu\nu}|\ll1$, background $\eta_{\mu\nu}=\mathrm{diag}(-c^2,1,1,1)$; interval $ds^2=(\eta_{\mu\nu}+h_{\mu\nu})dx^\mu dx^\nu$.

| Source | Location | Role |
|---|---|---|
| MTW; Maggiore; Schutz | Traceability Pending | Primary supporting |

**Assumptions:** flat background; $|h|\ll1$ (typically $\sim10^{-21}$ for detected signals, per Step 5).
**Conflict:** none. **Status:** ✅ VERIFIED. **Scope:** Core.
**Limitations:** first order in $h$; $\mathcal O(h^2)$ terms are discarded (strong-field relaxation: Maggiore Vol. 1, locator pending).

### 4.2 Claim 2 — TT gauge and coordinate fixity

**Formulation:** $h^\mathrm{TT}_{0\mu}=0$; $\delta^{ij}h^\mathrm{TT}_{ij}=0$; $\partial^jh^\mathrm{TT}_{ij}=0$ ($k^ih_{ij}=0$); $\Box h^\mathrm{TT}_{\mu\nu}=0$. Freely falling test masses initially at rest keep fixed coordinates, $\Delta x_\mathrm{coord}=L_0$.

| Source | Location | Role |
|---|---|---|
| MTW; Maggiore; Schutz; Saulson | Traceability Pending | Primary supporting |

**Assumptions / conventions:** TT is a **coordinate choice**, valid far from sources for freely falling masses. In non-TT frames (Fermi normal / local Lorentz) test-mass coordinates move under tidal acceleration $\ddot x^i=\tfrac12\ddot h^\mathrm{TT}_{ij}x^j$ (Step 5).
**Conflict:** none. **Status:** ✅ VERIFIED. **Scope:** Core.
**Limitations:** the $\Delta L=hL_0$ result is derived in TT coordinates; use in other frames needs re-derivation.

### 4.3 Claim 3 — Tensor polarization modes

**Formulation:** for $k=\hat z$, $h^\mathrm{TT}_{xx}=-h_{yy}^\mathrm{TT}=h_+(t-z/c)$, $h^\mathrm{TT}_{xy}=h^\mathrm{TT}_{yx}=h_\times(t-z/c)$; ten metric components reduce to two radiative degrees of freedom.

| Source | Location | Role |
|---|---|---|
| MTW; Maggiore; Schutz | Traceability Pending | Primary supporting |

**Conflict:** none. **Status:** ✅ VERIFIED. **Scope:** Core. **Limitations:** plane wave, propagation along $+z$.

### 4.4 Claim 4 — Detector tensor and antenna patterns

**Formulation:**
$d^{ij}\equiv\tfrac12(\hat e_x^i\hat e_x^j-\hat e_y^i\hat e_y^j)$;
$h_\mathrm{det}=d^{ij}h^\mathrm{TT}_{ij}=\tfrac12\big(h_+-(-h_+)\big)=h_+$;
$h_\mathrm{det}=F_+h_++F_\times h_\times$ with
$F_+=\tfrac12(1+\cos^2\theta)\cos2\phi\cos2\psi-\cos\theta\sin2\phi\sin2\psi$,
$F_\times=\tfrac12(1+\cos^2\theta)\cos2\phi\sin2\psi+\cos\theta\sin2\phi\cos2\psi$;
$F_+(0,0,0)=1$, $F_\times(0,0,0)=0$.

| Source | Location | Role |
|---|---|---|
| Schutz; Maggiore | Traceability Pending | Primary supporting ($d^{ij}$ and its ½ normalization) |
| MTW; Schutz | Traceability Pending | Primary supporting ($F_+=1$, $F_\times=0$ at aligned geometry) |
| Advanced LIGO review; Einstein Telescope design study | Traceability Pending | Independent confirmation (antenna-pattern form) |
| Stage 1 Lit. Validation, Claim 10 | §4.10.2–4.10.5 | Thorne (1995) §3.1 Eq. (2): $h\equiv F_+h_++F_\times h_\times$ — locator as recorded in Stage 1 |

**Assumptions / conventions:** orthogonal $90^\circ$ arms; equal arms; the ½ in $d^{ij}$ is the normalization that gives peak $F_+=1$.
**Conflict:** none. **Status:** 🟡 VERIFIED WITH EXPLICIT ASSUMPTIONS (Step 4 label: directly supported; moved to the assumption tier because the result holds for orthogonal arms and carries the normalization convention).
**Scope:** Core. **Limitations:** non-orthogonal arms scale the response by $\sin\zeta$ (§5.3); Einstein Telescope $60^\circ$ geometry is a Stage 3 configuration extension.

### 4.5 Claim 5 — Scalar shorthand $h(t)$

**Formulation:** under $\theta=\phi=\psi=0$, $h_\times=0$: $h(t)\equiv h_+(t)\equiv h_\mathrm{det}(t)$.

| Source | Location | Role |
|---|---|---|
| Maggiore; Advanced LIGO review | Traceability Pending | Primary supporting |
| Stage 1 Lit. Validation, Claim 10 | §4.10.2–4.10.5 (Thorne §3.1 Eq. (2); Abbott et al. 2016 §I p. 3; Cahillane & Mansell §2) | Independent confirmation of $h(t)$ as detector-projected strain |

**Assumptions:** overhead incidence; aligned plus polarization. General case: $h_\mathrm{det}=F_+h_++F_\times h_\times$.
**Conflict:** incident vs detector-projected strain is a notation distinction (§7.4). **Status:** 🟡 VERIFIED WITH EXPLICIT ASSUMPTIONS. **Scope:** Core (conditional).
**Limitations:** the shorthand must not be used for general sky position or polarization.

### 4.6 Claim 6 — Proper distance and individual-arm responses

**Formulation:**
$ds^2=-c^2dt^2+[1+h]dx^2+[1-h]dy^2+dz^2$;
$L_x=\int_0^{L_0}\sqrt{1+h}\,dx$, $L_y=\int_0^{L_0}\sqrt{1-h}\,dy$;
under LWA, $\sqrt{1\pm h}=1\pm\tfrac12h-\tfrac18h^2+\mathcal O(h^3)\approx1\pm\tfrac12h$, so
$\delta L_x=+\tfrac12hL_0$, $\delta L_y=-\tfrac12hL_0$.

| Source | Location | Role |
|---|---|---|
| MTW; Saulson; Maggiore | Traceability Pending | Primary supporting |
| Cahillane & Mansell (2021) | §2, Eqs. (8)–(10), pp. 2–3 (as recorded in Stage 1 §4.10.3): $\Delta L_x=h_+L_x/2$, $\Delta L_y=-h_+L_y/2$ | Independent confirmation of the per-arm factors |
| Stage 1 Lit. Validation, §4.10.6 | — | Same per-arm ½ already recorded as a derivation step |

**Assumptions:** TT gauge; fixed coordinate positions; LWA (so that $\sqrt{1\pm h}$ factors out of the integral); weak field. The ½ is the binomial coefficient, not an empirical loss factor.
**Conflict:** none (the ½ vs 1 apparent difference is resolved in Claim 7). **Status:** 🟡 VERIFIED WITH EXPLICIT ASSUMPTIONS. **Scope:** Core.
**Limitations:** first order in $h$; $-\tfrac18h^2L_0$ is the leading dropped term; $\mathcal O(h^2)\sim10^{-42}$ for $h\sim10^{-21}$.

### 4.7 Claim 7 — Differential combination

**Formulation:**
$\Delta L_\mathrm{arm}=(L_{x,0}-L_{y,0})+(\delta L_x-\delta L_y)=\big(+\tfrac12hL_0\big)-\big(-\tfrac12hL_0\big)=+1.0\,hL_0$.

| Source | Location | Role |
|---|---|---|
| MTW; Saulson; LIGO literature | Traceability Pending (Step 4 basis) | Primary supporting |
| Abbott et al. (2016) | §I, p. 3 (Stage 1 §4.10.3): $\Delta L=\delta L_x-\delta L_y=h(t)L$ | Direct |
| Cahillane & Mansell (2021) | §2, Eqs. (8)–(10), pp. 2–3: $\Delta L=h_+L$ | Direct |
| Thorne (1995, arXiv:gr-qc/9506086) | §3.1, Eq. (2): $\Delta L/L=F_+h_++F_\times h_\times\equiv h$ | Direct (confirmed against primary source in Stage 1) |
| Martynov et al. (2016) | §II, p. 3: $L=L_\parallel-L_\perp=h(f)L_0$ | Direct, frequency-domain form |

(All locators in this table are those recorded in Stage 1 Lit. Validation §4.10.3.)

**Assumptions:** equal nominal arms ($L_{x,0}=L_{y,0}$, so the static term cancels); orthogonal arms; aligned plus polarization; LWA; weak field.
**Conflict:** the factor ½ (single arm) vs 1 (differential) is a derivation step, not a conflict: the anti-symmetric traceless tensor makes the two arm contributions add. **Status:** 🟡 VERIFIED WITH EXPLICIT ASSUMPTIONS. **Scope:** Core.
**Limitations:** unequal arms leave a static offset $\Delta L_0=L_{x,0}-L_{y,0}$ (Schnupp asymmetry), which is a Stage 3/4 configuration item.

### 4.8 Claim 8 — Subtraction-order sign convention

**Formulation:** project convention $\Delta L_\mathrm{arm}\equiv L_x-L_y\Rightarrow+hL_0$; reversed order $\Delta L'\equiv L_y-L_x\Rightarrow-hL_0$.

| Source | Location | Role |
|---|---|---|
| Stage 1 Lit. Validation, Claim 1 | §4.1.2–4.1.3: Bond et al. §5.2 Eq. (5.10) p. 45; Martynov et al. §II p. 3; Abbott et al. §I p. 3 (all $L_x-L_y$ form); Dooley, Grote & van den Brand §2.1 p. 7 (reversed sign) | Convention comparison |
| Advanced LIGO review; GW150914 paper | Traceability Pending (Step 4 table) | Independent confirmation of $L_x-L_y$ form |

**Resolution:** a variable-definition choice. $|L_x-L_y|$ is invariant. Reversing the order changes only the overall sign of $\Delta L_\mathrm{arm}$ and hence of $\Delta\phi$. Stage 1 §14 establishes that the ideal scalar intensity is even in $\Delta\phi$, so the sign does not change the scalar intensity response. Any effect of the sign on field-level readout belongs to the later readout stage and is not claimed here.
**Status:** ⚠️ CONVENTION/DEFINITION DEPENDENT. **Scope:** Core (convention).
**Limitations:** the project convention must be used consistently across Stage 2, the interface, and code mapping.

### 4.9 Claim 9 — Long-Wavelength Approximation and $f^*$

**Formulation:** $\lambda_\mathrm{GW}\gg L_0\iff f_\mathrm{gw}\ll f^*\equiv c/(2\pi L_0)$. Physical condition: $f\ll f^*$. **Project-adopted operational criterion:** $f\le0.1f^*$.

| Source | Location | Role |
|---|---|---|
| MTW; Maggiore | Traceability Pending | Primary supporting (LWA definition) |
| Stage 1 Lit. Validation | §4.10.4, §5.4 (LWA required for strain-to-length coupling; confirmed against Thorne 1995; $f_*\sim12$ kHz for 4 km arms) | Independent confirmation |
| Einstein Telescope review | Traceability Pending | Supplementary (frequency scale) |
| LEGWORK | Traceability Pending | Supplementary only (software package, not a primary reference) |

**Conflict:** $f\ll f^*$ is the physical condition; $0.1f^*$ is a project engineering threshold and is not claimed as a literature value.
**Status:** ✅ VERIFIED for the definition and the physical condition; the $0.1f^*$ threshold is a project-adopted criterion outside literature validation. **Scope:** Core (validity boundary).
**Limitations:** per Stage 1 §5.4, the LWA is not needed for the purely optical phase relation; it is required here, for strain → arm length.

### 4.10 Claim 10 — Free spectral range and finite-arm response

**Formulation:** $f_\mathrm{FSR}=c/(2L_0)=\pi f^*$ (location of the first null, $\sin(\omega L_0/c)=0$);
finite-arm (no-cavity) response $C(f)=\mathrm{sinc}(\omega L_0/c)\,e^{-i\omega L_0/c}$, $\mathrm{sinc}(x)=\sin x/x$.

| Source | Location | Role |
|---|---|---|
| Advanced LIGO review | Eq. (A9) (as cited in Step 4) | Primary supporting for $C(f)$ |
| Advanced LIGO review; Schutz | Traceability Pending (other locators) | Supporting for $f_\mathrm{FSR}$ |
| Dooley et al.; Cahillane & Mansell | As flagged in Stage 1 §6.4 | LWA breakdown at high frequency |

**Assumptions:** simple Michelson, no cavities. **Terminology:** this document calls $C(f)$ the *finite-arm response*, not "single-pass", to avoid confusion with the round-trip factor of 2 in Stage 1.
**Status:** 🟡 VERIFIED WITH EXPLICIT ASSUMPTIONS. **Scope:** Boundary. **Limitations:** not included in the Stage 2 baseline; applies when $f\gtrsim0.1f^*$.

### 4.11 Claim 11 — Cavity pole

**Formulation:** $f_p=\dfrac{c}{4\pi L_0}\dfrac{1-r_1r_2}{\sqrt{r_1r_2}}$. With $c/(4\pi L_0)=f^*/2$, $r_2\approx1$, $r_1\approx1-T_\mathrm{ITM}/2$: $1-r_1r_2\approx T_\mathrm{ITM}/2$, so

$$f_p\approx\frac{f^*T_\mathrm{ITM}}{4}.$$

Illustrative evaluation (4 km, $T_\mathrm{ITM}=0.014$, $f^*=11{,}928.6$ Hz): $f_p\approx41.75\approx42$ Hz.

| Source | Location | Role |
|---|---|---|
| Advanced LIGO review; Advanced LIGO sensitivity paper | Traceability Pending (identified by short name in Step 4) | Primary supporting |

**Correction recorded:** earlier draft notes gave $f_p\approx(f^*/2)T_\mathrm{ITM}$ (about 83.5 Hz), which omitted the ½ from $1-r_1\approx T_\mathrm{ITM}/2$. That value is $2f_p$, the full width at half maximum. The earlier "80–350 Hz" range was attributed in the project cross-check to FWHM values or to signal-recycling-coupled bandwidths; **that attribution is not source-confirmed (Traceability Pending)** and the range is removed. The $T_\mathrm{ITM}=0.014$ value is the project cross-check's illustrative figure (Traceability Pending). $f_p$ is the half-width (pole) frequency, not the full linewidth.
**Status:** 🟡 VERIFIED WITH EXPLICIT ASSUMPTIONS (the $f^*T/4$ form needs $r_2\approx1$ and small $T$). **Scope:** Extension (Stage 3). **Limitations:** excluded from the Stage 2 baseline.

### 4.12 Claim 12 — Stage 2 → Stage 1 interface and factor-of-2 audit

**Formulation:** $\Delta\phi=\dfrac{4\pi}{\lambda_0}\Delta L_\mathrm{arm}=2k_0\Delta L_\mathrm{arm}\Rightarrow\Delta\phi(t)=\dfrac{4\pi L_0}{\lambda_0}h(t)$.
Per-arm: $\delta\phi_x=+\dfrac{2\pi L_0}{\lambda_0}h$, $\delta\phi_y=-\dfrac{2\pi L_0}{\lambda_0}h$, so $\delta\phi_x-\delta\phi_y=\dfrac{4\pi L_0}{\lambda_0}h$.
Numerical example (Document 1 values): for 4 km and 1064 nm the static gain is about $4.72\times10^{10}$ rad per unit strain; $h=10^{-21}$ gives about $4.72\times10^{-11}$ rad.

| Source | Location | Role |
|---|---|---|
| Stage 1 Lit. Validation, Claim 3 | §4.3.2–4.3.3: Dooley et al. §2.1 Eq. (3) p. 8; Bond et al. §5.2 Eq. (5.12) p. 46; Thorne (1995) §3.1 Eq. (2), §3.5 Eq. (4); Jaranowski & Królak §2.2 p. 7; Cahillane & Mansell App. A.1 Eq. (A5) p. 24 | Primary supporting (cited, not re-derived) |
| Stage 1 Lit. Validation, Claim 10 | §4.10 | Strain-to-length input |

**Factor-of-2 audit:** ½ per arm (binomial) → ½−(−½)=1 at the differential (anti-symmetry) → 2 from the optical round trip, in $\Delta\phi=2k_0\Delta L_\mathrm{arm}$ (Stage 1 §5, round-trip origin). No factor is missing or double-counted across the interface.
**Assumptions:** monochromatic light; static-arm optics at the instant of light return (valid inside the LWA regime).
**Status:** 🟡 VERIFIED WITH EXPLICIT ASSUMPTIONS. **Scope:** Core (interface).

---

## 5. Assumption Classification and Relaxation Map

### 5.1 Inventory

Eleven assumptions/conventions plus two boundary definitions (the earlier draft's "8 assumptions" is superseded by the Step 5 inventory).

| # | Assumption / convention | Class |
|---|---|---|
| 1 | Weak-field linearization, $|h_{\mu\nu}|\ll1$ | Physically required approximation |
| 2 | TT gauge | Coordinate/gauge choice |
| 3 | Normal propagation ($\theta=0$, $\hat k=\hat z$) | Special-case geometric choice |
| 4 | Aligned plus polarization ($\phi=\psi=0$, $h_\times=0$) | Special-case geometric choice |
| 5 | Perpendicular arms ($\zeta=90^\circ$) | Detector configuration choice |
| 6 | Equal nominal arms ($L_{x,0}=L_{y,0}=L_0$) | Detector configuration choice |
| 7 | Long-Wavelength Approximation, $f\ll f^*$ | Physically required approximation |
| 8 | Operational limit $f\le0.1f^*$ | Project-adopted criterion |
| 9 | Subtraction order $\Delta L_\mathrm{arm}\equiv L_x-L_y$ | Notation/convention |
| 10 | Detector-tensor normalization $d^{ij}=\tfrac12(\cdot)$ | Notation/convention |
| 11 | Scalar shorthand $h(t)$ | Notation/convention |
| 12 | Neglected finite-arm and cavity damping | Model boundary definition |
| 13 | Neglected readout and asymmetry offsets | Model boundary definition |

### 5.2 Mathematical role and consequence if relaxed

| Assumption | Entry point | Consequence if relaxed |
|---|---|---|
| Weak field | $g_{\mu\nu}$ expansion; $\sqrt{1\pm h}$ | Retain $\mathcal O(h^2)$ terms |
| TT gauge | Proper-length line integrals | Test-mass coordinates move in non-TT frames |
| $\theta=0$, aligned polarization, $\zeta=90^\circ$ | $d^{ij}h_{ij}^\mathrm{TT}$ | Antenna-pattern projection $F_+h_++F_\times h_\times$; opening factor $\sin\zeta$ |
| Equal arms | Static background subtraction | Static offset $\Delta L_0=L_{x,0}-L_{y,0}$ |
| LWA | $\int\sqrt{1\pm h(t,x)}\,dx$ | Finite-arm factor $C(f)$ |

### 5.3 Relaxation map

| Baseline assumption | Relaxed condition | General response |
|---|---|---|
| Weak field | Strong field | Higher-order terms |
| LWA | $f\sim f^*$ | $\Delta L_\mathrm{eff}(f)=L_0\,h(f)\,\mathrm{sinc}(\omega L_0/c)e^{-i\omega L_0/c}$ |
| $\theta=0$ | Arbitrary sky position | $F_+(\theta,\phi,\psi)$, $F_\times(\theta,\phi,\psi)$ |
| Plus polarization | Arbitrary polarization | $h_\mathrm{det}=F_+h_++F_\times h_\times$ |
| Orthogonal arms | $\zeta=60^\circ$ | $\Delta L=\sin\zeta\,hL_0=\tfrac{\sqrt3}{2}hL_0$ (Stage 3 configuration extension) |
| Equal arms | Asymmetry | Static offset $\Delta L_0$ added to the dynamic response |

---

## 6. Validity Domain and Frequency Hierarchy

### 6.1 Validity domain

$\Delta L_\mathrm{arm}(t)=h(t)L_0$ holds to first order in $h$ when all four boundaries are respected together:

1. $|h|\ll1$.
2. $f_\mathrm{gw}\ll f^*$ (operationally $f\le0.1f^*$).
3. Overhead incidence with aligned plus polarization.
4. Orthogonal arms with equal nominal lengths.

### 6.2 Two-layer frequency hierarchy

| Layer | Scale | Formula | Role |
|---|---|---|---|
| 1 — metric / finite-arm | Arm transfer frequency $f^*$ | $c/(2\pi L_0)$ | Upper bound of LWA validity |
| 1 — metric / finite-arm | Free spectral range $f_\mathrm{FSR}$ | $c/(2L_0)=\pi f^*$ | First null of the finite-arm response |
| 2 — resonant cavity (Stage 3) | Cavity pole $f_p$ | $\dfrac{c}{4\pi L_0}\dfrac{1-r_1r_2}{\sqrt{r_1r_2}}\approx\dfrac{f^*T_\mathrm{ITM}}{4}$ | Storage-time bandwidth; excluded from Stage 2 |

### 6.3 Numerical limits

| Detector | $L_0$ | $f^*$ | $0.1f^*$ | $f_\mathrm{FSR}$ |
|---|---|---|---|---|
| Advanced LIGO | 4 km | 11.93 kHz | ≈ 1.19 kHz | 37.5 kHz |
| Einstein Telescope | 10 km | 4.77 kHz | ≈ 477 Hz | 15.0 kHz |
| Table-top code | 1 m | 47.71 MHz | ≈ 4.77 MHz | 150 MHz |

(Step 4 and 5 round the 4 km $0.1f^*$ value to 1.20 kHz; $0.1\times11.93$ kHz is 1.19 kHz, used here.)

**Code operating point (as stated in Step 5):** $L_0=1$ m at $f_\mathrm{gw}=100$ Hz gives $f/f^*\approx2.1\times10^{-6}$, and the finite-arm error $1-\mathrm{sinc}(x)\approx x^2/6\approx7.3\times10^{-13}$, i.e. deep inside the LWA domain. This is an analytical statement only; checking that the repository actually uses these values is Document 3.

---

## 7. Apparent Conflicts and Their Resolution

### 7.1 Sign convention
$L_x-L_y$ vs $L_y-L_x$: sign convention (Claim 8, Stage 1 Claim 1). Not a contradiction.

### 7.2 Factor of 2
Three distinct factors (½ per arm; 1 at the differential; 2 from the round trip) are kept separate (Claim 12). Not a contradiction.

### 7.3 LWA vs optical phase
The LWA is required for strain → arm length (Claims 6, 7, 9) and not for the optical phase relation (Stage 1 §5.4, Document 1). Scope boundary, correctly separated.

### 7.4 Incident vs detector-projected strain
$h_+$ is the incident mode; $h_\mathrm{det}=F_+h_++F_\times h_\times$ is the detector-projected strain. They coincide only at the aligned geometry (Claims 4, 5).

### 7.5 Frequency-scale nomenclature
$f^*$, $f_\mathrm{FSR}$ and $f_p$ are distinct quantities in two physical layers (§6.2), related by $f_\mathrm{FSR}=\pi f^*$ and $f_p\approx f^*T/4$.

### 7.6 Research-history corrections

1. **Closure wording.** Earlier packages state the result as "exact … 100% verified … without unresolved analytical gaps". The result is first order in $h$ and conditional on the LWA, so §9 uses "valid to first order in $h$ under the stated conditions".
2. **Mixed condition.** The earlier "if and only if" mixed the physical LWA condition with the project threshold $0.1f^*$; they are now stated separately.
3. **Assumption count.** 8 (draft) → 11 plus 2 boundary definitions (Step 5).
4. **Cavity pole.** $f^*T/4$ replaces $f^*T/2$; the 80–350 Hz range is removed (Claim 11).
5. **LEGWORK demoted** to supplementary only.
6. **Fifth status label** ("derived") mapped into the Stage 1 tiers (§3.3).
7. **Sign-convention wording.** Step 4's statements that the reversed sign is "absorbed into DC readout calibration" and that Dooley's field goes as $\cos(k\Delta L)$ are not carried forward; they are not supported by the Stage 1 record. Only the Stage 1 result (scalar intensity unaffected) is used.
8. **"Single-pass" label** for $C(f)$ replaced by "finite-arm response".
9. **Rounding.** 4 km $0.1f^*$: 1.20 kHz → 1.19 kHz.

### 7.7 Overall
No genuine physical or mathematical contradiction was identified among the sources and packages examined. This is a statement about those materials, not about all possible GW-detector literature.

---

## 8. Stage Boundaries and Handoff

### 8.1 Excluded from Stage 2 (belongs to later stages)

- Finite-arm response $C(f)$ when $f\gtrsim0.1f^*$ (boundary; used only as the stated limit of validity).
- Fabry–Pérot cavity storage $K_-(f)\approx1/(1+if/f_p)$ and $f_p$ (Stage 3).
- Power/signal recycling, detuning, Schnupp asymmetry transfer functions (Stage 3).
- Readout and photodetector response: DC offsets, homodyne beating, output mode cleaner, photodiode electronics (Stage 4).
- Non-orthogonal / triangular geometries ($\sqrt3/2$ factor, Einstein Telescope) (Stage 3 configuration extension).
- Detector-network statistics, Fisher-matrix estimation (Stage 4 data analysis).

### 8.2 Four-level response hierarchy (for orientation only)

$\Delta L_\mathrm{arm}=hL_0$ (Level 1, $f\ll f^*$) → finite-arm $C(f)$ (Level 2) → Fabry–Pérot $H_\mathrm{FP}(f)$ (Level 3) → dual-recycled $H_\mathrm{DR}(f)$ (Level 4). Only Level 1 is the Stage 2 baseline.

### 8.3 Handoff to Document 3

Document 3 should check: the sign convention ($x$-arm minus $y$-arm) in the code; whether $h\to\Delta L$ uses $hL_0$ and not $\tfrac12hL_0$; whether the interface to the phase uses $4\pi/\lambda_0$; that the sinusoidal toy $h(t)$ operates inside the LWA domain; and that the static assumptions of §6.1 are respected. This document does not perform that check.

---

## 9. Literature Validation Results

### 9.1 Claim status summary (canonical)

| Claim | Formulation | Status | Scope |
|---|---|---|---|
| 1 | $g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu}$ | VERIFIED | Core |
| 2 | TT gauge, coordinate fixity | VERIFIED | Core |
| 3 | $h_+,h_\times$ tensor modes | VERIFIED | Core |
| 4 | $d^{ij}$, $F_+=1$, $F_\times=0$ | VERIFIED WITH EXPLICIT ASSUMPTIONS | Core |
| 5 | Scalar $h(t)$ | VERIFIED WITH EXPLICIT ASSUMPTIONS | Core (conditional) |
| 6 | $\delta L_{x,y}=\pm\tfrac12hL_0$ | VERIFIED WITH EXPLICIT ASSUMPTIONS | Core |
| 7 | $\Delta L_\mathrm{arm}=hL_0$ | VERIFIED WITH EXPLICIT ASSUMPTIONS | Core |
| 8 | Subtraction order | CONVENTION/DEFINITION DEPENDENT | Core (convention) |
| 9 | LWA and $f^*$ | VERIFIED | Core (validity boundary) |
| 10 | $f_\mathrm{FSR}$, $C(f)$ | VERIFIED WITH EXPLICIT ASSUMPTIONS | Boundary |
| 11 | $f_p$ | VERIFIED WITH EXPLICIT ASSUMPTIONS | Extension (Stage 3) |
| 12 | $\Delta\phi=(4\pi L_0/\lambda_0)h$ | VERIFIED WITH EXPLICIT ASSUMPTIONS | Core (interface) |

### 9.2 Groupings

- **Fully supported:** Claims 1, 2, 3, 9.
- **Require explicit assumptions:** Claims 4, 5, 6, 7, 10, 11, 12.
- **Convention-dependent:** Claim 8.
- **Moved to extensions / boundary:** Claim 11 (Stage 3); Claim 10 (boundary).
- **Traceability Pending:** all general-textbook references listed in §10.2.

### 9.3 Closure statement

> The relationship $\Delta L_\mathrm{arm}(t)=L_x(t)-L_y(t)=h(t)L_0$ is the proper-distance response of an interferometric gravitational-wave detector in the linearized Transverse-Traceless gauge, **valid to first order in $h$** and only when: the Long-Wavelength Approximation holds ($f_\mathrm{gw}\ll f^*=c/(2\pi L_0)$; the project operational criterion is $f_\mathrm{gw}\le0.1f^*$); the field is weak ($|h|\ll1$); the wave is overhead and plus-polarized ($\theta=\phi=\psi=0$, $h_\times=0$); and the detector has orthogonal arms of equal nominal length ($L_{x,0}=L_{y,0}=L_0$). The individual-arm factors of ½, the anti-symmetric sign mechanics, the frequency scales, and the Stage 2 → Stage 1 phase factor $\Delta\phi=(4\pi L_0/\lambda_0)h$ are consistent with the literature examined, with no factor of 2 missing or double-counted. Textbook-level references without explicit locators remain Traceability Pending.

**Result:** the Stage 2 strain-to-arm-response model is literature-supported under its stated assumptions. This document is the reference for Document 3 (code and physics-mapping audit).

---

## 10. Limitations of the Validation

### 10.1 Scope
Validates the idealized, static, linearized, aligned-geometry model. It does not validate a real detector, the sinusoidal toy model in the repository, or any code.

### 10.2 Traceability
The following were taken from the Step 4 / Step 5 packages without section, page, or equation locators and are **Traceability Pending**: MTW; Maggiore; Schutz; Saulson; the Advanced LIGO review (other than Eq. (A9)); the Advanced LIGO sensitivity paper; the Einstein Telescope design study; the GW150914 reference as cited in Step 4's sign table; LEGWORK (supplementary only); the $T_\mathrm{ITM}=0.014$ value and the origin of the "80–350 Hz" quotes. Locators taken from Stage 1 are reused as recorded there and are not re-verified in this document.

### 10.3 Source selection
No formal source-selection document exists. Sources were taken from the uploaded packages and the Stage 1 record.

### 10.4 Convention reconciliation
Resolves only the conventions encountered (subtraction order, half-vs-full difference inherited from Stage 1, detector-tensor normalization). It does not establish equivalence for every convention in the wider literature.

### 10.5 Derived vs literature-supported
Claims 6 and 7 are derived from literature-supported results as well as supported directly; readers needing excerpt-level traceability should consult the primary documents.

---

## 11. References

### 11.1 Cited with locators (as recorded in the Stage 1 literature-validation record)

1. Abbott, B. P., et al. (LIGO Scientific Collaboration and Virgo Collaboration) (2016). *Observation of Gravitational Waves from a Binary Black Hole Merger.* Phys. Rev. Lett. 116, 061102. arXiv:1602.03838.
2. Cahillane, C., & Mansell, G. (2021). *Review of the Advanced LIGO gravitational wave observatories leading to observing run four.* LIGO-P2100298.
3. Thorne, K. S. (1995). *Gravitational Waves.* arXiv:gr-qc/9506086.
4. Martynov, D. V., et al. (2016). *The Sensitivity of the Advanced LIGO Detectors at the Beginning of Gravitational Wave Astronomy.* Phys. Rev. D 93, 112004. arXiv:1604.00439.
5. Bond, C., Brown, D., Freise, A., & Strain, K. A. (2016/2017). *Interferometer techniques for gravitational-wave detection.* Living Rev. Relativ. 19, 3.
6. Dooley, K. L., Grote, H., & van den Brand, J. (2021). *Terrestrial Laser Interferometers.* arXiv:2103.01740.
7. Jaranowski, P., & Królak, A. (2012). *GW data analysis and formalism.* Living Reviews.

### 11.2 Referenced by short name in Step 4/5 (full bibliographic entries and locators Traceability Pending)

8. Misner, Thorne & Wheeler (MTW), *Gravitation*.
9. Maggiore, M., *Gravitational Waves*, Vol. 1.
10. Saulson, P. R., *Fundamentals of Interferometric Gravitational Wave Detectors*.
11. Schutz, B. F. (detector-response / antenna-pattern treatment).
12. Advanced LIGO review (Eq. (A9) for $C(f)$).
13. Einstein Telescope design study.
14. LEGWORK (supplementary only).

---

*End of document. This literature-validation record is the reference for the Stage 2 code and physics-mapping audit (Document 3).*
