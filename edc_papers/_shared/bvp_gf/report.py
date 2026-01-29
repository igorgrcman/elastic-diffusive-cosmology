#!/usr/bin/env python3
"""
report.py — Gate Report Generator for G_F BVP Pipeline

Issue: OPR-21 — Thick-brane BVP solution for G_F non-circular chain
Reference: docs/GF_NONCIRCULAR_FRAMEWORK_NOTE.md

This module generates:
- docs/GF_BVP_GATE_REPORT.md (human-readable gate evaluation)
- out/results.json (machine-readable results)
- out/profiles_*.csv (mode profile data)

Status: [OPEN] — Pipeline implemented, physics values provisional
"""

import json
import os
import subprocess
from datetime import datetime
from dataclasses import asdict
from typing import Dict, Optional
import numpy as np

from bvp_core import BVPSolution, ModeProfile
from overlaps import OverlapResults, GateEvaluation


# =============================================================================
# Utility Functions
# =============================================================================

def get_git_hash() -> str:
    """Get current git commit hash for reproducibility."""
    try:
        result = subprocess.run(
            ['git', 'rev-parse', '--short', 'HEAD'],
            capture_output=True, text=True, timeout=5
        )
        return result.stdout.strip() if result.returncode == 0 else "unknown"
    except Exception:
        return "unknown"


def get_config_digest(config: Dict) -> str:
    """Generate a short digest of the config for reproducibility."""
    import hashlib
    config_str = json.dumps(config, sort_keys=True)
    return hashlib.md5(config_str.encode()).hexdigest()[:8]


# =============================================================================
# JSON Results Output
# =============================================================================

def write_results_json(solution: BVPSolution, overlaps: OverlapResults,
                       gates: GateEvaluation, config: Dict,
                       output_path: str) -> None:
    """
    Write machine-readable results to JSON file.
    """
    results = {
        "metadata": {
            "generated": datetime.now().isoformat(),
            "git_hash": get_git_hash(),
            "config_digest": get_config_digest(config),
            "pipeline_version": "1.0.0",
            "status": "toy_baseline" if config.get('quick_run', {}).get('enabled', False) else "bvp_solution"
        },
        "solution": {
            "background_type": solution.background_type,
            "delta_GeV_inv": solution.delta,
            "domain_GeV_inv": list(solution.domain),
            "solver_method": solution.solver_method,
            "converged": solution.converged,
            "error_message": solution.error_message
        },
        "eigenvalues": {
            "lambda_w_L": solution.w_L.eigenvalue if solution.w_L else None,
            "lambda_w_R": solution.w_R.eigenvalue if solution.w_R else None,
            "lambda_w_phi": solution.w_phi.eigenvalue if solution.w_phi else None,
        },
        "overlaps": {
            "I_4_GeV": overlaps.I_4,
            "I_g": overlaps.I_g,
            "epsilon": overlaps.epsilon,
            "g5_squared_GeV_inv": overlaps.g5_squared,
            "g_eff_squared": overlaps.g_eff_squared,
            "M_eff_GeV": overlaps.M_eff,
            "M_eff_squared_GeV2": overlaps.M_eff_squared,
        },
        "target_comparison": {
            "X_EDC": overlaps.X_EDC,
            "X_target": overlaps.X_target,
            "X_ratio": overlaps.X_ratio,
            "X_error_percent": abs(overlaps.X_ratio - 1.0) * 100
        },
        "gates": {
            "gate1_I4": {
                "pass": gates.gate1_I4_pass,
                "ratio": gates.gate1_I4_ratio,
                "message": gates.gate1_message
            },
            "gate2_mass": {
                "pass": gates.gate2_mass_pass,
                "ratio": gates.gate2_mass_ratio,
                "message": gates.gate2_message
            },
            "gate3_coupling": {
                "pass": gates.gate3_coupling_pass,
                "ratio": gates.gate3_coupling_ratio,
                "message": gates.gate3_message
            },
            "all_pass": gates.all_gates_pass,
            "verdict": gates.overall_verdict,
            "fail_codes": gates.fail_codes
        }
    }

    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)


# =============================================================================
# CSV Profile Output
# =============================================================================

