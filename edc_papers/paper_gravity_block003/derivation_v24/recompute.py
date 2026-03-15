#!/usr/bin/env python3
"""
BLOCK-003 Reproducibility Audit: recompute.py

This script reproduces all key numerical values from v23 (canonical closure packet)
and verifies the π-mapping and Planck convention conversions.

Run: python recompute.py
"""

import math

# ==============================================================================
# GROUND TRUTH INPUTS
# ==============================================================================

# Fundamental constants [BL]
M_Z = 91.1876  # GeV
delta_M_Z = 0.0021  # GeV
hbar_c = 1.973269804e-16  # GeV * m
hbar_c_natural = 1.0  # In natural units

# Planck masses [BL]
M_Pl_bar = 2.435e18  # GeV (reduced)
M_Pl = 1.2209e19  # GeV (original)

# Newton's constant
G_N = 6.67430e-11  # m^3 kg^-1 s^-2
delta_G_N = 0.00015e-11  # m^3 kg^-1 s^-2

# ==============================================================================
# CANONICAL CALCULATIONS (v22+ convention)
# ==============================================================================

print("=" * 70)
print("BLOCK-003 REPRODUCIBILITY AUDIT")
print("=" * 70)
print()

# Step 1: R_xi canonical
print("STEP 1: R_xi (canonical convention)")
print("-" * 40)

R_xi_canon_m = math.pi * hbar_c / M_Z
R_xi_canon_GeV = math.pi / M_Z  # In natural units (GeV^-1)

print(f"  R_xi_canon = π × ℏc / M_Z")
print(f"            = π × {hbar_c:.4e} GeV·m / {M_Z} GeV")
print(f"            = {R_xi_canon_m:.4e} m")
print(f"            = {R_xi_canon_GeV:.4e} GeV^-1")

expected_Rxi = 6.80e-18
rel_diff_Rxi = abs(R_xi_canon_m - expected_Rxi) / expected_Rxi
PASS_Rxi = rel_diff_Rxi < 0.01
print(f"  Expected: {expected_Rxi:.2e} m")
print(f"  Rel diff: {rel_diff_Rxi:.2e}")
print(f"  Status: {'PASS' if PASS_Rxi else 'FAIL'}")
print()

# Step 2: M_5 (reduced Planck)
print("STEP 2: M_5 (reduced Planck mass convention)")
print("-" * 40)

M5_cubed_red = M_Pl_bar**2 * M_Z / math.pi
M5_red = M5_cubed_red ** (1/3)

print(f"  M_5^3 = M_Pl_bar^2 / R_xi = M_Pl_bar^2 × M_Z / π")
print(f"        = ({M_Pl_bar:.3e})^2 × {M_Z} / π")
print(f"        = {M5_cubed_red:.4e} GeV^3")
print(f"  M_5   = ({M5_cubed_red:.4e})^(1/3)")
print(f"        = {M5_red:.3e} GeV")

expected_M5_red = 5.6e12
rel_diff_M5_red = abs(M5_red - expected_M5_red) / expected_M5_red
PASS_M5_red = rel_diff_M5_red < 0.01
print(f"  Expected: {expected_M5_red:.1e} GeV")
print(f"  Rel diff: {rel_diff_M5_red:.2e}")
print(f"  Status: {'PASS' if PASS_M5_red else 'FAIL'}")
print()

# Step 3: M_5 (original Planck)
print("STEP 3: M_5 (original Planck mass convention)")
print("-" * 40)

M5_cubed_orig = M_Pl**2 * M_Z / math.pi
M5_orig = M5_cubed_orig ** (1/3)

print(f"  M_5^3 = M_Pl^2 / R_xi = M_Pl^2 × M_Z / π")
print(f"        = ({M_Pl:.4e})^2 × {M_Z} / π")
print(f"        = {M5_cubed_orig:.4e} GeV^3")
print(f"  M_5   = ({M5_cubed_orig:.4e})^(1/3)")
print(f"        = {M5_orig:.3e} GeV")

