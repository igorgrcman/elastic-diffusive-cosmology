#!/usr/bin/env python3
"""
SUPERHEAVY OUT-OF-SAMPLE TEST WITH PROPER REFIT
================================================
Train on A≤252 (ALPHA100), test on Z≥114 (superheavy).
This is the proper way to evaluate extrapolation performance.
"""

import math
import csv
from typing import List, Dict, Tuple

# =============================================================================
# DATA
# =============================================================================

def load_alpha100(filepath: str) -> List[Dict]:
    """Load ALPHA100 CSV dataset."""
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

# Superheavy experimental data (Z >= 114)
SUPERHEAVY = [
    {'nuclide': 'Fl-289', 'Z': 114, 'A': 289, 'Q_keV': 9820, 't12_s': 2.1, 'hindrance': 'H0'},
    {'nuclide': 'Fl-290', 'Z': 114, 'A': 290, 'Q_keV': 9190, 't12_s': 19.0, 'hindrance': 'H0'},
    {'nuclide': 'Mc-290', 'Z': 115, 'A': 290, 'Q_keV': 10410, 't12_s': 0.65, 'hindrance': 'H0'},
    {'nuclide': 'Lv-293', 'Z': 116, 'A': 293, 'Q_keV': 10670, 't12_s': 0.060, 'hindrance': 'H0'},
    {'nuclide': 'Ts-294', 'Z': 117, 'A': 294, 'Q_keV': 10810, 't12_s': 0.026, 'hindrance': 'H0'},
    {'nuclide': 'Og-294', 'Z': 118, 'A': 294, 'Q_keV': 11650, 't12_s': 0.0007, 'hindrance': 'H0'},
]

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
    return min(abs(n_A - k) for k in ALLOWED_N)

def calc_n_A(A: int, p: float) -> float:
    return p * (A ** (1/3))

# =============================================================================
# LINEAR REGRESSION
# =============================================================================

def mean(vals: List[float]) -> float:
    return sum(vals) / len(vals) if vals else 0

def dot(a: List[float], b: List[float]) -> float:
    return sum(x*y for x, y in zip(a, b))

def transpose(X: List[List[float]]) -> List[List[float]]:
    return [[row[i] for row in X] for i in range(len(X[0]))]

def solve_normal_equations(X: List[List[float]], y: List[float]) -> List[float]:
    """Solve X @ beta = y via (X'X)^(-1) X'y."""
    n = len(X)
    k = len(X[0])
    XT = transpose(X)

    # X'X
    XTX = [[dot(XT[i], [row[j] for row in X]) for j in range(k)] for i in range(k)]
    # X'y
    XTy = [dot(XT[i], y) for i in range(k)]

    # Gauss elimination
    A = [row[:] + [XTy[i]] for i, row in enumerate(XTX)]

    for col in range(k):
        max_row = col
        for row in range(col + 1, k):
            if abs(A[row][col]) > abs(A[max_row][col]):
                max_row = row
        A[col], A[max_row] = A[max_row], A[col]

        if abs(A[col][col]) < 1e-10:
            continue

        for row in range(col + 1, k):
            f = A[row][col] / A[col][col]
            for j in range(col, k + 1):
                A[row][j] -= f * A[col][j]

    beta = [0.0] * k
    for i in range(k - 1, -1, -1):
        beta[i] = A[i][k]
        for j in range(i + 1, k):
            beta[i] -= A[i][j] * beta[j]
        if abs(A[i][i]) > 1e-10:
            beta[i] /= A[i][i]

    return beta

# =============================================================================
# MODEL
# =============================================================================

def prepare_features(data: List[Dict], p: float) -> Tuple[List[List[float]], List[float]]:
    """Features: [1, Z_d/sqrt(Q), d(n), I(H1), I(H2)]"""
    X, y = [], []
    for d in data:
        Z_d = d['Z'] - 2
        Q_MeV = d['Q_keV'] / 1000.0
        gn = Z_d / math.sqrt(Q_MeV)
        dn = calc_d_n(calc_n_A(d['A'], p))
        ih1 = 1.0 if d['hindrance'] == 'H1' else 0.0
        ih2 = 1.0 if d['hindrance'] == 'H2' else 0.0
        X.append([1.0, gn, dn, ih1, ih2])
        y.append(math.log10(d['t12_s']))
    return X, y

def predict_single(d: Dict, beta: List[float], p: float) -> float:
    """Predict log10(t) for a single nuclide."""
    Z_d = d['Z'] - 2
    Q_MeV = d['Q_keV'] / 1000.0
    gn = Z_d / math.sqrt(Q_MeV)
    dn = calc_d_n(calc_n_A(d['A'], p))
    ih1 = 1.0 if d['hindrance'] == 'H1' else 0.0
    ih2 = 1.0 if d['hindrance'] == 'H2' else 0.0
    return dot([1.0, gn, dn, ih1, ih2], beta)

