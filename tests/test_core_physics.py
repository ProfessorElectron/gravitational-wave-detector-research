"""Regression tests for core interferometer and GW-response helpers."""

from __future__ import annotations

import unittest
import warnings

import numpy as np

from src.gravitational_wave import (
    strain_to_differential_displacement,
    warn_if_long_wavelength_approximation_invalid,
)
from src.interferometer import dark_port_intensity, photodetector_intensity


class InterferometerPortTests(unittest.TestCase):
    def test_bright_and_dark_ports_conserve_input_intensity(self) -> None:
        phase = np.linspace(-np.pi, np.pi, 101)
        total_intensity = photodetector_intensity(phase) + dark_port_intensity(phase)
        np.testing.assert_allclose(total_intensity, np.ones_like(phase))

    def test_dark_port_is_zero_at_zero_phase(self) -> None:
        self.assertEqual(dark_port_intensity(0.0), 0.0)


class GravitationalWaveResponseTests(unittest.TestCase):
    def test_strain_converts_to_differential_displacement(self) -> None:
        strain = np.array((-1e-21, 0.0, 1e-21))
        np.testing.assert_allclose(
            strain_to_differential_displacement(strain, 4_000.0),
            np.array((-4e-18, 0.0, 4e-18)),
        )

    def test_invalid_arm_length_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            strain_to_differential_displacement(1e-21, 0.0)

    def test_long_wavelength_guard_warns_above_threshold(self) -> None:
        with warnings.catch_warnings(record=True) as captured:
            warnings.simplefilter("always")
            warn_if_long_wavelength_approximation_invalid(1e7, 1.0)

        self.assertEqual(len(captured), 1)
        self.assertIs(captured[0].category, RuntimeWarning)


if __name__ == "__main__":
    unittest.main()
