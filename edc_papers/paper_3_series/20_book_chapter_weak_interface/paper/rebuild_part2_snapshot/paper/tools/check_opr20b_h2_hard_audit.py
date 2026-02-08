#!/usr/bin/env python3
"""
OPR-20b H2-Hard Audit Checker
=============================

Scans the H2-hard audit LaTeX file for:
1. Forbidden tokens (SM smuggling): M_W, M_Z, v, sin^2θ_W, "fit", "tuned", etc.
2. Paragraph endings with epistemic tags: [P], [Dc], [I], [BL], [M], [OPEN]
3. Reports counts of each tag type.

No external dependencies - uses only Python stdlib.

Usage:
    python check_opr20b_h2_hard_audit.py [path_to_tex_file]
"""

import re
import sys
from pathlib import Path
from collections import Counter
from typing import List, Tuple, Dict

# =============================================================================
# FORBIDDEN TOKENS
# =============================================================================

FORBIDDEN_PATTERNS = [
    # Tuning/fitting language outside consistency boxes
    (r'\bfit(?:ted|ting)?\s+to\s+SM', 'fitting to SM'),
    (r'\btuned\s+to\s+match', 'tuned to match'),
    (r'\bchosen\s+to\s+match', 'chosen to match'),
    (r'\badjusted\s+to\s+give', 'adjusted to give'),
    # Circular definitions
    (r'\bdefine\s+\$?\\?delta\$?\s*=', 'circular delta definition'),
    (r'\\equiv\s*R_\\xi\s*\$?\s*\\tagDc', 'false [Dc] on equiv'),
]

# Allowed SM terms (for consistency check boxes only)
ALLOWED_IN_CONSISTENCY = [
    'M_W', 'M_Z', 'sin^2\\theta_W', 'G_F', 'v',
]

# =============================================================================
# EPISTEMIC TAGS
# =============================================================================

TAG_PATTERNS = {
    '[P]': r'\\tagP\{\}',
    '[Dc]': r'\\tagDc\{\}',
    '[I]': r'\\tagI\{\}',
    '[BL]': r'\\tagBL\{\}',
    '[M]': r'\\tagM\{\}',
    '[OPEN]': r'\\tagOPEN\{\}',
    '[Def]': r'\\tagDef\{\}',
}

# =============================================================================
# MAIN FUNCTIONS
# =============================================================================

