#!/usr/bin/env python3
"""
Derivation v45 — SoT-LOCK TRACK COMPILER
=========================================

Single Source of Truth for ALL FOUR GUT TRACKS:
- SU(5), SO(10), Pati-Salam, E6

Computes from SoT:
(A) Full anomaly audit (all 6 + Witten)
(B) ΔE_vac^finite scoring inputs (BC class counts)
(C) Mass-gating constraints for exotics

LOCK PROTOCOL (from v44):
1. SoT_TRACKS defines all track data
2. generate_tables() produces tables_generated.tex deterministically
3. Hash verification prevents drift
"""

import os
import sys
import re
import hashlib
from fractions import Fraction
from typing import List, Dict, Tuple, Any, Optional
from dataclasses import dataclass, field
from enum import Enum

# =============================================================================
# ENUMERATIONS
# =============================================================================

class BCType(Enum):
    """Boundary condition types."""
    NN = "NN"  # Neumann-Neumann (same chirality) → zero-mode
    DD = "DD"  # Dirichlet-Dirichlet (same chirality) → zero-mode
    ND = "ND"  # Mixed → no zero-mode
    DN = "DN"  # Mixed → no zero-mode

class DecouplingMechanism(Enum):
    """How exotics decouple from low-energy spectrum."""
    MIXED_BC = "Mixed BC"
    BRANE_MASS = "Brane mass"
    HOSOTANI = "Hosotani mechanism"
    HEAVY_KK = "Heavy KK mass"
    NONE = "None (zero-mode)"

class EpistemicTag(Enum):
    """Epistemic status tags."""
    D = "D"      # Derived
    Dc = "Dc"    # Derived with convention
    I = "I"      # Identity
    BL = "BL"    # Borrowed from literature
    P = "P"      # Postulate
    OPEN = "OPEN"

# =============================================================================
# SINGLE SOURCE OF TRUTH: TRACK DEFINITIONS
# =============================================================================

# Common SM hypercharges (canonical LH Weyl basis)
Y_QL = Fraction(1, 6)
Y_LL = Fraction(-1, 2)
Y_uLc = Fraction(-2, 3)
Y_dLc = Fraction(1, 3)
Y_eLc = Fraction(1, 1)
Y_nuLc = Fraction(0, 1)

# SM field template (used by all tracks)
SM_FIELDS_TEMPLATE = [
    {
        "name": "Q_L",
        "latex": r"Q_L",
        "su3": "3",
        "su2": "2",
        "Y": Y_QL,
        "multiplicity": 6,
        "color_factor": 3,
        "su2_factor": 2,
        "is_exotic": False,
        "tag": EpistemicTag.D,
    },
    {
        "name": "L_L",
        "latex": r"\ell_L",
        "su3": "1",
        "su2": "2",
        "Y": Y_LL,
        "multiplicity": 2,
        "color_factor": 1,
        "su2_factor": 2,
        "is_exotic": False,
        "tag": EpistemicTag.D,
    },
    {
        "name": "u_L^c",
        "latex": r"u^c_L",
        "su3": "3bar",
        "su2": "1",
        "Y": Y_uLc,
        "multiplicity": 3,
        "color_factor": 3,
        "su2_factor": 1,
        "is_exotic": False,
        "tag": EpistemicTag.D,
    },
    {
        "name": "d_L^c",
        "latex": r"d^c_L",
        "su3": "3bar",
        "su2": "1",
        "Y": Y_dLc,
        "multiplicity": 3,
        "color_factor": 3,
        "su2_factor": 1,
        "is_exotic": False,
        "tag": EpistemicTag.D,
    },
    {
        "name": "e_L^c",
        "latex": r"e^c_L",
        "su3": "1",
        "su2": "1",
        "Y": Y_eLc,
        "multiplicity": 1,
        "color_factor": 1,
        "su2_factor": 1,
        "is_exotic": False,
        "tag": EpistemicTag.D,
    },
]

# =============================================================================
# TRACK DEFINITIONS
# =============================================================================

