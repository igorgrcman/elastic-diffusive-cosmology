#!/usr/bin/env python3
"""
no_smuggling_scan.py — Red Team Forensic Tool
Scans for potential SM/PDG value smuggling.
Reports instances where baseline values are used without [BL] tag.

ADVERSARIAL PREMISE: Any untagged SM value is potential smuggling.
"""

import subprocess
import re
import os
from pathlib import Path
from collections import defaultdict

# Risky tokens - SM/PDG values that MUST be tagged
RISKY_TOKENS = {
    # Masses (MeV)
    r"0\.511": "electron mass",
    r"105\.7": "muon mass",
    r"1776|1777": "tau mass",
    r"938\.3|938\.27": "proton mass",
    r"939\.6|939\.57": "neutron mass",
    r"91\.2|91\.19": "Z boson mass",
    r"80\.4|80\.38": "W boson mass",
    r"125\.": "Higgs mass",
    # Coupling constants
    r"137\.03|137\.036": "fine structure constant",
    r"0\.231|0\.2312": "sin^2(theta_W) at M_Z",
    r"1\.166|1\.1664": "Fermi constant",
    # Other
    r"246|v\s*=\s*246": "Higgs vev",
    r"0\.782|0\.78": "neutron-proton mass diff (MeV)",
    r"1836|1837": "proton/electron mass ratio",
    # Explicit references
    r"PDG": "PDG reference",
    r"CODATA": "CODATA reference",
}

# Tag patterns to check for
TAG_PATTERNS = [
    r"\\tagBL",
    r"\[BL\]",
    r"\\textbf\{BL\}",
    r"baseline",
    r"\\BL\{",
]

def check_line_for_tags(line):
    """Check if a line contains baseline tags."""
    for pattern in TAG_PATTERNS:
        if re.search(pattern, line, re.IGNORECASE):
            return True
    return False

def scan_file(filepath):
    """Scan a file for risky tokens and check tagging."""
    issues = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except Exception as e:
        return [{"error": str(e)}]

    for i, line in enumerate(lines, 1):
        for pattern, description in RISKY_TOKENS.items():
            if re.search(pattern, line, re.IGNORECASE):
                # Check this line and nearby lines for tags
                context_start = max(0, i - 3)
                context_end = min(len(lines), i + 2)
                context_lines = lines[context_start:context_end]

                has_tag = any(check_line_for_tags(l) for l in context_lines)

                issues.append({
                    'file': str(filepath),
                    'line': i,
                    'pattern': pattern,
                    'description': description,
                    'has_tag': has_tag,
                    'status': 'OK' if has_tag else 'SUSPICIOUS',
                    'context': line.strip()[:100]
                })

    return issues

def main():
    src_dir = Path(__file__).parent.parent.parent
    output_dir = Path(__file__).parent.parent

    print("=" * 70)
    print("RED TEAM NO-SMUGGLING SCAN")
    print("=" * 70)
    print("\nADVERSARIAL PREMISE: Any untagged SM value is potential smuggling.\n")

    all_issues = []
    files_scanned = 0

    # Scan all .tex files
    for tex_file in src_dir.rglob("*.tex"):
        # Skip aside_redteam folder
        if "aside_redteam" in str(tex_file):
            continue
        files_scanned += 1
        issues = scan_file(tex_file)
        all_issues.extend(issues)

    # Separate by status
    suspicious = [i for i in all_issues if i.get('status') == 'SUSPICIOUS']
    tagged = [i for i in all_issues if i.get('status') == 'OK']

    print(f"Files scanned: {files_scanned}")
    print(f"Total risky tokens found: {len(all_issues)}")
    print(f"  - Properly tagged [BL]: {len(tagged)}")
    print(f"  - SUSPICIOUS (untagged): {len(suspicious)}")

    # Write report
    report_path = output_dir / "no_smuggling_report.md"
    with open(report_path, 'w') as f:
        f.write("# No-Smuggling Scan Report\n\n")
        f.write("**Adversarial Premise:** Any untagged SM/PDG value is potential smuggling.\n\n")
        f.write(f"- Files scanned: {files_scanned}\n")
        f.write(f"- Total risky tokens: {len(all_issues)}\n")
        f.write(f"- Properly tagged: {len(tagged)}\n")
        f.write(f"- **SUSPICIOUS (untagged): {len(suspicious)}**\n\n")

        f.write("## SUSPICIOUS INSTANCES\n\n")
        f.write("These require immediate review:\n\n")

        # Group by file
        by_file = defaultdict(list)
        for issue in suspicious:
            by_file[issue['file']].append(issue)

        for filepath, issues in sorted(by_file.items()):
            rel_path = Path(filepath).relative_to(src_dir)
            f.write(f"### {rel_path}\n\n")
            for issue in issues:
                f.write(f"- **Line {issue['line']}**: `{issue['description']}`\n")
                f.write(f"  - Pattern: `{issue['pattern']}`\n")
                f.write(f"  - Context: `{issue['context'][:80]}...`\n\n")

        f.write("\n## PROPERLY TAGGED INSTANCES\n\n")
        f.write("These have [BL] tags nearby (sample):\n\n")
        for issue in tagged[:20]:
            rel_path = Path(issue['file']).relative_to(src_dir)
            f.write(f"- {rel_path}:{issue['line']} - {issue['description']}\n")

    print(f"\n[DONE] Report: {report_path}")

    if suspicious:
        print("\n" + "=" * 70)
        print("WARNING: SUSPICIOUS INSTANCES FOUND")
        print("=" * 70)
        for issue in suspicious[:10]:
            print(f"  {Path(issue['file']).name}:{issue['line']} - {issue['description']}")
        if len(suspicious) > 10:
            print(f"  ... and {len(suspicious) - 10} more")

if __name__ == "__main__":
    main()
