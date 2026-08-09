"""Inject a simple gravitational-wave strain into the interferometer model."""

from __future__ import annotations

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.gravitational_wave import sinusoidal_strain  # noqa: E402
from src.interferometer import phase_difference, photodetector_intensity  # noqa: E402


def _save_time_series_plot(
    time: np.ndarray,
    values: np.ndarray,
    title: str,
    ylabel: str,
    output_path: Path,
    color: str,
) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(time, values, color=color, linewidth=2)
    ax.set_title(title)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(output_path, dpi=180)
    return fig


def run_gravitational_wave_injection(show_plots: bool = True) -> tuple[Path, ...]:
    """Simulate h(t) -> Delta L(t) -> Delta phi(t) -> I(t)."""
    wavelength = 1064e-9
    input_intensity = 1.0

    arm_length = 1.0
    strain_amplitude = 1e-21
    gw_frequency = 100.0
    duration = 0.1
    sample_count = 10_000

    time = np.linspace(0.0, duration, sample_count)
    strain = sinusoidal_strain(time, strain_amplitude, gw_frequency)
    differential_displacement = arm_length * strain
    phase = phase_difference(differential_displacement, wavelength)
    intensity = photodetector_intensity(phase, input_intensity)
    intensity_change = intensity - input_intensity
    peak_phase_shift = np.max(np.abs(phase))
    small_angle_intensity_change = 0.25 * input_intensity * peak_phase_shift**2

    print("Gravitational-wave strain injection")
    print(f"Laser wavelength:       {wavelength:.3e} m")
    print(f"Arm length:             {arm_length:.3f} m")
    print(f"Strain amplitude:       {strain_amplitude:.3e}")
    print(f"GW frequency:           {gw_frequency:.1f} Hz")
    print(f"Peak Delta L:           {np.max(np.abs(differential_displacement)):.3e} m")
    print(f"Peak phase shift:       {peak_phase_shift:.3e} rad")
    print(f"Intensity change range: {np.min(intensity_change):.3e} to {np.max(intensity_change):.3e}")
    print(f"Small-angle estimate:   ~{small_angle_intensity_change:.3e} peak intensity drop")

    results_dir = REPO_ROOT / "results"
    results_dir.mkdir(exist_ok=True)

    strain_path = results_dir / "gw_injection_strain.png"
    displacement_path = results_dir / "gw_injection_displacement.png"
    phase_path = results_dir / "gw_injection_phase.png"
    intensity_path = results_dir / "gw_injection_intensity.png"

    figures = []
    figures.append(_save_time_series_plot(
        time,
        strain,
        "Injected Sinusoidal Gravitational-Wave Strain",
        "Strain h(t)",
        strain_path,
        "#1f77b4",
    ))
    figures.append(_save_time_series_plot(
        time,
        differential_displacement,
        "Differential Arm Displacement From Strain",
        "Differential displacement (m)",
        displacement_path,
        "#2ca02c",
    ))
    figures.append(_save_time_series_plot(
        time,
        phase,
        "Round-Trip Phase Shift From Strain",
        "Phase shift (rad)",
        phase_path,
        "#9467bd",
    ))

    fig_intensity, ax_intensity = plt.subplots(figsize=(9, 5))
    ax_intensity.plot(time, intensity, color="#d62728", linewidth=2)
    ax_intensity.set_title("Photodetector Output From GW Strain")
    ax_intensity.set_xlabel("Time (s)")
    ax_intensity.set_ylabel("Normalized photodetector intensity")
    ax_intensity.ticklabel_format(axis="y", style="plain", useOffset=False)
    ax_intensity.grid(True, alpha=0.3)
    fig_intensity.tight_layout()
    fig_intensity.savefig(intensity_path, dpi=180)
    figures.append(fig_intensity)

    if show_plots:
        plt.show()
    for figure in figures:
        plt.close(figure)

    output_paths = (strain_path, displacement_path, phase_path, intensity_path)
    for output_path in output_paths:
        print(f"Saved plot: {output_path}")

    return output_paths


if __name__ == "__main__":
    run_gravitational_wave_injection()
