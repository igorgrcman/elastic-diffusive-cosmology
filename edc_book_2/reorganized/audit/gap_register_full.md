# EDC Book 2 — Full Gap Register (Prelet Phrase Scan)

**Date:** 2026-01-31
**Branch:** audit/gap-register-full-v1
**Short Book:** 145 pages (reorganized/)
**Long Book (Donor):** 461 pages (src/)

---

## Executive Summary

| Gap Type | Count | Avg Risk | Primary Issues |
|----------|-------|----------|----------------|
| Type C (Narrative/Mechanism) | 10 | CRITICAL | Z₆ origin, barrier parameter, neutrino counting, RG context |
| Type B (Missing Derivation) | 7 | HIGH | Zero-mode selection, G_F chain, M_W details |
| Type A (Missing Definition) | 3 | MEDIUM | Plenum, reduction dictionary, notation examples |
| **Total** | **20** | | |

### Top 10 Most Critical Gaps

1. **GAP-4**: Z₆ coupling ratio origin (chapter_06) — CRITICAL
2. **GAP-10**: G_F reduction chain steps 2-3 (chapter_12) — CRITICAL
3. **GAP-12**: M_W derivation details (chapter_15) — CRITICAL
4. **GAP-7**: Z₃ to three generations mechanism (chapter_08) — CRITICAL
5. **GAP-16**: SU(3) ontological derivation (chapter_02) — CRITICAL
6. **GAP-1**: V−A structure emergence (chapter_10) — HIGH
7. **GAP-3**: Barrier parameter μ emergence (chapter_10) — HIGH
8. **GAP-5**: Plenum inflow definition (chapter_10) — HIGH
9. **GAP-8**: CKM hierarchy derivation (chapter_11) — HIGH
10. **GAP-11**: Reduction dictionary definition (bridge) — HIGH

### Gaps with NO Donor Found

- **GAP-15**: Frozen regime two routes — needs original explanation
- **GAP-20**: Part I → Part II transition diagram — meta-structural

---

## Gap Register (Ordered: C → B → A, then by page)

### TYPE C: Narrative/Mechanism Jumps (10 gaps)

---

#### GAP-4: Z₆ Coupling Ratio Origin [CRITICAL]

**Target (145):** `part2/chapter_06_electroweak.tex:50`
**Trigger:** "emerges from Z₆ symmetry"
**Context:** Asserts coupling ratio 1/4 from Z₆ but does NOT show crystallographic calculation

**Source (461):** `src/Z6_content_full.tex:1318-1342` (Theorem: Weinberg Angle from Z₆ Partition)

**Rupa:** Type C — mechanism jump
**Minimalni backfill:** 10-15 lines showing partition counting:
- Interior volume fraction vs boundary
- |Z₂|/|Z₆| = 1/3 calculation
- g'²/(g² + g'²) = 1/4 derivation

**Napomena:**
- SM-language risk: YES (lattice terminology)
- Dictionary box: YES (geometry → sin²θ_W)
- Tag fix: Add explicit [Der:Sym] for group theory step

---

#### GAP-7: Z₃ to Three Generations [CRITICAL]

**Target (145):** `part2/chapter_08_generations.tex:29-30`
**Trigger:** "documents an identification, not a derivation"
**Context:** Honest acknowledgment, but no mechanism for mode truncation at n=2

**Source (461):** `src/Z6_content_full.tex` (generation truncation sections — partial)

**Rupa:** Type C — mechanism gap (deepest unsolved problem)
**Minimalni backfill:** 8-12 lines enumerating candidate mechanisms:
- Dynamical truncation options
- Mode quantization rules
- Topological constraint candidates
- Explicit [Open] status

**Napomena:**
- SM-language risk: NO
- Dictionary box: YES (Z₃ cardinality → generation count)
- Tag fix: Keep [I] but add scope note on what would upgrade to [Dc]

---

#### GAP-1: V−A Structure Emergence [HIGH]

**Target (145):** `part2/chapter_10_va_structure.tex:20`
**Trigger:** "it follows mathematically"
**Context:** Claims mathematical following from assumptions without bridging explanation

**Source (461):** `src/EDC_Part_II_Weak_Sector_rebuild.tex` (domain-wall sections)

**Rupa:** Type C — narrative jump
**Minimalni backfill:** 10-15 lines explaining Jackiw-Rebbi mechanism as bridge

