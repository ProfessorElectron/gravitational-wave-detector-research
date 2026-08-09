"""Basic Michelson interferometer equations.

This module intentionally stays small: it contains the reusable physics for a
minimal, ideal Michelson interferometer. Noise, realistic optics, and signal
recovery belong in later milestones.
"""

from __future__ import annotations

import numpy as np


def differential_arm_length(length_x: float, length_y: float) -> float:
    """Return the arm-length difference Lx - Ly in meters."""
    return length_x - length_y


def phase_difference(
    differential_length: float | np.ndarray,
    wavelength: float,
) -> float | np.ndarray:
    """Return the round-trip phase difference in radians.

    A Michelson beam travels to a mirror and back, so a one-way arm-length
    difference Delta L produces a round-trip optical path difference of
    2 * Delta L. The phase difference is therefore 4*pi*Delta L/lambda.
    """
    if wavelength <= 0:
        raise ValueError("wavelength must be positive")

    return 4.0 * np.pi * differential_length / wavelength


def photodetector_intensity(
    phase: float | np.ndarray,
    input_intensity: float = 1.0,
) -> float | np.ndarray:
    """Return ideal bright-port Michelson intensity.

    The result is normalized by ``input_intensity`` and follows
    I = (I0 / 2) * (1 + cos(phase)).
    """
    if input_intensity < 0:
        raise ValueError("input_intensity must be non-negative")

    return 0.5 * input_intensity * (1.0 + np.cos(phase))


def intensity_from_arm_lengths(
    length_x: float,
    length_y: float,
    wavelength: float,
    input_intensity: float = 1.0,
) -> float:
    """Calculate detector intensity directly from Michelson arm lengths."""
    delta_l = differential_arm_length(length_x, length_y)
    phase = phase_difference(delta_l, wavelength)
    return float(photodetector_intensity(phase, input_intensity))

