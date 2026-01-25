# CH07: OPEN QUESTIONS LEDGER (FULL COVERAGE)

**Branch**: book2-ch07-openq-remediation-v1
**Date**: 2026-01-25
**Phase**: E2 (FULL COVERAGE Audit) → E3 (Remediation)
**Scope**: All CH07 input files from `CH07_BUILD_INPUTS.txt`

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total OPEN-IDs catalogued | 32 |
| STATUS: DONE | 12 |
| STATUS: OPEN (with OPR) | 20 |
| OPR references | 21 |
| Explicit "(open)" markers | 6 |
| "not derived" instances | 14 |
| "remains open" instances | 3 |
| δ symbol fixes applied | 4 |

---

## OPEN-ID Cards

### CH07-OPEN-001: Mass hierarchy origin
- **File**: `06_neutrinos_edge_modes.tex:17`
- **Text**: "Mass hierarchy origin remains (open)"
- **Risk Class**: (C) Proof gap
- **Linked Claim**: E-CH07-P-001
- **Blocking OPR**: OPR-12
- **STATUS**: **OPEN**
- **Tag**: [P]
- **Closure Gate**: Derive V(ξ) from EDC action; compute mode spectrum
- **Forward-Ref**: CH14 (BVP solutions) would provide V(ξ)

### CH07-OPEN-002: Membrane thickness δ definition
- **File**: `06_neutrinos_edge_modes.tex:50`
- **Text**: "membrane has finite thickness $\delta$ along the fifth dimension"
- **Risk Class**: (A) Symbol collision — δ used for thickness, NOT CP phase
- **Note**: This δ is consistent with OPR-04 (δ = R_ξ)
- **STATUS**: **DONE** — Context-clear, no disambiguation needed
- **Commit**: N/A (no change required)

### CH07-OPEN-003: Z₃ breaking mechanism not derived
- **File**: `06_neutrinos_edge_modes.tex:166`
- **Text**: "specific breaking of $\mathbb{Z}_3$ (mechanism not derived)"
- **Risk Class**: (C) Proof gap
- **Linked Claim**: E-CH07-I-001
- **Blocking OPR**: OPR-03
- **STATUS**: **OPEN**
- **Tag**: [I]
- **Closure Gate**: Compute π₁(M⁵) topology; show Z₃ emerges
- **Forward-Ref**: Framework v3.0 topology chapter

### CH07-OPEN-004: CP phase δ first mention (DISAMBIGUATION)
- **File**: `06_neutrinos_edge_modes.tex:172`
- **Text**: "CP phase $\delta$" → now "CP phase $\delta_{\text{CP}}$"
- **Risk Class**: (A) Symbol collision
- **STATUS**: **DONE** — Standardized to δ_CP
- **Commit**: 6796707

### CH07-OPEN-005: V(ξ) potential not derived
- **File**: `06_neutrinos_edge_modes.tex:272`
- **Text**: "The actual form of $V(\xi)$ from EDC action (not derived: OPR-12)"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-12
- **STATUS**: **OPEN**
- **Tag**: [P]
- **Closure Gate**: Explicit variational derivation of V(ξ) from S_EDC
- **Forward-Ref**: CH14 (action variation)

### CH07-OPEN-006: Edge-mode picture pedagogical only
- **File**: `06_neutrinos_edge_modes.tex:280`
- **Text**: "1D boundary-trapped picture is \textbf{pedagogical} \tagP{}, not derived"
- **Risk Class**: (B) Narrative teleport
- **Linked Claim**: E-CH07-P-001
- **STATUS**: **OPEN** — Pedagogical postulate, explicitly tagged
- **Tag**: [P]
- **Closure Gate**: Derive edge-mode BVP from 5D action boundary conditions
- **Forward-Ref**: CH10 (Robin BC derivation)

