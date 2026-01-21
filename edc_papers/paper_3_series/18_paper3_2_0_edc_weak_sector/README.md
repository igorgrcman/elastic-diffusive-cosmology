# Paper 3-2.0: EDC Weak Sector

**Title:** EDC Weak Sector: Mechanistic Brane Pipeline, Ontology Map, and Structural Pathway to G_F

**Version:** 0.1 (initial release)

**DOI:** TBD (pending Zenodo upload)

## Purpose

Journal-style umbrella document that:
1. Consolidates the unified **Absorption → Dissipation → Release** decay pipeline
2. Presents the **ontology map** (bulk-core / brane-dominant / edge mode / composite)
3. Promotes the **G_F structural pathway** (OPEN-W1) to visibility
4. Supersedes the narrative role of the Weak Program Overview (which becomes a registry index)

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
| Framework v2.0 | 10.5281/zenodo.18299085 | Foundation |
| Paper 3 (NJSR) | 10.5281/zenodo.18262721 | Neutron lifetime |
| Companion H | 10.5281/zenodo.18307539 | Thick-brane microphysics |
| Companion F | 10.5281/zenodo.18302953 | Selection rules |
| Companion G | 10.5281/zenodo.18303494 | Gauge emergence |
| Companion N | 10.5281/zenodo.18315110 | Neutron decay |
| Companion M | 10.5281/zenodo.18319888 | Muon decay |
| Companion T | 10.5281/zenodo.18319900 | Tau decay |
| Companion P | 10.5281/zenodo.18319913 | Pion decay |
| Companion L | 10.5281/zenodo.18321357 | Electron as brane defect |
| Companion V | 10.5281/zenodo.18321383 | Neutrino as edge mode |
| OPEN-W1 | 10.5281/zenodo.18321396 | G_F toy derivation |

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
