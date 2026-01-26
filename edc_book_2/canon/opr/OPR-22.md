# OPR-22: First-Principles G_eff from 5D Mediator Exchange

**Status**: CONDITIONAL [Dc] — structure derived, parameters [P]
**Created**: 2026-01-25
**Branch**: book2-opr22-geff-derivation-v1

### Status Addendum (2026-01-26, OPEN-22-4b.1a)

**Canonical slice convergence**: ✓ PASS
- Slice: (κ=0, ρ=0.20) under V_L = M² − M'
- Convergence: < 1% drift for x₁, |f₁(0)|², G_eff (N_grid: 2000→4000)
- All canonical G_eff tables use this slice only

**Robin κ>0 family**: OPEN-22-4b-R (exploratory)
- NOT part of canonical G_eff tables
- Current solver yields trivial brane amplitude
- Pending: toy analytic verification + physical interpretation

---

## Purpose

Derive the effective 4D four-fermion contact strength G_eff from first principles using:
- OPR-19: g₅ → g₄,n dimensional reduction with warp cancellation
- OPR-20: Mediator mass m₁ = x₁/ℓ from Sturm–Liouville eigenvalue
- OPR-21: BVP mode profiles f_n(ξ) and Robin BC structure

**Key distinction**: G_eff is the EDC-computed quantity; G_F is the measured Fermi constant [BL]. We derive G_eff without using G_F as input.

**Closure criteria**:
- FULL [Dc]: G_eff computed from derived V(ξ), derived BC parameters, derived ℓ
- CONDITIONAL [Dc]: Structure derived, but V(ξ), κ, ℓ, g₅ remain [P]
- Remains [P]: Any SM observable used as input without derivation

---

## Lemma Chain

### L1: 5D Gauge-Fermion Action [M]

Starting from the canonical 5D action with gauge field and fermion current:

$$S = \int d^4x \, d\xi \, \sqrt{-G} \left[ -\frac{1}{4g_5^2} F_{MN} F^{MN} + \bar{\psi} \Gamma^M D_M \psi \right]$$

The gauge-fermion interaction term:

$$S_{\text{int}} = \int d^4x \, d\xi \, \sqrt{-G} \, g_5 \, J^M A_M$$

where $J^M$ is the 5D fermion current.

**Status**: [M] — standard field theory definition

---

### L2: Working Default — Brane-Localized Current [P]

**Assumption (WD-22-1)**: The fermion current relevant for weak interactions is localized on the brane at $\xi = 0$:

$$J^\mu(x,\xi) = j^\mu(x) \, \delta(\xi)$$

where $j^\mu(x)$ is the 4D fermion current.

**Alternative** (OPEN-22-1): Bulk-distributed current $J^\mu(x,\xi) = j^\mu(x) \rho(\xi)$ where $\rho(\xi)$ is the fermion localization profile.

**Rationale**: Brane-localized current is the standard ansatz in RS-type models and provides a clean derivation. The bulk alternative introduces overlap integrals that remain OPEN until OPR-21 provides physical profiles.

**Status**: [P] — working hypothesis

---

### L3: KK Mode Expansion [Dc]

Expand the gauge field (cf. OPR-20, L2):

$$A_\mu(x,\xi) = \sum_{n=0}^{\infty} a_\mu^{(n)}(x) \, f_n(\xi)$$

where:
- $a_\mu^{(n)}(x)$ are 4D gauge fields with mass $m_n$
- $f_n(\xi)$ are extra-dimensional mode profiles satisfying the Sturm–Liouville equation

**Status**: [Dc] — standard KK decomposition

---

### L4: Mode Normalization Convention [Dc]

**Convention (OPR-19)**: Natural normalization on domain $[0, \ell]$:

$$\int_0^\ell d\xi \, |f_n(\xi)|^2 = \ell$$

This gives a flat profile $f_0(\xi) = 1$ for the zero mode (Neumann BC).

**Resulting 4D coupling** (from OPR-19, L8):

$$\boxed{g_{4,n}^2 = \frac{g_5^2}{\ell}}$$

**Dimensional check**: $[g_5^2/\ell] = L/L = 1$ ✓

**Status**: [Dc] — derived from OPR-19 normalization

