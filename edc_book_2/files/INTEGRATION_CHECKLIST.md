# EDC BOOK 2 REORGANIZATION - INTEGRATION CHECKLIST

**Date**: 2026-01-30  
**Version**: 1.0  
**Purpose**: Phase-by-phase implementation tracking  
**Duration**: 7 weeks

---

## PHASE 1: INFRASTRUCTURE & RESTRUCTURE (Week 1-2)

### Week 1: Setup

#### Monday-Tuesday: Directory Structure
- [ ] Create `/book2_reorganized/` directory
- [ ] Create subdirectories:
  ```
  /chapters/
  /appendices/
  /figures/
  /templates/
  /preamble/
  ```
- [ ] Copy LaTeX preamble from original
- [ ] Set up main.tex with new structure

#### Wednesday-Thursday: Templates Installation
- [ ] Copy `FINAL_EPISTEMIC_STANDARD.tex` → `/preamble/epistemic.tex`
- [ ] Copy `TEMPLATE_RESULT_PRESENTATION.tex` → `/templates/result.tex`
- [ ] Copy `TEMPLATE_5D_MECHANISM_BOX.tex` → `/templates/mechanism_box.tex`
- [ ] Create `/templates/status_box.tex`
- [ ] Test compilation of templates

#### Friday: Chapter Stubs
- [ ] Create `bridge_ch0.tex` (Bridge Chapter 0)
- [ ] Create `ch01_weak_interface.tex`
- [ ] Create `ch02_ontology.tex`
- [ ] Create `ch03_frozen.tex`
- [ ] Create `ch04_z6.tex`
- [ ] Create `ch05_case_studies.tex`
- [ ] Create `ch06_electroweak.tex`
- [ ] Create `ch07_leptons.tex`
- [ ] Create `ch08_three_gen.tex`
- [ ] Create `ch09_neutrinos.tex`
- [ ] Create `ch10_va_structure.tex`
- [ ] Create `ch11_ckm.tex`
- [ ] Create `ch12_gf_chain.tex`
- [ ] Create `ch13_foundation.tex`
- [ ] Create `ch14_bvp.tex`
- [ ] Create `ch15_mw_gf.tex`
- [ ] Create `ch16_summary.tex`
- [ ] Create `ch17_epilogue.tex`

### Week 2: Content Migration

#### Monday-Tuesday: Bridge Chapter 0
- [ ] Write intro (5 pages)
- [ ] Add "What Book 1 Established" section
  - [ ] List m_p/m_e = 6π⁵ with reference
  - [ ] List α⁻¹ formula with reference
  - [ ] List proton/neutron structures
  - [ ] List σ = 8.82 MeV/fm²
- [ ] Add "What Book 2 Adds" section
- [ ] Add "Reading Strategy" section
- [ ] **Integrate FINAL_EPISTEMIC_STANDARD.tex** in full
- [ ] Add baseline constants table
- [ ] Verify all cross-references compile

#### Wednesday: Chapter 1 Reorganization
- [ ] Extract neutron lifetime section from original Ch 1
- [ ] Place neutron lifetime as section 1.2 (early!)
- [ ] Reduce overview from 30 → 10 pages
- [ ] Move detailed case studies → Ch 5
- [ ] Add 3 "5D Mechanism" boxes:
  - [ ] Box 1.1: Thick Brane Necessity
  - [ ] Box 1.2: Junction Relaxation
  - [ ] Box 1.3: Energy Ledger
- [ ] Target: 50 pages total

#### Thursday-Friday: OPR Consolidation Outline
- [ ] Create Ch 12 outline: G_F Chain Overview
  - [ ] Parameter ledger table
  - [ ] Dependency graph (TikZ)
  - [ ] Status summary
- [ ] Create Ch 13 outline: Foundation Parameters
  - [ ] OPR-01, 04, 19 structure
- [ ] Create Ch 14 outline: BVP
  - [ ] Formulation
  - [ ] Attempts (honest history)
  - [ ] Current status: OPEN
- [ ] Create Ch 15 outline: M_W and G_F
  - [ ] Framework only
  - [ ] Blocked by OPR-21

---

## PHASE 2: CONTENT ADDITION (Week 3-4)

### Week 3: Mechanism Boxes + Critical Derivations

