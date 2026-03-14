# Particle Anatomy and Decay Rediscovery Index

**Date:** 2026-03-14
**Branch:** `research/topological-pinning-v7_8-integration`
**Scope:** Forensic rediscovery and indexing — no new derivations, no new ontology

---

## 1. Executive Verdict

The repo already contains a **substantial, developed 5D particle anatomy and decay
ontology** covering proton, neutron, electron, muon, tau, pion, and neutrino.
The material is **distributed across three layers**:

1. **Paper 3 series** (canonical published companions with DOIs) — the most
   detailed derivations and the primary source for each particle.
2. **Book 2** (`edc_book_2/`) — a consolidated weak-sector ontology hub with
   per-particle case studies and a five-category classification diagram.
3. **Book 4** (`edc_book_4/`) — proton/neutron anatomy in EDC-native terms
   (no SM labels; uses contamination-safe vocabulary).

No single file contains the entire ontology. The **closest thing to a unified
source** is `edc_book_2/src/sections/04_ontology.tex` (five-category
classification with TikZ diagram) backed by per-particle case study files
(sections 05–10). The Framework v2.0 PDF
(`00_Framework_v2_0__DOI_10.5281_zenodo.18299085.pdf`) is the most comprehensive
single document but is a reference paper, not a narrative.

The ontology is **more developed than scattered** — it follows a clear
architectural pattern (companion paper per particle, case study per particle in
Book 2, ontology dictionary in Book 4). But no single retrieval path gives the
complete picture without reading 4–6 files.

---

## 2. Scope of Search

### What was searched

| Pass | Corpus | Searched | Notes |
|------|--------|----------|-------|
| **1** | Priority companion corpus (10 PDFs) | YES — all 10 PDFs read via repo copies at `edc_papers/paper_3_series/releases/pdfs/` | `/mnt/data/` not available; repo copies are identical (SHA256SUMS verified) |
| **2** | `edc_papers/paper_3_series/**` | YES — all tex sources inspected | Found 17 companion/paper directories |
| **3** | `edc_papers/**` (other) | YES — `paper_2/`, `paper_gravity_block003/`, `_shared/` | Limited particle anatomy content |
| **4** | `edc_book_4/**` | YES — all chapters, appendices, ontology/, audit/ | Major proton/neutron anatomy source |
| **4** | `edc_book_2/**` | YES — src/sections/ fully inspected | **Major find**: full weak-sector ontology hub |
| **4** | `edc_book/` (Book 1) | YES — glossary, chapter 4 | "Plenum" terminology; Book 1 only |
| **5** | Other branches | NOT NEEDED — current branch sufficient | |

### What was excluded

- Build artifacts (`.aux`, `.log`, `.out`)
- Binary PDFs were read via the Read tool's PDF capability
- Code files inspected only for ontology relevance (not computation details)

---

## 3. High-Value Findings Summary

Ranked by importance for the current indexing mission:

1. **Book 2 ontology hub** (`edc_book_2/src/sections/04_ontology.tex`) — five-category
   particle classification (bulk-core junction, brane-dominant fundamental,
   brane defect, edge mode, composite) with TikZ diagram. This is the single
   best "what is what" file.

2. **Book 2 per-particle case studies** (sections 05–10) — neutron, muon, tau,
   pion, electron, neutrino each have a dedicated case study with
   `edcAtAGlance` boxes.

3. **Framework v2.0** (PDF 00) — 37-page canonical reference. Contains proton
   (Y-junction S³×S³×S³), neutron (asymmetric half-Steiner), electron (B³
   vortex), Z₆ ring, Plenum, SU(3) from 3 arms, muon/tau mass formulas,
   3-generation theorem, beta decay = junction relaxation, neutrino = ξ-wave.

4. **Companion H: Weak Interactions** (PDF 09 / tex source) — complete catalog
   of six weak processes (β⁻, β⁺, EC, IBD, 2νββ, 0νββ) via bulk-core pumping
   through frozen projection boundary. The primary decay ontology source.

5. **Companion F: Proton Junction** (PDF 07) — variational derivation of 120°
   Steiner angles, Hopf bridge, S³ config space, m_p/m_e = 6π⁵. The primary
   proton anatomy derivation.

6. **Companion G: Mass Difference** (PDF 08) — Z₆ ring, asymmetry parameter q,
   neutron at half-Steiner, Δm = 1.293 MeV derivation.

