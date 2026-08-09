"""Compare Michelson interferometer operating points.

This experiment adds a static phase offset to a tiny gravitational-wave phase
perturbation and compares the resulting photodetector response.
"""

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


def run_operating_point_comparison(show_plots: bool = True) -> tuple[Path, Path]:
    """Compare GW response at different static phase offsets."""
    wavelength = 1064e-9
    input_intensity = 1.0

    arm_length = 1.0
    strain_amplitude = 1e-21
    gw_frequency = 100.0
    duration = 0.1
    sample_count = 10_000

    operating_points = (
        ("phi0 = 0", 0.0, "#1f77b4"),
        ("phi0 = pi/4", np.pi / 4.0, "#ff7f0e"),
        ("phi0 = pi/2", np.pi / 2.0, "#2ca02c"),
    )

    time = np.linspace(0.0, duration, sample_count)
    strain = sinusoidal_strain(time, strain_amplitude, gw_frequency)
    differential_displacement = arm_length * strain
    gw_phase = phase_difference(differential_displacement, wavelength)
    peak_gw_phase = np.max(np.abs(gw_phase))

    print("Interferometer operating point comparison")
    print(f"Laser wavelength: {wavelength:.3e} m")
    print(f"Arm length:       {arm_length:.3f} m")
    print(f"Strain amplitude: {strain_amplitude:.3e}")
    print(f"GW frequency:     {gw_frequency:.1f} Hz")
    print(f"Peak GW phase:    {peak_gw_phase:.3e} rad")
    print()

    results_dir = REPO_ROOT / "results"
    results_dir.mkdir(exist_ok=True)
    intensity_path = results_dir / "operating_point_intensity.png"
    response_path = results_dir / "operating_point_response.png"

    fig_intensity, ax_intensity = plt.subplots(figsize=(9, 5))
    fig_response, ax_response = plt.subplots(figsize=(9, 5))

    for label, static_phase, color in operating_points:
        phase = static_phase + gw_phase
        intensity = photodetector_intensity(phase, input_intensity)
        static_intensity = photodetector_intensity(static_phase, input_intensity)
        response = intensity - static_intensity
        linear_response = -0.5 * input_intensity * np.sin(static_phase) * gw_phase

        max_response = np.max(np.abs(response))
        max_linear_response = np.max(np.abs(linear_response))

        print(label)
        print(f"  Static intensity:          {static_intensity:.6f}")
        print(f"  Max numerical response:    {max_response:.3e}")
        print(f"  Max linear approximation:  {max_linear_response:.3e}")

        ax_intensity.plot(time, intensity, label=label, color=color, linewidth=2)
        ax_response.plot(time, response, label=label, color=color, linewidth=2)

    ax_intensity.set_title("Photodetector Output at Different Operating Points")
    ax_intensity.set_xlabel("Time (s)")
    ax_intensity.set_ylabel("Normalized photodetector intensity")
    ax_intensity.ticklabel_format(axis="y", style="plain", useOffset=False)
    ax_intensity.grid(True, alpha=0.3)
    ax_intensity.legend()
    fig_intensity.tight_layout()
    fig_intensity.savefig(intensity_path, dpi=180)

    ax_response.set_title("Small-Signal Response Around Each Operating Point")
    ax_response.set_xlabel("Time (s)")
    ax_response.set_ylabel("Intensity change from static intensity")
    ax_response.grid(True, alpha=0.3)
    ax_response.legend()
    fig_response.tight_layout()
    fig_response.savefig(response_path, dpi=180)

    if show_plots:
        plt.show()
    plt.close(fig_intensity)
    plt.close(fig_response)

    print()
    print(f"Saved intensity comparison: {intensity_path}")
    print(f"Saved response comparison:  {response_path}")
    return intensity_path, response_path


if __name__ == "__main__":
    run_operating_point_comparison()
