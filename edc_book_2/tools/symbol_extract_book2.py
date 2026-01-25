#!/usr/bin/env python3
"""
symbol_extract_book2.py — Extract symbols + anchors from Book 2 LaTeX

Purpose: Inventory only — NO replacements, NO modifications.
Generates machine-readable symbol list with file:line anchors.

Output: YAML/JSON with symbol occurrences by file and context.
"""

import re
import os
import sys
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Tier-1 symbols that MUST be found
TIER1_SYMBOLS = {
    r'\\xi': 'ξ (5D coordinate)',
    r'R_\\xi': 'R_ξ (compactification radius)',
    r'\\sigma': 'σ (brane tension)',
    r'\\eta': 'η (metric signature or parameter)',
    r'P_\\mathrm\{bulk\}': 'P_bulk (bulk pressure)',
    r'\\mathcal\{M\}\^5': 'M⁵ (5D manifold)',
    r'\\Sigma\^3': 'Σ³ (3D brane)',
    r'M_\{5,\\mathrm\{Pl\}\}': 'M_{5,Pl} (5D Planck mass)',
    r'z_1': 'z₁ (Z6 complex)',
    r'z_2': 'z₂ (Z6 complex)',
}

# Symbol patterns to extract (LaTeX)
SYMBOL_PATTERNS = [
    # Greek letters
    (r'\\xi', 'greek', 'xi'),
    (r'\\eta', 'greek', 'eta'),
    (r'\\sigma', 'greek', 'sigma'),
    (r'\\alpha', 'greek', 'alpha'),
    (r'\\kappa', 'greek', 'kappa'),
    (r'\\delta', 'greek', 'delta'),
    (r'\\theta', 'greek', 'theta'),
    (r'\\phi', 'greek', 'phi'),
    (r'\\psi', 'greek', 'psi'),
    (r'\\Psi', 'greek', 'Psi'),
    (r'\\Sigma', 'greek', 'Sigma'),
    (r'\\Gamma', 'greek', 'Gamma'),
    (r'\\Lambda', 'greek', 'Lambda'),

    # Manifold/topology
    (r'\\mathcal\{M\}\^5', 'manifold', 'M5_calligraphic'),
    (r'\\mathcal\{M\}\^4', 'manifold', 'M4_calligraphic'),
    (r'M_5\b', 'ambiguous', 'M_5_raw'),  # Potential collision
    (r'M5\b', 'ambiguous', 'M5_raw'),
    (r'\\Sigma\^3|\\Sigma_3|\\Sigma\{3\}', 'topology', 'Sigma3'),
    (r'S\^1|S_1', 'topology', 'S1'),
    (r'S\^3|S_3', 'topology', 'S3'),
    (r'B\^3|B_3', 'topology', 'B3'),

    # Coordinates
    (r'R_\\xi|\\Rxi', 'scale', 'R_xi'),
    (r'R_z', 'violation', 'R_z_forbidden'),
    (r'x\^\\mu', 'coordinate', 'x_mu'),
    (r'\(x,\s*y,\s*z\)', 'coordinate', 'xyz_3D'),
    (r'\(x\^\\mu,\s*z\)', 'violation', 'xmu_z_tuple'),
    (r'\(x\^\\mu,\s*\\xi\)', 'coordinate', 'xmu_xi_tuple'),
    (r'\\Delta\\xi|\\Deltaξ', 'coordinate', 'Delta_xi'),
    (r'\\Delta z', 'ambiguous', 'Delta_z'),
    (r'z_H|z_\\mathrm\{H\}', 'ambiguous', 'z_H'),
    (r'\\xi_H|\\xi_\\mathrm\{H\}', 'coordinate', 'xi_H'),

    # Masses and Planck
    (r'M_\{5,\\mathrm\{Pl\}\}|M_\{5,Pl\}', 'mass', 'M_5Pl'),
    (r'M_\{Pl\}|M_\\mathrm\{Pl\}', 'mass', 'M_Pl'),
    (r'm_e', 'mass', 'm_e'),
    (r'm_p', 'mass', 'm_p'),
    (r'm_n', 'mass', 'm_n'),
    (r'm_\\mu', 'mass', 'm_mu'),
    (r'm_\\tau', 'mass', 'm_tau'),
    (r'\\Delta m_\{?np\}?', 'mass', 'Delta_m_np'),

    # Couplings and constants
    (r'G_5|G_\{5\}', 'coupling', 'G_5'),
    (r'G_4|G_\{4\}', 'coupling', 'G_4'),
    (r'G_F|G_\{F\}', 'coupling', 'G_F'),
    (r'g_5|g_\{5\}', 'coupling', 'g_5'),

    # Z6 program
    (r'Z_6|\\mathbb\{Z\}_6', 'group', 'Z6'),
    (r'Z_3|\\mathbb\{Z\}_3', 'group', 'Z3'),
    (r'Z_2|\\mathbb\{Z\}_2', 'group', 'Z2'),
    (r'z_1', 'complex', 'z_1_complex'),
    (r'z_2', 'complex', 'z_2_complex'),

    # Actions
    (r'S_\{?\\mathrm\{tot\}\}?|S_tot', 'action', 'S_tot'),
    (r'S_\{?\\mathrm\{bulk\}\}?|S_bulk', 'action', 'S_bulk'),
    (r'S_\{?\\mathrm\{brane\}\}?|S_brane', 'action', 'S_brane'),
    (r'S_\{?\\mathrm\{GHY\}\}?|S_GHY', 'action', 'S_GHY'),

    # Bulk-brane current
    (r'\\Jbb\{[^}]*\}|J\^\\nu_\{bulk\\to brane\}', 'current', 'J_bulk_brane'),

    # Fields
    (r'A_\\mu', 'field', 'A_mu'),
    (r'g_\{\\mu\\nu\}', 'metric', 'g_munu'),
    (r'G_\{AB\}', 'metric', 'G_AB'),
]

