#!/usr/bin/env python3
"""
Derivation v25 — Proxy Family Robustness Verification Script

This script independently verifies all numerical values in derivation v25,
computing R_xi and M_5 for each electroweak proxy (M_Z, M_W, v_EW) and
quantifying robustness metrics.

Author: EDC Collaboration
Date: February 2026
"""

import numpy as np

# ============================================================
# CONSTANTS
# ============================================================

# Fundamental constants
HBAR_C_GEV_M = 1.97327e-16  # GeV·m
HBAR_C_MEV_FM = 197.327     # MeV·fm

# Planck masses
M_PL_REDUCED = 2.435e18     # GeV (reduced Planck mass)
M_PL_ORIGINAL = 1.221e19    # GeV (original Planck mass)

# Electroweak proxy values (PDG 2024)
M_Z = 91.1876               # GeV
M_Z_ERR = 0.0021            # GeV

M_W = 80.3692               # GeV
M_W_ERR = 0.0133            # GeV

V_EW = 246.22               # GeV
V_EW_ERR = 0.01             # GeV (nominal; has scheme dependence)

# Conversion factor
FACTOR_8PI_THIRD = (8 * np.pi) ** (1/3)  # ≈ 2.929

# ============================================================
# DERIVED QUANTITIES
# ============================================================

def compute_Rxi(M_star):
    """
    Compute compactification scale R_xi from proxy mass.

    R_xi = π ℏc / M_star

    Args:
        M_star: Proxy mass in GeV

    Returns:
        R_xi in meters
    """
    return np.pi * HBAR_C_GEV_M / M_star


def compute_Rxi_natural(M_star):
    """
    Compute R_xi in natural units (GeV^-1).

    R_xi = π / M_star
    """
    return np.pi / M_star


def compute_M5_reduced(M_star):
    """
    Compute 5D Planck mass (reduced convention).

    M_5^(red) = (M_Pl^2 · M_star / (π ℏc))^(1/3)

    But more simply in natural units:
    M_5^(red) = (M_Pl^2 / R_xi)^(1/3) = (M_Pl^2 · M_star / π)^(1/3)

    Args:
        M_star: Proxy mass in GeV

    Returns:
        M_5 in GeV
    """
    # Using natural units formula
    return (M_PL_REDUCED**2 * M_star / np.pi) ** (1/3)


def compute_M5_original(M_star):
    """
    Compute 5D Planck mass (original convention).

    M_5^(orig) = (8π)^(1/3) · M_5^(red)
    """
    return FACTOR_8PI_THIRD * compute_M5_reduced(M_star)


def compute_delta_log10_M5(M_star, M_ref=M_Z):
    """
    Compute logarithmic deviation in M_5 relative to reference.

    Δlog₁₀(M_5) = (1/3) log₁₀(M_star / M_ref)
    """
    return (1/3) * np.log10(M_star / M_ref)


def compute_M5_ratio(M_star, M_ref=M_Z):
    """
    Compute ratio M_5(M_star) / M_5(M_ref).

    = (M_star / M_ref)^(1/3)
    """
    return (M_star / M_ref) ** (1/3)


def compute_Rxi_ratio(M_star, M_ref=M_Z):
    """
    Compute ratio R_xi(M_star) / R_xi(M_ref).

    = M_ref / M_star
    """
    return M_ref / M_star


def compute_error_M5(delta_M_star_rel):
    """
    Compute relative error in M_5 from relative error in M_star.

    δM_5/M_5 = (1/3) δM_star/M_star
    """
    return delta_M_star_rel / 3


# ============================================================
# MAIN COMPUTATION
# ============================================================

