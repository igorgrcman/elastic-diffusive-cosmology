# Notation Correction Checklist — All EDC Books

**Date:** 2026-03-16
**Step:** 9 of 9 (Integration Program)
**Reference:** CANONICAL_NOTATION.md, edc_macros.sty

---

## Priority Legend

- **P0 (CRITICAL):** Bare δ — actively causes 50× scale errors
- **P1 (HIGH):** z→ξ, σ labeling — semantic confusion
- **P2 (MEDIUM):** M_5, κ, η — disambiguation
- **P3 (LOW):** Style alignment, macro adoption

---

## Book I Corrections (edc_book/)

### P0: Bare δ → Subscripted

- [ ] `chapter_0_theory_core.tex`: Identify all bare δ uses; assign δ_J or R_ξ based on context
- [ ] `chapter_6_quantum_constants.tex`: δ in mass scaling formulas → determine which scale
- [ ] `chapter_11_verifications.tex:135–142`: δ in verification formulas → δ_J (junction context)
- [ ] `chapter_4_leptons.tex`: δ in electron/muon formulas → determine R_ξ or δ_J

### P1: z → ξ (5D Coordinate)

- [ ] `chapter_0_theory_core.tex:167`: z in 5D coordinate tuple → ξ
- [ ] `chapter_0_theory_core.tex:192`: z in 5D context → ξ
- [ ] Any other instances: search `\bz\b` in 5D depth context → ξ
- [ ] **Preserve:** z in (x,y,z) 3D Cartesian tuples — do NOT change

### P1: σ Labeling

- [ ] `chapter_4_leptons.tex:208,214,222`: σ in mass formulas → clarify σ_eff or σ_surf
- [ ] `chapter_6_quantum_constants.tex:788–793`: σ_eff note → add [Cal] tag explicitly
- [ ] Any σ with dimensions [M³] → label σ_surf

### P2: M_5 Disambiguation

- [ ] `chapter_0_theory_core.tex:145,189`: Verify 𝓜⁵ (calligraphic) for manifold
- [ ] Any M_5 for Planck mass → M_{5,Pl}

### P3: Macro Adoption

- [ ] Add `\usepackage{edc_macros}` to Book I preamble
- [ ] Replace manual symbol definitions with macro calls

---

## Book II Corrections (edc_book_2/)

### P0: Bare δ → Subscripted

- [ ] `src/sections/05_case_neutron.tex:174–177`: δ in junction stiffness → δ_J
- [ ] `src/sections/ch14_bvp_closure_pack.tex`: δ in BVP context → δ_BL or Δ (kink)
- [ ] `src/sections/06_neutrinos_edge_modes.tex`: δ in overlap formulas → δ_BL
- [ ] `src/sections/ch16_opr04_delta_derivation.tex`: Multiple δ scales — assign each
- [ ] All other bare δ: audit via `grep -n "\\\\delta[^_]" *.tex`

### P1: Already Remediated (Phase D)

- [x] z → ξ: 39+ fixes applied
- [x] M_5 → 𝓜⁵ / M_{5,Pl}: 19 fixes applied
- [x] (x^μ, z) → (x^μ, ξ): 3 fixes applied

### P2: κ Disambiguation

- [ ] `src/sections/06_neutrinos_edge_modes.tex:70–71`: κ → κ_pen (penetration depth)
- [ ] `src/sections/ch11_opr20_attemptG_BC_provenance.tex`: κ in overlap → κ_pen or κ_BC
- [ ] `src/sections/05_three_generations.tex`: κ in generation context → verify which κ
- [ ] All Robin BC contexts: κ → κ_BC

### P2: η Clarification

- [ ] First use of η in each chapter: add "(bulk viscosity)" or subscript _μν for metric
- [ ] `src/sections/02_geometry_interface.tex`: η context → verify

### P3: Macro Adoption

- [ ] Import edc_macros.sty or merge with existing meta_macros.tex
- [ ] Replace manual \newcommand definitions that duplicate edc_macros.sty

---

## Book IV Corrections (edc_book_4/)

### P0: Bare δ → Subscripted

