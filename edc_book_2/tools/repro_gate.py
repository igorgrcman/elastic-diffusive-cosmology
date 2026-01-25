#!/usr/bin/env python3
"""
================================================================================
GATE: REPRO Pack Verification
================================================================================

Verifies that:
1. All expected REPRO outputs exist
2. Outputs contain required fields
3. All scripts report PASS status
4. Manifest is complete and consistent

Usage:
    python tools/repro_gate.py

Exit codes:
    0 — All verifications pass
    1 — One or more verifications fail
================================================================================
"""

import json
import sys
from pathlib import Path

# Configuration
BOOK2_DIR = Path(__file__).parent.parent
REPRO_DIR = BOOK2_DIR / "repro"
OUTPUT_DIR = REPRO_DIR / "output"
MANIFEST_FILE = REPRO_DIR / "REPRO_MANIFEST.yml"

# Expected outputs
EXPECTED_OUTPUTS = [
    "sin2_z6_verify.json",
    "sin2_rg_running.json",
]

# Required fields in each output
REQUIRED_FIELDS = [
    "script",
    "classification",
    "supports_claims",
    "overall_verification",
]


def check_outputs_exist():
    """Check that all expected output files exist."""
    print("Checking output files...")
    missing = []
    for filename in EXPECTED_OUTPUTS:
        filepath = OUTPUT_DIR / filename
        if not filepath.exists():
            missing.append(filename)
            print(f"  ✗ MISSING: {filename}")
        else:
            print(f"  ✓ Found: {filename}")

    return len(missing) == 0, missing


def check_output_fields():
    """Check that outputs contain required fields."""
    print("\nChecking output structure...")
    issues = []

    for filename in EXPECTED_OUTPUTS:
        filepath = OUTPUT_DIR / filename
        if not filepath.exists():
            continue

        try:
            with open(filepath) as f:
                data = json.load(f)

            for field in REQUIRED_FIELDS:
                if field not in data:
                    issues.append(f"{filename}: missing field '{field}'")
                    print(f"  ✗ {filename}: missing '{field}'")

            if "overall_verification" in data:
                status = data["overall_verification"]
                if status == "PASS":
                    print(f"  ✓ {filename}: verification PASS")
                else:
                    print(f"  ✗ {filename}: verification {status}")
                    issues.append(f"{filename}: verification {status}")

        except json.JSONDecodeError as e:
            issues.append(f"{filename}: invalid JSON ({e})")
            print(f"  ✗ {filename}: invalid JSON")

    return len(issues) == 0, issues


def check_manifest():
    """Check that manifest file exists and is valid."""
    print("\nChecking manifest...")

    if not MANIFEST_FILE.exists():
        print(f"  ✗ MISSING: {MANIFEST_FILE.name}")
        return False, ["Manifest file missing"]

    print(f"  ✓ Found: {MANIFEST_FILE.name}")

    # Basic YAML validation (without pyyaml dependency)
    content = MANIFEST_FILE.read_text()

    required_sections = ["metadata:", "scripts:", "validation:"]
    missing_sections = []

    for section in required_sections:
        if section not in content:
            missing_sections.append(section)
            print(f"  ✗ Missing section: {section}")
        else:
            print(f"  ✓ Has section: {section}")

    return len(missing_sections) == 0, missing_sections


def check_checksums():
    """Check that checksum file exists."""
    print("\nChecking checksums...")

    checksum_file = OUTPUT_DIR / "checksums.sha256"
    if not checksum_file.exists():
        print(f"  ✗ MISSING: checksums.sha256")
        return False, ["Checksum file missing"]

    print(f"  ✓ Found: checksums.sha256")

    # Verify at least one checksum entry
    content = checksum_file.read_text()
    checksum_lines = [l for l in content.split('\n')
                      if l and not l.startswith('#')]

    if len(checksum_lines) < len(EXPECTED_OUTPUTS):
        print(f"  ✗ Expected {len(EXPECTED_OUTPUTS)} checksums, found {len(checksum_lines)}")
        return False, ["Incomplete checksum file"]

    print(f"  ✓ Contains {len(checksum_lines)} checksums")
    return True, []


def main():
    """Run all gate checks."""
    print("=" * 60)
    print("GATE: REPRO Pack Verification")
    print("=" * 60)
    print(f"REPRO directory: {REPRO_DIR}")
    print("")

    all_pass = True
    all_issues = []

    # Check 1: Outputs exist
    ok, issues = check_outputs_exist()
    if not ok:
        all_pass = False
        all_issues.extend(issues)

    # Check 2: Output structure
    ok, issues = check_output_fields()
    if not ok:
        all_pass = False
        all_issues.extend(issues)

    # Check 3: Manifest
    ok, issues = check_manifest()
    if not ok:
        all_pass = False
        all_issues.extend(issues)

    # Check 4: Checksums
    ok, issues = check_checksums()
    if not ok:
        all_pass = False
        all_issues.extend(issues)

    # Summary
    print("")
    print("=" * 60)
    if all_pass:
        print("GATE RESULT: PASS")
        print("=" * 60)
        return 0
    else:
        print("GATE RESULT: FAIL")
        print("=" * 60)
        print("\nIssues found:")
        for issue in all_issues:
            print(f"  - {issue}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
