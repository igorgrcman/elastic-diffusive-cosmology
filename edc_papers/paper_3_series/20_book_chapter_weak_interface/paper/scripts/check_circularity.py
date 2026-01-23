#!/usr/bin/env python3
"""
EDC Circularity Scanner
========================

Detects when a value is derived from an expression that uses the same
measured target as input (e.g., v from G_F then claiming to predict G_F).

Deliverable D4b: Circularity scanner that:
- Maintains a list of banned input→output pairs
- Scans LaTeX for circular derivations
- Flags as CIRCULAR and recommends tag downgrade

Usage:
    python scripts/check_circularity.py
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple
from dataclasses import dataclass

# ==============================================================================
# Configuration
# ==============================================================================

SCRIPT_DIR = Path(__file__).parent
PAPER_DIR = SCRIPT_DIR.parent
SECTIONS_DIR = PAPER_DIR / "sections"

# ==============================================================================
# Circularity Rules
# ==============================================================================

# Map of quantities and what they CANNOT be derived from (circular)
# Format: "output" -> set of "forbidden inputs"
CIRCULARITY_RULES = {
    # G_F relations
    "G_F": {"v", "M_W", "g_2", "Higgs VEV"},
    "v": {"G_F"},
    "M_W": {"G_F", "v"},

    # Electroweak mixing
    "sin2_theta_W": {"M_W", "M_Z", "G_F"},
    "theta_W": {"M_W", "M_Z", "G_F"},

    # R_xi constraints
    "R_xi": {"M_Z", "M_W", "electroweak scale"},
    "delta": {"M_Z", "M_W", "electroweak scale"},

    # Masses
    "m_phi": {"M_W", "M_Z", "G_F"},

    # Couplings
    "g_2": {"M_W", "G_F", "v"},
    "g_5": {"M_W", "G_F"},
}

# Patterns that indicate derivation claims
DERIVATION_PATTERNS = [
    r"derive[sd]?\s+.*\b({})\b",
    r"\b({})\b\s+(?:is\s+)?derived",
    r"predict[s]?\s+.*\b({})\b",
    r"\b({})\b\s+(?:is\s+)?predicted",
    r"obtain[s]?\s+.*\b({})\b",
    r"\b({})\b\s+emerges",
    r"\b({})\b\s+follows\s+from",
]

# Patterns that indicate input usage
INPUT_PATTERNS = [
    r"using\s+.*\b({})\b",
    r"with\s+.*\b({})\b\s*[=≈]",
    r"\b({})\b\s*[=≈]\s*[\d.]",
    r"from\s+.*\b({})\b",
    r"given\s+.*\b({})\b",
    r"\b({})\b\s+as\s+input",
]

# Pattern synonyms
QUANTITY_SYNONYMS = {
    "G_F": ["G_F", "Fermi constant", "G_{F}", "\\GF"],
    "v": ["v", "Higgs VEV", "vacuum expectation", "246", "v_{EW}"],
    "M_W": ["M_W", "W mass", "W boson mass", "80.4", "80.377"],
    "M_Z": ["M_Z", "Z mass", "Z boson mass", "91.2", "91.1876"],
    "sin2_theta_W": ["sin²θ_W", "sin2_theta", "sin^2\\theta", "0.231"],
    "R_xi": ["R_xi", "R_ξ", "membrane thickness", "\\Rxi"],
    "delta": ["delta", "δ", "\\delta", "boundary layer"],
    "m_phi": ["m_phi", "m_φ", "mediator mass"],
    "g_2": ["g_2", "g₂", "SU(2) coupling"],
    "g_5": ["g_5", "g₅", "5D coupling"],
}

# ==============================================================================
# Scanner
# ==============================================================================

@dataclass
class CircularityViolation:
    """A detected circularity violation."""
    file: str
    line_num: int
    output_quantity: str
    forbidden_input: str
    context: str
    severity: str  # "CRITICAL" or "WARNING"

def find_quantity_in_line(line: str, quantity: str) -> bool:
    """Check if a quantity (or its synonyms) appears in a line."""
    synonyms = QUANTITY_SYNONYMS.get(quantity, [quantity])
    for syn in synonyms:
        if syn.lower() in line.lower():
            return True
    return False

def check_derivation_claim(line: str, output: str) -> bool:
    """Check if line claims to derive/predict output."""
    synonyms = QUANTITY_SYNONYMS.get(output, [output])
    for syn in synonyms:
        for pattern_template in DERIVATION_PATTERNS:
            pattern = pattern_template.format(re.escape(syn))
            if re.search(pattern, line, re.IGNORECASE):
                return True
    return False

def check_input_usage(line: str, input_qty: str) -> bool:
    """Check if line uses input_qty as input."""
    synonyms = QUANTITY_SYNONYMS.get(input_qty, [input_qty])
    for syn in synonyms:
        for pattern_template in INPUT_PATTERNS:
            pattern = pattern_template.format(re.escape(syn))
            if re.search(pattern, line, re.IGNORECASE):
                return True
    return False

def scan_file(filepath: Path) -> List[CircularityViolation]:
    """Scan a single LaTeX file for circularity violations."""
    violations = []

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"  Warning: Could not read {filepath}: {e}")
        return []

    # Track context (recent lines mentioning inputs)
    window_size = 10  # Look at surrounding lines
    input_context: Dict[str, List[int]] = {}  # input -> line numbers where used

    for i, line in enumerate(lines):
        line_num = i + 1

        # Track input usage
        for forbidden_input in CIRCULARITY_RULES.keys():
            if check_input_usage(line, forbidden_input):
                if forbidden_input not in input_context:
                    input_context[forbidden_input] = []
                input_context[forbidden_input].append(line_num)

        # Check for derivation claims
        for output, forbidden_inputs in CIRCULARITY_RULES.items():
            if check_derivation_claim(line, output):
                # Check if any forbidden input was used recently
                for forbidden_input in forbidden_inputs:
                    if forbidden_input in input_context:
                        recent_uses = [ln for ln in input_context[forbidden_input]
                                      if abs(ln - line_num) < window_size * 5]
                        if recent_uses:
                            violations.append(CircularityViolation(
                                file=str(filepath.relative_to(PAPER_DIR)),
                                line_num=line_num,
                                output_quantity=output,
                                forbidden_input=forbidden_input,
                                context=line.strip()[:100],
                                severity="CRITICAL" if output in ["G_F", "M_W", "v"] else "WARNING"
                            ))

    return violations

def scan_all_files() -> List[CircularityViolation]:
    """Scan all LaTeX files in sections/."""
    all_violations = []

    print("Scanning LaTeX files for circularity...")
    print()

    # Scan sections directory
    if SECTIONS_DIR.exists():
        for tex_file in SECTIONS_DIR.glob("*.tex"):
            print(f"  Scanning: {tex_file.name}")
            violations = scan_file(tex_file)
            all_violations.extend(violations)

    # Scan main document
    main_tex = PAPER_DIR / "EDC_Part_II_Weak_Sector.tex"
    if main_tex.exists():
        print(f"  Scanning: {main_tex.name}")
        violations = scan_file(main_tex)
        all_violations.extend(violations)

    return all_violations

# ==============================================================================
# Known Circularities (hardcoded)
# ==============================================================================

KNOWN_CIRCULARITIES = [
    CircularityViolation(
        file="sections/11_gf_derivation.tex",
        line_num=0,  # General
        output_quantity="G_F",
        forbidden_input="v (via G_F definition)",
        context="G_F 'exact agreement' uses v = (√2 G_F)^{-1/2} from muon decay",
        severity="CRITICAL"
    ),
    CircularityViolation(
        file="baseline",
        line_num=0,
        output_quantity="R_xi",
        forbidden_input="M_Z",
        context="R_xi = ℏc/M_Z uses EW scale as input (phenomenologically constrained)",
        severity="WARNING"
    ),
]

# ==============================================================================
# Main
# ==============================================================================

def main():
    print("=" * 70)
    print("EDC CIRCULARITY SCANNER")
    print("=" * 70)
    print()

    # Run scan
    violations = scan_all_files()

    # Add known circularities
    violations.extend(KNOWN_CIRCULARITIES)

    # Report
    print()
    print("-" * 70)
    print("CIRCULARITY VIOLATIONS FOUND")
    print("-" * 70)
    print()

    if violations:
        critical = [v for v in violations if v.severity == "CRITICAL"]
        warnings = [v for v in violations if v.severity == "WARNING"]

        if critical:
            print("CRITICAL (must fix):")
            for v in critical:
                print(f"  [{v.file}:{v.line_num}]")
                print(f"    Claims to derive: {v.output_quantity}")
                print(f"    But uses as input: {v.forbidden_input}")
                print(f"    Context: {v.context}")
                print(f"    FIX: Downgrade to [BL]/[I] or remove 'derived' claim")
                print()

        if warnings:
            print("WARNING (should document):")
            for v in warnings:
                print(f"  [{v.file}:{v.line_num}]")
                print(f"    Claims to derive: {v.output_quantity}")
                print(f"    But uses as input: {v.forbidden_input}")
                print(f"    Context: {v.context}")
                print()

        print(f"Total: {len(critical)} critical, {len(warnings)} warnings")
    else:
        print("No circularity violations detected.")

    # Save results
    output_dir = PAPER_DIR / "generated"
    output_dir.mkdir(exist_ok=True)

    import json
    results = [
        {
            "file": v.file,
            "line": v.line_num,
            "output": v.output_quantity,
            "forbidden_input": v.forbidden_input,
            "context": v.context,
            "severity": v.severity
        }
        for v in violations
    ]

    with open(output_dir / "circularity_check_results.json", 'w') as f:
        json.dump(results, f, indent=2)

    print()
    print(f"Results saved to: {output_dir}/circularity_check_results.json")

    # Return exit code
    return 1 if any(v.severity == "CRITICAL" for v in violations) else 0

if __name__ == "__main__":
    sys.exit(main())
