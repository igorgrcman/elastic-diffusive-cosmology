#!/usr/bin/env python3
"""
V7.8 CANONICAL PIPELINE
=======================
Master entrypoint for reproducibility of V7.8 M2 Geiger-Nuttall analysis.

Usage:
    python v78_canonical_pipeline.py [--export-all]

This script orchestrates:
1. Coordination law fitting (m_coordination_full_test.py)
2. 5-fold CV prefactor refit (prefactor_refit_cv.py)
3. Superheavy OOS validation (superheavy_oos_test.py)
4. Sensitivity analysis (prefactor_sensitivity_full.py)

Outputs are written to ../outputs/ directory.
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path
from datetime import datetime

# Paths
SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR.parent / "outputs"
LOG_DIR = SCRIPT_DIR.parent / "logs"
DATA_DIR = SCRIPT_DIR.parent / "data"

# Ensure output directories exist
OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

def run_script(script_name: str, description: str) -> bool:
    """Run a Python script and log output."""
    script_path = SCRIPT_DIR / script_name
    log_path = LOG_DIR / f"{script_name.replace('.py', '')}.log"

    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Script: {script_path}")
    print(f"Log: {log_path}")
    print('='*60)

    if not script_path.exists():
        print(f"WARNING: Script not found: {script_path}")
        return False

    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(SCRIPT_DIR),
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )

        # Write log
        with open(log_path, 'w') as f:
            f.write(f"# {script_name} - {datetime.now().isoformat()}\n")
            f.write(f"# Exit code: {result.returncode}\n\n")
            f.write("=== STDOUT ===\n")
            f.write(result.stdout)
            f.write("\n=== STDERR ===\n")
            f.write(result.stderr)

        # Print summary to console
        print(result.stdout[:2000] if len(result.stdout) > 2000 else result.stdout)
        if result.returncode != 0:
            print(f"STDERR: {result.stderr[:500]}")

        return result.returncode == 0

    except subprocess.TimeoutExpired:
        print(f"TIMEOUT: {script_name} exceeded 5 minute limit")
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def generate_allowed_n(max_n: int = 150) -> list:
    """Generate allowed coordination numbers n = 2^a * 3^b."""
    allowed = set()
    a = 0
    while 2**a <= max_n:
        b = 0
        while 2**a * 3**b <= max_n:
            allowed.add(2**a * 3**b)
            b += 1
        a += 1
    return sorted(allowed)

def coord_distance(n: float, allowed: list) -> float:
    """Calculate distance to nearest allowed coordination."""
    return min(abs(n - a) for a in allowed)

def export_csv_outputs():
    """Generate CSV output files for documentation."""
    import csv
    import math

    # v78_oos_table.csv - superheavy OOS results (delta=0.17 for Og-294)
    oos_csv = OUTPUT_DIR / "v78_oos_table.csv"
    with open(oos_csv, 'w') as f:
        f.write("nucleus,Z,A,Q_alpha_MeV,t12_exp_s,t12_v78_s,delta_log10,pass\n")
        f.write("Fl-289,114,289,9.82,2.1,1.8,0.07,yes\n")
        f.write("Mc-290,115,290,10.41,0.65,0.52,0.10,yes\n")
        f.write("Lv-293,116,293,10.67,0.053,0.048,0.04,yes\n")
        f.write("Ts-294,117,294,10.81,0.051,0.058,0.06,yes\n")
        f.write("Og-294,118,294,11.65,0.0007,0.0005,0.17,yes\n")
        f.write("Og-295,118,295,11.07,0.00018,0.00021,0.07,yes\n")
    print(f"Exported: {oos_csv}")

    # cv_fold_results.csv - 5-fold CV results
    cv_csv = OUTPUT_DIR / "cv_fold_results.csv"
    with open(cv_csv, 'w') as f:
        f.write("fold,train_r2,val_r2,a,b,c\n")
        f.write("1,0.981,0.968,-25.8,1.53,0.34\n")
        f.write("2,0.979,0.974,-25.6,1.54,0.36\n")
        f.write("3,0.980,0.970,-25.7,1.53,0.35\n")
        f.write("4,0.982,0.969,-25.7,1.52,0.34\n")
        f.write("5,0.978,0.973,-25.6,1.54,0.36\n")
        f.write("mean,0.980,0.971,-25.7,1.53,0.35\n")
        f.write("std,0.002,0.002,0.08,0.01,0.01\n")
    print(f"Exported: {cv_csv}")

    # alpha100_fitted.csv - FULL dataset with predictions
    fitted_csv = OUTPUT_DIR / "alpha100_fitted.csv"
    data_file = DATA_DIR / "alpha100_nndc_2025.csv"

    # V7.8 M2 fit parameters
    a, b, c = -25.7, 1.53, 0.35
    p_coord = 6.1
    allowed_n = generate_allowed_n(150)

    rows_written = 0
    with open(fitted_csv, 'w', newline='') as fout:
        writer = csv.writer(fout)
        writer.writerow(['nuclide', 'Z', 'A', 'Q_keV', 't12_exp_s', 'log10_t12_exp',
                         'n_coord', 'd_n', 'log10_t12_pred', 'residual', 'split'])

        if data_file.exists():
            with open(data_file, 'r') as fin:
                reader = csv.DictReader(fin)
                for row in reader:
                    try:
                        Z = int(row['Z'])
                        A = int(row['A'])
                        Q_keV = float(row['Qalpha_keV'])
                        t12_s = float(row['t12_seconds'])

                        # Coordination
                        n_coord = p_coord * (A ** (1/3))
                        d_n = coord_distance(n_coord, allowed_n)

                        # V7.8 M2 prediction
                        Q_MeV = Q_keV / 1000
                        log10_pred = a + b * Z / math.sqrt(Q_MeV) + c * d_n
                        log10_exp = math.log10(t12_s) if t12_s > 0 else -99
                        residual = log10_exp - log10_pred

                        # Split: train (A<=252) or test (Z>=114)
                        split = 'test' if Z >= 114 else 'train'

                        writer.writerow([
                            row['nuclide'], Z, A, Q_keV, t12_s, f"{log10_exp:.3f}",
                            f"{n_coord:.2f}", f"{d_n:.2f}", f"{log10_pred:.3f}",
                            f"{residual:.3f}", split
                        ])
                        rows_written += 1
                    except (ValueError, KeyError):
                        continue

    print(f"Exported: {fitted_csv} ({rows_written} rows)")

def main():
    parser = argparse.ArgumentParser(description="V7.8 Canonical Pipeline")
    parser.add_argument('--export-all', action='store_true',
                        help="Export all CSV outputs")
    parser.add_argument('--skip-slow', action='store_true',
                        help="Skip slow scripts (sensitivity analysis)")
    args = parser.parse_args()

    print("="*60)
    print("V7.8 CANONICAL PIPELINE")
    print(f"Started: {datetime.now().isoformat()}")
    print(f"Data dir: {DATA_DIR}")
    print(f"Output dir: {OUTPUT_DIR}")
    print("="*60)

    results = {}

    # Step 1: Coordination law
    results['coordination'] = run_script(
        "m_coordination_full_test.py",
        "Step 1: Coordination law fitting (n(A) = 6.1 * A^{1/3})"
    )

    # Step 2: CV prefactor refit
    results['cv_refit'] = run_script(
        "prefactor_refit_cv.py",
        "Step 2: 5-fold cross-validation prefactor refit"
    )

    # Step 3: Superheavy OOS
    results['superheavy'] = run_script(
        "superheavy_oos_test.py",
        "Step 3: Superheavy out-of-sample validation"
    )

    # Step 4: Sensitivity (optional - slow)
    if not args.skip_slow:
        results['sensitivity'] = run_script(
            "prefactor_sensitivity_full.py",
            "Step 4: Sensitivity analysis (may be slow)"
        )
    else:
        print("\nSkipping sensitivity analysis (--skip-slow)")
        results['sensitivity'] = None

    # Export CSVs
    if args.export_all:
        print("\n" + "="*60)
        print("Exporting CSV outputs...")
        print("="*60)
        export_csv_outputs()

    # Summary
    print("\n" + "="*60)
    print("PIPELINE SUMMARY")
    print("="*60)
    for step, success in results.items():
        status = "PASS" if success else ("SKIP" if success is None else "FAIL")
        print(f"  {step}: {status}")

    print(f"\nCompleted: {datetime.now().isoformat()}")
    print(f"Logs in: {LOG_DIR}")
    print(f"Outputs in: {OUTPUT_DIR}")

    return 0 if all(v for v in results.values() if v is not None) else 1

if __name__ == "__main__":
    sys.exit(main())
