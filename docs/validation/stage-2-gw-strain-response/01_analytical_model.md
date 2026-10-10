# Analytical Model — Gravitational-Wave Strain to Differential Arm Response (Stage 2)

**Status:** Stage 2 analytical derivation complete, including the interface to the frozen Stage 1 optical model. Literature validation, code audit, and numerical validation of this derivation are separate, later documents (Section 16). This document is a derivation record; it does not claim literature or empirical validation.

---

## 1. Purpose and scope

### 1.1 Purpose

This document establishes the analytical model that connects a gravitational-wave (GW) strain $h(t)$ to the differential arm-length response of an ideal two-arm Michelson interferometer, and then to the optical phase and output intensity through the frozen Stage 1 model.

It answers two questions together: **what physics was derived** (Sections 4–11), and **under what definitions, conventions, and assumptions it holds** (Sections 3, 9, and 14). The second question is load-bearing. Every result below holds only under the conventions of Section 3 and the assumptions of Section 14.

The physical question addressed is why a GW produces a differential arm-length change at all. The model is established independently of the repository implementation and independently of literature validation; both are performed against this document, not the reverse.

### 1.2 In scope

- weak-field metric perturbation and the definition of strain;
- Transverse-Traceless (TT) gauge and test-mass coordinate fixity;
- polarization modes and detector-projected strain, stated at the level needed for the aligned baseline;
- proper arm lengths and the long-wavelength approximation (LWA);
- individual arm perturbations and their antisymmetric signs;
- the differential arm response $\Delta L_\mathrm{arm}(t)=h(t)L_0$;
- the connection of that response to the frozen Stage 1 optical phase and intensity relations.

### 1.3 Outside scope

- derivation of the general antenna-pattern functions, and multi-detector network response;
- finite-arm optical transit corrections, Fabry–Pérot arm cavities, power/signal recycling, readout schemes, and non-orthogonal arm geometries (named in Section 15, not developed);
- physical noise, PSD/ASD modelling, and sensitivity;
- assessment of the repository's existing $h(t)\to\Delta L(t)$ simulation (a later code-audit stage, Section 16).

### 1.4 Interface with the frozen Stage 1 model

Stage 1 treats the differential arm length $\Delta L_\mathrm{arm}$ as a specified input and establishes the downstream optical response. Stage 2 begins by establishing the physical relation between strain and that input:

$$
\text{Stage 2: } h(t)\rightarrow\Delta L_\mathrm{arm}(t)
\qquad\qquad
\text{Stage 1 (frozen): } \Delta L_\mathrm{arm}\rightarrow\Delta L_\mathrm{rt}\rightarrow\Delta\phi\rightarrow I_\mathrm{bright/dark}
$$

The relation $\Delta L_\mathrm{arm}(t)=h(t)L_0$ was a candidate relation at the start of Stage 2 and was not treated as validated. It is derived independently in Sections 4–8. The Stage 1 derivation is not re-derived or modified here.

*Terminology:* this document uses "Stage" for the project pipeline. The Stage 1 document's "Phase 1" label refers to the same ideal-Michelson optical stage.

---

## 2. Physical system and geometry

The system is the ideal two-arm Michelson interferometer of Stage 1, now exposed to a plane gravitational wave.

- **Coordinate frame:** a 4-dimensional Cartesian TT frame $(t,x,y,z)$ anchored at the central beamsplitter, origin $(0,0,0)$.
- **Arms:** the $x$-arm lies along $+x$ from $x=0$ to $x=L_0$; the $y$-arm lies along $+y$ from $y=0$ to $y=L_0$. The arms are orthogonal ($\zeta=90^\circ$) with equal nominal unperturbed lengths $L_{x,0}=L_{y,0}=L_0$.
- **Wave:** a plane GW arriving from directly overhead ($\theta=0$), propagating along $+z$ at speed $c$, orthogonal to the detector plane.
- **Alignment:** "$+$ polarization aligned with the arms" means the quadrupolar principal axes of elongation and contraction ($\phi=0,\ \psi=0$) coincide with the $x$- and $y$-arm directions. This sets $h_\times=0$.
- **Test-mass positions** (coordinate values, fixed in TT gauge, Section 4.3):

