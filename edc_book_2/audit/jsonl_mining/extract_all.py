#!/usr/bin/env python3
"""
Full extraction script for JSONL conversation files.
Extracts ALL derivations, equations, parameters, and blocked items.
"""

import json
import re
import sys
from pathlib import Path
from collections import defaultdict
import hashlib

def extract_equations(text):
    """Extract all LaTeX equations from text."""
    equations = []

    # Display math: $$ ... $$
    for match in re.finditer(r'\$\$([^$]+)\$\$', text, re.DOTALL):
        eq = match.group(1).strip()
        if len(eq) > 3:  # Skip trivial
            equations.append(('display', eq))

    # \[ ... \]
    for match in re.finditer(r'\\\[([^\]]+)\\\]', text, re.DOTALL):
        eq = match.group(1).strip()
        if len(eq) > 3:
            equations.append(('display', eq))

    # \begin{equation} ... \end{equation}
    for match in re.finditer(r'\\begin\{equation\*?\}(.*?)\\end\{equation\*?\}', text, re.DOTALL):
        eq = match.group(1).strip()
        if len(eq) > 3:
            equations.append(('equation', eq))

    # \begin{align} ... \end{align}
    for match in re.finditer(r'\\begin\{align\*?\}(.*?)\\end\{align\*?\}', text, re.DOTALL):
        eq = match.group(1).strip()
        if len(eq) > 3:
            equations.append(('align', eq))

    # Inline math: $ ... $ (be careful not to match $$)
    for match in re.finditer(r'(?<!\$)\$([^$\n]+)\$(?!\$)', text):
        eq = match.group(1).strip()
        if len(eq) > 3 and '=' in eq:  # Only inline equations with =
            equations.append(('inline', eq))

    return equations

def extract_parameters(text):
    """Extract numerical parameters and constants."""
    params = []

    # Pattern for parameter definitions: name = value (with optional units)
    patterns = [
        r'([A-Za-z_][A-Za-z0-9_]*)\s*[=≈]\s*([\d.]+(?:\s*[×x]\s*10\^?[-\d]+)?)\s*(eV|GeV|MeV|TeV|keV|fm|m|s|Hz|K|kg|J|W)?',
        r'\\([A-Za-z]+)\s*[=≈]\s*([\d.]+(?:\s*\\times\s*10\^\{?[-\d]+\}?)?)',
        r'([α-ωΑ-Ω][A-Za-z0-9_]*)\s*[=≈]\s*([\d.]+)',
    ]

    for pattern in patterns:
        for match in re.finditer(pattern, text):
            params.append(match.group(0))

    # Specific EDC parameters
    edc_params = [
        r'ℓ\s*[=≈]\s*[\d.]+',
        r'L_0\s*[=≈]\s*[\d.]+',
        r'R_p\s*[=≈]\s*[\d.]+',
        r'κ\s*[=≈]\s*[\d.]+',
        r'Δ\s*[=≈]\s*[\d.]+',
        r'ξ\s*[=≈]\s*[\d.]+',
        r'F_bulk\s*[=≈]\s*[\d.]+',
        r'g_5\s*[=≈]\s*[\d.]+',
        r'M_5\s*[=≈]\s*[\d.]+',
        r'λ\s*[=≈]\s*[\d.]+',
        r'Λ\s*[=≈]\s*[\d.]+',
    ]

    for pattern in edc_params:
        for match in re.finditer(pattern, text):
            params.append(match.group(0))

    return list(set(params))

def extract_derivations(text):
    """Extract derivation chains and logical steps."""
    derivations = []

    # Look for numbered steps
    step_pattern = r'(?:Step\s*\d+|^\d+\.|^\(\d+\))[:\.]?\s*(.+?)(?=(?:Step\s*\d+|^\d+\.|^\(\d+\)|$))'
    for match in re.finditer(step_pattern, text, re.MULTILINE | re.DOTALL):
        content = match.group(0).strip()
        if len(content) > 20:
            derivations.append(('step', content[:500]))

    # Look for "therefore", "thus", "hence", "it follows"
    conclusion_patterns = [
        r'(?:therefore|thus|hence|it follows that|we obtain|this gives|this yields|we find|we get)[:\s]+(.+?)(?:\.|$)',
        r'(?:combining|substituting|from|using)[:\s]+(.+?)(?:we (?:get|obtain|find|have))',
    ]

    for pattern in conclusion_patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            content = match.group(0).strip()
            if len(content) > 20:
                derivations.append(('conclusion', content[:500]))

    # Look for proof structures
    proof_pattern = r'(?:Proof|Derivation|Calculation)[:\.]?\s*(.+?)(?:QED|□|∎|$)'
    for match in re.finditer(proof_pattern, text, re.DOTALL | re.IGNORECASE):
        content = match.group(0).strip()
        if len(content) > 50:
            derivations.append(('proof', content[:1000]))

    return derivations

