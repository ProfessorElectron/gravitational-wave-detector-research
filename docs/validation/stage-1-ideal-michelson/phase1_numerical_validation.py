"""Phase 1 numerical validation — reproducible rerun of T1-T13.

Imports the actual repository implementation (src/interferometer.py) and
independently reproduces the T1-T13 test suite recorded in
numerical_validation.md, printing environment info, obtained results, and
numerical error against the previously recorded values so the two can be
compared directly.

Run with: python3 validation/phase1_numerical_validation.py
"""
from __future__ import annotations

import platform
import sys

import numpy as np

from src.interferometer import (
    differential_arm_length,
    phase_difference,
    photodetector_intensity,
    intensity_from_arm_lengths,
)

WAVELENGTH = 1064e-9  # m, matches the prior T1-T13 record throughout


def print_environment() -> None:
    print("=" * 60)
    print("Environment")
    print("=" * 60)
    print(f"Python version : {platform.python_version()}")
    print(f"NumPy version  : {np.__version__}")
    print(f"Platform       : {platform.platform()}")
    print()


def test_t1() -> bool:
    """T1 - Differential arm length: DeltaL = Lx - Ly, including sign."""
    print("-" * 60)
    print("T1 - Differential Arm-Length Validation")
    print("-" * 60)

    cases = [
        ("Equal arms", 1.0, 1.0, 0.0),
        ("X longer", 1.0000001, 1.0, 1.0e-7),
        ("Y longer", 1.0, 1.0000001, -1.0e-7),
        ("Ordinary unequal", 1.2, 0.8, 0.4),
    ]

    all_pass = True
    max_err = 0.0
    for name, lx, ly, expected in cases:
        actual = differential_arm_length(lx, ly)
        err = abs(actual - expected)
        max_err = max(max_err, err)
        ok = err < 1e-12
        all_pass &= ok
        print(f"  {name:20s} Lx={lx!r:14} Ly={ly!r:14} "
              f"expected={expected!r:22} actual={actual!r:22} "
              f"abs_err={err:.3e} {'PASS' if ok else 'FAIL'}")

    print(f"  Max observed absolute error: {max_err:.3e} m")
    print(f"  Previously recorded max error: 1.11e-16 m")
    print(f"  T1 RESULT: {'PASS' if all_pass else 'FAIL'}")
    print()
    return all_pass


def test_t2() -> bool:
    """T2 - Round-trip factor: DeltaL_rt = 2*DeltaL_arm, cross-checked against
    phase_difference(). No separate round-trip function exists in the
    repository, so this is a physical/algebraic consistency check, not an
    independent test of a separate implementation."""
    print("-" * 60)
    print("T2 - Round-Trip Optical Path Difference and Factor of 2")
    print("-" * 60)

    all_pass = True
    max_err = 0.0
    for label, delta_l_arm in [("Positive", 1e-9), ("Negative", -1e-9)]:
        delta_l_rt = 2.0 * delta_l_arm
        expected_phase = 2.0 * np.pi * delta_l_rt / WAVELENGTH
        actual_phase = phase_difference(delta_l_arm, WAVELENGTH)
        err = abs(actual_phase - expected_phase)
        max_err = max(max_err, err)
        ok = err < 1e-12
        all_pass &= ok
        print(f"  {label:10s} DeltaL_arm={delta_l_arm:+.3e} m -> "
              f"DeltaL_rt={delta_l_rt:+.3e} m -> "
              f"expected_phase={expected_phase:+.15f} "
              f"actual_phase={actual_phase:+.15f} "
              f"abs_err={err:.3e} {'PASS' if ok else 'FAIL'}")

    print(f"  Max observed absolute error: {max_err:.3e} rad")
    print(f"  Previously recorded max error: ~1.7e-18 rad")
    print("  Note: no round_trip_difference() function exists in "
          "src/interferometer.py; this is a cross-formulation consistency "
          "check, not an independent implementation test.")
    print(f"  T2 RESULT: {'PASS' if all_pass else 'FAIL'}")
    print()
    return all_pass


