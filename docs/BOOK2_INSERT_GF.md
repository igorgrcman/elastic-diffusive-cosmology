# Book 2 Insert: G_F Constraint

**Created:** 2026-01-29
**LaTeX source:** `edc_papers/_shared/boxes/gf_constraint_box.tex`
**Insertion point:** `edc_book_2/src/sections/11_gf_derivation.tex` (after Stoplight Verdict)

---

## Canon Summary (3 sentences)

1. **G_F is a constraint, not a derivation.** First-principles calculation (RED-C) requires g₅, m_φ, and BVP solution—none of which are complete.

2. **Naive 5D overlap is too large.** In localized-fermion setups, g₅² I₄ ~ O(1) because ∫|f|⁴ ~ 1/width is naturally large. Matching tiny G_F ~ 10⁻⁵ GeV⁻² requires either EW-scale mediator OR strong chiral suppression.

3. **BVP overlap is a decisive falsification channel.** If neither mechanism delivers the required suppression (>10× mismatch), the mode-overlap picture fails.

---

## Stoplight Status

| Level | Status | Description |
|-------|--------|-------------|
| **GREEN-A** | Achieved | EW consistency closure (sin²θ_W → g² → M_W → G_F), with v circularity caveat |
| **YELLOW-B** | Achieved | Mechanism identified (mode overlap explains "weakness"), qualitative only |
| **RED-C** | **OPEN** | First-principles derivation (g₅, m_φ, f_L from BVP) |

---

## Constraint Window

```
g_eff² / M_eff² ∈ [0.9, 1.1] × G_F     (±10% tolerance)

Dimensionless target: X := G_F m_e² = 3.04 × 10⁻¹²  (natural units)
```

---

## Upgrade Roadmap (RED-C → [Der])

```
BVP Solution (OPR-04/OPR-21)
       ↓
Mode Profiles f_L(χ)
       ↓
Overlap I₄ + Mediator m_φ (OPR-20)
       ↓
5D Coupling g₅ (OPR-19)
       ↓
G_F First-Principles (OPR-22)
```

---

## Cross-References

| Topic | Source |
|-------|--------|
| Full constraint analysis | `docs/GF_CONSTRAINT_NOTE.md` |
| Overlap suppression (Lemma Case B) | `edc_papers/_shared/lemmas/projection_reduction_lemma.tex` |
| Chapter 11 (G_F derivation) | `edc_book_2/src/sections/11_gf_derivation.tex` |
| BVP workpackage | `edc_book_2/src/sections/ch12_bvp_workpackage.tex` |

---

*This insert provides book-ready canon text for the G_F constraint falsification channel.*
