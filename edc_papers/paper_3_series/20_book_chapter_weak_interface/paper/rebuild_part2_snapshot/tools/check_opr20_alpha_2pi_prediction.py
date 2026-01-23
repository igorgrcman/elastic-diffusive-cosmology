#!/usr/bin/env python3
"""
OPR-20 Attempt H: α = 2π Prediction Tool

Purpose:
- Run the BVP solver at α = 2π (natural value from δ = R_ξ)
- Compute x₁ and m_φ predictions
- Verify that x₁ falls in the target range [2.3, 2.8]
- No SM inputs used to SET parameters

NO-SMUGGLING:
- α = 2π comes from ℓ/δ = 2πR_ξ/R_ξ = 2π [Dc]
- R_ξ from Part I [P] (diffusion scale)
- M_W appears only in DIAGNOSTIC comparison [BL]

Usage:
    python3 check_opr20_alpha_2pi_prediction.py
"""

import numpy as np
from dataclasses import dataclass
from typing import Optional
import sys

# ==============================================================================
# PHYSICAL CONSTANTS (FORBIDDEN AS INPUTS TO DETERMINE α)
# ==============================================================================

# Baseline for COMPARISON ONLY [BL]
M_W_GEV = 80.4  # GeV — SM weak boson mass

# Conversion
HBARC_GEV_FM = 0.197327  # GeV·fm

# ==============================================================================
# EDC PARAMETERS [P] from Part I
# ==============================================================================

@dataclass
class EDCParameters:
    """EDC membrane parameters from Part I."""
    R_xi_fm: float = 1e-3       # Diffusion scale [fm] [P] (~10⁻³ fm)
    sigma: float = 68.5         # Membrane tension [MeV/fm²] [P]
    r_e_fm: float = 2.818e-3    # Classical electron radius [fm] [BL]


# ==============================================================================
# ROBIN BC SOLVER (simplified from solve_opr20_mediator_bvp.py)
# ==============================================================================

def solve_robin_bvp(alpha: float, N: int = 400) -> tuple:
    """
    Solve empty-box BVP with symmetric Robin BC: f' + α·f = 0 at both ends.

    This uses the same discretization as solve_opr20_mediator_bvp.py:
    - N interior points (i = 1, ..., N)
    - Grid spacing h = 1/(N+1)
    - Boundary values f_0 and f_{N+1} eliminated via Robin BC

    Returns:
        (x1, eigenvalues, xi, profile)
    """
    # Grid: N interior points with h = 1/(N+1)
    h = 1.0 / (N + 1)
    xi = np.array([(i + 1) * h for i in range(N)])  # Interior points only

    # Empty box: V = 0
    V = np.zeros(N)

    # Build Hamiltonian matrix with Robin BC
    H = np.zeros((N, N))

    # Standard tridiagonal interior
    for i in range(N):
        H[i, i] = 2.0 / h**2 + V[i]
        if i > 0:
            H[i, i-1] = -1.0 / h**2
        if i < N - 1:
            H[i, i+1] = -1.0 / h**2

    # Left BC modification at row 0 (corresponds to xi_1)
    # Robin at left: f'(0) + alpha*f(0) = 0
    # One-sided: (f_1 - f_0)/h + alpha*f_0 = 0
    # => f_0 = f_1 / (1 + alpha*h)
    beta_L = 1.0 / (1.0 + alpha * h) if (1.0 + alpha * h) > 1e-10 else 0.0
    H[0, 0] = (2.0 - beta_L) / h**2 + V[0]

    # Right BC modification at row N-1
    # Robin at right: f'(1) + alpha*f(1) = 0
    # => f_{N+1} = f_N / (1 + alpha*h)
    beta_R = 1.0 / (1.0 + alpha * h) if (1.0 + alpha * h) > 1e-10 else 0.0
    H[N-1, N-1] = (2.0 - beta_R) / h**2 + V[N-1]

    # Solve eigenvalue problem
    eigenvalues, eigenvectors = np.linalg.eigh(H)

    # x_n = sqrt(λ_n)
    x_values = np.sqrt(np.maximum(eigenvalues, 0))

    # Ground state
    x1 = x_values[0]
    profile = eigenvectors[:, 0]

    # Normalize
    norm = np.sqrt(np.trapezoid(profile**2, xi))
    profile = profile / norm

    return x1, x_values[:5], xi, profile


def compute_m_phi(x1: float, R_xi_fm: float) -> float:
    """
    Compute mediator mass from eigenvalue.

    m_φ = x₁/ℓ = x₁/(2π√2 R_ξ)

    Returns m_φ in GeV.
    """
    ell_fm = 2 * np.pi * np.sqrt(2) * R_xi_fm  # [Dc] from Attempt E
    m_phi_inv_fm = x1 / ell_fm
    m_phi_GeV = m_phi_inv_fm * HBARC_GEV_FM
    return m_phi_GeV


