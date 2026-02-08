#!/usr/bin/env python3
"""
Notation Refactor Script: z → ξ for EDC Part II
Converts physical 5D coordinate from z to ξ (xi) to match Paper 2 canon.

Safety features:
- Only replaces in math contexts (anchored patterns)
- Preserves labels, refs, code blocks
- Reports all changes for audit
"""

import re
import os
from pathlib import Path
from typing import List, Tuple, Dict

# Patterns to replace (z as physical 5D coordinate)
# Each tuple: (pattern, replacement, description)
REPLACEMENTS: List[Tuple[str, str, str]] = [
    # Functions with z argument
    (r'V\(z\)', r'V(\\xi)', 'Potential V(z)'),
    (r'V\(z,', r'V(\\xi,', 'Potential V(z, ...)'),
    (r'f\(z\)', r'f(\\xi)', 'Profile f(z)'),
    (r'f\(z,', r'f(\\xi,', 'Profile f(z, ...)'),
    (r'm\(z\)', r'm(\\xi)', 'Mass profile m(z)'),
    (r'm\(z,', r'm(\\xi,', 'Mass profile m(z, ...)'),
    (r'\\psi\(z\)', r'\\psi(\\xi)', 'Wavefunction psi(z)'),
    (r'\\phi\(z\)', r'\\phi(\\xi)', 'Field phi(z)'),
    (r'\\varphi\(z\)', r'\\varphi(\\xi)', 'Field varphi(z)'),

    # Derivatives
    (r'\\frac\{d\}\{dz\}', r'\\frac{d}{d\\xi}', 'First derivative d/dz'),
    (r'\\frac\{d\^2\}\{dz\^2\}', r'\\frac{d^2}{d\\xi^2}', 'Second derivative d²/dz²'),
    (r'\\frac\{d\^\{2\}\}\{dz\^\{2\}\}', r'\\frac{d^{2}}{d\\xi^{2}}', 'Second derivative d^{2}/dz^{2}'),
    (r"f'\(z\)", r"f'(\\xi)", "f'(z)"),
    (r"f''\(z\)", r"f''(\\xi)", "f''(z)"),

    # Integrals (careful with dz)
    (r'\\int_0\^\\infty([^d]*)\\s*dz', r'\\int_0^\\infty\\1 d\\xi', 'Integral dz (0 to infty)'),
    (r'\\int_0\^z([^d]*)\\s*dz', r'\\int_0^\\xi\\1 d\\xi', 'Integral dz (0 to z)'),
    (r'\\,\\s*dz', r'\\, d\\xi', 'Measure dz'),
    (r"\\s+dz'", r" d\\xi'", "Measure dz'"),
    (r"dz'", r"d\\xi'", "Measure dz' standalone"),

    # Boundaries and domains
    (r'z\s*=\s*0', r'\\xi = 0', 'Boundary z=0'),
    (r'z\s*\\to\s*0', r'\\xi \\to 0', 'Limit z→0'),
    (r'z\s*\\to\s*\\infty', r'\\xi \\to \\infty', 'Limit z→∞'),
    (r'z\s*\\ge\s*0', r'\\xi \\ge 0', 'Domain z≥0'),
    (r'z\s*\\geq\s*0', r'\\xi \\geq 0', 'Domain z≥0'),
    (r'z\s*>\s*0', r'\\xi > 0', 'Domain z>0'),
    (r'z\\s*\\in\\s*\[0', r'\\xi \\in [0', 'Domain z∈[0...'),

    # Specific constructs
    (r'\$z\$(?=\s+(?:is|denotes|represents|coordinate))', r'$\\xi$', 'Standalone $z$ before definition'),
    (r'coordinate\s+\$z\$', r'coordinate $\\xi$', 'coordinate $z$'),
    (r'coordinate\s+z\b', r'coordinate \\xi', 'coordinate z'),
    (r'\\left\[\s*0\s*,\s*\\ell\s*\\right\]', r'[0, \\ell]', 'Domain [0,ℓ] cleanup'),

    # Half-line constructs
    (r'z\s*\\in\s*\[0,\s*\\infty\)', r'\\xi \\in [0, \\infty)', 'Half-line domain'),
    (r'z\s*\\in\s*\[0,\s*\\ell\]', r'\\xi \\in [0, \\ell]', 'Compact domain'),

    # Profile arguments in narrative
    (r'profile\s+at\s+\$?z\$?', r'profile at $\\xi$', 'profile at z'),
    (r'at\s+\$z\s*=', r'at $\\xi =', 'at $z ='),
]