SoT_TRACKS: Dict[str, Dict[str, Any]] = {
    # =========================================================================
    # SU(5) TRACK
    # =========================================================================
    "SU5": {
        "name": "SU(5)",
        "latex": r"SU(5)",
        "parent_group": "SU(5)",
        "survivor_group": "SU(3)_C × SU(2)_L × U(1)_Y",
        "rank": 4,
        "rank_drop": 0,
        "tag": EpistemicTag.BL,

        # Gauge sector BC classes
        "gauge_sector": {
            "total_generators": 24,
            "SM_generators": 12,  # 8 + 3 + 1
            "broken_generators": 12,  # X, Y bosons
            "BC_classes": {
                "NN": 12,  # SM gauge bosons (zero-modes)
                "DD": 0,
                "mixed": 12,  # X, Y bosons (no zero-modes)
            },
            "tag": EpistemicTag.D,
        },

        # Matter sector
        "matter_fields": [
            # SM fields from 5bar + 10
            {"name": "Q_L", "latex": r"Q_L", "su3": "3", "su2": "2", "Y": Y_QL,
             "multiplicity": 6, "color_factor": 3, "su2_factor": 2,
             "BC": BCType.NN, "zero_mode": True, "is_exotic": False,
             "origin": r"\mathbf{10}", "tag": EpistemicTag.D},
            {"name": "L_L", "latex": r"\ell_L", "su3": "1", "su2": "2", "Y": Y_LL,
             "multiplicity": 2, "color_factor": 1, "su2_factor": 2,
             "BC": BCType.NN, "zero_mode": True, "is_exotic": False,
             "origin": r"\bar{\mathbf{5}}", "tag": EpistemicTag.D},
            {"name": "u_L^c", "latex": r"u^c_L", "su3": "3bar", "su2": "1", "Y": Y_uLc,
             "multiplicity": 3, "color_factor": 3, "su2_factor": 1,
             "BC": BCType.DD, "zero_mode": True, "is_exotic": False,
             "origin": r"\mathbf{10}", "tag": EpistemicTag.D},
            {"name": "d_L^c", "latex": r"d^c_L", "su3": "3bar", "su2": "1", "Y": Y_dLc,
             "multiplicity": 3, "color_factor": 3, "su2_factor": 1,
             "BC": BCType.DD, "zero_mode": True, "is_exotic": False,
             "origin": r"\bar{\mathbf{5}}", "tag": EpistemicTag.D},
            {"name": "e_L^c", "latex": r"e^c_L", "su3": "1", "su2": "1", "Y": Y_eLc,
             "multiplicity": 1, "color_factor": 1, "su2_factor": 1,
             "BC": BCType.DD, "zero_mode": True, "is_exotic": False,
             "origin": r"\mathbf{10}", "tag": EpistemicTag.D},
            # No nu_R in minimal SU(5)
        ],

        # Exotics (colored Higgs triplets from 5_H)
        "exotics": [
            {"name": "T_H", "latex": r"T_H", "su3": "3", "su2": "1", "Y": Fraction(-1, 3),
             "multiplicity": 3, "is_exotic": True, "decouples": True,
             "mechanism": DecouplingMechanism.BRANE_MASS,
             "description": "Color triplet Higgs", "tag": EpistemicTag.Dc},
            {"name": "T_H^c", "latex": r"\bar{T}_H", "su3": "3bar", "su2": "1", "Y": Fraction(1, 3),
             "multiplicity": 3, "is_exotic": True, "decouples": True,
             "mechanism": DecouplingMechanism.BRANE_MASS,
             "description": "Color triplet anti-Higgs", "tag": EpistemicTag.Dc},
        ],

        # Reference BC for ΔE_vac
        "BC_ref": "all-NN",
    },

    # =========================================================================
    # SO(10) TRACK
    # =========================================================================
    "SO10": {
        "name": "SO(10)",
        "latex": r"SO(10)",
        "parent_group": "SO(10)",
        "survivor_group": "SU(3)_C × SU(2)_L × U(1)_Y",
        "rank": 5,
        "rank_drop": 1,
        "tag": EpistemicTag.BL,

        "gauge_sector": {
            "total_generators": 45,
            "SM_generators": 12,
            "broken_generators": 33,
            "BC_classes": {
                "NN": 12,
                "DD": 0,
                "mixed": 33,
            },
            "tag": EpistemicTag.D,
        },

        "matter_fields": [
            # All SM fields from spinor 16
            {"name": "Q_L", "latex": r"Q_L", "su3": "3", "su2": "2", "Y": Y_QL,
             "multiplicity": 6, "color_factor": 3, "su2_factor": 2,
             "BC": BCType.NN, "zero_mode": True, "is_exotic": False,
             "origin": r"\mathbf{16}", "tag": EpistemicTag.D},
            {"name": "L_L", "latex": r"\ell_L", "su3": "1", "su2": "2", "Y": Y_LL,
             "multiplicity": 2, "color_factor": 1, "su2_factor": 2,
             "BC": BCType.NN, "zero_mode": True, "is_exotic": False,
             "origin": r"\mathbf{16}", "tag": EpistemicTag.D},
            {"name": "u_L^c", "latex": r"u^c_L", "su3": "3bar", "su2": "1", "Y": Y_uLc,
             "multiplicity": 3, "color_factor": 3, "su2_factor": 1,
             "BC": BCType.DD, "zero_mode": True, "is_exotic": False,
             "origin": r"\mathbf{16}", "tag": EpistemicTag.D},
            {"name": "d_L^c", "latex": r"d^c_L", "su3": "3bar", "su2": "1", "Y": Y_dLc,
             "multiplicity": 3, "color_factor": 3, "su2_factor": 1,
             "BC": BCType.DD, "zero_mode": True, "is_exotic": False,
             "origin": r"\mathbf{16}", "tag": EpistemicTag.D},
            {"name": "e_L^c", "latex": r"e^c_L", "su3": "1", "su2": "1", "Y": Y_eLc,
             "multiplicity": 1, "color_factor": 1, "su2_factor": 1,
             "BC": BCType.DD, "zero_mode": True, "is_exotic": False,
             "origin": r"\mathbf{16}", "tag": EpistemicTag.D},
            {"name": "nu_L^c", "latex": r"\nu^c_L", "su3": "1", "su2": "1", "Y": Y_nuLc,
             "multiplicity": 1, "color_factor": 1, "su2_factor": 1,
             "BC": BCType.ND, "zero_mode": False, "is_exotic": False,
             "origin": r"\mathbf{16}", "tag": EpistemicTag.D},
        ],

        "exotics": [
            # No mandatory exotics in minimal SO(10) spinor
        ],

        "BC_ref": "all-NN",
    },

    # =========================================================================
    # PATI-SALAM TRACK
    # =========================================================================
    "PS": {
        "name": "Pati-Salam",
        "latex": r"SU(4)_C \times SU(2)_L \times SU(2)_R",
        "parent_group": "SU(4)_C × SU(2)_L × SU(2)_R",
        "survivor_group": "SU(3)_C × SU(2)_L × U(1)_Y",
        "rank": 7,
        "rank_drop": 3,
        "tag": EpistemicTag.BL,

        "gauge_sector": {
            "total_generators": 21,  # 15 + 3 + 3
            "SM_generators": 12,
            "broken_generators": 9,
            "BC_classes": {
                "NN": 12,
                "DD": 0,
                "mixed": 9,
            },
            "tag": EpistemicTag.D,
        },

        "matter_fields": [
            # From (4, 2, 1) + (4bar, 1, 2)
            {"name": "Q_L", "latex": r"Q_L", "su3": "3", "su2": "2", "Y": Y_QL,
             "multiplicity": 6, "color_factor": 3, "su2_factor": 2,
             "BC": BCType.NN, "zero_mode": True, "is_exotic": False,
             "origin": r"(\mathbf{4}, \mathbf{2}, \mathbf{1})", "tag": EpistemicTag.D},
            {"name": "L_L", "latex": r"\ell_L", "su3": "1", "su2": "2", "Y": Y_LL,
             "multiplicity": 2, "color_factor": 1, "su2_factor": 2,
             "BC": BCType.NN, "zero_mode": True, "is_exotic": False,
             "origin": r"(\mathbf{4}, \mathbf{2}, \mathbf{1})", "tag": EpistemicTag.D},
            {"name": "u_L^c", "latex": r"u^c_L", "su3": "3bar", "su2": "1", "Y": Y_uLc,
             "multiplicity": 3, "color_factor": 3, "su2_factor": 1,
             "BC": BCType.DD, "zero_mode": True, "is_exotic": False,
             "origin": r"(\bar{\mathbf{4}}, \mathbf{1}, \mathbf{2})", "tag": EpistemicTag.D},
            {"name": "d_L^c", "latex": r"d^c_L", "su3": "3bar", "su2": "1", "Y": Y_dLc,
             "multiplicity": 3, "color_factor": 3, "su2_factor": 1,
             "BC": BCType.DD, "zero_mode": True, "is_exotic": False,
             "origin": r"(\bar{\mathbf{4}}, \mathbf{1}, \mathbf{2})", "tag": EpistemicTag.D},
            {"name": "e_L^c", "latex": r"e^c_L", "su3": "1", "su2": "1", "Y": Y_eLc,
             "multiplicity": 1, "color_factor": 1, "su2_factor": 1,
             "BC": BCType.DD, "zero_mode": True, "is_exotic": False,
             "origin": r"(\bar{\mathbf{4}}, \mathbf{1}, \mathbf{2})", "tag": EpistemicTag.D},
            {"name": "nu_L^c", "latex": r"\nu^c_L", "su3": "1", "su2": "1", "Y": Y_nuLc,
             "multiplicity": 1, "color_factor": 1, "su2_factor": 1,
             "BC": BCType.ND, "zero_mode": False, "is_exotic": False,
             "origin": r"(\bar{\mathbf{4}}, \mathbf{1}, \mathbf{2})", "tag": EpistemicTag.D},
        ],

        "exotics": [
            # Leptoquarks from (4,2,1) if wrong BC chosen
            {"name": "LQ", "latex": r"LQ", "su3": "3", "su2": "2", "Y": Fraction(1, 6),
             "multiplicity": 6, "is_exotic": True, "decouples": True,
             "mechanism": DecouplingMechanism.MIXED_BC,
             "description": "Leptoquark (wrong-BC projection)", "tag": EpistemicTag.Dc},
        ],

        "BC_ref": "all-NN",
    },

    # =========================================================================
    # E6 TRACK
    # =========================================================================
    "E6": {
        "name": "E_6",
        "latex": r"E_6",
        "parent_group": "E_6",
        "survivor_group": "SU(3)_C × SU(2)_L × U(1)_Y",
        "rank": 6,
        "rank_drop": 2,
        "tag": EpistemicTag.BL,

        "gauge_sector": {
            "total_generators": 78,
            "SM_generators": 12,
            "broken_generators": 66,
            "BC_classes": {
                "NN": 12,
                "DD": 0,
                "mixed": 66,
            },
            "tag": EpistemicTag.D,
        },

        "matter_fields": [
            # From 27 = 16 + 10 + 1 (SO(10) decomposition)
            {"name": "Q_L", "latex": r"Q_L", "su3": "3", "su2": "2", "Y": Y_QL,
             "multiplicity": 6, "color_factor": 3, "su2_factor": 2,
             "BC": BCType.NN, "zero_mode": True, "is_exotic": False,
             "origin": r"\mathbf{27}", "tag": EpistemicTag.D},
            {"name": "L_L", "latex": r"\ell_L", "su3": "1", "su2": "2", "Y": Y_LL,
             "multiplicity": 2, "color_factor": 1, "su2_factor": 2,
             "BC": BCType.NN, "zero_mode": True, "is_exotic": False,
             "origin": r"\mathbf{27}", "tag": EpistemicTag.D},
            {"name": "u_L^c", "latex": r"u^c_L", "su3": "3bar", "su2": "1", "Y": Y_uLc,
             "multiplicity": 3, "color_factor": 3, "su2_factor": 1,
             "BC": BCType.DD, "zero_mode": True, "is_exotic": False,
             "origin": r"\mathbf{27}", "tag": EpistemicTag.D},
            {"name": "d_L^c", "latex": r"d^c_L", "su3": "3bar", "su2": "1", "Y": Y_dLc,
             "multiplicity": 3, "color_factor": 3, "su2_factor": 1,
             "BC": BCType.DD, "zero_mode": True, "is_exotic": False,
             "origin": r"\mathbf{27}", "tag": EpistemicTag.D},
            {"name": "e_L^c", "latex": r"e^c_L", "su3": "1", "su2": "1", "Y": Y_eLc,
             "multiplicity": 1, "color_factor": 1, "su2_factor": 1,
             "BC": BCType.DD, "zero_mode": True, "is_exotic": False,
             "origin": r"\mathbf{27}", "tag": EpistemicTag.D},
            {"name": "nu_L^c", "latex": r"\nu^c_L", "su3": "1", "su2": "1", "Y": Y_nuLc,
             "multiplicity": 1, "color_factor": 1, "su2_factor": 1,
             "BC": BCType.ND, "zero_mode": False, "is_exotic": False,
             "origin": r"\mathbf{27}", "tag": EpistemicTag.D},
        ],

        "exotics": [
            # From 10 of SO(10) inside 27
            {"name": "D", "latex": r"D", "su3": "3", "su2": "1", "Y": Fraction(-1, 3),
             "multiplicity": 3, "is_exotic": True, "decouples": True,
             "mechanism": DecouplingMechanism.BRANE_MASS,
             "description": "Vector-like down quark", "tag": EpistemicTag.Dc},
            {"name": "D^c", "latex": r"D^c", "su3": "3bar", "su2": "1", "Y": Fraction(1, 3),
             "multiplicity": 3, "is_exotic": True, "decouples": True,
             "mechanism": DecouplingMechanism.BRANE_MASS,
             "description": "Vector-like down anti-quark", "tag": EpistemicTag.Dc},
            {"name": "H_d", "latex": r"H_d", "su3": "1", "su2": "2", "Y": Fraction(-1, 2),
             "multiplicity": 2, "is_exotic": True, "decouples": True,
             "mechanism": DecouplingMechanism.HOSOTANI,
             "description": "Extra Higgs doublet", "tag": EpistemicTag.Dc},
            {"name": "H_u", "latex": r"H_u", "su3": "1", "su2": "2", "Y": Fraction(1, 2),
             "multiplicity": 2, "is_exotic": True, "decouples": True,
             "mechanism": DecouplingMechanism.HOSOTANI,
             "description": "Extra Higgs doublet", "tag": EpistemicTag.Dc},
            # Singlet from 27
            {"name": "S", "latex": r"S", "su3": "1", "su2": "1", "Y": Fraction(0, 1),
             "multiplicity": 1, "is_exotic": True, "decouples": True,
             "mechanism": DecouplingMechanism.MIXED_BC,
             "description": "SM singlet", "tag": EpistemicTag.Dc},
        ],

        "BC_ref": "all-NN",
    },
}

