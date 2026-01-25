#!/usr/bin/env python3
"""
symbol_audit.py — Context-aware symbol audit for EDC Book 2

Scans LaTeX sources for symbol usage and classifies each occurrence.
Does NOT perform any replacements — audit only.

Classification labels:
- CLASS_5D_DEPTH: ξ used as 5D compact coordinate (EXPECTED)
- CLASS_3D_Z: z used as 3D spatial coordinate (OK)
- CLASS_Z6: z₁, z₂ used in Z6 program (OK)
- CLASS_DUMMY: Integration/summation dummy variable (OK)
- CLASS_TOPOLOGY: S¹ topology reference (OK)
- CLASS_VIOLATION_Z_AS_5D: z used as 5D depth (BAD)
- CLASS_VIOLATION_MANIFOLD: M5/M_5 instead of \mathcal{M}^5 (BAD)
- CLASS_UNKNOWN: Needs manual review

Output: SYMBOL_AUDIT_REPORT.md + SYMBOL_AUDIT_REPORT.csv
"""

import os
import re
import csv
from pathlib import Path
from datetime import datetime

# Patterns to detect
PATTERNS = {
    'xi_depth': r'\\xi(?![a-zA-Z])',  # ξ as coordinate
    'R_xi': r'R_\\xi|\\Rxi',  # R_ξ scale
    'z_standalone': r'(?<![a-zA-Z_\\])z(?![a-zA-Z0-9_])',  # standalone z
    'z_subscript': r'z_[0-9]|z_\{[0-9]\}',  # z₁, z₂ etc
    'z_in_coord': r'x\^\{?\\mu\}?,\s*z\)?|z\s*\)|,\s*z\s*\)',  # (x^μ, z) pattern
    'delta_z': r'\\Delta\s*z|\\delta\s*z',  # Δz pattern
    'M5_bad': r'(?<!\\mathcal\{)M[_\^]?5(?!\})',  # M5 or M_5 or M^5 without mathcal
    'mathcal_M': r'\\mathcal\{M\}\^5',  # Correct \mathcal{M}^5
    'Sigma': r'\\Sigma\^?3?',  # Σ or Σ³
    'S1_topology': r'S\^1|S\^{1}',  # S¹ topology
    'Z6': r'Z_?6|Z_\{6\}',  # Z₆ symmetry
}

# Context patterns that indicate 5D depth usage
CONTEXT_5D_DEPTH = [
    r'fifth\s+dimension',
    r'5D\s+(coordinate|direction|depth)',
    r'compact\s+(coordinate|direction|dimension)',
    r'extra\s+dimension',
    r'bulk.*coordinate',
    r'along\s+.*\s+z',
    r'z\s*=\s*0',  # boundary at z=0
    r'd[zξ]',  # integration element
    r'∂.*z',  # derivative wrt z
    r'f\(.*z\)',  # function of z
]

# Context patterns that indicate 3D spatial z
CONTEXT_3D_SPATIAL = [
    r'x,\s*y,\s*z',  # (x, y, z) spatial
    r'spatial\s+coordinate',
    r'3D\s+.*z',
]


def classify_z_usage(line: str, context_before: str, context_after: str) -> str:
    """Classify a z occurrence based on context."""
    full_context = context_before + line + context_after

    # Check for Z6 context
    if re.search(r'Z_?6|Z6', full_context):
        return 'CLASS_Z6'

    # Check for z₁, z₂ subscripts
    if re.search(r'z_[12]|z_\{[12]\}', line):
        return 'CLASS_Z6'

    # Check for 3D spatial context
    if re.search(r'x,\s*y,\s*z|spatial|3D\s+coord', full_context, re.IGNORECASE):
        return 'CLASS_3D_Z'

    # Check for 5D depth context (VIOLATION)
    for pattern in CONTEXT_5D_DEPTH:
        if re.search(pattern, full_context, re.IGNORECASE):
            return 'CLASS_VIOLATION_Z_AS_5D'

    # Check for coordinate tuple patterns like (x^μ, z) - likely 5D
    if re.search(r'x\^.*,\s*z\)|x\^\{?\\mu\}?,\s*z', line):
        return 'CLASS_VIOLATION_Z_AS_5D'

    # Check for Δz which often means 5D separation
    if re.search(r'\\Delta\s*z', line):
        return 'CLASS_VIOLATION_Z_AS_5D'

    return 'CLASS_UNKNOWN'


def classify_xi_usage(line: str, context: str) -> str:
    """Classify a ξ occurrence."""
    # Almost always 5D depth in EDC
    if re.search(r'coherence|GL|Ginzburg', context, re.IGNORECASE):
        return 'CLASS_GL_COHERENCE'  # Collision case
    return 'CLASS_5D_DEPTH'


