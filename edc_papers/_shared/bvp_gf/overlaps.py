#!/usr/bin/env python3
"""
overlaps.py — Overlap Integral Computation for G_F Non-Circular Chain

Issue: OPR-21 — Thick-brane BVP solution for G_F non-circular chain
Reference: edc_papers/_shared/derivations/gf_noncircular_chain_framework.tex

This module computes:
- I_4 = ∫ dχ w_L² w_R² w_φ² (four-point overlap)
- I_g = ∫ dχ w_φ² (gauge overlap for g_eff)
- ε = ∫ dχ w_L w_R (chirality suppression factor)
- X_EDC from the non-circular formula

Status: [OPEN] — Pipeline implemented, physics values provisional
"""

import numpy as np
from dataclasses import dataclass
from typing import Dict, Optional
from bvp_core import BVPSolution, ModeProfile


# =============================================================================
# Physical Constants (natural units)
# =============================================================================

G_F_MEASURED = 1.1663787e-5  # GeV^{-2}
M_E = 0.51099895e-3  # GeV
ALPHA = 1 / 137.036
SIN2_THETA_W = 0.25  # [Der] from Z₆

# Target dimensionless combination
X_TARGET = G_F_MEASURED * M_E**2  # ≈ 3.04 × 10^{-12}

# SM convention factor
C_SM = 1.0 / (4.0 * np.sqrt(2))  # ≈ 0.177


# =============================================================================
# Data Classes
# =============================================================================

@dataclass
class OverlapResults:
    """Container for all overlap integral results."""
    # Primary overlaps
    I_4: float              # ∫ dχ w_L² w_R² w_φ²
    I_g: float              # ∫ dχ w_φ² (gauge overlap)
    epsilon: float          # ∫ dχ w_L w_R (chirality suppression)

    # Derived quantities
    g5_squared: float       # 5D gauge coupling squared [Dc]
    g_eff_squared: float    # Effective 4D coupling squared
    M_eff: float            # Effective mediator mass (GeV)
    M_eff_squared: float    # M_eff² (GeV²)

    # Target comparison
    X_EDC: float            # Computed dimensionless G_F × m_e²
    X_target: float         # Target value
    X_ratio: float          # X_EDC / X_target

    # Diagnostics
    lambda_0: float         # KK eigenvalue (from w_phi)
    delta: float            # Brane thickness parameter


@dataclass
class GateEvaluation:
    """Container for falsification gate evaluation."""
    # Gate 1: Overlap window
    gate1_I4_pass: bool
    gate1_I4_ratio: float
    gate1_message: str

    # Gate 2: Mass scaling
    gate2_mass_pass: bool
    gate2_mass_ratio: float
    gate2_message: str

    # Gate 3: Coupling compatibility
    gate3_coupling_pass: bool
    gate3_coupling_ratio: float
    gate3_message: str

    # Overall
    all_gates_pass: bool
    overall_verdict: str
    fail_codes: list


# =============================================================================
# Overlap Integral Computation
# =============================================================================

def compute_I4(w_L: ModeProfile, w_R: ModeProfile, w_phi: ModeProfile) -> float:
    """
    Compute the four-point overlap integral.

    I_4 = ∫ dχ w_L(χ)² w_R(χ)² w_φ(χ)²

    This integral has dimension [length]^{-1} = [energy].

    Reference: gf_noncircular_chain_framework.tex, eq. (eq:I4_def)
    """
    # Interpolate all modes to common grid (use w_phi's grid as reference)
    chi = w_phi.chi

    # If grids differ, interpolate
    if not np.allclose(w_L.chi, chi):
        w_L_interp = np.interp(chi, w_L.chi, w_L.profile)
    else:
        w_L_interp = w_L.profile

    if not np.allclose(w_R.chi, chi):
        w_R_interp = np.interp(chi, w_R.chi, w_R.profile)
    else:
        w_R_interp = w_R.profile

    w_phi_arr = w_phi.profile

    # Compute integrand
    integrand = w_L_interp**2 * w_R_interp**2 * w_phi_arr**2

    # Integrate using trapezoidal rule
    I_4 = np.trapezoid(integrand, chi)

    return I_4


def compute_I_g(w_phi: ModeProfile) -> float:
    """
    Compute the gauge overlap integral.

    I_g = ∫ dχ w_φ(χ)²

    For properly normalized modes, this should be 1.
    """
    return np.trapezoid(w_phi.profile**2, w_phi.chi)


def compute_epsilon(w_L: ModeProfile, w_R: ModeProfile) -> float:
    """
    Compute the chirality suppression factor.

    ε = ∫ dχ w_L(χ) w_R(χ)

    This measures the overlap between left and right modes.
    For well-separated modes, ε << 1.
    """
    chi = w_L.chi

    if not np.allclose(w_R.chi, chi):
        w_R_interp = np.interp(chi, w_R.chi, w_R.profile)
    else:
        w_R_interp = w_R.profile

    integrand = w_L.profile * w_R_interp
    epsilon = np.trapezoid(integrand, chi)

    return epsilon


# =============================================================================
# Derived Quantities
# =============================================================================

