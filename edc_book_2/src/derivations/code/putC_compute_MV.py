#!/usr/bin/env python3
"""
PUT C EXECUTION: Compute M(q), V(q) from explicit 5D models
============================================================

This script implements two minimal 5D model variants and computes
the effective 1D action S_eff[q] = ∫dt (½ M(q) q̇² − V(q)).

Variants:
  1) Flat bulk toy model — sanity baseline
  2) Warped/RS-like metric — candidate for metastability

Epistemic Status:
  - Model definitions: [Def] or [I] (ansatz choices)
  - Derivation steps: [Dc] (conditional on model)
  - Numerical results: [Cal] (computed, not fundamental)
  - Comparison targets: [BL] (PDG) or [Dc] (book formula)

Date: 2026-01-27
Repository: edc_book_2/src/derivations/code/
"""

import numpy as np
import json
import csv
import os
from dataclasses import dataclass, asdict
from typing import Tuple, Optional, Dict, Any, List

# Try to import scipy for optimization; fall back to custom if unavailable
try:
    from scipy.optimize import minimize_scalar, minimize, brentq
    from scipy.integrate import quad
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False
    print("WARNING: scipy not available. Using simplified numerical methods.")

# Try to import matplotlib for plotting
try:
    import matplotlib
    matplotlib.use('Agg')  # Non-interactive backend
    import matplotlib.pyplot as plt
    PLOTTING_AVAILABLE = True
except ImportError:
    PLOTTING_AVAILABLE = False
    print("WARNING: matplotlib not available. Skipping plots.")


# =============================================================================
# PHYSICAL CONSTANTS [BL] — from PDG/CODATA
# =============================================================================

# Electron mass
M_E_MEV = 0.51099895  # MeV [BL] PDG 2022

# Fine structure constant
ALPHA = 1.0 / 137.035999084  # [BL] CODATA 2018

# Neutron-proton mass difference options
DELTA_M_NP_PDG = 1.29333236  # MeV [BL] PDG 2022 (Option B)
DELTA_M_NP_BOOK = (5.0/2.0 + 4.0*ALPHA) * M_E_MEV  # MeV [Dc] (Option A)

# Calibrated barrier height from WKB fit
V_B_CAL = 2.6  # MeV [Cal]

# Z3 conjecture predictions
V_B_CONJ_B = 2.0 * DELTA_M_NP_PDG  # MeV [Dc] Option B
V_B_CONJ_A = 2.0 * DELTA_M_NP_BOOK  # MeV [Dc] Option A


# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class ModelParameters:
    """Parameters for a 5D model variant."""
    name: str
    tau: float  # String tension [MeV/fm]
    L0: float   # In-brane leg projection [fm]
    k: float    # Warp parameter [1/fm] (0 for flat)
    sigma: float  # Brane tension [MeV/fm²]
    delta: float  # Brane thickness [fm]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ComputationResult:
    """Results from V(q), M(q) computation."""
    variant: str
    params: Dict[str, Any]

    # Potential landscape
    q_values: List[float]
    V_values: List[float]
    M_values: List[float]

    # Stationary points (if found)
    q_n: Optional[float]  # Neutron metastable minimum
    q_B: Optional[float]  # Barrier saddle
    q_0: Optional[float]  # Proton ground state

    # Derived quantities
    V_at_q0: Optional[float]
    V_at_qn: Optional[float]
    V_at_qB: Optional[float]
    V_B: Optional[float]  # V(q_B) - V(q_n)
    Delta_m_model: Optional[float]  # V(q_n) - V(q_0)

    # Curvatures at extrema
    V_pp_at_qn: Optional[float]  # V''(q_n)
    V_pp_at_qB: Optional[float]  # V''(q_B)

    # Comparison to targets
    V_B_vs_cal_pct: Optional[float]
    V_B_vs_conj_A_pct: Optional[float]
    V_B_vs_conj_B_pct: Optional[float]

    # Status
    has_metastability: bool
    notes: str


# =============================================================================
# VARIANT 1: FLAT BULK TOY MODEL
# =============================================================================

def variant1_leg_length(q: float, L0: float) -> float:
    """
    Leg length in flat bulk model.

    Geometry [Def]:
      - Junction node at ξ = q
      - Leg endpoint on brane at ξ = 0
      - In-brane projection of leg = L0

    Derivation [Dc]:
      L_leg(q) = √(L0² + q²)

    This is the standard 3D distance in flat (η + dξ²) metric.
    """
    return np.sqrt(L0**2 + q**2)


def variant1_V(q: float, params: ModelParameters) -> float:
    """
    Potential energy for Variant 1 (flat bulk).

    V(q) = 3 × τ × L_leg(q)  [Dc]

    (Three identical legs by Z₃ symmetry)
    """
    L_leg = variant1_leg_length(q, params.L0)
    return 3.0 * params.tau * L_leg


def variant1_dV(q: float, params: ModelParameters, eps: float = 1e-8) -> float:
    """First derivative V'(q) by central difference."""
    return (variant1_V(q + eps, params) - variant1_V(q - eps, params)) / (2 * eps)


def variant1_d2V(q: float, params: ModelParameters, eps: float = 1e-6) -> float:
    """Second derivative V''(q) by central difference."""
    return (variant1_V(q + eps, params) - 2*variant1_V(q, params) + variant1_V(q - eps, params)) / eps**2


def variant1_M(q: float, params: ModelParameters) -> float:
    """
    Effective mass M(q) for Variant 1.

    Derivation [Dc]:
      Kinetic term comes from time derivatives of leg embedding.
      For leg i with node at ξ = q(t):
        T_leg,i = (1/2) × (∂L_leg/∂q)² × τ × q̇²

      ∂L_leg/∂q = q / √(L0² + q²)

      M(q) = 3 × τ × (q / L_leg(q))²

    Note: This is a simplified model; full Nambu-Goto has more complex
    worldsheet kinetic terms. Tagged as [Dc/P].
    """
    L_leg = variant1_leg_length(q, params.L0)
    if L_leg < 1e-12:
        return 0.0
    return 3.0 * params.tau * (q / L_leg)**2


