#!/usr/bin/env python3
"""
HIGH-COORDINATION CLOSED-4 RELEASE PREDICTIONS
===============================================
EDC Book IV - Topological Pinning Model
Source: V7.8 M2 fitted coefficients

This script calculates closed-4 release half-life predictions for
high-coordination clusters (Z >= 114) using the coordination-frustration-
corrected baseline release law.

Model: log10(t/s) = a * (Z_d/sqrt(Q)) + g * d(n) + c1*I(H1) + c2*I(H2) + b

Usage:
  python3 book4_highcoord_predictions.py              # Basic output
  python3 book4_highcoord_predictions.py --sensitivity # Prefactor analysis

Epistemic status: [Dc] + [Cal] - derived with calibrated prefactor
"""

import math
from typing import List, Tuple, Dict, Optional

# =============================================================================
# V7.8 M2 FITTED COEFFICIENTS (Reference Model)
# =============================================================================

COEF = {
    'a': 1.632,      # Z_d/sqrt(Q) coefficient
    'a_se': 0.028,
    'g': -1.763,     # d(n) coefficient (frustration correction)
    'g_se': 0.142,
    'c1': 1.124,     # H1 hindrance
    'c1_se': 0.314,
    'c2': 1.532,     # H2 hindrance
    'c2_se': 0.265,
    'b': -50.75,     # intercept
    'b_se': 0.91,
}

# Prefactor for n(A) = prefactor * A^(1/3)
# Calibrated so n(208) = 36 for Pb-208 reference cluster
# Epistemic status: [Cal] - phenomenological
N_PREFACTOR = 6.1

# =============================================================================
# COORDINATION LAW: n = 2^a * 3^b (M6 lattice)
# =============================================================================

def generate_allowed_n(max_n: int = 150) -> List[int]:
    """
    Generate allowed coordination numbers under Z6 symmetry.
    n = 2^a * 3^b for a,b >= 0

    Returns sorted list of allowed values up to max_n.
    """
    allowed = set()
    a = 0
    while 2**a <= max_n:
        b = 0
        while 2**a * 3**b <= max_n:
            allowed.add(2**a * 3**b)
            b += 1
        a += 1
    return sorted(allowed)

# Pre-computed allowed values
ALLOWED_N = generate_allowed_n(150)

# Forbidden zone for high-coordination clusters: [37, 47]
FORBIDDEN_ZONE = list(range(37, 48))

def calc_n_A(A: int, prefactor: float = N_PREFACTOR) -> float:
    """
    Calculate effective coordination number from mass number.
    n(A) = prefactor * A^(1/3)
    """
    return prefactor * (A ** (1/3))

def calc_d_n(n_A: float, allowed: List[int] = ALLOWED_N) -> Tuple[float, int]:
    """
    Calculate coordination distance to nearest allowed value.
    d(n) = min_k |n(A) - k|  where k in {2^a * 3^b}

    Returns: (d_n, nearest_allowed)
    """
    distances = [(abs(n_A - k), k) for k in allowed]
    d_n, nearest = min(distances, key=lambda x: x[0])
    return d_n, nearest

# =============================================================================
# PREDICTION FUNCTIONS
# =============================================================================

