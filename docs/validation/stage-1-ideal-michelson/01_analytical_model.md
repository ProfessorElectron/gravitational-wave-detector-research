# Analytical Model — Ideal Michelson Interferometer (Phase 1)

**Status:** Phase 1 optical derivation complete, including the field-level
beamsplitter treatment. Numerical validation of this derivation is
documented separately in `numerical_validation.md` (tests T10–T13).

## 1. Purpose and scope

This document establishes the analytical model of the ideal two-arm Michelson
interferometer used as the **Phase 1 physics baseline** for the
gravitational-wave detector research project.

The model is established independently of the repository implementation. It
provides the analytical reference against which subsequent literature
validation, code comparison, and numerical validation are performed.

This document answers two distinct questions together: **what physics was
derived** (the derivation chain in Sections 2, 4–17), and **under what
definitions, conventions, and assumptions it is valid** (Section 3,
Section 7.2, and Section 18). The latter is not a separate appendix — it is
load-bearing: every boxed result in this document holds only under the
definitions fixed in Section 3 and the idealizations listed in Section 18,
and should be read together with them rather than in isolation.

The primary Phase 1 model describes the optical response of a minimal ideal
two-arm Michelson interferometer. A simplified gravitational-wave
strain-to-arm-length relation is included separately only as a boundary to
the subsequent gravitational-wave response stages.

The central analytical chain is

$$
L_x,L_y
\rightarrow
\Delta L_\mathrm{arm}
\rightarrow
\Delta L_\mathrm{rt}
\rightarrow
\Delta\phi
\rightarrow
\text{field recombination}
\rightarrow
I_\mathrm{bright},I_\mathrm{dark}.
$$

The analytical model is intended to be the independent physics reference for
the subsequent validation stages.

### 1.1 Phase 1 scope

The Phase 1 model establishes:

* ideal two-arm Michelson geometry;
* physical differential arm length;
* round-trip optical path difference;
* differential optical phase;
* the beamsplitter/output-port convention, at the field level;
* field-level recombination;
* ideal bright-port and dark-port intensity;
* constructive and destructive interference conditions;
* differential-arm-length periodicity;
* symmetry of the ideal scalar intensity response.

### 1.2 Outside the Phase 1 optical model

The following are not developed as part of the core Phase 1 optical
derivation:

* Fabry–Pérot arm cavities;
* power recycling;
* signal recycling;
* realistic detector operating-point control;
* physical detector noise;
* PSD/ASD modelling;
* detector sensitivity;
* general antenna-pattern response;
* advanced detector optical response;
* realistic optical losses;
* beam imperfections or mode mismatch;
* calibration.

The physical derivation of how a gravitational-wave strain produces
differential arm displacement belongs to the subsequent GW-response stages.

---

## 2. Physical system being modeled

The system considered here is a minimal ideal two-arm Michelson
interferometer.

Conceptually:

$$
\text{Input laser}
\rightarrow
\text{50:50 beamsplitter}
\rightarrow
\begin{cases}
\text{x arm}\\
\text{y arm}
\end{cases}
$$

The fields propagate to the respective end mirrors, return to the
beamsplitter, and recombine at the output ports.

The physical one-way arm lengths are defined as

$$
L_x = \text{one-way physical length of the x arm},
$$

$$
L_y = \text{one-way physical length of the y arm}.
$$

The model explicitly distinguishes these physical one-way lengths from the
optical path accumulated during the round trip.

The arms are treated as ideal within the scope defined above.

---

## 3. Variables and conventions

The following conventions are fixed throughout Phase 1.

| Symbol | Meaning | Convention |
| ----------------------- | ------------------------------------------------ | ----------------------- |
| $L_x$ | x-arm one-way physical length | positive |
| $L_y$ | y-arm one-way physical length | positive |
| $\Delta L_\mathrm{arm}$ | differential one-way arm length | signed full difference |
| $\Delta L_\mathrm{rt}$ | differential round-trip optical path difference | signed |
| $\lambda$ | optical wavelength | positive |
| $k$ | optical wavenumber | $k=2\pi/\lambda$ |
| $\Delta\phi$ | differential optical phase | signed |
| $I_0$ | reference/input intensity or power normalization | non-negative |

### 3.1 Full-difference convention

This project uses the **full-difference convention**

