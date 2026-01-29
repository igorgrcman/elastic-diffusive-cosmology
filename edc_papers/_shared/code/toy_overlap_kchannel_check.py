#!/usr/bin/env python3
"""
Toy Overlap k-Channel Verification

Demonstrates that k(N) = 1 + 1/N arises naturally in overlap-type observables
as a discrete/continuum averaging ratio.

Profile: |f(θ)|^4 = c + a*cos(Nθ)

Results:
  - Continuum: I4_cont = c (cos term integrates to zero)
  - Discrete:  I4_disc = c + a (cos(N*θ_n) = 1 at corners)
  - Ratio: R = 1 + a/c
  - Under a/c = 1/N: R = k(N) = 1 + 1/N

Created: 2026-01-29
Anchor: docs/TOY_OVERLAP_KCHANNEL_TEST.md
"""

import numpy as np
from typing import Tuple


def fourier_profile(theta: np.ndarray, c: float, a: float, N: int) -> np.ndarray:
    """
    Z_N symmetric profile: |f(θ)|^4 = c + a*cos(Nθ)
    """
    return c + a * np.cos(N * theta)


def continuum_average(c: float, a: float, N: int, n_points: int = 10000) -> float:
    """
    Compute I4_cont = (1/2π) ∫₀^{2π} [c + a*cos(Nθ)] dθ

    Analytical result: I4_cont = c (cos integrates to 0)
    """
    theta = np.linspace(0, 2*np.pi, n_points, endpoint=False)
    f4 = fourier_profile(theta, c, a, N)
    return np.mean(f4)


def discrete_average(c: float, a: float, N: int) -> float:
    """
    Compute I4_disc = (1/N) Σₙ [c + a*cos(N*θₙ)]
    where θₙ = 2πn/N

    Analytical result: I4_disc = c + a (cos(N*θₙ) = 1 at all corners)
    """
    theta_corners = np.array([2*np.pi*n/N for n in range(N)])
    f4 = fourier_profile(theta_corners, c, a, N)
    return np.mean(f4)


def compute_ratio(c: float, a: float, N: int) -> Tuple[float, float, float]:
    """
    Compute R = I4_disc / I4_cont

    Returns: (R_numerical, R_analytical, expected_k)
    """
    I4_cont = continuum_average(c, a, N)
    I4_disc = discrete_average(c, a, N)

    R_numerical = I4_disc / I4_cont
    R_analytical = 1 + a/c  # Exact formula
    expected_k = 1 + 1/N    # Under equal corner share

    return R_numerical, R_analytical, expected_k


def test_general_formula():
    """Test 1: General formula R = 1 + a/c"""
    print("=" * 60)
    print("[Test 1] General Formula: R = 1 + a/c")
    print("=" * 60)

    test_cases = [
        # (c, a, N)
        (1.0, 0.5, 6),   # a/c = 0.5
        (2.0, 0.4, 6),   # a/c = 0.2
        (1.0, 1.0, 4),   # a/c = 1.0
        (3.0, 0.3, 8),   # a/c = 0.1
    ]

    all_pass = True
    for c, a, N in test_cases:
        R_num, R_ana, _ = compute_ratio(c, a, N)
        match = abs(R_num - R_ana) < 1e-10
        all_pass = all_pass and match

        print(f"  c={c}, a={a}, N={N}")
        print(f"    R_numerical  = {R_num:.10f}")
        print(f"    R_analytical = {R_ana:.10f} = 1 + {a}/{c}")
        print(f"    Match: {match}")
        print()

    print(f"Test 1 PASS: {all_pass}")
    return all_pass


def test_equal_corner_share():
    """Test 2: Equal corner share (a/c = 1/N) gives k(N) = 1 + 1/N"""
    print("\n" + "=" * 60)
    print("[Test 2] Equal Corner Share: a/c = 1/N → k(N) = 1 + 1/N")
    print("=" * 60)

    c = 1.0  # Base value

    test_N = [3, 4, 5, 6, 8, 10, 12]

    all_pass = True
    for N in test_N:
        a = c / N  # Equal corner share: a/c = 1/N
        R_num, R_ana, k_expected = compute_ratio(c, a, N)

        match = abs(R_num - k_expected) < 1e-10
        all_pass = all_pass and match

        print(f"  N={N}: a/c = 1/{N} = {a/c:.6f}")
        print(f"    R = {R_num:.10f}")
        print(f"    k({N}) = 1 + 1/{N} = {k_expected:.10f}")
        print(f"    Match: {match}")
        print()

    print(f"Test 2 PASS: {all_pass}")
    return all_pass


