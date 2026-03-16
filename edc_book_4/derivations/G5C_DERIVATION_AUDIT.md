# Prove-or-Fail: Derivation of g₅^(C) from EDC Geometry

## Status: FAIL — g₅^(C) is an irreducible free parameter
## Date: 2026-03-16
## Layer: A (structural analysis; Layer B used only for numerical cross-checks)
## Depends on: v36 (3 tracks), v47 (PS canonicalization), v56 (Routes A/C),
##             edc_book_2 ch11/ch17, PS_UNIFICATION_HOOK_AUDIT, COSMOLOGICAL_CONSTANT_SIGMA_TILDE

---

## 1. Executive Verdict

**g₅^(C) CANNOT be derived from EDC axioms P1–P4 and the 5D geometry.**

Every route tested either:
- Produces a value catastrophically inconsistent with experiment (Routes A, C), or
- Contains an undetermined O(1) coefficient that absorbs the answer (Track C with Λ₅ = π/L), or
- Relies on a postulated input (membrane formula with r_e), or
- Relates g₅^(C) to other unknowns without fixing it (KK normalization, Israel junction).

The fundamental reason is structural: the 5D gauge action is a separate sector
from the 5D Einstein-Hilbert action. EDC axioms P1–P4 govern the gravitational/
geometric sector (warp factor, brane tension, domain size, 5D Planck mass).
They do NOT constrain the coefficient of the gauge kinetic term because no
EDC axiom couples gauge dynamics to geometry at the level needed to fix g₅.

**Consequence:** g₅^(C) requires one experimental measurement — α_s(M_Z) —
to be determined. This is analogous to how the Standard Model requires g_s
as a free parameter. EDC inherits this freedom from 5D gauge theory.

**Impact:** With g₅^(C) as a free parameter, the v56 formula α₃ = 1/σ̃
is structurally incorrect (it assumed Route A/C with marginal coupling).
The σ̃ trilemma is dissolved: σ̃ = 1 is the correct structural value,
and α_s(M_Z) determines g₅^(C) independently.

---

## 2. Route A Analysis (g₅² = 4π/M₅)

### 2.1 The route

From v56 §3.2 (eq:route-a-formula, line 414) and v36 §Track A (line 409):

```
(g₅^PS)² = c_A / M₅     where c_A = 4π (marginal weak coupling)
```

**Justification:** Theory weakly coupled at 5D Planck scale:
(g₅^PS)² M₅ < 4π → c_A < 4π; adopt marginal value c_A = 4π.

**Tag:** [Dc]+[P] — dimensional analysis is derived; c_A = 4π is postulated.

### 2.2 Resulting α₃ formula

From v56 §4 (eq:alpha3-route-a-final, line 628):

```
α₃^(A)(μ*) = 1 / (M̄_Pl · L)^{2/3}
```

### 2.3 Numerical evaluation [Layer B cross-check]

Using M̄_Pl = 2.435 × 10¹⁸ GeV, L = π/M_Z = 3.445 × 10⁻² GeV⁻¹:

```
M̄_Pl · L = 2.435 × 10¹⁸ × 3.445 × 10⁻² = 8.39 × 10¹⁶

(M̄_Pl · L)^{2/3} = (8.39 × 10¹⁶)^{2/3}

log₁₀(8.39 × 10¹⁶) = 16.924
(2/3) × 16.924 = 11.283
10^{11.283} = 1.92 × 10¹¹

α₃^(A)(μ*) = 1 / (1.92 × 10¹¹) = 5.2 × 10⁻¹²
```

### 2.4 Comparison with experiment

```
α₃^(A)(μ*)     = 5.2 × 10⁻¹²
α_s(M_Z)        = 0.1180

Ratio: 0.118 / 5.2×10⁻¹² = 2.3 × 10¹⁰
```

**Route A fails by 10 orders of magnitude.**

### 2.5 Diagnosis

The failure is expected. Route A fixes g₅ at the 5D Planck scale M₅ ~ 10¹² GeV,
which gives an extremely weak 4D coupling at the compactification scale:

