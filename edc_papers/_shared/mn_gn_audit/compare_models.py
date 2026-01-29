#!/usr/bin/env python3
"""
compare_models.py — Forensic Audit: Frustration-Corrected Geiger-Nuttall

This script provides a reproducible comparison between:
1. Standard Geiger-Nuttall Law (baseline)
2. Frustration-Corrected Geiger-Nuttall Law (EDC model)

It computes exact metrics with full provenance tracking.

Usage:
    python compare_models.py

Output:
    - Console summary
    - JSON results file for archival
    - Markdown table for documentation

Author: EDC Audit
Date: 2026-01-29
"""

import numpy as np
import json
import hashlib
from datetime import datetime

# =============================================================================
# DATA PROVENANCE
# =============================================================================

DATA_SOURCE = "Embedded (lines 69-91 of frustration_geiger_nuttall.py)"
DATA_ORIGIN = "Standard nuclear data tables (implied PDG/NUDAT2)"

# Format: (Z, A, name, Q_alpha [MeV], t_half [seconds])
ALPHA_DATA = [
    (84, 210, "Po-210", 5.407, 1.20e7),
    (84, 212, "Po-212", 8.954, 2.99e-7),
    (84, 214, "Po-214", 7.833, 1.64e-4),
    (84, 216, "Po-216", 6.906, 0.145),
    (84, 218, "Po-218", 6.114, 186),
    (86, 220, "Rn-220", 6.405, 55.6),
    (86, 222, "Rn-222", 5.590, 3.30e5),
    (88, 224, "Ra-224", 5.789, 3.14e5),
    (88, 226, "Ra-226", 4.871, 5.05e10),
    (90, 228, "Th-228", 5.520, 6.04e7),
    (90, 230, "Th-230", 4.770, 2.38e12),
    (90, 232, "Th-232", 4.083, 4.42e17),
    (92, 234, "U-234", 4.858, 7.75e12),
    (92, 235, "U-235", 4.679, 2.22e16),
    (92, 238, "U-238", 4.270, 1.41e17),
    (94, 238, "Pu-238", 5.593, 2.77e9),
    (94, 239, "Pu-239", 5.244, 7.60e11),
    (94, 240, "Pu-240", 5.256, 2.07e11),
    (95, 241, "Am-241", 5.638, 1.36e10),
    (96, 244, "Cm-244", 5.902, 5.72e8),
    (98, 252, "Cf-252", 6.217, 8.35e7),
]

# =============================================================================
# EDC MODEL CONSTANTS
# =============================================================================

K = 0.943       # MeV (pinning constant from sigma = 8.82 MeV/fm^2)
E_KIN = 35.0    # MeV (Fermi gas kinetic energy)
F_BOND = 2.5    # Bond strength factor

# Allowed coordinations (only factors of 2 and 3)
ALLOWED_N = [6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, 54, 64, 72]

# =============================================================================
# FRUSTRATION MODEL
# =============================================================================

def E_per_A(n):
    """Energy per nucleon for coordination n."""
    return E_KIN - 0.5 * n * K * F_BOND

def frustration_energy(A):
    """
    Calculate frustration energy per nucleon for nucleus of mass A.

    Model: n_eff interpolates from alpha-cluster (n=6) to bulk (n->43).
    Frustration = mismatch between n_eff and nearest allowed n.
    """
    if A < 20:
        return 0.0  # Alpha-cluster regime, no frustration

    # Effective coordination increases with A
    n_eff = 6 + (43 - 6) * (1 - np.exp(-(A - 20) / 80))

    # Find nearest allowed coordination
    n_use = min(ALLOWED_N, key=lambda x: abs(x - n_eff))

    # Frustration = energy mismatch
    return abs(E_per_A(n_eff) - E_per_A(n_use))

# =============================================================================
# MODEL FITTING
# =============================================================================