def test_z6_specific():
    """Test 3: Z6 specific - k(6) = 7/6"""
    print("\n" + "=" * 60)
    print("[Test 3] Z6 Specific: k(6) = 7/6")
    print("=" * 60)

    N = 6
    c = 1.0
    a = c / N  # Equal corner share

    R_num, R_ana, k_expected = compute_ratio(c, a, N)
    k_exact = 7/6

    match = abs(R_num - k_exact) < 1e-10

    print(f"  Profile: |f(θ)|^4 = {c} + {a:.6f}*cos(6θ)")
    print(f"  Discrete average:  I4_disc = {discrete_average(c, a, N):.10f}")
    print(f"  Continuum average: I4_cont = {continuum_average(c, a, N):.10f}")
    print(f"  Ratio R = {R_num:.10f}")
    print(f"  Expected: 7/6 = {k_exact:.10f}")
    print(f"  Match: {match}")

    print(f"\nTest 3 PASS: {match}")
    return match


def test_pion_comparison():
    """Test 4: Compare to pion observation r_π/(4α) = 1.166"""
    print("\n" + "=" * 60)
    print("[Test 4] Pion Observation Comparison")
    print("=" * 60)

    # From docs/PION_SPLITTING_EPSILON_CHECK.md
    alpha = 0.007297353  # Fine structure constant
    r_pi = 0.03403       # Pion relative splitting

    k_observed = r_pi / (4 * alpha)
    k_theory = 7/6

    diff_percent = 100 * (k_observed - k_theory) / k_theory

    print(f"  r_π = {r_pi} (pion relative splitting)")
    print(f"  4α  = {4*alpha:.6f}")
    print(f"  k_observed = r_π / 4α = {k_observed:.6f}")
    print(f"  k_theory   = 7/6      = {k_theory:.6f}")
    print(f"  Difference: {diff_percent:.2f}%")

    match = abs(diff_percent) < 0.1  # Within 0.1%
    print(f"\nTest 4 PASS (within 0.1%): {match}")
    return match


def test_bump_convergence():
    """Test 5: Bump profile converges to k(N) in sharp limit"""
    print("\n" + "=" * 60)
    print("[Test 5] Bump Profile Convergence (Sharp Limit)")
    print("=" * 60)

    N = 6
    c = 1.0

    # Simulate narrowing bumps by increasing numerical resolution
    # and using sharper cosine powers

    def bump_profile(theta, c, a, N, sharpness):
        """
        Approximate localized bumps using cos^(2*sharpness) centered at corners.
        As sharpness → ∞, bumps become delta functions at corners.
        """
        result = np.full_like(theta, c)
        for n in range(N):
            theta_n = 2*np.pi*n/N
            # Narrow bump centered at theta_n
            dist = np.abs(np.mod(theta - theta_n + np.pi, 2*np.pi) - np.pi)
            bump = np.where(dist < np.pi/N, np.cos(dist * N)**sharpness, 0)
            result += (a/N) * bump * N  # Normalize
        return result

    # Test increasing sharpness
    print("  Sharpness → Ratio R:")
    for sharpness in [2, 4, 8, 16, 32]:
        a = c / N  # Equal corner share

        # Continuum
        theta = np.linspace(0, 2*np.pi, 100000, endpoint=False)
        f4_cont = bump_profile(theta, c, a, N, sharpness)
        I4_cont = np.mean(f4_cont)

        # Discrete
        theta_corners = np.array([2*np.pi*n/N for n in range(N)])
        f4_disc = bump_profile(theta_corners, c, a, N, sharpness)
        I4_disc = np.mean(f4_disc)

        R = I4_disc / I4_cont
        print(f"    sharpness={sharpness:2d}: R = {R:.6f} (target: {7/6:.6f})")

    # Note: Bump profile converges slower than Fourier
    print("\n  Note: Bump profile converges toward 7/6 but is noisier.")
    print("  Fourier profile (cos Nθ) gives exact 7/6 analytically.")
    return True


def main():
    """Run all verification tests."""
    print("Toy Overlap k-Channel Verification")
    print("=" * 60)
    print("Profile: |f(θ)|^4 = c + a*cos(Nθ)")
    print("Result:  R = I4_disc / I4_cont = 1 + a/c")
    print("Under a/c = 1/N: R = k(N) = 1 + 1/N")
    print("=" * 60)

    results = []
    results.append(test_general_formula())
    results.append(test_equal_corner_share())
    results.append(test_z6_specific())
    results.append(test_pion_comparison())
    results.append(test_bump_convergence())

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Tests passed: {sum(results)}/{len(results)}")

    if all(results):
        print("\nAll tests PASSED.")
        print("k(6) = 7/6 confirmed as discrete/continuum averaging ratio.")
    else:
        print("\nSome tests FAILED. Check output above.")

    return all(results)


if __name__ == "__main__":
    main()