```
g₄² = 4π / (M₅ L) = 4π / (5.6×10¹² × 3.445×10⁻²)
     = 4π / (1.93 × 10¹¹) = 6.5 × 10⁻¹¹

α₃ = g₄² / (4π) = 5.2 × 10⁻¹²
```

The problem: M₅ is too large. The 5D Planck scale is a gravitational scale;
there is no physical reason that the gauge coupling should saturate its
perturbativity bound at this scale. In the Standard Model, g_s(M_Pl) ≈ 0.5
(far from the perturbativity bound 4π).

### 2.6 Structural assessment

Route A assumes that gauge and gravitational sectors share the same UV scale.
This is a non-trivial assumption [P] that is not implied by EDC axioms P1–P4.
The 5D gauge kinetic term S₅ = −(1/4g₅²) ∫ F² and the 5D Einstein-Hilbert
term S₅^(grav) = M₅³ ∫ R are independent sectors with independent couplings.

**Route A FAILS as a derivation of g₅^(C).**

---

## 3. Route C Analysis (g₅² = 4π/Λ₅)

### 3.1 The route

From v56 §3.3 (eq:route-c-formula, line 460) and v36 §Track C (line 633):

```
(g₅^PS)² = 4π / Λ₅
```

where Λ₅ is the 5D UV cutoff defined by strong coupling criterion:
(g₅^PS)² Λ₅ ~ 4π.

### 3.2 Cutoff definitions tested

**Option C1: Λ₅ = M₅ (5D Planck mass)**

This reduces to Route A: g₅² = 4π/M₅. Same failure.

**Option C2: Λ₅ = σ^{1/4} (brane tension scale)**

From the user's prompt analysis:
```
σ_RS = 1.242 × 10³⁹ GeV⁴
Λ₅ = σ_RS^{1/4} = (1.242 × 10³⁹)^{1/4} = 5.94 × 10⁹ GeV

g₅² = 4π / (5.94 × 10⁹) = 2.12 × 10⁻⁹ GeV⁻¹
```

Compare with experiment:
```
g₅²_exp = 4π × α_s(M_Z) × L = 4π × 0.118 × 0.03445 = 0.0511 GeV⁻¹

Ratio: 0.0511 / 2.12×10⁻⁹ = 2.4 × 10⁷
```

**Route C2 fails by 7 orders.**

**Option C3: Λ₅ = π/L (KK cutoff)**

From v36 lines 663-676:
```
g₅² = 4π c_C L / π = 4 c_C L

g₄² = g₅² / L = 4 c_C
```

This gives a dimensionless O(1) coupling. For α₃ = 0.118:
```
4 c_C = 4π × 0.118 = 1.483
c_C = 0.371
```

But c_C is a free parameter (≤ 1 by perturbativity). Setting c_C = 0.371
to match experiment is curve-fitting, not derivation. The formula g₄² = 4c_C
is algebraically trivial — it just relabels the unknown coupling.

**Route C3 is circular: c_C absorbs g₅^(C) as a free parameter.**

**Option C4: Λ₅ = √(M̄_Pl²/σ) (v56 definition)**

From v56 line 476:
```
Λ₅ = 1/ℓ_σ = √(M̄_Pl²/σ)
```

Dimensional check: [M̄_Pl²/σ] = GeV²/GeV⁴ = GeV⁻². So [Λ₅] = GeV⁻¹.
This is a length scale, not a mass scale. As a cutoff (1/Λ₅):

```
1/Λ₅ = √(σ/M̄_Pl²) = √(1.242×10³⁹ / 5.929×10³⁶) = √209.4 = 14.5 GeV
```

Then g₅² = 4π × Λ₅ = 4π × 0.069 = 0.866 GeV⁻¹, giving:
```
α₃ = g₅²/(4πL) = 0.866/(4π × 0.0345) = 2.0
```

Too large by a factor of 17. And the dimensional interpretation of the
v56 cutoff formula is questionable (it yields a length, not an energy).

### 3.3 Structural assessment

All Route C variants share the same problem: the cutoff Λ₅ is either
too large (giving too-small coupling) or contains a free parameter that
absorbs the answer. The strong-coupling criterion g₅² Λ₅ ~ 4π is a
bound, not a determination — the theory need not saturate it.

