# PATCH NOTES: Brane Research Phase

**Date:** 2026-01-20 (updated)
**Branch:** `main`

---

## Summary

This patch establishes the **canonical thick-brane microphysics formalism** in Companion N, providing:
1. Formal coupling between bulk-core coordinates and brane-layer modes
2. Energy partition ledger for bulk→brane→3D energy flow
3. Frozen projection operator mapping brane modes to observable particles
4. Effective damped equation for junction relaxation
5. **Two-regime (Pump→Store→Emit) process model** (added 2026-01-20)
6. **Complete thick-brane definitions copied from H** to make N self-contained

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
10_companion_N_neutron_junction/paper/main.tex   # +250 lines (expanded thick-brane + two-regime model)
```

---

## Session 2 Additions (2026-01-20)

### Thick-Brane Content from H (copied to N for self-containment)

| Section | Content | Tag |
|---------|---------|-----|
| §2.1 | Thin vs Thick Brane definition | [Def] |
| §2.2 | Core definitions (Bulk-Core, Brane-Layer, 3D Outputs) | [P]/[Def] |
| §2.3 | Thick-brane geometry diagram (Fig. 2) | [P] |
| §2.4 | Canonical Energy-Exchange statement (verbatim from Framework v2.0) | [BL] |

### Two-Regime Process Model (new §5.5)

| Component | Content | Tag |
|-----------|---------|-----|
| Pumping regime | Bulk→brane energy transfer via L_int | [P] |
| Emission regime | Brane→3D via frozen projection | [Dc]/[P] |
| Switch criterion | Regime boundary Ξ ≪ 1 (not threshold) | [Def]/[P] |
| One-line summary | "Brane absorbs from junction, emits as particles" | [P] |

**Note:** Switch criterion refined in Session 3 from threshold to regime-boundary formulation.

### Build Verification

```bash
cd edc_papers/paper_3_series/10_companion_N_neutron_junction/paper/
xelatex -interaction=nonstopmode main.tex && xelatex main.tex && xelatex main.tex
# Output: main.pdf (17 pages, 220 KB)
```

---

## Session 3 Additions (2026-01-20)

### Refined Two-Regime Model (§5.5 rewrite)

| Component | Content | Tag |
|-----------|---------|-----|
| Regime parameter Ξ(t) | Ratio Π_pump/Π_release | [Def]/[P] |
| Trigger condition | q(t*) ≈ 0 ∧ Ξ(t*) ≪ 1 | [Def]/[P] |
| Charging integral | E_brane(t) = ∫Π_pump dt | [Def]/[OPEN] |
| Two-step release map | ΔE_brane → {brane modes} → P_frozen → {3D} | [Dc]/[P] |
| E_other decomposition | E_recoil + E_soft + E_bulk_residual | [Dc]/[P] |
| Physical Narration Rule | 5D cause → brane response → 3D output | [Def] |

### Epistemic Guardrail Updates

| Statement | Tag |
|-----------|-----|
| τ_n = [BL] (empirical benchmark, not fit target) | [BL] |
| "τ_n is not a control knob" | [Def] |
| Mechanism explanation ≠ parameter calibration | Guardrail |

### Key Equations Added

```latex
% Regime parameter
\Xi(t) \equiv \frac{\Pi_{\mathrm{pump}}(t)}{\Pi_{\mathrm{release}}(t)}

% Trigger condition
\mathcal{T}_{n\to p}: q(t_*) \approx 0 \land \Xi(t_*) \ll 1

% Charging integral
\mathcal{E}_{\mathrm{brane}}(t) \equiv \int_{t_i}^{t} \Pi_{\mathrm{pump}}(t')\,dt'

% Two-step release map
\Delta E_{\mathrm{brane}} \to \{\phi_k\} \xrightarrow{\mathcal{P}_{\mathrm{frozen}}} \{e^-, \bar{\nu}_e, \ldots\}_{3D}

% E_other decomposition
E_{\mathrm{other}} = E_{\mathrm{recoil}} + E_{\mathrm{soft}} + E_{\mathrm{bulk\,residual}}
```

### Build Verification (Session 3)

```bash
cd edc_papers/paper_3_series/10_companion_N_neutron_junction/paper/
xelatex -interaction=nonstopmode main.tex && xelatex main.tex
# Output: main.pdf (19 pages)
```

---

*Generated: 2026-01-20 (Session 3)*
