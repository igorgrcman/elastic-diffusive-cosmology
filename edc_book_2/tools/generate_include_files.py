#!/usr/bin/env python3
"""
generate_include_files.py — Extract document bodies from standalone LaTeX files

For each standalone .tex file (with \documentclass), creates a .include.tex
sibling containing only the document body (content between \begin{document}
and \end{document}).

This allows including standalone derivations into Book2 without nested
document structures.
"""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent

# List of orphan standalone files to process
ORPHAN_FILES = [
    # Derivations
    "edc_papers/_shared/derivations/delta_from_5d_action_proton_scale.tex",
    "edc_papers/_shared/derivations/dlr_from_chiral_localization.tex",
    "edc_papers/_shared/derivations/fw_from_stability_and_spectrum.tex",
    "edc_papers/_shared/derivations/gf_noncircular_chain_framework.tex",
    "edc_papers/_shared/derivations/gf_potential_shapes_from_5d.tex",
    "edc_papers/_shared/derivations/israel_zn_fixed_points_anchors.tex",
    "edc_papers/_shared/derivations/prefactor_A_from_fluctuations.tex",
    "edc_papers/_shared/derivations/zn_anisotropy_normalization_from_action.tex",
    "edc_papers/_shared/derivations/zn_mode_selection_nonlinear_W.tex",
    "edc_papers/_shared/derivations/zn_ring_delta_pinning_modes.tex",
    "edc_papers/_shared/derivations/zn_strong_pinning_regimes.tex",
    "edc_papers/_shared/derivations/zn_symmetry_breaking_one_defect.tex",
    "edc_papers/_shared/derivations/zn_toy_functional_from_5d_action.tex",
    # Lemmas
    "edc_papers/_shared/lemmas/z6_discrete_averaging_lemma.tex",
    "edc_papers/_shared/lemmas/zn_discrete_averaging_lemma.tex",
]


def extract_document_body(content: str, filename_stem: str = None) -> str:
    """
    Extract content between \begin{document} and \end{document}.

    Also removes:
    - \maketitle (we'll handle titles in the appendix)
    - \tableofcontents
    - \begin{abstract}...\end{abstract} (not defined in book class)

    And converts:
    - hypothesis environment -> conjecture (defined in Book2)
    - \label{X} -> \label{DL:<filename>:X} to avoid multiply-defined labels
    """
    # Find \begin{document}
    begin_match = re.search(r'\\begin\{document\}', content)
    if not begin_match:
        return None

    # Find \end{document}
    end_match = re.search(r'\\end\{document\}', content)
    if not end_match:
        return None

    # Extract body
    body = content[begin_match.end():end_match.start()]

    # Remove \maketitle
    body = re.sub(r'\\maketitle\s*', '', body)

    # Remove \tableofcontents
    body = re.sub(r'\\tableofcontents\s*', '', body)

    # Remove abstract environment (not defined in book class)
    body = re.sub(r'\\begin\{abstract\}.*?\\end\{abstract\}', '', body, flags=re.DOTALL)

    # Convert hypothesis environment to conjecture (defined in Book2)
    body = re.sub(r'\\begin\{hypothesis\}', r'\\begin{conjecture}', body)
    body = re.sub(r'\\end\{hypothesis\}', r'\\end{conjecture}', body)

    # Prefix labels to avoid multiply-defined when including multiple derivations
    # \label{foo} -> \label{DL:<filename>:foo}
    if filename_stem:
        # Create a short prefix from filename (e.g., "zn_toy_functional" -> "zn-toy-func")
        short_prefix = filename_stem.replace('_', '-')[:20]
        body = re.sub(
            r'\\label\{([^}]+)\}',
            rf'\\label{{DL:{short_prefix}:\1}}',
            body
        )
        # Also update \ref, \eqref, \cref to match
        body = re.sub(
            r'\\(ref|eqref|cref)\{([^}]+)\}',
            lambda m: f'\\{m.group(1)}{{DL:{short_prefix}:{m.group(2)}}}',
            body
        )

    # Strip leading/trailing whitespace
    body = body.strip()

    return body


def extract_title(content: str) -> str:
    """Extract the document title from \title{...}."""
    match = re.search(r'\\title\{([^}]+)\}', content)
    if match:
        return match.group(1)
    return None


def generate_include_file(source_path: Path) -> tuple:
    """
    Generate a .include.tex file from a standalone source.

    Returns (include_path, title, success).
    """
    # Read source
    try:
        content = source_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"ERROR: Cannot read {source_path}: {e}")
        return None, None, False

    # Check it's standalone
    if '\\documentclass' not in content:
        print(f"SKIP: {source_path.name} is not a standalone document")
        return None, None, False

    # Extract body (with label prefixing to avoid collisions)
    body = extract_document_body(content, filename_stem=source_path.stem)
    if body is None:
        print(f"ERROR: Cannot extract body from {source_path.name}")
        return None, None, False

    # Extract title
    title = extract_title(content)

    # Generate include file path
    include_path = source_path.with_suffix('.include.tex')

    # Create include content with clear provenance
    rel_source = source_path.relative_to(REPO_ROOT)
    include_content = f"""% =============================================================================
% EXTRACTED INCLUDE BODY — AUTO-GENERATED
% =============================================================================
% Source: {rel_source} (standalone derivation document)
% This file: Includable body extract for Book2 Derivation Library
%
% DO NOT EDIT THIS FILE DIRECTLY.
% Edit the standalone source ({source_path.name}) instead, then regenerate.
%
% Labels are prefixed with DL:<filename>: to avoid collisions in Book2.
% Generated by: edc_book_2/tools/generate_include_files.py
% =============================================================================

{body}
"""

    # Write include file
    try:
        include_path.write_text(include_content, encoding='utf-8')
        print(f"CREATED: {include_path.name} ({len(body)} chars)")
        return include_path, title, True
    except Exception as e:
        print(f"ERROR: Cannot write {include_path}: {e}")
        return None, None, False


def main():
    print("Generating .include.tex files for orphan standalone documents")
    print("=" * 60)

    results = []

    for rel_path in ORPHAN_FILES:
        source_path = REPO_ROOT / rel_path
        if not source_path.exists():
            print(f"WARNING: {rel_path} does not exist")
            continue

        include_path, title, success = generate_include_file(source_path)
        if success:
            results.append({
                'source': rel_path,
                'include': str(include_path.relative_to(REPO_ROOT)),
                'title': title or source_path.stem.replace('_', ' ').title(),
            })

    print()
    print("=" * 60)
    print(f"Generated {len(results)} include files")
    print()

    # Print summary for use in appendix
    print("For APPENDIX_DERIVATION_LIBRARY.tex:")
    print("-" * 40)
    for r in results:
        print(f"\\subsection{{{r['title']}}}")
        print(f"\\input{{\\EDCPAPERS/{r['include'].replace('edc_papers/', '')}}}")
        print()

    return results


if __name__ == "__main__":
    main()
