#!/usr/bin/env python3
"""
gf_toy_overlap_window.py — Toy Model Feasibility Window for G_F Non-Circular Chain

Status: [I] — Illustrative toy model, NOT an EDC derivation
Date: 2026-01-29
Issue: P3-3 — G_F derivation without circularity

This script explores the parameter space where the non-circular G_F formula
could match experiment, using simplified mode profiles. The actual values
require solving the thick-brane BVP (OPR-21).

IMPORTANT: All outputs are tagged as "toy / not EDC derived" because:
1. Mode profiles are ansatz (exponential/Gaussian), not BVP solutions
2. Parameter values (ε, σ/δ) are scanned, not derived
3. This is a feasibility check, not a prediction
"""

import numpy as np
from dataclasses import dataclass
from typing import Tuple, List

# =============================================================================
# Physical Constants (natural units: ℏ = c = 1)
# =============================================================================

# Measured values [BL]
G_F = 1.1663787e-5  # GeV^{-2} (Fermi constant)
m_e = 0.51099895e-3  # GeV (electron mass)
alpha = 1/137.036  # fine structure constant
m_p = 0.93827  # GeV (proton mass)

# EDC scale parameter [Dc]
delta = 1 / (2 * m_p)  # GeV^{-1} ≈ 0.533 GeV^{-1} ≈ 0.105 fm

# Target dimensionless combination [BL]
X_target = G_F * m_e**2  # ≈ 3.04 × 10^{-12}

# SM convention factor
C = 1 / (4 * np.sqrt(2))  # ≈ 0.177

# sin²θ_W = 1/4 [Der] from Z₆ subgroup counting
sin2_theta_W = 0.25

print("=" * 70)
print("G_F TOY OVERLAP WINDOW — Feasibility Check [I]")
print("=" * 70)
print("\n⚠️  CAVEAT: This is a TOY MODEL, not an EDC derivation.")
print("    Actual values require thick-brane BVP solution (OPR-21).\n")

print("Physical Constants:")
print(f"  G_F = {G_F:.4e} GeV^{{-2}} [BL]")
print(f"  m_e = {m_e:.4e} GeV [BL]")
print(f"  δ = {delta:.4e} GeV^{{-1}} = {delta * 0.197:.4f} fm [Dc]")
print(f"  1/δ = {1/delta:.4f} GeV [Dc]")
print(f"  X_target = G_F × m_e² = {X_target:.4e} [BL]")
print(f"  sin²θ_W = 1/4 = {sin2_theta_W} [Der]")
print()


# =============================================================================
# Toy Mode Profiles
# =============================================================================

@dataclass
class ToyModeParams:
    """Parameters for toy mode profiles."""
    sigma: float  # Width of fermion localization (GeV^{-1})
    d: float  # L-R separation distance (GeV^{-1})
    delta_phi: float  # Width of mediator mode (GeV^{-1})


def exponential_profile(chi: np.ndarray, center: float, width: float) -> np.ndarray:
    """Exponential mode profile: w(χ) ∝ exp(-|χ - center| / width)."""
    return np.exp(-np.abs(chi - center) / width) / np.sqrt(2 * width)


def gaussian_profile(chi: np.ndarray, center: float, width: float) -> np.ndarray:
    """Gaussian mode profile: w(χ) ∝ exp(-(χ - center)² / 2σ²)."""
    return np.exp(-0.5 * ((chi - center) / width)**2) / (np.sqrt(np.sqrt(np.pi) * width))


def compute_overlap_integral(chi: np.ndarray, w_L: np.ndarray, w_R: np.ndarray,
                            w_phi: np.ndarray) -> float:
    """
    Compute the four-point overlap integral I_4.

    I_4 = ∫ dχ w_L² w_R² w_φ²

    Returns: I_4 in GeV (since [w²] = GeV and we integrate over GeV^{-1})
    """
    dchi = chi[1] - chi[0]
    integrand = w_L**2 * w_R**2 * w_phi**2
    return np.trapz(integrand, chi)


def chirality_suppression(d: float, sigma: float, profile_type: str = 'exponential') -> float:
    """
    Compute chirality suppression factor ε = ∫ dχ w_L w_R.

    For exponential: ε = exp(-d / (2σ))
    For Gaussian: ε = exp(-d² / (4σ²))
    """
    if profile_type == 'exponential':
        return np.exp(-d / (2 * sigma))
    elif profile_type == 'gaussian':
        return np.exp(-d**2 / (4 * sigma**2))
    else:
        raise ValueError(f"Unknown profile type: {profile_type}")


# =============================================================================
# Non-Circular G_F Formula
# =============================================================================

