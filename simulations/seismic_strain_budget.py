"""Calibrate the seismic displacement source into a strain PSD and ASD."""

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
    displacement_psd_to_strain,
    psd_to_asd,
    seismic_displacement_asd,
)


def run_seismic_strain_budget(show_plots: bool = True) -> Path:
    """Validate seismic displacement-to-strain calibration in the PSD domain."""
    effective_arm_length = 1.0
    reference_asd = 1e-9
    reference_frequency = 10.0
    exponent = 2.0
    minimum_frequency = 1.0
    maximum_frequency = 100.0

    frequencies = np.logspace(np.log10(minimum_frequency), np.log10(maximum_frequency), 500)
    displacement_asd = seismic_displacement_asd(
        frequencies,
        reference_asd,
        reference_frequency,
        exponent,
        minimum_frequency,
        maximum_frequency,
    )
    displacement_psd = asd_to_psd(displacement_asd)
    strain_psd = displacement_psd_to_strain(displacement_psd, effective_arm_length)
    strain_asd = psd_to_asd(strain_psd)
    direct_strain_asd = displacement_asd_to_strain(displacement_asd, effective_arm_length)

    displacement_slope, _ = np.polyfit(np.log10(frequencies), np.log10(displacement_asd), 1)
    strain_slope, _ = np.polyfit(np.log10(frequencies), np.log10(strain_asd), 1)
    psd_check = np.allclose(displacement_asd**2, displacement_psd, rtol=1e-12, atol=0.0)
    psd_check &= np.allclose(strain_asd**2, strain_psd, rtol=1e-12, atol=0.0)
    calibration_check = np.allclose(strain_asd, direct_strain_asd, rtol=1e-12, atol=0.0)

    print("Seismic strain calibration")
    print("--------------------------")
    print(f"Frequency range:       {minimum_frequency:.0f}-{maximum_frequency:.0f} Hz")
    print(f"Effective arm length:  {effective_arm_length:.3f} m")
    print(f"Model exponent:        {-exponent:.3f}")
    print(f"Fitted displacement:   {displacement_slope:.3f}")
    print(f"Fitted strain:         {strain_slope:.3f}")
    print(f"ASD squared = PSD:     {'PASS' if psd_check else 'FAIL'}")
    print(f"Calibration:           {'PASS' if calibration_check else 'FAIL'}")

    results_dir = REPO_ROOT / "results"
    results_dir.mkdir(exist_ok=True)
    output_path = results_dir / "seismic_strain_budget.png"

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].loglog(frequencies, displacement_asd, color="#8c564b")
    axes[0].set_title("Seismic Displacement ASD")
    axes[0].set_xlabel("Frequency (Hz)")
    axes[0].set_ylabel("Displacement ASD (m / sqrt(Hz))")
    axes[0].grid(True, which="both", alpha=0.3)

    axes[1].loglog(frequencies, strain_asd, color="#d62728")
    axes[1].set_title("Calibrated Equivalent Strain ASD")
    axes[1].set_xlabel("Frequency (Hz)")
    axes[1].set_ylabel("Strain ASD (1 / sqrt(Hz))")
    axes[1].grid(True, which="both", alpha=0.3)

    fig.suptitle("Seismic Displacement Noise Through Effective Arm-Length Calibration")
    fig.tight_layout()
    fig.savefig(output_path, dpi=180)

    if show_plots:
        plt.show()
    plt.close(fig)

    print(f"Saved calibrated strain plot: {output_path}")
    return output_path


if __name__ == "__main__":
    run_seismic_strain_budget()