7. **Book 4 chapters ch01–ch03** — proton (anchor junction), junction symmetries
   (Z₆→Z₃→Z₂), neutron (metastable junction) in contamination-safe EDC-native
   vocabulary. No SM labels.

8. **Paper 3 series draft companions** (M, T, P, L, V, N) — muon, tau, pion,
   electron, neutrino, neutron junction analyses at draft stage (v0.1–v0.3).

9. **Book 4 canonical ontology dictionary** (`edc_book_4/ontology/EDC_ONTOLOGY_CANON.md`)
   — LOCKED v1.0. Full avoid→use translation table. Authoritative for Books 2–4.

10. **Weak Program Overview** (paper_3_series/14) — registry/index document
    tying together all companion decay papers under unified pipeline.

---

## 4. Priority Companion Corpus Findings

All 10 priority files were searched via their repo copies at
`edc_papers/paper_3_series/releases/pdfs/`.

| ID | File | Contains | Proton/Neutron | Decay | Pion/Weak | Maturity | Canon | Notes |
|----|------|----------|---------------|-------|-----------|----------|-------|-------|
| 00 | `00_Framework_v2_0` | Full EDC reference (37pp) | **COMPREHENSIVE**: proton Y-junction S³×S³×S³, neutron half-Steiner, electron B³ vortex, Z₆ ring, Plenum, SU(3) from 3-arm junction | Beta decay = junction relaxation (§14.1), neutrino = ξ-wave (§14.2), weak = junction-slip | Muon mass [I], tau mass [I], 3-gen theorem [Dc], meson defined, pion mentioned | Canonical | YES | Single richest document |
| 01 | `01_Paper3_NJSR_Journal` | Neutron lifetime paper (22pp) | Reviews proton/neutron/electron classification, collective coordinate q | NJSR tunneling, INFLOW/OUTFLOW, golden-ratio tail, R_det, 10/10 gates, τ_n calibrated | Muon/tau deferred to future work | Canonical | YES | Primary neutron decay paper |
| 02 | `02_CompanionA_Effective_Lagrangian` | L_eff derivation (9pp) | Neutron/proton as q boundary conditions, AdS₅ bulk, Israel conditions | Derives V(q) = V_B q²(1−q)² and M(q) = M₀(1−2q)² from 5D geometry | None | Canonical | YES | Derivation machinery |
| 03 | `03_CompanionB_WKB_Prefactor` | WKB computation (7pp) | Neutron as metastable 1D state only | WKB B=0.72, A₀, R_det=0.63, golden-ratio φ, lifetime calibrated, 10/10 gates | None | Canonical | YES | Numerical computation |
| 04 | `04_CompanionC_5D_KK_Reduction` | 5D→1D pipeline (8pp) | 7-stage reduction chain, collective coordinate q, RS brane setup | V(q), M(q), S_eff pipeline; V_B = [OPEN] | None | Canonical | YES | Pipeline structure |
| 05 | `05_CompanionD_Selection_Rules` | n decay selection rules (8pp) | Brane/Plenum, Y-junction q, defect table (Q, W, p^ξ classification) | Two-output selection rule: electron (Q=−1, p^ξ=0) + antineutrino (Q=0, p^ξ≠0). Excluded alternatives. Helicity. | None | Canonical | YES | **Key**: all outputs created ON brane |
| 06 | `06_CompanionE_Symmetry_Ops` | Symmetry operators (19pp) | M₅ product, Z₆ sectors, su(3) junction algebra, defect classification table | Three operators (E, R, M); beta-minus ledger; ξ-wave = antineutrino | E operator mentions e→μ→τ (1 line only) | Canonical | YES | Formal operator definitions |
| 07 | `07_CompanionF_Proton_Junction` | Proton variational (13pp) | **PRIMARY proton source**: 120° Steiner [Der], Hopf bridge, S³ config, C_p=(2π²)³, m_p/m_e = 6π⁵ | Minimal (defers to G, H) | Heavier baryons mentioned (Λ⁰) | Canonical | YES | Zero calibrated parameters |
| 08 | `08_CompanionG_Mass_Difference` | n-p mass split (12pp) | Z₆ ring, q parameter, half-Steiner neutron, quark windings W_u=+2/3 W_d=−1/3, SU(3) color from Y-junction | Δm = −2V₃ = 1.293 MeV (0.2% accuracy). Oscillator: proton=\|0⟩, neutron=\|1⟩ | None | Canonical | YES | One calibrated parameter (V₃) |
| 09 | `09_CompanionH_Weak_Interactions` | Weak interactions (20pp) | Thick-brane: bulk-core + brane-layer + frozen boundary. Proton=\|0⟩, neutron=\|1⟩, electron=winding+1, neutrino=delocalized wave | **COMPLETE catalog**: β⁻, β⁺, EC, IBD, 2νββ, 0νββ. Bulk-core pumping hypothesis. Process table + frozen boundary table. σ = 8.82 MeV/fm² derived. | Proton decay p→e⁺+π⁰ as falsification test (pion as SM label only). Muon/tau flagged [Open]. | Canonical [P] | YES | **Primary decay ontology** |

