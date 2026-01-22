# Research Timeline — Part II: The Weak Interface

**Version:** 1.0
**Created:** 2026-01-22
**Purpose:** Chronological record of Part II development

---

## Phase 1: Foundation (January 2026)

### 2026-01-18 — Initial Structure

**What happened:**
- Part II structure established with 13 chapters
- Chapter outline covering: geometry, particle cases, electroweak parameters, mixing

**Files created:**
- `EDC_Part_II_Weak_Sector.tex`
- `sections/` directory with initial chapter stubs

**Key decisions:**
- Unified pipeline approach (geometry → chirality → observable)
- Reader Contract at beginning

---

### 2026-01-19 — Chapter 3 & 5 Development

**What happened:**
- sin²θ_W = 1/4 derivation completed
- RG running calculation added
- N_g = 3 from Z₆/Z₂ quotient established

**Key results:**
- sin²θ_W(M_Z) = 0.2314 (0.08% from PDG)
- Three generations from discrete symmetry counting

**Files modified:**
- `sections/05_three_generations.tex`

---

### 2026-01-20 — Chapter 11 GREEN-A/YELLOW-B/RED-C Framework

**What happened:**
- Developed three-level derivation status naming
- Established G_F pathway structure
- Identified circularity issue with v dependence

**Key insight:**
- G_F "exact agreement" is consistency, not prediction
- True independent claim is sin²θ_W = 1/4

**Commit:** `aba4822`

---

### 2026-01-21 — Chapter 11 Reviewer-Proof Upgrades

**What happened:**
- Added explicit circularity firewall
- Created Chain Boxes for derivation summaries
- Upgraded companion notes (CH11_GF_NOTES.md v2)

**Files modified:**
- `sections/11_gf_derivation.tex`
- `CH11_GF_NOTES.md`

**Commit:** `b4ff06a`

---

## Phase 2: CKM Development (January 22, 2026)

### 2026-01-22 Morning — Chapter 7 Attempt 1

**What happened:**
- Computed Z₃ DFT baseline for CKM matrix
- Result: |V_ij|² = 1/3 for all elements
- Falsified against PDG (×144 off for diagonal elements)
- Quantified breaking amplitudes: ε_us ~ 0.39, ε_cb ~ 0.07, ε_ub ~ 0.007

**Key insight:**
- Pure Z₃ symmetry insufficient
- Significant breaking required for realistic CKM
- Negative result is valuable documentation

**Files modified:**
- `sections/07_ckm_cp.tex`
- `CH7_CKM_CP_NOTES.md` (v2)

**Commit:** `a2e9a6e`

---

### 2026-01-22 Afternoon — Chapter 7 Attempt 2

**What happened:**
- Implemented overlap model with exponential profiles
- Demonstrated Wolfenstein hierarchy from single parameter
- Calibration: Δz/(2κ) = -ln(λ) ≈ 1.49

**Key results:**
- λ, λ², λ³ scaling emerges naturally from overlap suppression
- CKM vs PMNS explained via localization width difference
- Numerical demo in Python confirms scaling

**Files created:**
- `code/ckm_overlap_attempt2.py`

**Files modified:**
- `sections/07_ckm_cp.tex`
- `CH7_CKM_CP_NOTES.md` (v3)

**Commit:** `3b1aa94`

---

### 2026-01-22 Late Afternoon — Meta Documentation

**What happened:**
- Created meta-documentation infrastructure
- Claim Ledger with 17 entries
- Decision Log with 6 entries
- Research Timeline (this file)
- Evidence Map with cross-references

**Files created:**
- `_shared/meta/` (3 utility files)
- `meta_part2/` (6 LaTeX files)
- `meta_part2_md/` (4 Markdown files)

**Commit:** pending

---

## Open Work Items

### High Priority
1. **Chapter 6**: PMNS numeric demonstration (parallel to Ch7 Attempt 2)
2. **Chapter 7**: CP phase δ treatment
3. **Chapter 11**: RED-C first-principles pathway

### Medium Priority
4. Cross-reference verification across all chapters
5. Figure updates for unified pipeline
6. Bibliography consolidation

### Low Priority (Future)
7. Companion paper extraction for individual results
8. Zenodo DOI assignment for data files

---

## Lessons Learned

### What Worked
- Falsify-first approach (Attempt 1 → Attempt 2)
- Explicit epistemic tagging from start
- Companion notes (.md files) for detailed logs

### What Could Improve
- Earlier identification of circularity issues
- More systematic equation labeling
- Automated claim status checking

---

*Research Timeline v1.0 — Last updated 2026-01-22*
