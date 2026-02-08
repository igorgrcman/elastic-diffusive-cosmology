#!/usr/bin/env python3
"""
V7.8 Model Fitting Script
Fits M0-M7 models with proxy variables to test mediation
"""

import csv
import math
import os
from collections import defaultdict

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIT_DIR = os.path.dirname(SCRIPT_DIR)
INPUT_CSV = os.path.join(AUDIT_DIR, "04_DATASET_AUGMENTATION.csv")

def load_data():
    """Load augmented dataset."""
    data = []
    with open(INPUT_CSV, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            record = {
                'nuclide': row['nuclide'],
                'Z': int(row['Z']),
                'A': int(row['A']),
                't12_seconds': float(row['t12_seconds']),
                'Qalpha_keV': float(row['Qalpha_keV']),
                'd_n': float(row['d_n']),
                'hindrance_class': row['hindrance_class'],
                'proxy_deform': float(row['proxy_deform']),
                'proxy_Salpha': float(row['proxy_Salpha']),
            }
            # Derived
            record['log10_t12'] = math.log10(record['t12_seconds'])
            record['Z_sqrt_Q'] = record['Z'] / math.sqrt(record['Qalpha_keV'] / 1000)  # Q in MeV
            record['I_H1'] = 1 if record['hindrance_class'] == 'H1' else 0
            record['I_H2'] = 1 if record['hindrance_class'] == 'H2' else 0
            data.append(record)
    return data

def ols_fit(X, y):
    """
    Simple OLS regression using normal equations.
    X: list of lists (n_samples x n_features)
    y: list (n_samples)
    Returns: coefficients, residuals, R², adjusted R², AIC, BIC
    """
    n = len(y)
    k = len(X[0])

    # Add intercept
    X_aug = [[1] + row for row in X]
    k_aug = k + 1

    # X'X
    XtX = [[sum(X_aug[i][j] * X_aug[i][l] for i in range(n)) for l in range(k_aug)] for j in range(k_aug)]

    # X'y
    Xty = [sum(X_aug[i][j] * y[i] for i in range(n)) for j in range(k_aug)]

    # Solve (X'X)^-1 X'y using Gaussian elimination
    coef = solve_linear_system(XtX, Xty)

    # Predictions and residuals
    y_pred = [sum(coef[j] * X_aug[i][j] for j in range(k_aug)) for i in range(n)]
    residuals = [y[i] - y_pred[i] for i in range(n)]

    # SS
    y_mean = sum(y) / n
    SS_tot = sum((yi - y_mean) ** 2 for yi in y)
    SS_res = sum(r ** 2 for r in residuals)

    R2 = 1 - SS_res / SS_tot
    R2_adj = 1 - (1 - R2) * (n - 1) / (n - k_aug)

    # RMSE
    RMSE = math.sqrt(SS_res / n)

    # AIC, BIC
    log_likelihood = -n/2 * (1 + math.log(2 * math.pi) + math.log(SS_res / n))
    AIC = 2 * k_aug - 2 * log_likelihood
    BIC = k_aug * math.log(n) - 2 * log_likelihood

    # Standard errors (approximate)
    MSE = SS_res / (n - k_aug)
    try:
        XtX_inv = invert_matrix(XtX)
        SE = [math.sqrt(MSE * XtX_inv[j][j]) if XtX_inv[j][j] > 0 else 0 for j in range(k_aug)]
    except:
        SE = [0] * k_aug

    return {
        'coef': coef,
        'SE': SE,
        'R2': R2,
        'R2_adj': R2_adj,
        'RMSE': RMSE,
        'AIC': AIC,
        'BIC': BIC,
        'n': n,
        'k': k_aug,
        'residuals': residuals
    }

def solve_linear_system(A, b):
    """Solve Ax = b using Gaussian elimination with partial pivoting."""
    n = len(b)
    # Augmented matrix
    M = [A[i][:] + [b[i]] for i in range(n)]

    # Forward elimination
    for col in range(n):
        # Pivot
        max_row = max(range(col, n), key=lambda r: abs(M[r][col]))
        M[col], M[max_row] = M[max_row], M[col]

        if abs(M[col][col]) < 1e-12:
            continue

        for row in range(col + 1, n):
            factor = M[row][col] / M[col][col]
            for j in range(col, n + 1):
                M[row][j] -= factor * M[col][j]

    # Back substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        if abs(M[i][i]) < 1e-12:
            x[i] = 0
        else:
            x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]

    return x

