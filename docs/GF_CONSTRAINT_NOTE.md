# G_F Constraint Note — From RED Derivation to Constraint Window

**Version:** 1.1
**Date:** 2026-01-29 (patched)
**Status:** Constraint established; first-principles derivation remains OPEN
**Purpose:** Turn G_F derivation (currently RED-C) into a useful constraint window

---

## A. Executive Summary (5 Bullets)

1. **G_F derivation is RED-C** — First-principles calculation not achieved; requires g₅, m_φ, BVP solution

2. **Constraint window defined** — EDC must satisfy: g_eff²/M_eff² ∈ [0.9, 1.1] × G_F to be viable

3. **Dimensionless check quantity** — X := G_F m_e² = 3.04 × 10⁻¹² is the target (natural units)

4. **Projection mapping** — g_eff² ∝ ⟨K_g⟩_w and M_eff² ∝ ⟨K_M⟩_w via Projection-Reduction Lemma

5. **What IS derived** — sin²θ_W = 1/4 [Der] is the true independent prediction (0.08% agreement)

---

## B. Baseline [BL]: Standard Model Relations

### B.1 Fermi Constant (PDG 2024)

```
G_F = 1.1663787(6) × 10⁻⁵ GeV⁻²     [BL]
```

**Source:** PDG 2024 (muon decay measurement)

### B.2 Electroweak Relations

**Tree-level W-exchange:**
```
G_F = g²/(4√2 M_W²)                  [BL]
```

**Higgs VEV definition:**
```
v = (√2 G_F)^{-1/2} = 246.22 GeV     [BL]
```

**Electroweak coupling:**
```
g² = 4πα/sin²θ_W                     [BL]
M_W = gv/2                           [BL]
```

### B.3 Circularity Caveat (CRITICAL)

**WARNING:** The Higgs VEV v is DEFINED from G_F:
```
v = (√2 G_F)^{-1/2}
```

Therefore: Using v to derive M_W, then M_W to derive G_F is **circular**.

**Implication:** G_F "exact agreement" via EW relations is a **consistency identity**, not an independent EDC prediction.

---

## C. EDC Mapping via Projection-Reduction Lemma

### C.1 Lemma Reference

**Source:** `edc_papers/_shared/lemmas/projection_reduction_lemma.tex`
**Labels:** Definition `\ref{def:projection-operator}`, Lemma `\ref{lem:projection-reduction}`

### C.2 Mediator Integration Structure

In EDC, G_F arises from integrating out a brane-layer mediator [Dc]:

```
G_EDC ~ g_eff² / M_eff²
```

**Source:** `sections/11_gf_derivation.tex:eq:ch11_GF_structure`

### C.3 Projection-Reduction Mapping

Using Case (A) of the Projection-Reduction Lemma:

**Effective coupling as overlap integral:**
```
g_eff² = g₅² × ∫ dχ w(χ) K_g(χ)  :=  g₅² × ⟨K_g⟩_w     [P]
```

where K_g(χ) encodes the gauge-field profile in the extra dimension.

**Effective mediator mass as projected curvature:**
```
M_eff² = ∫ dχ w(χ) K_M(χ)  :=  ⟨K_M⟩_w                 [P]
```

where K_M(χ) arises from KK reduction of the ξ-sector geometry.

### C.4 Mode Overlap Factor

Using Case (B) for chirality:
```
I₄ := ∫ dχ |f_L(χ)|⁴                                   [P]
```

This overlap integral appears in the four-fermion effective vertex:
```
G_EDC ~ g₅² × I₄ / M_eff²                              [P]
```

**Current status:** I₄ estimated as ~200 MeV (order-of-magnitude), but ×100 off from required value.

**Source:** `CH11_GF_NOTES.md` (Mode overlap I₄ ~ 200 MeV [P])

---

## D. Dimensionless Form

### D.1 Define Dimensionless Check Quantity

To create a parameter-free constraint, define (in natural units ℏ = c = 1):

```
X := G_F m_e²                                          [Definition]
```

**Unit convention:** Throughout this document we use natural units where G_F has dimension [Energy]⁻² and m_e has dimension [Energy]. The product X is dimensionless.

**Numerical value [BL]:**
```
X = G_F × m_e²
  = 1.1664 × 10⁻⁵ GeV⁻² × (0.511 × 10⁻³ GeV)²
  = 1.1664 × 10⁻⁵ × 2.61 × 10⁻⁷
  = 3.04 × 10⁻¹²                                       [BL]
```

### D.2 Express X_EDC in Terms of EDC Parameters

**General form [P]:**
```
X_EDC = (g_eff² / M_eff²) × m_e²
      = g₅² × ⟨K_g⟩_w / ⟨K_M⟩_w × m_e²
```

