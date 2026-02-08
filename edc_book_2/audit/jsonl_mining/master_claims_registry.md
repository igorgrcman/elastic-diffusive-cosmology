# Master Claims Registry

**Generated:** 2026-01-31
**Sources:** 22826edd, 73d92ff5, 98cc5184, 5251e090, ce8dadbd sessions

---

## Summary

| Category | Count |
|----------|-------|
| Derived [Der] | 16 |
| Derived Conditional [Dc] | 47 |
| Identified [I] | 23 |
| Calibrated [Cal] | 8 |
| Baseline [BL] | 12 |
| Open [OPEN] | 25+ |
| Mathematical [M] | 10 |

---

## Key Physical Claims

### CLAIM-001: Weinberg Angle
- **claim_id:** CLAIM-WA-001
- **statement:** `sin^2(theta_W) = 1/4 = 0.25` at tree level from Z6 symmetry
- **epistemic_tag:** [Dc] - Derived conditional on Z6 symmetry identification
- **dependencies:** Z6 = Z2 x Z3 symmetry structure, g'^2/g^2 = |Z2|/|Z6| = 2/6 = 1/3
- **source_pointer:** 22826edd:1553-1623, ch10_electroweak_bridge.tex
- **comparison:** Experiment: 0.2314 at M_Z (8% running deviation expected)

### CLAIM-002: Fermi Constant Chain
- **claim_id:** CLAIM-GF-001
- **statement:** `G_F = g_5^2 * ell^2 * I_4 / x_1^2` from 5D to 4D reduction
- **epistemic_tag:** [Dc] - spine established, I_4 blocked by OPR-21
- **dependencies:** g_5 (5D coupling), ell (domain size), I_4 (overlap integral), x_1 (first eigenvalue)
- **source_pointer:** 98cc5184, 22826edd:16959
- **notes:** I_4 calculation requires BVP solution (OPR-21 OPEN)

### CLAIM-003: Neutron Lifetime
- **claim_id:** CLAIM-TAU-001
- **statement:** `tau_n ~ 879 s` from WKB tunneling with V_B ~ 2.6 MeV
- **epistemic_tag:** [Cal] - V_B calibrated to match tau_n
- **dependencies:** V_B (barrier height), M(q) (effective mass), q (collective coordinate)
- **source_pointer:** 22826edd:26109, 98cc5184
- **notes:** V_B derivation from 5D is OPEN, tau_n = 879s is [Cal] not [Der]

### CLAIM-004: Generation Count
- **claim_id:** CLAIM-NGEN-001
- **statement:** `N_bound = 3` generations from BVP spectral counting
- **epistemic_tag:** [OPEN] - requires V(xi) and BC derivation from 5D action
- **dependencies:** V(xi) potential, boundary conditions, mu-window [25,35)
- **source_pointer:** 22826edd:3509, ch14_bvp_closure_pack.tex
- **notes:** Blocked by OPR-21 (potential not derived)

### CLAIM-005: V-A Structure
- **claim_id:** CLAIM-VA-001
- **statement:** `R_LR < 10^{-3}` from exponential suppression R_LR ~ exp(-C*mu)
- **epistemic_tag:** [Dc] - conditional on mu > ln(10^3)/C with C = O(1)
- **dependencies:** mu parameter, C coefficient from potential shape
- **source_pointer:** 22826edd:4122-4401
- **notes:** C determination blocked by BVP closure (OPR-21)

### CLAIM-006: Scale Identification delta = R_xi
- **claim_id:** CLAIM-SCALE-001
- **statement:** `delta = R_xi = hbar*c/M_Z ~ 2.2e-3 fm`
- **epistemic_tag:** [P] - Postulated, cannot upgrade without unique-scale proof
- **dependencies:** M_Z (baseline), membrane microphysics
- **source_pointer:** 22826edd:1968, OPR-04
- **notes:** Blocks OPR-02 Route C upgrade