# z-context classification patterns
Z_CONTEXT_PATTERNS = [
    (r'\(\s*x\s*,\s*y\s*,\s*z\s*\)', 'z_3D_spatial', '3D spatial (x,y,z)'),
    (r'\(\s*x\^\{?\\mu\}?\s*,\s*z\s*\)', 'z_5D_violation', '5D tuple (x^μ,z) → should be ξ'),
    (r'\\phi\s*\(\s*x\s*,\s*z\s*\)|\\phi\s*\(\s*x\^\{?\\mu\}?\s*,\s*z\s*\)', 'z_5D_field', 'Field in 5D'),
    (r'z_1|z_2', 'z_Z6_complex', 'Z6 complex'),
    (r'\\Delta\s*z', 'z_5D_separation', '5D separation'),
    (r'z_H|z_\{H\}|z_\\mathrm\{H\}', 'z_5D_horizon', '5D horizon boundary'),
    (r'f\s*\(\s*z\s*\)', 'z_5D_profile', '5D profile function'),
    (r'\\int.*dz', 'z_integration', 'Integration variable'),
    (r'\\xi_[ijk]|\\xi_\{[ijk]\}', 'xi_generation', 'Generation position'),
    (r'z_[ijk](?!_)|z_\{[ijk]\}', 'z_generation_maybe', 'Possible generation position (should be ξ)'),
]


def extract_context(line: str, match_pos: int, context_chars: int = 60) -> str:
    """Extract surrounding context for a match."""
    start = max(0, match_pos - context_chars)
    end = min(len(line), match_pos + context_chars)
    return line[start:end].strip()


def find_section_label(lines: list, line_num: int) -> str:
    """Find nearest section/label before this line."""
    for i in range(line_num, max(-1, line_num - 50), -1):
        if i < 0 or i >= len(lines):
            continue
        line = lines[i]
        # Look for section/subsection
        sec_match = re.search(r'\\(sub)*section\*?\{([^}]+)\}', line)
        if sec_match:
            return f"§{sec_match.group(2)[:40]}"
        # Look for label
        lbl_match = re.search(r'\\label\{([^}]+)\}', line)
        if lbl_match:
            return f"label:{lbl_match.group(1)}"
    return ""


