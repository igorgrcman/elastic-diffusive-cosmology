# Derivation v42: E₆ Anomaly Audit + Exotics Mass Gating

## Overview

This derivation performs an ultra-hard audit of the BC-selected GUT track ranking from v41, where E₆ achieved the lowest ΔE_vac^finite due to its large exotic fermion content.

## Key Results

1. **Anomaly Audit**: Complete analysis of gauge and gravitational anomalies for surviving chiral spectra after BC projection
2. **Mass Gating Framework**: Conditions under which exotic fermions decouple from low-energy physics
3. **Track Admissibility**: Three-stage decision pipeline determining which tracks are physically viable
4. **E₆ Verdict**: E₆ passes anomaly gate but is CONDITIONAL on mass gating

## Three-Stage Pipeline

```
Stage 1: BC Selection via ΔE_vac^finite
  → E₆ < PS < SU(5) < SO(10)

Stage 2: Anomaly Gate
  → SU(5): PASS, SO(10): PASS, PS: CONDITIONAL, E₆: PASS

Stage 3: Mass Gating Gate
  → SU(5): SAFE, SO(10): SAFE, PS: SAFE, E₆: CONDITIONAL
```

## Final Admissibility

| Track  | Stage 1 | Stage 2 | Stage 3 | Overall       |
|--------|---------|---------|---------|---------------|
| SU(5)  | 3rd     | PASS    | SAFE    | ADMISSIBLE    |
| SO(10) | 4th     | PASS    | SAFE    | ADMISSIBLE    |
| PS     | 2nd     | COND    | SAFE    | CONDITIONAL   |
| E₆     | **1st** | PASS    | COND    | CONDITIONAL   |

## Key Numbers

- Pages: 33
- Equation environments: 160
- Labeled equations: 292
- Reviewer traps: 32

## Dependencies

- v33: Chiral BC from 5D Dirac variation
- v35: GUT BC survivor map
- v37: ΔE_vac^finite subtraction protocol
- v40: Gauge-only vacuum energy ranking
- v41: Matter-augmented ranking (E₆ wins)

## Files

- `main.tex`: LaTeX source
- `main.pdf`: Compiled PDF
- `recompute.py`: Verification script (27 checks)
- `REPORT.md`: Inputs used table
- `ACCEPTANCE.md`: Acceptance criteria checklist
- `EDC_BLOCK003_DERIVATION_V42_E6_ANOMALY_AUDIT_EXOTICS_MASS_GATING.pdf`: Export PDF

## Verification

```bash
python3 recompute.py
```

All 27 checks should pass.
