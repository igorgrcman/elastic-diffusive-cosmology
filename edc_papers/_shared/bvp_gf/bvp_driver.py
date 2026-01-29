#!/usr/bin/env python3
"""
bvp_driver.py — Main Driver for G_F BVP Pipeline

Issue: OPR-21 — Thick-brane BVP solution for G_F non-circular chain
Reference: docs/GF_NONCIRCULAR_FRAMEWORK_NOTE.md

Usage:
    python3 bvp_driver.py --config config.yaml
    python3 bvp_driver.py --config config.yaml --quick-run
    python3 bvp_driver.py --help

Outputs:
    out/results.json        — Machine-readable results
    out/profiles_*.csv      — Mode profile data
    docs/GF_BVP_GATE_REPORT.md — Gate evaluation report

Status: [OPEN] — Pipeline implemented, physics values provisional
"""

import argparse
import os
import sys
import yaml
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bvp_core import solve_thick_brane_bvp, generate_toy_profiles, BVPSolution
from overlaps import compute_all_overlaps, evaluate_gates, OverlapResults, GateEvaluation
from report import (write_results_json, write_all_profiles, write_gate_report,
                    get_git_hash, get_config_digest)


# =============================================================================
# Configuration Loading
# =============================================================================

def load_config(config_path: str) -> dict:
    """Load configuration from YAML file."""
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config


def validate_config(config: dict) -> bool:
    """Validate configuration has required fields."""
    required_sections = ['physical', 'background', 'domain', 'modes', 'solver', 'gates']

    for section in required_sections:
        if section not in config:
            print(f"ERROR: Missing required config section: {section}")
            return False

    required_physical = ['delta_GeV_inv', 'm_e_GeV', 'alpha', 'sin2_theta_W', 'X_target']
    for field in required_physical:
        if field not in config['physical']:
            print(f"ERROR: Missing required physical parameter: {field}")
            return False

    return True


# =============================================================================
# Main Pipeline
# =============================================================================

def run_pipeline(config: dict, output_dir: str, docs_dir: str,
                 quick_run: bool = False, verbose: int = 1) -> int:
    """
    Run the complete BVP pipeline.

    Args:
        config: Configuration dictionary
        output_dir: Directory for output files
        docs_dir: Directory for documentation (gate report)
        quick_run: If True, use toy profiles instead of BVP
        verbose: Verbosity level (0=silent, 1=summary, 2=detailed)

    Returns:
        0 on success, 1 on failure
    """
    if verbose >= 1:
        print("=" * 70)
        print("G_F BVP Pipeline — OPR-21")
        print("=" * 70)
        print(f"\nGit commit: {get_git_hash()}")
        print(f"Config digest: {get_config_digest(config)}")
        print()

    # Override quick_run from config if specified
    if quick_run:
        config.setdefault('quick_run', {})['enabled'] = True

    is_quick = config.get('quick_run', {}).get('enabled', False)

    # -------------------------------------------------------------------------
    # Step 1: Solve BVP (or generate toy profiles)
    # -------------------------------------------------------------------------
    if verbose >= 1:
        if is_quick:
            print("Step 1: Generating toy profiles (quick-run mode)...")
        else:
            print("Step 1: Solving thick-brane BVP...")

    try:
        if is_quick:
            solution = generate_toy_profiles(config)
        else:
            solution = solve_thick_brane_bvp(config)
    except Exception as e:
        print(f"ERROR in BVP solver: {e}")
        return 1

    if verbose >= 2:
        print(f"  Background: {solution.background_type}")
        print(f"  Converged: {solution.converged}")
        if solution.error_message != "OK":
            print(f"  Message: {solution.error_message}")

    if not solution.converged and not is_quick:
        print(f"WARNING: BVP did not converge: {solution.error_message}")

    # -------------------------------------------------------------------------
    # Step 2: Compute overlaps
    # -------------------------------------------------------------------------
    if verbose >= 1:
        print("Step 2: Computing overlap integrals...")

    try:
        overlaps = compute_all_overlaps(solution, config)
    except Exception as e:
        print(f"ERROR in overlap computation: {e}")
        return 1

    if verbose >= 2:
        print(f"  I_4 = {overlaps.I_4:.4e} GeV")
        print(f"  I_g = {overlaps.I_g:.4f}")
        print(f"  ε = {overlaps.epsilon:.4e}")
        print(f"  M_eff = {overlaps.M_eff:.4f} GeV")
        print(f"  X_EDC = {overlaps.X_EDC:.4e}")
        print(f"  X_EDC / X_target = {overlaps.X_ratio:.4f}")

    # -------------------------------------------------------------------------
    # Step 3: Evaluate gates
    # -------------------------------------------------------------------------
    if verbose >= 1:
        print("Step 3: Evaluating falsification gates...")

    gates = evaluate_gates(overlaps, config)

    if verbose >= 1:
        print(f"\n  Gate 1 (I_4):    {gates.gate1_message}")
        print(f"  Gate 2 (M_eff):  {gates.gate2_message}")
        print(f"  Gate 3 (g_eff²): {gates.gate3_message}")
        print(f"\n  Verdict: {gates.overall_verdict}")

    # -------------------------------------------------------------------------
    # Step 4: Write outputs
    # -------------------------------------------------------------------------
    if verbose >= 1:
        print("\nStep 4: Writing output files...")

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(docs_dir, exist_ok=True)

    # Write results.json
    results_path = os.path.join(output_dir, "results.json")
    write_results_json(solution, overlaps, gates, config, results_path)
    if verbose >= 2:
        print(f"  Written: {results_path}")

    # Write profile CSVs
    profile_files = write_all_profiles(solution, output_dir)
    if verbose >= 2:
        for f in profile_files:
            print(f"  Written: {f}")

    # Write gate report
    report_path = os.path.join(docs_dir, "GF_BVP_GATE_REPORT.md")
    write_gate_report(solution, overlaps, gates, config, report_path)
    if verbose >= 2:
        print(f"  Written: {report_path}")

    # -------------------------------------------------------------------------
    # Summary
    # -------------------------------------------------------------------------
    if verbose >= 1:
        print("\n" + "=" * 70)
        print("SUMMARY")
        print("=" * 70)
        print(f"\nRun type: {'TOY BASELINE' if is_quick else 'BVP SOLUTION'}")
        print(f"\nKey results:")
        print(f"  M_eff = {overlaps.M_eff:.4f} GeV")
        print(f"  I_4 = {overlaps.I_4:.4e} GeV")
        print(f"  X_EDC = {overlaps.X_EDC:.4e}")
        print(f"  X_target = {overlaps.X_target:.4e}")
        print(f"  X_EDC / X_target = {overlaps.X_ratio:.4f}")
        print(f"\nGate verdict: {gates.overall_verdict}")
        if gates.fail_codes:
            print(f"Fail codes: {', '.join(gates.fail_codes)}")
        print(f"\nOutputs:")
        print(f"  {results_path}")
        for f in profile_files:
            print(f"  {f}")
        print(f"  {report_path}")
        print("\n" + "=" * 70)

    return 0


