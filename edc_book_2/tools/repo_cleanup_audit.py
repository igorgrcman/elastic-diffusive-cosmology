#!/usr/bin/env python3
"""
Repo-Wide Cleanup Audit Tool
=============================
Comprehensive scan for LLM/log artifacts across:
- edc_book_2/src/**
- edc_papers/_shared/derivations/**
- edc_papers/_shared/lemmas/**
- edc_papers/_shared/boxes/**
- docs/**/*.md

Generates:
- REPO_CLEANUP_AUDIT.md
- REPO_CLEANUP_PATCHLOG.md
"""

import os
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Set, Tuple, Optional
from datetime import datetime

# Configuration
REPO_ROOT = Path(__file__).parent.parent.parent
BOOK2_ROOT = REPO_ROOT / "edc_book_2"
EDC_PAPERS = REPO_ROOT / "edc_papers"
DOCS_ROOT = REPO_ROOT / "docs"

# Target directories
SCAN_TARGETS = [
    (BOOK2_ROOT / "src", ["*.tex", "*.md"]),
    (EDC_PAPERS / "_shared" / "derivations", ["*.tex"]),
    (EDC_PAPERS / "_shared" / "lemmas", ["*.tex"]),
    (EDC_PAPERS / "_shared" / "boxes", ["*.tex"]),
    (DOCS_ROOT, ["*.md"]),
    (BOOK2_ROOT / "docs", ["*.md"]),
]

@dataclass
class Issue:
    file: str
    line: int
    category: str
    snippet: str
    action: str  # DELETE, KEEP, MANUAL
    reason: str

@dataclass
class Patch:
    file: str
    line: int
    old_text: str
    new_text: str
    reason: str
    applied: bool = False

@dataclass
class AuditResults:
    issues: List[Issue] = field(default_factory=list)
    patches: List[Patch] = field(default_factory=list)
    files_scanned: int = 0
    lines_deleted: int = 0
    files_modified: Set[str] = field(default_factory=set)
    standalone_checked: int = 0
    include_files_ok: int = 0
    include_files_missing: List[str] = field(default_factory=list)

# ============================================================================
# LLM ARTIFACT PATTERNS (Non-negotiable - delete when found as plain prose)
# ============================================================================

# These patterns indicate LLM/log artifacts that should be removed
LLM_ARTIFACT_PATTERNS = [
    # Exact phrases that are always artifacts
    (re.compile(r'^\s*END\s+OUTPUT\s*$', re.IGNORECASE), "END OUTPUT marker"),
    (re.compile(r'^\s*Session\s+Summary\s*$', re.IGNORECASE), "Session Summary header"),
    (re.compile(r'^\s*Files\s+changed:\s*$', re.IGNORECASE), "Files changed marker"),
    (re.compile(r'^\s*Compile\s+status:\s*', re.IGNORECASE), "Compile status marker"),
    (re.compile(r'^\s*Output\s+Summary\s*$', re.IGNORECASE), "Output Summary marker"),
    (re.compile(r'PASS\s*\(\s*\d+\s*pages?\s*\)', re.IGNORECASE), "PASS (N pages) marker"),
    (re.compile(r'^\s*Co-Authored-By:\s*Claude', re.MULTILINE), "Co-authored-by Claude"),
    (re.compile(r'^\s*Next\s+steps:\s*$', re.IGNORECASE), "Next steps marker"),
    (re.compile(r'^\s*Worked\s+for\s+\d+', re.IGNORECASE), "Worked for N marker"),
    (re.compile(r'^\s*Cooked\s+for\s+\d+', re.IGNORECASE), "Cooked for N marker"),
    (re.compile(r'^\s*Baked\s+for\s+\d+', re.IGNORECASE), "Baked for N marker"),
    (re.compile(r'^\s*git\s+push\s*$', re.IGNORECASE), "git push command"),
    (re.compile(r'^❯', re.MULTILINE), "Terminal prompt"),
]

