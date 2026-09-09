# Milestone 8A: Physical Noise Architecture

## Purpose

The current detector model uses additive white Gaussian readout noise. This
document defines the contract for replacing that toy model with independent,
frequency-dependent physical noise terms. The first seismic source and an
idealized quantum shot-noise term now implement this contract.

The first implementation will be a simplified seismic displacement noise model.
Quantum, thermal, and Newtonian terms will be added only after their parameters
and calibration domain are defined.

## Common frequency grid and units

Every noise function receives a strictly positive frequency array in Hz and
returns a one-sided PSD. Source terms may be modeled in one of three domains:

| Domain | PSD units | Use |
| --- | --- | --- |
| Readout | intensity squared / Hz | Existing simulated photodetector output |
| Displacement | m squared / Hz | Mechanical and environmental disturbances |
| Strain | 1 / Hz | Detector sensitivity and pyGWINC comparison |

ASD is always the square root of the PSD. ASDs are not added directly. For
independent sources in a common domain:

```text
S_total(f) = sum(S_i(f))
ASD_total(f) = sqrt(S_total(f))
```

Each source must declare its output domain. Terms in different domains must be
calibrated before they are combined.

## Detector calibration contract

At the existing pi/2 operating point, the linearized readout response is:

```text
R_output_per_strain = -0.5 * I0 * sin(phi0) * (4 * pi * L / lambda)
```

For the current ideal Michelson model this is frequency-independent. It maps
strain to readout intensity change. The corresponding conversions are:

```text
ASD_strain(f) = ASD_readout(f) / abs(R_output_per_strain)
ASD_readout(f) = abs(R_output_per_strain) * ASD_strain(f)

ASD_strain(f) = ASD_displacement(f) / L
```

The last expression follows from the simplified differential-arm relation
Delta L = L h. Future cavity and control models may replace the constant
response with a frequency-dependent transfer function.

## Source specification

| Source | Physical origin | Initial native domain | Required parameters before implementation | pyGWINC comparison term |
| --- | --- | --- | --- | --- |
| Seismic | Ground displacement coupled through isolation and suspension | Displacement | reference ASD, reference frequency, power-law exponent, valid frequency range, low-frequency cutoff | Seismic |
| Newtonian | Gravity-gradient force from nearby moving mass | Displacement or strain | site density, ground-motion spectrum, wave speed, test-mass height, coupling geometry | Newtonian / gravity-gradient |
| Suspension thermal | Mechanical loss in suspension fibers and modes | Displacement | temperature, test-mass properties, fiber geometry, loss model, suspension resonances | Suspension Thermal |
| Coating thermal | Brownian and thermo-optic coating fluctuations | Displacement | temperature, coating material loss, layer design, beam radius, substrate properties | Coating Brownian and Coating Thermo-Optic |
| Substrate thermal | Brownian and thermo-elastic substrate fluctuations | Displacement | temperature, substrate material, beam radius, loss model | Substrate Brownian and Substrate Thermo-Elastic |
| Quantum | Shot noise and radiation-pressure noise of the optical readout | Strain or readout | laser wavelength, circulating power, arm/cavity parameters, test-mass mass, squeezing and readout settings | Quantum |
| Residual gas | Refractive-index fluctuations from residual gas | Strain or displacement | pressure, gas composition, temperature, beam geometry | Excess Gas |

The listed pyGWINC names are comparison labels, not equations to copy. Our
implementation must state its assumptions and units separately.

## First source: simplified seismic noise

The first source is deliberately a parameterized model, not a claim of
Advanced-LIGO realism:

```text
ASD_seismic_displacement(f) = A_ref * (f / f_ref)^(-n)
S_seismic_displacement(f) = ASD_seismic_displacement(f)^2
```

Parameters:

| Parameter | Units | Meaning |
| --- | --- | --- |
| `reference_asd` | m / sqrt(Hz) | Displacement ASD at the reference frequency |
| `reference_frequency` | Hz | Frequency at which `reference_asd` is specified |
| `exponent` | dimensionless | Power-law falloff exponent |
| `minimum_frequency` | Hz | Lower validity limit; prevents an unphysical f = 0 singularity |
| `maximum_frequency` | Hz | Upper validity limit for the simplified model |

The 8B validation must show a non-flat displacement ASD with log-log slope
approximately `-exponent`, and a strain ASD obtained by division by arm length.

## Idealized quantum shot-noise term

The first quantum contribution is an ideal photodetector shot-noise model,
calibrated directly into strain:

```text
ASD_shot_strain = lambda / (2 * pi * L_eff) * sqrt(2 * e / I_photo)
```

It is frequency-independent in this model. `I_photo` is a photocurrent in A
and `e` is the elementary charge in C. This is not a full interferometer
quantum-noise model: it excludes radiation-pressure noise, squeezing, cavity
response, and quantum correlations.

## Planned software boundary

The physical-noise layer has these roles:

```text
physical_noise.py
  seismic_displacement_asd(frequency, parameters) -> ASD in m / sqrt(Hz)
  shot_noise_strain_asd(frequency, parameters) -> ASD in 1 / sqrt(Hz)
  asd_to_psd(asd) -> PSD in corresponding squared units
  psd_to_asd(psd) -> ASD in corresponding root units
  displacement_psd_to_strain(psd, arm_length) -> PSD in 1 / Hz
  total_psd(*source_psds) -> PSD in a shared domain
  displacement_asd_to_strain(asd, arm_length) -> ASD in 1 / sqrt(Hz)
  readout_asd_to_strain(asd, response) -> ASD in 1 / sqrt(Hz)
```

The implementation will validate array shape, finite non-negative PSD values,
strictly positive frequencies, and matching domains before summation.

## pyGWINC comparison plan

pyGWINC is a noise-budget calculator with source traces and calibrated total
PSD/ASD output. It provides canonical detector budgets, including aLIGO, A+,
Voyager, and Cosmic Explorer variants. Its budget interface distinguishes a
noise source from a calibration and combines them into a final budget.

Our comparison workflow will be:

1. Select and record one pyGWINC detector configuration and its parameter file.
2. Use the same positive frequency grid in both tools.
3. Compare source shapes and total sensitivity only in strain PSD or strain ASD.
4. Record any deliberately simplified assumptions, rather than treating an
   agreement in curve shape as full physical equivalence.
5. Keep pyGWINC as an external reference calculation, not a dependency of the
   first seismic implementation.

## Milestone 8A acceptance criteria

- Every source has a stated physical origin, domain, units, and required parameters.
- PSD summation occurs only after calibration into a common domain.
- The readout-to-strain calibration is explicit and tied to the existing pi/2 model.
- The first seismic model has defined parameters and a bounded valid frequency range.
- pyGWINC comparison is planned at the calibrated strain-spectrum level.
