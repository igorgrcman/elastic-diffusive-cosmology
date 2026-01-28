#!/usr/bin/env python3
"""
Bath 4: Rξ Screening via Multipole Suppression
Route F v3.8 — Test symmetry-forbidden leading coupling

Key idea:
- Instead of monopole coupling q·π, use derivative coupling q·∇^m π
- This gives form factor ~ (kRξ)^m in Fourier space
- At k ~ 1/L₀, suppression factor ~ (Rξ/L₀)^(2m)
- For Rξ ~ 0.002 fm, L₀ ~ 1 fm, m=1: (0.002)^2 ~ 4×10⁻⁶

WARNING (from Igor):
- Bath 4 can suppress E_fluct (good for Θ)
- But same suppression will kill γ (bad for Υ)
- Unless damping comes from separate channel (Bath 2: bulk wake)

Target: E_fluct suppression ≥ 110× (from 3844 keV to ~35 keV)
"""

import numpy as np
from scipy import integrate
import json

# =============================================================================
# CONSTANTS
# =============================================================================

hbar_c = 197.327  # MeV·fm
m_e = 0.511  # MeV
m_p = 938.272  # MeV
m_n = 939.565  # MeV
Delta_m_np = m_n - m_p  # 1.293 MeV
alpha = 1/137.036

# =============================================================================
# LOCKED PARAMETERS
# =============================================================================

L0_fm = 1.0  # fm - junction extent
delta_fm = hbar_c / (2 * m_p)  # 0.105 fm - Compton anchor
sigma_MeV_fm2 = (m_e**3) / (alpha**3 * hbar_c**2)  # 8.82 MeV/fm²
E0_MeV = sigma_MeV_fm2 * L0_fm**2  # 8.82 MeV

# EW scale (Rξ)
# From EDC: Rξ ~ α × λ_e / (2π) or similar
# For this test, use Rξ ~ 0.002 fm (electroweak scale)
R_xi_fm = 0.002  # fm [I] - to be derived properly

# Convert to natural units
L0_nat = L0_fm / hbar_c  # MeV⁻¹
delta_nat = delta_fm / hbar_c  # MeV⁻¹
R_xi_nat = R_xi_fm / hbar_c  # MeV⁻¹
sigma_nat = sigma_MeV_fm2 * hbar_c**2  # MeV³

# Barrier frequency estimate
omega_b_MeV = E0_MeV

print("="*70)
print("BATH 4: Rξ SCREENING VIA MULTIPOLE SUPPRESSION")
print("="*70)

print(f"\nParameters:")
print(f"  L₀ = {L0_fm:.4f} fm")
print(f"  δ  = {delta_fm:.4f} fm")
print(f"  Rξ = {R_xi_fm:.4f} fm")
print(f"  σ  = {sigma_MeV_fm2:.2f} MeV/fm²")
print(f"  E₀ = {E0_MeV:.2f} MeV")

print(f"\nScale ratios:")
print(f"  Rξ/L₀ = {R_xi_fm/L0_fm:.4f}")
print(f"  (Rξ/L₀)² = {(R_xi_fm/L0_fm)**2:.2e}")
print(f"  (Rξ/L₀)⁴ = {(R_xi_fm/L0_fm)**4:.2e}")

# =============================================================================
# BATH 4: MULTIPOLE SCREENING
# =============================================================================

def J_omega_bath4(omega, L0, delta, R_xi, c_pi, sigma, m_multipole):
    """
    Spectral density with multipole screening.

    J(ω) ∝ ω³ × (ωRξ/c_π)^(2m) × F²(ωL₀/c_π) × F²(ωδ/c_π)

    The (ωRξ/c_π)^(2m) factor comes from derivative coupling.
    For m=1: dipole-like coupling (monopole forbidden by symmetry)
    For m=2: quadrupole-like
    """
    # Dimensionless arguments
    x_L0 = omega * L0 / c_pi
    x_delta = omega * delta / c_pi
    x_Rxi = omega * R_xi / c_pi

    # Gaussian form factors
    F_L0 = np.exp(-x_L0**2 / 2)
    F_delta = np.exp(-x_delta**2 / 2)

    # Multipole screening factor
    screening = x_Rxi**(2 * m_multipole)

    # Coupling prefactor
    coupling = sigma * L0**2  # E₀

    # Cutoff scale for normalization
    omega_c = c_pi / L0

    return coupling * (omega/omega_c)**3 * screening * F_L0**2 * F_delta**2


def compute_E_fluct_bath4(L0, delta, R_xi, c_pi, sigma, m_multipole):
    """
    Compute E_fluct with multipole screening.
    """
    omega_c = c_pi / L0

    def integrand(omega):
        if omega < 1e-10:
            return 0
        J = J_omega_bath4(omega, L0, delta, R_xi, c_pi, sigma, m_multipole)
        return J / omega

    result, error = integrate.quad(integrand, 1e-6 * omega_c, 5 * omega_c)
    return result


# =============================================================================
# MAIN CALCULATION
# =============================================================================