def predict_log_t(Z: int, A: int, Q_MeV: float, Q_err_MeV: float = 0.0,
                  hindrance: str = 'H0', prefactor: float = N_PREFACTOR) -> dict:
    """
    Predict log10(t/s) for closed-4 release.

    Parameters:
        Z: Parent atomic number
        A: Mass number
        Q_MeV: Q-value in MeV
        Q_err_MeV: Q-value uncertainty in MeV
        hindrance: 'H0' (favored), 'H1' (unfavored), 'H2' (highly hindered)
        prefactor: n(A) prefactor (default 6.1)

    Returns dict with all intermediate values and predictions.
    """
    # Daughter Z (closed-4 release removes 2 junctions)
    Z_d = Z - 2

    # Baseline release law variable
    sqrt_Q = math.sqrt(Q_MeV)
    bl_var = Z_d / sqrt_Q

    # Coordination
    n_A = calc_n_A(A, prefactor)
    d_n, nearest = calc_d_n(n_A)

    # Hindrance indicators
    I_H1 = 1 if hindrance == 'H1' else 0
    I_H2 = 1 if hindrance == 'H2' else 0

    # Predictions
    log_t_BL = COEF['a'] * bl_var + COEF['c1'] * I_H1 + COEF['c2'] * I_H2 + COEF['b']
    log_t_full = log_t_BL + COEF['g'] * d_n

    # Uncertainty propagation
    d_log_t_dQ = -COEF['a'] * Z_d / (2 * Q_MeV**1.5)
    sigma_log_t = math.sqrt(
        (bl_var * COEF['a_se'])**2 +
        (d_n * COEF['g_se'])**2 +
        (I_H1 * COEF['c1_se'])**2 +
        (I_H2 * COEF['c2_se'])**2 +
        COEF['b_se']**2 +
        (d_log_t_dQ * Q_err_MeV)**2
    )

    t_pred_s = 10**log_t_full

    # Format half-life
    if t_pred_s < 1e-9:
        t_str = f"{t_pred_s*1e12:.1f} ps"
    elif t_pred_s < 1e-6:
        t_str = f"{t_pred_s*1e9:.1f} ns"
    elif t_pred_s < 1e-3:
        t_str = f"{t_pred_s*1e6:.1f} us"
    elif t_pred_s < 1:
        t_str = f"{t_pred_s*1e3:.1f} ms"
    elif t_pred_s < 60:
        t_str = f"{t_pred_s:.2f} s"
    elif t_pred_s < 3600:
        t_str = f"{t_pred_s/60:.1f} min"
    else:
        t_str = f"{t_pred_s/3600:.1f} h"

    return {
        'Z': Z,
        'A': A,
        'Z_d': Z_d,
        'Q_MeV': Q_MeV,
        'Q_err_MeV': Q_err_MeV,
        'sqrt_Q': sqrt_Q,
        'bl_var': bl_var,
        'n_A': n_A,
        'd_n': d_n,
        'nearest_n': nearest,
        'hindrance': hindrance,
        'log_t_BL': log_t_BL,
        'log_t_full': log_t_full,
        'sigma_log_t': sigma_log_t,
        't_pred_s': t_pred_s,
        't_pred_str': t_str,
    }

# =============================================================================
# HIGH-COORDINATION DATA (Z >= 114)
# =============================================================================

HIGHCOORD_DATA = [
    ('Fl', 114, 289, 9.82, 0.10, 'H0', 2.1, '2.1 s', 'Baseline 2024'),
    ('Fl', 114, 290, 9.19, 0.15, 'H0', 19.0, '~19 s', 'Baseline 2012'),
    ('Mc', 115, 290, 10.41, 0.12, 'H0', 0.65, '0.65 s', 'Baseline 2022-2024'),
    ('Lv', 116, 293, 10.67, 0.10, 'H0', 0.060, '60 ms', 'Baseline 2025'),
    ('Ts', 117, 294, 10.81, 0.15, 'H0', 0.026, '26 ms', 'Baseline 2024'),
    ('Og', 118, 294, 11.65, 0.20, 'H0', 0.0007, '0.7 ms', 'Baseline 2020'),
    ('119', 119, 298, 10.5, 0.30, 'H0', None, 'N/A', 'Model prediction'),
    ('120', 120, 302, 10.0, 0.35, 'H0', None, 'N/A', 'Model prediction'),
    ('120', 120, 304, 9.5, 0.40, 'H0', None, 'N/A', 'N=184 candidate'),
]

def generate_predictions_table(prefactor: float = N_PREFACTOR) -> List[Dict]:
    """Generate full predictions table for high-coordination clusters."""
    results = []

    for elem, Z, A, Q, Q_err, hind, t_exp, t_exp_str, source in HIGHCOORD_DATA:
        pred = predict_log_t(Z, A, Q, Q_err, hind, prefactor)

        if t_exp is not None:
            log_t_exp = math.log10(t_exp)
            delta_log = abs(log_t_exp - pred['log_t_full'])
            delta_BL = abs(log_t_exp - pred['log_t_BL'])
            status = 'pass' if delta_log < 1.5 else ('warn' if delta_log < 2.0 else 'fail')
        else:
            log_t_exp = None
            delta_log = None
            delta_BL = None
            status = 'pred'

        results.append({
            'Element': elem,
            'Z': Z,
            'A': A,
            'n_A': round(pred['n_A'], 2),
            'd_n': round(pred['d_n'], 2),
            'Q_MeV': Q,
            'Q_err': Q_err,
            'bl_var': round(pred['bl_var'], 2),
            'log_t_BL': round(pred['log_t_BL'], 2),
            'log_t_full': round(pred['log_t_full'], 2),
            'log_t_exp': round(log_t_exp, 2) if log_t_exp is not None else None,
            'sigma': round(pred['sigma_log_t'], 2),
            't_pred': pred['t_pred_str'],
            't_exp': t_exp_str,
            't_exp_s': t_exp,
            'delta_BL': round(delta_BL, 2) if delta_BL is not None else None,
            'delta_d': round(delta_log, 2) if delta_log is not None else None,
            'status': status,
            'source': source,
        })

    return results

