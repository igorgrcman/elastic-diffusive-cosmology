# Derivation v45 — SoT-Lock Track Compiler

**Full Spectrum → Anomalies + ΔE_vac + Mass Gating**

## Summary

This derivation implements an engineering-grade "track compiler" that processes
GUT track definitions and produces:
- (A) Full anomaly audit (all 6 + Witten) for all tracks
- (B) ΔE_vac^finite scoring inputs
- (C) Mass-gating constraints for exotics

All four GUT tracks processed: SU(5), SO(10), Pati-Salam, E6

## Key Features

1. **Unified SoT_TRACKS**: All track data in one Python structure
2. **Track compiler**: Definition → anomalies + ΔE_vac + gating
3. **Auto-generated tables**: 8 tables from SoT (no manual entry)
4. **Hash lock**: SHA-256 verification prevents drift
5. **Admissibility classification**: PASS/CONDITIONAL/FAIL with reason codes

## Files

| File | Description |
|------|-------------|
| `main.tex` | Main LaTeX document |
| `main.pdf` | Compiled PDF |
| `recompute.py` | SoT_TRACKS + verification (56 checks) |
| `tables_generated.tex` | Auto-generated tables (DO NOT EDIT) |
| `EDC_BLOCK003_DERIVATION_V45_SOT_LOCK_TRACK_COMPILER.pdf` | Export PDF |

## Reproduction

```bash
cd derivation_v45
python3 recompute.py      # Generate tables + run 56 checks
pdflatex main.tex         # Build PDF
pdflatex main.tex         # Resolve references
```

Expected output: `ALL CHECKS PASSED` with 56/56 checks

## Metrics

- **Pages**: 28 (requirement: ≥28)
- **Equations**: 192 (requirement: ≥160)
- **Labels**: 291 (requirement: ≥220)
- **Verification checks**: 56 (requirement: ≥30)
- **Reviewer traps**: 18 (requirement: ≥16)

## Track Results

| Track | Anomalies | Exotics Gated | Status |
|-------|-----------|---------------|--------|
| SU(5) | All = 0 | 2/2 (brane mass) | CONDITIONAL |
| SO(10) | All = 0 | 0/0 | PASS |
| PS | All = 0 | 1/1 (mixed BC) | PASS |
| E6 | All = 0 | 5/5 | CONDITIONAL |

## Dependencies

- v35: BC registry
- v37: Regulator invariance
- v40/v41: ΔE_vac ranking
- v42/v43: Anomaly closure
- v44: SoT lock protocol

## Hash

Tables hash: `a80b3886903152d3`
