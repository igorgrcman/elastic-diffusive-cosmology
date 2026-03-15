# Derivation v46 — No-Escape Track Selector

**Deterministic Choice from SoT + ΔE_vac + Burden + Hooks**

## Summary

This derivation implements a deterministic "No-Escape Track Selector" that
consumes the v45 Single Source of Truth (SoT) and produces exactly one
selected GUT track or an explicit UNRESOLVED status.

## Decision Pipeline

1. **Stage 0 (Hard Gates):** Anomaly = 0, hash-lock verified
2. **Stage 1 (Admissibility):** PASS > CONDITIONAL; AC-P47-17 exclusion
3. **Stage 2 (Vacuum Energy):** min ΔE_vac^finite
4. **Stage 3 (Burden):** min mechanism burden B
5. **Stage 4 (Hooks):** max prediction hooks H
6. **Tie-breakers:** dim(G), rank drop, exotic count

## Selection Result

| Stage | Winner | Criterion |
|-------|--------|-----------|
| 0 | All pass | Anomalies = 0, hash verified |
| 1 | SO(10), PS | PASS status (SU5, E6 excluded) |
| 2 | **Pati-Salam** | S_vac(PS) = 25 < S_vac(SO10) = 49 |

**Selected Track: Pati-Salam**

## Files

| File | Description |
|------|-------------|
| `main.tex` | Main LaTeX document |
| `main.pdf` | Compiled PDF |
| `recompute.py` | Decision engine + 55 checks |
| `tables_generated.tex` | Auto-generated tables |
| `EDC_BLOCK003_DERIVATION_V46_NO_ESCAPE_TRACK_SELECTOR.pdf` | Export PDF |

## Reproduction

```bash
cd derivation_v46
python3 recompute.py      # Generate tables + run 55 checks
pdflatex main.tex         # Build PDF
pdflatex main.tex         # Resolve references
```

Expected output: `ALL CHECKS PASSED` with PS SELECTED

## Metrics

- **Pages**: 26 (requirement: ≥26)
- **Equations**: 228 (requirement: ≥160)
- **Labels**: 350 (requirement: ≥240)
- **Verification checks**: 55 (requirement: ≥45)
- **Reviewer traps**: 18 (requirement: ≥18)

## Hash Verification

- v45 SoT hash: `a80b3886903152d3` (VERIFIED)
- v46 tables hash: `2742edea37e863ac`

## Dependencies

- v45: SoT-lock track compiler
- v41: ΔE_vac ranking
- v37: Regulator invariance
