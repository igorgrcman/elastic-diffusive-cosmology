#!/usr/bin/env python3
"""
Bath 2: Bulk Viscosity — CORRECTED CALCULATION (v2)

Addresses criticisms:
1. Explicit units discipline (natural units box)
2. O(1) coefficients made explicit
3. Proper dimensional analysis
4. Honest epistemic tagging

Working in natural units: hbar = c = 1
- [length] = 1/[energy]
- [time] = 1/[energy]
- [mass] = [energy]
- [frequency] = [energy]
- 1 fm = 1/(197.3 MeV)
"""

import numpy as np
import json

# =============================================================================
# UNITS BOX: Natural units (hbar = c = 1)
# =============================================================================

print("=" * 70)
print("UNITS BOX: Natural Units (hbar = c = 1)")
print("=" * 70)
print("""
Conversions:
  1 fm = 1/(197.3 MeV) = 5.07e-3 MeV^(-1)
  1 MeV = 197.3 fm^(-1)

Dimensions in natural units:
  [length] = [time] = 1/[energy]
  [mass] = [energy]
  [velocity] = dimensionless
  [acceleration] = [energy]^2
  [force] = [energy]^2

In Langevin equation: M q'' + gamma q' + V'(q) = xi(t)
  [M] = [energy]           (mass)
  [gamma] = [energy]^2     (friction coefficient)
  [V'] = [energy]^2        (force)
  [omega] = [energy]       (frequency)

Dimensionless damping: Upsilon = gamma / (M * omega_b)
""")

# =============================================================================
# CONSTANTS AND CONVERSIONS
# =============================================================================

hbar_c_MeV_fm = 197.327  # MeV * fm

def fm_to_invMeV(x_fm):
    """Convert fm to MeV^(-1)"""
    return x_fm / hbar_c_MeV_fm

def MeV_fm2_to_MeV3(sigma):
    """Convert MeV/fm^2 to MeV^3 (natural units)"""
    return sigma * hbar_c_MeV_fm**2

# =============================================================================
# INPUT PARAMETERS (from Route C / EDC)
# =============================================================================

print("\n" + "=" * 70)
print("INPUT PARAMETERS")
print("=" * 70)

# In conventional units
sigma_conv = 8.82  # MeV/fm^2 [Dc]
delta_conv = 0.105  # fm [I]
L0_conv = 1.0  # fm [I]
m_p = 938.272  # MeV [BL]
Delta_V = 1.293  # MeV [BL] = Delta m_np

print(f"\nConventional units:")
print(f"  sigma = {sigma_conv:.2f} MeV/fm^2  [Dc]")
print(f"  delta = {delta_conv:.3f} fm       [I]")
print(f"  L0    = {L0_conv:.1f} fm          [I]")
print(f"  m_p   = {m_p:.3f} MeV        [BL]")
print(f"  Delta_V = {Delta_V:.3f} MeV      [BL]")

# Convert to natural units
sigma_nat = MeV_fm2_to_MeV3(sigma_conv)  # MeV^3
delta_nat = fm_to_invMeV(delta_conv)  # MeV^(-1)
L0_nat = fm_to_invMeV(L0_conv)  # MeV^(-1)

print(f"\nNatural units (hbar=c=1):")
print(f"  sigma = {sigma_nat:.2e} MeV^3")
print(f"  delta = {delta_nat:.4e} MeV^(-1)")
print(f"  L0    = {L0_nat:.4e} MeV^(-1)")

# =============================================================================
# DERIVED QUANTITIES (with explicit O(1) coefficients)
# =============================================================================

print("\n" + "=" * 70)
print("DERIVED QUANTITIES (with O(1) coefficients)")
print("=" * 70)

# Barrier frequency
E0_MeV = sigma_conv * L0_conv**2  # MeV (junction energy scale)
omega_b = E0_MeV  # MeV (in natural units, frequency = energy)

print(f"\nBarrier frequency:")
print(f"  E0 = sigma * L0^2 = {E0_MeV:.2f} MeV")
print(f"  omega_b = E0 = {omega_b:.2f} MeV  [Dc]")

# Effective mass
M_eff = m_p  # MeV
print(f"\nEffective mass:")
print(f"  M_eff = m_p = {M_eff:.2f} MeV  [I]")

# =============================================================================
# VISCOSITY MODEL (with explicit coefficients) [P]
# =============================================================================