def compute_variant1(params: ModelParameters, q_max: float = 2.0, n_points: int = 200) -> ComputationResult:
    """
    Compute V(q), M(q) for Variant 1 (flat bulk toy model).

    Expected outcome [P]: No metastable minimum — V(q) monotonically
    increases with q (pure Nambu-Goto has no built-in barrier).
    """
    q_values = np.linspace(0, q_max, n_points)
    V_values = [variant1_V(q, params) for q in q_values]
    M_values = [variant1_M(q, params) for q in q_values]

    # Check for stationary points
    # V'(q) = 3τ × q / √(L0² + q²)
    # This is always > 0 for q > 0, so no interior minimum.

    q_0 = 0.0  # Global minimum at q=0 (proton)
    V_at_q0 = variant1_V(q_0, params)

    # No metastable minimum expected
    has_metastability = False
    q_n = None
    q_B = None
    V_at_qn = None
    V_at_qB = None
    V_B = None
    Delta_m_model = None
    V_pp_at_qn = None
    V_pp_at_qB = None

    notes = (
        "Variant 1 (flat bulk): V(q) = 3τ√(L0²+q²) is monotonically increasing. "
        "No metastable minimum exists. This confirms that pure Nambu-Goto "
        "in flat space requires additional physics (warping, brane tension, "
        "or node energy) to produce metastability."
    )

    return ComputationResult(
        variant="flat_bulk_toy",
        params=params.to_dict(),
        q_values=list(q_values),
        V_values=V_values,
        M_values=M_values,
        q_n=q_n,
        q_B=q_B,
        q_0=q_0,
        V_at_q0=V_at_q0,
        V_at_qn=V_at_qn,
        V_at_qB=V_at_qB,
        V_B=V_B,
        Delta_m_model=Delta_m_model,
        V_pp_at_qn=V_pp_at_qn,
        V_pp_at_qB=V_pp_at_qB,
        V_B_vs_cal_pct=None,
        V_B_vs_conj_A_pct=None,
        V_B_vs_conj_B_pct=None,
        has_metastability=has_metastability,
        notes=notes
    )


# =============================================================================
# VARIANT 2: WARPED/RS-LIKE METRIC
# =============================================================================

def variant2_warp_factor(xi: float, k: float) -> float:
    """
    Warp factor e^{-k|ξ|} for RS-like metric.

    Metric [Def/I]:
      ds² = e^{-2k|ξ|} η_{μν} dx^μ dx^ν + dξ²

    Convention: k > 0 gives exponential suppression into bulk.
    """
    return np.exp(-k * np.abs(xi))


def variant2_leg_energy_integrand(xi: float, dxi_dl: float, k: float) -> float:
    """
    Integrand for leg energy in warped metric.

    Effective length element [Dc]:
      dℓ_eff² = e^{-2kξ} dℓ_3² + dξ²

    For leg parametrized by in-brane arc length ℓ:
      E_leg = τ ∫₀^{L0} dℓ √(e^{-2kξ(ℓ)} + (dξ/dℓ)²)
    """
    warp = variant2_warp_factor(xi, k)
    return np.sqrt(warp**2 + dxi_dl**2)


def variant2_leg_energy_straight(q: float, L0: float, k: float, tau: float) -> float:
    """
    Leg energy assuming STRAIGHT embedding ξ(ℓ) = q × (1 - ℓ/L0).

    This is NOT the variational minimum but provides an upper bound [Dc].

    For straight embedding:
      dξ/dℓ = -q/L0 (constant)
      ξ(ℓ) = q(1 - ℓ/L0)

    E_leg = τ ∫₀^{L0} dℓ √(e^{-2kξ(ℓ)} + (q/L0)²)
    """
    if not SCIPY_AVAILABLE:
        # Simple trapezoidal integration
        n = 100
        dl = L0 / n
        E = 0.0
        for i in range(n):
            l = (i + 0.5) * dl
            xi = q * (1.0 - l / L0)
            warp = variant2_warp_factor(xi, k)
            dxi_dl = -q / L0
            E += np.sqrt(warp**2 + dxi_dl**2) * dl
        return tau * E

    def integrand(l):
        xi = q * (1.0 - l / L0)
        warp = variant2_warp_factor(xi, k)
        dxi_dl = -q / L0
        return np.sqrt(warp**2 + dxi_dl**2)

    result, _ = quad(integrand, 0, L0, limit=100)
    return tau * result


def variant2_leg_energy_variational(q: float, L0: float, k: float, tau: float,
                                     n_segments: int = 20) -> float:
    """
    Leg energy with variational minimization over embedding ξ(ℓ).

    Method [Dc]:
      Discretize leg into n_segments, optimize intermediate ξ values
      to minimize total energy.

      Boundary conditions:
        ξ(0) = q  (at junction node)
        ξ(L0) = 0 (at brane endpoint)

    This gives the true geodesic in the warped metric.
    """
    if not SCIPY_AVAILABLE:
        # Fall back to straight embedding
        return variant2_leg_energy_straight(q, L0, k, tau)

    if q < 1e-10:
        # At q=0, leg is entirely on brane
        return tau * L0

    dl = L0 / n_segments

    def energy_functional(xi_interior):
        """Total energy for given interior ξ values."""
        # Build full ξ array: [q, xi_interior..., 0]
        xi_full = np.concatenate([[q], xi_interior, [0.0]])

        E = 0.0
        for i in range(n_segments):
            xi_i = xi_full[i]
            xi_ip1 = xi_full[i + 1]
            xi_mid = 0.5 * (xi_i + xi_ip1)
            dxi = xi_ip1 - xi_i

            warp = variant2_warp_factor(xi_mid, k)
            E += np.sqrt(warp**2 + (dxi / dl)**2) * dl

        return tau * E

    # Initial guess: linear interpolation
    xi_init = np.linspace(q, 0, n_segments + 1)[1:-1]

    # Bounds: ξ should be between 0 and q (monotonic descent)
    bounds = [(0, q) for _ in range(n_segments - 1)]

    result = minimize(energy_functional, xi_init, bounds=bounds, method='L-BFGS-B')

    return result.fun