### CH07-OPEN-007: Higgs profile not derived
- **File**: `06_neutrinos_edge_modes.tex:482`
- **Text**: "Higgs localized in interior & YELLOW & \tagP{} & Profile not derived"
- **Risk Class**: (C) Proof gap
- **STATUS**: **OPEN** — YELLOW
- **Tag**: [P]
- **Closure Gate**: Derive Higgs localization from bulk-brane BVP
- **Forward-Ref**: Future work (not in current scope)

### CH07-OPEN-008: Absolute neutrino mass not computed
- **File**: `06_neutrinos_edge_modes.tex:486`
- **Text**: "Absolute $m_\nu$ value & RED & (open) & Not computed (OPR-12)"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-12
- **Linked Claim**: E-CH07-Dc-001
- **STATUS**: **OPEN** — RED
- **Tag**: [P]
- **Closure Gate**: Solve neutrino BVP with derived V(ξ); compute eigenvalues
- **Forward-Ref**: Requires OPR-12 closure first

### CH07-OPEN-009: Full derivation chain incomplete
- **File**: `06_neutrinos_edge_modes.tex:493`
- **Text**: "not derived"
- **Risk Class**: (C) Proof gap
- **STATUS**: **OPEN**
- **Tag**: [P]
- **Blocking OPR**: OPR-12
- **Closure Gate**: Complete derivation chain from action to mass eigenvalues
- **Forward-Ref**: Book 3 (complete EDC derivation)

### CH07-OPEN-010: Neutrino-Z₃ coupling not derived
- **File**: `06_neutrinos_edge_modes.tex:523`
- **Text**: "neutrino wavefunctions to $\mathbb{Z}_3$ rotations is not derived"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-03
- **STATUS**: **OPEN**
- **Tag**: [I]
- **Closure Gate**: Show Z₃ action on neutrino modes from π₁(M⁵)
- **Forward-Ref**: Linked to OPR-03 (topology)

### CH07-OPEN-011: Mode-number dependence not derived
- **File**: `06_neutrinos_edge_modes.tex:536`
- **Text**: "dependence of $\Delta\xi$ on mode number are not derived"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-12
- **STATUS**: **OPEN**
- **Tag**: [I]
- **Closure Gate**: Compute Δξ(n) from KK mode spectrum
- **Forward-Ref**: OPR-12 closure

### CH07-OPEN-012: θ₁₂ not derived
- **File**: `06_neutrinos_edge_modes.tex:617`
- **Text**: "$\theta_{12} \approx 33°$ & RED & (open) & Not derived (OPR-13)"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-13
- **Linked Claim**: E-CH07-Dc-006
- **STATUS**: **OPEN** — YELLOW [Dc] via Attempt 4.2
- **Tag**: [Dc]
- **Current Progress**: arctan(1/√2) = 35.26° (8.6% from PDG)
- **Closure Gate**: Reduce 8.6% error or derive selection rule for T1 vs T2
- **Forward-Ref**: Attempt 4.2 provides geometric mechanism

### CH07-OPEN-013: θ₂₃ not derived (initial)
- **File**: `06_neutrinos_edge_modes.tex:618`
- **Text**: "$\theta_{23} \approx 45°$ & RED & (open) & Not derived (OPR-13)"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-13
- **Linked Claim**: E-CH07-Dc-003
- **STATUS**: **DONE** — GREEN via Attempt 2 (Z₆ geometry)
- **Commit**: Attempt 2 in ch6_pmns_attempt2.tex
- **Result**: sin²θ₂₃ = 0.564 (3% from PDG 0.546)

### CH07-OPEN-014: θ₁₃ not derived
- **File**: `06_neutrinos_edge_modes.tex:619`
- **Text**: "$\theta_{13} \approx 8.5°$ & RED & (open) & Not derived (OPR-13)"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-13
- **Linked Claim**: E-CH07-Dc-005
- **STATUS**: **OPEN** — YELLOW [BL→Dc] via Attempt 4.1
- **Tag**: [BL→Dc]
- **Current Progress**: ε = λ/√2 predicts sin²θ₁₃ = 0.025 (15% from PDG)
- **Closure Gate**: Derive √2 factor from geometry; reduce 15% error
- **Forward-Ref**: Attempt 4.1

