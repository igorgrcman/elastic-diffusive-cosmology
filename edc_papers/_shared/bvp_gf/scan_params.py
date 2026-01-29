#!/usr/bin/env python3
"""
scan_params.py — Parameter Scan for G_F BVP I4 Suppression

Issue: OPR-21b — Scan LR separation and fermion width to suppress I4
Goal: Find parameters where X_EDC / X_target ≈ 1

Scans over:
- LR_separation_delta: {0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0, 10.0}
- fermion_width_delta: {1.0, 0.8, 0.6, 0.4, 0.3, 0.2, 0.1, 0.05}

Outputs:
- out/scan_results.csv: Full scan results
- out/best_candidates.json: Top candidates ranked by closeness to ratio=1

Usage:
    python3 scan_params.py
    python3 scan_params.py --config config.yaml
"""

import os
import sys
import json
import csv
import copy
import argparse
from datetime import datetime
from pathlib import Path
import numpy as np

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import yaml
from bvp_core import solve_thick_brane_bvp, BVPSolution
from overlaps import compute_all_overlaps, evaluate_gates, OverlapResults, GateEvaluation
from report import get_git_hash, get_config_digest


# =============================================================================
# Scan Parameters
# =============================================================================

# Primary lever: LR separation (larger = less overlap)
LR_SEPARATION_VALUES = [0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0, 10.0, 12.0, 15.0]

# Secondary lever: fermion width (smaller = narrower modes = less overlap)
FERMION_WIDTH_VALUES = [1.0, 0.8, 0.6, 0.4, 0.3, 0.2, 0.1, 0.05, 0.02]

# Baseline values (from original config)
BASELINE_LR_SEP = 2.0
BASELINE_FERMION_WIDTH = 0.1
BASELINE_RATIO = 38.4


# =============================================================================
# Scan Functions
# =============================================================================

def load_config(config_path: str) -> dict:
    """Load base configuration from YAML."""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def run_single_point(config: dict, lr_sep: float, fw: float,
                     verbose: bool = False) -> dict:
    """
    Run BVP pipeline for a single parameter point.

    Returns dict with all relevant metrics.
    """
    # Modify config for this point
    cfg = copy.deepcopy(config)
    cfg['modes']['LR_separation_delta'] = lr_sep
    cfg['modes']['fermion_width_delta'] = fw

    # Use smaller grid for faster scan
    cfg['domain']['n_points'] = 501

    result = {
        'LR_separation_delta': lr_sep,
        'fermion_width_delta': fw,
        'converged': False,
        'normalizable': False,
        'M_eff': np.nan,
        'I_4': np.nan,
        'epsilon': np.nan,
        'X_EDC': np.nan,
        'X_ratio': np.nan,
        'log_ratio': np.nan,
        'gate1_pass': False,
        'gate2_pass': False,
        'gate3_pass': False,
        'all_gates_pass': False,
        'fail_codes': [],
        'error': ''
    }

    try:
        # Solve BVP
        solution = solve_thick_brane_bvp(cfg)

        result['converged'] = solution.converged

        # Check normalizability
        all_normalizable = True
        for mode in [solution.w_L, solution.w_R, solution.w_phi]:
            if mode is not None and not mode.is_normalizable:
                all_normalizable = False
        result['normalizable'] = all_normalizable

        if not solution.converged:
            result['error'] = solution.error_message
            return result

        # Compute overlaps
        overlaps = compute_all_overlaps(solution, cfg)
        result['M_eff'] = overlaps.M_eff
        result['I_4'] = overlaps.I_4
        result['epsilon'] = overlaps.epsilon
        result['X_EDC'] = overlaps.X_EDC
        result['X_ratio'] = overlaps.X_ratio

        # Compute log ratio (for ranking)
        if overlaps.X_ratio > 0:
            result['log_ratio'] = np.log10(overlaps.X_ratio)
        else:
            result['log_ratio'] = np.nan

        # Evaluate gates
        gates = evaluate_gates(overlaps, cfg)
        result['gate1_pass'] = gates.gate1_I4_pass
        result['gate2_pass'] = gates.gate2_mass_pass
        result['gate3_pass'] = gates.gate3_coupling_pass
        result['all_gates_pass'] = gates.all_gates_pass
        result['fail_codes'] = gates.fail_codes

        if verbose:
            status = "✓" if gates.all_gates_pass else "✗"
            print(f"  LR={lr_sep:4.1f}, fw={fw:5.3f}: ratio={overlaps.X_ratio:8.3f} {status}")

    except Exception as e:
        result['error'] = str(e)
        if verbose:
            print(f"  LR={lr_sep:4.1f}, fw={fw:5.3f}: ERROR: {e}")

    return result


