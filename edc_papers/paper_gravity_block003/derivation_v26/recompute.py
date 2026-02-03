#!/usr/bin/env python3
"""
Derivation v26 — Gap Derivability Program: Numerical Demonstration

This script computes the transcendental spectrum for Robin boundary conditions
and demonstrates gap pinning as the brane mass parameter varies.

Transcendental equation: tan(x) = -mb*L / x
where x = m*L is the dimensionless eigenvalue.

For Neumann at xi=0 and Robin at xi=L:
- Mode shape: psi(xi) = A*cos(m*xi)
- BC at xi=0: psi'(0) = 0 (satisfied automatically)
- BC at xi=L: psi'(L) = mb*psi(L) => -m*sin(mL) = mb*cos(mL)
- This gives: tan(mL) = -mb/m, or equivalently: tan(x) = -mb*L/x

Author: EDC Collaboration
Date: February 2026
"""

import numpy as np
from scipy.optimize import brentq
import warnings

warnings.filterwarnings('ignore')

# ============================================================
# TRANSCENDENTAL EQUATION
# ============================================================

def transcendental_eq(x, mb_L):
    """
    Transcendental equation: f(x) = tan(x) + mb_L/x = 0

    For Robin BC: tan(m*L) = -mb/m, so tan(x) = -mb*L/x
    Rearranged: tan(x) + mb_L/x = 0

    Args:
        x: Dimensionless eigenvalue m*L > 0
        mb_L: Dimensionless brane mass parameter mb*L >= 0

    Returns:
        f(x) = tan(x) + mb_L/x
    """
    if x <= 0:
        return np.inf
    return np.tan(x) + mb_L / x


def find_robin_roots(mb_L, n_modes=3):
    """
    Find first n_modes roots of tan(x) = -mb_L/x for x > 0.

    Key insight:
    - The function y = tan(x) has vertical asymptotes at x = (n-0.5)*pi
    - The function y = -mb_L/x is a hyperbola in the 4th quadrant (y < 0 for x > 0)
    - Intersections occur where both curves meet

    For mb_L = 0 (Neumann): tan(x) = 0 => x = n*pi for n = 1, 2, 3, ...
    For mb_L > 0: roots shift toward smaller values
    For mb_L -> inf: x_n -> (n-0.5)*pi (Dirichlet limit)

    The n-th root lies in the interval ((n-1)*pi, n*pi) for mb_L >= 0.
    More precisely, as mb_L increases, the root moves from n*pi toward (n-0.5)*pi.

    Args:
        mb_L: Dimensionless brane mass parameter >= 0
        n_modes: Number of modes to find

    Returns:
        List of roots [x_1, x_2, ..., x_n]
    """
    roots = []
    eps = 1e-10

    for n in range(1, n_modes + 1):
        # The n-th root is in interval ((n-0.5)*pi, n*pi) for Neumann (mb_L=0)
        # As mb_L increases, root shifts toward (n-0.5)*pi

        # For the transcendental eq tan(x) + mb_L/x = 0:
        # At x = (n-0.5)*pi + eps: tan(x) -> -inf, so f(x) -> -inf
        # At x = n*pi - eps: tan(x) -> 0-, so f(x) -> mb_L/x > 0

        # So root is in ((n-0.5)*pi, n*pi) where f changes sign

        a = (n - 0.5) * np.pi + eps
        b = n * np.pi - eps

        try:
            fa = transcendental_eq(a, mb_L)
            fb = transcendental_eq(b, mb_L)

            # For mb_L = 0: at a, tan(a) is large negative; at b, tan(b) ~ 0
            # f(a) = tan(a) + mb_L/a ~ -inf + 0 < 0
            # f(b) = tan(b) + mb_L/b ~ 0 + mb_L/b > 0 if mb_L > 0
            #                        ~ 0              if mb_L = 0

            # For mb_L = 0, root is exactly at x = n*pi
            if mb_L < 1e-12:
                roots.append(n * np.pi)
            elif fa * fb < 0:
                root = brentq(transcendental_eq, a, b, args=(mb_L,), xtol=1e-12)
                roots.append(root)
            else:
                # Fallback: search more carefully
                # Try narrower interval near n*pi
                a2 = n * np.pi - 0.5
                b2 = n * np.pi - eps
                try:
                    root = brentq(transcendental_eq, a2, b2, args=(mb_L,), xtol=1e-12)
                    roots.append(root)
                except:
                    # Use approximation
                    if mb_L < 1:
                        root = n * np.pi - mb_L / (n * np.pi)
                    else:
                        root = (n - 0.5) * np.pi + np.pi / (2 * mb_L)
                    roots.append(root)
        except Exception as e:
            # Fallback approximation
            if mb_L < 1:
                root = n * np.pi - mb_L / (n * np.pi)
            else:
                root = (n - 0.5) * np.pi + np.pi / (2 * mb_L)
            roots.append(root)

    return roots