**Key gap in priority corpus:** No EDC-native pion, muon, or tau derivation
exists in the 10 priority companion PDFs. These exist only in the draft-stage
companions (M, T, P) found in the tex sources.

---

## 5. Canonical Proton / Neutron Anatomy Sources

| ID | File/Path | Branch | Contains | Maturity | Canon | Notes |
|----|-----------|--------|----------|----------|-------|-------|
| PA-1 | `edc_papers/paper_3_series/releases/pdfs/00_Framework_v2_0...pdf` | current | Proton: Y-junction S³×S³×S³, Steiner 120°, Z₆ ring s=0. Neutron: half-Steiner, s=1, Δm=(8/π)m_e. Electron: B³ vortex. Full 5D anatomy. | Canonical | YES | Single most comprehensive source |
| PA-2 | `edc_papers/paper_3_series/07_companion_F.../paper/main.tex` | current | Proton variational foundation: Postulates 1–2 (Y-junction, brane-constrained vertex), Steiner theorem [Der], Nambu-Goto action, Hopf bridge S³, C_p=(2π²)³, m_p/m_e=6π⁵ | Canonical | YES | Primary proton derivation |
| PA-3 | `edc_papers/paper_3_series/08_companion_G.../paper/main.tex` | current | Z₆=Z₃×Z₂ symmetry, asymmetry parameter q, ring with O(2) transverse sector, quark windings, SU(3) color from 8 junction modes, Δm derivation | Canonical | YES | Primary n-p mass split derivation |
| PA-4 | `edc_book_4/chapters/ch01_proton_ground.tex` | current | Anchor junction: Steiner 120° [Der], topological protection (π₁), Nambu-Goto E=τL, Z₆ crystallization chain (Route B), observerbox: anchor↔proton | Canonical (Book 4) | YES | EDC-native vocabulary |
| PA-5 | `edc_book_4/chapters/ch03_neutron_metastable.tex` | current | Metastable junction: Z₃ config, reaction coordinate q, double-well V(q) [P], barrier V_B=2Δm_np, observerbox: metastable↔neutron | Canonical (Book 4) | YES | EDC-native vocabulary |
| PA-6 | `edc_book_4/chapters/ch02_junction_symmetries.tex` | current | Z₆→Z₃→Z₂ chain, M₆ lattice, junction-subgroup correspondence, observerbox: anchor/metastable/cluster↔proton/neutron/nucleus | Canonical (Book 4) | YES | Bridges anatomy → binding |
| PA-7 | `edc_papers/paper_3_series/10_companion_N.../paper/main.tex` | current | Neutron junction detailed: excited Y-junction, q collective coordinate, thick-brane 3-layer, ring+3-springs analogy [I/P] | Draft v0.1 | NO | Extends Companion G |
| PA-8 | `edc_book_2/src/sections/04_ontology.tex` | current | Five-category particle classification incl. proton (bulk-core junction, q=0) and neutron (bulk-core junction, q>0) | Filled | YES | Best single-page overview |
| PA-9 | `edc_papers/paper_3_series/05_companion_D.../paper/main.tex` | current | Brane/Plenum structure: M₅, brane Σ at ξ=0, Plenum at ξ>0. Y-junction q. Topological charge Q. Key: ALL outputs created ON brane. | Canonical | YES | Clarifies Plenum/brane boundary |
| PA-10 | `edc_book_4/ontology/EDC_ONTOLOGY_CANON.md` | current | LOCKED v1.0 dictionary: anchor junction=proton, metastable=neutron, loop=electron, edge-mode=photon, bulk mode=graviton, cluster=nucleus, closed-4=alpha | Canonical | YES | Authoritative translation |

### Three-leg / ring / Plenum picture