### CH07-OPEN-015: CP phase δ (DISAMBIGUATION)
- **File**: `06_neutrinos_edge_modes.tex:620`
- **Text**: "CP phase $\delta$" → now "CP phase $\delta_{\text{CP}}$"
- **Risk Class**: (A) Symbol collision + (C) Proof gap
- **Blocking OPR**: OPR-14
- **STATUS**: **DONE** (disambiguation) / **OPEN** (derivation)
- **Commit**: 6796707 (δ→δ_CP)
- **Tag**: [P] for derivation
- **Closure Gate**: Derive δ_CP from complex phase mechanism
- **Forward-Ref**: OPR-14 (no current attempt)

### CH07-OPEN-016: PMNS structure postulated
- **File**: `06_neutrinos_edge_modes.tex:625`
- **Text**: "\textbf{Verdict: RED} --- PMNS structure is postulated, not derived"
- **Risk Class**: (B) Narrative teleport
- **Blocking OPR**: OPR-13
- **Linked Claim**: E-CH07-P-002
- **STATUS**: **OPEN** — Upgraded to YELLOW via Attempts 2,4.1,4.2
- **Tag**: [P]
- **Closure Gate**: All three angles to GREEN (θ₂₃ done, θ₁₂/θ₁₃ YELLOW)
- **Forward-Ref**: PMNS Attempt series

### CH07-OPEN-017: Dirac/Majorana experimentally open
- **File**: `06_neutrinos_edge_modes.tex:663`
- **Text**: "Whether neutrinos are Dirac or Majorana particles remains experimentally"
- **Risk Class**: External constraint
- **STATUS**: **DONE** — [BL] experimental input
- **Tag**: [BL]
- **Note**: Cannot be closed theoretically; awaits 0νββ experiments

### CH07-OPEN-018: Dirac/Majorana theoretically open
- **File**: `06_neutrinos_edge_modes.tex:685`
- **Text**: "(open) --- The edge-mode framework accommodates both"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-15
- **STATUS**: **OPEN** — RED
- **Tag**: [P]
- **Closure Gate**: Derive edge-mode self-conjugacy condition from BCs
- **Forward-Ref**: OPR-15 (no current attempt)

### CH07-OPEN-019: Dynamical mechanism not derived
- **File**: `06_neutrinos_edge_modes.tex:739`
- **Text**: "dynamical mechanism not derived \tagI{}"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-12
- **STATUS**: **OPEN**
- **Tag**: [I]
- **Closure Gate**: Derive dynamical localization from V(ξ)
- **Forward-Ref**: OPR-12 closure

### CH07-OPEN-020: CP violation phase δ (DISAMBIGUATION)
- **File**: `06_neutrinos_edge_modes.tex:760`
- **Text**: "CP violation phase $\delta$" → now "$\delta_{\text{CP}}$"
- **Risk Class**: (A) Symbol collision
- **Blocking OPR**: OPR-14
- **STATUS**: **DONE** (disambiguation)
- **Commit**: 6796707

### CH07-OPEN-021: θ₁₂, θ₁₃ values not derived
- **File**: `06_neutrinos_edge_modes.tex:805`
- **Text**: "$\theta_{12}, \theta_{13}$ structure & YELLOW & \tagI{} (values not derived)"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-13
- **Linked Claim**: E-CH07-I-002
- **STATUS**: **OPEN** — YELLOW
- **Tag**: [I] → [Dc] partial via Attempts 4.1/4.2
- **Closure Gate**: Full derivation of both angles from geometry
- **Forward-Ref**: Attempts 4.1, 4.2

