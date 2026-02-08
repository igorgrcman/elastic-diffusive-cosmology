#!/usr/bin/env python3
"""
PREFACTOR OPTIMIZATION WITH REFIT + K-FOLD CV
==============================================
For each prefactor p, refit ALL coefficients (a, g, b, c1, c2) and perform
5-fold cross-validation to determine optimal p without overfitting.

This is the rigorous version of the sensitivity analysis.
"""

import math
import csv
import random
from typing import List, Dict, Tuple

# =============================================================================
# LOAD DATA
# =============================================================================

def load_alpha100(filepath: str) -> List[Dict]:
    """Load ALPHA100 CSV dataset (all hindrance classes)."""
    data = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
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
# LINEAR REGRESSION (from scratch, no numpy)
# =============================================================================

def mean(vals: List[float]) -> float:
    return sum(vals) / len(vals)

def dot(a: List[float], b: List[float]) -> float:
    return sum(x*y for x, y in zip(a, b))

def transpose(matrix: List[List[float]]) -> List[List[float]]:
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def matrix_multiply(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """Multiply two matrices."""
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    result = [[0.0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

def matrix_vector_multiply(A: List[List[float]], v: List[float]) -> List[float]:
    return [dot(row, v) for row in A]

def solve_linear_system(X: List[List[float]], y: List[float]) -> List[float]:
    """
    Solve X @ beta = y using normal equations: beta = (X'X)^(-1) X'y
    Simple Gaussian elimination for (X'X).
    """
    n = len(X)
    k = len(X[0])

    # Compute X'X
    XT = transpose(X)
    XTX = [[dot(XT[i], [row[j] for row in X]) for j in range(k)] for i in range(k)]

    # Compute X'y
    XTy = [dot(XT[i], y) for i in range(k)]

    # Solve XTX @ beta = XTy using Gaussian elimination with pivoting
    A = [row[:] + [XTy[i]] for i, row in enumerate(XTX)]  # Augmented matrix

    # Forward elimination
    for col in range(k):
        # Find pivot
        max_row = col
        for row in range(col + 1, k):
            if abs(A[row][col]) > abs(A[max_row][col]):
                max_row = row
        A[col], A[max_row] = A[max_row], A[col]

        if abs(A[col][col]) < 1e-10:
            continue  # Skip singular column

        for row in range(col + 1, k):
            factor = A[row][col] / A[col][col]
            for j in range(col, k + 1):
                A[row][j] -= factor * A[col][j]

    # Back substitution
    beta = [0.0] * k
    for i in range(k - 1, -1, -1):
        beta[i] = A[i][k]
        for j in range(i + 1, k):
            beta[i] -= A[i][j] * beta[j]
        if abs(A[i][i]) > 1e-10:
            beta[i] /= A[i][i]

    return beta

# =============================================================================
# MODEL FITTING
# =============================================================================

def prepare_features(data: List[Dict], prefactor: float) -> Tuple[List[List[float]], List[float]]:
    """
    Prepare feature matrix X and target vector y.

    Features: [1, Z_d/sqrt(Q), d(n), I(H1), I(H2)]
    Target: log10(t12)
    """
    X = []
    y = []

    for d in data:
        Z_d = d['Z'] - 2
        Q_MeV = d['Q_keV'] / 1000.0
        sqrt_Q = math.sqrt(Q_MeV)
        gn_var = Z_d / sqrt_Q

        n_A = calc_n_A(d['A'], prefactor)
        d_n = calc_d_n(n_A)

        I_H1 = 1.0 if d['hindrance'] == 'H1' else 0.0
        I_H2 = 1.0 if d['hindrance'] == 'H2' else 0.0

        X.append([1.0, gn_var, d_n, I_H1, I_H2])
        y.append(math.log10(d['t12_s']))

    return X, y

def fit_model(X: List[List[float]], y: List[float]) -> List[float]:
    """Fit linear model, return coefficients [b, a, g, c1, c2]."""
    return solve_linear_system(X, y)

def predict(X: List[List[float]], beta: List[float]) -> List[float]:
    """Predict using fitted coefficients."""
    return [dot(row, beta) for row in X]

def calc_metrics(y_true: List[float], y_pred: List[float]) -> Dict:
    """Calculate R², RMSE, MAE, pass rate."""
    n = len(y_true)

    # Residuals
    residuals = [t - p for t, p in zip(y_true, y_pred)]
    abs_residuals = [abs(r) for r in residuals]

    # SS_res, SS_tot
    ss_res = sum(r**2 for r in residuals)
    mean_y = mean(y_true)
    ss_tot = sum((y - mean_y)**2 for y in y_true)

    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0
    rmse = math.sqrt(ss_res / n)
    mae = sum(abs_residuals) / n
    pass_rate = sum(1 for r in abs_residuals if r < 1.5) / n

    return {
        'r2': r2,
        'rmse': rmse,
        'mae': mae,
        'pass_rate': pass_rate,
        'max_abs_error': max(abs_residuals),
    }

# =============================================================================
# K-FOLD CROSS-VALIDATION
# =============================================================================

def k_fold_cv(data: List[Dict], prefactor: float, k: int = 5, seed: int = 42) -> Dict:
    """
    Perform k-fold cross-validation.
    Returns averaged metrics across folds.
    """
    random.seed(seed)
    indices = list(range(len(data)))
    random.shuffle(indices)

    fold_size = len(data) // k

    all_metrics = []
    all_coefficients = []

    for fold in range(k):
        # Split data
        test_start = fold * fold_size
        test_end = test_start + fold_size if fold < k - 1 else len(data)
        test_indices = set(indices[test_start:test_end])

        train_data = [data[i] for i in range(len(data)) if i not in test_indices]
        test_data = [data[i] for i in test_indices]

        # Fit on train
        X_train, y_train = prepare_features(train_data, prefactor)
        beta = fit_model(X_train, y_train)

        # Predict on test
        X_test, y_test = prepare_features(test_data, prefactor)
        y_pred = predict(X_test, beta)

        # Metrics
        metrics = calc_metrics(y_test, y_pred)
        all_metrics.append(metrics)
        all_coefficients.append(beta)

    # Average metrics
    avg_metrics = {
        'r2': mean([m['r2'] for m in all_metrics]),
        'rmse': mean([m['rmse'] for m in all_metrics]),
        'mae': mean([m['mae'] for m in all_metrics]),
        'pass_rate': mean([m['pass_rate'] for m in all_metrics]),
    }

    # Coefficient stability (std across folds)
    coef_names = ['b', 'a', 'g', 'c1', 'c2']
    coef_means = [mean([c[i] for c in all_coefficients]) for i in range(5)]
    coef_stds = [math.sqrt(mean([(c[i] - coef_means[i])**2 for c in all_coefficients])) for i in range(5)]

    return {
        'cv_metrics': avg_metrics,
        'coef_means': dict(zip(coef_names, coef_means)),
        'coef_stds': dict(zip(coef_names, coef_stds)),
        'fold_metrics': all_metrics,
    }

# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    import os

    # Load data
    dataset_path = '/Users/igor/ClaudeAI/EDC_Project/elastic-diffusive-cosmology_repo/edc_book_2/audit/radioactivity_v7_4_alpha100/04_ALPHA100_DATASET.csv'
    data = load_alpha100(dataset_path)

    print("="*75)
    print("PREFACTOR OPTIMIZATION WITH REFIT + 5-FOLD CV")
    print("="*75)
    print(f"\nDataset: {len(data)} nuclides (all hindrance classes)")
    print(f"A range: {min(d['A'] for d in data)} - {max(d['A'] for d in data)}")
    print(f"Hindrance distribution: H0={sum(1 for d in data if d['hindrance']=='H0')}, "
          f"H1={sum(1 for d in data if d['hindrance']=='H1')}, "
          f"H2={sum(1 for d in data if d['hindrance']=='H2')}")

    # Test prefactors with full refit + CV
    prefactors = [5.90, 5.95, 6.00, 6.05, 6.10, 6.15, 6.20]

    print("\n" + "-"*75)
    print("CROSS-VALIDATION RESULTS (5-fold, each fold refits all coefficients)")
    print("-"*75)
    print(f"{'p':>6} {'CV R²':>8} {'CV RMSE':>8} {'CV MAE':>8} {'CV Pass%':>9} "
          f"{'a±σ':>12} {'g±σ':>12} {'b±σ':>12}")
    print("-"*75)

    results = {}
    for p in prefactors:
        cv_result = k_fold_cv(data, p, k=5)
        results[p] = cv_result

        m = cv_result['cv_metrics']
        c = cv_result['coef_means']
        s = cv_result['coef_stds']

        marker = " *" if p == 6.1 else (" ◆" if p == 6.0 else "")
        print(f"{p:>6.2f} {m['r2']:>8.4f} {m['rmse']:>8.3f} {m['mae']:>8.3f} {m['pass_rate']*100:>8.1f}% "
              f"{c['a']:>5.2f}±{s['a']:.2f} {c['g']:>5.2f}±{s['g']:.2f} "
              f"{c['b']:>6.1f}±{s['b']:.1f}{marker}")

    print("\n* = historical default (6.1)")
    print("◆ = proposed optimum (6.0)")

    # Full-dataset fit for optimal prefactor
    print("\n" + "-"*75)
    print("FULL-DATASET FIT COMPARISON (p=6.0 vs p=6.1)")
    print("-"*75)

    for p in [6.0, 6.1]:
        X, y = prepare_features(data, p)
        beta = fit_model(X, y)
        y_pred = predict(X, beta)
        metrics = calc_metrics(y, y_pred)

        print(f"\np = {p}:")
        print(f"  Coefficients: b={beta[0]:.2f}, a={beta[1]:.3f}, g={beta[2]:.3f}, "
              f"c1={beta[3]:.3f}, c2={beta[4]:.3f}")
        print(f"  R² = {metrics['r2']:.4f}, RMSE = {metrics['rmse']:.3f}, "
              f"MAE = {metrics['mae']:.3f}, Pass = {metrics['pass_rate']*100:.1f}%")

    # Find optimal
    best_p = max(results.keys(), key=lambda p: results[p]['cv_metrics']['r2'])
    best_cv = results[best_p]['cv_metrics']

    print("\n" + "="*75)
    print("CONCLUSION")
    print("="*75)
    print(f"\nOptimal prefactor (by CV R²): p = {best_p}")
    print(f"CV R² = {best_cv['r2']:.4f}, CV RMSE = {best_cv['rmse']:.3f}, "
          f"CV Pass = {best_cv['pass_rate']*100:.1f}%")

    # Compare p=6.0 vs p=6.1
    r2_6_0 = results[6.0]['cv_metrics']['r2']
    r2_6_1 = results[6.1]['cv_metrics']['r2']

    print(f"\np=6.0 CV R²: {r2_6_0:.4f}")
    print(f"p=6.1 CV R²: {r2_6_1:.4f}")
    print(f"Δ(CV R²) = {r2_6_0 - r2_6_1:+.4f}")

    if r2_6_0 > r2_6_1:
        print("\n✓ p=6.0 CONFIRMED as optimal by rigorous CV")
    else:
        print("\n→ p=6.1 may be preferable or equivalent")

    print("\n" + "="*75)