def test_t3() -> bool:
    """T3 - Phase-difference known-answer validation."""
    print("-" * 60)
    print("T3 - Phase-Difference Known-Answer Validation")
    print("-" * 60)

    cases = [
        ("0", 0.0, 0.0),
        ("lambda/8", WAVELENGTH / 8, np.pi / 2),
        ("lambda/4", WAVELENGTH / 4, np.pi),
        ("lambda/2", WAVELENGTH / 2, 2 * np.pi),
        ("-lambda/4", -WAVELENGTH / 4, -np.pi),
    ]

    all_pass = True
    max_err = 0.0
    for label, delta_l, expected in cases:
        actual = phase_difference(delta_l, WAVELENGTH)
        err = abs(actual - expected)
        max_err = max(max_err, err)
        ok = err < 1e-9
        all_pass &= ok
        print(f"  DeltaL={label:10s} expected={expected:+.16f} "
              f"actual={actual:+.16f} abs_err={err:.3e} "
              f"{'PASS' if ok else 'FAIL'}")

    # Odd-symmetry and phase-doubling checks
    phi_pos = phase_difference(WAVELENGTH / 8, WAVELENGTH)
    phi_neg = phase_difference(-WAVELENGTH / 8, WAVELENGTH)
    odd_sym_ok = abs(phi_pos + phi_neg) < 1e-12
    phi_double = phase_difference(WAVELENGTH / 4, WAVELENGTH)
    doubling_ok = abs(phi_double - 2 * phi_pos) < 1e-9
    print(f"  Odd symmetry phi(-x) = -phi(x): {'PASS' if odd_sym_ok else 'FAIL'}")
    print(f"  Doubling phi(2x) = 2*phi(x):    {'PASS' if doubling_ok else 'FAIL'}")
    all_pass &= odd_sym_ok and doubling_ok

    print(f"  Max observed absolute error: {max_err:.3e} rad")
    print(f"  T3 RESULT: {'PASS' if all_pass else 'FAIL'}")
    print()
    return all_pass


def test_t4() -> bool:
    """T4 - Bright-port intensity known-answer validation."""
    print("-" * 60)
    print("T4 - Bright-Port Intensity and Interference Conditions")
    print("-" * 60)

    cases = [
        ("0", 0.0, 1.0),
        ("lambda/8", WAVELENGTH / 8, 0.5),
        ("lambda/4", WAVELENGTH / 4, 0.0),
        ("lambda/2", WAVELENGTH / 2, 1.0),
        ("-lambda/4", -WAVELENGTH / 4, 0.0),
    ]

    all_pass = True
    max_err = 0.0
    for label, delta_l, expected in cases:
        phase = phase_difference(delta_l, WAVELENGTH)
        actual = photodetector_intensity(phase, 1.0)
        err = abs(actual - expected)
        max_err = max(max_err, err)
        ok = err < 1e-9
        all_pass &= ok
        print(f"  DeltaL={label:10s} expected_I={expected:.6f} "
              f"actual_I={actual:.15f} abs_err={err:.3e} "
              f"{'PASS' if ok else 'FAIL'}")

    print(f"  Max observed absolute error: {max_err:.3e}")
    print(f"  T4 RESULT: {'PASS' if all_pass else 'FAIL'}")
    print()
    return all_pass