def write_profile_csv(mode: ModeProfile, output_path: str) -> None:
    """
    Write mode profile to CSV file.
    """
    header = "chi_GeV_inv,profile,profile_squared\n"

    with open(output_path, 'w') as f:
        f.write(f"# Mode: {mode.name}\n")
        f.write(f"# Eigenvalue: {mode.eigenvalue}\n")
        f.write(f"# Normalization: {mode.normalization}\n")
        f.write(f"# Nodes: {mode.n_nodes}\n")
        f.write(f"# Normalizable: {mode.is_normalizable}\n")
        f.write(header)

        for i, chi in enumerate(mode.chi):
            w = mode.profile[i]
            f.write(f"{chi:.10e},{w:.10e},{w**2:.10e}\n")


def write_all_profiles(solution: BVPSolution, output_dir: str) -> list:
    """
    Write all mode profiles to CSV files.

    Returns list of created files.
    """
    files_created = []

    for mode in [solution.w_L, solution.w_R, solution.w_phi]:
        if mode is not None:
            filename = f"profiles_{mode.name}.csv"
            filepath = os.path.join(output_dir, filename)
            write_profile_csv(mode, filepath)
            files_created.append(filepath)

    return files_created


# =============================================================================
# Markdown Report Generation
# =============================================================================