def read_file(filepath: str) -> str:
    """Read LaTeX file content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def check_forbidden_tokens(content: str) -> List[Tuple[str, int, str]]:
    """
    Check for forbidden tokens.
    Returns list of (pattern_desc, line_num, matched_text).
    """
    findings = []
    lines = content.split('\n')

    # Track if we're in a consistency check box
    in_consistency_box = False

    for line_num, line in enumerate(lines, 1):
        # Check if entering/exiting consistency box
        if 'Consistency Check' in line or 'title=.*Consistency' in line:
            in_consistency_box = True
        if '\\end{tcolorbox}' in line and in_consistency_box:
            in_consistency_box = False
            continue

        # Skip forbidden checks inside consistency boxes
        if in_consistency_box:
            continue

        for pattern, desc in FORBIDDEN_PATTERNS:
            matches = re.finditer(pattern, line, re.IGNORECASE)
            for match in matches:
                findings.append((desc, line_num, match.group()))

    return findings


def count_epistemic_tags(content: str) -> Dict[str, int]:
    """Count occurrences of each epistemic tag."""
    counts = {}
    for tag_name, pattern in TAG_PATTERNS.items():
        counts[tag_name] = len(re.findall(pattern, content))
    return counts


def check_paragraph_tags(content: str) -> Tuple[int, int, List[int]]:
    """
    Check if paragraphs end with epistemic tags.
    Returns: (total_paragraphs, tagged_paragraphs, untagged_line_nums)

    A "paragraph" is defined as a text block ending with double newline
    or before a LaTeX environment/command.
    """
    # Find potential paragraph endings
    # Look for lines that aren't empty, comments, or commands, and precede blank lines
    lines = content.split('\n')

    tagged = 0
    untagged = 0
    untagged_lines = []

    # Combine all tag patterns
    any_tag_pattern = '|'.join(TAG_PATTERNS.values())

    for i, line in enumerate(lines):
        line_stripped = line.strip()

        # Skip empty lines, pure comments, commands, environments
        if not line_stripped:
            continue
        if line_stripped.startswith('%'):
            continue
        if line_stripped.startswith('\\begin') or line_stripped.startswith('\\end'):
            continue
        if line_stripped.startswith('\\item'):
            # Item lines should ideally have tags, but we'll be lenient
            continue
        if re.match(r'^\\[a-zA-Z]+(\[.*\])?(\{.*\})?$', line_stripped):
            continue

        # Check if this line is followed by blank line or environment (paragraph end)
        is_paragraph_end = False
        if i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if not next_line or next_line.startswith('\\') or next_line.startswith('%'):
                is_paragraph_end = True
        else:
            is_paragraph_end = True  # Last line

        if is_paragraph_end and not line_stripped.endswith('}'):
            # This might be a narrative paragraph that should end with a tag
            if re.search(any_tag_pattern, line):
                tagged += 1
            else:
                # Check if the line has actual content (not just commands)
                content_line = re.sub(r'\\[a-zA-Z]+(\{[^}]*\})?', '', line_stripped)
                if len(content_line.strip()) > 10:  # Has meaningful content
                    untagged += 1
                    untagged_lines.append(i + 1)

    return tagged + untagged, tagged, untagged_lines[:10]  # Limit to first 10


def print_report(filepath: str, forbidden: List, tag_counts: Dict,
                 para_stats: Tuple) -> bool:
    """Print audit report. Returns True if all checks pass."""
    print("=" * 70)
    print(f"OPR-20b H2-Hard Audit Report")
    print(f"File: {filepath}")
    print("=" * 70)

    all_pass = True

    # Forbidden tokens check
    print("\n[1] FORBIDDEN TOKENS CHECK")
    print("-" * 40)
    if forbidden:
        all_pass = False
        print(f"FAIL: Found {len(forbidden)} forbidden tokens:")
        for desc, line_num, text in forbidden:
            print(f"  Line {line_num}: {desc} -- '{text[:50]}...'")
    else:
        print("PASS: No forbidden tokens found")

    # Epistemic tags count
    print("\n[2] EPISTEMIC TAG COUNTS")
    print("-" * 40)
    total = sum(tag_counts.values())
    for tag, count in sorted(tag_counts.items()):
        print(f"  {tag:8s}: {count:3d}")
    print(f"  {'TOTAL':8s}: {total:3d}")

    # Tag coverage assessment
    if total < 20:
        print("\nWARNING: Low tag count - may indicate missing tags")

    # Paragraph tag check
    print("\n[3] PARAGRAPH TAGGING CHECK")
    print("-" * 40)
    total_para, tagged_para, untagged_lines = para_stats
    coverage = (tagged_para / total_para * 100) if total_para > 0 else 0
    print(f"  Paragraphs checked: {total_para}")
    print(f"  With tags: {tagged_para}")
    print(f"  Coverage: {coverage:.1f}%")

    if untagged_lines:
        print(f"\n  Note: Some lines may lack tags (sample line numbers):")
        print(f"    {untagged_lines}")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    # Check for required elements
    required = ['[P]', '[Dc]', '[OPEN]']
    missing_required = [t for t in required if tag_counts.get(t, 0) == 0]

    if missing_required:
        all_pass = False
        print(f"FAIL: Missing required tags: {missing_required}")

    if all_pass:
        print("STATUS: PASS - Audit file meets H2-Hard requirements")
    else:
        print("STATUS: FAIL - Issues found (see above)")

    print("=" * 70)

    return all_pass


def main():
    # Default path
    default_path = Path(__file__).parent.parent / 'sections' / \
                   'ch11_opr20_attemptH2_delta_Rxi_hard_audit.tex'

    if len(sys.argv) > 1:
        filepath = Path(sys.argv[1])
    else:
        filepath = default_path

    if not filepath.exists():
        print(f"ERROR: File not found: {filepath}")
        sys.exit(1)

    content = read_file(filepath)

    # Run checks
    forbidden = check_forbidden_tokens(content)
    tag_counts = count_epistemic_tags(content)
    para_stats = check_paragraph_tags(content)

    # Print report
    success = print_report(filepath, forbidden, tag_counts, para_stats)

    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