def classify_z_usage(line: str, context: str) -> dict:
    """Classify z usage in context."""
    result = {
        'type': 'unknown',
        'description': 'Unclassified z usage',
        'is_violation': False,
    }

    full_text = context + " " + line

    for pattern, z_type, desc in Z_CONTEXT_PATTERNS:
        if re.search(pattern, full_text, re.IGNORECASE):
            result['type'] = z_type
            result['description'] = desc
            result['is_violation'] = 'violation' in z_type or '5D' in z_type
            break

    return result


def extract_from_file(filepath: Path) -> dict:
    """Extract all symbols from a LaTeX file."""
    results = {
        'file': str(filepath.name),
        'path': str(filepath),
        'symbols': defaultdict(list),
        'violations': [],
        'z_usages': [],
        'tier1_found': set(),
    }

    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
            lines = content.split('\n')
    except Exception as e:
        results['error'] = str(e)
        return results

    # Check tier-1 symbols
    for pattern, name in TIER1_SYMBOLS.items():
        if re.search(pattern, content):
            results['tier1_found'].add(name)

    # Extract all symbol occurrences
    for line_num, line in enumerate(lines, 1):
        # Skip comments
        if line.strip().startswith('%'):
            continue

        for pattern, sym_type, sym_name in SYMBOL_PATTERNS:
            for match in re.finditer(pattern, line):
                context = extract_context(line, match.start())
                section = find_section_label(lines, line_num - 1)

                occurrence = {
                    'line': line_num,
                    'match': match.group(),
                    'context': context,
                    'section': section,
                }

                results['symbols'][sym_name].append(occurrence)

                # Track violations
                if sym_type == 'violation':
                    results['violations'].append({
                        'symbol': sym_name,
                        'line': line_num,
                        'context': context,
                        'section': section,
                    })

                # Track ambiguous z usages
                if sym_type == 'ambiguous' and 'z' in sym_name.lower():
                    z_class = classify_z_usage(line, context)
                    results['z_usages'].append({
                        'symbol': sym_name,
                        'line': line_num,
                        'context': context,
                        'section': section,
                        'classification': z_class,
                    })

    # Convert set to list for JSON serialization
    results['tier1_found'] = list(results['tier1_found'])

    return results


def scan_book2_sources(src_dir: Path) -> dict:
    """Scan all Book 2 source files."""
    results = {
        'timestamp': datetime.now().isoformat(),
        'source_dir': str(src_dir),
        'files': [],
        'summary': {
            'total_files': 0,
            'symbols_by_type': defaultdict(int),
            'violations': [],
            'tier1_coverage': {},
        },
    }

    tex_files = sorted(src_dir.rglob('*.tex'))
    results['summary']['total_files'] = len(tex_files)

    all_tier1 = set()

    for tex_file in tex_files:
        # Skip build/output directories
        if 'build' in str(tex_file) or 'output' in str(tex_file):
            continue

        file_result = extract_from_file(tex_file)
        results['files'].append(file_result)

        # Aggregate
        for sym_name, occurrences in file_result['symbols'].items():
            results['summary']['symbols_by_type'][sym_name] += len(occurrences)

        results['summary']['violations'].extend(file_result['violations'])
        all_tier1.update(file_result['tier1_found'])

    # Tier-1 coverage report
    for pattern, name in TIER1_SYMBOLS.items():
        results['summary']['tier1_coverage'][name] = name in all_tier1

    return results


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Extract symbols from Book 2 LaTeX')
    parser.add_argument('--src', default='src', help='Source directory')
    parser.add_argument('--output', default='symbol_extract_book2.json', help='Output file')
    args = parser.parse_args()

    # Determine source directory
    script_dir = Path(__file__).parent.parent
    src_dir = script_dir / args.src

    if not src_dir.exists():
        print(f"Error: Source directory not found: {src_dir}")
        sys.exit(1)

    print(f"Scanning: {src_dir}")
    results = scan_book2_sources(src_dir)

    # Output
    output_path = script_dir / 'audit' / 'notation' / args.output
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)

    print(f"Output: {output_path}")
    print(f"Files scanned: {results['summary']['total_files']}")
    print(f"Violations found: {len(results['summary']['violations'])}")
    print(f"Tier-1 coverage: {sum(results['summary']['tier1_coverage'].values())}/{len(TIER1_SYMBOLS)}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
