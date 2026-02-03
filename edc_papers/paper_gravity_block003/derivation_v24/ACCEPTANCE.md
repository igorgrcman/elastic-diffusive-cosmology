# Derivation v24 — Acceptance Criteria

## Required Checks (AC-P32-*)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P32-1 | Only derivation_v24/ modified/created | ✅ PASS |
| AC-P32-2 | FROZEN main.tex MD5 = e592a943... | ✅ PASS |
| AC-P32-3 | PDF builds, 0 undefined refs/cites, 0 private paths | ✅ PASS |
| AC-P32-4 | ≥ 10 pages | ✅ PASS (10 pages) |
| AC-P32-5 | ≥ 40 equation environments | ✅ PASS (48) |
| AC-P32-6 | recompute.py generates same numbers as main.tex | ✅ PASS |
| AC-P32-7 | π-map PASS (algebraic identity) | ✅ PASS |
| AC-P32-8 | Planck-map PASS (8π)^{1/3} | ✅ PASS |
| AC-P32-9 | Export name correct | ✅ PASS |

## Build Verification

| Check | Result |
|-------|--------|
| Compiles without errors | ✅ |
| No undefined references | ✅ |
| No undefined citations | ✅ |
| No private paths in PDF | ✅ |

## Python Verification (recompute.py)

| Check | Expected | Computed | Status |
|-------|----------|----------|--------|
| R_ξ^canon | 6.80e-18 m | 6.798e-18 m | ✅ PASS |
| M_5 (reduced) | 5.6e12 GeV | 5.56e12 GeV | ✅ PASS |
| M_5 (original) | 1.6e13 GeV | 1.63e13 GeV | ✅ PASS |
| π × R_ξ^old = R_ξ^canon | exact | <1e-10 | ✅ PASS |
| π^{-1/3} × M_5^old = M_5^canon | 0.683 | 0.683 | ✅ PASS |
| M_5^orig / M_5^red | 2.924 | 2.929 | ✅ PASS |
| δM_5/M_5 | 1.1e-5 | 1.07e-5 | ✅ PASS |

## Content Verification

| Section | Content | Status |
|---------|---------|--------|
| §1 | Ground truth inputs table | ✅ |
| §2 | Canonical calculations (step-by-step) | ✅ |
| §3 | Old ↔ Canonical π-map audit | ✅ |
| §4 | Error propagation | ✅ |
| §5 | Regression table (v15-v24) | ✅ |
| §6 | Audit summary table | ✅ |
| App A | Dimensional analysis | ✅ |
| App B | Python script reference | ✅ |

## Numerical Values Reproduced

| Quantity | v23 Value | v24 Reproduced |
|----------|-----------|----------------|
| R_ξ^canon | 6.80e-18 m | 6.798e-18 m |
| M_5^red | 5.6e12 GeV | 5.56e12 GeV |
| M_5^orig | 1.6e13 GeV | 1.63e13 GeV |
| δM_5/M_5 | 1.1e-5 | 1.07e-5 |

## Final Status

**✅ ALL ACCEPTANCE CRITERIA MET**

---

*Acceptance recorded: 2026-02-03*