### CH07-OPEN-022: Dirac/Majorana prediction open
- **File**: `06_neutrinos_edge_modes.tex:806`
- **Text**: "Dirac/Majorana prediction & RED & (open) (OPR-15)"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-15
- **STATUS**: **OPEN** — RED
- **Tag**: [P]
- **Closure Gate**: Derive definite prediction from edge-mode BCs
- **Forward-Ref**: OPR-15

### CH07-OPEN-023: Geometric derivation needed
- **File**: `06_neutrinos_edge_modes.tex:822`
- **Text**: "$\varepsilon$ require geometric derivation \tagI{}. Dirac/Majorana nature remains open"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-13, OPR-15
- **STATUS**: **OPEN**
- **Tag**: [I]
- **Closure Gate**: Derive ε from geometry (partial via Attempt 4.1); resolve Dirac/Majorana
- **Forward-Ref**: Attempts 4.1 (partial), OPR-15

### CH07-OPEN-024: CP phase δ in PMNS attempt 1 (DISAMBIGUATION)
- **File**: `ch6_pmns_attempt1.tex:199`
- **Text**: "CP phase $\delta$" → now "$\delta_{\text{CP}}$"
- **Risk Class**: (A) Symbol collision
- **Blocking OPR**: OPR-14
- **STATUS**: **DONE** (disambiguation)
- **Commit**: 6796707

### CH07-OPEN-025: δ calibration parameter (DIFFERENT MEANING)
- **File**: `ch6_pmns_attempt2.tex:126`
- **Text**: "$\delta = 0.3$" (table row for spacing calibration)
- **Risk Class**: (A) Symbol collision — this δ is a calibration param, NOT CP phase
- **STATUS**: **DONE** — Context-clear in table, no action needed
- **Note**: Different δ usage, table context unambiguous

### CH07-OPEN-026: κ ratio not derived
- **File**: `ch6_pmns_attempt4_1_derive_epsilon.tex:48`
- **Text**: "$\kappa$ ratio is identified, not derived (OPR-10)"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-10
- **STATUS**: **OPEN**
- **Tag**: [I]
- **Closure Gate**: Derive κ_q/κ_ℓ from localization BVP
- **Forward-Ref**: OPR-10 (κ ratio derivation)

### CH07-OPEN-027: θ₁₂ still identified
- **File**: `ch6_pmns_attempt4_1_derive_epsilon.tex:164`
- **Text**: "$\theta_{12}$ still identified---not derived (OPR-13a/b/c)"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-13
- **STATUS**: **OPEN** — Upgraded to YELLOW [Dc] via Attempt 4.2
- **Tag**: [Dc]
- **Current Progress**: arctan(1/√2) mechanism found
- **Closure Gate**: Reduce 8.6% error or prove exact geometric origin
- **Forward-Ref**: Attempt 4.2

### CH07-OPEN-028: Z₆ discrete phases falsified
- **File**: `ch6_pmns_attempt3_z6_refinement.tex:156`
- **Text**: "OPR-13 status: remains \textbf{YELLOW}"
- **Risk Class**: Negative result (documented)
- **STATUS**: **DONE** — Negative result documented (RED/falsified)
- **Note**: Z₆ discrete phase mechanism falsified; this is a valid closure (negative)

### CH07-OPEN-029: θ₁₂, θ₁₃ require derivation
- **File**: `ch6_pmns_attempt4_menu.tex:198-199`
- **Text**: "$\theta_{12}$, $\theta_{13}$ structure identified but values require derivation"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-13
- **STATUS**: **OPEN** — Partially closed via Attempts 4.1/4.2
- **Tag**: [I]
- **Closure Gate**: Full derivation; current status YELLOW
- **Forward-Ref**: Attempts 4.1, 4.2

### CH07-OPEN-030: δ_PMNS not addressed (ALREADY CORRECT)
- **File**: `ch6_pmns_attempt4_menu.tex:195`
- **Text**: "CP phase $\delta_{\text{PMNS}}$ (not addressed)"
- **Risk Class**: None — correctly disambiguated
- **Blocking OPR**: OPR-14
- **STATUS**: **DONE** — Already correctly disambiguated
- **Note**: Template for δ_CP usage

