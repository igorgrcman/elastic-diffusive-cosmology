#!/usr/bin/env python3
"""
collect_labels_and_cites.py - LaTeX Label/Citation Inventory and Validation Tool

This script collects all \label{} definitions and \ref{}/\cite{} usages from
LaTeX files, then checks for:
  1. Undefined references (refs used but not defined)
  2. Undefined citations (cites used but not in bib)
  3. Orphan labels (labels defined but never referenced)

Usage:
    python tools/collect_labels_and_cites.py [--ci]

Options:
    --ci    Exit with non-zero code if undefined refs/cites found (for CI)

Output:
    - Prints summary to stdout
    - Creates bvp_reports/label_cite_inventory.md with full inventory
"""

import re
import sys
import glob
from pathlib import Path
from collections import defaultdict
from datetime import datetime

def extract_labels(tex_content: str, filename: str) -> dict:
    """Extract all \label{key} definitions from tex content."""
    labels = {}
    pattern = r'\\label\{([^}]+)\}'
    for match in re.finditer(pattern, tex_content):
        key = match.group(1)
        # Get line number
        line_num = tex_content[:match.start()].count('\n') + 1
        labels[key] = {'file': filename, 'line': line_num}
    return labels

def extract_refs(tex_content: str, filename: str) -> dict:
    """Extract all \ref{key}, \eqref{key}, \pageref{key} usages."""
    refs = defaultdict(list)
    pattern = r'\\(?:eq)?ref\{([^}]+)\}|\\pageref\{([^}]+)\}'
    for match in re.finditer(pattern, tex_content):
        key = match.group(1) or match.group(2)
        line_num = tex_content[:match.start()].count('\n') + 1
        refs[key].append({'file': filename, 'line': line_num})
    return refs

def extract_cites(tex_content: str, filename: str) -> dict:
    """Extract all \cite{key1,key2,...} usages."""
    cites = defaultdict(list)
    pattern = r'\\cite[tp]?\*?\{([^}]+)\}'
    for match in re.finditer(pattern, tex_content):
        keys = match.group(1).split(',')
        line_num = tex_content[:match.start()].count('\n') + 1
        for key in keys:
            key = key.strip()
            if key:
                cites[key].append({'file': filename, 'line': line_num})
    return cites

def extract_bib_keys(bib_content: str) -> set:
    """Extract all entry keys from a .bib file."""
    keys = set()
    pattern = r'@\w+\{([^,]+),'
    for match in re.finditer(pattern, bib_content):
        keys.add(match.group(1).strip())
    return keys

