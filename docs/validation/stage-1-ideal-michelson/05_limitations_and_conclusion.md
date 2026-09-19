# Phase 1 Limitations and Conclusion — Ideal Michelson Interferometer

**Status:** Complete. This is the closing document of the Phase 1 record. It
synthesizes the findings of `analytical_model.md`, `literature_validation.md`,
`code_and_simulation_audit.md`, and `numerical_validation.md`; it does not
re-derive, re-validate, re-audit, or re-test anything already established in
those four documents. Each is cited by section, not restated.

---

## 1. Purpose and Scope

### 1.1 Purpose

Each of the four preceding documents already states its own limitations,
scoped to its own question:

| Document | Question it answers | Its own limitations section |
|---|---|---|
| `analytical_model.md` | What physics was derived? | §19 |
| `literature_validation.md` | What supports it? | §8 |
| `code_and_simulation_audit.md` | Is it implemented? | §1.3, §5.6, §9 |
| `numerical_validation.md` | Is it reproduced? | §9 |

None of them answers the fifth question the Master Plan assigns to this
document specifically: **what can we conclude, and where does Phase 1
stop?** That requires synthesizing across all four, which is this
document's sole purpose.

### 1.2 Out of scope

This document does not introduce new physics, new literature evidence, new
code changes, or new numerical tests. Where a limitation is already fully
covered in one of the four documents, this document points to it rather
than repeating it.

---

## 2. Combined Validation Status

The project's governing principle is:

$$
\boxed{\text{implemented}\neq\text{validated}\neq\text{physically justified}}
$$

With all four documents now complete, this section states, for the first
time in one place, which of the three legs holds for each part of the
Phase 1 model.

| Phase 1 element | Physically justified | Implemented | Numerically validated |
|---|---|---|---|
| Bright-port scalar chain ($\Delta L_\mathrm{arm}=L_x-L_y$, $\Delta L_\mathrm{rt}=2\Delta L_\mathrm{arm}$, $\Delta\phi=4\pi\Delta L_\mathrm{arm}/\lambda$, $I_\mathrm{bright}$) | Yes — `literature_validation.md` Claims 1, 2, 3, 6 (§7.1–§7.4) | Yes — `code_and_simulation_audit.md` §5.1–§5.3, §5.5 (Category A) | Yes — `numerical_validation.md` T1–T5, T8, T9 (§4, §10.1) |
| Beamsplitter matrix, field recombination, dark-port response | Yes — `literature_validation.md` Claims 4, 5, 7 (§7.1–§7.4) | **No** — `code_and_simulation_audit.md` §5.4, §5.6 (Category B) | Yes, against an independent reference model, not repository code — `numerical_validation.md` T10–T13, §6.2, §10.2 |
| GW strain-to-length coupling ($\Delta L_\mathrm{arm}(t)=h(t)L_0$) | Yes, under explicit assumptions — `literature_validation.md` Claim 10 (§7.1) | Present as Stage 2 code, deliberately not audited as Phase 1 — `code_and_simulation_audit.md` §6.2, §8 | Deliberately not tested — `numerical_validation.md` §1.2, §8 |

All three legs hold together for the bright-port scalar chain. For the
dark-port/field-level result, two legs hold and "implemented" does not —
this is a scope limitation, not a discrepancy, per Category B in
`code_and_simulation_audit.md` §11.2 and the Scope Limitations in
`numerical_validation.md` §10.2. The GW-coupling row is the Phase 1/Phase 2
interface addressed in Section 3 below, and its incomplete row is the
correct, deliberate handoff state rather than a gap.

No row shows a genuine discrepancy (Category C) anywhere in the evidence
chain — `code_and_simulation_audit.md` §11.3 and `numerical_validation.md`
§10.3 both record none.

---

## 3. Phase 1 / Phase 2 Boundary

Four separate boundary statements already exist. This section reconciles
them into one canonical statement for Phase 2 to build from.

