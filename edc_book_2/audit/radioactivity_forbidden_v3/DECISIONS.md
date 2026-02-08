# DECISIONS V3: Research Methodology Decisions

**Created**: 2026-01-31
**Purpose**: Document all methodology and scope decisions

---

## Decision Registry

### D-V3-001: Citation Precision Requirement

**Decision**: All donor citations must include file path AND line range (not just file)

**Rationale**: V2 had file-level citations; V3 requires reproducibility down to exact lines

**Format**: `file.md:start-end` (e.g., `22826edd_full.md:2440-2540`)

---

### D-V3-002: Exclude M43 from Forbidden Catalog

**Decision**: FORBIDDEN_CATALOG.md covers n=37..47 but n=43 gets separate treatment as "nuclear saturation optimum"

**Rationale**:
- n=43 is the ONLY forbidden value with physical significance (n_opt ≈ 43.3)
- It deserves separate analysis, not just a row in a table
- Already covered extensively in LAW-2 (DN-010, DN-011)

---

### D-V3-003: Decay Chain EDC Annotations

**Decision**: All decay chain files include EDC annotation columns with [Open] placeholders

**Columns**: A, n(A) Estimate, d(n), Frustration Level, Mode Explanation

**Rationale**: Prepare for future n(A) formula integration (OQ-V2-007)

---

### D-V3-004: Nuclear Data Blocking

**Decision**: ALL nuclear data (t₁/₂, Q, branching ratios) marked [BL:SOURCE_TBD]

**Rationale**:
- Guardrail: no hallucinated numerics
- Data must come from NNDC/IAEA via approved channel
- Prevents false precision in research notes

---

### D-V3-005: Epistemic Tag System

**Decision**: Use 6-tier epistemic tag system consistently:

| Tag | Meaning | Example |
|-----|---------|---------|
| [Der] | Derived from axioms | n = 2^a × 3^b from Z₆ |
| [I] | Inferred from fit/pattern | G-N law R² = 0.9941 |
| [P] | Proposed/hypothetical | Mode selection from d(n) |
| [Cal] | Calibrated from data | K ≈ 0.8 MeV |
| [BL] | Blocked (needs source) | t₁/₂ values |
| [Open] | Unresolved question | n(A) formula |

---

### D-V3-006: Crystal/Lattice Add-on Scope

**Decision**: Crystal add-on focuses on:
1. Allowed bulk structures (n = 2^a × 3^b compatible)
2. Forbidden structures (n = 5, 7, 11 incompatible)
3. Mapping to physical crystals (FCC, BCC, HCP)

**Exclusion**: No discussion of quasicrystals without source support

---

### D-V3-007: n(A) Research Strategy

**Decision**: N_A_MAPPING_RESEARCH.md structured as:
1. What sources say about n(A)
2. Candidate formulas with epistemic tags
3. Upgrade checklist (what would promote [P] → [I] → [Der])

**Rationale**: OQ-V2-007 is "kingpin" - closing it unlocks chain verification

---

### D-V3-008: Supernova Hypothesis Status

**Decision**: Keep supernova hypothesis as [P] with explicit "no source support" note

**Evidence**: Grep returned 0 matches for "supernova" in mined sessions

**Path to upgrade**: Would need r-process derivation from EDC principles

---

### D-V3-009: V3 vs V2 Relationship

**Decision**: V3 is refinement of V2, not replacement

**V3 additions**:
- DONOR_TRACEBACK.md (precise citations)
- N_A_MAPPING_RESEARCH.md (new focus area)
- EPSILON_F_RESEARCH.md (new focus area)
- Crystal add-on (3 files)

**V2 carried forward**: Laws, decay chains, forbidden matrix (refined)

---

## Summary Table

| ID | Topic | Decision | Impact |
|----|-------|----------|--------|
| D-V3-001 | Citations | file:line-range required | Reproducibility |
| D-V3-002 | M43 | Separate from catalog | Special treatment |
| D-V3-003 | Chains | EDC annotation columns | Future n(A) integration |
| D-V3-004 | Data | [BL:SOURCE_TBD] blocking | No hallucination |
| D-V3-005 | Tags | 6-tier system | Consistency |
| D-V3-006 | Crystal | 3-file add-on scope | Tractable scope |
| D-V3-007 | n(A) | Research structure | Kingpin focus |
| D-V3-008 | Supernova | [P] no source | Honest tagging |
| D-V3-009 | V2/V3 | Refinement not replacement | Continuity |
