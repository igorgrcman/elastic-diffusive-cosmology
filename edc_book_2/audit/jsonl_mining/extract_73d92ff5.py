#!/usr/bin/env python3
"""
Full extraction script for 73d92ff5-39ec-459c-a15f-10648db8fe6d.jsonl
Theory Maturity/Gap Analysis session (~109 MB)
"""

import json
import re
import os
from collections import defaultdict
from datetime import datetime

INPUT_FILE = "/Users/igor/ClaudeAI/EDC_Project/dmining/projects/-Users-igor-ClaudeAI-EDC-Project-EDC-Research-PRIVATE/73d92ff5-39ec-459c-a15f-10648db8fe6d.jsonl"
OUTPUT_DIR = "/Users/igor/ClaudeAI/EDC_Project/elastic-diffusive-cosmology_repo/edc_book_2/audit/jsonl_mining/reports"

# Storage structures
all_messages = []
derivations = []
equations = []
gap_items = defaultdict(list)  # Route A, B, C, D, E, F
blockers = []
tier_classifications = {"tier1": [], "tier2": [], "tier3": []}
parameters = []
snippets = []

def extract_text_from_content(content):
    """Extract text from various content formats"""
    if isinstance(content, str):
        return content
    elif isinstance(content, list):
        texts = []
        for item in content:
            if isinstance(item, str):
                texts.append(item)
            elif isinstance(item, dict):
                if item.get('type') == 'text':
                    texts.append(item.get('text', ''))
                elif item.get('type') == 'thinking':
                    texts.append(item.get('thinking', ''))
                elif item.get('type') == 'tool_use':
                    inp = item.get('input', {})
                    if isinstance(inp, dict):
                        texts.append(str(inp))
                elif item.get('type') == 'tool_result':
                    texts.append(str(item.get('content', '')))
        return '\n'.join(texts)
    elif isinstance(content, dict):
        if content.get('type') == 'text':
            return content.get('text', '')
        return str(content)
    return ''

def extract_message_text(data):
    """Extract text from the new JSONL structure"""
    texts = []

    # Direct content field
    if 'content' in data:
        texts.append(extract_text_from_content(data['content']))

    # Nested message structure
    if 'message' in data:
        msg = data['message']
        if isinstance(msg, dict):
            if 'content' in msg:
                texts.append(extract_text_from_content(msg['content']))

    return '\n'.join(texts)

def find_equations(text):
    """Extract all equations from text"""
    found = []

    # Display math $$...$$
    display = re.findall(r'\$\$([^$]+)\$\$', text, re.DOTALL)
    for eq in display:
        found.append(('display', eq.strip()))

    # Inline math $...$
    inline = re.findall(r'(?<!\$)\$([^$\n]{3,})\$(?!\$)', text)
    for eq in inline:
        if not eq.startswith('$') and len(eq) > 3:
            found.append(('inline', eq.strip()))

    # LaTeX environments
    for env in ['equation', 'align', 'eqnarray', 'gather', 'multline']:
        pattern = rf'\\begin\{{{env}\*?\}}(.*?)\\end\{{{env}\*?\}}'
        matches = re.findall(pattern, text, re.DOTALL)
        for m in matches:
            found.append((env, m.strip()))

    # Key physics expressions (assignment style)
    phys_patterns = [
        r'([τℓℏωπαβγδεζηθκλμνξρστφχψΩΛΓΣΠΔ][_\d]*)\s*[=≈≡]\s*([\d\.\-\+eE×\^/\(\)\s]+(?:s|eV|GeV|MeV|fm|m)?)',
        r'(B̂|B_hat|Bhat)\s*[=≈≡]\s*([\d\.\-\+eE×\^/\(\)\s]+)',
        r'(d\s*ln\s*B[̂]?\s*/\s*d\s*ln\s*\w+)\s*[≈=]\s*([\d\.\-\+eE]+)',
        r'(\w+_\{?[A-Za-z0-9]+\}?)\s*=\s*([\d\.\-\+eE×\^]+(?:\s*\\times\s*10\^\{[\d\-]+\})?)',
    ]
    for pat in phys_patterns:
        matches = re.finditer(pat, text)
        for m in matches:
            found.append(('physics', m.group(0)))

    return found