* **Derivation's view** (`analytical_model.md` §16): the optical model
  (Sections 2–15) is conceptually independent of the strain-to-length
  relation; the two combine only as
  $h(t)\rightarrow\Delta L_\mathrm{arm}(t)\rightarrow\Delta L_\mathrm{rt}(t)\rightarrow\Delta\phi(t)\rightarrow I_\mathrm{bright/dark}(t)$,
  of which Phase 1 establishes only the
  $\Delta L_\mathrm{arm}\rightarrow I_\mathrm{bright/dark}$ portion.
* **Literature's view** (`literature_validation.md` §6): Claim 10
  ($\Delta L_\mathrm{arm}(t)=h(t)L_0$) is retained only as the interface to
  the GW-response stage, not as a tenth core optical result.
* **Implementation's view** (`code_and_simulation_audit.md` §8): Stage 2
  code (`src/gravitational_wave.py`,
  `simulations/gravitational_wave_injection.py`) already exists in the
  repository but is classified, not evaluated, by this Phase 1 audit.
* **Testing's view** (`numerical_validation.md` §1.2, §8): GW strain
  coupling is explicitly excluded from the T1–T13 suite.

**Canonical statement:** Phase 1 ends at, and does not cross, the relation
$\Delta L_\mathrm{arm}(t)=h(t)L_0$. Everything on the $\Delta L_\mathrm{arm}\rightarrow I$
side of that relation is derived, literature-supported, and (for the
bright-port path) implemented and numerically validated. Everything on the
$h(t)\rightarrow\Delta L_\mathrm{arm}(t)$ side — including the Stage 2 code
already present in the repository — is explicitly Phase 2's responsibility
to evaluate, not Phase 1's.

---

## 4. Frozen Conventions Carried Forward to Phase 2

Resolved in `literature_validation.md` §5 and fixed in `analytical_model.md`
§3, §7, §17; Phase 2 work must keep these conventions unless a documented
justification is given for changing them (`analytical_model.md` §17.1):

1. **Full-difference arm length:** $\Delta L_\mathrm{arm}=L_x-L_y$, not the
   half-difference $(L_x-L_y)/2$ convention used by some cited sources
   (`literature_validation.md` §5.1).
2. **Symmetric beamsplitter phase convention:** $\varphi_t=\pi/2$,
   $\varphi_r=0$, giving
   $B=\frac{1}{\sqrt2}\begin{pmatrix}1&i\\i&1\end{pmatrix}$, not the
   Fresnel $\pm1$ convention (`literature_validation.md` §5.3).
3. **Port labeling under that convention:** the port varying as
   $\sin(\Delta\phi/2)$ is dark/antisymmetric; the port varying as
   $\cos(\Delta\phi/2)$ is bright/symmetric (`literature_validation.md`
   §5.2; `analytical_model.md` §8.4).
4. **One-way arm-length convention:** $L_x,L_y$ are one-way distances from
   beamsplitter to end mirror; the round-trip factor of 2 is applied
   explicitly, never folded into a redefined "arm length"
   (`analytical_model.md` §18).
5. **Reciprocal-beamsplitter assumption:** the same matrix $B$ is used for
   both the initial split and the recombination pass
   (`analytical_model.md` §7.2, §18).

---

## 5. Limitations (by reference)

Each of the following is fully documented in its originating section and is
not repeated here:

* **Physical idealizations of the model itself** — monochromatic input,
  lossless beamsplitter, perfect mirrors, no optical loss, static arm
  lengths in the core derivation, single spatial mode, scalar polarization,
  vacuum second input port: `analytical_model.md` §18–§19.
* **Evidence-gathering limitations** — source availability, search
  methodology, source-selection documentation, bibliographic completeness,
  limits of convention reconciliation, scope of the validated result,
  evidence-traceability: `literature_validation.md` §8.
* **Implementation scope limitations** — dark port and field-level model
  not implemented; Stages 3, 8, 9 have no repository code; no automated
  regression suite; no version-control metadata in the supplied archive:
  `code_and_simulation_audit.md` §4.1, §5.4, §5.6, §9, §11.2.
