# P55 / Derivation v54: BLOCK-003 Canonical Single Document

## Summary

This derivation consolidates the complete BLOCK-003 chain (v45–v53) into a single, readable canonical reference document. It provides a deterministic narrative from track selection to electroweak predictions.

## Key Features

1. **Deterministic Track Selection**
   - PASS > CONDITIONAL scoring algorithm
   - PS uniquely selected (score = 5)

2. **PS Canonicalization**
   - Coupling matching: 1/g_Y² = c_R/g_R² + c_{B-L}/g_{B-L}²
   - Trace ledger verified
   - Two-route verification

3. **Electroweak Predictions**
   - sin²θ_W(μ_*) = 5/12
   - G_F formula (structural)
   - c_R + c_{B-L} = 7/5

4. **Invariance Suite**
   - Scheme invariance (T1 = T2)
   - Unit invariance (S-scaling)
   - Log hygiene (dimensionless)
   - Regulator invariance

5. **Layer Separation**
   - Layer A: Canonical (hash-locked)
   - Layer B: External adapter (quarantined)
   - Hash Firewall protocol

## Files

| File | Description |
|------|-------------|
| main.tex | LaTeX source (33 pages) |
| main.pdf | Compiled document |
| recompute.py | Verification script (83 checks) |
| REPORT.md | Detailed report |
| README.md | This file |
| ACCEPTANCE.md | Acceptance criteria |

## Verification

```bash
python3 recompute.py
```

Expected output:
```
Total: 83/83 CHECKS PASSED
All checks PASS
v54 tables hash: 19c69e794c9703b7
```

## Hash Chain

| Version | Topic | Hash |
|---------|-------|------|
| v45 | SoT Lock Track Compiler | a80b3886903152d3 |
| v46 | No-Escape Track Selector | 2742edea37e863ac |
| v47 | PS Coupling Matching | 7a9682f333d5349e |
| v48 | G_F Numerical Closure | c4f114aa0c662b66 |
| v49 | Weinberg Angle Closure | 81010ef2faedcefd |
| v50 | PS→IR Matching Scalemap | cebf3e5baf0de863 |
| v51 | Log Hygiene + Unit Inv | ed8fa089897b2d8c |
| v52 | PS Prediction Pack | ed92d9bc43b8d26b |
| v53 | Observable Interface | 89a4854b0bdfd332 |
| v54 | Canonical Single Document | 19c69e794c9703b7 |

## Export

`EDC_BLOCK003_DERIVATION_V54_BLOCK003_CANONICAL_SINGLE_DOCUMENT.pdf`

## Hard Rules

- HR-0: No overwrite of existing derivation_v*/
- HR-1: No forbidden anchors in Layer A
- HR-2: No build artifacts committed
- HR-3: Hash chain verified
- HR-4: Deterministic narrative
- HR-5: No destructive git operations
