#!/usr/bin/env python3
"""
Prelet (jump) scan for EDC Book 2.
Detects narrative/derivation jumps and maps them to LaTeX sources.
"""

import os
import re
import json
import subprocess
from pathlib import Path
from collections import defaultdict

# Trigger phrases that indicate potential gaps
TRIGGER_PATTERNS = [
    # English - strong inference markers
    r'\btherefore\b', r'\bthus\b', r'\bhence\b', r'\bit follows that\b',
    r'\bimplies\b', r'\bguarantees\b', r'\byields\b', r'\bwe obtain\b',
    r'\bwe conclude\b', r'\bconclusion\b',
    # English - obviousness claims
    r'\bit is clear\b', r'\bobviously\b', r'\bstraightforward\b',
    r'\bone can show\b', r'\bas is well known\b', r'\btrivially\b',
    r'\bclearly\b', r'\bevident\b',
    # English - derivation references
    r'\bfollows from\b', r'\bby symmetry\b', r'\bby inspection\b',
    r'\bwe identify\b', r'\bis identified with\b', r'\bidentification\b',
    # English - mapping/dictionary
    r'\bcorresponds to\b', r'\bmaps to\b', r'\bdictionary\b',
    r'\banchored by\b', r'\bcalibrated to\b', r'\bmatches\b',
    # Croatian
    r'\bdakle\b', r'\bstoga\b', r'\bslijedi\b', r'\bimplicira\b',
    r'\bjamči\b', r'\bočito\b', r'\bjasno je\b', r'\btrivijalno\b',
    r'\bpoznato je\b', r'\bvidimo da\b', r'\bzaključujemo\b',
    r'\bidentificiramo\b', r'\bodgovara\b',
]

# Compile patterns
TRIGGER_REGEX = re.compile('|'.join(TRIGGER_PATTERNS), re.IGNORECASE)

# SM terms that might indicate dictionary-step issues
SM_TERMS = [
    r'\bW boson\b', r'\bZ boson\b', r'\bM_W\b', r'\bM_Z\b',
    r'\bCKM\b', r'\bPMNS\b', r'\bFermi\b', r'\bG_F\b',
    r'\bWeinberg\b', r'\btheta_W\b', r'\bsin.*theta\b',
    r'\bHiggs\b', r'\belectroweak\b',
]
SM_REGEX = re.compile('|'.join(SM_TERMS), re.IGNORECASE)


def extract_pages(pdf_path: str, output_dir: str) -> list:
    """Extract text from each page of the PDF."""
    pages = []
    # Get total pages
    result = subprocess.run(['pdfinfo', pdf_path], capture_output=True, text=True)
    total_pages = 145  # default
    for line in result.stdout.split('\n'):
        if line.startswith('Pages:'):
            total_pages = int(line.split(':')[1].strip())
            break

    # Extract each page
    for page_num in range(1, total_pages + 1):
        output_file = os.path.join(output_dir, f'page_{page_num:03d}.txt')
        subprocess.run([
            'pdftotext', '-f', str(page_num), '-l', str(page_num),
            '-layout', pdf_path, output_file
        ], capture_output=True)

        if os.path.exists(output_file):
            with open(output_file, 'r', encoding='utf-8', errors='replace') as f:
                text = f.read()
                pages.append({'page': page_num, 'text': text})

    return pages


def find_triggers(text: str, page_num: int) -> list:
    """Find trigger phrases in text and extract snippets."""
    findings = []
    sentences = re.split(r'(?<=[.!?])\s+', text)

    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) < 10:
            continue

        matches = TRIGGER_REGEX.findall(sentence)
        if matches:
            # Get snippet (max 200 chars)
            snippet = sentence[:200] + ('...' if len(sentence) > 200 else '')

            # Classify type
            gap_type = classify_gap(sentence)

            # Check for SM terms
            has_sm = bool(SM_REGEX.search(sentence))

            findings.append({
                'page': page_num,
                'trigger': matches[0].lower(),
                'snippet': snippet,
                'type': gap_type,
                'has_sm_terms': has_sm,
                'full_sentence': sentence,
            })

    return findings


