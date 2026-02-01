# V7.9 INTEGRATION PLAN

**Created**: 2026-01-31
**Purpose**: Step-by-step implementation guide

---

## Overview

**Goal**: Integrate V7.4–V7.8 α-decay findings into `compile_topological_pinning.tex` derivation document.

**Approach**: Create the missing `BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex` file that the wrapper references, incorporating both the M6 theoretical framework and the new empirical audit results.

---

## Step-by-Step Plan

### Step 1: Create BOOK_SECTION File Structure ✓

**Action**: Create `src/derivations/BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex`

**Content structure**:
```latex
% Section 1: Introduction and M6 Foundation
% Section 2: Free vs Bound Neutron
% Section 3: Alpha-Decay Empirical Audit [NEW]
% Section 4: Falsification Framework
% Section 5: Open Questions
% Appendix: Forbidden Alternatives Matrix
```

**Risk**: LOW — creating new file, not modifying existing

### Step 2: Convert M6 Exploration to LaTeX (Sections 1-2) ✓

**Source**: `src/derivations/M6_TOPOLOGICAL_MODEL_EXPLORATION.md`
**Lines**: 1-380

**Conversion tasks**:
- Markdown tables → LaTeX tabular
- Code blocks → equation environments
- Section headers → \section/\subsection
- Preserve epistemic tags as margin notes or inline

**Risk**: LOW — straightforward conversion

### Step 3: Write α-Decay Audit Section (Section 3) ✓

**Sources**:
| Content | Source File | Lines |
|---------|-------------|-------|
| n(A) mapping | V7.4/07_RESIDUALS_DN_CORRELATION_V7_4.md | 5-20 |
| V7.4 results | V7.4/06_GN_FIT_V7_4.md | 82-106 |
| V7.8 results | V7.8/07_FIT_RESULTS_V7_8.md | 56-71, 126-131 |
| Sign resolution | V7.6.1/01_TEST_BARRIER_vs_PREFACTOR.md | 162-217 |
| Robustness | V7.5/00_README.md | 10-50 |
| Mediation | V7.8/08_MEDIATION_AND_INTERPRETATION.md | 70-89 |

**Key constraints**:
- All numerics must be traceable (no hallucination)
- Sign-safe language throughout
- Explicit epistemic tags

**Risk**: MEDIUM — requires careful sign-safe language

### Step 4: Write Falsification Section (Section 4) ✓

**Sources**:
| Content | Source File | Lines |
|---------|-------------|-------|
| Passed tests | V7.5/00_README.md | 30-60 |
| Open tests | V7.7/10_OPEN_QUESTIONS_V7_7.md | 10-80 |
| Predictions | V7.7/04_PREFACTOR_MECHANISM_MODEL.md | 159-189 |

**Risk**: LOW — mostly list formatting

### Step 5: Write Open Questions Section (Section 5) ✓

**Sources**:
| Content | Source File | Lines |
|---------|-------------|-------|
| Updated kingpins | V7.8/10_OPEN_QUESTIONS_V7_8.md | 25-150 |
| Path to [Der] | V7.8/10_OPEN_QUESTIONS_V7_8.md | 195-208 |

**Risk**: LOW — straightforward

### Step 6: Add Forbidden Alternatives Appendix ✓

**Source**: V7.7/07_FORBIDDEN_ALTERNATIVES_BEYOND_M43.md lines 35-48

**Risk**: LOW — table conversion

### Step 7: Update Abstract (if needed)

**Current abstract** (line 39 of wrapper):
> "Frustration-Corrected Geiger-Nuttall Law for α-decay (R² = 0.9941, 44.7% improvement)"

**Check**: Verify this matches V7.8 results. If not, flag for update.

**Note**: R² = 0.9812 in V7.8 M7, not 0.9941. Abstract may need correction.

**Risk**: LOW — small text change

### Step 8: Generate Patch ✓

**Action**: Create unified diff in `06_PATCH.diff`

**Scope**:
- New file: BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex
- Possible small fix to wrapper abstract

**Risk**: LOW

### Step 9: Test Compilation

**Commands**:
```bash
cd /Users/igor/ClaudeAI/EDC_Project/elastic-diffusive-cosmology_repo/edc_book_2/src/derivations
pdflatex compile_topological_pinning.tex
```

**Expected issues**:
- Missing packages (unlikely, standard set)
- BibTeX references (none expected)

**Risk**: LOW

### Step 10: Commit

**Message**:
```
integrate(v7.8): tie topological pinning to α-decay prefactor evidence

- Create BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex with M6 framework
- Add Section 3: α-decay empirical audit (V7.4-V7.8)
- Sign-safe interpretation: frustration → S_α enhancement
- Update falsification tests from V7.7/V7.8
```

**Risk**: LOW

---

## Non-Goals

| Item | Reason |
|------|--------|
| Modify Book2 spine | G0 guardrail |
| Add new physics derivations | Out of scope — integration only |
| Resolve open kingpins | Research task, not integration |
| Update V7.4 regression with V7.8 numbers uniformly | Different scaling; document both |
| Create new figures | Text-only integration |

---

## Risk Matrix

| Step | Risk | Mitigation |
|------|------|------------|
| 1 | LOW | N/A |
| 2 | LOW | Direct conversion |
| 3 | **MEDIUM** | Use claim ledger; sign-safe checklist |
| 4 | LOW | N/A |
| 5 | LOW | N/A |
| 6 | LOW | N/A |
| 7 | LOW | Verify against V7.8 |
| 8 | LOW | N/A |
| 9 | LOW | Standard LaTeX |
| 10 | LOW | N/A |

---

## Rollback Plan

If integration fails:
1. `git checkout main -- src/derivations/`
2. Delete audit folder (optional)
3. Document failure in SESSION_LOG.md

---

## Acceptance Checklist

- [ ] BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex exists
- [ ] Compiles without error
- [ ] All claims in 04_CLAIM_LEDGER.md traceable
- [ ] Sign-safe language verified
- [ ] Epistemic tags present
- [ ] No Book2 modifications
- [ ] Committed to branch

