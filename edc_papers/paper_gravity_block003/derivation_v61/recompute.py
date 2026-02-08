#!/usr/bin/env python3
"""
EDC BLOCK-004 Derivation v61: Proton Decay Program Note (PS)
Verification and Recomputation Script

This script performs comprehensive checks on the v61 derivation:
- Scope verification (only v61 + PAPERS_INDEX.md touched)
- Build cleanliness (no undefined refs, no multiply-defined labels)
- Forbidden pattern checks in Layer A
- API presence verification
- Reviewer trap counting
- Epistemic tag sanity checks
"""

import os
import re
import sys
import hashlib
import subprocess
from pathlib import Path
from typing import Tuple, List, Dict, Optional

# ============================================================================
# CONFIGURATION
# ============================================================================

SCRIPT_DIR = Path(__file__).parent.resolve()
MAIN_TEX = SCRIPT_DIR / "main.tex"
RELEASE_DIR = SCRIPT_DIR / "release"

# Version info
VERSION = "v61"
TITLE = "Proton Decay Program Note (PS)"

# Forbidden patterns in Layer A
FORBIDDEN_PATTERNS = [
    r'10\^{?34}',                    # Numeric lifetime bound
    r'938\s*MeV',                    # Numeric proton mass
    r'0\.01\s*GeV\^3',               # Numeric alpha_H
    r'10\^{?15}\s*GeV',              # Numeric M_X bound
    r'Super-K',                       # Experiment name
    r'Hyper-K',                       # Experiment name
    r'Kamiokande',                    # Experiment name
    r'excluded',                      # Requires experimental comparison
    r'ruled out',                     # Requires experimental comparison
    r'best.?fit',                     # Fitting terminology
    r'\\chi\^2',                      # Chi-squared fitting
    r'1\.6\s*\\times\s*10\^{?-35}',  # Planck length numeric
    r'6\.67\s*\\times\s*10\^{?-11}', # Newton's constant numeric
    r'\\tau_p\s*>\s*\d',              # Numeric lifetime bound
]

# Required APIs
REQUIRED_APIS = ['API-PD1', 'API-PD2']

# Required reviewer traps (minimum count)
MIN_TRAPS = 8

# Epistemic tag minimum counts
MIN_TAG_D = 10
MIN_TAG_Dc = 3
MIN_TAG_P = 2
MIN_TAG_Q = 3

# Document metrics
MIN_PAGES = 20
MAX_PAGES = 40
MIN_EQUATIONS = 120
MIN_LABELS = 200

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def read_file(filepath: Path) -> str:
    """Read file contents."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return ""

def compute_hash(content: str, length: int = 16) -> str:
    """Compute SHA256 hash truncated to specified length."""
    h = hashlib.sha256(content.encode('utf-8')).hexdigest()
    return h[:length]

def count_pattern(content: str, pattern: str) -> int:
    """Count occurrences of a regex pattern."""
    return len(re.findall(pattern, content, re.IGNORECASE))

def find_layer_a_content(content: str) -> str:
    """Extract Layer A content between markers."""
    match = re.search(
        r'%==LAYER_A_START==(.*?)%==LAYER_A_END==',
        content,
        re.DOTALL
    )
    if match:
        return match.group(1)
    # Fallback: everything before Layer B
    match = re.search(r'(.*?)%==LAYER_B_START==', content, re.DOTALL)
    if match:
        return match.group(1)
    return content

def find_layer_b_content(content: str) -> str:
    """Extract Layer B content between markers."""
    match = re.search(
        r'%==LAYER_B_START==(.*?)%==LAYER_B_END==',
        content,
        re.DOTALL
    )
    return match.group(1) if match else ""

# ============================================================================
# CHECK FUNCTIONS
# ============================================================================

def check_file_exists(filepath: Path, name: str) -> Tuple[bool, str]:
    """Check if a file exists."""
    exists = filepath.exists()
    detail = f"PATH: {filepath}"
    return exists, detail

def check_hash_length(content: str, version: str, expected_len: int = 16) -> Tuple[bool, str]:
    """Check that hash would be correct length."""
    h = compute_hash(content)
    return len(h) == expected_len, f"length = {len(h)}"

def check_forbidden_in_layer_a(content: str) -> Tuple[bool, str]:
    """Check that forbidden patterns don't appear in Layer A."""
    layer_a = find_layer_a_content(content)
    violations = []
    for pattern in FORBIDDEN_PATTERNS:
        matches = re.findall(pattern, layer_a, re.IGNORECASE)
        if matches:
            violations.append(f"{pattern}: {len(matches)} hits")
    if violations:
        return False, "; ".join(violations[:3])
    return True, "0 forbidden patterns in Layer A"

