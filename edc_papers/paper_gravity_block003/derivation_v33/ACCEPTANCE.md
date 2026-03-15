# Derivation v33 — Acceptance Criteria

## A) Scope, Reproducibility, Hygiene

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-1 | Scope-only: v33/ + PAPERS_INDEX.md | PASS |
| AC-P40-2 | Build integrity: 0 undefined refs | PASS |
| AC-P40-3 | Pages ≥ 24 | PASS (29 pages) |
| AC-P40-4 | Equation environments ≥ 140 | PASS (150) |
| AC-P40-5 | Labeled equations ≥ 80 | PASS (155) |
| AC-P40-6 | Export name exact | PASS |

## B) Forbidden Inputs + Dependency-Proof

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-7 | No forbidden tokens anywhere | PASS |
| AC-P40-8 | Inputs Used table (dependency-proof) | PASS |
| AC-P40-9 | Hard grep gate in recompute.py | PASS |

## C) Track M: Matter/Chirality/Higgs

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-M1 | 5D Dirac action + variation | PASS (Sec 2) |
| AC-P40-M2 | Chiral BC theorem with proof | PASS (Thm 3.1) |
| AC-P40-M3 | Mode decomposition + eigenvalue problem | PASS (Sec 4) |
| AC-P40-M4 | Zero mode profile + normalization | PASS (Lemma 4.1) |
| AC-P40-M5 | Anomaly Risk Matrix | PASS (Table 6.1) |
| AC-P40-M6 | Gauge-Higgs Unification skeleton | PASS (Prop 7.1) |
| AC-P40-M7 | Hosotani mechanism | PASS (Def 7.1) |
| AC-P40-M8 | Yukawa overlap formula | PASS (Thm 8.1) |
| AC-P40-M9 | BC Registry v33 ≥ 6 entries | PASS (10 entries) |

## D) Track R: RG/Matching/Running

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-R1 | Gauge matching formula boxed | PASS (Thm 10.1) |
| AC-P40-R2 | $I_{\text{gauge}}$ for flat/warped | PASS (Sec 10) |
| AC-P40-R3 | KK spectrum N/D/Robin | PASS (Sec 11) |
| AC-P40-R4 | $\mu_{\text{KK}}$ definition | PASS (Def 11.1) |
| AC-P40-R5 | Piecewise running formula | PASS (Thm 12.1) |
| AC-P40-R6 | Scale Regime Map TikZ | PASS (Fig 1) |
| AC-P40-R7 | Track-to-RG Dictionary | PASS (Table 14.1) |
| AC-P40-R8 | Hypercharge normalization | PASS (Sec 15) |
| AC-P40-R9 | Threshold corrections | PASS (Sec 16) |
| AC-P40-R10 | Reviewer Trap Checklist ≥ 16 | PASS (16 traps) |

## E) recompute.py

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-10 | ≥ 15 checks, all PASS | PASS (18/18) |
| AC-P40-11 | BC consistency checks | PASS |
| AC-P40-12 | Normalization checks | PASS |
| AC-P40-13 | KK gap checks | PASS |
| AC-P40-14 | Wilson line periodicity | PASS |
| AC-P40-15 | Dimensional consistency | PASS |
| AC-P40-16 | Hypercharge c_Y check | PASS |

## F) Dependency-Proof

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-17 | Inputs Used table complete | PASS |
| AC-P40-18 | All numeric values tagged | PASS |
| AC-P40-19 | No physics inputs used | PASS |

---

## Build Verification

| Check | Result |
|-------|--------|
| Compiles without errors | PASS |
| No undefined references | PASS (0) |
| No multiply defined | PASS (0) |
| No private paths | PASS |

```bash
$ pdflatex main.tex
Output written on main.pdf (29 pages, 686268 bytes).

$ grep -c "undefined" main.log
0
```

## Content Verification

### Track M Sections

| Section | Content | Status |
|---------|---------|--------|
| 2 | 5D Dirac Action | PASS |
| 3 | Chiral BCs | PASS |
| 4 | Zero Mode Condition | PASS |
| 5 | Warped Fermions | PASS |
| 6 | Anomaly Assessment | PASS |
| 7 | Gauge-Higgs ($A_5$) | PASS |
| 8 | Yukawa Overlap | PASS |
| 9 | BC Registry v33 | PASS |

### Track R Sections

| Section | Content | Status |
|---------|---------|--------|
| 10 | Gauge Coupling | PASS |
| 11 | KK Spectrum | PASS |
| 12 | Piecewise Running | PASS |
| 13 | Scale Regime Map | PASS |
| 14 | Track-RG Dictionary | PASS |
| 15 | Hypercharge | PASS |
| 16 | Matching Conditions | PASS |
| 17 | Reviewer Traps | PASS |

### Appendices

| Appendix | Content | Status |
|----------|---------|--------|
| A | Spinor Conventions | PASS |
| B | Mode Orthogonality | PASS |
| C | Wilson Line | PASS |
| D | Hosotani Details | PASS |
| E | Threshold Details | PASS |
| F | Robin BC Analysis | PASS |
| G | Group Theory | PASS |
| H | Beta Coefficients | PASS |
| I | Dimensions | PASS |
| J | Conservation Audit | PASS |
| K | Fermion Mode Detail | PASS |
| L | Warped Geometry | PASS |

## Python Verification (recompute.py)

| Check | Result |
|-------|--------|
| Forbidden token grep | PASS |
| Fermion BC consistency | PASS |
| Flat normalization | PASS |
| Exponential normalization | PASS |
| Neumann spectrum | PASS |
| Dirichlet spectrum | PASS |
| Wilson periodicity | PASS |
| Gauge matching dims | PASS |
| Yukawa matching dims | PASS |
| Hypercharge c_Y | PASS |
| Generator counts | PASS |
| Beta coefficients | PASS |
| KK scale definition | PASS |
| Warped localization | PASS |
| No private paths | PASS |
| SM anomaly cancel | PASS |
| Equation count | PASS |
| Labeled equations | PASS |

**Total**: 18/18 CHECKS PASSED

## Forbidden Inputs Verification

| Token | main.tex | recompute.py | REPORT.md | Status |
|-------|----------|--------------|-----------|--------|
| 91.19 (M_Z) | NO | NO | NO | PASS |
| 80.38 (M_W) | NO | NO | NO | PASS |
| 246.2 (v_EW) | NO | NO | NO | PASS |
| 1.616e-35 (l_P) | NO | NO | NO | PASS |
| 6.674e-11 (G_N) | NO | NO | NO | PASS |
| 1/137 (alpha_EM) | NO | NO | NO | PASS |

---

## Final Status

**ALL ACCEPTANCE CRITERIA MET**

---

*Acceptance recorded: 2026-02-03*