# Patterns to EXCLUDE (do not touch)
EXCLUSIONS = [
    r'\\label\{',      # Labels
    r'\\ref\{',        # References
    r'\\zeta',         # Zeta symbol
    r'z_\{?\\alpha',   # Z_alpha (flavor positions)
    r'z_m',            # Z_m (mass positions)
    r'Z_[236]',        # Z2, Z3, Z6 groups
    r'\\mathbb\{Z\}',  # Integer group
    r'verbatim',       # Code blocks
    r'lstlisting',     # Code listings
    r'\.py',           # Python files
    r'\.csv',          # CSV files
]

def should_skip_line(line: str) -> bool:
    """Check if line should be skipped (contains exclusion patterns)."""
    for excl in EXCLUSIONS:
        if re.search(excl, line, re.IGNORECASE):
            return True
    return False

def refactor_file(filepath: Path, dry_run: bool = False) -> Dict:
    """Refactor a single file. Returns change report."""
    report = {
        'file': str(filepath),
        'changes': [],
        'skipped': [],
        'total_replacements': 0
    }

    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        report['error'] = str(e)
        return report

    lines = content.split('\n')
    new_lines = []

    for line_num, line in enumerate(lines, 1):
        if should_skip_line(line):
            new_lines.append(line)
            report['skipped'].append((line_num, 'exclusion pattern'))
            continue

        new_line = line
        for pattern, replacement, desc in REPLACEMENTS:
            matches = list(re.finditer(pattern, new_line))
            if matches:
                new_line = re.sub(pattern, replacement, new_line)
                for m in matches:
                    report['changes'].append({
                        'line': line_num,
                        'pattern': desc,
                        'before': m.group(0),
                        'after': replacement
                    })
                    report['total_replacements'] += 1

        new_lines.append(new_line)

    new_content = '\n'.join(new_lines)

    if not dry_run and new_content != content:
        filepath.write_text(new_content, encoding='utf-8')

    return report

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Refactor z → ξ in EDC Part II')
    parser.add_argument('--dry-run', action='store_true', help='Show changes without applying')
    parser.add_argument('--file', type=str, help='Process single file')
    args = parser.parse_args()

    sections_dir = Path(__file__).parent.parent / 'sections'

    if args.file:
        files = [Path(args.file)]
    else:
        files = sorted(sections_dir.glob('*.tex'))

    total_changes = 0
    all_reports = []

    for f in files:
        report = refactor_file(f, dry_run=args.dry_run)
        if report['total_replacements'] > 0:
            all_reports.append(report)
            total_changes += report['total_replacements']
            print(f"[{'DRY' if args.dry_run else 'DONE'}] {f.name}: {report['total_replacements']} replacements")

    print(f"\n{'='*60}")
    print(f"TOTAL: {total_changes} replacements in {len(all_reports)} files")

    if args.dry_run:
        print("\nRun without --dry-run to apply changes")

    # Write detailed report
    report_path = Path(__file__).parent.parent / 'NOTATION_REFACTOR_REPORT.md'
    with open(report_path, 'w') as f:
        f.write("# Notation Refactor Report: z → ξ\n\n")
        f.write(f"**Total replacements:** {total_changes}\n")
        f.write(f"**Files modified:** {len(all_reports)}\n\n")

        for report in all_reports:
            f.write(f"## {Path(report['file']).name}\n\n")
            f.write(f"Replacements: {report['total_replacements']}\n\n")
            if report['changes']:
                f.write("| Line | Pattern | Before | After |\n")
                f.write("|------|---------|--------|-------|\n")
                for c in report['changes'][:20]:  # Limit to first 20
                    f.write(f"| {c['line']} | {c['pattern']} | `{c['before']}` | `{c['after']}` |\n")
                if len(report['changes']) > 20:
                    f.write(f"| ... | {len(report['changes'])-20} more | ... | ... |\n")
            f.write("\n")

    print(f"\nDetailed report written to: {report_path}")

if __name__ == '__main__':
    main()
