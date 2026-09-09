"""Simple detector noise models."""

from __future__ import annotations

import numpy as np


def add_gaussian_noise(
    signal: np.ndarray,
    standard_deviation: float,
    seed: int | None = None,
) -> np.ndarray:
    """Return signal plus zero-mean Gaussian measurement noise."""
    if standard_deviation < 0:
        raise ValueError("standard_deviation must be non-negative")

    generator = np.random.default_rng(seed)
    return signal + generator.normal(0.0, standard_deviation, np.shape(signal))