def run_scan(config: dict, verbose: bool = True) -> list:
    """
    Run full parameter scan.

    Returns list of result dicts.
    """
    results = []
    total = len(LR_SEPARATION_VALUES) * len(FERMION_WIDTH_VALUES)

    if verbose:
        print(f"\nScanning {total} parameter points...")
        print(f"  LR_separation_delta: {LR_SEPARATION_VALUES}")
        print(f"  fermion_width_delta: {FERMION_WIDTH_VALUES}")
        print()

    count = 0
    for lr_sep in LR_SEPARATION_VALUES:
        for fw in FERMION_WIDTH_VALUES:
            count += 1
            if verbose and count % 10 == 0:
                print(f"Progress: {count}/{total}")

            result = run_single_point(config, lr_sep, fw, verbose=False)
            results.append(result)

    return results


def rank_results(results: list) -> list:
    """
    Rank results by closeness to ratio=1.

    Primary: minimize |log10(ratio)|
    Secondary: avoid non-normalizable, keep M_eff reasonable
    """
    valid_results = []

    for r in results:
        if not r['converged']:
            continue
        if not r['normalizable']:
            continue
        if np.isnan(r['X_ratio']) or r['X_ratio'] <= 0:
            continue

        # Compute score (lower is better)
        log_ratio = abs(np.log10(r['X_ratio']))

        # Penalize if Gate 2 fails (M_eff out of range)
        penalty = 0
        if not r['gate2_pass']:
            penalty += 10

        # Penalize if ratio is too far off (> 100)
        if r['X_ratio'] > 100 or r['X_ratio'] < 0.01:
            penalty += 5

        r['score'] = log_ratio + penalty
        valid_results.append(r)

    # Sort by score
    valid_results.sort(key=lambda x: x['score'])

    return valid_results


def write_scan_csv(results: list, output_path: str) -> None:
    """Write scan results to CSV."""
    fieldnames = [
        'LR_separation_delta', 'fermion_width_delta',
        'converged', 'normalizable',
        'M_eff', 'I_4', 'epsilon', 'X_EDC', 'X_ratio', 'log_ratio',
        'gate1_pass', 'gate2_pass', 'gate3_pass', 'all_gates_pass',
        'fail_codes', 'error'
    ]

    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        for r in results:
            # Convert fail_codes list to string
            row = r.copy()
            row['fail_codes'] = ','.join(r['fail_codes'])
            writer.writerow(row)


def write_best_candidates(ranked: list, output_path: str, top_n: int = 10) -> None:
    """Write best candidates to JSON."""
    candidates = []

    for i, r in enumerate(ranked[:top_n]):
        candidates.append({
            'rank': i + 1,
            'LR_separation_delta': float(r['LR_separation_delta']),
            'fermion_width_delta': float(r['fermion_width_delta']),
            'X_ratio': float(r['X_ratio']),
            'log_ratio': float(r['log_ratio']),
            'M_eff_GeV': float(r['M_eff']),
            'I_4_GeV': float(r['I_4']),
            'epsilon': float(r['epsilon']),
            'gate1_I4_pass': bool(r['gate1_pass']),
            'gate2_mass_pass': bool(r['gate2_pass']),
            'gate3_coupling_pass': bool(r['gate3_pass']),
            'all_gates_pass': bool(r['all_gates_pass']),
            'fail_codes': list(r['fail_codes']),
            'score': float(r['score'])
        })

    output = {
        'metadata': {
            'generated': datetime.now().isoformat(),
            'git_hash': get_git_hash(),
            'baseline_ratio': BASELINE_RATIO,
            'total_points_scanned': len(ranked),
            'top_n': top_n
        },
        'best_candidates': candidates
    }

    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)


