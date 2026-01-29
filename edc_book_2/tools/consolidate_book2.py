#!/usr/bin/env python3
"""
Book 2 Consolidation Audit & Patch Tool
========================================
Scans the entire Book 2 LaTeX tree for consistency issues and applies
conservative, logged patches.

Categories:
A) Unit conventions (ambiguous δ, mixed units)
B) Notation drift (m_p vs mp, g_5 vs g5, etc.)
C) Epistemic tag hygiene
D) Stoplight verdict presence
E) Duplication (overlap integral, δ explanations, gate definitions)
F) LaTeX hygiene (labels, macros, multiply-defined)

Output:
- BOOK2_CONSOLIDATION_AUDIT.md
- BOOK2_CONSOLIDATION_PATCHLOG.md
- BOOK2_CANON_RULES.md
"""

import os
import re
import json
import hashlib
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Set, Tuple, Optional
from datetime import datetime

# Configuration
REPO_ROOT = Path(__file__).parent.parent.parent
BOOK2_ROOT = REPO_ROOT / "edc_book_2"
BOOK2_SRC = BOOK2_ROOT / "src"
EDC_PAPERS = REPO_ROOT / "edc_papers"
DOCS_DIR = BOOK2_ROOT / "docs"

@dataclass
class Issue:
    category: str
    subcategory: str
    file: str
    line: int
    context: str
    description: str
    severity: str  # LOW, MED, HIGH
    suggested_fix: str = ""

@dataclass
class Patch:
    file: str
    line: int
    old_text: str
    new_text: str
    reason: str
    risk: str  # LOW, MED, HIGH
    applied: bool = False

@dataclass
class AuditResults:
    issues: List[Issue] = field(default_factory=list)
    patches: List[Patch] = field(default_factory=list)
    files_scanned: Set[str] = field(default_factory=set)
    include_graph: Dict[str, List[str]] = field(default_factory=dict)

# ============================================================================
# PATTERN DEFINITIONS
# ============================================================================

# Unit convention patterns
UNIT_PATTERNS = {
    "ambiguous_delta_no_hbar": re.compile(
        r'\\delta\s*[=~]\s*[12]/\s*\(?2?\s*m_?[pP]\)?(?!.*\\hbar)',
        re.IGNORECASE
    ),
    "delta_without_subscript_mixed_context": re.compile(
        r'(?<!_)\\delta(?!_)(?!\\text)(?!\\mathrm)',
    ),
    "mixed_fm_gev": re.compile(
        r'(?:fm.*GeV\^?\{?-1\}?|GeV\^?\{?-1\}?.*fm)',
        re.IGNORECASE
    ),
}

# Notation drift patterns
NOTATION_PATTERNS = {
    "mp_inconsistent": [
        (re.compile(r'(?<![_\\])mp(?![_a-zA-Z])'), r'm_p'),  # mp -> m_p
        (re.compile(r'M_[pP](?!lanck)'), r'm_p'),  # M_p -> m_p (except Planck)
    ],
    "g5_inconsistent": [
        (re.compile(r'g5(?!\^)(?!_)'), r'g_5'),  # g5 -> g_5
        (re.compile(r'g_\{5\}'), r'g_5'),  # g_{5} -> g_5 (simpler)
    ],
    "I4_inconsistent": [
        (re.compile(r'I4(?!_)'), r'I_4'),  # I4 -> I_4
        (re.compile(r'I_\{4\}'), r'I_4'),  # I_{4} -> I_4
    ],
}

# Epistemic tag patterns
EPISTEMIC_TAGS = ['[Der]', '[Dc]', '[I]', '[P]', '[Cal]', '[BL]']
TAG_PATTERN = re.compile(r'\[(Der|Dc|I|P|Cal|BL)\]')
TAG_MACRO_PATTERN = re.compile(r'\\tag(Der|Dc|I|P|Cal|BL)\{\}')