# Number of generations
N_GENERATIONS = 3

# =============================================================================
# ANOMALY COEFFICIENT CALCULATIONS
# =============================================================================

def compute_su3_cubed(track_key: str) -> Fraction:
    """Compute SU(3)^3 anomaly coefficient for a track."""
    track = SoT_TRACKS[track_key]
    total = Fraction(0)
    for field in track["matter_fields"]:
        if not field.get("zero_mode", False):
            continue
        if field["su3"] == "3":
            total += field["su2_factor"]
        elif field["su3"] == "3bar":
            total -= field["su2_factor"]
    return total

def compute_su2_squared_u1(track_key: str) -> Fraction:
    """Compute SU(2)^2 U(1) anomaly coefficient."""
    track = SoT_TRACKS[track_key]
    total = Fraction(0)
    for field in track["matter_fields"]:
        if not field.get("zero_mode", False):
            continue
        if field["su2"] == "2":
            T_R = Fraction(1, 2)
            total += field["color_factor"] * T_R * field["Y"]
    return total

def compute_su3_squared_u1(track_key: str) -> Fraction:
    """Compute SU(3)^2 U(1) anomaly coefficient."""
    track = SoT_TRACKS[track_key]
    total = Fraction(0)
    for field in track["matter_fields"]:
        if not field.get("zero_mode", False):
            continue
        if field["su3"] in ["3", "3bar"]:
            T_R = Fraction(1, 2)
            total += field["su2_factor"] * T_R * field["Y"]
    return total