def compute_g5_squared(delta: float, alpha: float = ALPHA,
                       sin2_theta_W: float = SIN2_THETA_W) -> float:
    """
    Estimate 5D gauge coupling squared from natural scaling.

    [g_5²] = [length] = [energy]^{-1}

    Natural scale: g_5² ~ δ × (4πα / sin²θ_W)

    Reference: gf_noncircular_chain_framework.tex, Section 2A
    """
    return delta * 4 * np.pi * alpha / sin2_theta_W


def compute_M_eff(lambda_0: float, delta: float) -> float:
    """
    Compute effective mediator mass from KK eigenvalue.

    M_eff² = λ_0 / δ²  →  M_eff = √λ_0 / δ

    Reference: gf_noncircular_chain_framework.tex, eq. (111)
    """
    if lambda_0 < 0:
        # Bound state: |λ_0| is the binding energy
        return np.sqrt(np.abs(lambda_0)) / delta
    else:
        return np.sqrt(lambda_0) / delta


def compute_X_EDC(g5_squared: float, I_4: float, M_eff: float,
                  m_e: float = M_E) -> float:
    """
    Compute the dimensionless G_F prediction.

    X_EDC = C × (g_5² × I_4 × m_e²) / M_eff²

    where C = 1/(4√2) is the SM convention factor.

    Reference: gf_noncircular_chain_framework.tex, eq. (eq:X_EDC)
    """
    if M_eff == 0:
        return np.inf

    return C_SM * g5_squared * I_4 * m_e**2 / M_eff**2


# =============================================================================
# Main Overlap Computation
# =============================================================================

def compute_all_overlaps(solution: BVPSolution, config: Dict) -> OverlapResults:
    """
    Compute all overlap integrals and derived quantities from BVP solution.

    Args:
        solution: BVP solution containing mode profiles
        config: Configuration dictionary

    Returns:
        OverlapResults with all computed quantities
    """
    phys = config['physical']
    delta = phys['delta_GeV_inv']
    m_e = phys['m_e_GeV']
    alpha = phys['alpha']
    sin2_theta_W = phys['sin2_theta_W']
    X_target = phys['X_target']

    # Compute primary overlaps
    if solution.w_L is None or solution.w_R is None or solution.w_phi is None:
        raise ValueError("Missing mode profiles for overlap computation")

    I_4 = compute_I4(solution.w_L, solution.w_R, solution.w_phi)
    I_g = compute_I_g(solution.w_phi)
    epsilon = compute_epsilon(solution.w_L, solution.w_R)

    # Compute derived quantities
    g5_squared = compute_g5_squared(delta, alpha, sin2_theta_W)
    g_eff_squared = g5_squared * I_g

    # KK eigenvalue from mediator mode
    lambda_0 = solution.w_phi.eigenvalue
    M_eff = compute_M_eff(lambda_0, delta)
    M_eff_squared = M_eff**2

    # Target comparison
    X_EDC = compute_X_EDC(g5_squared, I_4, M_eff, m_e)
    X_ratio = X_EDC / X_target if X_target != 0 else np.inf

    return OverlapResults(
        I_4=I_4,
        I_g=I_g,
        epsilon=epsilon,
        g5_squared=g5_squared,
        g_eff_squared=g_eff_squared,
        M_eff=M_eff,
        M_eff_squared=M_eff_squared,
        X_EDC=X_EDC,
        X_target=X_target,
        X_ratio=X_ratio,
        lambda_0=lambda_0,
        delta=delta
    )


# =============================================================================
# Gate Evaluation
# =============================================================================

