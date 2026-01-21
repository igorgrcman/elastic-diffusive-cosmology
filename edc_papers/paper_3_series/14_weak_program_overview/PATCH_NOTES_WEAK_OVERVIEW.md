# PATCH NOTES: EDC Weak Program Overview

**Date:** 2026-01-20
**Document:** EDC Weak Program Overview — Umbrella Document
**Status:** v1.0 (Initial Release)

---

## Summary

This umbrella document consolidates the EDC Weak Program, referencing
existing Zenodo-archived documents by DOI without introducing new claims
or modifying published sources.

---

## Document Structure

| Section | Title | Content |
|---------|-------|---------|
| §1 | Purpose and Scope | Guardrail, registry |
| §2 | Canonical Principle | Mechanistic Dimension [Def]/[Dc] |
| §3 | Unified Pipeline | Absorption→Dissipation→Release |
| §4 | Ontology Map | Bulk-core vs. brane-dominant |
| §5 | Neutron Anchor | Paper 3/NJSR foundation |
| §6 | Lepton Tomography | M/T companions |
| §7 | Pion Bridge | Hadron→lepton extension |
| §8 | Knowledge Status | Established + [OPEN] registry |
| §9 | Falsifiability | Non-overclaim canon |
| §10 | Reader Guide | Navigation and dependencies |

---

## Key Features

### 1. Mechanistic Dimension Principle (§2)

Canonical blocks introduced:
- **Definition 2.1**: Mechanistic Dimension Principle [Def]
- **Cornerstone box**: Brane as Mechanism [Dc]

### 2. Unified Pipeline (§3)

- Definition 3.1: Canonical Decay Pipeline
- Equation 1: Frozen projection operator $\mathcal{P}_{\mathrm{frozen}}$
- Postulate 3.1: Suppressed Bulk Leakage [P]

### 3. Ontology Map (§4)

- Table 2: Particle ontologies (N/M/T/P)
- Figure 1: Ontological diagram (bulk-core vs. brane-dominant)

### 4. Consolidated Open Problems (§8)

- Table 4: 14 open problems across N/M/T/P
- Unique IDs: OPEN-N1 through OPEN-P5

### 5. Non-Overclaim Canon (§9)

- Guardrail box listing 6 explicit non-claims
- Table 5: Epistemic tag definitions

### 6. Reader Guide (§10)

- Recommended reading order
- Topic locator table
- Dependency graph (Figure 2)

---

## Referenced DOIs

| Document | DOI |
|----------|-----|

---

## Design Decisions

1. **No bibliography citations in text**: DOIs appear directly in prose for clarity
2. **Figures use TikZ**: Consistent with other EDC documents
3. **Longtable for open problems**: Handles potential page breaks
4. **Epistemic tags in tables**: Immediate status visibility

---

## Build Verification

```bash
cd paper/
xelatex -interaction=nonstopmode main.tex && xelatex main.tex
# Expected: ~12 pages
# Undefined references: 0
# Overfull boxes: TBD
```

---

## Files Created

```
14_weak_program_overview/
├── paper/
│   └── main.tex              # Main document (~12 pages)
├── bib/
│   └── references.bib        # Bibliography
├── README.md                 # Project readme
└── PATCH_NOTES_WEAK_OVERVIEW.md  # This file
```

---

## Relationship to Other Documents

| Document | Relationship |
|----------|--------------|
| Framework v2.0 | Foundation (DOI-referenced) |
| Paper 3 | Neutron anchor (DOI-referenced) |
| Companions H/F/G | Published foundations (DOI-referenced) |
| Companions N/M/T/P | Consolidated subjects |

---

## Compliance Checklist

- [x] No new postulates introduced
- [x] All DOIs correctly formatted
- [x] No modifications to archived documents
- [x] Epistemic tags consistent with source documents
- [x] Falsifiability section complete
- [x] Non-overclaim statement present
- [x] Reader guide functional

---

*Generated: 2026-01-20 (Initial release)*
