# P62 / Derivation v58: Λ_QCD Extraction — Acceptance Criteria

## AC-P62 Checklist

### Build & Scope Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| AC-P62-1 | Scope-only: only derivation_v58/ + PAPERS_INDEX.md touched | PASS |
| AC-P62-2 | Build clean: 0 undefined refs, 0 multiply-defined labels | PASS |
| AC-P62-3 | Pages ≥ 26 | PASS (29 pages) |
| AC-P62-4 | Equation environments ≥ 180 | PASS (180+) |
| AC-P62-5 | Labels ≥ 260 | PASS (278) |

### Firewall Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| AC-P62-6 | Forbidden patterns only in QUARANTINED sections | PASS |
| AC-P62-7 | No bare experimental numbers outside quarantine | PASS |
| AC-P62-8 | No experimental values in title | PASS |
| AC-P62-9 | No experimental values in abstract | PASS |
| AC-P62-10 | Layer A declared unchanged | PASS |

### Verification Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| AC-P62-11 | recompute.py checks ≥ 57 and ALL PASS | PASS (57/57) |
| AC-P62-12 | SoT hash lock present and verified | PASS |
| AC-P62-13 | Two-route Λ: Λ₁ = Λ₂ within tolerance | PASS |
| AC-P62-14 | Threshold invariance: T1 = T2 within tolerance | PASS |

### No-Fit Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| AC-P62-15 | No-Fit policy explicitly stated | PASS |
| AC-P62-16 | σ̃ swept, not fitted | PASS |
| AC-P62-17 | No optimizer/minimizer code | PASS |

### Content Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| AC-P62-18 | Route Λ₁ (1-loop) defined | PASS |
| AC-P62-19 | Route Λ₂ (2-loop/numeric) defined | PASS |
| AC-P62-20 | Policy T1 (step-function) defined | PASS |
| AC-P62-21 | Policy T2 (matched continuity) defined | PASS |
| AC-P62-22 | QUARANTINED inputs table ≥ 8 | PASS (10) |
| AC-P62-23 | Threat model present | PASS |
| AC-P62-24 | No Backflow Theorem v2 | PASS |
| AC-P62-25 | Reviewer traps ≥ 10 | PASS (15) |
| AC-P62-26 | [Q] tags ≥ 20 | PASS (50+) |

### Indexing Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| AC-P62-27 | PAPERS_INDEX.md updated with v58 row + hash | PASS |
| AC-P62-28 | Export filename exact | PASS |

---

## Verification Summary

```
Total: 57/57 CHECKS PASSED
All checks PASS

v57 hash verified: fadd71e1e0adfa69
v58 SoT hash: 67ce04beef9f7f79
```

---

## Document Statistics

| Metric | Value | Requirement | Status |
|--------|-------|-------------|--------|
| Pages | 29 | ≥26 | PASS |
| Equations | 180+ | ≥180 | PASS |
| Labels | 278 | ≥260 | PASS |
| Checks | 57 | ≥57 | PASS |
| Reviewer Traps | 15 | ≥10 | PASS |
| Forbidden Hits | 0 | 0 | PASS |
| [Q] Tags | 50+ | ≥20 | PASS |

---

## Files Delivered

| File | Description |
|------|-------------|
| main.tex | LaTeX source (29 pages) |
| main.pdf | Compiled document |
| recompute.py | Verification script (57 checks) |
| REPORT.md | Detailed report |
| README.md | Documentation |
| ACCEPTANCE.md | This file |
| EDC_BLOCK004_DERIVATION_V58_LAYERB_LAMBDAQCD_EXTRACTION_TWOROUTE_QUARANTINED.pdf | Export PDF |

---

## Key Results (Summary)

```
L_B ∩ L_A = ∅                              [NO BACKFLOW v2]
Route Λ₁: 1-loop analytic inversion        [VERIFIED]
Route Λ₂: Numeric/2-loop                   [VERIFIED]
|Λ₁ - Λ₂| / Λ₁ < 0.15                      [TWO-ROUTE CONSISTENT]
Policy T1: Step-function decoupling        [VERIFIED]
Policy T2: Matched continuity              [VERIFIED]
|Λ^(T1) - Λ^(T2)| / Λ^(T1) < 0.05         [THRESHOLD INVARIANT]
σ̃ is SWEPT, not FITTED                    [NO-FIT POLICY]
All values tagged [Q]                       [QUARANTINED]
```

---

## Acceptance Decision

**ACCEPTED** — All AC-P62 criteria satisfied.

Date: 2026-02-07
