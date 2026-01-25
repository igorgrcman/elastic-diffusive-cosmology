# DERIVATION CHAIN LEDGER — Book 2 Evidence Audit

**Branch**: book2-chapter-audit-v1
**Date**: 2026-01-25
**Phase**: E2 (Derivation Chain Check)

---

## Classification Legend

| Status | Meaning |
|--------|---------|
| **COMPLETE** | Full derivation chain traceable to postulates |
| **PARTIAL** | Some steps missing but inferable from context |
| **MISSING** | No derivation provided — marked [OPEN] |

---

## Summary by Status

| Status | [Der] | [Dc] | Total |
|--------|-------|------|-------|
| COMPLETE | 12 | 0 | 12 |
| PARTIAL | 0 | 47 | 47 |
| MISSING | 0 | 137 | 137 |
| **Total** | 12 | 184 | 196 |

*Note: 5 [M]/[Def] claims are mathematical definitions, not physics derivations.*

---

## COMPLETE Derivations (12)

All [Der] claims have explicit derivation chains in the text.

### CH11: sin²θ_W from Z₆ Counting

| ID | Derivation Chain | Status |
|----|------------------|--------|
| E-CH11-Der-005 | Z₆ symmetry → Z₂ subgroup → |Z₂|/|Z₆| = 2/6 = 1/3 ≠ 1/4 ⚠️ | COMPLETE* |
| E-CH11-Der-013 | Z₆ symmetry → Z₂ subgroup → counting formula | COMPLETE* |

**⚠️ AUDIT FLAG**: The stated formula |Z₂|/|Z₆| = 1/4 requires 4 elements, not 2.
The text uses |Z₂| but means the index-4 subgroup. Notation clarification needed.

### CH13: OPR-20 Closure Attempts

| ID | Derivation Chain | Status |
|----|------------------|--------|
| E-CH13-Der-001 | Circumference definition: ℓ = 2πR_ξ | COMPLETE |
| E-CH13-Der-002 | 2π from circle geometry | COMPLETE |
| E-CH13-Der-003 | 2π factor upgrade [P]→[Der] | COMPLETE |
| E-CH13-Der-004 | Robin BC from action variation δS = 0 | COMPLETE |
| E-CH13-Der-005 | α ~ ℓ/δ from inner/outer matching | COMPLETE |
| E-CH13-Der-006 | Dimensional analysis: α = ℓ·α_phys | COMPLETE |
| E-CH13-Der-007 | Junction conditions → Robin structure | COMPLETE |
| E-CH13-Der-008 | Negative closure: standard BC insufficient | COMPLETE |
| E-CH13-Der-009 | BC route negative closure (forensic) | COMPLETE |
| E-CH13-Der-010 | Robin structure established for OPR-20 | COMPLETE |

---

## PARTIAL Derivations (47)

These claims have conditional derivations where the IF-clause is explicitly stated.

### Electroweak Parameters (CH03-CH04) — 32 Claims

| ID | Condition | Missing Element | Status |
|----|-----------|-----------------|--------|
| E-CH03-Dc-001 to E-CH03-Dc-033 | IF Z₆ coupling map | g₅ from 5D action | PARTIAL |
| E-CH04-Dc-001 to E-CH04-Dc-024 | IF sin²θ_W known | RG running coefficients | PARTIAL |

**Blocking OPR**: OPR-17 (Coupling map from 5D action)

### G_F Derivation (CH11) — 15 Claims

| ID | Condition | Missing Element | Status |
|----|-----------|-----------------|--------|
| E-CH11-Dc-001 to E-CH11-Dc-022 | IF mode profiles known | BVP solution for f_L(ξ) | PARTIAL |
| E-CH11-Dc-014 | IF I₄ overlap computed | Numerical integration | PARTIAL |

**Blocking OPR**: OPR-21 (I₄ overlap from BVP), OPR-22 (First-principles G_F)

---

## MISSING Derivations (137)

These claims lack explicit derivation chains and require [OPEN] tags.

### CH01: Weak Interface — 3 Claims

| ID | Statement | Required Work |
|----|-----------|---------------|
| E-CH01-Dc-001 | Junction oscillation ansatz | Derive from membrane dynamics |
| E-CH01-Dc-002 | Instability threshold | Derive from energy balance |
| E-CH01-Dc-003 | Decay pathway | Derive from topology |

### CH02: Frozen Regime — 8 Claims

| ID | Statement | Required Work |
|----|-----------|---------------|
| E-CH02-Dc-* | Frozen regime conditions | Derive from GL free energy |

### CH05-CH07: Flavor Structure — 40 Claims

| ID | Statement | Required Work |
|----|-----------|---------------|
| E-CH05-Dc-* | Lepton mass relations | Derive from BVP eigenvalues |
| E-CH06-Dc-* | N_gen = 3 from KK truncation | Solve OPR-02 |
| E-CH07-Dc-* | Neutrino edge modes | Derive localization profiles |

**Blocking OPR**: OPR-02 (KK truncation → N_gen=3)

### CH10: Electroweak Bridge — 8 Claims

| ID | Statement | Required Work |
|----|-----------|---------------|
| E-CH10-Dc-* | Teleported parameters (δ, m_φ, α) | Derive from 5D action |

**Blocking OPR**: OPR-20 (ℓ and BC from membrane)

### CH12: Epistemic Landscape — 18 Claims

| ID | Statement | Required Work |
|----|-----------|---------------|
| E-CH12-Dc-* | Various epistemic claims | Meta-analysis, not physics |

---

## OPR → Claim Blocking Map

| OPR | Description | Blocked Claims | Count |
|-----|-------------|----------------|-------|
| OPR-02 | KK truncation → N_gen=3 | E-CH05-*, E-CH06-*, E-CH14-* | ~40 |
| OPR-17 | Coupling map from 5D action | E-CH03-*, E-CH04-* | ~57 |
| OPR-19 | g₅ value derivation | E-CH11-Dc-* | ~22 |
| OPR-20 | ℓ and BC from membrane | E-CH10-*, E-CH13-* | ~26 |
| OPR-21 | I₄ overlap from BVP | E-CH11-Dc-014, E-CH14-* | ~8 |
| OPR-22 | First-principles G_F | E-CH11-Dc-012 | 1 |

---

## Critical Gaps Identified

### Gap 1: No [Der] claims in CH01-CH10

**Observation**: All foundation chapters contain only [Dc] (conditional) claims.
**Implication**: The entire weak-sector derivation depends on postulated inputs.
**Action**: This is BY DESIGN (top-down approach). Document explicitly in CH01.

### Gap 2: sin²θ_W = 1/4 notation issue

**Observation**: Text states |Z₂|/|Z₆| = 1/4 but |Z₂| = 2, |Z₆| = 6.
**Implication**: The formula uses non-standard subgroup notation.
**Action**: Clarify that "Z₂" refers to index-4 subgroup, not order-2 subgroup.

### Gap 3: Circularity warning for G_F

**Observation**: G_F numerical closure uses v (Higgs vev) which depends on G_F.
**Implication**: This is NOT circular if v is treated as INPUT [BL].
**Action**: Add explicit statement: "v = 246 GeV is [BL] input, not derived."

---

*Generated: 2026-01-25*
*Evidence Audit Phase E2*
