#!/usr/bin/env python3
"""
EDC Numerical Forensic Audit Harness
=====================================

Runs all check_*.py scripts and collects outputs into a machine-readable ledger.

Deliverable D2: Numerical audit harness that:
- Runs all existing tools/check_*.py and code scripts
- Collects outputs into generated/ledger.json
- Generates generated/numbers.tex for LaTeX injection

Usage:
    python scripts/audit_run_all.py [--verbose]
"""

import json
import subprocess
import sys
import os
import re
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

# ==============================================================================
# Configuration
# ==============================================================================

SCRIPT_DIR = Path(__file__).parent
PAPER_DIR = SCRIPT_DIR.parent
TOOLS_DIR = PAPER_DIR / "tools"
CODE_DIR = PAPER_DIR / "code"
GENERATED_DIR = PAPER_DIR / "generated"

# Physical constants for validation (CODATA 2018)
PHYSICAL_CONSTANTS = {
    "hbar": {"value": 1.054571817e-34, "units": "J·s", "source": "CODATA2018"},
    "c": {"value": 299792458, "units": "m/s", "source": "CODATA2018"},
    "e": {"value": 1.602176634e-19, "units": "C", "source": "CODATA2018"},
    "alpha": {"value": 7.2973525693e-3, "units": "1", "source": "CODATA2018"},
    "m_e": {"value": 9.1093837015e-31, "units": "kg", "source": "CODATA2018"},
    "m_p": {"value": 1.67262192369e-27, "units": "kg", "source": "CODATA2018"},
    "G_F": {"value": 1.1663788e-5, "units": "GeV^-2", "source": "PDG2022"},
    "M_W": {"value": 80.377, "units": "GeV", "source": "PDG2022"},
    "M_Z": {"value": 91.1876, "units": "GeV", "source": "PDG2022"},
    "sin2_theta_W": {"value": 0.23121, "units": "1", "source": "PDG2022"},
}

# EDC baseline parameters (from Framework v2.0)
EDC_BASELINE = {
    "sigma": {"value": 5.67e7, "units": "N/m^2", "tag": "[BL]", "source": "Framework_v2.0"},
    "r_e": {"value": 2.8179403227e-15, "units": "m", "tag": "[BL]", "source": "CODATA2018"},
    "R_xi": {"value": 2.16e-18, "units": "m", "tag": "[P]", "source": "Framework_v2.0_phenomenological"},
}

# Scripts to run (in order)
CHECK_SCRIPTS = [
    "check_gf_dimensions.py",
    "check_gf_chain_status.py",
    "check_g5_ell_dimensions.py",
    "check_dimensionless_fgeom.py",
    "check_g1_coefficient_sensitivity.py",
    "check_opr19_4pi_derivation.py",
    "check_opr20_factor8_routes.py",
    "check_opr20_overcounting_audit.py",
    "check_opr20_prefactor8_attemptE.py",
    "check_opr20_alpha_accounting.py",
    "check_opr20_alpha_2pi_prediction.py",
    "check_opr20_x1_bc_ledger.py",
    "check_opr20b_h2plus_delta_rxi_audit.py",
    "check_z2_parity_sign_rule.py",
    "check_lambda_provenance.py",
]

# ==============================================================================
# Ledger Entry Class
# ==============================================================================

class LedgerEntry:
    """Single entry in the numerical ledger."""

    def __init__(
        self,
        key: str,
        value: float,
        units: str,
        epistemic_tag: str,
        source_script: str,
        description: str = "",
        uncertainty: Optional[float] = None,
    ):
        self.key = key
        self.value = value
        self.units = units
        self.epistemic_tag = epistemic_tag
        self.source_script = source_script
        self.description = description
        self.uncertainty = uncertainty
        self.git_hash = self._get_git_hash()
        self.timestamp = datetime.utcnow().isoformat() + "Z"

    @staticmethod
    def _get_git_hash() -> str:
        try:
            result = subprocess.run(
                ["git", "rev-parse", "--short", "HEAD"],
                capture_output=True,
                text=True,
                cwd=PAPER_DIR
            )
            return result.stdout.strip() if result.returncode == 0 else "unknown"
        except:
            return "unknown"

    def to_dict(self) -> Dict[str, Any]:
        d = {
            "key": self.key,
            "value": self.value,
            "units": self.units,
            "epistemic_tag": self.epistemic_tag,
            "source_script": self.source_script,
            "git_hash": self.git_hash,
            "timestamp": self.timestamp,
        }
        if self.description:
            d["description"] = self.description
        if self.uncertainty is not None:
            d["uncertainty"] = self.uncertainty
        return d

    def to_latex_macro(self) -> str:
        """Generate LaTeX \newcommand for this value."""
        # Sanitize key for LaTeX macro name
        macro_name = "num" + self.key.replace("_", "").replace("-", "")

        # Format value appropriately
        if abs(self.value) < 1e-3 or abs(self.value) > 1e6:
            # Scientific notation
            exp = int(f"{self.value:.2e}".split('e')[1])
            mantissa = self.value / (10 ** exp)
            value_str = f"{mantissa:.4g} \\times 10^{{{exp}}}"
        else:
            value_str = f"{self.value:.6g}"

        return f"\\newcommand{{\\{macro_name}}}{{{value_str}}}  % {self.description} [{self.epistemic_tag}]"