def test_t5() -> bool:
    """T5 - End-to-end implementation chain via intensity_from_arm_lengths()."""
    print("-" * 60)
    print("T5 - End-to-End Chain Validation")
    print("-" * 60)

    lx0 = 1.0
    cases = [
        ("0", lx0, 1.0),
        ("lambda/8", lx0 + WAVELENGTH / 8, 0.5),
        ("lambda/4", lx0 + WAVELENGTH / 4, 0.0),
        ("lambda/2", lx0 + WAVELENGTH / 2, 1.0),
        ("-lambda/4", lx0 - WAVELENGTH / 4, 0.0),
    ]

    all_pass = True
    max_err = 0.0
    for label, lx, expected in cases:
        actual = intensity_from_arm_lengths(lx, lx0, WAVELENGTH, 1.0)
        err = abs(actual - expected)
        max_err = max(max_err, err)
        ok = err < 1e-6
        all_pass &= ok
        print(f"  DeltaL={label:10s} expected_I={expected:.6f} "
              f"actual_I={actual:.15f} abs_err={err:.3e} "
              f"{'PASS' if ok else 'FAIL'}")

    print(f"  Max observed absolute error: {max_err:.3e}")
    print(f"  Previously recorded outlier at lambda/8: ~5.77e-10 "
          f"(floating-point representation of lambda/8 as an arm length)")
    print(f"  T5 RESULT: {'PASS' if all_pass else 'FAIL'}")
    print()
    return all_pass


def test_t6() -> bool:
    """T6 - Periodicity and symmetry of the bright-port response."""
    print("-" * 60)
    print("T6 - Periodicity and Symmetry")
    print("-" * 60)

    ratios = [-0.37, -0.10, 0.0, 0.13, 0.49]
    all_pass = True

    print("  6.1 Periodicity: I(DeltaL + lambda/2) == I(DeltaL)")
    max_err_period = 0.0
    for r in ratios:
        dl = r * WAVELENGTH
        i1 = photodetector_intensity(phase_difference(dl, WAVELENGTH), 1.0)
        i2 = photodetector_intensity(
            phase_difference(dl + WAVELENGTH / 2, WAVELENGTH), 1.0
        )
        err = abs(i1 - i2)
        max_err_period = max(max_err_period, err)
        ok = err < 1e-9
        all_pass &= ok
        print(f"    DeltaL/lambda={r:+.2f}  I(DeltaL)={i1:.12f}  "
              f"I(DeltaL+lambda/2)={i2:.12f}  diff={err:.3e} "
              f"{'PASS' if ok else 'FAIL'}")
    print(f"    Max discrepancy: {max_err_period:.3e}")

    print("  6.2 Symmetry: I(+DeltaL) == I(-DeltaL)")
    max_err_sym = 0.0
    for r in ratios:
        dl = r * WAVELENGTH
        i_pos = photodetector_intensity(phase_difference(dl, WAVELENGTH), 1.0)
        i_neg = photodetector_intensity(phase_difference(-dl, WAVELENGTH), 1.0)
        err = abs(i_pos - i_neg)
        max_err_sym = max(max_err_sym, err)
        ok = err < 1e-12
        all_pass &= ok
        print(f"    DeltaL/lambda={r:+.2f}  I(+DeltaL)={i_pos:.12f}  "
              f"I(-DeltaL)={i_neg:.12f}  diff={err:.3e} "
              f"{'PASS' if ok else 'FAIL'}")
    print(f"    Max discrepancy: {max_err_sym:.3e}")

    print(f"  T6 RESULT: {'PASS' if all_pass else 'FAIL'}")
    print()
    return all_pass


def test_t7() -> bool:
    """T7 - Numerical fringe-spacing validation."""
    print("-" * 60)
    print("T7 - Numerical Fringe-Spacing Validation")
    print("-" * 60)

    n_points = 20001
    dl_sweep = np.linspace(-2 * WAVELENGTH, 2 * WAVELENGTH, n_points)
    intensity = photodetector_intensity(
        phase_difference(dl_sweep, WAVELENGTH), 1.0
    )

    # Find local maxima (interior points higher than both neighbors)
    is_max = (intensity[1:-1] > intensity[:-2]) & (intensity[1:-1] > intensity[2:])
    peak_positions = dl_sweep[1:-1][is_max]

    spacings = np.diff(peak_positions)
    expected_spacing = WAVELENGTH / 2
    max_err = float(np.max(np.abs(spacings - expected_spacing)))

    print(f"  Detected {len(peak_positions)} fringe maxima")
    print(f"  Expected spacing (lambda/2): {expected_spacing:.6e} m")
    print(f"  Measured spacing (mean):     {np.mean(spacings):.6e} m")
    print(f"  Max deviation from lambda/2: {max_err:.3e} m")

    ok = max_err < 1e-9  # loose bound; grid resolution, not physics, limits this
    print(f"  T7 RESULT: {'PASS' if ok else 'FAIL'}")
    print("  Note: this measures the sweep's own output against the same "
          "formula under test (periodicity already established in T6/§13), "
          "not an independently constructed reference.")
    print()
    return ok


