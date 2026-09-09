"""Measure how white Gaussian measurement noise scales in the frequency domain."""

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
from src.spectral_analysis import welch_amplitude_spectral_density  # noqa: E402


def run_noise_spectrum_analysis(show_plots: bool = True) -> tuple[Path, Path]:
    """Compare Welch ASD floors across controlled Gaussian noise levels."""
    wavelength = 1064e-9
    input_intensity = 1.0
    arm_length = 1.0
    static_phase = np.pi / 2.0
    strain_amplitude = 1e-21
    gw_frequency = 100.0

    sampling_rate = 4096.0
    duration = 4.0
    segment_length = 4096
    overlap = 0.5
    sample_count = int(sampling_rate * duration)
    noise_levels = np.array((1e-7, 3e-7, 1e-6, 3e-6, 1e-5, 3e-5, 1e-4))
    random_seed = 12345

    time = np.arange(sample_count) / sampling_rate
    strain = sinusoidal_strain(time, strain_amplitude, gw_frequency)
    differential_displacement = arm_length * strain
    gw_phase = phase_difference(differential_displacement, wavelength)
    clean_response = -0.5 * input_intensity * np.sin(static_phase) * gw_phase

    asd_curves, floor_values = [], []
    frequencies: np.ndarray | None = None

    for index, noise_standard_deviation in enumerate(noise_levels):
        measured_response = add_gaussian_noise(
            clean_response,
            standard_deviation=float(noise_standard_deviation),
            seed=random_seed + index,
        )
        current_frequencies, asd = welch_amplitude_spectral_density(
            measured_response,
            sampling_rate,
            segment_length=segment_length,
            overlap=overlap,
        )
        floor_band = (20.0 < current_frequencies) & (current_frequencies < 80.0)
        asd_curves.append(asd)
        floor_values.append(float(np.median(asd[floor_band])))
        frequencies = current_frequencies

    if frequencies is None:
        raise RuntimeError("No ASD curves were calculated")

    floor_values = np.asarray(floor_values)
    scaling_slope, scaling_intercept = np.polyfit(
        np.log10(noise_levels),
        np.log10(floor_values),
        deg=1,
    )
    fitted_floor = 10.0 ** (scaling_intercept + scaling_slope * np.log10(noise_levels))
    expected_floor = noise_levels * np.sqrt(2.0 / sampling_rate)
    nonzero = frequencies > 0.0

    print("Frequency-domain noise scaling analysis")
    print(f"Injected GW frequency:      {gw_frequency:.1f} Hz")
    print(f"ASD floor band:              20 Hz < f < 80 Hz")
    print(f"Welch segment resolution:    {sampling_rate / segment_length:.3f} Hz")
    print(f"Log-log ASD-floor slope:     {scaling_slope:.3f}")
    print()
    for noise_standard_deviation, floor in zip(noise_levels, floor_values):
        print(f"sigma = {noise_standard_deviation:.1e}  median ASD floor = {floor:.3e} intensity units / sqrt(Hz)")

    results_dir = REPO_ROOT / "results"
    results_dir.mkdir(exist_ok=True)
    asd_output_path = results_dir / "noise_spectrum_asd.png"
    scaling_output_path = results_dir / "noise_spectrum_scaling.png"

    fig_asd, ax_asd = plt.subplots(figsize=(10, 6))
    for noise_standard_deviation, asd in zip(noise_levels, asd_curves):
        ax_asd.semilogy(frequencies[nonzero], asd[nonzero], label=f"sigma = {noise_standard_deviation:.0e}")
    ax_asd.axvline(gw_frequency, color="#111111", linestyle="--", label="100 Hz injection")
    ax_asd.set_title("Welch ASD for Increasing Gaussian Measurement Noise")
    ax_asd.set_xlabel("Frequency (Hz)")
    ax_asd.set_ylabel("ASD (intensity units / sqrt(Hz))")
    ax_asd.set_xlim(1.0, 500.0)
    ax_asd.grid(True, which="both", alpha=0.3)
    ax_asd.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=4)
    fig_asd.tight_layout(rect=(0.0, 0.06, 1.0, 1.0))
    fig_asd.savefig(asd_output_path, dpi=180)

    fig_scaling, ax_scaling = plt.subplots(figsize=(8, 6))
    ax_scaling.loglog(noise_levels, floor_values, "o", label="Measured median ASD floor")
    ax_scaling.loglog(
        noise_levels,
        fitted_floor,
        "--",
        linewidth=2,
        label=f"Log-log fit (slope = {scaling_slope:.3f})",
    )
    ax_scaling.loglog(
        noise_levels,
        expected_floor,
        ":",
        linewidth=2,
        label="White-noise expectation",
    )
    ax_scaling.set_title("Frequency-Domain Noise Floor vs Measurement Noise")
    ax_scaling.set_xlabel("Gaussian noise standard deviation")
    ax_scaling.set_ylabel("Median ASD floor (intensity units / sqrt(Hz))")
    ax_scaling.grid(True, which="both", alpha=0.3)
    ax_scaling.legend()
    fig_scaling.tight_layout()
    fig_scaling.savefig(scaling_output_path, dpi=180)

    if show_plots:
        plt.show()
    plt.close(fig_asd)
    plt.close(fig_scaling)

    print()
    print(f"Saved ASD comparison:       {asd_output_path}")
    print(f"Saved scaling comparison:   {scaling_output_path}")
    return asd_output_path, scaling_output_path


if __name__ == "__main__":
    run_noise_spectrum_analysis()
