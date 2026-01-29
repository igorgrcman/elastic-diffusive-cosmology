#!/usr/bin/env python3
"""
Book 2 Full Cleanup Audit Tool
==============================
Comprehensive scan for artifacts, formatting issues, and hygiene problems.

Categories:
1) LLM/log remnants
2) Path/placeholder junk
3) Inconsistent δ usage
4) Tag hygiene
5) Label hygiene
6) Duplicated boilerplate
7) LaTeX style breakages
8) Typography artifacts

Output:
- BOOK2_FULL_CLEANUP_AUDIT.md
- BOOK2_FULL_CLEANUP_SUMMARY.md
- BOOK2_FULL_CLEANUP_PATCHLOG.md
"""

import os
import re
import json
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
    file: str
    line: int
    category: str
    subcategory: str
    snippet: str
    severity: str  # LOW, MED, HIGH
    autofixable: bool
    fix_description: str = ""

@dataclass
class Patch:
    file: str
    line: int
    old_text: str
    new_text: str
    category: str
    reason: str
    applied: bool = False

@dataclass
class AuditResults:
    issues: List[Issue] = field(default_factory=list)
    patches: List[Patch] = field(default_factory=list)
    files_scanned: Set[str] = field(default_factory=set)
    categories: Dict[str, int] = field(default_factory=dict)

# ============================================================================
# PATTERN DEFINITIONS
# ============================================================================

# Category 1: LLM/log remnants (very specific patterns to avoid false positives)
LLM_REMNANTS = [
    (re.compile(r'^\s*%*\s*END\s+OUTPUT\s*$', re.IGNORECASE | re.MULTILINE), "END OUTPUT marker", True),
    (re.compile(r'^\s*%*\s*Session\s+Summary\s*$', re.IGNORECASE | re.MULTILINE), "Session Summary", True),
    (re.compile(r'^\s*%*\s*Files\s+changed:\s*$', re.IGNORECASE | re.MULTILINE), "Files changed marker", True),
    (re.compile(r'PASS\s*\(\s*\d+\s*pages?\s*\)', re.IGNORECASE), "PASS (N pages) marker", True),
    (re.compile(r'^\s*Co-Authored-By:\s*Claude', re.MULTILINE), "Co-authored-by marker", True),
]

# Category 2: Path/placeholder junk
PATH_PATTERNS = [
    (re.compile(r'Full\s+derivation:\s*[<\["]?[\w/._-]+[>\]"]?', re.IGNORECASE), "Full derivation path"),
    (re.compile(r'/Users/\w+/'), "Absolute user path"),
    (re.compile(r'C:\\Users\\', re.IGNORECASE), "Windows path"),
    (re.compile(r'~\/[\w/._-]+'), "Home directory path"),
    (re.compile(r'\\input\{[^}]*edc_papers[^}]*\}(?!.*\\EDCPAPERS)'), "Raw edc_papers path (should use \\EDCPAPERS)"),
]

# Category 3: δ usage patterns
DELTA_PATTERNS = [
    (re.compile(r'(?<!_)\\delta(?!_)(?!\s*=\s*\d+°)(?!\\text)(?!\\mathrm)'), "bare_delta"),
]

# Category 4: Tag hygiene
TAG_PATTERNS = [
    (re.compile(r'\[Der\](?!\s*})'), "literal_Der_tag"),
    (re.compile(r'\[Dc\](?!\s*})'), "literal_Dc_tag"),
    (re.compile(r'\[I\](?!\s*})'), "literal_I_tag"),
    (re.compile(r'\[P\](?!\s*})'), "literal_P_tag"),
    (re.compile(r'\[Cal\](?!\s*})'), "literal_Cal_tag"),
    (re.compile(r'\[BL\](?!\s*})'), "literal_BL_tag"),
]

# Category 5: Label patterns
LABEL_PATTERN = re.compile(r'\\label\{([^}]+)\}')

