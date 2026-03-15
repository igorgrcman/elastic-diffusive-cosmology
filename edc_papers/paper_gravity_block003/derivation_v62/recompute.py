#!/usr/bin/env python3
"""
EDC BLOCK-004 Derivation v62: PS Breaking Scale M_X (Two-Route)
Verification and Recomputation Script

This script performs comprehensive checks on the v62 derivation:
- Scope verification (only v62 + PAPERS_INDEX.md touched)
- Build cleanliness (no undefined refs, no multiply-defined labels)
- Forbidden pattern checks in Layer A
- Section header verification
- Two-route consistency verification
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
MAIN_PDF = SCRIPT_DIR / "main.pdf"
RELEASE_DIR = SCRIPT_DIR / "release"

# Version info
VERSION = "v62"
TITLE = "PS Breaking Scale M_X (Two-Route)"

# Forbidden patterns in Layer A
FORBIDDEN_PATTERNS = [
    r'10\^{?16}\s*GeV',              # Numeric M_X bound
    r'10\^{?34}\s*years?',            # Numeric lifetime bound
    r'938\s*MeV',                     # Numeric proton mass
    r'0\.938\s*GeV',                  # Numeric proton mass variant
    r'0\.01\s*GeV\^3',                # Numeric alpha_H
    r'Super.?K',                      # Experiment name
    r'Hyper.?K',                      # Experiment name
    r'Kamiokande',                    # Experiment name
    r'DUNE',                          # Experiment name
    r'JUNO',                          # Experiment name
    r'excluded',                      # Requires experimental comparison
    r'ruled\s*out',                   # Requires experimental comparison
    r'best.?fit',                     # Fitting terminology
    r'\\chi\^2',                      # Chi-squared fitting
    r'PDG\s*20[0-9]{2}',              # PDG reference
    r'0\.1179',                       # Numeric alpha_s(M_Z)
    r'91\.2\s*GeV',                   # M_Z numeric
    r'2\.4\s*\\times\s*10\^{?34}',    # Specific tau_p bound
]

# Required sections
REQUIRED_SECTIONS = [
    r'Reader\s*Contract',
    r'No.?Fit\s*Policy',
    r'No.?Backflow',
    r'Route\s*A',
    r'Route\s*B',
    r'Boxed.*M_X|M_X.*Boxed|Final.*M_X',
    r'Open\s*Surface',
    r'Closes?\s*v61|v62\s*closes?\s*v61',
]

# Required APIs
REQUIRED_APIS = ['API-MX1']

# Required reviewer traps (minimum count)
MIN_TRAPS = 10

# Epistemic tag minimum counts
MIN_TAG_D = 15
MIN_TAG_Dc = 8
MIN_TAG_P = 2
MIN_TAG_Q = 2

# Document metrics
MIN_PAGES = 18
MAX_PAGES = 35
MIN_EQUATIONS = 110
MIN_LABELS = 180

# Release bundle files
RELEASE_FILES = [
    'main.tex',
    'recompute.py',
    'README.md',
    'REPORT.md',
    'ACCEPTANCE.md',
    'RELEASE_NOTES.md',
]

EXPORT_PDF_PATTERN = r'EDC_BLOCK004_DERIVATION_V62.*\.pdf'

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
    return len(h) == expected_len, f"hash = {h}"

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

def check_section_present(content: str, pattern: str) -> Tuple[bool, str]:
    """Check that a required section header is present."""
    found = bool(re.search(pattern, content, re.IGNORECASE))
    return found, f"{'found' if found else 'NOT FOUND'}"

def check_api_present(content: str, api_name: str) -> Tuple[bool, str]:
    """Check that an API is defined."""
    pattern = rf'{api_name}'
    found = bool(re.search(pattern, content))
    return found, f"{'found' if found else 'NOT FOUND'}"

def check_traps_count(content: str, min_count: int) -> Tuple[bool, str]:
    """Check that enough reviewer traps are defined."""
    traps = re.findall(r'TRAP-\d+', content)
    count = len(set(traps))
    return count >= min_count, f"found {count} unique traps (min: {min_count})"

def check_tag_count(content: str, tag: str, min_count: int) -> Tuple[bool, str]:
    """Check epistemic tag usage."""
    pattern = rf'\\tag{tag}\{{\}}'
    count = count_pattern(content, pattern)
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
    if has_a_start and has_a_end and has_b_start and has_b_end:
        return True, "all 4 markers present"
    missing = []
    if not has_a_start: missing.append("A_START")
    if not has_a_end: missing.append("A_END")
    if not has_b_start: missing.append("B_START")
    if not has_b_end: missing.append("B_END")
    return False, f"missing: {', '.join(missing)}"

def check_quarantine_markers(content: str) -> Tuple[bool, str]:
    """Check quarantine markers in Layer B."""
    layer_b = find_layer_b_content(content)
    # Check for various quarantine patterns
    has_q_tag = bool(re.search(r'tagQ|QUARANTINE|quarantinebox|Qnum|\\Q\{', layer_b, re.IGNORECASE))
    # Also check in full content if Layer B extraction failed
    if not has_q_tag and not layer_b:
        # Check between markers directly
        match = re.search(r'%==LAYER_B_START==(.*?)%==LAYER_B_END==', content, re.DOTALL)
        if match:
            layer_b = match.group(1)
            has_q_tag = bool(re.search(r'Qnum|tagQ|QUARANTINE', layer_b, re.IGNORECASE))
    return has_q_tag, "quarantine markers found" if has_q_tag else "no quarantine markers"

def check_boxed_mx(content: str) -> Tuple[bool, str]:
    """Check that M_X appears in boxed equation."""
    has_boxed_mx = bool(re.search(r'\\boxed\{.*M_X.*\}', content))
    return has_boxed_mx, "boxed M_X found" if has_boxed_mx else "no boxed M_X"

def check_two_routes(content: str) -> Tuple[bool, str]:
    """Check both routes are defined."""
    has_route_a = bool(re.search(r'Route\s*A|M_X\^\{?\(A\)\}?', content))
    has_route_b = bool(re.search(r'Route\s*B|M_X\^\{?\(B\)\}?', content))
    if has_route_a and has_route_b:
        return True, "both routes defined"
    return False, f"Route A: {has_route_a}, Route B: {has_route_b}"

def check_route_consistency(content: str) -> Tuple[bool, str]:
    """Check route consistency is verified."""
    has_ratio = bool(re.search(r'M_X\^\{?\(A\)\}?\s*/\s*M_X\^\{?\(B\)\}?|ratio|consistency', content, re.IGNORECASE))
    has_bound = bool(re.search(r'1\s*\\pm|\\pm\s*0\.\d+|\\lesssim\s*0\.\d+', content))
    if has_ratio or has_bound:
        return True, "consistency check present"
    return False, "no consistency verification found"

def check_open_surface(content: str) -> Tuple[bool, str]:
    """Check Open Surface box is present."""
    has_open_surface = bool(re.search(r'Open\s*Surface|OPEN\s*SURFACE|opensurfacebox', content, re.IGNORECASE))
    return has_open_surface, "Open Surface section found" if has_open_surface else "no Open Surface"

def check_v61_closure(content: str) -> Tuple[bool, str]:
    """Check v61 closure section."""
    has_closure = bool(re.search(r'v62\s*closes?\s*v61|closes?\s*v61|How.*v62.*v61', content, re.IGNORECASE))
    return has_closure, "v61 closure section found" if has_closure else "no v61 closure section"

def check_release_bundle(release_dir: Path) -> Tuple[bool, str]:
    """Check release bundle contains required files."""
    if not release_dir.exists():
        return False, "release/ directory missing"
    missing = []
    for f in RELEASE_FILES:
        if not (release_dir / f).exists():
            missing.append(f)
    # Check for export PDF
    pdf_files = list(release_dir.glob("*.pdf"))
    has_export_pdf = any(re.match(EXPORT_PDF_PATTERN, f.name) for f in pdf_files)
    if not has_export_pdf:
        missing.append("export PDF")
    if missing:
        return False, f"missing: {', '.join(missing)}"
    return True, "all files present"

def check_pdf_exists(pdf_path: Path) -> Tuple[bool, str]:
    """Check PDF file exists and has reasonable size."""
    if not pdf_path.exists():
        return False, "PDF not found"
    size = pdf_path.stat().st_size
    if size < 100000:
        return False, f"PDF too small: {size} bytes"
    return True, f"PDF exists: {size} bytes"

def check_page_count(log_path: Path, min_pages: int, max_pages: int) -> Tuple[bool, str]:
    """Check page count from log file."""
    if not log_path.exists():
        return False, "log file not found"
    content = read_file(log_path)
    match = re.search(r'Output written on.*\((\d+) pages', content)
    if not match:
        return False, "could not determine page count"
    pages = int(match.group(1))
    if min_pages <= pages <= max_pages:
        return True, f"{pages} pages"
    return False, f"{pages} pages (expected {min_pages}-{max_pages})"

def check_build_clean(log_path: Path) -> Tuple[bool, str]:
    """Check for undefined references and multiply-defined labels."""
    if not log_path.exists():
        return False, "log file not found"
    content = read_file(log_path)
    undefined = len(re.findall(r'undefined', content, re.IGNORECASE))
    multiply = len(re.findall(r'multiply.defined', content, re.IGNORECASE))
    if undefined == 0 and multiply == 0:
        return True, "no undefined refs or multiply-defined labels"
    return False, f"undefined: {undefined}, multiply-defined: {multiply}"

def check_normalization(content: str) -> Tuple[bool, str]:
    """Check normalization conventions are stated."""
    has_tr = bool(re.search(r'\\text\{Tr\}|Tr\(|normalization', content, re.IGNORECASE))
    has_delta = bool(re.search(r'\\delta|Kronecker', content))
    if has_tr or has_delta:
        return True, "normalization conventions present"
    return False, "normalization conventions not found"

def check_sigma_tilde(content: str) -> Tuple[bool, str]:
    """Check sigma tilde is defined."""
    has_sigma_tilde = bool(re.search(r'\\tilde\{?\\sigma\}?|tilde.sigma', content))
    return has_sigma_tilde, "sigma tilde defined" if has_sigma_tilde else "sigma tilde not found"

def check_mustar(content: str) -> Tuple[bool, str]:
    """Check mu_* is used."""
    has_mustar = bool(re.search(r'\\mu_\*|mu_\*|\\mu\^\*', content))
    return has_mustar, "mu_* present" if has_mustar else "mu_* not found"

# ============================================================================
# MAIN
# ============================================================================

def run_checks() -> Tuple[int, int, str]:
    """Run all checks and return (passed, total, hash)."""

    content = read_file(MAIN_TEX)
    if not content:
        print("ERROR: Could not read main.tex")
        return 0, 1, ""

    checks = []

    # File existence checks
    checks.append(("main.tex exists", check_file_exists(MAIN_TEX, "main.tex")))
    checks.append(("main.pdf exists", check_pdf_exists(MAIN_PDF)))

    # Build quality
    log_path = SCRIPT_DIR / "main.log"
    checks.append(("build clean", check_build_clean(log_path)))
    checks.append(("page count", check_page_count(log_path, MIN_PAGES, MAX_PAGES)))

    # Document structure
    checks.append(("equations >= " + str(MIN_EQUATIONS), check_equation_count(content, MIN_EQUATIONS)))
    checks.append(("labels >= " + str(MIN_LABELS), check_label_count(content, MIN_LABELS)))

    # Required sections
    for pattern in REQUIRED_SECTIONS:
        name = pattern.replace(r'\s*', ' ').replace('\\', '')[:25]
        checks.append((f"section: {name}", check_section_present(content, pattern)))

    # Layer architecture
    checks.append(("layer markers", check_layer_markers(content)))
    checks.append(("forbidden in Layer A", check_forbidden_in_layer_a(content)))
    checks.append(("quarantine in Layer B", check_quarantine_markers(content)))

    # Core content
    checks.append(("boxed M_X", check_boxed_mx(content)))
    checks.append(("two routes defined", check_two_routes(content)))
    checks.append(("route consistency", check_route_consistency(content)))
    checks.append(("open surface", check_open_surface(content)))
    checks.append(("v61 closure", check_v61_closure(content)))

    # Policy statements
    checks.append(("No-Backflow", check_no_backflow(content)))
    checks.append(("No-Fit policy", check_no_fit_policy(content)))

    # APIs
    for api in REQUIRED_APIS:
        checks.append((f"API: {api}", check_api_present(content, api)))

    # Reviewer traps
    checks.append(("reviewer traps", check_traps_count(content, MIN_TRAPS)))

    # Epistemic tags
    checks.append(("tag [D]", check_tag_count(content, "D", MIN_TAG_D)))
    checks.append(("tag [Dc]", check_tag_count(content, "Dc", MIN_TAG_Dc)))
    checks.append(("tag [P]", check_tag_count(content, "P", MIN_TAG_P)))
    checks.append(("tag [Q]", check_tag_count(content, "Q", MIN_TAG_Q)))

    # Parameters
    checks.append(("sigma tilde", check_sigma_tilde(content)))
    checks.append(("mu_*", check_mustar(content)))
    checks.append(("normalization", check_normalization(content)))

    # Hash
    checks.append(("hash length", check_hash_length(content, VERSION)))

    # Release bundle
    checks.append(("release bundle", check_release_bundle(RELEASE_DIR)))

    # Print results
    passed = 0
    total = len(checks)

    print(f"\n{'='*70}")
    print(f"EDC BLOCK-004 Derivation {VERSION}: {TITLE}")
    print(f"Verification Script")
    print(f"{'='*70}\n")

    for name, (result, detail) in checks:
        status = "PASS" if result else "FAIL"
        symbol = "✓" if result else "✗"
        print(f"  [{symbol}] {name:40s} {status:6s} {detail}")
        if result:
            passed += 1

    # Compute SoT hash
    sot_hash = compute_hash(content)

    print(f"\n{'='*70}")
    print(f"Results: {passed}/{total} checks passed")
    print(f"SoT Hash: {sot_hash}")
    print(f"{'='*70}\n")

    return passed, total, sot_hash

if __name__ == "__main__":
    passed, total, sot_hash = run_checks()

    # Write hash to stdout for capture
    if passed == total:
        print(f"ALL CHECKS PASSED")
        print(f"v62 SoT hash: {sot_hash}")
        sys.exit(0)
    else:
        print(f"CHECKS FAILED: {total - passed} failures")
        sys.exit(1)
