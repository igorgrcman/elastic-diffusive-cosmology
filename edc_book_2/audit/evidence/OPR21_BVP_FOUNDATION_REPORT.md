# OPR-21 BVP Foundation Sprint — Audit Report

**Date**: 2026-01-25
**Branch**: `book2-opr21-bvp-foundation-v1`
**Status**: STRONG PARTIAL

---

## Executive Summary

This sprint established the **mathematical foundation** for OPR-21 (BVP mode profiles), documenting the lemma chain from domain definition through numerical validation. The infrastructure is now complete; closure requires deriving the physical potential V(ξ) from the 5D action.

### Key Results

| Item | Status | Evidence |
|------|--------|----------|
| L1: Domain definition | ESTABLISHED [M] | ch14_bvp_closure_pack.tex:135-153 |
| L2: 5D→1D reduction | PARTIAL [Dc] | ch14_bvp_closure_pack.tex:239-344 |
| L3: Robin BC form | ESTABLISHED [M] | ch14_bvp_closure_pack.tex:169-228 |
| L4: Sturm-Liouville | ESTABLISHED [M] | ch14_bvp_closure_pack.tex:206-237 |
| L5: Toy validation | ESTABLISHED [M] | code/opr21_bvp_demo.py, outputs verified |

### Blocking Items

1. **V(ξ) derivation** — NOT yet completed from 5D action
2. **BC parameter derivation** — NOT yet completed from Israel junction
3. **Physical N_bound** — Cannot compute without physical V(ξ)

---

## Deliverables Created

### D1: OPR-21 Lemma Chain Document

**File**: `canon/opr/OPR-21.md`

**Contents**:
- L1-L5 lemma statements with status
- Output object definitions (ψ_n, x₁, I₄, N_bound)
- Closure conditions
- Cross-references to book chapters

### D2: BVP Demo Script

**File**: `code/opr21_bvp_demo.py`

**Outputs generated**:
- `code/output/opr21_robustness_table.md` — BC variation scan
- `code/output/opr21_phase_diagram.md` — V₀ sweep
- `code/output/opr21_summary.json` — Machine-readable summary

**Key findings from demo**:
- N_bound is STABLE under BC variations (for toy potential)
- Phase transitions occur at V₀ ~ 3, ~15, ~30 (for Pöschl-Teller)
- N_bound = 3 requires V₀ > 25 (in dimensionless units)

### D3: This Audit Report

**File**: `audit/evidence/OPR21_BVP_FOUNDATION_REPORT.md`

---

## Infrastructure Validation

### Robustness Test Results

For toy potential V(ξ) = -10 sech²(ξ):

| ξ_max | κ (Robin) | N_bound | x₁ | I₄ |
|-------|-----------|---------|-------|-------|
| 10.0 | 0.0 | 1 | 7.45 | 0.717 |
| 12.0 | 0.5 | 1 | 7.43 | 0.716 |
| 14.0 | 1.0 | 1 | 7.38 | 0.718 |

**Verdict**: N_bound STABLE across all tested (ξ_max, κ) pairs.

### Phase Diagram Results

| V₀ | N_bound | Transition |
|----|---------|------------|
| 1.0 | 0 | — |
| 3.0 | 1 | 0→1 at V₀~2 |
| 10.0 | 1 | — |
| 15.0 | 2 | 1→2 at V₀~12 |
| 25.0 | 2 | — |
| 30.0 | 3 | 2→3 at V₀~28 |

**Verdict**: N_bound = 3 is NOT automatic. Requires sufficient potential depth.

---

## Book Integration Status

### Existing Coverage

| Chapter | File | BVP Content | Status |
|---------|------|-------------|--------|
| CH12 | ch12_bvp_workpackage.tex | Work package definition | Infrastructure |
| CH14 | ch14_bvp_closure_pack.tex | Formal closure pack | Comprehensive |
| — | bvp_halfline_toy_demo.py | Toy figure generation | Demo only |

### Integration Recommendation

No new book patches required. Existing CH14 coverage is comprehensive. The OPR-21.md document provides the formal lemma chain referenced by CH14.

---

## OPR Status Updates

### OPR-21 [B] BVP mode profiles

**Previous status**: OPEN
**New status**: STRONG PARTIAL

**Justification**:
- All infrastructure lemmas (L1, L3, L4) now ESTABLISHED
- Toy model validation complete (L5)
- Reduction lemma (L2) has structure but awaits V(ξ) derivation

**Remaining for CLOSED**:
1. Complete V(ξ) derivation from 5D action (L2 closure)
2. Derive BC parameters from Israel junction (L3.2 closure)
3. Compute N_bound for physical potential
4. Verify robustness of N_bound = 3

### Downstream OPRs

| OPR | Blocked by OPR-21 | Status |
|-----|-------------------|--------|
| OPR-02 | N_bound = 3 | Still OPEN |
| OPR-22 | I₄ from physical profiles | Still OPEN |

---

## Technical Notes

### Finite Difference vs Analytic

The existing `bvp_halfline_toy_demo.py` uses analytic Pöschl-Teller formulas. The new `opr21_bvp_demo.py` uses finite difference methods, which:

1. Are more general (work for any V(ξ))
2. Validate the numerical infrastructure
3. Give consistent N_bound values

### Simpson vs Trapezoid Integration

The demo uses `scipy.integrate.simpson` when available, falling back to `np.trapezoid`. Both give consistent I₄ values to 3 decimal places.

---

## Next Steps

### Immediate (within sprint)

- [x] Create OPR-21.md lemma chain
- [x] Create opr21_bvp_demo.py
- [x] Run demo, verify outputs
- [x] Create this audit report
- [ ] Commit and push branch

### Short-term (next sprint)

- [ ] Derive V(ξ) from 5D Dirac + warp factor
- [ ] Connect membrane parameters (σ, r_e) to potential parameters

### Medium-term (OPR-21 closure)

- [ ] Derive BC from Israel junction
- [ ] Compute N_bound for physical potential
- [ ] Show N_bound = 3 robustly

---

## Commit Plan

```
git add canon/opr/OPR-21.md
git add code/opr21_bvp_demo.py
git add code/output/opr21_*.md
git add code/output/opr21_summary.json
git add audit/evidence/OPR21_BVP_FOUNDATION_REPORT.md
git commit -m "OPR-21 foundation: lemma chain, demo script, audit report

- Create OPR-21.md with L1-L5 lemma chain
- Create opr21_bvp_demo.py for infrastructure validation
- Robustness test: N_bound STABLE under BC variations
- Phase diagram: N_bound=3 requires V₀>25 (toy potential)
- Status: STRONG PARTIAL (awaits V(ξ) from 5D action)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

*Generated: 2026-01-25*
*Sprint: book2-opr21-bvp-foundation-v1*
