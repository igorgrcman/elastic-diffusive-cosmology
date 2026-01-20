# PATCH NOTES: Brane Research Phase

**Date:** 2026-01-20
**Branch:** `main`

---

## Summary

This patch establishes the **canonical thick-brane microphysics formalism** in Companion N, providing:
1. Formal coupling between bulk-core coordinates and brane-layer modes
2. Energy partition ledger for bulk→brane→3D energy flow
3. Frozen projection operator mapping brane modes to observable particles
4. Effective damped equation for junction relaxation

**Note:** Companion H is published and NOT modified.

---

## Companion N — Thick-Brane Microphysics (Complete)

**File:** `10_companion_N_neutron_junction/paper/main.tex`

### §5: Pumping and Dissipation Pathway

Already contains:
- Coupling term `L_int = g q(t) φ(-δ/2, t)` [P]/[OPEN] (Postulate 2)
- Energy pathway diagram

**Added:**
- Energy partition ledger [Dc]:
  ```
  ΔE_bulk = ΔE_brane-layer + ΔE_residual
  ```
- Brane-layer dissipation subsection with damped equation [P]/[OPEN]:
  ```
  M q̈ + Γ q̇ + ∂_q V(q) = 0
  ```

### §6: Frozen Projection Boundary

**Added new subsection §6.3:** Formal Frozen Projection Operator

| Definition | Content | Tag |
|------------|---------|-----|
| Brane-layer field | φ(y,t) with y ∈ [-δ/2, +δ/2] | [Def] |
| Frozen projection | P_frozen: φ(+δ/2,t) → {e⁻, ν̄, ...}₃D | [Def]/[Dc] |
| Frozen criterion | ℏω ≫ E_env | [Def]/[Dc] |

**Key equations:**
```latex
\mathcal{P}_{\mathrm{frozen}}: \phi(+\delta/2, t) \mapsto \{e^-, \bar{\nu}_e, \ldots\}_{3D}
\hbar\omega \gg E_{\mathrm{env}}   % Frozen criterion
```

---

## Build Verification

```bash
cd edc_papers/paper_3_series/10_companion_N_neutron_junction/paper/
xelatex -interaction=nonstopmode main.tex && xelatex main.tex
# Output: main.pdf (13 pages)
```

---

## Epistemic Classification

| Claim | Tag | Status |
|-------|-----|--------|
| Coupling L_int = g q φ | [P]/[OPEN] | Postulated, derivation open |
| Energy partition ledger | [Dc] | Consequence of conservation |
| Damped equation M q̈ + Γ q̇ + ∂V = 0 | [P]/[OPEN] | Heuristic, derivation open |
| Frozen projection P_frozen | [Def]/[Dc] | Defined, justified from Paper 2 |
| Frozen criterion ℏω ≫ E_env | [Def]/[Dc] | Definition with physical motivation |

---

## Open Problems (Flagged)

1. **Derive coupling constant g from 5D action** [OPEN]
2. **Derive Γ from thick-brane microphysics** [OPEN]
3. **Establish WKB–damping bridge:** Map ν₀ ↔ Γ [OPEN]

---

## Files Modified

```
10_companion_N_neutron_junction/paper/main.tex   # +66 lines
```

---

*Generated: 2026-01-20*
