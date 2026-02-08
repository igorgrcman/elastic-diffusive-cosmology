#!/usr/bin/env python3
"""
V7.8 Dataset Augmentation Script
Adds proxy_deform and proxy_Salpha columns to V7.4 dataset
"""

import csv
import math

# Input/output paths (relative to script location)
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIT_DIR = os.path.dirname(SCRIPT_DIR)
BASE_AUDIT = os.path.dirname(AUDIT_DIR)
INPUT_CSV = os.path.join(BASE_AUDIT, "radioactivity_v7_4_alpha100", "04_ALPHA100_DATASET.csv")
OUTPUT_CSV = os.path.join(AUDIT_DIR, "04_DATASET_AUGMENTATION.csv")

def compute_proxy_deform(Z, A):
    """
    Shell distance deformation proxy.
    proxy_deform = |N - 126| * |Z - 82| / 1000
    """
    N = A - Z
    return abs(N - 126) * abs(Z - 82) / 1000.0

def compute_proxy_Salpha(Z, A):
    """
    Royer preformation estimate (log10 scale).
    log10(P_alpha) = -2.52 + 0.0121*Z - 0.0087*N + 0.0023*A
    """
    N = A - Z
    log_Pa = -2.52 + 0.0121 * Z - 0.0087 * N + 0.0023 * A
    return log_Pa

def main():
    rows = []

    with open(INPUT_CSV, 'r') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + [
            'proxy_deform',
            'proxy_Salpha',
            'proxy_deform_source',
            'proxy_Salpha_source'
        ]

        for row in reader:
            Z = int(row['Z'])
            A = int(row['A'])

            # Compute proxies
            row['proxy_deform'] = f"{compute_proxy_deform(Z, A):.4f}"
            row['proxy_Salpha'] = f"{compute_proxy_Salpha(Z, A):.4f}"
            row['proxy_deform_source'] = "D4"  # Derived shell distance
            row['proxy_Salpha_source'] = "D3"  # Royer 2010

            rows.append(row)

    # Write augmented dataset
    with open(OUTPUT_CSV, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {OUTPUT_CSV}")

    # Print summary statistics
    deform_vals = [float(r['proxy_deform']) for r in rows]
    salpha_vals = [float(r['proxy_Salpha']) for r in rows]

    print(f"\nproxy_deform: min={min(deform_vals):.3f}, max={max(deform_vals):.3f}, mean={sum(deform_vals)/len(deform_vals):.3f}")
    print(f"proxy_Salpha: min={min(salpha_vals):.3f}, max={max(salpha_vals):.3f}, mean={sum(salpha_vals)/len(salpha_vals):.3f}")

if __name__ == "__main__":
    main()