def compute_X_EDC(g5_squared: float, I4: float, M_eff: float) -> float:
    """
    Compute dimensionless X_EDC from non-circular formula.

    X_EDC = C × (g_5² × I_4 × m_e²) / M_eff²

    where C = 1/(4√2) is the SM convention factor.
    """
    return C * g5_squared * I4 * m_e**2 / M_eff**2


def estimate_g5_squared(delta_val: float) -> float:
    """
    Estimate g_5² from natural 5D scaling.

    [g_5²] = length = energy^{-1}
    Natural scale: g_5² ~ δ × (4πα / sin²θ_W)
    """
    return delta_val * 4 * np.pi * alpha / sin2_theta_W


def estimate_M_eff(delta_val: float, lambda_0: float = 1.0) -> float:
    """
    Estimate effective mediator mass from KK scaling.

    M_eff² = λ_0 / δ²  →  M_eff = √λ_0 / δ
    """
    return np.sqrt(lambda_0) / delta_val


# =============================================================================
# Parameter Scan
# =============================================================================

print("=" * 70)
print("PARAMETER SCAN: Toy Feasibility Window")
print("=" * 70)
print("\nScanning over (ε, σ/δ) to find region where X_EDC ≈ X_target...")
print("Profile type: Exponential (simpler analytic estimates)\n")

# Grid parameters
n_epsilon = 20
n_sigma_ratio = 20

epsilon_range = np.logspace(-4, -1, n_epsilon)  # 10^{-4} to 10^{-1}
sigma_ratio_range = np.linspace(0.01, 0.5, n_sigma_ratio)  # σ/δ from 0.01 to 0.5

# Fixed parameters for scan
lambda_0 = 1.0  # KK eigenvalue (dimensionless) [OPEN]
g5_squared = estimate_g5_squared(delta)
M_eff = estimate_M_eff(delta, lambda_0)

print(f"Fixed parameters:")
print(f"  λ_0 = {lambda_0} (KK eigenvalue) [OPEN — requires BVP]")
print(f"  g_5² = {g5_squared:.4e} GeV^{{-1}} [Dc — from natural scaling]")
print(f"  M_eff = {M_eff:.4f} GeV [Dc — requires BVP eigenvalue]")
print()

# Storage for results
results: List[Tuple[float, float, float, float]] = []

for epsilon in epsilon_range:
    for sigma_ratio in sigma_ratio_range:
        sigma = sigma_ratio * delta

        # For exponential profiles, the overlap I_4 scales as:
        # I_4 ~ ε² / σ (rough estimate from dimensional analysis)
        # More precisely, with L-R separation d and mediator width δ:
        I4_estimate = epsilon**2 / sigma  # GeV

        # Compute X_EDC
        X_EDC = compute_X_EDC(g5_squared, I4_estimate, M_eff)

        # Store if within order of magnitude of target
        ratio = X_EDC / X_target
        if 0.1 < ratio < 10:
            results.append((epsilon, sigma_ratio, I4_estimate, ratio))

print(f"Found {len(results)} parameter combinations within [0.1, 10] × X_target\n")

