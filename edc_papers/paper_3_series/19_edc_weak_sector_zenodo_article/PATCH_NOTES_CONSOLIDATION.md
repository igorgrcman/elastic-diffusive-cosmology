# PATCH NOTES: EDC Weak Sector Consolidation

**Date:** 2026-01-21

## Summary

This document consolidates the entire EDC Weak Program into a single coherent
Zenodo article, replacing the previous multi-document structure.

## What Was Consolidated

Content merged from the following sources:

| Source | Contribution |
|--------|--------------|
| Paper 3J (Paper 3-2.0) | Title, abstract, overall structure |
| Companion N | Neutron case study, bulk-core junction ontology |
| Companion M | Muon case study, brane-dominant excitation |
| Companion T | Tau case study, higher mode spectrum |
| Companion P | Pion case study, composite ontology, helicity suppression |
| Companion L | Electron ontology, brane defect |
| Companion V | Neutrino ontology, edge mode, chirality filter |
| OPEN-W1 | G_F structural pathway |
| Weak Program Overview | Registry structure (now internalized) |

## What Was Removed

- All Zenodo DOI references (previous DOIs deprecated)
- DOI registry tables
- "Internal QA" / audit language from public text
- Redundant pipeline explanations (unified into §3)
- Redundant ontology definitions (unified into §2)

## What Was Kept

- All physics content (mechanistic narration, epistemic tagging)
- Projection operator formalism (P_frozen decomposition)
- Case study details for each particle
- G_F structural pathway (no numerical closure)
- Falsifiability criteria
- Open problem list

## Structure

```
§1 Scope and Empirical Baselines
   - Scope guardrail
   - Baseline table (PDG/CODATA values)
   - What framework provides
   - What remains open

§2 Mechanistic Dimension Principle
   - Definition of mechanistic dimensions
   - Brane as interface
   - Language precision (canonical vocabulary)
   - Ontological categories

§3 Unified Decay Pipeline
   - Absorption → Dissipation → Release
   - Pipeline diagram (TikZ)
   - Energy ledger
   - Universality table

§4 Projection Operators
   - P_frozen = P_energy ∘ P_mode ∘ P_chir
   - Each operator defined
   - Helicity suppression from chirality

§5 Case Studies
   - Neutron (bulk-core junction)
   - Muon (brane-dominant fundamental)
   - Tau (brane-dominant higher mode)
   - Pion (brane-dominant composite)
   - Electron (brane defect)
   - Neutrino (edge mode)

§6 Structural Pathway to G_F
   - Effective Lagrangian form
   - G_EDC ~ g_eff²/m_φ²
   - Decomposition of g_eff
   - No-fit declaration
   - Closure targets

§7 Falsifiability and Epistemic Boundaries
   - Six falsifiability criteria
   - Specific failure modes
   - Epistemic status table
   - Honest uncertainty

§8 Open Problems
   - Numerical closures (lifetimes, G_F magnitude)
   - Mass spectrum (e, μ, τ, π, ν)
   - Structural completions (helicity, V-A, flavor mixing)
   - Extended scope (quark confinement, CP violation)
   - Priority ranking
```

## Files Created

- `paper/main.tex` — Main document (~25 pages when compiled)
- `paper/sections/01_scope.tex` — Scope and baselines
- `paper/sections/02_mechanism.tex` — Mechanistic dimension principle
- `paper/sections/03_pipeline.tex` — Unified pipeline
- `paper/sections/04_operators.tex` — Projection operators
- `paper/sections/05_cases.tex` — Case studies
- `paper/sections/06_gf_pathway.tex` — G_F structural pathway
- `paper/sections/07_falsifiability.tex` — Falsifiability
- `paper/sections/08_open.tex` — Open problems
- `figures/fig_pipeline.tex` — Pipeline TikZ diagram
- `bib/references.bib` — External references only
- `README.md` — Build instructions
- `PATCH_NOTES_CONSOLIDATION.md` — This file

## DOI Cleanup

All strings matching `10.5281/zenodo.*` have been removed from the consolidated
article. The bibliography contains only external references (PDG, CODATA, etc.).

Previous companion DOIs are deprecated and should not be cited in new work.
This consolidated article is the canonical source for EDC Weak Sector content.

---

*Generated: 2026-01-21 (Consolidation release)*