def main():
    ci_mode = '--ci' in sys.argv

    # Find all tex files
    base_dir = Path(__file__).parent.parent
    tex_files = list(base_dir.glob('**/*.tex'))
    # Exclude backup/rebuild directories
    tex_files = [f for f in tex_files if 'rebuild_part2_snapshot' not in str(f)]
    tex_files = [f for f in tex_files if '_backup' not in str(f)]

    # Find bib files
    bib_files = list(base_dir.glob('**/*.bib'))
    bib_files = [f for f in bib_files if 'rebuild_part2_snapshot' not in str(f)]

    # Collect all labels, refs, and cites
    all_labels = {}
    all_refs = defaultdict(list)
    all_cites = defaultdict(list)
    bib_keys = set()

    for tex_file in tex_files:
        try:
            content = tex_file.read_text(encoding='utf-8', errors='ignore')
            rel_path = str(tex_file.relative_to(base_dir))

            labels = extract_labels(content, rel_path)
            all_labels.update(labels)

            refs = extract_refs(content, rel_path)
            for key, locs in refs.items():
                all_refs[key].extend(locs)

            cites = extract_cites(content, rel_path)
            for key, locs in cites.items():
                all_cites[key].extend(locs)
        except Exception as e:
            print(f"Warning: Could not process {tex_file}: {e}", file=sys.stderr)

    for bib_file in bib_files:
        try:
            content = bib_file.read_text(encoding='utf-8', errors='ignore')
            bib_keys.update(extract_bib_keys(content))
        except Exception as e:
            print(f"Warning: Could not process {bib_file}: {e}", file=sys.stderr)

    # Find issues
    undefined_refs = {k: v for k, v in all_refs.items() if k not in all_labels}
    undefined_cites = {k: v for k, v in all_cites.items() if k not in bib_keys}
    orphan_labels = {k: v for k, v in all_labels.items() if k not in all_refs}

    # Generate report
    report_lines = [
        f"# LaTeX Label/Citation Inventory Report",
        f"",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"",
        f"## Summary",
        f"",
        f"| Metric | Count |",
        f"|--------|-------|",
        f"| Labels defined | {len(all_labels)} |",
        f"| References used | {len(all_refs)} |",
        f"| Citations used | {len(all_cites)} |",
        f"| Bib entries | {len(bib_keys)} |",
        f"| **Undefined refs** | **{len(undefined_refs)}** |",
        f"| **Undefined cites** | **{len(undefined_cites)}** |",
        f"| Orphan labels | {len(orphan_labels)} |",
        f"",
    ]

    if undefined_refs:
        report_lines.append("## Undefined References (ERRORS)")
        report_lines.append("")
        for key, locs in sorted(undefined_refs.items()):
            report_lines.append(f"- `{key}`:")
            for loc in locs[:3]:  # Show first 3 locations
                report_lines.append(f"  - {loc['file']}:{loc['line']}")
            if len(locs) > 3:
                report_lines.append(f"  - ... and {len(locs)-3} more")
        report_lines.append("")

    if undefined_cites:
        report_lines.append("## Undefined Citations (ERRORS)")
        report_lines.append("")
        for key, locs in sorted(undefined_cites.items()):
            report_lines.append(f"- `{key}`:")
            for loc in locs[:3]:
                report_lines.append(f"  - {loc['file']}:{loc['line']}")
            if len(locs) > 3:
                report_lines.append(f"  - ... and {len(locs)-3} more")
        report_lines.append("")

    if orphan_labels:
        report_lines.append("## Orphan Labels (warnings, may be intentional)")
        report_lines.append("")
        for key, info in sorted(orphan_labels.items())[:20]:  # Limit to first 20
            report_lines.append(f"- `{key}` ({info['file']}:{info['line']})")
        if len(orphan_labels) > 20:
            report_lines.append(f"- ... and {len(orphan_labels)-20} more")
        report_lines.append("")

    # Print summary to stdout
    print("=" * 60)
    print("LaTeX Label/Citation Inventory")
    print("=" * 60)
    print(f"Labels defined:    {len(all_labels)}")
    print(f"References used:   {len(all_refs)}")
    print(f"Citations used:    {len(all_cites)}")
    print(f"Bib entries:       {len(bib_keys)}")
    print("-" * 60)
    print(f"UNDEFINED REFS:    {len(undefined_refs)}")
    print(f"UNDEFINED CITES:   {len(undefined_cites)}")
    print(f"Orphan labels:     {len(orphan_labels)}")
    print("=" * 60)

    if undefined_refs:
        print("\nUndefined references:")
        for key in sorted(undefined_refs.keys())[:10]:
            print(f"  - {key}")
        if len(undefined_refs) > 10:
            print(f"  ... and {len(undefined_refs)-10} more")

    if undefined_cites:
        print("\nUndefined citations:")
        for key in sorted(undefined_cites.keys())[:10]:
            print(f"  - {key}")
        if len(undefined_cites) > 10:
            print(f"  ... and {len(undefined_cites)-10} more")

    # Write full report
    report_dir = base_dir / 'bvp_reports'
    report_dir.mkdir(exist_ok=True)
    report_file = report_dir / 'label_cite_inventory.md'
    report_file.write_text('\n'.join(report_lines), encoding='utf-8')
    print(f"\nFull report written to: {report_file}")

    # CI mode exit code
    if ci_mode:
        if undefined_refs or undefined_cites:
            print("\n[CI] FAIL: Undefined refs/cites found")
            sys.exit(1)
        else:
            print("\n[CI] PASS: No undefined refs/cites")
            sys.exit(0)

if __name__ == '__main__':
    main()