| Element | Coordinates $(x,y,z)$ |
|---|---|
| Beamsplitter / corner station | $(0,0,0)$ |
| End test mass X | $(L_0,0,0)$ |
| End test mass Y | $(0,L_0,0)$ |

---

## 3. Variables, conventions, and notation map

### 3.1 Symbols

| Symbol | Meaning | Convention |
|---|---|---|
| $g_{\mu\nu}$, $\eta_{\mu\nu}$ | spacetime metric; flat background | $\eta_{\mu\nu}=\mathrm{diag}(-c^2,1,1,1)$ |
| $h_{\mu\nu}$ | metric perturbation tensor | $\lvert h_{\mu\nu}\rvert\ll1$ |
| $h_+,\ h_\times$ | plus and cross polarization amplitudes | dimensionless |
| $h_\mathrm{det}(t)$ | detector-projected strain | dimensionless |
| $h(t)$ | working scalar strain | $h\equiv h_+\equiv h_\mathrm{det}$ in the aligned baseline (Section 4.6) |
| $F_+,\ F_\times$ | antenna-pattern functions | dimensionless, $0\le\lvert F\rvert\le1$ |
| $L_0$ | nominal one-way arm length | $L_0\equiv L_{x,0}=L_{y,0}$, metres |
| $L_x(t),\ L_y(t)$ | proper one-way arm lengths | metres |
| $\delta L_x,\ \delta L_y$ | proper-length perturbations | $\delta L_i\equiv L_i-L_0$ |
| $\Delta L_\mathrm{arm}$ | differential one-way arm length | signed full difference |
| $\Delta L_\mathrm{rt}$ | round-trip optical path difference | signed (Stage 1) |
| $\lambda_0,\ k_0$ | vacuum wavelength; wavenumber | $k_0=2\pi/\lambda_0$ |
| $\Delta\phi$ | differential optical phase | signed, radians |
| $f_\mathrm{gw}$, $f^*$ | GW frequency; LWA reference frequency | $f^*\equiv c/(2\pi L_0)$ |

### 3.2 Conventions

- **Full-difference convention**, identical to Stage 1: $\Delta L_\mathrm{arm}\equiv L_x-L_y=\delta L_x-\delta L_y$. The half-difference convention used in some literature is a different definition of the same imbalance and is not used here.
- **Arm labelling:** $L_x$ is the arm along $+x$ (the inline arm); $L_y$ is the arm along $+y$ (the perpendicular arm).
- **Sign:** $\Delta L_\mathrm{arm}>0$ means the $x$-arm is longer.

### 3.3 Notation map

$$
g_{\mu\nu}\xrightarrow{\text{weak field}}h_{\mu\nu}\xrightarrow{\text{TT gauge}}h^\mathrm{TT}_{ij}\xrightarrow{\text{polarization basis}}(h_+,h_\times)\xrightarrow{(F_+,F_\times)}h_\mathrm{det}(t)\xrightarrow{\text{aligned baseline}}h(t)
$$

---

## 4. Gravitational-wave strain and its representation

### 4.1 Operational definition of strain

Strain is the dimensionless fractional deformation of proper spatial separation produced by passing gravitational radiation: an oscillating tidal deformation that stretches space along one transverse direction while contracting it along the orthogonal one. Representations used in this project:

- $h(t)$ — instantaneous scalar time series;
- $h_0$ — peak waveform amplitude (for example $1.0\times10^{-21}$);
- $h_c$ — characteristic strain.

Strain is strictly dimensionless ($\mathrm{m/m}$). Expressions such as "strain/$\sqrt{\mathrm{Hz}}$" refer to the amplitude spectral density $\sqrt{S_h(f)}$ (units $\mathrm{Hz}^{-1/2}$), not to raw strain. GW strain $h$ is also unrelated to the reduced Hubble parameter $h=H_0/(100\ \mathrm{km\,s^{-1}\,Mpc^{-1}})$.

How this single-symbol definition applies to a single arm versus the differential arm combination is fixed in Sections 7 and 8.

### 4.2 Weak-field metric perturbation

Far from strong-field sources the metric is a small perturbation of flat spacetime:

$$
g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu},\qquad \lvert h_{\mu\nu}\rvert\ll1 .
$$