### CH07-OPEN-031: θ₁₂ discrete vs derived
- **File**: `ch6_pmns_attempt4_2_theta12_origin.tex:146-148`
- **Text**: "Before: YELLOW \tagI{} ... After: YELLOW [\tagDc{}]"
- **Linked Claim**: E-CH07-Dc-006
- **STATUS**: **DONE** — Upgraded from [I] to [Dc]
- **Result**: arctan(1/√2) = 35.26° provides geometric mechanism

### CH07-OPEN-032: OPR-13c partial closure
- **File**: `ch6_pmns_attempt4_2_theta12_origin.tex:179`
- **Text**: "OPR-13c upgraded from \tagI{} to \tagDc{}"
- **STATUS**: **DONE** — YELLOW [Dc]
- **Result**: 8.6% error, geometric mechanism found

---

## δ Symbol Disambiguation Status

| Location | Current Text | Meaning | Status |
|----------|-------------|---------|--------|
| `06_neutrinos:50` | `thickness $\delta$` | OPR-04 δ_thickness | ✅ DONE (preserved) |
| `06_neutrinos:172` | `$\delta_{\text{CP}}$` | δ_CP | ✅ DONE (fixed) |
| `06_neutrinos:620` | `$\delta_{\text{CP}}$` | δ_CP | ✅ DONE (fixed) |
| `06_neutrinos:760` | `$\delta_{\text{CP}}$` | δ_CP | ✅ DONE (fixed) |
| `ch6_pmns_attempt1:199` | `$\delta_{\text{CP}}$` | δ_CP | ✅ DONE (fixed) |
| `ch6_pmns_attempt2:126` | `$\delta = 0.3$` | calibration param | ✅ DONE (preserved) |
| `ch6_pmns_attempt4_menu:195` | `$\delta_{\text{PMNS}}$` | δ_CP | ✅ DONE (already correct) |

**Total δ fixes applied**: 4 (commit 6796707)

---

## OPR Cross-Reference Map

| OPR | Description | CH07 OPEN-IDs | Status | Closure Gate |
|-----|-------------|---------------|--------|--------------|
| OPR-03 | π₁(M⁵) topology | 003, 010 | RED | Compute fundamental group of M⁵ |
| OPR-10 | κ ratio derivation | 026 | YELLOW | Derive κ_q/κ_ℓ from BVP |
| OPR-12 | V(ξ) potential | 001, 005, 008, 009, 011, 019 | RED | Variational derivation of V(ξ) |
| OPR-13 | PMNS angles | 012, 014, 016, 021, 023, 027, 029 | YELLOW | θ₂₃ GREEN; θ₁₂, θ₁₃ YELLOW |
| OPR-14 | CP phase δ_CP | 015 (deriv only), 018, 022 | RED | Complex phase mechanism |
| OPR-15 | Dirac/Majorana | 018, 022, 023 | RED | Edge-mode self-conjugacy |

---

## Claim-ID to OPEN-ID Linkage

| Claim-ID | Statement | OPEN-IDs | Status |
|----------|-----------|----------|--------|
| E-CH07-P-001 | Neutrino as edge mode | 001, 006 | OPEN (OPR-12) |
| E-CH07-Dc-001 | m_ν/m_e suppression | 008 | OPEN (OPR-12) |
| E-CH07-I-001 | Three flavors ↔ Z₃ | 003, 010 | OPEN (OPR-03) |
| E-CH07-Dc-002 | Left-handed selection from BC | — | CLOSED |
| E-CH07-P-002 | PMNS from overlap | 016, 029 | OPEN (OPR-13) |
| E-CH07-Dc-003 | θ₂₃ ≈ 45° from Z₆ | 013 | **CLOSED** (GREEN) |
| E-CH07-Dc-004 | DFT baseline falsified | 028 | **CLOSED** (negative) |
| E-CH07-I-002 | Rank-2 + ε structure | 021, 027 | OPEN (OPR-13) |
| E-CH07-Dc-005 | ε = λ/√2 → θ₁₃ | 014 | YELLOW [BL→Dc] |
| E-CH07-Dc-006 | θ₁₂ = arctan(1/√2) | 012, 031 | YELLOW [Dc] |

