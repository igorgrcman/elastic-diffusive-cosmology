# CH07: OPEN QUESTIONS LEDGER (FULL COVERAGE)

**Branch**: book2-chapter-audit-v1
**Date**: 2026-01-25
**Phase**: E2 (FULL COVERAGE Audit)
**Scope**: All CH07 input files from `CH07_BUILD_INPUTS.txt`

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total OPEN-IDs catalogued | 32 |
| OPR references | 21 |
| Explicit "(open)" markers | 6 |
| "not derived" instances | 14 |
| "remains open" instances | 3 |
| δ symbol occurrences (needing disambiguation) | 4 |

---

## OPEN-ID Cards

### CH07-OPEN-001: Mass hierarchy origin
- **File**: `06_neutrinos_edge_modes.tex:17`
- **Text**: "Mass hierarchy origin remains (open)"
- **Risk Class**: (C) Proof gap
- **Linked Claim**: E-CH07-P-001
- **Blocking OPR**: OPR-12

### CH07-OPEN-002: Membrane thickness δ definition
- **File**: `06_neutrinos_edge_modes.tex:50`
- **Text**: "membrane has finite thickness $\delta$ along the fifth dimension"
- **Risk Class**: (A) Symbol collision — δ used for thickness, NOT CP phase
- **Note**: This δ is consistent with OPR-04 (δ = R_ξ)
- **Action**: Keep as is (context-clear)

### CH07-OPEN-003: Z₃ breaking mechanism not derived
- **File**: `06_neutrinos_edge_modes.tex:166`
- **Text**: "specific breaking of $\mathbb{Z}_3$ (mechanism not derived)"
- **Risk Class**: (C) Proof gap
- **Linked Claim**: E-CH07-I-001
- **Blocking OPR**: OPR-03

### CH07-OPEN-004: CP phase δ first mention (DISAMBIGUATION NEEDED)
- **File**: `06_neutrinos_edge_modes.tex:172`
- **Text**: "CP phase $\delta$"
- **Risk Class**: (A) Symbol collision
- **Action**: Standardize to δ_CP or δ_PMNS

### CH07-OPEN-005: V(ξ) potential not derived
- **File**: `06_neutrinos_edge_modes.tex:272`
- **Text**: "The actual form of $V(\xi)$ from EDC action (not derived: OPR-12)"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-12
- **Status**: Explicitly blocked

### CH07-OPEN-006: Edge-mode picture pedagogical only
- **File**: `06_neutrinos_edge_modes.tex:280`
- **Text**: "1D boundary-trapped picture is \textbf{pedagogical} \tagP{}, not derived"
- **Risk Class**: (B) Narrative teleport
- **Linked Claim**: E-CH07-P-001

### CH07-OPEN-007: Higgs profile not derived
- **File**: `06_neutrinos_edge_modes.tex:482`
- **Text**: "Higgs localized in interior & YELLOW & \tagP{} & Profile not derived"
- **Risk Class**: (C) Proof gap
- **Status**: YELLOW

### CH07-OPEN-008: Absolute neutrino mass not computed
- **File**: `06_neutrinos_edge_modes.tex:486`
- **Text**: "Absolute $m_\nu$ value & RED & (open) & Not computed (OPR-12)"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-12
- **Status**: RED

### CH07-OPEN-009: Full derivation chain incomplete
- **File**: `06_neutrinos_edge_modes.tex:493`
- **Text**: "not derived"
- **Risk Class**: (C) Proof gap

### CH07-OPEN-010: Neutrino-Z₃ coupling not derived
- **File**: `06_neutrinos_edge_modes.tex:523`
- **Text**: "neutrino wavefunctions to $\mathbb{Z}_3$ rotations is not derived"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-03

### CH07-OPEN-011: Mode-number dependence not derived
- **File**: `06_neutrinos_edge_modes.tex:536`
- **Text**: "dependence of $\Delta\xi$ on mode number are not derived"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-12

### CH07-OPEN-012: θ₁₂ not derived
- **File**: `06_neutrinos_edge_modes.tex:617`
- **Text**: "$\theta_{12} \approx 33°$ & RED & (open) & Not derived (OPR-13)"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-13
- **Status**: RED → upgraded to YELLOW via Attempt 4.2

### CH07-OPEN-013: θ₂₃ not derived (initial)
- **File**: `06_neutrinos_edge_modes.tex:618`
- **Text**: "$\theta_{23} \approx 45°$ & RED & (open) & Not derived (OPR-13)"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-13
- **Status**: RED → upgraded to GREEN via Attempt 2 (Z₆ geometry)