$$
\boxed{\Delta L_\mathrm{arm}=L_x-L_y}.
$$

Thus:

* $\Delta L_\mathrm{arm}>0$: the x arm is longer;
* $\Delta L_\mathrm{arm}<0$: the y arm is longer;
* $\Delta L_\mathrm{arm}=0$: the arms have equal nominal length.

Some literature uses a half-difference convention such as

$$
\Delta L=\frac{L_x-L_y}{2}.
$$

That is a different definition of the same physical arm imbalance. It must
not be silently substituted for the project definition.

The factor-of-two distinction is therefore kept explicit throughout the
analytical model.

---

## 4. Differential arm length

Physically, an ideal Michelson interferometer is sensitive only to the
*imbalance* between its two arms, not to their absolute lengths: if both arms
changed length by the same amount, no interference effect would result. The
differential arm length is defined to isolate exactly this imbalance.

The physical differential arm length is defined by

$$
\boxed{\Delta L_\mathrm{arm}=L_x-L_y}.
$$

This quantity describes the difference between the physical **one-way**
lengths of the two arms.

It is important to distinguish this quantity from the optical path
difference experienced by the propagating field, because the light travels
to the end mirror and returns.

---

## 5. Round-trip optical path difference

In a Michelson interferometer, light propagates

$$
\text{beamsplitter}
\rightarrow
\text{end mirror}
\rightarrow
\text{beamsplitter}.
$$

Consequently, the optical path associated with each arm is twice its one-way
physical length:

$$
L_{x,\mathrm{rt}}=2L_x,
$$

$$
L_{y,\mathrm{rt}}=2L_y.
$$

The differential round-trip optical path is therefore

$$
\Delta L_\mathrm{rt}
=
2L_x-2L_y.
$$

Factoring gives

$$
\Delta L_\mathrm{rt}
=
2(L_x-L_y).
$$

Using the Phase 1 definition of differential arm length,

$$
\boxed{\Delta L_\mathrm{rt}=2\Delta L_\mathrm{arm}}.
$$

The factor of two in this relation originates specifically from the
**round trip of the optical field**.

This distinction resolves the factor-of-two ambiguity that can arise when
different definitions of arm-length difference are used.

---

## 6. Differential optical phase

Physically, what the interferometer actually measures is not a path-length
difference directly, but an interference pattern, which depends on how many
optical cycles of phase separate the two returning fields. The round-trip
path difference derived above must therefore be converted into a phase
before it can be connected to a measurable intensity.

For an optical wavelength $\lambda$, the optical phase accumulated per unit
path length is

$$
k=\frac{2\pi}{\lambda}.
$$

The phase associated with the differential optical path is therefore

$$
\Delta\phi
=
\frac{2\pi}{\lambda}\Delta L_\mathrm{rt}.
$$

Substituting

$$
\Delta L_\mathrm{rt}=2\Delta L_\mathrm{arm}
$$

gives

$$
\Delta\phi
=
\frac{2\pi}{\lambda}
(2\Delta L_\mathrm{arm}),
$$

and therefore

$$
\boxed{
\Delta\phi
=
\frac{4\pi}{\lambda}\Delta L_\mathrm{arm}
}.
$$

Equivalently, using

$$
k=\frac{2\pi}{\lambda},
$$

the phase relation becomes

$$
\boxed{
\Delta\phi=2k\Delta L_\mathrm{arm}
}.
$$

Thus the complete relation is

$$
\boxed{
\Delta\phi
=
\frac{2\pi}{\lambda}\Delta L_\mathrm{rt}
=
\frac{4\pi}{\lambda}\Delta L_\mathrm{arm}
=
2k\Delta L_\mathrm{arm}
}.
$$

### 6.1 Origin of the factors

The factors in the phase relation have distinct meanings.

The factor of $2$ in

$$
\Delta\phi=2k\Delta L_\mathrm{arm}
$$

comes from the optical field travelling to the end mirror and back.

The factor

$$
\frac{2\pi}{\lambda}
$$

is the optical phase change per unit optical path length.

These two factors should not be conflated.

### 6.2 Long-wavelength approximation

The long-wavelength approximation for gravitational waves is **not
required** for this purely optical phase relation.

The equation

$$
\Delta\phi
=
\frac{2\pi}{\lambda}\Delta L_\mathrm{rt}
$$

describes the optical phase associated with the specified differential path
length.