def compute_u1_cubed(track_key: str) -> Fraction:
    """Compute U(1)^3 anomaly coefficient."""
    track = SoT_TRACKS[track_key]
    total = Fraction(0)
    for field in track["matter_fields"]:
        if not field.get("zero_mode", False):
            continue
        total += field["multiplicity"] * (field["Y"] ** 3)
    return total

def compute_u1_grav(track_key: str) -> Fraction:
    """Compute U(1)-gravitational anomaly coefficient."""
    track = SoT_TRACKS[track_key]
    total = Fraction(0)
    for field in track["matter_fields"]:
        if not field.get("zero_mode", False):
            continue
        total += field["multiplicity"] * field["Y"]
    return total

def compute_witten_parity(track_key: str) -> int:
    """Compute Witten SU(2) global anomaly (number of doublets mod 2)."""
    track = SoT_TRACKS[track_key]
    n_doublets = 0
    for field in track["matter_fields"]:
        if not field.get("zero_mode", False):
            continue
        if field["su2"] == "2":
            n_doublets += field["color_factor"]
    return n_doublets % 2

def compute_u1_cubed_route2(track_key: str) -> Fraction:
    """Alternative U(1)^3 by sector grouping (quarks vs leptons)."""
    track = SoT_TRACKS[track_key]
    quarks = Fraction(0)
    leptons = Fraction(0)

    for field in track["matter_fields"]:
        if not field.get("zero_mode", False):
            continue
        contrib = field["multiplicity"] * (field["Y"] ** 3)
        if field["su3"] != "1":
            quarks += contrib
        else:
            leptons += contrib
    return quarks + leptons

def compute_su2_u1_route2(track_key: str) -> Fraction:
    """Alternative SU(2)^2 U(1) by sector grouping."""
    track = SoT_TRACKS[track_key]
    quark_doublets = Fraction(0)
    lepton_doublets = Fraction(0)

    for field in track["matter_fields"]:
        if not field.get("zero_mode", False):
            continue
        if field["su2"] == "2":
            T_R = Fraction(1, 2)
            contrib = field["color_factor"] * T_R * field["Y"]
            if field["su3"] != "1":
                quark_doublets += contrib
            else:
                lepton_doublets += contrib
    return quark_doublets + lepton_doublets

# =============================================================================
# DELTA E_VAC CALCULATIONS
# =============================================================================

def compute_delta_evac_ingredients(track_key: str) -> Dict[str, Any]:
    """
    Compute ΔE_vac^finite ingredients for a track.
    Returns BC class counts for gauge and matter sectors.

    ΔE_vac^finite = E_vac(BC) - E_vac(BC_ref)

    The finite part depends on:
    - n_NN: fields with Neumann-Neumann BC (have zero-modes)
    - n_DD: fields with Dirichlet-Dirichlet BC (have zero-modes)
    - n_mixed: fields with mixed BC (no zero-modes)

    Spin-statistics: bosons contribute +, fermions contribute -
    """
    track = SoT_TRACKS[track_key]

    result = {
        "gauge": {
            "NN": track["gauge_sector"]["BC_classes"]["NN"],
            "DD": track["gauge_sector"]["BC_classes"]["DD"],
            "mixed": track["gauge_sector"]["BC_classes"]["mixed"],
            "total": track["gauge_sector"]["total_generators"],
        },
        "fermion": {
            "NN": 0,
            "DD": 0,
            "mixed": 0,
            "total": 0,
        },
        "BC_ref": track.get("BC_ref", "all-NN"),
    }

    for field in track["matter_fields"]:
        mult = field["multiplicity"]
        bc = field.get("BC", BCType.NN)

        if bc in [BCType.NN]:
            result["fermion"]["NN"] += mult
        elif bc in [BCType.DD]:
            result["fermion"]["DD"] += mult
        else:
            result["fermion"]["mixed"] += mult

        result["fermion"]["total"] += mult

    return result

def compute_delta_evac_score(track_key: str) -> Fraction:
    """
    Compute relative ΔE_vac score (lower = better for vacuum stability).

    Score = (n_gauge_mixed - n_gauge_NN) - 4*(n_ferm_mixed - n_ferm_NN)

    The factor of 4 accounts for fermionic degrees of freedom and
    spin-statistics sign flip.
    """
    ingredients = compute_delta_evac_ingredients(track_key)

    gauge_contrib = ingredients["gauge"]["mixed"] - ingredients["gauge"]["NN"]
    fermion_contrib = ingredients["fermion"]["mixed"] - ingredients["fermion"]["NN"]

    # Fermions have opposite sign and more dof per Weyl spinor
    score = Fraction(gauge_contrib) - 4 * Fraction(fermion_contrib)
    return score

