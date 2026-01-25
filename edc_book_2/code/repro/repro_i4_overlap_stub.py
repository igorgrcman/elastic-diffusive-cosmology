#!/usr/bin/env python3
"""
================================================================================
ARTIFACT CLASSIFICATION: REPRO (Stub — OPR-21 Blocked)
================================================================================
This script is a REPRODUCIBILITY artifact that documents the I₄ overlap
integral calculation for the G_F derivation.

STATUS: BLOCKED by OPR-21 (I₄ overlap from BVP)

The script will FAIL with a clear error message until the blocking conditions
are resolved. This is intentional — it documents what is missing.

Supports claims:
- E-CH11-Dc-014: G_F = G₅ ∫|f_L|⁴ dξ
- E-CH14-Dc-*: BVP eigenvalue claims

References:
- src/sections/11_gf_derivation.tex, Eq. (eq:ch11_overlap)
- canon/opr/OPR_REGISTRY.md, OPR-21
================================================================================

Required inputs (currently MISSING — OPR-21):
    1. f_L(ξ) — Left-handed fermion mode profile from BVP solution
    2. V(ξ) — 5D potential from membrane action (OPR-20 dependency)
    3. α — Robin BC parameter from action variation (OPR-02 dependency)

When OPR-21 is closed, this script will:
    1. Load f_L(ξ) from BVP solver output
    2. Compute I₄ = ∫₀^∞ |f_L(ξ)|⁴ dξ
    3. Output I₄ value with uncertainty estimate
    4. Generate comparison plot
    5. Record hash of output
"""

import sys
from pathlib import Path

# Configuration
SCRIPT_NAME = "repro_i4_overlap_stub.py"
OUTPUT_DIR = Path(__file__).parent.parent / "output"
OPR_BLOCKED = "OPR-21"

# Required input files (will exist after OPR-21 closure)
REQUIRED_INPUTS = {
    "f_L_profile": "output/bvp_fL_profile.npy",
    "bvp_params": "output/bvp_params.json",
}


def check_inputs():
    """Check if required inputs exist."""
    missing = []
    for name, path in REQUIRED_INPUTS.items():
        full_path = Path(__file__).parent.parent / path
        if not full_path.exists():
            missing.append(name)
    return missing


def fail_with_opr_reference(missing_inputs):
    """Exit with clear error message referencing OPR."""
    print("=" * 70)
    print(f"REPRO SCRIPT BLOCKED: {SCRIPT_NAME}")
    print("=" * 70)
    print()
    print(f"This script is blocked by {OPR_BLOCKED}: I₄ overlap from BVP")
    print()
    print("MISSING INPUTS:")
    for inp in missing_inputs:
        print(f"  - {inp}: {REQUIRED_INPUTS[inp]}")
    print()
    print("RESOLUTION REQUIRED:")
    print("  1. Close OPR-02: Derive Robin α from action variation")
    print("  2. Close OPR-20: Derive V(ξ) and ℓ from membrane physics")
    print("  3. Solve BVP for f_L(ξ) with physical inputs")
    print("  4. Save f_L profile to output/bvp_fL_profile.npy")
    print("  5. Re-run this script")
    print()
    print("See: canon/opr/OPR_REGISTRY.md for full OPR details")
    print("=" * 70)
    sys.exit(1)


def compute_i4(f_L, xi):
    """
    Compute the overlap integral I₄ = ∫|f_L(ξ)|⁴ dξ

    This function will be called after OPR-21 is closed.

    Parameters:
        f_L: array — Left-handed fermion mode profile
        xi: array — 5D coordinate grid

    Returns:
        I4: float — Overlap integral value (dimension: length)
    """
    import numpy as np
    from scipy.integrate import simpson

    integrand = np.abs(f_L)**4
    I4 = simpson(integrand, x=xi)
    return I4


def main():
    print(f"Running: {SCRIPT_NAME}")
    print(f"Classification: REPRO (Stub — {OPR_BLOCKED} Blocked)")
    print()

    # Check for required inputs
    missing = check_inputs()

    if missing:
        fail_with_opr_reference(missing)

    # If we get here, inputs exist — proceed with calculation
    # (This code path will be reached after OPR-21 closure)
    try:
        import numpy as np
        import json

        # Load inputs
        f_L_path = Path(__file__).parent.parent / REQUIRED_INPUTS["f_L_profile"]
        params_path = Path(__file__).parent.parent / REQUIRED_INPUTS["bvp_params"]

        f_L_data = np.load(f_L_path)
        with open(params_path) as f:
            params = json.load(f)

        xi = f_L_data['xi']
        f_L = f_L_data['f_L']

        # Compute I₄
        I4 = compute_i4(f_L, xi)

        print(f"I₄ = {I4:.6e} (natural units)")
        print(f"Parameters: α = {params.get('alpha', 'N/A')}, ℓ = {params.get('ell', 'N/A')}")

        # Save output
        OUTPUT_DIR.mkdir(exist_ok=True)
        output_file = OUTPUT_DIR / "repro_i4_result.txt"
        with open(output_file, 'w') as f:
            f.write(f"I4 = {I4}\n")
            f.write(f"alpha = {params.get('alpha', 'N/A')}\n")
            f.write(f"ell = {params.get('ell', 'N/A')}\n")

        print(f"Output saved: {output_file}")

    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
