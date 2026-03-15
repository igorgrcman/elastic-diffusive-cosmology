#!/usr/bin/env python3
"""
recompute.py for derivation v37: BC Selection Principle Sketch

Verifies:
1. Forbidden token gate
2. Equation count ≥ 90
3. Page count ≥ 18
4. Four selectors present
5. Pipeline diagram present
6. Prediction hooks table
7. SA verification equations
8. Robin spectrum formula
9. Vacuum energy formula
10. Dimensional analysis
11. No private paths
12. Epistemic ledger
13. Gauge BC compatibility
14. Fermion BC consistency

ALL CHECKS MUST PASS
"""

import re
import subprocess
import sys
from pathlib import Path

# Configuration
REQUIRED_EQUATIONS = 90
REQUIRED_PAGES = 18
REQUIRED_SELECTORS = 4
REQUIRED_HOOKS = 4

FORBIDDEN_TOKENS = [
    r"91\.19",          # M_Z
    r"80\.38",          # M_W
    r"246\.2",          # v_EW
    r"1\.616.*10",      # ell_P
    r"6\.674.*10",      # G_N
    r"1/" + "137",      # alpha_EM (split to avoid self-match)
]

PRIVATE_PATH_PATTERNS = [
    r"/Users/",
    r"/home/",
    r"C:\\",
    r"file://",
]

def check_forbidden_tokens(content, filename):
    """Check for forbidden numerical inputs."""
    for pattern in FORBIDDEN_TOKENS:
        if re.search(pattern, content):
            return False, f"Forbidden token '{pattern}' found in {filename}"
    return True, "No forbidden tokens"

def check_private_paths(content, filename):
    """Check for private filesystem paths."""
    for pattern in PRIVATE_PATH_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            return False, f"Private path pattern '{pattern}' found in {filename}"
    return True, "No private paths"

def count_equations(content):
    """Count equation environments."""
    eq_pattern = r"\\begin\{equation\}|\\begin\{align\}"
    matches = re.findall(eq_pattern, content)
    return len(matches)

def check_selectors(content):
    """Verify four selectors are present."""
    selectors = [
        r"Selector\s*1.*Variation",
        r"Selector\s*2.*Self-Adjoint",
        r"Selector\s*3.*Topolog",
        r"Selector\s*4.*Vacuum",
    ]
    count = sum(1 for s in selectors if re.search(s, content, re.IGNORECASE))
    return count >= REQUIRED_SELECTORS, f"{count}/4 selectors"

def check_pipeline(content):
    """Check for pipeline diagram."""
    has_tikz = r"\begin{tikzpicture}" in content
    has_pipeline = "Pipeline" in content and "Stage" in content
    return has_tikz and has_pipeline, "Pipeline diagram" if has_tikz else "Missing pipeline"

def check_hooks_table(content):
    """Check for prediction hooks table."""
    hooks = ["Gap", "Survivors", "G_F", "Higgs"]
    found = sum(1 for h in hooks if h in content)
    has_table = r"\begin{table}" in content and "hook" in content.lower()
    return found >= REQUIRED_HOOKS and has_table, f"{found}/4 hooks"

def check_sa_verification(content):
    """Check self-adjointness verification equations."""
    patterns = [
        r"verify-NN",
        r"verify-DD",
        r"verify-RR",
        r"Green.*identity",
    ]
    found = sum(1 for p in patterns if re.search(p, content, re.IGNORECASE))
    return found >= 3, f"{found}/4 SA verifications"

def check_robin_spectrum(content):
    """Check Robin spectrum formula."""
    has_formula = r"\\tan\(m.*L\)" in content or r"tan(m" in content
    has_transcendental = "transcendental" in content.lower()
    return has_formula or has_transcendental, "Robin spectrum formula"

def check_vacuum_energy(content):
    """Check vacuum energy formula."""
    patterns = [
        r"\\mathcal\{E\}_.*vac",
        r"E_.*Casimir",
        r"zeta.*regulariz",
    ]
    found = sum(1 for p in patterns if re.search(p, content, re.IGNORECASE))
    return found >= 2, f"{found}/3 vacuum energy elements"

def check_dimensional_analysis(content):
    """Check dimensional analysis section."""
    patterns = [
        r"\[m_b\]",
        r"\[\\lambda\]",
        r"dimensionless",
    ]
    found = sum(1 for p in patterns if re.search(p, content))
    return found >= 2, f"{found}/3 dimensional elements"

def check_epistemic_ledger(content):
    """Check epistemic ledger appendix."""
    has_ledger = "Epistemic Ledger" in content or "ledger" in content
    has_tags = all(tag in content for tag in ["[D]", "[P]", "[BL]", "[OPEN]"])
    return has_ledger and has_tags, "Epistemic ledger"