def find_derivations(text, msg_index):
    """Find derivation blocks"""
    found = []

    # Look for derivation markers
    markers = [
        r'(?:Derivation|DERIVATION)[:\s\-–]+([^\n]+(?:\n(?![A-Z]{3,})[^\n]+){0,20})',
        r'(?:derive|deriving|derived)[:\s\-–]+([^\n]+(?:\n(?![A-Z]{3,})[^\n]+){0,10})',
        r'(?:proof|Proof|PROOF)[:\s\-–]+([^\n]+(?:\n(?![A-Z]{3,})[^\n]+){0,15})',
        r'(?:shows|showing|show)\s+(?:that|how)[:\s\-–]+([^\n]+(?:\n(?![A-Z]{3,})[^\n]+){0,10})',
        r'Step\s+\d+[a-z]?[:\s\-–]+([^\n]+(?:\n(?![A-Z]{3,}|Step)[^\n]+){0,15})',
    ]

    for pattern in markers:
        matches = re.finditer(pattern, text, re.IGNORECASE | re.MULTILINE)
        for m in matches:
            found.append({
                'index': msg_index,
                'type': 'derivation',
                'content': m.group(0)[:2000],
                'context': text[max(0, m.start()-100):m.end()+100][:2500]
            })

    return found

def find_gaps(text, msg_index):
    """Find gap analysis items"""
    found = defaultdict(list)

    route_patterns = [
        (r'(?:Route|ROUTE)\s*A[\s:\-–]*(.*?)(?=Route|ROUTE|$|\n\n)', 'A'),
        (r'(?:Route|ROUTE)\s*B[\s:\-–]*(.*?)(?=Route|ROUTE|$|\n\n)', 'B'),
        (r'(?:Route|ROUTE)\s*C[\s:\-–]*(.*?)(?=Route|ROUTE|$|\n\n)', 'C'),
        (r'(?:Route|ROUTE)\s*D[\s:\-–]*(.*?)(?=Route|ROUTE|$|\n\n)', 'D'),
        (r'(?:Route|ROUTE)\s*E[\s:\-–]*(.*?)(?=Route|ROUTE|$|\n\n)', 'E'),
        (r'(?:Route|ROUTE)\s*F[\s:\-–]*(.*?)(?=Route|ROUTE|$|\n\n)', 'F'),
    ]

    for pattern, route in route_patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE | re.DOTALL)
        for m in matches:
            found[route].append({
                'index': msg_index,
                'content': m.group(0)[:1500],
                'context': text[max(0, m.start()-50):m.end()+200][:2000]
            })

    # GAP-N patterns
    gap_matches = re.finditer(r'GAP[-\s]*(\d+)[\s:\-–]*(.*?)(?=GAP[-\s]*\d+|$|\n\n)', text, re.IGNORECASE | re.DOTALL)
    for m in gap_matches:
        gap_num = m.group(1)
        found[f'GAP-{gap_num}'].append({
            'index': msg_index,
            'content': m.group(0)[:1500],
            'context': text[max(0, m.start()-50):m.end()+200][:2000]
        })

    return found

def find_blockers(text, msg_index):
    """Find blocker definitions"""
    found = []

    blocker_patterns = [
        r'(?:blocker|BLOCKER|Blocker)[\s:\-–]*(.*?)(?=blocker|BLOCKER|$|\n\n)',
        r'(?:blocked|BLOCKED)[\s:\-–by]*(.*?)(?=blocked|$|\n\n)',
        r'(?:blocking|BLOCKING)[\s:\-–]*(.*?)(?=blocking|$|\n\n)',
        r'(?:obstacle|OBSTACLE)[\s:\-–]*(.*?)(?=obstacle|$|\n\n)',
        r'(?:impediment|IMPEDIMENT)[\s:\-–]*(.*?)(?=impediment|$|\n\n)',
        r'(?:uncertainty|UNCERTAINTY)[\s:\-–]*(.*?)(?=uncertainty|$|\n\n)',
        r'(?:epistemic|EPISTEMIC)[\s:\-–]*(.*?)(?=epistemic|$|\n\n)',
    ]

    for pattern in blocker_patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE | re.DOTALL)
        for m in matches:
            found.append({
                'index': msg_index,
                'type': 'blocker',
                'content': m.group(0)[:1000],
                'context': text[max(0, m.start()-100):m.end()+200][:1500]
            })

    return found

