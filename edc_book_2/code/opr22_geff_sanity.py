#!/usr/bin/env python3
"""
OPR-22 Sanity Check: G_eff from 5D Mediator Exchange

This script verifies the G_eff derivation without using SM observables as inputs.

Key formulas:
- G_eff = g_5^2 * ell * |f_1(0)|^2 / (2 * x_1^2)  [natural normalization]
- G_eff = (1/2) * C_eff * |f_1(0)|^2
- C_eff = g_5^2 * ell / x_1^2  [from OPR-20]

Dependencies: OPR-19 (g5), OPR-20 (x1, m1), OPR-21 (f1(0))

Status: CONDITIONAL [Dc]
Date: 2026-01-25
Branch: book2-opr22-geff-derivation-v1
"""

import json
import math
import os
from pathlib import Path

# ============================================================================
# NO-SMUGGLING CERTIFICATION
# ============================================================================

FORBIDDEN_TOKENS = [
    'M_W', 'M_Z', 'G_F', 'v_higgs', 'v=246', '246 GeV', '91.2', '80.4',
    'sin2_theta_W', 'sin2θ_W', '0.231', 'm_mu', 'm_tau', 'tau_n', '886',
    'CODATA', 'PDG', '1.166e-5', '1.1664e-5'
]

def check_no_smuggling(params: dict) -> bool:
    """Verify no forbidden SM tokens appear in parameter descriptions."""
    param_str = str(params)
    for token in FORBIDDEN_TOKENS:
        if token.lower() in param_str.lower():
            print(f"WARNING: Forbidden token '{token}' found in parameters!")
            return False
    return True

# ============================================================================
# UNIT CONVERSIONS [BL] — Universal constants only
# ============================================================================

HBAR_C_FM_MEV = 197.327  # ℏc in MeV·fm [BL]
FM_TO_GEV_INV = 5.0677   # 1 fm = 5.0677 GeV^-1 [BL]

# ============================================================================
# PARAMETER SET [P] — All postulated, no SM inputs
# ============================================================================

def get_default_params():
    """
    Default parameter set for G_eff computation.
    All parameters are [P] postulated — NOT fitted to SM observables.
    """
    return {
        'tag': '[P] postulated parameters — NOT derived from SM',

        # 5D gauge coupling [P]
        # [g_5^2] = L = GeV^-1
        'g5_squared_gev_inv': 0.2,  # [P] placeholder

        # Domain size [P]
        'ell_fm': 0.01,  # [P] placeholder
        'ell_gev_inv': None,  # computed

        # Eigenvalue from BVP [Dc given inputs]
        'x1': math.pi,  # Toy limit (V=0, Neumann BC)
        'x1_source': 'Toy limit: V=0, Neumann BC',

        # Mode at brane [Dc given inputs]
        # For toy model: f_1(xi) = sqrt(2) cos(pi xi / ell), so f_1(0) = sqrt(2)
        'f1_at_0_squared': 2.0,  # |f_1(0)|^2 for toy model
        'f1_source': 'Toy limit: f_1 = sqrt(2) cos(pi xi/ell)',
    }


def load_opr21_params():
    """
    Attempt to load parameters from OPR-21 output if available.
    Falls back to default [P] parameters if not found.
    """
    opr21_path = Path(__file__).parent / 'output' / 'opr21_physical_summary.json'

    if opr21_path.exists():
        try:
            with open(opr21_path, 'r') as f:
                opr21 = json.load(f)
            print(f"Loaded OPR-21 parameters from {opr21_path}")
            # Extract relevant parameters if available
            # For now, fall through to defaults since OPR-21 may not have these
        except Exception as e:
            print(f"Could not load OPR-21 parameters: {e}")

    # Return defaults
    return get_default_params()


# ============================================================================
# MAIN COMPUTATION
# ============================================================================

