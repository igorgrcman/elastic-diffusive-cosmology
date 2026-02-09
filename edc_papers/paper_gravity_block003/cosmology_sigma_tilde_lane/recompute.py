#!/usr/bin/env python3
"""
recompute.py - Verification checks for cosmology σ̃ export lane

Runs >= 48 checks and exits nonzero on failure.
No external packages required.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

# Configuration
LANE_DIR = Path(__file__).parent
ALLOWED_PATHS = [
    "edc_papers/paper_gravity_block003/cosmology_sigma_tilde_lane/",
    "edc_papers/PAPERS_INDEX.md"
]

FORBIDDEN_PATTERNS = [
    "PDG", "Super-K", "SuperK", "Kamiokande", "SK",
    "experimental", "lattice", "bound", "limit"
]

REQUIRED_FILES = [
    "README.md",
    "sigma_tilde_schema.json",
    "SIGMA_TILDE_EXPORT_CONTRACT.md",
    "build_sigma_tilde_stub.py",
    "recompute.py",
    "TSTAR_DEFINITION.md",
    "TSTAR_DERIVATION_5D.md",
    "REPORT.md"
]

# Additional forbidden patterns for no-backflow guard
NOBACKFLOW_FORBIDDEN = [
    "PDG", "Super-K", "SuperK", "Kamiokande", "SK",
    "experimental", "lattice", "bound", "limit",
    "fit", "optimiz"
]

# Required headings in TSTAR_DERIVATION_5D.md
DERIVATION_REQUIRED_HEADINGS = [
    "Conventions",
    "5D Action",
    "Israel Junction",
    "Route A",
    "Route B",
    "Dimensional Checks"
]


def check(name, condition):
    """Print check result and return 1 if passed, 0 if failed."""
    status = "PASS" if condition else "FAIL"
    print(f"  [{status}] {name}")
    return 1 if condition else 0


def load_json(path):
    """Load JSON file, return None on error."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError, IOError):
        return None


def validate_schema_structure(schema):
    """Basic structural validation of the schema file."""
    if not isinstance(schema, dict):
        return False
    required_keys = ["$schema", "type", "required", "properties"]
    return all(k in schema for k in required_keys)


def validate_stub_structure(stub, schema):
    """Validate stub against schema (structural, no jsonschema pkg)."""
    if not isinstance(stub, dict):
        return False

    # Check required fields from schema
    required = schema.get("required", [])
    if not all(k in stub for k in required):
        return False

    # Check no additional properties
    allowed_keys = set(schema.get("properties", {}).keys())
    if set(stub.keys()) - allowed_keys:
        return False

    return True


def check_forbidden_in_file(filepath, patterns):
    """Check if file contains any forbidden patterns."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        for pattern in patterns:
            if pattern in content:
                return False, pattern
        return True, None
    except (FileNotFoundError, IOError):
        return False, "FILE_ERROR"


def get_repo_root():
    """Get the git repository root directory."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def get_git_diff_files():
    """Get list of modified files from git (relative to repo root)."""
    repo_root = get_repo_root()
    if not repo_root:
        return []

    try:
        result = subprocess.run(
            ["git", "diff", "--name-only"],
            capture_output=True, text=True, check=True, cwd=repo_root
        )
        staged = subprocess.run(
            ["git", "diff", "--name-only", "--cached"],
            capture_output=True, text=True, check=True, cwd=repo_root
        )
        untracked = subprocess.run(
            ["git", "ls-files", "--others", "--exclude-standard"],
            capture_output=True, text=True, check=True, cwd=repo_root
        )
        all_files = (
            result.stdout.strip().split("\n") +
            staged.stdout.strip().split("\n") +
            untracked.stdout.strip().split("\n")
        )
        return [f for f in all_files if f]
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []


def files_in_allowed_paths(files, allowed):
    """Check all files are within allowed paths."""
    for f in files:
        if not any(f.startswith(p) or f == p.rstrip("/") for p in allowed):
            return False, f
    return True, None


