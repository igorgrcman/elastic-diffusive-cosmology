# aside_neutron_dual_route — STATUS MAP

**Last updated:** 2026-01-27

**5D Forensic Audit Statement:**
> All current neutron numbers ($\tau_n$, $V_B$, $q_n$) use the **effective 1D WKB/bridge model**;
> the full 5D derivation (derive $S_{\mathrm{eff}}[q]$, $M(q)$, $V(q)$, $V_B$ from 5D action)
> is **not yet implemented**.

---

## MAIN TEXT IMPLEMENTATION

Dual-route proof for neutron is in `sections/05b_neutron_dual_route.tex`:
- Route A: `\label{subsec:neutron_routeA_structural}` (5D structural/metastability)
- Route B: `\label{subsec:neutron_routeB_wkb}` (effective 1D WKB lifetime)
- Convergence: `\label{subsec:neutron_convergence}`

---

## ROUTE A: 5D Structural / Metastability

```
[Dc] A0: Proton is local minimum at q=0 (from proton dual-route)
    ↓
[M]+[P] A1 (lem:A1_topo_sector): Topological sector preserved during τ_obs
    ↓
[Der]+[P] A2 (lem:A2_energy_functional): E[q] = E_0 + V(q) structure
    ↓
[Dc]+[P] A3 (prop:A3_metastable): Neutron is metastable at q_n > 0
```

**What Route A establishes:**
- Neutron is in same topological sector as proton
- Neutron has higher energy than proton (E(q_n) > E(0))
- Decay is relaxation within sector, not topology change

**What Route A does NOT derive:**
- Specific V(q) shape [P]
- Barrier height V_B [P]/[Cal]
- BC do not create attraction [Der] (from aside_frozen_brane_bc_v1)

---

## ROUTE B: Effective 1D WKB / Bridge

```
[P]+[Dc] B1 (lem:B1_effective_action): S_eff[q] = ∫dt(½M(q)q̇² - V(q))
    ↓
[M] B2 (lem:B2_wkb): Standard WKB tunneling formula
    ↓
[Cal] B3 (prop:B3_calibration): V_B ≈ 2.6 MeV reproduces τ_n ≈ 879 s
```

**What Route B establishes:**
- Effective 1D model reproduces observed lifetime
- WKB tunneling mechanism is consistent

**What Route B does NOT derive (OPEN):**
- V(q) from 5D action
- M(q) from 5D geometry
- V_B from first principles (currently [Cal])
- Γ_0 from mode spectrum

---

## CLAIM STATUS

| Claim | Status | Source |
|-------|--------|--------|
| Neutron in Y-junction sector | [M]+[P] | Lemma A1 |
| E(q_n) > E(0) | [Dc] | Route A chain |
| Metastable local minimum | [Dc]+[P] | Prop A3 |
| τ_n ≈ 879 s reproduced | [Cal] | Prop B3 |
| BC do not generate attraction | [Der] | aside_frozen_brane_bc_v1 audit |

---

## OPEN DERIVATIONS (5D → Effective)

| Target | Current | Goal | Priority |
|--------|---------|------|----------|
| V(q) | [P] assumed shape | [Der] from S_5D | HIGH |
| M(q) | [P] assumed | [Der] from 5D kinetic | HIGH |
| V_B | [Cal] ≈ 2.6 MeV | [Der] from V(q) | HIGH |
| Γ_0 | [Cal] ~10^15 s^-1 | [Der] from modes | MEDIUM |
| q_n | [I] identified | [Der] from V'(q)=0 | MEDIUM |

---

## GUARDRAILS

**Do NOT claim:**
- BC create attraction (FALSE per aside_frozen_brane_bc_v1)
- SM weak interaction derivation (not used)
- Full 5D derivation complete (OPEN)

**Allowed language:**
- BC provide scale δ and mode spectrum
- Barrier mechanism is topological/geometric
- Current numbers are [Cal] from effective 1D model

---

## RELATED FILES

- `sections/05_case_neutron.tex` — Main neutron case study
- `sections/05_neutron_story.tex` — Narrative neutron section
- `sections/04b_proton_anchor.tex` — Proton anchor (dependency)
- `sections/04c_routeB_z6_steiner.tex` — Proton Route B (pattern)
- `aside_frozen_brane_bc_v1/` — BC audit (no attraction)

---

## CONVERGENCE SUMMARY

| Aspect | Route A | Route B |
|--------|---------|---------|
| Framework | 5D structural | Effective 1D |
| Output | Metastability [Dc]+[P] | τ_n [Cal] |
| Quantitative | No | Yes |
| 5D-derived | Partial | OPEN |
| Uses SM | No | No |

Both routes agree: **Neutron is metastable excitation above proton anchor.**