#### Monday: Boxes Ch 1-2
- [ ] Write Box 1.1: Thick Brane Necessity (use template)
- [ ] Write Box 1.2: Junction Relaxation (detailed)
- [ ] Write Box 1.3: Energy Ledger + Bulk
- [ ] Write Box 2.1: Topological Defect
- [ ] Write Box 2.2: Brane-Dominant Mode
- [ ] Write Box 2.3: Edge Mode (Neutrino) - use template example
- [ ] Write Box 2.4: Composite States
- [ ] Verify all boxes compile

#### Tuesday: Boxes Ch 3-4
- [ ] Write Box 3.1: Frozen Projection
- [ ] Write Box 3.2: Mode Overlap
- [ ] Write Box 4.1: Z₆ → SU(3) Emergence
- [ ] Write Box 4.2: Discrete → Continuous
- [ ] Write Box 4.3: Three Generations
- [ ] Verify compilation

#### Wednesday-Thursday: Critical Derivations (Priority 1)
- [ ] **Derivation 1: ℓ_p/r_e = 2π³** (Ch 3 or Bridge)
  - [ ] Setup: Y-junction + Z₆ lattice
  - [ ] Steiner angles (120°)
  - [ ] Geometric calculation
  - [ ] Show 2π³ emerges
  - [ ] ~5 pages with figures

- [ ] **Derivation 2: (4π + 5/6) in α** (Ch 3)
  - [ ] 5D gauge field A_M setup
  - [ ] KK reduction with R_ξ
  - [ ] Finite-size corrections
  - [ ] Show (4π + 5/6) decomposition
  - [ ] ~8 pages

- [ ] **Derivation 3: sin²θ_W RG Running** (Ch 6)
  - [ ] β-functions explicit
  - [ ] Integration Λ_comp → M_Z
  - [ ] Match 1/4 → 0.231
  - [ ] Solve for Λ_comp
  - [ ] ~6 pages

#### Friday: Neutron Barrier + Status Boxes
- [ ] **Derivation 4: Neutron Barrier Height B** (Ch 5)
  - [ ] Potential V(y) form
  - [ ] Turning points
  - [ ] WKB integral B = ∫√(2m(E-V))dy
  - [ ] ~4 pages

- [ ] Create status box for m_p/m_e (use template)
- [ ] Create status box for α
- [ ] Create status box for sin²θ_W

### Week 4: More Derivations + Boxes Ch 5-11

#### Monday-Tuesday: KK Mode Derivation
- [ ] **Derivation 5: 8 Gluons from KK Modes** (Ch 4)
  - [ ] Z₆ mode structure
  - [ ] Zero mode counting
  - [ ] Show 3×3 - 1 = 8
  - [ ] ~5 pages

#### Wednesday: Additional Mechanism Boxes
- [ ] Box 6.1: Z₆ Partition → Weinberg Angle
- [ ] Box 9.1: Neutrino Edge Mode (detailed version)
- [ ] Box 10.1: V-A Chirality (if not already in Ch 10)
- [ ] 2-3 more boxes as needed (Ch 7, 11)

#### Thursday-Friday: Book 1 Integration
- [ ] Add Book 1 reference boxes throughout:
  - [ ] "Book 1 Established: m_p/m_e" (Ch 3)
  - [ ] "Book 1 Established: proton structure" (Ch 4)
  - [ ] "Book 1 Established: α formula" (Ch 3)
- [ ] Verify all Book 1 citations correct
- [ ] Add "See Book 1, Ch X, Sec Y" references

---

## PHASE 3: POLISH & VISUAL AIDS (Week 5-6)

### Week 5: Status Boxes + Diagrams

#### Monday-Tuesday: Status Boxes (All Results)
- [ ] Status box: m_p/m_e (Ch 3)
- [ ] Status box: α (Ch 3)
- [ ] Status box: sin²θ_W (Ch 6)
- [ ] Status box: 3 generations (Ch 8)
- [ ] Status box: τ_n (Ch 5)
- [ ] Status box: G_F framework (Ch 15)
- [ ] 5-10 more boxes for other results