| Concept | Where it lives | Notes |
|---------|---------------|-------|
| **Three-leg Y-junction** | Companion F (variational), Framework v2.0 (§8), Book 4 ch01 (anchor), Companion G (Z₆ ring) | Consistently defined everywhere |
| **Ring / transverse ring** | Companion G (O(2) transverse sector, §1.3), Framework v2.0 (§9, Z₆ ring with 6 positions) | Ring = compact internal coordinate of junction vertex |
| **Plenum** | Framework v2.0 (§4.1.1), Companion D (§3.1), Book 1 glossary | Modeling language for bulk (5D). NOT used in Books 2 or 4. |
| **Deep junction / descending into bulk** | Companion F (Postulate 2: vertex on brane, arms into bulk), Companion A (brane embedding X^A) | Arms extend into 5D; vertex constrained to 4D brane |

---

## 6. Canonical Decay Ontology Sources

| ID | File/Path | Branch | Decay Content | Maturity | Canon | Notes |
|----|-----------|--------|--------------|----------|-------|-------|
| DO-1 | `edc_papers/paper_3_series/09_companion_H.../paper/main.tex` | current | **Complete weak catalog**: β⁻, β⁺, EC, IBD, 2νββ, 0νββ. Bulk-core pumping through frozen projection boundary. Process table. Frozen boundary behavior table. Proton stability (spontaneous decay FORBIDDEN). σ=8.82 MeV/fm² derived. S/ℏ=60 [Cal]. | Canonical [P] | YES | **Primary decay source** |
| DO-2 | `edc_papers/paper_3_series/releases/pdfs/00_Framework_v2_0...pdf` | current | Beta decay = junction relaxation (§14.1): Z₆ ring rotation θ=60°→0°, winding change d→u, electron created for charge conservation, antineutrino (ξ-wave) carries energy. Weak force = junction-slip [P]. | Canonical | YES | Foundational decay narrative |
| DO-3 | `edc_papers/paper_3_series/01_paper3.../paper/body_shared/main_body.tex` | current | NJSR tunneling: V(q)=16V_B q²(1−q)²+Qq, Γ=A₀exp(−B/ℏ), INFLOW/OUTFLOW. Electron=brane-bound, antineutrino=bulk-escape. 10/10 gates. | Canonical | YES | Primary neutron lifetime calculation |
| DO-4 | `edc_papers/paper_3_series/05_companion_D.../paper/main.tex` | current | Two-output selection rule [Dc]: electron (Q=−1, W=0, p^ξ=0) + antineutrino (Q=0, W=0, p^ξ≠0). Excluded alternatives table. Helicity assignment. | Canonical | YES | WHY exactly e⁻ + ν̄_e |
| DO-5 | `edc_papers/paper_3_series/06_companion_E.../paper/sections/06_beta_decay_ledger.tex` | current | Full conservation ledger: W, Q, sector s, baryon #, lepton #. Neutral channel theorem. ξ-wave = antineutrino [P]. | Canonical | YES | Bookkeeping verification |
| DO-6 | `edc_book_2/src/sections/05_case_neutron.tex` | current | Neutron beta-decay case study. Pipeline: junction relaxation → thick-brane charging → frozen projection. Three-stage: absorption → dissipation → release. | Filled | YES | Narrative case study |
| DO-7 | `edc_book_4/chapters/ch03_neutron_metastable.tex` | current | Double-well V(q), barrier V_B, instanton chain σ→K→V_B→S_E→τ_n. Observerbox: metastable decay ↔ neutron beta decay. | Canonical (Book 4) | YES | EDC-native vocabulary |

### Decay mechanism summary (as found in sources)

The canonical mechanism is **bulk-core pumping through frozen projection boundary**
(Companion H):

1. Junction excited state |1⟩ (neutron) relaxes to ground state |0⟩ (proton)
2. Released energy flows through one-way frozen boundary (bulk→brane: permitted;
   brane→bulk: suppressed)
3. Brane-layer modes excited: electron (localized deformation, winding +1) +
   antineutrino (delocalized wave, lepton number −1)
4. Frozen projection maps brane-layer modes to 3D observables

All six weak processes (β⁻, β⁺, EC, IBD, 2νββ, 0νββ) follow this single
pipeline with variations in direction and energy source.

---

## 7. Wider Particle Decay Sources

