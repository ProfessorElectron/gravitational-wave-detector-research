# Gravitational Wave Detector Research


## Overview

This repository documents an interdisciplinary research initiative exploring the principles of gravitational wave detection through theoretical study, computational modelling, signal processing, and the development of a tabletop Michelson interferometer prototype.

The long-term vision is to create a research platform inspired by detectors such as LIGO and future space-based observatories like LISA, while providing an accessible framework for studying interferometric gravitational-wave detection.

The project combines:

- Gravitational wave physics
- Michelson interferometer simulation
- Signal processing
- Noise analysis
- Tabletop experimental interferometer
- Future conceptual space-based detector studies

---

## Objectives

- Develop a rigorous understanding of gravitational wave physics and interferometric detection principles.
- Develop a mathematical and computational model of a Michelson interferometer.
- Simulate detector responses to gravitational wave signals under realistic noise conditions.
- Implement signal-processing techniques including filtering, Fourier analysis, and matched filtering.
- Validate computational methods using publicly available gravitational wave data.
- Design and construct a tabletop Michelson interferometer as an experimental prototype.
- Investigate the feasibility of a conceptual space-based interferometric mission inspired by LISA.

---

## Research Roadmap

### Phase 1
Literature Review and Physics Foundations

### Phase 2
Mathematical Modelling

### Phase 3
Computational Interferometer Simulation

### Phase 4
Signal Processing and Noise Analysis

### Phase 5
Validation Using Public LIGO Data

### Phase 6
Experimental Tabletop Interferometer

### Phase 7
Conceptual Space-Based Detector Study

### Phase 8
Technical Report and Research Publication

---

## Current Status

**Current Phase**

Phase 2/3 - Mathematical Modelling & Computational Interferometer Simulation

**Timeline**

30 July 2026 onward

**Current Focus**

- Implementing the minimal Michelson interferometer model
- Calculating differential arm length, phase difference, and detector intensity
- Sweeping differential displacement to generate the first fringe pattern

---

## Repository Structure

README.md
requirements.txt
src/
simulations/
analysis/
data/
results/
docs/
papers/

Run the first simulation:

```powershell
python simulations/basic_interferometer.py
```

The plot is saved to `results/basic_interferometer_fringe.png`.

Run the first time-dependent simulation:

```powershell
python simulations/time_dependent_interferometer.py
```

The displacement and photodetector output plots are saved in `results/`.

---

## License

This project is licensed under the MIT License.
