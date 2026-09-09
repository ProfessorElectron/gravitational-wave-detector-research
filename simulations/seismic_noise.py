"""Validate a bounded power-law seismic displacement-noise model."""

from __future__ import annotations

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.physical_noise import (  # noqa: E402
    asd_to_psd,
    displacement_asd_to_strain,
    seismic_displacement_asd,
)


def run_seismic_noise_simulation(show_plots: bool = True) -> Path:
    """Generate and calibrate the first bounded frequency-dependent noise ASD."""
    arm_length = 1.0
    reference_asd = 1e-9
    reference_frequency = 10.0
    exponent = 2.0
    minimum_frequency = 1.0
    maximum_frequency = 100.0
    sample_count = 500

    frequencies = np.logspace(
        np.log10(minimum_frequency),
        np.log10(maximum_frequency),
        sample_count,
    )
    displacement_asd = seismic_displacement_asd(
        frequencies,
        reference_asd,
        reference_frequency,
        exponent,
        minimum_frequency,
        maximum_frequency,
    )
    displacement_psd = asd_to_psd(displacement_asd)
    strain_asd = displacement_asd_to_strain(displacement_asd, arm_length)
    fitted_slope, _ = np.polyfit(np.log10(frequencies), np.log10(displacement_asd), 1)

    print("Bounded seismic-noise model")
    print(f"Reference displacement ASD: {reference_asd:.3e} m / sqrt(Hz)")
    print(f"Reference frequency:        {reference_frequency:.1f} Hz")
    print(f"Power-law exponent:         {exponent:.3f}")
    print(f"Valid frequency range:      {minimum_frequency:.1f} to {maximum_frequency:.1f} Hz")
    print(f"Arm length:                 {arm_length:.3f} m")
    print(f"Expected ASD slope:         {-exponent:.3f}")
    print(f"Fitted ASD slope:           {fitted_slope:.3f}")
    print(f"ASD squared equals PSD:     {np.allclose(displacement_asd**2, displacement_psd, rtol=1e-12, atol=0.0)}")
    print(f"Strain PSD units:           1 / Hz")

    results_dir = REPO_ROOT / "results"
    results_dir.mkdir(exist_ok=True)
    output_path = results_dir / "seismic_noise.png"

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].loglog(frequencies, displacement_asd, color="#8c564b")
    axes[0].set_title("Bounded Seismic Displacement ASD")
    axes[0].set_xlabel("Frequency (Hz)")
    axes[0].set_ylabel("Displacement ASD (m / sqrt(Hz))")
    axes[0].grid(True, which="both", alpha=0.3)

    axes[1].loglog(frequencies, strain_asd, color="#d62728")
    axes[1].set_title("Equivalent Strain ASD")
    axes[1].set_xlabel("Frequency (Hz)")
    axes[1].set_ylabel("Strain ASD (1 / sqrt(Hz))")
    axes[1].grid(True, which="both", alpha=0.3)

    fig.suptitle("Simplified Seismic Noise: Displacement to Strain Calibration")
    fig.tight_layout()
    fig.savefig(output_path, dpi=180)

    if show_plots:
        plt.show()
    plt.close(fig)

    print(f"Saved seismic-noise plot: {output_path}")
    return output_path


if __name__ == "__main__":
    run_seismic_noise_simulation()
