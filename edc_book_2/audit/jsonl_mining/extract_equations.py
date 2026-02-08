#!/usr/bin/env python3
"""
Full extraction of equations, derivations, and blocked items from JSONL session file.
Processes the 22826edd session (~207 MB, ~49K lines).
"""

import json
import re
import os
from collections import defaultdict
from typing import Dict, List, Any, Tuple
import hashlib

INPUT_FILE = "/Users/igor/ClaudeAI/EDC_Project/dmining/projects/-Users-igor-ClaudeAI-EDC-Project-EDC-Research-PRIVATE/22826edd-2441-4230-bbfc-5bbb12e57e39.jsonl"
OUTPUT_DIR = "/Users/igor/ClaudeAI/EDC_Project/elastic-diffusive-cosmology_repo/edc_book_2/audit/jsonl_mining/reports"

# Patterns for extraction
EQUATION_PATTERNS = [
    # LaTeX display math
    r'\$\$([^$]+)\$\$',
    r'\\\[([^\]]+)\\\]',
    r'\\begin\{equation\}(.*?)\\end\{equation\}',
    r'\\begin\{align\}(.*?)\\end\{align\}',
    r'\\begin\{align\*\}(.*?)\\end\{align\*\}',
    # Inline math with equals
    r'\$([^$]*=[^$]*)\$',
]

# Patterns for specific EDC content
EDC_PATTERNS = {
    'parameter_def': r'(?:where|with|define|let|set)\s+([A-Za-z_][A-Za-z0-9_]*)\s*(?:=|:=|≡)',
    'dictionary_step': r'(?:dictionary|mapping|EDC\s*↔\s*SM|correspondence)',
    'blocked': r'(?:blocked|blocking|blocks|BLOCKED)',
    'derivation': r'(?:deriv|proof|follows from|we have|therefore|thus|hence|substituting)',
    'numerical': r'(?:\d+\.?\d*\s*(?:±|×|×10|e-?\d+)|error budget|precision|accuracy)',
    'epsilon': r'(?:ε|\\epsilon|\\varepsilon)\s*(?:_\{?[A-Za-z0-9]+\}?)?\s*[=≈≃]',
    'coupling': r'(?:g_[A-Za-z0-9]+|G_[A-Za-z0-9]+|α|\\alpha)\s*[=≈≃]',
    'mass': r'(?:m_[A-Za-z0-9]+|M_[A-Za-z0-9]+)\s*[=≈≃]',
}