---

### L5: Brane-Localized Coupling [Dc]

For brane-localized current at $\xi = 0$, the interaction becomes:

$$S_{\text{int}} = g_5 \int d^4x \, j^\mu(x) \, A_\mu(x, \xi=0)$$

Substituting the KK expansion:

$$S_{\text{int}} = g_5 \sum_n \int d^4x \, j^\mu(x) \, a_\mu^{(n)}(x) \, f_n(0)$$

**Effective 4D coupling to mode n**:

$$\boxed{g_{\text{eff},n} = g_5 \, f_n(0)}$$

**Status**: [Dc] — follows from brane localization ansatz (L2)

---

### L6: Invariant Coupling Structure [Dc]

**Lemma L6.1** (Normalization Invariance)

Under rescaling $f_n \to c \cdot f_n$, the effective coupling transforms as:
- Normalization: $\int |f_n|^2 \to c^2 \int |f_n|^2$, so $g_{4,n}^2 \to g_{4,n}^2 / c^2$
- Brane evaluation: $f_n(0) \to c \cdot f_n(0)$, so $g_{\text{eff},n} \to c \cdot g_{\text{eff},n}$

**Key observation**: For brane-localized current, the physical coupling involves $g_{\text{eff},n}$, not $g_{4,n}$ directly.

**Invariant combination**:

$$\frac{g_{\text{eff},n}^2}{m_n^2} = \frac{g_5^2 \, f_n(0)^2}{m_n^2}$$

This is independent of normalization convention.

**For natural normalization** ($\int |f_n|^2 = \ell$, $f_0 = 1$):

If $f_n(0) \sim \mathcal{O}(1)$ (mode not suppressed at brane), then:

$$\frac{g_{\text{eff},n}^2}{m_n^2} \sim \frac{g_5^2}{m_n^2} = \frac{g_5^2 \ell^2}{x_n^2}$$

**Status**: [Dc] — algebraic manipulation

---

### L7: Integrate Out Mediator [Dc]

**Lemma L7.1** (Effective Four-Fermion Operator)

At energies $E \ll m_1$, integrating out the first massive mode $n=1$ generates a four-fermion contact interaction:

$$\mathcal{L}_{\text{eff}} = -\frac{g_{\text{eff},1}^2}{2 m_1^2} \, (j^\mu j_\mu)$$

**Definition L7.2** (Effective Contact Strength)

$$\boxed{G_{\text{eff}} := \frac{g_{\text{eff},1}^2}{2 m_1^2} = \frac{g_5^2 \, f_1(0)^2}{2 m_1^2}}$$

The factor of 2 arises from the standard normalization of four-fermion operators (Fermi theory convention).

**Status**: [Dc] — standard effective field theory

---

### L8: Invariant EFT Result and Dimensional Analysis [Dc]

**L8.1: Invariant Four-Fermion Formula**

The invariant result from integrating out the mediator is:

$$\boxed{G_{\text{eff}} = \frac{g_{4,1}^2}{2 m_1^2}}$$

where $g_{4,1}$ is the **dimensionless** 4D coupling to the first massive mode.

**L8.2: Brane-Localized Coupling Rule**

For brane-localized current at $\xi = 0$, the 4D coupling is:

$$g_{4,1} = g_5 \cdot \tilde{f}_1(0)$$

where $\tilde{f}_1$ is the **unit-normalized** profile: $\int_0^\ell |\tilde{f}_1|^2 d\xi = 1$, so $[\tilde{f}_1] = L^{-1/2}$.

**L8.3: Dimensional Bookkeeping**

| Quantity | Dimension | Source |
|----------|-----------|--------|
| $g_5$ | $L^{1/2}$ | 5D action: $[1/g_5^2] \cdot L^5 \cdot L^{-4} = 1$ |
| $\tilde{f}_1(0)$ | $L^{-1/2}$ | Unit normalization: $\int |\tilde{f}|^2 d\xi = 1$ |
| $g_{4,1} = g_5 \tilde{f}_1(0)$ | 1 | Dimensionless 4D coupling ✓ |
| $m_1$ | $L^{-1}$ | Mass eigenvalue |
| $G_{\text{eff}} = g_{4,1}^2/(2m_1^2)$ | $L^2$ | GeV⁻² ✓ |