def generate_gate_report(solution: BVPSolution, overlaps: OverlapResults,
                         gates: GateEvaluation, config: Dict) -> str:
    """
    Generate markdown report for G_F BVP gate evaluation.
    """
    git_hash = get_git_hash()
    config_digest = get_config_digest(config)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    is_toy = config.get('quick_run', {}).get('enabled', False)
    run_type = "TOY BASELINE" if is_toy else "BVP SOLUTION"

    # Status indicator
    if gates.all_gates_pass:
        status_color = "GREEN"
        status_icon = "✓"
    elif any([gates.gate1_I4_pass, gates.gate2_mass_pass, gates.gate3_coupling_pass]):
        status_color = "YELLOW"
        status_icon = "⚠"
    else:
        status_color = "RED"
        status_icon = "✗"

    report = f"""# G_F BVP Gate Report

**Generated:** {timestamp}
**Git commit:** `{git_hash}`
**Config digest:** `{config_digest}`
**Run type:** {run_type}
**Overall status:** {status_icon} **{status_color}**

---

## Executive Summary

| Metric | Value | Status |
|--------|-------|--------|
| X_EDC / X_target | {overlaps.X_ratio:.3f} | {"✓" if 0.9 < overlaps.X_ratio < 1.1 else "⚠"} |
| Gate 1 (I_4) | {gates.gate1_I4_ratio:.2e} | {"✓" if gates.gate1_I4_pass else "✗"} |
| Gate 2 (M_eff) | {gates.gate2_mass_ratio:.2f} | {"✓" if gates.gate2_mass_pass else "✗"} |
| Gate 3 (g_eff²) | {gates.gate3_coupling_ratio:.2f} | {"✓" if gates.gate3_coupling_pass else "✗"} |

**Verdict:** {gates.overall_verdict}

"""

    if gates.fail_codes:
        report += f"**Fail codes:** `{', '.join(gates.fail_codes)}`\n\n"

    report += f"""---

## 1. BVP Solution Summary

| Parameter | Value | Unit |
|-----------|-------|------|
| Background | {solution.background_type} | — |
| δ (brane thickness) | {solution.delta:.4f} | GeV⁻¹ |
| Domain | [{solution.domain[0]:.2f}, {solution.domain[1]:.2f}] | GeV⁻¹ |
| Solver | {solution.solver_method} | — |
| Converged | {solution.converged} | — |

"""

    if solution.error_message and solution.error_message != "OK":
        report += f"**Solver message:** {solution.error_message}\n\n"

    report += """### Mode Profiles

| Mode | λ (eigenvalue) | Normalizable | Nodes |
|------|----------------|--------------|-------|
"""

    for mode in [solution.w_L, solution.w_R, solution.w_phi]:
        if mode is not None:
            report += f"| {mode.name} | {mode.eigenvalue:.4f} | {mode.is_normalizable} | {mode.n_nodes} |\n"

    report += f"""

---

## 2. Overlap Integrals

| Integral | Value | Unit | Definition |
|----------|-------|------|------------|
| I_4 | {overlaps.I_4:.4e} | GeV | ∫ dχ w_L² w_R² w_φ² |
| I_g | {overlaps.I_g:.4f} | — | ∫ dχ w_φ² |
| ε | {overlaps.epsilon:.4e} | — | ∫ dχ w_L w_R |

---

## 3. Derived Quantities

| Quantity | Value | Unit | Status |
|----------|-------|------|--------|
| g_5² | {overlaps.g5_squared:.4e} | GeV⁻¹ | [Dc] |
| g_eff² | {overlaps.g_eff_squared:.4e} | — | [Dc] |
| M_eff | {overlaps.M_eff:.4f} | GeV | [OPEN] |
| λ_0 | {overlaps.lambda_0:.4f} | — | [OPEN] |

---

## 4. Target Comparison

### Formula
```
X_EDC = C × (g_5² × I_4 × m_e²) / M_eff²

where C = 1/(4√2) ≈ 0.177
```

### Values

| Quantity | Value |
|----------|-------|
| X_target | {overlaps.X_target:.4e} |
| X_EDC | {overlaps.X_EDC:.4e} |
| X_EDC / X_target | {overlaps.X_ratio:.4f} |
| Error | {abs(overlaps.X_ratio - 1.0) * 100:.1f}% |

---

## 5. Gate Evaluation

### Gate 1: Overlap Window

**Criterion:** I_4 ∈ [0.1, 10] × I_4_required

| Metric | Value |
|--------|-------|
| I_4 (computed) | {overlaps.I_4:.4e} GeV |
| I_4 (required for target) | {overlaps.I_4 / gates.gate1_I4_ratio:.4e} GeV |
| Ratio | {gates.gate1_I4_ratio:.2e} |
| **Result** | {gates.gate1_message} |

### Gate 2: Mass Scaling

**Criterion:** M_eff ∈ [0.1, 10] × (1/δ)

| Metric | Value |
|--------|-------|
| M_eff (computed) | {overlaps.M_eff:.4f} GeV |
| 1/δ (expected) | {1.0/solution.delta:.4f} GeV |
| Ratio | {gates.gate2_mass_ratio:.2f} |
| **Result** | {gates.gate2_message} |

### Gate 3: Coupling Compatibility

**Criterion:** g_eff² ∈ [0.1, 10] × (4πα/sin²θ_W)

| Metric | Value |
|--------|-------|
| g_eff² (computed) | {overlaps.g_eff_squared:.4e} |
| 4πα/sin²θ_W | {4 * 3.14159 * 0.0073 / 0.25:.4f} |
| Ratio | {gates.gate3_coupling_ratio:.2f} |
| **Result** | {gates.gate3_message} |

---

## 6. Reproducibility

To reproduce this run:

```bash
cd edc_papers/_shared/bvp_gf
python3 bvp_driver.py --config config.yaml
```

**Outputs:**
- `out/results.json` — Machine-readable results
- `out/profiles_*.csv` — Mode profile data
- `docs/GF_BVP_GATE_REPORT.md` — This report

---

## 7. Caveats

"""

    if is_toy:
        report += """⚠️ **This is a TOY BASELINE run.**

The mode profiles are simplified exponential ansätze, NOT solutions to the
thick-brane BVP. The results demonstrate pipeline functionality but do NOT
represent physical predictions.

To run with actual BVP solution, set `quick_run.enabled: false` in config.yaml.

"""
    else:
        report += """⚠️ **Physics background is provisional.**

The background geometry and fermion localization model are working assumptions.
The BVP solution is mathematically correct for the specified potential, but
the physical identification with EDC brane structure requires further validation.

"""

    report += f"""---

## Cross-References

| Document | Content |
|----------|---------|
| `docs/GF_NONCIRCULAR_FRAMEWORK_NOTE.md` | Framework overview |
| `edc_papers/_shared/derivations/gf_noncircular_chain_framework.tex` | Full derivation |
| `edc_papers/_shared/bvp_gf/config.yaml` | Pipeline configuration |
| `edc_papers/_shared/bvp_gf/README.md` | Usage instructions |

---

*Report generated by `edc_papers/_shared/bvp_gf/report.py`*
"""

    return report


def write_gate_report(solution: BVPSolution, overlaps: OverlapResults,
                      gates: GateEvaluation, config: Dict,
                      output_path: str) -> None:
    """
    Write gate report to markdown file.
    """
    report = generate_gate_report(solution, overlaps, gates, config)

    with open(output_path, 'w') as f:
        f.write(report)


# =============================================================================
# Test / Demo
# =============================================================================

if __name__ == "__main__":
    print("Report Module — Test Run")
    print("=" * 60)
    print(f"Git hash: {get_git_hash()}")
    print("Test complete.")
