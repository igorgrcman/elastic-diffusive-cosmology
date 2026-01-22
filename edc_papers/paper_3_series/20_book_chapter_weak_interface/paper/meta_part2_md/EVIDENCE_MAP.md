# Evidence Map — Part II: The Weak Interface

**Version:** 1.0
**Created:** 2026-01-22
**Purpose:** Cross-reference claims to source files and equations

---

## Source File Index

### Main Chapters

| File | Chapter | Key Content |
|------|---------|-------------|
| `sections/00_reader_contract.tex` | Preface | Reader contract, what Part II delivers |
| `sections/01_how_we_got_here.tex` | 1 | Part I recap, Z₆ emergence |
| `sections/02_geometry_interface.tex` | 2 | Weak interface geometry, throat structure |
| `sections/03_unified_pipeline.tex` | 3 | Unified pipeline: geometry → chirality → observable |
| `sections/04_ontology.tex` | 4 | Particle ontology in 5D |
| `sections/05_three_generations.tex` | 5 | N_g = 3, sin²θ_W = 1/4 |
| `sections/06_neutrinos_edge_modes.tex` | 6 | Neutrinos as edge modes, PMNS |
| `sections/07_ckm_cp.tex` | 7 | CKM matrix, CP violation |
| `sections/09_va_structure.tex` | 9 | V–A from chirality projection |
| `sections/11_gf_derivation.tex` | 11 | G_F from geometry |

### Companion Notes

| File | Content |
|------|---------|
| `CH7_CKM_CP_NOTES.md` | CKM development log, Attempt 1 & 2 |
| `CH11_GF_NOTES.md` | G_F derivation levels, circularity discussion |

### Code

| File | Purpose |
|------|---------|
| `code/ckm_overlap_attempt2.py` | CKM overlap model numerical demo |

---

## Key Equation Labels

### Chapter 3: Electroweak Parameters

| Label | Equation | Content |
|-------|----------|---------|
| `eq:ch3_sin2_bare` | (3.12) | sin²θ_W = \|Z₂\|/\|Z₆\| = 1/4 |
| `eq:ch3_sin2_mz` | (3.15) | sin²θ_W(M_Z) = 0.2314 after RG |
| `eq:ch3_g2` | (3.18) | g² = 4πα/sin²θ_W |

### Chapter 5: Three Generations

| Label | Equation | Content |
|-------|----------|---------|
| `eq:ch5_Ng_3` | (5.8) | N_g = \|Z₆/Z₂\| = 3 |
| `eq:ch5_flavor_z3` | (5.12) | Flavor as Z₃ cyclic label |

### Chapter 7: CKM Matrix

| Label | Equation | Content |
|-------|----------|---------|
| `eq:ch7_dft_ckm` | (7.5) | DFT baseline \|V_ij\|² = 1/3 |
| `eq:ch7_epsilon_def` | (7.8) | Breaking amplitude ε = 1 - V_ii |
| `eq:ch7_overlap_exp` | (7.18) | O_ij ∝ exp(-\|Δz\|/2κ) |
| `eq:ch7_dz_kappa` | (7.22) | Δz/(2κ) = -ln(λ) ≈ 1.49 |

### Chapter 9: V–A Structure

| Label | Equation | Content |
|-------|----------|---------|
| `eq:ch9_va_projection` | (9.8) | V–A from boundary chirality |
| `eq:ch9_rh_suppression` | (9.12) | RH current = 0 from Neumann BC |

### Chapter 11: Fermi Constant

| Label | Equation | Content |
|-------|----------|---------|
| `eq:ch11_gf_ew` | (11.8) | G_F = g²/(4√2 M_W²) |
| `eq:ch11_gf_mediator` | (11.15) | G_F ~ g_eff²/m_φ² (tree level) |

---

## External References

| Reference | Type | Used For |
|-----------|------|----------|
| PDG 2024 | Baseline | CKM values, sin²θ_W, G_F, M_W, masses |
| CODATA 2018 | Baseline | α, ℏ, c, fundamental constants |
| Framework v2.0 | EDC | Canonical bulk–brane statement (Remark 4.5) |
| Paper 2 (α derivation) | EDC | Fine-structure constant derivation |

---

## Claim → Evidence Links

### GREEN Claims

| Claim ID | Evidence Type | Location |
|----------|---------------|----------|
| CL-3.1 | Equation | sections/05_three_generations.tex:~180 |
| CL-3.2 | Table + Equation | sections/05_three_generations.tex, Table 3.1 |
| CL-3.3 | Equation | sections/05_three_generations.tex |
| CL-5.1 | Equation | sections/05_three_generations.tex |
| CL-9.1 | Equation + Chain Box | sections/09_va_structure.tex |
| CL-9.2 | Equation | sections/09_va_structure.tex |
| CL-11.1 | Section | sections/11_gf_derivation.tex, §11.2 |

### YELLOW Claims

| Claim ID | Evidence Type | Location |
|----------|---------------|----------|
| CL-3.4 | Equation + Note | sections/11_gf_derivation.tex (circularity) |
| CL-5.2 | Interpretation | sections/05_three_generations.tex |
| CL-6.1 | Equation | sections/06_neutrinos_edge_modes.tex |
| CL-7.2 | Equation + Code | sections/07_ckm_cp.tex, code/ckm_overlap_attempt2.py |
| CL-7.3 | Equation | sections/07_ckm_cp.tex |
| CL-11.2 | Section | sections/11_gf_derivation.tex, §11.3 |

### RED/FALSIFIED Claims

| Claim ID | Evidence Type | Location |
|----------|---------------|----------|
| CL-6.2 | Open problem | sections/06_neutrinos_edge_modes.tex |
| CL-7.1 | Falsification | sections/07_ckm_cp.tex, Table 7.1 |
| CL-7.4 | Open problem | sections/07_ckm_cp.tex |
| CL-11.3 | Open problem | sections/11_gf_derivation.tex, §11.4 |

---

## Git Commit References

| Commit | Date | Key Changes |
|--------|------|-------------|
| `aba4822` | 2026-01-20 | Ch11 GREEN-A/B/C framework |
| `b4ff06a` | 2026-01-21 | Ch11 reviewer-proof upgrades |
| `a2e9a6e` | 2026-01-22 | Ch7 Attempt 1 (DFT baseline) |
| `3b1aa94` | 2026-01-22 | Ch7 Attempt 2 (overlap model) |

---

*Evidence Map v1.0 — Last updated 2026-01-22*