**Napomena:**
- SM-language risk: YES ("left-handed", "chirality")
- Dictionary box: YES
- Tag fix: Separate [P] assumptions from [Der] consequences

---

#### GAP-3: Barrier Parameter μ Emergence [HIGH]

**Target (145):** `part2/chapter_10_va_structure.tex:668-674`
**Trigger:** "The localization mechanism implies exponential suppression"
**Context:** States suppression without deriving μ from first principles

**Source (461):** `src/EDC_Part_II_Weak_Sector_rebuild.tex` (quantitative V−A)

**Rupa:** Type C — mechanism jump
**Minimalni backfill:** 8-12 lines linking barrier height μ to membrane parameters (σ, δ, m₀)

**Napomena:**
- SM-language risk: YES
- Dictionary box: YES
- Tag fix: Add [Cal] note if μ is anchored

---

#### GAP-9: Neutrino Counting [MEDIUM]

**Target (145):** `part2/chapter_09_neutrinos.tex:152-154`
**Trigger:** "implies exactly three distinct sectors... dictionary step"
**Context:** Z₃ cardinality identified with N_ν but mapping unexplained

**Source (461):** `src/Z6_content_full.tex` (symmetry → spectrum)

**Rupa:** Type C — mechanism jump
**Minimalni backfill:** 5-8 lines showing explicit mapping rule: Z₃ sectors ↔ (e, μ, τ)

**Napomena:**
- SM-language risk: YES ("active neutrinos")
- Dictionary box: YES
- Tag fix: Already [Dc], add scope clarification

---

#### GAP-13: RG Running Context [MEDIUM]

**Target (145):** `part3/chapter_15_mw_gf.tex:134-138`
**Trigger:** "RG running of sin²θ_W from tree to M_Z scale: ∼3–5%"
**Context:** States correction without explaining why EDC tree-level differs from measured

**Source (461):** Generic QFT knowledge (not in donor files)

**Rupa:** Type C — mechanism gap
**Minimalni backfill:** 5-8 lines explaining tree-level = boundary condition, not physical scale

**Napomena:**
- SM-language risk: YES (QCD coupling running)
- Dictionary box: YES
- Tag fix: Add [BL] for SM running formula

---

#### GAP-15: Frozen Regime Two Routes [MEDIUM-HIGH]

**Target (145):** `part1/chapter_03_frozen.tex:113-128`
**Trigger:** "Therefore: Γ = 0 (exactly, not approximately) [Dc]"
**Context:** Route B (superselection) postulated without conceptual motivation

**Source (461):** NOT FOUND — needs original explanation

**Rupa:** Type C — mechanism jump
**Minimalni backfill:** 8-10 lines with physical picture: why topological superselection prevents decay

**Napomena:**
- SM-language risk: NO
- Dictionary box: YES
- Tag fix: Clarify [P] vs [Dc] boundary
- **STATUS: NO DONOR**

---

#### GAP-17: Overlap Model Calibration [MEDIUM]

**Target (145):** `part2/chapter_11_ckm.tex:264`
**Trigger:** "Single parameter Δξ/(2κ) ≈ 1.5 produces Wolfenstein hierarchy"
**Context:** Asserts fit without showing procedure

**Source (461):** `src/EDC_Part_II_Weak_Sector_rebuild.tex` (CKM fitting section)

**Rupa:** Type C — mechanism jump
**Minimalni backfill:** 8-12 lines showing fitting procedure explicitly

**Napomena:**
- SM-language risk: YES ("Wolfenstein hierarchy")
- Dictionary box: NO
- Tag fix: Add [Cal] disclosure

---

#### GAP-20: Part I → Part II Transition [MEDIUM]

**Target (145):** `bridge/chapter_0_bridge.tex:42-43`
**Trigger:** "Quantitative derivations... in Chapters 12–15"
**Context:** Lists chapters without logical sequence or prerequisites

**Source (461):** N/A — meta-structural

**Rupa:** Type C — narrative structure gap
**Minimalni backfill:** Dependency diagram showing chapter flow

**Napomena:**
- SM-language risk: NO
- Dictionary box: YES (chapter roadmap)
- **STATUS: NO DONOR (structural)**

---

### TYPE B: Missing Derivations (7 gaps)

---

#### GAP-10: G_F Reduction Chain Steps 2-3 [CRITICAL]