def variant2_brane_contribution(q: float, params: ModelParameters) -> float:
    """
    Brane contribution to potential from membrane tension.

    Model [P/Dc]:
      When junction node is displaced by q, it creates a "dimple" in the
      brane. The energy cost is proportional to the area change.

      Minimal surface assumption (axisymmetric dimple):
        ΔA(q) ≈ π (q² / δ)  for small q/δ

      where δ is the characteristic brane thickness.

      V_brane(q) = σ × ΔA(q) = σ π q² / δ

    This is a [P] term — the geometric form is assumed, not derived.
    """
    if params.delta < 1e-12:
        return 0.0
    return params.sigma * np.pi * q**2 / params.delta


def variant2_V(q: float, params: ModelParameters, use_variational: bool = True) -> float:
    """
    Total potential energy for Variant 2 (warped bulk).

    V(q) = 3 × E_leg(q) + V_brane(q)  [Dc]

    Components:
      - E_leg: Nambu-Goto in warped metric (variational or straight)
      - V_brane: Membrane tension contribution [P]
      - V_node: Set to 0 in this minimal model [P]
    """
    if use_variational:
        E_leg = variant2_leg_energy_variational(q, params.L0, params.k, params.tau)
    else:
        E_leg = variant2_leg_energy_straight(q, params.L0, params.k, params.tau)

    V_brane = variant2_brane_contribution(q, params)
    V_node = 0.0  # [P] — no explicit node energy in minimal model

    return 3.0 * E_leg + V_brane + V_node


def variant2_dV(q: float, params: ModelParameters, eps: float = 1e-6,
                use_variational: bool = True) -> float:
    """First derivative V'(q) by central difference."""
    if q < eps:
        return (variant2_V(eps, params, use_variational) -
                variant2_V(0, params, use_variational)) / eps
    return (variant2_V(q + eps, params, use_variational) -
            variant2_V(q - eps, params, use_variational)) / (2 * eps)


def variant2_d2V(q: float, params: ModelParameters, eps: float = 1e-5,
                 use_variational: bool = True) -> float:
    """Second derivative V''(q) by central difference."""
    return (variant2_V(q + eps, params, use_variational) -
            2*variant2_V(q, params, use_variational) +
            variant2_V(q - eps, params, use_variational)) / eps**2


def variant2_M(q: float, params: ModelParameters) -> float:
    """
    Effective mass M(q) for Variant 2.

    Simplified estimate [Dc/P]:
      M(q) ≈ 3τ × (average warp factor)² × (q/L_eff)²

    For more rigorous treatment, would need full worldsheet kinetic analysis.
    This is tagged as [Dc/P] — form is derived but coefficient approximate.
    """
    # Use average warp factor along leg
    avg_warp = 0.5 * (1.0 + variant2_warp_factor(q, params.k))
    L_eff = np.sqrt(params.L0**2 + q**2)

    if L_eff < 1e-12:
        return 0.0

    return 3.0 * params.tau * avg_warp**2 * (q / L_eff)**2


def find_extrema_variant2(params: ModelParameters, q_max: float = 2.0,
                          use_variational: bool = True) -> Tuple[Optional[float], Optional[float]]:
    """
    Find stationary points of V(q) for Variant 2.

    Returns (q_n, q_B) where:
      q_n = metastable minimum (neutron), if exists
      q_B = barrier saddle point, if exists

    Method: Scan V'(q) for sign changes, then refine with Brent's method.
    """
    if not SCIPY_AVAILABLE:
        # Simple scan for extrema
        n = 100
        dq = q_max / n

        q_n = None
        q_B = None

        # Look for sign changes in V'(q)
        prev_dV = variant2_dV(dq, params, use_variational=use_variational)
        for i in range(2, n):
            q = i * dq
            curr_dV = variant2_dV(q, params, use_variational=use_variational)

            if prev_dV > 0 and curr_dV < 0:
                # Local maximum (barrier)
                q_B = q - 0.5 * dq
            elif prev_dV < 0 and curr_dV > 0:
                # Local minimum (metastable)
                q_n = q - 0.5 * dq

            prev_dV = curr_dV

        return q_n, q_B

    # Scipy-based root finding
    def dV_func(q):
        if q < 1e-10:
            q = 1e-10
        return variant2_dV(q, params, use_variational=use_variational)

    # Scan for sign changes
    n = 50
    q_grid = np.linspace(0.01, q_max, n)
    dV_grid = [dV_func(q) for q in q_grid]

    q_n = None
    q_B = None

    for i in range(len(q_grid) - 1):
        if dV_grid[i] * dV_grid[i+1] < 0:
            # Sign change detected
            try:
                q_root = brentq(dV_func, q_grid[i], q_grid[i+1])
                d2V = variant2_d2V(q_root, params, use_variational=use_variational)

                if d2V > 0:
                    # Local minimum
                    if q_n is None or q_root > q_n:
                        q_n = q_root
                else:
                    # Local maximum (barrier)
                    if q_B is None or q_root < q_B:
                        q_B = q_root
            except:
                pass

    return q_n, q_B


