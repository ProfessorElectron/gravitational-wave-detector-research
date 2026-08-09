"""Run a time-dependent Michelson interferometer simulation.

This experiment injects an artificial sinusoidal differential displacement and
plots the displacement and photodetector response over time.
"""

from __future__ import annotations

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.interferometer import phase_difference, photodetector_intensity  # noqa: E402


def run_time_dependent_simulation(show_plots: bool = True) -> tuple[Path, Path]:
    """Simulate Delta L(t) -> Delta phi(t) -> I(t)."""
    wavelength = 1064e-9
    input_intensity = 1.0

    amplitude = 1e-9
    frequency = 100.0
    duration = 0.1
    sample_count = 10_000

    time = np.linspace(0.0, duration, sample_count)
    differential_displacement = amplitude * np.sin(2.0 * np.pi * frequency * time)
    phase = phase_difference(differential_displacement, wavelength)
    intensity = photodetector_intensity(phase, input_intensity)

    print("Time-dependent Michelson interferometer")
    print(f"Laser wavelength:       {wavelength:.3e} m")
    print(f"Displacement amplitude: {amplitude:.3e} m")
    print(f"Displacement frequency: {frequency:.1f} Hz")
    print(f"Duration:               {duration:.3f} s")
    print(f"Samples:                {sample_count}")
    print(f"Peak phase shift:       {np.max(np.abs(phase)):.3e} rad")
    print(f"Intensity range:        {np.min(intensity):.6f} to {np.max(intensity):.6f}")

    results_dir = REPO_ROOT / "results"
    results_dir.mkdir(exist_ok=True)
    displacement_path = results_dir / "time_dependent_displacement.png"
    intensity_path = results_dir / "time_dependent_intensity.png"

    fig_displacement, ax_displacement = plt.subplots(figsize=(9, 5))
    ax_displacement.plot(
        time,
        differential_displacement,
        color="#1f77b4",
        linewidth=2,
    )
    ax_displacement.set_title("Artificial Differential Arm Displacement")
    ax_displacement.set_xlabel("Time (s)")
    ax_displacement.set_ylabel("Differential displacement (m)")
    ax_displacement.grid(True, alpha=0.3)
    fig_displacement.tight_layout()
    fig_displacement.savefig(displacement_path, dpi=180)

    fig_intensity, ax_intensity = plt.subplots(figsize=(9, 5))
    ax_intensity.plot(time, intensity, color="#d62728", linewidth=2)
    ax_intensity.set_title("Time-Dependent Photodetector Output")
    ax_intensity.set_xlabel("Time (s)")
    ax_intensity.set_ylabel("Normalized photodetector intensity")
    ax_intensity.ticklabel_format(axis="y", style="plain", useOffset=False)
    ax_intensity.grid(True, alpha=0.3)
    fig_intensity.tight_layout()
    fig_intensity.savefig(intensity_path, dpi=180)

    if show_plots:
        plt.show()
    plt.close(fig_displacement)
    plt.close(fig_intensity)

    print(f"Saved displacement plot: {displacement_path}")
    print(f"Saved intensity plot:    {intensity_path}")
    return displacement_path, intensity_path


if __name__ == "__main__":
    run_time_dependent_simulation()
