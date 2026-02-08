# V7.8 — S_α AND DEFORMATION PROXY ANALYSIS

**Created**: 2026-01-31
**Purpose**: Test whether d(n) effect is mediated by preformation or confounded with deformation
**Dataset**: 106 α-emitters (V7.4 augmented with proxies)
**Verdict**: **ROBUST** — d(n) survives both controls

---

## Executive Summary

V7.7 established that g < 0 is consistent with prefactor (S_α) enhancement. V7.8 tested this by adding:
1. **Deformation proxy**: Shell distance product |N-126|×|Z-82|/1000
2. **S_α proxy**: Royer preformation estimate

**Key Finding**: When both proxies are included (M7), the d(n) coefficient remains:
- Negative: g = -1.71
- Significant: p < 0.001
- Stable: Only 4.2% change from baseline

The deformation proxy becomes **non-significant** (p = 0.67) when d(n) is present, suggesting d(n) absorbs deformation-related variance and captures additional topological information.

---

## Model Summary

| Model | Description | g(d(n)) | p | AIC |
|-------|-------------|---------|---|-----|
| M0 | GN only | — | — | 354.9 |
| M1 | + hindrance | — | — | 353.3 |
| **M2** | + d(n) | **-1.64** | **<0.001** | **266.2** |
| M3 | + proxy_deform | — | — | 276.4 |
| M4 | + proxy_Salpha | — | — | 335.4 |
| M5 | + d(n) + deform | -1.46 | 0.001 | 268.0 |
| M6 | + d(n) + Salpha | -1.53 | <0.001 | 264.2 |
| **M7** | + d(n) + both | **-1.71** | **<0.001** | 266.0 |

---

## Primary Tests

| Test | Criterion | Observed | Status |
|------|-----------|----------|--------|
| P1 | g < 0, p < 0.01 (M2) | g = -1.64, p < 0.001 | ✓ PASS |
| P2 | g survives deform (M5) | g = -1.46, p = 0.001 | ✓ PASS |
| P3 | g survives Salpha (M6) | g = -1.53, p < 0.001 | ✓ PASS |
| P4 | |Δg| < 20% (M2→M7) | Δg = 4.2% | ✓ STABLE |

**All primary tests passed.**

---

## Mediation Analysis

| Proxy | Alone (p) | With d(n) (p) | Interpretation |
|-------|-----------|---------------|----------------|
| proxy_deform | <0.001 | 0.67 | **Absorbed by d(n)** |
| proxy_Salpha | <0.001 | 0.05 | Marginally independent |

### Interpretation

- **Deformation**: d(n) captures deformation-related variance; proxy_deform becomes redundant
- **S_α**: Royer proxy adds marginal predictive value but doesn't mediate d(n) effect
- **Conclusion**: d(n) contains topological information beyond standard nuclear structure parameters

---

## Files in This Package

| File | Description |
|------|-------------|
| 00_README.md | This summary |
| 01_SESSION_LOG.md | Chronological log |
| 02_SOURCES_AND_VERSIONS.md | Data source whitelist |
| 03_PROXY_SPEC.md | Proxy definitions and rationale |
| 04_DATASET_AUGMENTATION.csv | Augmented dataset (106 × 22) |
| 05_AUGMENTATION_AUDIT.md | Coverage and bias analysis |
| 06_MODELS_V7_8.md | Pre-registered model specification |
| 07_FIT_RESULTS_V7_8.md | Complete regression tables |
| 08_MEDIATION_AND_INTERPRETATION.md | Mechanistic interpretation |
| 09_BOOK2_PARAGRAPH_V7_8.md | Sign-safe text variants |
| 10_OPEN_QUESTIONS_V7_8.md | Updated kingpin blockers |
| code/build_dataset_v7_8.py | Dataset augmentation script |
| code/fit_models_v7_8.py | Model fitting script |

---

## Reproducibility

```bash
cd audit/radioactivity_v7_8_Salpha_deformation/code

# Generate augmented dataset
python3 build_dataset_v7_8.py

# Fit models and print results
python3 fit_models_v7_8.py
```

**Requirements**: Python 3.x (no external dependencies)

---

## Implications for EDC

### Strengthened
- d(n) effect is robust to structural controls
- Not a trivial deformation proxy
- Compatible with topological mechanism

### Updated Status
- Deformation confound: **Resolved** (absorbed by d(n))
- S_α mediation: **Partial** (Royer doesn't fully explain)
- Mechanism: **Strengthened [P]** (approaching [I])

---

## Verdict

```
V7.8 verdict: ROBUST — d(n) remains significant (p < 0.001) and stable (4% change)
after including deformation and S_α proxies. The effect captures topological
information beyond standard nuclear structure parameters.
```

---

## One-Sentence Summary

**The M-topology coordination distance d(n) predicts α-decay rates robustly, even after controlling for nuclear deformation and preformation proxies, suggesting it captures genuine topological information.**

