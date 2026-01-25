# OPR Policy — Book 2 Canon

**Status**: CANON (immutable once merged)
**Date**: 2026-01-25
**Branch**: book2-opr-registry-v1

---

## What is an OPR?

An **Open Problem Registry (OPR)** entry documents a specific gap in the derivation chain that prevents a physics claim from being fully derived ([Der]) from first principles.

OPRs are NOT:
- Vague "future work" items
- Wishlist features
- Editorial improvements

OPRs ARE:
- Precise statements of what is missing
- Binary closure conditions
- Traceable to specific blocked claims

---

## OPR Categories

| Code | Category | Description |
|------|----------|-------------|
| **[A]** | Action/EOM | Derivation from 5D action (bulk, brane, GHY, Israel) |
| **[B]** | Boundary/BC | Robin/Israel conditions, junctions, normalization |
| **[C]** | Constant/Anchor | Independent measurement/calibration of 5D quantity |
| **[N]** | Numerics/Repro | Reproducible script with hashed output |
| **[T]** | Topology/Geometry | Manifold structure, π₁, embeddings, Z₆ program |
| **[X]** | Cross-chapter | Missing bridge/definition from earlier chapter |

---

## OPR Status Definitions

| Status | Meaning |
|--------|---------|
| **OPEN** | No progress; blocking element not addressed |
| **PARTIAL** | Some progress; explicit IF-conditions documented |
| **CLOSED** | Closure test passes; derivation chain complete |

---

## Required Fields for Each OPR

Every OPR entry MUST include:

1. **ID**: OPR-XX [Category]
2. **Short name**: One-line identifier
3. **Missing**: Precise statement of what is absent
4. **Blocks**: List of claim IDs + chapter anchors
5. **Minimum closure deliverable**: Concrete bullet list
6. **Closure test**: Binary pass/fail condition
7. **No-smuggling note**: How closure avoids circular calibration

---

## No-Smuggling Principle

**Definition**: A derivation "smuggles" if it uses a downstream result as input to derive an upstream quantity.

**Example of smuggling**:
- Using G_F (derived) to constrain σ (postulated) → INVALID
- Using σ (postulated) to derive G_F (result) → VALID

**Rule**: Every OPR closure must demonstrate that no downstream-derived values were used as inputs.

---

## Closure Test Requirements

A closure test must be:
1. **Binary**: Either PASS or FAIL, no "maybe"
2. **Verifiable**: Can be checked by running a script or tracing equations
3. **Documented**: Result recorded in OPR_REGISTRY.md

**Valid closure tests**:
- "α appears as coefficient in boundary term variation; matches BVP BC"
- "Script repro_gf.py produces G_F within 1% of PDG; output hash matches"
- "Equation chain (E1)→(E2)→(E3)→result exists with all inputs tagged"

**Invalid closure tests**:
- "Seems reasonable"
- "Approximately matches"
- "Will be derived later"

---

## OPR Lifecycle

```
OPEN → work on closure → PARTIAL (if IF-conditions explicit)
                       → CLOSED (if closure test passes)
```

**Downgrade rule**: A CLOSED OPR can revert to OPEN if:
- The derivation is found to smuggle
- A gate fails that depends on the closure
- The closure test is invalidated

---

## Integration with Audit

1. **OPR_REGISTRY.md** is the authoritative source for all OPRs
2. **OPR_CLAIM_CROSSWALK.md** maps every blocked claim to an OPR
3. **tools/opr_linker.py** validates the crosswalk
4. No claim may remain "MISSING" without an assigned OPR
5. Any new symbol/teleport/BC dependency must map to an OPR before merge

---

## Amendment Process

To add a new OPR:
1. Propose in a branch with justification
2. Show which claims are blocked
3. Define closure test
4. Review and merge

To close an OPR:
1. Provide evidence (equation chain, script output, hash)
2. Run opr_linker.py to verify no regressions
3. Update OPR_REGISTRY.md status to CLOSED
4. Document in closure notes

---

*This policy is CANON for Book 2. Violations block merge.*