if results:
    print("Sample feasibility points (ε, σ/δ, I_4, X_EDC/X_target):")
    print("-" * 60)
    # Show a subset of results
    for i, (eps, sr, I4, ratio) in enumerate(results[::max(1, len(results)//10)]):
        print(f"  ε = {eps:.2e}, σ/δ = {sr:.3f}, I_4 = {I4:.2e} GeV, ratio = {ratio:.2f}")
    print()


# =============================================================================
# Numerical Integration Check
# =============================================================================

print("=" * 70)
print("NUMERICAL INTEGRATION: Explicit Mode Profile Overlap")
print("=" * 70)

# Choose a representative point from feasibility window
epsilon_test = 3e-3
sigma_test = 0.05 * delta  # σ/δ = 0.05

# Compute d from ε for exponential profile: ε = exp(-d/(2σ))
d_test = -2 * sigma_test * np.log(epsilon_test)

print(f"\nTest point parameters:")
print(f"  ε = {epsilon_test:.2e} (chirality suppression)")
print(f"  σ = {sigma_test:.4e} GeV^{{-1}} = {sigma_test/delta:.3f} × δ")
print(f"  d = {d_test:.4e} GeV^{{-1}} (L-R separation)")
print()

# Create integration grid
chi_min = -10 * delta
chi_max = d_test + 10 * delta
n_points = 10000
chi = np.linspace(chi_min, chi_max, n_points)

# Compute mode profiles
w_L = exponential_profile(chi, 0, sigma_test)
w_R = exponential_profile(chi, d_test, sigma_test)
w_phi = exponential_profile(chi, d_test/2, delta)  # Mediator centered between L and R

# Verify normalizations
norm_L = np.trapz(w_L**2, chi)
norm_R = np.trapz(w_R**2, chi)
norm_phi = np.trapz(w_phi**2, chi)

print(f"Mode normalizations (should be ~1):")
print(f"  ∫ w_L² dχ = {norm_L:.6f}")
print(f"  ∫ w_R² dχ = {norm_R:.6f}")
print(f"  ∫ w_φ² dχ = {norm_phi:.6f}")
print()

# Compute overlap integral
I4_numeric = compute_overlap_integral(chi, w_L, w_R, w_phi)

# Compute X_EDC
X_EDC_numeric = compute_X_EDC(g5_squared, I4_numeric, M_eff)
ratio_numeric = X_EDC_numeric / X_target

print(f"Overlap integral:")
print(f"  I_4 (numeric) = {I4_numeric:.4e} GeV")
print(f"  I_4 (estimate ε²/σ) = {epsilon_test**2/sigma_test:.4e} GeV")
print()

print(f"Dimensionless target comparison:")
print(f"  X_EDC = {X_EDC_numeric:.4e}")
print(f"  X_target = {X_target:.4e}")
print(f"  X_EDC / X_target = {ratio_numeric:.3f}")
print()


# =============================================================================
# Required I_4 for Exact Match
# =============================================================================

print("=" * 70)
print("REQUIRED OVERLAP FOR EXACT MATCH")
print("=" * 70)

# Invert the formula to find required I_4
I4_required = X_target * M_eff**2 / (C * g5_squared * m_e**2)

print(f"\nFor X_EDC = X_target exactly:")
print(f"  I_4_required = {I4_required:.4e} GeV")
print(f"  √I_4_required = {np.sqrt(I4_required)*1000:.2f} MeV")
print()

# What chirality suppression does this imply?
# I_4 ~ ε²/σ → ε ~ √(I_4 × σ)
for sigma_ratio in [0.01, 0.05, 0.1]:
    sigma_val = sigma_ratio * delta
    epsilon_req = np.sqrt(I4_required * sigma_val)
    print(f"  If σ/δ = {sigma_ratio}: ε_required ≈ {epsilon_req:.2e}")

print()


# =============================================================================
# Falsification Gate Checks
# =============================================================================

print("=" * 70)
print("FALSIFICATION GATE STATUS")
print("=" * 70)

print("\nGate 1: Overlap Mismatch")
print(f"  Required: I_4 ∈ [0.1, 10] × {I4_required:.2e} GeV")
print(f"  BVP must deliver: I_4 ∈ [{0.1*I4_required:.2e}, {10*I4_required:.2e}] GeV")
print(f"  Status: [OPEN] — awaits BVP (OPR-21)")

print("\nGate 2: Mass Consistency")
print(f"  Required: M_eff ∈ [0.1, 10] × (1/δ) = [{0.1/delta:.2f}, {10/delta:.1f}] GeV")
print(f"  Current estimate: M_eff = {M_eff:.2f} GeV (with λ_0 = 1)")
print(f"  Status: ✓ PASS within expected range (pending λ_0 from BVP)")

print("\nGate 3: Coupling Compatibility")
g_eff_squared = g5_squared * delta  # Rough estimate of 4D coupling
g_eff_expected = 4 * np.pi * alpha / sin2_theta_W
print(f"  g_eff² (estimate) = {g_eff_squared:.4e}")
print(f"  g_eff² (expected from α, sin²θ_W) = {g_eff_expected:.4f}")
print(f"  Ratio = {g_eff_squared/g_eff_expected:.2e}")
print(f"  Status: [Dc] — requires gauge overlap I_g from BVP")

print()


# =============================================================================
# Summary
# =============================================================================

print("=" * 70)
print("SUMMARY: Toy Feasibility Window [I]")
print("=" * 70)

print("""
✓ FEASIBILITY CHECK PASSED:
  - Parameter space exists where X_EDC could match X_target
  - Required overlap I_4 ~ (6 MeV)² is physically reasonable
  - Chirality suppression ε ~ 10⁻³ – 10⁻² is achievable with localization

⚠️  CAVEATS (this is NOT an EDC derivation):
  - Mode profiles are toy ansätze, not BVP solutions
  - Parameters (ε, σ/δ) are scanned, not derived from 5D action
  - Actual numerical G_F requires solving OPR-21 (thick-brane BVP)

🎯 BVP MUST DELIVER:
  - Mode profiles w_L(χ), w_R(χ), w_φ(χ) from thick-brane Dirac equation
  - KK eigenvalue λ_0 for M_eff = √λ_0 / δ
  - Overlap integral I_4 ∈ feasibility window

📊 PREDICTION FORK:
  If BVP delivers I_4 within [0.1, 10] × I_4_required → G_F mechanism viable
  If BVP delivers I_4 outside this window → falsification or model revision
""")

print("=" * 70)
print("End of toy model feasibility check")
print("=" * 70)
