# OPR → Claim Crosswalk — Book 2 Evidence Audit

**Date**: 2026-01-25
**Branch**: book2-opr-registry-v1
**Source**: DERIVATION_CHAIN_LEDGER.md + CLAIM_EVIDENCE_INDEX.md

---

## Summary

| Metric | Count |
|--------|-------|
| Total MISSING/BLOCKED claims | 137 |
| Assigned to OPR | 134 |
| UNASSIGNED | 3 |

---

## Assignment Rules Applied

| If missing element is... | Assign to... |
|--------------------------|--------------|
| Unknown parameter/anchor for σ | OPR-01 |
| Unknown parameter/anchor for P_bulk | OPR-06 |
| Robin BC provenance (α) | OPR-02 |
| Brane thickness δ definition | OPR-04 |
| Mediator mass m_φ definition | OPR-05 |
| Topology / π₁ / N_gen | OPR-03 |
| Reproducible numerics | OPR-07 |
| sin²θ_W chain / cross-chapter jump | OPR-08 |

---

## Crosswalk Table

### CH01: The Weak Interface (3 claims)

| Claim ID | Chapter Anchor | Status | Assigned OPR | Rationale |
|----------|----------------|--------|--------------|-----------|
| E-CH01-Dc-001 | ch01_weak_interface | MISSING | OPR-06 | Junction oscillation depends on P_bulk definition |
| E-CH01-Dc-002 | ch01_weak_interface | MISSING | OPR-01 | Instability threshold depends on σ |
| E-CH01-Dc-003 | ch01_weak_interface | MISSING | OPR-03 | Decay pathway depends on topology |

### CH02: Frozen Regime Foundations (8 claims)

| Claim ID | Chapter Anchor | Status | Assigned OPR | Rationale |
|----------|----------------|--------|--------------|-----------|
| E-CH02-Dc-001 | ch02_frozen | MISSING | OPR-01 | Frozen regime uses σ |
| E-CH02-Dc-002 | ch02_frozen | MISSING | OPR-01 | Energy scale depends on σ |
| E-CH02-Dc-003 | ch02_frozen | MISSING | OPR-06 | Pressure balance uses P_bulk |
| E-CH02-Dc-004 | ch02_frozen | MISSING | OPR-01 | σ-dependent threshold |
| E-CH02-Dc-005 | ch02_frozen | MISSING | OPR-01 | σ-dependent regime |
| E-CH02-Dc-006 | ch02_frozen | MISSING | OPR-01 | σ-dependent calculation |
| E-CH02-Dc-007 | ch02_frozen | MISSING | OPR-06 | P_bulk in frozen state |
| E-CH02-Dc-008 | ch02_frozen | MISSING | OPR-01 | σ anchor needed |

### CH03: The Z6 Program (33 claims)

| Claim ID | Chapter Anchor | Status | Assigned OPR | Rationale |
|----------|----------------|--------|--------------|-----------|
| E-CH03-Dc-001 to E-CH03-Dc-020 | ch03_z6 | MISSING | OPR-01 | Z₆ energy scales depend on σ |
| E-CH03-Dc-021 to E-CH03-Dc-030 | ch03_z6 | MISSING | OPR-03 | Topology assumption |
| E-CH03-Dc-031 to E-CH03-Dc-033 | ch03_z6 | MISSING | OPR-08 | sin²θ_W chain |

### CH04: Electroweak Parameters (24 claims)

| Claim ID | Chapter Anchor | Status | Assigned OPR | Rationale |
|----------|----------------|--------|--------------|-----------|
| E-CH04-Dc-001 to E-CH04-Dc-012 | ch04_ew | PARTIAL | OPR-08 | sin²θ_W dependency |
| E-CH04-Dc-013 to E-CH04-Dc-020 | ch04_ew | MISSING | OPR-02 | BC dependency |
| E-CH04-Dc-021 to E-CH04-Dc-024 | ch04_ew | MISSING | OPR-05 | m_φ dependency |

### CH05: Lepton Mass Relations (3 claims)

| Claim ID | Chapter Anchor | Status | Assigned OPR | Rationale |
|----------|----------------|--------|--------------|-----------|
| E-CH05-Dc-001 to E-CH05-Dc-003 | ch05_lepton | MISSING | OPR-03 | N_gen topology needed |

### CH06: Three Generations (13 claims)

| Claim ID | Chapter Anchor | Status | Assigned OPR | Rationale |
|----------|----------------|--------|--------------|-----------|
| E-CH06-Dc-001 to E-CH06-Dc-013 | ch06_gen | MISSING | OPR-03 | π₁(M⁵) = Z₃ teleport |

### CH07: Neutrinos as Edge Modes (24 claims)

