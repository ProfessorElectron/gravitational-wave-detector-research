"""Add Gaussian measurement noise to the linearized detector readout."""

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
from src.noise import add_gaussian_noise  # noqa: E402


def _response_amplitude(signal: np.ndarray) -> float:
    """Return half the peak-to-peak amplitude of a response."""
    return 0.5 * float(np.max(signal) - np.min(signal))


def run_noisy_detector_simulation(show_plots: bool = True) -> tuple[Path, Path]:
    """Simulate a GW readout at pi/2 and add Gaussian measurement noise."""
    wavelength = 1064e-9
    input_intensity = 1.0

    arm_length = 1.0
    static_phase = np.pi / 2.0
    strain_amplitude = 1e-21
    gw_frequency = 100.0
    duration = 0.1
    sample_count = 10_000

    noise_levels = (1e-6, 1e-5, 1e-4)
    random_seed = 12345

    time = np.linspace(0.0, duration, sample_count)
    strain = sinusoidal_strain(time, strain_amplitude, gw_frequency)
    differential_displacement = arm_length * strain
    gw_phase = phase_difference(differential_displacement, wavelength)

    phase = static_phase + gw_phase
    intensity = photodetector_intensity(phase, input_intensity)
    static_intensity = photodetector_intensity(static_phase, input_intensity)
    signal_response = intensity - static_intensity
    linear_response = -0.5 * input_intensity * np.sin(static_phase) * gw_phase

    signal_amplitude = _response_amplitude(linear_response)

    print("Noisy detector simulation")
    print(f"Operating point:       pi/2")
    print(f"Laser wavelength:      {wavelength:.3e} m")
    print(f"Arm length:            {arm_length:.3f} m")
    print(f"Strain amplitude:      {strain_amplitude:.3e}")
    print(f"GW frequency:          {gw_frequency:.1f} Hz")
    print(f"Peak GW phase:         {np.max(np.abs(gw_phase)):.3e} rad")
    print(f"Signal amplitude:      {signal_amplitude:.3e} intensity units")
    print(f"Random seed:           {random_seed}")
    print()

    results_dir = REPO_ROOT / "results"
    results_dir.mkdir(exist_ok=True)
    overlay_path = results_dir / "noisy_detector_overlay.png"
    zoom_path = results_dir / "noisy_detector_signal_vs_noise.png"

    fig_overlay, axes = plt.subplots(
        len(noise_levels),
        1,
        figsize=(10, 8),
        sharex=True,
    )
    fig_zoom, ax_zoom = plt.subplots(figsize=(9, 5))

    ax_zoom.plot(
        time,
        linear_response,
        color="#111111",
        linewidth=2,
        label="Noise-free linear signal",
    )

    for index, noise_standard_deviation in enumerate(noise_levels):
        measured_response = add_gaussian_noise(
            signal_response,
            standard_deviation=noise_standard_deviation,
            seed=random_seed + index,
        )
        measured_intensity = static_intensity + measured_response
        noise_to_signal = noise_standard_deviation / signal_amplitude

        print(f"sigma = {noise_standard_deviation:.1e}")
        print(f"  Noise / signal amplitude: {noise_to_signal:.3e}")
        print(f"  Measured response std:    {np.std(measured_response):.3e}")

        axis = axes[index]
        axis.plot(
            time,
            measured_intensity,
            color="#1f77b4",
            linewidth=0.8,
            label="Noisy measured intensity",
        )
        axis.plot(
            time,
            intensity,
            color="#d62728",
            linewidth=1.8,
            label="Noise-free intensity",
        )
        axis.set_title(f"Gaussian measurement noise: sigma = {noise_standard_deviation:.0e}")
        axis.set_ylabel("Intensity")
        axis.ticklabel_format(axis="y", style="plain", useOffset=False)
        axis.grid(True, alpha=0.3)
        axis.legend(loc="upper right")

        ax_zoom.plot(
            time,
            measured_response,
            linewidth=0.7,
            alpha=0.8,
            label=f"Noisy response, sigma = {noise_standard_deviation:.0e}",
        )

    axes[-1].set_xlabel("Time (s)")
    fig_overlay.suptitle("Noisy Photodetector Output at pi/2 Operating Point")
    fig_overlay.tight_layout()
    fig_overlay.savefig(overlay_path, dpi=180)

    ax_zoom.set_title("Signal Response Compared With Gaussian Measurement Noise")
    ax_zoom.set_xlabel("Time (s)")
    ax_zoom.set_ylabel("Intensity change from static intensity")
    ax_zoom.grid(True, alpha=0.3)
    ax_zoom.legend()
    fig_zoom.tight_layout()
    fig_zoom.savefig(zoom_path, dpi=180)

    if show_plots:
        plt.show()
    plt.close(fig_overlay)
    plt.close(fig_zoom)

    print()
    print(f"Saved noisy overlay plot: {overlay_path}")
    print(f"Saved signal/noise plot:  {zoom_path}")
    return overlay_path, zoom_path


if __name__ == "__main__":
    run_noisy_detector_simulation()