- [ ] `chapters/ch04_sigma_to_K.tex`: δ in pinning constant formula → δ_J
- [ ] `chapters/ch08_L0_delta_ratio.tex`: All δ → δ_J (junction thickness throughout)
- [ ] `chapters/ch09_instanton.tex`: δ in bounce action → δ_J
- [ ] `chapters/ch03_neutron_metastable.tex`: δ in metastable state → δ_J
- [ ] `chapters/ch06_tunneling.tex`: δ in barrier formula → δ_J
- [ ] `appendices/app_L0delta_model_bvp.tex`: δ in BVP model → clarify δ_J vs δ_BL
- [ ] **ALL references to L₀/δ:** → L₀/δ_J (explicitly)

### P0: σ Value Consistency

- [ ] Identify every σ numerical value in Book IV chapters
- [ ] Label each as σ_jun (8.82) or σ_cell (5.86) or σ_eff (generic)
- [ ] `chapters/ch04_sigma_to_K.tex`: Verify which σ enters K formula
- [ ] `chapters/ch10_deuterium.tex`: σ in binding energy → verify value
- [ ] `chapters/ch11_helium4.tex`: σ in binding → verify value
- [ ] **Do NOT change numerical values** — only add subscript labels
- [ ] Add footnote noting OPR-34 (σ discrepancy) where both values appear

### P1: L₀/δ Clarification

- [ ] Every "L₀/δ" → "L₀/δ_J" (20+ occurrences)
- [ ] `derivations/L0_DELTA_PI2_DERIVATION.md`: Already uses δ_J — verify consistency
- [ ] `audit/DELTA_CANONICAL_MAP.md`: Reference document — already correct

### P2: Macro Adoption

- [ ] Merge edc_macros.sty with existing preamble.tex
- [ ] Replace manual definitions with macro calls
- [ ] Add `\usepackage{edc_macros}` path to main.tex

---

## Papers Corrections (edc_papers/)

### P1: z → ξ

- [ ] Paper 3 rebuild snapshot: z in 5D context → ξ (~5 instances)
- [ ] Paper 2: verify ξ usage (likely already correct)

### P2: Macro Alignment

- [ ] Import edc_macros.sty into papers/_shared/style/
- [ ] Align existing edc_style.tex macros with canonical names
- [ ] Resolve any macro name conflicts

### P3: Five Pillars Draft

- [ ] `papers/FIVE_PILLARS_DRAFT_v1.tex`: Already uses canonical notation — verify
- [ ] `papers/SUPERHEAVY_PREDICTIONS_v1.tex`: Already uses canonical notation — verify

---

## Code Corrections (Python)

### P0: δ Parameter Name

- [ ] `derive_C_integrals.py`: `DELTA_EDC = 0.1` → Clarify: is this δ_J (0.105 fm)?
- [ ] `putC_compute_MV.py`: `delta` parameter → rename to `delta_J`
- [ ] `opr04_delta_consistency_check.py`: All δ references → subscripted in comments
- [ ] `superheavy_predictions.py`: Verify no bare δ in model parameters

### P1: σ Value

- [ ] `derive_C_integrals.py`: `SIGMA_EDC = 8.82` → label as σ_jun in comments
- [ ] Verify which σ each script uses and document

---

## Validation Procedure

After applying corrections:

1. Run `gate_notation.sh` on all modified .tex files
2. Compile each book to verify no LaTeX errors
3. Verify bare δ count is zero: `grep -rn "\\\\delta[^_{]" *.tex | grep -v "\\\\Delta"`
4. Verify z-for-5D count is zero: search context-aware
5. Spot-check 10 random formulas for correct subscripts

---

## Tracking

| Book | P0 items | P1 items | P2 items | P3 items | Total |
|------|----------|----------|----------|----------|-------|
| Book I | 4 | 5 | 2 | 1 | 12 |
| Book II | 5 | 0 (done) | 4 | 1 | 10 |
| Book IV | 9 | 1 | 1 | — | 11 |
| Papers | 0 | 1 | 2 | 1 | 4 |
| Code | 2 | 1 | — | — | 3 |
| **Total** | **20** | **8** | **9** | **3** | **40** |

**Estimated effort:**
- P0 (bare δ): ~2 hours focused find-and-replace with context checking
- P1 (z→ξ, σ): ~1 hour
- P2 (disambiguation): ~1 hour
- P3 (macros): ~30 minutes

---

**Sealed:** 2026-03-16. Step 9 of 9. Correction checklist: 40 items across 4 books + code.
20 P0 (critical), 8 P1 (high), 9 P2 (medium), 3 P3 (low).
