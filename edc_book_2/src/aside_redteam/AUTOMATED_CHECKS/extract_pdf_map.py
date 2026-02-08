#!/usr/bin/env python3
"""
extract_pdf_map.py — Red Team Forensic Tool
Extracts page→section map and keyphrase index from PDF.

Note: Requires PyMuPDF (fitz) for PDF parsing.
If not available, falls back to TOC parsing from .toc file.
"""

import re
import os
from pathlib import Path
from collections import defaultdict

# Key phrases to index (plain strings, not regex)
KEY_PHRASES = [
    "Z6", "Z_6", "mathbb{Z}_6",
    "frozen", "frozen regime",
    "Steiner", "Y-junction",
    "projection operator",
    "Weinberg", "theta_W",
    "proton", "neutron",
    "generation", "N_g",
    "coupling",
    "hexagonal", "lattice",
    "topolog",
    "PDG", "CODATA", "baseline",
]

def parse_toc_file(toc_path):
    """Parse LaTeX .toc file for section→page mapping."""
    sections = []
    try:
        with open(toc_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        return [{"error": str(e)}]

    # Pattern: \contentsline {section/chapter}{Title}{Page}
    pattern = r'\\contentsline\s*\{(section|chapter|subsection)\}\{([^}]+)\}\{(\d+)\}'
    for match in re.finditer(pattern, content):
        level = match.group(1)
        title = match.group(2)
        page = int(match.group(3))

        # Clean up title (remove \numberline, math, etc.)
        title = re.sub(r'\\numberline\s*\{[^}]*\}', '', title)
        title = re.sub(r'\\\w+', '', title)  # Remove LaTeX commands
        title = re.sub(r'\{|\}', '', title)  # Remove braces
        title = title.strip()

        sections.append({
            'level': level,
            'title': title[:80],  # Truncate
            'page': page
        })

    return sections

def build_keyphrase_index(tex_files, src_dir):
    """Build keyphrase→file:line index from .tex files."""
    index = defaultdict(list)

    for tex_file in tex_files:
        try:
            with open(tex_file, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
        except:
            continue

        rel_path = str(tex_file.relative_to(src_dir))

        for i, line in enumerate(lines, 1):
            for phrase in KEY_PHRASES:
                if re.search(phrase, line, re.IGNORECASE):
                    index[phrase].append({
                        'file': rel_path,
                        'line': i,
                        'context': line.strip()[:60]
                    })

    return index

def main():
    src_dir = Path(__file__).parent.parent.parent
    output_dir = Path(__file__).parent.parent

    print("=" * 60)
    print("RED TEAM PDF/TOC MAP EXTRACTOR")
    print("=" * 60)

    # Find .toc file
    toc_files = list(src_dir.glob("*.toc"))
    sections = []

    if toc_files:
        print(f"\nParsing TOC: {toc_files[0].name}")
        sections = parse_toc_file(toc_files[0])
        print(f"  Found {len(sections)} sections")
    else:
        print("\nNo .toc file found. Skipping TOC extraction.")

    # Build keyphrase index from .tex files
    print("\nBuilding keyphrase index...")
    tex_files = [f for f in src_dir.rglob("*.tex") if "aside_redteam" not in str(f)]
    keyphrase_index = build_keyphrase_index(tex_files, src_dir)

    print(f"  Indexed {len(tex_files)} .tex files")
    for phrase in sorted(keyphrase_index.keys()):
        print(f"  {phrase}: {len(keyphrase_index[phrase])} occurrences")

    # Write TOC map
    toc_map_path = output_dir / "pdf_toc_map.md"
    with open(toc_map_path, 'w') as f:
        f.write("# PDF Table of Contents Map\n\n")

        if sections:
            f.write("| Page | Level | Title |\n")
            f.write("|------|-------|-------|\n")
            for sec in sections[:100]:  # Limit to 100
                if 'error' in sec:
                    f.write(f"| ERROR | - | {sec['error']} |\n")
                else:
                    f.write(f"| {sec['page']} | {sec['level']} | {sec['title'][:50]} |\n")
        else:
            f.write("*No TOC data available*\n")

    # Write keyphrase index
    keyphrase_path = output_dir / "keyphrase_index.md"
    with open(keyphrase_path, 'w') as f:
        f.write("# Keyphrase Index\n\n")
        f.write("Key terms indexed across source files.\n\n")

        for phrase in sorted(keyphrase_index.keys()):
            occurrences = keyphrase_index[phrase]
            f.write(f"## `{phrase}` ({len(occurrences)} occurrences)\n\n")

            # Group by file
            by_file = defaultdict(list)
            for occ in occurrences:
                by_file[occ['file']].append(occ)

            for filepath, occs in sorted(by_file.items())[:10]:  # Limit files
                f.write(f"**{filepath}:**\n")
                for occ in occs[:5]:  # Limit lines per file
                    f.write(f"- L{occ['line']}: `{occ['context'][:50]}...`\n")
                if len(occs) > 5:
                    f.write(f"- *... and {len(occs) - 5} more*\n")
                f.write("\n")

    print(f"\n[DONE] TOC map: {toc_map_path}")
    print(f"[DONE] Keyphrase index: {keyphrase_path}")

if __name__ == "__main__":
    main()