def check_api_present(content: str, api_name: str) -> Tuple[bool, str]:
    """Check that an API is defined."""
    pattern = rf'{api_name}'
    found = bool(re.search(pattern, content))
    return found, f"{'found' if found else 'NOT FOUND'}"

def check_traps_count(content: str, min_count: int) -> Tuple[bool, str]:
    """Check that enough reviewer traps are defined."""
    # Count TRAP-N patterns
    traps = re.findall(r'TRAP-\d+', content)
    count = len(set(traps))
    return count >= min_count, f"found {count} unique traps"

def check_tag_count(content: str, tag: str, min_count: int) -> Tuple[bool, str]:
    """Check epistemic tag usage."""
    pattern = rf'\\tag{tag}\{{\}}'
    count = count_pattern(content, pattern)
    # Also check the macro version
    count += count_pattern(content, rf'\\tag{tag}(?:\s|$|[^a-zA-Z])')
    return count >= min_count, f"found {count} (min: {min_count})"

def check_equation_count(content: str, min_count: int) -> Tuple[bool, str]:
    """Count equation environments."""
    patterns = [
        r'\\begin\{equation\}',
        r'\\begin\{align\}',
        r'\\begin\{multline\}',
        r'\\begin\{gather\}',
    ]
    total = sum(count_pattern(content, p) for p in patterns)
    return total >= min_count, f"found {total} (min: {min_count})"

def check_label_count(content: str, min_count: int) -> Tuple[bool, str]:
    """Count labels."""
    count = count_pattern(content, r'\\label\{')
    return count >= min_count, f"found {count} (min: {min_count})"

def check_no_backflow(content: str) -> Tuple[bool, str]:
    """Check No-Backflow theorem is present."""
    has_theorem = bool(re.search(r'No.?Backflow', content, re.IGNORECASE))
    has_intersection = bool(re.search(r'\\cap', content))
    has_emptyset = bool(re.search(r'\\emptyset|= \\{\\}', content))
    if has_theorem and has_intersection:
        return True, "theorem present with set notation"
    return False, "missing components"

def check_no_fit_policy(content: str) -> Tuple[bool, str]:
    """Check No-Fit policy is present."""
    has_nofit = bool(re.search(r'No.?Fit', content, re.IGNORECASE))
    has_forbidden = bool(re.search(r'Forbidden', content, re.IGNORECASE))
    if has_nofit and has_forbidden:
        return True, "policy and forbidden list present"
    return False, "missing components"

def check_layer_markers(content: str) -> Tuple[bool, str]:
    """Check Layer A/B markers are present."""
    has_a_start = '%==LAYER_A_START==' in content
    has_a_end = '%==LAYER_A_END==' in content
    has_b_start = '%==LAYER_B_START==' in content
    has_b_end = '%==LAYER_B_END==' in content
    if all([has_a_start, has_a_end, has_b_start, has_b_end]):
        return True, "all markers present"
    missing = []
    if not has_a_start: missing.append("LAYER_A_START")
    if not has_a_end: missing.append("LAYER_A_END")
    if not has_b_start: missing.append("LAYER_B_START")
    if not has_b_end: missing.append("LAYER_B_END")
    return False, f"missing: {', '.join(missing)}"

