"""Build the first two-source physical strain-noise budget."""

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
    displacement_psd_to_strain,
    psd_to_asd,
    seismic_displacement_asd,
    shot_noise_strain_asd,
    total_psd,
)


def run_physical_noise_budget(show_plots: bool = True) -> Path:
    """Combine seismic and idealized photon shot noise in the strain domain."""
    wavelength = 1064e-9
    effective_arm_length = 1.0
    photocurrent = 1e-11
    elementary_charge = 1.602176634e-19

    reference_asd = 1e-9
    reference_frequency = 10.0
    seismic_exponent = 2.0
    minimum_frequency = 1.0
    maximum_frequency = 100.0

    frequencies = np.logspace(np.log10(minimum_frequency), np.log10(maximum_frequency), 500)

    seismic_asd_displacement = seismic_displacement_asd(
        frequencies,
        reference_asd,
        reference_frequency,
        seismic_exponent,
        minimum_frequency,
        maximum_frequency,
    )
    seismic_displacement_psd = asd_to_psd(seismic_asd_displacement)
    seismic_strain_psd = displacement_psd_to_strain(
        seismic_displacement_psd,
        effective_arm_length,
    )
    seismic_strain_asd = psd_to_asd(seismic_strain_psd)

    shot_strain_asd = shot_noise_strain_asd(
        frequencies,
        wavelength,
        effective_arm_length,
        photocurrent,
        elementary_charge,
    )
    shot_strain_psd = asd_to_psd(shot_strain_asd)

    combined_strain_psd = total_psd(seismic_strain_psd, shot_strain_psd)
    combined_strain_asd = psd_to_asd(combined_strain_psd)
    incorrect_asd_sum = seismic_strain_asd + shot_strain_asd

    crossover_index = int(np.argmin(np.abs(np.log10(seismic_strain_asd / shot_strain_asd))))
    crossover_frequency = float(frequencies[crossover_index])
    psd_sum_check = np.allclose(
        combined_strain_psd,
        seismic_strain_psd + shot_strain_psd,
        rtol=1e-12,
        atol=0.0,
    )
    asd_check = np.allclose(combined_strain_asd**2, combined_strain_psd, rtol=1e-12, atol=0.0)
    direct_asd_sum_differs = not np.allclose(
        incorrect_asd_sum,
        combined_strain_asd,
        rtol=1e-12,
        atol=0.0,
    )
    maximum_direct_sum_error = np.max(incorrect_asd_sum / combined_strain_asd - 1.0)

    print("Two-source physical strain-noise budget")
    print("--------------------------------------")
    print("Seismic source: displacement ASD in m / sqrt(Hz), then calibrated to strain")
    print("Shot source:    idealized photodetector shot-noise strain ASD in 1 / sqrt(Hz)")
    print(f"Frequency range:       {minimum_frequency:.0f}-{maximum_frequency:.0f} Hz")
    print(f"Seismic exponent:      {-seismic_exponent:.3f}")
    print(f"Wavelength:            {wavelength:.3e} m")
    print(f"Effective arm length:  {effective_arm_length:.3f} m")
    print(f"Reference photocurrent:{photocurrent:.3e} A")
    print(f"Shot-noise ASD:        {shot_strain_asd[0]:.3e} 1 / sqrt(Hz)")
    print(f"Nearest crossover:     {crossover_frequency:.3f} Hz")
    print(f"PSD sum:               {'PASS' if psd_sum_check else 'FAIL'}")
    print(f"ASD squared = PSD:     {'PASS' if asd_check else 'FAIL'}")
    print(f"Direct ASD sum differs:{'PASS' if direct_asd_sum_differs else 'FAIL'}")
    print(f"Largest direct-sum error: {maximum_direct_sum_error:.3f}")

    results_dir = REPO_ROOT / "results"
    results_dir.mkdir(exist_ok=True)
    output_path = results_dir / "physical_noise_budget.png"

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    axes[0].loglog(frequencies, seismic_strain_asd, label="Seismic strain ASD", color="#8c564b")
    axes[0].loglog(frequencies, shot_strain_asd, label="Idealized shot-noise ASD", color="#1f77b4")
    axes[0].loglog(frequencies, combined_strain_asd, label="Correct total ASD", color="#2ca02c", linewidth=2)
    axes[0].loglog(frequencies, incorrect_asd_sum, "--", label="Incorrect direct ASD sum", color="#d62728")
    axes[0].axvline(crossover_frequency, color="#111111", linestyle=":", label="Nearest crossover")
    axes[0].set_title("Strain ASD Budget")
    axes[0].set_xlabel("Frequency (Hz)")
    axes[0].set_ylabel("Strain ASD (1 / sqrt(Hz))")
    axes[0].grid(True, which="both", alpha=0.3)
    axes[0].legend()

    axes[1].loglog(frequencies, seismic_strain_psd, label="Seismic strain PSD", color="#8c564b")
    axes[1].loglog(frequencies, shot_strain_psd, label="Shot-noise strain PSD", color="#1f77b4")
    axes[1].loglog(frequencies, combined_strain_psd, label="Total strain PSD", color="#2ca02c", linewidth=2)
    axes[1].set_title("PSD Addition in the Common Strain Domain")
    axes[1].set_xlabel("Frequency (Hz)")
    axes[1].set_ylabel("Strain PSD (1 / Hz)")
    axes[1].grid(True, which="both", alpha=0.3)
    axes[1].legend()

    fig.suptitle("Seismic Plus Idealized Quantum Shot Noise")
    fig.tight_layout()
    fig.savefig(output_path, dpi=180)

    if show_plots:
        plt.show()
    plt.close(fig)

    print(f"Saved physical-noise budget: {output_path}")
    return output_path


if __name__ == "__main__":
    run_physical_noise_budget()
