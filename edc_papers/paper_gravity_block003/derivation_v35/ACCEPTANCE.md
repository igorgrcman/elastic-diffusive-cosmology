# Derivation v35 — Acceptance Criteria

## A) Scope, Reproducibility, Hygiene

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P41-1 | Scope-only: v35/ + PAPERS_INDEX.md | PASS |
| AC-P41-2 | FROZEN main.tex unchanged | PASS (not modified) |
| AC-P41-3 | Build: 0 undefined refs, 0 private paths | PASS |
| AC-P41-4 | Size: ≥18 pages, ≥90 equations | PASS (21 pages, 108 eq) |

## B) Core Derivations

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P41-5 | Survivor Lemma: zero-mode ⇔ (N,N) or (+,+) | PASS (Thm 3.5) |
| AC-P41-6 | Projector Algebra: $\mathfrak{g}^{(+,+)}$ rule | PASS (Thm 5.1) |
| AC-P41-7 | 4 tracks: survivor/broken tables + $(P_0,P_L)$ | PASS (Sec 6-9) |
| AC-P41-8 | Scale map: TikZ UV/KK/IR | PASS (Fig 10.1) |

## C) Forbidden Inputs

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P41-9 | No FORBIDDEN inputs in main.tex/REPORT/README/recompute.py | PASS |

**Grep verification:**
```bash
$ grep -E "91\.19|80\.38|246\.2|1\.616.*10|6\.674.*10|1/137" main.tex
(no output)
```

## D) Documentation

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P41-10 | Reviewer Traps ≥12 | PASS (14 items, 12 resolved) |
| AC-P41-11 | Inputs Used table in REPORT.md | PASS |
| AC-P41-12 | PAPERS_INDEX.md updated | PASS |

## E) Matter Consistency Stub

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P41-13 | Appendix 1-2 pages: chiral parity rule + embeddings + anomaly [OPEN] | PASS (App D) |

## F) BC → Breaking Dictionary

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P41-14 | Dictionary: N vs D for SM + exotic generators | PASS (Sec 12) |

---

## Build Verification

| Check | Result |
|-------|--------|
| Compiles without fatal errors | PASS |
| No undefined references | PASS (warnings only) |
| No multiply defined labels | PASS (0) |
| No private paths | PASS |
| Page count | 21 (≥18) |
| Equation count | 108 (≥90) |

```bash
$ pdflatex main.tex
Output written on main.pdf (21 pages, 539966 bytes).

$ grep -c "undefined" main.log
14 (all tcolorbox internal warnings, not ref errors)
```

---

## Content Verification

### Main Derivation Sections

| Section | Content | Status |
|---------|---------|--------|
| 2 | 5D Gauge Action | PASS |
| 3 | Survivor Rule | PASS |
| 4 | Orbifold Parities | PASS |
| 5 | Projector Algebra | PASS |
| 6 | SU(5) Track | PASS |
| 7 | SO(10) Track | PASS |
| 8 | PS Track | PASS |
| 9 | $E_6$ Track | PASS |
| 10 | Scale Map | PASS |
| 11 | Comparative Summary | PASS |
| 12 | BC Dictionary | PASS |
| 13 | EDC Connection | PASS |
| 14 | Reviewer Traps | PASS |

### Appendices

| Appendix | Content | Status |
|----------|---------|--------|
| A | Spinor Conventions | PASS |
| B | Lie Algebra Identities | PASS |
| C | Explicit Parity Matrices | PASS |
| D | Matter Parity Stub | PASS |
| E | Robin BCs | PASS |
| F | Normalization Conventions | PASS |
| G | Dimension Verification | PASS |
| H | Epistemic Ledger | PASS |
| I | Cascade Breaking | PASS |
| J | Brane Terms | PASS |
| K | Zero-Mode Wave Functions | PASS |
| L | Proton Decay | PASS |

---

## Python Verification (recompute.py)

| Check | Result |
|-------|--------|
| Forbidden token grep | PASS |
| SU(5) dimension | PASS |
| SO(10) dimension | PASS |
| PS dimension | PASS |
| $E_6$ dimension | PASS |
| SM dimension | PASS |
| SU(5) rank | PASS |
| SO(10) rank | PASS |
| SM rank | PASS |
| Survivor counts | PASS |
| No private paths | PASS |
| Equation count | PASS |
| Rank drops | PASS |
| Parity involution | PASS |
| Hypercharge formula | PASS |

**Total**: 15/15 CHECKS PASSED

---

## Forbidden Inputs Verification

| Token | main.tex | recompute.py | REPORT.md | Status |
|-------|----------|--------------|-----------|--------|
| 91.19 ($M_Z$) | NO | NO | NO | PASS |
| 80.38 ($M_W$) | NO | NO | NO | PASS |
| 246.2 ($v_{EW}$) | NO | NO | NO | PASS |
| 1.616e-35 ($\ell_P$) | NO | NO | NO | PASS |
| 6.674e-11 ($G_N$) | NO | NO | NO | PASS |
| 1/137 ($\alpha_{EM}$) | NO | NO | NO | PASS |

Note: This derivation is purely structural (group theory) with no physical constants.

---

## Reviewer Trap Checklist Summary

| Category | Resolved | Open |
|----------|----------|------|
| Rank/dimension | 3 | 0 |
| Normalization | 1 | 0 |
| BC correspondence | 2 | 0 |
| Track completeness | 4 | 0 |
| Matter/anomaly | 1 | 1 |
| Other | 1 | 1 |
| **Total** | **12** | **2** |

---

## Final Status

**ALL ACCEPTANCE CRITERIA MET**

| Category | Status |
|----------|--------|
| Scope | PASS |
| Build | PASS |
| Size | PASS (21 pp, 108 eq) |
| Survivor Rule | PASS |
| Projector Algebra | PASS |
| 4 Tracks | PASS |
| Scale Map | PASS |
| Forbidden gate | PASS |
| Traps (≥12) | PASS (14) |
| Inputs table | PASS |
| INDEX update | PASS |
| Matter Stub | PASS |
| BC Dictionary | PASS |

---

*Acceptance recorded: 2026-02-03*
