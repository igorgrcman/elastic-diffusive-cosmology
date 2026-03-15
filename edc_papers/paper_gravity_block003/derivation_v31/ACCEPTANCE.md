# Derivation v31 — Acceptance Criteria

## Required Checks (AC-P39-*)

| ID | Criterion | Status |
|----|-----------|--------|
| AC-P39-1 | BC Registry: ≥4 field types | PASS (graviton, gauge, scalar, fermion) |
| AC-P39-2 | Scale Regime Map with TikZ figure | PASS (Figure 1) |
| AC-P39-3 | Gauge bridge slot derived | PASS (Eq 38, §4) |
| AC-P39-4 | ≥90 equations, ≥18 pages | PASS (97 eqs, 21 pages) |
| AC-P39-5 | recompute.py ≥10 checks, ALL PASS | PASS (15 checks) |
| AC-P39-6 | Inputs table w/o forbidden | PASS (REPORT.md §1) |
| AC-P39-7 | FROZEN main.tex unchanged | PASS (v31 is new) |
| AC-P39-8 | Export PDF filename exact | PASS |
| AC-P39-9 | PAPERS_INDEX row + detailed entry | PASS |
| AC-P39-10 | Generator Survival Matrix | PASS (Table 3) |

## Build Verification

| Check | Result |
|-------|--------|
| Compiles without errors | PASS |
| No undefined references | PASS (0) |
| No multiply defined | PASS (0) |
| No private paths in PDF | PASS |

## Content Verification

| Section | Content | Status |
|---------|---------|--------|
| §1 | Reader Contract + Tags | PASS |
| §2 | 5D Gauge Action | PASS |
| §3 | KK Decomposition | PASS |
| §4 | Gauge Normalization | PASS |
| §5 | BC Registry | PASS |
| §6 | Scale Regime Map | PASS |
| §7 | CS Terms | PASS |
| §8 | Coupling Running | PASS |
| §9 | Unification Route | PASS |
| §10 | Epistemic Ledger | PASS |
| §11 | Reviewer Traps | PASS |
| §12 | Conclusions | PASS |
| App A | Dimensional Analysis | PASS |
| App B | Mode Details | PASS |
| App C | Warped Geometry | PASS |
| App D | Group Theory | PASS |
| App E | Extended Derivations | PASS |
| App F | Fermion BC | PASS |
| App G | Numerical Examples | PASS |
| App H | Comparison | PASS |

## Python Verification (recompute.py)

| Check | Expected | Computed | Status |
|-------|----------|----------|--------|
| [g₅²] = [M]⁻¹ | dim check | verified | PASS |
| [g₄²] = 1 | dimensionless | verified | PASS |
| Bridge dimension | consistent | verified | PASS |
| Neumann I_gauge | 1 | 1.0 | PASS |
| Neumann spectrum | nπ/L | verified | PASS |
| Dirichlet no zero | m₁ > 0 | 3.1416 | PASS |
| Robin spectrum | transcendental | x₁=0.86 | PASS |
| Orthonormality | δ_mn | verified | PASS |
| CS quantization | k ∈ ℤ | verified | PASS |
| U(1) count | 1 | 1 | PASS |
| Generator count | 8 | 8 | PASS |
| KK threshold | π/L | verified | PASS |
| Warped cancel | equality | verified | PASS |
| No forbidden | none | none | PASS |
| SL form | verified | verified | PASS |

**Total**: 15/15 CHECKS PASSED

## AC-P39-6: No Forbidden Inputs

| Forbidden Input | Appears in main.tex | Appears in recompute.py | Status |
|-----------------|---------------------|-------------------------|--------|
| M_Z = 91.19 GeV | NO | NO | PASS |
| M_W = 80.38 GeV | NO | NO | PASS |
| v_EW = 246.2 GeV | NO | NO | PASS |
| α_EM = 1/137 | NO | NO | PASS |
| G_N | NO | NO | PASS |
| ℓ_P | NO | NO | PASS |

## AC-P39-1: BC Registry Verification

| Field Type | Covered | BC Types | Status |
|------------|---------|----------|--------|
| Graviton | Yes | N/N, Robin | PASS |
| Gauge boson | Yes | N/N, D/D, N/D, Robin | PASS |
| Scalar | Yes | N/N, D/D | PASS |
| Fermion | Yes | orbifold | PASS |

**AC-P39-1 STATUS: PASS** (4 field types)

## AC-P39-2: Scale Regime Map Verification

| Component | Present | Status |
|-----------|---------|--------|
| TikZ figure | Yes (Figure 1) | PASS |
| UV regime | E ≫ 1/L | PASS |
| KK threshold | E ~ 1/L | PASS |
| IR regime | E ≪ 1/L | PASS |
| Explicit thresholds | m_gap = x₁/L | PASS |

**AC-P39-2 STATUS: PASS**

## AC-P39-10: Generator Survival Matrix

| Component | Present | Status |
|-----------|---------|--------|
| Table format | Yes (Table 3) | PASS |
| All 8 generators | T¹..T⁸ | PASS |
| BC assignments | N and D | PASS |
| Zero mode column | Yes | PASS |
| 4D role column | Yes | PASS |

**AC-P39-10 STATUS: PASS**

## Trap-to-Equation Mapping

| Trap | Key Reference | Status |
|------|---------------|--------|
| TRAP-1 | No α_EM | PASS |
| TRAP-2 | [OPEN] for SM | PASS |
| TRAP-3 | [P] for G | PASS |
| TRAP-4 | Lemma 2.1 | PASS |
| TRAP-5 | Eq (24) | PASS |
| TRAP-6 | Eq (28) | PASS |
| TRAP-7 | [OPEN] | PASS |
| TRAP-8 | Thm 2.2 | PASS |
| TRAP-9 | App C | PASS |
| TRAP-10 | Eq (46) | PASS |
| TRAP-11 | Figure 1 | PASS |
| TRAP-12 | Table 3 | PASS |
| TRAP-13 | Lemma 6.2 | PASS |
| TRAP-14 | Thm 7.1 | PASS |

## Final Status

**ALL ACCEPTANCE CRITERIA MET**

---

*Acceptance recorded: 2026-02-03*