# Patterns that need context check (only delete if NOT in legitimate context)
CONTEXT_PATTERNS = [
    (re.compile(r'─{20,}'), "Long dash separator", ["verbatim", "lstlisting", "comment"]),
    (re.compile(r'═{20,}'), "Long double-line separator", ["verbatim", "lstlisting", "comment"]),
]

# ============================================================================
# FILE SCANNING
# ============================================================================

def collect_files(targets: List[Tuple[Path, List[str]]]) -> List[Path]:
    """Collect all files matching patterns in target directories."""
    files = []
    for base_dir, patterns in targets:
        if not base_dir.exists():
            continue
        for pattern in patterns:
            files.extend(base_dir.rglob(pattern))
    return files

def is_in_safe_context(content: str, match_pos: int, safe_contexts: List[str]) -> bool:
    """Check if a match position is within a safe context."""
    # Get surrounding content
    start = max(0, match_pos - 200)
    end = min(len(content), match_pos + 200)
    context = content[start:end].lower()

    for safe in safe_contexts:
        if safe in context:
            return True

    # Also check if line starts with %
    line_start = content.rfind('\n', 0, match_pos) + 1
    if match_pos > line_start and content[line_start:match_pos].strip().startswith('%'):
        return True

    return False

def scan_file(file_path: Path, results: AuditResults) -> List[Tuple[int, str, str]]:
    """Scan a single file for artifacts. Returns list of (line_num, old_text, reason)."""
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
        lines = content.split('\n')
    except Exception as e:
        return []

    results.files_scanned += 1
    rel_path = str(file_path.relative_to(REPO_ROOT))
    deletions = []

    # Check each line
    for line_num, line in enumerate(lines, 1):
        stripped = line.strip()

        # Skip empty lines
        if not stripped:
            continue

        # Check LLM artifact patterns
        for pattern, desc in LLM_ARTIFACT_PATTERNS:
            if pattern.search(line):
                # Check if inside comment, verbatim, etc.
                is_comment = stripped.startswith('%') or stripped.startswith('#')
                is_in_code_block = False

                # For markdown, check if in code block
                if file_path.suffix == '.md':
                    before = '\n'.join(lines[:line_num-1])
                    code_starts = before.count('```')
                    is_in_code_block = code_starts % 2 == 1

                # Skip if this is a template/example in documentation
                if 'template' in rel_path.lower() or 'example' in line.lower():
                    results.issues.append(Issue(
                        file=rel_path,
                        line=line_num,
                        category=desc,
                        snippet=line[:60],
                        action="KEEP",
                        reason="Template/example content"
                    ))
                    continue

                # Skip if in documentation files (SESSION_LOG, AUDIT, PATCHLOG, etc.)
                doc_patterns = ['CANON_BUNDLE', 'SESSION_LOG', 'AUDIT', 'PATCHLOG',
                               'SUMMARY', 'REPORT', 'LOG', 'STATUS']
                if any(p in rel_path.upper() for p in doc_patterns):
                    results.issues.append(Issue(
                        file=rel_path,
                        line=line_num,
                        category=desc,
                        snippet=line[:60],
                        action="KEEP",
                        reason="Documentation/log file"
                    ))
                    continue

                if is_comment or is_in_code_block:
                    results.issues.append(Issue(
                        file=rel_path,
                        line=line_num,
                        category=desc,
                        snippet=line[:60],
                        action="KEEP",
                        reason="Inside comment/code block"
                    ))
                else:
                    # This is a real artifact - mark for deletion
                    results.issues.append(Issue(
                        file=rel_path,
                        line=line_num,
                        category=desc,
                        snippet=line[:60],
                        action="DELETE",
                        reason="LLM/log artifact in prose"
                    ))
                    deletions.append((line_num, line, desc))
                break

    return deletions

