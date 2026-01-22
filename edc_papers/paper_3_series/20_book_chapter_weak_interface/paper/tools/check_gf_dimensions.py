#!/usr/bin/env python3
"""
G_F Dimensional Consistency Check
==================================
Verifies that the EDC effective operator has correct dimensions for G_F.

This is a sanity check, not a derivation. It confirms:
1. [G_F] = [E]^-2 in natural units
2. [g_eff^2 / m_phi^2] = [E]^-2
3. The structural form is dimensionally consistent

Run: python3 tools/check_gf_dimensions.py
"""

from dataclasses import dataclass
from typing import Dict

@dataclass
class Dimension:
    """Energy dimension in natural units (hbar = c = 1)."""
    power: float  # [E]^power

    def __repr__(self):
        if self.power == 0:
            return "[E]^0 (dimensionless)"
        elif self.power == 1:
            return "[E]^1"
        elif self.power == -1:
            return "[E]^-1"
        else:
            return f"[E]^{self.power}"

    def __mul__(self, other: 'Dimension') -> 'Dimension':
        return Dimension(self.power + other.power)

    def __truediv__(self, other: 'Dimension') -> 'Dimension':
        return Dimension(self.power - other.power)

    def __pow__(self, n: float) -> 'Dimension':
        return Dimension(self.power * n)

    def __eq__(self, other: 'Dimension') -> bool:
        return abs(self.power - other.power) < 1e-10


def check_gf_dimensions():
    """Check dimensional consistency of G_F derivation chain."""

    print("=" * 60)
    print("G_F Dimensional Consistency Check")
    print("=" * 60)
    print()

    # Define basic dimensions
    E = Dimension(1)      # Energy
    E0 = Dimension(0)     # Dimensionless
    E_inv = Dimension(-1) # 1/Energy
    E_inv2 = Dimension(-2) # 1/Energy^2

    # G_F target dimension
    G_F_dim = E_inv2
    print(f"Target: [G_F] = {G_F_dim}")
    print()

    # SM side: G_F = g^2 / (4*sqrt(2) * M_W^2)
    print("SM relation: G_F = g^2 / (4*sqrt(2) * M_W^2)")
    g_dim = E0  # gauge coupling is dimensionless
    M_W_dim = E
    SM_result = (g_dim ** 2) / (M_W_dim ** 2)
    print(f"  [g] = {g_dim}")
    print(f"  [M_W] = {M_W_dim}")
    print(f"  [g^2 / M_W^2] = {SM_result}")
    print(f"  Check: {SM_result} == {G_F_dim} ? {'PASS' if SM_result == G_F_dim else 'FAIL'}")
    print()

    # EDC side: G_EDC = g_eff^2 / m_phi^2
    print("EDC relation: G_EDC ~ g_eff^2 / m_phi^2")
    g_eff_dim = E0  # effective 4D coupling is dimensionless
    m_phi_dim = E   # mediator mass
    EDC_result = (g_eff_dim ** 2) / (m_phi_dim ** 2)
    print(f"  [g_eff] = {g_eff_dim}")
    print(f"  [m_phi] = {m_phi_dim}")
    print(f"  [g_eff^2 / m_phi^2] = {EDC_result}")
    print(f"  Check: {EDC_result} == {G_F_dim} ? {'PASS' if EDC_result == G_F_dim else 'FAIL'}")
    print()

    # 5D to 4D reduction: G_F = G_5 * I_4
    print("5D reduction: G_F = G_5 * I_4 (overlap integral)")
    G_5_dim = Dimension(-3)  # 5D Fermi coupling [E]^-3
    I_4_dim = E  # Overlap integral has dim [length] = [E]^-1... wait
    # Actually I_4 = ∫ |f_L|^4 dz, and [f_L^2] is normalized so ∫|f_L|^2 dz = 1
    # This means [f_L]^2 has dim [length]^-1 = [E]^1, so [f_L] ~ [E]^1/2
    # Then [|f_L|^4] ~ [E]^2, and [∫ |f_L|^4 dz] ~ [E]^2 * [E]^-1 = [E]^1
    I_4_dim = E
    reduction_result = G_5_dim * I_4_dim
    print(f"  [G_5] = {G_5_dim} (5D Fermi coupling)")
    print(f"  [I_4] = {I_4_dim} (overlap integral)")
    print(f"  [G_5 * I_4] = {reduction_result}")
    print(f"  Check: {reduction_result} == {G_F_dim} ? {'PASS' if reduction_result == G_F_dim else 'FAIL'}")
    print()

    # Summary
    print("=" * 60)
    all_pass = (SM_result == G_F_dim) and (EDC_result == G_F_dim) and (reduction_result == G_F_dim)
    if all_pass:
        print("DIMENSIONAL CONSISTENCY: ALL CHECKS PASS")
    else:
        print("DIMENSIONAL CONSISTENCY: SOME CHECKS FAILED")
    print("=" * 60)
    print()
    print("Note: This confirms dimensional consistency, not numerical values.")
    print("The actual G_F derivation requires computing g_eff, m_phi, I_4.")

    return all_pass


if __name__ == "__main__":
    success = check_gf_dimensions()
    exit(0 if success else 1)