#### Wednesday-Thursday: Visual Diagrams (Priority)
- [ ] Diagram 1: 5D → 3D Projection (TikZ)
- [ ] Diagram 2: Thick vs Thin Brane (side-by-side)
- [ ] Diagram 3: Y-Junction Geometry (3D view)
- [ ] Diagram 4: Z₆ Hexagonal Lattice
- [ ] Diagram 5: G_F Derivation Chain (flowchart)
- [ ] Diagram 6: OPR Dependency Graph
- [ ] Diagram 7: Three Generation Counting (visual)
- [ ] Diagram 8: Parameter Ledger (table with colors)

#### Friday: More Diagrams
- [ ] Diagram 9: Edge Mode Wavefunction
- [ ] Diagram 10: Mode Overlap Schematic
- [ ] Diagram 11: V-A Chirality Separation
- [ ] Diagram 12: Energy Flow Pipeline
- [ ] Diagram 13: Falsification Channels (decision tree)
- [ ] Diagram 14: Asymmetric Y-Junction (neutron)
- [ ] Diagram 15: Z₃ Quotient Structure

### Week 6: Cross-References + Bibliography

#### Monday-Tuesday: Cross-Reference Audit
- [ ] Verify all \ref{sec:...} work
- [ ] Verify all \ref{eq:...} work
- [ ] Verify all \ref{fig:...} work
- [ ] Verify all \ref{tab:...} work
- [ ] Check Table~\ref{tab:baseline_constants} everywhere
- [ ] Check OPR references point to Appendix

#### Wednesday: Bibliography
- [ ] Add all PDG 2024 citations
- [ ] Add all CODATA 2022 citations
- [ ] Add Book 1 self-citation
- [ ] Add relevant papers (weak sector, etc.)
- [ ] Format bibliography (bibtex)
- [ ] Verify all \cite{} compile

#### Thursday-Friday: Index Generation
- [ ] Mark index entries (\index{...})
  - [ ] All parameters (σ, δ, g₅, etc.)
  - [ ] All results (m_p/m_e, α, etc.)
  - [ ] All concepts (frozen regime, edge mode, etc.)
  - [ ] All particles (proton, neutron, neutrino, etc.)
- [ ] Generate index (makeindex)
- [ ] Verify index entries correct

---

## PHASE 4: REVIEW & CORRECTIONS (Week 7)

### Monday: Full Read-Through
- [ ] Read Bridge Ch 0 → check flow
- [ ] Read Part I (Ch 1-5) → check learning curve
- [ ] Read Part II (Ch 6-11) → check predictions clear
- [ ] Read Part III (Ch 12-16) → check technical clarity
- [ ] Read Epilogue (Ch 17)
- [ ] Note any awkward transitions
- [ ] Note any forward references that don't pay off

### Tuesday: Technical Verification
- [ ] Check ALL equations compile
- [ ] Verify dimensional analysis correct
- [ ] Check numerical values match baseline table
- [ ] Verify error percentages calculated correctly
- [ ] Check all [tag] assignments
- [ ] Verify C_red appears where needed

### Wednesday: Epistemic Tag Audit
- [ ] Search for ALL [Dc] tags → verify conditional on C_red
- [ ] Search for ALL [Der] tags → verify no PDG mapping
- [ ] Search for ALL [Open] tags → verify in OPR appendix
- [ ] Check subtags [Dc:Sym], [Der:Num], etc. used correctly
- [ ] Verify no conflicting tags (same result different tags)
- [ ] Generate tag consistency report

### Thursday: Language Audit
- [ ] Search for "predicts" → replace with "yields" (if reduction incomplete)
- [ ] Search for "verified" → replace with "matches" (if error budget open)
- [ ] Search for "proves" → replace with "shows" or "derives"
- [ ] Search for "certain" → add qualifiers
- [ ] Check all "within EDC framework" caveats present
- [ ] Verify conservative tone throughout

### Friday: Final Corrections + PDF Generation
- [ ] Fix all issues from Mon-Thu
- [ ] Final spell check
- [ ] Final compilation test
- [ ] Generate PDF (all chapters)
- [ ] Check PDF for:
  - [ ] TOC complete
  - [ ] All figures render
  - [ ] All cross-references work
  - [ ] Bibliography formatted
  - [ ] Index at end
- [ ] Archive final version
- [ ] Create backup

---

