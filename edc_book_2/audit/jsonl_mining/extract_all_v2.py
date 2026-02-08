#!/usr/bin/env python3
"""
Full extraction script for JSONL conversation files (v2).
Handles Claude Code JSONL format with nested content.
Extracts ALL derivations, equations, parameters, and blocked items.
"""

import json
import re
import sys
from pathlib import Path
from collections import defaultdict
import hashlib

def extract_text_from_message(data):
    """Extract all text content from a JSONL message entry."""
    texts = []
    role = data.get('type', 'unknown')

    # Handle message field
    if 'message' in data:
        msg = data['message']
        if isinstance(msg, dict):
            role = msg.get('role', role)
            content = msg.get('content', '')

            if isinstance(content, str):
                texts.append(content)
            elif isinstance(content, list):
                for item in content:
                    if isinstance(item, str):
                        texts.append(item)
                    elif isinstance(item, dict):
                        if 'text' in item:
                            texts.append(item['text'])
                        if 'thinking' in item:
                            texts.append(item['thinking'])

    # Handle direct content field
    if 'content' in data:
        content = data['content']
        if isinstance(content, str):
            texts.append(content)
        elif isinstance(content, list):
            for item in content:
                if isinstance(item, str):
                    texts.append(item)
                elif isinstance(item, dict) and 'text' in item:
                    texts.append(item['text'])

    return '\n'.join(texts), role

def extract_equations(text):
    """Extract all LaTeX equations from text."""
    equations = []
    seen = set()

    # Display math: $$ ... $$
    for match in re.finditer(r'\$\$(.+?)\$\$', text, re.DOTALL):
        eq = match.group(1).strip()
        if len(eq) > 3 and eq not in seen:
            seen.add(eq)
            equations.append(('display', eq))

    # \[ ... \]
    for match in re.finditer(r'\\\[(.+?)\\\]', text, re.DOTALL):
        eq = match.group(1).strip()
        if len(eq) > 3 and eq not in seen:
            seen.add(eq)
            equations.append(('display-bracket', eq))

    # \begin{equation} ... \end{equation}
    for match in re.finditer(r'\\begin\{equation\*?\}(.+?)\\end\{equation\*?\}', text, re.DOTALL):
        eq = match.group(1).strip()
        if len(eq) > 3 and eq not in seen:
            seen.add(eq)
            equations.append(('equation', eq))

    # \begin{align} ... \end{align}
    for match in re.finditer(r'\\begin\{align\*?\}(.+?)\\end\{align\*?\}', text, re.DOTALL):
        eq = match.group(1).strip()
        if len(eq) > 3 and eq not in seen:
            seen.add(eq)
            equations.append(('align', eq))

    # Inline important equations: X = ... (with key physics terms)
    physics_terms = r'(?:G|c|ℏ|σ|F_bulk|M_5|g_5|κ|α|Λ|ℓ|R_ξ|L_0|R_p|Δ|m_n|τ_n|sin.*θ|cos.*θ|tan.*θ)'
    inline_pattern = rf'({physics_terms})\s*[=≈]\s*([^\n,;]+)'
    for match in re.finditer(inline_pattern, text):
        eq = match.group(0).strip()
        if len(eq) > 5 and eq not in seen:
            seen.add(eq)
            equations.append(('inline-physics', eq))

    # Numerical results: X = number (with units)
    num_pattern = r'([A-Za-zα-ωΑ-Ω_][A-Za-z0-9_]*)\s*[=≈]\s*([\d.]+(?:\s*[×x]\s*10\^?\{?[-\d]+\}?)?)\s*(eV|GeV|MeV|TeV|keV|fm|m|s|Hz|K|kg|J|W|m/s²?)?'
    for match in re.finditer(num_pattern, text):
        eq = match.group(0).strip()
        if len(eq) > 3 and eq not in seen:
            seen.add(eq)
            equations.append(('numerical', eq))

    return equations