def classify_gap(sentence: str) -> str:
    """Classify gap type: A (definition), B (derivation), C (narrative jump)."""
    s_lower = sentence.lower()

    # Type A: Missing definition indicators
    if any(w in s_lower for w in ['define', 'notation', 'symbol', 'denote', 'let']):
        return 'A'
    if re.search(r'\b[a-z]_\{?\w+\}?\s*(is|=|denotes)', s_lower):
        return 'A'

    # Type B: Missing derivation indicators
    if any(w in s_lower for w in ['one can show', 'it follows', 'we obtain',
                                   'straightforward', 'trivial', 'proof']):
        return 'B'
    if re.search(r'(derive|derivation|equation|formula)', s_lower):
        return 'B'

    # Type C: Narrative/mechanism jump
    if any(w in s_lower for w in ['physical', 'mechanism', 'interpret',
                                   'dictionary', 'identifies', 'maps to']):
        return 'C'

    # Default to B (most common)
    return 'B'


def map_to_latex(snippet: str, tex_files: list) -> tuple:
    """Try to map snippet to LaTeX source file and line."""
    # Clean snippet for searching
    clean_snippet = re.sub(r'\$[^$]+\$', '', snippet)  # Remove math
    clean_snippet = re.sub(r'\\[a-zA-Z]+\{[^}]*\}', '', clean_snippet)  # Remove commands
    clean_snippet = re.sub(r'\s+', ' ', clean_snippet).strip()

    # Get key words (3+ chars, not common)
    words = [w for w in clean_snippet.split() if len(w) >= 4 and w.lower() not in
             {'that', 'this', 'with', 'from', 'have', 'been', 'were', 'will', 'into'}]

    if len(words) < 2:
        return None, None

    # Search pattern: first few significant words
    search_phrase = ' '.join(words[:4])

    for tex_file in tex_files:
        if not os.path.exists(tex_file):
            continue
        try:
            result = subprocess.run(
                ['grep', '-n', '-i', words[0], tex_file],
                capture_output=True, text=True
            )
            for line in result.stdout.split('\n'):
                if line and ':' in line:
                    line_num = int(line.split(':')[0])
                    line_content = ':'.join(line.split(':')[1:])
                    # Check if multiple words match
                    matches = sum(1 for w in words[:4] if w.lower() in line_content.lower())
                    if matches >= 2:
                        return tex_file, line_num
        except Exception:
            pass

    return None, None


def infer_chapter(tex_file: str, page_num: int) -> str:
    """Infer chapter from tex filename or page number."""
    if tex_file:
        # Extract chapter number from filename
        match = re.search(r'chapter_(\d+)', tex_file)
        if match:
            return f'CH{match.group(1).zfill(2)}'
        if 'bridge' in tex_file.lower():
            return 'CH00'
        if 'notation' in tex_file.lower():
            return 'APP-N'

    # Estimate from page number (rough mapping)
    if page_num <= 10:
        return 'FRONT'
    elif page_num <= 20:
        return 'CH00'
    elif page_num <= 35:
        return 'CH01'
    elif page_num <= 50:
        return 'CH02-05'
    elif page_num <= 80:
        return 'CH06-09'
    elif page_num <= 110:
        return 'CH10-13'
    elif page_num <= 135:
        return 'CH14-16'
    else:
        return 'CH17-APP'


def generate_id(chapter: str, page: int, seq: int) -> str:
    """Generate stable GAPFIX ID."""
    return f'GAPFIX-{chapter}-P{page:03d}-{seq:02d}'