def compute_I4(xi: np.ndarray, profile: np.ndarray) -> float:
    """Compute overlap integral I₄ = ∫|f|⁴ dξ."""
    return np.trapezoid(profile**4, xi)


# ==============================================================================
# MAIN PREDICTION
# ==============================================================================

def main():
    print("=" * 78)
    print("OPR-20 ATTEMPT H: α = 2π PREDICTION (δ = R_ξ gate)")
    print("=" * 78)
    print()

    # No-smuggling banner
    print("NO-SMUGGLING VERIFICATION:")
    print("-" * 40)
    print("α = 2π comes from:")
    print("  • ℓ = 2π R_ξ       [Dc] (circumference, Attempt E)")
    print("  • δ = R_ξ          [P]  (diffusion scale = boundary layer thickness)")
    print("  • α = ℓ/δ = 2π     [Dc] (structure) + [P] (δ = R_ξ identification)")
    print()
    print("FORBIDDEN inputs: M_W, G_F, g₂, v (NOT used to determine α)")
    print("M_W = 80.4 GeV appears ONLY in diagnostic comparison [BL]")
    print("=" * 78)
    print()

    # Parameters
    params = EDCParameters()
    alpha = 2 * np.pi  # Natural value from δ = R_ξ

    print(f"EDC Parameters [P]:")
    print(f"  R_ξ = {params.R_xi_fm} fm (diffusion scale)")
    print(f"  ℓ = 2π√2 R_ξ = {2*np.pi*np.sqrt(2)*params.R_xi_fm:.6f} fm")
    print()
    print(f"Robin Parameter:")
    print(f"  α = 2π = {alpha:.6f} (from δ = R_ξ)")
    print()

    # Solve BVP
    print("Solving Robin BVP...")
    x1, x_values, xi, profile = solve_robin_bvp(alpha)
    I4 = compute_I4(xi, profile)

    print()
    print("=" * 78)
    print("RESULTS")
    print("=" * 78)
    print()

    # Eigenvalue
    print(f"Ground state eigenvalue:")
    print(f"  x₁ = {x1:.6f}")
    print()

    # Target check
    target_min, target_max = 2.3, 2.8
    in_target = target_min <= x1 <= target_max
    status = "YES (GREENLIGHT)" if in_target else "NO"
    print(f"Target range check:")
    print(f"  Target: x₁ ∈ [{target_min}, {target_max}]")
    print(f"  In range: {status}")
    print()

    # Mass prediction
    m_phi = compute_m_phi(x1, params.R_xi_fm)
    print(f"Mediator mass prediction:")
    print(f"  m_φ = x₁/ℓ = {m_phi:.2f} GeV")
    print()

    # Diagnostic comparison [BL]
    print("-" * 40)
    print("DIAGNOSTIC COMPARISON [BL] (NOT input):")
    deviation = 100 * (m_phi - M_W_GEV) / M_W_GEV
    print(f"  M_W = {M_W_GEV} GeV (SM)")
    print(f"  m_φ/M_W = {m_phi/M_W_GEV:.4f}")
    print(f"  Deviation: {deviation:+.1f}%")
    print("-" * 40)
    print()

    # Overlap integral
    print(f"Overlap integral:")
    print(f"  I₄ = {I4:.6f}")
    print()

    # Summary box
    print("=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print()
    print("┌─────────────────────────────────────────────────────────────────────────┐")
    print("│  α = 2π PREDICTION (Attempt G + H)                                      │")
    print("├─────────────────────────────────────────────────────────────────────────┤")
    print(f"│  Robin parameter:  α = 2π ≈ {alpha:.3f}                                   │")
    print(f"│  Ground state:     x₁ = {x1:.4f}                                         │")
    print(f"│  Target range:     [{target_min}, {target_max}]  →  {'IN RANGE' if in_target else 'OUT OF RANGE':^10}                     │")
    print(f"│  Mediator mass:    m_φ = {m_phi:.1f} GeV                                     │")
    print(f"│  vs M_W [BL]:      {deviation:+.1f}%                                              │")
    print("├─────────────────────────────────────────────────────────────────────────┤")
    print("│  Epistemic status:                                                      │")
    print("│    • Robin form from action:  [Dc]                                      │")
    print("│    • α ~ ℓ/δ structure:       [Dc]                                      │")
    print("│    • δ = R_ξ identification:  [P] (Attempt H target)                    │")
    print("└─────────────────────────────────────────────────────────────────────────┘")
    print()

    # Upgrade condition
    print("UPGRADE CONDITION:")
    print("  OPR-20 → YELLOW [P] if δ = R_ξ is established from Part I microphysics")
    print()

    return 0 if in_target else 1


if __name__ == "__main__":
    sys.exit(main())
