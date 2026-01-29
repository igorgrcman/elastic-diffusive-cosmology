#!/usr/bin/env python3
"""
bvp_core.py — Core BVP Solver for Thick-Brane Mode Profiles

Issue: OPR-21 — Thick-brane BVP solution for G_F non-circular chain
Reference: edc_papers/_shared/derivations/gf_noncircular_chain_framework.tex

This module solves the 1D Schrödinger-like eigenvalue problem:
    -d²w/dχ² + V(χ)w = λw

for mode profiles w_L, w_R, w_φ in a thick-brane background.

Methods available:
- Finite difference (sparse eigenvalue problem)
- Shooting (root finding)

Status: [OPEN] — Pipeline implemented, physics background provisional
"""

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh, eigs
from scipy.integrate import solve_bvp, solve_ivp
from scipy.optimize import brentq
from dataclasses import dataclass
from typing import Tuple, List, Optional, Dict, Callable
import warnings


# =============================================================================
# Data Classes for Results
# =============================================================================

@dataclass
class ModeProfile:
    """Container for a single mode profile result."""
    name: str                     # "w_L", "w_R", "w_phi"
    chi: np.ndarray              # Grid points
    profile: np.ndarray          # Mode profile w(χ)
    eigenvalue: float            # Eigenvalue λ (dimensionless)
    normalization: float         # ∫|w|² dχ (should be 1)
    is_normalizable: bool        # Whether mode decays at boundaries
    n_nodes: int                 # Number of nodes (for mode identification)


@dataclass
class BVPSolution:
    """Container for complete BVP solution."""
    w_L: Optional[ModeProfile]
    w_R: Optional[ModeProfile]
    w_phi: Optional[ModeProfile]
    background_type: str
    delta: float                 # Brane thickness in GeV^{-1}
    domain: Tuple[float, float]  # (chi_min, chi_max) in GeV^{-1}
    solver_method: str
    converged: bool
    error_message: str


# =============================================================================
# Background Potentials
# =============================================================================

def gaussian_wall_potential(chi: np.ndarray, delta: float, width: float) -> np.ndarray:
    """
    Gaussian wall background potential.

    V(χ) = V_0 × exp(-χ²/(2w²))

    where V_0 is chosen such that the bound state has the right properties.

    For the mediator (scalar/gauge), this gives localization near χ=0.
    """
    w = width * delta
    # Potential depth chosen to give bound state with M ~ 1/δ
    V_0 = -1.0 / delta**2  # Negative = attractive
    return V_0 * np.exp(-chi**2 / (2 * w**2))


def rs_like_potential(chi: np.ndarray, delta: float, k: float) -> np.ndarray:
    """
    Randall-Sundrum-like warp factor potential.

    In RS, the effective potential for KK modes has the form:
    V(χ) = (15/4) k² - 3k δ(χ)

    We smooth the delta function with width δ.
    """
    # Smoothed delta function
    delta_smooth = np.exp(-chi**2 / (2 * delta**2)) / (np.sqrt(2 * np.pi) * delta)
    V_bulk = (15.0 / 4.0) * k**2
    V_brane = -3.0 * k * delta_smooth
    return V_bulk + V_brane


def tanh_wall_potential(chi: np.ndarray, delta: float, steepness: float) -> np.ndarray:
    """
    Tanh domain wall potential.

    V(χ) = -V_0 × sech²(χ/w)

    This is the classic reflectionless potential with known analytic solutions.
    """
    w = delta / steepness
    V_0 = 1.0 / delta**2
    return -V_0 / np.cosh(chi / w)**2


def fermion_domain_wall_mass(chi: np.ndarray, delta: float,
                             center: float = 0.0) -> np.ndarray:
    """
    Domain wall mass profile for chiral fermion localization.

    m(χ) = m_0 × tanh((χ - center)/δ)

    This profile localizes left-handed modes on one side and
    right-handed modes on the other.
    """
    m_0 = 1.0 / delta
    return m_0 * np.tanh((chi - center) / delta)


def fermion_effective_potential(chi: np.ndarray, mass_profile: np.ndarray,
                                chirality: str) -> np.ndarray:
    """
    Effective Schrödinger potential for fermion in domain wall background.

    For a fermion with mass m(χ), the effective 1D potential is:
    V_± = m² ∓ m'

    where + is for right-handed and - is for left-handed.
    """
    # Compute derivative using finite differences
    dchi = chi[1] - chi[0]
    m_prime = np.gradient(mass_profile, dchi)

    m_squared = mass_profile**2

    if chirality == "left":
        return m_squared - m_prime
    elif chirality == "right":
        return m_squared + m_prime
    else:
        raise ValueError(f"Unknown chirality: {chirality}")