# Duplication patterns (phrases that should be single-source)
DUPLICATION_PATTERNS = {
    "overlap_integral_def": re.compile(
        r'overlap\s+integral.*(?:measures|defined|definition)',
        re.IGNORECASE
    ),
    "delta_scale_explanation": re.compile(
        r'\\delta.*(?:nucl|EW|thickness|scale).*(?:Compton|brane|fm)',
        re.IGNORECASE
    ),
    "kchannel_averaging": re.compile(
        r'k.*channel.*(?:averaging|correction|factor)',
        re.IGNORECASE
    ),
}

# Stoplight verdict detection
STOPLIGHT_PATTERN = re.compile(
    r'(?:Stoplight|stoplight).*(?:Verdict|verdict|Status|status)',
    re.IGNORECASE
)

# Label patterns
LABEL_PATTERN = re.compile(r'\\label\{([^}]+)\}')
REF_PATTERN = re.compile(r'\\(?:ref|eqref|autoref|cref)\{([^}]+)\}')

# Include patterns
INCLUDE_PATTERN = re.compile(r'\\(?:input|include|subfile)\{([^}]+)\}')

# ============================================================================
# SCANNING FUNCTIONS
# ============================================================================

def parse_include_tree(main_tex: Path) -> Dict[str, List[str]]:
    """Parse the full include tree starting from main.tex."""
    graph = {}
    visited = set()

    def resolve_path(include_path: str, from_file: Path) -> Optional[Path]:
        """Resolve an include path relative to the including file."""
        # Handle \EDCPAPERS macro
        if '\\EDCPAPERS' in include_path:
            include_path = include_path.replace('\\EDCPAPERS', '../../edc_papers')

        # Add .tex extension if missing
        if not include_path.endswith('.tex'):
            include_path += '.tex'

        # Try relative to from_file's directory
        candidate = from_file.parent / include_path
        if candidate.exists():
            return candidate.resolve()

        # Try relative to BOOK2_SRC
        candidate = BOOK2_SRC / include_path
        if candidate.exists():
            return candidate.resolve()

        # Try relative to repo root
        candidate = REPO_ROOT / include_path
        if candidate.exists():
            return candidate.resolve()

        return None

    def scan_file(file_path: Path):
        if file_path in visited or not file_path.exists():
            return
        visited.add(file_path)

        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            return

        includes = []
        for match in INCLUDE_PATTERN.finditer(content):
            inc_path = match.group(1)
            resolved = resolve_path(inc_path, file_path)
            if resolved:
                includes.append(str(resolved))
                scan_file(resolved)

        graph[str(file_path)] = includes

    scan_file(main_tex)
    return graph