# Category 7: LaTeX style breakages
LATEX_ISSUES = [
    (re.compile(r'[^\\]\{[^}]*$', re.MULTILINE), "unmatched_open_brace"),
    (re.compile(r'^[^%]*\}[^{]*$', re.MULTILINE), "potential_unmatched_close"),
    (re.compile(r'\\begin\{verbatim\}.*\\end\{verbatim\}', re.DOTALL), "verbatim_block"),
]

# Category 8: Typography artifacts (conservative - only in prose, not indentation)
TYPO_PATTERNS = [
    # Only match double space after a word (not at line start/indentation)
    (re.compile(r'(?<=[a-zA-Z,.;:!?])  (?=[a-zA-Z])'), "double_space_in_prose"),
    (re.compile(r'(?<=[a-zA-Z]) ,'), "space_before_comma"),
    (re.compile(r'(?<=[a-zA-Z])\.\.(?!\.)'), "double_period"),
    (re.compile(r'\?\?'), "double_question"),
]

# ============================================================================
# INCLUDE GRAPH PARSING
# ============================================================================

INCLUDE_PATTERN = re.compile(r'\\(?:input|include|subfile)\{([^}]+)\}')

def parse_include_tree(main_tex: Path) -> Set[str]:
    """Parse the full include tree starting from main.tex."""
    visited = set()

    def resolve_path(include_path: str, from_file: Path) -> Optional[Path]:
        """Resolve an include path relative to the including file."""
        original = include_path

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

        for match in INCLUDE_PATTERN.finditer(content):
            inc_path = match.group(1)
            resolved = resolve_path(inc_path, file_path)
            if resolved:
                scan_file(resolved)

    scan_file(main_tex)
    return {str(p) for p in visited}

# ============================================================================
# SCANNING FUNCTIONS
# ============================================================================