def compute_variant2(params: ModelParameters, q_max: float = 2.0, n_points: int = 200,
                     use_variational: bool = True) -> ComputationResult:
    """
    Compute V(q), M(q) for Variant 2 (warped/RS-like metric).

    Expected outcome [P]: Metastability may emerge from competition between:
      - Leg stretching cost (increases with q)
      - Warp factor suppression (decreases effective tension at large ξ)
      - Brane tension contribution (quadratic in q)
    """
    q_values = np.linspace(0, q_max, n_points)
    V_values = [variant2_V(q, params, use_variational) for q in q_values]
    M_values = [variant2_M(q, params) for q in q_values]

    # Ground state at q=0
    q_0 = 0.0
    V_at_q0 = variant2_V(q_0, params, use_variational)

    # Find extrema
    q_n, q_B = find_extrema_variant2(params, q_max, use_variational)

    has_metastability = (q_n is not None and q_B is not None and q_B < q_n)

    # Compute derived quantities
    V_at_qn = None
    V_at_qB = None
    V_B = None
    Delta_m_model = None
    V_pp_at_qn = None
    V_pp_at_qB = None
    V_B_vs_cal_pct = None
    V_B_vs_conj_A_pct = None
    V_B_vs_conj_B_pct = None

    if q_n is not None:
        V_at_qn = variant2_V(q_n, params, use_variational)
        V_pp_at_qn = variant2_d2V(q_n, params, use_variational=use_variational)
        Delta_m_model = V_at_qn - V_at_q0

    if q_B is not None:
        V_at_qB = variant2_V(q_B, params, use_variational)
        V_pp_at_qB = variant2_d2V(q_B, params, use_variational=use_variational)

    if has_metastability:
        V_B = V_at_qB - V_at_qn

        if V_B > 0:
            V_B_vs_cal_pct = (V_B - V_B_CAL) / V_B_CAL * 100
            V_B_vs_conj_A_pct = (V_B - V_B_CONJ_A) / V_B_CONJ_A * 100
            V_B_vs_conj_B_pct = (V_B - V_B_CONJ_B) / V_B_CONJ_B * 100

    # Generate notes
    if has_metastability:
        notes = (
            f"Variant 2 (warped bulk): Metastability FOUND. "
            f"q_n = {q_n:.4f} fm, q_B = {q_B:.4f} fm, V_B = {V_B:.4f} MeV. "
            f"The warping + brane tension creates a barrier."
        )
    else:
        if q_n is None and q_B is None:
            notes = (
                "Variant 2 (warped bulk): No metastability with these parameters. "
                "V(q) is monotonic. Try: increase k (stronger warping), "
                "increase σ (brane tension), or decrease τ (string tension)."
            )
        elif q_n is not None and q_B is None:
            notes = (
                f"Variant 2 (warped bulk): Found minimum at q_n = {q_n:.4f} fm "
                f"but no barrier. The minimum may be the global minimum or "
                f"barrier is outside scan range."
            )
        else:
            notes = (
                f"Variant 2 (warped bulk): Unusual landscape. "
                f"q_n = {q_n}, q_B = {q_B}. Check parameter regime."
            )

    return ComputationResult(
        variant="warped_RS_like",
        params=params.to_dict(),
        q_values=list(q_values),
        V_values=V_values,
        M_values=M_values,
        q_n=q_n,
        q_B=q_B,
        q_0=q_0,
        V_at_q0=V_at_q0,
        V_at_qn=V_at_qn,
        V_at_qB=V_at_qB,
        V_B=V_B,
        Delta_m_model=Delta_m_model,
        V_pp_at_qn=V_pp_at_qn,
        V_pp_at_qB=V_pp_at_qB,
        V_B_vs_cal_pct=V_B_vs_cal_pct,
        V_B_vs_conj_A_pct=V_B_vs_conj_A_pct,
        V_B_vs_conj_B_pct=V_B_vs_conj_B_pct,
        has_metastability=has_metastability,
        notes=notes
    )


# =============================================================================
# VARIANT 3: WARPED + PHENOMENOLOGICAL NODE ENERGY
# =============================================================================

def variant3_node_energy(q: float, V_node_0: float, q_star: float, width: float) -> float:
    """
    Phenomenological node energy that favors a specific bulk depth.

    Model [P]:
      The junction node has an energy that DECREASES as it moves into the
      bulk, reaching a minimum at some characteristic depth q_star.

      V_node(q) = -V_node_0 × exp(-(q - q_star)² / (2 × width²))

      Physical motivation:
        - Junction couples to bulk fields (e.g., Plenum energy density)
        - Coupling is stronger at certain depths due to resonance/matching
        - This creates an attractive "well" in the bulk

      Parameters:
        V_node_0: Depth of the well [MeV]
        q_star: Location of minimum [fm]
        width: Width of the well [fm]

    This is a [P] term — phenomenological, not derived from action.
    """
    return -V_node_0 * np.exp(-(q - q_star)**2 / (2 * width**2))


def variant3_V(q: float, params: ModelParameters, V_node_0: float, q_star: float,
               width: float, use_variational: bool = False) -> float:
    """
    Total potential for Variant 3 (warped + node energy).

    V(q) = 3 × E_leg(q) + V_brane(q) + V_node(q)  [Dc/P]

    The node energy provides the mechanism for metastability:
      - At small q: leg cost dominates → pushes back to q=0
      - At q ~ q_star: node well dominates → creates local minimum
      - Barrier between them from competition
    """
    # Leg energy (straight embedding for speed)
    E_leg = variant2_leg_energy_straight(q, params.L0, params.k, params.tau)

    # Brane tension
    V_brane = variant2_brane_contribution(q, params)

    # Node energy (phenomenological well)
    V_node = variant3_node_energy(q, V_node_0, q_star, width)

    return 3.0 * E_leg + V_brane + V_node


def variant3_dV(q: float, params: ModelParameters, V_node_0: float, q_star: float,
                width: float, eps: float = 1e-6) -> float:
    """First derivative V'(q) by central difference."""
    if q < eps:
        return (variant3_V(eps, params, V_node_0, q_star, width) -
                variant3_V(0, params, V_node_0, q_star, width)) / eps
    return (variant3_V(q + eps, params, V_node_0, q_star, width) -
            variant3_V(q - eps, params, V_node_0, q_star, width)) / (2 * eps)


def variant3_d2V(q: float, params: ModelParameters, V_node_0: float, q_star: float,
                 width: float, eps: float = 1e-5) -> float:
    """Second derivative V''(q)."""
    return (variant3_V(q + eps, params, V_node_0, q_star, width) -
            2*variant3_V(q, params, V_node_0, q_star, width) +
            variant3_V(q - eps, params, V_node_0, q_star, width)) / eps**2


