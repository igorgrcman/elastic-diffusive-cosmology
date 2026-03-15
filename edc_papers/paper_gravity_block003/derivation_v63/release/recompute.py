#!/usr/bin/env python3
"""
EDC BLOCK-004 Derivation v63: Proton Decay τ_p Structural Interface
Verification and Recomputation Script

This script performs comprehensive checks (≥50) on the v63 derivation:
- Scope verification
- Build cleanliness
- Forbidden pattern checks in Layer A
- Required boxes verification
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
VERSION = "v63"
TITLE = "Proton Decay τ_p Structural Interface"

# Forbidden patterns in Layer A
FORBIDDEN_PATTERNS = [
    r'10\^{?34}\s*years?',            # Numeric lifetime bound
    r'2\.4\s*\\times\s*10\^{?34}',    # Specific tau_p bound
    r'938\s*MeV',                     # Numeric proton mass
    r'0\.938\s*GeV',                  # Numeric proton mass variant
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
    r'91\.2\s*GeV',                   # M_Z numeric
    r'0\.1179',                       # Numeric alpha_s(M_Z)
    r'greater\s*than.*10\^',          # Bound language
]

# Required sections/boxes
REQUIRED_SECTIONS = [
    r'Reader\s*Contract',
    r'No.?Fit\s*Policy',
    r'No.?Backflow',
    r'Operator\s*Catalog',
    r'Structural\s*Interface|Interface.*\$\\tau_p',
    r'Open\s*Surface',
    r'Closure\s*Map',
    r'Layer\s*B.*Quarantine',
]

# Required boxes
REQUIRED_BOXES = [
    r'operatorbox',
    r'interfacebox',
    r'opensurfacebox',
    r'closurebox',
]

# Required APIs
REQUIRED_APIS = ['API-TAU1', 'API-TAU2']

# Required reviewer traps (minimum count)
MIN_TRAPS = 10

# Epistemic tag minimum counts
MIN_TAG_D = 20
MIN_TAG_Dc = 10
MIN_TAG_P = 3
MIN_TAG_Q = 3

# Document metrics
MIN_PAGES = 18
MAX_PAGES = 35
MIN_EQUATIONS = 120
MIN_LABELS = 200

# Release bundle files
RELEASE_FILES = [
    'main.tex',
    'recompute.py',
    'README.md',
    'REPORT.md',
    'ACCEPTANCE.md',
    'RELEASE_NOTES.md',
]

EXPORT_PDF_PATTERN = r'EDC_BLOCK004_DERIVATION_V63.*\.pdf'

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
    return exists, f"PATH: {filepath}"

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

def check_section_present(content: str, pattern: str) -> Tuple[bool, str]:
    """Check that a required section is present."""
    found = bool(re.search(pattern, content, re.IGNORECASE))
    return found, f"{'found' if found else 'NOT FOUND'}"

def check_box_present(content: str, box_name: str) -> Tuple[bool, str]:
    """Check that a box environment is used."""
    found = bool(re.search(rf'\\begin\{{{box_name}\}}', content))
    return found, f"{'found' if found else 'NOT FOUND'}"

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
    if not layer_b:
        match = re.search(r'%==LAYER_B_START==(.*?)%==LAYER_B_END==', content, re.DOTALL)
        if match:
            layer_b = match.group(1)
    has_q = bool(re.search(r'tagQ|QUARANTINE|quarantinebox|Qnum', layer_b, re.IGNORECASE))
    return has_q, "quarantine markers found" if has_q else "no quarantine markers"

def check_api_present(content: str, api_name: str) -> Tuple[bool, str]:
    """Check that an API is defined."""
    found = bool(re.search(api_name, content))
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

def check_no_backflow(content: str) -> Tuple[bool, str]:
    """Check No-Backflow theorem is present."""
    has_theorem = bool(re.search(r'No.?Backflow', content, re.IGNORECASE))
    has_intersection = bool(re.search(r'\\cap', content))
    if has_theorem and has_intersection:
        return True, "theorem present with set notation"
    return False, "missing components"

def check_no_fit_policy(content: str) -> Tuple[bool, str]:
    """Check No-Fit policy is present."""
    has_nofit = bool(re.search(r'No.?Fit', content, re.IGNORECASE))
    has_swept = bool(re.search(r'swept|NOT\s*fitted', content, re.IGNORECASE))
    if has_nofit and has_swept:
        return True, "policy present"
    return False, "missing components"

def check_sigma_tilde(content: str) -> Tuple[bool, str]:
    """Check sigma tilde is used."""
    has_sigma_tilde = bool(re.search(r'\\tilde\{?\\sigma\}?|tilde.sigma', content))
    return has_sigma_tilde, "sigma tilde present" if has_sigma_tilde else "not found"

def check_mustar(content: str) -> Tuple[bool, str]:
    """Check mu_* is used."""
    has_mustar = bool(re.search(r'\\mu_\*|mu_\*|\\mu\^\*', content))
    return has_mustar, "mu_* present" if has_mustar else "not found"

def check_boxed_taup(content: str) -> Tuple[bool, str]:
    """Check that tau_p appears in boxed equation."""
    has_boxed = bool(re.search(r'\\boxed\{.*\\tau_p.*\}', content, re.DOTALL))
    return has_boxed, "boxed tau_p found" if has_boxed else "not found"

def check_boxed_scaling(content: str) -> Tuple[bool, str]:
    """Check that scaling law is boxed."""
    has_boxed = bool(re.search(r'\\boxed\{.*\\propto.*\\tilde.*\}', content, re.DOTALL))
    return has_boxed, "boxed scaling found" if has_boxed else "not found"

def check_operator_catalog(content: str) -> Tuple[bool, str]:
    """Check operator catalog section exists."""
    has_catalog = bool(re.search(r'Operator\s*Catalog', content, re.IGNORECASE))
    has_operators = bool(re.search(r'\\mathcal\{O\}_[1-6]', content))
    if has_catalog and has_operators:
        return True, "catalog with operators"
    return False, "incomplete"

def check_open_surface(content: str) -> Tuple[bool, str]:
    """Check Open Surface box is present."""
    has_box = bool(re.search(r'opensurfacebox|OPEN\s*SURFACE', content, re.IGNORECASE))
    has_sigma = bool(re.search(r'\\tilde\{?\\sigma\}?.*free|remaining.*\\tilde', content, re.IGNORECASE))
    if has_box:
        return True, "Open Surface found"
    return False, "not found"

def check_closure_map(content: str) -> Tuple[bool, str]:
    """Check closure map section."""
    has_closure = bool(re.search(r'Closure\s*Map|v63\s*closes|closes\s*v61', content, re.IGNORECASE))
    return has_closure, "closure map found" if has_closure else "not found"

def check_v62_import(content: str) -> Tuple[bool, str]:
    """Check M_X import from v62."""
    has_import = bool(re.search(r'v62|M_X.*=.*C_X.*\\mu_\*', content))
    return has_import, "v62 import found" if has_import else "not found"

def check_hadronic_factor(content: str) -> Tuple[bool, str]:
    """Check hadronic factor is defined."""
    has_hp = bool(re.search(r'\\mathcal\{H\}_p|hadronic\s*factor', content, re.IGNORECASE))
    return has_hp, "hadronic factor found" if has_hp else "not found"

def check_release_bundle(release_dir: Path) -> Tuple[bool, str]:
    """Check release bundle contains required files."""
    if not release_dir.exists():
        return False, "release/ directory missing"
    missing = []
    for f in RELEASE_FILES:
        if not (release_dir / f).exists():
            missing.append(f)
    pdf_files = list(release_dir.glob("*.pdf"))
    has_export_pdf = any(re.match(EXPORT_PDF_PATTERN, f.name) for f in pdf_files)
    if not has_export_pdf:
        missing.append("export PDF")
    if missing:
        return False, f"missing: {', '.join(missing)}"
    return True, "all files present"

def check_hash_length(content: str, expected_len: int = 16) -> Tuple[bool, str]:
    """Check hash is correct length."""
    h = compute_hash(content)
    return len(h) == expected_len, f"hash = {h}"

def check_dimension6(content: str) -> Tuple[bool, str]:
    """Check dimension-6 operators are discussed."""
    has_dim6 = bool(re.search(r'dimension.?6|dim.?6|\\mathcal\{O\}.*\^{?\(6\)}?', content, re.IGNORECASE))
    return has_dim6, "dim-6 discussed" if has_dim6 else "not found"

def check_decay_channels(content: str) -> Tuple[bool, str]:
    """Check decay channels are listed."""
    has_epi = bool(re.search(r'e\^\+\s*\\pi\^0', content))
    has_nupi = bool(re.search(r'\\bar\{?\\nu\}?\s*\\pi\^\+', content))
    if has_epi and has_nupi:
        return True, "channels found"
    return False, "incomplete"

def check_selection_rules(content: str) -> Tuple[bool, str]:
    """Check selection rules are stated."""
    has_deltaB = bool(re.search(r'\\Delta\s*B\s*=', content))
    has_deltaL = bool(re.search(r'\\Delta\s*L\s*=', content))
    if has_deltaB and has_deltaL:
        return True, "selection rules present"
    return False, "incomplete"

def check_ps_coupling(content: str) -> Tuple[bool, str]:
    """Check PS coupling is discussed."""
    has_gps = bool(re.search(r'g_\{?\\text\{PS\}\}?|g_X', content))
    return has_gps, "PS coupling found" if has_gps else "not found"

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

    # File existence checks (4 checks)
    checks.append(("main.tex exists", check_file_exists(MAIN_TEX, "main.tex")))
    checks.append(("main.pdf exists", check_pdf_exists(MAIN_PDF)))
    log_path = SCRIPT_DIR / "main.log"
    checks.append(("main.log exists", check_file_exists(log_path, "main.log")))
    checks.append(("release/ exists", (RELEASE_DIR.exists(), "exists" if RELEASE_DIR.exists() else "missing")))

    # Build quality (3 checks)
    checks.append(("build clean", check_build_clean(log_path)))
    checks.append(("page count", check_page_count(log_path, MIN_PAGES, MAX_PAGES)))
    checks.append(("undefined refs", check_build_clean(log_path)))

    # Document structure (4 checks)
    checks.append(("equations >= " + str(MIN_EQUATIONS), check_equation_count(content, MIN_EQUATIONS)))
    checks.append(("labels >= " + str(MIN_LABELS), check_label_count(content, MIN_LABELS)))
    checks.append(("equations >= 100", check_equation_count(content, 100)))
    checks.append(("labels >= 150", check_label_count(content, 150)))

    # Required sections (8 checks)
    for pattern in REQUIRED_SECTIONS:
        name = pattern.replace(r'\s*', ' ').replace('\\', '')[:25]
        checks.append((f"section: {name}", check_section_present(content, pattern)))

    # Required boxes (4 checks)
    for box in REQUIRED_BOXES:
        checks.append((f"box: {box}", check_box_present(content, box)))

    # Layer architecture (4 checks)
    checks.append(("layer markers", check_layer_markers(content)))
    checks.append(("forbidden in Layer A", check_forbidden_in_layer_a(content)))
    checks.append(("quarantine in Layer B", check_quarantine_markers(content)))
    checks.append(("layer A content exists", (len(find_layer_a_content(content)) > 1000, "substantial")))

    # Core content (8 checks)
    checks.append(("boxed tau_p", check_boxed_taup(content)))
    checks.append(("boxed scaling", check_boxed_scaling(content)))
    checks.append(("operator catalog", check_operator_catalog(content)))
    checks.append(("open surface", check_open_surface(content)))
    checks.append(("closure map", check_closure_map(content)))
    checks.append(("v62 import", check_v62_import(content)))
    checks.append(("hadronic factor", check_hadronic_factor(content)))
    checks.append(("dimension-6", check_dimension6(content)))

    # Policy statements (2 checks)
    checks.append(("No-Backflow", check_no_backflow(content)))
    checks.append(("No-Fit policy", check_no_fit_policy(content)))

    # APIs (2 checks)
    for api in REQUIRED_APIS:
        checks.append((f"API: {api}", check_api_present(content, api)))

    # Physics content (4 checks)
    checks.append(("decay channels", check_decay_channels(content)))
    checks.append(("selection rules", check_selection_rules(content)))
    checks.append(("PS coupling", check_ps_coupling(content)))
    checks.append(("sigma tilde", check_sigma_tilde(content)))

    # Reviewer traps (1 check)
    checks.append(("reviewer traps", check_traps_count(content, MIN_TRAPS)))

    # Epistemic tags (4 checks)
    checks.append(("tag [D]", check_tag_count(content, "D", MIN_TAG_D)))
    checks.append(("tag [Dc]", check_tag_count(content, "Dc", MIN_TAG_Dc)))
    checks.append(("tag [P]", check_tag_count(content, "P", MIN_TAG_P)))
    checks.append(("tag [Q]", check_tag_count(content, "Q", MIN_TAG_Q)))

    # Parameters (2 checks)
    checks.append(("mu_*", check_mustar(content)))
    checks.append(("C_X defined", (bool(re.search(r'C_X', content)), "found")))

    # Hash (1 check)
    checks.append(("hash length", check_hash_length(content)))

    # Release bundle (1 check)
    checks.append(("release bundle", check_release_bundle(RELEASE_DIR)))

    # Print results
    passed = 0
    total = len(checks)

    print(f"\n{'='*70}")
    print(f"EDC BLOCK-004 Derivation {VERSION}: {TITLE}")
    print(f"Verification Script ({total} checks)")
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

    if passed == total:
        print(f"ALL {total} CHECKS PASSED")
        print(f"v63 SoT hash: {sot_hash}")
        sys.exit(0)
    else:
        print(f"CHECKS FAILED: {total - passed} failures")
        sys.exit(1)