def extract_derivation_chains(text):
    """Extract derivation chains and logical steps."""
    derivations = []

    # Multi-step derivations with "Step N" format
    step_blocks = re.findall(r'((?:Step\s*\d+[:\.\)]?\s*.+?\n?)+)', text, re.IGNORECASE | re.DOTALL)
    for block in step_blocks:
        if len(block) > 50:
            derivations.append(('step-chain', block[:2000]))

    # Numbered derivations (1. ... 2. ... etc)
    numbered_blocks = re.findall(r'((?:\d+\.\s+.+?\n)+)', text)
    for block in numbered_blocks:
        if len(block) > 100 and ('=' in block or 'therefore' in block.lower()):
            derivations.append(('numbered', block[:1500]))

    # "From X ... we get/obtain Y" patterns
    from_patterns = [
        r'From\s+(.+?)\s*(?:we\s+(?:get|obtain|find|have|derive)|this\s+gives)',
        r'Starting\s+(?:from|with)\s+(.+?)\s*(?:we\s+(?:get|obtain|find)|,)',
        r'Using\s+(.+?)\s*(?:we\s+(?:get|obtain|find|have)|gives|yields)',
        r'Substituting\s+(.+?)\s*(?:into|gives|yields|we\s+get)',
        r'Combining\s+(.+?)\s*(?:gives|yields|we\s+(?:get|obtain))',
    ]
    for pattern in from_patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE | re.DOTALL):
            content = match.group(0)
            if len(content) > 30:
                derivations.append(('logic-chain', content[:500]))

    # "Therefore/Thus/Hence" conclusions
    conclusion_pattern = r'(?:Therefore|Thus|Hence|It follows|This gives|This yields|We obtain|We find)[:\s]+(.+?)(?:\n\n|$)'
    for match in re.finditer(conclusion_pattern, text, re.IGNORECASE | re.DOTALL):
        content = match.group(0)
        if len(content) > 20:
            derivations.append(('conclusion', content[:500]))

    # "Proof/Derivation" blocks
    proof_pattern = r'(?:Proof|Derivation|Calculation|Analysis)[:\.\s]+(.+?)(?:QED|□|∎|\n\n\n|$)'
    for match in re.finditer(proof_pattern, text, re.IGNORECASE | re.DOTALL):
        content = match.group(0)
        if len(content) > 100:
            derivations.append(('proof', content[:2000]))

    # Key physics derivations (specific EDC terms)
    edc_patterns = [
        r'(?:G\s*=|Newton.*constant|gravitational\s+constant).+?(?:\n\n|$)',
        r'(?:F_bulk|bulk\s+force).+?(?:\n\n|$)',
        r'(?:membrane\s+tension|σ\s*=).+?(?:\n\n|$)',
        r'(?:neutron\s+lifetime|τ_n).+?(?:\n\n|$)',
        r'(?:sin²θ|Weinberg|weak\s+mixing).+?(?:\n\n|$)',
        r'(?:α\s*=|fine.structure).+?(?:\n\n|$)',
        r'(?:Fermi\s+constant|G_F).+?(?:\n\n|$)',
        r'(?:Yukawa|coupling).+?(?:\n\n|$)',
    ]
    for pattern in edc_patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE | re.DOTALL):
            content = match.group(0)
            if len(content) > 50:
                derivations.append(('edc-physics', content[:1000]))

    return derivations

def extract_parameters(text):
    """Extract numerical parameters and constants."""
    params = []
    seen = set()

    # Standard parameter definitions
    patterns = [
        # Name = value with optional units
        r'([A-Za-z_][A-Za-z0-9_]*)\s*[=≈]\s*([\d.]+(?:\s*[×x]\s*10\^?\{?[-\d]+\}?)?)\s*(eV|GeV|MeV|TeV|keV|fm|m|s|Hz|K|kg|J|W|m/s²?)?',
        # Greek letters
        r'([α-ωΑ-Ω](?:_[A-Za-z0-9]+)?)\s*[=≈]\s*([\d.]+(?:\s*[×x]\s*10\^?\{?[-\d]+\}?)?)',
        # LaTeX-style
        r'\\([A-Za-z]+)\s*[=≈]\s*([\d.]+(?:\s*\\times\s*10\^\{?[-\d]+\}?)?)',
    ]

    for pattern in patterns:
        for match in re.finditer(pattern, text):
            param = match.group(0).strip()
            if param not in seen and len(param) > 3:
                seen.add(param)
                params.append(param)

    # Specific EDC parameters with Unicode
    edc_patterns = [
        r'ℓ\s*[=≈]\s*[\d.]+(?:\s*[×x]\s*10\^?[-\d]+)?(?:\s*\w+)?',
        r'L_0\s*[=≈]\s*[\d.]+(?:\s*[×x]\s*10\^?[-\d]+)?(?:\s*\w+)?',
        r'R_[pξ]\s*[=≈]\s*[\d.]+(?:\s*[×x]\s*10\^?[-\d]+)?(?:\s*\w+)?',
        r'κ\s*[=≈]\s*[\d.]+',
        r'Δ\s*[=≈]\s*[\d.]+',
        r'ξ\s*[=≈]\s*[\d.]+',
        r'F_bulk\s*[=≈]\s*[\d.]+(?:\s*[×x]\s*10\^?[-\d]+)?',
        r'g_5\s*[=≈]\s*[\d.]+(?:\s*[×x]\s*10\^?[-\d]+)?',
        r'M_5\s*[=≈]\s*[\d.]+(?:\s*[×x]\s*10\^?[-\d]+)?',
        r'λ\s*[=≈]\s*[\d.]+',
        r'Λ\s*[=≈]\s*[\d.]+(?:\s*[×x]\s*10\^?[-\d]+)?',
        r'σ\s*[=≈]\s*[\d.]+(?:\s*[×x]\s*10\^?[-\d]+)?',
    ]

    for pattern in edc_patterns:
        for match in re.finditer(pattern, text):
            param = match.group(0).strip()
            if param not in seen:
                seen.add(param)
                params.append(param)

    return params

