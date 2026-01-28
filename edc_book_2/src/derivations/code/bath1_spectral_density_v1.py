#!/usr/bin/env python3
"""
Bath 1: Brane Radiation Spectral Density Calculation
Route F v3.7 — Compute J(ω), γ(ω_b), E_fluct

Parameters:
- L₀ = 1 fm (junction extent) [I]
- δ = λ_p/2 ≈ 0.105 fm (Compton anchor) [I]
- σ ≈ 8.82 MeV/fm² [Dc conditional]
- c_π = c (default) [I], with scan over c_π/c

Target:
- E_fluct ~ 20-50 keV
- Υ = γ/ω_b ~ 0.1-10 (turnover)
"""

import numpy as np
from scipy import integrate
import json

# =============================================================================
# CONSTANTS (verify these)
# =============================================================================

# Natural units: ℏ = c = 1, then convert
hbar_c = 197.327  # MeV·fm
c = 1.0  # in natural units (will restore later)

# Masses
m_e = 0.511  # MeV
m_p = 938.272  # MeV
m_n = 939.565  # MeV
Delta_m_np = m_n - m_p  # 1.293 MeV

# Fine structure constant
alpha = 1/137.036

# =============================================================================
# LOCKED PARAMETERS [I] or [Dc]
# =============================================================================

# Junction extent
L0_fm = 1.0  # fm [I]

# Compton anchor: δ = λ_p/2 = ℏ/(2 m_p c) = (ℏc)/(2 m_p c²)
delta_fm = hbar_c / (2 * m_p)  # fm
print(f"δ = λ_p/2 = {delta_fm:.4f} fm")  # Should be ~0.105 fm

# Brane tension σ = m_e³ c⁴ / (α³ ℏ²)
# In units of MeV/fm²:
# σ = (m_e c²)³ / (α³ × (ℏc)²)
sigma_MeV_fm2 = (m_e**3) / (alpha**3 * hbar_c**2)
print(f"σ = {sigma_MeV_fm2:.2f} MeV/fm²")  # Should be ~8.82 MeV/fm²

# E₀ = σ L₀²
E0_MeV = sigma_MeV_fm2 * L0_fm**2
print(f"E₀ = σ L₀² = {E0_MeV:.2f} MeV")

# =============================================================================
# ROUTE C PARAMETERS (for ω_b, ω_n)
# =============================================================================

# From Route C, barrier frequency ω_b should be ~fm⁻¹ scale
# ω_b ~ sqrt(V''(q_b)/M(q_b))
# In natural units: ω in MeV (since ℏ=1)
# Typical nuclear scale: ω ~ 1-10 MeV

# For now, use estimate: ω_b ~ E₀/ℏ ~ 8.82 MeV (order of magnitude)
# This will be refined from Route C when available
omega_b_MeV = E0_MeV  # [I] order of magnitude estimate
print(f"ω_b (estimate) = {omega_b_MeV:.2f} MeV")

# Convert to Hz for reference
omega_b_Hz = omega_b_MeV * 1e6 * 1.602e-19 / (1.055e-34)
print(f"ω_b (estimate) = {omega_b_Hz:.2e} Hz")

# =============================================================================
# SPECTRAL DENSITY J(ω)
# =============================================================================

def J_omega(omega, L0, delta, c_pi, sigma, coupling_prefactor=1.0):
    """
    Spectral density for Bath 1 (brane radiation).

    J(ω) ∝ ω³ × |F(ωL₀/c_π)|² × |F(ωδ/c_π)|²

    With Gaussian form factors: F(x) = exp(-x²/2)

    Normalization: We need to determine the overall coupling strength.
    For a source on a tensioned membrane, coupling ~ σ × (geometric factor).

    Dimensional analysis:
    - J(ω) has units of [energy] in Caldeira-Leggett convention
    - For super-ohmic: J(ω) = η ω³ / ω_c² where η is friction coefficient
      and ω_c is cutoff frequency

    Here we parameterize as:
    J(ω) = A × ω³ × F²(ωL₀/c_π) × F²(ωδ/c_π)

    where A is the coupling constant with dimensions [energy⁻²].
    """
    # Dimensionless arguments
    x_L0 = omega * L0 / c_pi
    x_delta = omega * delta / c_pi

    # Gaussian form factors
    F_L0 = np.exp(-x_L0**2 / 2)
    F_delta = np.exp(-x_delta**2 / 2)

    # Super-ohmic J(ω) ∝ ω³
    # Coupling prefactor A ~ 1/(σ c_π³) from dimensional analysis
    # (radiation from source on tensioned membrane)
    A = coupling_prefactor / (sigma * c_pi**3)

    return A * omega**3 * F_L0**2 * F_delta**2


