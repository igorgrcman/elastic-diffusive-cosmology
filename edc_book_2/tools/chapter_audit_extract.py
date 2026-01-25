#!/usr/bin/env python3
"""
chapter_audit_extract.py — Extract equations, claims, and symbols from Book 2 chapters

Usage:
    python3 tools/chapter_audit_extract.py --chapter CH01 --output audit/chapters/CH01_AUDIT.md
    python3 tools/chapter_audit_extract.py --all --summary

Extracts:
    - Equations (labeled + unlabeled)
    - Claims with epistemic tags ([Der], [BL], [P], etc.)
    - Symbols used (matched against GLOBAL_SYMBOL_TABLE)
    - Section structure

Author: Claude Code
Date: 2026-01-24
"""

import argparse
import json
import re
import os
from pathlib import Path
from collections import defaultdict

# Base paths
BOOK2_SRC = Path("/Users/igor/ClaudeAI/EDC_Project/elastic-diffusive-cosmology_repo/edc_book_2/src")
AUDIT_DIR = Path("/Users/igor/ClaudeAI/EDC_Project/elastic-diffusive-cosmology_repo/edc_book_2/audit")

# Chapter map from CHAPTER_MAP.yml (hardcoded for reliability)
CHAPTER_MAP = {
    "CH01": {
        "title": "The Weak Interface",
        "files": [
            "sections/00_reader_contract.tex",
            "sections/01_how_we_got_here.tex",
            "sections/02_geometry_interface.tex",
            "sections/03_unified_pipeline.tex",
            "sections/04a_unified_master_figure.tex",
            "sections/04_ontology.tex",
            "sections/04b_proton_anchor.tex",
            "sections/05_case_neutron.tex",
            "sections/06_case_muon.tex",
            "sections/07_case_tau.tex",
            "sections/09_case_electron.tex",
            "sections/08_case_pion.tex",
            "sections/10_case_neutrino.tex",
            "sections/11_gf_pathway.tex",
            "sections/13_summary.tex"
        ]
    },
    "CH02": {
        "title": "Frozen Regime Foundations",
        "files": ["sections/02_frozen_regime_foundations.tex"]
    },
    "CH03": {
        "title": "The Z6 Program",
        "files": ["Z6_content_full.tex"]
    }
}

# Epistemic tags
EPISTEMIC_TAGS = ["[BL]", "[Der]", "[Dc]", "[I]", "[Cal]", "[P]", "[M]", "[Def]", "[OPEN]"]

# Tier-1 symbols from GLOBAL_SYMBOL_TABLE
TIER1_SYMBOLS = {
    r"\\xi(?![a-zA-Z])": "ξ",
    r"R_\\xi|\\Rxi": "R_ξ",
    r"\\sigma(?![a-zA-Z])": "σ",
    r"\\eta(?![a-zA-Z])": "η",
    r"\\mathcal\{M\}\^5": "M⁵",
    r"\\Sigma\^3": "Σ³",
    r"M_\{5,\\mathrm\{Pl\}\}": "M_{5,Pl}",
    r"z_1|z_2": "z₁/z₂",
    r"G_5": "G₅",
    r"G_F": "G_F",
    r"\\alpha(?![a-zA-Z])": "α",
    r"m_e": "m_e",
    r"m_p": "m_p",
    r"m_n": "m_n",
}

# Forbidden patterns from NOTATION_POLICY
FORBIDDEN_PATTERNS = [
    (r"(?<!\{)z(?![_0-9a-zA-Z\}])\s*[=<>≈]", "z used as 5D coordinate (should be ξ)"),
    (r"\\partial_z", "∂_z should be ∂_ξ"),
    (r"dz(?!\s*[a-zA-Z])", "dz integration should be dξ"),
    (r"(?<![\\mathcal\{])M5(?![,])", "M5 should be \\mathcal{M}^5"),
    (r"M_5(?!\s*,)", "M_5 ambiguous — use \\mathcal{M}^5 or M_{5,Pl}"),
]

