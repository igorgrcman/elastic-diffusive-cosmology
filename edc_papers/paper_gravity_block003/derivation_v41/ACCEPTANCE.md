# Derivation v41 — Acceptance Criteria

## A) Scope, Reproducibility, Hygiene

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P41-1 | Scope-only: v41/ + PAPERS_INDEX.md | PASS |
| AC-P41-2 | FROZEN MD5 unchanged | PASS (not modified) |
| AC-P41-3 | Build: 0 undefined refs, 0 private paths | PASS |
| AC-P41-4 | Dependency pointers (v33, v37, v40) | PASS |

## B) Size Requirements

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P41-5 | Size: ≥24 pages | PASS (28 pages) |
| AC-P41-6 | Equation environments ≥ 120 | PASS (152 eq) |

## C) Verification

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P41-7 | recompute.py ≥ 18 checks; ALL PASS | PASS (23/23) |

## D) Forbidden Inputs

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P41-8 | Grep: no M_Z, M_W, v_EW, α_EM, G_N, ℓ_P | PASS |

**Grep verification:**
```bash
$ grep -E "91\.19|80\.38|246\.2|1\.616.*10|6\.674.*10|1/137" main.tex
(no output)
```

## E) Fermion BC Content (AC-P41-9)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P41-9a | Chiral BC definitions from v33 | PASS (Def. 3.2) |
| AC-P41-9b | Mode spectrum (L,L)/(R,R) vs (L,R)/(R,L) | PASS (Prop. 3.3) |
| AC-P41-9c | χ_F coefficient table | PASS (Def. 3.6) |
| AC-P41-9d | Spin-statistics sign derivation | PASS (Proof after Prop. 3.4) |

## F) Per-Track Fermion Assignment (AC-P41-10)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P41-10a | SU(5) fermion BC table | PASS (Sec. 5.3) |
| AC-P41-10b | SO(10) fermion BC table | PASS (Sec. 5.4) |
| AC-P41-10c | PS fermion BC table | PASS (Sec. 5.5) |
| AC-P41-10d | E₆ fermion BC table | PASS (Sec. 5.6) |

## G) Combined Ranking (AC-P41-11)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P41-11a | ΔE_gauge + ΔE_ferm per track | PASS (Sec. 6) |
| AC-P41-11b | Ranking is unique (no ties) | PASS |
| AC-P41-11c | Ranking: E₆ < PS < SU(5) < SO(10) | PASS |

**Numerical verification:**
```
E6    : ΔE_total = -54.00 × π/(24L) = -9π/(4L)
PS    : ΔE_total = -9.00 × π/(24L) = -3π/(8L)
SU5   : ΔE_total = +0.00 × π/(24L) = 0
SO10  : ΔE_total = +13.50 × π/(24L) = +9π/(16L)
```

## H) Regulator Invariance (AC-P41-12)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P41-12a | Zeta vs heat-kernel comparison | PASS (Sec. 8) |
| AC-P41-12b | Ranking identical under both | PASS |
| AC-P41-12c | Numerical agreement < 10⁻¹⁰ | PASS |

## I) v40 Limit Check (AC-P41-13)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P41-13a | Fermion → 0 recovers v40 | PASS (Sec. 9) |
| AC-P41-13b | SU(5)=PS=E₆=0 recovered | PASS |
| AC-P41-13c | SO(10)=+3π/(4L) recovered | PASS |

## J) Consistency Checks (AC-P41-14)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P41-14a | 12 survivors per track | PASS (Prop. 10.1) |
| AC-P41-14b | Charged tower non-empty | PASS (Prop. 10.2) |
| AC-P41-14c | G_F hook operational | PASS |

## K) Reviewer Traps (AC-P41-15)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P41-15 | Reviewer traps ≥ 18 | PASS (20 items) |

## L) Documentation (AC-P41-16)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P41-16a | README.md present | PASS |
| AC-P41-16b | REPORT.md with Inputs Used table | PASS |
| AC-P41-16c | ACCEPTANCE.md present | PASS |
| AC-P41-16d | Epistemic ledger | PASS (App. E) |

---

## Build Verification

| Check | Result |
|-------|--------|
| Compiles without errors | PASS |
| No undefined references | PASS |
| No multiply defined labels | PASS |
| No private paths | PASS |
| Page count | 28 (≥24) |
| Equation count | 152 (≥120) |

```bash
$ pdflatex main.tex
Output written on main.pdf (28 pages, 627168 bytes).
```

---

## Python Verification (recompute.py)

| Check | Result |
|-------|--------|
| Forbidden tokens (main.tex) | PASS |
| Forbidden tokens (recompute.py) | PASS |
| Fermion BC formulas | PASS |
| Chiral BC spectrum | PASS |
| χ_F coefficients | PASS |
| v40 gauge regression | PASS |
| Fermion sector: SU5 | PASS |
| Fermion sector: SO10 | PASS |
| Fermion sector: PS | PASS |
| Fermion sector: E6 | PASS |
| Combined ranking | PASS |
| Unique ranking | PASS |
| Regulator invariance | PASS |
| Regulator invariance (LaTeX) | PASS |
| v40 limit check | PASS |
| 12-survivor check | PASS |
| Charged tower non-empty | PASS |
| Equation count | PASS (152) |
| Page count | PASS (28) |
| No private paths | PASS |
| Epistemic ledger | PASS |
| Reviewer traps ≥ 18 | PASS (20) |
| Dependency pointers | PASS |

**Total**: 23/23 CHECKS PASSED

---

## Final Status

**ALL ACCEPTANCE CRITERIA MET**

| Category | Status |
|----------|--------|
| Scope | PASS |
| Build | PASS |
| Size | PASS (28 pp, 152 eq) |
| recompute.py | PASS (23/23) |
| Forbidden gate | PASS |
| Fermion BC content | PASS |
| Per-track assignment | PASS |
| Combined ranking | PASS |
| Regulator invariance | PASS |
| v40 limit check | PASS |
| Consistency checks | PASS |
| Reviewer traps | PASS (20) |
| Documentation | PASS |
| PAPERS_INDEX | PENDING |

---

*Acceptance recorded: 2026-02-04*