def apply_deletions(file_path: Path, deletions: List[Tuple[int, str, str]], results: AuditResults):
    """Apply deletions to a file."""
    if not deletions:
        return

    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
        lines = content.split('\n')

        # Sort by line number descending to preserve positions
        deletions.sort(key=lambda x: x[0], reverse=True)

        for line_num, old_text, reason in deletions:
            idx = line_num - 1
            if idx < len(lines):
                results.patches.append(Patch(
                    file=str(file_path.relative_to(REPO_ROOT)),
                    line=line_num,
                    old_text=old_text[:60],
                    new_text="(deleted)",
                    reason=reason,
                    applied=True
                ))
                lines.pop(idx)
                results.lines_deleted += 1

        # Remove double blank lines created by deletions
        new_content = '\n'.join(lines)
        new_content = re.sub(r'\n\n\n+', '\n\n', new_content)

        file_path.write_text(new_content, encoding='utf-8')
        results.files_modified.add(str(file_path.relative_to(REPO_ROOT)))

    except Exception as e:
        print(f"  Error applying deletions to {file_path}: {e}")

# ============================================================================
# STANDALONE DERIVATION CHECK
# ============================================================================

def check_standalone_derivations(results: AuditResults):
    """Check that standalone derivations have .include.tex siblings."""
    derivations_dir = EDC_PAPERS / "_shared" / "derivations"
    if not derivations_dir.exists():
        return

    for tex_file in derivations_dir.glob("*.tex"):
        # Skip if it's already an include file
        if ".include" in tex_file.name:
            continue

        # Check if it's a standalone document
        try:
            content = tex_file.read_text(encoding='utf-8', errors='ignore')
            if '\\documentclass' in content:
                results.standalone_checked += 1

                # Check for sibling .include.tex
                include_name = tex_file.stem + ".include.tex"
                include_path = tex_file.parent / include_name

                if include_path.exists():
                    results.include_files_ok += 1
                else:
                    results.include_files_missing.append(str(tex_file.relative_to(REPO_ROOT)))
        except Exception:
            pass

# ============================================================================
# REPORT GENERATION
# ============================================================================