def invert_matrix(A):
    """Invert matrix using Gaussian elimination."""
    n = len(A)
    # Augment with identity
    M = [A[i][:] + [1 if j == i else 0 for j in range(n)] for i in range(n)]

    # Forward elimination
    for col in range(n):
        max_row = max(range(col, n), key=lambda r: abs(M[r][col]))
        M[col], M[max_row] = M[max_row], M[col]

        if abs(M[col][col]) < 1e-12:
            raise ValueError("Singular matrix")

        scale = M[col][col]
        for j in range(2 * n):
            M[col][j] /= scale

        for row in range(n):
            if row != col:
                factor = M[row][col]
                for j in range(2 * n):
                    M[row][j] -= factor * M[col][j]

    return [row[n:] for row in M]

def compute_t_stat(coef, se):
    """Compute t-statistic."""
    if se == 0 or abs(se) < 1e-12:
        return float('inf') if coef != 0 else 0
    return coef / se

def t_to_p(t, df):
    """Approximate p-value from t-statistic (two-tailed)."""
    # Using approximation for large df
    if df > 30:
        # Normal approximation
        z = abs(t)
        p = 2 * (1 - normal_cdf(z))
        return p
    else:
        # Rough approximation
        return 2 * (1 - normal_cdf(abs(t) * math.sqrt(df / (df + t*t))))

def normal_cdf(x):
    """Standard normal CDF approximation."""
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))

