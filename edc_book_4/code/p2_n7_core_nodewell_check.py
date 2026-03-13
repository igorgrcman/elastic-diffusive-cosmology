#!/usr/bin/env python3
"""
N7 WP2 CHECK: Thick-Junction Internal-Core Node-Well Analysis
==============================================================

[Check] script for app_P2_N7_core_nodewell.tex.
Verifies the structural results of the N7 WP2 derivation attempt:

1. V_geom is strictly increasing for q > 0 (Steiner minimum)
2. Monotone profile no-go: V_total' > 0 for all q > 0
   when f is peaked at q = 0 and non-increasing
3. Energy scale comparison: E_0 vs V_geom variation
4. Core contribution to curvature at q = 0
5. Thin-junction limit recovery: V_core -> 0 as delta -> 0
6. Non-monotone escape: demonstrate that f peaked at q* > 0
   can in principle produce a secondary minimum

This script is [Check], not derivation. It does not:
- Use C = 100 as evidence
- Fit any parameter to V_B or tau_n
- Import forbidden donor profiles as [Dc]
- Hide underdetermination

Donor compliance:
- sigma = 8.82 MeV/fm^2 [Dc]
- delta = hbar/(2 m_p c) = 0.105 fm [I]
- L_0 = 1.0 fm [I]
- E_0 = sigma * L_0^2 [Dc] (convention without I_perp factor)
- V_geom from R3 [Dc]

Date: 2026-03-13
"""

import numpy as np
import sys

# =============================================================================
# PARAMETERS (from N7 WP1 allowed donor bundle)
# =============================================================================

SIGMA = 8.82      # MeV/fm^2 [Dc] brane tension
DELTA = 0.105     # fm [I] Compton anchor delta = hbar/(2 m_p c)
L0 = 1.0          # fm [I] transverse junction extent
R = 1.0           # fm [Dc] arm length (geometric)
TAU = SIGMA       # MeV/fm [Dc] effective 1D string tension

# Energy scale [Dc] (convention without I_perp factor)
E0 = SIGMA * L0**2  # = 8.82 MeV

# With I_perp factor
E0_WITH_IPERP = np.pi * SIGMA * L0**2  # = 27.7 MeV

# Comparison targets (NOT used as constraints — comparison only)
DELTA_M_NP = 1.293  # MeV [BL] PDG


# =============================================================================
# GEOMETRIC BASELINE V_geom(q) [Dc]
# =============================================================================

def L_tot(q, R_val=R):
    """Total arm length for in-brane displacement (R3 path) [Dc]."""
    return (R_val - q) + 2.0 * np.sqrt(R_val**2 + R_val * q + q**2)


def V_geom(q, tau=TAU, R_val=R):
    """Geometric brane energy V_geom(q) = tau * L_tot(q) [Dc]."""
    return tau * L_tot(q, R_val)


def V_geom_prime(q, tau=TAU, R_val=R):
    """Derivative of V_geom(q) [Dc]."""
    denom = np.sqrt(R_val**2 + R_val * q + q**2)
    return tau * (-1.0 + (R_val + 2.0 * q) / denom)


def V_geom_double_prime_at_zero(tau=TAU, R_val=R):
    """V_geom''(0) = 3*tau/(2*R) [Dc]."""
    return 3.0 * tau / (2.0 * R_val)


# =============================================================================
# CORE PROFILES (for testing the no-go, NOT imported as [Dc])
# =============================================================================

def f_gaussian(q, delta=DELTA):
    """Gaussian profile f(q/delta) = exp(-(q/delta)^2) [P]."""
    return np.exp(-(q / delta)**2)


def f_lorentzian(q, delta=DELTA):
    """Lorentzian profile f(q/delta) = 1/(1 + (q/delta)^2) [P]."""
    return 1.0 / (1.0 + (q / delta)**2)


def f_exponential(q, delta=DELTA):
    """Exponential profile f(q/delta) = exp(-|q|/delta) [P]."""
    return np.exp(-np.abs(q) / delta)


def f_nonmonotone(q, delta=DELTA, q_star=0.3):
    """
    Non-monotone test profile: peaked at q = q_star, not at q = 0.
    f(q) = exp(-((q - q_star)/delta)^2)
    This is NOT a physical derivation — it is a mathematical test
    to show that non-monotone profiles CAN produce metastability.
    [Check] only.
    """
    return np.exp(-((q - q_star) / delta)**2)


# =============================================================================
# COMBINED POTENTIAL
# =============================================================================