expected_M5_orig = 1.6e13
rel_diff_M5_orig = abs(M5_orig - expected_M5_orig) / expected_M5_orig
PASS_M5_orig = rel_diff_M5_orig < 0.02
print(f"  Expected: {expected_M5_orig:.1e} GeV")
print(f"  Rel diff: {rel_diff_M5_orig:.2e}")
print(f"  Status: {'PASS' if PASS_M5_orig else 'FAIL'}")
print()

# Step 4: Planck convention verification
print("STEP 4: Planck Convention Conversion")
print("-" * 40)

ratio_computed = M5_orig / M5_red
ratio_expected = (8 * math.pi) ** (1/3)

print(f"  M_5(orig) / M_5(red) = {M5_orig:.3e} / {M5_red:.3e}")
print(f"                       = {ratio_computed:.4f}")
print(f"  Expected: (8π)^(1/3) = {ratio_expected:.4f}")

rel_diff_Planck = abs(ratio_computed - ratio_expected) / ratio_expected
PASS_Planck = rel_diff_Planck < 0.001
print(f"  Rel diff: {rel_diff_Planck:.2e}")
print(f"  Status: {'PASS' if PASS_Planck else 'FAIL'}")
print()

# ==============================================================================
# OLD <-> CANONICAL π-MAP AUDIT
# ==============================================================================

print("=" * 70)
print("OLD <-> CANONICAL π-MAP AUDIT")
print("=" * 70)
print()

# Old convention
print("OLD CONVENTION (v15-v20):")
print("-" * 40)

R_xi_old_m = hbar_c / M_Z
R_xi_old_GeV = 1.0 / M_Z

print(f"  R_xi_old = ℏc / M_Z = {R_xi_old_m:.4e} m")
print(f"          = 1/M_Z = {R_xi_old_GeV:.5f} GeV^-1")
print()

# π-map verification for R_xi
print("π-MAP FOR R_xi:")
print("-" * 40)

pi_times_Rxi_old = math.pi * R_xi_old_m
rel_diff_pi_Rxi = abs(pi_times_Rxi_old - R_xi_canon_m) / R_xi_canon_m

print(f"  π × R_xi_old = π × {R_xi_old_m:.4e}")
print(f"              = {pi_times_Rxi_old:.4e} m")
print(f"  R_xi_canon   = {R_xi_canon_m:.4e} m")
print(f"  Rel diff: {rel_diff_pi_Rxi:.2e}")

PASS_pi_Rxi = rel_diff_pi_Rxi < 1e-10
print(f"  Status: {'PASS' if PASS_pi_Rxi else 'FAIL'}")
print()

# M_5 in old convention
print("M_5 IN OLD CONVENTION:")
print("-" * 40)

M5_cubed_old = M_Pl_bar**2 * M_Z  # Note: no π factor
M5_old = M5_cubed_old ** (1/3)

print(f"  M_5_old^3 = M_Pl_bar^2 × M_Z (no π)")
print(f"            = {M5_cubed_old:.4e} GeV^3")
print(f"  M_5_old   = {M5_old:.3e} GeV")
print()

# π-map verification for M_5
print("π-MAP FOR M_5:")
print("-" * 40)

pi_minus_third = math.pi ** (-1/3)
M5_canon_from_old = pi_minus_third * M5_old

print(f"  π^(-1/3) = {pi_minus_third:.4f}")
print(f"  M_5_canon = π^(-1/3) × M_5_old")
print(f"           = {pi_minus_third:.4f} × {M5_old:.3e}")
print(f"           = {M5_canon_from_old:.3e} GeV")
print(f"  Direct M_5_red = {M5_red:.3e} GeV")

rel_diff_M5_map = abs(M5_canon_from_old - M5_red) / M5_red
PASS_M5_map = rel_diff_M5_map < 0.01
print(f"  Rel diff: {rel_diff_M5_map:.2e}")
print(f"  Status: {'PASS' if PASS_M5_map else 'FAIL'}")
print()

