# P59 / Derivation v55: BLOCK-004 PS → QCD (α₃) Structural Closure

## Summary

This derivation initiates **BLOCK-004** (Strong Sector) by deriving the
Pati-Salam to QCD coupling matching and establishing the canonical α₃(μ*)
observable at the EDC reference scale μ* := π/L.

## Key Features

1. **Color Matching Theorem**
   - Embedding: SU(3)_c ⊂ SU(4)_C
   - Trace normalization: c_C = 1
   - Two-route verification: T1 = T2

2. **Observable Interface API**
   - API-C1: μ* := π/L (canonical)
   - API-C2: α₃(μ*) = g₃²(μ*)/(4π)
   - API-C3: RG connector (symbolic)
   - API-C4: Threshold hooks (TEMPLATE)

3. **Layer A/B Firewall**
   - Layer A: Structural derivations only
   - Layer B: Quarantined external anchors
   - Hash firewall enforced

4. **RG Translation**
   - β₃ = -7 (SM structural constant)
   - Scheme invariance verified

## Files

| File | Description |
|------|-------------|
| main.tex | LaTeX source |
| main.pdf | Compiled document |
| recompute.py | Verification script (SoT + hash lock) |
| REPORT.md | Detailed report |
| README.md | This file |
| ACCEPTANCE.md | Acceptance criteria |

## Verification

```bash
python3 recompute.py
```

Expected output:
```
Total: 55+/55+ CHECKS PASSED
All checks PASS
v55 SoT hash: [computed]
```

## Hash Chain

| Version | Topic | Hash |
|---------|-------|------|
| v54 | BLOCK-003 Canonical | 19c69e794c9703b7 |
| v55 | PS → QCD α₃ Closure | [computed] |

## Export

`EDC_BLOCK004_DERIVATION_V55_PS_TO_QCD_ALPHA3_STRUCTURAL_CLOSURE.pdf`

## Hard Rules

- HR-0: No overwrite of existing derivation_v*/
- HR-1: No forbidden anchors in Layer A
- HR-2: No build artifacts committed
- HR-3: SoT hash verified
- HR-4: Two-route verification (T1 = T2)
- HR-5: Log hygiene (USED vs TEMPLATE)
