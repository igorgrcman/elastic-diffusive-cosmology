# Nuclear Topology Parameter Ledger (Internal)

**Status:** Internal research note support; NOT part of Paper 3 build
**Version:** 1.0
**Date:** 2026-01-15
**Companion to:** `NUCLEAR_TOPOLOGY_NOTE.md`

---

> **UPOZORENJE:** Ovaj ledger definira parametre za istraživački model.
> Nijedan parametar nije kalibriran niti deriviran. Svi su [P] ili [OPEN].

---

## Parameter Table

| ID | Symbol | Meaning / Physical interpretation | Appears in term | Units / scaling | Status | Default placeholder | Derivation / Calibration path |
|----|--------|-----------------------------------|-----------------|-----------------|--------|---------------------|-------------------------------|
| **A. Edge / Link Structure** |||||||
| NT-P01 | $T_{pp}$ | Tension on proton-proton edge | $E_{\text{tension}}$ | Energy/Length | [P] | $T_0$ (reference) | Derive from string action; calibrate to p-p scattering? [OPEN] |
| NT-P02 | $T_{pn}$ | Tension on proton-neutron edge | $E_{\text{tension}}$ | Energy/Length | [P] | $\approx T_0$ | Assume $\approx T_{pp}$ initially; refine from deuteron binding [OPEN] |
| NT-P03 | $T_{nn}$ | Tension on neutron-neutron edge | $E_{\text{tension}}$ | Energy/Length | [P] | $\approx T_0$ | Assume $\approx T_{pp}$; dineutron unstable suggests different? [OPEN] |
| NT-P04 | $L_0$ | Preferred/rest edge length | $E_{\text{tension}}$ (if Hookean) | Length | [P] | $\sim 1$ fm | From nuclear radius scaling $r_0 A^{1/3}$; $r_0 \approx 1.2$ fm [BL] |
| **B. Junction / Angle Frustration** |||||||
| NT-P05 | $J_p$ | Junction penalty at p-vertex | $E_{\text{junction}}$ | Energy | [P] | $J_0$ (reference) | Derive from 5D action expansion around Y-junction [OPEN] |
| NT-P06 | $J_n$ | Junction penalty at n-vertex | $E_{\text{junction}}$ | Energy | [P] | $\approx J_0$ | Assume $\approx J_p$ initially; n may have different geometry [OPEN] |
| NT-P07 | $\theta_0^{(3)}$ | Preferred angle for degree-3 vertex | $F(\{\theta_k\})$ | Degrees | [Dc] | **120°** | Steiner theorem for equal tensions in 2D [M] |
| NT-P08 | $\theta_0^{(4)}$ | Preferred angle for degree-4 vertex | $F(\{\theta_k\})$ | Degrees | [P] | 109.5° (tetrahedral) or 90° (square) | Geometry-dependent; not derived [OPEN] |
| NT-P09 | $\alpha_{\text{ang}}$ | Exponent in angle penalty $(\theta - \theta_0)^\alpha$ | $F(\{\theta_k\})$ | Dimensionless | [P] | 2 (quadratic) | Ansatz; could be 1 (linear) or 4 (quartic) [OPEN] |
| **C. Curvature / Bending** |||||||
| NT-P10 | $\kappa_{\text{bend}}$ | Bending modulus / rigidity | $E_{\text{bend}}$ | Energy | [P] | — | Derive from membrane elastic constants [OPEN] |
| NT-P11 | $\ell_{\text{bend}}$ | Smoothing / discretization scale | $E_{\text{bend}}^{\text{disc}}$ | Length | [P] | $\sim L_0$ | Set by mesh resolution; not physical [I] |
| NT-P12 | $\bar{\xi}$ | Reference bulk depth | $E_{\text{bend}}^{\text{disc}}$ | Length | [P] | 0 (membrane at $\xi=0$) | Convention choice [Def] |
| **D. Bulk / Pressure Coupling** |||||||
| NT-P13 | $P_{\text{bulk}}$ | Effective Plenum pressure | $E_{\text{bulk}}$ | Energy/Volume | [P] | $> 0$ | From EDC KB-POST-005; numerical value [OPEN] |
| NT-P14 | $\gamma_{\text{bulk}}$ | Coupling strength to $V_{\text{eff}}$ | $E_{\text{bulk}}$ | Dimensionless | [P] | 1 | Absorbed into $P_{\text{bulk}}$ definition [Def] |
| NT-P15 | $V_{\text{eff}}$ form | Functional form of effective volume | $E_{\text{bulk}}$ | Volume | [P] | Convex hull? Delaunay? | Multiple definitions possible [OPEN] |
| **E. Constraints / Regularizers** |||||||
| NT-P16 | $\lambda_{\text{overlap}}$ | Penalty for edge crossing | Constraint term | Energy | [P] | Large ($\gg T_0 L_0$) | Hard constraint proxy; set to enforce planarity [I] |
| NT-P17 | $\varepsilon_{\text{core}}$ | Short-distance cutoff / core size | Regularizer | Length | [P] | $\sim 0.5$ fm | Prevents node collapse; from nucleon size [BL] |
| NT-P18 | $\lambda_{\text{Coulomb}}$ | Coulomb repulsion strength (if included) | $E_{\text{Coulomb}}$ | Energy·Length | [BL] | $e^2/(4\pi\varepsilon_0) \approx 1.44$ MeV·fm | Known constant [BL] |
| **F. Graph Structure (not continuous)** |||||||
| NT-P19 | $d_{\max}$ | Maximum allowed vertex degree | Graph constraint | Integer | [P] | 3 or 4 | Y-junction suggests 3; tetrahedra allow 4 [OPEN] |
| NT-P20 | Allowed edge types | Which (p,p), (p,n), (n,n) edges exist | Graph structure | Discrete | [P] | All allowed | Could restrict e.g. no (n,n) edges [OPEN] |