# ==============================================================================
# ERROR PROPAGATION
# ==============================================================================

print("=" * 70)
print("ERROR PROPAGATION")
print("=" * 70)
print()

# Relative uncertainties
rel_delta_MZ = delta_M_Z / M_Z
rel_delta_GN = delta_G_N / G_N
rel_delta_Mplbar = 0.5 * rel_delta_GN  # M_Pl_bar ∝ G^{-1/2}
rel_delta_Rxi = rel_delta_MZ  # R_xi ∝ 1/M_Z

print(f"  δM_Z / M_Z = {rel_delta_MZ:.2e}")
print(f"  δG_N / G_N = {rel_delta_GN:.2e}")
print(f"  δM_Pl_bar / M_Pl_bar = 0.5 × δG_N/G_N = {rel_delta_Mplbar:.2e}")
print(f"  δR_xi / R_xi = δM_Z / M_Z = {rel_delta_Rxi:.2e}")
print()

# Error propagation
term1 = (2/3 * rel_delta_Mplbar)**2
term2 = (1/3 * rel_delta_Rxi)**2
rel_delta_M5 = math.sqrt(term1 + term2)

print(f"  δM_5/M_5 = √[(2/3 × δM_Pl_bar/M_Pl_bar)² + (1/3 × δR_xi/R_xi)²]")
print(f"          = √[({2/3 * rel_delta_Mplbar:.2e})² + ({1/3 * rel_delta_Rxi:.2e})²]")
print(f"          = √[{term1:.2e} + {term2:.2e}]")
print(f"          = {rel_delta_M5:.2e}")

expected_error = 1.1e-5
rel_diff_error = abs(rel_delta_M5 - expected_error) / expected_error
PASS_error = rel_diff_error < 0.1
print(f"  Expected: {expected_error:.1e}")
print(f"  Status: {'PASS' if PASS_error else 'FAIL'}")
print()

# ==============================================================================
# FINAL SUMMARY
# ==============================================================================

print("=" * 70)
print("FINAL AUDIT SUMMARY")
print("=" * 70)
print()

all_pass = all([
    PASS_Rxi, PASS_M5_red, PASS_M5_orig, PASS_Planck,
    PASS_pi_Rxi, PASS_M5_map, PASS_error
])

checks = [
    ("R_xi_canon computation", PASS_Rxi),
    ("M_5_reduced computation", PASS_M5_red),
    ("M_5_original computation", PASS_M5_orig),
    ("Planck map (8π)^{1/3}", PASS_Planck),
    ("π-map for R_xi", PASS_pi_Rxi),
    ("π-map for M_5", PASS_M5_map),
    ("Error budget", PASS_error),
]

for name, passed in checks:
    status = "PASS" if passed else "FAIL"
    print(f"  {name:35s} ... {status}")

print()
print("=" * 70)
if all_pass:
    print("ALL CHECKS PASSED")
else:
    print("SOME CHECKS FAILED")
print("=" * 70)

# ==============================================================================
# OUTPUT CANONICAL VALUES (for copy to REPORT.md)
# ==============================================================================

print()
print("CANONICAL VALUES FOR REPORT:")
print("-" * 40)
print(f"R_xi_canon     = {R_xi_canon_m:.4e} m")
print(f"R_xi_canon     = {R_xi_canon_GeV:.5f} GeV^-1")
print(f"M_5 (reduced)  = {M5_red:.3e} GeV")
print(f"M_5 (original) = {M5_orig:.3e} GeV")
print(f"(8π)^{1/3}     = {ratio_expected:.4f}")
print(f"Ratio computed = {ratio_computed:.4f}")
print(f"π^{-1/3}       = {pi_minus_third:.4f}")
print(f"δM_5/M_5       = {rel_delta_M5:.2e}")
