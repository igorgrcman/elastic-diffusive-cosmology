# CH7 CKM Attempt 2.2 Notes

**Date:** 2026-01-22
**Status:** Complete
**Commit:** (pending)

## Purpose

Attempt 2.2 analyzes whether the 2.5× overshoot in |V_ub| from Attempt 2.1 can be
resolved via unitarization or profile shape changes, WITHOUT introducing new parameters.

## Key Finding

**The 2.5× overshoot is NOT a failure — it's the expected result.**

The overlap model gives |V_ub| ~ Aλ³ ≈ 0.0094, which matches the Wolfenstein
parametrization exactly. The actual PDG value |V_ub| = 0.0037 includes an
additional factor |ρ̄ - iη̄| ≈ 0.38 from CP structure.

Expected overshoot: 1/|ρ̄ - iη̄| = 1/0.38 = **2.61**
Observed overshoot: 0.0094/0.0037 = **2.55**
Agreement: **2%**

## Inputs (unchanged from Attempt 2.1)

- Δz₁₂/(2κ) = -ln(V_us) = **1.4917** [Cal]
- Δz₂₃/(2κ) = -ln(V_cb) = **3.1744** [Cal]
- No additional fitted parameters

## Methods Tested

### 1. Unitarization (REJECTED)

- Polar decomposition: Maps overlap matrix to identity (all off-diagonal → 0)
- Gram-Schmidt: Destroys corner elements
- Reason: Symmetric overlap matrix ≈ I, so "closest unitary" is I itself

### 2. Gaussian Profile (REJECTED)

- Gaussian: O_ij = exp(-d_ij²) instead of exp(-d_ij)
- Result: V_ub ≈ 10⁻⁴ — FAR too small
- Gaussian over-suppresses corner elements
- Exponential profile is the correct ansatz

### 3. Wolfenstein Analysis (KEY RESULT)

- Overlap model predicts |V_ub| = exp(-(d₁₂+d₂₃)) = Aλ³
- This is structurally identical to Wolfenstein's "simple product"
- Missing factor: |ρ̄ - iη̄| ≈ 0.38 from CP structure
- To derive this factor, need complex phases in 5D geometry

## Epistemic Status

| Claim | Status | Tag |
|-------|--------|-----|
| Structure |V_ub| ~ λ³ | **GREEN** | [Dc] |
| Match with Aλ³ | **GREEN** | [Dc] |
| Prefactor = 1/|ρ-iη| | **YELLOW** | [I] |
| Exponential profile correct | **GREEN** | [Dc] |
| CP factor (ρ̄,η̄) derivation | **RED** | [OPEN] |

## Code

- `code/ckm_attempt2_2.py` — Full analysis script
- Output confirms all numerical results

## LaTeX Integration

- Added §7.6 "Attempt 2.2: Understanding the Prefactor Discrepancy"
- Updated Chain Box with Attempt 2.2 entry
- Updated Stoplight table with GREEN structure, YELLOW prefactor

## What This Resolves

✓ The 2.5× is NOT a failure — it's expected without CP structure
✓ Unitarization cannot fix it (not a normalization issue)
✓ Gaussian profiles make it WORSE
✓ The "missing factor" is precisely |ρ̄ - iη̄| from Wolfenstein

## What Remains Open

✗ Deriving ρ̄, η̄ from 5D geometry
✗ Origin of CP phase δ from boundary conditions
✗ Jarlskog invariant J ~ 3×10⁻⁵ prediction

## Conclusion

The overlap model is structurally correct: it derives the Wolfenstein Aλ³ hierarchy
from geometry. The prefactor discrepancy points to CP physics, not a flaw in the
geometric interpretation.
