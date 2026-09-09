"""Frequency-domain utilities for simulated detector readouts."""

from __future__ import annotations

import numpy as np


def _validate_signal(
    signal: np.ndarray,
    sampling_rate: float,
) -> np.ndarray:
    """Return a validated one-dimensional signal array."""
    values = np.asarray(signal, dtype=float)
    if values.ndim != 1 or values.size < 2:
        raise ValueError("signal must be one-dimensional with at least two samples")
    if sampling_rate <= 0:
        raise ValueError("sampling_rate must be positive")
    return values


def _one_sided(values: np.ndarray, sample_count: int) -> np.ndarray:
    """Double non-DC Fourier bins for a real-valued one-sided spectrum."""
    spectrum = values.copy()
    if sample_count % 2 == 0:
        spectrum[1:-1] *= 2.0
    else:
        spectrum[1:] *= 2.0
    return spectrum


def fft_spectrum(
    signal: np.ndarray,
    sampling_rate: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Return one-sided frequency bins and amplitude spectrum.

    The mean is removed before the transform so a static detector offset does
    not dominate the zero-frequency bin. The returned amplitude is normalized
    so a bin-centred sine wave has its time-domain peak amplitude.
    """
    values = _validate_signal(signal, sampling_rate)
    sample_count = len(values)
    raw_spectrum = np.fft.rfft(values - np.mean(values))
    amplitudes = _one_sided(np.abs(raw_spectrum) / sample_count, sample_count)
    frequencies = np.fft.rfftfreq(sample_count, 1.0 / sampling_rate)
    return frequencies, amplitudes


def windowed_fft_spectrum(
    signal: np.ndarray,
    sampling_rate: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Return a one-sided FFT amplitude spectrum using a Hann window.

    The mean is removed before windowing, and the spectrum is corrected by the
    window coherent gain so a bin-centred sine retains its peak amplitude.
    """
    values = _validate_signal(signal, sampling_rate)
    sample_count = len(values)
    window = np.hanning(sample_count)
    raw_spectrum = np.fft.rfft((values - np.mean(values)) * window)
    coherent_gain = np.sum(window) / sample_count
    amplitudes = _one_sided(
        np.abs(raw_spectrum) / (sample_count * coherent_gain),
        sample_count,
    )
    frequencies = np.fft.rfftfreq(sample_count, 1.0 / sampling_rate)
    return frequencies, amplitudes


def power_spectral_density(
    signal: np.ndarray,
    sampling_rate: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Return a one-sided periodogram power spectral density.

    The PSD has units of signal-squared per hertz. It is intentionally a
    single-record periodogram; Welch averaging can be added when the project
    moves to longer, more realistic noise records.
    """
    values = _validate_signal(signal, sampling_rate)
    sample_count = len(values)
    raw_spectrum = np.fft.rfft(values - np.mean(values))
    psd = _one_sided(
        np.abs(raw_spectrum) ** 2 / (sampling_rate * sample_count),
        sample_count,
    )
    frequencies = np.fft.rfftfreq(sample_count, 1.0 / sampling_rate)
    return frequencies, psd


def amplitude_spectral_density(
    signal: np.ndarray,
    sampling_rate: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Return one-sided frequency bins and amplitude spectral density.

    The ASD is the square root of the one-sided PSD and has units of signal
    per square-root hertz.
    """
    frequencies, psd = power_spectral_density(signal, sampling_rate)
    return frequencies, np.sqrt(psd)


def welch_power_spectral_density(
    signal: np.ndarray,
    sampling_rate: float,
    segment_length: int = 4096,
    overlap: float = 0.5,
) -> tuple[np.ndarray, np.ndarray]:
    """Estimate a one-sided PSD from overlapping Hann-windowed segments."""
    values = _validate_signal(signal, sampling_rate)
    if not 2 <= segment_length <= len(values):
        raise ValueError("segment_length must be between 2 and the signal length")
    if not 0.0 <= overlap < 1.0:
        raise ValueError("overlap must satisfy 0 <= overlap < 1")

    step = int(segment_length * (1.0 - overlap))
    if step < 1:
        raise ValueError("overlap produces an invalid segment step")

    window = np.hanning(segment_length)
    window_power = np.sum(window**2)
    psd_segments = []

    for start in range(0, len(values) - segment_length + 1, step):
        segment = values[start : start + segment_length]
        windowed_segment = (segment - np.mean(segment)) * window
        raw_spectrum = np.fft.rfft(windowed_segment)
        psd = _one_sided(
            np.abs(raw_spectrum) ** 2 / (sampling_rate * window_power),
            segment_length,
        )
        psd_segments.append(psd)

    frequencies = np.fft.rfftfreq(segment_length, 1.0 / sampling_rate)
    return frequencies, np.mean(psd_segments, axis=0)


def welch_amplitude_spectral_density(
    signal: np.ndarray,
    sampling_rate: float,
    segment_length: int = 4096,
    overlap: float = 0.5,
) -> tuple[np.ndarray, np.ndarray]:
    """Estimate a one-sided ASD using the Welch PSD estimate."""
    frequencies, psd = welch_power_spectral_density(signal, sampling_rate, segment_length, overlap)
    return frequencies, np.sqrt(psd)