| Particle/Family | File/Path | Branch | What Exists | Status | Usefulness |
|----------------|-----------|--------|-------------|--------|------------|
| **Pion** | `edc_papers/paper_3_series/13_companion_P_pion_decay/paper/main.tex` | current | Brane-dominant composite, junction-pair candidate micro-ontology [P/Open], helicity suppression from chirality projection [P/Open], metastability from brane localization. v0.3 QA-hardened. | Draft | Useful — most developed pion source |
| **Pion** | `edc_book_2/src/sections/08_case_pion.tex` | current | Pion case study: composite junction-pair, hadron→lepton bridge, chiral projection produces helicity suppression. edcAtAGlance box. | Filled | Useful — narrative |
| **Muon** | `edc_papers/paper_3_series/11_companion_M_muon_decay_tomography/paper/main.tex` | current | Brane-dominant excitation (not bulk-core junction) [P]. Purely leptonic decay: same absorption→dissipation→release pipeline without bulk-core. Chiral filter. Contrast table: neutron (junction) vs muon (mode). v0.2. | Draft | Useful — muon-specific |
| **Muon** | `edc_book_2/src/sections/06_case_muon.tex` | current | Muon case study: brane-dominant mode relaxation, "clean room" test, V-A may be geometric. | Filled | Useful — narrative |
| **Muon mass** | Framework v2.0, §15.3 | current | m_μ/m_e = (3/2)(1+α⁻¹), 0.14% accuracy. Muon = excited electron (n=1 ξ-oscillation). [I] | Canonical | Reference formula |
| **Tau** | `edc_papers/paper_3_series/12_companion_T_tau_decay/paper/main.tex` | current | Higher-mode brane excitation [P]. Mode index hypothesis: n_e < n_μ < n_τ. Leptonic tau decays. Hadronic channels deferred [Open]. v0.1. | Draft | Useful — tau-specific |
| **Tau** | `edc_book_2/src/sections/07_case_tau.tex` | current | Tau case study: higher-mode brane, same ontology as muon, larger energy opens hadronic channels. | Filled | Useful — narrative |
| **Tau mass** | Framework v2.0, §15.7 | current | m_τ/m_μ = 16π/3, 0.37% accuracy. Tau couples to all 8 SU(3) generators. [I] | Canonical | Reference formula |
| **Electron** | `edc_papers/paper_3_series/15_companion_L_electron_brane_defect/paper/main.tex` | current | Stable observer-facing brane-layer defect [P/Def]. Selection rules: why e⁻ selected over μ⁻/τ⁻. Three-layer brane. v0.1. | Draft | Useful |
| **Electron** | `edc_book_2/src/sections/09_case_electron.tex` | current | Ground-state brane defect. Stability from mode spectrum (no lower charged state). Three-layer brane structure. | Filled | Useful — narrative |
| **Electron** | Companion F, §5 / Paper 3 NJSR | current | Frozen vortex, B³ config space, C_e=4π/3, golden-ratio tail φ=(1+√5)/2. | Canonical | Derivation source |
| **Electron stability** | Companion H, §10.1 | current | Implicit: frozen boundary prevents spontaneous brane→bulk; electron has no lower-energy charged state. Explicit: proton decay p→e⁺+π⁰ FORBIDDEN. | Canonical | Indirect but definitive |
| **Neutrino** | `edc_papers/paper_3_series/16_companion_V_neutrino_edge_mode/paper/main.tex` | current | Edge mode at bulk-brane interface. Weak coupling from suppressed wavefunction overlap. | Draft | Useful |
| **Neutrino** | `edc_book_2/src/sections/10_case_neutrino.tex` | current | Edge mode case study. Boundary/edge mode at bulk-brane interface. | Filled | Useful — narrative |
| **Neutrino** | Framework v2.0, §14.2 | current | ξ-wave: propagating wave in compact S¹_ξ dimension [P]. Near-massless, weak interaction, high penetration. | Canonical | Foundational definition |
| **3 generations** | Framework v2.0, §15.11 | current | Four independent arguments: topological stability of 3-arm junction, generator exhaustion, Z₆ completeness, dimensional counting. 4th generation forbidden [Dc]. | Canonical | Important constraint |
| **Excitation operator E** | Companion E, §5.1 | current | Physical interpretation: generation transitions e→μ→τ. Preserves W, Q, C, s. One-line mention only. | Canonical | Formal definition only |

### Summary of wider-particle maturity