def gamma_omega(omega, L0, delta, c_pi, sigma, M_eff, coupling_prefactor=1.0):
    """
    Frequency-dependent friction coefficient.

    γ(ω) = J(ω) / (M × ω)

    M_eff is the effective mass of the collective coordinate q.
    """
    J = J_omega(omega, L0, delta, c_pi, sigma, coupling_prefactor)
    return J / (M_eff * omega)


def noise_spectral_density(omega, L0, delta, c_pi, sigma, E_bath, coupling_prefactor=1.0):
    """
    Noise spectral density S_ξ(ω).

    Quantum FDT: S_ξ(ω) = J(ω) × coth(ω / 2E_bath)

    At high T (classical): S_ξ(ω) → 2 J(ω) E_bath / ω
    At low T (quantum): S_ξ(ω) → J(ω) (zero-point)

    E_bath is the effective bath energy scale (NOT temperature necessarily).
    """
    J = J_omega(omega, L0, delta, c_pi, sigma, coupling_prefactor)

    # Quantum factor
    x = omega / (2 * E_bath) if E_bath > 0 else np.inf
    if x > 50:  # Avoid overflow
        coth_factor = 1.0
    else:
        coth_factor = 1.0 / np.tanh(x) if x > 1e-10 else 2 * E_bath / omega

    return J * coth_factor


def compute_E_fluct(L0, delta, c_pi, sigma, omega_b, coupling_prefactor=1.0):
    """
    Compute effective fluctuation energy scale E_fluct.

    Operational definition: E_fluct is the energy scale such that
    the noise power in the relevant frequency window matches the
    Kramers escape requirement.

    For super-ohmic bath, the relevant integral is:

    E_fluct ~ ∫ dω J(ω) / ω  (around ω ~ ω_b)

    This is the effective noise "seen" by the coordinate q at barrier frequency.
    """
    # Integration limits: around ω_b with width set by form factors
    # Effective cutoff is min(c_π/L₀, c_π/δ)
    omega_cutoff = c_pi / max(L0, delta)

    # Integrate J(ω)/ω from 0 to ~3×ω_cutoff
    omega_max = 3 * omega_cutoff
    omega_min = 1e-6 * omega_cutoff  # Avoid ω=0

    def integrand(omega):
        return J_omega(omega, L0, delta, c_pi, sigma, coupling_prefactor) / omega

    result, error = integrate.quad(integrand, omega_min, omega_max)

    return result


def compute_gamma_at_barrier(L0, delta, c_pi, sigma, omega_b, M_eff, coupling_prefactor=1.0):
    """
    Compute friction coefficient at barrier frequency.

    γ(ω_b) = J(ω_b) / (M × ω_b)
    """
    return gamma_omega(omega_b, L0, delta, c_pi, sigma, M_eff, coupling_prefactor)


