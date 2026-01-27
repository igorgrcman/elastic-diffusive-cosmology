# aside_m5_to_z6_proof — STATUS MAP

**Last updated:** 2026-01-27

This folder contains derivation attempts for the M5 → Z6 → Steiner chain.
Some attempts were successful, one was retracted.

**MAIN TEXT IMPLEMENTATION:** Dual-route proof is now in `sections/`:
- Route A: `sections/04b_proton_anchor.tex` (§proton_routeA_anchor)
- Route B: `sections/04c_routeB_z6_steiner.tex` (§routeB_z6_to_steiner)
- Convergence: §convergence_routes

---

## FILE STATUS

| File | Status | Notes |
|------|--------|-------|
| `M5_TO_Z6_PROOF.md` | **ACTIVE** | Main proof document |
| `AXIOM_EXTRACT.md` | **ACTIVE** | Axiom extraction |
| `COMPATIBLE_SYMMETRIES.md` | **ACTIVE** | Symmetry analysis |
| `PATCH_IMPACT_NOTE.md` | **ACTIVE** | Impact assessment |
| `SHORT_SUMMARY.txt` | **ACTIVE** | Summary |
| `ADDENDUM_V_r_DERIVATION.md` | **ACTIVE** | Error acknowledgment for retracted derivation |
| `DERIVATION_V_r_FROM_BC.md` | **⚠️ RETRACTED** | Moved to `aside_archive/` |

---

## CLAIM STATUS

| Claim | Status | Source |
|-------|--------|--------|
| BC → attraction | **FALSE** | See `aside_p2_closure_v3/`, `aside_frozen_brane_bc_v1/` |
| BC → minimum | **FALSE** | Linearized V'_lin(d) > 0 for all BC |
| Core/topology → repulsion | **[Der]** | `aside_p2_closure_v3/02_CORE_REPULSION_FROM_FUNCTIONAL.md` |
| Minimum existence | **[Dc]** | Conditional on V_core + log growth balance |
| Z6 from [P]+[M] | **[Dc]** | Current chain (P2 flux tubes + Kepler-Hales) |

---

## CURRENT DERIVATION CHAIN (CORRECT)

### ROUTE A: Topology + Nambu-Goto + Steiner (§proton_routeA_anchor)
```
[M]+[P] Lemma 1 (lem:topo_protection): π₁ obstruction → topological protection
    ↓
[Der] Lemma 2 (lem:nambu_goto): Nambu-Goto → E = τL (frozen static limit)
    ↓
[M] Theorem (thm:steiner): Steiner optimality (120° angles minimize length)
    ↓
[Dc] Corollary (cor:proton_minimum): Proton Y-junction is local minimum
```
**Main text:** `sections/04b_proton_anchor.tex`

### ROUTE B: P2 + Crystallization + Steiner (§routeB_z6_to_steiner)
```
[P] Postulate P2 (post:P2_flux_tubes): Flux tubes have repulsion + confinement
  ↓
[M] Lemma B1 (lem:B1_kepler_hales): Kepler-Hales optimal 2D packing
  ↓
[Dc] Lemma B2 (lem:B2_hex_crystallization): Hexagonal crystallization
  ↓
[Dc] Lemma B3 (lem:B3_equal_tensions): Z6 symmetry → equal tensions
  ↓
[M] Theorem B (thm:B_steiner_equal_tension): Equal tensions → Steiner 120°
  ↓
[Dc] Corollary B (cor:B_proton_steiner): Proton 120° via Route B
```
**Main text:** `sections/04c_routeB_z6_steiner.tex`

### CONVERGENCE (§convergence_routes)
Both routes share Steiner theorem [M] as terminal step.
Physics enters differently: Route A (topology), Route B (crystallization).
The 120° result is overdetermined.

### BC CLARIFICATION (rem:routeB_BC_disclaimer)
```
[Der] BC (Neumann/Robin/Dirichlet) provide δ scale and mode spectrum
[Der] V'_lin(d) > 0 for ALL BC choices (no attraction from BC!)
[Der] Minimum from V_core + V_lin balance (topology, not BC)
```
**Audit source:** `aside_frozen_brane_bc_v1/`

---

## RETRACTED DERIVATION (DO NOT USE)

The file `DERIVATION_V_r_FROM_BC.md` claimed:
> "BC FORCE the inter-defect potential V(d) to have a minimum"

This was **proven false** in:
- `aside_p2_closure_v3/01_SIGN_AND_MONOTONICITY.md` — V'_lin(d) > 0 always
- `aside_frozen_brane_bc_v1/05_SIGN_AND_MINIMUM_ANALYSIS.md` — all BC scenarios monotonic
- `aside_frozen_brane_bc_v1/07_VERDICT.txt` — "BC create attraction is FALSE"

The retracted file is preserved for forensic traceability in:
`aside_archive/DERIVATION_V_r_FROM_BC__RETRACTED.md`

---

## WHAT'S OPEN

1. Derive V_core from 5D action (currently phenomenological)
2. Derive P2 from more fundamental postulates (currently [P])
3. Complete M5 topology → Z6 without P2 (speculative)
