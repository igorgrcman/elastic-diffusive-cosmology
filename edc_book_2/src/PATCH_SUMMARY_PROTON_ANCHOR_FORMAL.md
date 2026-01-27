# PATCH SUMMARY: Dual-Route Proton Anchor Proof

**Date:** 2026-01-27
**Files Modified:**
- `sections/04b_proton_anchor.tex` — Route A formal proof + convergence preview
- `sections/04c_routeB_z6_steiner.tex` — **NEW** Route B formal proof
- `EDC_Part_II_Weak_Sector_rebuild.tex` — preamble + include Route B
- `aside_m5_to_z6_proof/STATUS_MAP.md` — dual-route documentation

---

## Summary

Added formal Lemma-Theorem-Corollary proof chain for proton stability, independent
of the Z6 crystallization program. This establishes proton as topological-geometric
minimum using only:
1. Topological protection (pi_1 obstruction)
2. Nambu-Goto action (E = tau*L)
3. Steiner theorem (120 degree angles minimize length)

## Changes

### 04b_proton_anchor.tex

**Added section:** `\subsubsection{Proton Topological Anchor --- Formal Statement}`

| Component | Status | Content |
|-----------|--------|---------|
| Lemma 1 | [M]+[P] | Topological protection from pi_1 |
| Lemma 2 | [Der] | Nambu-Goto gives E = tau*L |
| Theorem 1 | [M] | Steiner optimality (classical) |
| Corollary 1 | [Dc] | Proton Y-junction is local minimum |
| Remark | [Der] | BC clarification (no attraction from BC) |

**Updated status table** to reflect formal proof references.

### EDC_Part_II_Weak_Sector_rebuild.tex

**Added environments:**
```latex
\newtcolorbox{edcLemmaBox}[2]{...}
\newtcolorbox{edcTheoremBox}[2]{...}
\newtcolorbox{edcCorollaryBox}[2]{...}
```

### aside_m5_to_z6_proof/STATUS_MAP.md

**Added:** Separate derivation chains for:
- A. Proton Stability (independent path)
- B. Z6 Crystallization (complementary path)
- C. BC Clarification

---

## Key Clarifications

1. **BC do NOT create attraction:** V'_lin(d) > 0 for all BC choices
2. **Minimum from topology:** V_core (radial-frozen) + V_lin (log growth) balance
3. **Steiner is [M]:** Mathematical theorem, not EDC-specific
4. **Proton stability is now [Dc]:** Derived consequence of formal proof chain

---

## Epistemic Status Before/After

| Claim | Before | After |
|-------|--------|-------|
| Proton is Y-junction minimum | [P] → [Dc] in Ch2 | [Dc] via formal proof |
| 120° Steiner angles | [Dc] from Ch2 | [M] classical geometry |
| BC create attraction | (implicit assumption) | **FALSE** [Der] |
| Minimum mechanism | unclear | [Der] V_core + V_lin balance |

---

## Verification

Build command:
```bash
cd edc_book_2/src && latexmk -xelatex -interaction=nonstopmode EDC_Part_II_Weak_Sector_rebuild.tex
```

## References

- `aside_frozen_brane_bc_v1/07_VERDICT.txt` — BC clarification
- `aside_frozen_brane_bc_v1/06_RELATION_TO_RADIAL_STEP_FROZEN.md` — Two types of "frozen"
- `aside_archive/DERIVATION_V_r_FROM_BC__RETRACTED.md` — Retracted erroneous derivation
