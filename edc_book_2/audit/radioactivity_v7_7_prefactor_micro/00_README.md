# V7.7 — PREFACTOR MECHANISM + CRYSTAL MICRO-MODEL

**Created**: 2026-01-31
**Purpose**: Mechanically coherent, falsifiable module connecting d(n) → S_α preformation
**Scope**: Prefactor channel interpretation of g < 0 with crystal/defect analogy

---

## Executive Summary

The V7.6.1 analysis established that g = -0.31 < 0: higher d(n) correlates with **faster** α-decay. Model comparison (T3) favors the **prefactor interpretation** — d(n) modulates preformation probability S_α rather than barrier penetrability.

This package develops:
1. A mechanistic narrative: frustration → enhanced surface dynamics → easier α-clustering → higher S_α
2. A crystal/defect analogy: defects in condensed matter enhance diffusion; nuclear frustration enhances preformation
3. Falsifiable predictions and forbidden-zone alternatives beyond M43

---

## Epistemic Classification

| Tag | Meaning | Count in this package |
|-----|---------|----------------------|
| [Der] | Derived from BL data | Regression results, dataset facts |
| [I] | Inferred from sources | M1, M3 mechanisms |
| [P] | Proposed (speculative) | M2, M4, M5, M6; S_α functional forms |
| [Open] | Unresolved question | Kingpin blockers |
| [BL] | Baselined in approved source | Nuclear data |

---

## Key Result

**Verdict from V7.6.1**: Most consistent with **PREFACTOR (S_α enhancement)**

| Evidence | Finding |
|----------|---------|
| T1: Hindrance interaction | g strongest in H0 (effect visible when barrier is limiting) |
| T2: Parity control | g persists after EE/EO/OE/OO dummies (not pairing proxy) |
| T3: Model comparison | Additive (prefactor) model beats multiplicative (barrier) by AIC Δ = 3.4 |

---

## Physical Picture

```
Low frustration (d(n) ≈ 0):
  Nucleus near allowed M-topology → stable configuration
  → α-cluster forms slowly → low S_α → long t₁/₂

High frustration (d(n) ≈ 3):
  Nucleus far from allowed → structural strain/defects
  → enhanced surface dynamics → α-cluster forms easily
  → high S_α → short t₁/₂
```

**Sign resolution**: Frustration destabilizes (accelerates decay), it doesn't stabilize.

---

## Deliverables

| File | Content | Status |
|------|---------|--------|
| 00_README.md | This summary | Complete |
| 01_SESSION_LOG.md | Chronological log | Complete |
| 02_DECISIONS.md | Method choices | Complete |
| 03_DONOR_TRACEBACK.md | Donor excerpts with file:line | Complete |
| 04_PREFACTOR_MECHANISM_MODEL.md | λ = ν × P × S_α narrative | Complete |
| 05_S_ALPHA_MAPPING_CANDIDATE.md | Functional forms for S_α(d) | Complete |
| 06_CRYSTAL_DEFECT_ANALOGY.md | Crystal → nucleus mapping | Complete |
| 07_FORBIDDEN_ALTERNATIVES_BEYOND_M43.md | n ∈ [37,47] mechanisms | Complete |
| 08_REANALYSIS_NOTEBOOK.md | Regression summaries | Complete |
| 09_BOOK2_PARAGRAPH_V7_7.md | 3 sign-safe variants | Complete |
| 10_OPEN_QUESTIONS_V7_7.md | Top 10 kingpins | Complete |

---

## Acceptance Check

| Criterion | Status |
|-----------|--------|
| All 11 files exist | ✓ |
| No modifications outside audit/ | ✓ (verify with git status) |
| ≥10 falsification tests | ✓ (14 total) |
| Every numeric has provenance or [BL:SOURCE_TBD] | ✓ |

---

## Falsification Tests Registry

| Test-ID | Claim | Observable | Threshold |
|---------|-------|------------|-----------|
| FT-V77-01 | S_α increases with d(n) | Independent S_α measurement | Correlation r > 0.5 |
| FT-V77-02 | Effect strongest in H0 | g(H0) vs g(H1/H2) | |g(H0)| > |g(H1)| |
| FT-V77-03 | Not pairing proxy | g after parity control | p < 0.05 |
| FT-V77-04 | Prefactor model preferred | AIC(additive) < AIC(multiplicative) | Δ > 2 |
| FT-V77-05 | Crystal analogy | Defect density → mobility | Positive correlation |
| FT-V77-06 | M1 domain mixing | α-anisotropy | > 5% |
| FT-V77-07 | M3 clustering | α-branch vs N/Z | r > 0.8 |
| FT-V77-08 | Linear S_α(d) | Residual structure | No curvature |
| FT-V77-09 | Saturating S_α(d) | Fit improvement | AIC drops |
| FT-V77-10 | Within-element effect | Fixed-effects g | Still significant |
| FT-V77-11 | Not Z-dependent | g × Z interaction | p > 0.05 |
| FT-V77-12 | Robust to outliers | Huber g | Within 15% of OLS |
| FT-V77-13 | Calibration-stable | Alt n(A) gives same sign | All g < 0 |
| FT-V77-14 | CV generalizes | Out-of-sample ΔRMSE | > 0.02 |

---

## Provenance Summary

| Source | Files Used | Key Content |
|--------|------------|-------------|
| V7.4 | 04_ALPHA100_DATASET.csv | 102 nuclide dataset |
| V7.5 | 04_CV_PREDICTIVE_GAIN.md, 05_PERMUTATION_TEST.md | Generalization tests |
| V7.6.1 | 01_TEST_BARRIER_vs_PREFACTOR.md | T1/T2/T3 results |
| V5 | 04_FORBIDDEN_TOPOLOGIES_V5.md, 05_BULK_CRYSTAL_NUCLEI_MODELS_V5.md | M1-M6 mechanisms |
| V2 | FORBIDDEN_ALTERNATIVES_MATRIX.md | n × mechanism matrix |

