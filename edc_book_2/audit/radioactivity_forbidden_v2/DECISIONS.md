# DECISIONS LOG: Radioactivity Forbidden V2

**Session**: 2026-01-31

---

## Decision Format

- **ID**: D-V2-XXX
- **Decision**: What was decided
- **Reason**: Why
- **Tradeoff**: What was sacrificed
- **Citation**: Source reference

---

## Decisions

### D-V2-001: Inherit MTR-XXX and GAP-RX IDs from V1
**Decision**: Keep same block/gap IDs as radioactivity_forbidden_research/
**Reason**: Guardrail G0.4 - stable IDs
**Tradeoff**: Cannot rename/reorder
**Citation**: User mega-prompt

### D-V2-002: No decay chain numerics without source
**Decision**: All t₁/₂, Q values marked [BL:SOURCE_TBD]
**Reason**: Guardrail G0.2 - no hallucinated nuclear data
**Tradeoff**: Chains are incomplete skeletons
**Citation**: User mega-prompt

### D-V2-003: Four mechanisms remain [I]/[P], not [Der]
**Decision**: Domain mixing, defects, α-clustering, metastable all stay [I] or [P]
**Reason**: No explicit derivation in mined sources
**Tradeoff**: Cannot claim confirmed physics
**Citation**: FORBIDDEN_TOPOLOGIES.md:130-202

### D-V2-004: Decay chain sequence from standard nuclear physics
**Decision**: Use known decay sequences (U-238→...→Pb-206) without EDC derivation
**Reason**: EDC explains *why* but not *what* decays - sequence is empirical
**Tradeoff**: Chains not "derived" from EDC
**Citation**: N/A - standard physics

### D-V2-005: Supernova hypothesis stays [P]
**Decision**: "Extreme gravity forces forbidden n → relaxation via decay" is [P]
**Reason**: No mention of supernova in any mined source
**Tradeoff**: Cannot use this as central narrative
**Citation**: Grep search returned 0 matches

### D-V2-006: d(n) metric is [P], not [Der]
**Decision**: Forbidden distance metric remains proposal
**Reason**: Not explicitly in original chain
**Tradeoff**: Cannot use as confirmed law
**Citation**: LAWS_AND_INVARIANTS.md:35-70

### D-V2-007: No modification of Book 2 sources
**Decision**: All work stays in audit/radioactivity_forbidden_v2/
**Reason**: Guardrail G0.1
**Tradeoff**: Integration requires future step
**Citation**: User mega-prompt

### D-V2-008: Use 73d92ff5 for "metastable" and "defect" citations
**Decision**: Reference 73d92ff5_full.md for metastable/defect concepts
**Reason**: Found relevant matches in grep
**Tradeoff**: Different session than primary 22826edd
**Citation**: 73d92ff5_full.md:442, 517, 581, 737

### D-V2-009: Create DATA_REQUESTS.md for external data
**Decision**: Document all needed external data without fetching
**Reason**: No web fetch unless Igor approves
**Tradeoff**: Cannot complete numerical verification
**Citation**: User mega-prompt