# =============================================================================
# Finite Difference Eigenvalue Solver
# =============================================================================

def build_hamiltonian_matrix(chi: np.ndarray, V: np.ndarray,
                             bc_type: str = "dirichlet") -> sparse.csr_matrix:
    """
    Build the discretized Hamiltonian matrix for the eigenvalue problem.

    H = -d²/dχ² + V(χ)

    Uses second-order finite differences.

    Args:
        chi: Grid points
        V: Potential values at grid points
        bc_type: "dirichlet" (w=0 at boundaries) or "neumann" (w'=0)

    Returns:
        Sparse Hamiltonian matrix
    """
    n = len(chi)
    dchi = chi[1] - chi[0]
    dchi2 = dchi**2

    # Kinetic energy: -d²/dχ² using three-point stencil
    # -w''(χ) ≈ (-w_{i-1} + 2w_i - w_{i+1}) / dχ²
    diag_main = 2.0 / dchi2 + V
    diag_off = -1.0 / dchi2 * np.ones(n - 1)

    H = sparse.diags([diag_off, diag_main, diag_off], [-1, 0, 1], format='csr')

    # Apply boundary conditions
    if bc_type == "dirichlet":
        # w(±L) = 0: already implicit in matrix structure
        pass
    elif bc_type == "neumann":
        # w'(±L) = 0: modify first and last rows
        # Use one-sided derivative: w_1 = w_0 (ghost point)
        H = H.tolil()
        H[0, 0] = 1.0 / dchi2 + V[0]
        H[0, 1] = -1.0 / dchi2
        H[-1, -1] = 1.0 / dchi2 + V[-1]
        H[-1, -2] = -1.0 / dchi2
        H = H.tocsr()

    return H


def solve_eigenvalue_problem(chi: np.ndarray, V: np.ndarray,
                             n_eigenvalues: int = 5,
                             bc_type: str = "dirichlet",
                             which: str = "SM") -> Tuple[np.ndarray, np.ndarray]:
    """
    Solve the eigenvalue problem Hw = λw.

    Args:
        chi: Grid points
        V: Potential values
        n_eigenvalues: Number of eigenvalues to compute
        bc_type: Boundary condition type
        which: Which eigenvalues ("SM" = smallest magnitude, "SA" = smallest algebraic)

    Returns:
        eigenvalues: Array of eigenvalues
        eigenvectors: Array of eigenvectors (columns)
    """
    H = build_hamiltonian_matrix(chi, V, bc_type)

    # Use sparse eigensolver
    # Note: eigsh requires Hermitian matrix, which H is
    try:
        k = min(n_eigenvalues, len(chi) - 2)
        eigenvalues, eigenvectors = eigsh(H, k=k, which=which)

        # Sort by eigenvalue
        idx = np.argsort(eigenvalues)
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]

        return eigenvalues, eigenvectors

    except Exception as e:
        warnings.warn(f"Eigenvalue solver failed: {e}")
        return np.array([]), np.array([])


# =============================================================================
# Mode Profile Computation
# =============================================================================

def normalize_mode(chi: np.ndarray, w: np.ndarray) -> Tuple[np.ndarray, float]:
    """
    Normalize mode profile to ∫|w|² dχ = 1.

    Returns:
        w_normalized: Normalized profile
        norm: Original norm (for diagnostics)
    """
    dchi = chi[1] - chi[0]
    norm = np.sqrt(np.trapezoid(w**2, chi))

    if norm > 1e-15:
        w_normalized = w / norm
    else:
        w_normalized = w
        norm = 0.0

    return w_normalized, norm


def count_nodes(w: np.ndarray) -> int:
    """Count the number of nodes (zero crossings) in the mode profile."""
    signs = np.sign(w[:-1]) * np.sign(w[1:])
    return int(np.sum(signs < 0))


def check_normalizability(chi: np.ndarray, w: np.ndarray,
                          threshold: float = 0.01) -> bool:
    """
    Check if mode is normalizable (decays at boundaries).

    A mode is considered normalizable if its amplitude at the boundaries
    is less than threshold × max amplitude.
    """
    w_max = np.max(np.abs(w))
    if w_max < 1e-15:
        return False

    boundary_amp = max(np.abs(w[0]), np.abs(w[-1]))
    return boundary_amp / w_max < threshold