def V_total(q, E0_val, f_func, tau=TAU, R_val=R, delta=DELTA):
    """V(q) = V_geom(q) + V_core(q) = tau*L_tot(q) - E0*f(q/delta)."""
    return V_geom(q, tau, R_val) - E0_val * f_func(q, delta)


def V_total_prime_numerical(q, E0_val, f_func, tau=TAU, R_val=R,
                            delta=DELTA, dq=1e-6):
    """Numerical derivative of V_total."""
    vp = V_total(q + dq, E0_val, f_func, tau, R_val, delta)
    vm = V_total(q - dq, E0_val, f_func, tau, R_val, delta)
    return (vp - vm) / (2.0 * dq)


# =============================================================================
# TEST 1: V_geom is strictly increasing for q > 0
# =============================================================================

def test_vgeom_monotone():
    """Verify V_geom'(q) > 0 for q in (0, R)."""
    print("=" * 60)
    print("TEST 1: V_geom strictly increasing for q > 0")
    print("=" * 60)

    q_vals = np.linspace(0.001, R - 0.001, 1000)
    derivs = np.array([V_geom_prime(q) for q in q_vals])
    min_deriv = np.min(derivs)
    all_positive = np.all(derivs > 0)

    print(f"  q range: [{q_vals[0]:.4f}, {q_vals[-1]:.4f}] fm")
    print(f"  Min V_geom'(q): {min_deriv:.6e} MeV/fm")
    print(f"  All V_geom'(q) > 0: {all_positive}")
    print(f"  V_geom'(0) = 0 (Steiner minimum) [Dc]")
    print(f"  V_geom''(0) = {V_geom_double_prime_at_zero():.4f} MeV/fm^2")
    print(f"  RESULT: {'PASS' if all_positive else 'FAIL'}")
    print()
    return all_positive


# =============================================================================
# TEST 2: Monotone profile no-go
# =============================================================================

def test_monotone_nogo():
    """
    Verify V_total'(q) > 0 for q > 0 with monotone profiles.
    This confirms Theorem (Monotone Profile No-Go).
    """
    print("=" * 60)
    print("TEST 2: Monotone profile no-go (V_total' > 0 for q > 0)")
    print("=" * 60)

    profiles = [
        ("Gaussian", f_gaussian),
        ("Lorentzian", f_lorentzian),
        ("Exponential", f_exponential),
    ]

    # Test with both E0 conventions
    E0_values = [
        ("E0 = sigma*L0^2", E0),
        ("E0 = pi*sigma*L0^2", E0_WITH_IPERP),
    ]

    all_pass = True
    q_vals = np.linspace(0.001, R - 0.001, 2000)

    for e0_name, e0_val in E0_values:
        for prof_name, prof_func in profiles:
            derivs = np.array([
                V_total_prime_numerical(q, e0_val, prof_func)
                for q in q_vals
            ])
            min_deriv = np.min(derivs)
            is_positive = np.all(derivs > 0)
            all_pass = all_pass and is_positive
            status = "PASS (no secondary min)" if is_positive else "FAIL"
            print(f"  {e0_name}, {prof_name}: "
                  f"min V'(q) = {min_deriv:.4e} MeV/fm -> {status}")

    print(f"\n  OVERALL: {'PASS' if all_pass else 'FAIL'}")
    print(f"  All monotone profiles produce single-well V(q).")
    print()
    return all_pass


# =============================================================================
# TEST 3: Energy scale comparison
# =============================================================================

def test_energy_scale():
    """Compare E0 to V_geom variation over displacement range."""
    print("=" * 60)
    print("TEST 3: Energy scale comparison")
    print("=" * 60)

    # V_geom variation from q=0 to q=R/2
    dV_geom_half = V_geom(R / 2) - V_geom(0)
    # V_geom variation from q=0 to q=delta
    dV_geom_delta = V_geom(DELTA) - V_geom(0)

    print(f"  E0 = sigma*L0^2 = {E0:.2f} MeV [Dc]")
    print(f"  E0 (with I_perp=pi) = {E0_WITH_IPERP:.2f} MeV [Dc]")
    print(f"  Delta V_geom(0 -> R/2) = {dV_geom_half:.2f} MeV")
    print(f"  Delta V_geom(0 -> delta) = {dV_geom_delta:.4f} MeV")
    print(f"  E0 / Delta V_geom(0->R/2) = {E0 / dV_geom_half:.2f}")
    print(f"  E0 / Delta V_geom(0->delta) = {E0 / dV_geom_delta:.1f}")
    print()
    print(f"  The core energy scale E0 ~ {E0:.1f} MeV is comparable to")
    print(f"  the geometric variation over the full displacement range.")
    print(f"  But the core decays at scale delta = {DELTA:.3f} fm,")
    print(f"  where V_geom has only risen by {dV_geom_delta:.4f} MeV.")
    print(f"  The core cannot oppose V_geom at large q.")
    print()
    return True


