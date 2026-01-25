# Symbol Decision Protocol

Authority: Published artifacts (Framework v2.0, Paper 2, Companions A–H, Book Part I)
Status: CANON LAW — Book 2 must conform
Generated: 2026-01-24

---

## Purpose

This document defines HOW to classify symbol usage context and make replacement decisions.
NO blind grep/replace is ever permitted.

---

## 1. Decision Flowchart

```
SYMBOL DETECTED IN BOOK 2
          │
          ▼
┌─────────────────────────────────┐
│ Step 1: IDENTIFY PHYSICAL ROLE  │
│ What does this symbol represent │
│ in the LOCAL context (±10 lines)?│
└─────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────┐
│ Step 2: CLASSIFY CONTEXT        │
│ Choose exactly ONE class:       │
│  (A) 5D compact coordinate      │
│  (B) 3D spatial coordinate      │
│  (C) Z6 complex variable        │
│  (D) Mass parameter             │
│  (E) Manifold symbol            │
│  (F) Dummy integration variable │
│  (G) Topology label             │
│  (H) Other (must explain)       │
└─────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────┐
│ Step 3: LOOKUP CANON RULE       │
│ Check SYMBOL_MASTER_TABLE.md    │
│ for this class + symbol combo   │
└─────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────┐
│ Step 4: DETERMINE ACTION        │
│  • Matches canon → OK           │
│  • Violates canon → MUST-FIX    │
│  • Ambiguous → TODO-REVIEW      │
└─────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────┐
│ Step 5: DOCUMENT                │
│ Add entry to LEDGER before      │
│ making any change               │
└─────────────────────────────────┘
```

---

## 2. Context Classification Rules

### Class A: 5D Compact Coordinate

**Indicators**:
- Appears in 5D field arguments: φ(x^μ, ?)
- Used as compact dimension: ? ∈ [0, 2πR]
- Profile functions: f(?)
- Separation in extra dimension: Δ?
- KK reduction context
- "Bulk coordinate", "depth", "extra dimension"

**Canon requirement**: Must use **ξ** (xi), never z.

### Class B: 3D Spatial Coordinate

**Indicators**:
- Appears in (x, y, z) tuple
- Explicit "3D spatial" context
- No 5D/bulk/compact dimension indicators

**Canon requirement**: May use **z**.

### Class C: Z6 Complex Variable

**Indicators**:
- Appears as z₁, z₂ (subscripted)
- Z6 symmetry context
- Polynomial roots, complex plane
- NOT a coordinate

**Canon requirement**: Use **z₁, z₂** (not z alone).

### Class D: Mass Parameter

**Indicators**:
- Appears in energy/mass formulas
- Dimensional analysis gives mass
- Examples: M_5 in G_5 ~ 1/M_5², Planck mass

**Canon requirement**: Use **M_{5,Pl}** for 5D Planck mass, never M_5 or M5.

### Class E: Manifold Symbol

**Indicators**:
- Topology context: π₁(M), M = ... × S¹
- "Bulk manifold", "5D spacetime"
- Geometric/topological statements

**Canon requirement**: Use **\mathcal{M}^5**, never M5 or M_5.

### Class F: Dummy Integration Variable

**Indicators**:
- Inside integral: ∫...d?
- Summation index
- No physical meaning outside the expression

**Canon requirement**: Document explicitly. May use any symbol if scoped.

### Class G: Topology Label

**Indicators**:
- S¹, S³, B³ as topological spaces
- NOT coordinates

**Canon requirement**: S¹ is topology, ξ is coordinate on it.

### Class H: Other

If none of the above apply, explain the physical role explicitly.

---

## 3. Decision Log Format

Every classification decision must be logged:

```markdown
| ID | File | Line | Symbol | Class | Canon Rule | Decision | Rationale |
```

**ID format**: `VR-###` (Violation Report number)

**Decision values**:
- `OK` — matches canon
- `MUST-FIX` — violates canon, unambiguous fix
- `TODO-REVIEW` — ambiguous, needs human judgment
- `COLLISION` — symbol has multiple meanings in same file

---

## 4. Hard Rules (No Exceptions)

### Rule R1: z → ξ for 5D Depth
If z is used as the 5D compact coordinate, it MUST be replaced with ξ.
**Check**: Does the context mention "extra dimension", "bulk", "compact"?

### Rule R2: M5/M_5 → \mathcal{M}^5 for Manifold
If M5 or M_5 refers to the 5D bulk manifold, use \mathcal{M}^5.
**Check**: Is this topology/geometry (manifold) or physics (mass scale)?

### Rule R3: M5/M_5 → M_{5,Pl} for Mass
If M_5 appears in mass formulas (G ~ 1/M²), use M_{5,Pl}.
**Check**: Does dimensional analysis give mass?

### Rule R4: Subscripted z₁, z₂ are Z6 Variables
Never confuse with coordinates. Check for Z6/polynomial context.

### Rule R5: ξ Collision — Coherence Length
Paper 2 uses ξ for both 5D coordinate AND GL coherence length.
**Resolution**: When coherence length meaning is needed, use ξ_GL.

---

## 5. Verification After Any Change

After making any symbol replacement:

1. Run `tools/symbol_audit.py` — check violation count decreased
2. Run `tools/gate_notation.sh` — check forbidden patterns
3. Run full build — verify 0 errors, 0 undefined refs
4. Confirm page count unchanged (387)

---

## 6. Escalation

If a symbol cannot be classified with certainty:

1. Add entry to REPLACEMENT_RISK_LEDGER.md with status TODO-REVIEW
2. Include context snippet (±5 lines)
3. Explain why ambiguous
4. Do NOT change the symbol
5. Tag for human review

---

## Version History

| Date | Change | By |
|------|--------|-----|
| 2026-01-24 | Initial creation | Claude |