if __name__ == "__main__":

    c_pi = 1.0  # c_π/c = 1 (default)

    print("\n" + "="*70)
    print("SCAN OVER MULTIPOLE ORDER m")
    print("="*70)

    # Bath 1 reference (m=0, no screening)
    E_fluct_bath1 = compute_E_fluct_bath4(L0_nat, delta_nat, R_xi_nat, c_pi, sigma_nat, m_multipole=0)
    E_fluct_bath1_keV = E_fluct_bath1 * 1000

    print(f"\nReference (Bath 1, m=0): E_fluct = {E_fluct_bath1_keV:.1f} keV")

    results = []
    m_values = [0, 1, 2, 3, 4]

    for m in m_values:
        E_fluct = compute_E_fluct_bath4(L0_nat, delta_nat, R_xi_nat, c_pi, sigma_nat, m_multipole=m)
        E_fluct_keV = E_fluct * 1000

        # Suppression factor relative to m=0
        suppression = E_fluct_bath1 / E_fluct if E_fluct > 0 else np.inf

        # Θ = ΔV / E_fluct
        Theta = Delta_m_np / E_fluct if E_fluct > 0 else np.inf

        # Expected suppression from scale ratio
        expected_suppression = (L0_fm / R_xi_fm)**(2 * m) if m > 0 else 1

        # Check if target achieved
        target_Theta = 55
        ok = Theta >= target_Theta * 0.8  # Within 20% of target
        status = "✓" if ok else "✗"

        print(f"\nm = {m}:")
        print(f"  E_fluct = {E_fluct_keV:.2e} keV")
        print(f"  Suppression = {suppression:.2e}× (expected: {expected_suppression:.2e}×)")
        print(f"  Θ = {Theta:.1f} (target: ~55)")
        print(f"  Status: {status}")

        results.append({
            'm_multipole': m,
            'E_fluct_keV': E_fluct_keV,
            'suppression': suppression,
            'expected_suppression': expected_suppression,
            'Theta': Theta,
            'ok': bool(ok),
            'status': status
        })

    # ==========================================================================
    # SUMMARY
    # ==========================================================================

    print("\n" + "="*70)
    print("SUMMARY: Bath 4 Multipole Screening")
    print("="*70)

    print(f"\nTarget: Θ ~ 55 (E_fluct ~ 24 keV)")
    print(f"Bath 1 baseline: E_fluct = {E_fluct_bath1_keV:.1f} keV, Θ = {Delta_m_np/E_fluct_bath1:.2f}")
    print(f"\nRξ/L₀ = {R_xi_fm/L0_fm:.4f}")

    print(f"\n{'m':<4} {'E_fluct(keV)':<14} {'Suppress':<12} {'Θ':<10} {'Status'}")
    print("-"*50)

    for res in results:
        print(f"{res['m_multipole']:<4} {res['E_fluct_keV']:<14.2e} "
              f"{res['suppression']:<12.2e} {res['Theta']:<10.1f} {res['status']}")

    # ==========================================================================
    # VERDICT
    # ==========================================================================

    print("\n" + "="*70)
    print("VERDICT")
    print("="*70)

    # Find minimum m that achieves target
    viable = [r for r in results if r['Theta'] >= 50]

    if viable:
        best = min(viable, key=lambda x: x['m_multipole'])
        print(f"\n✓ Bath 4 CAN achieve Θ ~ 55 with m = {best['m_multipole']}")
        print(f"  E_fluct = {best['E_fluct_keV']:.2e} keV")
        print(f"  Suppression factor = {best['suppression']:.2e}×")
    else:
        print(f"\n✗ Bath 4 cannot achieve Θ ~ 55 with tested m values")
        print(f"  Need higher m or different Rξ")

    # WARNING about Υ
    print("\n" + "="*70)
    print("⚠️  CRITICAL WARNING: DAMPING")
    print("="*70)
    print("""
Bath 4 suppresses BOTH noise AND damping via the same factor.

If Bath 1 gave:
  Υ = γ/ω_b ~ 10⁻⁸ (already catastrophically underdamped)

Then Bath 4 with suppression S will give:
  Υ_new = Υ_old / S ~ 10⁻⁸ / S

For S ~ 10⁶ (m=1): Υ_new ~ 10⁻¹⁴ (even worse!)

CONCLUSION:
  Bath 4 can fix Θ (noise), but DESTROYS Υ (damping).

  To make Route F work, need TWO-CHANNEL approach:
  - Noise: Bath 4 (screened brane) → Θ ~ 55 ✓
  - Damping: Bath 2 (bulk wake) → Υ ~ 1 ✓

  This requires showing that bulk wake provides γ ~ ω_b
  without contributing significant noise to q.
""")

    # ==========================================================================
    # SAVE RESULTS
    # ==========================================================================

    output = {
        'parameters': {
            'L0_fm': L0_fm,
            'delta_fm': delta_fm,
            'R_xi_fm': R_xi_fm,
            'sigma_MeV_fm2': sigma_MeV_fm2,
            'E0_MeV': E0_MeV,
            'c_pi_ratio': c_pi
        },
        'results': results,
        'warning': 'Bath 4 suppresses both noise AND damping. Need two-channel approach.'
    }

    output_file = '/Users/igor/ClaudeAI/EDC_Project/elastic-diffusive-cosmology_repo/edc_book_2/src/derivations/artifacts/bath4_results_v1.json'
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\nResults saved to: {output_file}")
