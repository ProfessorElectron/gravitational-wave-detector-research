"""Sweep Gaussian noise levels and estimate RMS SNR."""

from __future__ import annotations

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.gravitational_wave import sinusoidal_strain  # noqa: E402
from src.interferometer import phase_difference  # noqa: E402
from src.noise import add_gaussian_noise  # noqa: E402
from src.signal_analysis import rms_snr  # noqa: E402


def run_snr_analysis(show_plots: bool = True) -> Path:
    """Estimate SNR for a known injected signal across noise levels."""
    wavelength = 1064e-9
    input_intensity = 1.0

    arm_length = 1.0
    static_phase = np.pi / 2.0
    strain_amplitude = 1e-21
    gw_frequency = 100.0
    duration = 0.1
    sample_count = 10_000

    noise_levels = np.array((1e-7, 3e-7, 1e-6, 3e-6, 1e-5, 3e-5, 1e-4))
    random_seed = 12345

    time = np.linspace(0.0, duration, sample_count)
    strain = sinusoidal_strain(time, strain_amplitude, gw_frequency)
    differential_displacement = arm_length * strain
    gw_phase = phase_difference(differential_displacement, wavelength)

    signal_response = -0.5 * input_intensity * np.sin(static_phase) * gw_phase

    signal_rms_values = []
    noise_rms_values = []
    snr_values = []

    print("RMS SNR analysis")
    print(f"Operating point:  pi/2")
    print(f"Arm length:       {arm_length:.3f} m")
    print(f"Strain amplitude: {strain_amplitude:.3e}")
    print(f"GW frequency:     {gw_frequency:.1f} Hz")
    print(f"Peak GW phase:    {np.max(np.abs(gw_phase)):.3e} rad")
    print(f"Random seed:      {random_seed}")
    print()

    for index, noise_standard_deviation in enumerate(noise_levels):
        measured_response = add_gaussian_noise(
            signal_response,
            standard_deviation=float(noise_standard_deviation),
            seed=random_seed + index,
        )
        signal_rms, noise_rms, snr = rms_snr(signal_response, measured_response)

        signal_rms_values.append(signal_rms)
        noise_rms_values.append(noise_rms)
        snr_values.append(snr)

        print(f"sigma = {noise_standard_deviation:.1e}")
        print(f"  signal RMS: {signal_rms:.3e}")
        print(f"  noise RMS:  {noise_rms:.3e}")
        print(f"  SNR:        {snr:.3e}")

    signal_rms_values = np.array(signal_rms_values)
    noise_rms_values = np.array(noise_rms_values)
    snr_values = np.array(snr_values)
    expected_snr = signal_rms_values[0] / noise_levels

    results_dir = REPO_ROOT / "results"
    results_dir.mkdir(exist_ok=True)
    output_path = results_dir / "snr_vs_noise.png"

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.loglog(
        noise_levels,
        snr_values,
        marker="o",
        linewidth=2,
        label="Measured RMS SNR",
    )
    ax.loglog(
        noise_levels,
        expected_snr,
        linestyle="--",
        linewidth=2,
        label="Expected 1/sigma scaling",
    )
    ax.set_title("RMS SNR vs Gaussian Measurement Noise")
    ax.set_xlabel("Noise standard deviation")
    ax.set_ylabel("SNR")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_path, dpi=180)

    if show_plots:
        plt.show()
    plt.close(fig)

    print()
    print(f"Saved SNR plot: {output_path}")
    return output_path


if __name__ == "__main__":
    run_snr_analysis()