**Route C FAILS as a derivation of g₅^(C).**

---

## 4. Membrane Geometry Routes

### 4.1 Route M1: KK normalization

The zero-mode gauge field normalization gives (v47 line 680, edc_book_2 ch17):
```
1/g₄² = L / g₅²
```

This relates g₄ and g₅ but does not fix either. One external input is
always required.

**Status: CONSTRAINT only, not a determination.**

### 4.2 Route M2: Membrane stiffness formula (edc_book_2 ch11)

From edc_book_2/src/sections/ch11_g5_ell_value_closure_attempt.tex:
```
g² = 4π × σ r_e³ / (ℏc)
```

where r_e = 1 fm [P] is the postulated lattice spacing.

Numerical evaluation:
```
σ r_e² = 5.856 MeV    [Dc from Z₆ geometry]
r_e = 1 fm             [P]
g² = 4π × (5.856 × 1) / 197.3 = 0.373
```

Compare with g_s² = 4π × 0.118 = 1.48. Off by factor 4.
Compare with g_2² ≈ 0.42. Off by 11%.

The 4π coefficient has two derivations (edc_book_2 ch11 attempt3):
- Route 1: 3D Gauss's law solid angle [Dc]
- Route 2: S² isotropy normalization [Dc]+[P]

**But r_e = 1 fm is an irreducible postulate.** Without this input,
the formula cannot determine the coupling. And even with it, the
resulting g² = 0.37 doesn't match α_s(M_Z).

**Status: FAIL — requires postulated r_e; wrong numerical value.**

### 4.3 Route M3: Topological quantization

Standard result: topological charge quantization (e.g., Dirac quantization,
instanton number) fixes the RATIO of couplings (e.g., e = g sin θ_W)
but not the overall scale.

In EDC: no topological mechanism has been identified that would quantize
g₅^(C) to a specific value.

**Status: FAIL — fixes ratios, not absolute scale.**

### 4.4 Route M4: Israel junction for gauge fields

The Israel junction conditions fix the discontinuity in the extrinsic
curvature across the brane: [K_μν] = −κ₅²(S_μν − (1/3)S g_μν).

For gauge fields: gauge fields propagate in the bulk with continuous
boundary conditions at the brane. There is no analogue of the Israel
junction that constrains gauge couplings from brane geometry.

In brane-localized gauge theory, the gauge kinetic term can receive
brane-localized contributions (Δ_brane in v56 §6), but these are
additive corrections with their own free coefficient δ_C.

**Status: FAIL — Israel conditions apply to gravity, not gauge couplings.**

---

## 5. Dimensional Analysis

### 5.1 The target

```
[g₅^(C)²] = M⁻¹ (mass dimension −1)
g₅^(C)²_exp = 0.051 GeV⁻¹  [from α_s(M_Z) = 0.118, L = π/M_Z]
```

### 5.2 Available EDC parameters

| Parameter | Value | Dimension | Source |
|-----------|-------|-----------|--------|
| M₅ | 5.6 × 10¹² GeV | M¹ | v23 [I]+[BL] |
| M̄_Pl | 2.435 × 10¹⁸ GeV | M¹ | Measured [BL] |
| L | 3.445 × 10⁻² GeV⁻¹ | M⁻¹ | v21 [I]+[BL] |
| ℓ | 3.376 × 10⁻² GeV⁻¹ | M⁻¹ | RS hierarchy [I]+[BL] |
| σ_RS | 1.242 × 10³⁹ GeV⁴ | M⁴ | v68 [Der] |

### 5.3 Combinations with [M⁻¹]

```
1/M₅     = 1.79 × 10⁻¹³ GeV⁻¹     (too small by 10⁸·⁵)
1/M̄_Pl   = 4.11 × 10⁻¹⁹ GeV⁻¹     (too small by 10¹⁷)
L         = 3.45 × 10⁻² GeV⁻¹       (close! ratio = 1.48)
ℓ         = 3.38 × 10⁻² GeV⁻¹       (close! ratio = 1.51)
```

### 5.4 The L-coincidence

