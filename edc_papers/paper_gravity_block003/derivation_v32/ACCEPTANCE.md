# Derivation v32 — Acceptance Criteria

## A) Scope, Reproducibility, Hygiene

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-1 | Scope-only: v32/ + PAPERS_INDEX.md | PASS |
| AC-P40-2 | FROZEN main.tex MD5 unchanged | PASS (e592a943...) |
| AC-P40-3 | Build integrity: 0 undefined refs | PASS |
| AC-P40-4 | Pages >= 22 | PASS (26 pages) |
| AC-P40-5 | Equation environments >= 120 | PASS (126) |
| AC-P40-6 | Export name exact | PASS |

## B) Forbidden Inputs + Dependency-Proof

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-7 | No forbidden tokens anywhere | PASS |
| AC-P40-8 | Inputs Used table (dependency-proof) | PASS |
| AC-P40-9 | Hard grep gate in recompute.py | PASS |

## C) BC Registry

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-10 | BC Registry >= 4 field types | PASS (graviton, gauge, scalar, fermion) |
| AC-P40-11 | BC from action variation | PASS (Theorem 2.1) |

## D) Gauge Parent -> SM

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-12 | Explicit parent group | PASS (SU(5), SO(10), E_6) |
| AC-P40-13 | Generator Survival Matrix >= 12 | PASS (24+ for SU(5)) |
| AC-P40-14 | Closure proof | PASS (Theorems 7.1, 8.1) |
| AC-P40-15 | Count check | PASS (8+3+1=12) |

## E) Spectra + Gap Control

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-16 | Mode equations | PASS (Eq. 13) |
| AC-P40-17 | BC-dependent spectra | PASS (N/D/Robin) |
| AC-P40-18 | A_5 accounting | PASS (Section 11) |

## F) Coupling Bridges

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-19 | Gauge coupling bridge derived | PASS (Theorem 5.1) |
| AC-P40-20 | Subgroup mapping | PASS (Eq. 43-45) |
| AC-P40-21 | Dimensional audit | PASS (Lemma 5.1, App A) |

## G) Scale-Change Rule

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-22 | Scale Regime Map TikZ | PASS (Figure 1) |
| AC-P40-23 | Explicit matching conditions | PASS (Eq. 29-30) |

## H) Reviewer Hardening

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-24 | Epistemic ledger table | PASS (Section 14) |
| AC-P40-25 | Traps >= 12 gauge-specific | PASS (14 traps) |
| AC-P40-26 | Anomaly sanity note | PASS ([OPEN] noted for E_6) |

## I) recompute.py

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-27 | >= 12 checks, all PASS | PASS (16/16) |
| AC-P40-28 | Numerics table | PASS (Inputs Used) |

## J) Indexing + Git

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-29 | PAPERS_INDEX updated | PASS |
| AC-P40-30 | Clean git, proper commit | PASS |

## Pati-Salam Specific (from Addendum)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P40-11-PS | PS track with embedding, BC, survival, Y formula | PASS |
| AC-P40-12-PS | 45=21+24 count | PASS |
| AC-P40-13-PS | 2 PS checks in recompute.py | PASS |

---

## Build Verification

| Check | Result |
|-------|--------|
| Compiles without errors | PASS |
| No undefined references | PASS (0) |
| No multiply defined | PASS (0) |
| No private paths | PASS |

## Content Verification

| Section | Content | Status |
|---------|---------|--------|
| 1 | Reader Contract | PASS |
| 2 | 5D Action + BC Derivation | PASS |
| 3 | KK Spectra | PASS |
| 4 | Scale Regime Map | PASS |
| 5 | Gauge Coupling Bridge | PASS |
| 6 | BC Registry | PASS |
| 7 | Track S: SU(5) | PASS |
| 8 | Track O: SO(10) | PASS |
| 9 | Track P: Pati-Salam | PASS |
| 10 | Track E: E_6 | PASS |
| 11 | A_5 Accounting | PASS |
| 12 | Unified Couplings | PASS |
| 13 | Internal Closure | PASS |
| 14 | Epistemic Ledger | PASS |
| 15 | Reviewer Traps | PASS |
| 16 | Conclusions | PASS |
| App A-K | Extended | PASS |

## Python Verification (recompute.py)

| Check | Result |
|-------|--------|
| Forbidden token grep | PASS |
| SU(5) count | PASS |
| SO(10) count | PASS |
| PS count | PASS |
| PS->SM count | PASS |
| E_6 count | PASS |
| Neumann zero mode | PASS |
| Dirichlet no zero | PASS |
| Robin spectrum | PASS |
| Gap monotonicity | PASS |
| Dimensions | PASS |
| Hypercharge c_Y | PASS |
| Scale map present | PASS |
| Algebra closure | PASS |
| No private paths | PASS |
| Equation count | PASS |

**Total**: 16/16 CHECKS PASSED

## Forbidden Inputs Verification

| Token | main.tex | recompute.py | REPORT.md | Status |
|-------|----------|--------------|-----------|--------|
| M_Z (91.19) | NO | NO | NO | PASS |
| M_W (80.38) | NO | NO | NO | PASS |
| v_EW (246.2) | NO | NO | NO | PASS |
| l_P | NO | NO | NO | PASS |
| G_N | NO | NO | NO | PASS |
| alpha_EM | NO | NO | NO | PASS |

---

## Final Status

**ALL ACCEPTANCE CRITERIA MET**

---

*Acceptance recorded: 2026-02-03*
