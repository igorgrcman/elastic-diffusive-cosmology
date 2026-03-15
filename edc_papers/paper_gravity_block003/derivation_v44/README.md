# Derivation v44 — Anomaly One-Shot: SoT Lock

**Single Source of Truth + LaTeX↔Python Lock**

## Summary

This derivation establishes an engineering-grade lock protocol for SM anomaly calculations.
All numerical values in LaTeX tables are auto-generated from a Single Source of Truth (SoT)
defined in `recompute.py`, with SHA-256 hash verification to prevent drift.

## Key Features

1. **Single Source of Truth (SoT)**: All field data (representations, multiplicities,
   hypercharges, boundary conditions, epistemic tags) defined in exactly one place

2. **Auto-generated tables**: `tables_generated.tex` produced programmatically from SoT,
   not manually typed

3. **Hash verification**: Any manual edit to generated tables causes build failure

4. **Complete anomaly audit**: All 6 gauge anomalies + Witten parity computed from SoT:
   - SU(3)³ = 0
   - SU(2)²U(1) = 0
   - SU(3)²U(1) = 0
   - U(1)³ = 0
   - U(1)-gravitational = 0
   - Witten SU(2) parity = even

5. **Two-route verification**: Critical anomalies verified by independent calculation paths

## Files

| File | Description |
|------|-------------|
| `main.tex` | Main LaTeX document |
| `main.pdf` | Compiled PDF |
| `recompute.py` | SoT + verification script |
| `tables_generated.tex` | Auto-generated tables (DO NOT EDIT) |
| `EDC_BLOCK003_DERIVATION_V44_ANOMALY_ONESHOT_SOT_LOCK.pdf` | Export PDF |

## Reproduction

```bash
cd derivation_v44
python3 recompute.py      # Generate tables + run 26 checks
pdflatex main.tex         # Build PDF
pdflatex main.tex         # Resolve references
```

Expected output: `ALL CHECKS PASSED`

## Metrics

- **Pages**: 30 (requirement: ≥24)
- **Equations**: 155 (requirement: ≥140)
- **Labels**: 242 (requirement: ≥180)
- **Verification checks**: 26 (requirement: ≥25)
- **Reviewer traps**: 16 (requirement: ≥14)

## Lock Protocol

**DO NOT manually edit `tables_generated.tex`!**

To update tables legitimately:
1. Edit `SoT_FIELDS` in `recompute.py`
2. Run `python3 recompute.py`
3. Commit both files together

## Dependencies

- Prior derivations: v35 (BC registry), v37 (regulator protocol), v43 (PS anomaly closure)
- No forbidden inputs: M_Z, M_W, v_EW, α_EM, G_N, ℓ_P

## Hash

Tables hash: `ea07022b108f0721`
