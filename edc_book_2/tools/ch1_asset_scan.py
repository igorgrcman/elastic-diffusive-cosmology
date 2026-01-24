#!/usr/bin/env python3
"""
CH1 Asset Scanner (Paranoid Mode)
Scans CH1 source files for asset references and validates existence.
Detects ambiguities across multiple trees.
"""

import os
import sys
import re
import hashlib
import csv
from pathlib import Path
from datetime import datetime

# Configuration
SRC_ROOT = Path(__file__).parent.parent / "src"
SNAPSHOT_ROOT = Path(__file__).parent.parent.parent / "edc_papers/paper_3_series/20_book_chapter_weak_interface/paper/rebuild_part2_snapshot/paper"
AUDIT_DIR = Path(__file__).parent.parent / "audit/ch1"
INPUTS_FILE = AUDIT_DIR / "CH1_BUILD_INPUTS.txt"

# Common extensions to try
COMMON_EXTS = ['.pdf', '.png', '.jpg', '.jpeg', '.tex', '']

def sha256_16(filepath):
    """Return first 16 chars of SHA256 hash."""
    try:
        with open(filepath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:16]
    except:
        return ""

def file_size(filepath):
    """Return file size in bytes."""
    try:
        return os.path.getsize(filepath)
    except:
        return 0

