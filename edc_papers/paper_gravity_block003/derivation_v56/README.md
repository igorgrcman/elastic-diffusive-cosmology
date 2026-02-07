# P60 / Derivation v56: BLOCK-004 α₃(μ*) Numerical Closure

## Summary

This derivation upgrades v55 from structural α₃(μ*) to numerical closure
(or strictly bounded closure) in Layer A, while preserving the Layer A/B
firewall and hash chain discipline.

## Key Features

1. **PS Unification Hook**
   - Postulate: g₅^(C) = g₅^(L) = g₅^(R) = g₅^(B-L)
   - Tag: [P] (postulate, not derived)
   - Where-used: g₅ fixing, α_PS definition

2. **Admissible Routes**
   - Route A (Tension): (g₅^PS)² = 4π/M₅
   - Route C (Cutoff): (g₅^PS)² = 4π/Λ₅
   - Route B (GUT): EXCLUDED by HR-P47-1

3. **α₃(μ*) Closure**
   - Baseline: α₃(μ*) = 1/(M̄_Pl · L)^{2/3} = 1/σ̃
   - Bounded: α₃(μ*) = (1/σ̃) · (1 ± ε_max)
   - Status: PREDICTION (or BOUNDED_PREDICTION)

4. **Two-Route Verification**
   - T1: via g₄C matching
   - T2: direct 5D→4D reduction
   - Result: T1 = T2 VERIFIED

5. **Layer A/B Firewall**
   - Layer A: Structural derivations only
   - Layer B: Quarantined external anchors
   - Hash firewall: no backflow

## Files

| File | Description |
|------|-------------|
| main.tex | LaTeX source |
| main.pdf | Compiled document |
| recompute.py | Verification script (70+ checks) |
| REPORT.md | Detailed report |
| README.md | This file |
| ACCEPTANCE.md | Acceptance criteria |

## Verification

```bash
python3 recompute.py
```

Expected output:
```
Total: 70+/70+ CHECKS PASSED
All checks PASS
v56 SoT hash: [computed]
```

## Hash Chain

| Version | Topic | Hash |
|---------|-------|------|
| v54 | BLOCK-003 Canonical | 19c69e794c9703b7 |
| v55 | PS → QCD Structural | 1794377561879613 |
| v56 | α₃ Numerical Closure | [computed] |

## Export

`EDC_BLOCK004_DERIVATION_V56_ALPHA3_MUSTHAVE_NUMERICAL_CLOSURE_NO_CONTAMINATION.pdf`

## Hard Rules

- HR-0: No overwrite of existing derivation_v*/
- HR-1: No forbidden anchors in Layer A
- HR-2: No build artifacts committed
- HR-3: SoT hash verified
- HR-4: Two-route verification (T1 = T2)
- HR-5: Log hygiene (USED vs TEMPLATE)
- HR-P47-1: PASS > CONDITIONAL
