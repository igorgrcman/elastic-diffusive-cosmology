# V7.8 SESSION LOG

**Session**: S_α and Deformation Proxy Analysis
**Date**: 2026-01-31
**Status**: COMPLETE

---

## Chronological Log

### 15:00 — Setup

**Action**: Create V7.8 folder structure
**Command**: `mkdir -p audit/radioactivity_v7_8_Salpha_deformation/{code,data/proxies}`
**Result**: Success

### 15:05 — Read V7.4 Dataset

**Action**: Load 04_ALPHA100_DATASET.csv
**Result**: 106 nuclides loaded (Z = 83-100, A = 206-257)

### 15:10 — Define Proxies

**Action**: Write 03_PROXY_SPEC.md
**Proxies defined**:
- proxy_deform = |N-126| × |Z-82| / 1000 (shell distance)
- proxy_Salpha = Royer formula (log₁₀ P_α)
**Result**: Both computable from Z, A — 100% coverage

### 15:15 — Create Build Script

**Action**: Write code/build_dataset_v7_8.py
**Result**: Script to compute proxies and output augmented CSV

### 15:20 — Generate Augmented Dataset

**Action**: Run build_dataset_v7_8.py
**Output**: 04_DATASET_AUGMENTATION.csv (106 rows, 22 columns)
**Summary**:
- proxy_deform: min=0.000, max=0.558, mean=0.158
- proxy_Salpha: min=-2.168, max=-2.053, mean=-2.105

### 15:25 — Create Fitting Script

**Action**: Write code/fit_models_v7_8.py
**Models**: M0-M7 hierarchy
**Result**: Custom OLS implementation (no external deps)

### 15:30 — Run Model Fitting

**Action**: Execute fit_models_v7_8.py
**Key results**:
- M2: g = -1.643, p < 0.001
- M5: g = -1.460, p = 0.001 (with deform); proxy_deform p = 0.67
- M6: g = -1.525, p < 0.001 (with Salpha); proxy_Salpha p = 0.05
- M7: g = -1.711, p < 0.001 (full); Δg = 4.2%

### 15:45 — Verdict

**Result**: ROBUST — g survives all controls

### 15:50 — Write Documentation

**Actions**:
- 02_SOURCES_AND_VERSIONS.md
- 03_PROXY_SPEC.md
- 05_AUGMENTATION_AUDIT.md
- 06_MODELS_V7_8.md
- 07_FIT_RESULTS_V7_8.md
- 08_MEDIATION_AND_INTERPRETATION.md
- 09_BOOK2_PARAGRAPH_V7_8.md
- 10_OPEN_QUESTIONS_V7_8.md
- 00_README.md
- 01_SESSION_LOG.md

---

## Files Created

| # | File | Description |
|---|------|-------------|
| 1 | 00_README.md | Executive summary |
| 2 | 01_SESSION_LOG.md | This file |
| 3 | 02_SOURCES_AND_VERSIONS.md | Whitelist |
| 4 | 03_PROXY_SPEC.md | Proxy definitions |
| 5 | 04_DATASET_AUGMENTATION.csv | Augmented data |
| 6 | 05_AUGMENTATION_AUDIT.md | Coverage analysis |
| 7 | 06_MODELS_V7_8.md | Model specification |
| 8 | 07_FIT_RESULTS_V7_8.md | Regression tables |
| 9 | 08_MEDIATION_AND_INTERPRETATION.md | Mechanism analysis |
| 10 | 09_BOOK2_PARAGRAPH_V7_8.md | Text variants |
| 11 | 10_OPEN_QUESTIONS_V7_8.md | Updated kingpins |
| 12 | code/build_dataset_v7_8.py | Data augmentation |
| 13 | code/fit_models_v7_8.py | Model fitting |

---

## Key Commands

```bash
# Generate augmented dataset
cd audit/radioactivity_v7_8_Salpha_deformation/code
python3 build_dataset_v7_8.py

# Fit models
python3 fit_models_v7_8.py
```

---

## Numerical Summary

| Test | M2 Baseline | M7 Full | Change |
|------|-------------|---------|--------|
| g(d(n)) | -1.643 | -1.711 | -4.2% |
| p(g) | <0.001 | <0.001 | Stable |
| R² | 0.9805 | 0.9812 | +0.07% |

---

## Guardrail Compliance

| Guardrail | Status |
|-----------|--------|
| No Book2 .tex edits | ✓ |
| Full provenance | ✓ |
| Epistemic tags | ✓ |
| Sign-safe interpretation | ✓ |
| No silent rewrites | ✓ |
| No branch deletion | ✓ (N/A) |

---

## Verdict

**V7.8 verdict: ROBUST — d(n) remains significant (p < 0.001) and stable (4% change) after including deformation and S_α proxies.**