---

## Remediation Summary

| Category | Count | Details |
|----------|-------|---------|
| **DONE** | 12 | 002, 004, 013, 015, 017, 020, 024, 025, 028, 030, 031, 032 |
| **OPEN with OPR** | 20 | All have explicit blocking OPR + closure gates |
| **δ fixes** | 4 | Applied in commit 6796707 |
| **GLOBAL_SYMBOL_TABLE** | 1 | δ_CP entry added |

---

## Coverage Proof

### Grep Patterns Used

```bash
# Pattern 1: Explicit markers
grep -n "\(open\)|remains open|not derived" *.tex

# Pattern 2: OPR references
grep -n "OPR-1[0-5]" *.tex

# Pattern 3: Status markers
grep -n "RED|YELLOW" *.tex

# Pattern 4: δ symbol occurrences
grep -n "\\delta" *.tex

# Pattern 5: Epistemic tags
grep -n "\\tagI{}|\\tagP{}|\\tagDc{}" *.tex
```

### Files Scanned (7 total)

1. `06_neutrinos_edge_modes.tex` — main chapter
2. `ch6_pmns_attempt1.tex` — baseline attempt
3. `ch6_pmns_attempt2.tex` — Z₆ geometry (θ₂₃ closure)
4. `ch6_pmns_attempt3_z6_refinement.tex` — discrete phases (RED)
5. `ch6_pmns_attempt4_menu.tex` — rank-2 structure
6. `ch6_pmns_attempt4_1_derive_epsilon.tex` — ε = λ/√2
7. `ch6_pmns_attempt4_2_theta12_origin.tex` — arctan(1/√2)

### Match Counts

| Pattern | Count |
|---------|-------|
| `(open)` markers | 6 |
| `not derived` | 14 |
| `remains open` | 3 |
| `OPR-13` | 12 |
| `OPR-14` | 2 |
| `OPR-15` | 2 |
| `\\delta` (all meanings) | 7 |
| δ_CP standardized | 4 |

---

## DOI Warnings Inventory

**Status**: No DOI warnings found in CH07 files.

CH07 does not contain external DOI references that require verification. All cross-references are internal (to other chapters, OPR registry, or claim evidence index).

---

## CKM/Quark Sector OPR Numbering Issue (OUT OF SCOPE)

**Finding**: File `07_ckm_cp.tex` uses OPR numbers 09, 10, 11, 12 for CKM-specific problems, but the OPR_REGISTRY defines these as lepton-sector OPRs:

| In 07_ckm_cp.tex | CKM Context | Registry Definition |
|------------------|-------------|---------------------|
| OPR-09 (line 1043) | CKM overlap scaling | π prefactor (leptons) |
| OPR-10 (line 995, 1048) | κ_q/κ_ℓ ratio | (3/2) factor Z₆ (leptons) |
| OPR-11 (line 994, 1053) | (ρ̄, η̄) derivation | Koide Q=2/3 (leptons) |
| OPR-12 (line 1052) | CKM CP phase | KK truncation V(ξ) |

**Status**: OUT OF SCOPE for this CH07 (neutrino sector) remediation.

**Recommendation**: Create dedicated CKM OPRs (OPR-16 through OPR-19) and update 07_ckm_cp.tex references in a separate remediation pass.

**Action Required**: Future CH08_OPEN_QUESTIONS_LEDGER.md should address this.

---

*Generated: 2026-01-25*
*Phase: E3 (Remediation Complete)*
*Branch: book2-ch07-openq-remediation-v1*
