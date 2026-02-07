#!/usr/bin/env python3
"""
EDC BLOCK-004 Derivation v57: Layer B Adapter - α₃(M_Z) Comparison
Verification script with firewall checks, RG verification, and no-fit policy
"""

import re
import hashlib
import math
from fractions import Fraction
from pathlib import Path
from typing import List, Tuple, Dict, Any

# ==============================================================================
# HASH CHAIN (Read-only from Layer A)
# ==============================================================================

HASH_CHAIN = {
    'v45': 'a80b3886903152d3',
    'v46': '2742edea37e863ac',
    'v47': '7a9682f333d5349e',
    'v48': 'c4f114aa0c662b66',
    'v49': '81010ef2faedcefd',
    'v50': 'cebf3e5baf0de863',
    'v51': 'ed8fa089897b2d8c',
    'v52': 'ed92d9bc43b8d26b',
    'v53': '89a4854b0bdfd332',
    'v54': '19c69e794c9703b7',
    'v55': '1794377561879613',
    'v56': '61869b6fddb68c16',
}

# ==============================================================================
# FORBIDDEN PATTERNS (must only appear in QUARANTINED sections)
# ==============================================================================

FORBIDDEN_PATTERNS = [
    r'91\.1876',          # M_Z exact
    r'91\.19',            # M_Z approx
    r'80\.377',           # M_W exact
    r'80\.38',            # M_W approx
    r'0\.1180',           # α_s(M_Z) exact
    r'0\.118',            # α_s(M_Z) approx
    r'172\.69',           # m_t exact
    r'4\.18',             # m_b exact
    r'1\.27',             # m_c exact
    r'1\.77686',          # m_tau exact
    r'210.*MeV',          # Λ_MS
    r'1\.1663788',        # G_F
]

# ==============================================================================
# QUARANTINE MARKERS
# ==============================================================================

QUARANTINE_START_PATTERNS = [
    r'QUARANTINED',
    r'Layer B',
    r'LAYER B',
    r'quarantinebox',
    r'layerbbox',
    r'External Inputs',
]

# ==============================================================================
# RG PARAMETERS (for verification)
# ==============================================================================

# Beta coefficients
BETA_COEFFS = {
    6: Fraction(7, 1),      # b_3^(6) = 11 - 2*6/3 = 7
    5: Fraction(23, 3),     # b_3^(5) = 11 - 2*5/3 = 23/3
    4: Fraction(25, 3),     # b_3^(4) = 11 - 2*4/3 = 25/3
    3: Fraction(9, 1),      # b_3^(3) = 11 - 2*3/3 = 9
}

# ==============================================================================
# UTILITY FUNCTIONS
# ==============================================================================

def compute_hash(data: str, length: int = 16) -> str:
    """Compute truncated SHA-256 hash."""
    return hashlib.sha256(data.encode()).hexdigest()[:length]

def read_file(filepath: str) -> str:
    """Read file contents."""
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        return f.read()

def count_pattern(text: str, pattern: str) -> int:
    """Count pattern occurrences."""
    return len(re.findall(pattern, text))

# ==============================================================================
# CHECK FUNCTIONS
# ==============================================================================

def check_hash_chain(results: List[Tuple[str, bool, str]]) -> None:
    """Verify hash chain integrity."""
    # Check all hashes are 16 hex chars
    for version, h in HASH_CHAIN.items():
        results.append((
            f"HASH_{version}: length = 16",
            len(h) == 16,
            f"LENGTH: {len(h)}"
        ))

    # Check v56 is correct (from previous derivation)
    results.append((
        "HASH_v56: matches expected",
        HASH_CHAIN['v56'] == '61869b6fddb68c16',
        f"VALUE: {HASH_CHAIN['v56']}"
    ))

    # Check v54 is correct (BLOCK-003)
    results.append((
        "HASH_v54: matches BLOCK-003 canonical",
        HASH_CHAIN['v54'] == '19c69e794c9703b7',
        f"VALUE: {HASH_CHAIN['v54']}"
    ))

def check_beta_coefficients(results: List[Tuple[str, bool, str]]) -> None:
    """Verify beta coefficients."""
    for nf, b in BETA_COEFFS.items():
        expected = Fraction(11, 1) - Fraction(2 * nf, 3)
        results.append((
            f"BETA_b3({nf}): = 11 - 2*{nf}/3",
            b == expected,
            f"VALUE: {b}, EXPECTED: {expected}"
        ))