## QUALITY GATES (Must Pass Before Next Phase)

### Gate 1 (End of Week 2): Structure Complete
- [ ] All 17 chapter files created
- [ ] Bridge Ch 0 complete with epistemic standard
- [ ] Ch 1 reorganized (50 pages, τ_n front-loaded)
- [ ] OPR chapters outlined (12-15)
- [ ] Baseline constants table integrated

### Gate 2 (End of Week 4): Core Content Added
- [ ] 10+ "5D Mechanism" boxes written
- [ ] 5 critical derivations completed:
  - [ ] ℓ_p/r_e = 2π³
  - [ ] (4π + 5/6)
  - [ ] sin²θ_W RG
  - [ ] Neutron barrier B
  - [ ] 8 gluons KK
- [ ] Book 1 integration sections added
- [ ] Main text ~500 pages

### Gate 3 (End of Week 6): Polish Complete
- [ ] All status boxes added
- [ ] 15 visual diagrams created
- [ ] Cross-references verified
- [ ] Bibliography complete
- [ ] Index generated

### Gate 4 (End of Week 7): Publication Ready
- [ ] Technical review passed
- [ ] Epistemic tag audit passed
- [ ] Language audit passed
- [ ] PDF compiles cleanly
- [ ] No broken references
- [ ] Ready for external review

---

## CRITICAL REMINDERS

### Before Starting
- [ ] Read FINAL_REORGANIZATION_PLAN.md completely
- [ ] Read FINAL_EPISTEMIC_STANDARD.tex
- [ ] Understand 5D→3D paradigm
- [ ] Know epistemic tag system

### During Work
- [ ] Use templates for ALL new content
- [ ] Tag EVERY result with [Dc]/[Der]/etc.
- [ ] Include C_red where normalization relevant
- [ ] Add error budgets to major results
- [ ] Write 5D mechanism boxes for key concepts
- [ ] Reference Book 1, don't re-derive

### Before Finishing
- [ ] Verify tag consistency
- [ ] Check conservative language
- [ ] Test all cross-references
- [ ] Generate final PDF
- [ ] Archive everything

---

## RISK MITIGATION

### If Behind Schedule
**Priority cuts** (in order):
1. Reduce number of mechanism boxes (20 → 15)
2. Defer some Priority 2 derivations
3. Simplify some diagrams
4. Reduce epilogue length

**Never cut**:
- Bridge Ch 0 epistemic standard
- Ch 1 reorganization
- Critical derivations (Priority 1)
- OPR consolidation
- Tag audit

### If Technical Issues
**Common problems**:
- LaTeX compilation errors → check package versions
- Cross-reference broken → verify label consistency
- Figures not rendering → check file paths
- Bibliography issues → verify bibtex format

**Escalation**:
- Document issue in `/issues/` directory
- Note blocking chapters
- Seek help if > 1 day blocked

---

## SUCCESS METRICS

### Quantitative
- [ ] Total pages: 550-580
- [ ] Learning curve: result in first 20 pages ✓
- [ ] Mechanism boxes: ≥15 added
- [ ] Derivations completed: ≥5 critical ones
- [ ] Diagrams: ≥12 created
- [ ] Tag audit: 0 inconsistencies

### Qualitative
- [ ] Reads smoothly (feedback from test reader)
- [ ] 5D mechanisms always clear
- [ ] Mathematics complete (no missing steps)
- [ ] Epistemic honesty maintained
- [ ] Professional appearance

---

## COMPLETION CRITERIA

Book 2 reorganization is COMPLETE when:

1. ✅ All 17 chapters written and compiled
2. ✅ Bridge Ch 0 with epistemic standard integrated
3. ✅ Minimum 5 critical derivations added
4. ✅ Minimum 15 "5D Mechanism" boxes added
5. ✅ OPR chapters consolidated (12-15)
6. ✅ All major results have status boxes
7. ✅ Epistemic tag audit passed (0 errors)
8. ✅ Language audit passed (conservative tone)
9. ✅ PDF compiles without errors
10. ✅ Ready for external review

---

**Document End**

**Version**: 1.0  
**Date**: 2026-01-30  
**Status**: Ready for Implementation  
**Next Action**: Begin Phase 1, Week 1, Monday