def scan_file_for_issues(file_path: Path, results: AuditResults):
    """Scan a single file for all issue categories."""
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
        lines = content.split('\n')
    except Exception as e:
        results.issues.append(Issue(
            category="ERROR",
            subcategory="read_error",
            file=str(file_path),
            line=0,
            context="",
            description=f"Could not read file: {e}",
            severity="HIGH"
        ))
        return

    results.files_scanned.add(str(file_path))
    rel_path = str(file_path.relative_to(REPO_ROOT) if REPO_ROOT in file_path.parents else file_path)

    # Track labels in this file
    labels_in_file = []

    for line_num, line in enumerate(lines, 1):
        # Skip comments
        if line.strip().startswith('%'):
            continue

        # A) Unit conventions
        if 'delta' in line.lower() or '\\delta' in line:
            # Check for ambiguous δ without ℏ context
            if re.search(r'\\delta\s*[=~≈]', line):
                if 'hbar' not in line.lower() and 'ℏ' not in line:
                    # Check if natural units declared nearby
                    context_start = max(0, line_num - 10)
                    context_lines = '\n'.join(lines[context_start:line_num])
                    if 'natural units' not in context_lines.lower() and 'hbar=c=1' not in context_lines.lower():
                        results.issues.append(Issue(
                            category="A_UNITS",
                            subcategory="ambiguous_delta",
                            file=rel_path,
                            line=line_num,
                            context=line.strip()[:80],
                            description="δ definition without explicit ℏ or natural units declaration",
                            severity="MED",
                            suggested_fix="Add ℏ=c=1 note or explicit ℏ/(2m_p c)"
                        ))

        # B) Notation drift
        for pattern_name, replacements in NOTATION_PATTERNS.items():
            for pattern, replacement in replacements:
                if pattern.search(line):
                    results.issues.append(Issue(
                        category="B_NOTATION",
                        subcategory=pattern_name,
                        file=rel_path,
                        line=line_num,
                        context=line.strip()[:80],
                        description=f"Notation inconsistency: should use {replacement}",
                        severity="LOW",
                        suggested_fix=f"Replace with {replacement}"
                    ))

        # C) Epistemic tags - check for claims without tags
        claim_words = ['derive', 'show', 'prove', 'establish', 'yields', 'gives']
        if any(word in line.lower() for word in claim_words):
            if not TAG_PATTERN.search(line) and not TAG_MACRO_PATTERN.search(line):
                # Check nearby lines
                context_range = lines[max(0, line_num-3):min(len(lines), line_num+3)]
                context_text = '\n'.join(context_range)
                if not TAG_PATTERN.search(context_text) and not TAG_MACRO_PATTERN.search(context_text):
                    results.issues.append(Issue(
                        category="C_EPISTEMIC",
                        subcategory="missing_tag",
                        file=rel_path,
                        line=line_num,
                        context=line.strip()[:80],
                        description="Claim-like statement without epistemic tag nearby",
                        severity="LOW",
                        suggested_fix="Add appropriate epistemic tag [Der]/[Dc]/[I]/[P]/[Cal]"
                    ))

        # E) Duplication detection
        for dup_name, dup_pattern in DUPLICATION_PATTERNS.items():
            if dup_pattern.search(line):
                # Check if this is a reference to canon or the canon itself
                if '_shared/' not in rel_path and 'canon' not in line.lower():
                    results.issues.append(Issue(
                        category="E_DUPLICATION",
                        subcategory=dup_name,
                        file=rel_path,
                        line=line_num,
                        context=line.strip()[:80],
                        description=f"Potential duplicate of canon content ({dup_name})",
                        severity="MED",
                        suggested_fix="Consider replacing with \\input to shared canon"
                    ))

        # F) LaTeX hygiene - labels
        for match in LABEL_PATTERN.finditer(line):
            label = match.group(1)
            labels_in_file.append((label, line_num))

            # Check for proper prefixing in include files
            if '.include' in rel_path and not label.startswith('DL:'):
                results.issues.append(Issue(
                    category="F_LATEX",
                    subcategory="label_prefix",
                    file=rel_path,
                    line=line_num,
                    context=f"\\label{{{label}}}",
                    description="Include file label should have DL: prefix",
                    severity="LOW",
                    suggested_fix=f"Use DL:<filename>:{label}"
                ))

    # D) Stoplight verdict - check at file level
    if any(kw in rel_path.lower() for kw in ['case_', 'ch1', 'ch2', 'opr']):
        if not STOPLIGHT_PATTERN.search(content):
            # Check if file makes claims
            if any(word in content.lower() for word in ['derive', 'gate', 'verdict', 'status']):
                results.issues.append(Issue(
                    category="D_STOPLIGHT",
                    subcategory="missing_verdict",
                    file=rel_path,
                    line=0,
                    context="(file-level)",
                    description="Chapter file appears to make claims but has no stoplight verdict",
                    severity="MED",
                    suggested_fix="Add stoplight verdict section"
                ))

