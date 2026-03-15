# Derivation v50: PS → IR Matching & Physical-Scale Map

## Overview

This derivation establishes a rigorous, regulator- and scheme-aware matching scaffold for descending from the KK scale μ_KK = π/L to a symbolic IR scale μ_IR, without using any forbidden experimental inputs.

## Key Results

### Physical Scale Map (Two Panels)
- **Panel A:** Energy regimes: Λ_5 → 5D PS bulk → μ_KK → 4D EFT → μ_IR
- **Panel B:** Coupling flow: g_5 → (g_L, g_R, g_{B-L}) → g_Y → SM couplings

### Matching Stack
1. **At μ_KK:** PS matching with BKT: `1/g_Y² = (3/5)/g_R² + (4/5)/g_{B-L}²`
2. **Running:** `d(1/g²)/d ln μ = b/(8π²)` with derived beta coefficients
3. **Thresholds:** `Δ_i` with scheme-invariant finite parts

### Scheme Invariance
- Two-route verification (T1: match→run, T2: run→match)
- Lemma proving invariant combinations

### Exotics Gating
- BC-gating mechanism for PS exotics
- Condition: μ_gate ≥ μ_KK (symbolic inequality)

### Notation Registry
- Complete registry of all symbols with meanings and dimensions
- Authoritative: no unregistered symbols allowed

## Hard Rules

- **PS Canonical Lock:** Pati-Salam track, switching forbidden
- **Forbidden Inputs:** Electroweak masses, VEV, Newton's constant, Planck length NOT USED
- **Notation Lock:** All symbols in registry

## Reproduction

```bash
cd derivation_v50
python3 recompute.py      # 37/37 checks must PASS
pdflatex main.tex
pdflatex main.tex
```

## Export

`EDC_BLOCK003_DERIVATION_V50_PS_TO_IR_MATCHING_SCALEMAP.pdf`

## Dependencies

- v47: Coupling matching and Weinberg hook
- v48: G_F closure, L determination
- v49: Weinberg angle at KK scale

## Hash Chain

- v45: `a80b3886903152d3`
- v46: `2742edea37e863ac`
- v47: `7a9682f333d5349e`
- v48: `c4f114aa0c662b66`
- v49: `81010ef2faedcefd`
- v50 tables: `cebf3e5baf0de863`

## Metrics

| Metric | Required | Achieved |
|--------|----------|----------|
| Pages | ≥24 | 24 |
| Equations | ≥160 | 296 |
| Checks | ≥25 | 37 |
| Traps | ≥18 | 18 |

## Status

**MATCHING SCAFFOLD COMPLETE** — Framework for IR predictions without forbidden inputs.