def extract_from_file(filepath):
    """Extract equations, claims, symbols from a single LaTeX file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
    except FileNotFoundError:
        return None

    results = {
        "file": str(filepath),
        "equations_labeled": [],
        "equations_unlabeled": [],
        "claims": [],
        "symbols_tier1": defaultdict(int),
        "symbols_all": defaultdict(int),
        "forbidden_violations": [],
        "sections": [],
        "line_count": len(lines)
    }

    # Extract labeled equations
    labeled_eq = re.findall(r'\\begin\{equation\}(.*?)\\label\{([^}]+)\}(.*?)\\end\{equation\}',
                            content, re.DOTALL)
    for pre, label, post in labeled_eq:
        eq_content = (pre + post).strip()
        results["equations_labeled"].append({
            "label": label,
            "content": eq_content[:200] + ("..." if len(eq_content) > 200 else "")
        })

    # Extract unlabeled equations
    all_equations = re.findall(r'\\begin\{equation\}(.*?)\\end\{equation\}', content, re.DOTALL)
    labeled_count = len(labeled_eq)
    unlabeled_count = len(all_equations) - labeled_count
    results["equations_unlabeled_count"] = unlabeled_count

    # Extract align environments
    align_eqs = re.findall(r'\\begin\{align\*?\}(.*?)\\end\{align\*?\}', content, re.DOTALL)
    results["align_blocks"] = len(align_eqs)

    # Extract claims with epistemic tags
    for i, line in enumerate(lines, 1):
        for tag in EPISTEMIC_TAGS:
            if tag in line:
                results["claims"].append({
                    "line": i,
                    "tag": tag,
                    "text": line.strip()[:150]
                })

    # Count tier-1 symbols
    for pattern, name in TIER1_SYMBOLS.items():
        matches = re.findall(pattern, content)
        if matches:
            results["symbols_tier1"][name] = len(matches)

    # Check for forbidden patterns
    for i, line in enumerate(lines, 1):
        for pattern, desc in FORBIDDEN_PATTERNS:
            if re.search(pattern, line):
                # Additional context check to reduce false positives
                if "z_1" in line or "z_2" in line:
                    continue  # Z6 complex roots are OK
                if "(x, y, z)" in line or "(x,y,z)" in line:
                    continue  # 3D tuple is OK
                results["forbidden_violations"].append({
                    "line": i,
                    "pattern": desc,
                    "context": line.strip()[:100]
                })

    # Extract sections
    sections = re.findall(r'\\(section|subsection|subsubsection)\{([^}]+)\}', content)
    results["sections"] = [{"type": s[0], "title": s[1]} for s in sections]

    return results

def analyze_chapter(chapter_id):
    """Analyze all files in a chapter."""
    if chapter_id not in CHAPTER_MAP:
        print(f"Unknown chapter: {chapter_id}")
        return None

    chapter = CHAPTER_MAP[chapter_id]
    chapter_results = {
        "chapter_id": chapter_id,
        "title": chapter["title"],
        "files_analyzed": [],
        "total_labeled_equations": 0,
        "total_unlabeled_equations": 0,
        "total_claims": 0,
        "symbols_summary": defaultdict(int),
        "violations_summary": [],
        "all_claims": [],
        "all_equations": []
    }

    for rel_path in chapter["files"]:
        filepath = BOOK2_SRC / rel_path
        results = extract_from_file(filepath)
        if results:
            chapter_results["files_analyzed"].append(results)
            chapter_results["total_labeled_equations"] += len(results["equations_labeled"])
            chapter_results["total_unlabeled_equations"] += results.get("equations_unlabeled_count", 0)
            chapter_results["total_claims"] += len(results["claims"])

            for sym, count in results["symbols_tier1"].items():
                chapter_results["symbols_summary"][sym] += count

            chapter_results["violations_summary"].extend(results["forbidden_violations"])
            chapter_results["all_claims"].extend(results["claims"])
            chapter_results["all_equations"].extend(results["equations_labeled"])

    return chapter_results

def generate_audit_report(chapter_results):
    """Generate markdown audit report for a chapter."""
    cr = chapter_results

    report = f"""# {cr['chapter_id']} Audit Report: {cr['title']}

**Generated**: 2026-01-24
**Branch**: book2-chapter-audit-v1
**Status**: MECHANICAL_DONE

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Files Analyzed | {len(cr['files_analyzed'])} |
| Labeled Equations | {cr['total_labeled_equations']} |
| Unlabeled Equations | {cr['total_unlabeled_equations']} |
| Claims with Tags | {cr['total_claims']} |
| Forbidden Violations | {len(cr['violations_summary'])} |

---

## Tier-1 Symbol Usage