def main():
    print("=" * 60)
    print("Cosmology σ̃ Export Lane - Verification Checks")
    print("=" * 60)
    print()

    passed = 0
    total = 0

    # ============================================================
    # Section 1: File Existence (5 checks)
    # ============================================================
    print("Section 1: File Existence")
    print("-" * 40)

    for filename in REQUIRED_FILES:
        total += 1
        filepath = LANE_DIR / filename
        passed += check(f"FE-{total:03d}: {filename} exists", filepath.exists())

    print()

    # ============================================================
    # Section 2: Schema Validation (5 checks)
    # ============================================================
    print("Section 2: Schema Validation")
    print("-" * 40)

    schema_path = LANE_DIR / "sigma_tilde_schema.json"
    schema = load_json(schema_path)

    total += 1
    passed += check("SV-001: Schema file parses as JSON", schema is not None)

    total += 1
    passed += check("SV-002: Schema has $schema field",
                    schema and "$schema" in schema)

    total += 1
    passed += check("SV-003: Schema has type=object",
                    schema and schema.get("type") == "object")

    total += 1
    passed += check("SV-004: Schema has required array",
                    schema and isinstance(schema.get("required"), list))

    total += 1
    passed += check("SV-005: Schema disallows additionalProperties",
                    schema and schema.get("additionalProperties") is False)

    print()

    # ============================================================
    # Section 3: Stub Generation (5 checks)
    # ============================================================
    print("Section 3: Stub Generation")
    print("-" * 40)

    # Run build_sigma_tilde_stub.py
    stub_script = LANE_DIR / "build_sigma_tilde_stub.py"
    stub_output = LANE_DIR / "sigma_tilde_value.json"

    try:
        result = subprocess.run(
            [sys.executable, str(stub_script)],
            capture_output=True, text=True, cwd=str(LANE_DIR)
        )
        stub_ran = result.returncode == 0
    except Exception:
        stub_ran = False

    total += 1
    passed += check("SG-001: Stub script runs without error", stub_ran)

    total += 1
    passed += check("SG-002: sigma_tilde_value.json created", stub_output.exists())

    stub = load_json(stub_output) if stub_output.exists() else None

    total += 1
    passed += check("SG-003: Stub file parses as JSON", stub is not None)

    total += 1
    passed += check("SG-004: Stub has schema_version field",
                    stub and "schema_version" in stub)

    total += 1
    passed += check("SG-005: Stub has created_utc field",
                    stub and "created_utc" in stub)

    print()

    # ============================================================
    # Section 4: Stub Content Validation (5 checks)
    # ============================================================
    print("Section 4: Stub Content Validation")
    print("-" * 40)

    total += 1
    passed += check("SC-001: sigma_tilde.status == TBD",
                    stub and stub.get("sigma_tilde", {}).get("status") == "TBD")

    total += 1
    passed += check("SC-002: sigma_tilde.value is null",
                    stub and stub.get("sigma_tilde", {}).get("value") is None)

    total += 1
    passed += check("SC-003: t_star.status == TBD",
                    stub and stub.get("t_star", {}).get("status") == "TBD")

    total += 1
    passed += check("SC-004: firewall.layer == A",
                    stub and stub.get("firewall", {}).get("layer") == "A")

    total += 1
    passed += check("SC-005: firewall.forbidden_gate_pass == false",
                    stub and stub.get("firewall", {}).get("forbidden_gate_pass") is False)

    print()

    # ============================================================
    # Section 5: Schema Compliance (3 checks)
    # ============================================================
    print("Section 5: Schema Compliance")
    print("-" * 40)

    total += 1
    passed += check("SCO-001: Stub validates against schema structure",
                    schema and stub and validate_stub_structure(stub, schema))

    total += 1
    required_fields = schema.get("required", []) if schema else []
    passed += check("SCO-002: All required fields present in stub",
                    stub and all(k in stub for k in required_fields))

    total += 1
    stub_keys = set(stub.keys()) if stub else set()
    schema_props = set(schema.get("properties", {}).keys()) if schema else set()
    passed += check("SCO-003: No extra fields in stub",
                    stub_keys <= schema_props)

    print()

    # ============================================================
    # Section 6: Forbidden Patterns (4 checks)
    # ============================================================
    print("Section 6: Forbidden Patterns")
    print("-" * 40)

    # Check stub JSON
    total += 1
    if stub_output.exists():
        ok, pattern = check_forbidden_in_file(stub_output, FORBIDDEN_PATTERNS)
        passed += check(f"FP-001: sigma_tilde_value.json clean (no forbidden)",
                        ok)
        if not ok and pattern != "FILE_ERROR":
            print(f"         Found: '{pattern}'")
    else:
        passed += check("FP-001: sigma_tilde_value.json clean", False)

    # Check README
    total += 1
    readme_path = LANE_DIR / "README.md"
    ok, pattern = check_forbidden_in_file(readme_path, FORBIDDEN_PATTERNS)
    passed += check("FP-002: README.md clean (no forbidden)", ok)
    if not ok and pattern != "FILE_ERROR":
        print(f"         Found: '{pattern}'")

    # Check contract
    total += 1
    contract_path = LANE_DIR / "SIGMA_TILDE_EXPORT_CONTRACT.md"
    ok, pattern = check_forbidden_in_file(contract_path, FORBIDDEN_PATTERNS)
    passed += check("FP-003: Contract clean (no forbidden)", ok)
    if not ok and pattern != "FILE_ERROR":
        print(f"         Found: '{pattern}'")

    # Check schema
    total += 1
    ok, pattern = check_forbidden_in_file(schema_path, FORBIDDEN_PATTERNS)
    passed += check("FP-004: Schema clean (no forbidden)", ok)
    if not ok and pattern != "FILE_ERROR":
        print(f"         Found: '{pattern}'")

    # Check TSTAR_DEFINITION.md
    total += 1
    tstar_path = LANE_DIR / "TSTAR_DEFINITION.md"
    ok, pattern = check_forbidden_in_file(tstar_path, FORBIDDEN_PATTERNS)
    passed += check("FP-005: TSTAR_DEFINITION.md clean (no forbidden)", ok)
    if not ok and pattern != "FILE_ERROR":
        print(f"         Found: '{pattern}'")

    print()

    # ============================================================
    # Section 7: T_* Definition Content (5 checks)
    # ============================================================
    print("Section 7: T_* Definition Content")
    print("-" * 40)

    # Read TSTAR_DEFINITION.md content
    tstar_content = ""
    if tstar_path.exists():
        try:
            with open(tstar_path, "r", encoding="utf-8") as f:
                tstar_content = f.read()
        except IOError:
            pass

    # Check for σ̃ = σ / T_* formula (various forms)
    total += 1
    formula_variants = [
        "σ̃ = σ / T_*",
        "σ̃ = σ/T_*",
        "sigma_tilde = sigma / T_*",
        "σ/T_*"
    ]
    has_formula = any(v in tstar_content for v in formula_variants)
    passed += check("TD-001: Contains σ̃ = σ / T_* formula", has_formula)

    # Check for [P] epistemic tag
    total += 1
    has_pending_tag = "[P]" in tstar_content
    passed += check("TD-002: Contains [P] epistemic tag", has_pending_tag)

    # Check for [Dc] epistemic tag
    total += 1
    has_contract_tag = "[Dc]" in tstar_content
    passed += check("TD-003: Contains [Dc] epistemic tag", has_contract_tag)

    # Check for [I] invariant tag
    total += 1
    has_invariant_tag = "[I]" in tstar_content
    passed += check("TD-004: Contains [I] epistemic tag", has_invariant_tag)

    # Check for No-Backflow statement
    total += 1
    has_backflow = "No-Backflow" in tstar_content or "no-backflow" in tstar_content.lower()
    passed += check("TD-005: Contains No-Backflow statement", has_backflow)

    print()

    # ============================================================
    # Section 8: 5D Derivation Content (6 checks)
    # ============================================================
    print("Section 8: 5D Derivation Content")
    print("-" * 40)

    # Read TSTAR_DERIVATION_5D.md content
    deriv_path = LANE_DIR / "TSTAR_DERIVATION_5D.md"
    deriv_content = ""
    if deriv_path.exists():
        try:
            with open(deriv_path, "r", encoding="utf-8") as f:
                deriv_content = f.read()
        except IOError:
            pass

    # Check for required headings
    for heading in DERIVATION_REQUIRED_HEADINGS:
        total += 1
        has_heading = heading in deriv_content
        passed += check(f"D5-{DERIVATION_REQUIRED_HEADINGS.index(heading)+1:03d}: Contains '{heading}' section", has_heading)

    print()

    # ============================================================
    # Section 9: 5D Derivation Equations (3 checks)
    # ============================================================
    print("Section 9: 5D Derivation Equations")
    print("-" * 40)

    # Check for T_* = pattern
    total += 1
    import re
    has_tstar_eq = bool(re.search(r"T_\*\s*=", deriv_content) or "T_*^{(A)}" in deriv_content or "T_*^{(B)}" in deriv_content)
    passed += check("DE-001: Contains T_* = equation", has_tstar_eq)

    # Check for Israel/K_{μν} junction equation
    total += 1
    has_israel = "K_μν" in deriv_content or "K_{μν}" in deriv_content or "[K_" in deriv_content or "Israel" in deriv_content
    passed += check("DE-002: Contains Israel junction / K_μν", has_israel)

    # Check for σ̃ = σ / T_* in derivation
    total += 1
    has_sigma_ratio = "σ̃ = σ / T_*" in deriv_content or "σ/T_*" in deriv_content or "σ̃ = σ/T_*" in deriv_content
    passed += check("DE-003: Contains σ̃ = σ / T_* formula", has_sigma_ratio)

    print()

    # ============================================================
    # Section 10: No-Backflow Guard (NB-001)
    # ============================================================
    print("Section 10: No-Backflow Guard")
    print("-" * 40)

    # Scan all lane documents for forbidden patterns
    nb_files = [
        "TSTAR_DERIVATION_5D.md",
        "TSTAR_DEFINITION.md",
        "SIGMA_TILDE_EXPORT_CONTRACT.md",
        "README.md"
    ]

    total += 1
    nb_pass = True
    nb_violations = []
    for fname in nb_files:
        fpath = LANE_DIR / fname
        if fpath.exists():
            ok, pattern = check_forbidden_in_file(fpath, NOBACKFLOW_FORBIDDEN)
            if not ok:
                nb_pass = False
                nb_violations.append(f"{fname}: '{pattern}'")

    passed += check("NB-001: No-backflow guard (all docs)", nb_pass)
    if not nb_pass:
        for v in nb_violations:
            print(f"         Violation: {v}")

    # Also check TSTAR_DERIVATION_5D.md in firewall
    total += 1
    ok, pattern = check_forbidden_in_file(deriv_path, FORBIDDEN_PATTERNS)
    passed += check("FP-006: TSTAR_DERIVATION_5D.md clean (firewall)", ok)
    if not ok and pattern != "FILE_ERROR":
        print(f"         Found: '{pattern}'")

    print()

    # ============================================================
    # Section 11: Path/Scope Verification (3 checks)
    # ============================================================
    print("Section 11: Path/Scope Verification")
    print("-" * 40)

    total += 1
    passed += check("PS-001: Lane directory name correct",
                    LANE_DIR.name == "cosmology_sigma_tilde_lane")

    total += 1
    parent_ok = LANE_DIR.parent.name == "paper_gravity_block003"
    passed += check("PS-002: Parent directory is paper_gravity_block003", parent_ok)

    # Check git modifications are in allowed paths
    total += 1
    changed_files = get_git_diff_files()
    ok, bad_file = files_in_allowed_paths(changed_files, ALLOWED_PATHS)
    passed += check("PS-003: All changes in allowed paths", ok)
    if not ok:
        print(f"         Violation: {bad_file}")

    print()

    # ============================================================
    # Summary
    # ============================================================
    print("=" * 60)
    print(f"SUMMARY: {passed}/{total} checks passed")
    print("=" * 60)

    if passed == total:
        print("\nALL CHECKS PASSED")
        # Clean up generated stub if all passed
        if stub_output.exists():
            stub_output.unlink()
            print("(Cleaned up generated sigma_tilde_value.json)")
        return 0
    else:
        print(f"\nFAILED: {total - passed} check(s)")
        return 1


if __name__ == "__main__":
    sys.exit(main())
