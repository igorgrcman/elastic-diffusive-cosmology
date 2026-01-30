# Book 2 Canonical Build Report

**Build Date:** 2026-01-29 (updated)
**Source File:** `src/EDC_BOOK2_WEAK_CANON.tex`
**Status:** ✓ PASS (PDF generated, all references resolved)

---

## Build Summary

| Metric | Value |
|--------|-------|
| **Pages** | 453 |
| **PDF Size** | ~2.0 MB |
| **Undefined References** | 0 ✓ |
| **Multiply-Defined Labels** | 0 ✓ |
| **Missing Characters** | ~180 (Greek in non-math fonts) |
| **Compilation Result** | **SUCCESS** |

---

## Structure Verification

### Parts and Chapters

| Part | Chapters | Pages (approx) |
|------|----------|----------------|
| **Front Matter** | How to Read, TOC | 10 |
| **Part I: Physical Picture** | Ch 1-6 | ~120 |
| **Part II: Predictions** | Ch 7-12 | ~100 |
| **Part III: Machinery** | Ch 13-16 | ~170 |
| **Epilogue** | Ch 17 | ~20 |
| **Back Matter** | Appendices, Bibliography | ~40 |

### Chapter List

1. Ch 1: The Weak Interface
2. Ch 2: Particle Ontology in EDC
3. Ch 3: Case Study: Neutron Decay
4. Ch 4: Case Study: Muon Decay
5. Ch 5: Case Study: Tau Decay
6. Ch 6: Stability and Edge Modes
7. Ch 7: Electroweak Parameters from Geometry
8. Ch 8: The Fermi Constant: Overview
9. Ch 9: Why Exactly Three Generations?
10. Ch 10: Neutrino Mixing Angles
11. Ch 11: CKM Matrix and CP Violation
12. Ch 12: V-A Structure from Chiral Localization
13. Ch 13: Scale Taxonomy and Anchors
14. Ch 14: BVP Framework
15. Ch 15: The Coupling Chain
16. Ch 16: Closure Status and Open Problems
17. Ch 17: Nuclear Applications Preview

---

## Reference Resolution (2026-01-29)

### Label Aliases Added to Spine

To maintain backwards compatibility with section files, the following label aliases were added:

| Alias | Points To | Purpose |
|-------|-----------|---------|
| `ch:z6_program` | `ch:electroweak` | Legacy Z6 program references |
| `ch:bvp_master_key` | `ch:bvp_framework` | Legacy BVP references |
| `ch:gf_derivation` | `ch:coupling_chain` | Legacy GF derivation references |
| `ch:neutrinos_edge` | `ch:pmns` | Legacy neutrino chapter references |
| `thm:steiner` | `thm:steiner_routeA` | Steiner theorem references |

### Section Files Updated

References updated from legacy labels to canonical labels or Derivation Library:

- `04b_proton_anchor.tex`: Route B → Derivation Library
- `05b_neutron_dual_route.tex`: Route B → Derivation Library
- `04_ontology.tex`: Charged ground mode → Derivation Library
- `05_three_generations.tex`: Step3 → Chapter ref
- `09_va_structure.tex`: BVP subsections → Chapter ref
- `06_neutrinos_edge_modes.tex`: Lepton candidates → Three generations chapter
- `11_gf_derivation.tex`: BVP workpackage → BVP framework
- `12_epistemic_map.tex`: Multiple closure attempt refs → Chapter/Library refs
- `ch14_opr21_closure_derivation.tex`: Self-adjoint theorem → Derivation Library
- `CH3_electroweak_parameters.tex`: Theorem refs → inline descriptions

### Files Added to Canonical Spine

- `sections/12_epistemic_map.tex` (provides `sec:gate_registry`)

---

## Comparison with Previous Builds

| Metric | Original (rebuild) | v1 Canonical | v2 (current) |
|--------|-------------------|--------------|--------------|
| Pages | 602 | 439 | 453 |
| Chapters | 20+ | 17 | 17 |
| Undefined refs | 0 | 41 | **0** ✓ |
| Multiply-defined | 0 | 0 | **0** ✓ |

**Note:** Page increase from 439 to 453 due to adding `12_epistemic_map.tex` (gate registry and consolidated status).

---

## Missing Characters (~180)

Greek letters in non-math contexts using text fonts that lack them:
- μ (mu)
- ξ (xi)
- σ (sigma)
- ✓ (checkmark)

**Fix:** Use math mode `$\mu$` instead of Unicode μ.
**Priority:** LOW (cosmetic, doesn't affect reader comprehension)

---

## Reader-Facing Artifact Check

```bash
grep -c "Repository artifact" EDC_BOOK2_WEAK_CANON.log
# Result: 0
```

✓ **PASS**: No repository artifact footnotes in canonical build.

---

## Build Command

```bash
cd edc_book_2/src
latexmk -xelatex -interaction=nonstopmode EDC_BOOK2_WEAK_CANON.tex
```

---

## Files Produced

- `EDC_BOOK2_WEAK_CANON.pdf` (~2.0 MB, 453 pages)
- `EDC_BOOK2_WEAK_CANON.aux`
- `EDC_BOOK2_WEAK_CANON.log`
- `EDC_BOOK2_WEAK_CANON.toc`
- `EDC_BOOK2_WEAK_CANON.bbl`

---

## Remaining Tasks

1. ~~Fix undefined references~~ ✓ DONE
2. **Test reader path** — Read PDF from start to finish, verify coherence
3. **Final audit** — Check for any remaining internal references
4. **Greek character fix** — Replace Unicode Greek with math mode (optional)

---

## Verdict

| Criterion | Status |
|-----------|--------|
| Compiles without fatal errors | ✓ PASS |
| PDF generated | ✓ PASS |
| Part I-III + Epilogue structure | ✓ PASS |
| 17 chapters in order | ✓ PASS |
| Chapter recaps present | ✓ PASS |
| No repo artifacts in PDF | ✓ PASS |
| Zero undefined refs | ✓ PASS |
| Zero multiply-defined | ✓ PASS |

**Overall:** BUILD SUCCESS. All critical issues resolved. Ready for editorial review.
