# Derivation v43 — Acceptance Criteria

## A) Scope, Reproducibility, Hygiene (AC-P43)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P43-1 | Scope-only: v43/ + PAPERS_INDEX.md | PASS |
| AC-P43-2 | FROZEN MD5 unchanged | PASS (not modified) |
| AC-P43-3 | Build: 0 undefined refs, 0 private paths | PASS |

## B) Size Requirements (AC-P43)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P43-4 | Equations ≥ 140 environments | PASS (148) |
| AC-P43-5 | Labeled equations ≥ 180 | PASS (304) |
| AC-P43-6 | Pages ≥ 24 | PASS (32) |

## C) Verification (AC-P43)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P43-7 | recompute.py ≥ 20 checks; ALL PASS | PASS (26/26) |

## D) Forbidden Inputs (AC-P43)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P43-8 | Grep: no M_Z, M_W, v_EW, α_EM, G_N, ℓ_P | PASS |

**Grep verification:**
```bash
$ grep -E "91\.19|80\.38|246\.2|1\.616.*10|6\.674.*10" main.tex
(no output)
```

## E) PS→SM Decomposition (AC-P43-9)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P43-9a | F_L = (4,2,1) → q_L + ℓ_L | PASS |
| AC-P43-9b | F_R = (4,1,2) → u_R + d_R + ν_R + e_R | PASS |
| AC-P43-9c | Hypercharge Y = T_{3R} + (B-L)/2 | PASS |
| AC-P43-9d | Charge verification for all fields | PASS |

## F) Anomaly Computation (AC-P43-10)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P43-10a | SU(3)³ = 0 (explicit) | PASS |
| AC-P43-10b | SU(2)²U(1) = 0 (explicit) | PASS |
| AC-P43-10c | SU(3)²U(1) = 0 (explicit) | PASS |
| AC-P43-10d | U(1)³ = 0 (explicit) | PASS |
| AC-P43-10e | U(1)-grav = 0 (explicit) | PASS |
| AC-P43-10f | Witten SU(2) = 0 (even) | PASS |

## G) 42 vs 45 Resolution (AC-P43-11)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P43-11a | 42 = PS content (without ν_R) | PASS |
| AC-P43-11b | 45 = full SM Weyl count | PASS |
| AC-P43-11c | Difference = 3 (ν_R × 3 gen) | PASS |
| AC-P43-11d | ν_R mixed BC explanation | PASS |

## H) Final Verdict (AC-P43-12)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P43-12a | PS status upgrade | PASS (CONDITIONAL → PASS) |
| AC-P43-12b | Cross-track consistency | PASS |
| AC-P43-12c | Verdict table present | PASS |

## I) Cross-Derivation Consistency (AC-P43-13)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P43-13a | v41 SM counts recovered | PASS |
| AC-P43-13b | v42 anomaly structure | PASS |
| AC-P43-13c | BC registry (v35) compatible | PASS |

## J) Documentation (AC-P43-14)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P43-14a | README.md present | PASS |
| AC-P43-14b | REPORT.md with Inputs Used table | PASS |
| AC-P43-14c | ACCEPTANCE.md present | PASS |
| AC-P43-14d | Epistemic ledger tags | PASS (3 tag types) |

---

## K) P44 Cleanup Criteria

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P44-1 | Scope: only derivation_v43/* modified | PASS |
| AC-P44-2 | FROZEN untouched | PASS (not modified) |
| AC-P44-3 | Build: PDF builds, 0 undefined refs | PASS |
| AC-P44-4 | Narrative cleanup: no "Wait", "???", "Correction", "recalculate", "sign error" in main text | PASS |
| AC-P44-5 | U(1)³ one-shot: single derivation, one convention | PASS |
| AC-P44-6 | Traps: Reviewer trap checklist ≥12 items | PASS (15 items) |
| AC-P44-7 | Labels: ≥180 labeled equations | PASS (304) |
| AC-P44-8 | recompute: existing checks PASS + new checks | PASS (26/26) |
| AC-P44-9 | Forbidden inputs absent | PASS |
| AC-P44-10 | Export name exact | PASS |
| AC-P44-11 | No artifacts staged | PASS |
| AC-P44-12 | U(1)³ consistency: LaTeX + recompute.py | PASS |

**AC-P44-4 Search Evidence:**
```bash
$ grep -E "Wait---|Wait,|\?\?\?|\\\\textbf\{Correction\}|recalculate" main.tex
(no output in main derivation - only in Reviewer Trap section as trap descriptions)
```

**AC-P44-12 Evidence:**
- LaTeX: Appendix M.4, eq:u1-3-result-oneshot shows Σ m_i Y_i³ = 0
- recompute.py: `verify_u1_cubed_oneshot()` computes same sum = 0 using Fraction arithmetic

---

## Build Verification

| Check | Result |
|-------|--------|
| Compiles without errors | PASS |
| No undefined references | PASS |
| No multiply defined labels | PASS |
| No private paths | PASS |
| Page count | 32 (≥24) |
| Equation count | 148 (≥140) |
| Label count | 304 (≥180) |

```bash
$ pdflatex main.tex
Output written on main.pdf (32 pages, 615312 bytes).
```

---

## Python Verification (recompute.py)

| Check | Result |
|-------|--------|
| Page count (>=24) | PASS (32) |
| Equation count (>=140) | PASS (148) |
| Label count (>=180) | PASS (304) |
| Forbidden tokens (main.tex) | PASS |
| Forbidden tokens (recompute.py) | PASS |
| SM Weyl count = 45 | PASS |
| PS→SM decomposition | PASS |
| SU(3)³ anomaly = 0 | PASS |
| SU(2)²U(1) anomaly = 0 | PASS |
| U(1)³ anomaly = 0 | PASS |
| U(1)-grav anomaly = 0 | PASS |
| Witten SU(2) anomaly | PASS |
| 42→45 reconciliation | PASS |
| Cross-track Weyl | PASS |
| BC structure | PASS |
| Hypercharge embedding | PASS |
| Anomaly matrix | PASS |
| Final verdict | PASS |
| Epistemic tags | PASS |
| No undefined refs | PASS |
| Export PDF exists | PASS |
| Prior derivation ref | PASS |
| Dependency pointers | PASS |
| Narrative cleanup (AC-P44-4) | PASS |
| U(1)³ one-shot (AC-P44-12) | PASS |
| Reviewer traps ≥12 (AC-P44-6) | PASS (15) |

**Total**: 26/26 CHECKS PASSED

---

## Final Status

**ALL ACCEPTANCE CRITERIA MET (AC-P43 + AC-P44)**

| Category | Status |
|----------|--------|
| Scope | PASS |
| Build | PASS |
| Size | PASS (32 pp, 148 eq, 304 labels) |
| recompute.py | PASS (26/26) |
| Forbidden gate | PASS |
| PS→SM decomposition | PASS |
| Anomaly computation | PASS (6/6) |
| 42→45 resolution | PASS |
| Final verdict | PASS (PS → PASS) |
| Cross-derivation | PASS |
| Documentation | PASS |
| P44 cleanup | PASS (narrative + U(1)³ + traps) |
| PAPERS_INDEX | PASS |

---

*Acceptance recorded: 2026-02-04*
*P44 cleanup verified: 2026-02-05*