def baseline_gn_predict(d: Dict, beta: List[float]) -> float:
    """Baseline GN (no d(n) term)."""
    Z_d = d['Z'] - 2
    Q_MeV = d['Q_keV'] / 1000.0
    gn = Z_d / math.sqrt(Q_MeV)
    ih1 = 1.0 if d['hindrance'] == 'H1' else 0.0
    ih2 = 1.0 if d['hindrance'] == 'H2' else 0.0
    # beta = [b, a, g, c1, c2], baseline uses only [b, a, 0, c1, c2]
    return beta[0] + beta[1] * gn + beta[3] * ih1 + beta[4] * ih2

# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    # Load training data
    path = '/Users/igor/ClaudeAI/EDC_Project/elastic-diffusive-cosmology_repo/edc_book_2/audit/radioactivity_v7_4_alpha100/04_ALPHA100_DATASET.csv'
    train_data = load_alpha100(path)

    print("="*80)
    print("SUPERHEAVY OUT-OF-SAMPLE TEST (Train: A≤257, Test: Z≥114)")
    print("="*80)
    print(f"\nTraining set: {len(train_data)} nuclides")
    print(f"Test set: {len(SUPERHEAVY)} superheavy nuclides")

    # Test different prefactors
    prefactors = [5.95, 6.00, 6.05, 6.10, 6.15]

    print("\n" + "-"*80)
    print("PREFACTOR COMPARISON (all coefficients refitted on training set)")
    print("-"*80)
    print(f"{'p':>5} {'Train R²':>9} {'SHE Mean Δ':>11} {'SHE Max Δ':>10} {'SHE Pass':>9} {'Og-294 Δ':>10}")
    print("-"*80)

    for p in prefactors:
        # Fit on training data
        X_train, y_train = prepare_features(train_data, p)
        beta = solve_normal_equations(X_train, y_train)

        # Training metrics
        y_pred_train = [dot(x, beta) for x in X_train]
        ss_res = sum((t - pr)**2 for t, pr in zip(y_train, y_pred_train))
        ss_tot = sum((t - mean(y_train))**2 for t in y_train)
        train_r2 = 1 - ss_res / ss_tot

        # Superheavy predictions
        she_deltas = []
        og_delta = None

        for d in SUPERHEAVY:
            log_t_exp = math.log10(d['t12_s'])
            log_t_pred = predict_single(d, beta, p)
            delta = abs(log_t_exp - log_t_pred)
            she_deltas.append(delta)

            if d['nuclide'] == 'Og-294':
                og_delta = delta

        mean_she_delta = mean(she_deltas)
        max_she_delta = max(she_deltas)
        pass_count = sum(1 for d in she_deltas if d < 1.5)

        marker = " *" if p == 6.1 else (" ◆" if p == 6.0 else "")
        print(f"{p:>5.2f} {train_r2:>9.4f} {mean_she_delta:>11.2f} {max_she_delta:>10.2f} "
              f"{pass_count}/{len(SUPERHEAVY):>7} {og_delta:>10.2f}{marker}")

    # Detailed results for p=6.0 and p=6.1
    print("\n" + "-"*80)
    print("DETAILED SUPERHEAVY PREDICTIONS")
    print("-"*80)

    for p in [6.0, 6.1]:
        X_train, y_train = prepare_features(train_data, p)
        beta = solve_normal_equations(X_train, y_train)

        print(f"\n--- p = {p} ---")
        print(f"Fitted: b={beta[0]:.2f}, a={beta[1]:.3f}, g={beta[2]:.3f}, c1={beta[3]:.3f}, c2={beta[4]:.3f}")
        print()
        print(f"{'Nuclide':<10} {'A':>4} {'d(n)':>6} {'log t exp':>10} {'log t GN':>10} {'log t full':>11} {'Δ(full)':>8}")

        for d in SUPERHEAVY:
            log_t_exp = math.log10(d['t12_s'])
            log_t_full = predict_single(d, beta, p)
            log_t_gn = baseline_gn_predict(d, beta)
            dn = calc_d_n(calc_n_A(d['A'], p))
            delta = abs(log_t_exp - log_t_full)

            status = "✓" if delta < 1.5 else ("⚠" if delta < 2.0 else "✗")
            print(f"{d['nuclide']:<10} {d['A']:>4} {dn:>6.2f} {log_t_exp:>10.2f} "
                  f"{log_t_gn:>10.2f} {log_t_full:>11.2f} {delta:>7.2f} {status}")

    print("\n" + "="*80)
    print("CONCLUSION")
    print("="*80)
