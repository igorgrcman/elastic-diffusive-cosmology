# Label & Reference Audit — Final

**Date:** 2026-02-10
**PDF:** main.pdf (224 pages)

---

## Summary

| Metric | Count |
|--------|-------|
| Undefined references | **0** |
| Multiply-defined labels | **0** |
| `??` in PDF | **0** |

---

## Label Inventory

| Type | Prefix | Count |
|------|--------|-------|
| Chapters | `ch:` | 17 |
| Sections | `sec:` | 173 |
| Equations | `eq:` | 74 |
| Tables | `tab:` | 38 |
| Figures | `fig:` | ~5 |
| Appendices | `app:` | 6 |
| Derivations | `deriv:` | 1 |

---

## Chapter Labels (Canonical)

| Ch | Label | Title |
|----|-------|-------|
| 1 | `ch:anchor` | Anchor Junction as Topological Ground State |
| 2 | `ch:junction` | Junction Symmetries |
| 3 | `ch:metastable` | The Metastable Junction |
| 4 | `ch:sigma_to_K` | From Brane Tension to Pinning Constant |
| 5 | `ch:M6` | The M₆ Coordination Lattice |
| 6 | `ch:instanton` | The Instanton Chain |
| 7 | `ch:kappa` | The Homotopy Factor κ |
| 8 | `ch:L0delta` | The L₀/δ Ratio |
| 9 | `ch:tau_n` | Metastable Lifetime Prediction |
| 10 | `ch:deuterium` | Deuterium Binding |
| 11 | `ch:helium4` | The Closed-4 Unit |
| 12 | `ch:light_clusters` | Light Cluster Systematics |
| 13 | `ch:barrier_release` | Barrier-Release Law |
| 14 | `ch:frustrated` | Coordination Frustration |
| 15 | `ch:high_coord` | High-Coordination Predictions |
| 16 | `ch:unified` | The Unified Picture |
| 17 | `ch:repro` | Reproducibility & Verification |

---

## Appendix Labels

| App | Label | Title |
|-----|-------|-------|
| A | `app:superheavy` | Code: superheavy_predictions.py |
| B | `app:kramers` | Code: kramers_double_well_v2.py |
| C | `app:tables` | Numerical Tables |
| D | `app:provenance` | Provenance Index |
| Q | `app:quarantine` | Calibration Quarantine |
| X | `app:analogies` | Analogies (Non-Binding) |

---

## Verification

```bash
grep "LaTeX Warning.*undefined" main.log
# Result: (empty - no warnings)

grep "multiply defined" main.log
# Result: (empty - no warnings)

pdftotext main.pdf - | grep -c "??"
# Result: 0
```

**Status:** ✅ PASS — All references resolved
