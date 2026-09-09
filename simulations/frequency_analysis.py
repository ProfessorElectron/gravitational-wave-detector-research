"""Show a 100 Hz gravitational-wave injection in the frequency domain."""

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
    amplitude_spectral_density,
    fft_spectrum,
    power_spectral_density,
)


def run_frequency_analysis(show_plots: bool = True) -> Path:
    """Inject a 100 Hz signal and display its FFT, PSD, and ASD."""
    wavelength = 1064e-9
    input_intensity = 1.0

    arm_length = 1.0
    static_phase = np.pi / 2.0
    strain_amplitude = 1e-21
    gw_frequency = 100.0

    sampling_rate = 4096.0
    duration = 4.0
    sample_count = int(sampling_rate * duration)
    random_seed = 12345

    time = np.arange(sample_count) / sampling_rate
    strain = sinusoidal_strain(time, strain_amplitude, gw_frequency)
    differential_displacement = arm_length * strain
    gw_phase = phase_difference(differential_displacement, wavelength)

    # At pi/2 the first-order Michelson readout is linear in the GW phase.
    clean_response = -0.5 * input_intensity * np.sin(static_phase) * gw_phase
    signal_amplitude = 0.5 * float(np.ptp(clean_response))
    noise_standard_deviation = 0.5 * signal_amplitude
    measured_response = add_gaussian_noise(clean_response, noise_standard_deviation, random_seed)

    frequencies, amplitudes = fft_spectrum(measured_response, sampling_rate)
    _, psd = power_spectral_density(measured_response, sampling_rate)
    _, asd = amplitude_spectral_density(measured_response, sampling_rate)

    peak_index = int(np.argmax(amplitudes[1:]) + 1)
    peak_frequency = float(frequencies[peak_index])
    frequency_resolution = sampling_rate / sample_count

    print("Frequency-domain detector analysis")
    print(f"Operating point:           pi/2")
    print(f"Arm length:                {arm_length:.3f} m")
    print(f"Strain amplitude:          {strain_amplitude:.3e}")
    print(f"Injected GW frequency:     {gw_frequency:.1f} Hz")
    print(f"Sampling rate:             {sampling_rate:.1f} Hz")
    print(f"Duration:                  {duration:.1f} s")
    print(f"Frequency resolution:      {frequency_resolution:.3f} Hz")
    print(f"Response amplitude:        {signal_amplitude:.3e} intensity units")
    print(f"Noise standard deviation:  {noise_standard_deviation:.3e} intensity units")
    print(f"Strongest FFT feature:     {peak_frequency:.3f} Hz")
    print(f"Random seed:               {random_seed}")

    results_dir = REPO_ROOT / "results"
    results_dir.mkdir(exist_ok=True)
    output_path = results_dir / "frequency_analysis.png"

    display_duration = 0.05
    display_samples = int(display_duration * sampling_rate)
    nonzero = frequencies > 0.0

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    axes[0, 0].plot(time[:display_samples], measured_response[:display_samples], color="#1f77b4", label="Noisy response")
    axes[0, 0].plot(time[:display_samples], clean_response[:display_samples], color="#d62728", linewidth=1.5, label="Injected linear response")
    axes[0, 0].set_title("Detector Readout: First 50 ms")
    axes[0, 0].set_xlabel("Time (s)")
    axes[0, 0].set_ylabel("Intensity change")
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].legend()

    axes[0, 1].plot(frequencies, amplitudes, color="#2ca02c", linewidth=1.0)
    axes[0, 1].axvline(gw_frequency, color="#d62728", linestyle="--", label="100 Hz injection")
    axes[0, 1].set_title("One-Sided FFT Amplitude Spectrum")
    axes[0, 1].set_xlabel("Frequency (Hz)")
    axes[0, 1].set_ylabel("Amplitude (intensity units)")
    axes[0, 1].set_xlim(0.0, 250.0)
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].legend()

    axes[1, 0].loglog(frequencies[nonzero], psd[nonzero], color="#9467bd")
    axes[1, 0].axvline(gw_frequency, color="#d62728", linestyle="--", label="100 Hz injection")
    axes[1, 0].set_title("One-Sided Power Spectral Density")
    axes[1, 0].set_xlabel("Frequency (Hz)")
    axes[1, 0].set_ylabel("PSD (intensity units squared / Hz)")
    axes[1, 0].grid(True, which="both", alpha=0.3)
    axes[1, 0].legend()

    axes[1, 1].loglog(frequencies[nonzero], asd[nonzero], color="#ff7f0e")
    axes[1, 1].axvline(gw_frequency, color="#d62728", linestyle="--", label="100 Hz injection")
    axes[1, 1].set_title("One-Sided Amplitude Spectral Density")
    axes[1, 1].set_xlabel("Frequency (Hz)")
    axes[1, 1].set_ylabel("ASD (intensity units / sqrt(Hz))")
    axes[1, 1].grid(True, which="both", alpha=0.3)
    axes[1, 1].legend()

    fig.suptitle("100 Hz GW Injection: FFT, PSD, and ASD")
    fig.tight_layout()
    fig.savefig(output_path, dpi=180)

    if show_plots:
        plt.show()
    plt.close(fig)

    print()
    print(f"Saved frequency-domain plot: {output_path}")
    return output_path


if __name__ == "__main__":
    run_frequency_analysis()
