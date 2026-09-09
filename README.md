# Gravitational Wave Detector Research

## Overview

This repository documents an ongoing research project exploring gravitational-
wave detection through theoretical study, mathematical modelling, computational
simulation, signal processing, and experimental development.

The current focus is a modular Michelson interferometer model, extended step by
step toward gravitational-wave signal analysis and detector-noise modelling.
The long-term goal is a reproducible research framework inspired by ground-
based detectors such as LIGO, with later exploration of space-based concepts
such as LISA.

The project combines:

- Gravitational-wave physics
- Michelson interferometer modelling
- Numerical simulation
- Signal processing and frequency-domain analysis
- Detector-noise modelling
- Experimental interferometry
- Future space-based detector studies

## Objectives

- Develop a strong understanding of gravitational-wave physics and
  interferometric detection.
- Build and validate a computational Michelson interferometer model.
- Simulate detector responses to gravitational-wave signals.
- Study signal-to-noise behaviour and frequency-domain characteristics.
- Develop physically motivated detector-noise models.
- Validate against established models and public gravitational-wave data.
- Design and construct a tabletop Michelson interferometer.
- Explore a conceptual space-based interferometric detector.

## Research Roadmap

1. Literature Review and Physics Foundations
2. Mathematical Modelling
3. Computational Interferometer Simulation
4. Signal Processing and Noise Analysis
5. Validation Using Public LIGO Data
6. Experimental Tabletop Interferometer
7. Conceptual Space-Based Detector Study
8. Technical Report and Research Publication

## Current Status

**Current phase:** Phase 4 - Signal Processing and Noise Analysis

### Completed

- Basic Michelson interferometer model
- Time-dependent interferometer response
- Gravitational-wave strain injection
- Operating-point analysis
- Controlled Gaussian measurement noise and RMS SNR analysis
- FFT, PSD, ASD, windowed FFT, and Welch spectral analysis
- Measurement-noise spectral scaling analysis
- Physical detector-noise architecture
- Simplified seismic noise model and displacement-to-strain calibration
- Combined seismic and idealized shot-noise strain budget

### Next

- External validation against pyGWINC
- Improved gravitational-wave detector response
- Public LIGO data analysis
- Signal injection and recovery
- Tabletop Michelson interferometer
- Conceptual space-based detector modelling

## Current Detector Model

The present computational model follows the simplified chain:

```text
h(t)
 ↓
Delta L(t)
 ↓
Delta phi(t)
 ↓
I(t)
```

Gravitational-wave strain is converted into differential arm displacement,
interferometer phase response, and photodetector output. Current simulations
generally use a 1064 nm laser wavelength and a 1 m effective arm length.

The response is deliberately simplified. Future work will add a fuller
treatment of gravitational-wave polarizations, source direction, detector
geometry, and antenna response.

## Physical Noise Model

The current physical-noise framework contains a simplified seismic displacement
source and an idealized photodetector shot-noise source. Seismic noise is
calibrated into the strain domain before combination.

Independent sources are combined through their power spectral densities, not by
adding ASDs directly:

```text
S_total(f) = S_seismic(f) + S_shot(f)
ASD_total(f) = sqrt(S_total(f))
```

The current two-source budget validates:

```text
PSD addition                  : PASS
ASD squared = PSD             : PASS
Direct ASD addition differs   : PASS
Seismic/shot crossover        : 57.480 Hz
Maximum ASD addition error    : 41.4%
```

The shot-noise term uses a 10 pA reference photocurrent as a pedagogical
low-light example. It excludes radiation-pressure noise, optical cavity
effects, squeezing, and quantum correlations. The seismic source is a bounded
power-law model, not a realistic LIGO seismic spectrum.

## Repository Structure

```text
README.md
requirements.txt
src/          Reusable interferometer, spectral, and physical-noise tools
simulations/  Runnable validation experiments
results/      Generated figures
docs/         Model and architecture notes
papers/       Research references
```

## Running Simulations

Run commands from the repository root. Generated figures are saved in
`results/`.

Basic Michelson interferometer:

```powershell
python simulations/basic_interferometer.py
```

Time-dependent response and gravitational-wave injection:

```powershell
python simulations/time_dependent_interferometer.py
python simulations/gravitational_wave_injection.py
python simulations/operating_point.py
```

Measurement-noise and SNR analysis:

```powershell
python simulations/noisy_detector.py
python simulations/snr_analysis.py
```

Frequency-domain analysis:

```powershell
python simulations/frequency_analysis.py
python simulations/welch_analysis.py
python simulations/noise_spectrum.py
```

Physical-noise analysis:

```powershell
python simulations/seismic_noise.py
python simulations/seismic_strain_budget.py
python simulations/physical_noise_budget.py
```

## Validation Path

```text
Theory
 ↓
Mathematical model
 ↓
Numerical implementation
 ↓
Internal validation
 ↓
Spectral analysis
 ↓
Physical-noise modelling
 ↓
External validation
 ↓
Public detector data
 ↓
Experimental validation
```

The next major step is comparison with an established detector-noise modelling
framework, particularly pyGWINC. The current model does not reproduce the full
behaviour of a gravitational-wave detector.

## Current Limitations

- Simplified gravitational-wave response
- No full polarization or antenna-pattern treatment
- No optical cavity model
- Simplified quantum and seismic noise
- No thermal or Newtonian noise model
- No suspension dynamics or complete detector calibration

These limitations are part of the planned development roadmap.

## License

This project is licensed under the MIT License.
