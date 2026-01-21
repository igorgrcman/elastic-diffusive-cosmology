# Paper 3J: Mechanistic Dimensions in EDC — The Weak-Sector Brane Interface

**Title:** Mechanistic Dimensions in EDC: The Weak-Sector Brane Interface

**Subtitle:** Unified Absorption–Dissipation–Release Pipeline from Neutron to Leptons

**Version:** Paper 3J (Journal Synthesis)

**DOI:** TBD (pending Zenodo upload)

## Purpose

This is the primary journal-style umbrella narrative for the EDC Weak Program;
the "Weak Program Overview" remains an internal registry/index (DOIs + OPEN checklist),
not a superseded publication.

This paper:
1. Consolidates the unified **Absorption → Dissipation → Release** decay pipeline
2. Presents the **ontology map** (bulk-core / brane-dominant / edge mode / composite)
3. Promotes the **G_F structural pathway** (OPEN-W1) to visibility
4. Provides the **primary reading path** for the EDC Weak Program

## Document Status

| Section | Status |
|---------|--------|
| §1 Introduction | Complete |
| §2 Unified Decay Pipeline | Complete |
| §3 Ontology Regimes | Complete |
| §4 Case Studies (N,M,T,P,L,V) | Complete |
| §5 G_F Structural Pathway | Complete |
| §6 Quantitative Summary | Complete |
| §7 Discussion | Complete |
| §8 Conclusion | Complete |
| Fig A (Pipeline) | Complete |
| Fig B (Ontology Map) | Complete |

## Build Instructions

```bash
cd paper
xelatex -interaction=nonstopmode main.tex
biber main
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
```

Or with latexmk:
```bash
latexmk -xelatex -interaction=nonstopmode main.tex
```

## Dependencies

This paper references and builds upon:

| Document | DOI | Role |
|----------|-----|------|

## Key Contributions

1. **Unified Pipeline** (Fig. 1): Shows how all weak decays follow the same
   bulk-trigger → brane-dissipation → observer-projection sequence.

2. **Ontology Map** (Fig. 2): Classifies particles by their 5D localization:
   - Bulk-core: neutron (junction oscillator)
   - Brane-dominant: charged leptons (mode index ordering)
   - Edge mode: neutrino (interface excitation)
   - Composite: pion (hadron-to-lepton bridge)

3. **G_F Pathway**: Demonstrates structural scaling G_EDC ~ g_eff²/m_φ²
   from geometric suppression (not a fundamental vertex).

## Figures

- `figures/fig_unified_pipeline.tex` — TikZ source for the decay pipeline
- `figures/fig_ontology_map.tex` — TikZ source for the ontology/dependency map

## Changelog

See `PATCH_NOTES_PAPER3_2_0.md` for detailed history.
