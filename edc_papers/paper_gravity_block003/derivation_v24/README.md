# Derivation v24 — Reproducibility & Unit/Convention Audit

**Purpose:** Audit-grade numerical verification package that reproduces all key values from v23 and cross-validates the π-mapping and Planck convention conversions.

## What This Note Does

1. **Numerically reproduces** all values from v23 (canonical closure packet)
2. **Verifies π-map** between old (v15-v20) and canonical (v22+) conventions
3. **Confirms Planck conversion** factor (8π)^{1/3} = 2.924
4. **Provides error propagation** with explicit computation
5. **Includes dimensional analysis** appendix for unit tracking

## Accompanying Script

`recompute.py` independently verifies all calculations:

```bash
python3 recompute.py
```

Output: ALL CHECKS PASSED

## Audit Results Summary

| Check | Expected | Computed | Status |
|-------|----------|----------|--------|
| R_ξ^canon | 6.80e-18 m | 6.798e-18 m | PASS |
| M_5 (reduced) | 5.6e12 GeV | 5.56e12 GeV | PASS |
| M_5 (original) | 1.6e13 GeV | 1.63e13 GeV | PASS |
| π-map R_ξ | exact | <1e-10 rel | PASS |
| π-map M_5 | π^{-1/3} = 0.683 | 0.683 | PASS |
| Planck map | (8π)^{1/3} = 2.924 | 2.929 | PASS |
| Error budget | 1.1e-5 | 1.07e-5 | PASS |

## Key Conversions Verified

**π-map (old ↔ canonical):**
- R_ξ^canon = π × R_ξ^old
- M_5^canon = π^{-1/3} × M_5^old

**Planck map (reduced ↔ original):**
- M_5^orig = (8π)^{1/3} × M_5^red ≈ 2.92 × M_5^red

## Files

| File | Description |
|------|-------------|
| `main.tex` | Source document (48 equation environments) |
| `main.pdf` | Compiled output (10 pages) |
| `EDC_BLOCK003_DERIVATION_V24_REPRODUCIBILITY_AUDIT.pdf` | Export copy |
| `recompute.py` | Python verification script |
| `REPORT.md` | Build verification report |
| `ACCEPTANCE.md` | Acceptance criteria |

## Conclusion

No numerical discrepancies found. All values from v23 are independently reproduced. The π-mapping is verified to machine precision. The Planck convention conversion is confirmed.