def parse_graphicspath(main_tex):
    """Extract graphicspath entries from main.tex."""
    paths = []
    try:
        with open(main_tex, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            # Match \graphicspath{{path1/}{path2/}}
            match = re.search(r'\\graphicspath\s*\{([^}]+)\}', content)
            if match:
                inner = match.group(1)
                # Extract individual paths
                for m in re.finditer(r'\{([^}]+)\}', inner):
                    paths.append(m.group(1))
    except:
        pass
    return paths

def find_asset_refs(tex_file):
    """Find all asset references in a TeX file."""
    refs = []
    try:
        with open(tex_file, 'r', encoding='utf-8', errors='ignore') as f:
            for lineno, line in enumerate(f, 1):
                # Skip commented lines
                stripped = line.lstrip()
                if stripped.startswith('%'):
                    continue
                # Remove inline comments
                if '%' in line:
                    comment_pos = line.index('%')
                    line = line[:comment_pos]

                # \includegraphics
                for m in re.finditer(r'\\includegraphics(?:\[[^\]]*\])?\s*\{([^}]+)\}', line):
                    refs.append({
                        'type': 'FIGURE',
                        'file': str(tex_file),
                        'line': lineno,
                        'snippet': m.group(0)[:120],
                        'raw_path': m.group(1).strip()
                    })

                # \includepdf
                for m in re.finditer(r'\\includepdf(?:\[[^\]]*\])?\s*\{([^}]+)\}', line):
                    refs.append({
                        'type': 'PDF',
                        'file': str(tex_file),
                        'line': lineno,
                        'snippet': m.group(0)[:120],
                        'raw_path': m.group(1).strip()
                    })

                # \input for code/output or figures
                for m in re.finditer(r'\\input\s*\{([^}]+)\}', line):
                    path = m.group(1).strip()
                    if 'code' in path.lower() or 'figure' in path.lower() or 'output' in path.lower():
                        refs.append({
                            'type': 'TABLE_TEX' if 'code' in path.lower() else 'FIGURE',
                            'file': str(tex_file),
                            'line': lineno,
                            'snippet': m.group(0)[:120],
                            'raw_path': path
                        })
    except Exception as e:
        print(f"Error parsing {tex_file}: {e}", file=sys.stderr)
    return refs

def resolve_path(raw_path, including_file, graphicspaths, src_root, snapshot_root):
    """
    Resolve asset path using paranoid rules.
    Returns: (resolved_path, candidates_list, resolution_rule)
    """
    candidates = []
    including_dir = Path(including_file).parent

    # Try with various extensions
    paths_to_try = [raw_path]
    if not any(raw_path.endswith(ext) for ext in COMMON_EXTS if ext):
        paths_to_try.extend([raw_path + ext for ext in COMMON_EXTS if ext])

    # Rule 1: Relative to including file
    for p in paths_to_try:
        full = including_dir / p
        if full.exists():
            candidates.append(('RELATIVE', str(full.resolve())))

    # Rule 2: From src_root
    for p in paths_to_try:
        full = src_root / p
        if full.exists() and str(full.resolve()) not in [c[1] for c in candidates]:
            candidates.append(('SRC_ROOT', str(full.resolve())))

    # Rule 3: graphicspath entries
    for gp in graphicspaths:
        gp_full = src_root / gp
        for p in paths_to_try:
            full = gp_full / p
            if full.exists() and str(full.resolve()) not in [c[1] for c in candidates]:
                candidates.append(('GRAPHICSPATH', str(full.resolve())))

    # Rule 4: Snapshot tree
    if snapshot_root and snapshot_root.exists():
        for p in paths_to_try:
            full = snapshot_root / p
            if full.exists() and str(full.resolve()) not in [c[1] for c in candidates]:
                candidates.append(('SNAPSHOT', str(full.resolve())))

    if len(candidates) == 0:
        return ("MISSING", [], "NONE")
    elif len(candidates) == 1:
        return (candidates[0][1], candidates, candidates[0][0])
    else:
        # Multiple candidates - check if all have same hash
        hashes = set(sha256_16(c[1]) for c in candidates)
        if len(hashes) == 1:
            # All same hash - prefer non-snapshot, return first
            for c in candidates:
                if c[0] != 'SNAPSHOT':
                    return (c[1], candidates, c[0] + "_DEDUP")
            return (candidates[0][1], candidates, candidates[0][0] + "_DEDUP")
        else:
            return ("AMBIGUOUS", candidates, "MULTI")

def main():
    print("CH1 Asset Scanner (Paranoid Mode)")
    print("=" * 50)

    # Read CH1 input files
    if not INPUTS_FILE.exists():
        print(f"ERROR: {INPUTS_FILE} not found", file=sys.stderr)
        sys.exit(1)

    ch1_files = []
    with open(INPUTS_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                ch1_files.append(SRC_ROOT / line)

    print(f"Scanning {len(ch1_files)} CH1 files...")

    # Parse graphicspath from main.tex
    main_tex = SRC_ROOT / "EDC_Part_II_Weak_Sector_rebuild.tex"
    graphicspaths = parse_graphicspath(main_tex)
    print(f"Found graphicspaths: {graphicspaths}")

    # Collect all asset refs
    all_refs = []
    for f in ch1_files:
        if f.exists():
            refs = find_asset_refs(f)
            all_refs.extend(refs)

    print(f"Found {len(all_refs)} asset references")

    # Resolve each ref
    assets = []
    for i, ref in enumerate(all_refs, 1):
        resolved, candidates, rule = resolve_path(
            ref['raw_path'],
            ref['file'],
            graphicspaths,
            SRC_ROOT,
            SNAPSHOT_ROOT if SNAPSHOT_ROOT.exists() else None
        )

        # Check for ambiguity
        # If all candidates have same hash, not really ambiguous - just duplicates
        candidate_hashes = set(sha256_16(c[1]) for c in candidates)
        all_same_hash = len(candidate_hashes) == 1 and len(candidates) > 1

        ambiguous = len(candidates) > 1 and not all_same_hash
        ambiguity_reason = ""
        if len(candidates) > 1:
            if all_same_hash:
                ambiguity_reason = "IDENTICAL_COPIES"  # Not a real ambiguity
            else:
                # Determine reason
                rules_used = set(c[0] for c in candidates)
                if 'SNAPSHOT' in rules_used and len(rules_used) > 1:
                    ambiguity_reason = "MULTI_TREE"
                elif len(rules_used) > 1:
                    ambiguity_reason = "MULTI_PATH"
                else:
                    ambiguity_reason = "DUPLICATE_NAME"

        # Check existence and compute hashes
        exists = resolved not in ["MISSING", "AMBIGUOUS"]
        size = file_size(resolved) if exists else 0
        sha = sha256_16(resolved) if exists else ""

        # Check snapshot drift
        status = "OK" if exists else "MISSING"
        if ambiguous:
            status = "AMBIGUOUS"
            # Check if any candidates have different hashes
            hashes = set()
            for _, cpath in candidates:
                h = sha256_16(cpath)
                if h:
                    hashes.add(h)
            if len(hashes) > 1:
                status = "STALE_SUSPECTED"

        assets.append({
            'asset_id': f"CH1-A{i:03d}",
            'type': ref['type'],
            'referenced_from': ref['file'].replace(str(SRC_ROOT) + '/', ''),
            'referenced_line': ref['line'],
            'latex_snippet': ref['snippet'],
            'raw_path': ref['raw_path'],
            'resolved_path': resolved if exists else "MISSING",
            'exists_on_disk': 'YES' if exists else 'NO',
            'size_bytes': size,
            'sha256_16': sha,
            'generator': 'NONE',
            'regeneration_cmd': '',
            'status': status,
            'action': 'NONE' if exists and not ambiguous else ('PLACEHOLDER' if not exists else 'TODO'),
            'notes': '',
            'candidates_found': len(candidates),
            'candidate_paths': ';'.join(c[1] for c in candidates),
            'candidate_sha256_16': ';'.join(sha256_16(c[1]) for c in candidates),
            'resolution_rule_used': rule,
            'ambiguous': 'YES' if ambiguous else 'NO',
            'ambiguity_reason': ambiguity_reason
        })

    # Generate outputs
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)

    # CSV
    csv_file = AUDIT_DIR / "CH1_ASSET_INDEX.csv"
    with open(csv_file, 'w', newline='') as f:
        if assets:
            writer = csv.DictWriter(f, fieldnames=assets[0].keys())
            writer.writeheader()
            writer.writerows(assets)
    print(f"Written: {csv_file}")

    # Markdown index
    md_file = AUDIT_DIR / "CH1_ASSET_INDEX.md"
    with open(md_file, 'w') as f:
        f.write("# CH1 Asset Index\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write("## Summary\n\n")
        f.write(f"| Metric | Count |\n|--------|-------|\n")
        f.write(f"| Total assets | {len(assets)} |\n")
        f.write(f"| Existing | {sum(1 for a in assets if a['exists_on_disk']=='YES')} |\n")
        f.write(f"| Missing | {sum(1 for a in assets if a['exists_on_disk']=='NO')} |\n")
        f.write(f"| Ambiguous | {sum(1 for a in assets if a['ambiguous']=='YES')} |\n")
        f.write(f"| Stale suspected | {sum(1 for a in assets if a['status']=='STALE_SUSPECTED')} |\n\n")

        f.write("## Asset List\n\n")
        f.write("| ID | Type | Raw Path | Status | Exists |\n")
        f.write("|----|------|----------|--------|--------|\n")
        for a in assets:
            f.write(f"| {a['asset_id']} | {a['type']} | `{a['raw_path']}` | {a['status']} | {a['exists_on_disk']} |\n")
    print(f"Written: {md_file}")

    # Gaps report
    gaps_file = AUDIT_DIR / "CH1_ASSET_GAPS.md"
    missing = [a for a in assets if a['exists_on_disk'] == 'NO']
    with open(gaps_file, 'w') as f:
        f.write("# CH1 Asset Gaps\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        if missing:
            f.write(f"## Missing Assets ({len(missing)})\n\n")
            for a in missing:
                f.write(f"### {a['asset_id']}: `{a['raw_path']}`\n\n")
                f.write(f"- **Referenced from**: {a['referenced_from']}:{a['referenced_line']}\n")
                f.write(f"- **LaTeX**: `{a['latex_snippet']}`\n")
                f.write(f"- **Action**: PLACEHOLDER needed\n")
                f.write(f"- **Closure**: Restore file OR regenerate via script\n\n")
        else:
            f.write("No missing assets found.\n")
    print(f"Written: {gaps_file}")

    # Ambiguities report
    amb_file = AUDIT_DIR / "CH1_ASSET_AMBIGUITIES.md"
    ambiguous = [a for a in assets if a['ambiguous'] == 'YES']
    with open(amb_file, 'w') as f:
        f.write("# CH1 Asset Ambiguities\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write("## Zero Ambiguity Gate Summary\n\n")
        f.write(f"| Metric | Count |\n|--------|-------|\n")
        f.write(f"| Total assets | {len(assets)} |\n")
        f.write(f"| Ambiguous | {len(ambiguous)} |\n")
        f.write(f"| Missing | {len(missing)} |\n")
        f.write(f"| Stale suspected | {sum(1 for a in assets if a['status']=='STALE_SUSPECTED')} |\n\n")

        if len(ambiguous) == 0:
            f.write("**GATE: PASS** (no ambiguities)\n\n")
        else:
            f.write("**GATE: FAIL** (ambiguities detected)\n\n")
            f.write("## Ambiguous Assets\n\n")
            for a in ambiguous:
                f.write(f"### {a['asset_id']}: `{a['raw_path']}`\n\n")
                f.write(f"- **Reason**: {a['ambiguity_reason']}\n")
                f.write(f"- **Candidates**:\n")
                paths = a['candidate_paths'].split(';')
                hashes = a['candidate_sha256_16'].split(';')
                for p, h in zip(paths, hashes):
                    f.write(f"  - `{p}` (sha: {h})\n")
                f.write(f"- **Recommendation**: Use explicit relative path or consolidate\n\n")
    print(f"Written: {amb_file}")

    # Gate report
    gate_file = AUDIT_DIR / "CH1_ASSET_GATE_REPORT.md"
    missing_without_plan = [a for a in assets if a['exists_on_disk'] == 'NO']
    gate_pass = len(ambiguous) == 0
    with open(gate_file, 'w') as f:
        f.write("# CH1 Asset Gate Report\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write("## Asset Gate\n\n")
        f.write(f"- Ambiguous count: {len(ambiguous)}\n")
        f.write(f"- Missing count: {len(missing)}\n")
        f.write(f"- **Result**: {'PASS' if gate_pass else 'FAIL'}\n\n")
        if not gate_pass:
            f.write("### Blockers\n\n")
            for a in ambiguous:
                f.write(f"- {a['asset_id']}: {a['raw_path']} ({a['ambiguity_reason']})\n")
        f.write("\n## Snapshot Drift Gate (Informational)\n\n")
        stale = [a for a in assets if a['status'] == 'STALE_SUSPECTED']
        f.write(f"- Stale suspected: {len(stale)}\n")
        f.write(f"- **Result**: PASS (informational only)\n")
    print(f"Written: {gate_file}")

    # Return exit code
    if gate_pass:
        print("\nAsset Gate: PASS")
        return 0
    else:
        print("\nAsset Gate: FAIL")
        return 1

if __name__ == "__main__":
    sys.exit(main())