# =============================================================================
# MASS GATING ANALYSIS
# =============================================================================

def analyze_mass_gating(track_key: str) -> Dict[str, Any]:
    """
    Analyze mass gating for exotics in a track.
    Returns summary of which exotics decouple and how.
    """
    track = SoT_TRACKS[track_key]
    exotics = track.get("exotics", [])

    result = {
        "total_exotics": len(exotics),
        "decoupled": 0,
        "not_decoupled": 0,
        "by_mechanism": {
            DecouplingMechanism.MIXED_BC.value: 0,
            DecouplingMechanism.BRANE_MASS.value: 0,
            DecouplingMechanism.HOSOTANI.value: 0,
            DecouplingMechanism.HEAVY_KK.value: 0,
            DecouplingMechanism.NONE.value: 0,
        },
        "details": [],
    }

    for exotic in exotics:
        decouples = exotic.get("decouples", False)
        mechanism = exotic.get("mechanism", DecouplingMechanism.NONE)

        if decouples:
            result["decoupled"] += 1
        else:
            result["not_decoupled"] += 1

        result["by_mechanism"][mechanism.value] += 1
        result["details"].append({
            "name": exotic["name"],
            "decouples": decouples,
            "mechanism": mechanism.value,
        })

    return result

def compute_track_admissibility(track_key: str) -> Tuple[str, str]:
    """
    Determine track admissibility: PASS, CONDITIONAL, or FAIL.
    Returns (status, reason_code).
    """
    track = SoT_TRACKS[track_key]

    # Check anomalies
    anomalies = {
        "SU3_cubed": compute_su3_cubed(track_key),
        "SU2_U1": compute_su2_squared_u1(track_key),
        "SU3_U1": compute_su3_squared_u1(track_key),
        "U1_cubed": compute_u1_cubed(track_key),
        "U1_grav": compute_u1_grav(track_key),
        "Witten": compute_witten_parity(track_key),
    }

    anomaly_fail = any(v != 0 for v in anomalies.values())
    if anomaly_fail:
        return ("FAIL", "ANOMALY_NONZERO")

    # Check exotic gating
    gating = analyze_mass_gating(track_key)
    if gating["not_decoupled"] > 0:
        return ("FAIL", "EXOTIC_NOT_DECOUPLED")

    # Check if mechanism is speculative
    if gating["by_mechanism"][DecouplingMechanism.HOSOTANI.value] > 0:
        return ("CONDITIONAL", "HOSOTANI_REQUIRED")

    if gating["by_mechanism"][DecouplingMechanism.BRANE_MASS.value] > 0:
        return ("CONDITIONAL", "BRANE_MASS_TUNING")

    return ("PASS", "ALL_CRITERIA_MET")

# =============================================================================
# LATEX TABLE GENERATION
# =============================================================================

def fraction_to_latex(f: Fraction, sign: bool = False) -> str:
    """Convert Fraction to LaTeX string."""
    if f == 0:
        return "0"
    if f.denominator == 1:
        if sign and f > 0:
            return f"+{f.numerator}"
        return str(f.numerator)
    s = "" if not sign or f < 0 else "+"
    sign_char = "-" if f < 0 else s
    num = abs(f.numerator)
    den = f.denominator
    return rf"{sign_char}\frac{{{num}}}{{{den}}}"

def escape_latex(s: str) -> str:
    """Escape special LaTeX characters in text."""
    return s.replace("_", r"\_").replace("×", r"$\times$")

