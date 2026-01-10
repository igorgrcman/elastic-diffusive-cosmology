
"""edc_gravity_from_edc.py

EDC Gravity Verification Suite (Bridge: River Model -> PG -> Schwarzschild)

Epistemic status (strict):
  - IDENTIFIED: River-flow profile v(r)^2 = 2GM/r (Newtonian potential mapping)
  - BASELINE: Coordinate equivalence of Painlevé–Gullstrand and Schwarzschild forms
  - DERIVED (within this script): Algebraic construction of PG metric and removal of cross-term
  - DERIVED (weak-field expansion): PPN gamma extracted from the metric expansion

This script DOES NOT prove that EDC derives the Newtonian potential or the acoustic-metric mapping
from first principles. It verifies internal mathematical consistency of the bridge layer.

Units: SI for numerical parts (baseline constants), symbolic algebra keeps c, G, M.
"""

import numpy as np
import sympy as sp


def _ppn_gamma_from_schwarzschild_weak_field():
    """Extract PPN gamma from the weak-field expansion.

    Use:
      g_tt = -(1 - 2U/c^2) c^2 + O(U^2)
      g_rr =  1 + 2γ U/c^2 + O(U^2)
    with U = GM/r.

    For Schwarzschild, γ = 1.
    """
    r, G, M, c = sp.symbols("r G M c", positive=True)
    U = G * M / r

    g_rr = 1 / (1 - 2 * U / c**2)

    # series in eps = U/c^2 about 0
    eps = sp.Symbol("eps")
    g_rr_series = sp.series(g_rr.subs(U / c**2, eps), eps, 0, 2).removeO()
    # g_rr ≈ 1 + 2*eps + ...
    coeff = sp.expand(g_rr_series - 1).coeff(eps, 1)  # should be 2*gamma
    gamma = sp.simplify(coeff / 2)
    return sp.simplify(gamma)


def _build_pg_metric():
    """Build the Painlevé–Gullstrand (PG) metric for radial flow v(r).

    PG line element:
      ds^2 = -(c^2 - v^2) dt^2 + 2 v dt dr + dr^2 + r^2 dΩ^2

    with v(r)^2 = 2GM/r (IDENTIFIED mapping).
    """
    r, theta, G, M, c = sp.symbols("r theta G M c", positive=True)
    v = sp.sqrt(2 * G * M / r)
    rs = 2 * G * M / c**2

    g = sp.Matrix(
        [
            [-(c**2 - v**2), v, 0, 0],
            [v, 1, 0, 0],
            [0, 0, r**2, 0],
            [0, 0, 0, r**2 * sp.sin(theta) ** 2],
        ]
    )
    return g, rs, v


def _pg_to_schwarzschild_rr():
    """Remove PG cross-term and recover Schwarzschild g_rr.

    Use the standard time shift:
      dt_S = dt + (v / (c^2 - v^2)) dr

    The rr component becomes:
      g_rr^S = 1 + v^2/(c^2 - v^2) = 1/(1 - r_s/r)
    """
    r, G, M, c = sp.symbols("r G M c", positive=True)
    v = sp.sqrt(2 * G * M / r)
    rs = 2 * G * M / c**2

    g_rr_s = 1 + v**2 / (c**2 - v**2)
    g_rr_s_simplified = sp.simplify(g_rr_s.subs(v**2, c**2 * rs / r))
    g_rr_expected = 1 / (1 - rs / r)
    return sp.simplify(g_rr_s_simplified), sp.simplify(g_rr_expected)


def run():
    print("=" * 60)
    print("EDC GRAVITY VERIFICATION SUITE (Bridge Layer)")
    print("Based on Book v17.49 River Model / PG mapping")
    print("=" * 60)
    print()

    g_pg, rs, v = _build_pg_metric()
    print("[IDENTIFIED] River-flow profile: v(r)^2 = 2GM/r")
    print("[DERIVED] PG metric components (t,r sector):")
    print(f"  g_tt = {sp.simplify(g_pg[0,0])}")
    print(f"  g_tr = {sp.simplify(g_pg[0,1])}")
    print(f"  g_rr = {sp.simplify(g_pg[1,1])}")
    print()

    g_rr_s, g_rr_expected = _pg_to_schwarzschild_rr()
    print("[BASELINE/DERIVED] PG -> Schwarzschild (cross-term removal) check:")
    print(f"  Derived g_rr^S  = {g_rr_s}")
    print(f"  Expected g_rr^S = {g_rr_expected}")
    print(f"  PASS: {sp.simplify(g_rr_s - g_rr_expected) == 0}")
    print()

    gamma = _ppn_gamma_from_schwarzschild_weak_field()
    print("[DERIVED] PPN parameter gamma (from weak-field expansion):")
    print(f"  gamma = {gamma}")
    print("  PASS: gamma == 1" if gamma == 1 else "  FAIL: gamma != 1")
    print()

    # --- Numerical observables (baseline constants) ---
    # These constants are NOT derived by EDC in this script.
    # They are used only to generate concrete numbers for well-known weak-field observables.
    G_val = 6.67430e-11       # CODATA baseline
    c_val = 299792458.0       # exact SI
    M_sun = 1.98847e30        # baseline (commonly used)
    R_sun = 6.957e8           # baseline (commonly used)

    # Light deflection at limb (PPN): alpha = (1+gamma) * 2GM/(c^2 b)
    gamma_val = 1.0
    alpha_rad = (1.0 + gamma_val) * (2.0 * G_val * M_sun) / (c_val**2 * R_sun)
    alpha_arcsec = alpha_rad * (180.0 / np.pi) * 3600.0

    # Gravitational redshift (weak field): z ≈ GM/(Rc^2)
    z = (G_val * M_sun) / (R_sun * c_val**2)

    print("[OBSERVABLE] Light deflection at Sun limb (baseline PPN formula):")
    print(f"  alpha = {alpha_arcsec:.4f} arcsec")
    ref = 1.7505  # common benchmark (depends on inputs)
    rel_err = abs(alpha_arcsec - ref) / ref
    print(f"  reference (benchmark): {ref:.4f} arcsec")
    print(f"  relative deviation:    {rel_err*100.0:.4f}%")
    print()

    print("[OBSERVABLE] Gravitational redshift at Sun surface (weak field):")
    print(f"  z ≈ GM/(Rc^2) = {z:.3e}")
    print()

    print("=" * 60)
    print("CONCLUSION (strict):")
    print("• Bridge-layer math (River v(r) -> PG metric -> Schwarzschild form) is consistent.")
    print("• This does NOT yet prove that EDC derives v(r) or the mapping from first principles.")
    print("=" * 60)


if __name__ == "__main__":
    run()