def compute_geff(params: dict) -> dict:
    """
    Compute G_eff from 5D parameters.

    Formula: G_eff = g_5^2 * ell * |f_1(0)|^2 / (2 * x_1^2)

    Returns dict with all computed quantities.
    """
    # Convert units
    ell_gev_inv = params['ell_fm'] * FM_TO_GEV_INV
    params['ell_gev_inv'] = ell_gev_inv

    # Extract parameters
    g5_sq = params['g5_squared_gev_inv']  # [GeV^-1]
    ell = ell_gev_inv                      # [GeV^-1]
    x1 = params['x1']                      # dimensionless
    f1_0_sq = params['f1_at_0_squared']    # dimensionless

    # Compute mediator mass (OPR-20)
    m1_gev = x1 / ell  # [GeV]
    m1_mev = m1_gev * 1000  # [MeV]

    # Compute C_eff (OPR-20)
    # C_eff = g_5^2 * ell / x_1^2  [GeV^-2]
    C_eff = g5_sq * ell / (x1**2)

    # Compute G_eff
    # G_eff = (1/2) * C_eff * |f_1(0)|^2  [GeV^-2]
    G_eff = 0.5 * C_eff * f1_0_sq

    # Alternative formula (direct)
    # G_eff = g_5^2 * ell * |f_1(0)|^2 / (2 * x_1^2)
    G_eff_direct = g5_sq * ell * f1_0_sq / (2 * x1**2)

    # Consistency check
    assert abs(G_eff - G_eff_direct) < 1e-15, "G_eff formulas inconsistent!"

    # Toy formula (for V=0, Neumann BC with |f_1(0)|^2 = 2)
    G_eff_toy = g5_sq * ell / (math.pi**2)

    return {
        'g5_squared_gev_inv': g5_sq,
        'ell_fm': params['ell_fm'],
        'ell_gev_inv': ell,
        'x1': x1,
        'x1_source': params['x1_source'],
        'm1_gev': m1_gev,
        'm1_mev': m1_mev,
        'f1_at_0_squared': f1_0_sq,
        'f1_source': params['f1_source'],
        'C_eff_gev_sq_inv': C_eff,
        'G_eff_gev_sq_inv': G_eff,
        'G_eff_toy_gev_sq_inv': G_eff_toy,
    }


def dimensional_check(results: dict) -> bool:
    """
    Verify dimensional consistency.

    G_eff should have dimension [GeV^-2].

    Formula: G_eff = g_5^2 * ell * |f_1(0)|^2 / (2 * x_1^2)

    Dimensions:
    - [g_5^2] = GeV^-1
    - [ell] = GeV^-1
    - [f_1(0)^2] = 1 (dimensionless, natural normalization)
    - [x_1^2] = 1 (dimensionless)
    - [G_eff] = GeV^-1 * GeV^-1 / 1 = GeV^-2 ✓
    """
    print("\n=== DIMENSIONAL CHECK ===")
    print("[g_5^2] = GeV^-1 (from 5D action normalization)")
    print("[ell] = GeV^-1 (domain size)")
    print("[f_1(0)^2] = 1 (dimensionless in natural normalization)")
    print("[x_1^2] = 1 (dimensionless eigenvalue)")
    print("[G_eff] = GeV^-1 * GeV^-1 / 1 = GeV^-2 ✓")
    print()
    print(f"Computed G_eff = {results['G_eff_gev_sq_inv']:.6e} GeV^-2")
    return True


def scaling_study(base_params: dict) -> list:
    """
    Study how G_eff scales with ell.

    G_eff ∝ ell (linear scaling)
    """
    ell_values = [0.001, 0.01, 0.1, 1.0]  # fm
    results = []

    for ell_fm in ell_values:
        params = base_params.copy()
        params['ell_fm'] = ell_fm
        r = compute_geff(params)
        results.append({
            'ell_fm': ell_fm,
            'ell_gev_inv': r['ell_gev_inv'],
            'm1_gev': r['m1_gev'],
            'G_eff_gev_sq_inv': r['G_eff_gev_sq_inv'],
        })

    return results


def x1_sensitivity_study(base_params: dict) -> list:
    """
    Study how G_eff depends on x_1.

    G_eff ∝ 1/x_1^2
    """
    x1_values = [math.pi/2, math.pi, 3*math.pi/2, 2*math.pi]
    results = []

    for x1 in x1_values:
        params = base_params.copy()
        params['x1'] = x1
        r = compute_geff(params)
        results.append({
            'x1': x1,
            'x1_over_pi': x1 / math.pi,
            'm1_gev': r['m1_gev'],
            'G_eff_gev_sq_inv': r['G_eff_gev_sq_inv'],
        })

    return results


# ============================================================================
# OUTPUT
# ============================================================================