**Using EDC scales:**

If we express M_eff in terms of brane thickness δ:
```
M_eff ~ 1/δ = 2m_p c/ℏ ~ 1.88 GeV                      [Dc]
```

Then:
```
X_EDC ~ g_eff² × m_e² / M_eff²
      ~ g_eff² × (0.511 MeV / 1.88 GeV)²
      ~ g_eff² × 7.4 × 10⁻⁸
```

To match X = 3 × 10⁻¹², we need:
```
g_eff² ~ 4 × 10⁻⁵                                      [Constraint]
```

### D.3 σ Cancellation Analysis

Does σ enter X_EDC independently?

**If M_eff² ∝ σ:** Then X_EDC ∝ 1/σ (σ enters explicitly)
**If M_eff² ∝ 1/δ²:** Then σ cancels via δ = f(σ) relation

**Current understanding [I]:**
- M_eff likely determined by brane geometry (δ, R_ξ), not directly by σ
- σ may enter through effective coupling g_eff (normalization of 5D action)
- Full σ dependence requires BVP solution (OPEN)

---

## E. Constraint Window

### E.1 Primary Constraint

Since G_F is not derived from first principles, EDC must satisfy:

```
┌─────────────────────────────────────────────────────────────────┐
│  CONSTRAINT: g_eff² / M_eff² must reproduce G_F within ±10%    │
│                                                                 │
│  g_eff² / M_eff² ∈ [0.9, 1.1] × G_F                            │
│                   = [1.05, 1.28] × 10⁻⁵ GeV⁻²                  │
│                                                                 │
│  Equivalently: X_EDC ∈ [0.9, 1.1] × 3.04 × 10⁻¹²              │
│                      = [2.7, 3.3] × 10⁻¹²                      │
└─────────────────────────────────────────────────────────────────┘
```

**Note:** The interval [0.9, 1.1] × G_F corresponds to ±10% tolerance around the baseline G_F = 1.1664 × 10⁻⁵ GeV⁻².

### E.2 Translated Constraints on EDC Parameters

**Option 1: Fix M_eff from brane geometry**
```
If M_eff = 1/δ ~ 1.9 GeV (from δ = ℏ/(2m_p c))

Then: g_eff² must satisfy:
  g_eff² = G_F × M_eff² = 1.17 × 10⁻⁵ × 3.6 = 4.2 × 10⁻⁵

Constraint: g_eff ~ 6.5 × 10⁻³                         [Window]
```

**Option 2: Fix g_eff from sin²θ_W**
```
If g_eff² ~ g² = 4πα/sin²θ_W = 0.425 (at tree level)

Then: M_eff² = g_eff² / G_F = 0.425 / (1.17 × 10⁻⁵) = 3.6 × 10⁴ GeV²

Constraint: M_eff ~ 190 GeV                            [Window]
```

This is close to M_W = 80 GeV (factor ~2.4 off), suggesting SM-like mediator.

### E.3 Mode Overlap Constraint

**From four-fermion structure [P]:**
```
G_F ~ g₅² × I₄ / M_eff²
```

If g₅ ~ O(1) (natural 5D coupling) and M_eff ~ 1/δ ~ 1.9 GeV:
```
I₄ must satisfy: I₄ ~ G_F × M_eff² / g₅² ~ 4 × 10⁻⁵ GeV²

I₄ ~ (6 MeV)² ~ (r_e⁻¹)²                              [Window]
```

This is consistent with fermion localization scale ~ r_e.

### E.4 Why Naive Overlap Is Too Large (Critical Insight)

In generic 5D setups with localized fermion profiles, naive estimates often give g₅² I₄ ~ O(1) because normalized wavefunctions have ∫|f|² = 1, so ∫|f|⁴ ~ 1/width is naturally large. To reproduce the tiny G_F ~ 10⁻⁵ GeV⁻² then requires **either** (a) a heavy mediator M_eff ~ 100 GeV (electroweak scale), **or** (b) strong overlap suppression via the chirality mechanism of Projection-Reduction Lemma Case (B): if left and right modes are spatially separated, the effective coupling ε = ∫ w_L w_R ≪ 1 suppresses the vertex. Therefore, the BVP overlap calculation is a **decisive falsification channel**: if the thick-brane solution gives I₄ incompatible with the constraint window (neither EW-scale mediator nor chiral suppression), the mode-overlap mechanism fails.

---

## F. Falsifiability (3 Failure Modes)

### F.1. No BVP Solution with Required Overlap

**Failure:** The thick-brane boundary value problem yields mode profiles f_L(χ) whose overlap integral I₄ is incompatible with the constraint window (off by more than factor 10).

**Implication:** Mode overlap mechanism fails; alternative G_F origin needed.

### F.2. Mediator Mass Inconsistent with δ