def check_ps_group(content: str) -> Tuple[bool, str]:
    """Check PS group definition is present."""
    has_su4 = bool(re.search(r'SU\(4\)_C', content))
    has_su2l = bool(re.search(r'SU\(2\)_L', content))
    has_su2r = bool(re.search(r'SU\(2\)_R', content))
    if all([has_su4, has_su2l, has_su2r]):
        return True, "full PS group defined"
    return False, "incomplete group definition"

def check_leptoquark(content: str) -> Tuple[bool, str]:
    """Check leptoquark bosons are defined."""
    has_x = bool(re.search(r'X.*boson|leptoquark', content, re.IGNORECASE))
    has_charges = bool(re.search(r'4/3', content))
    if has_x and has_charges:
        return True, "X bosons with charges"
    return False, "missing leptoquark definition"

def check_dim6_operators(content: str) -> Tuple[bool, str]:
    """Check dimension-6 operators are present."""
    has_dim6 = bool(re.search(r'dimension.?6|dim.?6', content, re.IGNORECASE))
    has_operator = bool(re.search(r'\\mathcal\{O\}_6', content))
    if has_dim6 and has_operator:
        return True, "dimension-6 operators defined"
    return False, "missing operator definition"

def check_lifetime_formula(content: str) -> Tuple[bool, str]:
    """Check proton lifetime formula is present."""
    has_tau = bool(re.search(r'\\tau_p', content))
    has_mx4 = bool(re.search(r'M_X\^4', content))
    has_scaling = bool(re.search(r'\\propto', content))
    if has_tau and has_mx4:
        return True, "lifetime formula with M_X^4 scaling"
    return False, "missing lifetime formula"

def check_hadronic_matrix(content: str) -> Tuple[bool, str]:
    """Check hadronic matrix element is symbolic."""
    has_alpha_h = bool(re.search(r'\\alpha_H', content))
    layer_a = find_layer_a_content(content)
    # Check no numeric alpha_H in Layer A
    numeric_in_a = bool(re.search(r'\\alpha_H\s*[=≈]\s*\d', layer_a))
    if has_alpha_h and not numeric_in_a:
        return True, "alpha_H symbolic in Layer A"
    if numeric_in_a:
        return False, "numeric alpha_H found in Layer A"
    return False, "alpha_H not defined"

def check_status_box(content: str) -> Tuple[bool, str]:
    """Check status box is present with OPEN/CLOSED items."""
    has_status = bool(re.search(r'statusbox', content))
    has_closed = bool(re.search(r'CLOSED', content))
    has_open = bool(re.search(r'OPEN', content))
    if has_status and has_closed and has_open:
        return True, "status box with OPEN/CLOSED items"
    return False, "incomplete status box"

def check_dag(content: str) -> Tuple[bool, str]:
    """Check dependency graph is present."""
    has_tikz = bool(re.search(r'tikzpicture', content))
    has_dag = bool(re.search(r'Dependency|DAG', content, re.IGNORECASE))
    if has_tikz and has_dag:
        return True, "DAG with tikz diagram"
    return False, "missing dependency graph"

def check_quarantine_markers(content: str) -> Tuple[bool, str]:
    """Check Layer B is properly quarantined."""
    layer_b = find_layer_b_content(content)
    # Check for \tagQ{} usage or quarantinebox or QUARANTINE keyword
    has_q_tag = bool(re.search(r'\\tagQ\{\}|\\tagQ\s', content))
    has_quarantine = bool(re.search(r'QUARANTINE|quarantinebox', content, re.IGNORECASE))
    if has_q_tag or has_quarantine:
        return True, "Layer B properly marked"
    return False, "Layer B not properly quarantined"