The long-wavelength approximation enters later when relating
gravitational-wave strain to detector-arm length change.

---

## 7. Beamsplitter convention (field level)

The analytical model uses a 50:50 beamsplitter, characterized at the field
level rather than asserted as a pair of scalar intensity formulas. The
bright-port and dark-port expressions in Section 9 are derived consequences
of the convention stated here, not independent postulates.

### 7.1 Beamsplitter matrix

The beamsplitter is represented by the unitary transformation

$$
\boxed{
B=
\frac{1}{\sqrt2}
\begin{pmatrix}
1&i\\
i&1
\end{pmatrix}
}.
$$

This places a relative phase of $i$ on the reflected component and leaves
the transmitted component unshifted, consistent with standard
energy-conserving beamsplitter conventions.

Unitarity, $B^\dagger B = I$, holds exactly:

$$
B^\dagger B
=
\frac{1}{2}
\begin{pmatrix}1&-i\\-i&1\end{pmatrix}
\begin{pmatrix}1&i\\i&1\end{pmatrix}
=
\frac{1}{2}
\begin{pmatrix}2&0\\0&2\end{pmatrix}
=I.
$$

Unitarity is required for the beamsplitter to conserve total optical power.

### 7.2 Convention status

The convention above is an explicitly stated **choice**, not a uniquely
mandatory physical beamsplitter matrix. An equivalent, differently phased
convention would relabel which output port is identified as bright versus
dark without changing the physical observables. What must remain fixed for
the remainder of Phase 1 is that the same convention, once chosen, is used
consistently for both the initial split and the recombination.

This document adopts the further convention that the **same matrix** $B$ is
used for both the initial beamsplitting and the recombination (a
reciprocal-beamsplitter assumption). This is stated explicitly as an
assumption in Section 18.

---

## 8. Field propagation and recombination

Physically, the two output ports must together account for all of the input
power (an ideal beamsplitter neither creates nor absorbs energy), and which
port is bright versus dark can only depend on the *relative* phase between
the two arms, not on their absolute lengths. The field-level derivation
below is expected to reproduce both properties, and does so as a consequence
of unitarity rather than by construction.

The field-level derivation proceeds in the following order.

### 8.1 Input field

The interferometer is driven by a single input optical field entering one
input port, with the second input port unoccupied at the classical level:

$$
\mathbf E_\mathrm{in}
=
\begin{pmatrix}
E_\mathrm{in}\\
0
\end{pmatrix}.
$$

### 8.2 First beamsplitter

Applying $B$ to the input field distributes it between the x and y arms:

$$
\mathbf E_\mathrm{arms}
=
B\,\mathbf E_\mathrm{in}
=
\frac{1}{\sqrt2}
\begin{pmatrix}
E_\mathrm{in}\\
iE_\mathrm{in}
\end{pmatrix}.
$$

### 8.3 Round-trip propagation

After propagation to the end mirrors and back, each arm field acquires its
respective round-trip optical phase:

$$
E_{x,\mathrm{ret}} = \frac{E_\mathrm{in}}{\sqrt2}\,e^{i2kL_x},
\qquad
E_{y,\mathrm{ret}} = \frac{iE_\mathrm{in}}{\sqrt2}\,e^{i2kL_y}.
$$

Define the average phase and differential phase

$$
\phi_\mathrm{av}=k(L_x+L_y),
\qquad
\Delta\phi=2k(L_x-L_y),
$$

which is consistent with the Section 6 result, since
$\Delta\phi = 2k\,\Delta L_\mathrm{arm} = 2k(L_x-L_y)$.

### 8.4 Recombination

The returning fields are recombined by applying $B$ a second time:

$$
\begin{pmatrix}
E_\mathrm{dark}\\
E_\mathrm{bright}
\end{pmatrix}
=
B
\begin{pmatrix}
E_{x,\mathrm{ret}}\\
E_{y,\mathrm{ret}}
\end{pmatrix}.
$$

Carrying out the matrix multiplication and factoring
$e^{i2kL_x}\pm e^{i2kL_y} = e^{i\phi_\mathrm{av}}\big(2\cos(\Delta\phi/2)\ \text{or}\ 2i\sin(\Delta\phi/2)\big)$
gives the output fields