print("\n" + "=" * 70)
print("VISCOSITY MODEL [P] — Dimensional Analysis with O(1) Coefficients")
print("=" * 70)

print("""
Ansatz (Stokes-like for 5D extended object):

  rho_plenum = C_rho * sigma / delta        [P]
  eta = C_eta * rho * c * ell               [P]  (with ell = C_ell * delta)
  gamma = C_gamma * eta * L0                [P]

Combined: gamma = C * sigma * L0  (in appropriate units)
where C = C_gamma * C_eta * C_ell * C_rho is the combined O(1) factor.

This is DIMENSIONAL ANALYSIS, not derivation from 5D action.
Tag: [P] with O(1) uncertainty.
""")

# =============================================================================
# CALCULATION: gamma and Upsilon as function of C
# =============================================================================

print("\n" + "=" * 70)
print("CALCULATION: Upsilon(C)")
print("=" * 70)

# In natural units:
# gamma [MeV^2] = C * sigma [MeV^3] * L0 [MeV^(-1)] = C * sigma * L0 [MeV^2]
# Upsilon = gamma / (M_eff * omega_b) = (C * sigma * L0) / (m_p * omega_b)

gamma_over_C = sigma_nat * L0_nat  # MeV^2 / C
print(f"\ngamma/C = sigma_nat * L0_nat = {gamma_over_C:.2e} MeV^2")

Upsilon_over_C = gamma_over_C / (M_eff * omega_b)
print(f"Upsilon/C = gamma/(C * M_eff * omega_b) = {Upsilon_over_C:.4f}")

print(f"\n{'C':>6} | {'gamma (MeV^2)':>14} | {'Upsilon':>10} | {'Regime':>15}")
print("-" * 55)

C_values = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0]
results = []

for C in C_values:
    gamma = C * gamma_over_C
    Upsilon = C * Upsilon_over_C

    if Upsilon < 0.1:
        regime = "UNDERDAMPED"
    elif Upsilon > 10:
        regime = "OVERDAMPED"
    else:
        regime = "TURNOVER"

    print(f"{C:6.1f} | {gamma:14.2e} | {Upsilon:10.3f} | {regime:>15}")

    results.append({
        'C': C,
        'gamma_MeV2': gamma,
        'Upsilon': Upsilon,
        'regime': regime
    })

# =============================================================================
# KEY RESULT
# =============================================================================

print("\n" + "=" * 70)
print("KEY RESULT")
print("=" * 70)

C_for_turnover_low = 0.1 / Upsilon_over_C
C_for_turnover_high = 10.0 / Upsilon_over_C

print(f"""
Upsilon = {Upsilon_over_C:.4f} * C

TURNOVER REGIME (0.1 < Upsilon < 10) requires:
  {C_for_turnover_low:.1f} < C < {C_for_turnover_high:.1f}

For C = 1 (naive estimate):  Upsilon = {Upsilon_over_C:.3f}
For C = 5 (moderate):        Upsilon = {5*Upsilon_over_C:.3f}

CONCLUSION:
  - Dimensional analysis gives Upsilon ~ O(0.1 - 1) for C ~ O(1)
  - Turnover regime is NATURAL, not fine-tuned
  - But exact value depends on unknown O(1) coefficients
  - Tag: [P] with O(1) uncertainty, NOT [Dc]
""")

# =============================================================================
# LIFETIME ESTIMATE
# =============================================================================

print("\n" + "=" * 70)
print("LIFETIME ESTIMATE")
print("=" * 70)

# Kramers formula (simplified):
# tau ~ (2*pi/omega_n) * (1/Upsilon) * exp(Theta)
#
# In turnover regime, prefactor is O(1/omega_b)

hbar_MeV_s = 6.582e-22  # MeV * s

def tau_kramers(omega_b_MeV, Upsilon, Theta):
    """Kramers escape time in seconds"""
    prefactor = 2 * np.pi * hbar_MeV_s / omega_b_MeV  # seconds
    return prefactor * (1/Upsilon) * np.exp(Theta)

print(f"\nKramers formula: tau ~ (2*pi*hbar/omega_b) * (1/Upsilon) * exp(Theta)")
print(f"\nWith omega_b = {omega_b:.2f} MeV:")
print(f"  Prefactor = 2*pi*hbar/omega_b = {2*np.pi*hbar_MeV_s/omega_b:.2e} s")