def extract_blocked_items(text):
    """Extract blocked/uncertain items and research gaps."""
    blocked = []

    patterns = [
        r'(?:BLOCKED|STUCK|UNCLEAR|UNCERTAIN|UNKNOWN|TBD|TODO|FIXME|QUESTION|ISSUE|GAP)[:\s]+(.+?)(?:\n|$)',
        r'(?:problem|difficulty|challenge|obstacle|discrepancy|inconsistenc)[:\s]+(.+?)(?:\n|$)',
        r'(?:needs?\s+(?:to\s+be|further|more|investigation)|requires?\s+(?:further|more|clarification))[:\s]+(.+?)(?:\n|$)',
        r'\?\?\?+(.+?)(?:\n|$)',
        r'(?:gap|missing|incomplete|unresolved)[:\s]+(.+?)(?:\n|$)',
        r'(?:factor\s+of\s+\d+|off\s+by\s+\d+|discrepancy)[:\s]*(.+?)(?:\n|$)',
    ]

    for pattern in patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            content = match.group(0).strip()
            if len(content) > 10:
                blocked.append(content[:500])

    return blocked

def extract_key_results(text):
    """Extract key results and findings."""
    results = []

    patterns = [
        r'(?:KEY\s+RESULT|MAIN\s+RESULT|IMPORTANT\s+(?:RESULT|FINDING)|FINDING|CONCLUSION)[:\s]+(.+?)(?:\n\n|$)',
        r'(?:This\s+(?:shows|demonstrates|proves|confirms|establishes|gives|yields))[:\s]+(.+?)(?:\.|$)',
        r'(?:agreement|consistent\s+with|matches?|reproduces?|recovers?)[:\s]+(.+?)(?:\.|$)',
        r'(?:SUCCESS|VERIFIED|CONFIRMED)[:\s!]+(.+?)(?:\n|$)',
        r'(?:derived|obtained|found)[:\s]+(.+?)\s*(?:from|using|via)',
    ]

    for pattern in patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE | re.DOTALL):
            content = match.group(0).strip()
            if len(content) > 20:
                results.append(content[:500])

    return results