# =============================================================================
# Command Line Interface
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="G_F BVP Pipeline — OPR-21: Thick-brane mode profiles and overlaps",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python3 bvp_driver.py --config config.yaml
    python3 bvp_driver.py --config config.yaml --quick-run
    python3 bvp_driver.py --config config.yaml -v 2

Reference:
    docs/GF_NONCIRCULAR_FRAMEWORK_NOTE.md
    edc_papers/_shared/derivations/gf_noncircular_chain_framework.tex
"""
    )

    parser.add_argument(
        '--config', '-c',
        type=str,
        default='config.yaml',
        help='Path to configuration YAML file (default: config.yaml)'
    )

    parser.add_argument(
        '--quick-run', '-q',
        action='store_true',
        help='Use toy profiles instead of BVP solution (fast, for testing)'
    )

    parser.add_argument(
        '--output-dir', '-o',
        type=str,
        default=None,
        help='Output directory (default: out/ relative to config)'
    )

    parser.add_argument(
        '--docs-dir', '-d',
        type=str,
        default=None,
        help='Documentation directory (default: ../../../docs relative to config)'
    )

    parser.add_argument(
        '--verbose', '-v',
        type=int,
        default=1,
        choices=[0, 1, 2],
        help='Verbosity level: 0=silent, 1=summary, 2=detailed (default: 1)'
    )

    args = parser.parse_args()

    # Resolve paths
    config_path = Path(args.config).resolve()

    if not config_path.exists():
        print(f"ERROR: Config file not found: {config_path}")
        sys.exit(1)

    # Load config
    config = load_config(str(config_path))

    if not validate_config(config):
        sys.exit(1)

    # Resolve output directories
    config_dir = config_path.parent

    if args.output_dir:
        output_dir = Path(args.output_dir).resolve()
    else:
        output_dir = config_dir / config.get('output', {}).get('dir', 'out')

    if args.docs_dir:
        docs_dir = Path(args.docs_dir).resolve()
    else:
        # Default: repo docs/ directory
        docs_dir = config_dir.parent.parent.parent / 'docs'

    # Run pipeline
    exit_code = run_pipeline(
        config=config,
        output_dir=str(output_dir),
        docs_dir=str(docs_dir),
        quick_run=args.quick_run,
        verbose=args.verbose
    )

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