| Particle | Canonical (DOI) | Book 2 case study | Draft companion | Overall status |
|----------|----------------|-------------------|-----------------|----------------|
| Proton | F, G, Framework | 04_ontology | — | **Complete** |
| Neutron | D, E, G, H, Paper 3 | 04_ontology, 05_case | N (v0.1) | **Complete** |
| Electron | F (vortex), Paper 3 (soliton) | 09_case | L (v0.1) | **Strong** |
| Neutrino | D (selection), E (ξ-wave), H (brane wave) | 10_case | V (draft) | **Strong** |
| Muon | Framework (mass formula) | 06_case | M (v0.2) | **Moderate** — mass formula canonical, decay ontology draft |
| Tau | Framework (mass formula) | 07_case | T (v0.1) | **Moderate** — same as muon |
| Pion | — | 08_case | P (v0.3 QA) | **Draft** — no canonical derivation, ontology exploratory |

---

## 8. Best Narrative / Ontology Containers

| ID | File/Path | Function | Why important |
|----|-----------|----------|---------------|
| OC-1 | `edc_book_2/src/sections/04_ontology.tex` | **Five-category particle classification hub** with TikZ diagram | Single best "what is what" file for all particles |
| OC-2 | `edc_book_4/ontology/EDC_ONTOLOGY_CANON.md` | **LOCKED ontology dictionary** v1.0 | Authoritative avoid→use translation for all EDC books |
| OC-3 | `edc_book_4/CC_PROMPT_HEADER.md` | Quick-reference particle→topological-state table | Fast lookup |
| OC-4 | `edc_papers/paper_3_series/releases/pdfs/00_Framework_v2_0...pdf` | **Framework reference** (37pp) | Most comprehensive single document |
| OC-5 | `edc_papers/paper_3_series/14_weak_program_overview/paper/main.tex` | **Weak program registry/index** | Ties all companion decay papers under unified pipeline |
| OC-6 | `edc_book_4/NARRATIVE_SPINE.md` | Book 4 narrative architecture | Part-by-part chapter flow |
| OC-7 | `edc_book_2/src/sections/05-10` (case studies as group) | **Per-particle narrative case studies** | Each has edcAtAGlance box with baseline, EDC view, insight, predictions |
| OC-8 | `edc_book_4/audit/CHAPTER_MAP.md` | Chapter-level status/result map | Index into Book 4 content |

---

## 9. Fragmentation Assessment

### Is the ontology centralized or fragmented?

**Architecturally organized but physically distributed.** The ontology follows a
clear three-layer architecture:

- **Layer 1 (derivation):** paper_3_series companions — one per particle/topic
- **Layer 2 (narrative):** Book 2 case studies — one per particle
- **Layer 3 (EDC-native):** Book 4 chapters — proton/neutron only (SM labels banned)

This is not fragmentation in the negative sense — it is a deliberate separation
of concerns. But it means no single file gives the complete picture.

### Do proton/neutron anatomy and decay live in one place or many?

**Many.** Proton anatomy: Companion F (derivation) + Book 4 ch01 (narrative) +
Framework v2.0 (summary). Neutron anatomy: Companion G (mass) + Companion H
(decay) + Book 4 ch03 (narrative) + Paper 3 (lifetime). Decay: Companion H
(catalog) + Companion D (selection rules) + Book 2 §05 (case study).

### Does pion decay live in paper_3_series, companions, or elsewhere?

**Primarily in paper_3_series**: Companion P (`13_companion_P_pion_decay/`, v0.3
draft) is the most developed pion source. Book 2 (`08_case_pion.tex`) has a
narrative case study. No canonical (DOI-published) pion paper exists.

### Would a canonical consolidation document be worthwhile?

**Yes**, if the goal is to have a single-file retrieval path for the entire 5D
particle anatomy and decay ontology. Currently this requires reading 4–6 files.
However, the existing architecture (derivation → case study → EDC-native
chapter) is sound and may not need replacement — it may only need an improved
index (which this document provides).

---

## 10. Dead Ends / Superseded Descriptions Worth Preserving