* **Testing scope limitations** — no coverage of optical losses, beam
  imperfections, physical noise, GW strain coupling, polarization/antenna
  response, operating-point control, PSD/ASD, sensitivity, matched
  filtering, or experimental data: `numerical_validation.md` §9.

One item spans two documents and is worth stating once, here: both
`code_and_simulation_audit.md` §4.1 and `numerical_validation.md` §12 note
the absence of a commit hash for the audited/tested repository state. Per
the agreed workflow, this document, together with the other four, is to be
captured in a single Phase 1 closing commit; §7 below will be updated with
that hash once it exists, and the other two documents' own traceability
sections should be updated at the same time.

---

## 6. What Phase 1 Establishes

* The complete ideal two-arm Michelson optical model — differential arm
  length, round-trip optical path, differential phase, the beamsplitter
  transformation, field-level recombination, bright- and dark-port
  intensity, interference conditions, periodicity, and symmetry — is
  independently derived, literature-supported, and numerically validated in
  its entirety.
* The bright-port scalar path of that model is implemented in
  `src/interferometer.py` and numerically reproduces the analytical
  predictions with no genuine discrepancy.
* The dark-port and field-level portion of the model is physically
  justified and numerically validated through an independently constructed
  reference model, though not implemented in the repository.
* No genuine physics discrepancy was identified anywhere in the evidence
  chain — derivation, literature, implementation, or numerical test.

## 7. What Phase 1 Does Not Establish

* Whether the dark-port response should be implemented in the repository —
  a design decision outside this project's remit at this stage, not a
  physics question.
* Any Stage 2–9 physics: GW strain coupling, polarization and antenna
  response, operating-point linearization, physical detector noise,
  PSD/ASD and sensitivity, signal recovery/SNR, public-data validation, or
  the integrated detector model.
* Behavior under realistic optical losses, beam imperfections, or quantum
  noise.
* Agreement with real interferometer or gravitational-wave detector data.

---

## 8. Final Phase 1 Status Verdict

$$
\boxed{\text{PHASE 1 — CLOSED}}
$$

The bright-port scalar implementation is validated against the frozen
analytical model with no code modification required. The dark-port and
field-level result is analytically and numerically established but not
implemented, which is recorded as a scope status for any future decision to
extend the repository — not as an open item blocking Phase 1 closure. No
genuine discrepancy exists anywhere in the four-document evidence chain.

Phase 1 is closed and provides the frozen physics baseline
(`analytical_model.md` §17) on which Phase 2 work is to be built, subject to
the boundary in Section 3 and the conventions in Section 4 above.

---

## 9. Document Index and Traceability

| Document | Question | Status |
|---|---|---|
| `analytical_model.md` | What physics was derived? | Complete |
| `literature_validation.md` | What supports it? | Complete |
| `code_and_simulation_audit.md` | Is it implemented? | Complete |
| `numerical_validation.md` | Is it reproduced? | Complete |
| `limitations_and_conclusion.md` (this document) | What can we conclude, and where does it stop? | Complete |
| `README.md` | Final status and navigation | Pending update — the old 8-phase roadmap, including the tabletop interferometer and LISA/space-detector items, is deprecated in favor of the Stage 1–9 Master Plan and has not yet been edited in the repository. That update is outside this document's scope. |

**Repository:** `gravitational-wave-detector-research-main`.
**Commit hash:** not yet available — see Section 5; to be recorded here
once the single Phase 1 closing commit is made.

---

## 10. Handoff to Phase 2

Phase 2 begins from the frozen baseline in `analytical_model.md` §17 and
the boundary stated in Section 3 above, and is expected to establish the
physical justification, implementation, and numerical validation of
$\Delta L_\mathrm{arm}(t)=h(t)L_0$ and its generalization
$h_\mathrm{det}(t)=F_+h_+(t)+F_\times h_\times(t)$
(`analytical_model.md` §16), using the same four-stage evidence chain —
analytical derivation, literature validation, code and simulation audit,
numerical validation — that produced this Phase 1 record, and closing with
its own limitations-and-conclusion document in the same form as this one.