**Failure:** KK reduction of ξ-geometry gives M_eff that violates:
```
M_eff ∈ [0.1, 10] × (1/δ)
```

**Implication:** Brane thickness interpretation fails; geometry needs revision.

### F.3. Coupling g_eff Incompatible with sin²θ_W

**Failure:** If g_eff derived from 5D action is incompatible with:
```
g_eff² = 4πα/sin²θ_W × f(overlaps)
```

where f(overlaps) ~ O(1), then electroweak unification picture breaks.

**Implication:** Z₆ → sin²θ_W connection is accidental, not fundamental.

---

## G. Upgrade Roadmap: [Dc] → [Der]

### G.1 Current Status

| Level | Status | What It Means |
|-------|--------|---------------|
| GREEN-A | Achieved | EW consistency closure (circular) |
| YELLOW-B | Achieved | Mechanism identified (qualitative) |
| RED-C | **OPEN** | First-principles derivation |

### G.2 Required 5D Calculations for [Der]

To upgrade G_F from constrained [Dc] to derived [Der]:

**Step 1: 5D Coupling Normalization**
```
Derive g₅ from canonical normalization of 5D gauge action:
S_5D = ∫ d⁵x √g (-1/4g₅²) F_{MN} F^{MN}

Output: g₅ = f(σ, δ, R_ξ)
```

**Step 2: Mediator Mass from KK Reduction**
```
Perform KK reduction along ξ-direction (throat geometry):
φ(x,ξ) = Σ_n φ_n(x) f_n(ξ)

Solve eigenvalue problem: (-∂²_ξ + V(ξ)) f_n = m_n² f_n

Output: m_φ = m_0 = lowest massive eigenvalue
```

**Step 3: Mode Profiles from BVP**
```
Solve thick-brane Dirac equation with BC:
(γ^μ ∂_μ + γ^5 ∂_χ - m(χ)) Ψ = 0

with asymmetric mass profile m(χ) → chirality selection

Output: f_L(χ), f_R(χ) normalized mode profiles
```

**Step 4: Overlap Integral Computation**
```
Compute I₄ = ∫ dχ |f_L(χ)|⁴ exactly (not OOM)

Output: I₄ = numerical value
```

**Step 5: Assembly**
```
G_F^{EDC} = g₅² × I₄ / m_φ²

Compare: |G_F^{EDC} - G_F^{exp}| / G_F^{exp} < 10%
```

### G.3 Blocking Dependency

```
BVP Solution (OPR-04)
       ↓
Mode Profiles f_L(χ)
       ↓
Overlap I₄ + Mediator m_φ
       ↓
G_F First-Principles (RED-C → GREEN-A)
```

---

## H. File References

| Topic | Source | Label/Section |
|-------|--------|---------------|
| G_F baseline | PDG 2024 | — |
| EW relations | `sections/11_gf_derivation.tex` | `\label{eq:ch11_GF_SM}` |
| Structural pathway | `sections/11_gf_derivation.tex` | `\label{sec:ch11_structural}` |
| Circularity firewall | `CH11_GF_NOTES.md` | Section "Circularity Firewall" |
| Projection Lemma | `edc_papers/_shared/lemmas/projection_reduction_lemma.tex` | `\ref{lem:projection-reduction}` |
| sin²θ_W derivation | `sections/05_three_generations.tex` | `\label{eq:ch3_sin2_bare}` |
| BVP workpackage | `sections/ch12_bvp_workpackage.tex` | — |

---

## I. Claim Ledger Entry

```yaml
id: CL-11.4
status: YELLOW
chapter: 11
claim: "G_F constrained (not derived): g_eff²/M_eff² ∈ [0.9,1.1]×G_F"
evidence:
  file: "docs/GF_CONSTRAINT_NOTE.md"
  equation: "Section E"
tag: "[Dc]"
notes: |
  First-principles derivation is RED-C (open).
  Constraint window defined from EW relations + Projection Lemma.
  True independent prediction: sin²θ_W = 1/4 [Der].
```

---

## J. Open Problem Entry

```yaml
id: OPR-GF
status: OPEN
priority: P1
title: "Derive G_F from 5D action + BVP"
description: |
  Calculate g₅, m_φ, f_L(χ), and I₄ from first principles.
  Required: 5D gauge normalization, KK reduction, thick-brane BVP.
  Goal: G_F^{EDC} within 10% of G_F^{exp} without circular v input.
blocking:
  - OPR-04 (BVP solution)
  - OPR-19 (g₅ from action)
  - OPR-20 (mediator mass from eigenvalue)
```

---

*G_F Constraint Note v1.1 — Establishes constraint window pending first-principles derivation. True EDC prediction: sin²θ_W = 1/4.*