def process_jsonl_file(filepath):
    """Process a single JSONL file and extract all content."""

    all_equations = []
    all_derivations = []
    all_parameters = []
    all_blocked = []
    all_results = []
    all_snippets = []
    message_count = 0

    with open(filepath, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                continue

            # Skip non-message entries
            if data.get('type') == 'file-history-snapshot':
                continue

            text_content, role = extract_text_from_message(data)

            if not text_content or len(text_content) < 20:
                continue

            message_count += 1

            # Extract all content types
            equations = extract_equations(text_content)
            for eq_type, eq in equations:
                all_equations.append({
                    'type': eq_type,
                    'equation': eq,
                    'line': line_num,
                    'role': role
                })

            derivations = extract_derivation_chains(text_content)
            for deriv_type, deriv in derivations:
                all_derivations.append({
                    'type': deriv_type,
                    'content': deriv,
                    'line': line_num,
                    'role': role
                })

            parameters = extract_parameters(text_content)
            for param in parameters:
                all_parameters.append({
                    'parameter': param,
                    'line': line_num,
                    'role': role
                })

            blocked = extract_blocked_items(text_content)
            for item in blocked:
                all_blocked.append({
                    'item': item,
                    'line': line_num,
                    'role': role
                })

            results = extract_key_results(text_content)
            for result in results:
                all_results.append({
                    'result': result,
                    'line': line_num,
                    'role': role
                })

            # Store significant snippets (messages with equations or derivations)
            if equations or derivations or len(text_content) > 500:
                snippet_hash = hashlib.md5(text_content[:200].encode()).hexdigest()[:8]
                all_snippets.append({
                    'id': f"{line_num}_{snippet_hash}",
                    'line': line_num,
                    'role': role,
                    'preview': text_content[:300] + "..." if len(text_content) > 300 else text_content,
                    'full_text': text_content,
                    'has_equations': len(equations) > 0,
                    'has_derivations': len(derivations) > 0,
                    'equation_count': len(equations),
                    'derivation_count': len(derivations)
                })

    return {
        'message_count': message_count,
        'equations': all_equations,
        'derivations': all_derivations,
        'parameters': all_parameters,
        'blocked': all_blocked,
        'results': all_results,
        'snippets': all_snippets
    }

def write_full_report(data, filepath, output_dir):
    """Write the full extraction report."""
    file_id = Path(filepath).stem

    report = f"""# Full Extraction Report: {file_id}

## Source File
- Path: {filepath}
- Messages processed: {data['message_count']}

## Summary Statistics
- Total equations: {len(data['equations'])}
- Total derivations: {len(data['derivations'])}
- Total parameters: {len(data['parameters'])}
- Total blocked items: {len(data['blocked'])}
- Total key results: {len(data['results'])}
- Significant snippets: {len(data['snippets'])}

---

## DERIVATIONS ({len(data['derivations'])} total)

"""

    for i, deriv in enumerate(data['derivations'], 1):
        report += f"""### Derivation {i} (Line {deriv['line']}, Type: {deriv['type']})
Role: {deriv['role']}

```
{deriv['content']}
```

---

"""

    report += f"""

## PARAMETERS ({len(data['parameters'])} total)

| # | Parameter | Line | Role |
|---|-----------|------|------|
"""

    seen_params = set()
    param_count = 0
    for param in data['parameters']:
        if param['parameter'] not in seen_params:
            seen_params.add(param['parameter'])
            param_count += 1
            report += f"| {param_count} | `{param['parameter']}` | {param['line']} | {param['role']} |\n"

    report += f"""

## BLOCKED ITEMS ({len(data['blocked'])} total)

"""

    for i, item in enumerate(data['blocked'], 1):
        report += f"""### Blocked {i} (Line {item['line']})
```
{item['item']}
```

"""

    report += f"""

## KEY RESULTS ({len(data['results'])} total)

"""

    for i, result in enumerate(data['results'], 1):
        report += f"""### Result {i} (Line {result['line']})
```
{result['result']}
```

"""

    output_path = output_dir / f"{file_id}_full.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)

    return output_path

def write_equations_report(data, filepath, output_dir):
    """Write the equations-only report."""
    file_id = Path(filepath).stem

    report = f"""# Equations Report: {file_id}

Total equations extracted: {len(data['equations'])}

---

"""

    # Group by type
    by_type = defaultdict(list)
    for eq in data['equations']:
        by_type[eq['type']].append(eq)

    for eq_type in sorted(by_type.keys()):
        equations = by_type[eq_type]
        report += f"""## {eq_type.upper()} ({len(equations)} total)

"""
        for i, eq in enumerate(equations, 1):
            report += f"""### Eq-{eq_type}-{i} (Line {eq['line']}, Role: {eq['role']})
```
{eq['equation']}
```

"""

    output_path = output_dir / f"{file_id}_equations.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)

    return output_path

def write_snippets_json(data, filepath, output_dir):
    """Write the snippets JSON file."""
    file_id = Path(filepath).stem

    # Include all significant snippets
    significant = [s for s in data['snippets'] if s['has_equations'] or s['has_derivations'] or len(s['full_text']) > 1000]

    output = {
        'file_id': file_id,
        'source': str(filepath),
        'total_messages': data['message_count'],
        'total_snippets': len(data['snippets']),
        'significant_snippets': len(significant),
        'equation_count': len(data['equations']),
        'derivation_count': len(data['derivations']),
        'parameter_count': len(data['parameters']),
        'blocked_count': len(data['blocked']),
        'result_count': len(data['results']),
        'snippets': significant
    }

    output_path = output_dir / f"{file_id}_snippets.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    return output_path

def main():
    if len(sys.argv) < 3:
        print("Usage: python extract_all_v2.py <jsonl_file> <output_dir>")
        sys.exit(1)

    filepath = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Processing: {filepath}")
    print(f"Output dir: {output_dir}")

    data = process_jsonl_file(filepath)

    full_path = write_full_report(data, filepath, output_dir)
    eq_path = write_equations_report(data, filepath, output_dir)
    snippets_path = write_snippets_json(data, filepath, output_dir)

    print(f"\nExtraction complete:")
    print(f"  Messages: {data['message_count']}")
    print(f"  Equations: {len(data['equations'])}")
    print(f"  Derivations: {len(data['derivations'])}")
    print(f"  Parameters: {len(data['parameters'])}")
    print(f"  Blocked: {len(data['blocked'])}")
    print(f"  Results: {len(data['results'])}")
    print(f"  Snippets: {len(data['snippets'])}")
    print(f"\nFiles written:")
    print(f"  {full_path}")
    print(f"  {eq_path}")
    print(f"  {snippets_path}")

if __name__ == '__main__':
    main()
