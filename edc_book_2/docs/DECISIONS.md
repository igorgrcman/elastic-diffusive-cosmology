# DECISIONS.md — Architectural Decision Records

**Last updated:** 2026-01-28

---

## Format

```
### ADR-XXX: [Title]
**Date:** YYYY-MM-DD
**Status:** Accepted / Superseded / Deprecated
**Context:** [Why decision was needed]
**Decision:** [What was decided]
**Rationale:** [Why this option]
**Alternatives considered:** [Other options]
**Consequences:** [Impact]
```

---

## ADR-001: L₀/δ = 9.33 for Dynamic Processes

**Date:** 2026-01-28
**Status:** Accepted (with noted tension)

**Context:**
Two candidate values exist for L₀/δ:
- Route S (Static): π² ≈ 9.87 — optimizes m_p
- Route D (Dynamic): 9.33 — optimizes τ_n

The difference is only 5.5% but produces factor ~30 difference in τ_n due to exponential sensitivity.

**Decision:**
Use L₀/δ = 9.33 for neutron lifetime calculations.

**Rationale:**
- Gives τ_n ≈ 879 s with reasonable prefactor A ≈ 0.84
- Route S would require A ≈ 0.03 (unrealistic)
- Physical interpretation: dynamic processes "see" effective scale due to quantum/boundary corrections

**Alternatives considered:**
- Use π² everywhere: rejected (τ_n off by factor 30)
- Derive unique value from action: OPEN PROBLEM

**Consequences:**
- m_p prediction has +4.9% error (acceptable)
- Internal tension documented but unresolved
- Need to derive effective scale from 5D action

---

## ADR-002: Rename M6 Model → Topological Pinning Model

**Date:** 2026-01-28
**Status:** Accepted

**Context:**
Original model was called "M6" assuming coordination n = 6 (honeycomb). Analysis showed:
- Multiple coordinations are allowed: n = 2^a × 3^b
- Predictions for α-cluster nuclei are independent of n
- "M6" name is misleading

**Decision:**
Rename to "Topological Pinning Model" throughout.

**Rationale:**
- More accurate description of the mechanism (pinning, not specific coordination)
- Avoids confusion about n = 6 being special
- Emphasizes that K (from σ) is the key parameter, not n

**Alternatives considered:**
- Keep "M6" as historical name: rejected (confusing)
- Use "Mn Model" with variable n: rejected (still implies n is central)

**Consequences:**
- File renamed: BOOK_SECTION_M6_TOPOLOGICAL_MODEL.tex → BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex
- All references updated
- Commit 115177f

---

## ADR-003: Epistemic Honesty on τ_n Precision

**Date:** 2026-01-28
**Status:** Accepted

**Context:**
Red team critique identified inconsistency:
- Some places claimed "<1% error" for τ_n
- This was misleading because prefactor A = 0.84 is calibrated [Cal], not derived

**Decision:**
Distinguish uncalibrated and calibrated results explicitly:
- Uncalibrated (A = 1): τ_n ~ 10³ s (order of magnitude)
- Calibrated (A = 0.84): τ_n ≈ 879 s

**Rationale:**
- Epistemic honesty requires marking [Cal] vs [Dc]
- "<1%" only true because we tuned A
- The real achievement is getting correct ORDER OF MAGNITUDE from topology

**Alternatives considered:**
- Claim "<1%" is valid since A is O(1): rejected (misleading)
- Drop τ_n result entirely: rejected (still valuable)

**Consequences:**
- Updated BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex
- Updated BOOK_SECTION_NEUTRON_LIFETIME.tex
- Summary table status changed to [Dc/Cal]*
- Commits a94a7e0, cc32549

---

## ADR-004: Coordination Constraint Grounding

**Date:** 2026-01-28
**Status:** Accepted

**Context:**
Red team critique noted that "n = 43 forbidden because prime" sounds like numerology.

**Decision:**
Ground the constraint in geometry:
1. Y-junction trivalent constraint → factor 3
2. Quantum spin/isospin doubling → factors of 2
3. Therefore n = 2^a × 3^b

**Rationale:**
- "43 is prime" is consequence, not explanation
- Geometric argument shows WHY only factors 2 and 3 are allowed
- This is a constraint from junction geometry, not numerology

**Alternatives considered:**
- Leave as "prime forbidden": rejected (sounds like numerology)
- Remove n = 43 discussion: rejected (important result)

**Consequences:**
- Added explicit geometric argument in tex files
- Changed language from "prime > 3" to "n ≠ 2^a × 3^b"
- Commit a94a7e0

---

## ADR-005: Adopt Stateless Workflow with Mandatory Docs

**Date:** 2026-01-28
**Status:** Accepted

**Context:**
CC loses context between sessions. Previous work gets forgotten, leading to:
- Re-deriving already-established results
- Inconsistent claims
- Lost decisions

**Decision:**
Implement 3-layer memory system:
1. CLAUDE.md with mandatory workflow rules
2. docs/SESSION_LOG.md as append-only bookkeeping
3. Git hooks/CI to enforce documentation updates

**Rationale:**
- CC is stateless — treat it as a tool, not collaborator
- Externalize memory to repo
- Force documentation through automation

**Alternatives considered:**
- Trust CC to remember: rejected (doesn't work)
- Manual reminders: rejected (unreliable)

**Consequences:**
- Created docs/ directory with 5 mandatory files
- Created CLAUDE.md with workflow rules
- Git hook planned (not yet implemented)

---

## Open Decisions (Pending)

### PENDING-001: Unique Value for L₀/δ
How to resolve π² vs 9.33 tension?

### PENDING-002: Derive Prefactor A
What calculation method for fluctuation determinant?

### PENDING-003: Pure G_F Derivation
How to derive weak coupling without circular input?