def test_t8() -> bool:
    """T8 - Intensity bounds sanity check (supplementary, not core)."""
    print("-" * 60)
    print("T8 - Intensity Bounds Sanity Check")
    print("-" * 60)

    dl_sweep = np.linspace(-2 * WAVELENGTH, 2 * WAVELENGTH, 4001)
    phases = phase_difference(dl_sweep, WAVELENGTH)

    all_pass = True
    for i0 in [0.0, 1.0, 2.5, 10.0]:
        intensity = photodetector_intensity(phases, i0)
        lo, hi = float(np.min(intensity)), float(np.max(intensity))
        ok = (lo >= -1e-12) and (hi <= i0 + 1e-9)
        all_pass &= ok
        print(f"  I0={i0:5.2f}  min={lo:.6e}  max={hi:.6e}  "
              f"bounds=[0,{i0}]  {'PASS' if ok else 'FAIL'}")

    print(f"  T8 RESULT: {'PASS' if all_pass else 'FAIL'} (supplementary sanity check)")
    print()
    return all_pass


def test_t9() -> bool:
    """T9 - Equal-arm operating point. Dark-port value uses the analytical
    complementary relation directly (no dark-port function exists in the
    repository)."""
    print("-" * 60)
    print("T9 - Equal-Arm Operating Point")
    print("-" * 60)

    lx = ly = 1.0
    dl = differential_arm_length(lx, ly)
    phase = phase_difference(dl, WAVELENGTH)
    i_bright = photodetector_intensity(phase, 1.0)
    i_dark_analytical = 0.5 * (1.0 - np.cos(phase))  # analytical relation, not repo code
    conservation_err = abs((i_bright + i_dark_analytical) - 1.0)

    print(f"  Lx=Ly={lx}  -> DeltaL={dl}  -> Delta_phi={phase}")
    print(f"  I_bright = {i_bright:.12f}")
    print(f"  I_dark (analytical relation, not repository code) = {i_dark_analytical:.12f}")
    print(f"  I_bright + I_dark = {i_bright + i_dark_analytical:.12f}  "
          f"(conservation error {conservation_err:.3e})")

    ok = (abs(dl) < 1e-15 and abs(phase) < 1e-15
          and abs(i_bright - 1.0) < 1e-12 and abs(i_dark_analytical) < 1e-12)
    print("  Note: local quadratic response near this point belongs to "
          "Stage 4 (operating-point linearization), not tested here.")
    print(f"  T9 RESULT: {'PASS' if ok else 'FAIL'} (supporting check)")
    print()
    return ok


def beamsplitter_matrix() -> np.ndarray:
    """The frozen B matrix — not repository code (none exists); constructed
    here solely as the independent field-level reference for T10-T13."""
    return (1 / np.sqrt(2)) * np.array([[1, 1j], [1j, 1]])