$$
\boxed{
E_\mathrm{dark}
=
iE_\mathrm{in}\,e^{i\phi_\mathrm{av}}
\sin\!\left(\frac{\Delta\phi}{2}\right)
}
$$

$$
\boxed{
E_\mathrm{bright}
=
iE_\mathrm{in}\,e^{i\phi_\mathrm{av}}
\cos\!\left(\frac{\Delta\phi}{2}\right)
}.
$$

Using $I \propto |E|^2$ and normalizing so that $|E_\mathrm{in}|^2 = I_0$:

$$
\boxed{
I_\mathrm{dark}
=
I_0\sin^2\!\left(\frac{\Delta\phi}{2}\right)
=
\frac{I_0}{2}\left(1-\cos\Delta\phi\right)
}
$$

$$
\boxed{
I_\mathrm{bright}
=
I_0\cos^2\!\left(\frac{\Delta\phi}{2}\right)
=
\frac{I_0}{2}\left(1+\cos\Delta\phi\right)
}.
$$

The half-angle identities $\cos^2(x) = \tfrac12(1+\cos2x)$ and
$\sin^2(x) = \tfrac12(1-\cos2x)$ recover the scalar intensity forms used
throughout the rest of this document. The bright/dark-port intensities are
therefore derived consequences of the field-level convention in Section 7,
not independently asserted formulas.

Numerical confirmation of this derivation (beamsplitter unitarity, field
recombination, power conservation, and known-answer checks at
$\Delta\phi = 0, \pi/2, \pi, -\pi$) is documented separately in
`numerical_validation.md` (tests T10–T13) and is not repeated here.

---

## 9. Bright-port and dark-port intensity

For the current scalar Phase 1 implementation, the represented detector
output is the **bright/symmetric port**.

The ideal bright-port intensity is

$$
\boxed{
I_\mathrm{bright}
=
\frac{I_0}{2}
\left(1+\cos\Delta\phi\right)
}.
$$

Substituting the Phase 1 phase relation gives

$$
I_\mathrm{bright}
=
\frac{I_0}{2}
\left[
1+
\cos
\left(
\frac{4\pi}{\lambda}\Delta L_\mathrm{arm}
\right)
\right].
$$

The corresponding dark/antisymmetric-port expression under the same
convention is

$$
\boxed{
I_\mathrm{dark}
=
\frac{I_0}{2}
\left(1-\cos\Delta\phi\right)
}.
$$

The two expressions satisfy

$$
\boxed{
I_\mathrm{bright}+I_\mathrm{dark}=I_0
}.
$$

Both expressions now follow directly from the Section 8 field-level
derivation. The repository's current scalar implementation
(`src/interferometer.py`) implements only the bright-port expression; the
dark-port expression is established analytically here but is not yet
implemented in code.

---

## 10. Complete static analytical chain

The complete Phase 1 optical model is

$$
L_x,L_y
$$

$$
\downarrow
$$

$$
\boxed{\Delta L_\mathrm{arm}=L_x-L_y}
$$

$$
\downarrow
$$

$$
\boxed{\Delta L_\mathrm{rt}=2\Delta L_\mathrm{arm}}
$$

$$
\downarrow
$$

$$
\boxed{
\Delta\phi
=
\frac{2\pi}{\lambda}\Delta L_\mathrm{rt}
=
\frac{4\pi}{\lambda}\Delta L_\mathrm{arm}
}
$$

$$
\downarrow
$$

$$
\text{field-level propagation and recombination (Sections 7--8)}
$$

$$
\downarrow
$$

$$
\boxed{
I_\mathrm{bright}
=
\frac{I_0}{2}(1+\cos\Delta\phi)
}
$$

$$
\boxed{
I_\mathrm{dark}
=
\frac{I_0}{2}(1-\cos\Delta\phi)
}.
$$

Thus the analytical model can be summarized as

$$
\boxed{
L_x,L_y
\rightarrow
\Delta L_\mathrm{arm}
\rightarrow
\Delta L_\mathrm{rt}
\rightarrow
\Delta\phi
\rightarrow
I_\mathrm{bright},I_\mathrm{dark}
}.
$$

---

## 11. Constructive interference

Constructive interference occurs when the differential optical phase is an
integer multiple of $2\pi$:

$$
\Delta\phi=2\pi n,
\qquad
n\in\mathbb{Z}.
$$

Using

$$
\Delta\phi
=
\frac{4\pi}{\lambda}\Delta L_\mathrm{arm},
$$