def main():
    # Configuration
    pdf_path = 'main.pdf'
    tmp_dir = 'audit/_tmp_pages'
    output_report = 'audit/prelet_scan_report.md'
    output_json = 'audit/prelet_scan_findings.json'

    # Find all tex files
    tex_files = []
    for pattern in ['*.tex', 'part1/*.tex', 'part2/*.tex', 'part3/*.tex',
                    'epilogue/*.tex', 'bridge/*.tex', 'appendices/*.tex',
                    'includes/*.tex', 'frontmatter/*.tex']:
        tex_files.extend([str(p) for p in Path('.').glob(pattern)])

    print(f"Found {len(tex_files)} LaTeX files")
    print(f"Extracting pages from {pdf_path}...")

    # Extract pages
    os.makedirs(tmp_dir, exist_ok=True)
    pages = extract_pages(pdf_path, tmp_dir)
    print(f"Extracted {len(pages)} pages")

    # Find all triggers
    all_findings = []
    page_counters = defaultdict(int)

    for page_data in pages:
        page_num = page_data['page']
        findings = find_triggers(page_data['text'], page_num)

        for f in findings:
            page_counters[page_num] += 1
            seq = page_counters[page_num]

            # Map to LaTeX
            tex_file, tex_line = map_to_latex(f['snippet'], tex_files)
            chapter = infer_chapter(tex_file, page_num)

            finding = {
                'id': generate_id(chapter, page_num, seq),
                'pdf_page': page_num,
                'trigger': f['trigger'],
                'snippet': f['snippet'],
                'type': f['type'],
                'tex_file': tex_file,
                'tex_line': tex_line,
                'chapter': chapter,
                'notes': []
            }

            if f['has_sm_terms']:
                finding['notes'].append('sm_risk')
            if 'dictionary' in f['trigger'] or 'identif' in f['trigger']:
                finding['notes'].append('dictionary_step')
            if tex_file is None:
                finding['notes'].append('UNRESOLVED')

            all_findings.append(finding)

    print(f"Found {len(all_findings)} potential gaps")

    # Filter to most significant (limit per page to avoid noise)
    significant_findings = []
    page_counts = defaultdict(int)
    for f in all_findings:
        if page_counts[f['pdf_page']] < 3:  # Max 3 per page
            significant_findings.append(f)
            page_counts[f['pdf_page']] += 1

    print(f"Selected {len(significant_findings)} significant findings")

    # Generate report
    generate_report(significant_findings, output_report, len(pages))

    # Save JSON
    with open(output_json, 'w') as f:
        json.dump(significant_findings, f, indent=2)
    print(f"Saved JSON to {output_json}")

    # Return findings for patching
    return significant_findings


def generate_report(findings: list, output_path: str, total_pages: int):
    """Generate markdown report."""
    # Count stats
    total = len(findings)
    mapped = sum(1 for f in findings if f['tex_file'])
    unresolved = total - mapped
    by_type = {'A': 0, 'B': 0, 'C': 0}
    for f in findings:
        by_type[f['type']] += 1

    report = f"""# Prelet Scan Report - EDC Part II (Weak Sector)

## Summary

- **Total pages scanned**: {total_pages}
- **Total findings**: {total}
- **Mapped to LaTeX**: {mapped}
- **Unresolved mappings**: {unresolved}

### By Type
- **Type A** (missing definition): {by_type['A']}
- **Type B** (missing derivation): {by_type['B']}
- **Type C** (narrative/mechanism jump): {by_type['C']}

## Findings

| ID | PDF Page | Trigger | Snippet | Type | Target LaTeX | Backfill Plan | Notes |
|----|----------|---------|---------|------|--------------|---------------|-------|
"""

    for f in findings:
        tex_target = f'{f["tex_file"]}:{f["tex_line"]}' if f['tex_file'] else 'UNRESOLVED'
        snippet_short = f['snippet'][:60] + '...' if len(f['snippet']) > 60 else f['snippet']
        snippet_short = snippet_short.replace('|', '\\|').replace('\n', ' ')

        # Backfill plan based on type
        if f['type'] == 'A':
            plan = 'Add symbol definition in notation.tex or inline'
        elif f['type'] == 'B':
            plan = 'Add 5-15 lines + 1-3 eq; tag [Der] vs [Dc]'
        else:
            plan = 'Add mechanism box or dictionary step'

        notes = ', '.join(f['notes']) if f['notes'] else '-'

        report += f"| {f['id']} | {f['pdf_page']} | {f['trigger']} | {snippet_short} | {f['type']} | {tex_target} | {plan} | {notes} |\n"

    report += """

## Legend

- **Type A**: Missing definition - symbol appears without definition
- **Type B**: Missing derivation - intermediate steps missing, "one can show" without proof
- **Type C**: Narrative/mechanism jump - math-to-physics leap, SM language risk

## Next Steps

1. For each RESOLVED finding: insert GAPFIX comment marker in LaTeX source
2. For Type A: add minimal definition in notation.tex
3. For Type B/C with sm_risk: recommend dictionary-box placement
4. Backfill from 461-page version where applicable
"""

    with open(output_path, 'w') as f:
        f.write(report)
    print(f"Saved report to {output_path}")


if __name__ == '__main__':
    findings = main()