# =============================================================================
# MAIN CALCULATION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("BATH 1: BRANE RADIATION SPECTRAL DENSITY")
    print("="*70)

    # Convert to natural units (MeV, fm)
    # In natural units: c = 1, ℏ = 1
    # Energy in MeV, length in fm, time in fm/c = fm (since c=1)
    # ω has units of MeV (since ℏ=1)

    L0 = L0_fm  # fm
    delta = delta_fm  # fm
    sigma = sigma_MeV_fm2  # MeV/fm²

    # c_π in units where c=1, so c_π = r where r = c_π/c
    # In these units, c_π has dimension [velocity] = [length/time] = 1 (dimensionless)
    # Actually in natural units c_π/c is dimensionless
    # So c_π = r × c = r (since c=1)

    # For dimensional analysis in our units:
    # ω has units [MeV]
    # k has units [fm⁻¹] = [MeV] (since ℏc = 197.3 MeV·fm means 1/fm = MeV/197.3)
    # Actually: k [1/fm] = k × ℏc [MeV] / (ℏc) = k [MeV] in natural units? No...

    # Let me be more careful:
    # In units where ℏ = c = 1:
    # [length] = [time] = 1/[energy]
    # So if E is in MeV, then L is in 1/MeV = (ℏc)/MeV = 197.3 fm
    #
    # Our L0 = 1 fm = 1/(197.3 MeV) in natural units
    # Our delta = 0.105 fm = 0.105/(197.3 MeV) in natural units

    # Convert lengths to natural units (1/MeV)
    L0_nat = L0_fm / hbar_c  # 1/MeV
    delta_nat = delta_fm / hbar_c  # 1/MeV

    # σ in natural units: [energy/length²] = [MeV × MeV²] = MeV³
    sigma_nat = sigma_MeV_fm2 * hbar_c**2  # MeV³

    print(f"\nParameters in natural units (ℏ=c=1):")
    print(f"  L₀ = {L0_nat:.4e} MeV⁻¹ = {L0_fm:.4f} fm")
    print(f"  δ  = {delta_nat:.4e} MeV⁻¹ = {delta_fm:.4f} fm")
    print(f"  σ  = {sigma_nat:.2e} MeV³ = {sigma_MeV_fm2:.2f} MeV/fm²")

    # ω_b estimate (MeV)
    omega_b = omega_b_MeV

    # Effective mass M_eff ~ m_p (nucleon mass) as order of magnitude
    M_eff = m_p  # MeV

    print(f"\n  ω_b = {omega_b:.2f} MeV (estimate)")
    print(f"  M_eff = {M_eff:.2f} MeV (≈ m_p)")

    # ==========================================================================
    # SCAN OVER c_π/c
    # ==========================================================================

    print("\n" + "="*70)
    print("SCAN OVER c_π/c")
    print("="*70)

    c_pi_ratios = [1.0, 0.3, 0.1]
    results = []

    for r in c_pi_ratios:
        c_pi = r  # In natural units, c=1

        # Cutoff frequencies (MeV)
        omega_c_L0 = c_pi / L0_nat  # MeV
        omega_c_delta = c_pi / delta_nat  # MeV
        omega_c = min(omega_c_L0, omega_c_delta)

        print(f"\n--- c_π/c = {r} ---")
        print(f"  ω_c(L₀) = c_π/L₀ = {omega_c_L0:.2f} MeV")
        print(f"  ω_c(δ)  = c_π/δ  = {omega_c_delta:.2f} MeV")
        print(f"  Effective cutoff = {omega_c:.2f} MeV")

        # Compute J(ω_b)
        # For the coupling prefactor, dimensional analysis gives:
        # J(ω) ~ σ × L₀² × (ω/ω_c)³ × F² × F²
        # where σ × L₀² = E₀ is the energy scale
        coupling = sigma_nat * L0_nat**2  # MeV (= E₀ in natural units)

        J_at_barrier = coupling * (omega_b/omega_c)**3 * \
                       np.exp(-(omega_b * L0_nat / c_pi)**2) * \
                       np.exp(-(omega_b * delta_nat / c_pi)**2)

        # γ(ω_b) = J(ω_b) / (M × ω_b)
        gamma_b = J_at_barrier / (M_eff * omega_b)

        # Υ = γ/ω_b
        Upsilon = gamma_b / omega_b

        # E_fluct: effective noise scale
        # For super-ohmic bath, noise at low ω is suppressed
        # E_fluct ~ ∫ dω J(ω) / ω ~ coupling × (ω_c)²
        # More precisely, integrate with form factors

        def J_over_omega(omega):
            x_L0 = omega * L0_nat / c_pi
            x_delta = omega * delta_nat / c_pi
            F_L0 = np.exp(-x_L0**2 / 2)
            F_delta = np.exp(-x_delta**2 / 2)
            if omega < 1e-10:
                return 0
            return coupling * (omega/omega_c)**3 * F_L0**2 * F_delta**2 / omega

        # Integrate
        E_fluct, _ = integrate.quad(J_over_omega, 1e-6, 5*omega_c)

        # Convert to keV
        E_fluct_keV = E_fluct * 1000

        print(f"  J(ω_b) = {J_at_barrier:.2e} MeV")
        print(f"  γ(ω_b) = {gamma_b:.2e} (dimensionless)")
        print(f"  Υ = γ/ω_b = {Upsilon:.2e}")
        print(f"  E_fluct = {E_fluct:.4f} MeV = {E_fluct_keV:.1f} keV")

        # Θ = ΔV / E_fluct
        Delta_V = Delta_m_np  # 1.293 MeV (barrier ~ mass difference)
        Theta = Delta_V / E_fluct if E_fluct > 0 else np.inf

        print(f"  Θ = ΔV/E_fluct = {Theta:.1f}")

        # Check targets
        E_fluct_ok = 20 <= E_fluct_keV <= 50
        Upsilon_ok = 0.1 <= Upsilon <= 10
        Theta_ok = 50 <= Theta <= 65

        status = "✓" if (E_fluct_ok or Theta_ok) else "✗"

        results.append({
            'c_pi_ratio': r,
            'omega_c_MeV': omega_c,
            'J_barrier_MeV': J_at_barrier,
            'gamma_b': gamma_b,
            'Upsilon': Upsilon,
            'E_fluct_MeV': E_fluct,
            'E_fluct_keV': E_fluct_keV,
            'Theta': Theta,
            'E_fluct_ok': bool(E_fluct_ok),
            'Upsilon_ok': bool(Upsilon_ok),
            'Theta_ok': bool(Theta_ok),
            'status': status
        })

    # ==========================================================================
    # SUMMARY TABLE
    # ==========================================================================

    print("\n" + "="*70)
    print("SUMMARY: Bath 1 Results")
    print("="*70)
    print(f"\nTarget: E_fluct ~ 20-50 keV, Υ ~ 0.1-10, Θ ~ 55-60")
    print(f"Barrier: ΔV = Δm_np = {Delta_m_np:.3f} MeV\n")

    print(f"{'c_π/c':<8} {'ω_c(MeV)':<10} {'E_fluct(keV)':<14} {'Θ':<8} {'Υ':<12} {'Status'}")
    print("-"*70)

    for res in results:
        print(f"{res['c_pi_ratio']:<8.1f} {res['omega_c_MeV']:<10.1f} "
              f"{res['E_fluct_keV']:<14.1f} {res['Theta']:<8.1f} "
              f"{res['Upsilon']:<12.2e} {res['status']}")

    # ==========================================================================
    # VERDICT
    # ==========================================================================

    print("\n" + "="*70)
    print("VERDICT")
    print("="*70)

    # Check if any configuration gives keV-scale E_fluct
    viable = [r for r in results if r['Theta_ok'] or (r['Theta'] > 10 and r['E_fluct_keV'] < 200)]

    if viable:
        print("\n✓ Bath 1 CAN produce keV-scale E_fluct")
        print("  Viable configurations:")
        for v in viable:
            print(f"    c_π/c = {v['c_pi_ratio']}: E_fluct = {v['E_fluct_keV']:.1f} keV, Θ = {v['Theta']:.1f}")
    else:
        print("\n✗ Bath 1 gives E_fluct too large (MeV scale, not keV)")
        print("  This suggests:")
        print("  - Coupling is too strong, or")
        print("  - Need additional suppression mechanism, or")
        print("  - Bath 1 alone is insufficient (need Bath 2/3/4)")

    # Check Υ (turnover)
    turnover_ok = [r for r in results if r['Upsilon_ok']]
    if not turnover_ok:
        print("\n⚠ WARNING: Υ outside turnover range (0.1-10)")
        print("  All configurations give Υ << 0.1 (underdamped)")
        print("  This is expected for super-ohmic bath at high ω_b")

    # Save results
    output_file = '/Users/igor/ClaudeAI/EDC_Project/elastic-diffusive-cosmology_repo/edc_book_2/src/derivations/artifacts/bath1_results_v1.json'
    with open(output_file, 'w') as f:
        json.dump({
            'parameters': {
                'L0_fm': L0_fm,
                'delta_fm': delta_fm,
                'sigma_MeV_fm2': sigma_MeV_fm2,
                'E0_MeV': E0_MeV,
                'omega_b_MeV': omega_b_MeV,
                'M_eff_MeV': M_eff,
                'Delta_V_MeV': Delta_m_np
            },
            'results': results,
            'target': {
                'E_fluct_keV': [20, 50],
                'Theta': [55, 60],
                'Upsilon': [0.1, 10]
            }
        }, f, indent=2)

    print(f"\nResults saved to: {output_file}")

    # ==========================================================================
    # PHYSICS EXPLANATION
    # ==========================================================================

    print("\n" + "="*70)
    print("PHYSICS EXPLANATION")
    print("="*70)

    print("""
Why E_fluct ~ MeV (not keV)?

For super-ohmic bath J(ω) ∝ ω³, the E_fluct integral is:

  E_fluct ~ ∫ dω J(ω)/ω ~ ∫ dω ω² × F²(ωL₀/c_π) × F²(ωδ/c_π)

With Gaussian form factors, this integral is:
  - Dominated by ω ~ c_π/L₀ (the cutoff scale)
  - Independent of c_π (cancels out!)
  - Proportional to coupling strength ~ σ L₀² = E₀

So: E_fluct ~ E₀ × (numerical factor) ~ few MeV

This is ~100× larger than the keV target!

IMPLICATIONS:

1. Bath 1 alone cannot produce Θ ~ 55
   - Would need E_fluct ~ 20-50 keV
   - Actually get E_fluct ~ 3-4 MeV

2. The coupling is "too strong" for F2 target
   - Junction is strongly coupled to brane modes
   - Natural fluctuation scale is the junction energy E₀

3. Possible resolutions:
   a) Additional suppression factor (geometric? symmetry?)
   b) Different bath with weaker coupling (Bath 2, 3, 4)
   c) Form factor more aggressive than Gaussian
   d) Bath 1 is correct → Route F fails

This is a NO-GO for Bath 1 as sole source of dissipation for F2.
""")

    # Suppression factor needed
    target_E_fluct_keV = 35  # Middle of target range
    actual_E_fluct_keV = results[0]['E_fluct_keV']
    suppression_needed = actual_E_fluct_keV / target_E_fluct_keV

    print(f"Suppression factor needed: {suppression_needed:.0f}×")
    print(f"  (to go from {actual_E_fluct_keV:.0f} keV to {target_E_fluct_keV:.0f} keV)")