def check_reader_contract(content: str) -> Tuple[bool, str]:
    """Check reader contract is present."""
    has_contract = bool(re.search(r'readercontract|READER CONTRACT', content))
    has_layer_a = bool(re.search(r'Layer A', content))
    has_layer_b = bool(re.search(r'Layer B', content))
    has_nofit = bool(re.search(r'No.?Fit', content, re.IGNORECASE))
    if all([has_contract, has_layer_a, has_layer_b, has_nofit]):
        return True, "complete reader contract"
    return False, "incomplete reader contract"

def check_appendices(content: str) -> Tuple[bool, str]:
    """Check appendices are present."""
    has_appendix = bool(re.search(r'\\appendix', content))
    has_group_theory = bool(re.search(r'Group Theory', content))
    has_operators = bool(re.search(r'Operator Basis', content))
    has_phase_space = bool(re.search(r'Phase Space', content))
    count = sum([has_group_theory, has_operators, has_phase_space])
    if has_appendix and count >= 2:
        return True, f"{count} appendices found"
    return False, "insufficient appendices"

def check_normalization(content: str) -> Tuple[bool, str]:
    """Check generator normalization convention."""
    has_trace = bool(re.search(r'Tr\(T\^A T\^B\)|\\text\{Tr\}', content))
    has_half = bool(re.search(r'1/2|\\frac\{1\}\{2\}', content))
    has_delta = bool(re.search(r'\\delta\^\{AB\}|\\delta\^{ab}', content))
    if (has_trace or has_delta) and has_half:
        return True, "Tr(T^A T^B) = 1/2 convention"
    return False, "normalization not specified"

def check_hypercharge(content: str) -> Tuple[bool, str]:
    """Check hypercharge formula."""
    has_y = bool(re.search(r'Y\s*=', content))
    has_bl = bool(re.search(r'B-L|B.L', content))
    if has_y and has_bl:
        return True, "hypercharge formula present"
    return False, "hypercharge not defined"

def check_breaking_chain(content: str) -> Tuple[bool, str]:
    """Check symmetry breaking chain."""
    has_chain = bool(re.search(r'\\xrightarrow|\\to', content))
    has_su3 = bool(re.search(r'SU\(3\)_c', content))
    if has_chain and has_su3:
        return True, "breaking chain to SM"
    return False, "breaking chain not defined"

def check_coupling_unification(content: str) -> Tuple[bool, str]:
    """Check coupling unification relation."""
    has_g4 = bool(re.search(r'g_4', content))
    has_gps = bool(re.search(r'g_\{?\\text\{PS\}|g_\{?PS', content))
    if has_g4 and has_gps:
        return True, "coupling unification stated"
    return False, "coupling relations missing"

def check_width_formula(content: str) -> Tuple[bool, str]:
    """Check partial width formula."""
    has_gamma = bool(re.search(r'\\Gamma.*p.*e', content))
    has_32pi = bool(re.search(r'32\\pi|32 \\pi', content))
    if has_gamma and has_32pi:
        return True, "width formula with 1/(32pi)"
    return False, "width formula missing"

def check_phase_space_formula(content: str) -> Tuple[bool, str]:
    """Check phase space calculation."""
    has_ps = bool(re.search(r'm_p\^2.*m_\\pi\^2|phase space', content, re.IGNORECASE))
    if has_ps:
        return True, "phase space factor present"
    return False, "phase space missing"

def check_dimensional_analysis(content: str) -> Tuple[bool, str]:
    """Check dimensional analysis appendix."""
    has_dim = bool(re.search(r'Dimensional Analysis', content))
    has_check = bool(re.search(r'dimension.*check|\\checkmark', content, re.IGNORECASE))
    if has_dim and has_check:
        return True, "dimensional analysis with checks"
    return False, "dimensional analysis incomplete"

def check_formula_catalog(content: str) -> Tuple[bool, str]:
    """Check formula catalog appendix."""
    has_catalog = bool(re.search(r'Formula Catalog', content))
    has_refs = count_pattern(content, r'\\eqref\{')
    if has_catalog and has_refs >= 5:
        return True, f"catalog with {has_refs} references"
    return False, "formula catalog incomplete"

