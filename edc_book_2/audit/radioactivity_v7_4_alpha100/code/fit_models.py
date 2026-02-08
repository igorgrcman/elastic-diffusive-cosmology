#!/usr/bin/env python3
"""
fit_models.py - V7.4 Geiger-Nuttall Model Fitting

Purpose: Fit Models 0-3 to the α102 dataset
Status: [Der] - Statistical analysis

Usage:
    python fit_models.py

Output:
    Model coefficients, R², p-values, and diagnostics
"""

import numpy as np
import pandas as pd
from scipy import stats
from pathlib import Path

def load_dataset():
    """Load the α102 dataset."""
    csv_path = Path(__file__).parent.parent / "04_ALPHA100_DATASET.csv"
    df = pd.read_csv(csv_path)
    return df

def fit_model_0(df):
    """
    Model 0: Baseline Geiger-Nuttall
    log10(t_half) = a * (Z / sqrt(Qα)) + b
    """
    y = np.log10(df['t12_seconds'].values)
    X = df['Z'].values / np.sqrt(df['Qalpha_keV'].values)

    # Add constant
    X_with_const = np.column_stack([np.ones(len(X)), X])

    # OLS fit
    beta, residuals, rank, s = np.linalg.lstsq(X_with_const, y, rcond=None)

    y_pred = X_with_const @ beta
    resid = y - y_pred

    n = len(y)
    k = 2  # intercept + slope
    ss_res = np.sum(resid ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r_squared = 1 - ss_res / ss_tot

    rmse = np.sqrt(ss_res / n)

    return {
        'model': 'M0: G-N baseline',
        'coefficients': {'b': beta[0], 'a': beta[1]},
        'R2': r_squared,
        'RMSE': rmse,
        'n': n,
        'residuals': resid,
        'y_pred': y_pred
    }

def fit_model_1(df):
    """
    Model 1: G-N + Hindrance
    log10(t_half) = a * (Z / sqrt(Qα)) + b + c1*I(H1) + c2*I(H2)
    """
    y = np.log10(df['t12_seconds'].values)
    X_gn = df['Z'].values / np.sqrt(df['Qalpha_keV'].values)
    I_H1 = (df['hindrance_class'] == 'H1').astype(float).values
    I_H2 = (df['hindrance_class'] == 'H2').astype(float).values

    # Design matrix
    X = np.column_stack([np.ones(len(y)), X_gn, I_H1, I_H2])

    # OLS fit
    beta, residuals, rank, s = np.linalg.lstsq(X, y, rcond=None)

    y_pred = X @ beta
    resid = y - y_pred

    n = len(y)
    k = 4
    ss_res = np.sum(resid ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r_squared = 1 - ss_res / ss_tot

    rmse = np.sqrt(ss_res / n)

    return {
        'model': 'M1: G-N + Hindrance',
        'coefficients': {'b': beta[0], 'a': beta[1], 'c1': beta[2], 'c2': beta[3]},
        'R2': r_squared,
        'RMSE': rmse,
        'n': n,
        'residuals': resid,
        'y_pred': y_pred
    }

def fit_model_2(df):
    """
    Model 2: G-N + Hindrance + d(n)
    log10(t_half) = a * (Z / sqrt(Qα)) + b + c1*I(H1) + c2*I(H2) + g*d(n)
    """
    y = np.log10(df['t12_seconds'].values)
    X_gn = df['Z'].values / np.sqrt(df['Qalpha_keV'].values)
    I_H1 = (df['hindrance_class'] == 'H1').astype(float).values
    I_H2 = (df['hindrance_class'] == 'H2').astype(float).values
    d_n = df['d_n'].values

    # Design matrix
    X = np.column_stack([np.ones(len(y)), X_gn, I_H1, I_H2, d_n])

    # OLS fit
    beta, residuals, rank, s = np.linalg.lstsq(X, y, rcond=None)

    y_pred = X @ beta
    resid = y - y_pred

    n = len(y)
    k = 5
    ss_res = np.sum(resid ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r_squared = 1 - ss_res / ss_tot

    rmse = np.sqrt(ss_res / n)

    # Standard errors (simplified)
    mse = ss_res / (n - k)
    var_beta = mse * np.linalg.inv(X.T @ X)
    se = np.sqrt(np.diag(var_beta))

    # t-statistics and p-values
    t_stats = beta / se
    p_values = 2 * (1 - stats.t.cdf(np.abs(t_stats), n - k))

    return {
        'model': 'M2: G-N + Hindrance + d(n)',
        'coefficients': {'b': beta[0], 'a': beta[1], 'c1': beta[2], 'c2': beta[3], 'g': beta[4]},
        'se': {'b': se[0], 'a': se[1], 'c1': se[2], 'c2': se[3], 'g': se[4]},
        't': {'b': t_stats[0], 'a': t_stats[1], 'c1': t_stats[2], 'c2': t_stats[3], 'g': t_stats[4]},
        'p': {'b': p_values[0], 'a': p_values[1], 'c1': p_values[2], 'c2': p_values[3], 'g': p_values[4]},
        'R2': r_squared,
        'RMSE': rmse,
        'n': n,
        'residuals': resid,
        'y_pred': y_pred
    }

def fit_model_3(df):
    """
    Model 3: G-N + d(n) only
    log10(t_half) = a * (Z / sqrt(Qα)) + b + g*d(n)
    """
    y = np.log10(df['t12_seconds'].values)
    X_gn = df['Z'].values / np.sqrt(df['Qalpha_keV'].values)
    d_n = df['d_n'].values

    # Design matrix
    X = np.column_stack([np.ones(len(y)), X_gn, d_n])

    # OLS fit
    beta, residuals, rank, s = np.linalg.lstsq(X, y, rcond=None)

    y_pred = X @ beta
    resid = y - y_pred

    n = len(y)
    k = 3
    ss_res = np.sum(resid ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r_squared = 1 - ss_res / ss_tot

    rmse = np.sqrt(ss_res / n)

    return {
        'model': 'M3: G-N + d(n) only',
        'coefficients': {'b': beta[0], 'a': beta[1], 'g': beta[2]},
        'R2': r_squared,
        'RMSE': rmse,
        'n': n,
        'residuals': resid,
        'y_pred': y_pred
    }

def main():
    """Fit all models and report results."""
    print("V7.4 Geiger-Nuttall Model Fitting")
    print("=" * 60)

    try:
        df = load_dataset()
        print(f"\nLoaded dataset: {len(df)} nuclides")
    except FileNotFoundError:
        print("\nDataset not found. Using simulated results.")
        print("(Run with actual CSV for real analysis)")
        return

    # Fit models
    print("\n" + "-" * 60)
    m0 = fit_model_0(df)
    print(f"\n{m0['model']}")
    print(f"  R² = {m0['R2']:.4f}")
    print(f"  RMSE = {m0['RMSE']:.3f}")
    print(f"  a = {m0['coefficients']['a']:.3f}")
    print(f"  b = {m0['coefficients']['b']:.2f}")

    print("\n" + "-" * 60)
    m1 = fit_model_1(df)
    print(f"\n{m1['model']}")
    print(f"  R² = {m1['R2']:.4f}")
    print(f"  RMSE = {m1['RMSE']:.3f}")
    print(f"  c1 (H1) = {m1['coefficients']['c1']:.3f}")
    print(f"  c2 (H2) = {m1['coefficients']['c2']:.3f}")

    print("\n" + "-" * 60)
    m2 = fit_model_2(df)
    print(f"\n{m2['model']}")
    print(f"  R² = {m2['R2']:.4f}")
    print(f"  RMSE = {m2['RMSE']:.3f}")
    print(f"  g (d_n) = {m2['coefficients']['g']:.3f} ± {m2['se']['g']:.3f}")
    print(f"  t = {m2['t']['g']:.2f}")
    print(f"  p = {m2['p']['g']:.4f}")

    # 95% CI for g
    g = m2['coefficients']['g']
    se_g = m2['se']['g']
    ci_low = g - 1.96 * se_g
    ci_high = g + 1.96 * se_g
    print(f"  95% CI: [{ci_low:.3f}, {ci_high:.3f}]")

    print("\n" + "-" * 60)
    m3 = fit_model_3(df)
    print(f"\n{m3['model']}")
    print(f"  R² = {m3['R2']:.4f}")
    print(f"  g (d_n) = {m3['coefficients']['g']:.3f}")

    # Correlation test
    print("\n" + "=" * 60)
    print("\nResidual-d(n) Correlation (from M1 residuals)")
    r, p = stats.pearsonr(m1['residuals'], df['d_n'].values)
    print(f"  Pearson r = {r:.3f}")
    print(f"  p-value = {p:.4f}")

    rho, p_rho = stats.spearmanr(m1['residuals'], df['d_n'].values)
    print(f"  Spearman ρ = {rho:.3f}")
    print(f"  p-value = {p_rho:.4f}")

    print("\n" + "=" * 60)
    print("\nVERDICT EVALUATION")
    print("-" * 40)
    if m2['p']['g'] <= 0.01:
        print("✓ p ≤ 0.01: PASS")
    else:
        print("✗ p ≤ 0.01: FAIL")

    if m2['coefficients']['g'] < 0:
        print("✓ Sign stable (negative): PASS")
    else:
        print("✗ Sign stable: FAIL")

    if ci_high < 0:
        print("✓ 95% CI excludes zero: PASS")
    else:
        print("✗ 95% CI excludes zero: FAIL")

    if m2['p']['g'] <= 0.01 and m2['coefficients']['g'] < 0 and ci_high < 0:
        print("\n>>> VERDICT: EVIDENCE <<<")
    elif m2['p']['g'] <= 0.10 and m2['coefficients']['g'] < 0:
        print("\n>>> VERDICT: SUGGESTIVE <<<")
    else:
        print("\n>>> VERDICT: NULL <<<")

if __name__ == "__main__":
    main()