$h_{\mu\nu}$ is a symmetric second-rank tensor in 4D ($4\times4$, 10 independent components). It modulates the physical interval, $ds^2=(\eta_{\mu\nu}+h_{\mu\nu})\,dx^\mu dx^\nu$. The tensor $h_{\mu\nu}$ is the full 10-component field; the scalar $h(t)$ is a one-dimensional projection along a specific baseline.

### 4.3 TT gauge and test-mass fixity

General coordinate covariance gives gauge freedom. The TT gauge fixes it so that exactly the two physical radiative degrees of freedom remain, through four defining conditions:

1. $h^\mathrm{TT}_{0\mu}=0$ (purely spatial);
2. $h^i{}_i=h_{xx}+h_{yy}+h_{zz}=0$ (traceless);
3. $\partial^jh^\mathrm{TT}_{ij}=0$ (transverse); for propagation along $+z$, $h^\mathrm{TT}_{z\mu}=0$;
4. $\Box h^\mathrm{TT}_{\mu\nu}=0$ (vacuum wave equation, propagation at $c$).

In this gauge $\Gamma^i{}_{00}=\tfrac12\eta^{ik}(2\partial_0h_{k0}-\partial_kh_{00})=0$. Freely falling test masses initially at rest therefore remain at **constant coordinate positions**, $\Delta x_\mathrm{coord}=L_0=\text{const}$. All physical wave effects then appear as modulations of proper distance, $S=\int\sqrt{g_{ij}\,dx^i dx^j}$, and of photon round-trip travel time, $t_0=\tfrac1c\int\sqrt{g_{ij}\,dx^i dx^j}$.

### 4.4 Polarization modes

Linearized GR gives two independent orthogonal quadrupolar modes. For propagation along $+z$,

$$
h^\mathrm{TT}_{\mu\nu}(t,z)=
\begin{pmatrix}
0&0&0&0\\
0&h_+&h_\times&0\\
0&h_\times&-h_+&0\\
0&0&0&0
\end{pmatrix},
\qquad h_{xx}=-h_{yy}=h_+,\ \ h_{xy}=h_{yx}=h_\times ,
$$

with argument $(t-z/c)$ in each amplitude. The $h_+$ mode expands proper distance along $x$ while contracting it along $y$, and the reverse on the next half-cycle. The $h_\times$ mode has the same pattern rotated by $45^\circ$. Rotating the transverse axes by $\psi$ transforms the modes as

$$
h'_+=h_+\cos2\psi+h_\times\sin2\psi,\qquad
h'_\times=-h_+\sin2\psi+h_\times\cos2\psi .
$$

### 4.5 Detector-projected strain and antenna patterns

An interferometer is a directional instrument that senses a single scalar differential response, a linear superposition of the two modes:

$$
h_\mathrm{det}(t)=F_+(\theta,\phi,\psi)\,h_+(t)+F_\times(\theta,\phi,\psi)\,h_\times(t).
$$

$F_+$ and $F_\times$ are dimensionless coupling factors determined by the source direction $(\theta,\phi)$, the polarization angle $\psi$, and the interferometer opening angle. For an orthogonal ($90^\circ$) L-shaped detector:

$$
F_+=\tfrac12(1+\cos^2\theta)\cos2\phi\cos2\psi-\cos\theta\sin2\phi\sin2\psi,
$$

$$
F_\times=\tfrac12(1+\cos^2\theta)\cos2\phi\sin2\psi+\cos\theta\sin2\phi\cos2\psi .
$$

These forms are **stated, not derived**, in Stage 2; they are evaluated only at the aligned point below.

### 4.6 Aligned-baseline equivalence

For overhead incidence with arm-aligned plus polarization ($\theta=0,\ \phi=0,\ \psi=0,\ h_\times=0$): $\cos\theta=1$, $\cos2\phi=1$, $\sin2\phi=0$, $\cos2\psi=1$, $\sin2\psi=0$, hence $F_+=1$, $F_\times=0$ and

$$
h_\mathrm{det}(t)=(1)\,h_+(t)+(0)\,h_\times(t)=h_+(t).
$$

The working scalar strain, the plus mode, and the detector-projected strain are therefore identical in the aligned baseline:

$$
h(t)\equiv h_+(t)\equiv h_\mathrm{det}(t).
$$

---

