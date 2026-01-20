# PATCH NOTES: Brane Research Phase

**Date:** 2026-01-20
**Branch:** `restructure/paper3-companion-doi-split`

---

## Summary

This patch establishes the **canonical thick-brane microphysics formalism** across Companions H and N, providing:
1. Formal coupling between bulk-core coordinates and brane-layer modes
2. Energy partition ledger for bulk→brane→3D energy flow
3. Frozen projection operator mapping brane modes to observable particles
4. Effective damped equation for junction relaxation

---

## Deliverables

### D1: Companion H — Thick-Brane Microphysics Foundation (v3.0)

**File:** `09_companion_H_weak_interactions/paper/main.tex`

Added new subsections after §2.7:

| Subsection | Content | Tag |
|------------|---------|-----|
| §2.8 Formal Coupling Term | `L_int = g q(t) φ(y=-δ/2, t)` | [P]/[OPEN] |
| §2.9 Energy Partition Ledger | `ΔE_bulk = ΔE_brane-layer + ΔE_residual` | [Dc] |
| §2.10 Frozen Projection Operator | `P_frozen: φ(+δ/2,t) → {e⁻, e⁺, ν, ...}₃D` | [Def]/[Dc] |
| §2.11 Complete Pipeline | TikZ diagram + summary table | [P]/[Dc] |

**Key equations introduced:**
```latex
\mathcal{L}_{\mathrm{int}} = g \, q(t) \, \phi(y = -\delta/2, t)   % [P]/[OPEN]
\Delta E_{\mathrm{bulk}} = \Delta E_{\mathrm{brane-layer}} + \Delta E_{\mathrm{residual}}   % [Dc]
\mathcal{P}_{\mathrm{frozen}}: \phi(+\delta/2, t) \mapsto \{e^-, e^+, \nu, \ldots\}_{3D}   % [Def]
\hbar\omega \gg E_{\mathrm{env}}   % Frozen criterion [Def]/[Dc]
```

### D2: Companion N — Brane-Layer Dissipation Subsection

**File:** `10_companion_N_neutron_junction/paper/main.tex`

Added §5.4 "Brane-Layer Dissipation (Effective Damping Model)":

**Key equation:**
```latex
M \ddot{q} + \Gamma \dot{q} + \partial_q V(q) = 0   % [P]/[OPEN]
```

**Content:**
- Definition of effective damped equation with physical interpretation
- Explanation of Γ as brane-layer dissipation coefficient
- Energy partition from damping: `ΔE_dissipated = ∫ Γ q̇² dt`
- Connection to WKB treatment (τₙ via tunneling vs. classical damping)
- Explicit statement: Γ is NOT fitted to τₙ yet [OPEN]

### D3: Summary Table

| Object | Where it lives | What carries energy | Tag |
|--------|----------------|---------------------|-----|
| Junction coordinate q(t) | Bulk-core (5D) | Geometric excitation | [Def] |
| Brane-layer field φ(y,t) | Brane (thickness δ) | Membrane modes | [Def] |
| Frozen output | Observer-facing (3D) | Particles (e⁻, ν, etc.) | [Dc]/[P] |
| Damping coefficient Γ | Effective (integrated out) | Bulk→brane coupling | [P]/[OPEN] |

---

## Build Verification

```bash
# Companion H
cd edc_papers/paper_3_series/09_companion_H_weak_interactions/paper/
xelatex -interaction=nonstopmode main.tex && xelatex main.tex
# Output: main.pdf (9–10 pages)

# Companion N
cd edc_papers/paper_3_series/10_companion_N_neutron_junction/paper/
xelatex -interaction=nonstopmode main.tex && xelatex main.tex
# Output: main.pdf (12 pages)
```

**Status:** Both PDFs compile successfully. Minor TikZ decoration warning in H (cosmetic).

---

## Epistemic Classification

| Claim | Tag | Status |
|-------|-----|--------|
| Coupling L_int = g q φ | [P]/[OPEN] | Postulated, derivation open |
| Energy partition ledger | [Dc] | Consequence of conservation |
| Frozen projection P_frozen | [Def]/[Dc] | Defined, justified from Paper 2 |
| Frozen criterion ℏω ≫ E_env | [Def]/[Dc] | Definition with physical motivation |
| Damped equation M q̈ + Γ q̇ + ∂V = 0 | [P]/[OPEN] | Heuristic, derivation open |
| Γ interpretation | [P]/[OPEN] | Physical, not fitted |

---

## Open Problems (Flagged)

1. **Derive coupling constant g from 5D action** [OPEN]
2. **Derive Γ from thick-brane microphysics** [OPEN]
3. **Establish WKB–damping bridge:** Map ν₀ ↔ Γ [OPEN]
4. **Frozen criterion from variational principle** [OPEN]

---

## Files Modified

```
09_companion_H_weak_interactions/paper/main.tex   # +~150 lines (new subsections)
10_companion_N_neutron_junction/paper/main.tex    # +~60 lines (dissipation subsection)
```

---

## Commit Message

```
Brane Research Phase: Add thick-brane microphysics formalism

Companion H (v3.0):
- Add formal coupling term L_int = g q(t) φ(-δ/2, t) [P]/[OPEN]
- Add energy partition ledger [Dc]
- Add frozen projection operator P_frozen [Def]/[Dc]
- Add complete pipeline diagram + summary table

Companion N:
- Add §5.4 brane-layer dissipation with damped equation [P]/[OPEN]
- Explain Γ as effective coupling (NOT fitted to τ_n)
- Connect to WKB treatment [OPEN]

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

---

*Generated: 2026-01-20*
