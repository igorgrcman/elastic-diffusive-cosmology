# DECISIONS V5

**Created**: 2026-01-31
**Purpose**: Document methodology and scope decisions

---

## Decision Registry

### D-V5-001: Donor Target 50+

**Decision**: Extend donor count from V4's 45 to 50+ with new targeted searches

**Method**: Grep for keywords in 22826edd_full.md, verify line ranges

---

### D-V5-002: Main Chain Reconstruction

**Decision**: Task 1 requires baseline chain reconstruction:
Z₆ → allowed n → n≈43 forbidden → frustration → ΔV_eff → G-N law

**Constraint**: No new claims; citations required for each step

---

### D-V5-003: Beyond-M43 Focus

**Decision**: FT table must explicitly address:
"Can heavy nuclides form other topological structures besides M43 and forbidden 44–47?"

**Answer format**: Structured "Yes-if / No-if" with discriminants

---

### D-V5-004: Mechanism Formalization

**Decision**: Each mechanism M1-M6 must define:
1. State variable
2. n_eff modification
3. ε_f scaling
4. Decay mode prediction
5. Observable discriminator
6. Falsification test

---

### D-V5-005: EDC Block Standard

**Decision**: Decay chain steps use standard EDC annotation block:
```
DC-XXX: [Parent] → [Daughter] ([Mode])
- n(A): [value] [P/I/Der]
- d(n): [value] (toward [36/48])
- Mechanism: [M1-M6]
- Prediction: [α/β/SF] [P]
- Branching: [Y/N] (ratio if known)
```

---

### D-V5-006: No Hallucinated Data

**Decision**: All nuclear data [BL:SOURCE_TBD] unless:
1. Present in mined sources with citation
2. Present in V4 with citation chain

---

### D-V5-007: Verification Plan

**Decision**: Create explicit upgrade path:
[P] → [I]: What data would infer
[I] → [Der]: What derivation would prove

---

### D-V5-008: Notebook Index

**Decision**: Create 14_NOTEBOOK_INDEX with:
- Key line ranges for each law/claim
- Cross-reference to donor IDs
- Quick lookup capability

---

## Summary

| ID | Topic | Decision |
|----|-------|----------|
| D-V5-001 | Donors | Target 50+ |
| D-V5-002 | Baseline | Full reconstruction |
| D-V5-003 | Beyond M43 | Explicit answer |
| D-V5-004 | Mechanisms | Full formalization |
| D-V5-005 | EDC blocks | Standard format |
| D-V5-006 | Data | No hallucination |
| D-V5-007 | Upgrade | Explicit path |
| D-V5-008 | Index | Quick lookup |