def main():
    data = load_data()
    n = len(data)
    print(f"Loaded {n} nuclides\n")

    # Prepare common variables
    y = [d['log10_t12'] for d in data]

    results = {}

    # M0: GN only
    X_M0 = [[d['Z_sqrt_Q']] for d in data]
    results['M0'] = ols_fit(X_M0, y)
    results['M0']['name'] = 'M0: GN only'
    results['M0']['predictors'] = ['intercept', 'Z/√Q']

    # M1: GN + hindrance
    X_M1 = [[d['Z_sqrt_Q'], d['I_H1'], d['I_H2']] for d in data]
    results['M1'] = ols_fit(X_M1, y)
    results['M1']['name'] = 'M1: GN + hindrance'
    results['M1']['predictors'] = ['intercept', 'Z/√Q', 'I(H1)', 'I(H2)']

    # M2: M1 + d(n)
    X_M2 = [[d['Z_sqrt_Q'], d['I_H1'], d['I_H2'], d['d_n']] for d in data]
    results['M2'] = ols_fit(X_M2, y)
    results['M2']['name'] = 'M2: M1 + d(n)'
    results['M2']['predictors'] = ['intercept', 'Z/√Q', 'I(H1)', 'I(H2)', 'd(n)']

    # M3: M1 + proxy_deform
    X_M3 = [[d['Z_sqrt_Q'], d['I_H1'], d['I_H2'], d['proxy_deform']] for d in data]
    results['M3'] = ols_fit(X_M3, y)
    results['M3']['name'] = 'M3: M1 + proxy_deform'
    results['M3']['predictors'] = ['intercept', 'Z/√Q', 'I(H1)', 'I(H2)', 'proxy_deform']

    # M4: M1 + proxy_Salpha
    X_M4 = [[d['Z_sqrt_Q'], d['I_H1'], d['I_H2'], d['proxy_Salpha']] for d in data]
    results['M4'] = ols_fit(X_M4, y)
    results['M4']['name'] = 'M4: M1 + proxy_Salpha'
    results['M4']['predictors'] = ['intercept', 'Z/√Q', 'I(H1)', 'I(H2)', 'proxy_Salpha']

    # M5: M1 + d(n) + proxy_deform
    X_M5 = [[d['Z_sqrt_Q'], d['I_H1'], d['I_H2'], d['d_n'], d['proxy_deform']] for d in data]
    results['M5'] = ols_fit(X_M5, y)
    results['M5']['name'] = 'M5: M1 + d(n) + proxy_deform'
    results['M5']['predictors'] = ['intercept', 'Z/√Q', 'I(H1)', 'I(H2)', 'd(n)', 'proxy_deform']

    # M6: M1 + d(n) + proxy_Salpha
    X_M6 = [[d['Z_sqrt_Q'], d['I_H1'], d['I_H2'], d['d_n'], d['proxy_Salpha']] for d in data]
    results['M6'] = ols_fit(X_M6, y)
    results['M6']['name'] = 'M6: M1 + d(n) + proxy_Salpha'
    results['M6']['predictors'] = ['intercept', 'Z/√Q', 'I(H1)', 'I(H2)', 'd(n)', 'proxy_Salpha']

    # M7: Full model
    X_M7 = [[d['Z_sqrt_Q'], d['I_H1'], d['I_H2'], d['d_n'], d['proxy_deform'], d['proxy_Salpha']] for d in data]
    results['M7'] = ols_fit(X_M7, y)
    results['M7']['name'] = 'M7: Full model'
    results['M7']['predictors'] = ['intercept', 'Z/√Q', 'I(H1)', 'I(H2)', 'd(n)', 'proxy_deform', 'proxy_Salpha']

    # Print results
    print("=" * 80)
    print("V7.8 MODEL FITTING RESULTS")
    print("=" * 80)

    for model_name in ['M0', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7']:
        r = results[model_name]
        print(f"\n{r['name']}")
        print("-" * 60)
        print(f"{'Predictor':<20} {'Coef':>10} {'SE':>10} {'t':>8} {'p':>10}")
        print("-" * 60)

        for i, pred in enumerate(r['predictors']):
            coef = r['coef'][i]
            se = r['SE'][i]
            t = compute_t_stat(coef, se)
            p = t_to_p(t, r['n'] - r['k'])
            p_str = f"{p:.4f}" if p >= 0.0001 else "<0.0001"
            print(f"{pred:<20} {coef:>10.4f} {se:>10.4f} {t:>8.2f} {p_str:>10}")

        print("-" * 60)
        print(f"R² = {r['R2']:.4f}, R²_adj = {r['R2_adj']:.4f}, RMSE = {r['RMSE']:.4f}")
        print(f"AIC = {r['AIC']:.2f}, BIC = {r['BIC']:.2f}, n = {r['n']}, k = {r['k']}")

    # Key comparison: g in M2 vs M5, M6, M7
    print("\n" + "=" * 80)
    print("MEDIATION ANALYSIS: d(n) coefficient across models")
    print("=" * 80)

    g_M2 = results['M2']['coef'][4]  # d(n) in M2
    se_M2 = results['M2']['SE'][4]

    # Find d(n) index in M5, M6, M7 (it's at position 4)
    g_M5 = results['M5']['coef'][4]
    se_M5 = results['M5']['SE'][4]

    g_M6 = results['M6']['coef'][4]
    se_M6 = results['M6']['SE'][4]

    g_M7 = results['M7']['coef'][4]
    se_M7 = results['M7']['SE'][4]

    print(f"\n{'Model':<30} {'g(d(n))':<12} {'SE':<10} {'Δg vs M2':<12} {'% change':<10}")
    print("-" * 70)
    print(f"{'M2: baseline':<30} {g_M2:<12.4f} {se_M2:<10.4f} {'—':<12} {'—':<10}")
    print(f"{'M5: + proxy_deform':<30} {g_M5:<12.4f} {se_M5:<10.4f} {g_M5 - g_M2:<12.4f} {100*(g_M5-g_M2)/abs(g_M2):<10.1f}%")
    print(f"{'M6: + proxy_Salpha':<30} {g_M6:<12.4f} {se_M6:<10.4f} {g_M6 - g_M2:<12.4f} {100*(g_M6-g_M2)/abs(g_M2):<10.1f}%")
    print(f"{'M7: + both proxies':<30} {g_M7:<12.4f} {se_M7:<10.4f} {g_M7 - g_M2:<12.4f} {100*(g_M7-g_M2)/abs(g_M2):<10.1f}%")

    # Verdict
    print("\n" + "=" * 80)
    print("VERDICT")
    print("=" * 80)

    # Check if g remains significant and negative
    t_M7 = compute_t_stat(g_M7, se_M7)
    p_M7 = t_to_p(t_M7, results['M7']['n'] - results['M7']['k'])

    delta_g_percent = 100 * abs(g_M7 - g_M2) / abs(g_M2)

    if g_M7 < 0 and p_M7 < 0.05 and delta_g_percent < 30:
        verdict = "ROBUST"
        explanation = f"g remains negative ({g_M7:.3f}), significant (p={p_M7:.4f}), and stable ({delta_g_percent:.1f}% change)"
    elif g_M7 < 0 and p_M7 < 0.05 and delta_g_percent >= 30:
        verdict = "MEDIATION"
        explanation = f"g is reduced by {delta_g_percent:.1f}% but remains significant; proxies partially mediate"
    elif g_M7 >= 0 or p_M7 >= 0.05:
        verdict = "COLLAPSE"
        explanation = f"g loses significance (p={p_M7:.4f}) or changes sign when proxies included"
    else:
        verdict = "INCONCLUSIVE"
        explanation = "Mixed evidence"

    print(f"\nV7.8 verdict: {verdict} — {explanation}")

    return results, verdict

if __name__ == "__main__":
    results, verdict = main()