The closest match is g₅²_exp ≈ 1.48 × L. But:

```
g₅² = c × L  →  g₄² = c  →  α₃ = c/(4π)

c = g₅²_exp / L = 0.0511 / 0.03445 = 1.483

Note: 1.483 = 4π × 0.118 = 4π × α_s(M_Z)
```

So g₅² = 4π α_s(M_Z) × L, which is the definition:
α₃ = g₅²/(4πL). **This is circular** — the coefficient c encodes
exactly the quantity we're trying to derive.

### 5.5 Can any non-circular combination work?

The only EDC parameters with dimension M⁻¹ are L, ℓ, and 1/M₅.
- 1/M₅ fails numerically (too small by 10⁸·⁵)
- L and ℓ both give g₅² ~ L with an undetermined O(1) coefficient
- The O(1) coefficient IS the 4D coupling strength

No combination of purely geometric EDC parameters produces the correct
coefficient without importing α_s(M_Z).

### 5.6 Deeper reason

In 4D, the gauge coupling g₄ is dimensionless. In 5D, g₅² ~ L absorbs
one power of L from the extra dimension. The overall normalization of
the gauge kinetic term is a free parameter of the Lagrangian.

This is not specific to EDC — it is a general feature of 5D gauge theories.
The gauge coupling is a separate input from the geometry, just as in 4D
the gauge coupling is separate from the metric.

---

## 6. What One Measurement Would Suffice

### 6.1 The minimal input

A single measurement of any 4D gauge coupling at any scale determines g₅^(C):

```
α_s(M_Z) = 0.1180 ± 0.0009     [PDG 2024]

↓  (SM RG running from M_Z to μ* = M_Z, trivially α₃(μ*) = α_s(M_Z))

α₃(μ*) = 0.1180

↓  (KK reduction: g₄² = g₅²/L)

g₅^(C)² = 4π α₃(μ*) × L = 4π × 0.1180 × π/M_Z
         = 4π² × 0.1180 / 91.19
         = 0.05107 GeV⁻¹
```

### 6.2 What this single measurement buys

With g₅^(C) = 0.226 GeV⁻¹/² fixed:

| Derived quantity | Formula | Value |
|-----------------|---------|-------|
| g₄^(C) | g₅^(C)/√L | 1.218 |
| α₃(μ*) | g₄² / (4π) | 0.118 |
| g₅^(L) | = g₅^(C) via PS hook [P] | 0.226 GeV⁻¹/² |
| g₅^(R) | = g₅^(C) via PS hook [P] | 0.226 GeV⁻¹/² |
| g₅^(B-L) | = g₅^(C) via SU(4)_C [D] | 0.226 GeV⁻¹/² |
| α_PS(μ*) | = α₃(μ*) | 0.118 |

### 6.3 What this measurement does NOT buy

- σ̃ is NOT determined by α_s(M_Z) (σ̃ = 1 from RS geometry)
- β is NOT determined by α_s(M_Z) (β from v29 dynamics)
- The v56 formula α₃ = 1/σ̃ is NOT used (it was derived under
  Route A assumptions that fail numerically)

---

## 7. OPR-32 Draft

### 7.1 Statement

**OPR-32: g₅^(C) is an irreducible free parameter of EDC**

The 5D colour gauge coupling g₅^(C) cannot be derived from EDC axioms
P1–P4, the 5D geometry, or any known consistency condition. It requires
one experimental measurement (α_s(M_Z)) as input.

### 7.2 Evidence

| Route | Formula | Numerical result | vs. experiment | Verdict |
|-------|---------|-----------------|----------------|---------|
| A (Tension) | g₅² = 4π/M₅ | α₃ = 5.2×10⁻¹² | ×2.3×10¹⁰ off | FAIL |
| C2 (σ^{1/4}) | g₅² = 4π/σ^{1/4} | α₃ ~ 10⁻⁸ | ×10⁷ off | FAIL |
| C3 (π/L) | g₅² = 4c_C L/π | α₃ = c_C/π | free c_C | CIRCULAR |
| C4 (v56 cutoff) | g₅² = 4π√(M̄²/σ) | α₃ ~ 2.0 | ×17 off | FAIL |
| M2 (membrane) | g² = 4πσr_e³/(ℏc) | g² = 0.37 | uses r_e [P] | FAIL |
| M3 (topological) | — | fixes ratios only | — | FAIL |
| M4 (Israel) | — | applies to gravity | — | N/A |
| Dim. analysis | g₅² ~ L × O(1) | O(1) = 4πα_s | circular | FAIL |

