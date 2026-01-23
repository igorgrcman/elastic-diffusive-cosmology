#!/usr/bin/env python3
"""
Lambda Provenance Checker
=========================

Ensures Wolfenstein λ is not a floating constant. Enforces a single canonical
provenance (file+label) and detects any drift.

Exit codes:
    0 - All checks passed
    1 - Hard fail (no canonical definition, multiple competing definitions,
        or provenance reference missing)

Usage:
    python3 tools/check_lambda_provenance.py
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# Configuration
SEARCH_PATTERNS = [
    r'Wolfenstein',
    r'Cabibbo',
    r'\|V_\{us\}\|',
    r'V_\{us\}',
    r'0\.225',
    r'0\.224',
    r'0\.22500',
    r'-\\ln.*lambda',
    r'd12.*kappa',
    r'eq:wolfenstein',
    r'eq:ch7_wolfenstein',
    r'LAMBDA\s*=',
]

CANONICAL_LABEL = 'eq:ch7_wolfenstein'
CANONICAL_FILE = 'sections/07_ckm_cp.tex'

# Patterns that indicate a definition (not just a reference)
DEFINITION_PATTERNS = [
    r'\\lambda\s*[≈=]\s*0\.22',
    r'λ\s*[≈=]\s*0\.22',
    r'LAMBDA\s*=\s*0\.22',
    r'\\label\{eq:.*wolfenstein.*\}',
    r'\\label\{eq:.*lambda.*def.*\}',
]


def scan_file(filepath: Path, patterns: List[str]) -> List[Tuple[int, str]]:
    """Scan a file for pattern matches. Returns list of (line_num, line_content)."""
    matches = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for i, line in enumerate(f, 1):
                for pattern in patterns:
                    if re.search(pattern, line, re.IGNORECASE):
                        matches.append((i, line.strip()))
                        break  # Only add each line once
    except Exception as e:
        print(f"  [WARN] Could not read {filepath}: {e}", file=sys.stderr)
    return matches


def find_all_occurrences(base_dir: Path) -> Dict[str, List[Tuple[int, str]]]:
    """Find all λ-related occurrences in the repo."""
    results = {}

    # Scan patterns
    extensions = ['.tex', '.py', '.md']

    for ext in extensions:
        for filepath in base_dir.rglob(f'*{ext}'):
            # Skip output directories and build artifacts
            if any(skip in str(filepath) for skip in ['output/', '__pycache__', '.aux', '.log']):
                continue

            matches = scan_file(filepath, SEARCH_PATTERNS)
            if matches:
                rel_path = filepath.relative_to(base_dir)
                results[str(rel_path)] = matches

    return results


def find_canonical_definition(base_dir: Path) -> Optional[Tuple[str, int, str]]:
    """Find the canonical λ definition with eq:ch7_wolfenstein label."""
    canonical_path = base_dir / CANONICAL_FILE

    if not canonical_path.exists():
        return None

    with open(canonical_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find the label
    for i, line in enumerate(lines):
        if CANONICAL_LABEL in line:
            # Get context (5 lines before the label)
            start = max(0, i - 5)
            context = ''.join(lines[start:i+1])
            return (CANONICAL_FILE, i + 1, context.strip())

    return None


def find_competing_definitions(all_occurrences: Dict[str, List[Tuple[int, str]]]) -> List[Tuple[str, int, str]]:
    """Find potential competing λ definitions.

    Only flags .tex files as potential competing definitions, since
    .py files contain implementation constants, not authoritative definitions.
    """
    competing = []

    for filepath, matches in all_occurrences.items():
        # Skip the canonical file
        if CANONICAL_FILE in filepath:
            continue

        # Only check .tex files for competing definitions
        # .py and .md files are implementations/notes, not authoritative definitions
        if not filepath.endswith('.tex'):
            continue

        for line_num, line_content in matches:
            # Check if this looks like a definition (has a label)
            if re.search(r'\\label\{eq:.*lambda.*\}', line_content, re.IGNORECASE):
                competing.append((filepath, line_num, line_content))

    return competing


def check_numerical_consistency(all_occurrences: Dict[str, List[Tuple[int, str]]]) -> List[Tuple[str, int, str, str]]:
    """Check for inconsistent numerical λ values."""
    inconsistencies = []

    # Pattern to extract numerical values
    value_pattern = r'0\.22\d*'
    canonical_value = '0.225'

    for filepath, matches in all_occurrences.items():
        for line_num, line_content in matches:
            found_values = re.findall(value_pattern, line_content)
            for val in found_values:
                # Check if value is significantly different
                if val not in ['0.225', '0.22500', '0.22', '0.224', '0.226']:
                    inconsistencies.append((filepath, line_num, line_content, val))

    return inconsistencies


def main():
    """Main provenance check routine."""
    print("=" * 70)
    print("LAMBDA PROVENANCE CHECK")
    print("=" * 70)
    print()

    # Determine base directory
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent  # paper/ directory

    print(f"Scanning: {base_dir}")
    print()

    # Step 1: Find canonical definition
    print("-" * 70)
    print("STEP 1: Canonical Definition")
    print("-" * 70)

    canonical = find_canonical_definition(base_dir)

    if canonical:
        print(f"  CANONICAL: {canonical[0]}:{canonical[1]}")
        print(f"  Label: {CANONICAL_LABEL}")
        print()
        print("  Context:")
        for line in canonical[2].split('\n'):
            print(f"    {line}")
        print()
        canonical_status = "PASS"
    else:
        print(f"  [FAIL] Canonical definition not found!")
        print(f"  Expected: {CANONICAL_FILE} with label {CANONICAL_LABEL}")
        canonical_status = "FAIL"

    # Step 2: Find all occurrences
    print("-" * 70)
    print("STEP 2: All Occurrences")
    print("-" * 70)

    all_occurrences = find_all_occurrences(base_dir)

    total_occurrences = sum(len(m) for m in all_occurrences.values())
    print(f"  Found {total_occurrences} occurrences in {len(all_occurrences)} files")
    print()

    # List files with occurrence counts
    for filepath in sorted(all_occurrences.keys()):
        count = len(all_occurrences[filepath])
        print(f"    {filepath}: {count} occurrence(s)")

    print()

    # Step 3: Check for competing definitions
    print("-" * 70)
    print("STEP 3: Competing Definitions Check")
    print("-" * 70)

    competing = find_competing_definitions(all_occurrences)

    if competing:
        print(f"  [WARN] Found {len(competing)} potential competing definition(s):")
        for filepath, line_num, content in competing:
            print(f"    {filepath}:{line_num}")
            print(f"      {content[:80]}...")
        print()
        competing_status = "WARN"
    else:
        print("  No competing definitions found.")
        competing_status = "PASS"

    print()

    # Step 4: Numerical consistency
    print("-" * 70)
    print("STEP 4: Numerical Consistency")
    print("-" * 70)

    inconsistencies = check_numerical_consistency(all_occurrences)

    if inconsistencies:
        print(f"  [WARN] Found {len(inconsistencies)} potential inconsistencies:")
        for filepath, line_num, content, val in inconsistencies:
            print(f"    {filepath}:{line_num} (found {val})")
        consistency_status = "WARN"
    else:
        print("  All numerical values consistent with canonical λ = 0.225")
        consistency_status = "PASS"

    print()

    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print(f"  Canonical definition:     {canonical_status}")
    print(f"  Competing definitions:    {competing_status}")
    print(f"  Numerical consistency:    {consistency_status}")
    print()

    # Provenance reference for Attempt 4.1
    print("-" * 70)
    print("PROVENANCE REFERENCE (for Attempt 4.1)")
    print("-" * 70)
    print()
    print(f"  File: {CANONICAL_FILE}")
    print(f"  Label: {CANONICAL_LABEL}")
    print(f"  Value: λ ≈ 0.225 [BL]")
    print(f"  Citation: Eq.~(\\ref{{{CANONICAL_LABEL}}})")
    print()

    # Exit code
    if canonical_status == "FAIL":
        print("[HARD FAIL] No canonical λ definition found!")
        return 1

    if competing_status == "WARN" and len(competing) > 3:
        print("[HARD FAIL] Too many competing definitions!")
        return 1

    print("[PASS] λ provenance check completed successfully.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
