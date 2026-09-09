"""Frequency-dependent physical noise models and domain conversions."""

from __future__ import annotations

import numpy as np


def _positive_frequencies(frequency: np.ndarray) -> np.ndarray:
    """Return a validated one-dimensional positive frequency array in Hz."""
    values = np.asarray(frequency, dtype=float)
    if values.ndim != 1 or values.size == 0:
        raise ValueError("frequency must be a non-empty one-dimensional array")
    if not np.all(np.isfinite(values)) or np.any(values <= 0.0):
        raise ValueError("frequency values must be finite and positive")
    return values


def _nonnegative_values(values: np.ndarray, quantity: str) -> np.ndarray:
    """Return finite non-negative spectral values."""
    values = np.asarray(values, dtype=float)
    if not np.all(np.isfinite(values)) or np.any(values < 0.0):
        raise ValueError(f"{quantity} values must be finite and non-negative")
    return values


def seismic_displacement_asd(
    frequency: np.ndarray,
    reference_asd: float,
    reference_frequency: float,
    exponent: float,
    minimum_frequency: float,
    maximum_frequency: float,
) -> np.ndarray:
    """Return bounded power-law seismic displacement ASD in m / sqrt(Hz)."""
    frequencies = _positive_frequencies(frequency)
    if reference_asd < 0.0 or exponent < 0.0:
        raise ValueError("reference_asd and exponent must be non-negative")
    if reference_frequency <= 0.0:
        raise ValueError("reference_frequency must be positive")
    if minimum_frequency <= 0.0 or maximum_frequency < minimum_frequency:
        raise ValueError("frequency bounds must be positive and ordered")
    if np.any(frequencies < minimum_frequency) or np.any(frequencies > maximum_frequency):
        raise ValueError("frequency values must stay within the model bounds")

    return reference_asd * (frequencies / reference_frequency) ** (-exponent)


def asd_to_psd(asd: np.ndarray) -> np.ndarray:
    """Convert a non-negative ASD to a PSD in the corresponding squared units."""
    return _nonnegative_values(asd, "ASD") ** 2


def psd_to_asd(psd: np.ndarray) -> np.ndarray:
    """Convert a non-negative PSD to an ASD in the corresponding root units."""
    return np.sqrt(_nonnegative_values(psd, "PSD"))


def total_psd(*source_psds: np.ndarray) -> np.ndarray:
    """Sum independent PSDs that have already been calibrated to one domain."""
    if not source_psds:
        raise ValueError("at least one PSD is required")

    values = [_nonnegative_values(psd, "PSD") for psd in source_psds]
    if any(psd.shape != values[0].shape for psd in values[1:]):
        raise ValueError("all PSD arrays must have the same shape")
    return np.sum(values, axis=0)


def shot_noise_strain_asd(
    frequency: np.ndarray,
    wavelength: float,
    effective_arm_length: float,
    photocurrent: float,
    elementary_charge: float,
) -> np.ndarray:
    """Return ideal photodetector shot-noise strain ASD in 1 / sqrt(Hz).

    This is a shot-noise-only approximation around the pi/2 operating point.
    It excludes radiation-pressure noise and quantum correlations.
    """
    frequencies = _positive_frequencies(frequency)
    if min(wavelength, effective_arm_length, photocurrent, elementary_charge) <= 0.0:
        raise ValueError("shot-noise parameters must be positive")

    asd = wavelength / (2.0 * np.pi * effective_arm_length)
    asd *= np.sqrt(2.0 * elementary_charge / photocurrent)
    return np.full_like(frequencies, asd)


def displacement_psd_to_strain(psd: np.ndarray, arm_length: float) -> np.ndarray:
    """Convert displacement PSD in m squared / Hz to strain PSD in 1 / Hz."""
    if arm_length <= 0.0:
        raise ValueError("arm_length must be positive")
    return _nonnegative_values(psd, "PSD") / arm_length**2


def displacement_asd_to_strain(asd: np.ndarray, arm_length: float) -> np.ndarray:
    """Convert displacement ASD in m / sqrt(Hz) to strain ASD in 1 / sqrt(Hz)."""
    if arm_length <= 0.0:
        raise ValueError("arm_length must be positive")
    return _nonnegative_values(asd, "ASD") / arm_length