---

## Parameter Count Summary

| Status | Count | Parameters |
|--------|-------|------------|
| **[P]** | 14 | NT-P01–06, NT-P09–11, NT-P13–16, NT-P19–20 |
| **[Dc]** | 1 | NT-P07 ($\theta_0^{(3)} = 120°$) |
| **[BL]** | 2 | NT-P17 ($\varepsilon_{\text{core}}$), NT-P18 ($\lambda_{\text{Coulomb}}$) |
| **[Def]** | 2 | NT-P12 ($\bar{\xi}$), NT-P14 ($\gamma_{\text{bulk}}$) |
| **[I]** | 1 | NT-P11 ($\ell_{\text{bend}}$) |
| **[OPEN]** | — | All [P] parameters need derivation; noted in "path" column |

**Total: 20 parameters defined**

---

## Epistemic Discipline Footer

> **NAPOMENA O EPISTEMIČKOM STATUSU:**
>
> Parametri u ovom ledgeru **ne nadograđuju nijednu tvrdnju** iz Paper 3.
> Oni su scaffolding za buduće testove modela nuklearne topologije.
>
> - Svaka vrijednost bez derivacije je **[P]** (postulat) ili **[Cal]** (kalibracija).
> - Trenutno: **0 parametara je [Cal]** jer nema numeričkih eksperimenata.
> - Cilj: Reducirati [P] → [Dc] ili [D] kroz eksplicitne derivacije iz 5D akcije.

---

## Reduction Priority

Parametri s najvećim utjecajem na model, prioritet za derivaciju:

| Priority | Parameter | Why |
|----------|-----------|-----|
| 1 | $T_{pp}, T_{pn}, T_{nn}$ | Određuju osnovnu energetsku skalu |
| 2 | $J_p, J_n$ | Kontroliraju junction frustraciju |
| 3 | $P_{\text{bulk}}$ | Određuje volume-favoring dinamiku |
| 4 | $\theta_0^{(4)}$ | Kritično za 3D strukture |
| 5 | $V_{\text{eff}}$ forma | Utječe na koja (Z,N) su stabilna |

---

## Cross-Reference

| Ledger ID | NUCLEAR_TOPOLOGY_NOTE Section |
|-----------|------------------------------|
| NT-P01–04 | §3.2 (Tension term) |
| NT-P05–09 | §3.3 (Junction term) |
| NT-P10–12 | §3.5 (Bending term) |
| NT-P13–15 | §3.4 (Bulk term) |
| NT-P16–18 | Implicit in §2.2, §4.2 |
| NT-P19–20 | §2.1 (Graph definitions) |

---

*Kraj ledgera.*

**Changelog:**
- 2026-01-15: Inicijalna verzija (v1.0)
