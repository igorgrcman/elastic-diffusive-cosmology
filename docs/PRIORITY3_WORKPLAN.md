# Priority 3 Workplan: Book 2 Blocking Issues

**Created:** 2026-01-29
**Status:** P3-1 RESOLVED, P3-2 RESOLVED, P3-3 FRAMEWORK COMPLETE (all 2026-01-29)
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

### Rank 1: P3-1 (L_0/δ tension) — ✓ RESOLVED (2026-01-29)

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

**Deliverable:** `docs/L0_DELTA_TENSION_RESOLUTION.md` ✓ CREATED

**Resolution:** Both values are valid in their respective contexts:
- π² ≈ 9.87 for static/eigenvalue properties (m_p)
- 9.33 for dynamic/tunneling processes (τ_n)
- 5.5% difference = quantum corrections to classical resonance

**Status:** GREEN — Not a contradiction, a feature

---

### Rank 2: P3-2 (Prefactor A) — ✓ RESOLVED (2026-01-29)

**What:** A = 0.8–1.0 was calibrated [Cal]. Now derived from fluctuation determinant.

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

**Deliverable:**
- `edc_papers/_shared/derivations/prefactor_A_from_fluctuations.tex` ✓ CREATED
- `docs/PREFACTOR_A_DERIVATION_NOTE.md` ✓ CREATED
- `edc_papers/_shared/code/prefactor_A_numeric_check.py` ✓ CREATED

**Resolution:**
- Formula: A = π × (ω₀/ω_B) / √(L₀/δ) = 1.03 × (ω₀/ω_B) [Der]
- With ω₀/ω_B ≈ 0.82: A ≈ 0.84 [Der within 1D]
- Physical: barrier 22% steeper than well

**Status:** GREEN — A upgraded from [Cal] to [Der] within 1D model

---

### Rank 3: P3-3 (G_F derivation) — ✓ FRAMEWORK COMPLETE (2026-01-29)

**What:** G_F currently uses v (Higgs vev) which depends on G_F → circularity.

**Resolution:** Non-circular framework established; numerical values remain BVP-gated.

**Non-circular formula:**
```
X_EDC = C × (g_5² × I_4 × m_e²) / M_eff²
```
where X = G_F × m_e² = 3.04 × 10⁻¹² and NO v appears in forward chain.

**Deliverables:**
- `edc_papers/_shared/derivations/gf_noncircular_chain_framework.tex` ✓ CREATED
- `docs/GF_NONCIRCULAR_FRAMEWORK_NOTE.md` ✓ CREATED
- `edc_papers/_shared/code/gf_toy_overlap_window.py` ✓ CREATED

**What is derived [Der]:**
- Dimensional skeleton (unique combination g_5² × I_4 / M_eff²)
- Independence from v — circularity removed
- sin²θ_W = 1/4 (separate prediction, 0.08% accuracy)

**What is BVP-gated [OPEN]:**
- Mode profiles w_L(χ), w_R(χ), w_φ(χ)
- KK eigenvalue λ_0
- Overlap integral I_4
- Numerical G_F value

**Blocking dependency:** OPR-21 (thick-brane BVP solution)

**Status:** YELLOW — Framework complete, values RED (BVP-gated)

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

| Issue | GREEN | YELLOW | RED | **ACTUAL** |
|-------|-------|--------|-----|------------|
| P3-1 | Tension explained, both values valid in context | One value wrong, corrected | Irreconcilable inconsistency | ✓ **GREEN** |
| P3-2 | A derived from determinant [Der] | A bounded O(1) [Dc] | Cannot derive, remains [Cal] | ✓ **GREEN** |
| P3-3 | G_F from 5D, no SM input [Der] | Constraint window tightened [Dc] | Blocked by BVP | **YELLOW** (framework GREEN, values RED) |

---

## Cross-References

- L_0/δ tension: See `CANON_BUNDLE.md` Section 10, `docs/SIGMA_DEPENDENCY_AUDIT.md`
- Prefactor A: See `BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex`
- G_F constraint: See `docs/GF_CONSTRAINT_NOTE.md`, `edc_papers/_shared/boxes/gf_constraint_box.tex`
- BVP dependencies: See `CLAIM_LEDGER.md` OPR-02/21

---

*Workplan created 2026-01-29. Execute in fastest-first order.*