def scan_file(filepath: Path) -> list:
    """Scan a single file for symbol issues."""
    results = []

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except Exception as e:
        return [{'file': str(filepath), 'error': str(e)}]

    for i, line in enumerate(lines, 1):
        context_before = ''.join(lines[max(0, i-3):i-1])
        context_after = ''.join(lines[i:min(len(lines), i+2)])

        # Check for bad M5 pattern
        if re.search(PATTERNS['M5_bad'], line):
            results.append({
                'file': str(filepath),
                'line': i,
                'token': 'M5/M_5',
                'context': line.strip()[:100],
                'classification': 'CLASS_VIOLATION_MANIFOLD',
                'decision': 'VIOLATION',
            })

        # Check for z in coordinate context
        z_coord_match = re.search(PATTERNS['z_in_coord'], line)
        if z_coord_match:
            classification = classify_z_usage(line, context_before, context_after)
            results.append({
                'file': str(filepath),
                'line': i,
                'token': z_coord_match.group(),
                'context': line.strip()[:100],
                'classification': classification,
                'decision': 'VIOLATION' if 'VIOLATION' in classification else 'OK' if classification != 'CLASS_UNKNOWN' else 'NEEDS_REVIEW',
            })

        # Check for Δz pattern
        delta_z_match = re.search(PATTERNS['delta_z'], line)
        if delta_z_match:
            classification = classify_z_usage(line, context_before, context_after)
            results.append({
                'file': str(filepath),
                'line': i,
                'token': delta_z_match.group(),
                'context': line.strip()[:100],
                'classification': classification,
                'decision': 'VIOLATION' if 'VIOLATION' in classification else 'NEEDS_REVIEW',
            })

    return results


def main():
    """Main entry point."""
    src_dir = Path(__file__).parent.parent / 'src' / 'sections'
    audit_dir = Path(__file__).parent.parent / 'audit' / 'notation'
    audit_dir.mkdir(parents=True, exist_ok=True)

    all_results = []
    file_count = 0

    # Scan all .tex files
    for tex_file in sorted(src_dir.glob('*.tex')):
        file_count += 1
        results = scan_file(tex_file)
        all_results.extend(results)

    # Count statistics
    violations = [r for r in all_results if r.get('decision') == 'VIOLATION']
    needs_review = [r for r in all_results if r.get('decision') == 'NEEDS_REVIEW']
    ok_count = len([r for r in all_results if r.get('decision') == 'OK'])

    # Write markdown report
    report_path = audit_dir / 'SYMBOL_AUDIT_REPORT.md'
    with open(report_path, 'w') as f:
        f.write(f"# Symbol Audit Report\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(f"## Summary\n\n")
        f.write(f"| Metric | Count |\n")
        f.write(f"|--------|-------|\n")
        f.write(f"| Files scanned | {file_count} |\n")
        f.write(f"| Total findings | {len(all_results)} |\n")
        f.write(f"| VIOLATIONS | {len(violations)} |\n")
        f.write(f"| NEEDS_REVIEW | {len(needs_review)} |\n")
        f.write(f"| OK | {ok_count} |\n\n")

        if violations:
            f.write(f"## Violations (z as 5D depth, bad manifold notation)\n\n")
            f.write(f"| File | Line | Token | Classification | Context |\n")
            f.write(f"|------|------|-------|----------------|----------|\n")
            for v in violations:
                ctx = v.get('context', '')[:60].replace('|', '\\|')
                f.write(f"| {Path(v['file']).name} | {v['line']} | `{v['token']}` | {v['classification']} | `{ctx}` |\n")

        if needs_review:
            f.write(f"\n## Needs Manual Review\n\n")
            f.write(f"| File | Line | Token | Context |\n")
            f.write(f"|------|------|-------|----------|\n")
            for r in needs_review[:50]:  # Limit to 50
                ctx = r.get('context', '')[:60].replace('|', '\\|')
                f.write(f"| {Path(r['file']).name} | {r['line']} | `{r['token']}` | `{ctx}` |\n")
            if len(needs_review) > 50:
                f.write(f"\n... and {len(needs_review) - 50} more\n")

        f.write(f"\n## Gate Status\n\n")
        if violations:
            f.write(f"**FAIL**: {len(violations)} violations found\n")
        else:
            f.write(f"**PASS**: No violations found\n")

    # Write CSV
    csv_path = audit_dir / 'SYMBOL_AUDIT_REPORT.csv'
    with open(csv_path, 'w', newline='') as f:
        if all_results:
            writer = csv.DictWriter(f, fieldnames=['file', 'line', 'token', 'context', 'classification', 'decision'])
            writer.writeheader()
            writer.writerows(all_results)

    # Print summary
    print(f"=== Symbol Audit Complete ===")
    print(f"Files scanned: {file_count}")
    print(f"Violations: {len(violations)}")
    print(f"Needs review: {len(needs_review)}")
    print(f"Report: {report_path}")

    return 0 if not violations else 1


if __name__ == '__main__':
    exit(main())
