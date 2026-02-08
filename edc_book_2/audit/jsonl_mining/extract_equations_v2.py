#!/usr/bin/env python3
"""
Enhanced extraction of equations, derivations, and blocked items from JSONL session file.
Version 2: More aggressive extraction patterns for EDC content.
"""

import json
import re
import os
from collections import defaultdict
from typing import Dict, List, Any, Tuple
import hashlib

INPUT_FILE = "/Users/igor/ClaudeAI/EDC_Project/dmining/projects/-Users-igor-ClaudeAI-EDC-Project-EDC-Research-PRIVATE/22826edd-2441-4230-bbfc-5bbb12e57e39.jsonl"
OUTPUT_DIR = "/Users/igor/ClaudeAI/EDC_Project/elastic-diffusive-cosmology_repo/edc_book_2/audit/jsonl_mining/reports"

class EquationExtractor:
    def __init__(self):
        self.equations = []
        self.derivations = []
        self.blocked_items = []
        self.parameters = []
        self.numerical_results = []
        self.dictionary_mappings = []
        self.derivation_chains = []
        self.seen_hashes = set()
        self.eq_counter = 0
        self.all_content_blocks = []

    def get_source_pointer(self, line_num: int, text: str, context_words: int = 25) -> str:
        """Create source pointer with line number and excerpt."""
        words = text.split()[:context_words]
        excerpt = ' '.join(words)
        if len(text.split()) > context_words:
            excerpt += '...'
        return f"Line {line_num}: \"{excerpt}\""

    def extract_latex_equations(self, text: str, line_num: int) -> List[Dict]:
        """Extract all LaTeX equations from text - more aggressive patterns."""
        results = []

        # Display math $$...$$
        for match in re.finditer(r'\$\$(.+?)\$\$', text, re.DOTALL):
            latex = match.group(1).strip()
            results.append({
                'latex': latex,
                'type': 'display',
                'position': match.start(),
                'context': text[max(0, match.start()-200):match.end()+200]
            })

        # \[...\]
        for match in re.finditer(r'\\\[(.+?)\\\]', text, re.DOTALL):
            latex = match.group(1).strip()
            if latex not in [r['latex'] for r in results]:
                results.append({
                    'latex': latex,
                    'type': 'display_bracket',
                    'position': match.start(),
                    'context': text[max(0, match.start()-200):match.end()+200]
                })

        # \begin{equation}...\end{equation}
        for match in re.finditer(r'\\begin\{equation\*?\}(.+?)\\end\{equation\*?\}', text, re.DOTALL):
            latex = match.group(1).strip()
            if latex not in [r['latex'] for r in results]:
                results.append({
                    'latex': latex,
                    'type': 'equation_env',
                    'position': match.start(),
                    'context': text[max(0, match.start()-200):match.end()+200]
                })

        # \begin{align}...\end{align}
        for match in re.finditer(r'\\begin\{align\*?\}(.+?)\\end\{align\*?\}', text, re.DOTALL):
            latex = match.group(1).strip()
            if latex not in [r['latex'] for r in results]:
                results.append({
                    'latex': latex,
                    'type': 'align_env',
                    'position': match.start(),
                    'context': text[max(0, match.start()-200):match.end()+200]
                })

        # Inline math - capture all significant ones
        for match in re.finditer(r'\$([^$]{2,200})\$', text):
            latex = match.group(1).strip()
            # Include if has equals, approx, or important symbols
            if any(op in latex for op in ['=', '\\equiv', '\\approx', '\\sim', '\\to', '\\rightarrow', '\\propto']):
                if latex not in [r['latex'] for r in results]:
                    results.append({
                        'latex': latex,
                        'type': 'inline',
                        'position': match.start(),
                        'context': text[max(0, match.start()-200):match.end()+200]
                    })

        # Also capture expressions with := or ≡ outside LaTeX
        for match in re.finditer(r'([A-Za-z_][A-Za-z0-9_]*)\s*(?::=|≡|≈)\s*([^\n;]{5,100})', text):
            latex = match.group(0)
            if latex not in [r['latex'] for r in results]:
                results.append({
                    'latex': latex,
                    'type': 'definition',
                    'position': match.start(),
                    'context': text[max(0, match.start()-100):match.end()+100]
                })

        return results

    def classify_epistemic_status(self, text: str, latex: str) -> str:
        """Classify epistemic status based on context."""
        text_lower = text.lower()

        if re.search(r'blocked|pending|unresolved|gap-\d+', text_lower):
            return 'BL'
        if re.search(r'measured|observed|experimental|pdg|data|empirical', text_lower):
            return 'M'
        if re.search(r'calculated|compute|yields|gives|obtain|result', text_lower):
            return 'Cal'
        if re.search(r'deriv|proof|follows|show that|we have|therefore|thus|hence', text_lower):
            return 'Der'
        if re.search(r'define|definition|convention|notation|denote', text_lower):
            return 'Dc'
        if re.search(r'inferred|implies|suggests|indicates|conclude', text_lower):
            return 'I'
        if re.search(r'open|unknown|unclear|tbd|todo|question', text_lower):
            return 'Open'

        return 'Der'

    def classify_topic(self, context: str, latex: str) -> str:
        """Classify the topic of an equation."""
        context_lower = context.lower()
        latex_lower = latex.lower()

        topic_patterns = [
            ('mass_hierarchy', r'mass hierarchy|m_1|m_2|m_3|neutrino mass'),
            ('mixing_angle', r'theta|mixing angle|pmns|ckm|sin.*2.*theta'),
            ('coupling', r'coupling|alpha|yukawa'),
            ('epsilon', r'epsilon|varepsilon|small parameter'),
            ('fermi', r'fermi|weak coupling'),
            ('lifetime', r'lifetime|decay time|half.?life'),
            ('width', r'width|decay rate'),
            ('mass', r'mass|gev|mev'),
            ('boson', r'higgs|boson|gauge'),
            ('lepton', r'electron|muon|lepton'),
            ('quark', r'quark'),
            ('cosmological', r'hubble|lambda|omega|cosmolog|dark'),
            ('topological', r'topolog|winding|homotop|instanton'),
            ('bvp', r'bvp|boundary value|profile|kink'),
            ('scale', r'planck|scale|cutoff|hierarchy'),
            ('symmetry', r'symmetry|lorentz|parity'),
        ]

        for topic, pattern in topic_patterns:
            try:
                if re.search(pattern, context_lower) or re.search(pattern, latex_lower):
                    return topic
            except re.error:
                continue

        return 'general'

    def extract_blocked_items(self, text: str, line_num: int) -> List[Dict]:
        """Extract blocked items and dependencies."""
        results = []

        patterns = [
            (r'[Bb]locked\s+(?:by|on|until)\s+([^.;\n]+)', 'blocked_by'),
            (r'[Bb]locks?\s+([^.;\n]+)', 'blocks'),
            (r'[Pp]ending\s+(?:on|resolution of)\s+([^.;\n]+)', 'pending'),
            (r'[Ww]aiting\s+(?:for|on)\s+([^.;\n]+)', 'waiting'),
            (r'GAP-(\d+)[:\s]+([^.;\n]+)', 'gap'),
            (r'BLOCKED:\s*([^.;\n]+)', 'blocked_explicit'),
            (r'unresolved[:\s]+([^.;\n]+)', 'unresolved'),
            (r'needs?\s+(?:fixing|resolution|work)[:\s]+([^.;\n]+)', 'needs_work'),
        ]

        for pattern, ptype in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                results.append({
                    'match': match.group(0),
                    'type': ptype,
                    'line': line_num,
                    'context': text[max(0, match.start()-150):match.end()+150]
                })

        return results

    def extract_numerical_results(self, text: str, line_num: int) -> List[Dict]:
        """Extract numerical results and error budgets."""
        results = []

        patterns = [
            # Value with uncertainty
            (r'(\d+\.?\d*)\s*(?:±|\\pm)\s*(\d+\.?\d*)', 'uncertainty'),
            # Scientific notation
            (r'(\d+\.?\d*)\s*(?:×|\\times)\s*10\^?\{?(-?\d+)\}?', 'scientific'),
            # Values with units
            (r'=\s*(\d+\.?\d*(?:\s*×\s*10\^?\{?-?\d+\}?)?)\s*(eV|GeV|MeV|keV|TeV|s|m|kg|fm)', 'with_units'),
            # Percentage/ppm
            (r'(\d+\.?\d*)\s*(%|ppm|ppb|per\s*cent)', 'percentage'),
            # Dimensionless numbers
            (r'=\s*(\d+\.\d{4,})', 'precise_value'),
            # Error budget
            (r'error\s+budget[^.;\n]{0,200}', 'error_budget'),
            # Sigma significance
            (r'(\d+\.?\d*)\s*σ|(\d+\.?\d*)\s*sigma', 'sigma'),
        ]

        for pattern, ntype in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                results.append({
                    'value': match.group(0),
                    'type': ntype,
                    'line': line_num,
                    'context': text[max(0, match.start()-100):match.end()+100]
                })

        return results

    def extract_dictionary_mappings(self, text: str, line_num: int) -> List[Dict]:
        """Extract EDC↔SM dictionary mappings - enhanced patterns."""
        results = []

        patterns = [
            (r'(?:EDC|edc)\s*(?:↔|<->|<=>|corresponds?\s+to)\s*(?:SM|Standard Model)', 'edc_sm'),
            (r'dictionary\s+(?:step|entry|mapping|item)[^.;\n]{0,200}', 'dict_step'),
            (r'(\$[^$]+\$)\s*(?:↔|<->|maps?\s+to|corresponds?\s+to)\s*(\$[^$]+\$)', 'latex_mapping'),
            (r'translate[ds]?\s+(?:to|into|as)[^.;\n]{0,100}', 'translation'),
            (r'interpret(?:ed|ation)?\s+as[^.;\n]{0,100}', 'interpretation'),
            (r'(?:in|under)\s+EDC[,:\s]+([^.;\n]{10,100})', 'in_edc'),
            (r'(?:in|under)\s+SM[,:\s]+([^.;\n]{10,100})', 'in_sm'),
            (r'correspondence[:\s]+([^.;\n]{10,150})', 'correspondence'),
            (r'identifies?\s+(?:as|with)[^.;\n]{0,100}', 'identification'),
            (r'maps?\s+\$[^$]+\$\s*(?:to|onto)\s*\$[^$]+\$', 'map_latex'),
        ]

        for pattern, mtype in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                results.append({
                    'mapping': match.group(0),
                    'type': mtype,
                    'line': line_num,
                    'context': text[max(0, match.start()-150):match.end()+150]
                })

        return results

    def extract_parameter_definitions(self, text: str, line_num: int) -> List[Dict]:
        """Extract parameter definitions - enhanced."""
        results = []

        patterns = [
            r'(?:where|with|define|let|set|denote)\s+\$?([A-Za-z_\\][A-Za-z0-9_\\{}]*)\$?\s*(?:=|:=|≡|\\equiv)\s*([^,;.\n]+)',
            r'\$([A-Za-z_\\][A-Za-z0-9_\\{}]*)\s*(?:=|:=|≡|\\equiv)\s*([^$]+)\$',
            r'([A-Za-z_][A-Za-z0-9_]*)\s+(?:is|are)\s+(?:defined|given)\s+(?:as|by)\s+([^.;\n]+)',
            r'(?:the\s+)?([A-Za-z_][A-Za-z0-9_]*)\s+parameter\s+(?:is|=)\s+([^.;\n]+)',
            r'\\([a-z]+)\s*(?:_\{[^}]+\})?\s*=\s*([^,;\n$]+)',
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, text):
                param = match.group(1) if len(match.groups()) >= 1 else match.group(0)
                defn = match.group(2) if len(match.groups()) >= 2 else ''
                results.append({
                    'parameter': param,
                    'definition': defn.strip(),
                    'line': line_num,
                    'context': text[max(0, match.start()-50):match.end()+50]
                })

        return results

    def extract_derivation_chains(self, text: str, line_num: int) -> List[Dict]:
        """Extract derivation chains and reasoning steps."""
        results = []

        # Look for step-by-step derivations
        patterns = [
            (r'(?:step\s+\d+|first|second|third|next|then|finally)[:\s]+([^.;\n]{20,300})', 'step'),
            (r'(?:therefore|thus|hence|consequently|it follows that)[:\s]+([^.;\n]{10,200})', 'conclusion'),
            (r'(?:substituting|inserting|using)[^.;\n]{5,100}(?:gives|yields|we get)[^.;\n]{5,150}', 'substitution'),
            (r'(?:from|by)\s+(?:eq\.?|equation)\s*[\(\[]?\d+[\)\]]?[^.;\n]{0,100}', 'from_equation'),
            (r'(?:combining|adding|multiplying)[^.;\n]{5,100}(?:gives|yields|we obtain)[^.;\n]{5,150}', 'combination'),
        ]

        for pattern, dtype in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                results.append({
                    'content': match.group(0),
                    'type': dtype,
                    'line': line_num,
                    'context': text[max(0, match.start()-100):match.end()+100]
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

        # Also check for 'text' field
        if isinstance(msg.get('text'), str):
            content += msg['text']

        if not content or len(content) < 10:
            return

        # Store content block for reference
        if len(content) > 100:
            self.all_content_blocks.append({
                'line': line_num,
                'length': len(content),
                'preview': content[:200]
            })

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
                eq['topic'] = self.classify_topic(eq['context'], eq['latex'])
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

        # Extract derivation chains
        derivations = self.extract_derivation_chains(content, line_num)
        self.derivation_chains.extend(derivations)

    def process_file(self, filepath: str):
        """Process the entire JSONL file."""
        print(f"Processing {filepath}...")

        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            for line_num, line in enumerate(f, 1):
                if line_num % 5000 == 0:
                    print(f"  Processed {line_num} lines, found {len(self.equations)} equations...")

                try:
                    data = json.loads(line.strip())
                except json.JSONDecodeError:
                    continue

                # Handle various conversation structures
                if isinstance(data, dict):
                    if 'messages' in data:
                        for msg in data['messages']:
                            self.process_message(msg, line_num)
                    elif 'content' in data:
                        self.process_message(data, line_num)
                    elif 'message' in data:
                        self.process_message(data['message'], line_num)
                    elif 'text' in data:
                        self.process_message(data, line_num)
                    elif 'assistant' in data:
                        self.process_message({'content': data['assistant']}, line_num)
                    elif 'human' in data:
                        self.process_message({'content': data['human']}, line_num)

        print(f"\nExtraction complete.")
        print(f"  Total content blocks processed: {len(self.all_content_blocks)}")
        print(f"  Equations: {len(self.equations)}")
        print(f"  Blocked items: {len(self.blocked_items)}")
        print(f"  Numerical results: {len(self.numerical_results)}")
        print(f"  Dictionary mappings: {len(self.dictionary_mappings)}")
        print(f"  Parameters: {len(self.parameters)}")
        print(f"  Derivation chains: {len(self.derivation_chains)}")

    def generate_full_report(self) -> str:
        """Generate the full markdown report."""
        lines = []
        lines.append("# Full Extraction Report: 22826edd Session\n")
        lines.append(f"**File:** 22826edd-2441-4230-bbfc-5bbb12e57e39.jsonl\n")
        lines.append(f"**Extraction Date:** Auto-generated (v2)\n\n")
        lines.append("## Summary Statistics\n")
        lines.append(f"- **Total Equations:** {len(self.equations)}\n")
        lines.append(f"- **Blocked Items:** {len(self.blocked_items)}\n")
        lines.append(f"- **Numerical Results:** {len(self.numerical_results)}\n")
        lines.append(f"- **Dictionary Mappings:** {len(self.dictionary_mappings)}\n")
        lines.append(f"- **Parameter Definitions:** {len(self.parameters)}\n")
        lines.append(f"- **Derivation Chains:** {len(self.derivation_chains)}\n")
        lines.append("\n---\n")

        # Equations by topic
        lines.append("## Equations by Topic\n")
        topics = defaultdict(list)
        for eq in self.equations:
            topics[eq['topic']].append(eq)

        for topic in sorted(topics.keys()):
            lines.append(f"\n### Topic: {topic} ({len(topics[topic])} equations)\n")
            for eq in topics[topic]:
                lines.append(f"\n#### {eq['eq_id']}\n")
                lines.append(f"**Type:** {eq['type']} | **Epistemic:** {eq['epistemic']}\n\n")
                lines.append(f"```latex\n{eq['latex']}\n```\n\n")
                # Explanation from context
                explanation = eq['context'].strip()[:500]
                lines.append(f"**Context:** {explanation}\n\n")
                lines.append(f"**Source:** {eq['source_pointer']}\n")
                lines.append("\n---\n")

        # Blocked items section
        lines.append("\n## Blocked Items\n")
        for item in self.blocked_items:
            lines.append(f"\n### Line {item['line']} - Type: {item['type']}\n")
            lines.append(f"**Match:** {item['match']}\n\n")
            lines.append(f"**Context:** {item['context'][:300]}...\n")

        # Numerical results section
        lines.append("\n## Numerical Results\n")
        by_type = defaultdict(list)
        for result in self.numerical_results:
            by_type[result['type']].append(result)

        for ntype, results in sorted(by_type.items()):
            lines.append(f"\n### {ntype} ({len(results)} items)\n")
            for r in results[:50]:  # Limit per type
                lines.append(f"- Line {r['line']}: `{r['value']}`\n")
            if len(results) > 50:
                lines.append(f"- ... and {len(results)-50} more\n")

        # Dictionary mappings section
        lines.append("\n## EDC↔SM Dictionary Mappings\n")
        for mapping in self.dictionary_mappings:
            lines.append(f"\n### Line {mapping['line']} - Type: {mapping['type']}\n")
            lines.append(f"**Mapping:** {mapping['mapping']}\n\n")
            lines.append(f"**Context:** {mapping['context'][:300]}...\n")

        # Parameter definitions section
        lines.append("\n## Parameter Definitions\n")
        for i, param in enumerate(self.parameters[:200]):  # Limit to 200
            lines.append(f"- **Line {param['line']}:** `{param['parameter']}` = {param.get('definition', 'N/A')[:100]}\n")
        if len(self.parameters) > 200:
            lines.append(f"\n... and {len(self.parameters)-200} more parameter definitions\n")

        # Derivation chains section
        lines.append("\n## Derivation Chains\n")
        for i, deriv in enumerate(self.derivation_chains[:100]):  # Limit to 100
            lines.append(f"\n### Line {deriv['line']} - {deriv['type']}\n")
            lines.append(f"{deriv['content'][:400]}\n")
        if len(self.derivation_chains) > 100:
            lines.append(f"\n... and {len(self.derivation_chains)-100} more derivation steps\n")

        return '\n'.join(lines)

    def generate_equations_list(self) -> str:
        """Generate equations list markdown."""
        lines = []
        lines.append("# Equations List: 22826edd Session\n\n")
        lines.append("Total equations: " + str(len(self.equations)) + "\n\n")
        lines.append("| eq_id | topic | type | latex (truncated) | source_pointer |\n")
        lines.append("|-------|-------|------|-------------------|----------------|\n")

        for eq in self.equations:
            latex_escaped = eq['latex'].replace('|', '\\|').replace('\n', ' ')
            if len(latex_escaped) > 80:
                latex_escaped = latex_escaped[:77] + '...'
            source = f"Line {eq['line']}"
            lines.append(f"| {eq['eq_id']} | {eq['topic']} | {eq['type']} | `{latex_escaped}` | {source} |\n")

        return '\n'.join(lines)

    def generate_snippets_json(self) -> str:
        """Generate JSON snippets file."""
        snippets = []

        for eq in self.equations:
            snippets.append({
                'eq_id': eq['eq_id'],
                'topic': eq['topic'],
                'latex': eq['latex'],
                'claims': eq.get('context', '')[:400],
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
        print(f"Wrote: 22826edd_full.md ({len(full_report)} chars)")

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
    print(f"Derivation chains: {len(extractor.derivation_chains)}")


if __name__ == '__main__':
    main()