## 5. Starting metric at the detector plane

For a wave along $+z$ with $h_\times=0$, the TT line element is

$$
ds^2=-c^2dt^2+[1+h_+(t-z/c)]\,dx^2+[1-h_+(t-z/c)]\,dy^2+dz^2 .
$$

The detector lies in the $x$–$y$ plane at $z=0$, so the retarded-time argument reduces to $t$ and, with Section 4.6,

$$
ds^2=-c^2dt^2+[1+h(t)]\,dx^2+[1-h(t)]\,dy^2+dz^2 ,
$$

$$
g_{\mu\nu}(t)=
\begin{pmatrix}
-c^2&0&0&0\\
0&1+h(t)&0&0\\
0&0&1-h(t)&0\\
0&0&0&1
\end{pmatrix}.
$$

---

## 6. Proper arm lengths and the long-wavelength approximation

### 6.1 Proper-length integrals

Proper distance along each arm at fixed coordinate time ($dt=0$) is

$$
L_x(t)=\int_0^{L_0}\sqrt{g_{xx}(t)}\,dx=\int_0^{L_0}\sqrt{1+h(t)}\,dx,\qquad
L_y(t)=\int_0^{L_0}\sqrt{g_{yy}(t)}\,dy=\int_0^{L_0}\sqrt{1-h(t)}\,dy .
$$

### 6.2 Role of the long-wavelength approximation

The physical observable is the photon round-trip time (Section 4.3). Under the LWA, $f_\mathrm{gw}\ll f^*\equiv c/(2\pi L_0)$, equivalently $\lambda_\mathrm{GW}\gg L_0$, the strain is spatially uniform along each arm at each instant and the light transit time is negligible compared with the GW period. Fixed-time proper length is then the appropriate arm-length measure, and $\sqrt{1\pm h(t)}$ can be taken outside the integrals:

$$
L_x(t)=\sqrt{1+h(t)}\,L_0,\qquad L_y(t)=\sqrt{1-h(t)}\,L_0 .
$$

The LWA belongs to this strain-to-arm-length step. It is not required for the purely optical phase relation inherited from Stage 1. Its quantitative domain is given in Section 9.

### 6.3 Binomial expansion and origin of the factor $\tfrac12$

For $\lvert h\rvert\ll1$ (typically $\sim10^{-21}$),

$$
\sqrt{1\pm h(t)}=(1\pm h)^{1/2}=1\pm\tfrac12h-\tfrac18h^2+\mathcal{O}(h^3)\approx1\pm\tfrac12h(t).
$$

The factor $\tfrac12$ is not a detector loss or efficiency factor. It is the exact first-order binomial coefficient of $\sqrt{g_{ii}}=(1\pm h)^{1/2}$. Truncating each single-arm length at first order leaves an error of order $h^2\sim10^{-42}$ for $\lvert h\rvert\sim10^{-21}$.

### 6.4 Individual proper arm lengths

$$
L_x(t)\approx L_0+\tfrac12h(t)L_0,\qquad L_y(t)\approx L_0-\tfrac12h(t)L_0 .
$$

---

## 7. Individual arm perturbations and antisymmetric signs

Defining $\delta L_i(t)\equiv L_i(t)-L_0$:

$$
\delta L_x(t)=+\tfrac12h(t)L_0\ \Rightarrow\ \frac{\delta L_x}{L_0}=+\tfrac12h(t),\qquad
\delta L_y(t)=-\tfrac12h(t)L_0\ \Rightarrow\ \frac{\delta L_y}{L_0}=-\tfrac12h(t).
$$

The opposite signs follow from the traceless quadrupolar structure ($h^\mathrm{TT}_{xx}=-h^\mathrm{TT}_{yy}=h_+$): an instantaneous $h>0$ stretches space along $x$ while compressing it along $y$ by the same amount. The $x$-arm extends ($\delta L_x>0$) and the $y$-arm compresses ($\delta L_y<0$).

For a single arm, the strain is therefore related to the fractional arm change by

$$
h(t)=2\,\frac{\delta L_x(t)}{L_0}=-2\,\frac{\delta L_y(t)}{L_0}.
$$

Dimensions: $[h]=\mathrm{m/m}$, $[L_0]=\mathrm{m}$, so $[\delta L_x]=[\delta L_y]=\mathrm{m}$.

