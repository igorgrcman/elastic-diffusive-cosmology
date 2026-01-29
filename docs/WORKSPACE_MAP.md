# WORKSPACE MAP (EDC_Project)

> **All paths in this document are repo-relative** (from git repo root).
> External paths use `../EDC_Research_PRIVATE/` notation.

**Generated:** 2026-01-28
**Purpose:** Single entry point for navigating the entire EDC workspace.
**Usage:** Read at START of every CC session. MANDATORY.

---

## P0 Always-read (every session)

| Priority | File | Purpose |
|----------|------|---------|
| 1 | `docs/CANON_BUNDLE.md` | All P0 canonical content in one file |
| 2 | `docs/WORKSPACE_MAP.md` | This file - navigation guide |
| 3 | `docs/CONCEPT_INDEX.md` | Lookup table for key concepts (39 entries) |
| 4 | `docs/KNOWLEDGE_INVENTORY.md` | Complete catalog: derivations, NO-GOs, open problems |
| 5 | `docs/STATUS.md` | Current state of ALL domains |
| 6 | `docs/TODO.md` | Prioritized actions across domains |
| 7 | `docs/SESSION_LOG.md` | Last entry - what was done recently |

---

## Sources of Truth by Domain

### Book 1 (EDC Theory Book v17.49)

| Item | Path |
|------|------|
| **LaTeX root** | `edc_book/main.tex` |
| **Chapters** | `edc_book/chapters/` |
| **Appendices** | `edc_book/appendices/` |
| **Epistemic standard** | `edc_book/EDC_EPISTEMIC_STANDARD.tex` |

**Key chapters:**
- `chapter_0_theory_core_V17.49.tex` - Core theory
- `chapter_3_confinement.tex` - Confinement, Y-junction, proton/neutron geometry
- `chapter_7_gravity.tex` - Gravity from 5D
- `chapter_9_electroweak_v17.48_patched.tex` - Electroweak sector

**Notes:** Book 1 is the PUBLISHED reference (v17.49). Contains geometric proton model (Y-junction) and confinement proof.

---

### Book 2 (Active Development)

| Item | Path |
|------|------|
| **Working root** | `edc_book_2/` |
| **Source derivations** | `edc_book_2/src/derivations/` |
| **Domain-specific docs** | `edc_book_2/docs/` |
| **CLAUDE.md (domain)** | `edc_book_2/CLAUDE.md` |

**Key source files:**
- `src/derivations/BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex` - Active
- `src/derivations/BOOK_SECTION_NEUTRON_LIFETIME.tex` - Active

**Notes:** Book 2 is under active development. Contains Topological Pinning Model, neutron lifetime WKB, frustration-corrected G-N law.

---

### Papers

| Item | Path |
|------|------|
| **Papers root** | `edc_papers/` |
| **Paper 2 (Frozen)** | `edc_papers/paper_2/paper/main.tex` |
| **Paper 2 derivations** | `edc_papers/paper_2/paper/derivations/` |
| **Paper 3 series** | `edc_papers/paper_3_series/` |
| **Paper 3 (private)** | `EDC_Research_PRIVATE/releases/paper_3_private/paper/main.tex` |
| **Paper 3 (public)** | `EDC_Research_PRIVATE/releases/paper_3_public/paper/main.tex` |

**Notes:**
- Paper 2: Frozen boundary criterion, step function, C = 4pi/3
- Paper 3: Neutron lifetime WKB, weak sector V-A structure, sin^2(theta_W) = 1/4

---

### Proton / Neutron Canonical Definitions (DO NOT RE-DERIVE)

| Particle | Source | Location | Status |
|----------|--------|----------|--------|
| **Proton** | Book 1: `chapter_3_confinement.tex` | Section 3.1.1 `\label{subsec:quarks_strings}` | [Der] |
| **Proton** | CANON_BUNDLE | Section 7.2 "Topological Structure" | [Der] |
| **Neutron** | CANON_BUNDLE | Section 7.3 "Neutron" | [Dc] |
| **Neutron** | CANON_BUNDLE | Section 14 "Companion N Plan" | [P/OPEN] |

**Proton definition (canonical):**
```
Topology: Y-junction (3 kraka pod 120deg)
Configuration: S^3 x S^3 x S^3 -> (2pi^2)^3
Charge: W = +1 (total winding)
Color: 3 arms = 3 QCD colors (8 modes = 8 gluons)
Stability: Steiner theorem -> 120deg UNIQUE minimum
```

**Neutron definition (canonical):**
```
Topology: Asymmetric Y-junction (theta = 60deg)
Parameter: q = 1/3 (half-Steiner)
Charge: W = 0, Q = 0
Instability: Can relax theta: 60deg -> 0deg (toward proton)
```

---

### KB / References

| Item | Path |
|------|------|
| **KB root** | `EDC_Research_PRIVATE/kb/` |
| **Turning points** | `EDC_Research_PRIVATE/kb/turning_points/` |
| **5D Universe KB** | `EDC_Research_PRIVATE/kb/5d_universe/` |
| **Anti-patterns** | `EDC_Research_PRIVATE/kb/5d_universe/ANTI_PATTERNS_3D_TRAPS.md` |

**Notes:** KB contains verified findings, anti-patterns (15 critical 3D traps), and turning point documents.

---

### Research Private

| Item | Path |
|------|------|
| **Root** | `EDC_Research_PRIVATE/` |
| **Derivations** | `EDC_Research_PRIVATE/derivations/` |
| **Releases** | `EDC_Research_PRIVATE/releases/` |
| **Domain CLAUDE.md** | `EDC_Research_PRIVATE/CLAUDE.md` |

**Notes:** Contains private research, analytic derivations, release packages for papers.

---

### Other Directories

| Directory | Purpose | Active? |
|-----------|---------|---------|
| `EDC_Book_2/` | Legacy Book 2 location | NO - use `edc_book_2/` |
| `edc_paper_2_archive/` | Archive of Paper 2 development | Archive only |
| `build/` | Build artifacts | Transient |
| `aside_proof_audit/` | Audit materials | Reference |
| `Literatura/` | Literature references | Reference |

---

## Cross-References

| When working on... | Also consult... |
|--------------------|-----------------|
| Book 2 derivations | `docs/CONCEPT_INDEX.md` for canonical definitions |
| Paper 3 weak sector | Book 1 chapter_9 for electroweak foundation |
| Neutron lifetime | Paper 2 frozen criterion, Paper 3 WKB |
| Topological pinning | Book 1 chapter_3 for confinement proof |
| Any 5D calculation | Anti-patterns (15 traps) in CANON_BUNDLE |

---

*Last updated: 2026-01-28*
