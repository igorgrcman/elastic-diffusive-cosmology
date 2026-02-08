#!/usr/bin/env python3
"""
PREFACTOR SENSITIVITY TEST ON FULL V7.8 DATASET
================================================
Test n(A) = p × A^(1/3) with p ∈ {6.0, 6.05, 6.1, 6.15, 6.2}
on the full ALPHA100 dataset (106 nuclides, A ≤ 257).

Purpose: Determine optimal prefactor for both actinide and superheavy regimes.
"""

import math
import csv
from typing import List, Dict, Tuple

# =============================================================================
# V7.8 M2 FITTED COEFFICIENTS
# =============================================================================

COEF = {
    'a': 1.593,
    'g': -1.643,
    'c1': 1.121,
    'c2': 1.538,
    'b': -50.77,
}

# =============================================================================
# COORDINATION LAW
# =============================================================================

def generate_allowed_n(max_n: int = 150) -> List[int]:
    allowed = set()
    a = 0
    while 2**a <= max_n:
        b = 0
        while 2**a * 3**b <= max_n:
            allowed.add(2**a * 3**b)
            b += 1
        a += 1
    return sorted(allowed)

ALLOWED_N = generate_allowed_n(150)

def calc_d_n(n_A: float) -> float:
    distances = [abs(n_A - k) for k in ALLOWED_N]
    return min(distances)

def calc_n_A(A: int, prefactor: float) -> float:
    return prefactor * (A ** (1/3))

# =============================================================================
# LOAD ALPHA100 DATASET
# =============================================================================

def load_alpha100(filepath: str) -> List[Dict]:
    """Load ALPHA100 CSV dataset."""
    data = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Skip hindered decays for clean comparison
            if row['hindrance_class'] in ['H1', 'H2']:
                continue

            try:
                data.append({
                    'nuclide': row['nuclide'],
                    'Z': int(row['Z']),
                    'A': int(row['A']),
                    't12_s': float(row['t12_seconds']),
                    'Q_keV': float(row['Qalpha_keV']),
                    'hindrance': row['hindrance_class'],
                })
            except (ValueError, KeyError):
                continue
    return data

# =============================================================================
# PREDICTION AND EVALUATION
# =============================================================================

def predict_log_t(Z: int, A: int, Q_keV: float, prefactor: float) -> Tuple[float, float, float]:
    """
    Returns: (log_t_GN, log_t_full, d_n)
    """
    Z_d = Z - 2
    Q_MeV = Q_keV / 1000.0
    sqrt_Q = math.sqrt(Q_MeV)
    gn_var = Z_d / sqrt_Q

    n_A = calc_n_A(A, prefactor)
    d_n = calc_d_n(n_A)

    log_t_GN = COEF['a'] * gn_var + COEF['b']
    log_t_full = log_t_GN + COEF['g'] * d_n

    return log_t_GN, log_t_full, d_n

def evaluate_prefactor(data: List[Dict], prefactor: float) -> Dict:
    """Evaluate model performance for a given prefactor."""
    results = []

    for d in data:
        log_t_exp = math.log10(d['t12_s'])
        log_t_GN, log_t_full, d_n = predict_log_t(d['Z'], d['A'], d['Q_keV'], prefactor)

        delta_GN = abs(log_t_exp - log_t_GN)
        delta_full = abs(log_t_exp - log_t_full)

        results.append({
            'nuclide': d['nuclide'],
            'Z': d['Z'],
            'A': d['A'],
            'log_t_exp': log_t_exp,
            'log_t_GN': log_t_GN,
            'log_t_full': log_t_full,
            'd_n': d_n,
            'delta_GN': delta_GN,
            'delta_full': delta_full,
        })

    # Calculate statistics
    delta_GN_vals = [r['delta_GN'] for r in results]
    delta_full_vals = [r['delta_full'] for r in results]

    # R² calculation (for full model)
    log_t_exp_vals = [r['log_t_exp'] for r in results]
    log_t_pred_vals = [r['log_t_full'] for r in results]

    mean_exp = sum(log_t_exp_vals) / len(log_t_exp_vals)
    ss_tot = sum((y - mean_exp)**2 for y in log_t_exp_vals)
    ss_res = sum((y - p)**2 for y, p in zip(log_t_exp_vals, log_t_pred_vals))
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0

    # RMSE
    rmse = math.sqrt(ss_res / len(results))

    return {
        'prefactor': prefactor,
        'n': len(results),
        'mean_delta_GN': sum(delta_GN_vals) / len(delta_GN_vals),
        'mean_delta_full': sum(delta_full_vals) / len(delta_full_vals),
        'max_delta_full': max(delta_full_vals),
        'r2': r2,
        'rmse': rmse,
        'pass_rate_1.5': sum(1 for d in delta_full_vals if d < 1.5) / len(delta_full_vals),
        'results': results,
    }