---

## 8. Differential arm response

### 8.1 Construction and baseline cancellation

With the fixed convention of Section 3.2,

$$
\Delta L_\mathrm{arm}(t)=[L_0+\delta L_x(t)]-[L_0+\delta L_y(t)]=(L_0-L_0)+[\delta L_x(t)-\delta L_y(t)].
$$

Because $L_{x,0}=L_{y,0}=L_0$, the static background cancels exactly, leaving $\Delta L_\mathrm{arm}=\delta L_x-\delta L_y$.

### 8.2 Combination of the half-contributions

$$
\Delta L_\mathrm{arm}(t)=\left(+\tfrac12h(t)L_0\right)-\left(-\tfrac12h(t)L_0\right)=\left(\tfrac12+\tfrac12\right)h(t)L_0 .
$$

The minus sign of the subtraction acts on the compression of the $y$-arm and turns it into an additive contribution, restoring unit scale:

$$
\boxed{\Delta L_\mathrm{arm}(t)=h(t)\,L_0}
$$

Thus the differential fractional change is $h$, while each single arm carries $h/2$ (Section 7). Dimensions: $[\Delta L_\mathrm{arm}]=\mathrm{m}$.

### 8.3 Sign convention

The project definition $\Delta L_\mathrm{arm}\equiv L_x-L_y$ gives $+h(t)L_0$. The reversed convention $L_y-L_x$ would give $-h(t)L_0$. Through the Stage 1 field relations this reverses the sign of the dark-port field (a global $\pi$ phase) and leaves both port intensities unchanged, because the ideal scalar intensity is even in $\Delta\phi$ (Stage 1, Section 14). The sign still matters as a convention for which arm is longer.

---

## 9. Validity domain: long-wavelength regime and quasi-static response

### 9.1 Frequency boundary

The physical condition for the LWA is

$$
f_\mathrm{gw}\ll f^*\equiv\frac{c}{2\pi L_0}.
$$

The project additionally adopts the quantitative operating criterion $f_\mathrm{gw}\le0.1\,f^*$. This is a **project-adopted operational criterion**, not a statement of the physical law above.

For the 4 km reference arm, $f^*\approx11.93$ kHz, so the project criterion corresponds to $f_\mathrm{gw}\le1.2$ kHz.

### 9.2 Time dependence

Stage 1 derived the optical response for static arm lengths and noted that extending it to $\Delta L_\mathrm{arm}(t)$ had not itself been derived. Stage 2 supplies the justification used in this project. In the LWA the photon transit time is quasi-instantaneous, $L_0/c\ll1/f_\mathrm{gw}$, so the frozen Stage 1 relations apply instant by instant, with $\Delta L_\mathrm{arm}\to\Delta L_\mathrm{arm}(t)$, and $\Delta\phi(t)$ tracks $h(t)$ synchronously without phase lag. This is a quasi-static argument under the stated regime. It is not a general time-dependent optical derivation, and it fails at $f_\mathrm{gw}\gtrsim f^*$ (Section 15).

---

## 10. Stage 2 → Stage 1 interface

### 10.1 Convention alignment

| Item | Stage 2 | Stage 1 | Match |
|---|---|---|---|
| Differential arm length | $L_x-L_y$ | $L_x-L_y$ | Identical |
| Arm orientation and quadrupolar inversion | $x$ expands, $y$ contracts for $h>0$ | same labelling | Identical |
| Nominal arm length | $L_{x,0}=L_{y,0}=L_0$ | same | Identical |
| Scale and units | $h$ dimensionless; lengths in m | same | Identical |

$\Delta L_\mathrm{arm}(t)=h(t)L_0$ therefore enters the Stage 1 relations directly, without intermediate scaling, conversion factors, or sign flips.

### 10.2 Inherited optical relations

From the frozen Stage 1 model (inherited, not re-derived):

$$
\Delta L_\mathrm{rt}=2\Delta L_\mathrm{arm},\qquad
\Delta\phi=\frac{2\pi}{\lambda_0}\Delta L_\mathrm{rt}=2k_0\Delta L_\mathrm{arm}=\frac{4\pi}{\lambda_0}\Delta L_\mathrm{arm}.
$$