| Item | Location | Status | Notes |
|------|----------|--------|-------|
| **"Plenum" terminology** | `edc_book/` (Book 1), Framework v2.0 §4.1.1 | Superseded in Books 2–4 | "Plenum" = bulk modeling language. Not wrong, but not used in current books. Preserved as historical. |
| **Proton Z₆ original notes** | `edc_papers/paper_3_series/Proton Z6/` | Historical | Original derivation notes (Croatian/English mix). Superseded by Companion F. |
| **m_μ/m_e = (3/2)(1+α⁻¹)** | Framework v2.0 §15.3 | [I] identified | Not derived from first principles. Tagged honestly. Not dead-end but not [Der]. |
| **m_τ/m_μ = 16π/3** | Framework v2.0 §15.7 | [I] identified | Same status as muon formula. |
| **Oscillator vs static potential equivalence** | Companion G §7 | [OPEN] | Two parallel descriptions of n-p splitting; their equivalence is unresolved. |

No major dead ends found. The existing ontology is internally consistent within
its epistemic tags.

---

## 11. Recommended Canonical Retrieval Path

### Path A: Proton/Neutron 5D Anatomy

1. **Start:** `edc_book_2/src/sections/04_ontology.tex` — five-category
   classification, get the big picture (1 page)
2. **Proton derivation:** `edc_papers/paper_3_series/07_companion_F.../paper/main.tex`
   — variational foundation, Steiner angles, Hopf bridge (13pp)
3. **Neutron-proton split:** `edc_papers/paper_3_series/08_companion_G.../paper/main.tex`
   — Z₆ ring, q parameter, mass difference (12pp)
4. **EDC-native narrative:** `edc_book_4/chapters/ch01_proton_ground.tex` then
   `ch03_neutron_metastable.tex` — contamination-safe vocabulary

### Path B: Neutron Decay / Brane-Relaxation Ontology

1. **Start:** `edc_papers/paper_3_series/09_companion_H.../paper/main.tex` —
   thick-brane picture, bulk-core pumping, complete process catalog (20pp)
2. **Selection rules:** `edc_papers/paper_3_series/05_companion_D.../paper/main.tex`
   — why exactly e⁻ + ν̄_e (8pp)
3. **Conservation ledger:** `edc_papers/paper_3_series/06_companion_E.../paper/sections/06_beta_decay_ledger.tex`
4. **Lifetime calculation:** Paper 3 NJSR (`01_paper3.../paper/body_shared/main_body.tex`)
5. **Narrative case study:** `edc_book_2/src/sections/05_case_neutron.tex`

### Path C: Pion / Wider Weak-Decay Ontology

1. **Overview:** `edc_papers/paper_3_series/14_weak_program_overview/paper/main.tex`
   — unified pipeline across all four particle types
2. **Pion:** `edc_papers/paper_3_series/13_companion_P_pion_decay/paper/main.tex`
   (v0.3 draft, QA-hardened)
3. **Muon:** `edc_papers/paper_3_series/11_companion_M_muon_decay_tomography/paper/main.tex`
   (v0.2 draft)
4. **Tau:** `edc_papers/paper_3_series/12_companion_T_tau_decay/paper/main.tex`
   (v0.1 draft)
5. **Electron:** `edc_papers/paper_3_series/15_companion_L_electron_brane_defect/paper/main.tex`
   (v0.1 draft)
6. **Neutrino:** `edc_papers/paper_3_series/16_companion_V_neutrino_edge_mode/paper/main.tex`
   (draft)
7. **Narrative case studies:** `edc_book_2/src/sections/06_case_muon.tex` through
   `10_case_neutrino.tex`

### Comprehensive reference (all particles)

For a single-document overview of the entire ontology:
`edc_papers/paper_3_series/releases/pdfs/00_Framework_v2_0__DOI_10.5281_zenodo.18299085.pdf`
(37pp, canonical, covers everything at survey depth).

---

## 12. Bottom Line

The repo already contains a **well-developed 5D particle anatomy and decay
ontology** covering seven particles (proton, neutron, electron, positron,
neutrino, muon, tau) plus pion. The proton/neutron anatomy and neutron decay
chain are canonical (published with DOIs, fully derived). The muon, tau, and
pion ontologies exist at draft stage in dedicated companion papers (v0.1–v0.3)
and as narrative case studies in Book 2. The five-category classification
(bulk-core junction / brane-dominant fundamental / brane defect / edge mode /
composite) in `edc_book_2/src/sections/04_ontology.tex` is the closest thing to
a unified particle-anatomy map.

The ontology the user remembers **exists and is more developed than a sketch** —
it spans ~17 companion papers and 6 case study files. The main gap is that pion,
muon, and tau treatments remain at draft status with no DOI-published canonical
version. If clean surface access to this ontology is needed, the recommended
entry point is Book 2's ontology section (Path A above), not a new document.