def check_gauge_bc(content):
    """Check gauge BC compatibility discussion."""
    patterns = [
        r"A_\\mu.*Neumann",
        r"A_5.*Dirichlet",
        r"zero-mode",
        r"gauge.*BC",
    ]
    found = sum(1 for p in patterns if re.search(p, content, re.IGNORECASE))
    return found >= 2, f"{found}/4 gauge BC elements"

def check_fermion_bc(content):
    """Check fermion BC discussion."""
    patterns = [
        r"\\psi_L",
        r"\\psi_R",
        r"chiral",
        r"Dirac",
    ]
    found = sum(1 for p in patterns if re.search(p, content, re.IGNORECASE))
    return found >= 3, f"{found}/4 fermion BC elements"

def get_page_count():
    """Get PDF page count."""
    try:
        # Try pdfinfo
        result = subprocess.run(
            ["pdfinfo", "main.pdf"],
            capture_output=True, text=True
        )
        for line in result.stdout.split("\n"):
            if "Pages:" in line:
                return int(line.split(":")[1].strip())
    except:
        pass

    # Fallback: check log file
    try:
        with open("main.log", "r") as f:
            log = f.read()
            match = re.search(r"Output written on main\.pdf \((\d+) pages", log)
            if match:
                return int(match.group(1))
    except:
        pass

    return 0

def main():
    """Run all verification checks."""
    print("=" * 60)
    print("v37 Verification: BC Selection Principle Sketch")
    print("=" * 60)
    print()

    # Read main.tex
    tex_path = Path("main.tex")
    if not tex_path.exists():
        print("ERROR: main.tex not found")
        sys.exit(1)

    content = tex_path.read_text()

    checks = []

    # Check 1: Forbidden tokens in main.tex
    passed, msg = check_forbidden_tokens(content, "main.tex")
    checks.append(("Forbidden tokens (main.tex)", passed, msg))

    # Check 2: Forbidden tokens in this script
    script_content = Path(__file__).read_text()
    passed, msg = check_forbidden_tokens(script_content, "recompute.py")
    checks.append(("Forbidden tokens (recompute.py)", passed, msg))

    # Check 3: Equation count
    eq_count = count_equations(content)
    passed = eq_count >= REQUIRED_EQUATIONS
    checks.append(("Equation count", passed, f"{eq_count} (req ≥{REQUIRED_EQUATIONS})"))

    # Check 4: Page count
    page_count = get_page_count()
    passed = page_count >= REQUIRED_PAGES
    checks.append(("Page count", passed, f"{page_count} (req ≥{REQUIRED_PAGES})"))

    # Check 5: Four selectors
    passed, msg = check_selectors(content)
    checks.append(("Four selectors", passed, msg))

    # Check 6: Pipeline diagram
    passed, msg = check_pipeline(content)
    checks.append(("Pipeline diagram", passed, msg))

    # Check 7: Prediction hooks
    passed, msg = check_hooks_table(content)
    checks.append(("Prediction hooks", passed, msg))

    # Check 8: SA verification
    passed, msg = check_sa_verification(content)
    checks.append(("SA verification", passed, msg))

    # Check 9: Robin spectrum
    passed, msg = check_robin_spectrum(content)
    checks.append(("Robin spectrum formula", passed, msg))

    # Check 10: Vacuum energy
    passed, msg = check_vacuum_energy(content)
    checks.append(("Vacuum energy", passed, msg))

    # Check 11: Dimensional analysis
    passed, msg = check_dimensional_analysis(content)
    checks.append(("Dimensional analysis", passed, msg))

    # Check 12: No private paths
    passed, msg = check_private_paths(content, "main.tex")
    checks.append(("No private paths", passed, msg))

    # Check 13: Epistemic ledger
    passed, msg = check_epistemic_ledger(content)
    checks.append(("Epistemic ledger", passed, msg))

    # Check 14: Gauge BC
    passed, msg = check_gauge_bc(content)
    checks.append(("Gauge BC compatibility", passed, msg))

    # Check 15: Fermion BC
    passed, msg = check_fermion_bc(content)
    checks.append(("Fermion BC consistency", passed, msg))

    # Print results
    all_passed = True
    for i, (name, passed, msg) in enumerate(checks, 1):
        status = "PASS" if passed else "FAIL"
        print(f"{i:2}. {name:30} {status:6} {msg}")
        if not passed:
            all_passed = False

    print()
    print("=" * 60)
    total = len(checks)
    passed_count = sum(1 for _, p, _ in checks if p)
    print(f"TOTAL: {passed_count}/{total} CHECKS PASSED")

    if all_passed:
        print("STATUS: ALL CHECKS PASSED ✓")
        return 0
    else:
        print("STATUS: SOME CHECKS FAILED ✗")
        return 1

if __name__ == "__main__":
    sys.exit(main())