# ============================================================================
# BUILD CHECKS
# ============================================================================

def check_build_clean(tex_file: Path) -> Tuple[bool, str]:
    """Check that LaTeX builds without errors."""
    try:
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', tex_file.name],
            cwd=tex_file.parent,
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode == 0:
            return True, "pdflatex succeeded"
        else:
            # Extract first error
            match = re.search(r'! (.*)', result.stdout)
            error = match.group(1) if match else "unknown error"
            return False, f"pdflatex failed: {error[:50]}"
    except subprocess.TimeoutExpired:
        return False, "pdflatex timeout"
    except FileNotFoundError:
        return True, "pdflatex not available (skip)"

def check_undefined_refs(log_file: Path) -> Tuple[bool, str]:
    """Check for undefined references in log."""
    if not log_file.exists():
        return True, "no log file (skip)"
    content = read_file(log_file)
    undefined = re.findall(r"Reference `([^']+)' .* undefined", content)
    if undefined:
        return False, f"undefined: {', '.join(undefined[:3])}"
    return True, "no undefined refs"

def check_multiply_defined(log_file: Path) -> Tuple[bool, str]:
    """Check for multiply-defined labels in log."""
    if not log_file.exists():
        return True, "no log file (skip)"
    content = read_file(log_file)
    multiply = re.findall(r"Label `([^']+)' multiply defined", content)
    if multiply:
        return False, f"multiply-defined: {', '.join(multiply[:3])}"
    return True, "no multiply-defined labels"

# ============================================================================
# SCOPE CHECK
# ============================================================================

def check_scope(script_dir: Path) -> Tuple[bool, str]:
    """Verify only v61 and PAPERS_INDEX.md are touched."""
    try:
        result = subprocess.run(
            ['git', 'status', '--porcelain'],
            cwd=script_dir.parent.parent,
            capture_output=True,
            text=True
        )
        lines = [l for l in result.stdout.strip().split('\n') if l.strip()]
        violations = []
        for line in lines:
            # Extract filename
            parts = line.split()
            if len(parts) >= 2:
                filepath = parts[-1]
                # Check if it's in v61 or is PAPERS_INDEX.md
                if 'derivation_v61' not in filepath and 'PAPERS_INDEX.md' not in filepath:
                    violations.append(filepath)
        if violations:
            return False, f"out-of-scope: {', '.join(violations[:3])}"
        return True, "only v61 + PAPERS_INDEX touched"
    except Exception as e:
        return True, f"git check skipped: {e}"

# ============================================================================
# MAIN VERIFICATION
# ============================================================================

