#!/usr/bin/env python3
"""
recompute.py for derivation v38: Hosotani Closure Roadmap

Verifies:
1. Forbidden token gate
2. Equation count ≥ 90
3. Page count ≥ 18
4. Roadmap stages (6 stages)
5. Wilson line parametrization
6. Effective potential structure
7. EW scale formula
8. Higgs mass formula
9. EDC connection
10. Closure conditions
11. No private paths
12. Epistemic ledger
13. Matter content discussion
14. GUT embedding
15. Warped extension

ALL CHECKS MUST PASS
"""

import re
import subprocess
import sys
from pathlib import Path

# Configuration
REQUIRED_EQUATIONS = 90
REQUIRED_PAGES = 18
REQUIRED_STAGES = 6

FORBIDDEN_TOKENS = [
    r"91\.19",          # M_Z
    r"80\.38",          # M_W
    r"246\.2",          # v_EW (as input)
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

def check_roadmap_stages(content):
    """Verify six roadmap stages are present."""
    stages = [
        r"Stage\s*1",
        r"Stage\s*2",
        r"Stage\s*3",
        r"Stage\s*4",
        r"Stage\s*5",
        r"Stage\s*6",
    ]
    count = sum(1 for s in stages if re.search(s, content, re.IGNORECASE))
    return count >= REQUIRED_STAGES, f"{count}/6 stages"

def check_wilson_line(content):
    """Check Wilson line parametrization."""
    patterns = [
        r"Wilson.*line",
        r"e\^{.*theta",
        r"\\mathcal\{P\}.*\\exp",
    ]
    found = sum(1 for p in patterns if re.search(p, content, re.IGNORECASE))
    return found >= 2, f"{found}/3 Wilson line elements"

def check_effective_potential(content):
    """Check effective potential structure."""
    patterns = [
        r"V_.*eff",
        r"one.*loop",
        r"\\cos.*\\theta",
        r"regulariz",
    ]
    found = sum(1 for p in patterns if re.search(p, content, re.IGNORECASE))
    return found >= 3, f"{found}/4 V_eff elements"

def check_ew_scale(content):
    """Check EW scale formula."""
    patterns = [
        r"v.*=.*theta.*g.*L",
        r"v_.*EW",
        r"electroweak.*scale",
    ]
    found = sum(1 for p in patterns if re.search(p, content, re.IGNORECASE))
    return found >= 2, f"{found}/3 EW scale elements"

def check_higgs_mass(content):
    """Check Higgs mass formula."""
    patterns = [
        r"m_H",
        r"Higgs.*mass",
        r"V''.*theta",
        r"curvature",
    ]
    found = sum(1 for p in patterns if re.search(p, content, re.IGNORECASE))
    return found >= 3, f"{found}/4 Higgs mass elements"

def check_edc_connection(content):
    """Check EDC parameter connection."""
    patterns = [
        r"\\beta",
        r"\\lambda",
        r"EDC",
        r"v27|v28|v29|v30",
    ]
    found = sum(1 for p in patterns if re.search(p, content))
    return found >= 3, f"{found}/4 EDC connection elements"

def check_closure_conditions(content):
    """Check closure conditions discussion."""
    patterns = [
        r"closure",
        r"\\theta\^\*",
        r"g_4",
        r"OPEN",
    ]
    found = sum(1 for p in patterns if re.search(p, content, re.IGNORECASE))
    return found >= 3, f"{found}/4 closure elements"

def check_epistemic_ledger(content):
    """Check epistemic ledger appendix."""
    has_ledger = "Epistemic Ledger" in content or "ledger" in content
    has_tags = all(tag in content for tag in ["[D]", "[P]", "[BL]", "[OPEN]"])
    return has_ledger and has_tags, "Epistemic ledger"

def check_matter_content(content):
    """Check matter content discussion."""
    patterns = [
        r"fermion",
        r"matter.*content",
        r"representation",
        r"anomaly",
    ]
    found = sum(1 for p in patterns if re.search(p, content, re.IGNORECASE))
    return found >= 3, f"{found}/4 matter content elements"

def check_gut_embedding(content):
    """Check GUT embedding discussion."""
    patterns = [
        r"GUT",
        r"SU\(5\)",
        r"SO\(5\)",
        r"unification",
    ]
    found = sum(1 for p in patterns if re.search(p, content, re.IGNORECASE))
    return found >= 2, f"{found}/4 GUT elements"

def check_warped_extension(content):
    """Check warped geometry extension."""
    patterns = [
        r"warp",
        r"Randall.*Sundrum|RS",
        r"e\^{.*k.*y",
        r"hierarchy",
    ]
    found = sum(1 for p in patterns if re.search(p, content, re.IGNORECASE))
    return found >= 2, f"{found}/4 warped elements"

def get_page_count():
    """Get PDF page count."""
    try:
        result = subprocess.run(
            ["pdfinfo", "main.pdf"],
            capture_output=True, text=True
        )
        for line in result.stdout.split("\n"):
            if "Pages:" in line:
                return int(line.split(":")[1].strip())
    except:
        pass

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
    print("v38 Verification: Hosotani Closure Roadmap")
    print("=" * 60)
    print()

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

    # Check 5: Roadmap stages
    passed, msg = check_roadmap_stages(content)
    checks.append(("Roadmap stages", passed, msg))

    # Check 6: Wilson line
    passed, msg = check_wilson_line(content)
    checks.append(("Wilson line", passed, msg))

    # Check 7: Effective potential
    passed, msg = check_effective_potential(content)
    checks.append(("Effective potential", passed, msg))

    # Check 8: EW scale
    passed, msg = check_ew_scale(content)
    checks.append(("EW scale formula", passed, msg))

    # Check 9: Higgs mass
    passed, msg = check_higgs_mass(content)
    checks.append(("Higgs mass formula", passed, msg))

    # Check 10: EDC connection
    passed, msg = check_edc_connection(content)
    checks.append(("EDC connection", passed, msg))

    # Check 11: Closure conditions
    passed, msg = check_closure_conditions(content)
    checks.append(("Closure conditions", passed, msg))

    # Check 12: No private paths
    passed, msg = check_private_paths(content, "main.tex")
    checks.append(("No private paths", passed, msg))

    # Check 13: Epistemic ledger
    passed, msg = check_epistemic_ledger(content)
    checks.append(("Epistemic ledger", passed, msg))

    # Check 14: Matter content
    passed, msg = check_matter_content(content)
    checks.append(("Matter content", passed, msg))

    # Check 15: GUT embedding
    passed, msg = check_gut_embedding(content)
    checks.append(("GUT embedding", passed, msg))

    # Check 16: Warped extension
    passed, msg = check_warped_extension(content)
    checks.append(("Warped extension", passed, msg))

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