class EquationExtractor:
    def __init__(self):
        self.equations = []
        self.derivations = []
        self.blocked_items = []
        self.parameters = []
        self.numerical_results = []
        self.dictionary_mappings = []
        self.seen_hashes = set()
        self.eq_counter = 0

    def get_source_pointer(self, line_num: int, text: str, context_words: int = 25) -> str:
        """Create source pointer with line number and excerpt."""
        words = text.split()[:context_words]
        excerpt = ' '.join(words)
        if len(text.split()) > context_words:
            excerpt += '...'
        return f"Line {line_num}: \"{excerpt}\""

    def extract_latex_equations(self, text: str, line_num: int) -> List[Dict]:
        """Extract all LaTeX equations from text."""
        results = []

        # Display math $$...$$
        for match in re.finditer(r'\$\$(.+?)\$\$', text, re.DOTALL):
            latex = match.group(1).strip()
            if '=' in latex or '\\equiv' in latex or '\\approx' in latex:
                results.append({
                    'latex': latex,
                    'type': 'display',
                    'position': match.start(),
                    'context': text[max(0, match.start()-100):match.end()+100]
                })

        # \[...\]
        for match in re.finditer(r'\\\[(.+?)\\\]', text, re.DOTALL):
            latex = match.group(1).strip()
            results.append({
                'latex': latex,
                'type': 'display',
                'position': match.start(),
                'context': text[max(0, match.start()-100):match.end()+100]
            })

        # \begin{equation}...\end{equation}
        for match in re.finditer(r'\\begin\{equation\*?\}(.+?)\\end\{equation\*?\}', text, re.DOTALL):
            latex = match.group(1).strip()
            results.append({
                'latex': latex,
                'type': 'equation',
                'position': match.start(),
                'context': text[max(0, match.start()-100):match.end()+100]
            })

        # \begin{align}...\end{align}
        for match in re.finditer(r'\\begin\{align\*?\}(.+?)\\end\{align\*?\}', text, re.DOTALL):
            latex = match.group(1).strip()
            results.append({
                'latex': latex,
                'type': 'align',
                'position': match.start(),
                'context': text[max(0, match.start()-100):match.end()+100]
            })

        # Inline math with equals sign $..=..$
        for match in re.finditer(r'\$([^$]{3,}?)\$', text):
            latex = match.group(1).strip()
            if '=' in latex or '\\equiv' in latex or '\\approx' in latex or '\\sim' in latex:
                # Skip if already captured in display math
                if not any(latex in r['latex'] for r in results):
                    results.append({
                        'latex': latex,
                        'type': 'inline',
                        'position': match.start(),
                        'context': text[max(0, match.start()-100):match.end()+100]
                    })

        return results

    def classify_epistemic_status(self, text: str, latex: str) -> str:
        """Classify epistemic status based on context."""
        text_lower = text.lower()

        if re.search(r'blocked|pending|unresolved|gap', text_lower):
            return 'BL'  # Blocked
        if re.search(r'measured|observed|experimental|PDG|data', text_lower):
            return 'M'   # Measured
        if re.search(r'calculated|compute|yields|gives|obtain', text_lower):
            return 'Cal' # Calculated
        if re.search(r'deriv|proof|follows|show that|we have', text_lower):
            return 'Der' # Derived
        if re.search(r'define|definition|convention|notation', text_lower):
            return 'Dc'  # Definition/Convention
        if re.search(r'inferred|implies|suggests|indicates', text_lower):
            return 'I'   # Inferred
        if re.search(r'open|unknown|unclear|TBD|TODO', text_lower):
            return 'Open'

        return 'Der'  # Default to Derived

    def extract_blocked_items(self, text: str, line_num: int) -> List[Dict]:
        """Extract blocked items and dependencies."""
        results = []

        # Look for blocked/blocking patterns
        patterns = [
            r'[Bb]locked\s+(?:by|on|until)\s+([^.;]+)',
            r'[Bb]locks?\s+([^.;]+)',
            r'[Pp]ending\s+(?:on|resolution of)\s+([^.;]+)',
            r'[Ww]aiting\s+(?:for|on)\s+([^.;]+)',
            r'GAP-\d+[^.;]*',
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, text):
                results.append({
                    'match': match.group(0),
                    'line': line_num,
                    'context': text[max(0, match.start()-150):match.end()+150]
                })

        return results

    def extract_numerical_results(self, text: str, line_num: int) -> List[Dict]:
        """Extract numerical results and error budgets."""
        results = []

        # Scientific notation values
        for match in re.finditer(r'(\d+\.?\d*)\s*(?:±|\\pm)\s*(\d+\.?\d*)', text):
            results.append({
                'value': match.group(0),
                'line': line_num,
                'context': text[max(0, match.start()-100):match.end()+100]
            })

        # Values with units
        for match in re.finditer(r'=\s*(\d+\.?\d*(?:\s*×\s*10\^?\{?-?\d+\}?)?)\s*(?:eV|GeV|MeV|keV|TeV|s|m|kg)', text):
            results.append({
                'value': match.group(0),
                'line': line_num,
                'context': text[max(0, match.start()-100):match.end()+100]
            })

        # Error budget mentions
        for match in re.finditer(r'error\s+budget[^.;]{0,200}', text, re.IGNORECASE):
            results.append({
                'value': match.group(0),
                'line': line_num,
                'type': 'error_budget'
            })

        return results

    def extract_dictionary_mappings(self, text: str, line_num: int) -> List[Dict]:
        """Extract EDC↔SM dictionary mappings."""
        results = []

        patterns = [
            r'(?:EDC|edc)\s*(?:↔|<->|corresponds to)\s*(?:SM|Standard Model)',
            r'dictionary\s+(?:step|entry|mapping)[^.;]{0,200}',
            r'(\$[^$]+\$)\s*(?:↔|<->|maps to|corresponds to)\s*(\$[^$]+\$)',
            r'translate[ds]?\s+(?:to|into|as)[^.;]{0,100}',
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                results.append({
                    'mapping': match.group(0),
                    'line': line_num,
                    'context': text[max(0, match.start()-100):match.end()+100]
                })

        return results

    def extract_parameter_definitions(self, text: str, line_num: int) -> List[Dict]:
        """Extract parameter definitions."""
        results = []

        patterns = [
            r'(?:where|with|define|let|set)\s+\$?([A-Za-z_\\][A-Za-z0-9_\\{}]*)\$?\s*(?:=|:=|≡|\\equiv)\s*([^,;.\n]+)',
            r'\$([A-Za-z_\\][A-Za-z0-9_\\{}]*)\s*(?:=|:=|≡|\\equiv)\s*([^$]+)\$',
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, text):
                results.append({
                    'parameter': match.group(1) if len(match.groups()) >= 1 else match.group(0),
                    'definition': match.group(2) if len(match.groups()) >= 2 else '',
                    'line': line_num,
                    'context': text[max(0, match.start()-50):match.end()+50]
                })

        return results

    def process_message(self, msg: Dict, line_num: int):
        """Process a single message from the JSONL."""
        content = ""

        # Handle different message structures
        if isinstance(msg.get('content'), str):
            content = msg['content']
        elif isinstance(msg.get('content'), list):
            for item in msg['content']:
                if isinstance(item, dict) and item.get('type') == 'text':
                    content += item.get('text', '') + '\n'
                elif isinstance(item, str):
                    content += item + '\n'

        if not content:
            return

        # Extract equations
        equations = self.extract_latex_equations(content, line_num)
        for eq in equations:
            eq_hash = hashlib.md5(eq['latex'].encode()).hexdigest()[:12]
            if eq_hash not in self.seen_hashes:
                self.seen_hashes.add(eq_hash)
                self.eq_counter += 1
                eq['eq_id'] = f"EQ-22826edd-{self.eq_counter:04d}"
                eq['line'] = line_num
                eq['epistemic'] = self.classify_epistemic_status(eq['context'], eq['latex'])
                eq['source_pointer'] = self.get_source_pointer(line_num, eq['context'])
                self.equations.append(eq)

        # Extract blocked items
        blocked = self.extract_blocked_items(content, line_num)
        self.blocked_items.extend(blocked)

        # Extract numerical results
        numerical = self.extract_numerical_results(content, line_num)
        self.numerical_results.extend(numerical)

        # Extract dictionary mappings
        mappings = self.extract_dictionary_mappings(content, line_num)
        self.dictionary_mappings.extend(mappings)

        # Extract parameter definitions
        params = self.extract_parameter_definitions(content, line_num)
        self.parameters.extend(params)

    def process_file(self, filepath: str):
        """Process the entire JSONL file."""
        print(f"Processing {filepath}...")

        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            for line_num, line in enumerate(f, 1):
                if line_num % 5000 == 0:
                    print(f"  Processed {line_num} lines...")

                try:
                    data = json.loads(line.strip())
                except json.JSONDecodeError:
                    continue

                # Handle conversation structure
                if isinstance(data, dict):
                    if 'messages' in data:
                        for msg in data['messages']:
                            self.process_message(msg, line_num)
                    elif 'content' in data:
                        self.process_message(data, line_num)
                    elif 'message' in data:
                        self.process_message(data['message'], line_num)

        print(f"Extraction complete.")
        print(f"  Equations: {len(self.equations)}")
        print(f"  Blocked items: {len(self.blocked_items)}")
        print(f"  Numerical results: {len(self.numerical_results)}")
        print(f"  Dictionary mappings: {len(self.dictionary_mappings)}")
        print(f"  Parameters: {len(self.parameters)}")

    def generate_full_report(self) -> str:
        """Generate the full markdown report."""
        lines = []
        lines.append("# Full Extraction Report: 22826edd Session\n")
        lines.append(f"**File:** 22826edd-2441-4230-bbfc-5bbb12e57e39.jsonl\n")
        lines.append(f"**Extraction Date:** Auto-generated\n")
        lines.append(f"**Total Equations:** {len(self.equations)}\n")
        lines.append(f"**Blocked Items:** {len(self.blocked_items)}\n")
        lines.append(f"**Numerical Results:** {len(self.numerical_results)}\n")
        lines.append(f"**Dictionary Mappings:** {len(self.dictionary_mappings)}\n")
        lines.append(f"**Parameter Definitions:** {len(self.parameters)}\n")
        lines.append("\n---\n")

        # Equations section
        lines.append("## 1. Equations (in order of appearance)\n")
        for eq in self.equations:
            lines.append(f"### {eq['eq_id']}\n")
            lines.append(f"**Type:** {eq['type']} | **Epistemic Status:** {eq['epistemic']}\n")
            lines.append(f"**LaTeX:**\n```latex\n{eq['latex']}\n```\n")
            lines.append(f"**Source:** {eq['source_pointer']}\n")
            lines.append("")

        # Blocked items section
        lines.append("\n## 2. Blocked Items\n")
        for item in self.blocked_items:
            lines.append(f"- **Line {item['line']}:** {item['match']}\n")
            lines.append(f"  Context: {item['context'][:200]}...\n")

        # Numerical results section
        lines.append("\n## 3. Numerical Results\n")
        for result in self.numerical_results:
            lines.append(f"- **Line {result['line']}:** {result['value']}\n")

        # Dictionary mappings section
        lines.append("\n## 4. EDC↔SM Dictionary Mappings\n")
        for mapping in self.dictionary_mappings:
            lines.append(f"- **Line {mapping['line']}:** {mapping['mapping']}\n")

        # Parameter definitions section
        lines.append("\n## 5. Parameter Definitions\n")
        for param in self.parameters:
            lines.append(f"- **Line {param['line']}:** `{param['parameter']}` = {param.get('definition', 'N/A')}\n")

        return '\n'.join(lines)

    def generate_equations_list(self) -> str:
        """Generate equations list markdown."""
        lines = []
        lines.append("# Equations List: 22826edd Session\n")
        lines.append("| eq_id | latex | source_pointer |\n")
        lines.append("|-------|-------|----------------|\n")

        for eq in self.equations:
            # Escape pipes in LaTeX
            latex_escaped = eq['latex'].replace('|', '\\|').replace('\n', ' ')[:100]
            source = eq['source_pointer'][:80].replace('|', '\\|')
            lines.append(f"| {eq['eq_id']} | `{latex_escaped}` | {source} |\n")

        return '\n'.join(lines)

    def generate_snippets_json(self) -> str:
        """Generate JSON snippets file."""
        snippets = []

        for eq in self.equations:
            # Determine topic from context
            context_lower = eq['context'].lower()
            topic = 'general'
            if 'mass' in context_lower or 'm_' in eq['latex'].lower():
                topic = 'mass'
            elif 'coupling' in context_lower or 'g_' in eq['latex'].lower():
                topic = 'coupling'
            elif 'epsilon' in context_lower or 'varepsilon' in eq['latex']:
                topic = 'epsilon'
            elif 'mixing' in context_lower or 'theta' in eq['latex']:
                topic = 'mixing_angle'
            elif 'lifetime' in context_lower or 'tau' in eq['latex']:
                topic = 'lifetime'
            elif 'width' in context_lower or 'gamma' in eq['latex'].lower():
                topic = 'decay_width'
            elif 'fermi' in context_lower or 'G_F' in eq['latex']:
                topic = 'fermi_constant'

            snippets.append({
                'eq_id': eq['eq_id'],
                'topic': topic,
                'latex': eq['latex'],
                'claims': eq.get('context', '')[:300],
                'source': f"Line {eq['line']}",
                'notes': f"Type: {eq['type']}, Epistemic: {eq['epistemic']}"
            })

        return json.dumps(snippets, indent=2, ensure_ascii=False)

    def write_outputs(self, output_dir: str):
        """Write all output files."""
        os.makedirs(output_dir, exist_ok=True)

        # Full report
        full_report = self.generate_full_report()
        with open(os.path.join(output_dir, '22826edd_full.md'), 'w', encoding='utf-8') as f:
            f.write(full_report)
        print(f"Wrote: 22826edd_full.md")

        # Equations list
        eq_list = self.generate_equations_list()
        with open(os.path.join(output_dir, '22826edd_equations.md'), 'w', encoding='utf-8') as f:
            f.write(eq_list)
        print(f"Wrote: 22826edd_equations.md")

        # JSON snippets
        snippets = self.generate_snippets_json()
        with open(os.path.join(output_dir, '22826edd_snippets.json'), 'w', encoding='utf-8') as f:
            f.write(snippets)
        print(f"Wrote: 22826edd_snippets.json")


def main():
    extractor = EquationExtractor()
    extractor.process_file(INPUT_FILE)
    extractor.write_outputs(OUTPUT_DIR)

    print("\n=== EXTRACTION SUMMARY ===")
    print(f"Total equations extracted: {len(extractor.equations)}")
    print(f"Blocked items: {len(extractor.blocked_items)}")
    print(f"Numerical results: {len(extractor.numerical_results)}")
    print(f"Dictionary mappings: {len(extractor.dictionary_mappings)}")
    print(f"Parameter definitions: {len(extractor.parameters)}")


if __name__ == '__main__':
    main()