### CLAIM-007: Proton Mass Formula
- **claim_id:** CLAIM-MP-001
- **statement:** `m_p ~ sigma * L_0^4 / delta^2 * (4/3) ~ 985 MeV` (5% error)
- **epistemic_tag:** [Dc/P] - Numerically works, not fully derived
- **dependencies:** sigma (membrane tension), L_0 (cell size), delta (thickness)
- **source_pointer:** 22826edd:47716-47741
- **notes:** Alternative: m_p ~ sigma*pi^8*delta^2 ~ 923 MeV (1.6% error)

### CLAIM-008: Gravitational Constant
- **claim_id:** CLAIM-G-001
- **statement:** `G = c^4 * R_xi^12 / (128*pi^2 * sigma * r_e^13)` (0.8% match)
- **epistemic_tag:** [I] - Identified by fitting, powers not derived
- **dependencies:** R_xi, sigma, r_e (all BL), c (exact)
- **source_pointer:** ce8dadbd:72, 5251e090
- **notes:** NOT circular (G doesn't appear on RHS), but powers 12,13 are fitted not derived

### CLAIM-009: Hierarchy Explanation
- **claim_id:** CLAIM-HIER-001
- **statement:** `(R_xi/r_e)^12 ~ 10^{-38}` explains gravity weakness
- **epistemic_tag:** [I] - Geometric pattern identified
- **dependencies:** R_xi (electroweak scale), r_e (classical electron radius)
- **source_pointer:** ce8dadbd:72
- **notes:** 12 = 4x3 interpretation speculative [P]

### CLAIM-010: Euler-Laplace Gravity Flow
- **claim_id:** CLAIM-GRAV-001
- **statement:** `v(r) = sqrt(2GM/r)` from Laplace + Euler equations
- **epistemic_tag:** [D conditional] - Derived, conditional on pressure deficit model
- **dependencies:** Plenum incompressibility [P], vortex exclusion [P], p_infinity = rho*c^2 [I]
- **source_pointer:** 5251e090:42
- **notes:** r_core = GM/c^2 = r_s/2 identified by matching

---

## Mixing/Mass Parameter Claims

### CLAIM-011: PMNS theta_23
- **claim_id:** CLAIM-PMNS-001
- **statement:** `sin^2(theta_23) = 0.564` from Z6 geometry
- **epistemic_tag:** [Dc]
- **dependencies:** Z6 discrete rotation structure
- **source_pointer:** 98cc5184

### CLAIM-012: PMNS theta_12
- **claim_id:** CLAIM-PMNS-002
- **statement:** `theta_12 = arctan(1/sqrt(2)) = 35.26 deg`
- **epistemic_tag:** [Dc] (8.6% error from experiment)
- **dependencies:** Geometric constraint
- **source_pointer:** 98cc5184

### CLAIM-013: Reactor Angle epsilon
- **claim_id:** CLAIM-PMNS-003
- **statement:** `epsilon = lambda/sqrt(2) ~ 0.159 rad`
- **epistemic_tag:** [BL->Dc] (uses lambda [BL])
- **dependencies:** Wolfenstein lambda parameter
- **source_pointer:** 98cc5184

### CLAIM-014: CKM Jarlskog
- **claim_id:** CLAIM-CKM-001
- **statement:** `J = 2.9e-5` (PDG: 3.08e-5, 6% error)
- **epistemic_tag:** [Dc]
- **dependencies:** Phase cancellation theorem, sign-flip rule
- **source_pointer:** 98cc5184

### CLAIM-015: Lepton Mass Ratios
- **claim_id:** CLAIM-MASS-001
- **statement:** `m_mu/m_e ~ 207`, `m_tau/m_e ~ 3477` from exponential suppression
- **epistemic_tag:** [I/OPEN] - Pattern identified, BVP calculation needed
- **dependencies:** Mode profiles f_L(xi), localization mechanism
- **source_pointer:** 22826edd:1430

---

## Barrier/Tunneling Claims

### CLAIM-016: Barrier Height
- **claim_id:** CLAIM-VB-001
- **statement:** `V_B ~ 2*Delta_m_np ~ 2.6 MeV` from Z3 barrier structure
- **epistemic_tag:** [Cal] - Fitted to tau_n, derivation OPEN
- **dependencies:** Delta_m_np = 1.293 MeV [BL], Z3 geometry
- **source_pointer:** 22826edd:14182, 27360

### CLAIM-017: Bounce Action
- **claim_id:** CLAIM-SE-001
- **statement:** `S_E/hbar ~ 58-62` from geometric ratio L_0/delta
- **epistemic_tag:** [Dc/I] - Multiple routes give similar values
- **dependencies:** L_0 (nucleon scale), delta (thickness), sigma
- **source_pointer:** 22826edd:47296-47819

### CLAIM-018: Pinning Constant
- **claim_id:** CLAIM-PIN-001
- **statement:** `K ~ 0.8 MeV per bond` from sigma
- **epistemic_tag:** [Dc/I] - Dimensionally correct, factor f~0.3 identified
- **dependencies:** sigma = 8.82 MeV/fm^2, contact area ~ pi*delta^2
- **source_pointer:** 22826edd:47831-47903

### CLAIM-019: Effective Temperature
- **claim_id:** CLAIM-TEFF-001
- **statement:** `T_eff ~ 20-50 keV` for bulk fluctuations
- **epistemic_tag:** [OPEN] - Must derive from 5D, artifact rejection
- **dependencies:** Delta V, barrier shape, fluctuation spectrum
- **source_pointer:** 22826edd:46964

---

## Dimensional/Scale Claims

### CLAIM-020: Membrane Tension
- **claim_id:** CLAIM-SIGMA-001
- **statement:** `sigma = m_e*c^2/(alpha*r_e^2) ~ 8.82 MeV/fm^2`
- **epistemic_tag:** [BL/Dc] - From EM parameters
- **dependencies:** m_e, alpha, r_e (all BL)
- **source_pointer:** 22826edd, ce8dadbd

### CLAIM-021: Domain Size
- **claim_id:** CLAIM-ELL-001
- **statement:** `ell ~ 1 fm` (nucleon-scale domain)
- **epistemic_tag:** [P/Cal] - Not derived from first principles
- **dependencies:** BVP closure requires specific ell for N_bound=3
- **source_pointer:** 22826edd:15944

### CLAIM-022: 4/3 Factor
- **claim_id:** CLAIM-FACTOR-001
- **statement:** `4/3` appears in m_p formula from bulk geometry
- **epistemic_tag:** [I] - Observed pattern, derivation incomplete
- **dependencies:** 5D integration, depth factor interpretation
- **source_pointer:** 22826edd:47716

---

## Status Summary by OPR

| Claim | Depends On | Status |
|-------|------------|--------|
| CLAIM-WA-001 | OPR-01 (Z6) | [Dc] - partial |
| CLAIM-GF-001 | OPR-19, OPR-21 | [Dc] - blocked |
| CLAIM-TAU-001 | V_B derivation | [Cal] |
| CLAIM-NGEN-001 | OPR-21 | [OPEN] |
| CLAIM-VA-001 | OPR-21 | [Dc] - blocked |
| CLAIM-SCALE-001 | OPR-04 | [P] |
| CLAIM-G-001 | Power derivation | [I] |
| CLAIM-GRAV-001 | Vortex mechanism | [D conditional] |

---

## Rejected/Circular Claims

| claim_id | statement | reason |
|----------|-----------|--------|
| CLAIM-REJ-001 | G = ell_P^2 * c^4 / (sigma*r_e^3) | CIRCULAR: ell_P contains G |
| CLAIM-REJ-002 | R_xi "derived" from M_Z | DEFINITION not derivation |
| CLAIM-REJ-003 | hbar "verified" from sigma_eff | TAUTOLOGY |

---

*Registry generated from JSONL mining reports*
