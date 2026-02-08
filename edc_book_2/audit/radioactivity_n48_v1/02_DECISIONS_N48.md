# DECISIONS N48 (V6)

**Created**: 2026-01-31
**Purpose**: Document methodology decisions for N48 module

---

## Decision Registry

### D-N48-001: n vs N Distinction
**Decision**: n = coordination number (topological), N = neutron number (not primary focus)
**Rationale**: V6 scope specifies n=48 as coordination target, not magic number N=48
**Impact**: All formulas use n(A), not N

### D-N48-002: Local vs Global Interpretation
**Decision**: Allow LOCAL effective n interpretation for heavy nuclei
**Rationale**: Global n(A) for A~300 falls in forbidden zone; must explain metastability
**Impact**: Enables M1, M2, M6 mechanisms

### D-N48-003: Default c = 6.1
**Decision**: Use c = 6.1 as default in n(A) = c × A^(1/3)
**Rationale**: Produces n(208) ≈ 36 (Pb stability) and n(488) ≈ 48 (SHE target)
**Range**: c ∈ [5.5, 8.0] documented as [P]

### D-N48-004: No New Mining
**Decision**: Use only files in audit/jsonl_mining/ and V4/V5 folders
**Rationale**: G8 guardrail; avoid context explosion
**Impact**: All citations from existing extracted files

### D-N48-005: Symbolic-First Pipeline
**Decision**: Keep Q, Z as symbols; only compute n(A), d(n)
**Rationale**: No [BL] numerics without source
**Impact**: Toy model is qualitative trend predictor only

### D-N48-006: Branching Rule as Testable Hypothesis
**Decision**: H-N48-01 stated as [P] with explicit falsification tests
**Rationale**: Cannot claim [Der] without full derivation chain
**Impact**: Scorecard approach shows current validation level

### D-N48-007: Mechanism Taxonomy Extends V4
**Decision**: M1-M6 inherited from V4; M7-M8 added as new [P]
**Rationale**: Maintain continuity; clearly mark extensions
**Impact**: 6 mechanisms grounded, 2 speculative

### D-N48-008: Assumption Ledger Mandatory
**Decision**: Every [P] tracked in file 11
**Rationale**: G11 guardrail; enables systematic upgrade path
**Impact**: 15 assumptions documented

---

## Summary Table

| ID | Topic | Decision |
|----|-------|----------|
| D-N48-001 | n vs N | Coordination, not neutrons |
| D-N48-002 | Scope | Local n allowed |
| D-N48-003 | Default c | 6.1 with range |
| D-N48-004 | Sources | No new mining |
| D-N48-005 | Pipeline | Symbolic-first |
| D-N48-006 | Branching | Testable [P] |
| D-N48-007 | Mechanisms | V4 + 2 new |
| D-N48-008 | Assumptions | All tracked |