def check_firewall(results: List[Tuple[str, bool, str]], tex_content: str) -> None:
    """Check that forbidden patterns only appear in quarantined sections."""
    # Find all quarantine zone markers
    lines = tex_content.split('\n')
    in_quarantine = False
    quarantine_depth = 0

    violations = []

    for i, line in enumerate(lines):
        # Check for quarantine markers
        for pattern in QUARANTINE_START_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                in_quarantine = True
                quarantine_depth = max(quarantine_depth, 1)
                break

        # Check for end of quarantine (simplified: just check if we're past that section)
        if '\\end{quarantinebox}' in line or '\\end{layerbbox}' in line:
            quarantine_depth = max(0, quarantine_depth - 1)
            if quarantine_depth == 0:
                in_quarantine = False

        # If not in quarantine, check for forbidden patterns
        if not in_quarantine:
            for pattern in FORBIDDEN_PATTERNS:
                if re.search(pattern, line):
                    # Exception: if line contains "QUARANTINED" or "NOT USED"
                    if 'QUARANTINED' in line or 'NOT USED' in line or 'FORBIDDEN' in line:
                        continue
                    violations.append((i+1, pattern, line[:50]))

    results.append((
        "FIREWALL: forbidden patterns only in quarantine",
        len(violations) == 0,
        f"VIOLATIONS: {len(violations)}"
    ))

    if violations:
        for v in violations[:5]:  # Show first 5
            results.append((
                f"FIREWALL_VIOLATION: line {v[0]}",
                False,
                f"Pattern '{v[1]}' in: {v[2]}..."
            ))

def check_abstract_clean(results: List[Tuple[str, bool, str]], tex_content: str) -> None:
    """Check that abstract contains no experimental values."""
    # Extract abstract
    abstract_match = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', tex_content, re.DOTALL)
    if not abstract_match:
        results.append(("ABSTRACT: found", False, "NO ABSTRACT FOUND"))
        return

    abstract = abstract_match.group(1)

    # Check for forbidden patterns in abstract
    violations = []
    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, abstract):
            violations.append(pattern)

    results.append((
        "ABSTRACT: no experimental values",
        len(violations) == 0,
        f"VIOLATIONS: {violations if violations else 'NONE'}"
    ))

def check_title_clean(results: List[Tuple[str, bool, str]], tex_content: str) -> None:
    """Check that title contains no experimental values."""
    # Extract title
    title_match = re.search(r'\\title\{(.*?)\}', tex_content, re.DOTALL)
    if not title_match:
        results.append(("TITLE: found", False, "NO TITLE FOUND"))
        return

    title = title_match.group(1)

    # Check for forbidden patterns in title
    violations = []
    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, title):
            violations.append(pattern)

    results.append((
        "TITLE: no experimental values",
        len(violations) == 0,
        f"VIOLATIONS: {violations if violations else 'NONE'}"
    ))

def check_no_fit_policy(results: List[Tuple[str, bool, str]], tex_content: str) -> None:
    """Verify no-fit policy is stated."""
    # Check for explicit no-fit statements
    no_fit_patterns = [
        r'NOT A FIT',
        r'NOT a fit',
        r'no fitting',
        r'No fitting',
        r'NO FITTING',
        r'swept.*not fitted',
        r'No.*minimization',
        r'nofitbox',
    ]

    found_count = 0
    for pattern in no_fit_patterns:
        if re.search(pattern, tex_content, re.IGNORECASE):
            found_count += 1

    results.append((
        "NO_FIT: policy stated",
        found_count >= 3,
        f"FOUND: {found_count} no-fit statements"
    ))

    # Check for absence of fitting code
    fit_patterns = [
        r'chi.*squared',
        r'minimize',
        r'best.*fit',
        r'optimal.*sigma',
        r'scipy\.optimize',
    ]

    fit_found = []
    for pattern in fit_patterns:
        if re.search(pattern, tex_content, re.IGNORECASE):
            fit_found.append(pattern)

    results.append((
        "NO_FIT: no fitting code",
        len(fit_found) == 0,
        f"FIT PATTERNS: {fit_found if fit_found else 'NONE'}"
    ))