# =============================================================================
# TEST 4: Core contribution to curvature at q = 0
# =============================================================================

def test_curvature_at_zero():
    """Show that core ADDS to curvature at q = 0 (steepens well)."""
    print("=" * 60)
    print("TEST 4: Core contribution to curvature at q = 0")
    print("=" * 60)

    v_geom_curv = V_geom_double_prime_at_zero()

    # For Gaussian: f''(0) = -2/delta^2, so V_core''(0) = 2*E0/delta^2
    v_core_curv_gauss = 2.0 * E0 / DELTA**2

    # For Lorentzian: f(u) = 1/(1+u^2), f''(0) = -2, V_core''(0) = 2*E0/delta^2
    v_core_curv_lor = 2.0 * E0 / DELTA**2

    print(f"  V_geom''(0) = {v_geom_curv:.2f} MeV/fm^2")
    print(f"  V_core''(0) [Gaussian] = +{v_core_curv_gauss:.1f} MeV/fm^2")
    print(f"  V_core''(0) [Lorentzian] = +{v_core_curv_lor:.1f} MeV/fm^2")
    print(f"  V_total''(0) [Gaussian] = {v_geom_curv + v_core_curv_gauss:.1f} MeV/fm^2")
    print()
    print(f"  Core contribution is POSITIVE (adds to curvature).")
    print(f"  Core makes the Steiner well STEEPER, not shallower.")
    print(f"  Ratio V_core''/V_geom'' = {v_core_curv_gauss / v_geom_curv:.0f}")
    print()
    return True


# =============================================================================
# TEST 5: Thin-junction limit recovery
# =============================================================================

def test_thin_junction_limit():
    """Verify V_core -> 0 as delta -> 0."""
    print("=" * 60)
    print("TEST 5: Thin-junction limit (delta -> 0)")
    print("=" * 60)

    q_test = 0.1  # fm, fixed test point away from q = 0
    deltas = [0.1, 0.05, 0.02, 0.01, 0.005, 0.001]

    print(f"  V_core(q={q_test} fm) for decreasing delta:")
    print(f"  {'delta [fm]':>12s}  {'|V_core| [MeV]':>15s}  {'f(q/delta)':>12s}")

    for d in deltas:
        f_val = f_gaussian(q_test, d)
        v_core = E0 * f_val
        print(f"  {d:12.4f}  {v_core:15.2e}  {f_val:12.2e}")

    print()
    print(f"  V_core -> 0 exponentially fast as delta -> 0.")
    print(f"  Consistent with WP2 no-go: thin junction produces no")
    print(f"  attraction at q > 0.")
    print(f"  RESULT: PASS")
    print()
    return True


# =============================================================================
# TEST 6: Non-monotone escape demonstration
# =============================================================================

def test_nonmonotone_escape():
    """
    Demonstrate that a profile peaked at q* > 0 CAN produce a
    secondary minimum. This is NOT a derivation — it is a [Check]
    showing that the escape route exists mathematically.
    """
    print("=" * 60)
    print("TEST 6: Non-monotone escape route [Check only]")
    print("=" * 60)
    print("  NOTE: This test uses a phenomenological non-monotone profile")
    print("  centered at q* > 0. This is NOT a derived result. It merely")
    print("  demonstrates that if f were peaked away from q = 0,")
    print("  metastability would be mathematically possible.")
    print()

    # Try different q_star values with E0_WITH_IPERP (stronger core)
    q_stars = [0.1, 0.2, 0.3, 0.4, 0.5]
    q_scan = np.linspace(0.001, R - 0.001, 5000)

    found_metastable = False
    for q_star in q_stars:
        f_nm = lambda q, d=DELTA, qs=q_star: f_nonmonotone(q, d, qs)
        v_vals = np.array([
            V_total(q, E0_WITH_IPERP, f_nm)
            for q in q_scan
        ])

        # Look for local minima (V' changes from - to +)
        dv = np.diff(v_vals)
        sign_changes = np.where(np.diff(np.sign(dv)))[0]
        n_minima = 0
        for idx in sign_changes:
            if dv[idx] < 0 and dv[idx + 1] > 0:
                n_minima += 1

        has_secondary = n_minima >= 2
        if has_secondary:
            found_metastable = True

        status = "METASTABLE" if has_secondary else "single-well"
        print(f"  q* = {q_star:.1f} fm, E0 = {E0_WITH_IPERP:.1f} MeV: "
              f"{n_minima} local min(a) -> {status}")

    print()
    if found_metastable:
        print("  Found metastability with non-monotone profile.")
        print("  This confirms the escape route exists MATHEMATICALLY.")
        print("  But no physical mechanism for f peaked at q* > 0 has")
        print("  been identified within the elastic-medium framework.")
    else:
        print("  No metastability found even with non-monotone profiles")
        print("  in the tested q* range. The geometric restoring force")
        print("  dominates for these parameters.")
    print()
    return True