The factor of 2 in $2k_0$ arises exclusively from the round trip of the optical field.

### 10.3 Master transfer equation

Substituting Section 8.2 into Section 10.2:

$$
\boxed{\Delta\phi(t)=\frac{4\pi L_0}{\lambda_0}\,h(t)}
$$

Dimensions: $[4\pi L_0/\lambda_0][h]=(\mathrm{m/m})(\mathrm{m/m})$, i.e. radians. Sign: $h>0$ gives $\delta L_x>0$, $\delta L_y<0$, $\Delta L_\mathrm{arm}>0$ and $\Delta\phi>0$ throughout.

### 10.4 Factor-of-two audit

Two factors appear and have distinct origins. The $\tfrac12$ in the individual arm responses comes from the binomial expansion (Section 6.3). The 2 in $4\pi/\lambda_0$ comes from round-trip propagation (Section 10.2). Evaluating arm by arm:

$$
\delta\phi_x=\frac{4\pi}{\lambda_0}\delta L_x=+\frac{2\pi L_0}{\lambda_0}h,\qquad
\delta\phi_y=\frac{4\pi}{\lambda_0}\delta L_y=-\frac{2\pi L_0}{\lambda_0}h,
$$

$$
\Delta\phi=\delta\phi_x-\delta\phi_y=\frac{4\pi L_0}{\lambda_0}h .
$$

This agrees identically with Section 10.3. No factor of 2 is missing or double-counted.

### 10.5 Port intensities

With the Stage 1 field-level convention (frozen, Stage 1 Sections 7–9):

$$
I_\mathrm{bright}(t)=\frac{I_0}{2}\big[1+\cos\Delta\phi(t)\big],\qquad
I_\mathrm{dark}(t)=\frac{I_0}{2}\big[1-\cos\Delta\phi(t)\big],
$$

with $\Delta\phi(t)$ from Section 10.3. Both ports are given because GW readout operates at the dark (antisymmetric) port; the bright-port form is the one currently represented in the repository's scalar implementation.

### 10.6 Static conversion gain

$$
G_\mathrm{phase,static}\equiv\frac{4\pi L_0}{\lambda_0}
=\frac{4\pi\times4000\ \mathrm{m}}{1064\times10^{-9}\ \mathrm{m}}\approx4.724\times10^{10}\ \mathrm{rad/strain}
\quad(L_0=4\ \mathrm{km},\ \lambda_0=1064\ \mathrm{nm}).
$$

Illustration: for $h=10^{-21}$, $\Delta\phi\approx4.72\times10^{-11}$ rad.

---

## 11. Complete derivation chain and dependency map

```text
1. Weak-field GR metric            g_μν = η_μν + h_μν,  |h| << 1
   │
2. TT gauge                        h_0μ = 0, h^i_i = 0, ∂^j h_ij = 0
   │                               (test masses fixed in coordinates: Δx_coord = L0)
3. Aligned baseline                θ = 0, φ = 0, ψ = 0, h_× = 0  →  F+ = 1, F× = 0
   │                               h ≡ h_+ ≡ h_det
4. Line element at z = 0           ds² = −c²dt² + (1+h)dx² + (1−h)dy² + dz²
   │
5. Proper lengths + LWA            L_x = √(1+h) L0,  L_y = √(1−h) L0
   │
6. Binomial expansion              δL_x = +½ h L0,  δL_y = −½ h L0
   │
7. Differential subtraction        ΔL_arm = δL_x − δL_y = h L0
   │
8. Stage 1 round trip + phase      ΔL_rt = 2ΔL_arm,  Δφ = (4π/λ0) ΔL_arm
   │
9. Master transfer                 Δφ(t) = (4π L0 / λ0) h(t)
   │
10. Stage 1 recombination          I_bright, I_dark = (I0/2)[1 ± cos Δφ]
```

---

## 12. Analytical limiting and consistency checks

These are analytical expectations against which later validation stages can compare. They are not themselves numerical tests.

