"""Compare raw, windowed, and Welch frequency-domain detector analysis."""

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
from src.spectral_analysis import (  # noqa: E402
    fft_spectrum,
    welch_amplitude_spectral_density,
    welch_power_spectral_density,
    windowed_fft_spectrum,
)


def run_welch_analysis(show_plots: bool = True) -> Path:
    """Compare raw FFT, Hann-windowed FFT, and Welch PSD/ASD estimates."""
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
    random_seed = 12345

    time = np.arange(sample_count) / sampling_rate
    strain = sinusoidal_strain(time, strain_amplitude, gw_frequency)
    differential_displacement = arm_length * strain
    gw_phase = phase_difference(differential_displacement, wavelength)
    clean_response = -0.5 * input_intensity * np.sin(static_phase) * gw_phase

    signal_amplitude = 0.5 * float(np.ptp(clean_response))
    noise_standard_deviation = 0.5 * signal_amplitude
    measured_response = add_gaussian_noise(clean_response, noise_standard_deviation, random_seed)

    frequencies_raw, amplitudes_raw = fft_spectrum(measured_response, sampling_rate)
    frequencies_windowed, amplitudes_windowed = windowed_fft_spectrum(measured_response, sampling_rate)
    frequencies_welch, psd_welch = welch_power_spectral_density(measured_response, sampling_rate, segment_length, overlap)
    _, asd_welch = welch_amplitude_spectral_density(measured_response, sampling_rate, segment_length, overlap)

    raw_peak_frequency = float(frequencies_raw[np.argmax(amplitudes_raw[1:]) + 1])
    windowed_peak_frequency = float(
        frequencies_windowed[np.argmax(amplitudes_windowed[1:]) + 1]
    )
    welch_peak_frequency = float(frequencies_welch[np.argmax(psd_welch[1:]) + 1])
    segment_step = int(segment_length * (1.0 - overlap))
    segment_count = len(range(0, sample_count - segment_length + 1, segment_step))

    print("Welch frequency-domain detector analysis")
    print(f"Injected GW frequency:       {gw_frequency:.1f} Hz")
    print(f"Sampling rate:               {sampling_rate:.1f} Hz")
    print(f"Duration:                    {duration:.1f} s")
    print(f"Raw FFT resolution:          {sampling_rate / sample_count:.3f} Hz")
    print(f"Welch segment resolution:    {sampling_rate / segment_length:.3f} Hz")
    print(f"Welch overlap:               {overlap:.0%}")
    print(f"Raw FFT peak:                {raw_peak_frequency:.3f} Hz")
    print(f"Windowed FFT peak:           {windowed_peak_frequency:.3f} Hz")
    print(f"Welch PSD peak:              {welch_peak_frequency:.3f} Hz")
    print(f"Number of Welch segments:    {segment_count}")

    results_dir = REPO_ROOT / "results"
    results_dir.mkdir(exist_ok=True)
    output_path = results_dir / "welch_analysis.png"
    nonzero_welch = frequencies_welch > 0.0

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    axes[0, 0].plot(frequencies_raw, amplitudes_raw, linewidth=1.0, label="Raw FFT")
    axes[0, 0].plot(frequencies_windowed, amplitudes_windowed, label="Hann-windowed FFT")
    axes[0, 0].axvline(gw_frequency, color="#d62728", linestyle="--", label="100 Hz injection")
    axes[0, 0].set_title("Raw vs Hann-Windowed FFT")
    axes[0, 0].set_xlabel("Frequency (Hz)")
    axes[0, 0].set_ylabel("Amplitude (intensity units)")
    axes[0, 0].set_xlim(0.0, 250.0)
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].legend()

    axes[0, 1].semilogy(frequencies_welch[nonzero_welch], psd_welch[nonzero_welch], color="#9467bd")
    axes[0, 1].axvline(gw_frequency, color="#d62728", linestyle="--", label="100 Hz injection")
    axes[0, 1].set_title("Welch Power Spectral Density")
    axes[0, 1].set_xlabel("Frequency (Hz)")
    axes[0, 1].set_ylabel("PSD (intensity units squared / Hz)")
    axes[0, 1].set_xlim(1.0, 250.0)
    axes[0, 1].grid(True, which="both", alpha=0.3)
    axes[0, 1].legend()

    axes[1, 0].semilogy(frequencies_welch[nonzero_welch], asd_welch[nonzero_welch], color="#ff7f0e")
    axes[1, 0].axvline(gw_frequency, color="#d62728", linestyle="--", label="100 Hz injection")
    axes[1, 0].set_title("Welch Amplitude Spectral Density")
    axes[1, 0].set_xlabel("Frequency (Hz)")
    axes[1, 0].set_ylabel("ASD (intensity units / sqrt(Hz))")
    axes[1, 0].set_xlim(1.0, 250.0)
    axes[1, 0].grid(True, which="both", alpha=0.3)
    axes[1, 0].legend()

    axes[1, 1].plot(frequencies_raw, amplitudes_raw, linewidth=0.8, label="Raw FFT")
    axes[1, 1].plot(frequencies_windowed, amplitudes_windowed, label="Hann-windowed FFT")
    axes[1, 1].axvline(gw_frequency, color="#d62728", linestyle="--", label="100 Hz")
    axes[1, 1].set_title("Windowing Near the 100 Hz Feature")
    axes[1, 1].set_xlabel("Frequency (Hz)")
    axes[1, 1].set_ylabel("Amplitude (intensity units)")
    axes[1, 1].set_xlim(80.0, 120.0)
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].legend()

    fig.suptitle("Frequency-Domain Analysis: FFT, Windowing, and Welch PSD")
    fig.tight_layout()
    fig.savefig(output_path, dpi=180)

    if show_plots:
        plt.show()
    plt.close(fig)

    print()
    print(f"Saved Welch analysis plot: {output_path}")
    return output_path


if __name__ == "__main__":
    run_welch_analysis()
