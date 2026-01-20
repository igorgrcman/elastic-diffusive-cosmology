# EDC Weak Program Overview

**Version:** 1.0
**Date:** 2026-01-20
**Status:** Umbrella/consolidation document

---

## Purpose

This document provides a unified overview of the EDC (Elastic Diffusive Cosmology)
Weak Program—a coordinated investigation of weak-sector phenomenology within the
thick-brane microphysics framework.

**Key characteristics:**
- **Consolidation only**: No new claims introduced
- **DOI-referenced**: All technical content cites archived sources
- **No retro-edits**: Published companions remain unchanged

---

## What This Document Covers

| Section | Content |
|---------|---------|
| §1 | Purpose, scope guardrail, document registry |
| §2 | Canonical principle: extra dimensions as mechanism |
| §3 | Unified pipeline: Absorption → Dissipation → Release |
| §4 | Ontology map: bulk-core vs. brane-dominant |
| §5 | The neutron anchor |
| §6 | Lepton spectrum tomography (μ, τ) |
| §7 | The pion bridge (hadron→lepton) |
| §8 | Consolidated knowledge status + open problems |
| §9 | Falsifiability and non-overclaim canon |
| §10 | Practical reader guide |

---

## Referenced Documents

| Document | DOI | Status |
|----------|-----|--------|
| Framework v2.0 | 10.5281/zenodo.18299085 | Published |
| Paper 3 (NJSR) | 10.5281/zenodo.18262721 | Published |
| Companion H | 10.5281/zenodo.18307539 | Published |
| Companion F | 10.5281/zenodo.18302953 | Published |
| Companion G | 10.5281/zenodo.18303494 | Published |
| Companion N | 10.5281/zenodo.18315110 | v3.0 |
| Companion M | 10.5281/zenodo.18319888 | v0.2 |
| Companion T | 10.5281/zenodo.18319900 | v0.1 |
| Companion P | 10.5281/zenodo.18319913 | v0.3 |
| **This doc** | **10.5281/zenodo.18319921** | v1.0 |

---

## Build Instructions

```bash
cd paper/
xelatex -interaction=nonstopmode main.tex && xelatex main.tex
# Expected: ~12 pages, no undefined references
```

---

## File Structure

```
14_weak_program_overview/
├── README.md                     # This file
├── PATCH_NOTES_WEAK_OVERVIEW.md  # Version history
├── paper/
│   ├── main.tex                  # Main document
│   └── main.pdf                  # Compiled output
└── bib/
    └── references.bib            # Bibliography (DOI references)
```

---

## Design Principles

1. **No new postulates**: All [P] claims reference source companions
2. **No modifications to archived docs**: DOIs are immutable
3. **Reader-first structure**: Practical guide for navigating the program
4. **Epistemic transparency**: Clear tagging of all claims

---

*Generated: 2026-01-20*