def collect_all_labels(results: AuditResults) -> Dict[str, List[Tuple[str, int]]]:
    """Collect all labels across scanned files."""
    all_labels = {}

    for file_path in results.files_scanned:
        try:
            content = Path(file_path).read_text(encoding='utf-8', errors='ignore')
            for match in LABEL_PATTERN.finditer(content):
                label = match.group(1)
                if label not in all_labels:
                    all_labels[label] = []
                # Find line number
                pos = match.start()
                line_num = content[:pos].count('\n') + 1
                all_labels[label].append((file_path, line_num))
        except Exception:
            pass

    return all_labels

def check_multiply_defined_labels(results: AuditResults):
    """Check for multiply-defined labels."""
    all_labels = collect_all_labels(results)

    for label, locations in all_labels.items():
        if len(locations) > 1:
            loc_str = "; ".join([f"{Path(f).name}:{ln}" for f, ln in locations])
            results.issues.append(Issue(
                category="F_LATEX",
                subcategory="multiply_defined",
                file="(multiple)",
                line=0,
                context=f"\\label{{{label}}}",
                description=f"Label defined {len(locations)} times: {loc_str}",
                severity="HIGH",
                suggested_fix="Rename or prefix labels to avoid collision"
            ))

# ============================================================================
# PATCHING FUNCTIONS
# ============================================================================

def apply_notation_patches(results: AuditResults, dry_run: bool = True):
    """Apply safe notation normalization patches."""
    safe_replacements = [
        # Only very safe, unambiguous replacements
        (re.compile(r'(?<![a-zA-Z_\\])mp(?![a-zA-Z_])'), r'm_p'),
        (re.compile(r'(?<![a-zA-Z_\\])g5(?![a-zA-Z_])'), r'g_5'),
        (re.compile(r'(?<![a-zA-Z_\\])I4(?![a-zA-Z_])'), r'I_4'),
    ]

    for file_path in results.files_scanned:
        try:
            path = Path(file_path)
            content = path.read_text(encoding='utf-8', errors='ignore')
            original = content

            for pattern, replacement in safe_replacements:
                matches = list(pattern.finditer(content))
                for match in reversed(matches):  # Reverse to preserve positions
                    old = match.group(0)
                    new = pattern.sub(replacement, old)
                    if old != new:
                        # Find line number
                        line_num = content[:match.start()].count('\n') + 1
                        results.patches.append(Patch(
                            file=str(path.relative_to(REPO_ROOT)),
                            line=line_num,
                            old_text=old,
                            new_text=new,
                            reason="Notation normalization",
                            risk="LOW",
                            applied=not dry_run
                        ))
                        if not dry_run:
                            content = content[:match.start()] + new + content[match.end():]

            if not dry_run and content != original:
                path.write_text(content, encoding='utf-8')

        except Exception as e:
            results.issues.append(Issue(
                category="ERROR",
                subcategory="patch_error",
                file=file_path,
                line=0,
                context="",
                description=f"Error applying patches: {e}",
                severity="HIGH"
            ))

# ============================================================================
# REPORT GENERATION
# ============================================================================