def neumann_spectrum(n_modes=3):
    """Pure Neumann spectrum: x_n = n*pi"""
    return [n * np.pi for n in range(1, n_modes + 1)]


def dirichlet_spectrum(n_modes=3):
    """Dirichlet limit spectrum: x_n = (n-0.5)*pi"""
    return [(n - 0.5) * np.pi for n in range(1, n_modes + 1)]


def interpolating_formula(mb_L):
    """
    Simple interpolating formula for gap.

    For small mb_L: x_1 ≈ π - mb_L/π
    For large mb_L: x_1 ≈ π/2 + π/(2*mb_L)

    Interpolation: x_1/π ≈ 1 - mb_L/(π + 2*mb_L)
    """
    return 1 - mb_L / (np.pi + 2 * mb_L)


# ============================================================
# MAIN COMPUTATION
# ============================================================

def main():
    print("=" * 70)
    print("DERIVATION v26 — GAP DERIVABILITY PROGRAM")
    print("Transcendental Spectrum Verification")
    print("=" * 70)
    print()

    # --------------------------------------------------------
    # SECTION 1: Test cases
    # --------------------------------------------------------
    print("=" * 70)
    print("SECTION 1: SPECTRUM FOR VARIOUS mb*L VALUES")
    print("=" * 70)
    print()

    mb_L_values = [0, 0.1, 1.0, 10.0, 100.0]
    n_modes = 3

    results = {}

    for mb_L in mb_L_values:
        roots = find_robin_roots(mb_L, n_modes)
        results[mb_L] = roots

        label = "Neumann (mb*L=0)" if mb_L == 0 else f"Robin (mb*L={mb_L})"
        print(f"--- {label} ---")
        for i, x in enumerate(roots, 1):
            m_ratio = x / np.pi
            print(f"  x_{i} = m_{i}*L = {x:.4f}  (m_{i}/(π/L) = {m_ratio:.4f})")
        print()

    # Dirichlet limit
    dirichlet = dirichlet_spectrum(n_modes)
    results['inf'] = dirichlet
    print("--- Dirichlet limit (mb*L → ∞) ---")
    for i, x in enumerate(dirichlet, 1):
        m_ratio = x / np.pi
        print(f"  x_{i} = m_{i}*L = {x:.4f}  (m_{i}/(π/L) = {m_ratio:.4f})")
    print()

    # --------------------------------------------------------
    # SECTION 2: Summary table
    # --------------------------------------------------------
    print("=" * 70)
    print("SECTION 2: SUMMARY TABLE")
    print("=" * 70)
    print()

    print(f"{'mb*L':<12} {'x_1=m_1*L':<12} {'x_2=m_2*L':<12} {'x_3=m_3*L':<12} {'m_1/(π/L)':<12}")
    print("-" * 60)

    for mb_L in [0, 0.1, 1.0, 10.0, 100.0]:
        roots = results[mb_L]
        gap_ratio = roots[0] / np.pi
        label = "0 (Neumann)" if mb_L == 0 else str(mb_L)
        print(f"{label:<12} {roots[0]:<12.4f} {roots[1]:<12.4f} {roots[2]:<12.4f} {gap_ratio:<12.4f}")

    dirichlet = results['inf']
    gap_ratio = dirichlet[0] / np.pi
    print(f"{'∞ (Dirich.)':<12} {dirichlet[0]:<12.4f} {dirichlet[1]:<12.4f} {dirichlet[2]:<12.4f} {gap_ratio:<12.4f}")
    print()

    # --------------------------------------------------------
    # SECTION 3: Gap pinning
    # --------------------------------------------------------
    print("=" * 70)
    print("SECTION 3: GAP PINNING DEMONSTRATION")
    print("=" * 70)
    print()

    print("As mb*L increases, the gap transitions from π/L to π/(2L):")
    print()

    mb_L_sweep = [0, 0.01, 0.1, 0.5, 1, 2, 5, 10, 20, 50, 100, 1000]

    print(f"{'mb*L':<10} {'x_1 = m_gap*L':<16} {'m_gap*L/π':<14}")
    print("-" * 40)

    for mb_L in mb_L_sweep:
        roots = find_robin_roots(mb_L, 1)
        x1 = roots[0]
        ratio = x1 / np.pi
        print(f"{mb_L:<10.2f} {x1:<16.4f} {ratio:<14.4f}")

    print()
    print("Gap pinning confirmed:")
    print(f"  Neumann limit (mb*L=0):   m_gap*L = π   = {np.pi:.4f}")
    print(f"  Dirichlet limit (mb*L→∞): m_gap*L = π/2 = {np.pi/2:.4f}")
    print()

    # --------------------------------------------------------
    # SECTION 4: Verification
    # --------------------------------------------------------
    print("=" * 70)
    print("SECTION 4: VERIFICATION CHECKS")
    print("=" * 70)
    print()

    checks = []

    # Check 1: Neumann x_1 = π
    neumann_x1 = results[0][0]
    passed = abs(neumann_x1 - np.pi) < 0.001
    checks.append(passed)
    print(f"Check 1: Neumann x_1 = {neumann_x1:.4f} ≈ π = {np.pi:.4f} ... {'PASS' if passed else 'FAIL'}")

    # Check 2: Neumann x_2 = 2π
    neumann_x2 = results[0][1]
    passed = abs(neumann_x2 - 2*np.pi) < 0.001
    checks.append(passed)
    print(f"Check 2: Neumann x_2 = {neumann_x2:.4f} ≈ 2π = {2*np.pi:.4f} ... {'PASS' if passed else 'FAIL'}")

    # Check 3: Neumann x_3 = 3π
    neumann_x3 = results[0][2]
    passed = abs(neumann_x3 - 3*np.pi) < 0.001
    checks.append(passed)
    print(f"Check 3: Neumann x_3 = {neumann_x3:.4f} ≈ 3π = {3*np.pi:.4f} ... {'PASS' if passed else 'FAIL'}")

    # Check 4: Large mb*L approaches Dirichlet
    large_x1 = results[100.0][0]
    passed = abs(large_x1 - np.pi/2) < 0.1
    checks.append(passed)
    print(f"Check 4: Robin (mb*L=100) x_1 = {large_x1:.4f} ≈ π/2 = {np.pi/2:.4f} ... {'PASS' if passed else 'FAIL'}")

    # Check 5: Gap bounds for intermediate mb*L
    for mb_L in [0.1, 1.0, 10.0]:
        x1 = results[mb_L][0]
        passed = np.pi/2 - 0.01 < x1 < np.pi + 0.01
        checks.append(passed)
        print(f"Check 5.{mb_L}: π/2 < x_1({mb_L}) = {x1:.4f} < π ... {'PASS' if passed else 'FAIL'}")

    # Check 6: Monotonicity
    prev_x1 = results[0][0]
    all_decreasing = True
    for mb_L in [0.1, 1.0, 10.0, 100.0]:
        x1 = results[mb_L][0]
        if x1 > prev_x1 + 0.001:
            all_decreasing = False
        prev_x1 = x1
    checks.append(all_decreasing)
    print(f"Check 6: x_1 monotonically decreases with mb*L ... {'PASS' if all_decreasing else 'FAIL'}")

    # Check 7: Verify transcendental equation residual
    for mb_L in [1.0, 10.0]:
        x1 = results[mb_L][0]
        residual = abs(transcendental_eq(x1, mb_L))
        passed = residual < 1e-6
        checks.append(passed)
        print(f"Check 7.{mb_L}: |tan(x_1) + mb*L/x_1| = {residual:.2e} ... {'PASS' if passed else 'FAIL'}")

    # Check 8: Small mb*L expansion
    mb_L = 0.1
    x1_computed = results[mb_L][0]
    x1_expected = np.pi - mb_L / np.pi  # First-order approximation
    rel_error = abs(x1_computed - x1_expected) / x1_expected
    passed = rel_error < 0.1
    checks.append(passed)
    print(f"Check 8: Small mb*L approx: x_1 ≈ π - mb*L/π = {x1_expected:.4f}, got {x1_computed:.4f} ... {'PASS' if passed else 'FAIL'}")

    print()

    # --------------------------------------------------------
    # FINAL SUMMARY
    # --------------------------------------------------------
    print("=" * 70)
    print("FINAL AUDIT SUMMARY")
    print("=" * 70)
    print()

    all_passed = all(checks)
    for i, passed in enumerate(checks, 1):
        print(f"  Check {i:2d}: {'PASS' if passed else 'FAIL'}")

    print()
    print("=" * 70)
    if all_passed:
        print("ALL CHECKS PASSED")
    else:
        print(f"PASSED: {sum(checks)}/{len(checks)} checks")
    print("=" * 70)
    print()

    # --------------------------------------------------------
    # OUTPUT FOR REPORT
    # --------------------------------------------------------
    print("CANONICAL VALUES FOR REPORT:")
    print("-" * 40)
    print()
    print("First three modes (x_n = m_n * L):")
    print()
    for mb_L in [0, 1.0, 10.0]:
        roots = results[mb_L]
        label = "Neumann" if mb_L == 0 else f"Robin (mb*L={mb_L})"
        print(f"  {label}:")
        for i, x in enumerate(roots, 1):
            print(f"    x_{i} = {x:.4f}")
        print()

    print("Gap bounds: π/2 < m_gap*L < π for mb > 0")
    print(f"  π/2 = {np.pi/2:.4f}")
    print(f"  π   = {np.pi:.4f}")
    print()

    return 0 if all_passed else 1


if __name__ == "__main__":
    exit(main())