gives

$$
\frac{4\pi}{\lambda}\Delta L_\mathrm{arm}
=
2\pi n.
$$

Therefore,

$$
\boxed{
\Delta L_\mathrm{arm}
=
\frac{n\lambda}{2}
}.
$$

At these points,

$$
\cos\Delta\phi=1,
$$

so

$$
I_\mathrm{bright}=I_0
$$

and

$$
I_\mathrm{dark}=0.
$$

Thus the bright port receives the maximum ideal optical intensity under the
chosen normalization.

---

## 12. Destructive interference

Destructive interference occurs when

$$
\Delta\phi=(2n+1)\pi,
\qquad
n\in\mathbb{Z}.
$$

Substituting the Phase 1 phase relation,

$$
\frac{4\pi}{\lambda}\Delta L_\mathrm{arm}
=
(2n+1)\pi.
$$

Therefore,

$$
\boxed{
\Delta L_\mathrm{arm}
=
\frac{(2n+1)\lambda}{4}
}.
$$

At these points,

$$
\cos\Delta\phi=-1,
$$

so

$$
I_\mathrm{bright}=0
$$

and

$$
I_\mathrm{dark}=I_0.
$$

---

## 13. Periodicity

The ideal intensity depends on the cosine of the differential optical phase.

Because

$$
\cos(\theta+2\pi)=\cos\theta,
$$

an increase in differential arm length by $\lambda/2$ changes the phase by

$$
\Delta\phi
\rightarrow
\Delta\phi
+
\frac{4\pi}{\lambda}
\frac{\lambda}{2}
=
\Delta\phi+2\pi.
$$

Therefore,

$$
I_\mathrm{bright}
\left(
\Delta L_\mathrm{arm}+\frac{\lambda}{2}
\right)
=
I_\mathrm{bright}(\Delta L_\mathrm{arm}),
$$

and likewise for the dark port.

The ideal interference pattern therefore has differential-arm-length period

$$
\boxed{
\Delta L_\mathrm{period}=\frac{\lambda}{2}
}.
$$

---

## 14. Symmetry

Because

$$
\cos(-\theta)=\cos\theta,
$$

the ideal bright-port intensity satisfies

$$
I_\mathrm{bright}(+\Delta L_\mathrm{arm})
=
I_\mathrm{bright}(-\Delta L_\mathrm{arm}).
$$

The corresponding dark-port intensity has the same even symmetry:

$$
I_\mathrm{dark}(+\Delta L_\mathrm{arm})
=
I_\mathrm{dark}(-\Delta L_\mathrm{arm}).
$$

Therefore, the ideal scalar intensity response is symmetric under reversal
of the sign of the differential arm-length change.

The sign of $\Delta L_\mathrm{arm}$ nevertheless remains important as a
convention for describing which arm is longer, even though it does not
change this ideal scalar intensity response.

---

## 15. Analytical limiting and consistency checks

The analytical model provides several direct checks for later numerical
validation.

### 15.1 Equal arms

For

$$
\Delta L_\mathrm{arm}=0,
$$

the phase difference is

$$
\Delta\phi=0.
$$

Therefore,

$$
I_\mathrm{bright}=I_0
$$

and

$$
I_\mathrm{dark}=0.
$$

### 15.2 Constructive condition

For

$$
\Delta L_\mathrm{arm}=\frac{n\lambda}{2},
$$

the bright-port response reaches its maximum:

$$
I_\mathrm{bright}=I_0.
$$

### 15.3 Destructive condition

For

$$
\Delta L_\mathrm{arm}
=
\frac{(2n+1)\lambda}{4},
$$

the bright-port response reaches zero:

$$
I_\mathrm{bright}=0.
$$

### 15.4 Periodicity

Changing

$$
\Delta L_\mathrm{arm}
\rightarrow
\Delta L_\mathrm{arm}+\frac{\lambda}{2}
$$

must leave the ideal intensity unchanged.

### 15.5 Symmetry

Changing

$$
\Delta L_\mathrm{arm}
\rightarrow
-\Delta L_\mathrm{arm}
$$

must leave the ideal scalar intensity unchanged.

These predictions form analytical expectations for the subsequent
numerical-validation stage (`numerical_validation.md`).

---

## 16. Gravitational-wave coupling boundary

