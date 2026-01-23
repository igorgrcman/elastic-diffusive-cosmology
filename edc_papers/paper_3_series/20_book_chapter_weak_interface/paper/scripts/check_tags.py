#!/usr/bin/env python3
"""
EDC Epistemic Tag Consistency Checker
======================================

Scans LaTeX for [Dc] tagged statements around ansatz words and flags
inconsistencies.

Deliverable D4c: Tag consistency checker that:
- Scans for [Dc] claims near "postulate", "assume", "ansatz" words
- Flags epistemic tag mismatches
- Recommends tag corrections

Usage:
    python scripts/check_tags.py
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass

# ==============================================================================
# Configuration
# ==============================================================================

SCRIPT_DIR = Path(__file__).parent
PAPER_DIR = SCRIPT_DIR.parent
SECTIONS_DIR = PAPER_DIR / "sections"

# ==============================================================================
# Tag Definitions
# ==============================================================================

# Valid epistemic tags
VALID_TAGS = {
    "[Der]": "Derived (explicit derivation from postulates)",
    "[Dc]": "Derived-conditional (derived under stated assumptions)",
    "[P]": "Postulated (assumption/hypothesis)",
    "[BL]": "Baseline (external reference: PDG/CODATA)",
    "[Cal]": "Calibrated (fitted to data)",
    "[I]": "Identified (pattern matching, not unique)",
    "[OPEN]": "Open problem (not yet resolved)",
    "[Def]": "Definition (by construction)",
}

# LaTeX tag macros
TAG_PATTERNS = [
    r"\\tag(Der|Dc|P|BL|Cal|I|OPEN|Def)\{\}",
    r"\\textbf\{\[(Der|Dc|P|BL|Cal|I|OPEN|Def)\]\}",
    r"\[(Der|Dc|P|BL|Cal|I|OPEN|Def)\]",
]

# Words that indicate postulates (should NOT be [Dc])
POSTULATE_WORDS = [
    "postulate", "assume", "assumption", "ansatz",
    "conjecture", "hypothesis", "propose", "proposed",
    "we take", "we set", "we choose", "we adopt",
    "phenomenologically", "by hand", "ad hoc",
]

# Words that indicate derivations (could be [Dc])
DERIVATION_WORDS = [
    "derive", "derivation", "derived",
    "follows from", "implies", "therefore",
    "we obtain", "we find", "we get",
    "emerges", "results in",
]

# Words that indicate identification (should be [I])
IDENTIFICATION_WORDS = [
    "identify", "identification", "identified",
    "matches", "corresponds to", "maps to",
    "recognize", "interpret as",
]

# ==============================================================================
# Checker
# ==============================================================================

@dataclass
class TagInconsistency:
    """A detected tag inconsistency."""
    file: str
    line_num: int
    current_tag: str
    suggested_tag: str
    reason: str
    context: str

def find_tags_in_line(line: str) -> List[str]:
    """Find all epistemic tags in a line."""
    tags = []
    for pattern in TAG_PATTERNS:
        matches = re.findall(pattern, line)
        tags.extend(matches)
    return tags

def check_line_consistency(line: str, line_num: int, filepath: Path) -> List[TagInconsistency]:
    """Check a single line for tag consistency."""
    inconsistencies = []

    line_lower = line.lower()
    tags_in_line = find_tags_in_line(line)

    # Check for [Dc] near postulate words
    if "Dc" in tags_in_line or "[Dc]" in line:
        for word in POSTULATE_WORDS:
            if word in line_lower:
                inconsistencies.append(TagInconsistency(
                    file=str(filepath.relative_to(PAPER_DIR)),
                    line_num=line_num,
                    current_tag="[Dc]",
                    suggested_tag="[P]",
                    reason=f"[Dc] used with postulate word '{word}'",
                    context=line.strip()[:80]
                ))
                break

    # Check for [Dc] near identification words (might need [I])
    if "Dc" in tags_in_line or "[Dc]" in line:
        for word in IDENTIFICATION_WORDS:
            if word in line_lower and "derive" not in line_lower:
                inconsistencies.append(TagInconsistency(
                    file=str(filepath.relative_to(PAPER_DIR)),
                    line_num=line_num,
                    current_tag="[Dc]",
                    suggested_tag="[I]",
                    reason=f"[Dc] used with identification word '{word}' (may need [I])",
                    context=line.strip()[:80]
                ))
                break

    # Check for derivation claims without any tag
    has_any_tag = any(re.search(p, line) for p in TAG_PATTERNS)
    if not has_any_tag:
        for word in DERIVATION_WORDS:
            if word in line_lower and "%" not in line[:50]:  # Not in comment
                # Only flag if it looks like a claim, not just discussion
                if any(claim in line_lower for claim in ["we derive", "is derived", "derivation of"]):
                    inconsistencies.append(TagInconsistency(
                        file=str(filepath.relative_to(PAPER_DIR)),
                        line_num=line_num,
                        current_tag="(none)",
                        suggested_tag="[Dc] or [P]",
                        reason=f"Derivation claim '{word}' without epistemic tag",
                        context=line.strip()[:80]
                    ))
                    break

    return inconsistencies

def scan_file(filepath: Path) -> List[TagInconsistency]:
    """Scan a single LaTeX file for tag inconsistencies."""
    inconsistencies = []

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"  Warning: Could not read {filepath}: {e}")
        return []

    for i, line in enumerate(lines):
        line_num = i + 1
        issues = check_line_consistency(line, line_num, filepath)
        inconsistencies.extend(issues)

    return inconsistencies

def scan_all_files() -> List[TagInconsistency]:
    """Scan all LaTeX files."""
    all_inconsistencies = []

    print("Scanning LaTeX files for tag inconsistencies...")
    print()

    # Scan sections directory
    if SECTIONS_DIR.exists():
        for tex_file in SECTIONS_DIR.glob("*.tex"):
            print(f"  Scanning: {tex_file.name}")
            issues = scan_file(tex_file)
            all_inconsistencies.extend(issues)

    # Scan main document
    main_tex = PAPER_DIR / "EDC_Part_II_Weak_Sector.tex"
    if main_tex.exists():
        print(f"  Scanning: {main_tex.name}")
        issues = scan_file(main_tex)
        all_inconsistencies.extend(issues)

    return all_inconsistencies

# ==============================================================================
# Summary Statistics
# ==============================================================================

def count_tags_in_file(filepath: Path) -> Dict[str, int]:
    """Count occurrences of each tag in a file."""
    counts = {tag: 0 for tag in VALID_TAGS}

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except:
        return counts

    for tag in VALID_TAGS:
        # Count both bracket form and macro form
        bracket_count = content.count(tag)
        tag_name = tag[1:-1]  # Remove brackets
        macro_count = content.count(f"\\tag{tag_name}")
        counts[tag] = bracket_count + macro_count

    return counts

def summarize_tags() -> Dict[str, int]:
    """Summarize tag usage across all files."""
    total_counts = {tag: 0 for tag in VALID_TAGS}

    if SECTIONS_DIR.exists():
        for tex_file in SECTIONS_DIR.glob("*.tex"):
            counts = count_tags_in_file(tex_file)
            for tag, count in counts.items():
                total_counts[tag] += count

    main_tex = PAPER_DIR / "EDC_Part_II_Weak_Sector.tex"
    if main_tex.exists():
        counts = count_tags_in_file(main_tex)
        for tag, count in counts.items():
            total_counts[tag] += count

    return total_counts

# ==============================================================================
# Main
# ==============================================================================

def main():
    print("=" * 70)
    print("EDC EPISTEMIC TAG CONSISTENCY CHECKER")
    print("=" * 70)
    print()

    # Tag usage summary
    print("Tag Usage Summary:")
    print("-" * 40)
    tag_counts = summarize_tags()
    for tag, count in sorted(tag_counts.items(), key=lambda x: -x[1]):
        if count > 0:
            print(f"  {tag:8} : {count:4} occurrences")
    print()

    # Run consistency scan
    inconsistencies = scan_all_files()

    # Report
    print()
    print("-" * 70)
    print("TAG INCONSISTENCIES FOUND")
    print("-" * 70)
    print()

    if inconsistencies:
        # Group by type
        dc_to_p = [i for i in inconsistencies if i.suggested_tag == "[P]"]
        dc_to_i = [i for i in inconsistencies if i.suggested_tag == "[I]"]
        untagged = [i for i in inconsistencies if i.current_tag == "(none)"]

        if dc_to_p:
            print(f"[Dc] → [P] (postulate words with derivation tag): {len(dc_to_p)}")
            for i in dc_to_p[:5]:  # Show first 5
                print(f"  {i.file}:{i.line_num} - {i.reason}")
                print(f"    Context: {i.context}")
            if len(dc_to_p) > 5:
                print(f"  ... and {len(dc_to_p) - 5} more")
            print()

        if dc_to_i:
            print(f"[Dc] → [I] (identification words with derivation tag): {len(dc_to_i)}")
            for i in dc_to_i[:5]:
                print(f"  {i.file}:{i.line_num} - {i.reason}")
                print(f"    Context: {i.context}")
            if len(dc_to_i) > 5:
                print(f"  ... and {len(dc_to_i) - 5} more")
            print()

        if untagged:
            print(f"Untagged derivation claims: {len(untagged)}")
            for i in untagged[:5]:
                print(f"  {i.file}:{i.line_num} - {i.reason}")
                print(f"    Context: {i.context}")
            if len(untagged) > 5:
                print(f"  ... and {len(untagged) - 5} more")
            print()

        print(f"Total inconsistencies: {len(inconsistencies)}")
    else:
        print("No tag inconsistencies detected.")

    # Save results
    output_dir = PAPER_DIR / "generated"
    output_dir.mkdir(exist_ok=True)

    import json
    results = {
        "tag_counts": tag_counts,
        "inconsistencies": [
            {
                "file": i.file,
                "line": i.line_num,
                "current_tag": i.current_tag,
                "suggested_tag": i.suggested_tag,
                "reason": i.reason,
                "context": i.context
            }
            for i in inconsistencies
        ]
    }

    with open(output_dir / "tag_check_results.json", 'w') as f:
        json.dump(results, f, indent=2)

    print()
    print(f"Results saved to: {output_dir}/tag_check_results.json")

    return 0

if __name__ == "__main__":
    sys.exit(main())