def compute_mode_profile(chi: np.ndarray, V: np.ndarray,
                         name: str,
                         n_eigenvalues: int = 5,
                         bc_type: str = "dirichlet") -> ModeProfile:
    """
    Compute a single mode profile from the BVP.

    Returns the ground state (lowest eigenvalue) mode.
    """
    eigenvalues, eigenvectors = solve_eigenvalue_problem(
        chi, V, n_eigenvalues, bc_type, which="SA"
    )

    if len(eigenvalues) == 0:
        return ModeProfile(
            name=name,
            chi=chi,
            profile=np.zeros_like(chi),
            eigenvalue=np.nan,
            normalization=0.0,
            is_normalizable=False,
            n_nodes=-1
        )

    # Take ground state (lowest eigenvalue)
    # For bound states in attractive potential, this is the most localized
    lambda_0 = eigenvalues[0]
    w_raw = eigenvectors[:, 0]

    # Normalize
    w_norm, original_norm = normalize_mode(chi, w_raw)

    # Make profile positive at center (convention)
    if w_norm[len(w_norm)//2] < 0:
        w_norm = -w_norm

    # Check normalizability
    is_norm = check_normalizability(chi, w_norm)

    # Count nodes
    n_nodes = count_nodes(w_norm)

    return ModeProfile(
        name=name,
        chi=chi,
        profile=w_norm,
        eigenvalue=lambda_0,
        normalization=np.trapezoid(w_norm**2, chi),
        is_normalizable=is_norm,
        n_nodes=n_nodes
    )


# =============================================================================
# Full BVP Solver
# =============================================================================

def solve_thick_brane_bvp(config: Dict) -> BVPSolution:
    """
    Main entry point: solve the thick-brane BVP for all mode profiles.

    Args:
        config: Configuration dictionary (from YAML)

    Returns:
        BVPSolution containing all mode profiles and metadata
    """
    # Extract parameters
    phys = config['physical']
    bg = config['background']
    dom = config['domain']
    modes_cfg = config['modes']
    solver_cfg = config['solver']

    delta = phys['delta_GeV_inv']

    # Build grid
    L = dom['L_delta'] * delta
    n_points = dom['n_points']

    if dom['grid_type'] == 'uniform':
        chi = np.linspace(-L, L, n_points)
    else:
        # Chebyshev grid (more points near boundaries)
        theta = np.linspace(0, np.pi, n_points)
        chi = L * np.cos(theta)[::-1]

    # Build background potential
    wall_width = bg['wall_width_delta'] * delta

    if bg['type'] == 'gaussian_wall':
        V_base = gaussian_wall_potential(chi, delta, bg['wall_width_delta'])
    elif bg['type'] == 'rs_like':
        V_base = rs_like_potential(chi, delta, bg['rs_warp_k'])
    elif bg['type'] == 'tanh_wall':
        V_base = tanh_wall_potential(chi, delta, bg['tanh_steepness'])
    else:
        # Default: simple harmonic well
        V_base = 0.5 * chi**2 / delta**4

    # Solve for each mode
    w_L = None
    w_R = None
    w_phi = None

    n_eig = modes_cfg['n_eigenvalues']
    bc_type = "dirichlet"  # Normalizable modes vanish at infinity

    # Mediator mode (scalar/gauge) — localized near brane
    if modes_cfg['compute_w_phi']:
        w_phi = compute_mode_profile(chi, V_base, "w_phi", n_eig, bc_type)

    # Fermion modes — use domain wall mass profile
    if modes_cfg['compute_w_L'] or modes_cfg['compute_w_R']:
        fermion_width = modes_cfg['fermion_width_delta'] * delta
        LR_sep = modes_cfg['LR_separation_delta'] * delta

        # Left-handed fermion: localized at χ < 0
        if modes_cfg['compute_w_L']:
            mass_L = fermion_domain_wall_mass(chi, fermion_width, center=-LR_sep/2)
            V_L = fermion_effective_potential(chi, mass_L, "left")
            w_L = compute_mode_profile(chi, V_L, "w_L", n_eig, bc_type)

        # Right-handed fermion: localized at χ > 0
        if modes_cfg['compute_w_R']:
            mass_R = fermion_domain_wall_mass(chi, fermion_width, center=+LR_sep/2)
            V_R = fermion_effective_potential(chi, mass_R, "right")
            w_R = compute_mode_profile(chi, V_R, "w_R", n_eig, bc_type)

    # Check convergence
    converged = True
    error_msg = ""

    if w_phi is not None and not w_phi.is_normalizable:
        converged = False
        error_msg += "w_phi not normalizable. "

    if w_L is not None and not w_L.is_normalizable:
        converged = False
        error_msg += "w_L not normalizable. "

    if w_R is not None and not w_R.is_normalizable:
        converged = False
        error_msg += "w_R not normalizable. "

    return BVPSolution(
        w_L=w_L,
        w_R=w_R,
        w_phi=w_phi,
        background_type=bg['type'],
        delta=delta,
        domain=(-L, L),
        solver_method=solver_cfg['method'],
        converged=converged,
        error_message=error_msg if error_msg else "OK"
    )


# =============================================================================
# Toy Profile Generators (for quick-run mode)
# =============================================================================

def generate_toy_profiles(config: Dict) -> BVPSolution:
    """
    Generate toy exponential profiles without solving BVP.

    This is for testing the pipeline quickly.
    """
    phys = config['physical']
    dom = config['domain']
    modes_cfg = config['modes']

    delta = phys['delta_GeV_inv']
    L = dom['L_delta'] * delta

    # Reduced grid for quick run
    n_points = config.get('quick_run', {}).get('n_points_quick', 201)
    chi = np.linspace(-L, L, n_points)

    # Toy parameters
    sigma = modes_cfg['fermion_width_delta'] * delta
    d = modes_cfg['LR_separation_delta'] * delta

    # Exponential profiles (from framework toy model)
    def exp_profile(chi, center, width):
        w = np.exp(-np.abs(chi - center) / width)
        norm = np.sqrt(np.trapezoid(w**2, chi))
        return w / norm if norm > 0 else w

    # Left fermion at -d/2
    w_L_arr = exp_profile(chi, -d/2, sigma)
    w_L = ModeProfile(
        name="w_L",
        chi=chi,
        profile=w_L_arr,
        eigenvalue=1.0 / sigma**2,  # Toy eigenvalue
        normalization=np.trapezoid(w_L_arr**2, chi),
        is_normalizable=True,
        n_nodes=0
    )

    # Right fermion at +d/2
    w_R_arr = exp_profile(chi, +d/2, sigma)
    w_R = ModeProfile(
        name="w_R",
        chi=chi,
        profile=w_R_arr,
        eigenvalue=1.0 / sigma**2,
        normalization=np.trapezoid(w_R_arr**2, chi),
        is_normalizable=True,
        n_nodes=0
    )

    # Mediator at center with width delta
    w_phi_arr = exp_profile(chi, 0, delta)
    w_phi = ModeProfile(
        name="w_phi",
        chi=chi,
        profile=w_phi_arr,
        eigenvalue=1.0 / delta**2,
        normalization=np.trapezoid(w_phi_arr**2, chi),
        is_normalizable=True,
        n_nodes=0
    )

    return BVPSolution(
        w_L=w_L,
        w_R=w_R,
        w_phi=w_phi,
        background_type="toy_exponential",
        delta=delta,
        domain=(-L, L),
        solver_method="toy_profiles",
        converged=True,
        error_message="Toy profiles (not BVP solution)"
    )


# =============================================================================
# Test / Demo
# =============================================================================

if __name__ == "__main__":
    print("BVP Core Module — Test Run")
    print("=" * 60)

    # Minimal test config
    test_config = {
        'physical': {
            'delta_GeV_inv': 0.533,
            'm_e_GeV': 0.00051099895,
            'alpha': 0.0072973525693,
            'sin2_theta_W': 0.25,
            'X_target': 3.04e-12,
        },
        'background': {
            'type': 'gaussian_wall',
            'wall_width_delta': 1.0,
            'rs_warp_k': 1.0,
            'tanh_steepness': 5.0,
        },
        'domain': {
            'L_delta': 10.0,
            'n_points': 501,
            'grid_type': 'uniform',
        },
        'modes': {
            'compute_w_L': True,
            'compute_w_R': True,
            'compute_w_phi': True,
            'fermion_model': 'domain_wall',
            'fermion_width_delta': 0.1,
            'LR_separation_delta': 2.0,
            'n_eigenvalues': 5,
        },
        'solver': {
            'method': 'finite_diff',
        },
    }

    print("\nSolving BVP...")
    solution = solve_thick_brane_bvp(test_config)

    print(f"\nBackground: {solution.background_type}")
    print(f"Converged: {solution.converged}")
    print(f"Error: {solution.error_message}")

    for mode in [solution.w_L, solution.w_R, solution.w_phi]:
        if mode is not None:
            print(f"\n{mode.name}:")
            print(f"  λ = {mode.eigenvalue:.6f}")
            print(f"  norm = {mode.normalization:.6f}")
            print(f"  normalizable = {mode.is_normalizable}")
            print(f"  nodes = {mode.n_nodes}")

    print("\n" + "=" * 60)
    print("Test complete.")