def test_t10() -> bool:
    """T10 - 50:50 beamsplitter validation (independent of repository code)."""
    print("-" * 60)
    print("T10 - 50:50 Beamsplitter Validation (independent field-level model)")
    print("-" * 60)

    b = beamsplitter_matrix()
    all_pass = True

    # 10.1 Unitarity
    identity_err = float(np.max(np.abs(b.conj().T @ b - np.eye(2))))
    ok = identity_err < 1e-12
    all_pass &= ok
    print(f"  10.1 Unitarity: max|B^dagger B - I| = {identity_err:.3e} "
          f"{'PASS' if ok else 'FAIL'}")

    # 10.2 50:50 splitting
    e_in = np.array([1.0 + 0j, 0.0 + 0j])
    e_out = b @ e_in
    i1, i2 = abs(e_out[0]) ** 2, abs(e_out[1]) ** 2
    ok = abs(i1 - 0.5) < 1e-12 and abs(i2 - 0.5) < 1e-12
    all_pass &= ok
    print(f"  10.2 50:50 split: I1={i1:.12f}  I2={i2:.12f} "
          f"{'PASS' if ok else 'FAIL'}")

    # 10.3 Energy conservation
    conservation_err = abs((i1 + i2) - 1.0)
    ok = conservation_err < 1e-12
    all_pass &= ok
    print(f"  10.3 Conservation: I1+I2={i1+i2:.12f}  "
          f"error={conservation_err:.3e} {'PASS' if ok else 'FAIL'}")

    # 10.4 Relative phase
    rel_phase = np.angle(e_out[1]) - np.angle(e_out[0])
    ok = abs(rel_phase - np.pi / 2) < 1e-12
    all_pass &= ok
    print(f"  10.4 Relative phase: {rel_phase:.16f} rad "
          f"(expected pi/2={np.pi/2:.16f}) {'PASS' if ok else 'FAIL'}")

    print(f"  T10 RESULT: {'PASS' if all_pass else 'FAIL'}")
    print()
    return all_pass


def field_level_powers(delta_l_arm: float) -> tuple[float, float]:
    """Independent field-level recombination, using the same B matrix for
    split and recombination. Parameterized directly via phi_av and
    Delta_phi (analytical_model.md §8.3) rather than large absolute arm
    lengths, to avoid catastrophic cancellation in exp(i*2*k*L) for
    L ~ O(1 m). Returns (I_dark, I_bright)."""
    b = beamsplitter_matrix()
    e_in = np.array([1.0 + 0j, 0.0 + 0j])
    e_split = b @ e_in  # [E_x, E_y] before round trip

    k = 2 * np.pi / WAVELENGTH
    delta_phi = 2 * k * delta_l_arm
    phi_av = 0.0  # arbitrary common phase; cancels in |.|^2, per §8.3

    e_x_ret = e_split[0] * np.exp(1j * (phi_av + delta_phi / 2))
    e_y_ret = e_split[1] * np.exp(1j * (phi_av - delta_phi / 2))

    e_out = b @ np.array([e_x_ret, e_y_ret])
    i_dark = abs(e_out[0]) ** 2
    i_bright = abs(e_out[1]) ** 2
    return i_dark, i_bright


def test_t11() -> bool:
    """T11 - Field-level recombination validation."""
    print("-" * 60)
    print("T11 - Field-Level Recombination Validation")
    print("-" * 60)

    all_pass = True
    cases = [
        ("0", 0.0, 0.0, 1.0),
        ("lambda/8", WAVELENGTH / 8, 0.5, 0.5),
        ("lambda/4", WAVELENGTH / 4, 1.0, 0.0),
        ("lambda/2", WAVELENGTH / 2, 0.0, 1.0),
        ("-lambda/4", -WAVELENGTH / 4, 1.0, 0.0),
    ]
    for label, dl, exp_dark, exp_bright in cases:
        i_dark, i_bright = field_level_powers(dl)
        err = max(abs(i_dark - exp_dark), abs(i_bright - exp_bright))
        ok = err < 1e-9
        all_pass &= ok
        print(f"  DeltaL={label:10s} I_dark={i_dark:.6e} (exp {exp_dark})  "
              f"I_bright={i_bright:.6e} (exp {exp_bright})  "
              f"{'PASS' if ok else 'FAIL'}")

    # Non-special case
    dl = 0.137 * WAVELENGTH
    phase = 2 * (2 * np.pi / WAVELENGTH) * dl
    exp_dark = np.sin(phase / 2) ** 2
    exp_bright = np.cos(phase / 2) ** 2
    i_dark, i_bright = field_level_powers(dl)
    err = max(abs(i_dark - exp_dark), abs(i_bright - exp_bright))
    ok = err < 1e-9
    all_pass &= ok
    print(f"  Non-special DeltaL=0.137*lambda: Delta_phi={phase:.10f} rad")
    print(f"    expected I_dark={exp_dark:.16f}  I_bright={exp_bright:.16f}")
    print(f"    actual   I_dark={i_dark:.16f}  I_bright={i_bright:.16f}")
    print(f"    max discrepancy={err:.3e} {'PASS' if ok else 'FAIL'}")

    print(f"  T11 RESULT: {'PASS' if all_pass else 'FAIL'}")
    print()
    return all_pass