print(f"\n{'Theta':>6} | {'Upsilon':>8} | {'tau (s)':>12} | {'tau_exp':>10}")
print("-" * 50)

Theta_values = [50, 55, 60]
Upsilon_values = [0.2, 1.0, 5.0]

for Theta in Theta_values:
    for Ups in Upsilon_values:
        tau = tau_kramers(omega_b, Ups, Theta)
        ratio = tau / 879  # ratio to experimental
        print(f"{Theta:6d} | {Ups:8.1f} | {tau:12.1e} | {ratio:10.2f}x")

# =============================================================================
# WHAT IS ACTUALLY DERIVED vs ASSUMED
# =============================================================================

print("\n" + "=" * 70)
print("EPISTEMIC STATUS: What is [Dc] vs [P] vs [OPEN]")
print("=" * 70)

print("""
[Dc] DERIVED:
  - omega_b = sigma * L0^2 = 8.82 MeV (from Route C parameters)
  - Dimensional scaling: gamma ~ sigma * L0 (dimensionally correct)
  - Upsilon ~ O(0.1-1) for O(1) coefficients (dimensional analysis)

[P] PROPOSED (ansatz):
  - rho_plenum = C_rho * sigma / delta
  - eta = C_eta * rho * c * delta
  - gamma = C_gamma * eta * L0
  - Combined coefficient C = C_gamma * C_eta * C_ell * C_rho ~ O(1)

[OPEN] NOT PROVEN:
  - Actual value of C (requires 5D linear response calculation)
  - Whether Stokes-like drag applies to 5D extended object
  - Bath 2 noise suppression on brane (FDT issue!)
  - Projection factor for bulk fluctuations onto q

[Cal] WOULD BE CALIBRATION:
  - Choosing C to match tau = 879 s
  - Choosing Theta to match tau = 879 s
""")

# =============================================================================
# HONEST VERDICT
# =============================================================================

print("\n" + "=" * 70)
print("HONEST VERDICT")
print("=" * 70)

print("""
TWO-CHANNEL MODEL STATUS:

1. Bath 4 (noise): Multipole screening CAN give Theta ~ 55 [Dc]
   - But m value (integer vs fractional) is [P] without geometric derivation

2. Bath 2 (damping): Dimensional analysis gives Upsilon ~ O(0.1-1) [P]
   - NOT "parameter-free" — hidden O(1) coefficients
   - NOT derived from 5D action — just dimensional estimate

3. Bulk noise suppression: UNPROVEN [OPEN]
   - Cannot claim "Bath 2 gives damping but no noise" without calculation
   - This is the critical gap in the two-channel argument

CORRECT VERDICT:
  "Route F: Two-channel CANDIDATE — Upsilon ~ O(1) is PLAUSIBLE
   from dimensional analysis, but bulk noise projection remains OPEN."

NOT:
  "Route F: CLOSED — tau = 879 s derived"
""")

# =============================================================================
# SAVE RESULTS
# =============================================================================

output = {
    'parameters': {
        'sigma_MeV_fm2': sigma_conv,
        'delta_fm': delta_conv,
        'L0_fm': L0_conv,
        'm_p_MeV': m_p,
        'Delta_V_MeV': Delta_V
    },
    'natural_units': {
        'sigma_MeV3': sigma_nat,
        'delta_invMeV': delta_nat,
        'L0_invMeV': L0_nat
    },
    'derived': {
        'omega_b_MeV': omega_b,
        'gamma_over_C_MeV2': gamma_over_C,
        'Upsilon_over_C': Upsilon_over_C
    },
    'scan': results,
    'turnover_range': {
        'C_min': C_for_turnover_low,
        'C_max': C_for_turnover_high
    },
    'epistemic': {
        'Upsilon_O1': '[P] - dimensional analysis with O(1) uncertainty',
        'bulk_noise': '[OPEN] - not proven',
        'verdict': 'CANDIDATE, not CLOSED'
    }
}

output_file = '/Users/igor/ClaudeAI/EDC_Project/elastic-diffusive-cosmology_repo/edc_book_2/src/derivations/artifacts/bath2_viscosity_v2.json'
with open(output_file, 'w') as f:
    json.dump(output, f, indent=2)

print(f"\nResults saved to: {output_file}")
