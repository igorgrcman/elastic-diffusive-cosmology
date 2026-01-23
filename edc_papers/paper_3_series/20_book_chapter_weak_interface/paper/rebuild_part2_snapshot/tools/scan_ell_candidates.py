#!/usr/bin/env python3
"""
Brane Thickness (ell) Candidate Scanner
========================================

Scans different candidate formulas for ell and computes the resulting
mediator mass m_phi = x_1 / ell.

Compares each to M_W ~ 80 GeV to assess plausibility.

Author: EDC Research / Claude Code
Date: 2026-01-22
Reference: sections/ch11_g5_ell_value_closure_attempt.tex
"""

import numpy as np
from dataclasses import dataclass
from typing import Callable, Optional

# Physical constants
HBAR_C = 197.3  # MeV * fm
M_W = 80379  # MeV (W boson mass)

# EDC parameters
SIGMA_RE2 = 5.856  # MeV (cell energy) [Dc]
R_E = 1.0  # fm (lattice spacing) [P]
R_XI = 1e-3  # fm (diffusion correlation length) [P]


@dataclass
class EllCandidate:
    """A candidate formula for brane thickness ell."""
    name: str
    tag: str  # Epistemic tag
    formula: Callable[[], float]  # Returns ell in fm
    description: str
    uses_sm: bool = False  # Does it use SM input?


def fm_to_GeV_inv(fm: float) -> float:
    """Convert fm to GeV^{-1}."""
    return fm / HBAR_C * 1000  # fm -> MeV^{-1} -> GeV^{-1}


def compute_m_phi(ell_fm: float, x_1: float = np.pi) -> float:
    """Compute mediator mass m_phi = x_1 / ell in MeV."""
    ell_MeV_inv = ell_fm / HBAR_C  # fm -> MeV^{-1}
    return x_1 / ell_MeV_inv  # MeV


# Define candidates
CANDIDATES = [
    EllCandidate(
        name="L1",
        tag="[I]",
        formula=lambda: np.pi / M_W * HBAR_C,  # pi/M_W in fm
        description="ell = pi / M_W (weak scale matching)",
        uses_sm=True
    ),
    EllCandidate(
        name="L2a",
        tag="[P]",
        formula=lambda: HBAR_C / SIGMA_RE2,  # fm
        description="ell = hbar*c / (sigma*r_e^2) (membrane scale)",
        uses_sm=False
    ),
    EllCandidate(
        name="L2b",
        tag="[P]",
        formula=lambda: HBAR_C / SIGMA_RE2 * 1e-3,  # with f_geom
        description="ell = (hbar*c / sigma*r_e^2) * 10^{-3}",
        uses_sm=False
    ),
    EllCandidate(
        name="L3",
        tag="[P]",
        formula=lambda: R_XI,  # fm
        description="ell = R_xi (diffusion correlation length)",
        uses_sm=False
    ),
    EllCandidate(
        name="L4",
        tag="[P]",
        formula=lambda: R_E,  # fm
        description="ell = r_e (lattice spacing)",
        uses_sm=False
    ),
    EllCandidate(
        name="L5",
        tag="[P]",
        formula=lambda: np.sqrt(R_E * R_XI),  # geometric mean
        description="ell = sqrt(r_e * R_xi) (geometric mean)",
        uses_sm=False
    ),
]


def main():
    """Scan all ell candidates and report results."""
    print("=" * 80)
    print("BRANE THICKNESS (ell) CANDIDATE SCAN")
    print("=" * 80)
    print()
    print(f"Target: m_phi ~ M_W = {M_W/1000:.1f} GeV")
    print()
    print("EDC Parameters:")
    print(f"  sigma*r_e^2 = {SIGMA_RE2:.3f} MeV [Dc]")
    print(f"  r_e = {R_E:.1f} fm [P]")
    print(f"  R_xi = {R_XI:.0e} fm [P]")
    print(f"  hbar*c = {HBAR_C:.1f} MeV*fm [BL]")
    print()
    print("-" * 80)
    print(f"{'Name':<8} {'Tag':<6} {'ell (fm)':<12} {'m_phi (GeV)':<14} {'m_phi/M_W':<10} {'SM-free?'}")
    print("-" * 80)

    for cand in CANDIDATES:
        ell_fm = cand.formula()
        m_phi_MeV = compute_m_phi(ell_fm)
        m_phi_GeV = m_phi_MeV / 1000
        ratio = m_phi_GeV / (M_W / 1000)
        sm_free = "YES" if not cand.uses_sm else "NO"

        # Color coding
        if 0.5 < ratio < 2.0:
            status = "\033[92m"  # Green - close to M_W
        elif 0.1 < ratio < 10:
            status = "\033[93m"  # Yellow - order of magnitude
        else:
            status = "\033[91m"  # Red - far off
        reset = "\033[0m"

        print(f"{cand.name:<8} {cand.tag:<6} {ell_fm:<12.2e} {status}{m_phi_GeV:<14.2f}{reset} {ratio:<10.2f} {sm_free}")

    print("-" * 80)
    print()
    print("CANDIDATE DETAILS:")
    print("-" * 80)
    for cand in CANDIDATES:
        ell_fm = cand.formula()
        m_phi_MeV = compute_m_phi(ell_fm)
        print(f"\n{cand.name}: {cand.description}")
        print(f"  Tag: {cand.tag}")
        print(f"  ell = {ell_fm:.4e} fm = {fm_to_GeV_inv(ell_fm):.4f} GeV^{{-1}}")
        print(f"  m_phi = {m_phi_MeV/1000:.2f} GeV")
        if cand.uses_sm:
            print("  WARNING: Uses SM input (M_W) - not first-principles!")

    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print("""
L1: Uses M_W directly -> gives M_W by construction (FORBIDDEN)
L2a: Pure membrane scale -> m_phi ~ 6 MeV (way too small!)
L2b: With f_geom ~ 10^{-3} -> m_phi ~ 60 GeV (reasonable)
L3: R_xi -> m_phi ~ 600 GeV (factor 8 too large)
L4: r_e -> m_phi ~ 0.6 GeV (way too small!)
L5: geometric mean -> m_phi ~ 20 GeV (factor 4 too small)

CONCLUSION:
- No SM-free candidate naturally gives M_W scale without tuning
- L2b requires unexplained f_geom ~ 10^{-3}
- L3 (R_xi) is closest SM-free candidate but overshoots by 8x
- The weak scale appears to require additional geometric input
""")

    # Check what f_geom would be needed for each base scale
    print("-" * 80)
    print("REQUIRED f_geom TO GET m_phi = M_W:")
    print("-" * 80)

    base_scales = [
        ("hbar*c / sigma*r_e^2", HBAR_C / SIGMA_RE2),
        ("r_e", R_E),
        ("R_xi", R_XI),
        ("sqrt(r_e * R_xi)", np.sqrt(R_E * R_XI)),
    ]

    ell_target = np.pi / M_W * HBAR_C  # fm

    for name, base_fm in base_scales:
        f_required = ell_target / base_fm
        print(f"  {name:<25}: f_geom = {f_required:.2e}")

    return True


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
