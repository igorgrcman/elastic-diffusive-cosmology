# Derivation v48: PS G_F Numerical Closure

## Title
**PS G_F NUMERICAL CLOSURE: g_5 + L Fix + KK Convergence + Brane Sensitivity**

## Summary

This derivation closes the three blocking items from v47's G_F readiness map:
1. **g_5 fixing:** Two admissible routes (A: tension, C: cutoff)
2. **L determination:** Structurally closed via EDC relations (β, σ)
3. **KK sum convergence:** Regulator-invariant with ζ(2) = π²/6

Additionally:
4. **BKT sensitivity:** Bounded perturbation with δG_F/G_F < 2r_B/L

## Key Results

### g_5 Fixing Routes

| Route | Formula | Tag | Status |
|-------|---------|-----|--------|
| A (Tension) | g_5² = c_A / M_5 | [Dc]+[P] | ADMISSIBLE |
| C (Cutoff) | g_5² = 4π / Λ_5 | [Dc]+[P] | ADMISSIBLE |
| B (GUT) | g_5² = g_GUT² L | [D]+[OPEN] | CONDITIONAL |

### L Determination
```
L = M̄_Pl √(β/σ) = (1/M̄_Pl) √(β/σ̃)
```

### KK Sum Convergence
```
Σ_{n=1}^∞ 1/n² = ζ(2) = π²/6
```
- Zeta regulator: π²/6 ✓
- Heat kernel: π²/6 ✓
- Pauli-Villars: π²/6 ✓

**Status:** REGULATOR_INVARIANT

### BKT Sensitivity
```
g_4² = g_5² / (L + r_B)
δG_F/G_F = -2 r_B/L
```
For r_B/L < 0.01: sub-2% effect

### Final G_F Closure
```
G_F = (√2/48) g_5² L
```

Dimension check: [G_F] = -1 + (-1) = -2 ✓

## Hash Chain

| Version | Hash |
|---------|------|
| v45 (SoT) | `a80b3886903152d3` |
| v46 (Selector) | `2742edea37e863ac` |
| v47 (PS Canon) | `7a9682f333d5349e` |
| v48 (Tables) | `c4f114aa0c662b66` |

## Reproduction

```bash
cd derivation_v48
python3 recompute.py      # Generate tables + run 49 checks
pdflatex main.tex         # Build PDF
pdflatex main.tex         # Resolve references
```

## Metrics

| Metric | Required | Achieved |
|--------|----------|----------|
| Pages | ≥26 | 27 |
| Equations | ≥170 | 333 |
| Labels | ≥240 | 297 |
| Checks | ≥45 | 49 |
| Traps | ≥18 | 18 |

## Files

- `main.tex` — Main document
- `main.pdf` — Compiled PDF (27 pages)
- `recompute.py` — Verification engine + checks
- `tables_generated.tex` — Auto-generated tables
- `EDC_BLOCK003_DERIVATION_V48_PS_GF_NUMERICAL_CLOSURE_G5_L_KK_CONVERGENCE.pdf` — Export
- `README.md`, `REPORT.md`, `ACCEPTANCE.md` — Documentation

## Compliance

- **PS Canonical Lock:** Enforced
- **HR-P48-N0 (Zero-Handwave):** All factors derived
- **Forbidden Inputs:** NOT USED

## Remaining Open (for numeric evaluation)

- β value (EDC parameter)
- σ̃ value (normalized tension)
- Route A/C coefficient

## Date
February 2026
