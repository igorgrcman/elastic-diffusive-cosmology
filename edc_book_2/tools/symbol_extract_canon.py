#!/usr/bin/env python3
"""
symbol_extract_canon.py — Extract symbols + definitions from Canon PDFs

Purpose: Build authoritative symbol dictionary from published artifacts.
Uses pdftotext for text extraction, then pattern matching for definitions.

Canonical Sources:
- Book Part I (EDC_Book_v17.49.pdf)
- Paper 2 (EDC_Paper2.pdf)
- Framework v2.0 + Paper 3 + Companions A-H (paper3_bundle/)

Output: JSON/YAML with symbol definitions and page anchors.
"""

import re
import os
import sys
import json
import subprocess
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Canon source configuration
CANON_SOURCES = {
    'book_part1': {
        'file': 'book_part1/EDC_Book_v17.49.pdf',
        'name': 'Book Part I',
        'authority': 'CANON',
    },
    'paper2': {
        'file': 'paper2/EDC_Paper2.pdf',
        'name': 'Paper 2',
        'authority': 'CANON',
    },
    'framework_v2': {
        'file': 'paper3_bundle/00_Framework_v2_0__DOI_10.5281_zenodo.18299085.pdf',
        'name': 'Framework v2.0',
        'authority': 'CANON-PRIMARY',
        'doi': '10.5281/zenodo.18299085',
    },
    'paper3': {
        'file': 'paper3_bundle/01_Paper3_NJSR_Journal__DOI_10.5281_zenodo.18262721.pdf',
        'name': 'Paper 3 (NJSR)',
        'authority': 'CANON',
        'doi': '10.5281/zenodo.18262721',
    },
    'companion_a': {
        'file': 'paper3_bundle/02_CompanionA_Effective_Lagrangian__DOI_10.5281_zenodo.18292841.pdf',
        'name': 'Companion A: Effective Lagrangian',
        'authority': 'CANON',
        'doi': '10.5281/zenodo.18292841',
    },
    'companion_b': {
        'file': 'paper3_bundle/03_CompanionB_WKB_Prefactor__DOI_10.5281_zenodo.18299637.pdf',
        'name': 'Companion B: WKB Prefactor',
        'authority': 'CANON',
        'doi': '10.5281/zenodo.18299637',
    },
    'companion_c': {
        'file': 'paper3_bundle/04_CompanionC_5D_KK_Reduction__DOI_10.5281_zenodo.18299751.pdf',
        'name': 'Companion C: 5D KK Reduction',
        'authority': 'CANON',
        'doi': '10.5281/zenodo.18299751',
    },
    'companion_d': {
        'file': 'paper3_bundle/05_CompanionD_Selection_Rules__DOI_10.5281_zenodo.18299855.pdf',
        'name': 'Companion D: Selection Rules',
        'authority': 'CANON',
        'doi': '10.5281/zenodo.18299855',
    },
    'companion_e': {
        'file': 'paper3_bundle/06_CompanionE_Symmetry_Operations__DOI_10.5281_zenodo.18300199.pdf',
        'name': 'Companion E: Symmetry Operations',
        'authority': 'CANON',
        'doi': '10.5281/zenodo.18300199',
    },
    'companion_f': {
        'file': 'paper3_bundle/07_CompanionF_Proton_Junction_Model__DOI_10.5281_zenodo.18302953.pdf',
        'name': 'Companion F: Proton Junction Model',
        'authority': 'CANON',
        'doi': '10.5281/zenodo.18302953',
    },
    'companion_g': {
        'file': 'paper3_bundle/08_CompanionG_Neutron_Proton_Mass__DOI_10.5281_zenodo.18303494.pdf',
        'name': 'Companion G: Neutron-Proton Mass',
        'authority': 'CANON',
        'doi': '10.5281/zenodo.18303494',
    },
    'companion_h': {
        'file': 'paper3_bundle/09_CompanionH_Weak_Interactions__DOI_10.5281_zenodo.18307539.pdf',
        'name': 'Companion H: Weak Interactions',
        'authority': 'CANON',
        'doi': '10.5281/zenodo.18307539',
    },
}

