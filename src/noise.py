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
    noise = generator.normal(
        loc=0.0,
        scale=standard_deviation,
        size=np.shape(signal),
    )
    return signal + noise

