# V7.9 FILE INVENTORY

**Created**: 2026-01-31
**Purpose**: Catalog all derivation files scanned for integration

---

## Target File

| File | Path | Lines | Status |
|------|------|-------|--------|
| compile_topological_pinning.tex | src/derivations/ | 49 | Wrapper, includes missing file |

---

## Derivation Files Scanned

### Primary (Directly Relevant)

| File | Lines | Relevance | Integration Use |
|------|-------|-----------|-----------------|
| `M6_TOPOLOGICAL_MODEL_EXPLORATION.md` | 473 | **HIGH** — Core M6 model, pinning constant K, toy Hamiltonian | Basis for Sections 1-2 |
| `M6_PINNING_CONSTANT_DERIVATION.md` | ~200 | MEDIUM — K ≈ 1 MeV derivation | Supporting reference |
| `M6_MODEL_SUMMARY.md` | ~100 | MEDIUM — Condensed M6 summary | Cross-check |
| `M6_GEOMETRY_DERIVATION.md` | ~150 | LOW — Geometric details | Not used |

### Secondary (Context)

| File | Lines | Relevance | Integration Use |
|------|-------|-----------|-----------------|
| `NEUTRON_LIFETIME_NARRATIVE_SYNTHESIS.md` | ~300 | MEDIUM — Neutron decay narrative | Background check |
| `Z3_SYMMETRY_ANALYSIS_NEUTRON.md` | ~250 | LOW — Z₃ symmetry focus | Not directly used |
| `V_B_FROM_Z3_BARRIER_CONJECTURE.md` | ~200 | LOW — Barrier conjecture | Background |
| `compile_neutron_section.tex` | 500+ | LOW — Different topic (neutron) | Not used |

### Tertiary (Unrelated)

| File | Relevance | Reason |
|------|-----------|--------|
| `DERIVE_*.md` files | NOT RELEVANT | Focus on L₀, κ, Ω₀ derivations |
| `M6_*_ANALYSIS.md` files | NOT RELEVANT | He-4, Li-6, Be-8 specific |
| `INSTANTON_*.md` | NOT RELEVANT | Instanton chain, different topic |

---

## Audit Packages Scanned (V7.x)

### V7.4: α100 Dataset [SOURCE]

| File | Lines | Key Content | Used |
|------|-------|-------------|------|
| `06_GN_FIT_V7_4.md` | 230 | g = -0.31 ± 0.11, p = 0.006 | **YES** (lines 82-106) |
| `07_RESIDUALS_DN_CORRELATION_V7_4.md` | ~150 | d(n) correlation details | Reference |
| `04_ALPHA100_DATASET.csv` | 106 rows | Raw data | Reference |

### V7.5: Generalization [SOURCE]

| File | Lines | Key Content | Used |
|------|-------|-------------|------|
| `04_CV_PREDICTIVE_GAIN.md` | ~100 | Cross-validation results | **YES** |
| `05_PERMUTATION_TEST.md` | ~100 | p_perm < 0.001 | **YES** |
| `06_ROBUST_REGRESSION.md` | ~100 | Huber stable | **YES** |
| `00_README.md` | ~80 | Summary | Reference |

### V7.6.1: Sign Resolution [SOURCE]

| File | Lines | Key Content | Used |
|------|-------|-------------|------|
| `01_TEST_BARRIER_vs_PREFACTOR.md` | 234 | T1-T3 tests, prefactor wins | **YES** (lines 162-217) |
| `00_README.md` | ~50 | Verdict: PREFACTOR | Reference |

### V7.7: Prefactor Mechanism [SOURCE]

| File | Lines | Key Content | Used |
|------|-------|-------------|------|
| `04_PREFACTOR_MECHANISM_MODEL.md` | 203 | λ = ν × P × S_α | **YES** (lines 9-21, 95-126) |
| `07_FORBIDDEN_ALTERNATIVES_BEYOND_M43.md` | 303 | Mechanism × n matrix | **YES** (lines 35-48) |
| `06_CRYSTAL_DEFECT_ANALOGY.md` | ~150 | Crystal analogy | **YES** (for [P] interpretation) |
| `10_OPEN_QUESTIONS_V7_7.md` | ~100 | Kingpins | **YES** |

### V7.8: Proxy Controls [SOURCE]

| File | Lines | Key Content | Used |
|------|-------|-------------|------|
| `07_FIT_RESULTS_V7_8.md` | 234 | M0-M7 tables, g robust | **YES** (lines 56-71, 126-131, 189-206) |
| `08_MEDIATION_AND_INTERPRETATION.md` | 193 | Mediation analysis | **YES** (lines 70-89) |
| `10_OPEN_QUESTIONS_V7_8.md` | ~200 | Updated kingpins | **YES** |
| `00_README.md` | 132 | Executive summary | Reference |

---

## Dependency Map

```
compile_topological_pinning.tex
    └── BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex [MISSING → CREATE]
            ├── Section 1-2: ← M6_TOPOLOGICAL_MODEL_EXPLORATION.md
            ├── Section 3: ← V7.4-V7.8 audit packages
            ├── Section 4: ← V7.7 falsification tests
            └── Section 5: ← V7.8 open questions
```

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Derivation .tex files | 2 |
| Derivation .md files scanned | 26 |
| V7.x audit packages used | 5 (V7.4, V7.5, V7.6.1, V7.7, V7.8) |
| V7.x files directly cited | 11 |
| New files to create | 1 (BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex) |

