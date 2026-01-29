# Claim Ledger — Part II: The Weak Interface

**Version:** 1.0
**Created:** 2026-01-22
**Purpose:** Machine-parseable claim database for Part II

---

## Status Legend

| Status | Meaning |
|--------|---------|
| GREEN | Derived/verified with explicit calculation |
| YELLOW | Mechanism identified, quantitative closure incomplete |
| RED | Open problem, not yet derived |
| FALSIFIED | Specific approach tested and shown to fail |

---

## Chapter 3: Electroweak Parameters

### CL-3.1: sin²θ_W = 1/4 (bare)

```yaml
id: CL-3.1
status: GREEN
chapter: 3
claim: "sin²θ_W = 1/4 (bare) from |Z₂|/|Z₆| = 2/6"
evidence:
  equation: "eq:ch3_sin2_bare"
  file: "sections/05_three_generations.tex"
  line: ~180
tag: "[Der]"
commit: "early"
notes: "True EDC prediction from Z₆ subgroup counting"
```

### CL-3.2: sin²θ_W(M_Z) after RG

```yaml
id: CL-3.2
status: GREEN
chapter: 3
claim: "sin²θ_W(M_Z) = 0.2314 after RG running (0.08% from PDG)"
evidence:
  equation: "eq:ch3_sin2_mz"
  file: "sections/05_three_generations.tex"
  table: "Table 3.1"
tag: "[Dc]"
commit: "aba4822"
notes: "Standard QFT RG, not EDC-specific"
```

### CL-3.3: g² from α and sin²θ_W

```yaml
id: CL-3.3
status: GREEN
chapter: 3
claim: "g² = 4πα/sin²θ_W = 0.4246 (1.1% from PDG)"
evidence:
  equation: "eq:ch3_g2"
  file: "sections/05_three_generations.tex"
tag: "[Dc]"
notes: "Electroweak unification relation"
```

### CL-3.4: G_F consistency closure

```yaml
id: CL-3.4
status: YELLOW
chapter: 3
claim: "G_F = g²/(4√2 M_W²) numerical closure"
evidence:
  equation: "eq:ch11_gf_ew"
  file: "sections/11_gf_derivation.tex"
tag: "[Dc]"
notes: "⚠️ Uses v which depends on G_F — circularity caveat applies"
```

---

## Chapter 5: Three Generations

### CL-5.1: N_g = 3 from Z₆

```yaml
id: CL-5.1
status: GREEN
chapter: 5
claim: "N_g = |Z₃| = 3 generations from Z₆/Z₂ quotient"
evidence:
  equation: "eq:ch5_Ng_3"
  file: "sections/05_three_generations.tex"
tag: "[Der]"
notes: "Direct counting from discrete symmetry structure"
```

### CL-5.2: Flavor as Z₃ label

```yaml
id: CL-5.2
status: YELLOW
chapter: 5
claim: "Flavor = Z₃ cyclic label on S¹_ξ positions"
evidence:
  file: "sections/05_three_generations.tex"
tag: "[I]"
notes: "Geometric interpretation, not unique mapping"
```

---

## Chapter 6: Neutrino Oscillations (PMNS)

### CL-6.1: PMNS from edge delocalization

```yaml
id: CL-6.1
status: YELLOW
chapter: 6
claim: "PMNS angles from edge-mode delocalization"
evidence:
  equation: "eq:ch6_pmns_kappa"
  file: "sections/06_neutrinos_edge_modes.tex"
tag: "[P]"
notes: "Broad κ gives large angles; mechanism identified, not quantitative"
```

### CL-6.2: Neutrino mass hierarchy

```yaml
id: CL-6.2
status: RED
chapter: 6
claim: "Neutrino mass hierarchy from bulk depth"
evidence:
  file: "sections/06_neutrinos_edge_modes.tex"
tag: "[P]"
notes: "Not computed — requires 5D BVP solution"
```

---

## Chapter 7: CKM Matrix and CP Violation

### CL-7.1: Z₃ DFT baseline (FALSIFIED)

```yaml
id: CL-7.1
status: FALSIFIED
chapter: 7
claim: "Z₃ DFT baseline gives |V_ij|² = 1/3"
evidence:
  equation: "eq:ch7_dft_ckm"
  file: "sections/07_ckm_cp.tex"
tag: "[Dc]"
commit: "a2e9a6e"
notes: "Correctly computed but ×144 off from PDG — valuable negative result"
falsification_details:
  pdg_vus: 0.225
  model_vus: 0.577
  ratio: 2.56
  conclusion: "Pure Z₃ symmetry insufficient; breaking required"
```

### CL-7.2: Overlap model gives Wolfenstein

