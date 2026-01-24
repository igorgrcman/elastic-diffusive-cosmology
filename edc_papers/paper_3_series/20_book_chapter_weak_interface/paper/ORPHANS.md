# Orphan Files Documentation

This document tracks files that exist in the `paper/` directory but are **NOT** compiled into the main document (`EDC_Part_II_Weak_Sector.tex`).

## Definition

An "orphan file" is a `.tex` file that:
1. Exists in the paper directory tree
2. Is NOT `\input{}` or `\include{}` by any file in the build graph
3. May contain development notes, research targets, or auto-generated content

## Current Orphan Files

### Research Targets (Development Notes)

These are standalone research documents, each with its own `\documentclass`:

| File | Status | Notes |
|------|--------|-------|
| `research_targets/RT-CH3-001_VA_FROM_INFLOW.tex` | **FIXED** | V-A structure from Plenum inflow |
| `research_targets/RT-CH3-001_WORKING_PHASE1.tex` | **FIXED** | Phase 1 working notes |
| `research_targets/RT-CH3-002_GF_FROM_MEDIATOR.tex` | **FIXED** | G_F from 5D mediator integration |
| `research_targets/RT-CH3-002_WORKING_PHASE1.tex` | **FIXED** | Asymmetric thick-brane profile |
| `research_targets/RT-CH3-002_WORKING_PHASE2.tex` | **FIXED** | G_F derivation Phase 2 |
| `research_targets/RT-CH3-002_WORKING_PHASE3.tex` | **CLEAN** | Weak coupling derivation (no z) |
| `research_targets/RT-CH3-002_WORKING_PHASE4.tex` | **CLEAN** | Weinberg angle derivation (no z) |
| `research_targets/RT-CH3-003_NEUTRON_LIFETIME.tex` | **CLEAN** | Peierls barrier tunneling (no z) |
| `research_targets/RT-CH3-004_LEPTON_MASS_HIERARCHY.tex` | **FIXED** | Mode spectrum hierarchy |
| `research_targets/RT-CH3-005_NEUTRINO_MASS.tex` | **FIXED** | Edge-mode dynamics |
| `research_targets/RT-CH3-006_KOIDE_PHASE.tex` | **CLEAN** | Koide phase derivation (no z) |

**Notation status**: All files with physical 5D coordinate updated to ξ-notation (2026-01-24).

### Auto-Generated Code Outputs

These files are produced by Python scripts and should be regenerated to update:

| File | Generator | Notation |
|------|-----------|----------|
| `code/output/bvp_halfline_phase_table.tex` | `bvp_halfline_phase.py` | Legacy z (update script) |
| `code/output/bvp_halfline_toy_table.tex` | `bvp_halfline_toy.py` | Legacy z (update script) |

See `code/output/README.md` for regeneration instructions.

## Build Graph Reference

For the complete list of files that ARE compiled into the main document, see:
- `BUILD_GRAPH_FILES.txt`

## Maintenance Policy

1. **Research targets**: Update notation manually when editing
2. **Code outputs**: Update generator scripts, then regenerate
3. **New orphans**: Add to this document with status

---
*Last updated: 2026-01-24*
*Notation canon: ξ = 5D physical depth coordinate*