def find_extrema_variant3(params: ModelParameters, V_node_0: float, q_star: float,
                          width: float, q_max: float = 3.0) -> Tuple[Optional[float], Optional[float]]:
    """Find stationary points for Variant 3."""
    if not SCIPY_AVAILABLE:
        n = 100
        dq = q_max / n
        q_n = None
        q_B = None

        prev_dV = variant3_dV(dq, params, V_node_0, q_star, width)
        for i in range(2, n):
            q = i * dq
            curr_dV = variant3_dV(q, params, V_node_0, q_star, width)

            if prev_dV > 0 and curr_dV < 0:
                q_B = q - 0.5 * dq
            elif prev_dV < 0 and curr_dV > 0:
                q_n = q - 0.5 * dq

            prev_dV = curr_dV

        return q_n, q_B

    def dV_func(q):
        if q < 1e-10:
            q = 1e-10
        return variant3_dV(q, params, V_node_0, q_star, width)

    n = 80
    q_grid = np.linspace(0.01, q_max, n)
    dV_grid = [dV_func(q) for q in q_grid]

    q_n = None
    q_B = None

    for i in range(len(q_grid) - 1):
        if dV_grid[i] * dV_grid[i+1] < 0:
            try:
                q_root = brentq(dV_func, q_grid[i], q_grid[i+1])
                d2V = variant3_d2V(q_root, params, V_node_0, q_star, width)

                if d2V > 0:
                    if q_n is None or q_root > q_n:
                        q_n = q_root
                else:
                    if q_B is None or (q_root < q_n if q_n else True):
                        q_B = q_root
            except:
                pass

    # Ensure q_B < q_n for proper metastability
    if q_n is not None and q_B is not None and q_B > q_n:
        q_n, q_B = None, None

    return q_n, q_B


def compute_variant3(params: ModelParameters, V_node_0: float, q_star: float,
                     width: float, q_max: float = 3.0, n_points: int = 200) -> ComputationResult:
    """
    Compute V(q), M(q) for Variant 3 (warped + phenomenological node energy).
    """
    q_values = np.linspace(0, q_max, n_points)
    V_values = [variant3_V(q, params, V_node_0, q_star, width) for q in q_values]
    M_values = [variant2_M(q, params) for q in q_values]  # Same M(q) as variant 2

    q_0 = 0.0
    V_at_q0 = variant3_V(q_0, params, V_node_0, q_star, width)

    q_n, q_B = find_extrema_variant3(params, V_node_0, q_star, width, q_max)

    has_metastability = (q_n is not None and q_B is not None and q_B < q_n)

    V_at_qn = None
    V_at_qB = None
    V_B = None
    Delta_m_model = None
    V_pp_at_qn = None
    V_pp_at_qB = None
    V_B_vs_cal_pct = None
    V_B_vs_conj_A_pct = None
    V_B_vs_conj_B_pct = None

    if q_n is not None:
        V_at_qn = variant3_V(q_n, params, V_node_0, q_star, width)
        V_pp_at_qn = variant3_d2V(q_n, params, V_node_0, q_star, width)
        Delta_m_model = V_at_qn - V_at_q0

    if q_B is not None:
        V_at_qB = variant3_V(q_B, params, V_node_0, q_star, width)
        V_pp_at_qB = variant3_d2V(q_B, params, V_node_0, q_star, width)

    if has_metastability:
        V_B = V_at_qB - V_at_qn

        if V_B is not None and V_B > 0:
            V_B_vs_cal_pct = (V_B - V_B_CAL) / V_B_CAL * 100
            V_B_vs_conj_A_pct = (V_B - V_B_CONJ_A) / V_B_CONJ_A * 100
            V_B_vs_conj_B_pct = (V_B - V_B_CONJ_B) / V_B_CONJ_B * 100

    # Update params dict with node energy parameters
    params_dict = params.to_dict()
    params_dict['V_node_0'] = V_node_0
    params_dict['q_star'] = q_star
    params_dict['width'] = width

    if has_metastability:
        notes = (
            f"Variant 3 (warped + node well): Metastability FOUND. "
            f"q_n = {q_n:.4f} fm, q_B = {q_B:.4f} fm, V_B = {V_B:.4f} MeV. "
            f"Node well at q* = {q_star} fm creates metastable configuration."
        )
    else:
        notes = (
            f"Variant 3 (warped + node well): No metastability with these parameters. "
            f"V_node_0 = {V_node_0}, q* = {q_star}, width = {width}."
        )

    return ComputationResult(
        variant="warped_plus_node_well",
        params=params_dict,
        q_values=list(q_values),
        V_values=V_values,
        M_values=M_values,
        q_n=q_n,
        q_B=q_B,
        q_0=q_0,
        V_at_q0=V_at_q0,
        V_at_qn=V_at_qn,
        V_at_qB=V_at_qB,
        V_B=V_B,
        Delta_m_model=Delta_m_model,
        V_pp_at_qn=V_pp_at_qn,
        V_pp_at_qB=V_pp_at_qB,
        V_B_vs_cal_pct=V_B_vs_cal_pct,
        V_B_vs_conj_A_pct=V_B_vs_conj_A_pct,
        V_B_vs_conj_B_pct=V_B_vs_conj_B_pct,
        has_metastability=has_metastability,
        notes=notes
    )


# =============================================================================
# PARAMETER SCAN
# =============================================================================

def scan_parameter_space() -> List[ComputationResult]:
    """
    Scan parameter space for Variant 2 to find metastability regions.

    Strategy [Dc]:
      Fix L0 (in-brane leg size) at nucleon scale ~ 1 fm.
      Scan over k (warp parameter), τ (string tension), σ (brane tension).

    Report which combinations yield metastability.
    """
    results = []

    # Base parameters [I] — order-of-magnitude estimates
    L0 = 1.0  # fm (nucleon scale)
    delta = 0.1  # fm (brane thickness)

    # Scan grids
    # τ: string tension. For QCD strings, τ ~ 1 GeV/fm ~ 1000 MeV/fm
    # For EDC, we use σ ~ 8.82 MeV/fm² from book; τ could be similar order or less
    tau_values = [1.0, 5.0, 10.0, 50.0, 100.0]  # MeV/fm

    # k: warp parameter. k ~ 1/fm gives O(1) warping over nucleon scale
    k_values = [0.5, 1.0, 2.0, 5.0, 10.0]  # 1/fm

    # σ: brane tension. Book value ~ 8.82 MeV/fm²
    sigma_values = [1.0, 5.0, 8.82, 20.0, 50.0]  # MeV/fm²

    print("\n" + "="*70)
    print("PARAMETER SCAN: Looking for metastability in Variant 2")
    print("="*70)

    metastable_count = 0

    for tau in tau_values:
        for k in k_values:
            for sigma in sigma_values:
                params = ModelParameters(
                    name=f"scan_tau{tau}_k{k}_sigma{sigma}",
                    tau=tau,
                    L0=L0,
                    k=k,
                    sigma=sigma,
                    delta=delta
                )

                # Quick computation (fewer points, straight embedding for speed)
                result = compute_variant2(params, q_max=2.0, n_points=50,
                                         use_variational=False)

                if result.has_metastability:
                    metastable_count += 1
                    print(f"  METASTABLE: τ={tau:.1f}, k={k:.1f}, σ={sigma:.2f} → "
                          f"V_B={result.V_B:.3f} MeV")
                    results.append(result)

    print(f"\nFound {metastable_count} metastable parameter sets out of "
          f"{len(tau_values)*len(k_values)*len(sigma_values)} scanned.")

    return results