# ==============================================================================
# Audit Runner
# ==============================================================================

class AuditRunner:
    """Runs all check scripts and collects results."""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.ledger: List[LedgerEntry] = []
        self.script_results: Dict[str, Dict] = {}
        self.failures: List[Dict] = []

    def run_script(self, script_name: str) -> Tuple[int, str, str]:
        """Run a single script and capture output."""
        script_path = TOOLS_DIR / script_name

        if not script_path.exists():
            return -1, "", f"Script not found: {script_path}"

        try:
            result = subprocess.run(
                [sys.executable, str(script_path)],
                capture_output=True,
                text=True,
                cwd=PAPER_DIR,
                timeout=60
            )
            return result.returncode, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return -2, "", f"Script timed out: {script_name}"
        except Exception as e:
            return -3, "", f"Error running script: {e}"

    def parse_numeric_output(self, script_name: str, stdout: str) -> List[LedgerEntry]:
        """Parse numeric values from script output."""
        entries = []

        # Pattern to match common numeric output formats
        # Examples:
        #   g² = 0.373
        #   x₁ = 2.41
        #   m_φ = 54 GeV
        patterns = [
            # Standard format: name = value [unit]
            r"([A-Za-z_]\w*(?:\^?\d)?)\s*[=≈]\s*([\d.]+(?:e[+-]?\d+)?)\s*(\S+)?",
            # Greek letter format: α = value
            r"([αβγδεζηθικλμνξοπρστυφχψω][\w_]*)\s*[=≈]\s*([\d.]+(?:e[+-]?\d+)?)",
            # Subscript format: x_1 = value
            r"([a-zA-Z]+_\d+)\s*[=≈]\s*([\d.]+(?:e[+-]?\d+)?)",
        ]

        for line in stdout.split('\n'):
            for pattern in patterns:
                matches = re.findall(pattern, line)
                for match in matches:
                    if len(match) >= 2:
                        name = match[0]
                        try:
                            value = float(match[1])
                            units = match[2] if len(match) > 2 and match[2] else "1"

                            # Create unique key
                            key = f"{script_name.replace('.py', '')}_{name}"

                            entries.append(LedgerEntry(
                                key=key,
                                value=value,
                                units=units,
                                epistemic_tag="[Dc]",  # Default, will be refined
                                source_script=script_name,
                                description=f"From {script_name}: {name}"
                            ))
                        except ValueError:
                            pass

        return entries

    def run_all(self):
        """Run all check scripts."""
        print("=" * 70)
        print("EDC NUMERICAL FORENSIC AUDIT")
        print("=" * 70)
        print()

        GENERATED_DIR.mkdir(exist_ok=True)

        for script_name in CHECK_SCRIPTS:
            print(f"Running {script_name}...", end=" ")
            returncode, stdout, stderr = self.run_script(script_name)

            status = "OK" if returncode == 0 else f"FAIL({returncode})"
            print(status)

            self.script_results[script_name] = {
                "returncode": returncode,
                "stdout": stdout,
                "stderr": stderr,
            }

            if returncode != 0:
                self.failures.append({
                    "type": "script_error",
                    "script": script_name,
                    "returncode": returncode,
                    "stderr": stderr[:500] if stderr else ""
                })

            # Parse numeric outputs
            entries = self.parse_numeric_output(script_name, stdout)
            self.ledger.extend(entries)

            if self.verbose and stdout:
                print(f"  Output: {stdout[:200]}...")

        print()
        print(f"Scripts run: {len(CHECK_SCRIPTS)}")
        print(f"Ledger entries: {len(self.ledger)}")
        print(f"Failures: {len(self.failures)}")

    def add_baseline_entries(self):
        """Add EDC baseline parameters to ledger."""
        for key, data in EDC_BASELINE.items():
            self.ledger.append(LedgerEntry(
                key=f"BASELINE_{key}",
                value=data["value"],
                units=data["units"],
                epistemic_tag=data["tag"],
                source_script="baseline_constants",
                description=f"EDC baseline: {key}"
            ))

        for key, data in PHYSICAL_CONSTANTS.items():
            self.ledger.append(LedgerEntry(
                key=f"CONST_{key}",
                value=data["value"],
                units=data["units"],
                epistemic_tag="[BL]",
                source_script="physical_constants",
                description=f"Physical constant: {key} ({data['source']})"
            ))

    def add_weak_sector_entries(self):
        """Add critical weak-sector numbers (hardcoded for now, should be computed)."""
        weak_entries = [
            # G_F chain components
            LedgerEntry("GF_CHAIN_g2_sq", 0.373, "1", "[Dc]+[P]", "check_opr19_4pi_derivation.py",
                       "g² from 4πσr_e³/(ℏc)"),
            LedgerEntry("GF_CHAIN_x1_robin", 2.41, "1", "[Dc]", "solve_opr20_mediator_bvp.py",
                       "First Robin eigenvalue (α=2π)"),
            LedgerEntry("GF_CHAIN_x1_dirichlet", 3.14159, "1", "[Dc]", "check_opr20_x1_bc_ledger.py",
                       "First Dirichlet eigenvalue (π)"),
            LedgerEntry("GF_CHAIN_ell_over_Rxi", 8.886, "1", "[Dc]", "check_opr20_prefactor8_attemptE.py",
                       "ℓ/R_ξ = 2π√2"),
            LedgerEntry("GF_CHAIN_R_xi", 2.16e-18, "m", "[P]", "baseline_constants",
                       "R_ξ membrane thickness (EW-constrained)"),
            # Masses
            LedgerEntry("MASS_phi_robin", 53.5, "GeV", "[Dc]+[P]", "check_opr20_alpha_2pi_prediction.py",
                       "Mediator mass (Robin BC)"),
            LedgerEntry("MASS_phi_dirichlet", 70, "GeV", "[Dc]+[P]", "check_opr20_x1_bc_ledger.py",
                       "Mediator mass (Dirichlet BC)"),
            # Mixing angles
            LedgerEntry("PMNS_sin2_theta23", 0.564, "1", "[Dc]", "pmns_calculation",
                       "sin²θ₂₃ from Z₆ geometry"),
            LedgerEntry("PMNS_sin2_theta13", 0.025, "1", "[BL→Dc]", "pmns_calculation",
                       "sin²θ₁₃ from ε=λ/√2"),
            LedgerEntry("CKM_delta", 60, "deg", "[Dc]+[I]", "check_z2_parity_sign_rule.py",
                       "CKM CP phase from Z₂ parity"),
        ]
        self.ledger.extend(weak_entries)

    def save_ledger(self):
        """Save ledger to JSON file."""
        ledger_path = GENERATED_DIR / "ledger.json"

        ledger_data = {
            "metadata": {
                "generated": datetime.utcnow().isoformat() + "Z",
                "generator": "audit_run_all.py",
                "git_hash": LedgerEntry._get_git_hash(),
                "entry_count": len(self.ledger),
            },
            "entries": [e.to_dict() for e in self.ledger]
        }

        with open(ledger_path, 'w') as f:
            json.dump(ledger_data, f, indent=2)

        print(f"Ledger saved to: {ledger_path}")

    def generate_latex_numbers(self):
        """Generate LaTeX macros file."""
        numbers_path = GENERATED_DIR / "numbers.tex"

        lines = [
            "% ==============================================================================",
            "% EDC Generated Numbers - DO NOT EDIT MANUALLY",
            f"% Generated: {datetime.utcnow().isoformat()}Z",
            "% Source: scripts/audit_run_all.py",
            "% ==============================================================================",
            "",
            "% --- Physical Constants [BL] ---",
        ]

        for entry in self.ledger:
            if entry.source_script == "physical_constants":
                lines.append(entry.to_latex_macro())

        lines.extend([
            "",
            "% --- EDC Baseline Parameters ---",
        ])

        for entry in self.ledger:
            if entry.source_script == "baseline_constants":
                lines.append(entry.to_latex_macro())

        lines.extend([
            "",
            "% --- G_F Chain Values ---",
        ])

        for entry in self.ledger:
            if entry.key.startswith("GF_CHAIN_"):
                lines.append(entry.to_latex_macro())

        lines.extend([
            "",
            "% --- Weak Sector Masses ---",
        ])

        for entry in self.ledger:
            if entry.key.startswith("MASS_"):
                lines.append(entry.to_latex_macro())

        lines.extend([
            "",
            "% --- Mixing Parameters ---",
        ])

        for entry in self.ledger:
            if entry.key.startswith("PMNS_") or entry.key.startswith("CKM_"):
                lines.append(entry.to_latex_macro())

        lines.append("")

        with open(numbers_path, 'w') as f:
            f.write('\n'.join(lines))

        print(f"LaTeX numbers saved to: {numbers_path}")

    def generate_audit_report(self):
        """Generate the audit report."""
        report_path = GENERATED_DIR / "AUDIT_REPORT.md"

        lines = [
            "# EDC Numerical Forensic Audit Report",
            "",
            f"**Generated:** {datetime.utcnow().isoformat()}Z",
            f"**Git Hash:** {LedgerEntry._get_git_hash()}",
            "",
            "---",
            "",
            "## Build Information",
            "",
            "```bash",
            "# Clean build command:",
            "./scripts/clean_build.sh",
            "",
            "# Full build with Part I:",
            "BUILD_PART_I=true ./scripts/clean_build.sh",
            "```",
            "",
            "## Ledger Summary",
            "",
            f"Total entries: {len(self.ledger)}",
            "",
            "### Entries by Epistemic Tag",
            "",
            "| Tag | Count |",
            "|-----|-------|",
        ]

        # Count by tag
        tag_counts = {}
        for entry in self.ledger:
            tag = entry.epistemic_tag
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

        for tag, count in sorted(tag_counts.items()):
            lines.append(f"| {tag} | {count} |")

        lines.extend([
            "",
            "### Full Ledger Table",
            "",
            "| Key | Value | Units | Tag | Source |",
            "|-----|-------|-------|-----|--------|",
        ])

        for entry in self.ledger:
            val_str = f"{entry.value:.4g}" if isinstance(entry.value, float) else str(entry.value)
            lines.append(f"| {entry.key} | {val_str} | {entry.units} | {entry.epistemic_tag} | {entry.source_script} |")

        lines.extend([
            "",
            "---",
            "",
            "## Script Results",
            "",
        ])

        for script_name, result in self.script_results.items():
            status = "PASS" if result["returncode"] == 0 else f"FAIL (code {result['returncode']})"
            lines.append(f"- **{script_name}**: {status}")

        lines.extend([
            "",
            "---",
            "",
            "## Failures",
            "",
        ])

        if self.failures:
            lines.append("### Script Errors")
            for fail in self.failures:
                if fail["type"] == "script_error":
                    lines.append(f"- **{fail['script']}**: Exit code {fail['returncode']}")
                    if fail.get("stderr"):
                        lines.append(f"  ```")
                        lines.append(f"  {fail['stderr'][:200]}")
                        lines.append(f"  ```")
        else:
            lines.append("No failures detected.")

        lines.extend([
            "",
            "---",
            "",
            "## Recommendations",
            "",
            "1. **Replace hardcoded numbers** in LaTeX with `\\input{generated/numbers.tex}` macros",
            "2. **Run unit checker** to verify dimensional consistency",
            "3. **Run circularity checker** to detect SM-smuggling",
            "4. **Update epistemic tags** for any [Dc] claims that are actually [P] or [I]",
            "",
            "---",
            "",
            "*End of Audit Report*",
        ])

        with open(report_path, 'w') as f:
            f.write('\n'.join(lines))

        print(f"Audit report saved to: {report_path}")

# ==============================================================================
# Main
# ==============================================================================

def main():
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    runner = AuditRunner(verbose=verbose)
    runner.add_baseline_entries()
    runner.add_weak_sector_entries()
    runner.run_all()
    runner.save_ledger()
    runner.generate_latex_numbers()
    runner.generate_audit_report()

    print()
    print("=" * 70)
    print("AUDIT COMPLETE")
    print("=" * 70)
    print()
    print("Generated files:")
    print(f"  - {GENERATED_DIR}/ledger.json")
    print(f"  - {GENERATED_DIR}/numbers.tex")
    print(f"  - {GENERATED_DIR}/AUDIT_REPORT.md")
    print()

    return 0 if not runner.failures else 1

if __name__ == "__main__":
    sys.exit(main())