def evaluate_gates(overlaps: OverlapResults, config: Dict) -> GateEvaluation:
    """
    Evaluate falsification gates from G_F framework.

    Gates:
    1. I_4 within [0.1, 10] × I_4_required
    2. M_eff within [0.1, 10] × (1/δ)
    3. g_eff² compatible with α and sin²θ_W

    Reference: docs/GF_NONCIRCULAR_FRAMEWORK_NOTE.md, Section 4
    """
    gates_cfg = config['gates']
    phys = config['physical']

    delta = phys['delta_GeV_inv']
    alpha = phys['alpha']
    sin2_theta_W = phys['sin2_theta_W']

    I4_factor = gates_cfg['I4_window_factor']
    M_factor = gates_cfg['M_eff_window_factor']
    X_tol = gates_cfg['X_EDC_tolerance']

    fail_codes = []

    # -------------------------------------------------------------------------
    # Gate 1: Overlap window
    # -------------------------------------------------------------------------
    # Required I_4 is whatever would give X_EDC = X_target
    # X_target = C × g_5² × I_4_req × m_e² / M_eff²
    # I_4_req = X_target × M_eff² / (C × g_5² × m_e²)
    if overlaps.M_eff > 0 and overlaps.g5_squared > 0:
        I_4_required = (overlaps.X_target * overlaps.M_eff**2 /
                        (C_SM * overlaps.g5_squared * M_E**2))
    else:
        I_4_required = 1e-3  # Fallback

    I4_ratio = overlaps.I_4 / I_4_required if I_4_required != 0 else np.inf

    gate1_pass = (1.0 / I4_factor) < I4_ratio < I4_factor

    if I4_ratio < 1.0 / I4_factor:
        gate1_msg = f"FAIL: I_4 too small (ratio={I4_ratio:.2e})"
        fail_codes.append("FAIL_I4_TOO_SMALL")
    elif I4_ratio > I4_factor:
        gate1_msg = f"FAIL: I_4 too large (ratio={I4_ratio:.2e})"
        fail_codes.append("FAIL_I4_TOO_LARGE")
    else:
        gate1_msg = f"PASS: I_4 within window (ratio={I4_ratio:.2f})"

    # -------------------------------------------------------------------------
    # Gate 2: Mass scaling
    # -------------------------------------------------------------------------
    M_expected = 1.0 / delta
    M_ratio = overlaps.M_eff / M_expected

    gate2_pass = (1.0 / M_factor) < M_ratio < M_factor

    if M_ratio < 1.0 / M_factor:
        gate2_msg = f"FAIL: M_eff too small (ratio={M_ratio:.2e})"
        fail_codes.append("FAIL_MASS_TOO_SMALL")
    elif M_ratio > M_factor:
        gate2_msg = f"FAIL: M_eff too large (ratio={M_ratio:.2e})"
        fail_codes.append("FAIL_MASS_TOO_LARGE")
    else:
        gate2_msg = f"PASS: M_eff within scaling (ratio={M_ratio:.2f})"

    # -------------------------------------------------------------------------
    # Gate 3: Coupling compatibility
    # -------------------------------------------------------------------------
    # Expected: g_eff² = 4πα / sin²θ_W × f(overlaps) with f ~ O(1)
    g_eff_expected = 4 * np.pi * alpha / sin2_theta_W
    g_ratio = overlaps.g_eff_squared / g_eff_expected

    # Allow O(1) variation
    gate3_pass = 0.1 < g_ratio < 10.0

    if g_ratio < 0.1:
        gate3_msg = f"FAIL: g_eff² too small (ratio={g_ratio:.2e})"
        fail_codes.append("FAIL_COUPLING_TOO_SMALL")
    elif g_ratio > 10.0:
        gate3_msg = f"FAIL: g_eff² too large (ratio={g_ratio:.2e})"
        fail_codes.append("FAIL_COUPLING_TOO_LARGE")
    else:
        gate3_msg = f"PASS: g_eff² compatible (ratio={g_ratio:.2f})"

    # -------------------------------------------------------------------------
    # Overall verdict
    # -------------------------------------------------------------------------
    all_pass = gate1_pass and gate2_pass and gate3_pass

    # Check X_EDC accuracy
    X_error = abs(overlaps.X_ratio - 1.0)

    if all_pass and X_error < X_tol:
        verdict = f"SUCCESS: X_EDC matches target within {X_tol*100:.0f}%"
    elif all_pass:
        verdict = f"GATES PASS but X_EDC off by {X_error*100:.1f}%"
    else:
        verdict = f"FAIL: {len(fail_codes)} gate(s) failed"

    return GateEvaluation(
        gate1_I4_pass=gate1_pass,
        gate1_I4_ratio=I4_ratio,
        gate1_message=gate1_msg,
        gate2_mass_pass=gate2_pass,
        gate2_mass_ratio=M_ratio,
        gate2_message=gate2_msg,
        gate3_coupling_pass=gate3_pass,
        gate3_coupling_ratio=g_ratio,
        gate3_message=gate3_msg,
        all_gates_pass=all_pass,
        overall_verdict=verdict,
        fail_codes=fail_codes
    )


# =============================================================================
# Test / Demo
# =============================================================================

if __name__ == "__main__":
    print("Overlaps Module — Test Run")
    print("=" * 60)

    # Create mock mode profiles for testing
    chi = np.linspace(-5, 5, 501)
    delta = 0.533

    # Simple Gaussian profiles
    def gaussian(x, center, width):
        g = np.exp(-(x - center)**2 / (2 * width**2))
        norm = np.sqrt(np.trapezoid(g**2, x))
        return g / norm

    w_L = ModeProfile(
        name="w_L", chi=chi, profile=gaussian(chi, -1, 0.3),
        eigenvalue=1.0, normalization=1.0, is_normalizable=True, n_nodes=0
    )
    w_R = ModeProfile(
        name="w_R", chi=chi, profile=gaussian(chi, +1, 0.3),
        eigenvalue=1.0, normalization=1.0, is_normalizable=True, n_nodes=0
    )
    w_phi = ModeProfile(
        name="w_phi", chi=chi, profile=gaussian(chi, 0, 0.5),
        eigenvalue=1.0, normalization=1.0, is_normalizable=True, n_nodes=0
    )

    # Test overlap computation
    I_4 = compute_I4(w_L, w_R, w_phi)
    I_g = compute_I_g(w_phi)
    eps = compute_epsilon(w_L, w_R)

    print(f"\nTest overlaps:")
    print(f"  I_4 = {I_4:.6e}")
    print(f"  I_g = {I_g:.6f}")
    print(f"  ε = {eps:.6e}")

    print("\n" + "=" * 60)
    print("Test complete.")
