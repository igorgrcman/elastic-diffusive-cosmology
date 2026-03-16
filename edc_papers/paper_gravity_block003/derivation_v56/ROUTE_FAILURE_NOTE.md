# Route A/C Numerical Failure — Post-Audit Note
## Date: 2026-03-16
## Status: WARNING — v56 routes fail numerically

## Finding

G5C derivation audit (commit: see OPR-32) showed that
Routes A and C of v56 fail numerically by 7-10 orders
of magnitude:

| Route | Formula | α₃ predicted | α_s(M_Z) | Factor off |
|-------|---------|--------------|-----------|------------|
| A | g₅² = 4π/M₅ | 5.2×10⁻¹² | 0.118 | 2.3×10¹⁰ |
| C (σ^{1/4}) | g₅² = 4π/σ^{1/4} | ~10⁻⁸ | 0.118 | ~10⁷ |

## Consequence

The formula α₃(μ*) = 1/σ̃ derived in v56 §4 is an
artefact of Route A assumptions that fail numerically.

The algebraic derivation in v56 is internally consistent
but the physical input (Route A coupling) is wrong by
10 orders of magnitude.

## What survives from v56

- Dimensional analysis [g₅²] = M⁻¹ [I]
- KK reduction g₄² = g₅²/L [I]
- PS unification hook [P] (still postulate)
- Brane perturbation structure [P]
- g₅^(B-L) = g₅^(C) from SU(4) [D]

## What is invalidated

- α₃ = 1/σ̃ (requires Route A → FAILS)
- β = σ̃⁴ (derived from Route A consistency → FAILS)
- σ̃ = 100 claim (based on α₃ = 1/σ̃ → FAILS)

## Correct picture

g₅^(C) is a free parameter fixed by α_s(M_Z) = 0.118.
σ̃ = 1 from RS geometry and Λ₄ constraint.
See: v68, COSMOLOGICAL_CONSTANT_SIGMA_TILDE.md,
     PS_UNIFICATION_HOOK_AUDIT.md, G5C_DERIVATION_AUDIT.md