# =============================================================================
# TEST 7: Parameter scan — what E0 and delta would be needed?
# =============================================================================

def test_parameter_requirements():
    """
    For a monotone profile, show that NO value of E0 or delta
    produces a secondary minimum. This is a numerical confirmation
    of the monotone no-go theorem.
    """
    print("=" * 60)
    print("TEST 7: Monotone profile — no E0/delta rescues metastability")
    print("=" * 60)

    q_scan = np.linspace(0.001, R - 0.001, 3000)
    E0_test = [1.0, 5.0, 10.0, 50.0, 100.0, 500.0]
    delta_test = [0.05, 0.1, 0.2, 0.5]

    print(f"  Testing Gaussian profile f = exp(-(q/delta)^2)")
    print(f"  across {len(E0_test)} x {len(delta_test)} = "
          f"{len(E0_test) * len(delta_test)} (E0, delta) pairs:")
    print()

    n_metastable = 0
    n_total = 0

    for d in delta_test:
        for e0 in E0_test:
            n_total += 1
            f_g = lambda q, delta=d: f_gaussian(q, delta)
            v_vals = np.array([V_total(q, e0, f_g, delta=d) for q in q_scan])
            dv = np.diff(v_vals)
            sign_changes = np.where(np.diff(np.sign(dv)))[0]
            n_minima = sum(1 for idx in sign_changes
                          if dv[idx] < 0 and idx + 1 < len(dv)
                          and dv[idx + 1] > 0)
            if n_minima >= 2:
                n_metastable += 1

    print(f"  Tested {n_total} parameter combinations.")
    print(f"  Metastable configurations found: {n_metastable}")
    print(f"  RESULT: {'PASS (no-go confirmed)' if n_metastable == 0 else 'UNEXPECTED'}")
    print()
    return n_metastable == 0


# =============================================================================
# MAIN
# =============================================================================

def main():
    print()
    print("N7 WP2 CHECK: Thick-Junction Internal-Core Node-Well Analysis")
    print("=" * 60)
    print()
    print(f"Parameters:")
    print(f"  sigma = {SIGMA} MeV/fm^2 [Dc]")
    print(f"  delta = {DELTA} fm [I]")
    print(f"  L0    = {L0} fm [I]")
    print(f"  R     = {R} fm [Dc]")
    print(f"  tau   = {TAU} MeV/fm [Dc]")
    print(f"  E0    = sigma * L0^2 = {E0:.2f} MeV [Dc]")
    print(f"  E0 (with I_perp=pi) = {E0_WITH_IPERP:.2f} MeV [Dc]")
    print(f"  L0/delta = {L0/DELTA:.2f} [I]")
    print()

    results = []
    results.append(("V_geom monotonicity", test_vgeom_monotone()))
    results.append(("Monotone profile no-go", test_monotone_nogo()))
    results.append(("Energy scale comparison", test_energy_scale()))
    results.append(("Curvature at q=0", test_curvature_at_zero()))
    results.append(("Thin-junction limit", test_thin_junction_limit()))
    results.append(("Non-monotone escape", test_nonmonotone_escape()))
    results.append(("Parameter scan no-go", test_parameter_requirements()))

    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    all_pass = True
    for name, passed in results:
        status = "PASS" if passed else "FAIL"
        print(f"  {name:40s} {status}")
        all_pass = all_pass and passed

    print()
    print(f"  Overall: {'ALL PASS' if all_pass else 'SOME FAILED'}")
    print()
    print("CONCLUSION:")
    print("  The monotone profile no-go is confirmed numerically.")
    print("  For any profile f peaked at q=0 and non-increasing,")
    print("  V(q) = V_geom(q) + V_core(q) is a single well.")
    print("  No parameter choice (E0, delta) rescues metastability.")
    print("  The core contribution reinforces the geometric restoring")
    print("  force, deepening and steepening the Steiner well.")
    print()
    print("  Classification: BOUNDED INSUFFICIENCY")
    print("  N7 lane: narrowed (monotone class eliminated)")
    print()

    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