def find_tiers(text, msg_index):
    """Find tier classifications"""
    found = {"tier1": [], "tier2": [], "tier3": []}

    tier_patterns = [
        (r'(?:Tier|TIER)\s*1[\s:\-–]*(.*?)(?=Tier|TIER|$|\n\n)', 'tier1'),
        (r'(?:Tier|TIER)\s*2[\s:\-–]*(.*?)(?=Tier|TIER|$|\n\n)', 'tier2'),
        (r'(?:Tier|TIER)\s*3[\s:\-–]*(.*?)(?=Tier|TIER|$|\n\n)', 'tier3'),
        (r'(?:Tier|TIER)\s*I(?!\w)[\s:\-–]*(.*?)(?=Tier|TIER|$|\n\n)', 'tier1'),
        (r'(?:Tier|TIER)\s*II(?!\w)[\s:\-–]*(.*?)(?=Tier|TIER|$|\n\n)', 'tier2'),
        (r'(?:Tier|TIER)\s*III(?!\w)[\s:\-–]*(.*?)(?=Tier|TIER|$|\n\n)', 'tier3'),
    ]

    for pattern, tier in tier_patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE | re.DOTALL)
        for m in matches:
            found[tier].append({
                'index': msg_index,
                'content': m.group(0)[:1000],
                'context': text[max(0, m.start()-50):m.end()+200][:1500]
            })

    return found

def find_parameters(text, msg_index):
    """Find parameter definitions"""
    found = []

    param_patterns = [
        # Physics parameters with units
        (r'([τℓℏωπαβγδεζηθκλμνξρστφχψΩΛΓΣΠΔ][_\d]*)\s*[=≈≡]\s*([0-9\.\-\+eE×\^]+(?:\s*(?:eV|GeV|MeV|TeV|keV|fm|cm|m|s|kg|K|Hz|J|W))?)', 'greek'),
        # Standard variable assignments
        (r'([A-Za-z_][A-Za-z_\d]*)\s*[=≈≡]\s*([0-9\.\-\+eE×\^]+(?:\s*(?:eV|GeV|MeV|TeV|keV|fm|cm|m|s|kg|K|Hz|J|W))?)', 'standard'),
        # LaTeX style
        (r'\\([A-Za-z]+)\s*[=≈≡]\s*([0-9\.\-\+eE×\^\\{}]+)', 'latex'),
        # Specific physics quantities
        (r'(B̂|B_hat|Bhat|tau|w_star|R_rms|R0|w\*)\s*[=≈≡]\s*([\d\.\-\+eE×\^/\(\)\s]+)', 'physics'),
        # Tagged definitions [Def], [Cal], [DIAG]
        (r'\[(?:Def|DEF|Cal|CAL|DIAG|diag)\]\s*([A-Za-z_τℓℏω][A-Za-z_\d]*)\s*[=≈≡]\s*([^\n\[\]]+)', 'tagged'),
    ]

    for pattern, ptype in param_patterns:
        matches = re.finditer(pattern, text)
        for m in matches:
            found.append({
                'index': msg_index,
                'parameter': m.group(1),
                'value': m.group(2),
                'param_type': ptype,
                'context': text[max(0, m.start()-50):m.end()+50][:300]
            })

    return found

def find_epistemic_tags(text, msg_index):
    """Find epistemic tagging [Def], [Cal], [DIAG], etc."""
    found = []

    tag_pattern = r'\[(Def|DEF|Cal|CAL|DIAG|Emp|EMP|Fit|FIT|Approx|APPROX|Hyp|HYP)\]([^\n\[]+)'
    matches = re.finditer(tag_pattern, text, re.IGNORECASE)
    for m in matches:
        found.append({
            'index': msg_index,
            'tag': m.group(1).upper(),
            'content': m.group(2).strip()[:500],
            'context': text[max(0, m.start()-30):m.end()+30][:600]
        })

    return found

def process_file():
    """Main processing function"""
    global all_messages, derivations, equations, gap_items, blockers, tier_classifications, parameters, snippets

    print(f"Processing {INPUT_FILE}...")

    line_count = 0
    msg_count = 0
    epistemic_tags = []

    with open(INPUT_FILE, 'r', encoding='utf-8', errors='replace') as f:
        for line in f:
            line_count += 1
            if line_count % 2000 == 0:
                print(f"  Processed {line_count} lines, extracted {msg_count} messages...")

            try:
                data = json.loads(line.strip())
            except json.JSONDecodeError:
                continue

            # Skip non-message entries
            entry_type = data.get('type', '')
            if entry_type in ['file-history-snapshot', 'summary']:
                continue

            # Extract message content using the new structure
            text = extract_message_text(data)

            if not text or len(text) < 10:
                continue

            msg_count += 1
            role = data.get('type', data.get('message', {}).get('role', 'unknown'))

            all_messages.append({
                'index': msg_count,
                'role': role,
                'uuid': data.get('uuid', ''),
                'timestamp': data.get('timestamp', ''),
                'text': text[:50000]
            })

            # Extract all components
            eqs = find_equations(text)
            for eq_type, eq_content in eqs:
                equations.append({
                    'index': msg_count,
                    'type': eq_type,
                    'equation': eq_content
                })

            derivations.extend(find_derivations(text, msg_count))

            gaps = find_gaps(text, msg_count)
            for route, items in gaps.items():
                gap_items[route].extend(items)

            blockers.extend(find_blockers(text, msg_count))

            tiers = find_tiers(text, msg_count)
            for tier, items in tiers.items():
                tier_classifications[tier].extend(items)

            parameters.extend(find_parameters(text, msg_count))
            epistemic_tags.extend(find_epistemic_tags(text, msg_count))

    print(f"Total lines: {line_count}, Messages extracted: {msg_count}")
    return msg_count, epistemic_tags

