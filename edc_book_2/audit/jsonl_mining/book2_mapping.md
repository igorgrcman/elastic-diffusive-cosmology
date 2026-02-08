# Book 2 Mapping: Extracted Derivations to Current Structure

**Generated:** 2026-01-31
**Source reports:** 73d92ff5, 22826edd, 98cc5184 (JSONL mining)
**Target:** reorganized/ (Book 2 v2.0, ~153 pages)

---

## Summary

| Status | Count | Description |
|--------|-------|-------------|
| ALREADY PRESENT | 14 | Content exists in Book 2 with proper tags |
| PARTIAL | 8 | Framework present but details incomplete |
| MISSING | 6 | Content in JSONL but not in Book 2 |

---

## Book 2 Chapter Structure

| Part | Chapter | File | Topic |
|------|---------|------|-------|
| Bridge | 0 | bridge/chapter_0_bridge.tex | Part I connection |
| I | 1 | part1/chapter_01_weak_interface.tex | Weak interface physics |
| I | 2 | part1/chapter_02_ontology.tex | Particle ontology |
| I | 3 | part1/chapter_03_frozen.tex | Frozen regime |
| I | 4 | part1/chapter_04_z6_program.tex | Z6 symmetry program |
| I | 5 | part1/chapter_05_case_studies.tex | Decay case studies |
| II | 6 | part2/chapter_06_electroweak.tex | Electroweak parameters |
| II | 7 | part2/chapter_07_leptons.tex | Lepton masses |
| II | 8 | part2/chapter_08_generations.tex | Generation structure |
| II | 9 | part2/chapter_09_neutrinos.tex | Neutrino physics |
| II | 10 | part2/chapter_10_va_structure.tex | V-A mechanism |
| II | 11 | part2/chapter_11_ckm.tex | CKM matrix |
| III | 12 | part3/chapter_12_gf_chain.tex | G_F derivation chain |
| III | 13 | part3/chapter_13_foundation_params.tex | Foundation parameters |
| III | 14 | part3/chapter_14_bvp.tex | BVP framework |
| III | 15 | part3/chapter_15_mw_gf.tex | M_W and G_F |
| III | 16 | part3/chapter_16_epistemic_summary.tex | Epistemic summary |
| Epilogue | 17 | epilogue/chapter_17_beyond.tex | Future directions |

---

## Detailed Mapping

### 1. Weinberg Angle / sin^2(theta_W) = 1/4

| Item Type | Description | Target Location | Status | Notes |
|-----------|-------------|-----------------|--------|-------|
| EQUATION | sin^2(theta_W) = 1/4 from Z6 | chapter_06_electroweak.tex Sec 2 | ALREADY PRESENT | GAP-4 DONE in TIER-0 |
| DERIVATION | Z6 = Z2 x Z3 partition counting | chapter_06_electroweak.tex Sec 2.1 | ALREADY PRESENT | Explicit |Z2|/|Z6| formula |
| COMPARISON | Tree-level vs PDG (8% diff) | chapter_06_electroweak.tex Sec 2.3 | ALREADY PRESENT | Error budget included |

**JSONL sources:** 22826edd (EQ-0006, EQ-0094, EQ-0227), 73d92ff5 (multiple)

---

### 2. Fermi Constant G_F Chain

| Item Type | Description | Target Location | Status | Notes |
|-----------|-------------|-----------------|--------|-------|
| CHAIN | g5 -> g4 -> G_eff -> G_F | chapter_12_gf_chain.tex | ALREADY PRESENT | GAP-10 DONE in TIER-0 |
| EQUATION | g4 = g5/sqrt(R_xi) | chapter_12_gf_chain.tex Sec 3 | ALREADY PRESENT | Standard KK reduction |
| MECHANISM | Tree-level W exchange | chapter_12_gf_chain.tex Sec 4 | ALREADY PRESENT | Mediator integration box |
| FORMULA | G_eff = g_5^2 l |f_1(0)|^2/(2x_1^2) | chapter_12_gf_chain.tex | PARTIAL | Formula present, numerical incomplete |

**JSONL sources:** 22826edd (EQ-0097, EQ-0205, EQ-0217), 73d92ff5 (extensive)

---

### 3. V-A Mechanism