# Definition patterns to search for
DEFINITION_PATTERNS = [
    r'is\s+defined\s+as',
    r'we\s+define',
    r'denote[sd]?\s+(?:by|as)?',
    r'where\s+\w+\s+is',
    r'let\s+\w+\s+(?:be|denote)',
    r'the\s+\w+\s+(?:coordinate|parameter|constant|variable|field)',
    r'(?:bulk|brane|membrane)\s+(?:coordinate|tension|thickness)',
    r'5D\s+(?:Planck|manifold|coordinate|bulk)',
    r'compactification\s+radius',
    r'fine\s+structure\s+constant',
    r'Fermi\s+constant',
]

# Symbol recognition in text (post-PDF extraction)
SYMBOL_TEXT_PATTERNS = [
    # Greek letters (as they appear after pdftotext)
    (r'\bξ\b|\\xi\b|xi\b', 'xi', 'ξ'),
    (r'\bη\b|\\eta\b|eta\b', 'eta', 'η'),
    (r'\bσ\b|\\sigma\b|sigma\b', 'sigma', 'σ'),
    (r'\bα\b|\\alpha\b|alpha\b', 'alpha', 'α'),
    (r'\bκ\b|\\kappa\b|kappa\b', 'kappa', 'κ'),
    (r'\bδ\b|\\delta\b|delta\b', 'delta', 'δ'),

    # Manifold
    (r'M5|M\s*5|M\^5|five[-\s]?dimensional\s+manifold', 'M5_manifold', 'M⁵'),
    (r'Σ3|Σ\s*3|Sigma\s*3|3[-\s]?brane', 'Sigma3', 'Σ³'),
    (r'S1|S\s*1|circle', 'S1', 'S¹'),

    # Scales
    (r'Rξ|R_ξ|R\s*ξ|compactification\s+radius', 'R_xi', 'R_ξ'),
    (r'ℓP|ℓ_P|Planck\s+length', 'ell_P', 'ℓ_P'),

    # Masses
    (r'M5,Pl|M_\{5,Pl\}|5D\s+Planck\s+mass', 'M_5Pl', 'M_{5,Pl}'),
    (r'me|m_e|electron\s+mass', 'm_e', 'm_e'),
    (r'mp|m_p|proton\s+mass', 'm_p', 'm_p'),
    (r'mn|m_n|neutron\s+mass', 'm_n', 'm_n'),
    (r'Δmnp|neutron[-\s]proton\s+mass', 'Delta_m_np', 'Δm_np'),

    # Couplings
    (r'G5|G_5|5D\s+gravitational', 'G_5', 'G₅'),
    (r'GF|G_F|Fermi\s+constant', 'G_F', 'G_F'),

    # Z6 program
    (r'Z6|Z_6|Z\s*6', 'Z6', 'Z₆'),
    (r'z1|z_1', 'z_1', 'z₁'),
    (r'z2|z_2', 'z_2', 'z₂'),
]


def extract_pdf_text(pdf_path: Path, page_num: int = None) -> str:
    """Extract text from PDF using pdftotext."""
    try:
        cmd = ['pdftotext', '-layout']
        if page_num is not None:
            cmd.extend(['-f', str(page_num), '-l', str(page_num)])
        cmd.extend([str(pdf_path), '-'])

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        return result.stdout
    except Exception as e:
        return f"ERROR: {e}"


def get_pdf_page_count(pdf_path: Path) -> int:
    """Get total page count of PDF."""
    try:
        result = subprocess.run(
            ['pdftotext', '-f', '1', '-l', '1', str(pdf_path), '-'],
            capture_output=True, text=True
        )
        # Try pdfinfo if available
        result = subprocess.run(
            ['pdfinfo', str(pdf_path)],
            capture_output=True, text=True
        )
        for line in result.stdout.split('\n'):
            if line.startswith('Pages:'):
                return int(line.split(':')[1].strip())
    except:
        pass
    return 50  # Default fallback