def main():
    print("=" * 70)
    print("DERIVATION v25 — PROXY FAMILY ROBUSTNESS VERIFICATION")
    print("=" * 70)
    print()

    # Define proxy family
    proxies = {
        'M_Z': (M_Z, M_Z_ERR),
        'M_W': (M_W, M_W_ERR),
        'v_EW': (V_EW, V_EW_ERR),
    }

    # --------------------------------------------------------
    # SECTION 1: Individual proxy calculations
    # --------------------------------------------------------
    print("=" * 70)
    print("PROXY FAMILY RESULTS")
    print("=" * 70)
    print()

    results = {}

    for name, (M_star, M_star_err) in proxies.items():
        print(f"--- {name} proxy ---")
        print(f"  M_star = {M_star:.4f} ± {M_star_err:.4f} GeV")
        print(f"  δM_star/M_star = {M_star_err/M_star:.2e}")
        print()

        # Compute R_xi
        Rxi = compute_Rxi(M_star)
        Rxi_nat = compute_Rxi_natural(M_star)
        print(f"  R_xi = {Rxi:.3e} m")
        print(f"  R_xi = {Rxi_nat:.5f} GeV^-1")
        print()

        # Compute M_5
        M5_red = compute_M5_reduced(M_star)
        M5_orig = compute_M5_original(M_star)
        print(f"  M_5 (reduced)  = {M5_red:.3e} GeV")
        print(f"  M_5 (original) = {M5_orig:.3e} GeV")
        print()

        # Compute ratios relative to M_Z
        delta_log = compute_delta_log10_M5(M_star, M_Z)
        ratio_M5 = compute_M5_ratio(M_star, M_Z)
        ratio_Rxi = compute_Rxi_ratio(M_star, M_Z)
        print(f"  M_star / M_Z = {M_star/M_Z:.4f}")
        print(f"  R_xi / R_xi(M_Z) = {ratio_Rxi:.4f}")
        print(f"  M_5 / M_5(M_Z) = {ratio_M5:.4f}")
        print(f"  Δlog₁₀(M_5) = {delta_log:+.4f}")
        print()

        # Error propagation
        delta_M_star_rel = M_star_err / M_star
        delta_Rxi_rel = delta_M_star_rel
        delta_M5_rel = compute_error_M5(delta_M_star_rel)
        print(f"  Error propagation:")
        print(f"    δR_xi/R_xi = {delta_Rxi_rel:.2e}")
        print(f"    δM_5/M_5 = {delta_M5_rel:.2e}")
        print()

        results[name] = {
            'M_star': M_star,
            'M_star_err': M_star_err,
            'Rxi': Rxi,
            'Rxi_nat': Rxi_nat,
            'M5_red': M5_red,
            'M5_orig': M5_orig,
            'delta_log': delta_log,
            'ratio_M5': ratio_M5,
            'ratio_Rxi': ratio_Rxi,
            'delta_M5_rel': delta_M5_rel,
        }

    # --------------------------------------------------------
    # SECTION 2: Robustness metrics
    # --------------------------------------------------------
    print("=" * 70)
    print("ROBUSTNESS METRICS")
    print("=" * 70)
    print()

    # Logarithmic spread
    delta_logs = [results[name]['delta_log'] for name in proxies]
    sigma_log = max(abs(d) for d in delta_logs)
    total_spread = max(delta_logs) - min(delta_logs)

    print(f"Δlog₁₀(M_5) values:")
    for name in proxies:
        print(f"  {name}: {results[name]['delta_log']:+.4f}")
    print()
    print(f"σ_log (max |Δlog₁₀|) = {sigma_log:.4f}")
    print(f"Total spread = {total_spread:.4f}")
    print()

    # Factor spread
    M5_values = [results[name]['M5_red'] for name in proxies]
    F_spread = max(M5_values) / min(M5_values)

    print(f"M_5 (reduced) range: [{min(M5_values):.2e}, {max(M5_values):.2e}] GeV")
    print(f"Factor spread F = {F_spread:.3f}")
    print()

    # Check: F should equal 10^(total_spread)
    F_from_log = 10**total_spread
    print(f"Verification: 10^(total_spread) = {F_from_log:.3f}")
    print()

    # --------------------------------------------------------
    # SECTION 3: Summary tables
    # --------------------------------------------------------
    print("=" * 70)
    print("SUMMARY TABLE")
    print("=" * 70)
    print()

    print(f"{'Proxy':<8} {'M_star':<10} {'δM/M':<12} {'R_xi (m)':<14} {'M5_red (GeV)':<14} {'M5_orig (GeV)':<14} {'Δlog₁₀M5':<10}")
    print("-" * 90)
    for name in proxies:
        r = results[name]
        print(f"{name:<8} {r['M_star']:<10.2f} {r['M_star_err']/r['M_star']:<12.2e} {r['Rxi']:<14.2e} {r['M5_red']:<14.2e} {r['M5_orig']:<14.2e} {r['delta_log']:<+10.3f}")
    print()

    print(f"{'Proxy':<8} {'M*/M_Z':<10} {'R_xi/R_xi(Z)':<14} {'M5/M5(Z)':<12}")
    print("-" * 50)
    for name in proxies:
        r = results[name]
        print(f"{name:<8} {r['M_star']/M_Z:<10.3f} {r['ratio_Rxi']:<14.3f} {r['ratio_M5']:<12.3f}")
    print()

    # --------------------------------------------------------
    # SECTION 4: Verification checks
    # --------------------------------------------------------
    print("=" * 70)
    print("VERIFICATION CHECKS")
    print("=" * 70)
    print()

    checks = []

    # Check 1: R_xi(M_Z) value
    Rxi_MZ_expected = 6.798e-18
    Rxi_MZ_computed = results['M_Z']['Rxi']
    rel_diff = abs(Rxi_MZ_computed - Rxi_MZ_expected) / Rxi_MZ_expected
    passed = rel_diff < 0.01
    checks.append(passed)
    print(f"R_xi(M_Z) = {Rxi_MZ_computed:.3e} m (expected ~6.80e-18) ... {'PASS' if passed else 'FAIL'}")

    # Check 2: M_5 (red) for M_Z
    M5_MZ_red_expected = 5.56e12
    M5_MZ_red_computed = results['M_Z']['M5_red']
    rel_diff = abs(M5_MZ_red_computed - M5_MZ_red_expected) / M5_MZ_red_expected
    passed = rel_diff < 0.01
    checks.append(passed)
    print(f"M_5^(red)(M_Z) = {M5_MZ_red_computed:.3e} GeV (expected ~5.56e12) ... {'PASS' if passed else 'FAIL'}")

    # Check 3: M_5 (orig) for M_Z
    M5_MZ_orig_expected = 1.63e13
    M5_MZ_orig_computed = results['M_Z']['M5_orig']
    rel_diff = abs(M5_MZ_orig_computed - M5_MZ_orig_expected) / M5_MZ_orig_expected
    passed = rel_diff < 0.01
    checks.append(passed)
    print(f"M_5^(orig)(M_Z) = {M5_MZ_orig_computed:.3e} GeV (expected ~1.63e13) ... {'PASS' if passed else 'FAIL'}")

    # Check 4: (8π)^(1/3) factor
    factor_expected = 2.929
    rel_diff = abs(FACTOR_8PI_THIRD - factor_expected) / factor_expected
    passed = rel_diff < 0.01
    checks.append(passed)
    print(f"(8π)^(1/3) = {FACTOR_8PI_THIRD:.4f} (expected ~2.929) ... {'PASS' if passed else 'FAIL'}")

    # Check 5: R_xi(M_W) > R_xi(M_Z) (since M_W < M_Z)
    passed = results['M_W']['Rxi'] > results['M_Z']['Rxi']
    checks.append(passed)
    print(f"R_xi(M_W) > R_xi(M_Z) check ... {'PASS' if passed else 'FAIL'}")

    # Check 6: R_xi(v_EW) < R_xi(M_Z) (since v_EW > M_Z)
    passed = results['v_EW']['Rxi'] < results['M_Z']['Rxi']
    checks.append(passed)
    print(f"R_xi(v_EW) < R_xi(M_Z) check ... {'PASS' if passed else 'FAIL'}")

    # Check 7: M_5 scaling (M_W < M_Z implies M_5(M_W) < M_5(M_Z))
    passed = results['M_W']['M5_red'] < results['M_Z']['M5_red']
    checks.append(passed)
    print(f"M_5(M_W) < M_5(M_Z) check ... {'PASS' if passed else 'FAIL'}")

    # Check 8: M_5 scaling (v_EW > M_Z implies M_5(v_EW) > M_5(M_Z))
    passed = results['v_EW']['M5_red'] > results['M_Z']['M5_red']
    checks.append(passed)
    print(f"M_5(v_EW) > M_5(M_Z) check ... {'PASS' if passed else 'FAIL'}")

    # Check 9: Δlog₁₀(M_5) for M_W
    delta_MW_expected = -0.018
    delta_MW_computed = results['M_W']['delta_log']
    passed = abs(delta_MW_computed - delta_MW_expected) < 0.002
    checks.append(passed)
    print(f"Δlog₁₀(M_5) for M_W = {delta_MW_computed:.4f} (expected ~-0.018) ... {'PASS' if passed else 'FAIL'}")

    # Check 10: Δlog₁₀(M_5) for v_EW
    delta_vEW_expected = 0.143
    delta_vEW_computed = results['v_EW']['delta_log']
    passed = abs(delta_vEW_computed - delta_vEW_expected) < 0.002
    checks.append(passed)
    print(f"Δlog₁₀(M_5) for v_EW = {delta_vEW_computed:.4f} (expected ~+0.143) ... {'PASS' if passed else 'FAIL'}")

    # Check 11: Total spread
    spread_expected = 0.161
    passed = abs(total_spread - spread_expected) < 0.002
    checks.append(passed)
    print(f"Total spread = {total_spread:.4f} (expected ~0.161) ... {'PASS' if passed else 'FAIL'}")

    # Check 12: Factor spread
    F_expected = 1.45
    passed = abs(F_spread - F_expected) < 0.02
    checks.append(passed)
    print(f"Factor spread = {F_spread:.3f} (expected ~1.45) ... {'PASS' if passed else 'FAIL'}")

    # Check 13: Error suppression factor (1/3)
    # δM_5/M_5 = (1/3) δM_star/M_star
    delta_M5_MZ = results['M_Z']['delta_M5_rel']
    delta_Mstar_MZ = M_Z_ERR / M_Z
    ratio = delta_M5_MZ / delta_Mstar_MZ
    passed = abs(ratio - 1/3) < 0.001
    checks.append(passed)
    print(f"Error suppression ratio = {ratio:.4f} (expected 0.3333) ... {'PASS' if passed else 'FAIL'}")

    # Check 14: M_5 values for M_W
    M5_MW_red_expected = 5.33e12
    rel_diff = abs(results['M_W']['M5_red'] - M5_MW_red_expected) / M5_MW_red_expected
    passed = rel_diff < 0.01
    checks.append(passed)
    print(f"M_5^(red)(M_W) = {results['M_W']['M5_red']:.3e} GeV (expected ~5.33e12) ... {'PASS' if passed else 'FAIL'}")

    # Check 15: M_5 values for v_EW
    M5_vEW_red_expected = 7.74e12
    rel_diff = abs(results['v_EW']['M5_red'] - M5_vEW_red_expected) / M5_vEW_red_expected
    passed = rel_diff < 0.01
    checks.append(passed)
    print(f"M_5^(red)(v_EW) = {results['v_EW']['M5_red']:.3e} GeV (expected ~7.74e12) ... {'PASS' if passed else 'FAIL'}")

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
        status = "PASS" if passed else "FAIL"
        print(f"  Check {i:2d}: {status}")

    print()
    print("=" * 70)
    if all_passed:
        print("ALL CHECKS PASSED")
    else:
        print("SOME CHECKS FAILED")
    print("=" * 70)
    print()

    # --------------------------------------------------------
    # OUTPUT FOR REPORT
    # --------------------------------------------------------
    print("CANONICAL VALUES FOR REPORT:")
    print("-" * 40)
    print(f"M_Z proxy:")
    print(f"  R_xi     = {results['M_Z']['Rxi']:.4e} m")
    print(f"  M_5(red) = {results['M_Z']['M5_red']:.3e} GeV")
    print(f"  M_5(orig)= {results['M_Z']['M5_orig']:.3e} GeV")
    print()
    print(f"M_W proxy:")
    print(f"  R_xi     = {results['M_W']['Rxi']:.4e} m")
    print(f"  M_5(red) = {results['M_W']['M5_red']:.3e} GeV")
    print(f"  M_5(orig)= {results['M_W']['M5_orig']:.3e} GeV")
    print()
    print(f"v_EW proxy:")
    print(f"  R_xi     = {results['v_EW']['Rxi']:.4e} m")
    print(f"  M_5(red) = {results['v_EW']['M5_red']:.3e} GeV")
    print(f"  M_5(orig)= {results['v_EW']['M5_orig']:.3e} GeV")
    print()
    print(f"Robustness metrics:")
    print(f"  Total spread Δlog₁₀(M_5) = {total_spread:.4f}")
    print(f"  Factor spread F = {F_spread:.3f}")
    print(f"  (8π)^(1/3) = {FACTOR_8PI_THIRD:.4f}")
    print()

    return 0 if all_passed else 1


if __name__ == "__main__":
    exit(main())