def generate_audit_report(results: AuditResults) -> str:
    """Generate REPO_CLEANUP_AUDIT.md"""
    report = []
    report.append("# Repo-Wide Cleanup Audit Report")
    report.append(f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append(f"**Files scanned:** {results.files_scanned}")
    report.append(f"**Issues found:** {len(results.issues)}")
    report.append(f"**Lines deleted:** {results.lines_deleted}")
    report.append(f"**Files modified:** {len(results.files_modified)}")

    # Action summary
    delete_count = sum(1 for i in results.issues if i.action == "DELETE")
    keep_count = sum(1 for i in results.issues if i.action == "KEEP")
    manual_count = sum(1 for i in results.issues if i.action == "MANUAL")

    report.append("\n## Action Summary\n")
    report.append(f"- **DELETE:** {delete_count}")
    report.append(f"- **KEEP:** {keep_count}")
    report.append(f"- **MANUAL:** {manual_count}")

    # Standalone derivations check
    report.append("\n## Standalone Derivations Check\n")
    report.append(f"- **Standalone files checked:** {results.standalone_checked}")
    report.append(f"- **Include siblings present:** {results.include_files_ok}")
    report.append(f"- **Include siblings missing:** {len(results.include_files_missing)}")

    if results.include_files_missing:
        report.append("\n**Missing include files:**")
        for f in results.include_files_missing:
            report.append(f"- `{f}`")

    # Issues table
    if results.issues:
        report.append("\n## Issues Found\n")
        report.append("| File | Line | Category | Action | Snippet | Reason |")
        report.append("|------|------|----------|--------|---------|--------|")

        for issue in results.issues[:200]:  # Limit to 200
            snippet = issue.snippet.replace('|', '\\|')[:40]
            report.append(f"| {Path(issue.file).name} | {issue.line} | {issue.category} | {issue.action} | `{snippet}` | {issue.reason} |")

        if len(results.issues) > 200:
            report.append(f"\n*... and {len(results.issues) - 200} more*")
    else:
        report.append("\n## Issues Found\n")
        report.append("**No LLM/log artifacts found.** The codebase is clean.")

    return '\n'.join(report)

def generate_patchlog(results: AuditResults) -> str:
    """Generate REPO_CLEANUP_PATCHLOG.md"""
    report = []
    report.append("# Repo-Wide Cleanup Patchlog")
    report.append(f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append(f"**Lines deleted:** {results.lines_deleted}")
    report.append(f"**Files modified:** {len(results.files_modified)}")
    report.append("\n**Physics changes:** 0 (only LLM/log artifacts removed)")

    if not results.patches:
        report.append("\n## Applied Patches\n")
        report.append("*No patches applied. The codebase was already clean.*")
        return '\n'.join(report)

    report.append("\n## Applied Patches\n")
    report.append("| File | Line | Before | After | Reason |")
    report.append("|------|------|--------|-------|--------|")

    for patch in results.patches:
        old = patch.old_text.replace('|', '\\|')
        new = patch.new_text.replace('|', '\\|')
        report.append(f"| {Path(patch.file).name} | {patch.line} | `{old}` | `{new}` | {patch.reason} |")

    # Files modified summary
    report.append("\n## Files Modified\n")
    for f in sorted(results.files_modified):
        count = sum(1 for p in results.patches if p.file == f)
        report.append(f"- `{f}`: {count} lines deleted")

    return '\n'.join(report)

# ============================================================================
# MAIN
# ============================================================================

def main():
    print("Repo-Wide Cleanup Audit Tool")
    print("=" * 50)

    results = AuditResults()

    # Step 1: Collect files
    print("\n[1/4] Collecting files to scan...")
    files = collect_files(SCAN_TARGETS)
    print(f"  Found {len(files)} files")

    # Step 2: Scan files
    print("\n[2/4] Scanning for LLM/log artifacts...")
    all_deletions = {}
    for file_path in files:
        deletions = scan_file(file_path, results)
        if deletions:
            all_deletions[file_path] = deletions
    print(f"  Found {len(results.issues)} potential issues")
    print(f"  {sum(1 for i in results.issues if i.action == 'DELETE')} marked for deletion")

    # Step 3: Apply deletions
    print("\n[3/4] Applying safe deletions...")
    for file_path, deletions in all_deletions.items():
        apply_deletions(file_path, deletions, results)
    print(f"  Deleted {results.lines_deleted} lines from {len(results.files_modified)} files")

    # Step 4: Check standalone derivations
    print("\n[4/4] Checking standalone derivations...")
    check_standalone_derivations(results)
    print(f"  Checked {results.standalone_checked} standalone files")
    print(f"  {results.include_files_ok} have include siblings")
    print(f"  {len(results.include_files_missing)} missing include files")

    # Generate reports
    print("\nGenerating reports...")
    docs_dir = BOOK2_ROOT / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)

    audit = generate_audit_report(results)
    (docs_dir / "REPO_CLEANUP_AUDIT.md").write_text(audit)
    print("  Wrote REPO_CLEANUP_AUDIT.md")

    patchlog = generate_patchlog(results)
    (docs_dir / "REPO_CLEANUP_PATCHLOG.md").write_text(patchlog)
    print("  Wrote REPO_CLEANUP_PATCHLOG.md")

    # Summary
    print("\n" + "=" * 50)
    print("AUDIT COMPLETE")
    print(f"  Files scanned: {results.files_scanned}")
    print(f"  Issues found: {len(results.issues)}")
    print(f"  Lines deleted: {results.lines_deleted}")
    print(f"  Files modified: {len(results.files_modified)}")
    print(f"  Physics changes: 0")

    return results

if __name__ == "__main__":
    main()
