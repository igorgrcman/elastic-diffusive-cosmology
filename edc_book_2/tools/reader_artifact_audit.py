#!/usr/bin/env python3
"""
Reader-Facing Artifact Audit Tool
==================================
Scans Book2 sources for reader-facing repository artifacts (.md references,
raw repo paths) that should be internalized or footnoted.

PASS criteria:
- No raw .md references outside of \footnote{Repository artifact: ...}
- No raw repo paths (docs/, edc_papers/, aside_*) in prose

ALLOWED exceptions:
- Inside \footnote{Repository artifact: ...}
- Inside % LaTeX comments
- Inside meta_part2/ files (explicitly meta-documentation)
- Inside verbatim/lstlisting environments

Usage:
    python tools/reader_artifact_audit.py [--fix-mode]

Exit codes:
    0 = PASS (no issues found)
    1 = FAIL (issues found)
"""

import os
import re
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import List, Tuple, Optional

# Configuration
REPO_ROOT = Path(__file__).parent.parent.parent
BOOK2_ROOT = REPO_ROOT / "edc_book_2"
EDC_PAPERS = REPO_ROOT / "edc_papers"

# Scan targets
SCAN_TARGETS = [
    BOOK2_ROOT / "src",
    EDC_PAPERS / "_shared" / "derivations",
    EDC_PAPERS / "_shared" / "lemmas",
    EDC_PAPERS / "_shared" / "boxes",
]

# Patterns for reader-facing artifacts
ARTIFACT_PATTERNS = [
    # .md file references (not in footnote)
    (re.compile(r'(?<!Repository artifact: )\\texttt\{[^}]*\.md\}'), ".md reference"),
    (re.compile(r'(?<!Repository artifact: )\{[^}]*\.md[^}]*\}'), ".md in braces"),
    # Raw repo paths
    (re.compile(r'\\texttt\{(?:docs|edc_papers|aside_)[^}]+\}'), "Raw repo path"),
    (re.compile(r'(?<!footnote\{Repository artifact: )docs/[A-Z][A-Z_]+\.md'), "docs/*.md path"),
    (re.compile(r'aside_[a-z_]+/'), "aside_* folder reference"),
]

# Allowed contexts (lines containing these are skipped)
ALLOWED_CONTEXTS = [
    re.compile(r'^%'),              # LaTeX comment
    re.compile(r'\\footnote\{Repository artifact:'),  # Proper footnote
    re.compile(r'\\footnotemark'),  # Footnote mark (table context)
    re.compile(r'\\footnotetext\{Repository artifact'),  # Footnote text
    re.compile(r'% COMPANION:'),    # Header comment
    re.compile(r'% Anchor:'),       # Header comment
]

# Files/directories to skip entirely
SKIP_PATTERNS = [
    'meta_part2/',      # Meta documentation - .md refs are appropriate
    'XX_teaser',        # Teaser content
    '.include.tex',     # Generated files (fix standalone instead)
]

@dataclass
class Issue:
    file: str
    line: int
    pattern: str
    content: str

def should_skip_file(filepath: str) -> bool:
    """Check if file should be skipped entirely."""
    for pattern in SKIP_PATTERNS:
        if pattern in filepath:
            return True
    return False

def is_allowed_context(line: str) -> bool:
    """Check if line is in an allowed context."""
    stripped = line.strip()
    for pattern in ALLOWED_CONTEXTS:
        if pattern.search(stripped):
            return True
    return False

def scan_file(filepath: Path) -> List[Issue]:
    """Scan a single file for reader-facing artifacts."""
    issues = []
    rel_path = str(filepath.relative_to(REPO_ROOT))

    if should_skip_file(rel_path):
        return []

    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
        lines = content.split('\n')
    except Exception:
        return []

    # Track if we're in a verbatim/lstlisting environment
    in_verbatim = False

    for line_num, line in enumerate(lines, 1):
        # Skip verbatim environments
        if r'\begin{verbatim}' in line or r'\begin{lstlisting}' in line:
            in_verbatim = True
            continue
        if r'\end{verbatim}' in line or r'\end{lstlisting}' in line:
            in_verbatim = False
            continue
        if in_verbatim:
            continue

        # Skip allowed contexts
        if is_allowed_context(line):
            continue

        # Check artifact patterns
        for pattern, desc in ARTIFACT_PATTERNS:
            if pattern.search(line):
                # Double-check it's not in a footnote
                if 'Repository artifact' in line:
                    continue
                if r'\footnote{' in line and '.md' in line:
                    # Check if .md is inside the footnote
                    # Simple heuristic: if footnote comes before .md, likely OK
                    fn_pos = line.find(r'\footnote{')
                    md_pos = line.find('.md')
                    if fn_pos < md_pos:
                        continue

                issues.append(Issue(
                    file=rel_path,
                    line=line_num,
                    pattern=desc,
                    content=line.strip()[:80]
                ))
                break  # One issue per line is enough

    return issues

def main():
    print("Reader-Facing Artifact Audit")
    print("=" * 60)

    all_issues: List[Issue] = []
    files_scanned = 0

    for target_dir in SCAN_TARGETS:
        if not target_dir.exists():
            continue

        for tex_file in target_dir.rglob("*.tex"):
            files_scanned += 1
            issues = scan_file(tex_file)
            all_issues.extend(issues)

    print(f"\nFiles scanned: {files_scanned}")
    print(f"Issues found: {len(all_issues)}")

    if not all_issues:
        print("\n✓ PASS - No reader-facing artifacts found")
        return 0

    print("\n✗ FAIL - Reader-facing artifacts detected:\n")
    print(f"{'File':<50} {'Line':<6} {'Pattern':<25}")
    print("-" * 81)

    for issue in all_issues:
        print(f"{issue.file:<50} {issue.line:<6} {issue.pattern:<25}")
        print(f"  → {issue.content}")
        print()

    print("\nTo fix these issues:")
    print("1. Replace raw .md/repo paths with internal Book2 references, OR")
    print("2. Move to footnote: \\footnote{Repository artifact: \\texttt{path}}")

    return 1

if __name__ == "__main__":
    sys.exit(main())
