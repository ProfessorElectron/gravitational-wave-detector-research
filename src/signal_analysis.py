"""Basic signal-analysis utilities."""

from __future__ import annotations

import numpy as np


def rms(values: np.ndarray) -> float:
    """Return the root-mean-square value of an array."""
    return float(np.sqrt(np.mean(np.square(values))))


def rms_snr(signal: np.ndarray, measured: np.ndarray) -> tuple[float, float, float]:
    """Return signal RMS, noise RMS, and signal-to-noise ratio.

    The noise is defined as measured - signal for controlled simulations where
    the injected signal is known.
    """
    if np.shape(signal) != np.shape(measured):
        raise ValueError("signal and measured must have the same shape")

    noise = measured - signal
    signal_rms = rms(signal)
    noise_rms = rms(noise)

    if noise_rms == 0.0:
        return signal_rms, noise_rms, float("inf")

    return signal_rms, noise_rms, signal_rms / noise_rms

