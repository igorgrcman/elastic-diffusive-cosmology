# PATCH NOTES — Paper 3-2.0: EDC Weak Sector

## v0.1 (2026-01-20)

**Initial Release**

### Created Files
- `paper/main.tex` — Journal-style umbrella document (~800 lines, 8 sections)
- `figures/fig_unified_pipeline.tex` — TikZ: Absorption → Dissipation → Release pipeline
- `figures/fig_ontology_map.tex` — TikZ: Ontology categories and document dependencies
- `bib/references.bib` — 16 DOI entries (12 EDC + 2 baseline + 2 OPEN)
- `README.md` — Build instructions and dependency table

### Structure

```
18_paper3_2_0_edc_weak_sector/
├── README.md
├── PATCH_NOTES_PAPER3_2_0.md
├── paper/
│   └── main.tex
├── figures/
│   ├── fig_unified_pipeline.tex
│   └── fig_ontology_map.tex
└── bib/
    └── references.bib
```

### Document Sections

| # | Section | Content |
|---|---------|---------|
| 1 | Introduction | Scope, audience, document map |
| 2 | Unified Decay Pipeline | Three-stage flow, P_frozen decomposition |
| 3 | Ontology Regimes | Bulk-core, brane-dominant, edge mode, composite |
| 4 | Case Studies | N, M, T, P, L, V — one page each |
| 5 | G_F Structural Pathway | OPEN-W1 promotion, no-fit policy |
| 6 | Quantitative Summary | Agreement table (τ_n, Γ_μ, Γ_π, etc.) |
| 7 | Discussion | Model scope, limitations, open problems |
| 8 | Conclusion | Summary and outlook |

### Key Features

1. **Physical Narration Rule** — Every key equation has mechanistic explanation
2. **Epistemic Tags** — [BL], [Def], [P], [Dc], [OPEN] throughout
3. **No-Fit Policy** — Explicit statement that EDC parameters are NOT tuned to SM values
4. **Complete DOI Registry** — All 12 EDC documents + baselines cited

### Figures

**Figure 1 (Unified Pipeline):**
- Three-stage horizontal flow: Absorption (red) → Dissipation (yellow) → Release (green)
- P_frozen decomposition: P_energy, P_mode, P_chir sub-operators
- Brane layer indicator showing bulk/brane/observer regions

**Figure 2 (Ontology Map):**
- Color-coded regions for particle categories
- Document nodes (Comp. N, L, M, T, V, P, OPEN-W1)
- Dependency arrows showing build-upon relationships
- Structural pathway indicated with dashed arrows

### Build Verification

- [x] xelatex ×3 compiles without errors
- [x] No undefined references
- [x] No undefined citations
- [x] TikZ figures render correctly
- [x] Output: 16 pages PDF

### Supersedes

This document supersedes the **narrative role** of:
- `14_weak_program_overview/` (which becomes a pure registry index)

The Overview remains as a quick-reference table; Paper 3-2.0 provides the unified narrative.

---

## Future Updates (Planned)

- v0.2: Add numerical values to quantitative summary table
- v0.3: Expand G_F pathway section after OPEN-W2 completion
- v1.0: Journal submission version (after G_F derivation complete)
