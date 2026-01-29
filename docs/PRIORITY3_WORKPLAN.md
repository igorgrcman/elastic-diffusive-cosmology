# Priority 3 Workplan: Book 2 Blocking Issues

**Created:** 2026-01-29
**Status:** Planning phase
**Purpose:** Ordered attack plan for the three P3 blockers

---

## The Three Blockers

| # | Issue | Current Status | Blocks |
|---|-------|----------------|--------|
| P3-1 | L_0/δ tension | Static: π², Dynamic: 9.33 | τ_n narrative coherence |
| P3-2 | Prefactor A | [Cal] = 0.8–1.0 | τ_n precision claim |
| P3-3 | G_F derivation | Circular (uses v) | Weak sector closure |

---

## Dependency Analysis

```
P3-1 (L_0/δ)
    ↓ influences
P3-2 (Prefactor A)  ← may depend on L_0/δ resolution
    ↓ influences
τ_n precision

P3-3 (G_F)
    ↓ independent track
    requires BVP solution (OPR-02/21)
```

**Key insight:** P3-1 and P3-2 are coupled; P3-3 is mostly independent but harder.

---

## Fastest-First Ordering

### Rank 1: P3-1 (L_0/δ tension) — FASTEST

**What:** Static equilibrium gives L_0/δ = π² ≈ 9.87; dynamic (τ_n fit) prefers ~9.33.

**Why fastest:**
- Pure analysis task (no new BVP needed)
- Data already exists in derivations
- Resolution may be: different physical contexts use different values

**Attack plan:**
1. Audit all L_0/δ appearances in canon (grep + read)
2. Identify which derivations use which value
3. Check if 9.33 vs 9.87 difference matters at current precision (<1%?)
4. Document resolution: either (a) they're both valid in different limits, or (b) one is wrong

**Deliverable:** `docs/L0_DELTA_TENSION_RESOLUTION.md`

**Estimated effort:** 1–2 sessions

---

### Rank 2: P3-2 (Prefactor A) — MEDIUM

**What:** A = 0.8–1.0 is calibrated [Cal], not derived. Should come from fluctuation determinant.

**Why medium:**
- Requires understanding Kramers escape rate theory
- Fluctuation determinant is standard but non-trivial
- May require numerical verification

**Dependencies:** May need L_0/δ resolution first (P3-1).

**Attack plan:**
1. Review Kramers theory in existing derivations
2. Identify what functional form A should have
3. Compute A from first principles (or show it's O(1) generically)
4. Compare with calibrated range

**Deliverable:** `docs/PREFACTOR_A_DERIVATION.md`

**Estimated effort:** 2–3 sessions

---

### Rank 3: P3-3 (G_F derivation) — HARDEST

**What:** G_F currently uses v (Higgs vev) which depends on G_F → circularity.

**Why hardest:**
- Requires full BVP solution (OPR-02/21 dependency)
- Needs (g_5, m_φ) from 5D first principles
- Most open-ended of the three

**Dependencies:**
- OPR-02/21 (thick-brane BVP)
- May need δ = R_ξ identification (OPR-20b)

**Attack plan:**
1. Clarify exactly what "no circularity" means (constraint window already exists)
2. Identify minimal path: what single quantity would close the loop?
3. If BVP is required, scope the BVP work
4. Alternative: tighten constraint window bounds without full derivation

**Deliverable:** `docs/GF_NONCIRCULAR_CLOSURE_PLAN.md`

**Estimated effort:** 3+ sessions (may remain [OPEN])

---

## Recommended Execution Order

```
Week 1: P3-1 (L_0/δ)
        ↓
Week 2: P3-2 (Prefactor A)
        ↓
Week 3+: P3-3 (G_F) — ongoing, may not fully close
```

---

## Success Criteria

| Issue | GREEN | YELLOW | RED |
|-------|-------|--------|-----|
| P3-1 | Tension explained, both values valid in context | One value wrong, corrected | Irreconcilable inconsistency |
| P3-2 | A derived from determinant [Der] | A bounded O(1) [Dc] | Cannot derive, remains [Cal] |
| P3-3 | G_F from 5D, no SM input [Der] | Constraint window tightened [Dc] | Blocked by BVP |

---

## Cross-References

- L_0/δ tension: See `CANON_BUNDLE.md` Section 10, `docs/SIGMA_DEPENDENCY_AUDIT.md`
- Prefactor A: See `BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex`
- G_F constraint: See `docs/GF_CONSTRAINT_NOTE.md`, `edc_papers/_shared/boxes/gf_constraint_box.tex`
- BVP dependencies: See `CLAIM_LEDGER.md` OPR-02/21

---

*Workplan created 2026-01-29. Execute in fastest-first order.*