# =============================================================================
# OUTPUT FUNCTIONS
# =============================================================================

def save_results_json(results: List[ComputationResult], filepath: str):
    """Save results to JSON file."""
    data = []
    for r in results:
        d = {
            'variant': r.variant,
            'params': r.params,
            'q_n': r.q_n,
            'q_B': r.q_B,
            'q_0': r.q_0,
            'V_at_q0': r.V_at_q0,
            'V_at_qn': r.V_at_qn,
            'V_at_qB': r.V_at_qB,
            'V_B': r.V_B,
            'Delta_m_model': r.Delta_m_model,
            'V_pp_at_qn': r.V_pp_at_qn,
            'V_pp_at_qB': r.V_pp_at_qB,
            'V_B_vs_cal_pct': r.V_B_vs_cal_pct,
            'V_B_vs_conj_A_pct': r.V_B_vs_conj_A_pct,
            'V_B_vs_conj_B_pct': r.V_B_vs_conj_B_pct,
            'has_metastability': r.has_metastability,
            'notes': r.notes
        }
        data.append(d)

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Results saved to {filepath}")


def save_results_csv(results: List[ComputationResult], filepath: str):
    """Save key results to CSV file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'variant', 'tau', 'L0', 'k', 'sigma', 'delta',
            'q_n', 'q_B', 'V_B', 'Delta_m_model',
            'V_B_vs_cal_pct', 'has_metastability'
        ])

        for r in results:
            writer.writerow([
                r.variant,
                r.params.get('tau', ''),
                r.params.get('L0', ''),
                r.params.get('k', ''),
                r.params.get('sigma', ''),
                r.params.get('delta', ''),
                f"{r.q_n:.6f}" if r.q_n else '',
                f"{r.q_B:.6f}" if r.q_B else '',
                f"{r.V_B:.6f}" if r.V_B else '',
                f"{r.Delta_m_model:.6f}" if r.Delta_m_model else '',
                f"{r.V_B_vs_cal_pct:.2f}" if r.V_B_vs_cal_pct else '',
                r.has_metastability
            ])

    print(f"Results saved to {filepath}")


def plot_potential(result: ComputationResult, filepath: str):
    """Generate V(q) plot."""
    if not PLOTTING_AVAILABLE:
        print(f"Plotting not available. Skipping {filepath}")
        return

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(result.q_values, result.V_values, 'b-', linewidth=2, label='V(q)')

    # Mark extrema
    if result.q_0 is not None:
        ax.axvline(result.q_0, color='g', linestyle='--', alpha=0.7, label=f'q₀ = {result.q_0:.3f} fm (proton)')

    if result.q_n is not None:
        ax.axvline(result.q_n, color='orange', linestyle='--', alpha=0.7, label=f'qₙ = {result.q_n:.3f} fm (neutron)')
        ax.plot(result.q_n, result.V_at_qn, 'o', color='orange', markersize=10)

    if result.q_B is not None:
        ax.axvline(result.q_B, color='r', linestyle='--', alpha=0.7, label=f'q_B = {result.q_B:.3f} fm (barrier)')
        ax.plot(result.q_B, result.V_at_qB, 's', color='r', markersize=10)

    ax.set_xlabel('q [fm]', fontsize=12)
    ax.set_ylabel('V(q) [MeV]', fontsize=12)
    ax.set_title(f'Effective Potential — {result.variant}', fontsize=14)
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3)

    # Add parameter info
    params_str = f"τ={result.params['tau']:.1f} MeV/fm, k={result.params['k']:.1f} 1/fm, σ={result.params['sigma']:.2f} MeV/fm²"
    ax.text(0.02, 0.98, params_str, transform=ax.transAxes, fontsize=9,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    if result.V_B is not None:
        vb_str = f"V_B = {result.V_B:.3f} MeV"
        ax.text(0.98, 0.98, vb_str, transform=ax.transAxes, fontsize=11,
                verticalalignment='top', horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Plot saved to {filepath}")


def plot_effective_mass(result: ComputationResult, filepath: str):
    """Generate M(q) plot."""
    if not PLOTTING_AVAILABLE:
        print(f"Plotting not available. Skipping {filepath}")
        return

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(result.q_values, result.M_values, 'b-', linewidth=2, label='M(q)')

    ax.set_xlabel('q [fm]', fontsize=12)
    ax.set_ylabel('M(q) [MeV/fm²]', fontsize=12)
    ax.set_title(f'Effective Mass — {result.variant}', fontsize=14)
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3)

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Plot saved to {filepath}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    print("="*70)
    print("PUT C EXECUTION: Computing M(q), V(q) from 5D Models")
    print("="*70)
    print()

    # --- Reference values ---
    print("REFERENCE VALUES:")
    print(f"  Δm_np (PDG) [BL]:  {DELTA_M_NP_PDG:.6f} MeV")
    print(f"  Δm_np (Book) [Dc]: {DELTA_M_NP_BOOK:.6f} MeV")
    print(f"  V_B_cal [Cal]:     {V_B_CAL:.3f} MeV")
    print(f"  V_B conj A [Dc]:   {V_B_CONJ_A:.4f} MeV (= 2 × Δm_np_Book)")
    print(f"  V_B conj B [Dc]:   {V_B_CONJ_B:.4f} MeV (= 2 × Δm_np_PDG)")
    print()

    all_results = []

    # --- VARIANT 1: Flat bulk toy model ---
    print("\n" + "="*70)
    print("VARIANT 1: Flat Bulk Toy Model")
    print("="*70)

    params_v1 = ModelParameters(
        name="flat_bulk_baseline",
        tau=10.0,  # MeV/fm [I] order of magnitude
        L0=1.0,    # fm [I] nucleon scale
        k=0.0,     # no warping
        sigma=8.82,  # MeV/fm² [Dc] book value (not used in V1)
        delta=0.1  # fm [P]
    )

    result_v1 = compute_variant1(params_v1)
    all_results.append(result_v1)

    print(f"\nResult: {result_v1.notes}")
    print(f"  q_0 = {result_v1.q_0:.4f} fm")
    print(f"  V(q_0) = {result_v1.V_at_q0:.4f} MeV")
    print(f"  Metastability: {result_v1.has_metastability}")

    # --- VARIANT 2: Warped/RS-like metric ---
    print("\n" + "="*70)
    print("VARIANT 2: Warped/RS-like Metric")
    print("="*70)

    # Baseline parameters (may need tuning)
    params_v2 = ModelParameters(
        name="warped_baseline",
        tau=5.0,    # MeV/fm [I] - lower than QCD to allow warping to dominate
        L0=1.0,     # fm [I]
        k=2.0,      # 1/fm [I] - moderate warping
        sigma=8.82, # MeV/fm² [Dc]
        delta=0.1   # fm [P]
    )

    print(f"\nBaseline parameters:")
    print(f"  τ = {params_v2.tau} MeV/fm")
    print(f"  L₀ = {params_v2.L0} fm")
    print(f"  k = {params_v2.k} 1/fm")
    print(f"  σ = {params_v2.sigma} MeV/fm²")
    print(f"  δ = {params_v2.delta} fm")

    result_v2 = compute_variant2(params_v2, use_variational=True)
    all_results.append(result_v2)

    print(f"\nResult: {result_v2.notes}")
    if result_v2.has_metastability:
        print(f"  q_n = {result_v2.q_n:.4f} fm")
        print(f"  q_B = {result_v2.q_B:.4f} fm")
        print(f"  V_B = {result_v2.V_B:.4f} MeV")
        print(f"  V_B vs cal: {result_v2.V_B_vs_cal_pct:.1f}%")
        print(f"  V_B vs conj A: {result_v2.V_B_vs_conj_A_pct:.1f}%")
        print(f"  V_B vs conj B: {result_v2.V_B_vs_conj_B_pct:.1f}%")

    # --- Parameter scan for Variant 2 ---
    scan_results = scan_parameter_space()
    all_results.extend(scan_results)

    # --- VARIANT 3: Warped + node well ---
    print("\n" + "="*70)
    print("VARIANT 3: Warped Metric + Phenomenological Node Well")
    print("="*70)

    # Physics interpretation [P]:
    # - Proton at q=0 is ground state
    # - Neutron at q=q_n > 0 is metastable (HIGHER energy than proton)
    # - Barrier at q_B between them
    #
    # The node well creates a "dip" in the monotonically rising leg potential,
    # creating a local minimum at q_n followed by barrier at q_B < q_n.
    #
    # Actually: for proper barrier structure, we need:
    #   V(0) < V(q_n) < V(q_B)  with q_B < q_n
    # This means the well creates a "second minimum" at q_n that is ABOVE
    # the ground state but below the intervening maximum.

    # Use lower string tension to make leg cost less dominant
    params_v3 = ModelParameters(
        name="variant3_base",
        tau=2.0,    # MeV/fm [I] - lower to allow well to dominate
        L0=1.0,     # fm [I]
        k=1.0,      # 1/fm [I] - moderate warping
        sigma=0.0,  # MeV/fm² - turn off brane contribution
        delta=0.1   # fm [P]
    )

    # Node well parameters [P]
    # The well should be deep enough and positioned to create metastability
    V_node_0 = 15.0   # MeV [P] - depth of well (must overcome leg cost slope)
    q_star = 1.2      # fm [P] - location of well minimum
    width = 0.4       # fm [P] - width of well

    print(f"\nVariant 3 parameters:")
    print(f"  τ = {params_v3.tau} MeV/fm (string tension)")
    print(f"  L₀ = {params_v3.L0} fm (leg projection)")
    print(f"  k = {params_v3.k} 1/fm (warp parameter)")
    print(f"  V_node_0 = {V_node_0} MeV (well depth)")
    print(f"  q* = {q_star} fm (well location)")
    print(f"  width = {width} fm (well width)")

    result_v3 = compute_variant3(params_v3, V_node_0, q_star, width)
    all_results.append(result_v3)

    print(f"\nResult: {result_v3.notes}")
    if result_v3.has_metastability:
        print(f"  q_n = {result_v3.q_n:.4f} fm")
        print(f"  q_B = {result_v3.q_B:.4f} fm")
        print(f"  V_B = {result_v3.V_B:.4f} MeV")
        print(f"  Δm_model = V(q_n) - V(0) = {result_v3.Delta_m_model:.4f} MeV")
        print(f"  V_B vs cal: {result_v3.V_B_vs_cal_pct:.1f}%")
        print(f"  V_B vs conj B: {result_v3.V_B_vs_conj_B_pct:.1f}%")

    # --- Scan Variant 3 to match V_B targets ---
    print("\n" + "="*70)
    print("VARIANT 3 TARGETED SCAN: Find parameters matching V_B ≈ 2.6 MeV")
    print("="*70)

    v3_results = []
    best_v3 = None
    best_error = float('inf')

    # Scan over V_node_0, q_star, width to find configurations matching V_B_cal
    # Use lower τ to allow well to dominate
    for tau_scan in [1.0, 2.0, 3.0]:
        for V_n0 in [10.0, 15.0, 20.0, 25.0, 30.0]:
            for q_s in [0.8, 1.0, 1.2, 1.5, 2.0]:
                for w in [0.3, 0.4, 0.5, 0.6]:
                    params_scan = ModelParameters(
                        name=f"v3_scan",
                        tau=tau_scan,
                        L0=1.0,
                        k=1.0,
                        sigma=0.0,
                        delta=0.1
                    )
                    r = compute_variant3(params_scan, V_n0, q_s, w, q_max=4.0, n_points=100)
                    if r.has_metastability and r.V_B is not None and r.V_B > 0:
                        v3_results.append(r)
                        error = abs(r.V_B - V_B_CAL)
                        if error < best_error:
                            best_error = error
                            best_v3 = r

    print(f"\nVariant 3 scan: {len(v3_results)} metastable configurations found")

    if best_v3 is not None:
        print(f"\nBest match to V_B_cal = 2.6 MeV:")
        print(f"  V_node_0 = {best_v3.params['V_node_0']:.1f} MeV")
        print(f"  q* = {best_v3.params['q_star']:.2f} fm")
        print(f"  width = {best_v3.params['width']:.2f} fm")
        print(f"  q_n = {best_v3.q_n:.4f} fm")
        print(f"  q_B = {best_v3.q_B:.4f} fm")
        print(f"  V_B = {best_v3.V_B:.4f} MeV")
        print(f"  Error vs V_B_cal: {best_v3.V_B_vs_cal_pct:.1f}%")

        # Also find best match to 2×Δm_np conjecture
        best_conj = min(v3_results, key=lambda r: abs(r.V_B - V_B_CONJ_B) if r.V_B else float('inf'))
        print(f"\nBest match to V_B = 2×Δm_np = {V_B_CONJ_B:.4f} MeV:")
        print(f"  V_node_0 = {best_conj.params['V_node_0']:.1f} MeV")
        print(f"  q* = {best_conj.params['q_star']:.2f} fm")
        print(f"  width = {best_conj.params['width']:.2f} fm")
        print(f"  V_B = {best_conj.V_B:.4f} MeV")
        print(f"  Error vs 2×Δm_np: {best_conj.V_B_vs_conj_B_pct:.1f}%")

        all_results.extend(v3_results)

        # Plot best V3 result
        plot_potential(best_v3, "derivations/figures/putC_Vq_variant3_best.png")

    # --- Find best match to V_B_cal ---
    print("\n" + "="*70)
    print("OVERALL BEST MATCH TO V_B_cal = 2.6 MeV")
    print("="*70)

    metastable_results = [r for r in all_results if r.has_metastability and r.V_B is not None]

    if metastable_results:
        best = min(metastable_results, key=lambda r: abs(r.V_B - V_B_CAL))
        print(f"\nBest match:")
        print(f"  Variant: {best.variant}")
        print(f"  Parameters: τ={best.params['tau']}, k={best.params['k']}, σ={best.params['sigma']}")
        print(f"  V_B = {best.V_B:.4f} MeV")
        print(f"  Error vs V_B_cal: {best.V_B_vs_cal_pct:.1f}%")

        # Generate plots for best match
        plot_potential(best, "derivations/figures/putC_Vq_best_match.png")
        plot_effective_mass(best, "derivations/figures/putC_Mq_best_match.png")
    else:
        print("\nNo metastable configurations found in scan.")
        print("Consider: larger σ, larger k, or smaller τ.")

    # --- Save outputs ---
    print("\n" + "="*70)
    print("SAVING OUTPUTS")
    print("="*70)

    save_results_json(all_results, "derivations/artifacts/putC_results.json")
    save_results_csv(all_results, "derivations/artifacts/putC_results.csv")

    # Plot baseline results
    plot_potential(result_v1, "derivations/figures/putC_Vq_variant1.png")
    plot_potential(result_v2, "derivations/figures/putC_Vq_variant2.png")
    plot_effective_mass(result_v2, "derivations/figures/putC_Mq_variant2.png")

    # --- Summary ---
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)

    n_v3_meta = len([r for r in all_results if r.variant == "warped_plus_node_well" and r.has_metastability])

    print(f"""
