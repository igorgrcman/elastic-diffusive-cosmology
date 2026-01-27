#!/usr/bin/env python3
"""
Δm_np OPTIONS + V_B PIPELINE CALCULATIONS
==========================================

This script computes all options for the neutron-proton mass difference
and the derived barrier height V_B in the Z₃ framework.

Epistemic Status:
- Option B (PDG): [BL] Baseline
- Option A (Book formula): [Dc] Conditionally derived
- V_B = 2 × Δm_np: [Dc] Z₃ barrier conjecture

Date: 2026-01-27
"""

import math

# =============================================================================
# BASELINE VALUES [BL] — from PDG/CODATA
# =============================================================================

m_e_MeV = 0.51099895  # Electron mass in MeV [BL] PDG 2022
alpha = 1.0 / 137.035999084  # Fine structure constant [BL] CODATA 2018
Delta_m_np_PDG = 1.29333236  # (m_n - m_p) in MeV [BL] PDG 2022

# V_B calibrated value from WKB model (current repo value)
V_B_cal = 2.6  # MeV [Cal] from WKB fit to τ_n ≈ 879 s

# =============================================================================
# OPTION CALCULATIONS
# =============================================================================

print("=" * 70)
print("Δm_np OPTIONS + V_B PIPELINE CALCULATIONS")
print("=" * 70)
print()

# --- OPTION B: PDG Baseline ---
Delta_m_B = Delta_m_np_PDG
print("OPTION B: PDG Baseline [BL]")
print(f"  Δm_np^(B) = {Delta_m_B:.6f} MeV")
print()

# --- OPTION A: Book formula (5/2 + 4α) m_e ---
coeff_geom = 5.0 / 2.0  # Geometric factor D_bulk/D_membrane
coeff_em = 4.0 * alpha  # EM correction from Dirac structure
coeff_total = coeff_geom + coeff_em

Delta_m_A = coeff_total * m_e_MeV
error_A_vs_PDG = abs(Delta_m_A - Delta_m_np_PDG) / Delta_m_np_PDG * 100

print("OPTION A: Book formula [Dc]")
print(f"  Δm_np^(A) = (5/2 + 4α) m_e")
print(f"  Coefficient = 5/2 + 4α = {coeff_geom:.4f} + {coeff_em:.6f} = {coeff_total:.6f}")
print(f"  Δm_np^(A) = {coeff_total:.6f} × {m_e_MeV:.6f} MeV = {Delta_m_A:.6f} MeV")
print(f"  Error vs PDG: {error_A_vs_PDG:.3f}%")
print()

# --- OPTION A1: Geometric only (5/2) m_e ---
Delta_m_A1 = coeff_geom * m_e_MeV
error_A1_vs_PDG = abs(Delta_m_A1 - Delta_m_np_PDG) / Delta_m_np_PDG * 100

print("OPTION A1: Geometric only [Dc]")
print(f"  Δm_np^(A1) = (5/2) m_e = {coeff_geom:.4f} × {m_e_MeV:.6f} MeV = {Delta_m_A1:.6f} MeV")
print(f"  Error vs PDG: {error_A1_vs_PDG:.3f}%")
print()

# --- OPTION A2: EM correction only ---
Delta_em = coeff_em * m_e_MeV

print("OPTION A2: EM correction component")
print(f"  Δ(EM) = 4α m_e = {coeff_em:.6f} × {m_e_MeV:.6f} MeV = {Delta_em:.6f} MeV")
print(f"  This is {Delta_em/Delta_m_np_PDG*100:.2f}% of the total mass difference")
print()

# --- WRONG FORMULA (for reference, to be removed) ---
wrong_coeff = 8.0 / math.pi
Delta_m_wrong = wrong_coeff * m_e_MeV
error_wrong_vs_PDG = abs(Delta_m_wrong - Delta_m_np_PDG) / Delta_m_np_PDG * 100

print("WRONG FORMULA (to be removed from repo):")
print(f"  Δm_np = 8 m_e / π = {wrong_coeff:.6f} × {m_e_MeV:.6f} MeV = {Delta_m_wrong:.6f} MeV")
print(f"  Error vs PDG: {error_wrong_vs_PDG:.3f}%")
print(f"  NOTE: This formula is NOT in codebase and was incorrectly introduced.")
print()

# =============================================================================
# V_B CALCULATIONS (Z₃ barrier conjecture: V_B = 2 × Δm_np)
# =============================================================================

print("=" * 70)
print("V_B = 2 × Δm_np (Z₃ BARRIER CONJECTURE) [Dc]")
print("=" * 70)
print()

V_B_optB = 2.0 * Delta_m_B
V_B_optA = 2.0 * Delta_m_A

error_VB_B_vs_cal = abs(V_B_optB - V_B_cal) / V_B_cal * 100
error_VB_A_vs_cal = abs(V_B_optA - V_B_cal) / V_B_cal * 100

