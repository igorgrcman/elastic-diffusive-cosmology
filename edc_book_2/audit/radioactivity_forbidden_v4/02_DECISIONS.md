# DECISIONS V4

**Created**: 2026-01-31
**Purpose**: Document methodology and scope decisions

---

## Decision Registry

### D-V4-001: M5 and M6 Mechanism Addition

**Decision**: Add two new candidate mechanisms beyond V3's M1-M4:
- M5: Quasicrystalline/aperiodic bulk lattices
- M6: Multi-shell core-mantle coordination mismatch

**Rationale**: V3 only covered 4 mechanisms; V4 requirement specifies 6
**Source support**: M5 [P] (no source); M6 [P/I] (domain-wall in 22826edd:4847)

---

### D-V4-002: FT Table Structure

**Decision**: Create FT-37..FT-47 entries with uniform structure:
- n value, forbidden status, prime factorization
- Candidate mechanisms (M1-M6) with likelihood
- Predicted decay mode preference
- Falsification test
- Citations

**Rationale**: Systematic coverage of entire forbidden zone

---

### D-V4-003: EDC Annotation Blocks

**Decision**: Each decay chain step gets an "EDC frustration bookkeeping block":
```
EDC BLOCK:
- d(n) direction: [↓ decreasing / ↑ increasing / ~ stable]
- Active mechanism: [M1/M2/M3/M4/M5/M6]
- Branching: [Y/N, ratio if known]
- Notes: [qualitative interpretation]
```

**Rationale**: Makes EDC interpretation explicit and traceable

---

### D-V4-004: Nucleus as Defect-Rich Crystal

**Decision**: Model heavy nuclei as finite, defect-rich analogs of bulk crystals:
- Core: attempts n ≈ 43 (forbidden)
- Surface: lower coordination (frustrated interface)
- Defects: α-clusters, domain walls

**Source**: 22826edd:41 "EDC string/defect sliku"

---

### D-V4-005: No Invented Branching Ratios

**Decision**: All branching ratios marked [BL:SOURCE_TBD] unless from mined sources
**Qualitative only**: "α-favored", "β-favored", "competitive"

**Rationale**: G2 guardrail (no hallucinated numerics)

---

### D-V4-006: Stable ID System

**Decision**: Use stable identifiers across V4:
- FT-XX: Forbidden topologies (FT-37, FT-38, ...)
- LAW-XX: Laws (LAW-1 through LAW-6+)
- GEN-XX: Generalizations (GEN-1 through GEN-5+)
- OQ-V4-XXX: Open questions
- DN-XXX: Donors (continue from V3 numbering)

---

### D-V4-007: Falsification Ledger Requirement

**Decision**: 09_LAWS_AND_INVARIANTS_V4.md must contain:
- At least 8 falsifiable predictions
- Clear criteria for rejection
- Observable discriminators

**Rationale**: Science requires falsifiability

---

### D-V4-008: Mechanism State Variables

**Decision**: Each mechanism (M1-M6) must define:
- State variable (what quantity tracks mechanism activity)
- How it modifies n_eff
- How frustration ε_f scales
- Preferred decay relief channel

**Rationale**: Makes mechanisms quantitatively comparable (even if qualitative)

---

### D-V4-009: V3 Inheritance

**Decision**: V4 inherits all V3 content; does not replace
- DONOR_TRACEBACK_V4 extends V3's DN-001..041
- LAW_REGISTRY_V4 extends V3's LAW-1..6, GEN-1..5
- Decay chains enhanced, not rewritten

---

## Summary

| ID | Topic | Decision |
|----|-------|----------|
| D-V4-001 | Mechanisms | Add M5, M6 |
| D-V4-002 | FT table | Full FT-37..47 |
| D-V4-003 | EDC blocks | Per-step annotation |
| D-V4-004 | Nucleus model | Defect-rich crystal |
| D-V4-005 | Branching | No invented ratios |
| D-V4-006 | IDs | Stable system |
| D-V4-007 | Falsification | 8+ tests |
| D-V4-008 | State vars | Per mechanism |
| D-V4-009 | Inheritance | Extends V3 |