| Symbol | Count | Status |
|--------|-------|--------|
"""

    for sym, count in sorted(cr['symbols_summary'].items(), key=lambda x: -x[1]):
        status = "✅ OK" if count > 0 else "—"
        report += f"| {sym} | {count} | {status} |\n"

    report += "\n---\n\n## Forbidden Pattern Violations\n\n"

    if cr['violations_summary']:
        report += "| File | Line | Pattern | Context |\n|------|------|---------|--------|\n"
        for v in cr['violations_summary']:
            file_short = Path(v.get('file', 'unknown')).name if 'file' in v else 'various'
            report += f"| {file_short} | {v['line']} | {v['pattern']} | `{v['context'][:50]}...` |\n"
    else:
        report += "*No violations found.*\n"

    report += "\n---\n\n## Epistemic Claims Summary\n\n"

    tag_counts = defaultdict(int)
    for claim in cr['all_claims']:
        tag_counts[claim['tag']] += 1

    report += "| Tag | Count | Meaning |\n|-----|-------|--------|\n"
    tag_meanings = {
        "[BL]": "Baseline (PDG/CODATA)",
        "[Der]": "Derived from principles",
        "[Dc]": "Derived conditional",
        "[I]": "Identified/pattern",
        "[Cal]": "Calibrated/fitted",
        "[P]": "Proposed/postulated",
        "[M]": "Mathematical theorem",
        "[Def]": "Definition",
        "[OPEN]": "Unresolved"
    }
    for tag in EPISTEMIC_TAGS:
        count = tag_counts.get(tag, 0)
        meaning = tag_meanings.get(tag, "")
        report += f"| {tag} | {count} | {meaning} |\n"

    report += "\n---\n\n## Files Analyzed\n\n"

    for f in cr['files_analyzed']:
        fname = Path(f['file']).name
        report += f"### {fname}\n\n"
        report += f"- Lines: {f['line_count']}\n"
        report += f"- Labeled equations: {len(f['equations_labeled'])}\n"
        report += f"- Align blocks: {f.get('align_blocks', 0)}\n"
        report += f"- Sections: {len(f['sections'])}\n"
        if f['sections']:
            for s in f['sections'][:5]:
                report += f"  - {s['type']}: {s['title']}\n"
            if len(f['sections']) > 5:
                report += f"  - ... and {len(f['sections']) - 5} more\n"
        report += "\n"

    report += """---

## TODO Items

- [ ] CONTEXT audit: Verify each symbol matches GLOBAL_SYMBOL_TABLE
- [ ] NARRATIVE audit: Check claim flow and evidence links
- [ ] EVIDENCE audit: Link each [Der] to derivation source

---

## Audit Level Status

| Level | Status |
|-------|--------|
| MECHANICAL | ✅ DONE |
| CONTEXT | ⏳ PENDING |
| NARRATIVE | ⏳ PENDING |
| EVIDENCE | ⏳ PENDING |

---

*Generated by chapter_audit_extract.py*
"""

    return report

def main():
    parser = argparse.ArgumentParser(description="Extract audit data from Book 2 chapters")
    parser.add_argument("--chapter", type=str, help="Chapter ID (e.g., CH01)")
    parser.add_argument("--all", action="store_true", help="Process all chapters CH01-CH03")
    parser.add_argument("--output", type=str, help="Output file path")
    parser.add_argument("--summary", action="store_true", help="Print summary to stdout")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    chapters_to_process = []

    if args.all:
        chapters_to_process = ["CH01", "CH02", "CH03"]
    elif args.chapter:
        chapters_to_process = [args.chapter]
    else:
        print("Specify --chapter CHXX or --all")
        return

    all_results = {}

    for ch_id in chapters_to_process:
        print(f"Analyzing {ch_id}...")
        results = analyze_chapter(ch_id)
        if results:
            all_results[ch_id] = results

            if args.json:
                # Convert defaultdicts to regular dicts for JSON
                results['symbols_summary'] = dict(results['symbols_summary'])
                print(json.dumps(results, indent=2, default=str))
            elif args.summary:
                print(f"\n{ch_id}: {results['title']}")
                print(f"  Files: {len(results['files_analyzed'])}")
                print(f"  Labeled equations: {results['total_labeled_equations']}")
                print(f"  Claims: {results['total_claims']}")
                print(f"  Violations: {len(results['violations_summary'])}")

            # Generate and save audit report
            output_path = args.output or AUDIT_DIR / "chapters" / f"{ch_id}_AUDIT.md"
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            report = generate_audit_report(results)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"  Report written to: {output_path}")

    return all_results

if __name__ == "__main__":
    main()