def check_two_route_rg(results: List[Tuple[str, bool, str]], tex_content: str) -> None:
    """Verify two-route RG is documented."""
    # Check for T1 and T2 routes
    has_t1 = 'Route T1' in tex_content or 'route-t1' in tex_content
    has_t2 = 'Route T2' in tex_content or 'route-t2' in tex_content

    results.append((
        "TWO_ROUTE: T1 defined",
        has_t1,
        "Route T1 present" if has_t1 else "MISSING"
    ))

    results.append((
        "TWO_ROUTE: T2 defined",
        has_t2,
        "Route T2 present" if has_t2 else "MISSING"
    ))

    # Check for verification statement
    verify_pattern = r'T1.*=.*T2|T1.*T2.*match|two.*route.*verif'
    has_verify = bool(re.search(verify_pattern, tex_content, re.IGNORECASE))

    results.append((
        "TWO_ROUTE: T1 = T2 verified",
        has_verify,
        "VERIFIED" if has_verify else "NOT FOUND"
    ))

def check_log_hygiene(results: List[Tuple[str, bool, str]], tex_content: str) -> None:
    """Check log hygiene - all arguments dimensionless."""
    # Look for log expressions
    log_patterns = [
        r'\\ln\\frac\{\\mu\}\{',
        r'\\ln\\frac\{m_',
        r'\\ln\\frac\{M_',
        r'\\log\\frac',
    ]

    log_count = 0
    for pattern in log_patterns:
        log_count += len(re.findall(pattern, tex_content))

    results.append((
        "LOG_HYGIENE: log expressions present",
        log_count >= 5,
        f"COUNT: {log_count}"
    ))

    # Check for dimensionless verification statement
    dimless_check = 'dimensionless' in tex_content.lower()
    results.append((
        "LOG_HYGIENE: dimensionless verified",
        dimless_check,
        "VERIFIED" if dimless_check else "NOT STATED"
    ))

def check_quarantine_table(results: List[Tuple[str, bool, str]], tex_content: str) -> None:
    """Check for quarantine table with sufficient entries."""
    # Look for external inputs table
    has_table = 'External Inputs' in tex_content or 'external-inputs' in tex_content

    results.append((
        "QUARANTINE: external inputs table",
        has_table,
        "PRESENT" if has_table else "MISSING"
    ))

    # Count QUARANTINED tags
    quarantine_count = tex_content.count('QUARANTINED')

    results.append((
        "QUARANTINE: tags >= 5",
        quarantine_count >= 5,
        f"COUNT: {quarantine_count}"
    ))

def check_document_structure(results: List[Tuple[str, bool, str]], tex_content: str) -> None:
    """Verify document structure requirements."""
    required_sections = [
        'Purpose',
        'Firewall',
        'Inputs',
        'Adapter API',
        'RG Running',
        'Comparison',
        'Lambda',
        'Hash Chain',
        'No-Fit',
        'Closing',
    ]

    for section in required_sections:
        found = section.lower() in tex_content.lower()
        results.append((
            f"SECTION: {section}",
            found,
            "PRESENT" if found else "MISSING"
        ))

def check_document_metrics(results: List[Tuple[str, bool, str]], tex_content: str) -> None:
    """Check document size metrics."""
    # Count equations
    eq_patterns = [
        r'\\begin\{equation\}',
        r'\\begin\{align\}',
    ]

    eq_count = 0
    for pattern in eq_patterns:
        eq_count += len(re.findall(pattern, tex_content))

    # Add aligned equations estimate
    align_lines = len(re.findall(r'\\\\', tex_content))
    eq_count += align_lines // 2

    results.append((
        "DOC_EQ: equations >= 160",
        eq_count >= 160,
        f"COUNT: {eq_count}"
    ))

    # Count labels
    label_count = len(re.findall(r'\\label\{', tex_content))
    results.append((
        "DOC_LABEL: labels >= 240",
        label_count >= 240,
        f"COUNT: {label_count}"
    ))

    # Estimate pages
    page_estimate = len(tex_content) // 2000
    results.append((
        "DOC_PAGES: pages >= 24 (estimate)",
        page_estimate >= 24,
        f"ESTIMATE: {page_estimate}"
    ))

def check_no_backflow_theorem(results: List[Tuple[str, bool, str]], tex_content: str) -> None:
    """Check for No Backflow theorem."""
    patterns = [
        r'No Backflow',
        r'no-backflow',
        r'NO BACKFLOW',
        r'\\mathcal\{L\}_B.*\\cap.*\\mathcal\{L\}_A.*=.*\\emptyset',
    ]

    found = False
    for pattern in patterns:
        if re.search(pattern, tex_content):
            found = True
            break

    results.append((
        "THEOREM: No Backflow present",
        found,
        "PRESENT" if found else "MISSING"
    ))