**L8.4: 5D Form Using Unit Normalization**

Substituting $g_{4,1} = g_5 \tilde{f}_1(0)$ and $m_1 = x_1/\ell$:

$$G_{\text{eff}} = \frac{g_5^2 |\tilde{f}_1(0)|^2}{2 m_1^2} = \frac{g_5^2 |\tilde{f}_1(0)|^2 \ell^2}{2 x_1^2}$$

**Dimensional check**: $[g_5^2 \ell^2 |\tilde{f}_1(0)|^2 / x_1^2] = L \cdot L^2 \cdot L^{-1} / 1 = L^2$ ✓

**Status**: [Dc]

---

### L9: Connection to OPR-20 C_eff [Dc]

**Convention change**: For natural normalization $\int |f_n|^2 d\xi = \ell$ with dimensionless $f_n$:

$$\tilde{f}_n = \frac{f_n}{\sqrt{\ell}}, \quad |\tilde{f}_n(0)|^2 = \frac{|f_n(0)|^2}{\ell}$$

**G_eff in natural normalization**:

$$G_{\text{eff}} = \frac{g_5^2 \, \ell^2}{2 x_1^2} \cdot \frac{|f_1(0)|^2}{\ell} = \frac{g_5^2 \, \ell \, |f_1(0)|^2}{2 x_1^2}$$

**Final boxed formula** (natural normalization, brane-localized current):

$$\boxed{G_{\text{eff}} = \frac{g_5^2 \, \ell}{2 x_1^2} \cdot |f_1(0)|^2}$$

**Relation to OPR-20 C_eff**:

$$G_{\text{eff}} = \frac{1}{2} \, C_{\text{eff}} \cdot |f_1(0)|^2$$

where $C_{\text{eff}} = g_5^2 \ell / x_1^2$ from OPR-20.

**Dimensional check**:
- $[C_{\text{eff}}] = L^2$ (from OPR-20)
- $[|f_1(0)|^2] = 1$ (natural normalization)
- $[G_{\text{eff}}] = L^2 = \text{GeV}^{-2}$ ✓

**Status**: [Dc] — combines all prior results

---

## Factor Audit Table

| Factor | Origin | Value/Expression | Status |
|--------|--------|------------------|--------|
| $g_5^2$ | 5D gauge coupling | [P] parameter | [P] |
| $\ell$ | Domain size | [P] parameter | [P] |
| $x_1$ | First eigenvalue | $x_1(\kappa, V)$ from BVP | [Dc] given inputs |
| $m_1$ | First massive mode | $x_1/\ell$ | [Dc] |
| $f_1(0)$ | Mode value at brane | From OPR-21 BVP | [Dc] given V, κ |
| 1/2 | Fermi convention | Standard EFT | [M] |
| $C_{\text{eff}}$ | OPR-20 contact | $g_5^2 \ell / x_1^2$ | [Dc] |

---

## Assumptions Ledger

| ID | Statement | Status | Reference |
|----|-----------|--------|-----------|
| A-22-1 | Warped metric ansatz | [P] | L1, OPR-19 |
| A-22-2 | Brane-localized fermion current | [P] (WD) | L2 |
| A-22-3 | Domain $\xi \in [0, \ell]$ with ℓ postulated | [P] | L3, OPR-20 |
| A-22-4 | Effective potential V(ξ) shape | [P] | OPR-21 |
| A-22-5 | Robin BC parameters κ₀, κₗ | [P] | OPR-21 |
| A-22-6 | Mediator = first massive mode | [P] | OPR-20 |
| A-22-7 | Natural normalization ∫|f|²dξ = ℓ | [Dc] | L4, OPR-19 |
| A-22-8 | Fermi convention factor 1/2 | [M] | L7 |

---

## No-Smuggling Checklist