def scan_file(file_path: Path, results: AuditResults, delta_context: Dict[str, bool]):
    """Scan a single file for all issue categories."""
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
        lines = content.split('\n')
    except Exception as e:
        return

    results.files_scanned.add(str(file_path))
    rel_path = str(file_path.relative_to(REPO_ROOT) if REPO_ROOT in file_path.parents else file_path)

    # Track which δ variants appear in this file
    has_delta_nucl = bool(re.search(r'\\delta_\{?(?:nucl|\\text\{nucl\})', content))
    has_delta_ew = bool(re.search(r'\\delta_\{?(?:EW|\\text\{EW\})', content))
    has_cp_delta = bool(re.search(r'\\delta\s*=\s*\d+°|CP.*\\delta|\\delta.*CP', content, re.IGNORECASE))

    for line_num, line in enumerate(lines, 1):
        # Skip pure comment lines for most checks
        stripped = line.strip()
        is_comment = stripped.startswith('%')

        # Category 1: LLM remnants (check even in comments - they shouldn't be there)
        for pattern, desc, can_autofix in LLM_REMNANTS:
            if pattern.search(line):
                # Skip if it's in a legitimate context (e.g., quoted, in verbatim)
                if 'verbatim' not in content[max(0, content.find(line)-100):content.find(line)].lower():
                    results.issues.append(Issue(
                        file=rel_path,
                        line=line_num,
                        category="1_LLM_REMNANTS",
                        subcategory=desc,
                        snippet=line.strip()[:80],
                        severity="MED",
                        autofixable=can_autofix and not is_comment,
                        fix_description="Remove LLM/log artifact line"
                    ))
                    results.categories["1_LLM_REMNANTS"] = results.categories.get("1_LLM_REMNANTS", 0) + 1

        if is_comment:
            continue  # Skip remaining checks for comments

        # Category 2: Path/placeholder junk
        for pattern, desc in PATH_PATTERNS:
            match = pattern.search(line)
            if match:
                results.issues.append(Issue(
                    file=rel_path,
                    line=line_num,
                    category="2_PATH_JUNK",
                    subcategory=desc,
                    snippet=line.strip()[:80],
                    severity="MED",
                    autofixable="edc_papers" in desc.lower(),  # Can fix path macro issues
                    fix_description="Replace with proper reference or \\EDCPAPERS macro"
                ))
                results.categories["2_PATH_JUNK"] = results.categories.get("2_PATH_JUNK", 0) + 1

        # Category 3: δ usage (only flag if both scales appear)
        if has_delta_nucl and has_delta_ew and not has_cp_delta:
            for pattern, desc in DELTA_PATTERNS:
                if pattern.search(line):
                    # Check if there's a disambiguation nearby
                    context_start = max(0, line_num - 5)
                    context_end = min(len(lines), line_num + 5)
                    context = '\n'.join(lines[context_start:context_end])
                    if 'disambiguation' not in context.lower() and 'scale' not in context.lower():
                        results.issues.append(Issue(
                            file=rel_path,
                            line=line_num,
                            category="3_DELTA_USAGE",
                            subcategory=desc,
                            snippet=line.strip()[:80],
                            severity="LOW",
                            autofixable=False,  # Needs manual review
                            fix_description="Add subscript or reference scale_disambiguation_box"
                        ))
                        results.categories["3_DELTA_USAGE"] = results.categories.get("3_DELTA_USAGE", 0) + 1

        # Category 4: Tag hygiene - check for literal tags where macros should be used
        # Only flag if file predominantly uses \tag macros (>50% macro usage)
        macro_count = len(re.findall(r'\\tag(?:Der|Dc|I|P|Cal|BL)\{', content))
        literal_count = len(re.findall(r'\[(Der|Dc|I|P|Cal|BL)\]', content))
        if macro_count > literal_count and literal_count > 0:
            for pattern, desc in TAG_PATTERNS:
                if pattern.search(line):
                    results.issues.append(Issue(
                        file=rel_path,
                        line=line_num,
                        category="4_TAG_HYGIENE",
                        subcategory=desc,
                        snippet=line.strip()[:80],
                        severity="LOW",
                        autofixable=False,  # Don't auto-convert - manual review
                        fix_description="Consider converting to \\tagXxx{} macro"
                    ))
                    results.categories["4_TAG_HYGIENE"] = results.categories.get("4_TAG_HYGIENE", 0) + 1

        # Category 5: Label hygiene for include files
        if '.include' in rel_path:
            for match in LABEL_PATTERN.finditer(line):
                label = match.group(1)
                if not label.startswith('DL:'):
                    results.issues.append(Issue(
                        file=rel_path,
                        line=line_num,
                        category="5_LABEL_HYGIENE",
                        subcategory="missing_DL_prefix",
                        snippet=f"\\label{{{label}}}",
                        severity="MED",
                        autofixable=False,  # Needs careful renaming
                        fix_description="Add DL:<filename>: prefix"
                    ))
                    results.categories["5_LABEL_HYGIENE"] = results.categories.get("5_LABEL_HYGIENE", 0) + 1

        # Category 8: Typography artifacts
        for pattern, desc in TYPO_PATTERNS:
            matches = list(pattern.finditer(line))
            for match in matches:
                # Skip if inside math mode or command
                pos = match.start()
                before = line[:pos]
                # Simple heuristic: skip if odd number of $ before
                if before.count('$') % 2 == 1:
                    continue
                # Skip if inside a command argument
                if '\\' in before[-10:] and '{' in before[-10:]:
                    continue

                results.issues.append(Issue(
                    file=rel_path,
                    line=line_num,
                    category="8_TYPOGRAPHY",
                    subcategory=desc,
                    snippet=line.strip()[:80],
                    severity="LOW",
                    autofixable=False,  # Typography needs manual review
                    fix_description=f"Consider fixing {desc.replace('_', ' ')}"
                ))
                results.categories["8_TYPOGRAPHY"] = results.categories.get("8_TYPOGRAPHY", 0) + 1
                break  # Only report once per line per pattern

# ============================================================================
# PATCH APPLICATION
# ============================================================================