| Check | Expectation |
|---|---|
| No strain | $h=0\Rightarrow\delta L_x=\delta L_y=0,\ \Delta L_\mathrm{arm}=0,\ \Delta\phi=0$ |
| Sign | $h>0\Rightarrow\Delta L_\mathrm{arm}>0$ and $\Delta\phi>0$ |
| Linearity | $\Delta L_\mathrm{arm}$ and $\Delta\phi$ are linear in $h$ at first order |
| Scaling | $\Delta L_\mathrm{arm}\propto L_0$; $\Delta\phi\propto L_0/\lambda_0$ |
| Dimensions | $\Delta L_\mathrm{arm}$ in m; $\Delta\phi$ in rad |
| Two-route agreement | direct substitution (Section 10.3) and arm-by-arm evaluation (Section 10.4) agree exactly |
| Antisymmetry | $\delta L_x=-\delta L_y$, so the static background cancels exactly in $\Delta L_\mathrm{arm}$ |
| Equal-arm static limit | $L_x=L_y\Rightarrow\Delta\phi=0$, $I_\mathrm{bright}=I_0$, $I_\mathrm{dark}=0$ (Stage 1) |

**Higher-order note.** Retaining the cubic term of the expansion in Section 6.3, $(1\pm h)^{1/2}=1\pm\tfrac12h-\tfrac18h^2\pm\tfrac1{16}h^3+\dots$, the differential combination is

$$
\Delta L_\mathrm{arm}=L_0\big[(1+h)^{1/2}-(1-h)^{1/2}\big]=L_0\left(h+\tfrac18h^3+\dots\right).
$$

The $h^2$ terms cancel in the subtraction, so the first correction to $\Delta L_\mathrm{arm}=hL_0$ is of relative order $h^2/8\sim10^{-43}$ for $\lvert h\rvert\sim10^{-21}$. Nonlinear metric corrections are therefore negligible at the weak-field amplitudes considered. This is a magnitude statement under the stated expansion, not an exact treatment of the full nonlinear problem.

---

## 13. Frozen results and freeze policy

### 13.1 Freeze policy

The results registered below are **frozen** for the duration of Stage 2 literature validation, code audit, and numerical validation. None of these equations, sign conventions, or the Stage 1 conventions they inherit may be changed during that work. Any proposed change requires documented justification and a full rerun of the affected validation before re-adoption. The Stage 1 freeze continues to apply to the Stage 1 results unchanged.

### 13.2 Frozen register

This register is the canonical single list; derivations are in the sections cited.

| ID | Result | Section |
|---|---|---|
| F1 | $h(t)\equiv h_+(t)\equiv h_\mathrm{det}(t)$ in the aligned baseline | 4.6 |
| F2 | $\delta L_x=+\tfrac12hL_0,\ \ \delta L_y=-\tfrac12hL_0$ | 7 |
| F3 | $\Delta L_\mathrm{arm}\equiv L_x-L_y=h(t)L_0$ | 8.2 |
| F4 | $\Delta\phi(t)=(4\pi L_0/\lambda_0)\,h(t)$ | 10.3 |
| F5 | $G_\mathrm{phase,static}\approx4.724\times10^{10}$ rad/strain (4 km, 1064 nm) | 10.6 |

F3 and F4 hold under the explicit assumptions of Section 14.

---

## 14. Assumptions

| # | Assumption | Role | Required for $\Delta L_\mathrm{arm}=hL_0$? | If relaxed |
|---|---|---|---|---|
| A1 | Weak-field linearization, $\lvert h\rvert\ll1$ | Justifies dropping $\mathcal{O}(h^2)$ in the expansion | Yes | nonlinear metric terms must be retained |
| A2 | TT gauge | Fixes test-mass coordinates; proper distance is the sole physical variable | Yes (TT frame) | in Fermi-normal coordinates test masses experience tidal accelerations |
| A3 | Plane wave, overhead incidence, $\theta=0$ | Restricts perturbation to the transverse $x$–$y$ plane | Yes (special case) | oblique directions require $F_+(\theta,\phi,\psi)$, $F_\times(\theta,\phi,\psi)$ |
| A4 | Aligned plus polarization, $\phi=\psi=0$, $h_\times=0$ | Gives $F_+=1,\ F_\times=0$ | Yes (special case) | general polarizations couple $h_+$ and $h_\times$ into both arms |
| A5 | Orthogonal arms, $\zeta=90^\circ$ | Sets the geometry along $x$ and $y$ | Yes (special case) | non-orthogonal arms acquire an opening-angle factor $\sin\zeta$ |
| A6 | Equal nominal baselines, $L_{x,0}=L_{y,0}=L_0$ | Cancels the static background | Yes | arm asymmetry leaves a static macroscopic offset |
| A7 | Long-wavelength regime, $f_\mathrm{gw}\ll f^*$ (project criterion $\le0.1f^*$) | Spatially uniform strain; quasi-static transit | Yes | high frequencies need a frequency-dependent transfer factor |
| A8 | Differential convention $\Delta L\equiv L_x-L_y$ | Fixes $+\tfrac12-(-\tfrac12)=+1$ | Yes (for the sign of $+hL_0$) | reversed convention gives $-hL_0$ (Section 8.3) |