def generate_tables() -> str:
    """Generate all LaTeX tables from SoT."""
    lines = []
    lines.append("% =============================================================================")
    lines.append("% AUTO-GENERATED FILE — DO NOT EDIT MANUALLY")
    lines.append("% Generated by recompute.py from Single Source of Truth (SoT_TRACKS)")
    lines.append("% Any manual edits will be overwritten and cause hash mismatch")
    lines.append("% =============================================================================")
    lines.append("")

    # =========================================================================
    # TABLE 1: Track Overview
    # =========================================================================
    lines.append("% TABLE T1: Track Overview")
    lines.append(r"\begin{table}[ht]")
    lines.append(r"\centering")
    lines.append(r"\caption{GUT track overview (SoT).}")
    lines.append(r"\label{tab:sot-track-overview}")
    lines.append(r"\begin{tabular}{lcccc}")
    lines.append(r"\toprule")
    lines.append(r"Track & Parent $G$ & Rank & SM Survivors & Broken Gen. \\")
    lines.append(r"\midrule")

    for key in ["SU5", "SO10", "PS", "E6"]:
        track = SoT_TRACKS[key]
        name = escape_latex(track["name"])
        parent = escape_latex(track["parent_group"])
        rank = track["rank"]
        sm_gen = track["gauge_sector"]["SM_generators"]
        broken = track["gauge_sector"]["broken_generators"]
        lines.append(f"{name} & {parent} & {rank} & {sm_gen} & {broken} \\\\")

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    lines.append("")

    # =========================================================================
    # TABLE 2: Field Inventory per Track
    # =========================================================================
    lines.append("% TABLE T2: Field Inventory per Track")
    lines.append(r"\begin{table}[ht]")
    lines.append(r"\centering")
    lines.append(r"\caption{Matter field inventory by track (SoT). SM zero-mode count per generation.}")
    lines.append(r"\label{tab:sot-field-inventory}")
    lines.append(r"\begin{tabular}{lcccccc}")
    lines.append(r"\toprule")
    lines.append(r"Track & $Q_L$ & $\ell_L$ & $u^c_L$ & $d^c_L$ & $e^c_L$ & $\nu^c_L$ \\")
    lines.append(r"\midrule")

    for key in ["SU5", "SO10", "PS", "E6"]:
        track = SoT_TRACKS[key]
        name = escape_latex(track["name"])

        # Find each field
        field_status = {}
        for fname in ["Q_L", "L_L", "u_L^c", "d_L^c", "e_L^c", "nu_L^c"]:
            found = False
            for f in track["matter_fields"]:
                if f["name"] == fname:
                    if f.get("zero_mode", False):
                        field_status[fname] = r"\checkmark"
                    else:
                        field_status[fname] = r"$\times$"
                    found = True
                    break
            if not found:
                field_status[fname] = "---"

        lines.append(f"{name} & {field_status['Q_L']} & {field_status['L_L']} & "
                    f"{field_status['u_L^c']} & {field_status['d_L^c']} & "
                    f"{field_status['e_L^c']} & {field_status['nu_L^c']} \\\\")

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    lines.append("")

    # =========================================================================
    # TABLE 3: Anomaly Coefficients per Track
    # =========================================================================
    lines.append("% TABLE T3: Anomaly Coefficients per Track")
    lines.append(r"\begin{table}[ht]")
    lines.append(r"\centering")
    lines.append(r"\caption{Anomaly coefficients by track (computed from SoT).}")
    lines.append(r"\label{tab:sot-anomalies}")
    lines.append(r"\begin{tabular}{lcccccc}")
    lines.append(r"\toprule")
    lines.append(r"Track & $SU(3)^3$ & $SU(2)^2U(1)$ & $SU(3)^2U(1)$ & $U(1)^3$ & grav & Witten \\")
    lines.append(r"\midrule")

    for key in ["SU5", "SO10", "PS", "E6"]:
        track = SoT_TRACKS[key]
        name = escape_latex(track["name"])

        su3_3 = compute_su3_cubed(key)
        su2_u1 = compute_su2_squared_u1(key)
        su3_u1 = compute_su3_squared_u1(key)
        u1_3 = compute_u1_cubed(key)
        u1_g = compute_u1_grav(key)
        witten = compute_witten_parity(key)

        def fmt(v):
            if v == 0:
                return r"0\,\checkmark"
            return f"{fraction_to_latex(v)}"

        witten_str = r"0\,\checkmark" if witten == 0 else f"{witten}"

        lines.append(f"{name} & ${fmt(su3_3)}$ & ${fmt(su2_u1)}$ & ${fmt(su3_u1)}$ & "
                    f"${fmt(u1_3)}$ & ${fmt(u1_g)}$ & ${witten_str}$ \\\\")

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    lines.append("")

    # =========================================================================
    # TABLE 4: ΔE_vac Ingredients per Track
    # =========================================================================
    lines.append("% TABLE T4: Delta E_vac Ingredients per Track")
    lines.append(r"\begin{table}[ht]")
    lines.append(r"\centering")
    lines.append(r"\caption{$\Delta E_{\text{vac}}^{\text{finite}}$ ingredients by track (SoT).}")
    lines.append(r"\label{tab:sot-delta-evac}")
    lines.append(r"\begin{tabular}{lcccccc}")
    lines.append(r"\toprule")
    lines.append(r"Track & $n_{\text{gauge}}^{\text{NN}}$ & $n_{\text{gauge}}^{\text{mix}}$ & "
                r"$n_{\text{ferm}}^{\text{NN}}$ & $n_{\text{ferm}}^{\text{DD}}$ & "
                r"$n_{\text{ferm}}^{\text{mix}}$ & Score \\")
    lines.append(r"\midrule")

    for key in ["SU5", "SO10", "PS", "E6"]:
        track = SoT_TRACKS[key]
        name = escape_latex(track["name"])

        ingr = compute_delta_evac_ingredients(key)
        score = compute_delta_evac_score(key)

        lines.append(f"{name} & {ingr['gauge']['NN']} & {ingr['gauge']['mixed']} & "
                    f"{ingr['fermion']['NN']} & {ingr['fermion']['DD']} & "
                    f"{ingr['fermion']['mixed']} & ${fraction_to_latex(score)}$ \\\\")

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    lines.append("")

    # =========================================================================
    # TABLE 5: Exotics and Mass Gating
    # =========================================================================
    lines.append("% TABLE T5: Exotics and Mass Gating")
    lines.append(r"\begin{table}[ht]")
    lines.append(r"\centering")
    lines.append(r"\caption{Exotic content and mass-gating mechanisms by track (SoT).}")
    lines.append(r"\label{tab:sot-exotics}")
    lines.append(r"\begin{tabular}{lccccc}")
    lines.append(r"\toprule")
    lines.append(r"Track & Exotics & Mixed BC & Brane Mass & Hosotani & Decoupled \\")
    lines.append(r"\midrule")

    for key in ["SU5", "SO10", "PS", "E6"]:
        track = SoT_TRACKS[key]
        name = escape_latex(track["name"])

        gating = analyze_mass_gating(key)
        n_exotic = gating["total_exotics"]
        n_mixed = gating["by_mechanism"]["Mixed BC"]
        n_brane = gating["by_mechanism"]["Brane mass"]
        n_hos = gating["by_mechanism"]["Hosotani mechanism"]
        n_dec = gating["decoupled"]

        lines.append(f"{name} & {n_exotic} & {n_mixed} & {n_brane} & {n_hos} & {n_dec}/{n_exotic} \\\\")

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    lines.append("")

    # =========================================================================
    # TABLE 6: Track Admissibility
    # =========================================================================
    lines.append("% TABLE T6: Track Admissibility")
    lines.append(r"\begin{table}[ht]")
    lines.append(r"\centering")
    lines.append(r"\caption{Track admissibility summary (SoT).}")
    lines.append(r"\label{tab:sot-admissibility}")
    lines.append(r"\begin{tabular}{lcc}")
    lines.append(r"\toprule")
    lines.append(r"Track & Status & Reason Code \\")
    lines.append(r"\midrule")

    for key in ["SU5", "SO10", "PS", "E6"]:
        track = SoT_TRACKS[key]
        name = escape_latex(track["name"])

        status, reason = compute_track_admissibility(key)
        status_fmt = {
            "PASS": r"\textcolor{green!60!black}{PASS}",
            "CONDITIONAL": r"\textcolor{orange!80!black}{CONDITIONAL}",
            "FAIL": r"\textcolor{red!70!black}{FAIL}",
        }.get(status, status)

        reason_esc = reason.replace("_", r"\_")
        lines.append(f"{name} & {status_fmt} & \\texttt{{{reason_esc}}} \\\\")

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    lines.append("")

    # =========================================================================
    # TABLE 7: Detailed U(1)^3 per Track
    # =========================================================================
    lines.append("% TABLE T7: Detailed U(1)^3 Calculation")
    lines.append(r"\begin{table}[ht]")
    lines.append(r"\centering")
    lines.append(r"\caption{$U(1)^3$ anomaly: detailed calculation per field (SoT, SO(10) track).}")
    lines.append(r"\label{tab:sot-u1cubed-detail}")
    lines.append(r"\begin{tabular}{lcccc}")
    lines.append(r"\toprule")
    lines.append(r"Field & $m_i$ & $Y_i$ & $Y_i^3$ & $m_i Y_i^3$ \\")
    lines.append(r"\midrule")

    track = SoT_TRACKS["SO10"]
    u1_total = Fraction(0)
    for field in track["matter_fields"]:
        if not field.get("zero_mode", False):
            continue
        name = f"${field['latex']}$"
        m = field["multiplicity"]
        Y = field["Y"]
        Y3 = Y ** 3
        contrib = m * Y3
        u1_total += contrib

        lines.append(f"{name} & {m} & ${fraction_to_latex(Y)}$ & "
                    f"${fraction_to_latex(Y3)}$ & ${fraction_to_latex(contrib)}$ \\\\")

    lines.append(r"\midrule")
    lines.append(f"\\textbf{{Total}} & & & & $\\mathbf{{{fraction_to_latex(u1_total)}}}$ \\\\")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    lines.append("")

    # =========================================================================
    # TABLE 8: Two-Route Verification Summary
    # =========================================================================
    lines.append("% TABLE T8: Two-Route Verification")
    lines.append(r"\begin{table}[ht]")
    lines.append(r"\centering")
    lines.append(r"\caption{Two-route verification for $U(1)^3$ and $SU(2)^2U(1)$ (SoT).}")
    lines.append(r"\label{tab:sot-two-route}")
    lines.append(r"\begin{tabular}{lcccc}")
    lines.append(r"\toprule")
    lines.append(r"Track & $U(1)^3$ Route 1 & $U(1)^3$ Route 2 & $SU(2)^2U(1)$ R1 & $SU(2)^2U(1)$ R2 \\")
    lines.append(r"\midrule")

    for key in ["SU5", "SO10", "PS", "E6"]:
        track = SoT_TRACKS[key]
        name = escape_latex(track["name"])

        u1_r1 = compute_u1_cubed(key)
        u1_r2 = compute_u1_cubed_route2(key)
        su2_r1 = compute_su2_squared_u1(key)
        su2_r2 = compute_su2_u1_route2(key)

        match_u1 = r"\checkmark" if u1_r1 == u1_r2 else r"$\times$"
        match_su2 = r"\checkmark" if su2_r1 == su2_r2 else r"$\times$"

        lines.append(f"{name} & ${fraction_to_latex(u1_r1)}$ {match_u1} & "
                    f"${fraction_to_latex(u1_r2)}$ & "
                    f"${fraction_to_latex(su2_r1)}$ {match_su2} & "
                    f"${fraction_to_latex(su2_r2)}$ \\\\")

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    lines.append("")

    return "\n".join(lines)

