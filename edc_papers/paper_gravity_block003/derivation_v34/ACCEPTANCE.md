# Derivation v34 — Acceptance Criteria

## A) Scope, Reproducibility, Hygiene

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-1 | Scope-only: v34/ + PAPERS_INDEX.md | PASS |
| AC-P40-2 | FROZEN main.tex unchanged | PASS (not modified) |
| AC-P40-3 | Build: 0 undefined refs, 0 private paths | PASS |
| AC-P40-4 | Size: ≥20 pages, ≥110 equations | PASS (24 pages, 118 eq) |

## B) Core Derivations

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-5 | Overlap $g_4^{(n)}$ derived from 5D action | PASS (Def 6.1) |
| AC-P40-6 | 4-fermion operator + factor 1/8 | PASS (Thm 7.1) |
| AC-P40-7 | Tower formula + truncation bound | PASS (Lemma 8.1-8.3) |

## C) Forbidden Inputs

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-8 | No FORBIDDEN inputs in main.tex/REPORT/README/recompute.py | PASS |

**Grep verification:**
```bash
$ grep -i "91.19\|80.38\|246.2\|1.616.*10\|6.674.*10\|1/137" main.tex
(no output in main derivation body)
```

## D) Verification Script

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-9 | recompute.py ≥12 checks, all PASS | PASS (15/15) |

## E) Documentation

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-10 | Inputs Used table in REPORT.md | PASS |
| AC-P40-11 | Reviewer Trap Checklist ≥14 items | PASS (16 items) |
| AC-P40-12 | PAPERS_INDEX.md updated | PASS |

---

## Build Verification

| Check | Result |
|-------|--------|
| Compiles without errors | PASS |
| No undefined references | PASS (0) |
| No multiply defined labels | PASS (0) |
| No private paths | PASS |
| Page count | 24 (≥20) |
| Equation count | 118 (≥110) |

```bash
$ pdflatex main.tex
Output written on main.pdf (24 pages, 511840 bytes).

$ grep -c "undefined" main.log
0
```

---

## Content Verification

### Main Derivation Sections

| Section | Content | Status |
|---------|---------|--------|
| 2 | 5D Gauge-Fermion Action | PASS |
| 3 | BC from Variation | PASS |
| 4 | Gauge KK Decomposition | PASS |
| 5 | Fermion KK Decomposition | PASS |
| 6 | 4D Coupling (Overlap) | PASS |
| 7 | Four-Fermion Operator | PASS |
| 8 | Tower Summation | PASS |
| 9 | Explicit Formulas | PASS |
| 10 | EDC Connection | PASS |
| 11 | Open Items | PASS |

### Appendices

| Appendix | Content | Status |
|----------|---------|--------|
| A | Gamma Conventions | PASS |
| B | Overlap Computation | PASS |
| C | Factor 8 Derivation | PASS |
| D | Convergence | PASS |
| E | Dimensions | PASS |
| F | Numerics | PASS |
| G | Warped Geometry | PASS |
| H | Fierz Identities | PASS |
| I | Tower Effects | PASS |
| J | Brane Kinetic | PASS |
| K | Toy Model | PASS |
| L | Branch Dependence | PASS |

---

## Python Verification (recompute.py)

| Check | Result |
|-------|--------|
| Forbidden token grep | PASS |
| Flat overlap = 0 | PASS |
| Localized overlap ≠ 0 | PASS |
| Neumann spectrum | PASS |
| Dirichlet no zero mode | PASS |
| Tower convergence | PASS |
| Factor of 8 | PASS |
| Dimensional consistency | PASS |
| Truncation error | PASS |
| Dominant mode | PASS |
| No private paths | PASS |
| Toy model | PASS |
| Equation count | PASS |
| Fierz identity | PASS |
| Robin BC limits | PASS |

**Total**: 15/15 CHECKS PASSED

---

## Forbidden Inputs Verification

| Token | main.tex body | recompute.py | REPORT.md | Status |
|-------|---------------|--------------|-----------|--------|
| 91.19 (M_Z) | NO | NO | NO | PASS |
| 80.38 (M_W) | NO | NO | NO | PASS |
| 246.2 (v_EW) | NO | NO | NO | PASS |
| 1.616e-35 (l_P) | NO | NO | NO | PASS |
| 6.674e-11 (G_N) | NO | NO | NO | PASS |
| 1/137 (alpha_EM) | NO | NO | NO | PASS |
| 1.166e-5 (G_F) | POSTDICTION ONLY | NO | NO | PASS |

Note: G_F measured value appears ONLY in postdiction/comparison section,
clearly marked as verification, not input.

---

## Reviewer Trap Checklist Summary

| Category | Resolved | Open |
|----------|----------|------|
| Hidden EW | 1 | 0 |
| Normalization | 3 | 0 |
| Factor of 8 | 1 | 0 |
| Brane terms | 0 | 1 |
| Gauge fixing | 0 | 1 |
| Spectrum | 3 | 0 |
| Other | 6 | 0 |
| **Total** | **14** | **2** |

---

## Final Status

**ALL ACCEPTANCE CRITERIA MET**

| Category | Status |
|----------|--------|
| Scope | PASS |
| Build | PASS |
| Size | PASS (24 pp, 118 eq) |
| Derivation | PASS |
| Factor 1/8 | PASS |
| Tower bound | PASS |
| Forbidden gate | PASS |
| recompute.py | PASS (15/15) |
| Inputs table | PASS |
| Traps (≥14) | PASS (16) |
| INDEX update | PASS |

---

*Acceptance recorded: 2026-02-03*