| Check | Status |
|-------|--------|
| No $M_W$ as input | ✓ |
| No $M_Z$ as input | ✓ |
| No $G_F$ as input | ✓ |
| No $v = 246$ GeV as input | ✓ |
| No $\sin^2\theta_W$ as input | ✓ |
| No $m_\mu$, $\tau_n$ as input | ✓ |
| Scale Taxonomy respected | ✓ |
| All rescalings explicit | ✓ |
| Profile normalization stated | ✓ |
| Dimensional analysis verified | ✓ |
| No double counting of $\|f_1(0)\|^2$ | ✓ |

---

## Failure Modes

| # | Failure Mode | How to Avoid | Status |
|---|--------------|--------------|--------|
| 1 | Using $G_F$ to fix $g_5$ or $\ell$ | All parameters [P]; no backsolving | ✓ Checked |
| 2 | Confusing unit vs natural normalization | Explicit conversion formulas | ✓ Checked |
| 3 | Missing factor of 2 in Fermi convention | Track from EFT definition | ✓ Checked |
| 4 | Wrong dimension for $g_5$ | State $[g_5] = L^{1/2}$ explicitly | ✓ Checked |
| 5 | Wrong dimension for $f_n$ | State convention (unit vs natural) | ✓ Checked |
| 6 | Ignoring $f_1(0)$ brane evaluation | Include in final formula | ✓ Checked |
| 7 | Assuming $f_1(0) = 1$ without justification | Note: depends on BC and V(ξ) | ✓ Checked |
| 8 | Mixing C_eff with G_eff | Distinct symbols, factor 1/2 differs | ✓ Checked |
| 9 | Bulk vs brane current confusion | State WD assumption explicitly | ✓ Checked |
| 10 | Circular: comparing to $G_F$ as validation | Label as "external comparison only" | ✓ Checked |
| 11 | Forgetting warp factor in coupling | Cf. OPR-19 warp cancellation | ✓ Checked |
| 12 | Wrong eigenvalue indexing ($m_0$ vs $m_1$) | Mediator is $n=1$, not $n=0$ | ✓ Checked |
| 13 | Double counting $\|f_1(0)\|^2$ | Brane coupling uses $g_{4,1} = g_5 \tilde{f}_1(0)$; C_eff has no $f_1(0)$ | ✓ Checked |

---

## Open Problems

| ID | Description | Priority | Status |
|----|-------------|----------|--------|
| OPEN-22-1 | Extract $\|f_1(0)\|^2$ from BVP mode profiles | HIGH | **RESOLVED** (2026-01-25) |
| OPEN-22-2 | Derive $g_5$ from UV completion or membrane physics | HIGH | OPEN |
| OPEN-22-3 | Derive $\ell$ from first principles | HIGH (shared with OPR-19/20) | OPEN |
| OPEN-22-4 | Compute $f_1(0)$ numerically for physical V(ξ) | MEDIUM | **CONDITIONAL [Dc]** |
| OPEN-22-5 | Include brane kinetic terms (BKT) and their effect on $G_{\text{eff}}$ | MEDIUM | OPEN |
| OPEN-22-6 | Multi-mediator corrections (sum over KK tower) | LOW | OPEN |
| OPEN-22-7 | Running of $G_{\text{eff}}$ with energy scale | LOW | OPEN |

---

## OPEN-22-1 Resolution: |f₁(0)|² Extraction from BVP

**Status**: RESOLVED [Dc] (2026-01-25)
**Sprint**: OPEN-22-1

### Summary

The brane amplitude |f₁(0)|² needed for G_eff has been extracted from the BVP mode profiles (OPR-21).

### Normalization Convention Bridge

**Natural normalization** (OPR-19/20 convention):
```
∫₀ˡ |f_n(ξ)|² dξ = ℓ     →  [f_n] = 1 (dimensionless)
f₀(ξ) = 1 (zero mode)
f₁(ξ) = √2 cos(πξ/ℓ) (first massive, toy limit)
```

**Unit normalization** (BVP solver output):
```
∫₀ˡ |f̃_n(ξ)|² dξ = 1     →  [f̃_n] = L^{-1/2}
f̃_n = f_n / √ℓ
```

**Conversion rule**:
```
|f̃_n(0)|² = |f_n(0)|² / ℓ
```

### Toy Limit Verification

For V(ξ) = 0 (flat potential) with Neumann BC:

| Quantity | Analytical | Numerical | Relative Error |
|----------|------------|-----------|----------------|
| x₁ | π ≈ 3.1416 | 3.1385 | 0.10% |
| \|f₁(0)\|² (natural) | 2.0000 | 2.0020 | 0.10% |

**Result**: Numerical extraction matches analytical toy limit to 0.1%.

### G_eff Connection

From L9, the final formula in natural normalization:
```
G_eff = g₅²ℓ|f₁(0)|²/(2x₁²)
      = ½ C_eff |f₁(0)|²      [using C_eff = g₅²ℓ/x₁² from OPR-20]
```

**Toy limit formula**:
```
G_eff^(toy) = g₅²ℓ × 2.0 / (2 × π²) = g₅²ℓ/π²
```

### Evidence Files

- `code/opr22_f1_brane_amplitude_extract.py` — Extraction script
- `code/output/opr22_f1_brane_amplitude.json` — Machine-readable results
- `code/output/opr22_f1_brane_amplitude_report.md` — Human-readable report

### Remaining Work

- Full [Der] closure requires derived parameter values (σ, Δ, ℓ, y, g₅) from independent physics

---

## OPEN-22-4 Resolution: Physical V(ξ) Pipeline

**Status**: CONDITIONAL [Dc] (2026-01-25)
**Sprint**: OPEN-22-4

### Summary

The complete pipeline OPR-01 → OPR-21 → OPR-22 is now operational with physical V(ξ):

```
σ, Δ, y [P] → M₀ [Dc] → V(ξ) [Dc] → BVP → f₁(0), x₁ [Dc] → G_eff [Dc]
```

### Physical Potential Used

From OPR-21 L2 (5D Dirac reduction, flat space):
```
V_L(ξ) = M(ξ)² - M'(ξ)
       = M₀² tanh²((ξ-ℓ/2)/Δ) - (M₀/Δ) sech²((ξ-ℓ/2)/Δ)
```

### M₀ from OPR-01 (Sigma Anchor)
```
M₀² = (3/4) y² σ Δ
μ = M₀ℓ (dimensionless parameter)
```

### Key Numerical Results (Target Regime: N_bound = 3)

| μ | x₁ | \|f₁(0)\|² | G_eff/(g₅²ℓ) |
|---|-----|-----------|--------------|
| 10 | 7.77 | 0.57 | 0.0048 |

**Note**: The physical domain wall potential V = M² - M' has N_bound = 3 at μ ≈ 10,
which differs from the Pöschl-Teller estimate (μ ∈ [25,35]). This reflects the
actual spectral properties of the derived potential.

### G_eff in Target Regime
```
G_eff = (g₅²ℓ) × |f₁(0)|² / (2x₁²)
      = (g₅²ℓ) × 0.57 / (2 × 60.4)
      = (g₅²ℓ) × 0.0048
```

### Evidence Files

- `code/opr22_open22_4_physical_run.py` — Pipeline script
- `code/output/open22_4_physical_summary.json` — Machine-readable results
- `code/output/open22_4_physical_table.md` — Human-readable table
- `audit/evidence/OPEN22_4_PHYSICAL_VEFF_REPORT.md` — Full evidence report

---

## OPEN-22-4b.1 Resolution: Slice-Family Stabilization

**Status**: CONDITIONAL [Dc] (2026-01-26)
**Sprint**: OPEN-22-4b.1

### Non-Universality Statement

**CRITICAL**: All band ranges below are **CONDITIONAL** on:
- Potential family: V_L = M² - M' (domain wall from 5D Dirac) [Dc]
- Boundary condition: κ (Robin BC parameter)
- Wall-to-domain ratio: ρ = Δ/ℓ

**Different shapes, BCs, or ρ values give different windows. No universal claims.**

### Slice-Family Sweep Summary

The physical μ-window [13, 17] was scanned for all slice combinations:
- κ ∈ {0, 0.5, 1, 2}
- ρ ∈ {0.05, 0.10, 0.20}
- μ ∈ [12, 18] (extended margin)

### Key Findings