def analyze_by_region(results: List[Dict], prefactor: float) -> Dict:
    """Analyze by mass region."""
    regions = {
        'Light (A<220)': [r for r in results if r['A'] < 220],
        'Actinide (220≤A<240)': [r for r in results if 220 <= r['A'] < 240],
        'Transuranium (A≥240)': [r for r in results if r['A'] >= 240],
    }

    analysis = {}
    for name, subset in regions.items():
        if not subset:
            continue
        delta_vals = [r['delta_full'] for r in subset]
        analysis[name] = {
            'n': len(subset),
            'mean_delta': sum(delta_vals) / len(delta_vals),
            'pass_rate': sum(1 for d in delta_vals if d < 1.5) / len(delta_vals),
        }

    return analysis

# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    import os

    # Find dataset
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(script_dir, '..', '..', '..', 'audit',
                                'radioactivity_v7_4_alpha100', '04_ALPHA100_DATASET.csv')

    if not os.path.exists(dataset_path):
        # Try alternative path
        dataset_path = '/Users/igor/ClaudeAI/EDC_Project/elastic-diffusive-cosmology_repo/edc_book_2/audit/radioactivity_v7_4_alpha100/04_ALPHA100_DATASET.csv'

    print("="*70)
    print("PREFACTOR SENSITIVITY TEST ON FULL V7.8 DATASET (H0 only)")
    print("="*70)

    # Load data
    data = load_alpha100(dataset_path)
    print(f"\nLoaded {len(data)} H0 nuclides from ALPHA100 dataset")
    print(f"A range: {min(d['A'] for d in data)} - {max(d['A'] for d in data)}")

    # Test prefactors
    prefactors = [5.9, 5.95, 6.0, 6.05, 6.1, 6.15, 6.2]

    print("\n" + "-"*70)
    print("GLOBAL RESULTS")
    print("-"*70)
    print(f"{'p':>6} {'N':>4} {'Mean Δ(GN)':>10} {'Mean Δ(full)':>12} {'Max Δ':>7} {'R²':>7} {'RMSE':>6} {'Pass%':>7}")
    print("-"*70)

    all_results = {}
    for p in prefactors:
        stats = evaluate_prefactor(data, p)
        all_results[p] = stats

        marker = " *" if p == 6.1 else (" ◆" if p == 6.0 else "")
        print(f"{p:>6.2f} {stats['n']:>4} {stats['mean_delta_GN']:>10.3f} "
              f"{stats['mean_delta_full']:>12.3f} {stats['max_delta_full']:>7.2f} "
              f"{stats['r2']:>7.4f} {stats['rmse']:>6.3f} {stats['pass_rate_1.5']*100:>6.1f}%{marker}")

    print("\n* = current default (6.1)")
    print("◆ = proposed for superheavy (6.0)")

    # Regional analysis for key prefactors
    print("\n" + "-"*70)
    print("REGIONAL ANALYSIS (by mass range)")
    print("-"*70)

    for p in [6.0, 6.1]:
        print(f"\n--- Prefactor = {p} ---")
        regions = analyze_by_region(all_results[p]['results'], p)
        for name, stats in regions.items():
            print(f"  {name:25s}: n={stats['n']:>3}, mean Δ={stats['mean_delta']:.3f}, pass={stats['pass_rate']*100:.1f}%")

    # Heavy element detail (U, Pu, Cm, Cf)
    print("\n" + "-"*70)
    print("HEAVY ELEMENT DETAIL (U, Pu, Cm, Cf)")
    print("-"*70)

    heavy_elements = ['U-', 'Pu-', 'Cm-', 'Cf-']

    for p in [6.0, 6.1]:
        print(f"\n--- Prefactor = {p} ---")
        print(f"{'Nuclide':<10} {'A':>4} {'d(n)':>6} {'log t exp':>10} {'log t pred':>10} {'Δ':>6}")

        for r in all_results[p]['results']:
            if any(r['nuclide'].startswith(el) for el in heavy_elements):
                print(f"{r['nuclide']:<10} {r['A']:>4} {r['d_n']:>6.2f} "
                      f"{r['log_t_exp']:>10.2f} {r['log_t_full']:>10.2f} {r['delta_full']:>6.2f}")

    # Conclusion
    print("\n" + "="*70)
    print("CONCLUSION")
    print("="*70)

    r2_6_0 = all_results[6.0]['r2']
    r2_6_1 = all_results[6.1]['r2']
    rmse_6_0 = all_results[6.0]['rmse']
    rmse_6_1 = all_results[6.1]['rmse']

    print(f"\np=6.0: R²={r2_6_0:.4f}, RMSE={rmse_6_0:.3f}")
    print(f"p=6.1: R²={r2_6_1:.4f}, RMSE={rmse_6_1:.3f}")

    if r2_6_0 > r2_6_1:
        print("\n→ p=6.0 gives BETTER global fit (higher R², lower RMSE)")
    elif r2_6_0 < r2_6_1:
        print("\n→ p=6.1 gives better global fit")
    else:
        print("\n→ Similar performance")

    print("\n" + "="*70)