The two parts of the broader detector model are deliberately kept separate.
The optical Michelson model derived in Sections 2–15 is conceptually
independent of the gravitational-wave strain-to-arm-length relation: the
optical derivation begins from a specified differential arm-length
perturbation, while the subsequent gravitational-wave response work
establishes how a gravitational wave produces that perturbation in the
first place,

$$
h(t)
\rightarrow
\Delta L_\mathrm{arm}(t).
$$

Combining the two gives the broader conceptual chain

$$
h(t)
\rightarrow
\Delta L_\mathrm{arm}(t)
\rightarrow
\Delta L_\mathrm{rt}(t)
\rightarrow
\Delta\phi(t)
\rightarrow
I_\mathrm{bright/dark}(t),
$$

of which only the $\Delta L_\mathrm{arm}(t)\rightarrow I_\mathrm{bright/dark}(t)$
portion is established by this document (Section 10).

For the simplified aligned, long-wavelength case used in the broader
detector model,

$$
\boxed{
\Delta L_\mathrm{arm}(t)=h(t)L_0
}
$$

where

$$
h(t)=\text{detector-projected gravitational-wave strain}
$$

and

$$
L_0=\text{nominal arm length}.
$$

This relation is used under the explicitly specified conditions:

1. Equal nominal arm lengths,

$$
L_x=L_y=L_0.
$$

2. An appropriate gravitational-wave propagation direction relative to the
   detector.

3. The $+$ polarization is aligned with the detector arms.

4. The strain used is the detector-projected strain.

5. The long-wavelength approximation is valid.

For general detector geometry, the projected strain may be written

$$
\boxed{
h_\mathrm{det}(t)
=
F_+h_+(t)+F_\times h_\times(t)
}.
$$

The general detector-response treatment belongs to the subsequent
gravitational-wave response stages and is not developed as part of the core
Phase 1 optical derivation.

The long-wavelength approximation belongs to the **GW strain-to-arm-length
relation** above, not to the basic optical phase relation derived in
Section 6. Accordingly, the GW coupling is treated as a **Phase 2 input to
the Phase 1 optical model** rather than as part of the core Phase 1 optical
derivation.

---

## 17. Frozen analytical results

### 17.1 Freeze policy

The results collected below are **frozen** for the duration of the Phase 1
numerical-validation work: none of these equations, sign conventions, or the
beamsplitter convention of Section 7 may be changed while numerical
validation (`numerical_validation.md`, tests T10–T13) is in progress. Any
proposed change to a frozen result requires a documented justification and a
full rerun of T10–T13 against the revised result before it can be
re-adopted. This freeze applies to the boxed results in this section only;
it does not extend to the Stage 2/3 material referenced in Section 16,
which remains open.

### 17.2 Frozen results

For the full-difference convention adopted throughout Phase 1:

$$
\boxed{
\Delta L_\mathrm{arm}=L_x-L_y
}
$$

$$
\boxed{
\Delta L_\mathrm{rt}=2\Delta L_\mathrm{arm}
}
$$

$$
\boxed{
k=\frac{2\pi}{\lambda}
}
$$

$$
\boxed{
\Delta\phi
=
\frac{2\pi}{\lambda}\Delta L_\mathrm{rt}
=
\frac{4\pi}{\lambda}\Delta L_\mathrm{arm}
=
2k\Delta L_\mathrm{arm}
}
$$

$$
\boxed{
B=
\frac{1}{\sqrt2}
\begin{pmatrix}
1&i\\
i&1
\end{pmatrix}
}
$$

$$
\boxed{
I_\mathrm{bright}
=
\frac{I_0}{2}(1+\cos\Delta\phi)
}
$$

$$
\boxed{
I_\mathrm{dark}
=
\frac{I_0}{2}(1-\cos\Delta\phi)
}
$$

$$
\boxed{
I_\mathrm{bright}+I_\mathrm{dark}=I_0
}
$$

$$
\boxed{
\Delta L_\mathrm{period}=\frac{\lambda}{2}
}
$$

Constructive interference:

$$
\boxed{
\Delta L_\mathrm{arm}=\frac{n\lambda}{2}
}
$$

Destructive interference:

$$
\boxed{
\Delta L_\mathrm{arm}
=
\frac{(2n+1)\lambda}{4}
}
$$

The simplified gravitational-wave coupling used in later phases is