def generate_audit_report(results: AuditResults) -> str:
    """Generate BOOK2_CONSOLIDATION_AUDIT.md"""
    report = []
    report.append("# Book 2 Consolidation Audit Report")
    report.append(f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append(f"**Files scanned:** {len(results.files_scanned)}")
    report.append(f"**Total issues:** {len(results.issues)}")

    # Summary by category
    report.append("\n## Summary by Category\n")
    categories = {}
    for issue in results.issues:
        cat = issue.category
        if cat not in categories:
            categories[cat] = {'HIGH': 0, 'MED': 0, 'LOW': 0}
        categories[cat][issue.severity] += 1

    report.append("| Category | HIGH | MED | LOW | Total |")
    report.append("|----------|------|-----|-----|-------|")
    for cat in sorted(categories.keys()):
        counts = categories[cat]
        total = sum(counts.values())
        report.append(f"| {cat} | {counts['HIGH']} | {counts['MED']} | {counts['LOW']} | {total} |")

    # Detailed issues by category
    for cat in sorted(categories.keys()):
        cat_issues = [i for i in results.issues if i.category == cat]
        report.append(f"\n## {cat}\n")

        # Group by subcategory
        subcats = {}
        for issue in cat_issues:
            if issue.subcategory not in subcats:
                subcats[issue.subcategory] = []
            subcats[issue.subcategory].append(issue)

        for subcat, issues in sorted(subcats.items()):
            report.append(f"\n### {subcat} ({len(issues)} issues)\n")
            report.append("| Severity | File | Line | Context | Fix |")
            report.append("|----------|------|------|---------|-----|")
            for issue in issues[:50]:  # Limit to 50 per subcategory
                context = issue.context.replace('|', '\\|')[:60]
                fix = issue.suggested_fix.replace('|', '\\|')[:40]
                report.append(f"| {issue.severity} | {Path(issue.file).name} | {issue.line} | `{context}` | {fix} |")
            if len(issues) > 50:
                report.append(f"\n*... and {len(issues) - 50} more*")

    return '\n'.join(report)

def generate_patchlog(results: AuditResults) -> str:
    """Generate BOOK2_CONSOLIDATION_PATCHLOG.md"""
    report = []
    report.append("# Book 2 Consolidation Patchlog")
    report.append(f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append(f"**Total patches:** {len(results.patches)}")
    report.append(f"**Applied:** {sum(1 for p in results.patches if p.applied)}")

    report.append("\n## Patch Log\n")
    report.append("| Risk | File | Line | Old | New | Reason | Applied |")
    report.append("|------|------|------|-----|-----|--------|---------|")

    for patch in results.patches:
        old = patch.old_text.replace('|', '\\|')[:30]
        new = patch.new_text.replace('|', '\\|')[:30]
        applied = "YES" if patch.applied else "NO"
        report.append(f"| {patch.risk} | {Path(patch.file).name} | {patch.line} | `{old}` | `{new}` | {patch.reason} | {applied} |")

    return '\n'.join(report)

def generate_canon_rules() -> str:
    """Generate BOOK2_CANON_RULES.md"""
    return """# Book 2 Canon Rules

**Generated:** {date}

## Unit Conventions

### Natural Units Declaration
When using natural units (ℏ = c = 1), this must be explicitly stated near the first usage.
Preferred: Include a note like "In this chapter, we use natural units where ℏ = c = 1."

### δ Scale Convention
| Context | Symbol | Definition | Value |
|---------|--------|------------|-------|
| Nuclear/nucleon chapters | δ, δ_nucl | ℏ/(2m_p c) | 0.105 fm |
| Electroweak BVP chapters | δ_EW | ℏc/M_Z | ~0.002 fm |

**Rule:** Never use bare δ when both scales appear. Use subscript or declare context.

### Mixed Unit Expressions
When mixing fm and GeV^-1:
- Always provide conversion: 1 fm ≈ 5.068 GeV^-1
- Or work entirely in one system within a derivation

## Notation Standards

| Correct | Incorrect | Notes |
|---------|-----------|-------|
| m_p | mp, M_p | Proton mass (lowercase subscript) |
| g_5 | g5, g_{5} | 5D coupling |
| I_4 | I4, I_{4} | Overlap integral |
| \\psi_L, \\psi_R | psi_L | Use backslash for Greek |
| G_F | GF, g_F | Fermi constant |

## Epistemic Tags

| Tag | Meaning | When to Use |
|-----|---------|-------------|
| [Der] | Derived | Explicit derivation from postulates exists |
| [Dc] | Derived Conditional | Derived IF certain assumptions hold |
| [I] | Identified | Pattern matching (not unique) |
| [P] | Proposed | Postulate/hypothesis |
| [Cal] | Calibrated | Parameter fitted to data |
| [BL] | Baseline | External reference (PDG/CODATA) |

**Rule:** Every claim in a Stoplight Verdict must have an epistemic tag.

## Label Prefixes

| File Type | Prefix Pattern | Example |
|-----------|----------------|---------|
| Main chapters | sec:, eq:, fig:, tab: | sec:gf_derivation |
| Include files (.include.tex) | DL:<filename>: | DL:delta_from_5d:eq:main |
| Shared boxes | box: | box:scale-disambiguation |

## Canon Files (Single Source of Truth)

| Concept | File | Label |
|---------|------|-------|
| Scale disambiguation | _shared/scale_disambiguation_box.tex | box:scale-disambiguation |
| Overlap integral I_4 | _shared/overlap_integral_canon.tex | box:overlap-integral-canon |
| Stoplight template | _shared/stoplight_stub.tex | (template) |
| Gate registry | sections/12_epistemic_map.tex | sec:gate_registry |

**Rule:** Do not duplicate these definitions. Use \\input or \\ref.

## k-channel Applicability

The k-channel correction k(N) = 1 + 1/N applies ONLY to:
- Averaging observables over discrete vs continuous distributions
- Spin-chain cross-validated contexts

It does NOT apply to:
- Overlap integrals
- Cardinality ratios
- Arbitrary multiplication

""".replace('{date}', datetime.now().strftime('%Y-%m-%d'))

# ============================================================================
# MAIN
# ============================================================================

def main():
    print("Book 2 Consolidation Audit Tool")
    print("=" * 50)

    results = AuditResults()

    # Step 1: Parse include tree
    print("\n[1/5] Parsing include tree...")
    main_tex = BOOK2_SRC / "main.tex"
    if not main_tex.exists():
        main_tex = BOOK2_SRC / "EDC_Part_II_Weak_Sector_rebuild.tex"

    results.include_graph = parse_include_tree(main_tex)
    print(f"  Found {len(results.include_graph)} files in include tree")

    # Step 2: Scan all files
    print("\n[2/5] Scanning files for issues...")
    for file_path in results.include_graph.keys():
        scan_file_for_issues(Path(file_path), results)
    print(f"  Found {len(results.issues)} issues")

    # Step 3: Check for multiply-defined labels
    print("\n[3/5] Checking for multiply-defined labels...")
    check_multiply_defined_labels(results)

    # Step 4: Generate patches (dry run)
    print("\n[4/5] Generating patches (dry run)...")
    apply_notation_patches(results, dry_run=True)
    print(f"  Generated {len(results.patches)} patches")

    # Step 5: Generate reports
    print("\n[5/5] Generating reports...")

    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    audit_report = generate_audit_report(results)
    (DOCS_DIR / "BOOK2_CONSOLIDATION_AUDIT.md").write_text(audit_report)
    print(f"  Wrote BOOK2_CONSOLIDATION_AUDIT.md")

    patchlog = generate_patchlog(results)
    (DOCS_DIR / "BOOK2_CONSOLIDATION_PATCHLOG.md").write_text(patchlog)
    print(f"  Wrote BOOK2_CONSOLIDATION_PATCHLOG.md")

    canon_rules = generate_canon_rules()
    (DOCS_DIR / "BOOK2_CANON_RULES.md").write_text(canon_rules)
    print(f"  Wrote BOOK2_CANON_RULES.md")

    # Summary
    print("\n" + "=" * 50)
    print("AUDIT COMPLETE")
    print(f"  Files scanned: {len(results.files_scanned)}")
    print(f"  Issues found: {len(results.issues)}")
    print(f"  Patches suggested: {len(results.patches)}")

    # Category breakdown
    cats = {}
    for i in results.issues:
        cats[i.category] = cats.get(i.category, 0) + 1
    print("\nIssues by category:")
    for cat, count in sorted(cats.items()):
        print(f"  {cat}: {count}")

    return results

if __name__ == "__main__":
    main()