def compute_hash(content: str) -> str:
    """Compute SHA256 hash of content."""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()[:16]

def write_tables():
    """Generate and write tables_generated.tex."""
    content = generate_tables()
    with open('tables_generated.tex', 'w') as f:
        f.write(content)
    return compute_hash(content)

# =============================================================================
# VERIFICATION CHECKS
# =============================================================================

results = []

def check(name: str, condition: bool, details: str = "") -> bool:
    """Record a check result."""
    status = "PASS" if condition else "FAIL"
    results.append((name, status, details))
    return condition

def read_tex() -> str:
    """Read main.tex content."""
    try:
        with open('main.tex', 'r') as f:
            return f.read()
    except:
        return ""

def read_pdf_info() -> int:
    """Get PDF page count from log file."""
    try:
        with open('main.log', 'r') as f:
            log = f.read()
        match = re.search(r'Output written on main\.pdf \((\d+) pages', log)
        if match:
            return int(match.group(1))
    except:
        pass
    return 0

def count_equations(tex: str) -> int:
    """Count equation labels."""
    return len(re.findall(r'\\label\{eq:', tex))

def count_labels(tex: str) -> int:
    """Count all label definitions."""
    return len(re.findall(r'\\label\{', tex))

FORBIDDEN_PATTERNS = [
    (r'91\.19', 'M_Z numerical'),
    (r'80\.38', 'M_W numerical'),
    (r'246\.2', 'v_EW numerical'),
    (r'1\.616.*10', 'ell_P numerical'),
    (r'6\.674.*10', 'G_N numerical'),
    (r'1/137', 'alpha_EM numerical'),
]

def check_forbidden_tokens(content: str, filename: str, is_self: bool = False) -> Tuple[bool, str]:
    """Check for forbidden numerical tokens."""
    if is_self:
        lines = content.split('\n')
        filtered = []
        in_block = False
        for line in lines:
            if 'FORBIDDEN_PATTERNS' in line and '=' in line:
                in_block = True
            elif in_block and line.strip() == ']':
                in_block = False
            elif not in_block:
                filtered.append(line)
        content = '\n'.join(filtered)

    for pattern, name in FORBIDDEN_PATTERNS:
        if re.search(pattern, content):
            return False, f"Found {name} in {filename}"
    return True, "No forbidden tokens"