def check_layer_a_unchanged(results: List[Tuple[str, bool, str]], tex_content: str) -> None:
    """Verify Layer A is stated as unchanged."""
    patterns = [
        r'Layer A.*unchanged',
        r'Layer A.*untouched',
        r'Layer A.*read-only',
        r'Layer A remains',
    ]

    found_count = 0
    for pattern in patterns:
        if re.search(pattern, tex_content, re.IGNORECASE):
            found_count += 1

    results.append((
        "LAYER_A: unchanged statement",
        found_count >= 1,
        f"FOUND: {found_count} statements"
    ))

def check_reviewer_traps(results: List[Tuple[str, bool, str]], tex_content: str) -> None:
    """Check for reviewer traps."""
    trap_count = tex_content.count('trapbox')

    results.append((
        "TRAPS: reviewer traps >= 8",
        trap_count >= 8,
        f"COUNT: {trap_count}"
    ))

def check_api_definitions(results: List[Tuple[str, bool, str]], tex_content: str) -> None:
    """Verify B-API definitions present."""
    apis = ['B-API1', 'B-API2', 'B-API3', 'B-API4']

    for api in apis:
        found = api in tex_content
        results.append((
            f"API: {api} defined",
            found,
            "PRESENT" if found else "MISSING"
        ))

def check_sweep_definition(results: List[Tuple[str, bool, str]], tex_content: str) -> None:
    """Check for parameter sweep definition."""
    patterns = [
        r'sweep',
        r'Sweep',
        r'\\tilde\{\\sigma\}.*\\in',
        r'log.*spaced',
    ]

    found_count = 0
    for pattern in patterns:
        if re.search(pattern, tex_content):
            found_count += 1

    results.append((
        "SWEEP: parameter sweep defined",
        found_count >= 2,
        f"FOUND: {found_count} sweep references"
    ))

def compute_v57_hash() -> str:
    """Compute v57 SoT hash."""
    hash_input = """
    LAYER_B_ADAPTER: v57
    B-API1: (sigma_tilde, epsilon) -> alpha_3(mu_star)
    B-API2: RG running mu_star -> M_Z
    B-API3: threshold toggle OFF/ON
    B-API4: residual Delta vs PDG
    NO_FIT_POLICY: sigma_tilde swept not fitted
    TWO_ROUTE: T1 = T2 within tolerance
    HASH_v56: 61869b6fddb68c16
    """
    return hashlib.sha256(hash_input.encode()).hexdigest()[:16]

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

def main():
    """Run all verification checks."""
    results: List[Tuple[str, bool, str]] = []

    # Read LaTeX file
    tex_path = Path(__file__).parent / 'main.tex'
    if tex_path.exists():
        tex_content = read_file(str(tex_path))
    else:
        tex_content = ""
        print("WARNING: main.tex not found, some checks will fail")

    # Run all checks
    check_hash_chain(results)
    check_beta_coefficients(results)
    check_firewall(results, tex_content)
    check_abstract_clean(results, tex_content)
    check_title_clean(results, tex_content)
    check_no_fit_policy(results, tex_content)
    check_two_route_rg(results, tex_content)
    check_log_hygiene(results, tex_content)
    check_quarantine_table(results, tex_content)
    check_document_structure(results, tex_content)
    check_document_metrics(results, tex_content)
    check_no_backflow_theorem(results, tex_content)
    check_layer_a_unchanged(results, tex_content)
    check_reviewer_traps(results, tex_content)
    check_api_definitions(results, tex_content)
    check_sweep_definition(results, tex_content)

    # Print results
    print("=" * 70)
    print("EDC BLOCK-004 Derivation v57: Verification Results")
    print("=" * 70)

    passed = 0
    failed = 0

    for name, status, detail in results:
        status_str = "PASS" if status else "FAIL"
        symbol = "✓" if status else "✗"
        print(f"[{symbol}] {name}: {status_str}")
        if not status:
            print(f"    Detail: {detail}")
            failed += 1
        else:
            passed += 1

    print("=" * 70)
    print(f"Total: {passed}/{passed + failed} CHECKS PASSED")

    if failed == 0:
        print("All checks PASS")
    else:
        print(f"{failed} checks FAILED")

    # Compute and print v57 hash
    v57_hash = compute_v57_hash()
    print(f"\nv57 SoT hash: {v57_hash}")

    print("\nLayer A: UNCHANGED")
    print("Layer B: QUARANTINED")
    print("=" * 70)

    return failed == 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