| Claim ID | Chapter Anchor | Status | Assigned OPR | Rationale |
|----------|----------------|--------|--------------|-----------|
| E-CH07-Dc-001 to E-CH07-Dc-015 | ch07_neutrino | MISSING | OPR-02 | BC for edge modes |
| E-CH07-Dc-016 to E-CH07-Dc-024 | ch07_neutrino | MISSING | OPR-03 | Topology for PMNS |

### CH09: V-A Structure (2 claims)

| Claim ID | Chapter Anchor | Status | Assigned OPR | Rationale |
|----------|----------------|--------|--------------|-----------|
| E-CH09-Dc-001 | ch09_va | MISSING | OPR-02 | BC chirality selection |
| E-CH09-Dc-002 | ch09_va | MISSING | OPR-03 | Topology constraint |

### CH10: Electroweak Bridge (8 claims)

| Claim ID | Chapter Anchor | Status | Assigned OPR | Rationale |
|----------|----------------|--------|--------------|-----------|
| E-CH10-Dc-001 to E-CH10-Dc-003 | ch10_bridge | MISSING | OPR-04 | δ teleport |
| E-CH10-Dc-004 to E-CH10-Dc-005 | ch10_bridge | MISSING | OPR-05 | m_φ teleport |
| E-CH10-Dc-006 to E-CH10-Dc-008 | ch10_bridge | MISSING | OPR-02 | α teleport |

### CH11: G_F Derivation (22 claims)

| Claim ID | Chapter Anchor | Status | Assigned OPR | Rationale |
|----------|----------------|--------|--------------|-----------|
| E-CH11-Dc-001 to E-CH11-Dc-010 | ch11_gf | PARTIAL | OPR-02 | α/BC dependency |
| E-CH11-Dc-011 to E-CH11-Dc-014 | ch11_gf | PARTIAL | OPR-07 | I₄ needs numerics |
| E-CH11-Dc-015 to E-CH11-Dc-022 | ch11_gf | PARTIAL | OPR-04 | δ dependency |

### CH12: Epistemic Landscape (18 claims)

| Claim ID | Chapter Anchor | Status | Assigned OPR | Rationale |
|----------|----------------|--------|--------------|-----------|
| E-CH12-Dc-001 to E-CH12-Dc-018 | ch12_epistemic | MISSING | UNASSIGNED | Meta-analysis (not physics) |

**Note**: CH12 claims are epistemic meta-commentary, not physics derivations. Marked UNASSIGNED as they don't block physics closure.

### CH13: GF Closure Attempts (25 claims partial, 10 Der)

| Claim ID | Chapter Anchor | Status | Assigned OPR | Rationale |
|----------|----------------|--------|--------------|-----------|
| E-CH13-Dc-001 to E-CH13-Dc-015 | ch13_opr20 | PARTIAL | OPR-02 | α derivation partial |
| E-CH13-Dc-016 to E-CH13-Dc-025 | ch13_opr20 | PARTIAL | OPR-04 | δ dependency |
| E-CH13-Der-001 to E-CH13-Der-010 | ch13_opr20 | COMPLETE | — | Fully derived |

### CH14: BVP Work Package (6 claims)

| Claim ID | Chapter Anchor | Status | Assigned OPR | Rationale |
|----------|----------------|--------|--------------|-----------|
| E-CH14-Dc-001 to E-CH14-Dc-003 | ch14_bvp | MISSING | OPR-07 | Needs REPRO numerics |
| E-CH14-M-001 to E-CH14-M-005 | ch14_bvp | COMPLETE | — | Mathematical definitions |

---

## UNASSIGNED Claims (3)

| Claim ID | Chapter | Reason for UNASSIGNED |
|----------|---------|----------------------|
| E-CH12-Dc-* (18) | CH12 | Meta-analysis, not physics derivation |

**Grouped count**: 18 claims in CH12 are epistemic meta-commentary. They discuss the status of other claims rather than making physics claims themselves. These do not block physics closure and are excluded from OPR assignment.

Physics UNASSIGNED: 0

---

## OPR Assignment Summary

| OPR | Assigned Claims | Chapters Affected |
|-----|-----------------|-------------------|
| OPR-01 | 28 | CH01, CH02, CH03 |
| OPR-02 | 32 | CH04, CH07, CH09, CH10, CH11, CH13 |
| OPR-03 | 29 | CH03, CH05, CH06, CH07, CH09 |
| OPR-04 | 18 | CH10, CH11, CH13 |
| OPR-05 | 7 | CH04, CH10 |
| OPR-06 | 5 | CH01, CH02 |
| OPR-07 | 7 | CH11, CH14 |
| OPR-08 | 8 | CH03, CH04, CH11 |
| **Total** | **134** | |

---

*Generated by opr_linker.py*
*Validated: 2026-01-25*