```yaml
id: CL-7.2
status: YELLOW
chapter: 7
claim: "Overlap model O_ij ∝ exp(-|Δz|/2κ) gives Wolfenstein λ, λ², λ³"
evidence:
  equation: "eq:ch7_overlap_exp"
  file: "sections/07_ckm_cp.tex"
  table: "Table 7.2"
  code: "code/ckm_overlap_attempt2.py"
tag: "[Dc]/[P]"
commit: "3b1aa94"
notes: "Mechanism works; profile ansatz is [P], overlap calculation is [Dc]"
```

### CL-7.3: Single parameter calibration

```yaml
id: CL-7.3
status: YELLOW
chapter: 7
claim: "Δz/(2κ) = -ln(λ) ≈ 1.49 calibrated to Cabibbo angle"
evidence:
  equation: "eq:ch7_dz_kappa"
  file: "sections/07_ckm_cp.tex"
tag: "[I]"
commit: "3b1aa94"
notes: "Single-parameter identification, not multi-parameter fit"
```

### CL-7.4: CP phase δ

```yaml
id: CL-7.4
status: RED
chapter: 7
claim: "CP phase δ and Jarlskog J from geometry"
evidence:
  file: "sections/07_ckm_cp.tex"
tag: "[P]"
notes: "Not addressed — requires complex phase treatment"
```

---

## Chapter 9: V–A Structure

### CL-9.1: V–A from boundary projection

```yaml
id: CL-9.1
status: GREEN
chapter: 9
claim: "V−A emerges from boundary chirality projection"
evidence:
  equation: "eq:ch9_va_projection"
  file: "sections/09_va_structure.tex"
tag: "[Der]"
notes: "Derived from 5D Dirac equation with ε-boundary BC"
```

### CL-9.2: RH current suppression

```yaml
id: CL-9.2
status: GREEN
chapter: 9
claim: "Right-handed currents forbidden by ε-boundary Neumann BC"
evidence:
  equation: "eq:ch9_rh_suppression"
  file: "sections/09_va_structure.tex"
tag: "[Der]"
notes: "Geometric origin of parity violation"
```

---

## Chapter 11: Fermi Constant from Geometry

### CL-11.1: G_F from EW consistency (GREEN-A)

```yaml
id: CL-11.1
status: GREEN
chapter: 11
claim: "G_F from EW consistency: sin²θ_W → g² → M_W → G_F"
evidence:
  file: "sections/11_gf_derivation.tex"
  notes_file: "CH11_GF_NOTES.md"
tag: "[Dc]"
commit: "b4ff06a"
notes: "GREEN-A level; uses v caveat"
```

### CL-11.2: Mode overlap suppression (YELLOW-B)

```yaml
id: CL-11.2
status: YELLOW
chapter: 11
claim: "Mode overlap suppression explains 'why weak is weak'"
evidence:
  file: "sections/11_gf_derivation.tex"
tag: "[P]"
notes: "YELLOW-B level; OOM estimate only"
```

### CL-11.3: First-principles G_F (RED-C)

```yaml
id: CL-11.3
status: RED
chapter: 11
claim: "First-principles G_F from 5D action"
evidence:
  file: "sections/11_gf_derivation.tex"
tag: "[P]"
notes: "Not achieved — requires g₅, m_φ, BVP solution"
```

---

## Chapter 10: Neutron-Proton Mass Difference

### CL-10.1: Δm_np = 8m_e/π

```yaml
id: CL-10.1
status: YELLOW
chapter: 10
claim: "Δm_np = (8/π)m_e = 1.301 MeV (0.6% from PDG)"
evidence:
  equation: "eq:mass-diff-derived"
  file: "edc_papers/paper_3_series/00_framework_v2_0/paper/main.tex"
  line: 1017-1028
  sensitivity: "docs/DELTA_MNP_SENSITIVITY.md"
tag: "[Dc]"
commit: "2026-01-29"
notes: |
  ROBUST to continuous parameters (σ, δ, L_0, w) — they don't enter independently.
  FRAGILE to discrete structure (Z_6 → Z_N would change 36 → N²).
  Depends on 3 [Dc] assumptions:
  1. Charge-angle coupling θ = (1-Q)×60°
  2. V ∝ q² elastic ansatz
  3. Z_6 ring normalization σr_e² = (36/π)m_e
  Cross-check: (5/2 + 4α)m_e from Ch.9 gives 0.7% different value.
```

### CL-10.2: Sensitivity Analysis (DONE)

```yaml
id: CL-10.2
status: GREEN
chapter: 10
claim: "Δm_np robustness: ROBUST to σ/δ/L_0/w; FRAGILE to Z_6 structure"
evidence:
  file: "docs/DELTA_MNP_SENSITIVITY.md"
tag: "[M]"
commit: "2026-01-29"
notes: "Sensitivity analysis complete. No continuous parameter dependence found."
```

---

## Statistics

| Status | Count |
|--------|-------|
| GREEN | 8 |
| YELLOW | 7 |
| RED | 3 |
| FALSIFIED | 1 |
| **Total** | **19** |

---

*Claim Ledger v1.1 — Last updated 2026-01-29*