def generate_scan_report(ranked: list, output_path: str) -> None:
    """Generate markdown scan report."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    git_hash = get_git_hash()

    # Get best candidate
    best = ranked[0] if ranked else None

    # Compute improvement
    if best:
        improvement = BASELINE_RATIO / best['X_ratio']
        new_ratio = best['X_ratio']
    else:
        improvement = 0
        new_ratio = np.nan

    report = f"""# G_F BVP Parameter Scan Report

**Generated:** {timestamp}
**Git commit:** `{git_hash}`
**Issue:** OPR-21b — Scan LR separation/width to suppress I4

---

## Executive Summary

| Metric | Baseline | Best Found | Improvement |
|--------|----------|------------|-------------|
| X_EDC / X_target | {BASELINE_RATIO:.1f} | {new_ratio:.3f} | {improvement:.1f}× |
| LR_separation_delta | {BASELINE_LR_SEP} | {best['LR_separation_delta'] if best else 'N/A'} | — |
| fermion_width_delta | {BASELINE_FERMION_WIDTH} | {best['fermion_width_delta'] if best else 'N/A'} | — |

"""

    if best:
        gate_status = "✓ ALL PASS" if best['all_gates_pass'] else f"✗ FAIL: {', '.join(best['fail_codes'])}"
        report += f"""**Best point gate status:** {gate_status}

---

## Scan Parameters

- **LR_separation_delta:** {LR_SEPARATION_VALUES}
- **fermion_width_delta:** {FERMION_WIDTH_VALUES}
- **Total points:** {len(LR_SEPARATION_VALUES) * len(FERMION_WIDTH_VALUES)}
- **Valid points:** {len(ranked)}

---

## Top 10 Candidates

| Rank | LR_sep | fw | X_ratio | M_eff (GeV) | I_4 (GeV) | Gates |
|------|--------|-----|---------|-------------|-----------|-------|
"""

    for i, r in enumerate(ranked[:10]):
        gates = "✓" if r['all_gates_pass'] else f"✗ ({','.join(r['fail_codes'][:1])})"
        report += f"| {i+1} | {r['LR_separation_delta']:.1f} | {r['fermion_width_delta']:.3f} | {r['X_ratio']:.3f} | {r['M_eff']:.3f} | {r['I_4']:.2e} | {gates} |\n"

    if best:
        report += f"""

---

## Best Candidate Analysis

### Parameters
```yaml
modes:
  LR_separation_delta: {best['LR_separation_delta']}
  fermion_width_delta: {best['fermion_width_delta']}
```

### Results
| Quantity | Value |
|----------|-------|
| M_eff | {best['M_eff']:.4f} GeV |
| I_4 | {best['I_4']:.4e} GeV |
| ε (chirality) | {best['epsilon']:.4e} |
| X_EDC / X_target | {best['X_ratio']:.4f} |

### Gate Evaluation
| Gate | Status | Notes |
|------|--------|-------|
| Gate 1 (I_4) | {'✓ PASS' if best['gate1_pass'] else '✗ FAIL'} | Overlap window |
| Gate 2 (M_eff) | {'✓ PASS' if best['gate2_pass'] else '✗ FAIL'} | Mass scaling |
| Gate 3 (g_eff²) | {'✓ PASS' if best['gate3_pass'] else '✗ FAIL'} | Coupling |

