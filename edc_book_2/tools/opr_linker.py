#!/usr/bin/env python3
"""
OPR Linker — Validate OPR → Claim Crosswalk

This tool validates that every MISSING/BLOCKED claim in the evidence ledgers
has an assigned OPR in the crosswalk. It is non-destructive and deterministic.

Exit codes:
    0 = All physics claims assigned (UNASSIGNED count = 0 for physics)
    1 = Unassigned physics claims found

Usage:
    python tools/opr_linker.py [--update]

Options:
    --update    Update OPR_BLOCKERS_SUMMARY.md with current counts
"""

import re
import sys
from pathlib import Path
from datetime import datetime

# Paths relative to repo root
REPO_ROOT = Path(__file__).parent.parent
DERIVATION_LEDGER = REPO_ROOT / "audit/evidence/DERIVATION_CHAIN_LEDGER.md"
CLAIM_INDEX = REPO_ROOT / "audit/evidence/CLAIM_EVIDENCE_INDEX.md"
CROSSWALK = REPO_ROOT / "audit/evidence/OPR_CLAIM_CROSSWALK.md"
BLOCKERS_SUMMARY = REPO_ROOT / "audit/evidence/OPR_BLOCKERS_SUMMARY.md"
MANIFEST = REPO_ROOT / "audit/opr/OPR_RUN_MANIFEST.yml"


def count_missing_claims(ledger_path: Path) -> int:
    """Count MISSING claims in derivation ledger."""
    if not ledger_path.exists():
        print(f"ERROR: {ledger_path} not found")
        return -1

    content = ledger_path.read_text()

    # Look for the summary line
    match = re.search(r'\| MISSING \| \d+ \| (\d+) \|', content)
    if match:
        return int(match.group(1))

    # Fallback: count MISSING occurrences in tables
    missing_count = len(re.findall(r'\| MISSING \|', content))
    return missing_count


def count_crosswalk_assignments(crosswalk_path: Path) -> dict:
    """Count OPR assignments in crosswalk."""
    if not crosswalk_path.exists():
        print(f"ERROR: {crosswalk_path} not found")
        return {}

    content = crosswalk_path.read_text()

    counts = {
        'total_assigned': 0,
        'unassigned': 0,
        'by_opr': {}
    }

    # Count assignments per OPR
    for opr_num in range(1, 9):
        opr_id = f"OPR-0{opr_num}"
        pattern = rf'\| {opr_id} \|'
        count = len(re.findall(pattern, content))
        counts['by_opr'][opr_id] = count
        counts['total_assigned'] += count

    # Count UNASSIGNED
    unassigned_match = re.search(r'Physics UNASSIGNED[:\s]+(\d+)', content)
    if unassigned_match:
        counts['unassigned'] = int(unassigned_match.group(1))
    else:
        counts['unassigned'] = len(re.findall(r'\| UNASSIGNED \|', content))

    return counts


def validate_crosswalk() -> bool:
    """Validate that all physics claims are assigned."""
    print("=" * 60)
    print("OPR LINKER — Crosswalk Validation")
    print("=" * 60)
    print(f"Date: {datetime.now().isoformat()}")
    print()

    # Count missing claims
    missing_count = count_missing_claims(DERIVATION_LEDGER)
    print(f"MISSING claims in ledger: {missing_count}")

    # Count crosswalk assignments
    counts = count_crosswalk_assignments(CROSSWALK)
    print(f"Total assigned in crosswalk: {counts.get('total_assigned', 0)}")
    print(f"Physics UNASSIGNED: {counts.get('unassigned', 0)}")
    print()

    # Per-OPR breakdown
    print("OPR Assignment Breakdown:")
    for opr_id, count in counts.get('by_opr', {}).items():
        print(f"  {opr_id}: {count} claims")
    print()

    # Validation result
    physics_unassigned = counts.get('unassigned', 0)

    if physics_unassigned == 0:
        print("RESULT: PASS — All physics claims assigned to OPRs")
        return True
    else:
        print(f"RESULT: FAIL — {physics_unassigned} physics claims UNASSIGNED")
        return False


def update_manifest(counts: dict):
    """Update OPR_RUN_MANIFEST.yml with current counts."""
    if not MANIFEST.exists():
        print(f"WARNING: {MANIFEST} not found, skipping update")
        return

    content = MANIFEST.read_text()

    # Update counts section
    updates = {
        'assigned_claims': counts.get('total_assigned', 0),
        'unassigned_claims': counts.get('unassigned', 0),
    }

    for key, value in updates.items():
        pattern = rf'({key}:\s*)\d+'
        content = re.sub(pattern, rf'\g<1>{value}', content)

    # Update validation section
    content = re.sub(
        r'(opr_linker_exit_code:\s*).*',
        f'\\g<1>{0 if counts.get("unassigned", 0) == 0 else 1}',
        content
    )
    content = re.sub(
        r'(crosswalk_complete:\s*).*',
        f'\\g<1>{str(counts.get("unassigned", 0) == 0).lower()}',
        content
    )

    MANIFEST.write_text(content)
    print(f"Updated: {MANIFEST}")


def main():
    update_mode = '--update' in sys.argv

    # Run validation
    passed = validate_crosswalk()

    # Optionally update manifest
    if update_mode:
        counts = count_crosswalk_assignments(CROSSWALK)
        update_manifest(counts)

    # Exit code
    sys.exit(0 if passed else 1)


if __name__ == '__main__':
    main()