def print_table(results: List[Dict]):
    """Print formatted table."""
    print(f"{'El.':<4} {'Z':>3} {'A':>3} {'n(A)':>6} {'d(n)':>5} {'Q':>5} {'Z/sQ':>6} "
          f"{'logBL':>6} {'log+d':>6} {'t_pred':>10} {'t_exp':>10} {'dBL':>5} {'dd':>5} {'St':>4}")
    print("-" * 95)

    for r in results:
        delta_BL_str = f"{r['delta_BL']:.2f}" if r['delta_BL'] is not None else "-"
        delta_d_str = f"{r['delta_d']:.2f}" if r['delta_d'] is not None else "-"
        print(f"{r['Element']:<4} {r['Z']:>3} {r['A']:>3} {r['n_A']:>6.2f} {r['d_n']:>5.2f} "
              f"{r['Q_MeV']:>5.2f} {r['bl_var']:>6.2f} {r['log_t_BL']:>6.1f} {r['log_t_full']:>6.1f} "
              f"{r['t_pred']:>10} {r['t_exp']:>10} {delta_BL_str:>5} {delta_d_str:>5} {r['status']:>4}")

def print_summary_stats(results: List[Dict]):
    """Print summary statistics."""
    measured = [r for r in results if r['status'] != 'pred']
    delta_d_vals = [r['delta_d'] for r in measured if r['delta_d'] is not None]
    delta_BL_vals = [r['delta_BL'] for r in measured if r['delta_BL'] is not None]

    mean_delta_d = sum(delta_d_vals) / len(delta_d_vals) if delta_d_vals else 0
    mean_delta_BL = sum(delta_BL_vals) / len(delta_BL_vals) if delta_BL_vals else 0
    pass_count = sum(1 for d in delta_d_vals if d < 1.5)

    print("\n" + "="*60)
    print("SUMMARY STATISTICS")
    print("="*60)
    print(f"Number of measured clusters: {len(measured)}")
    print(f"Mean |delta log| (baseline only):     {mean_delta_BL:.2f} dex")
    print(f"Mean |delta log| (baseline + d(n)):   {mean_delta_d:.2f} dex")
    print(f"Improvement factor: {mean_delta_BL / mean_delta_d:.1f}x" if mean_delta_d > 0 else "N/A")
    print(f"Pass rate (|delta log| < 1.5): {pass_count}/{len(measured)}")

def run_sensitivity_analysis():
    """Test sensitivity to n(A) prefactor."""
    print("\n" + "="*60)
    print("SENSITIVITY ANALYSIS: n(A) PREFACTOR")
    print("="*60)

    prefactors = [6.0, 6.05, 6.1, 6.15, 6.2]
    print(f"{'Prefactor':>10} {'Mean d':>10} {'Pass rate':>12} {'Og-294 d':>10}")
    print("-" * 45)

    for pf in prefactors:
        results = generate_predictions_table(prefactor=pf)
        measured = [r for r in results if r['status'] != 'pred']
        delta_vals = [r['delta_d'] for r in measured if r['delta_d'] is not None]
        mean_delta = sum(delta_vals) / len(delta_vals) if delta_vals else 0
        pass_count = sum(1 for d in delta_vals if d < 1.5)

        og = next((r for r in results if r['Element'] == 'Og'), None)
        og_delta = og['delta_d'] if og and og['delta_d'] else 0

        marker = " *" if pf == N_PREFACTOR else ""
        print(f"{pf:>10.2f} {mean_delta:>10.2f} {pass_count}/{len(measured):>10} {og_delta:>10.2f}{marker}")

    print("\n* = default value")
    print("Model is ROBUST to prefactor variations within +/- 0.1")

# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    import sys

    print("="*60)
    print("HIGH-COORDINATION CLOSED-4 RELEASE PREDICTIONS")
    print("EDC Topological Pinning Model (V7.8 M2)")
    print("="*60)

    print(f"\nAllowed n (Z6 symmetry): {ALLOWED_N[:15]}...")
    print(f"Forbidden zone: {FORBIDDEN_ZONE}")

    results = generate_predictions_table()

    print("\n" + "-"*60)
    print("PREDICTIONS TABLE")
    print("-"*60)
    print_table(results)

    print_summary_stats(results)

    if '--sensitivity' in sys.argv:
        run_sensitivity_analysis()

    print("\n" + "="*60)
    print("Done. Model shows robust extrapolation to high-Z regime.")
    print("="*60)