$$
\boxed{
\Delta L_\mathrm{arm}(t)=h(t)L_0
}
$$

under its explicitly stated assumptions.

---

## 18. Assumptions

The Phase 1 optical model and its field-level derivation rely on the
following idealizations:

1. **Monochromatic, coherent input field.** A single well-defined wavelength
   $\lambda$ and phase; no bandwidth, linewidth, or coherence-length
   effects are modeled.
2. **Ideal, lossless 50:50 beamsplitter**, exactly characterized by the
   matrix $B$ in Section 7.1. The same matrix $B$ is used for both the
   initial split and the recombination pass — the reciprocal-beamsplitter
   convention — which is a stated choice, not a forced physical necessity.
3. **Perfect end mirrors** — unity reflectivity, no absorption, no
   scattering.
4. **No optical loss anywhere** in either arm or at the beamsplitter.
5. **Static arm lengths** $L_x, L_y$ for the core derivation
   (Sections 2–15). No time dependence is introduced in the optical model
   itself.
6. **Single spatial mode, perfect beam overlap** at recombination — no mode
   mismatch, divergence, or misalignment.
7. **Scalar/uniform polarization treatment** for the optical field — no
   birefringence or polarization-dependent phase.
8. **Second input port treated as vacuum** (zero classical field). This
   matters only if quantum vacuum-noise coupling is considered later; it is
   not used in this classical derivation.
9. $I \propto |E|^2$, with $I_0$ the properly normalized input intensity.
10. **One-way arm-length convention** — $L_x, L_y$ are one-way distances
    from beamsplitter to end mirror; the round-trip factor of 2 is applied
    explicitly (Section 5) rather than folded into a redefined "arm length."

---

## 19. Limitations

1. **No optical losses.** Real beamsplitter/mirror imperfections, coating
   absorption, and scattering will degrade the exact 50:50 split and reduce
   achievable contrast below what this model predicts.
2. **No time dependence.** As derived, $\Delta\phi$ is static. Extending
   to $\Delta\phi(t)$ for gravitational-wave strain (Phase 2 / Stage 2)
   changes none of the underlying algebra but has not itself been derived
   or validated in this document.
3. **No cavity effects.** No power recycling, no signal recycling, no
   Fabry–Pérot arms. Real detectors substantially modify circulating power
   and frequency response beyond this model's scope.
4. **No quantum-noise treatment.** Shot noise, radiation-pressure noise, and
   vacuum-port fluctuations are excluded from this derivation; these belong
   to the physical-noise stage of the project.
5. **The beamsplitter convention is a choice, not a law.** A different but
   equivalent phase convention would relabel which port is identified as
   bright versus dark without changing the physical observables. This
   document's convention should not be read as the unique correct one.
6. **No finite beam size, alignment, or mode-mismatch effects.** The model
   assumes perfect spatial overlap and therefore represents an upper bound
   on achievable interference contrast.
7. **Code coverage is partial.** `src/interferometer.py` implements the
   bright-port formula only. The dark-port formula and the full field-level
   treatment derived here (Sections 7–8) are established analytically but
   are not yet implemented in the repository's code.
8. **Numerical validation checks internal consistency only.** The T10–T13
   tests referenced in `numerical_validation.md` confirm that this
   derivation is self-consistent to machine precision. They are not
   empirical validation against real interferometer data or published
   literature; that remains a separate future step.

---

## 20. Role in the validation workflow

This analytical model is established independently of whether the existing
repository code produces the expected result.

It therefore serves as the physics reference for the subsequent stages:

$$
\boxed{
\text{Analytical derivation}
\rightarrow
\text{Literature validation}
\rightarrow
\text{Code and simulation audit}
\rightarrow
\text{Numerical validation}
\rightarrow
\text{Conclusion}
}
$$

The distinction between these stages is deliberate:

* **Analytical model (this document):** What physics is being modeled, and
  how is it derived from a stated field-level convention?
* **Literature validation:** What external scientific evidence supports the
  model?
* **Code and simulation audit:** Does the repository implement the
  established physics?
* **Numerical validation** (`numerical_validation.md`): Does the
  implementation reproduce the analytical predictions?
* **Limitations and conclusion:** What has actually been established, and
  where does Phase 1 stop?

The analytical model therefore remains an independent reference rather than
a retrospective description of the existing code.
