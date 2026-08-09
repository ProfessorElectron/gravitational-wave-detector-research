"""Run the first ideal Michelson interferometer simulation.

The experiment sweeps differential arm displacement and plots the resulting
photodetector intensity fringe pattern.
"""

from __future__ import annotations

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.interferometer import (  # noqa: E402
    differential_arm_length,
    intensity_from_arm_lengths,
    phase_difference,
    photodetector_intensity,
)


def run_basic_sweep() -> Path:
    """Sweep differential arm length and save the first fringe plot."""
    wavelength = 1064e-9
    input_intensity = 1.0

    length_x = 1.0
    length_y = 1.0
    delta_l = differential_arm_length(length_x, length_y)
    phase = phase_difference(delta_l, wavelength)
    intensity = intensity_from_arm_lengths(
        length_x=length_x,
        length_y=length_y,
        wavelength=wavelength,
        input_intensity=input_intensity,
    )

    print("Michelson interferometer baseline")
    print(f"Laser wavelength: {wavelength:.3e} m")
    print(f"Arm X length:      {length_x:.6f} m")
    print(f"Arm Y length:      {length_y:.6f} m")
    print(f"Delta L:           {delta_l:.3e} m")
    print(f"Delta phase:       {phase:.3e} rad")
    print(f"Intensity:         {intensity:.6f}")

    sweep = np.linspace(-2.0 * wavelength, 2.0 * wavelength, 2000)
    sweep_phase = phase_difference(sweep, wavelength)
    sweep_intensity = photodetector_intensity(sweep_phase, input_intensity)

    results_dir = REPO_ROOT / "results"
    results_dir.mkdir(exist_ok=True)
    output_path = results_dir / "basic_interferometer_fringe.png"

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(sweep / wavelength, sweep_intensity, color="#1f77b4", linewidth=2)
    ax.set_title("Ideal Michelson Interferometer Fringe Pattern")
    ax.set_xlabel("Differential arm displacement / wavelength")
    ax.set_ylabel("Normalized photodetector intensity")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(output_path, dpi=180)
    plt.show()
    plt.close(fig)

    print(f"Saved plot: {output_path}")
    return output_path


if __name__ == "__main__":
    run_basic_sweep()