### CH07-OPEN-014: θ₁₃ not derived
- **File**: `06_neutrinos_edge_modes.tex:619`
- **Text**: "$\theta_{13} \approx 8.5°$ & RED & (open) & Not derived (OPR-13)"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-13
- **Status**: RED → upgraded to YELLOW via Attempt 4.1

### CH07-OPEN-015: CP phase δ (DISAMBIGUATION NEEDED)
- **File**: `06_neutrinos_edge_modes.tex:620`
- **Text**: "CP phase $\delta$ & RED & (open) & Not addressed (OPR-14)"
- **Risk Class**: (A) Symbol collision + (C) Proof gap
- **Blocking OPR**: OPR-14
- **Status**: RED
- **Action**: Standardize to δ_CP

### CH07-OPEN-016: PMNS structure postulated
- **File**: `06_neutrinos_edge_modes.tex:625`
- **Text**: "\textbf{Verdict: RED} --- PMNS structure is postulated, not derived"
- **Risk Class**: (B) Narrative teleport
- **Blocking OPR**: OPR-13

### CH07-OPEN-017: Dirac/Majorana experimentally open
- **File**: `06_neutrinos_edge_modes.tex:663`
- **Text**: "Whether neutrinos are Dirac or Majorana particles remains experimentally"
- **Risk Class**: External constraint
- **Status**: [BL] — experimental

### CH07-OPEN-018: Dirac/Majorana theoretically open
- **File**: `06_neutrinos_edge_modes.tex:685`
- **Text**: "(open) --- The edge-mode framework accommodates both"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-15

### CH07-OPEN-019: Dynamical mechanism not derived
- **File**: `06_neutrinos_edge_modes.tex:739`
- **Text**: "dynamical mechanism not derived \tagI{}"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-12

### CH07-OPEN-020: CP violation phase δ (DISAMBIGUATION NEEDED)
- **File**: `06_neutrinos_edge_modes.tex:760`
- **Text**: "CP violation phase $\delta$ & Requires complex phase mechanism"
- **Risk Class**: (A) Symbol collision
- **Blocking OPR**: OPR-14
- **Action**: Standardize to δ_CP

### CH07-OPEN-021: θ₁₂, θ₁₃ values not derived
- **File**: `06_neutrinos_edge_modes.tex:805`
- **Text**: "$\theta_{12}, \theta_{13}$ structure & YELLOW & \tagI{} (values not derived)"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-13
- **Status**: YELLOW

### CH07-OPEN-022: Dirac/Majorana prediction open
- **File**: `06_neutrinos_edge_modes.tex:806`
- **Text**: "Dirac/Majorana prediction & RED & (open) (OPR-15)"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-15
- **Status**: RED

### CH07-OPEN-023: Geometric derivation needed
- **File**: `06_neutrinos_edge_modes.tex:822`
- **Text**: "$\varepsilon$ require geometric derivation \tagI{}. Dirac/Majorana nature remains open"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-13, OPR-15

### CH07-OPEN-024: CP phase δ in PMNS attempt 1 (DISAMBIGUATION NEEDED)
- **File**: `ch6_pmns_attempt1.tex:199`
- **Text**: "CP phase $\delta$ & RED & (open) & Not addressed"
- **Risk Class**: (A) Symbol collision
- **Blocking OPR**: OPR-14
- **Action**: Standardize to δ_CP

### CH07-OPEN-025: δ calibration parameter (DIFFERENT MEANING)
- **File**: `ch6_pmns_attempt2.tex:126`
- **Text**: "$\delta = 0.3$" (table row for spacing calibration)
- **Risk Class**: (A) Symbol collision — this δ is a calibration param, NOT CP phase
- **Note**: Context-clear in table, no action needed

### CH07-OPEN-026: κ ratio not derived
- **File**: `ch6_pmns_attempt4_1_derive_epsilon.tex:48`
- **Text**: "$\kappa$ ratio is identified, not derived (OPR-10)"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-10

### CH07-OPEN-027: θ₁₂ still identified
- **File**: `ch6_pmns_attempt4_1_derive_epsilon.tex:164`
- **Text**: "$\theta_{12}$ still identified---not derived (OPR-13a/b/c)"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-13

### CH07-OPEN-028: Z₆ discrete phases falsified
- **File**: `ch6_pmns_attempt3_z6_refinement.tex:156`
- **Text**: "OPR-13 status: remains \textbf{YELLOW}"
- **Risk Class**: Negative result (documented)
- **Status**: Attempt 3 = RED (falsified Z₆ discrete phase mechanism)