**Target (145):** `part3/chapter_12_gf_chain.tex:40-42`
**Trigger:** "emerges from a chain of reductions"
**Context:** Lists chain (g₅ → g₄ → G_eff → G_F) but only derives step 1

**Source (461):** `src/EDC_Part_II_Weak_Sector_rebuild.tex` (full G_F chapter)

**Rupa:** Type B — missing derivation steps
**Minimalni backfill:** 15-20 lines + 2-3 equations:
- Mode overlap integral
- Normalization factor
- Dictionary mapping

**Napomena:**
- SM-language risk: YES ("Fermi coupling", "electroweak scale")
- Dictionary box: YES
- Tag fix: Add [Der] for each step, [Dc] for final mapping

---

#### GAP-12: M_W Derivation Details [CRITICAL]

**Target (145):** `part3/chapter_15_mw_gf.tex:1-50`
**Trigger:** "M_W ∼ ℏc/R_ξ"
**Context:** Formula given but not derived from 5D physics

**Source (461):** `src/EDC_Part_II_Weak_Sector_rebuild.tex` (full M_W chapter)

**Rupa:** Type B — missing derivation
**Minimalni backfill:** 12-15 lines + 2 equations:
- Quantitative derivation from membrane thickness
- Coupling and localization integrals

**Napomena:**
- SM-language risk: NO
- Dictionary box: YES
- Tag fix: Separate [Der] (scale) from [Cal] (numerical value)

---

#### GAP-16: SU(3) Ontological Derivation [CRITICAL]

**Target (145):** `part1/chapter_02_ontology.tex:148-149`
**Trigger:** "emerges from the junction symmetry group [Der]"
**Context:** Claims SU(3) emerges but lacks group-theoretic derivation

**Source (461):** Part I material (not in Part II src)

**Rupa:** Type B — missing derivation
**Minimalni backfill:** 10-15 lines:
- Y-junction three arms → S³ × S³ × S³ → SU(3) Lie algebra

**Napomena:**
- SM-language risk: YES (SU(3), group theory)
- Dictionary box: YES
- Tag fix: Keep [Der] but add explicit reference to Part I

---

#### GAP-2: Zero-Mode Selection Mechanism [MEDIUM]

**Target (145):** `part2/chapter_10_va_structure.tex:321-339`
**Trigger:** "The zero-mode limit..."
**Context:** Jumps to zero-mode without deriving decoupling from massive modes

**Source (461):** `src/Z6_content_full.tex` (chiral zero mode sections)

**Rupa:** Type B — missing derivation
**Minimalni backfill:** 8-10 lines showing WKB/asymptotic expansion

**Napomena:**
- SM-language risk: NO
- Dictionary box: NO
- Tag fix: Add derivation reference

---

#### GAP-6: Boundary Condition Emergence [MEDIUM-HIGH]

**Target (145):** `part2/chapter_10_va_structure.tex:938-947`
**Trigger:** "emerges from the normalizability requirement"
**Context:** Claims BC emerges but doesn't show normalizability analysis

**Source (461):** `src/Z6_content_full.tex` (boundary condition calculations)

**Rupa:** Type B — missing derivation
**Minimalni backfill:** 8-12 lines showing non-normalizability of right-handed modes

**Napomena:**
- SM-language risk: NO
- Dictionary box: YES
- Tag fix: Add [Der] for normalizability proof

---

#### GAP-8: CKM Hierarchy Derivation [HIGH]

**Target (145):** `part2/chapter_11_ckm.tex:261-265`
**Trigger:** "Pure Z₃ implies democratic mixing—wrong by factors up to 144"
**Context:** Shows failure but doesn't derive overlap model parameter

**Source (461):** `src/EDC_Part_II_Weak_Sector_rebuild.tex` (full CKM derivation)

**Rupa:** Type B — missing derivation
**Minimalni backfill:** 10-15 lines + 2 equations:
- Overlap integrals for localized wavefunctions
- Δξ/(2κ) ≈ 1.5 derivation

**Napomena:**
- SM-language risk: NO
- Dictionary box: NO
- Tag fix: Add [Cal] for fitted parameter

---

#### GAP-19: Mode Normalization Impact [MEDIUM]

**Target (145):** `part3/chapter_13_foundation_params.tex:292`
**Trigger:** "Mode normalization... affects g₅ → g₄ mapping"
**Context:** References future specification but impact not quantified