| Item Type | Description | Target Location | Status | Notes |
|-----------|-------------|-----------------|--------|-------|
| MECHANISM | Chirality filter from 5D | chapter_10_va_structure.tex | ALREADY PRESENT | GAP-1 DONE in TIER-0 |
| DERIVATION | Left-mode localization | chapter_10_va_structure.tex Sec 1-3 | ALREADY PRESENT | Full physical narrative |
| EQUATION | L_weak = psi gamma^mu (1-gamma5) psi W | chapter_10_va_structure.tex Eq 9.2 | ALREADY PRESENT | [BL] tag correct |
| FORMULA | Overlap determines coupling | chapter_10_va_structure.tex Sec 3 | ALREADY PRESENT | Geometric picture complete |

**JSONL sources:** 22826edd (V-A mentions 154 hits), 73d92ff5 (Eqs 49-55)

---

### 4. Neutron Lifetime

| Item Type | Description | Target Location | Status | Notes |
|-----------|-------------|-----------------|--------|-------|
| CALCULATION | tau_n ~ 10^3 s WKB | chapter_05_case_studies.tex Sec 2 | ALREADY PRESENT | Order-of-magnitude |
| BARRIER | V_B ~ 2.6 MeV calibration | chapter_05_case_studies.tex Sec 2.3 | ALREADY PRESENT | [Cal] tag correct |
| GEOMETRY | Y-junction tunneling | chapter_05_case_studies.tex Sec 2.1 | ALREADY PRESENT | 60-deg off-Steiner |
| ERROR BUDGET | V_B, mu, omega_0 sources | chapter_05_case_studies.tex Sec 2.4 | ALREADY PRESENT | Factor-of-2 total |

**JSONL sources:** 73d92ff5 (extensive tunnel calculations), 22826edd (EQ-0239, EQ-0242)

---

### 5. BVP Framework / Robin BC

| Item Type | Description | Target Location | Status | Notes |
|-----------|-------------|-----------------|--------|-------|
| EQUATION | -psi'' + V(y)psi = lambda psi | chapter_14_bvp.tex Eq 14.2 | ALREADY PRESENT | Generic setup |
| BOUNDARY | psi' + kappa psi = 0 | chapter_14_bvp.tex Sec 3 | ALREADY PRESENT | Robin BC mechanism |
| EIGENVALUE | tan(k delta) formula | chapter_14_bvp.tex Eq 14.7 | ALREADY PRESENT | [Der] tag |
| APPLICATION | M_W from lowest eigenvalue | chapter_14_bvp.tex Sec 4.1 | PARTIAL | GAP-12 partial |

**JSONL sources:** 22826edd (BVP 1143 hits), 73d92ff5 (mode equations)

---

### 6. F_bulk/G Relationship (Gravity-Membrane Interface)

| Item Type | Description | Target Location | Status | Notes |
|-----------|-------------|-----------------|--------|-------|
| CONCEPT | F_bulk = plenum gravitational inflow | NOT IN BOOK 2 | MISSING | In Part I, not Part II |
| EQUATION | v(r) = sqrt(2GM/r) | NOT IN BOOK 2 | MISSING | Gravitational sector |
| MECHANISM | Bulk flux couples to brane | bridge/chapter_0_bridge.tex (brief) | PARTIAL | Reference only |

**JSONL sources:** topic_index: F_bulk 10 files, 1404 hits; but weak sector focus

**Note:** F_bulk is primarily Part I (gravitational/cosmological) content, not Part II (weak sector).

---

### 7. Scale Taxonomy / Foundation Parameters

| Item Type | Description | Target Location | Status | Notes |
|-----------|-------------|-----------------|--------|-------|
| TABLE | Delta, delta, l, R_xi definitions | chapter_13_foundation_params.tex Sec 2 | ALREADY PRESENT | Canonical reference |
| DERIVATION | M_0 = sqrt(3)/2 y sqrt(sigma Delta) | chapter_13_foundation_params.tex Eq 13.9 | ALREADY PRESENT | OPR-01 result |
| CONSTRAINT | sigma Delta = 4v^2/3 | chapter_13_foundation_params.tex Eq 13.8 | ALREADY PRESENT | BPS constraint |
| ASSUMPTION | (A1)-(A3) scale identifications | chapter_13_foundation_params.tex Sec 2.1 | ALREADY PRESENT | Explicit labels |

**JSONL sources:** 22826edd (scale definitions throughout)

---

### 8. SSB Mechanism Comparison