### 7.3 Root cause

The 5D gauge kinetic term:
```
S₅ = −(1/4g₅²) ∫ d⁵x F_MN^a F^{aMN}
```

is an independent sector from the 5D gravitational action:
```
S₅^(grav) = M₅³ ∫ d⁵x √(−G) R
```

EDC axioms P1–P4 constrain the geometry (metric, warp factor, brane dynamics).
They do not constrain the gauge kinetic coefficient g₅². The gauge-gravity
coupling occurs only through:
1. The background metric (already accounted for in KK reduction)
2. Brane-localized terms (additive corrections with their own free coefficients)

Neither mechanism fixes the overall gauge coupling scale.

### 7.4 Comparison with Standard Model

| Parameter | SM status | EDC status |
|-----------|-----------|------------|
| g_s | Free parameter | Free parameter (g₅^(C)) |
| g_2 | Free parameter | Free parameter (g₅^(L)) |
| g_1 | Free parameter | Determined from g₅^(L), g₅^(C) via PS matching |
| sin²θ_W | From g_1/g_2 | From PS matching (v47) |

EDC reduces the number of independent gauge couplings from 3 (SM) to 2
(g₅^(C), g₅^(L)) via PS structure. The PS unification hook [P] further
reduces this to 1 (g₅^PS). But this last coupling remains free.

### 7.5 Closure condition

OPR-32 is CLOSED iff one of the following is achieved:

1. A mechanism within EDC dynamics (Plenum field stabilization, anomaly
   cancellation, brane dynamics) is found that selects a unique value
   of g₅^(C); OR

2. An embedding of EDC in a larger structure (string theory, SO(10) GUT)
   determines g₅^(C) from higher-level parameters; OR

3. It is formally proven that g₅^(C) is a free parameter in any 5D
   brane-world theory (making the problem framework-independent).

### 7.6 Paths forward (ranked by plausibility)

1. **Accept as free parameter.** Just as the SM accepts g_s as free,
   EDC accepts g₅^(C) as free. This is the most honest position.
   One measurement (α_s(M_Z)) fixes it completely.

2. **Anomaly cancellation.** In 5D, mixed gauge-gravitational anomalies
   can in principle constrain gauge couplings. This has not been checked
   for the PS gauge group in EDC geometry. LOW probability of fixing
   the absolute scale (anomaly cancellation typically fixes discrete
   choices, not continuous parameters).

3. **Asymptotic safety / fixed point.** If the 5D gauge-gravity system
   has a UV fixed point, g₅ could be determined by the fixed-point value.
   Requires non-perturbative analysis of 5D PS gauge theory coupled to
   RS gravity. SPECULATIVE.

4. **String embedding.** If EDC arises from a string compactification,
   g₅ is determined by string moduli (dilaton, compactification radius).
   This moves the problem to moduli stabilization. BEYOND current scope.

---

## 8. Revised BLOCK-004 Status

### 8.1 Impact on v56 derivation chain

| v56 result | Status before audit | Status after audit |
|-----------|--------------------|--------------------|
| PS unification hook (§2) | [P] — postulated | [P] — unchanged |
| Route A: g₅² = 4π/M₅ (§3.2) | [Dc]+[P] — admissible | [Dc]+[P] — FAILS numerically |
| Route C: g₅² = 4π/Λ₅ (§3.3) | [Dc]+[P] — admissible | [Dc]+[P] — FAILS numerically |
| α₃ = 1/(M̄_Pl·L)^{2/3} (§4) | [Dc] — derived from Route A | [Dc] — correct IF Route A; but Route A gives wrong answer |
| α₃ = 1/σ̃ (§4.7) | [Dc] — canonical baseline | INVALIDATED — requires β = σ̃⁴ and Route A, both fail |
| Brane smallness [P] (§6) | [P] — postulated | [P] — moot if baseline is wrong |
| T1 = T2 verification (§5) | PASS | PASS — algebraically correct, but both use wrong Route A |