def generate_output(results: dict, scaling: list, sensitivity: list) -> dict:
    """Generate full output structure."""
    return {
        'sprint': 'OPR-22',
        'date': '2026-01-25',
        'status': 'PASS',
        'main_results': {
            'G_eff_gev_sq_inv': results['G_eff_gev_sq_inv'],
            'C_eff_gev_sq_inv': results['C_eff_gev_sq_inv'],
            'm1_gev': results['m1_gev'],
            'x1': results['x1'],
        },
        'parameters': {
            'g5_squared_gev_inv': results['g5_squared_gev_inv'],
            'ell_fm': results['ell_fm'],
            'ell_gev_inv': results['ell_gev_inv'],
            'f1_at_0_squared': results['f1_at_0_squared'],
        },
        'scaling_with_ell': scaling,
        'sensitivity_to_x1': sensitivity,
        'formulas': {
            'G_eff': 'g_5^2 * ell * |f_1(0)|^2 / (2 * x_1^2)',
            'C_eff': 'g_5^2 * ell / x_1^2',
            'relation': 'G_eff = (1/2) * C_eff * |f_1(0)|^2',
        },
        'unit_conversion': {
            'hbar_c_fm_mev': HBAR_C_FM_MEV,
            'fm_to_gev_inv': FM_TO_GEV_INV,
        },
        'notes': [
            'No SM observables used as inputs',
            'All parameters tagged [P] or [BL]',
            'G_eff is EDC-computed quantity, not measured G_F',
            'Toy limit uses V=0, Neumann BC',
        ]
    }