| Item Type | Description | Target Location | Status | Notes |
|-----------|-------------|-----------------|--------|-------|
| COMPARISON | SM Higgs SSB vs EDC BVP | chapter_06_electroweak.tex | ALREADY PRESENT | GAP-5 DONE in TIER-1 |
| DICTIONARY | M_W from v vs M_W from eigenvalue | chapter_06_electroweak.tex | PARTIAL | Qualitative present |

**JSONL sources:** 22826edd (SSB references)

---

### 9. Yukawa / Overlap Integrals

| Item Type | Description | Target Location | Status | Notes |
|-----------|-------------|-----------------|--------|-------|
| FORMULA | I_4 = int |f_L|^4 d xi | chapter_07_leptons.tex | ALREADY PRESENT | GAP-11 DONE in TIER-1 |
| DERIVATION | Mass from overlap | chapter_07_leptons.tex | PARTIAL | Explicit formula needs work |
| EQUATION | [I_4] = L^-1 dimensions | chapter_12_gf_chain.tex | ALREADY PRESENT | Dimensional analysis |

**JSONL sources:** 22826edd (EQ-0088, EQ-0089)

---

### 10. Generation Structure / mu-Window

| Item Type | Description | Target Location | Status | Notes |
|-----------|-------------|-----------------|--------|-------|
| CONSTRAINT | mu in [25,35) for N_bound=3 | chapter_08_generations.tex | ALREADY PRESENT | GAP-14 DONE in TIER-1 |
| MECHANISM | KK truncation | chapter_08_generations.tex | ALREADY PRESENT | Explicit |
| FORMULA | mu := M_0 l | chapter_13_foundation_params.tex | ALREADY PRESENT | Canonical definition |

**JSONL sources:** 22826edd (EQ-0111, EQ-0131)

---

### 11. PMNS theta_12

| Item Type | Description | Target Location | Status | Notes |
|-----------|-------------|-----------------|--------|-------|
| CANDIDATE | theta_12 = arctan(1/sqrt(2)) ~ 35.3 deg | chapter_09_neutrinos.tex | ALREADY PRESENT | GAP-8 DONE in TIER-2 |
| COMPARISON | 8.6% from PDG 38.6 deg | chapter_09_neutrinos.tex | ALREADY PRESENT | Error noted |
| MECHANISM | Geometric origin | chapter_09_neutrinos.tex | PARTIAL | Derivation incomplete |

**JSONL sources:** backfill_report_tier2.md

---

### 12. g_5 Reduction Status

| Item Type | Description | Target Location | Status | Notes |
|-----------|-------------|-----------------|--------|-------|
| REDUCTION | g_5 -> g_4 formula | chapter_13_foundation_params.tex | ALREADY PRESENT | GAP-19 partial in TIER-2 |
| STATUS | g_5 itself remains [P] | chapter_13_foundation_params.tex | ALREADY PRESENT | Explicit acknowledgment |
| COMPARISON | SM g also primitive | chapter_13_foundation_params.tex | ALREADY PRESENT | Parity noted |

**JSONL sources:** 22826edd (EQ-0076, EQ-0077)

---

### 13. 5D Bulk Action Components

| Item Type | Description | Target Location | Status | Notes |
|-----------|-------------|-----------------|--------|-------|
| EQUATION | S_bulk = (1/2kappa5^2) int R^5 | chapter_14_bvp.tex (implicit) | PARTIAL | Used but not boxed |
| EQUATION | S_GHY = (1/kappa5^2) int K | chapter_14_bvp.tex (implicit) | PARTIAL | Used but not boxed |
| EQUATION | S_brane = -sigma int sqrt(-h) | chapter_13_foundation_params.tex | PARTIAL | Tension derivation uses |

**JSONL sources:** 73d92ff5 (Eqs 16, 35, 43, 126)

---

### 14. Homotopy / Topological Sector

| Item Type | Description | Target Location | Status | Notes |
|-----------|-------------|-----------------|--------|-------|
| EQUATIONS | pi_n(S^1), pi_n(S^2), pi_n(S^1 x S^2) | NOT IN BOOK 2 | MISSING | In Part I |
| MECHANISM | Charge from pi_1, spin from pi_2 | NOT IN BOOK 2 | MISSING | Ontology in Part I |

**JSONL sources:** 73d92ff5 (Eqs 104-116)

**Note:** Topological classifications are Part I content (chapter_02_ontology references but does not derive).

---