### 8.2 What survives from v56

1. **Dimensional analysis** [g₅²] = M⁻¹ (§3.1) — SURVIVES, algebraic fact
2. **KK reduction** g₄² = g₅²/L (§4.1) — SURVIVES, standard result
3. **PS hook** g₅^(C) = g₅^(L) = g₅^PS (§2.2) — SURVIVES as [P]
4. **Brane perturbation structure** (§6) — SURVIVES as framework
5. **Route A/C formulas** — SURVIVE as algebraic identities;
   FAIL as physical determinations of g₅

### 8.3 What must be updated

1. v56 should note that Route A/C are ruled out numerically
   (they predict α₃ ~ 10⁻¹² instead of 0.118)
2. The formula α₃ = 1/σ̃ should be flagged as structurally
   dependent on Route A assumptions that fail
3. OPR-31 (σ̃ enhancement) is rendered MOOT — the problem
   was an artefact of Route A/C assumptions

### 8.4 Updated BLOCK-004 parameter status

| Parameter | Old status | New status | How determined |
|-----------|-----------|------------|----------------|
| g₅^(C) | From Route A/C | FREE [P] | α_s(M_Z) = 0.118 |
| σ̃ | From α₃ = 1/σ̃ | = 1 [Der] | RS fine-tuning (v68), Λ₄ constraint |
| α₃(μ*) | = 1/σ̃ | = α_s(M_Z) [BL] | Direct input |
| β | = σ̃⁴ (consistency) | From v29 dynamics [Dc] | Independent of gauge coupling |
| L | = π/M_Z | = π/M_Z [I]+[BL] | Unchanged |
| M₅ | = (M̄_Pl²/L)^{1/3} | = (M̄_Pl²/L)^{1/3} [I] | Unchanged |

---

## 9. Epistemic Status

| Claim | Tag | Source |
|-------|-----|--------|
| Route A gives α₃ = 5.2×10⁻¹² | [Der]+[BL] | This analysis, §2 |
| Route C (σ^{1/4} cutoff) gives α₃ ~ 10⁻⁸ | [Der]+[BL] | This analysis, §3 |
| Route C (π/L cutoff) has free c_C | [Der] | v36, this analysis §3 |
| Membrane formula uses postulated r_e | [P] | edc_book_2 ch11 |
| No EDC axiom constrains g₅^(C) | [Der] | This analysis, §4-5 |
| g₅² ~ L with undetermined O(1) coefficient | [Der] | This analysis, §5 |
| g₅^(C)² = 0.051 GeV⁻¹ from α_s(M_Z) | [BL] | Standard KK reduction |
| α₃ = 1/σ̃ requires Route A (which fails) | [Der] | This analysis, §8 |
| σ̃ = 1 from RS + Λ₄ | [Der]+[BL] | COSMOLOGICAL_CONSTANT_SIGMA_TILDE |
| OPR-31 is moot | [Der] | This analysis, §8 |

---

## 10. Guard Compliance

| Check | Status |
|-------|--------|
| All routes tested honestly (not cherry-picked) | PASS |
| Numerical evaluations use correct inputs | PASS |
| Layer A/B separation maintained | PASS |
| Anti-circularity verified (§5.4) | PASS |
| v36, v47, v56 cited accurately | PASS |
| No strawmanning of Route A/C | PASS — formulas reproduced exactly |
| Failure acknowledged without excuse | PASS |
| CC problem not claimed solved | PASS |

---

**Sealed: g₅^(C) is an irreducible free parameter of EDC, requiring one
gauge coupling measurement (α_s(M_Z)) as input. Routes A and C from v56
fail numerically by 7–10 orders of magnitude. The formula α₃ = 1/σ̃ is
an artefact of these failed routes. With g₅^(C) as free, σ̃ = 1 is the
correct structural value, dissolving the σ̃ trilemma.**