The optical assumptions of Stage 1 (monochromatic coherent field; ideal lossless 50:50 beamsplitter with the same matrix used for splitting and recombination; perfect end mirrors; single spatial mode with perfect overlap; scalar polarization; second input port vacuum; one-way arm-length convention) are inherited unchanged and apply to Sections 10.2–10.6.

---

## 15. Limitations and explicit exclusions

**Not included in this model:**

- **Finite-arm optical transit response.** At high frequency the response acquires a cardinal-sine transfer factor $C(f)=\mathrm{sinc}(\omega L_0/c)\,e^{-i\omega L_0/c}$ (needed for $f\ge0.1f^*$).
- **Resonant arm cavities.** Fabry–Pérot dynamics, including the cavity pole $K_-(f)\approx1/(1+if/f_p)$ and storage time.
- **Recycling cavities and asymmetries.** Power and signal recycling gains and Schnupp-asymmetry transfer functions.
- **Readout schemes.** DC length offsets, homodyne local-oscillator beating, and output-mode-cleaner transmission.
- **Non-orthogonal geometries.** Opening-angle factors (for example $\sin60^\circ=\sqrt3/2$ for triangular configurations) are named only and not derived.
- **General sky response.** Derivation of $F_+,F_\times$ and network response (Section 4.5).
- **Explicit light-travel-time calculation.** Fixed-time proper length is used under the LWA (Section 6.2); a full round-trip photon-time derivation is not performed.
- **Nonlinear and strong-field corrections** beyond the expansion note of Section 12.
- **Noise, loss, and mode-mismatch effects**, as excluded in Stage 1.

**Scope of the result.** This is an analytical derivation. It establishes self-consistency of the strain-to-phase chain under the stated assumptions. It is not empirical validation against detector data, and it does not assess the repository's existing strain model.

---

## 16. Derivation status and role in the validation workflow

### 16.1 Derivation-status classification

| Item | Class |
|---|---|
| Weak-field metric, TT-gauge conditions, polarization matrix | Established framework, adopted |
| $F_+,\ F_\times$ general forms | Stated, not derived |
| Aligned-baseline collapse ($F_+=1,\ F_\times=0$) | Brief justification (evaluation) |
| Line element at $z=0$ | Brief justification (specialization) |
| Proper-length integrals, LWA factoring, binomial expansion | Full derivation |
| Individual arm perturbations and signs | Full derivation |
| Differential response $\Delta L_\mathrm{arm}=hL_0$ | Full derivation |
| $\Delta L_\mathrm{rt}$, $\Delta\phi$ relations, port intensities | Inherited from Stage 1 |
| Master transfer $\Delta\phi=(4\pi L_0/\lambda_0)h$ | Derived by substitution |
| Static gain value | Arithmetic evaluation |

### 16.2 Role in the validation workflow

This analytical model is established independently of the repository code and of literature support. It is one part of the Stage 2 documentation set and serves as the physics reference for the following stages, which are deliberately distinct:

- **Analytical model (this document):** what physics is modelled and how it is derived.
- **Literature validation (Document 2):** what external scientific evidence supports the model, including reconciliation of conventions across sources.
- **Code and simulation audit (Document 3):** whether the repository implements the established physics, including whether the existing $h(t)\to\Delta L(t)$ toy-model simulation is physically justified and under what approximation.
- **Numerical validation:** whether the implementation reproduces the analytical expectations of Section 12.
- **Limitations and conclusion:** what has actually been established and where Stage 2 stops.

The analytical model remains an independent reference, not a retrospective description of the existing code.