def test_t12() -> bool:
    """T12 - Bright + dark energy conservation."""
    print("-" * 60)
    print("T12 - Bright + Dark Power Conservation")
    print("-" * 60)

    phases = [0.0, np.pi / 2, np.pi, 1.234, 2.7, -0.8]
    all_pass = True
    max_err = 0.0
    for phi in phases:
        dl = phi * WAVELENGTH / (4 * np.pi)
        i_dark, i_bright = field_level_powers(dl)
        total = i_dark + i_bright
        err = abs(total - 1.0)
        max_err = max(max_err, err)
        ok = err < 1e-9
        all_pass &= ok
        print(f"  Delta_phi={phi:+.4f}  I_dark={i_dark:.10f}  "
              f"I_bright={i_bright:.10f}  sum={total:.12f}  "
              f"err={err:.3e} {'PASS' if ok else 'FAIL'}")

    print(f"  Max observed error: {max_err:.3e}")
    print(f"  T12 RESULT: {'PASS' if all_pass else 'FAIL'}")
    print()
    return all_pass


def test_t13() -> bool:
    """T13 - Dark-port known-answer validation (analytical relation, cross-
    checked against the field-level model; no dark-port function in repo)."""
    print("-" * 60)
    print("T13 - Dark-Port Known-Answer Validation")
    print("-" * 60)

    cases = [
        ("0", 0.0, 0.0),
        ("pi", np.pi, 1.0),
        ("pi/2", np.pi / 2, 0.5),
        ("-pi", -np.pi, 1.0),
    ]
    all_pass = True
    for label, phi, expected in cases:
        i_dark_analytical = 0.5 * (1.0 - np.cos(phi))
        dl = phi * WAVELENGTH / (4 * np.pi)
        i_dark_field, _ = field_level_powers(dl)
        err_expected = abs(i_dark_analytical - expected)
        err_cross = abs(i_dark_analytical - i_dark_field)
        ok = err_expected < 1e-9 and err_cross < 1e-9
        all_pass &= ok
        print(f"  Delta_phi={label:6s} expected={expected:.6f}  "
              f"analytical={i_dark_analytical:.12f}  "
              f"field-level={i_dark_field:.12f}  "
              f"{'PASS' if ok else 'FAIL'}")

    print("  Note: no dark-port function exists in src/interferometer.py; "
          "this cross-checks the analytical relation against the "
          "independent field-level model, per code_and_simulation_audit.md §5.4.")
    print(f"  T13 RESULT: {'PASS' if all_pass else 'FAIL'}")
    print()
    return all_pass


if __name__ == "__main__":
    print_environment()
    results = {}
    results["T1"] = test_t1()
    results["T2"] = test_t2()
    results["T3"] = test_t3()
    results["T4"] = test_t4()
    results["T5"] = test_t5()
    results["T6"] = test_t6()
    results["T7"] = test_t7()
    results["T8"] = test_t8()
    results["T9"] = test_t9()
    results["T10"] = test_t10()
    results["T11"] = test_t11()
    results["T12"] = test_t12()
    results["T13"] = test_t13()

    print("=" * 60)
    print("Summary")
    print("=" * 60)
    for name, passed in results.items():
        print(f"  {name}: {'PASS' if passed else 'FAIL'}")
    print()
    overall = all(results.values())
    print(f"Overall: {'ALL PASS' if overall else 'FAILURES PRESENT'}")