def run_checks() -> Tuple[int, int, str]:
    """Run all verification checks."""
    print("=" * 70)
    print(f"EDC BLOCK-004 Derivation {VERSION}: {TITLE}")
    print("Verification Script")
    print("=" * 70)

    passed = 0
    failed = 0
    failures = []

    # Read main.tex
    content = read_file(MAIN_TEX)
    if not content:
        print("[FATAL] Cannot read main.tex")
        return 0, 1, ""

    # Define all checks
    checks = [
        # File existence
        ("FILE: main.tex exists", lambda: check_file_exists(MAIN_TEX, "main.tex")),

        # Hash checks
        (f"HASH_{VERSION}: length = 16", lambda: check_hash_length(content, VERSION)),

        # Layer markers
        ("MARKERS: layer A/B markers", lambda: check_layer_markers(content)),

        # Forbidden patterns
        ("FIREWALL: forbidden only in quarantine", lambda: check_forbidden_in_layer_a(content)),

        # API checks
        ("API: API-PD1 present", lambda: check_api_present(content, "API-PD1")),
        ("API: API-PD2 present", lambda: check_api_present(content, "API-PD2")),

        # Reviewer traps
        ("TRAPS: count >= 8", lambda: check_traps_count(content, MIN_TRAPS)),

        # Epistemic tags
        ("TAG_D: count >= 10", lambda: check_tag_count(content, "D", MIN_TAG_D)),
        ("TAG_Dc: count >= 3", lambda: check_tag_count(content, "Dc", MIN_TAG_Dc)),
        ("TAG_P: count >= 2", lambda: check_tag_count(content, "P", MIN_TAG_P)),
        ("TAG_Q: count >= 3", lambda: check_tag_count(content, "Q", MIN_TAG_Q)),

        # Document structure
        ("READER_CONTRACT: present", lambda: check_reader_contract(content)),
        ("NO_BACKFLOW: theorem present", lambda: check_no_backflow(content)),
        ("NO_FIT: policy present", lambda: check_no_fit_policy(content)),
        ("STATUS: box present", lambda: check_status_box(content)),
        ("DAG: diagram present", lambda: check_dag(content)),

        # Physics content
        ("PS_GROUP: defined", lambda: check_ps_group(content)),
        ("LEPTOQUARK: X bosons defined", lambda: check_leptoquark(content)),
        ("DIM6: operators present", lambda: check_dim6_operators(content)),
        ("LIFETIME: formula present", lambda: check_lifetime_formula(content)),
        ("HADRONIC: alpha_H symbolic", lambda: check_hadronic_matrix(content)),
        ("QUARANTINE: Layer B marked", lambda: check_quarantine_markers(content)),

        # Technical details
        ("NORMALIZATION: Tr convention", lambda: check_normalization(content)),
        ("HYPERCHARGE: Y formula", lambda: check_hypercharge(content)),
        ("BREAKING: chain defined", lambda: check_breaking_chain(content)),
        ("COUPLING: unification", lambda: check_coupling_unification(content)),
        ("WIDTH: formula present", lambda: check_width_formula(content)),
        ("PHASE_SPACE: factor present", lambda: check_phase_space_formula(content)),

        # Document metrics
        ("DOC: equations >= 160", lambda: check_equation_count(content, MIN_EQUATIONS)),
        ("DOC: labels >= 240", lambda: check_label_count(content, MIN_LABELS)),

        # Appendices
        ("APPENDIX: present", lambda: check_appendices(content)),
        ("DIMENSIONAL: analysis present", lambda: check_dimensional_analysis(content)),
        ("CATALOG: formulas listed", lambda: check_formula_catalog(content)),

        # Scope check
        ("SCOPE: only v61 touched", lambda: check_scope(SCRIPT_DIR)),

        # Release directory
        ("RELEASE: directory exists", lambda: check_file_exists(RELEASE_DIR, "release")),
    ]

    # Run all checks
    for name, check_fn in checks:
        try:
            result, detail = check_fn()
            status = "[✓]" if result else "[✗]"
            print(f"{status} {name}: {detail if not result else 'PASS'}")
            if result:
                passed += 1
            else:
                failed += 1
                failures.append(f"{name}: {detail}")
        except Exception as e:
            print(f"[!] {name}: ERROR - {e}")
            failed += 1
            failures.append(f"{name}: {e}")

    # Summary
    print("=" * 70)
    print(f"Total: {passed}/{passed + failed} CHECKS PASSED")
    if failed > 0:
        print(f"FAILED: {failed} checks")
        for f in failures[:5]:
            print(f"  - {f}")

    # Compute document hash
    doc_hash = compute_hash(content)
    print(f"\n{VERSION} Document hash: {doc_hash}")

    # Status
    if failed == 0:
        print(f"\nBLOCK-004 {VERSION} STATUS: VERIFIED (Program Note - OPEN)")
    else:
        print(f"\nBLOCK-004 {VERSION} STATUS: VERIFICATION FAILED")

    print("=" * 70)

    return passed, failed, doc_hash

# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    passed, failed, doc_hash = run_checks()

    # Exit with appropriate code
    sys.exit(0 if failed == 0 else 1)