print("OPTION B: V_B from PDG baseline")
print(f"  V_B^(B) = 2 × {Delta_m_B:.6f} MeV = {V_B_optB:.6f} MeV")
print(f"  Error vs V_B_cal ({V_B_cal} MeV): {error_VB_B_vs_cal:.2f}%")
print()

print("OPTION A: V_B from Book formula")
print(f"  V_B^(A) = 2 × {Delta_m_A:.6f} MeV = {V_B_optA:.6f} MeV")
print(f"  Error vs V_B_cal ({V_B_cal} MeV): {error_VB_A_vs_cal:.2f}%")
print()

# --- E_barrier (above proton) = 3 × Δm_np ---
E_barrier_B = 3.0 * Delta_m_B
E_barrier_A = 3.0 * Delta_m_A
E_barrier_from_cal = V_B_cal + Delta_m_np_PDG

print("E_barrier (above proton) = V_B + Δm_np = 3 × Δm_np")
print(f"  E_barrier^(B) = 3 × {Delta_m_B:.6f} MeV = {E_barrier_B:.6f} MeV")
print(f"  E_barrier^(A) = 3 × {Delta_m_A:.6f} MeV = {E_barrier_A:.6f} MeV")
print(f"  E_barrier from cal = V_B_cal + Δm_np_PDG = {V_B_cal} + {Delta_m_np_PDG:.6f} = {E_barrier_from_cal:.6f} MeV")
print()

error_Ebar_B = abs(E_barrier_B - E_barrier_from_cal) / E_barrier_from_cal * 100
error_Ebar_A = abs(E_barrier_A - E_barrier_from_cal) / E_barrier_from_cal * 100

print(f"  Error E_barrier^(B) vs calibrated: {error_Ebar_B:.2f}%")
print(f"  Error E_barrier^(A) vs calibrated: {error_Ebar_A:.2f}%")
print()

# =============================================================================
# SUMMARY TABLE
# =============================================================================

print("=" * 70)
print("SUMMARY TABLE")
print("=" * 70)
print()
print("| Formula                    | Status | Value (MeV) | Error vs PDG |")
print("|----------------------------|--------|-------------|--------------|")
print(f"| Δm_np^(B) = PDG            | [BL]   | {Delta_m_B:.6f}   | —            |")
print(f"| Δm_np^(A) = (5/2+4α)m_e    | [Dc]   | {Delta_m_A:.6f}   | {error_A_vs_PDG:.3f}%       |")
print(f"| Δm_np^(A1) = (5/2)m_e      | [Dc]   | {Delta_m_A1:.6f}   | {error_A1_vs_PDG:.3f}%       |")
print(f"| Δ(EM) = 4α m_e             | [Dc]   | {Delta_em:.6f}   | (component)  |")
print()
print("| V_B formula                | Status | Value (MeV) | Error vs cal |")
print("|----------------------------|--------|-------------|--------------|")
print(f"| V_B^(B) = 2×Δm_np_PDG      | [Dc]   | {V_B_optB:.6f}   | {error_VB_B_vs_cal:.2f}%        |")
print(f"| V_B^(A) = 2×(5/2+4α)m_e    | [Dc]   | {V_B_optA:.6f}   | {error_VB_A_vs_cal:.2f}%        |")
print(f"| V_B_cal (WKB fit)          | [Cal]  | {V_B_cal:.6f}   | —            |")
print()
print("| E_barrier formula          | Status | Value (MeV) | Error vs cal |")
print("|----------------------------|--------|-------------|--------------|")
print(f"| E_bar^(B) = 3×Δm_np_PDG    | [Dc]   | {E_barrier_B:.6f}   | {error_Ebar_B:.2f}%        |")
print(f"| E_bar^(A) = 3×(5/2+4α)m_e  | [Dc]   | {E_barrier_A:.6f}   | {error_Ebar_A:.2f}%        |")
print(f"| E_bar_cal = V_B_cal+Δm_np  | [Cal]  | {E_barrier_from_cal:.6f}   | —            |")
print()

# =============================================================================
# DECISION MAP
# =============================================================================

print("=" * 70)
print("DECISION MAP: EPISTEMIC TAGS")
print("=" * 70)
print("""
Δm_np:
  Option B: [BL] (PDG baseline)
  Option A: [Dc] (Book formula, conditional on D_bulk/D_membrane = 5/2)

Z₃ invariance of junction sector:
  [Dc] (identical BC + Steiner ⇒ τ₁=τ₂=τ₃)

"No low-lying doublet partners":
  [BL] observational constraint (not proof)

Barrier is Z₃-symmetric (minimal symmetric saddle):
  [Dc]

"One unit per leg = Δm_np":
  OPEN [Dc] (requires 5D action verification)

V_B = 2 × Δm_np:
  [Dc] Z₃ barrier conjecture
  Numeric depends on which Δm_np option is chosen:
    Option B: V_B ≈ 2.587 MeV
    Option A: V_B ≈ 2.585 MeV
""")

print("=" * 70)
print("END OF CALCULATIONS")
print("=" * 70)
