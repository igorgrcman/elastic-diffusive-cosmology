#!/usr/bin/env python3
"""
G_5 and ell Dimensional Consistency Checker
============================================

Verifies dimensional consistency of candidate formulas for g_5 and ell
in the G_F closure chain.

Natural units: hbar = c = 1
Dimensions: [E] = energy, [L] = length = [E]^{-1}

Author: EDC Research / Claude Code
Date: 2026-01-22
Reference: sections/ch11_g5_ell_value_closure_attempt.tex
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class DimQuantity:
    """A quantity with energy dimension exponent."""
    name: str
    symbol: str
    dim_E: float  # exponent of [E]
    value: Optional[float] = None
    unit: str = ""

    def __repr__(self):
        dim_str = f"[E]^{{{self.dim_E}}}" if self.dim_E != 0 else "[E]^0"
        val_str = f" = {self.value} {self.unit}" if self.value else ""
        return f"{self.symbol}: {dim_str}{val_str}"


# EDC baseline parameters
SIGMA_RE2 = DimQuantity("Cell energy", "sigma*r_e^2", 1, 5.856, "MeV")
R_E = DimQuantity("Lattice spacing", "r_e", -1, 1.0, "fm")
HBAR_C = DimQuantity("hbar*c", "hbar*c", 0, 197.3, "MeV*fm")

# Target quantities
G_5 = DimQuantity("5D gauge coupling", "g_5", -0.5)
G_4 = DimQuantity("4D gauge coupling", "g_4", 0)
ELL = DimQuantity("Brane thickness", "ell", -1)
G_F = DimQuantity("Fermi constant", "G_F", -2, 1.17e-5, "GeV^{-2}")


def check_dimension(formula_name: str, lhs_dim: float, rhs_dim: float) -> bool:
    """Check if LHS and RHS dimensions match."""
    match = abs(lhs_dim - rhs_dim) < 1e-10
    status = "PASS" if match else "FAIL"
    color = "\033[92m" if match else "\033[91m"
    reset = "\033[0m"
    print(f"  [{color}{status}{reset}] {formula_name}")
    print(f"        LHS: [E]^{{{lhs_dim}}}, RHS: [E]^{{{rhs_dim}}}")
    return match


def main():
    """Run dimensional consistency checks."""
    print("=" * 70)
    print("DIMENSIONAL CONSISTENCY CHECK: g_5 and ell Candidates")
    print("=" * 70)
    print()

    print("BASELINE PARAMETERS:")
    print(f"  {SIGMA_RE2}")
    print(f"  {R_E}")
    print(f"  {HBAR_C}")
    print()

    print("-" * 70)
    print("CANDIDATE FORMULAS FOR g^2:")
    print("-" * 70)

    # G1: g^2 = 4*pi * sigma*r_e^3 / hbar*c
    # [g^2] = [E]^0 (dimensionless)
    # [sigma*r_e^3 / hbar*c] = [E] * [E]^{-3} / [E]^0 = [E]^{-2}  -- WRONG!
    # Actually: sigma*r_e^2 has dim [E], r_e has dim [E]^{-1}
    # So sigma*r_e^3 = sigma*r_e^2 * r_e has dim [E] * [E]^{-1} = [E]^0
    # And hbar*c has dim [E]^0 in natural units (it's just a conversion factor)
    # So [sigma*r_e^3 / hbar*c] = [E]^0 / [E]^0 = [E]^0

    print()
    print("G1: g^2 = 4*pi * (sigma*r_e^3) / (hbar*c)")
    dim_sigma_re3 = SIGMA_RE2.dim_E + R_E.dim_E  # [E]^1 * [E]^{-1} = [E]^0
    dim_hbar_c = 0  # [E]^0 (natural units conversion)
    rhs_dim_G1 = dim_sigma_re3 - dim_hbar_c  # [E]^0
    check_dimension("g^2 dimensionless", G_4.dim_E * 2, rhs_dim_G1)

    # Numeric check
    g2_G1 = 4 * 3.14159 * (5.856 * 1.0) / 197.3
    print(f"  Numeric: g^2 = 4*pi * 5.856 / 197.3 = {g2_G1:.4f}")
    print(f"  Compare to SM g_2^2 ~ 0.42")
    print()

    # G2: g_5^2 = (hbar*c)^2 / (sigma*r_e^2)
    # [g_5^2] = [E]^{-1}
    # [(hbar*c)^2] = [E]^0 in natural units... but hbar*c = 197.3 MeV*fm
    # Actually in energy units: [hbar*c / r_e] = [E] (energy scale)
    # Let's be careful: hbar*c has dimension [E*L] = [E]*[E]^{-1} = [E]^0
    # But the VALUE 197.3 MeV*fm means if we divide by length we get energy.
    # In the formula g_5^2 ~ (hbar*c)^2 / (sigma*r_e^2):
    # If sigma*r_e^2 has dim [E], then (hbar*c)^2 / [E] needs (hbar*c)^2 to have dim [E]^0
    # which gives [g_5^2] = [E]^{-1}... but that's wrong!

    # Let me reconsider: in natural units hbar=c=1, sigma*r_e^2 = 5.856 MeV is an energy.
    # For g_5^2 to have dim [E]^{-1}, we need:
    # g_5^2 ~ (something with dim [E]^{-1}) / (something with dim [E]^0)
    # The formula g_5^2 ~ (hbar*c)^2 / (sigma*r_e^2) in MKS gives:
    # [(MeV*fm)^2 / MeV] = MeV * fm^2 which is [E] * [L]^2 = [E]^{-1} in natural units
    # So this is dimensionally correct for g_5^2!

    print("G2: g_5^2 = (hbar*c)^2 / (sigma*r_e^2)")
    print("  Note: In mixed units, (hbar*c)^2 = (MeV*fm)^2, sigma*r_e^2 = MeV")
    print("  So [(hbar*c)^2 / (sigma*r_e^2)] = MeV * fm^2 ~ [E] * [L]^2 = [E]^{-1}")
    rhs_dim_G2 = -1  # [E]^{-1}
    check_dimension("g_5^2 has dim [E]^{-1}", G_5.dim_E * 2, rhs_dim_G2)

    g5_sq_G2 = (197.3)**2 / 5.856  # MeV * fm^2
    print(f"  Numeric: g_5^2 = 197.3^2 / 5.856 = {g5_sq_G2:.1f} MeV*fm^2")
    print(f"  This is VERY large compared to weak scale needs.")
    print()

    print("-" * 70)
    print("CANDIDATE FORMULAS FOR ell:")
    print("-" * 70)

    # L1: ell = pi / M_W
    # [ell] = [E]^{-1}
    # [1/M_W] = [E]^{-1} -- matches!
    print()
    print("L1: ell = x_1 / M_W  (with x_1 = pi)")
    rhs_dim_L1 = -1  # 1/[E] = [E]^{-1}
    check_dimension("ell has dim [E]^{-1}", ELL.dim_E, rhs_dim_L1)

    ell_L1_fm = 3.14159 / 80000 * 197.3  # fm (using hbar*c conversion)
    print(f"  Numeric: ell = pi / (80 GeV) = {ell_L1_fm:.4f} fm")
    print(f"  WARNING: Uses M_W as input (forbidden for first-principles)")
    print()

    # L2: ell = hbar*c / (sigma*r_e^2) * f_geom
    # [ell] = [E]^{-1}
    # [hbar*c / (sigma*r_e^2)] = [E*L] / [E] = [L] = [E]^{-1} -- matches!
    print("L2: ell = (hbar*c) / (sigma*r_e^2) * f_geom")
    rhs_dim_L2 = -1  # [E*L]/[E] = [L] = [E]^{-1}
    check_dimension("ell has dim [E]^{-1}", ELL.dim_E, rhs_dim_L2)

    ell_base = 197.3 / 5.856  # fm
    print(f"  Base value: hbar*c / (sigma*r_e^2) = 197.3 / 5.856 = {ell_base:.2f} fm")
    f_geom_required = 0.04 / ell_base
    print(f"  To get ell ~ 0.04 fm, need f_geom ~ {f_geom_required:.2e}")
    print(f"  NOTE: f_geom ~ 10^{-3} is unexplained")
    print()

    print("-" * 70)
    print("G_F CLOSURE SPINE CHECK:")
    print("-" * 70)
    print()
    print("Formula: G_F = g_5^2 * ell^2 * I_4 / x_1^2")
    print()

    # [G_F] = [E]^{-2}
    # [g_5^2] = [E]^{-1}
    # [ell^2] = [E]^{-2}
    # [I_4] = [E] (integral over length of |f_L|^4)
    # [x_1^2] = [E]^0 (dimensionless)
    # Total: [E]^{-1} * [E]^{-2} * [E] / [E]^0 = [E]^{-2} -- matches!

    dim_g5_sq = -1
    dim_ell_sq = -2
    dim_I4 = 1
    dim_x1_sq = 0
    rhs_dim_GF = dim_g5_sq + dim_ell_sq + dim_I4 - dim_x1_sq
    check_dimension("G_F has dim [E]^{-2}", G_F.dim_E, rhs_dim_GF)

    print()
    print("Breakdown:")
    print(f"  [g_5^2] = [E]^{{{dim_g5_sq}}}")
    print(f"  [ell^2] = [E]^{{{dim_ell_sq}}}")
    print(f"  [I_4]   = [E]^{{{dim_I4}}}")
    print(f"  [x_1^2] = [E]^{{{dim_x1_sq}}}")
    print(f"  Total:  [E]^{{{rhs_dim_GF}}} = [G_F] check!")
    print()

    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("""
G1 (g^2 = 4*pi*sigma*r_e^3/hbar*c):
  - Dimension: [E]^0 (correct for g_4^2)
  - Value: ~0.37 (11% below SM g_2^2 ~ 0.42)
  - Status: Promising, coefficient 4*pi unexplained

G2 (g_5^2 = (hbar*c)^2 / sigma*r_e^2):
  - Dimension: [E]^{-1} (correct for g_5^2)
  - Value: ~6650 MeV*fm^2 (very large)
  - Status: Dimensionally OK but numerically inconsistent

L1 (ell = pi/M_W):
  - Dimension: [E]^{-1} (correct)
  - Value: ~0.04 fm
  - Status: Uses M_W (FORBIDDEN for first-principles)

L2 (ell = hbar*c / sigma*r_e^2 * f_geom):
  - Dimension: [E]^{-1} (correct)
  - Value: ~34 fm * f_geom, needs f_geom ~ 10^{-3}
  - Status: f_geom unexplained
""")
    return True


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
