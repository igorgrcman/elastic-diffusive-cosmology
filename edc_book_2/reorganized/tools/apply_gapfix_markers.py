#!/usr/bin/env python3
"""
Apply GAPFIX markers to LaTeX sources based on prelet scan findings.
"""

import json
import os
from collections import defaultdict

def load_findings(json_path: str) -> list:
    """Load findings from JSON file."""
    with open(json_path, 'r') as f:
        return json.load(f)

def get_backfill_plan(gap_type: str) -> str:
    """Get backfill plan based on gap type."""
    if gap_type == 'A':
        return "add symbol definition in notation.tex or inline"
    elif gap_type == 'B':
        return "add 5-15 lines + 1-3 eq from long version (461pp)"
    else:  # C
        return "add dictionary box / mechanism step / scope note"

def apply_marker(filepath: str, line_num: int, finding: dict) -> bool:
    """Insert GAPFIX marker above the specified line."""
    if not os.path.exists(filepath):
        print(f"  WARNING: File not found: {filepath}")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if line_num < 1 or line_num > len(lines):
        print(f"  WARNING: Line {line_num} out of range for {filepath}")
        return False

    # Create marker comment
    gapfix_id = finding['id']
    gap_type = finding['type']
    trigger = finding['trigger']
    pdf_page = finding['pdf_page']
    backfill = get_backfill_plan(gap_type)
    notes = ', '.join(finding.get('notes', [])) or 'none'

    marker = f"% {gapfix_id} [Type {gap_type}] Trigger: \"{trigger}\" PDF p.{pdf_page}\n"
    marker += f"% TODO(backfill): {backfill}\n"
    if 'sm_risk' in finding.get('notes', []):
        marker += f"% WARNING: SM-language risk - verify dictionary boundary\n"

    # Insert marker before the specified line (0-indexed)
    insert_idx = line_num - 1

    # Check if marker already exists
    if gapfix_id in lines[insert_idx]:
        print(f"  SKIP: Marker already exists at {filepath}:{line_num}")
        return False

    lines.insert(insert_idx, marker)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    return True

def main():
    json_path = 'audit/prelet_scan_findings.json'
    findings = load_findings(json_path)

    # Group by file
    by_file = defaultdict(list)
    unresolved = []

    for f in findings:
        if f['tex_file']:
            by_file[f['tex_file']].append(f)
        else:
            unresolved.append(f)

    print(f"Total findings: {len(findings)}")
    print(f"Resolved (can patch): {len(findings) - len(unresolved)}")
    print(f"Unresolved: {len(unresolved)}")
    print()

    # Apply markers (in reverse line order to preserve line numbers)
    applied = 0
    skipped = 0

    for filepath, file_findings in sorted(by_file.items()):
        print(f"Processing {filepath}...")
        # Sort by line number descending to preserve indices
        file_findings_sorted = sorted(file_findings, key=lambda x: x['tex_line'], reverse=True)

        for finding in file_findings_sorted:
            if apply_marker(filepath, finding['tex_line'], finding):
                applied += 1
                print(f"  Applied: {finding['id']} at line {finding['tex_line']}")
            else:
                skipped += 1

    print()
    print(f"Applied: {applied} markers")
    print(f"Skipped: {skipped}")
    print(f"Unresolved (no tex mapping): {len(unresolved)}")

    # Print unresolved summary
    if unresolved:
        print()
        print("Unresolved findings (manual review needed):")
        for f in unresolved[:10]:  # First 10
            print(f"  {f['id']}: PDF p.{f['pdf_page']} - {f['trigger']}")
        if len(unresolved) > 10:
            print(f"  ... and {len(unresolved) - 10} more")

if __name__ == '__main__':
    main()