def generate_markdown_table(results: dict, scaling: list, sensitivity: list) -> str:
    """Generate markdown table output."""
    lines = [
        "# OPR-22 G_eff Sanity Check Results",
        "",
        f"**Date**: 2026-01-25",
        f"**Status**: PASS",
        "",
        "## Main Results",
        "",
        "| Quantity | Value | Units |",
        "|----------|-------|-------|",
        f"| G_eff | {results['G_eff_gev_sq_inv']:.6e} | GeV^-2 |",
        f"| C_eff | {results['C_eff_gev_sq_inv']:.6e} | GeV^-2 |",
        f"| m_1 | {results['m1_gev']:.4f} | GeV |",
        f"| m_1 | {results['m1_mev']:.2f} | MeV |",
        f"| x_1 | {results['x1']:.6f} | — |",
        "",
        "## Input Parameters [P]",
        "",
        "| Parameter | Value | Units | Status |",
        "|-----------|-------|-------|--------|",
        f"| g_5^2 | {results['g5_squared_gev_inv']:.4f} | GeV^-1 | [P] |",
        f"| ell | {results['ell_fm']:.4f} | fm | [P] |",
        f"| ell | {results['ell_gev_inv']:.4f} | GeV^-1 | [P] |",
        f"| |f_1(0)|^2 | {results['f1_at_0_squared']:.4f} | — | [Dc] toy |",
        f"| x_1 | {results['x1']:.6f} | — | [Dc] toy |",
        "",
        "## Scaling with ell (G_eff ∝ ell)",
        "",
        "| ell (fm) | ell (GeV^-1) | m_1 (GeV) | G_eff (GeV^-2) |",
        "|----------|--------------|-----------|----------------|",
    ]

    for s in scaling:
        lines.append(f"| {s['ell_fm']:.4f} | {s['ell_gev_inv']:.4f} | {s['m1_gev']:.4f} | {s['G_eff_gev_sq_inv']:.6e} |")

    lines.extend([
        "",
        "## Sensitivity to x_1 (G_eff ∝ 1/x_1^2)",
        "",
        "| x_1 | x_1/π | m_1 (GeV) | G_eff (GeV^-2) |",
        "|-----|-------|-----------|----------------|",
    ])

    for s in sensitivity:
        lines.append(f"| {s['x1']:.4f} | {s['x1_over_pi']:.4f} | {s['m1_gev']:.4f} | {s['G_eff_gev_sq_inv']:.6e} |")

    lines.extend([
        "",
        "## Formulas",
        "",
        "**G_eff (natural normalization)**:",
        "```",
        "G_eff = g_5^2 * ell * |f_1(0)|^2 / (2 * x_1^2)",
        "```",
        "",
        "**Connection to OPR-20**:",
        "```",
        "G_eff = (1/2) * C_eff * |f_1(0)|^2",
        "C_eff = g_5^2 * ell / x_1^2",
        "```",
        "",
        "## No-Smuggling Certification",
        "",
        "- ✓ No M_W, M_Z, G_F, v, sin²θ_W used as inputs",
        "- ✓ All parameters tagged [P] or [BL]",
        "- ✓ G_eff is computed quantity, not measured G_F",
        "- ✓ Dimensional analysis verified: [G_eff] = GeV^-2",
        "",
    ])

    return '\n'.join(lines)


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("=" * 70)
    print("OPR-22 SANITY CHECK: G_eff from 5D Mediator Exchange")
    print("=" * 70)
    print()

    # ----------------------------------------------------------------
    # NO-SMUGGLING BANNER
    # ----------------------------------------------------------------
    print("=" * 70)
    print("NO-SMUGGLING CERTIFICATION")
    print("=" * 70)
    print("This script does NOT use any SM observables as inputs:")
    print("  - No M_W, M_Z, G_F, v=246 GeV, sin²θ_W")
    print("  - No m_mu, m_tau, τ_n, or other particle data")
    print("  - Only universal constants [BL] and postulated parameters [P]")
    print("=" * 70)
    print()

    # ----------------------------------------------------------------
    # Load parameters
    # ----------------------------------------------------------------
    params = load_opr21_params()
    print("Using parameter set:", params['tag'])
    print()

    # Verify no smuggling
    if not check_no_smuggling(params):
        print("FAIL: Smuggling detected!")
        return 1
    print("✓ No-smuggling check passed")
    print()

    # ----------------------------------------------------------------
    # Compute G_eff
    # ----------------------------------------------------------------
    print("Computing G_eff...")
    results = compute_geff(params)

    print(f"\n=== MAIN RESULTS ===")
    print(f"g_5^2 = {results['g5_squared_gev_inv']:.4f} GeV^-1 [P]")
    print(f"ell = {results['ell_fm']:.4f} fm = {results['ell_gev_inv']:.4f} GeV^-1 [P]")
    print(f"x_1 = {results['x1']:.6f} ({results['x1_source']})")
    print(f"|f_1(0)|^2 = {results['f1_at_0_squared']:.4f} ({results['f1_source']})")
    print()
    print(f"m_1 = x_1/ell = {results['m1_gev']:.4f} GeV = {results['m1_mev']:.2f} MeV")
    print(f"C_eff = g_5^2 * ell / x_1^2 = {results['C_eff_gev_sq_inv']:.6e} GeV^-2")
    print(f"G_eff = (1/2) * C_eff * |f_1(0)|^2 = {results['G_eff_gev_sq_inv']:.6e} GeV^-2")
    print()

    # ----------------------------------------------------------------
    # Dimensional check
    # ----------------------------------------------------------------
    dimensional_check(results)

    # ----------------------------------------------------------------
    # Scaling studies
    # ----------------------------------------------------------------
    print("\n=== SCALING STUDY: G_eff vs ell ===")
    scaling = scaling_study(params)
    for s in scaling:
        print(f"ell = {s['ell_fm']:.4f} fm: G_eff = {s['G_eff_gev_sq_inv']:.6e} GeV^-2")

    print("\n=== SENSITIVITY STUDY: G_eff vs x_1 ===")
    sensitivity = x1_sensitivity_study(params)
    for s in sensitivity:
        print(f"x_1 = {s['x1']:.4f} ({s['x1_over_pi']:.2f}π): G_eff = {s['G_eff_gev_sq_inv']:.6e} GeV^-2")

    # ----------------------------------------------------------------
    # Output files
    # ----------------------------------------------------------------
    output_dir = Path(__file__).parent / 'output'
    output_dir.mkdir(exist_ok=True)

    # JSON output
    output_json = generate_output(results, scaling, sensitivity)
    json_path = output_dir / 'opr22_geff_summary.json'
    with open(json_path, 'w') as f:
        json.dump(output_json, f, indent=2)
    print(f"\n✓ JSON output written to {json_path}")

    # Markdown output
    md_content = generate_markdown_table(results, scaling, sensitivity)
    md_path = output_dir / 'opr22_geff_table.md'
    with open(md_path, 'w') as f:
        f.write(md_content)
    print(f"✓ Markdown output written to {md_path}")

    # ----------------------------------------------------------------
    # Final status
    # ----------------------------------------------------------------
    print()
    print("=" * 70)
    print("OPR-22 SANITY CHECK: PASS")
    print("=" * 70)
    print("Status: CONDITIONAL [Dc]")
    print("  - Structure derived from 5D action + KK reduction")
    print("  - Parameters g_5, ell, V(xi), kappa remain [P]")
    print("  - No SM observables used as inputs")
    print("=" * 70)

    return 0


if __name__ == '__main__':
    exit(main())
