"""Simple gravitational-wave strain models.

The functions here describe strain h(t). Converting strain into detector arm
displacement belongs in the simulation layer for now, so the validation chain
stays explicit.
"""

from __future__ import annotations

import numpy as np


def sinusoidal_strain(
    time: float | np.ndarray,
    amplitude: float,
    frequency: float,
    phase: float = 0.0,
) -> float | np.ndarray:
    """Return a sinusoidal gravitational-wave strain h(t)."""
    if frequency < 0:
        raise ValueError("frequency must be non-negative")

    return amplitude * np.sin(2.0 * np.pi * frequency * time + phase)

