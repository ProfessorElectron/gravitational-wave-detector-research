"""Simple gravitational-wave strain models.

The functions here describe strain h(t). Converting strain into detector arm
displacement belongs in the simulation layer for now, so the validation chain
stays explicit.
"""

from __future__ import annotations

import warnings

import numpy as np


SPEED_OF_LIGHT = 299_792_458.0


def _positive_arm_length(arm_length: float) -> float:
    """Validate and return a finite, positive arm length in meters."""
    try:
        value = float(arm_length)
    except (TypeError, ValueError) as error:
        raise ValueError("arm_length must be a finite positive number") from error

    if not np.isfinite(value) or value <= 0.0:
        raise ValueError("arm_length must be a finite positive number")
    return value


def _finite_scalar(value: float, name: str) -> float:
    """Validate and return a finite scalar value."""
    try:
        result = float(value)
    except (TypeError, ValueError) as error:
        raise ValueError(f"{name} must be a finite number") from error

    if not np.isfinite(result):
        raise ValueError(f"{name} must be a finite number")
    return result


def _finite_array(values: float | np.ndarray, name: str) -> np.ndarray:
    """Validate and return an array containing only finite numeric values."""
    try:
        result = np.asarray(values, dtype=float)
    except (TypeError, ValueError) as error:
        raise ValueError(f"{name} must contain only finite numeric values") from error

    if not np.all(np.isfinite(result)):
        raise ValueError(f"{name} must contain only finite numeric values")
    return result


def sinusoidal_strain(
    time: float | np.ndarray,
    amplitude: float,
    frequency: float,
    phase: float = 0.0,
) -> float | np.ndarray:
    """Return a sinusoidal gravitational-wave strain h(t)."""
    time_values = _finite_array(time, "time")

    amplitude_value = _finite_scalar(amplitude, "amplitude")
    frequency_value = _finite_scalar(frequency, "frequency")
    phase_value = _finite_scalar(phase, "phase")
    if frequency_value < 0.0:
        raise ValueError("frequency must be non-negative")

    return amplitude_value * np.sin(
        2.0 * np.pi * frequency_value * time_values + phase_value
    )


def strain_to_differential_displacement(
    strain: float | np.ndarray,
    arm_length: float,
) -> float | np.ndarray:
    """Convert strain h to differential arm displacement Delta L = L * h."""
    strain_values = _finite_array(strain, "strain")

    return _positive_arm_length(arm_length) * strain_values


def long_wavelength_characteristic_frequency(arm_length: float) -> float:
    """Return f_star = c / (2*pi*L), the finite-arm response scale in Hz."""
    return SPEED_OF_LIGHT / (2.0 * np.pi * _positive_arm_length(arm_length))


def warn_if_long_wavelength_approximation_invalid(
    frequency: float | np.ndarray,
    arm_length: float,
    maximum_fraction: float = 0.1,
) -> None:
    """Warn when the quasi-static arm-response approximation may fail.

    The simplified detector response is appropriate only when the GW frequency
    remains well below f_star = c / (2*pi*L). The default warning threshold is
    0.1 * f_star.
    """
    frequencies = _finite_array(frequency, "frequency")
    if np.any(frequencies < 0.0):
        raise ValueError("frequency must contain only finite non-negative values")

    fraction = _finite_scalar(maximum_fraction, "maximum_fraction")
    if not 0.0 < fraction <= 1.0:
        raise ValueError("maximum_fraction must be in the interval (0, 1]")

    threshold = fraction * long_wavelength_characteristic_frequency(arm_length)
    if np.any(frequencies > threshold):
        warnings.warn(
            "GW frequency exceeds the long-wavelength approximation threshold "
            f"({threshold:.3e} Hz); finite-arm response effects may be important.",
            RuntimeWarning,
            stacklevel=2,
        )