def apply_safe_patches(results: AuditResults) -> int:
    """Apply safe automatic patches and return count."""
    patches_applied = 0
    files_to_patch = {}

    for issue in results.issues:
        if not issue.autofixable:
            continue

        file_path = REPO_ROOT / issue.file
        if str(file_path) not in files_to_patch:
            try:
                files_to_patch[str(file_path)] = file_path.read_text(encoding='utf-8')
            except:
                continue

    # Group issues by file
    issues_by_file = {}
    for issue in results.issues:
        if issue.autofixable:
            if issue.file not in issues_by_file:
                issues_by_file[issue.file] = []
            issues_by_file[issue.file].append(issue)

    for rel_path, issues in issues_by_file.items():
        file_path = REPO_ROOT / rel_path
        if str(file_path) not in files_to_patch:
            continue

        content = files_to_patch[str(file_path)]
        lines = content.split('\n')
        modified = False

        # Sort issues by line number (reverse to preserve positions)
        issues.sort(key=lambda x: x.line, reverse=True)

        for issue in issues:
            line_idx = issue.line - 1
            if line_idx >= len(lines):
                continue

            old_line = lines[line_idx]
            new_line = old_line

            # Apply category-specific fixes
            if issue.category == "1_LLM_REMNANTS":
                # Remove the entire line if it's pure LLM artifact
                if any(kw in old_line.lower() for kw in ['end output', 'session summary', 'files changed', 'pass (', 'co-authored-by']):
                    new_line = ""  # Mark for deletion

            elif issue.category == "8_TYPOGRAPHY":
                if issue.subcategory == "double_space":
                    new_line = re.sub(r'  +', ' ', old_line)
                elif issue.subcategory == "space_before_comma":
                    new_line = re.sub(r' ,', ',', old_line)

            elif issue.category == "4_TAG_HYGIENE":
                # Convert literal tags to macros
                new_line = re.sub(r'\[Der\]', r'\\tagDer{}', old_line)
                new_line = re.sub(r'\[Dc\]', r'\\tagDc{}', new_line)
                new_line = re.sub(r'\[I\]', r'\\tagI{}', new_line)
                new_line = re.sub(r'\[P\]', r'\\tagP{}', new_line)
                new_line = re.sub(r'\[Cal\]', r'\\tagCal{}', new_line)
                new_line = re.sub(r'\[BL\]', r'\\tagBL{}', new_line)

            if new_line != old_line:
                results.patches.append(Patch(
                    file=rel_path,
                    line=issue.line,
                    old_text=old_line.strip()[:60],
                    new_text=new_line.strip()[:60] if new_line else "(deleted)",
                    category=issue.category,
                    reason=issue.fix_description,
                    applied=True
                ))
                lines[line_idx] = new_line
                modified = True
                patches_applied += 1

        # Remove empty lines that were marked for deletion
        lines = [l for l in lines if l is not None]

        if modified:
            new_content = '\n'.join(lines)
            # Remove double blank lines created by deletions
            new_content = re.sub(r'\n\n\n+', '\n\n', new_content)
            file_path.write_text(new_content, encoding='utf-8')

    return patches_applied

# ============================================================================
# SPECIAL CHECKS
# ============================================================================

def check_delta_derivation_file(results: AuditResults):
    """Special check for the delta_from_5d_action files."""
    targets = [
        EDC_PAPERS / "_shared/derivations/delta_from_5d_action_proton_scale.tex",
        EDC_PAPERS / "_shared/derivations/delta_from_5d_action_proton_scale.include.tex",
    ]

    for target in targets:
        if not target.exists():
            continue

        content = target.read_text(encoding='utf-8', errors='ignore')
        rel_path = str(target.relative_to(REPO_ROOT))

        # Check for proper δ_nucl usage
        has_bare_delta = bool(re.search(r'(?<!_)\\delta(?!_)(?!\s*=)', content))
        has_subscript_delta = bool(re.search(r'\\delta_\{?nucl', content))

        if has_bare_delta and not has_subscript_delta:
            results.issues.append(Issue(
                file=rel_path,
                line=0,
                category="3_DELTA_USAGE",
                subcategory="delta_derivation_file",
                snippet="File uses bare δ without δ_nucl subscript",
                severity="LOW",
                autofixable=False,
                fix_description="MANUAL REVIEW: Consider using δ_nucl per canon"
            ))
            results.categories["3_DELTA_USAGE"] = results.categories.get("3_DELTA_USAGE", 0) + 1

        # Check for LLM artifacts
        for pattern, desc, can_autofix in LLM_REMNANTS:
            if pattern.search(content):
                # Find line number
                for i, line in enumerate(content.split('\n'), 1):
                    if pattern.search(line):
                        results.issues.append(Issue(
                            file=rel_path,
                            line=i,
                            category="1_LLM_REMNANTS",
                            subcategory=desc,
                            snippet=line.strip()[:80],
                            severity="MED",
                            autofixable=can_autofix,
                            fix_description="Remove LLM artifact"
                        ))
                        results.categories["1_LLM_REMNANTS"] = results.categories.get("1_LLM_REMNANTS", 0) + 1
                        break

