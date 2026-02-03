# Derivation v29 — Acceptance Criteria

## Required Checks (AC-P37-*)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P37-1 | Only derivation_v29/ and PAPERS_INDEX modified | PASS |
| AC-P37-2 | FROZEN main.tex MD5 = e592a943... unchanged | PASS |
| AC-P37-3 | PDF builds, 0 undefined refs, 0 private paths | PASS |
| AC-P37-4 | Pages ≥ 14 | PASS (18 pages) |
| AC-P37-5 | Equation environments ≥ 80 | PASS (91) |
| AC-P37-6 | β derivation Route A (direct) | PASS (§3) |
| AC-P37-7 | β derivation Route B (via spectral) | PASS (§4) |
| AC-P37-8 | Control Law box | PASS (§5) |
| AC-P37-9 | Epistemic Ledger table | PASS (§7, tab:ledger) |
| AC-P37-10 | Reviewer Trap Checklist (10 traps) | PASS (§8) |
| AC-P37-11 | Units & Dimensional Audit appendix | PASS (Appendix A) |
| AC-P37-12 | Uncertainty/Error Budget section | PASS (§9) |
| AC-P37-13 | Dependency & Circularity Audit | PASS (§10, fig:dependency) |

## Build Verification

| Check | Result |
|-------|--------|
| Compiles without errors | PASS |
| No undefined references | PASS (0) |
| No multiply defined | PASS (0) |
| No private paths in PDF | PASS |

## Python Verification (recompute.py)

| Check | Expected | Computed | Status |
|-------|----------|----------|--------|
| β Route A = Route B | match | 4.89×10⁻³⁶ | PASS |
| Planck map ratio | √(8π) = 5.01 | 5.0133 | PASS |
| M₅ map ratio | (8π)^(1/3) = 2.93 | 2.9292 | PASS |
| L = πR consistency | 0 | 0 | PASS |
| Neumann limit x₁ | π | 3.141593 | PASS |
| Dirichlet limit x₁ | π/2 | 1.570798 | PASS |
| Monotonicity | decreasing | verified | PASS |
| Residuals | < 10⁻¹⁰ | all pass | PASS |
| Dimension checks | PASS | PASS | PASS |
| Uncertainty δβ/β | computed | 3.2×10⁻⁵ | PASS |

**Total**: 10/10 CHECKS PASSED

## AC-P37-11: Units & Dimensional Audit

| Requirement | Location | Status |
|-------------|----------|--------|
| SI dimensions table | Appendix A, tab:SI-dimensions | PASS |
| SI→natural conversion | Appendix A, §A.2 | PASS |
| Consistency check 1: [β]=1 | eq:dim-check-beta | PASS |
| Consistency check 2: [b]=1 | eq:dim-check-b | PASS |
| Consistency check 3: [m_gap]=M | eq:dim-check-mgap | PASS |
| Consistency check 4: [σL³]=[ℏc] | eq:dim-check-anchor | PASS |
| Consistency check 5: bridge | eq:dim-check-bridge | PASS |
| recompute.py DIMENSION CHECK | output | PASS |

## AC-P37-12: Uncertainty Budget

| Requirement | Location | Status |
|-------------|----------|--------|
| ℏ exact by SI 2019 | §9.1, item 1 | PASS |
| Uncertainty propagation | §9.2, eq:beta-uncertainty | PASS |
| δβ/β numeric value | eq:beta-uncertainty-numeric | PASS |
| Dominant contributor identified | §9.3 | PASS |
| δβ/β in main.tex | 3.2×10⁻⁵ | PASS |
| δβ/β in recompute.py | 3.18×10⁻⁵ | PASS |
| Agreement within 1% | |3.2-3.18|/3.2 = 0.6% | PASS |

## AC-P37-13: Dependency & Circularity Audit

| Requirement | Location | Status |
|-------------|----------|--------|
| TikZ dependency graph | §10.1, fig:dependency | PASS |
| β Form 1 (L open) | eq:beta-L-open | PASS |
| β Form 2 (L identified) | eq:beta-L-identified | PASS |
| Tags distinct | [BL] vs [I]+[BL] | PASS |
| "No double counting" proof | §10.2 | PASS |
| TRAP-6 equation mapping | eq:beta-L-open, eq:beta-L-identified | PASS |
| TRAP-7 equation mapping | Control Law eqs + Route A/B | PASS |

## Trap-to-Equation Mapping

| Trap | Key Equations |
|------|---------------|
| TRAP-1 | eq:beta-dim-check, eq:dim-check-beta |
| TRAP-2 | eq:hbar-exact, §9.1 |
| TRAP-3 | conv:length-dict, eq:L-def, eq:R-def, eq:Rxi-def |
| TRAP-4 | eq:Mpl-map, eq:M5-map, eq:beta-planck-change |
| TRAP-5 | tab:ledger, §8 TRAP-5 |
| TRAP-6 | eq:beta-L-open, eq:beta-L-identified |
| TRAP-7 | sec:route-a, sec:route-b, Control Law |
| TRAP-8 | eq:action-brane-mass, eq:robin-bc |
| TRAP-9 | §8 TRAP-9 |
| TRAP-10 | sec:numerical, tab:residuals, tab:monotonicity |

## Content Verification

| Section | Content | Status |
|---------|---------|--------|
| §1 | Conventions & Units | PASS |
| §2 | Definition of β | PASS |
| §3 | Route A: Direct Derivation | PASS |
| §4 | Route B: Via Spectral Equation | PASS |
| §5 | Control Law Box | PASS |
| §6 | Robin BC Origin | PASS |
| §7 | Epistemic Ledger | PASS |
| §8 | Reviewer Trap Checklist | PASS |
| §9 | Uncertainty Budget | PASS |
| §10 | Dependency Audit | PASS |
| §11 | Numerical Analysis | PASS |
| §12 | Conclusions | PASS |
| App A | Units & Dimensional Analysis | PASS |
| App B | Numerical Implementation | PASS |

## MD5 Checksums

| File | MD5 |
|------|-----|
| main.tex | (computed at commit) |
| main.pdf | (computed at commit) |
| export PDF | (matches main.pdf) |

## Final Status

**ALL ACCEPTANCE CRITERIA MET**

---

*Acceptance recorded: 2026-02-03*
