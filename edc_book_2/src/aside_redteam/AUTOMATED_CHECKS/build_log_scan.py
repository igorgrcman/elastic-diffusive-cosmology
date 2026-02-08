#!/usr/bin/env python3
"""
build_log_scan.py — Red Team Forensic Tool
Parses LaTeX build logs for warnings and errors.
Reports overfull hbox, undefined references, etc.

NOTE: This tool DOES NOT attempt to fix anything.
"""

import re
from pathlib import Path
from collections import Counter

def parse_build_log(log_path):
    """Parse a LaTeX build log for issues."""
    issues = {
        'overfull_hbox': [],
        'underfull_hbox': [],
        'undefined_ref': [],
        'undefined_cite': [],
        'missing_char': [],
        'errors': [],
        'warnings': [],
    }

    try:
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        return {'error': str(e)}

    # Overfull hbox
    for match in re.finditer(r'Overfull \\hbox \(([\d.]+)pt too wide\).*?lines? (\d+)(?:--(\d+))?', content):
        issues['overfull_hbox'].append({
            'magnitude': float(match.group(1)),
            'line_start': int(match.group(2)),
            'line_end': int(match.group(3)) if match.group(3) else int(match.group(2))
        })

    # Underfull hbox
    for match in re.finditer(r'Underfull \\hbox.*?lines? (\d+)', content):
        issues['underfull_hbox'].append({
            'line': int(match.group(1))
        })

    # Undefined references
    for match in re.finditer(r"Reference `([^']+)' on page (\d+) undefined", content):
        issues['undefined_ref'].append({
            'ref': match.group(1),
            'page': int(match.group(2))
        })

    # Undefined citations
    for match in re.finditer(r"Citation `([^']+)' on page (\d+) undefined", content):
        issues['undefined_cite'].append({
            'cite': match.group(1),
            'page': int(match.group(2))
        })

    # Missing characters
    for match in re.finditer(r'Missing character: There is no (.+?) in font', content):
        issues['missing_char'].append(match.group(1))

    # LaTeX errors
    for match in re.finditer(r'! (.+?)$', content, re.MULTILINE):
        issues['errors'].append(match.group(1))

    return issues

def main():
    src_dir = Path(__file__).parent.parent.parent
    output_dir = Path(__file__).parent.parent

    print("=" * 60)
    print("RED TEAM BUILD LOG SCAN")
    print("=" * 60)

    # Find log files
    log_files = list(src_dir.glob("*.log"))

    all_issues = {}

    for log_path in log_files:
        print(f"\nScanning: {log_path.name}")
        issues = parse_build_log(log_path)
        all_issues[log_path.name] = issues

        if 'error' in issues:
            print(f"  ERROR: {issues['error']}")
            continue

        print(f"  Overfull hbox: {len(issues['overfull_hbox'])}")
        print(f"  Underfull hbox: {len(issues['underfull_hbox'])}")
        print(f"  Undefined refs: {len(issues['undefined_ref'])}")
        print(f"  Undefined cites: {len(issues['undefined_cite'])}")
        print(f"  Missing chars: {len(issues['missing_char'])}")
        print(f"  Errors: {len(issues['errors'])}")

    # Write report
    report_path = output_dir / "build_log_report.md"
    with open(report_path, 'w') as f:
        f.write("# Build Log Scan Report\n\n")
        f.write("**NOTE:** This report is for forensic purposes only. No fixes attempted.\n\n")

        for log_name, issues in all_issues.items():
            f.write(f"## {log_name}\n\n")

            if 'error' in issues:
                f.write(f"ERROR: {issues['error']}\n\n")
                continue

            # Overfull hbox summary
            if issues['overfull_hbox']:
                f.write("### Overfull hbox\n\n")
                f.write(f"Total: {len(issues['overfull_hbox'])}\n\n")

                # Categorize by magnitude
                severe = [i for i in issues['overfull_hbox'] if i['magnitude'] > 10]
                moderate = [i for i in issues['overfull_hbox'] if 5 < i['magnitude'] <= 10]
                minor = [i for i in issues['overfull_hbox'] if i['magnitude'] <= 5]

                f.write(f"- Severe (>10pt): {len(severe)}\n")
                f.write(f"- Moderate (5-10pt): {len(moderate)}\n")
                f.write(f"- Minor (≤5pt): {len(minor)}\n\n")

                if severe:
                    f.write("**Severe instances:**\n")
                    for i in sorted(severe, key=lambda x: -x['magnitude'])[:10]:
                        f.write(f"- {i['magnitude']:.2f}pt at lines {i['line_start']}-{i['line_end']}\n")
                    f.write("\n")

            # Undefined refs
            if issues['undefined_ref']:
                f.write("### Undefined References\n\n")
                for ref in issues['undefined_ref'][:10]:
                    f.write(f"- `{ref['ref']}` on page {ref['page']}\n")
                if len(issues['undefined_ref']) > 10:
                    f.write(f"- ... and {len(issues['undefined_ref']) - 10} more\n")
                f.write("\n")

            # Missing chars
            if issues['missing_char']:
                f.write("### Missing Characters\n\n")
                char_counts = Counter(issues['missing_char'])
                for char, count in char_counts.most_common(10):
                    f.write(f"- `{char}`: {count} occurrences\n")
                f.write("\n")

    print(f"\n[DONE] Report: {report_path}")

if __name__ == "__main__":
    main()