def write_full_report(epistemic_tags):
    """Write the full report markdown"""
    filepath = os.path.join(OUTPUT_DIR, "73d92ff5_full.md")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("# Full Extraction Report: 73d92ff5-39ec-459c-a15f-10648db8fe6d.jsonl\n\n")
        f.write(f"**Generated**: {datetime.now().isoformat()}\n\n")
        f.write("**Session Type**: Theory Maturity/Gap Analysis\n\n")
        f.write("---\n\n")

        # Summary
        f.write("## Summary Statistics\n\n")
        f.write(f"- Total messages extracted: {len(all_messages)}\n")
        f.write(f"- Equations found: {len(equations)}\n")
        f.write(f"- Derivations found: {len(derivations)}\n")
        f.write(f"- Blockers found: {len(blockers)}\n")
        f.write(f"- Parameters found: {len(parameters)}\n")
        f.write(f"- Epistemic tags found: {len(epistemic_tags)}\n")
        f.write(f"- Gap items by route:\n")
        for route in sorted(gap_items.keys()):
            f.write(f"  - {route}: {len(gap_items[route])}\n")
        f.write(f"- Tier classifications:\n")
        for tier, items in tier_classifications.items():
            f.write(f"  - {tier}: {len(items)}\n")
        f.write("\n---\n\n")

        # Derivations
        f.write("## Derivations\n\n")
        for i, d in enumerate(derivations[:100], 1):
            f.write(f"### Derivation {i} (Message {d['index']})\n\n")
            f.write(f"```\n{d['content'][:1500]}\n```\n\n")
        if len(derivations) > 100:
            f.write(f"*... and {len(derivations) - 100} more derivations*\n\n")
        f.write("---\n\n")

        # Gap Analysis
        f.write("## Gap Analysis (Routes A-F and GAP-N)\n\n")
        for route in sorted(gap_items.keys()):
            f.write(f"### {route}\n\n")
            for i, item in enumerate(gap_items[route][:50], 1):
                f.write(f"**Item {i}** (Message {item['index']}):\n")
                f.write(f"```\n{item['content'][:1000]}\n```\n\n")
            if len(gap_items[route]) > 50:
                f.write(f"*... and {len(gap_items[route]) - 50} more items*\n\n")
        f.write("---\n\n")

        # Blockers
        f.write("## Blockers and Uncertainties\n\n")
        for i, b in enumerate(blockers[:50], 1):
            f.write(f"### Blocker {i} (Message {b['index']})\n\n")
            f.write(f"```\n{b['content'][:800]}\n```\n\n")
        if len(blockers) > 50:
            f.write(f"*... and {len(blockers) - 50} more blockers*\n\n")
        f.write("---\n\n")

        # Tier Classifications
        f.write("## Tier Classifications\n\n")
        for tier in ['tier1', 'tier2', 'tier3']:
            f.write(f"### {tier.upper()}\n\n")
            for i, item in enumerate(tier_classifications[tier][:30], 1):
                f.write(f"**Item {i}** (Message {item['index']}):\n")
                f.write(f"```\n{item['content'][:600]}\n```\n\n")
            if len(tier_classifications[tier]) > 30:
                f.write(f"*... and {len(tier_classifications[tier]) - 30} more items*\n\n")
        f.write("---\n\n")

        # Epistemic Tags
        f.write("## Epistemic Tags\n\n")
        tags_by_type = defaultdict(list)
        for t in epistemic_tags:
            tags_by_type[t['tag']].append(t)

        for tag_type in sorted(tags_by_type.keys()):
            f.write(f"### [{tag_type}] Tags ({len(tags_by_type[tag_type])})\n\n")
            for i, t in enumerate(tags_by_type[tag_type][:30], 1):
                f.write(f"- (Msg {t['index']}): {t['content'][:200]}\n")
            if len(tags_by_type[tag_type]) > 30:
                f.write(f"*... and {len(tags_by_type[tag_type]) - 30} more*\n\n")
        f.write("---\n\n")

        # Parameters
        f.write("## Parameters\n\n")
        f.write("| Parameter | Value | Type | Message | Context |\n")
        f.write("|-----------|-------|------|---------|--------|\n")
        seen_params = set()
        for p in parameters[:200]:
            key = (p['parameter'], p['value'])
            if key not in seen_params:
                seen_params.add(key)
                ctx = p['context'].replace('\n', ' ').replace('|', '\\|')[:80]
                f.write(f"| {p['parameter']} | {p['value']} | {p.get('param_type', 'unknown')} | {p['index']} | {ctx} |\n")
        if len(parameters) > 200:
            f.write(f"\n*... and more parameters (showing unique values)*\n\n")

        # Sample messages
        f.write("\n---\n\n## Sample Messages (every 10th)\n\n")
        for m in all_messages[::10][:50]:
            f.write(f"### Message {m['index']} ({m['role']})\n\n")
            f.write(f"**Timestamp**: {m.get('timestamp', 'N/A')}\n\n")
            f.write(f"```\n{m['text'][:2000]}\n```\n\n")

    print(f"Wrote: {filepath}")