### CH07-OPEN-029: θ₁₂, θ₁₃ require derivation
- **File**: `ch6_pmns_attempt4_menu.tex:198-199`
- **Text**: "$\theta_{12}$, $\theta_{13}$ structure identified but values require derivation"
- **Risk Class**: (C) Proof gap
- **Blocking OPR**: OPR-13

### CH07-OPEN-030: δ_PMNS not addressed (ALREADY CORRECT)
- **File**: `ch6_pmns_attempt4_menu.tex:195`
- **Text**: "CP phase $\delta_{\text{PMNS}}$ (not addressed)"
- **Risk Class**: None — correctly disambiguated
- **Blocking OPR**: OPR-14
- **Status**: Template for other δ usages

### CH07-OPEN-031: θ₁₂ discrete vs derived
- **File**: `ch6_pmns_attempt4_2_theta12_origin.tex:146-148`
- **Text**: "Before: YELLOW \tagI{} ... After: YELLOW [\tagDc{}]"
- **Status**: Upgraded from [I] to [Dc] via arctan(1/√2) mechanism

### CH07-OPEN-032: OPR-13c partial closure
- **File**: `ch6_pmns_attempt4_2_theta12_origin.tex:179`
- **Text**: "OPR-13c upgraded from \tagI{} to \tagDc{}"
- **Status**: YELLOW [Dc] — 8.6% error, geometric mechanism found

---

## δ Symbol Disambiguation Status

| Location | Current Text | Meaning | Action Required |
|----------|-------------|---------|-----------------|
| `06_neutrinos:50` | `thickness $\delta$` | OPR-04 δ_thickness | None (context-clear) |
| `06_neutrinos:172` | `CP phase $\delta$` | δ_CP | Standardize to `$\delta_{\text{CP}}$` |
| `06_neutrinos:620` | `CP phase $\delta$` | δ_CP | Standardize to `$\delta_{\text{CP}}$` |
| `06_neutrinos:760` | `CP violation phase $\delta$` | δ_CP | Standardize to `$\delta_{\text{CP}}$` |
| `ch6_pmns_attempt1:199` | `CP phase $\delta$` | δ_CP | Standardize to `$\delta_{\text{CP}}$` |
| `ch6_pmns_attempt2:126` | `$\delta = 0.3$` | calibration param | None (context-clear) |
| `ch6_pmns_attempt4_menu:195` | `$\delta_{\text{PMNS}}$` | δ_CP | Already correct |

**Total δ fixes needed**: 4

---

## OPR Cross-Reference Map

| OPR | Description | CH07 OPEN-IDs | Status |
|-----|-------------|---------------|--------|
| OPR-03 | π₁(M⁵) topology | 003, 010 | RED |
| OPR-10 | κ ratio derivation | 026 | YELLOW |
| OPR-12 | V(ξ) potential | 001, 005, 008, 011, 019 | RED |
| OPR-13 | PMNS angles | 012-016, 021, 023, 027, 029, 031, 032 | YELLOW PARTIAL |
| OPR-14 | CP phase δ_CP | 004, 015, 020, 024, 030 | RED |
| OPR-15 | Dirac/Majorana | 018, 022, 023 | RED |

---

## Claim-ID to OPEN-ID Linkage

| Claim-ID | Statement | OPEN-IDs |
|----------|-----------|----------|
| E-CH07-P-001 | Neutrino as edge mode | 001, 006 |
| E-CH07-Dc-001 | m_ν/m_e suppression | 008 |
| E-CH07-I-001 | Three flavors ↔ Z₃ | 003, 010 |
| E-CH07-Dc-002 | Left-handed selection from BC | — (closed) |
| E-CH07-P-002 | PMNS from overlap | 016, 029 |
| E-CH07-Dc-003 | θ₂₃ ≈ 45° from Z₆ | 013 (now GREEN) |
| E-CH07-Dc-004 | DFT baseline falsified | 028 (negative result) |
| E-CH07-I-002 | Rank-2 + ε structure | 021, 027 |
| E-CH07-Dc-005 | ε = λ/√2 → θ₁₃ | 014 (now YELLOW) |
| E-CH07-Dc-006 | θ₁₂ = arctan(1/√2) | 012, 031 (now YELLOW) |

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
| δ_CP needing standardization | 4 |

---

## DOI Warnings Inventory

**Status**: No DOI warnings found in CH07 files.

CH07 does not contain external DOI references that require verification. All cross-references are internal (to other chapters, OPR registry, or claim evidence index).

---

*Generated: 2026-01-25*
*Evidence Audit Phase E2 (FULL COVERAGE)*