# ============================================================================
# REPORT GENERATION
# ============================================================================

def generate_audit_report(results: AuditResults) -> str:
    """Generate BOOK2_FULL_CLEANUP_AUDIT.md"""
    report = []
    report.append("# Book 2 Full Cleanup Audit Report")
    report.append(f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append(f"**Files scanned:** {len(results.files_scanned)}")
    report.append(f"**Total issues:** {len(results.issues)}")

    # Issues by category
    report.append("\n## Issues by Category\n")
    report.append("| Category | Count | Autofixable |")
    report.append("|----------|-------|-------------|")

    for cat in sorted(results.categories.keys()):
        count = results.categories[cat]
        autofix = sum(1 for i in results.issues if i.category == cat and i.autofixable)
        report.append(f"| {cat} | {count} | {autofix} |")

    # Detailed issues
    for cat in sorted(results.categories.keys()):
        cat_issues = [i for i in results.issues if i.category == cat]
        if not cat_issues:
            continue

        report.append(f"\n## {cat}\n")
        report.append("| File | Line | Subcategory | Snippet | Severity | Autofix |")
        report.append("|------|------|-------------|---------|----------|---------|")

        for issue in cat_issues[:100]:  # Limit to 100 per category
            snippet = issue.snippet.replace('|', '\\|')[:50]
            autofix = "YES" if issue.autofixable else "NO"
            report.append(f"| {Path(issue.file).name} | {issue.line} | {issue.subcategory} | `{snippet}` | {issue.severity} | {autofix} |")

        if len(cat_issues) > 100:
            report.append(f"\n*... and {len(cat_issues) - 100} more*")

    return '\n'.join(report)

def generate_summary_report(results: AuditResults, patches_applied: int) -> str:
    """Generate BOOK2_FULL_CLEANUP_SUMMARY.md"""
    report = []
    report.append("# Book 2 Full Cleanup Summary")
    report.append(f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")

    report.append("\n## Metrics\n")
    report.append(f"- **Files scanned:** {len(results.files_scanned)}")
    report.append(f"- **Total issues found:** {len(results.issues)}")
    report.append(f"- **Autofixable issues:** {sum(1 for i in results.issues if i.autofixable)}")
    report.append(f"- **Patches applied:** {patches_applied}")
    report.append(f"- **Physics changes:** 0")

    report.append("\n## Issues by Category\n")
    for cat in sorted(results.categories.keys()):
        report.append(f"- **{cat}:** {results.categories[cat]}")

    report.append("\n## Top Offending Files\n")
    file_counts = {}
    for issue in results.issues:
        file_counts[issue.file] = file_counts.get(issue.file, 0) + 1

    sorted_files = sorted(file_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    report.append("| File | Issue Count |")
    report.append("|------|-------------|")
    for f, c in sorted_files:
        report.append(f"| {Path(f).name} | {c} |")

    report.append("\n## Risk Assessment\n")
    high = sum(1 for i in results.issues if i.severity == "HIGH")
    med = sum(1 for i in results.issues if i.severity == "MED")
    low = sum(1 for i in results.issues if i.severity == "LOW")
    report.append(f"- HIGH severity: {high}")
    report.append(f"- MED severity: {med}")
    report.append(f"- LOW severity: {low}")

    report.append("\n## Manual Review Required\n")
    manual = [i for i in results.issues if not i.autofixable and i.severity in ["HIGH", "MED"]]
    if manual:
        report.append("| File | Line | Category | Description |")
        report.append("|------|------|----------|-------------|")
        for issue in manual[:20]:
            report.append(f"| {Path(issue.file).name} | {issue.line} | {issue.category} | {issue.fix_description} |")
    else:
        report.append("No high-priority manual review items.")

    return '\n'.join(report)

def generate_patchlog(results: AuditResults) -> str:
    """Generate BOOK2_FULL_CLEANUP_PATCHLOG.md"""
    report = []
    report.append("# Book 2 Full Cleanup Patchlog")
    report.append(f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append(f"**Patches applied:** {sum(1 for p in results.patches if p.applied)}")
    report.append("\n**Physics changes:** 0 (all patches are formatting/hygiene only)")

    if not results.patches:
        report.append("\n*No patches applied.*")
        return '\n'.join(report)

    report.append("\n## Applied Patches\n")
    report.append("| File | Line | Category | Before | After | Reason |")
    report.append("|------|------|----------|--------|-------|--------|")

    for patch in results.patches:
        if patch.applied:
            old = patch.old_text.replace('|', '\\|')
            new = patch.new_text.replace('|', '\\|')
            report.append(f"| {Path(patch.file).name} | {patch.line} | {patch.category} | `{old}` | `{new}` | {patch.reason} |")

    return '\n'.join(report)

# ============================================================================
# MAIN
# ============================================================================

def main():
    print("Book 2 Full Cleanup Audit Tool")
    print("=" * 50)

    results = AuditResults()

    # Step 1: Parse include tree
    print("\n[1/5] Parsing include tree...")
    main_tex = BOOK2_SRC / "main.tex"
    if not main_tex.exists():
        main_tex = BOOK2_SRC / "EDC_Part_II_Weak_Sector_rebuild.tex"

    files_to_scan = parse_include_tree(main_tex)
    print(f"  Found {len(files_to_scan)} files in include tree")

    # Step 2: Scan all files
    print("\n[2/5] Scanning for issues...")
    delta_context = {}
    for file_path in files_to_scan:
        scan_file(Path(file_path), results, delta_context)
    print(f"  Found {len(results.issues)} issues")

    # Step 3: Special check for delta derivation
    print("\n[3/5] Checking delta derivation files...")
    check_delta_derivation_file(results)

    # Step 4: Apply safe patches
    print("\n[4/5] Applying safe patches...")
    patches_applied = apply_safe_patches(results)
    print(f"  Applied {patches_applied} patches")

    # Step 5: Generate reports
    print("\n[5/5] Generating reports...")
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    audit = generate_audit_report(results)
    (DOCS_DIR / "BOOK2_FULL_CLEANUP_AUDIT.md").write_text(audit)
    print("  Wrote BOOK2_FULL_CLEANUP_AUDIT.md")

    summary = generate_summary_report(results, patches_applied)
    (DOCS_DIR / "BOOK2_FULL_CLEANUP_SUMMARY.md").write_text(summary)
    print("  Wrote BOOK2_FULL_CLEANUP_SUMMARY.md")

    patchlog = generate_patchlog(results)
    (DOCS_DIR / "BOOK2_FULL_CLEANUP_PATCHLOG.md").write_text(patchlog)
    print("  Wrote BOOK2_FULL_CLEANUP_PATCHLOG.md")

    # Summary
    print("\n" + "=" * 50)
    print("AUDIT COMPLETE")
    print(f"  Files scanned: {len(results.files_scanned)}")
    print(f"  Issues found: {len(results.issues)}")
    print(f"  Patches applied: {patches_applied}")
    print(f"  Physics changes: 0")

    return results, patches_applied

if __name__ == "__main__":
    main()
