# DEPENDENCY GRAPH — Book 2 Narrative Audit

**Branch**: book2-chapter-audit-v1
**Date**: 2026-01-24
**Status**: Phase N1 COMPLETE

---

## Conceptual Flow Diagram

```
                        ┌─────────────────────────────────────────────────┐
                        │           PART I: FOUNDATIONS                   │
                        └─────────────────────────────────────────────────┘
                                           │
                    ┌──────────────────────┼──────────────────────┐
                    ▼                      ▼                      ▼
              ┌─────────┐           ┌─────────┐           ┌─────────┐
              │  CH02   │           │  CH03   │           │  CH04   │
              │ Frozen  │ ────────▶ │   Z₆    │ ────────▶ │   EW    │
              │ Regime  │           │ Program │           │ Params  │
              └─────────┘           └─────────┘           └─────────┘
                    │                    │                      │
                    │                    │                      │
                    │         ┌──────────┼──────────────────────┤
                    │         │          │                      │
                    ▼         ▼          ▼                      ▼
              ┌───────────────────────────────────────────────────────┐
              │                 CH01: Weak Interface                   │
              │          (Pipeline: Absorption → Release)             │
              └───────────────────────────────────────────────────────┘
                                           │
                        ┌──────────────────┼──────────────────┐
                        ▼                  ▼                  ▼
                  ┌─────────┐        ┌─────────┐        ┌─────────┐
                  │  CH05   │        │  CH06   │        │  CH07   │
                  │ Lepton  │        │  3 Gen  │        │Neutrino │
                  │ Masses  │        │ Count   │        │  Edge   │
                  └─────────┘        └─────────┘        └─────────┘
                        │                  │                  │
                        └──────────────────┼──────────────────┘
                                           ▼
                                     ┌─────────┐
                                     │  CH08   │
                                     │CKM + CP │
                                     └─────────┘
                                           │
                        ┌──────────────────┼──────────────────┐
                        ▼                  ▼                  ▼
                  ┌─────────┐        ┌─────────┐        ┌─────────┐
                  │  CH09   │        │  CH10   │        │  CH11   │
                  │  V-A    │ ──────▶│ EW      │ ──────▶│  G_F    │
                  │Structure│        │ Bridge  │        │Derivatn │
                  └─────────┘        └─────────┘        └─────────┘
                        │                                     │
                        │                 ┌───────────────────┤
                        │                 ▼                   ▼
                        │           ┌─────────┐        ┌─────────┐
                        │           │  CH12   │        │  CH13   │
                        └──────────▶│Epistemic│ ◀──────│G_F Clos │
                                    │   Map   │        │Attempts │
                                    └─────────┘        └─────────┘
                                           │                  │
                                           └────────┬─────────┘
                                                    ▼
                                              ┌─────────┐
                                              │  CH14   │
                                              │  BVP    │
                                              │Workpkg  │
                                              └─────────┘
```

---

## Adjacency List (Forward Dependencies)

| Source | → Targets | Type |
|--------|-----------|------|
| CH02 | CH03, CH04, CH01, CH05 | Frozen regime enables all |
| CH03 | CH01, CH04, CH05, CH06 | Z₆ factorization propagates |
| CH04 | CH01, CH05, CH09, CH10, CH11 | EW parameters used |
| CH01 | CH09, CH11 | Weak interface to V-A |
| CH05 | CH06, CH07, CH08 | Lepton structure |
| CH06 | CH07, CH08 | Generation count |
| CH07 | CH08 | Neutrino to CKM |
| CH08 | CH09, CH11 | Flavor to coupling |
| CH09 | CH10, CH11, CH14 | V-A central |
| CH10 | CH11, CH14 | Bridge to G_F |
| CH11 | CH12, CH13 | G_F chain |
| CH12 | CH13, CH14 | Epistemic hub |
| CH13 | CH14 | Closure to BVP |

---

## Critical Chains

### Chain 1: Geometry → Electroweak Parameters
```
CH02 (Frozen) → CH03 (Z₆) → CH04 (sin²θ_W = 1/4) → CH11 (G_F)
```
**Epistemic flow:** [P] → [Dc] → [Dc] → [Dc/I]

### Chain 2: Chirality → Weak Coupling
```
CH02 (M⁵ bulk) → CH09 (V-A) → CH10 (EW Bridge) → CH11 (G_F)
```
**Epistemic flow:** [P] → [Dc] → [P/I] → [Dc/I]

### Chain 3: Generation Structure → Mixing
```
CH03 (Z₃ ⊂ Z₆) → CH06 (N_gen=3) → CH07 (PMNS) → CH08 (CKM)
```
**Epistemic flow:** [M] → [I] → [I] → [I/Cal]

### Chain 4: G_F Closure
```
CH04 (θ_W) ──┐
CH09 (V-A) ──┼→ CH11 (G_F spine) → CH13 (attempts) → CH14 (BVP)
CH10 (BC) ───┘
```
**Epistemic flow:** [Dc] + [Dc] + [P] → [Dc/I] → [open] → [open]

---

## OPR Dependencies

| OPR | Defined In | Used By | Status |
|-----|------------|---------|--------|
| OPR-01 | CH06 | CH07, CH08 | YELLOW |
| OPR-02 | CH06 | CH14 | RED |
| OPR-03 | CH06 | — | RED |
| OPR-07 | CH09 | CH07 | OPEN |
| OPR-09–12 | CH08 | — | OPEN |
| OPR-17 | CH04, CH09 | CH10, CH11 | YELLOW |
| OPR-19 | CH11, CH13 | CH14 | RED-C |
| OPR-20 | CH10, CH11, CH13 | CH14 | RED-C |
| OPR-21 | CH11, CH13 | CH14 | RED |
| OPR-22 | CH11, CH13 | CH14 | RED |

---

## Teleport Risk Analysis

**Definition:** A "teleport" is when a concept/symbol appears without prior introduction.

### LOW RISK (well-connected)
- sin²θ_W: CH03 → CH04 → CH11 (explicit chain)
- V-A structure: CH09 → CH10 → CH11 (explicit chain)
- G_F: CH11 → CH12 → CH13 → CH14 (explicit chain)
- Z₆ factorization: CH02 → CH03 → everywhere (documented)

### MEDIUM RISK (could use bridging)
- m_φ (mediator mass): First appears CH10, not fully derived
- ℓ (brane layer): Appears CH10/CH11, origin unclear
- Robin BC α: CH10 introduces, needs physics motivation
- I₄ overlap: CH11 defines, BVP computes, needs bridge

### HIGH RISK (potential teleports)
- δ = R_ξ identification: Appears in OPR-20 attempts, lacks derivation
- π₁(M⁵) = Z₃: Mentioned CH06, never computed
- KK truncation mechanism: Proposed CH06, never executed

---

## Cross-Chapter Reference Summary

| Pattern | Count | Notes |
|---------|-------|-------|
| Forward refs (→) | 47 | Normal flow |
| Backward refs (←) | 12 | Intentional callbacks |
| OPR references | 23 | Open problem tracking |
| Framework v2.0 refs | 8 | Canonical source |
| Baseline [BL] refs | 31 | PDG/CODATA anchors |

---

*Generated: 2026-01-24*
*Audit Protocol: book2-narrative-audit-v1*