def extract_blocked_items(text):
    """Extract blocked/uncertain items and research gaps."""
    blocked = []

    patterns = [
        r'(?:blocked|stuck|unclear|uncertain|unknown|TBD|TODO|FIXME|QUESTION|ISSUE)[:\s]+(.+?)(?:\n|$)',
        r'(?:problem|difficulty|challenge|obstacle)[:\s]+(.+?)(?:\n|$)',
        r'(?:needs? (?:to be|further)|requires? (?:further|more))[:\s]+(.+?)(?:\n|$)',
        r'\?\?\?+(.+?)(?:\n|$)',
        r'(?:gap|missing|incomplete)[:\s]+(.+?)(?:\n|$)',
    ]

    for pattern in patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            content = match.group(0).strip()
            if len(content) > 10:
                blocked.append(content[:300])

    return blocked

def extract_key_results(text):
    """Extract key results and findings."""
    results = []

    patterns = [
        r'(?:key result|main result|important result|finding|conclusion)[:\s]+(.+?)(?:\n\n|$)',
        r'(?:this (?:shows|demonstrates|proves|confirms|establishes))[:\s]+(.+?)(?:\.|$)',
        r'(?:agreement|consistent with|matches?|reproduces?)[:\s]+(.+?)(?:\.|$)',
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

            # Extract text content from various message formats
            text_content = ""
            role = "unknown"

            if isinstance(data, dict):
                # Handle different JSONL formats
                if 'content' in data:
                    content = data['content']
                    if isinstance(content, str):
                        text_content = content
                    elif isinstance(content, list):
                        for item in content:
                            if isinstance(item, dict) and 'text' in item:
                                text_content += item['text'] + "\n"
                            elif isinstance(item, str):
                                text_content += item + "\n"

                if 'message' in data:
                    msg = data['message']
                    if isinstance(msg, dict) and 'content' in msg:
                        content = msg['content']
                        if isinstance(content, str):
                            text_content = content
                        elif isinstance(content, list):
                            for item in content:
                                if isinstance(item, dict) and 'text' in item:
                                    text_content += item['text'] + "\n"

                if 'text' in data:
                    text_content = data['text']

                role = data.get('role', data.get('type', 'unknown'))

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

            derivations = extract_derivations(text_content)
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
                    'preview': text_content[:200] + "..." if len(text_content) > 200 else text_content,
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
        report += f"""### Derivation {i} (Line {deriv['line']}, {deriv['type']})
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
    for i, param in enumerate(data['parameters'], 1):
        if param['parameter'] not in seen_params:
            seen_params.add(param['parameter'])
            report += f"| {i} | `{param['parameter']}` | {param['line']} | {param['role']} |\n"

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

    for eq_type, equations in by_type.items():
        report += f"""## {eq_type.upper()} EQUATIONS ({len(equations)} total)

"""
        for i, eq in enumerate(equations, 1):
            report += f"""### Eq-{eq_type}-{i} (Line {eq['line']})
```latex
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

    # Filter to most significant snippets
    significant = [s for s in data['snippets'] if s['has_equations'] or s['has_derivations']]

    output = {
        'file_id': file_id,
        'source': str(filepath),
        'total_snippets': len(data['snippets']),
        'significant_snippets': len(significant),
        'snippets': significant
    }

    output_path = output_dir / f"{file_id}_snippets.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    return output_path

def main():
    if len(sys.argv) < 3:
        print("Usage: python extract_all.py <jsonl_file> <output_dir>")
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