**Source (461):** `src/EDC_Part_II_Weak_Sector_rebuild.tex` (normalization sections)

**Rupa:** Type B — missing derivation
**Minimalni backfill:** 6-10 lines showing normalization factor propagation to G_F

**Napomena:**
- SM-language risk: NO
- Dictionary box: YES
- Tag fix: Quantify uncertainty explicitly

---

### TYPE A: Missing Definitions (3 gaps)

---

#### GAP-5: Plenum Inflow Definition [HIGH]

**Target (145):** `part2/chapter_10_va_structure.tex:15-37`
**Trigger:** "Plenum inflow determines mass profile sign"
**Context:** Introduces "Plenum" without explicit definition

**Source (461):** `src/EDC_Part_II_Weak_Sector_rebuild.tex` (opening sections)

**Rupa:** Type A — missing definition
**Minimalni backfill:** 1-2 paragraphs:
- Plenum = diffuse background scalar field in extra dimension
- Directional flow sets sign of effective potential

**Napomena:**
- SM-language risk: NO (neologism)
- Dictionary box: YES
- Tag fix: Add [P] for ontological concept

---

#### GAP-11: Reduction Dictionary Definition [HIGH]

**Target (145):** `bridge/chapter_0_bridge.tex:31-35`
**Trigger:** "Dictionary boundary... tagged Dc"
**Context:** Defines tag but not dictionary CONTENT

**Source (461):** `bridge/EPISTEMIC_STANDARD_COMPLETE_FINAL.tex:14-60`

**Rupa:** Type A — missing definition
**Minimalni backfill:** Master table of all 5D → 4D identifications

**Napomena:**
- SM-language risk: YES
- Dictionary box: YES (this IS the dictionary)
- Tag fix: N/A

---

#### GAP-14: Kink Model Scope [MEDIUM]

**Target (145):** `part3/chapter_13_foundation_params.tex:162-167`
**Trigger:** "scalar kink model... conditional dictionary assumption"
**Context:** Uses kink without defining field profile

**Source (461):** `src/CH3_electroweak_parameters.tex`

**Rupa:** Type A — missing definition
**Minimalni backfill:** 1-2 lines:
- kink = solitonic scalar field interpolating between vacuum minima

**Napomena:**
- SM-language risk: NO
- Dictionary box: YES
- Tag fix: Add [P] for model choice

---

## Donor File Summary

| Donor File | Priority | Gaps Covered |
|------------|----------|--------------|
| `src/Z6_content_full.tex` | CRITICAL | GAP-4, GAP-7, GAP-2, GAP-6, GAP-9 |
| `src/EDC_Part_II_Weak_Sector_rebuild.tex` | CRITICAL | GAP-1, GAP-3, GAP-8, GAP-10, GAP-12, GAP-17, GAP-19 |
| `src/CH3_electroweak_parameters.tex` | MEDIUM | GAP-14 |
| `bridge/EPISTEMIC_STANDARD_COMPLETE_FINAL.tex` | HIGH | GAP-11, GAP-18 |

---

## Dictionary Boxes Needed (Priority Order)

1. **Z₆ Partition → sin²θ_W** (GAP-4)
2. **Reduction Dictionary Master Table** (GAP-11)
3. **Plenum Inflow Definition** (GAP-5)
4. **Barrier Parameter μ → Localization** (GAP-3)
5. **Z₃ Cardinality → Generation Count** (GAP-7)
6. **Domain-Wall Fermion Localization** (GAP-1)
7. **RG Running Context** (GAP-13)
8. **Kink Model Definition** (GAP-14)

---

## SM-Language Risk Terms

| Term | Gaps | Definition Needed |
|------|------|-------------------|
| Left-handed, chirality | GAP-1, GAP-3 | 5D context explanation |
| Electroweak scale, Weinberg angle | GAP-4, GAP-10 | Historical SM terminology |
| Active neutrinos | GAP-9 | Neutrino physics jargon |
| Wolfenstein hierarchy, CKM | GAP-17 | Quark physics conventions |
| RG running, QCD coupling | GAP-13 | Renormalization concepts |
| SU(3) color | GAP-16 | Gauge theory terminology |

---

*Generated: 2026-01-31 | Branch: audit/gap-register-full-v1*