def find_definitions_in_text(text: str, page_num: int, source_name: str) -> list:
    """Find symbol definitions in extracted text."""
    definitions = []
    lines = text.split('\n')

    for line_num, line in enumerate(lines):
        # Check for definition patterns
        for pattern in DEFINITION_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                # Found a potential definition
                # Look for symbols in this line and surrounding context
                context_start = max(0, line_num - 1)
                context_end = min(len(lines), line_num + 2)
                context = ' '.join(lines[context_start:context_end])

                for sym_pattern, sym_id, sym_display in SYMBOL_TEXT_PATTERNS:
                    if re.search(sym_pattern, context, re.IGNORECASE):
                        snippet = line.strip()[:100]
                        definitions.append({
                            'symbol_id': sym_id,
                            'symbol_display': sym_display,
                            'page': page_num,
                            'source': source_name,
                            'snippet': snippet,
                            'definition_type': pattern[:30],
                        })

    return definitions


def extract_from_canon_pdf(source_key: str, source_config: dict, sources_dir: Path) -> dict:
    """Extract symbol definitions from a canon PDF."""
    pdf_path = sources_dir / source_config['file']

    result = {
        'source_key': source_key,
        'source_name': source_config['name'],
        'authority': source_config['authority'],
        'doi': source_config.get('doi', ''),
        'path': str(pdf_path),
        'exists': pdf_path.exists(),
        'definitions': [],
        'symbols_found': set(),
    }

    if not pdf_path.exists():
        result['error'] = f"PDF not found: {pdf_path}"
        return result

    # Get page count
    page_count = get_pdf_page_count(pdf_path)

    # Extract text page by page for accurate anchoring
    for page in range(1, min(page_count + 1, 100)):  # Limit to 100 pages
        text = extract_pdf_text(pdf_path, page)
        if text.startswith('ERROR'):
            continue

        defs = find_definitions_in_text(text, page, source_config['name'])
        result['definitions'].extend(defs)

        for d in defs:
            result['symbols_found'].add(d['symbol_id'])

    result['symbols_found'] = list(result['symbols_found'])
    return result


def build_canon_dictionary(sources_dir: Path) -> dict:
    """Build complete canon symbol dictionary."""
    results = {
        'timestamp': datetime.now().isoformat(),
        'sources_dir': str(sources_dir),
        'sources': {},
        'merged_dictionary': defaultdict(lambda: {
            'symbol_id': '',
            'symbol_display': '',
            'definitions': [],
            'canon_anchors': [],
            'primary_source': '',
        }),
    }

    for source_key, source_config in CANON_SOURCES.items():
        print(f"Processing: {source_config['name']}...")
        source_result = extract_from_canon_pdf(source_key, source_config, sources_dir)
        results['sources'][source_key] = source_result

        # Merge into dictionary
        for defn in source_result.get('definitions', []):
            sym_id = defn['symbol_id']
            entry = results['merged_dictionary'][sym_id]
            entry['symbol_id'] = sym_id
            entry['symbol_display'] = defn['symbol_display']
            entry['definitions'].append(defn)
            entry['canon_anchors'].append({
                'source': source_config['name'],
                'page': defn['page'],
                'snippet': defn['snippet'],
                'doi': source_config.get('doi', ''),
            })
            if source_config['authority'] == 'CANON-PRIMARY' and not entry['primary_source']:
                entry['primary_source'] = source_config['name']

    # Convert defaultdict to regular dict
    results['merged_dictionary'] = dict(results['merged_dictionary'])

    return results


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Extract symbols from Canon PDFs')
    parser.add_argument('--sources', required=True, help='Path to canon/sources directory')
    parser.add_argument('--output', default='canon_symbol_dictionary.json', help='Output file')
    args = parser.parse_args()

    sources_dir = Path(args.sources)
    if not sources_dir.exists():
        print(f"Error: Sources directory not found: {sources_dir}")
        sys.exit(1)

    print(f"Canon sources directory: {sources_dir}")
    results = build_canon_dictionary(sources_dir)

    # Output
    output_path = Path(args.output)
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)

    print(f"\nOutput: {output_path}")
    print(f"Sources processed: {len(results['sources'])}")
    print(f"Unique symbols found: {len(results['merged_dictionary'])}")

    # Print summary
    print("\nSymbols with canon anchors:")
    for sym_id, entry in sorted(results['merged_dictionary'].items()):
        anchor_count = len(entry['canon_anchors'])
        print(f"  {entry['symbol_display']:10} ({sym_id:15}): {anchor_count} anchors")

    return 0


if __name__ == '__main__':
    sys.exit(main())
