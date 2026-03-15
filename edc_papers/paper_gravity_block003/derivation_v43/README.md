# Derivation v43 — PS Chirality Closure + Anomaly Gate

## Purpose

Close the Pati–Salam CONDITIONAL status from v42 by:
1. Resolving the 42 vs 45 SM Weyl discrepancy
2. Providing explicit PS→SM decomposition with hypercharge embedding
3. Computing all anomaly sums explicitly from field tables
4. Upgrading PS from CONDITIONAL → PASS

## Key Results

- **42→45 Reconciliation**: The "missing" 3 Weyl fermions are ν_R with mixed BC → no zero-mode
- **Hypercharge Embedding**: Y = T_{3R} + (B-L)/2 verified for all SM fields
- **All Anomalies**: Computed explicitly, all vanish:
  - SU(3)³ = 0
  - SU(2)²U(1) = 0
  - SU(3)²U(1) = 0
  - U(1)³ = 0
  - U(1)-grav = 0
  - Witten SU(2) = 0 (even doublet count)
- **Final Verdict**: PS upgraded to PASS

## Dependencies

- **v35**: BC Registry (provides BC assignments)
- **v39**: Vacuum Energy Rankings
- **v41**: SM Fermion Count Audit
- **v42**: E₆ Anomaly Audit (established CONDITIONAL status)

## Files

| File | Description |
|------|-------------|
| main.tex | Main derivation document |
| main.pdf | Compiled PDF |
| EDC_BLOCK003_DERIVATION_V43_PS_CHIRALITY_ANOMALY_CLOSURE.pdf | Export copy |
| recompute.py | Verification script (≥20 checks) |
| README.md | This file |
| REPORT.md | Detailed report |
| ACCEPTANCE.md | Acceptance criteria |

## Verification

```bash
cd derivation_v43
python3 recompute.py
# Expected: 26/26 CHECKS PASSED
```

## Document Stats

| Metric | Value | Requirement |
|--------|-------|-------------|
| Pages | 32 | ≥24 |
| Equations | 148 | ≥140 |
| Labels | 304 | ≥180 |
| Checks | 26 | ≥20 |

## P44 Cleanup

- Removed working chatter ("Wait---", "Correction:", etc.)
- U(1)³ appendix rewritten as one-shot derivation using canonical LH Weyl basis
- Added Reader Contract box declaring conventions
- Added Reviewer Trap Checklist (15 items)
- AC-P44-12: U(1)³ = 0 verified both symbolically (LaTeX) and numerically (recompute.py)

---

*Created: 2026-02-04*
*P44 cleanup: 2026-02-05*