def write_equations_report():
    """Write the equations report markdown"""
    filepath = os.path.join(OUTPUT_DIR, "73d92ff5_equations.md")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("# Equations Extracted: 73d92ff5-39ec-459c-a15f-10648db8fe6d.jsonl\n\n")
        f.write(f"**Generated**: {datetime.now().isoformat()}\n\n")
        f.write(f"**Total Equations**: {len(equations)}\n\n")
        f.write("---\n\n")

        # Group by type
        by_type = defaultdict(list)
        for eq in equations:
            by_type[eq['type']].append(eq)

        for eq_type in sorted(by_type.keys()):
            f.write(f"## {eq_type.capitalize()} Equations ({len(by_type[eq_type])})\n\n")

            # Deduplicate
            seen = set()
            count = 0
            for eq in by_type[eq_type]:
                eq_clean = eq['equation'].strip()
                if eq_clean not in seen and len(eq_clean) > 3:
                    seen.add(eq_clean)
                    count += 1
                    if count <= 200:
                        f.write(f"**Eq {count}** (Msg {eq['index']}):\n")
                        if eq_type == 'display':
                            f.write(f"$$\n{eq_clean}\n$$\n\n")
                        elif eq_type == 'inline':
                            f.write(f"$${eq_clean}$$\n\n")
                        else:
                            f.write(f"```latex\n{eq_clean}\n```\n\n")

            if count > 200:
                f.write(f"*... and {count - 200} more unique equations*\n\n")
            f.write("---\n\n")

    print(f"Wrote: {filepath}")

def write_snippets_json(epistemic_tags):
    """Write the snippets JSON file"""
    filepath = os.path.join(OUTPUT_DIR, "73d92ff5_snippets.json")

    output = {
        "metadata": {
            "source": "73d92ff5-39ec-459c-a15f-10648db8fe6d.jsonl",
            "generated": datetime.now().isoformat(),
            "session_type": "Theory Maturity/Gap Analysis"
        },
        "counts": {
            "messages": len(all_messages),
            "equations": len(equations),
            "derivations": len(derivations),
            "blockers": len(blockers),
            "parameters": len(parameters),
            "epistemic_tags": len(epistemic_tags),
            "gap_items": {k: len(v) for k, v in gap_items.items()},
            "tier_classifications": {k: len(v) for k, v in tier_classifications.items()}
        },
        "equations": equations[:500],
        "derivations": derivations[:100],
        "blockers": blockers[:100],
        "parameters": parameters[:300],
        "epistemic_tags": epistemic_tags[:200],
        "gap_items": {k: v[:50] for k, v in gap_items.items()},
        "tier_classifications": {k: v[:50] for k, v in tier_classifications.items()},
        "sample_messages": [m for m in all_messages[::10]][:100]
    }

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Wrote: {filepath}")

if __name__ == "__main__":
    msg_count, epistemic_tags = process_file()
    write_full_report(epistemic_tags)
    write_equations_report()
    write_snippets_json(epistemic_tags)

    print("\n=== EXTRACTION COMPLETE ===")
    print(f"Messages: {len(all_messages)}")
    print(f"Equations: {len(equations)}")
    print(f"Derivations: {len(derivations)}")
    print(f"Blockers: {len(blockers)}")
    print(f"Parameters: {len(parameters)}")
    print(f"Epistemic tags: {len(epistemic_tags)}")
    print(f"Gap items: {sum(len(v) for v in gap_items.values())}")
    print(f"Tier items: {sum(len(v) for v in tier_classifications.values())}")