Variant 1 (Flat bulk):
  - No metastability (as expected)
  - V(q) = 3τ√(L₀²+q²) monotonically increasing
  - Status: [Dc] — confirms need for additional physics

Variant 2 (Warped/RS-like):
  - Metastability: {'FOUND' if result_v2.has_metastability else 'NOT FOUND with baseline params'}
  - Competition: leg stretching vs warp suppression vs brane tension
  - Status: [Dc/P] — model-dependent, requires tuning

Variant 3 (Warped + node well):
  - Metastability: {'FOUND' if result_v3.has_metastability else 'NOT FOUND'}
  - Phenomenological node well V_node(q) creates metastable minimum
  - Can match V_B ≈ 2.6 MeV with appropriate parameters
  - Status: [P/Cal] — node well is phenomenological, not derived

Parameter scans:
  - Variant 2: 125 combinations → {len([r for r in all_results if r.variant == "warped_RS_like" and r.has_metastability])} metastable
  - Variant 3: 100 combinations → {n_v3_meta} metastable

Key findings:
  1. Pure Nambu-Goto in flat space: NO barrier [Dc]
  2. Warped metric alone: insufficient for metastability
  3. Phenomenological node well: CAN produce V_B ≈ 2.6 MeV [Cal]
  4. V_B = 2×Δm_np NOT emerged naturally — requires fitting

CRITICAL CONCLUSION:
  The current 5D models do NOT uniquely derive V_B = 2×Δm_np.
  Metastability requires additional physics (node energy well).
  The [Dc] status of "V_B = 2×Δm_np" from Z3 analysis remains a
  conjecture awaiting first-principles derivation.

OPEN items for full [Der] closure:
  1) Derive node well V_node(q) from 5D action (bulk field coupling?)
  2) Fix parameters (V_node_0, q*, width) from independent physics
  3) Show V_B = 2Δm_np emerges without fitting
  4) Connect geometric scales (q_n, q_B) to Δm_np
  5) Derive M(q) from full worldsheet kinetics
""")

    print("="*70)
    print("PUT C EXECUTION COMPLETE")
    print("="*70)


if __name__ == "__main__":
    main()
