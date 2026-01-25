# Symbol Collision Map

Authority: Published artifacts (Framework v2.0, Paper 2, Companions A–H, Book Part I)
Status: CANON LAW — collisions must be resolved per rules below
Generated: 2026-01-24

---

## Purpose

This document lists REAL symbol collisions (same symbol, different meanings across canon)
and provides resolution rules for Book 2.

---

## Collision Registry

### COLLISION-001: ξ (5D Coordinate vs. Coherence Length)

| Aspect | Value |
|--------|-------|
| Symbol | ξ |
| Meaning A | 5D compact coordinate ∈ [0, 2πR_ξ) |
| Source A | Framework v2.0 Eq.(3) — **CANONICAL** |
| Meaning B | GL coherence length |
| Source B | Paper 2 §7 (frozen regime), GL theory context |
| Collision Risk | HIGH |

**Resolution Rule**:
- In EDC canon: **ξ = 5D compact coordinate** (always)
- When coherence length is needed: use **ξ_GL** or **λ_GL**
- Book 2 must use ξ for 5D depth only

**Detection**: If ξ appears near "coherence", "GL", "Ginzburg-Landau", flag for review.

---

### COLLISION-002: M_5 (Manifold vs. Planck Mass)

| Aspect | Value |
|--------|-------|
| Symbol | M_5, M5, M^5 |
| Meaning A | 5D bulk manifold |
| Source A | General relativity notation |
| Meaning B | 5D Planck mass scale |
| Source B | KK reduction, dimensional analysis |
| Collision Risk | HIGH |

**Resolution Rule**:
- For manifold: use **\mathcal{M}^5** (calligraphic M)
- For Planck mass: use **M_{5,\mathrm{Pl}}** or **M_{(5)}**
- **NEVER** use M5 or M_5 alone — always disambiguate

**Detection**:
- Topology context (π₁, ×, =) → manifold
- Mass formulas (G ~ 1/M², dimensional) → Planck mass

---

### COLLISION-003: z (3D Spatial vs. 5D Depth — BOOK 2 ONLY)

| Aspect | Value |
|--------|-------|
| Symbol | z |
| Meaning A | 3D spatial coordinate (in x,y,z tuple) |
| Source A | Standard 3D notation |
| Meaning B | 5D compact coordinate (WRONG in canon) |
| Source B | Some Book 2 chapters (legacy from drafts) |
| Collision Risk | HIGH |

**Resolution Rule**:
- For 3D spatial: **z** is OK
- For 5D depth: **MUST use ξ**, never z
- For Z6 complex variables: use **z₁, z₂** (subscripted only)

**Detection**:
- (x, y, z) tuple → 3D spatial, OK
- (x^μ, z) or φ(x, z) → 5D depth, VIOLATION
- Δz as "separation in extra dimension" → VIOLATION
- z₁, z₂ → Z6 variable, OK

---

### COLLISION-004: S¹ (Topology vs. Coordinate)

| Aspect | Value |
|--------|-------|
| Symbol | S¹ |
| Meaning A | Topological circle (abstract) |
| Source A | Topology notation |
| Meaning B | Parameterized by ξ |
| Source B | Framework v2.0 Eq.(1): M^5 = M^4 × S¹_ξ |
| Collision Risk | LOW |

**Resolution Rule**:
- S¹ is topology, ξ is the coordinate that parameterizes it
- Write: "topology S¹ parameterized by ξ"
- **NEVER**: "topology ξ ≃ S¹" (ξ is not a topology)

---

### COLLISION-005: Σ (Brane vs. Summation)

| Aspect | Value |
|--------|-------|
| Symbol | Σ |
| Meaning A | 3D brane Σ³ |
| Source A | Framework v2.0 Eq.(2) |
| Meaning B | Summation symbol |
| Source B | Standard math notation |
| Collision Risk | LOW |

**Resolution Rule**:
- For brane: use **Σ³** or **Σ^3** (with superscript)
- For summation: use **\sum** (not Σ)
- Context usually disambiguates

---

### COLLISION-006: R (Radius vs. Ricci)

| Aspect | Value |
|--------|-------|
| Symbol | R |
| Meaning A | Compactification radius R_ξ |
| Source A | Framework v2.0 Def.1.1 |
| Meaning B | Ricci scalar |
| Source B | General relativity |
| Collision Risk | MEDIUM |

**Resolution Rule**:
- Compactification radius: always **R_ξ** (subscripted)
- Ricci scalar: use **R** alone or **R_{(5)}** for 5D
- Context (geometry vs. scale) disambiguates

---

## Collision Detection Triggers

When scanning Book 2, flag for review if:

| Pattern | Potential Collision | Action |
|---------|---------------------|--------|
| ξ near "coherence", "GL" | COLLISION-001 | Review for ξ_GL |
| M_5, M5 in any context | COLLISION-002 | Classify manifold vs. mass |
| z in 5D context | COLLISION-003 | Must be ξ |
| (x^μ, z) tuple | COLLISION-003 | Likely 5D depth violation |
| Δz as separation | COLLISION-003 | Likely 5D depth violation |
| S¹ = ξ or ξ ≃ S¹ | COLLISION-004 | Wrong: S¹ is topology |
| Σ without superscript | COLLISION-005 | Add ³ for brane |

---

## Collision Count Summary

| ID | Symbol | Risk | Book 2 Occurrences |
|----|--------|------|-------------------|
| COLLISION-001 | ξ | HIGH | ~0 (rare in Book 2) |
| COLLISION-002 | M_5 | HIGH | 22 |
| COLLISION-003 | z | HIGH | 39 |
| COLLISION-004 | S¹ | LOW | ~0 |
| COLLISION-005 | Σ | LOW | ~0 |
| COLLISION-006 | R | MEDIUM | TBD |

---

## Version History

| Date | Change | By |
|------|--------|-----|
| 2026-01-24 | Initial creation with 6 collisions | Claude |