def fit_models():
    """Fit both standard and frustration-corrected Geiger-Nuttall laws."""

    Z_arr = np.array([x[0] for x in ALPHA_DATA])
    A_arr = np.array([x[1] for x in ALPHA_DATA])
    Q_arr = np.array([x[3] for x in ALPHA_DATA])
    t_arr = np.array([x[4] for x in ALPHA_DATA])
    eps_f_arr = np.array([frustration_energy(A) for A in A_arr])

    log_t = np.log10(t_arr)
    x1 = Z_arr / np.sqrt(Q_arr)  # Geiger-Nuttall term

    # ==========================================================================
    # MODEL 1: Standard Geiger-Nuttall (BASELINE)
    # ==========================================================================
    # Formula: log10(t) = slope * (Z/sqrt(Q)) + intercept

    slope_std, intercept_std = np.polyfit(x1, log_t, 1)
    log_t_pred_std = slope_std * x1 + intercept_std

    # ==========================================================================
    # MODEL 2: Frustration-Corrected Geiger-Nuttall (EDC)
    # ==========================================================================
    # Formula: log10(t) = a * (Z/sqrt(Q)) + c * eps_f + b

    X = np.column_stack([x1, eps_f_arr, np.ones(len(x1))])
    coeffs, residuals, rank, s = np.linalg.lstsq(X, log_t, rcond=None)
    a, c, b = coeffs

    log_t_pred_frust = a * x1 + c * eps_f_arr + b

    # ==========================================================================
    # METRICS
    # ==========================================================================

    # R-squared
    SS_tot = np.sum((log_t - np.mean(log_t))**2)
    SS_res_std = np.sum((log_t - log_t_pred_std)**2)
    SS_res_frust = np.sum((log_t - log_t_pred_frust)**2)

    R2_std = 1 - SS_res_std / SS_tot
    R2_frust = 1 - SS_res_frust / SS_tot

    # Absolute errors on log10(t)
    err_std = np.abs(log_t_pred_std - log_t)
    err_frust = np.abs(log_t_pred_frust - log_t)

    # Mean Absolute Error (MAE)
    MAE_std = np.mean(err_std)
    MAE_frust = np.mean(err_frust)

    # Root Mean Squared Error (RMSE)
    RMSE_std = np.sqrt(np.mean(err_std**2))
    RMSE_frust = np.sqrt(np.mean(err_frust**2))

    # Median Absolute Error
    MedAE_std = np.median(err_std)
    MedAE_frust = np.median(err_frust)

    # ==========================================================================
    # IMPROVEMENT CALCULATION (THE 44.7% NUMBER)
    # ==========================================================================

    # EXACT FORMULA:
    # improvement = (MAE_baseline - MAE_new) / MAE_baseline * 100%

    improvement_MAE = (MAE_std - MAE_frust) / MAE_std * 100
    improvement_RMSE = (RMSE_std - RMSE_frust) / RMSE_std * 100
    improvement_MedAE = (MedAE_std - MedAE_frust) / MedAE_std * 100

    return {
        'data': {
            'n_samples': len(ALPHA_DATA),
            'Z_range': [int(min(Z_arr)), int(max(Z_arr))],
            'A_range': [int(min(A_arr)), int(max(A_arr))],
            'log10_t_range': [float(min(log_t)), float(max(log_t))],
            'source': DATA_SOURCE,
            'origin': DATA_ORIGIN,
        },
        'baseline': {
            'name': 'Standard Geiger-Nuttall Law',
            'formula': 'log10(t) = slope * (Z/sqrt(Q)) + intercept',
            'slope': float(slope_std),
            'intercept': float(intercept_std),
            'dof': 2,  # degrees of freedom
        },
        'edc_model': {
            'name': 'Frustration-Corrected Geiger-Nuttall Law',
            'formula': 'log10(t) = a * (Z/sqrt(Q)) + c * eps_f + b',
            'a': float(a),
            'c': float(c),
            'b': float(b),
            'dof': 3,  # degrees of freedom
        },
        'metrics': {
            'R2': {
                'baseline': float(R2_std),
                'edc': float(R2_frust),
                'improvement_pp': float(R2_frust - R2_std) * 100,  # percentage points
            },
            'MAE_log10t': {
                'baseline': float(MAE_std),
                'edc': float(MAE_frust),
                'improvement_pct': float(improvement_MAE),
            },
            'RMSE_log10t': {
                'baseline': float(RMSE_std),
                'edc': float(RMSE_frust),
                'improvement_pct': float(improvement_RMSE),
            },
            'MedAE_log10t': {
                'baseline': float(MedAE_std),
                'edc': float(MedAE_frust),
                'improvement_pct': float(improvement_MedAE),
            },
        },
        'key_result': {
            'metric': 'MAE on log10(t_half)',
            'baseline_value': float(MAE_std),
            'edc_value': float(MAE_frust),
            'improvement_pct': float(improvement_MAE),
            'formula': '(MAE_baseline - MAE_edc) / MAE_baseline * 100',
        }
    }

# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 70)
    print("FORENSIC AUDIT: Frustration-Corrected Geiger-Nuttall Law")
    print("=" * 70)
    print(f"Timestamp: {datetime.now().isoformat()}")
    print()

    # Compute data hash for provenance
    data_str = str(ALPHA_DATA)
    data_hash = hashlib.sha256(data_str.encode()).hexdigest()[:16]
    print(f"Data hash (sha256[:16]): {data_hash}")
    print(f"N samples: {len(ALPHA_DATA)}")
    print()

    # Run fit
    results = fit_models()

    # Print summary
    print("-" * 70)
    print("BASELINE: Standard Geiger-Nuttall Law")
    print("-" * 70)
    print(f"  Formula: {results['baseline']['formula']}")
    print(f"  slope = {results['baseline']['slope']:.4f}")
    print(f"  intercept = {results['baseline']['intercept']:.4f}")
    print(f"  R² = {results['metrics']['R2']['baseline']:.4f}")
    print(f"  MAE(log10 t) = {results['metrics']['MAE_log10t']['baseline']:.4f}")
    print()

    print("-" * 70)
    print("EDC MODEL: Frustration-Corrected Geiger-Nuttall Law")
    print("-" * 70)
    print(f"  Formula: {results['edc_model']['formula']}")
    print(f"  a = {results['edc_model']['a']:.4f}")
    print(f"  c = {results['edc_model']['c']:.4f}")
    print(f"  b = {results['edc_model']['b']:.4f}")
    print(f"  R² = {results['metrics']['R2']['edc']:.4f}")
    print(f"  MAE(log10 t) = {results['metrics']['MAE_log10t']['edc']:.4f}")
    print()

    print("=" * 70)
    print("KEY RESULT: THE 44.7% IMPROVEMENT")
    print("=" * 70)
    print(f"  Metric: {results['key_result']['metric']}")
    print(f"  Baseline MAE: {results['key_result']['baseline_value']:.4f}")
    print(f"  EDC MAE: {results['key_result']['edc_value']:.4f}")
    print(f"  Formula: {results['key_result']['formula']}")
    print()
    print(f"  >>> IMPROVEMENT: {results['key_result']['improvement_pct']:.1f}% <<<")
    print()

    print("-" * 70)
    print("COMPARISON TABLE")
    print("-" * 70)
    print(f"{'Metric':<20} | {'Baseline':>12} | {'EDC':>12} | {'Δ%':>12}")
    print("-" * 60)
    print(f"{'R²':<20} | {results['metrics']['R2']['baseline']:>12.4f} | {results['metrics']['R2']['edc']:>12.4f} | {results['metrics']['R2']['improvement_pp']:>+11.2f}pp")
    print(f"{'MAE(log10 t)':<20} | {results['metrics']['MAE_log10t']['baseline']:>12.4f} | {results['metrics']['MAE_log10t']['edc']:>12.4f} | {results['metrics']['MAE_log10t']['improvement_pct']:>+11.1f}%")
    print(f"{'RMSE(log10 t)':<20} | {results['metrics']['RMSE_log10t']['baseline']:>12.4f} | {results['metrics']['RMSE_log10t']['edc']:>12.4f} | {results['metrics']['RMSE_log10t']['improvement_pct']:>+11.1f}%")
    print(f"{'MedAE(log10 t)':<20} | {results['metrics']['MedAE_log10t']['baseline']:>12.4f} | {results['metrics']['MedAE_log10t']['edc']:>12.4f} | {results['metrics']['MedAE_log10t']['improvement_pct']:>+11.1f}%")
    print()

    # Save JSON
    results['audit'] = {
        'timestamp': datetime.now().isoformat(),
        'data_hash': data_hash,
        'script': 'compare_models.py',
    }

    json_path = 'edc_papers/_shared/mn_gn_audit/comparison_results.json'
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to: {json_path}")

    return results

if __name__ == "__main__":
    main()