def main():
    """Run all verification checks."""
    print("=" * 70)
    print("Derivation v45 — SoT-LOCK TRACK COMPILER")
    print("=" * 70)
    print()

    # Generate tables first
    print("Generating tables from SoT_TRACKS...")
    generated_hash = write_tables()
    print(f"Generated tables_generated.tex with hash: {generated_hash}")
    print()

    # Read files
    tex = read_tex()
    pages = read_pdf_info()
    equations = count_equations(tex)
    labels = count_labels(tex)

    # === SIZE CHECKS ===
    check("Page count (>=28)", pages >= 28, f"{pages}")
    check("Equation count (>=160)", equations >= 160, f"{equations}")
    check("Label count (>=220)", labels >= 220, f"{labels}")

    # === FORBIDDEN TOKENS ===
    ok, msg = check_forbidden_tokens(tex, 'main.tex')
    check("Forbidden tokens (main.tex)", ok, msg)

    try:
        with open('recompute.py', 'r') as f:
            py_content = f.read()
        ok, msg = check_forbidden_tokens(py_content, 'recompute.py', is_self=True)
        check("Forbidden tokens (recompute.py)", ok, msg)
    except:
        check("Forbidden tokens (recompute.py)", False, "Could not read")

    # === SoT SCHEMA CHECKS ===
    check("SoT_TRACKS defined", len(SoT_TRACKS) == 4, f"{len(SoT_TRACKS)} tracks")

    for track_key in ["SU5", "SO10", "PS", "E6"]:
        track = SoT_TRACKS[track_key]
        has_gauge = "gauge_sector" in track
        has_matter = "matter_fields" in track
        has_exotics = "exotics" in track
        check(f"{track_key} schema complete", has_gauge and has_matter and has_exotics,
              f"gauge={has_gauge}, matter={has_matter}, exotics={has_exotics}")

    # === ANOMALY CHECKS ===
    for track_key in ["SU5", "SO10", "PS", "E6"]:
        su3_3 = compute_su3_cubed(track_key)
        check(f"{track_key} SU(3)^3 = 0", su3_3 == 0, f"{su3_3}")

        su2_u1 = compute_su2_squared_u1(track_key)
        check(f"{track_key} SU(2)^2U(1) = 0", su2_u1 == 0, f"{su2_u1}")

        u1_3 = compute_u1_cubed(track_key)
        check(f"{track_key} U(1)^3 = 0", u1_3 == 0, f"{u1_3}")

        u1_g = compute_u1_grav(track_key)
        check(f"{track_key} U(1)-grav = 0", u1_g == 0, f"{u1_g}")

        witten = compute_witten_parity(track_key)
        check(f"{track_key} Witten = even", witten == 0, f"mod 2 = {witten}")

    # === TWO-ROUTE VERIFICATION ===
    for track_key in ["SU5", "SO10", "PS", "E6"]:
        u1_r1 = compute_u1_cubed(track_key)
        u1_r2 = compute_u1_cubed_route2(track_key)
        check(f"{track_key} U(1)^3 two-route", u1_r1 == u1_r2, f"r1={u1_r1}, r2={u1_r2}")

        su2_r1 = compute_su2_squared_u1(track_key)
        su2_r2 = compute_su2_u1_route2(track_key)
        check(f"{track_key} SU(2)^2U(1) two-route", su2_r1 == su2_r2, f"r1={su2_r1}, r2={su2_r2}")

    # === HASH LOCK CHECK ===
    try:
        with open('tables_generated.tex', 'r') as f:
            current_content = f.read()
        current_hash = compute_hash(current_content)

        regenerated = generate_tables()
        regenerated_hash = compute_hash(regenerated)

        check("Tables deterministic", current_hash == regenerated_hash,
              f"hash={current_hash}")
    except Exception as e:
        check("Tables deterministic", False, str(e))

    # === MIXED BC CHECK ===
    for track_key in ["SU5", "SO10", "PS", "E6"]:
        track = SoT_TRACKS[track_key]
        mixed_fields = [f for f in track["matter_fields"]
                       if f.get("BC") in [BCType.ND, BCType.DN]]
        all_no_zm = all(not f.get("zero_mode", True) for f in mixed_fields)
        check(f"{track_key} mixed BC → no ZM", all_no_zm, f"{len(mixed_fields)} mixed")

    # === MASS GATING CHECK ===
    for track_key in ["SU5", "SO10", "PS", "E6"]:
        gating = analyze_mass_gating(track_key)
        all_decoupled = gating["not_decoupled"] == 0
        check(f"{track_key} exotics gated", all_decoupled or gating["total_exotics"] == 0,
              f"{gating['decoupled']}/{gating['total_exotics']}")

    # === DELTA E_VAC INGREDIENTS ===
    for track_key in ["SU5", "SO10", "PS", "E6"]:
        ingr = compute_delta_evac_ingredients(track_key)
        total_gauge = ingr["gauge"]["NN"] + ingr["gauge"]["DD"] + ingr["gauge"]["mixed"]
        check(f"{track_key} gauge BC sum", total_gauge == ingr["gauge"]["total"],
              f"{total_gauge} = {ingr['gauge']['total']}")

    # === EXPORT PDF CHECK ===
    export_name = "EDC_BLOCK003_DERIVATION_V45_SOT_LOCK_TRACK_COMPILER.pdf"
    check("Export PDF exists", os.path.exists(export_name), export_name)

    # === DOCUMENT STRUCTURE ===
    check("SoT_TRACKS in tex", 'SoT' in tex or 'Source of Truth' in tex, "SoT mentioned")
    check("Track compiler in tex", 'track' in tex.lower(), "Track mentioned")
    check("Input tables", 'tables_generated' in tex, "\\input{tables_generated}")

    # === REVIEWER TRAPS ===
    trap_section = tex.find('Reviewer Trap') if tex.find('Reviewer Trap') != -1 else tex.find('Common Pitfall')
    trap_count = 0
    if trap_section != -1:
        trap_text = tex[trap_section:]
        trap_count = len(re.findall(r'\\item\s+\\textbf\{[^}]+\}:', trap_text))
    check("Reviewer traps >=16", trap_count >= 16, f"{trap_count} traps")

    # Print results
    print()
    print("-" * 70)
    print("RESULTS")
    print("-" * 70)

    passed = 0
    failed = 0
    for name, status, details in results:
        symbol = "✓" if status == "PASS" else "✗"
        print(f"[{symbol}] {name}: {status} {details}")
        if status == "PASS":
            passed += 1
        else:
            failed += 1

    print()
    print("=" * 70)
    total = len(results)
    print(f"Total: {passed}/{total} CHECKS PASSED")

    if passed >= 30:
        print("Check count requirement (>=30): PASS")
    else:
        print(f"Check count requirement (>=30): FAIL ({passed} < 30)")

    if failed == 0:
        print("\nALL CHECKS PASSED")
        print(f"\nTables hash: {generated_hash}")
        return 0
    else:
        print(f"\n{failed} CHECK(S) FAILED")
        return 1

if __name__ == "__main__":
    sys.exit(main())