### 15. Induced Metric / Extrinsic Curvature

| Item Type | Description | Target Location | Status | Notes |
|-----------|-------------|-----------------|--------|-------|
| EQUATION | h_mu_nu = g_AB e^A_mu e^B_nu | chapter_14_bvp.tex (implicit) | PARTIAL | BVP uses but does not define |
| EQUATION | K_mu_nu = e^A_mu e^B_nu nabla_A n_B | NOT boxed | MISSING | Technical appendix candidate |

**JSONL sources:** 73d92ff5 (Eq 13)

---

### 16. Golden Ratio Asymptotics

| Item Type | Description | Target Location | Status | Notes |
|-----------|-------------|-----------------|--------|-------|
| EQUATION | alpha_+ = (sqrt(5)-1)/2 = phi-1 | NOT IN BOOK 2 | MISSING | Tail analysis |
| DERIVATION | Bessel asymptotics | NOT IN BOOK 2 | MISSING | Technical appendix candidate |

**JSONL sources:** 73d92ff5 (Eqs 66, 76, 119)

---

## GAP Status Cross-Reference

| GAP-ID | Description | Book 2 Location | Status | Tier |
|--------|-------------|-----------------|--------|------|
| GAP-1 | V-A dictionary | chapter_10_va_structure.tex | DONE | TIER-0 |
| GAP-4 | sin^2(theta_W) partition | chapter_06_electroweak.tex | DONE | TIER-0 |
| GAP-5 | SSB vs EDC | chapter_06_electroweak.tex | DONE | TIER-1 |
| GAP-8 | theta_12 candidate | chapter_09_neutrinos.tex | DONE | TIER-2 |
| GAP-10 | G_F chain | chapter_12_gf_chain.tex | DONE | TIER-0 |
| GAP-11 | Yukawa overlaps | chapter_07_leptons.tex | DONE | TIER-1 |
| GAP-14 | mu-window | chapter_08_generations.tex | DONE | TIER-1 |
| GAP-19 | g_5 reduction | chapter_13_foundation_params.tex | PARTIAL | TIER-2 |
| GAP-2 | V(xi) derivation | chapter_08_generations.tex | OPEN | - |
| GAP-3 | Hexagonal packing | chapter_08_generations.tex | OPEN | - |
| GAP-6 | CKM (rho,eta) | chapter_11_ckm.tex | PARTIAL | - |
| GAP-7 | CKM CP phase | chapter_11_ckm.tex | PARTIAL | - |
| GAP-9 | PMNS theta_13 | chapter_09_neutrinos.tex | OPEN | - |
| GAP-12 | BVP eigenvalue | chapter_14_bvp.tex | PARTIAL | - |
| GAP-13 | Barrier C | chapter_10_va_structure.tex | OPEN | - |
| GAP-15 | SU(2)_L origin | chapter_10_va_structure.tex | OPEN | - |
| GAP-16 | Neutrino hierarchy | chapter_09_neutrinos.tex | OPEN | - |
| GAP-17 | Dirac vs Majorana | chapter_09_neutrinos.tex | OPEN | - |
| GAP-18 | Robin kappa | chapter_15_mw_gf.tex | OPEN | - |
| GAP-20 | M_W prediction | chapter_15_mw_gf.tex | OPEN | - |

---

## Items MISSING from Book 2 (Potential Backfill)

1. **F_bulk gravitational coupling** - Part I content, not Part II scope
2. **Homotopy classifications (pi_n)** - Part I ontology, referenced but not derived
3. **Induced metric definitions** - Technical appendix candidate
4. **Golden ratio asymptotics** - Technical appendix candidate
5. **5D action component boxes** - Present implicitly, could be explicit
6. **Extrinsic curvature formulas** - Technical appendix candidate

---

## Recommendations

### Priority 1: Complete PARTIAL items
- GAP-6, GAP-7: CKM phase and (rho,eta) derivations
- GAP-12: BVP numerical solution
- GAP-19: Clarify g_5 status further

### Priority 2: Add missing technical definitions
- Box 5D action components in appendix
- Add induced metric/extrinsic curvature to notation appendix

### Priority 3: OPEN GAPs require new research
- GAP-2, GAP-3: Require V(xi) from action, hexagonal packing proof
- GAP-9, GAP-16, GAP-17: Neutrino sector predictions
- GAP-15: SU(2)_L origin (fundamental)

---

*End of mapping report*