---

## What Improved I4

The primary mechanism for reducing I_4 (and thus X_EDC) is:

1. **Increased LR separation:** Moving w_L and w_R further apart reduces their
   overlap. The baseline LR_sep={BASELINE_LR_SEP} gave too much overlap.
   Best found: LR_sep={best['LR_separation_delta']}.

2. **Narrower fermion width:** Smaller fermion_width_delta makes the mode
   profiles narrower, reducing the tails that overlap.
   Baseline: fw={BASELINE_FERMION_WIDTH}, Best: fw={best['fermion_width_delta']}.

**Improvement factor:** I_4 reduced by approximately {BASELINE_RATIO / best['X_ratio']:.1f}× compared to baseline.

"""

    report += """---

## Caveats

1. **Physics background still provisional [Dc]:** The gaussian_wall potential
   and domain wall fermion model are ansätze.

2. **Parameters are tuned, not derived:** The best point is found by scanning,
   not from first-principles 5D action reduction.

3. **Gate windows are order-of-magnitude:** The [0.1, 10] windows allow
   significant flexibility.

---

## Files Generated

| File | Description |
|------|-------------|
| `out/scan_results.csv` | Full scan data ({len(ranked)} valid points) |
| `out/best_candidates.json` | Top 10 candidates with metadata |
| `docs/GF_BVP_PARAMETER_SCAN.md` | This report |

---

## Recommended Next Steps

1. Update config.yaml with best parameters
2. Re-run driver to update gate report
3. Consider deriving V(χ) from 5D action reduction

---

*Report generated by `scan_params.py`*
"""

    with open(output_path, 'w') as f:
        f.write(report)


# =============================================================================
# Main
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Parameter scan for G_F BVP I4 suppression"
    )
    parser.add_argument(
        '--config', '-c',
        type=str,
        default='config.yaml',
        help='Path to base configuration YAML'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Verbose output'
    )

    args = parser.parse_args()

    # Resolve paths
    script_dir = Path(__file__).parent
    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = script_dir / config_path

    output_dir = script_dir / 'out'
    docs_dir = script_dir.parent.parent.parent / 'docs'

    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(docs_dir, exist_ok=True)

    print("=" * 70)
    print("G_F BVP Parameter Scan — OPR-21b")
    print("=" * 70)
    print(f"\nGit commit: {get_git_hash()}")
    print(f"Config: {config_path}")
    print(f"Output: {output_dir}")

    # Load config
    config = load_config(str(config_path))

    # Run scan
    results = run_scan(config, verbose=args.verbose)

    # Rank results
    ranked = rank_results(results)

    print(f"\nValid points: {len(ranked)} / {len(results)}")

    if ranked:
        best = ranked[0]
        print(f"\nBest candidate:")
        print(f"  LR_separation_delta: {best['LR_separation_delta']}")
        print(f"  fermion_width_delta: {best['fermion_width_delta']}")
        print(f"  X_ratio: {best['X_ratio']:.4f}")
        print(f"  Improvement: {BASELINE_RATIO / best['X_ratio']:.1f}×")
        print(f"  Gates: {'ALL PASS' if best['all_gates_pass'] else 'FAIL: ' + ', '.join(best['fail_codes'])}")

    # Write outputs
    csv_path = output_dir / 'scan_results.csv'
    json_path = output_dir / 'best_candidates.json'
    report_path = docs_dir / 'GF_BVP_PARAMETER_SCAN.md'

    write_scan_csv(results, str(csv_path))
    print(f"\nWritten: {csv_path}")

    write_best_candidates(ranked, str(json_path))
    print(f"Written: {json_path}")

    generate_scan_report(ranked, str(report_path))
    print(f"Written: {report_path}")

    print("\n" + "=" * 70)
    print("Scan complete.")
    print("=" * 70)

    return 0


if __name__ == "__main__":
    sys.exit(main())
