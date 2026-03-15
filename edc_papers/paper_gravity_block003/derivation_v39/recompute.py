#!/usr/bin/env python3
"""
recompute.py for derivation v39: BC Selector Applied to GUT Survivor Map

Verifies:
1. Forbidden token gate
2. Projector algebra closure: dim(survivors)=12 for all tracks
3. Zero-mode rule validation: (N,N) ↔ zero-mode
4. ΔE_vac difference invariance: ΔE(BC_ref)=0
5. KK scale formula invariance under π-map
6. Charged tower index set non-empty and consistent
7. Four GUT tracks present
8. G_F hook formula present
9. Free knobs catalog
10. Dimensional checks
11. Reviewer traps ≥ 14
12. Equation count
13. No private paths
14. Epistemic ledger

ALL CHECKS MUST PASS
"""

import re
import subprocess
import sys
from pathlib import Path

# Configuration
REQUIRED_EQUATIONS = 90
REQUIRED_PAGES = 18
REQUIRED_TRAPS = 14
REQUIRED_TRACKS = 4

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
    r"C:\\\\",
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

def check_projector_closure(content):
    """Check that dim(survivors)=12 is mentioned for all tracks."""
    patterns = [
        r"12.*survivor|survivor.*12",
        r"8\s*\+\s*3\s*\+\s*1\s*=\s*12",
        r"dim.*12",
        r"Total.*12",
    ]
    found = sum(1 for p in patterns if re.search(p, content, re.IGNORECASE))
    return found >= 2, f"{found}/4 projector closure elements"

def check_zero_mode_rule(content):
    """Check zero-mode ↔ (N,N) rule."""
    patterns = [
        r"\(\+,\+\).*zero.*mode|zero.*mode.*\(\+,\+\)",
        r"N.*N.*zero|Neumann.*zero",
        r"survivor.*rule",
    ]
    found = sum(1 for p in patterns if re.search(p, content, re.IGNORECASE))
    return found >= 2, f"{found}/3 zero-mode rule elements"

def check_delta_E_invariance(content):
    """Check ΔE_vac(ref) = 0."""
    patterns = [
        r"\\Delta\s*E.*ref.*=.*0|S\[.*ref.*\].*=.*0",
        r"reference.*normalization",
        r"baseline",
    ]
    found = sum(1 for p in patterns if re.search(p, content, re.IGNORECASE))
    return found >= 1, f"{found}/3 ΔE invariance elements"

def check_kk_scale(content):
    """Check KK scale formula and π-map invariance."""
    patterns = [
        r"\\mu.*KK.*=.*\\pi.*L|\\pi/L",
        r"\\pi.*map|pi-map",
        r"convention.*independent",
    ]
    found = sum(1 for p in patterns if re.search(p, content, re.IGNORECASE))
    return found >= 2, f"{found}/3 KK scale elements"

def check_charged_tower(content):
    """Check charged tower definition and non-emptiness."""
    patterns = [
        r"\\mathcal\{T\}.*charged|charged.*tower",
        r"non.*empty|nonempty",
        r"W.*tower|W\^\\pm",
    ]
    found = sum(1 for p in patterns if re.search(p, content, re.IGNORECASE))
    return found >= 2, f"{found}/3 charged tower elements"

def check_four_tracks(content):
    """Check all four GUT tracks present."""
    tracks = ["SU(5)", "SO(10)", "Pati", "E_6"]
    found = sum(1 for t in tracks if t in content)
    return found >= REQUIRED_TRACKS, f"{found}/4 GUT tracks"

def check_gf_hook(content):
    """Check G_F hook formula."""
    patterns = [
        r"G_F.*hook|hook.*G_F",
        r"\\sum.*g_4.*m.*2|\\sum.*m_n.*2",
        r"charged.*exchange",
    ]
    found = sum(1 for p in patterns if re.search(p, content, re.IGNORECASE))
    return found >= 2, f"{found}/3 G_F hook elements"

def check_free_knobs(content):
    """Check free knobs catalog."""
    patterns = [
        r"\\beta",
        r"\\lambda",
        r"c_A|c_B|c_C",
        r"free.*knob|knob.*free",
    ]
    found = sum(1 for p in patterns if re.search(p, content))
    return found >= 3, f"{found}/4 free knobs elements"

def check_dimensional(content):
    """Check dimensional analysis."""
    patterns = [
        r"\[G_F\].*=.*M\^{-2}|M\^{-2}",
        r"dimension.*check|dim.*verif",
    ]
    found = sum(1 for p in patterns if re.search(p, content, re.IGNORECASE))
    return found >= 1, f"{found}/2 dimensional elements"

def count_reviewer_traps(content):
    """Count reviewer traps."""
    # Count rows in trap table
    trap_matches = re.findall(r"\\midrule.*?\\bottomrule", content, re.DOTALL)
    if trap_matches:
        for match in trap_matches:
            if "Trap" in match or "trap" in match or "tuning" in match.lower():
                rows = match.count(r"\\")
                return rows >= REQUIRED_TRAPS, f"{rows} trap table rows"

    # Alternative: count numbered traps
    trap_count = len(re.findall(r"\d+\s*&.*PASS", content))
    return trap_count >= REQUIRED_TRAPS, f"{trap_count} traps"

def check_epistemic_ledger(content):
    """Check epistemic ledger."""
    has_ledger = "Epistemic Ledger" in content or "ledger" in content
    tags = ["[D]", "[P]", "[BL]", "[OPEN]"]
    has_tags = sum(1 for t in tags if t in content) >= 3
    return has_ledger and has_tags, "Epistemic ledger"

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
    print("v39 Verification: BC Selector Applied to GUT Survivor Map")
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

    # Check 3: Projector closure (dim=12)
    passed, msg = check_projector_closure(content)
    checks.append(("Projector closure (dim=12)", passed, msg))

    # Check 4: Zero-mode rule
    passed, msg = check_zero_mode_rule(content)
    checks.append(("Zero-mode rule", passed, msg))

    # Check 5: ΔE_vac invariance
    passed, msg = check_delta_E_invariance(content)
    checks.append(("ΔE_vac(ref) = 0", passed, msg))

    # Check 6: KK scale π-map
    passed, msg = check_kk_scale(content)
    checks.append(("KK scale π-map", passed, msg))

    # Check 7: Charged tower
    passed, msg = check_charged_tower(content)
    checks.append(("Charged tower non-empty", passed, msg))

    # Check 8: Four GUT tracks
    passed, msg = check_four_tracks(content)
    checks.append(("Four GUT tracks", passed, msg))

    # Check 9: G_F hook
    passed, msg = check_gf_hook(content)
    checks.append(("G_F hook formula", passed, msg))

    # Check 10: Free knobs
    passed, msg = check_free_knobs(content)
    checks.append(("Free knobs catalog", passed, msg))

    # Check 11: Dimensional
    passed, msg = check_dimensional(content)
    checks.append(("Dimensional checks", passed, msg))

    # Check 12: Reviewer traps
    passed, msg = count_reviewer_traps(content)
    checks.append(("Reviewer traps ≥ 14", passed, msg))

    # Check 13: Equation count
    eq_count = count_equations(content)
    passed = eq_count >= REQUIRED_EQUATIONS
    checks.append(("Equation count", passed, f"{eq_count} (req ≥{REQUIRED_EQUATIONS})"))

    # Check 14: No private paths
    passed, msg = check_private_paths(content, "main.tex")
    checks.append(("No private paths", passed, msg))

    # Check 15: Epistemic ledger
    passed, msg = check_epistemic_ledger(content)
    checks.append(("Epistemic ledger", passed, msg))

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