| ρ | κ | N=3 μ-range | x₁ range | |f₁(0)|² range | Converged? |
|---|---|-------------|----------|---------------|------------|
| 0.05 | all | NOT achieved | — | — | — |
| 0.10 | all | NOT achieved | — | — | — |
| **0.20** | **0.0 (N)** | **[13.0, 15.5]** | **[10.19, 11.38]** | **[0.039, 0.158]** | **✓ YES** |
| 0.20 | 0.5-2.0 | [14.0, 17.0] | [0.04, 0.10] | ≈ 0 | ✗ NO |

**Key finding**: Only **Neumann (κ=0) + ρ=0.20** gives converged, non-trivial results.
**⚠ ERRATUM (OPEN-22-4b.2)**: Robin κ>0 results in this table are **FD implementation artifacts**. The FD solver has a bug that gives Neumann-like eigenvalues regardless of κ. See `audit/evidence/OPEN22_4bR_ROBIN_VERIFICATION_REPORT.md`.

### Convergence Worst-Case

| Test Point | rel_x₁ | rel_|f₁|² | rel_G_eff |
|------------|--------|----------|-----------|
| Neumann, ρ=0.2, μ=15 | 0.0004% | 0.24% | 0.24% |
| Robin κ=0.5, ρ=0.2, μ=14 | 0.6% | 75% | 75% |

~~Robin BC cases have exponentially small |f₁(0)|² (10⁻⁸ to 10⁻⁹) which is numerically unstable.~~
**⚠ RETRACTED (OPEN-22-4b.2)**: This was an artifact of FD Robin implementation bug, NOT physical decoupling. Analytic + scipy.integrate.solve_bvp show Robin BC affects spectrum nontrivially. Canonical Neumann (κ=0) results remain valid.

### Physical Results (Neumann, ρ=0.2)

| μ | x₁ | |f₁(0)|² | G_eff/(g₅²ℓ) |
|---|-----|---------|--------------|
| 13.0 | 10.19 | 0.158 | 7.62×10⁻⁴ |
| 14.0 | 10.69 | 0.093 | 4.05×10⁻⁴ |
| 15.0 | 11.16 | 0.052 | 2.11×10⁻⁴ |
| 15.5 | 11.38 | 0.039 | 1.51×10⁻⁴ |

### Evidence Files

- `code/open22_4b1_slice_family_sweep.py` — Slice-family sweep script
- `code/output/open22_4b1_slices.json` — Full results (SHA256: e9fd569b...)
- `code/output/open22_4b1_slices_table.md` — Human-readable table (SHA256: e7f4b212...)
- `code/output/open22_4b1_convergence_worstcase.json` — Convergence data (SHA256: 7a5ed0d1...)
- `code/output/open22_4b1_meta.json` — Solver settings + file hashes
- `audit/evidence/OPEN22_4b_MU_SWEEP_AUDIT.md` — Evidence report (updated)

---

## Closure Criteria Summary

| Component | Status | Evidence |
|-----------|--------|----------|
| 5D action to 4D EFT | [Dc] | L1–L7 |
| Normalization conventions | [Dc] | L4, L6, L8 |
| G_eff formula structure | [Dc] | L8, L9 |
| Connection to OPR-19/20 | [Dc] | L4, L9 |
| Dimensional verification | [M] | L8.3 |
| g₅ value | [P] | Not derived |
| ℓ value | [P] | Not derived |
| V(ξ) shape | [P] | OPR-21 |
| BC parameters κ | [P] | OPR-21 |
| f₁(0) extraction procedure | **[Dc]** | **OPEN-22-1 resolved** |
| f₁(0) toy limit | **[Dc]** | **\|f₁(0)\|² = 2.00 verified** |
| f₁(0) physical value | [P] | OPR-21 V(ξ) needed |
| **Overall OPR-22** | **CONDITIONAL [Dc]** | |

---

## Cross-Links

- **OPR-19**: g₅ → g₄ dimensional reduction (provides coupling normalization)
- **OPR-20**: Mediator mass m₁ = x₁/ℓ (provides C_eff structure)
- **OPR-21**: BVP mode profiles (provides f_n(ξ) and f₁(0))
- **OPR-01**: σ → M₀ anchor (upstream dependency)
- **OPR-04**: Scale Taxonomy (δ, Δ, ℓ, R_ξ definitions)

---

*Canon file created 2026-01-25*
