# Warped Geometry Derivation of C in T_* = C·M₅³

**Date:** 2026-03-15
**Branch:** `archive/nuclear-topology-discovery`
**Program:** Prove-or-fail derivation of geometric coefficient C
**Anti-circularity:** Enforced (no G_N^obs, α, m_e, r_e, M_Z, σ̃ = 100)
**Governing document:** `edc_book_4/audit/COSMOLOGY_LANE_REPORT.md` (commit `cf93bcf`)

---

## 1. Executive Verdict

**FAIL — C is not determinable as a pure number in any of the three ansätze.**

In all three cases, C depends on the ratio k/M₅ (equivalently Λ₅/M₅⁵), which is a
free parameter of the 5D gravity model. No EDC constraint fixes this ratio without
introducing forbidden inputs or circular logic.

Moreover, a numerical exercise using allowed inputs (σ from nuclear calibration,
M̄_Pl from observation) shows that σ̃ = σ/(C·M₅³) is hierarchically small
(σ̃ ~ 10⁻¹⁸ for C = O(1)), reflecting the hierarchy between nuclear and gravitational
scales. The claimed value σ̃ = 100 is incompatible with standard 5D warped/compact
geometry given these inputs.

| Ansatz | C determinate? | Failure mode |
|--------|---------------|--------------|
| 1. Flat compact (Λ₅ = 0) | **No** | σ = 0 required for flat 4D; trivial |
| 2. RS I (two branes) | **No** | C = σκ₅²/(6k) depends on free k |
| 3. RS II (one brane) | **No** | Same junction physics as RS I |

**Epistemic tag: [NEGATIVE]** — This is a no-go result analogous to v4 (σ+ρ_P+R_ξ
insufficient) and v11 (σ underivable from EDC alone).

---

## 2. Ansatz 1 — Flat Compact (Λ₅ = 0)

### 2.1 Metric

```
ds² = η_μν dx^μ dx^ν + dξ²
```

with ξ ∈ [0, πR_ξ] (S¹/Z₂ orbifold, brane at ξ = 0).
Bulk cosmological constant Λ₅ = 0.

### 2.2 Bulk Einstein Equations

With Λ₅ = 0 and no sources in the bulk, the 5D Einstein equations reduce to:

```
R_AB^(5) = 0
```

The flat metric ds² = η_μν dx^μ dx^ν + dξ² trivially satisfies this.

### 2.3 Israel Junction Conditions

For a brane with tension σ at ξ = 0, the Israel junction condition gives:

```
[K_μν] = -κ₅² (S_μν - (1/3) g_μν S)
```

For pure tension brane S_μν = -σ g_μν, S = -4σ:

```
[K_μν] = -(κ₅² σ / 3) g_μν
```

With Z₂ symmetry:

```
K_μν⁺ = -(κ₅² σ / 6) g_μν
```

### 2.4 Consistency Problem

For the flat metric, the extrinsic curvature of any ξ = const surface is:

```
K_μν = -(1/2) ∂_ξ g_μν = 0
```

since g_μν = η_μν is independent of ξ.

The junction condition then requires:

```
0 = -(κ₅² σ / 6) g_μν
```

**This forces σ = 0.** A flat compact extra dimension with Λ₅ = 0 cannot support
a nonzero brane tension while maintaining flat 4D spacetime. A nonzero σ would
source curvature (the brane would be de Sitter/anti-de Sitter).

### 2.5 Effective 4D Planck Mass (σ = 0 case)

For σ = 0, the standard KK reduction gives:

```
M̄_Pl² = M₅³ · L       where L = πR_ξ (orbifold length)
```

**[I]** Dimensional check: [M₅³ · L] = [M]³ · [M]⁻¹ = [M]² = [M̄_Pl²] ✓

This gives: M₅³ = M̄_Pl² / (πR_ξ)

### 2.6 C Extraction

With σ = 0, T_* = C · M₅³ is formally defined but σ̃ = σ/T_* = 0/T_* = 0.

If we set C = 1, then T_* = M₅³ = M̄_Pl²/(πR_ξ). This is the unique natural
tension scale in the flat case. But σ̃ = 0 is trivial.

### 2.7 Ansatz 1 Verdict

**FAIL.** The flat compact ansatz is inconsistent with nonzero brane tension for
flat 4D spacetime. The question of C for σ̃ = σ/T_* is moot because σ = 0.

**Tag: [Dc]** — The result (σ = 0 forced by flatness) follows rigorously from
the junction condition.

---

## 3. Ansatz 2 — RS I (Two Branes)

### 3.1 Metric

```
ds² = e^{-2k|y|} η_μν dx^μ dx^ν + dy²
```

with y ∈ [0, πR_c], branes at y = 0 (UV/Planck brane) and y = πR_c (IR brane).
Z₂ orbifold symmetry at both branes.
Bulk cosmological constant Λ₅ < 0 (AdS₅).

### 3.2 Bulk Einstein Equations

The 5D Einstein-Hilbert action with cosmological constant:

```
S_bulk = ∫ d⁵x √{-G} [ R₅/(2κ₅²) - Λ₅ ]
```

For the warped ansatz, the (μν) components of the Einstein equation give
(away from the branes):

```
6 A'² = -κ₅² Λ₅        (Λ₅ < 0 → A'² > 0)
```

where A(y) = k|y| is the warp factor. This defines the AdS curvature scale:

```
k = √(-κ₅² Λ₅ / 6)
```

**[I]** Dimensional check:

```
[κ₅²] = [M]⁻³,  [Λ₅] = [M]⁵  (action convention)
[κ₅² Λ₅] = [M]²
[k] = [M]¹ ✓  (inverse length)
```

**[Dc]** Note on Λ₅ dimensions: In the action S_bulk = ∫d⁵x √{-G} (R₅/(2κ₅²) - Λ₅),
the Lagrangian density has [M]⁵, so [Λ₅] = [M]⁵. This differs from the
Einstein-equation convention where [Λ₅] = [M]². We use the action convention throughout.

### 3.3 Israel Junction Conditions at UV Brane (y = 0)

For the warp factor A(y) = k|y|, the extrinsic curvature of the y = 0⁺ surface is:

```
K_μν = -(1/2) ∂_y g_μν = A'(0⁺) · g_μν(0) = k · η_μν
```

(using the convention K_μν = A' g_μν for the outward-pointing normal.)

With Z₂ symmetry, [K_μν] = 2K_μν⁺:

```
[K_μν] = 2k g_μν
```

From the Israel equation [K_μν] = -κ₅²(S_μν - (1/3)Sg_μν) with S_μν = -σ g_μν:

```
2k g_μν = -(κ₅² σ / 3) g_μν
```

This gives:

```
σ_UV = -6k / κ₅²
```

The sign depends on the orientation convention. Using the RS convention where the
UV brane has positive tension:

```
σ_UV = 6k / κ₅² = 6k M₅³ / (8π) = (3/4π) k M₅³
```

**[I]** Dimensional check:

```
[k / κ₅²] = [M]¹ / [M]⁻³ = [M]⁴
```

**Dimensional tension.** This is the 3-brane tension with [σ_brane] = [M]⁴.

**Important:** The EDC brane tension σ_EDC = 8.82 MeV/fm² has dimensions [M]³
(energy per 2-area). The gravitational brane tension σ_brane has [M]⁴
(energy per 3-volume, appropriate for a 3-brane in 5D). These differ by one
power of mass:

```
[σ_brane] = [M]⁴ ≠ [σ_EDC] = [M]³
```

This dimensional mismatch between the EDC membrane tension and the standard
3-brane tension in 5D gravity is itself a structural issue that must be resolved
before σ̃ = σ/T_* can be meaningfully computed. (See §5.3.)

### 3.4 RS Fine-Tuning Condition

The RS solution requires exact cancellation between bulk and brane contributions
to achieve flat 4D spacetime. The brane tensions are completely determined:

```
σ_UV = 6k / κ₅²       (UV brane, positive tension)
σ_IR = -6k / κ₅²      (IR brane, negative tension)
```

**[Dc]** This is a fine-tuning condition, not a dynamical determination. The brane
tension is not predicted — rather, flatness of 4D spacetime requires this specific
relationship between σ, k, and κ₅².

### 3.5 Effective 4D Planck Mass

Integrating the graviton zero-mode over the compact dimension:

```
M̄_Pl² = c_norm · (M₅³ / k) · (1 - e^{-2kπR_c})
```

where c_norm is a numerical constant depending on the action normalization convention
(c_norm = 1/(256π²) in the convention κ₅² = 8π/M₅³ with the standard RS action;
the exact value does not affect the structural argument).

For kπR_c ≫ 1 (hierarchy regime):

```
M̄_Pl² ≈ c_norm · M₅³ / k
```

### 3.6 C Extraction

From the fine-tuning: σ_brane = 6k/κ₅² = (3/4π) k M₅³

Define T_* = C · M₅³. Then:

```
σ̃ = σ_brane / T_* = σ_brane / (C · M₅³) = (3k) / (4πC)
```

**C is not a pure number.** The ratio σ̃ depends on k, which is set by Λ₅:

```
k = √(-κ₅² Λ₅ / 6)
```

Λ₅ is a free parameter of the model. No EDC postulate or constraint fixes Λ₅.

### 3.7 Numerical Exercise (Anti-Circularity Maintained)

Using only allowed inputs:
- σ_EDC = 8.82 MeV/fm² ≈ 0.343 GeV³ [Cal]
- M̄_Pl = 2.435 × 10¹⁸ GeV [U]

From the two RS relations (ignoring O(1) convention factors, using ~ for
order-of-magnitude):

```
σ_brane ~ k M₅³          (fine-tuning)
M̄_Pl²  ~ M₅³ / k         (KK reduction)
```

Eliminating M₅:

```
σ_brane ~ k · (M̄_Pl² k) = M̄_Pl² k²
→ k ~ √(σ_brane / M̄_Pl²)
```

**Dimensional note:** To use σ_EDC ([M]³) in the RS fine-tuning ([M]⁴), we need
a conversion. Setting σ_brane = σ_EDC · μ where μ is some mass scale, or
alternatively recognizing that σ_brane and σ_EDC may refer to the same physical
quantity with different dimensional conventions. For the order-of-magnitude
estimate, we use σ_EDC³ ~ σ_brane⁴/μ⁴... the dimensional mismatch prevents a
clean numerical computation.

**Even ignoring the dimensional issue** and setting σ ~ 0.343 GeV³ naively:

```
k ~ √(σ / M̄_Pl²) ~ √(0.343 / 5.93 × 10³⁶) ~ √(5.8 × 10⁻³⁸) ~ 10⁻¹⁹ GeV
M₅³ ~ M̄_Pl² k ~ 5.93 × 10³⁶ × 10⁻¹⁹ ~ 10¹⁷ GeV³
```

With C = 1: T_* ~ M₅³ ~ 10¹⁷ GeV³

```
σ̃ = σ / T_* ~ 0.343 / 10¹⁷ ~ 10⁻¹⁸
```

**σ̃ ~ 10⁻¹⁸, not 100.** Off by 20 orders of magnitude.

This is the hierarchy problem: σ_EDC is a nuclear-scale tension (~MeV/fm²),
while M₅³ is a Planck-scale tension. Their ratio is necessarily tiny.

To get σ̃ = 100 would require C ~ 10⁻²⁰, which is not O(1) and would itself
require explanation (it IS the hierarchy).

### 3.8 Ansatz 2 Verdict

**FAIL.** Two independent reasons:

1. **C depends on k** (a free parameter set by Λ₅). It is not a pure geometric
   number.

2. **Even with k eliminated** using the KK relation, the resulting σ̃ reflects
   the hierarchy between nuclear and Planck scales: σ̃ ~ 10⁻¹⁸ ≪ 100.
   Getting σ̃ = 100 would require C ~ 10⁻²⁰.

**Tag: [NEGATIVE]** — The RS framework cannot produce σ̃ = 100 with O(1) geometric
coefficient C, given σ = 8.82 MeV/fm² and M̄_Pl from observation.

---

## 4. Ansatz 3 — RS II (One Brane)

### 4.1 Metric

```
ds² = e^{-2k|y|} η_μν dx^μ dx^ν + dy²
```

with y ∈ (-∞, +∞), single brane at y = 0. Z₂ symmetry.
Bulk: AdS₅ with Λ₅ < 0. No second brane.

### 4.2 Bulk Einstein Equations

Identical to Ansatz 2:

```
k = √(-κ₅² Λ₅ / 6)
```

### 4.3 Israel Junction Conditions

Identical to the UV brane in Ansatz 2 (same local geometry at y = 0):

```
σ = 6k / κ₅²
```

The fine-tuning condition is the same as RS I.

### 4.4 Effective 4D Planck Mass

In RS II, the extra dimension is non-compact (infinite). The 4D graviton is
a normalizable zero mode bound to the brane by the warp factor:

```
M̄_Pl² = c_norm · M₅³ / k
```

(This is the kπR_c → ∞ limit of the RS I formula, giving the same result.)

### 4.5 C Extraction

The analysis is identical to Ansatz 2:

```
σ̃ = σ / (C · M₅³) = (3k) / (4πC)
```

C depends on k. With k eliminated via M̄_Pl² ~ M₅³/k:

```
σ̃ ~ σ / M₅³ ~ 10⁻¹⁸   (for C = O(1))
```

### 4.6 RS II Specific Feature

In RS II, the AdS curvature scale k can in principle be related to the bulk
cosmological constant via:

```
k = √(-Λ₅ / (6M₅³))     (using κ₅² = 8π/M₅³)
```

But Λ₅ remains a free parameter. The RS II model does not determine k any
more than RS I does.

**Known RS literature result:** In RS II, the effective 4D cosmological constant
vanishes by fine-tuning when σ = 6k/κ₅². This is the same fine-tuning as RS I,
not a prediction.

### 4.7 Ansatz 3 Verdict

**FAIL.** Same failure modes as Ansatz 2:

1. C depends on k (free parameter)
2. σ̃ ~ 10⁻¹⁸ for C = O(1)

**Tag: [NEGATIVE]**

---

## 5. C Value Assessment

### 5.1 Summary of All Three Ansätze

| Ansatz | C expression | Free parameters | σ̃ (C = 1) | Verdict |
|--------|-------------|-----------------|-----------|---------|
| 1. Flat (Λ₅=0) | C = 1 (trivial) | — | 0 (forced) | FAIL: σ = 0 |
| 2. RS I | C = 3k/(4πσ̃) | k (from Λ₅) | ~10⁻¹⁸ | FAIL: C not pure |
| 3. RS II | C = 3k/(4πσ̃) | k (from Λ₅) | ~10⁻¹⁸ | FAIL: C not pure |

### 5.2 Root Cause: The Hierarchy

The fundamental obstacle is the hierarchy between the nuclear scale (σ_EDC) and
the gravitational scale (M₅³):

```
σ_EDC ~ 0.3 GeV³       (nuclear/membrane tension)
M₅³   ~ 10¹⁷ GeV³      (5D Planck scale, in RS framework)
Ratio ~ 10⁻¹⁸
```

This ratio IS the gauge hierarchy problem. No standard 5D warped geometry can
produce σ̃ = O(100) because that would require the brane tension to be ~100×
the gravitational scale — but the nuclear-scale tension is 10¹⁸ times SMALLER
than the gravitational scale.

**The value σ̃ = 100 would require the 5D Planck mass to be at the nuclear scale:**

```
σ̃ = 100 → T_* = σ/100 → C·M₅³ = σ/100
For C = 1: M₅³ = 3.43 × 10⁻³ GeV³ → M₅ ≈ 150 MeV
```

An M₅ ~ 150 MeV (nuclear scale) is excluded by gravitational experiments:
it would require a compact dimension of size L ~ M̄_Pl²/M₅³ ~ 10³⁹ GeV⁻¹ ~ 10²³ m
(~36 million light-years), far exceeding experimental bounds on extra dimensions
(L < 0.1 mm from gravitational force tests).

### 5.3 Dimensional Mismatch Issue

A structural issue emerged during the derivation: the EDC brane tension σ_EDC
has dimensions [M]³ (energy per 2D area), while the standard 3-brane tension
in 5D gravity has dimensions [M]⁴ (energy per 3D volume). These are related by:

```
σ_brane = σ_EDC · μ
```

where μ is some mass scale with [μ] = [M]¹. The identification of μ requires
specifying how the EDC membrane (described as a 2D surface tension) maps onto the
gravitational 3-brane. This mapping is not provided in the existing EDC documents.

This dimensional mismatch is an additional obstacle to computing σ̃, independent
of the C-determination problem.

### 5.4 What Would Be Needed

For C to be a pure number, one would need either:

1. **An additional EDC constraint fixing k/M₅** — e.g., a postulate or derivation
   that determines Λ₅ in terms of M₅. No such constraint exists in P1–P6.

2. **A non-standard geometry** where the warp factor structure differs from RS
   and produces a scale-free junction condition. No such geometry is known.

3. **A dynamical mechanism** that selects a specific k (analogous to moduli
   stabilization in string theory). This would introduce new physics beyond
   the three ansätze tested.

4. **Resolution of the dimensional mismatch** — if σ_EDC ([M]³) and σ_brane ([M]⁴)
   are identified through a specific geometric mechanism (e.g., σ_brane = σ_EDC · R_ξ⁻¹
   or similar), this could modify the numerical estimate. But it would not eliminate
   the hierarchy.

---

## 6. σ̃ Computation

**C was not determined. This section reports the conditional results.**

### 6.1 If C = 1 (Natural Scale)

```
T_* = M₅³ ~ 10¹⁷ GeV³
σ̃ = σ_EDC / T_* ~ 0.343 / 10¹⁷ ~ 10⁻¹⁸
```

### 6.2 If σ̃ = 100 (Working Backwards)

```
T_* = σ_EDC / 100 = 3.43 × 10⁻³ GeV³
C = T_* / M₅³ = 3.43 × 10⁻³ / 10¹⁷ = 3.4 × 10⁻²⁰
```

This C ~ 10⁻²⁰ is not O(1). It encodes the hierarchy.

### 6.3 If M₅ is at Nuclear Scale (Avoiding Hierarchy)

```
M₅ ~ 150 MeV → M₅³ ~ 3.4 × 10⁻³ GeV³
C = 1 → T_* = 3.4 × 10⁻³ GeV³ → σ̃ = 100
```

But then: L = M̄_Pl²/M₅³ ~ 10³⁹ GeV⁻¹ ~ 10²³ m.
**Excluded** by gravitational inverse-square-law tests (L < 37 μm for n = 1).

### 6.4 Provisional Assessment

The value σ̃ = 100 in `sigma_tilde_value.json` is not derivable from standard
5D warped geometry with the allowed inputs (σ_EDC = 8.82 MeV/fm², M̄_Pl).

Possible origins of the claimed value:
1. **Phenomenological requirement:** α₃ = 1/σ̃ ≈ 0.01, matching the strong
   coupling at a GUT-like scale. This would make σ̃ = 100 a [Cal] value, not [D].
2. **Different definition of T_*:** If T_* is defined at a scale other than M₅³
   (e.g., involving the EW scale or nuclear scale directly), the ratio could differ.
3. **Non-gravitational origin:** If σ̃ is determined by non-gravitational physics
   (e.g., gauge coupling unification constraints), the warped geometry ansatz
   is the wrong tool.

---

## 7. Epistemic Status

### 7.1 Results Table

| Result | Tag | Confidence |
|--------|-----|-----------|
| Flat ansatz forces σ = 0 | [Dc] | Rigorous (junction + flatness) |
| RS fine-tuning: σ = 6k/κ₅² | [Dc] | Standard RS result |
| C depends on k (not a pure number) | [Dc] | Follows from fine-tuning |
| σ̃ ~ 10⁻¹⁸ for C = O(1) | [Dc] | Hierarchy argument |
| σ̃ = 100 incompatible with standard 5D + allowed inputs | **[NEGATIVE]** | Strong |
| Dimensional mismatch σ_EDC vs σ_brane | [I] | Identified, not resolved |
| σ̃ = 100 may be [Cal] (from α₃ ≈ 0.01 requirement) | [I] | Hypothesis |

### 7.2 Anti-Circularity Verification

| Forbidden input | Used? | Verification |
|----------------|-------|-------------|
| G_N^obs | **No** | M̄_Pl used as [U] (universal constant, allowed) |
| α (fine structure) | **No** | Not invoked |
| m_e, r_e | **No** | Not invoked |
| M_Z | **No** | Not invoked |
| σ̃ = 100 | **No** | Used only in §6.2 as back-calculation |

### 7.3 Classification

This result is a **NEGATIVE** — a no-go theorem for deriving C as a pure number
from standard 5D warped geometry. It joins:

- **v4 NEGATIVE:** σ + ρ_P + R_ξ insufficient to close BLOCK-003
- **v11 NEGATIVE:** σ underivable from EDC alone
- **v16-A NEGATIVE:** R_ξ underivable internally

The new negative result:

- **C-derivation NEGATIVE:** C in T_* = C·M₅³ is not a pure number; σ̃ = 100
  is incompatible with standard 5D gravity + nuclear-scale σ + observed M̄_Pl.

---

## 8. What Remains Open

### 8.1 Immediate Open Problems

1. **Dimensional mismatch:** Resolve [σ_EDC] = [M]³ vs [σ_brane] = [M]⁴.
   The EDC "membrane tension" and the 5D gravitational "brane tension" have
   different dimensions. How they relate is not documented.

2. **Origin of σ̃ = 100:** If not from warped geometry, where does this value
   come from? The most likely source is phenomenological (α₃ = 1/σ̃ → σ̃ = 1/α₃),
   which would make it [Cal], not [D].

3. **What T_* actually is in EDC:** The cosmology lane defines T_* = C·M₅³, but
   if C is not O(1), then T_* is not naturally the 5D gravitational tension scale.
   What physical scale does T_* represent?

### 8.2 Paths Forward

| Path | What it would achieve | Difficulty |
|------|----------------------|-----------|
| Fix Λ₅ from EDC postulates | Determine k → fix C | Requires new postulate or derivation |
| Derive σ̃ from gauge unification (non-gravitational) | Bypass warped geometry entirely | May be the correct approach (v56 direction) |
| Resolve σ_EDC ↔ σ_brane dimensional map | Enable clean numerical calculation | Requires geometric analysis |
| Accept σ̃ = 100 as [Cal] and tag honestly | No new physics needed | Epistemic correction only |
| Large extra dimensions (ADD-type) with M₅ ~ TeV | Could reduce hierarchy | Requires n ≥ 2 extra dimensions |

### 8.3 Structural Implications

The failure to derive C suggests that the cosmology lane's approach — defining σ̃
through 5D gravitational geometry — may be targeting the wrong physics. The
σ̃ = 100 value, if genuine, likely originates from:

- **Gauge coupling unification** (α₃ = 1/σ̃ at unification scale)
- **Pati-Salam embedding** (sin²θ_W = 5/12 constraints from BLOCK-003)
- **Non-gravitational brane dynamics** (e.g., DBI action, gauge-gravity duality)

rather than from the 5D Einstein-Hilbert action and Israel junction conditions.

The cosmology lane may need to be re-routed: instead of
"5D gravity → T_* → σ̃", the chain may be
"gauge unification + EDC postulates → α₃ → σ̃ = 1/α₃".

### 8.4 Recommendation

1. **Re-tag σ̃ = 100 as [I] or [Cal]** in `sigma_tilde_value.json`.
   The "DERIVED" status and "PHYSICAL_DERIVATION" provenance are not supported.

2. **Investigate the gauge-coupling route** for σ̃. The v56 derivation
   (5D gauge coupling fixing) may provide a non-gravitational determination
   of σ̃ that avoids the hierarchy problem.

3. **Document the dimensional mismatch** as a formal open problem (OPR).
   The relationship between σ_EDC ([M]³) and σ_brane ([M]⁴) must be resolved
   for the cosmology lane to connect to the nuclear calibration.

---

## Appendix A: Conventions Used

| Symbol | Definition | Dimension | Source |
|--------|-----------|-----------|--------|
| κ₅² | 8π/M₅³ = 8πG₅ | [M]⁻³ | TSTAR_DERIVATION_5D.md §1.2 |
| M₅ | 5D Planck mass | [M]¹ | Standard |
| M̄_Pl | Reduced 4D Planck mass = 2.435 × 10¹⁸ GeV | [M]¹ | PDG [U] |
| σ_EDC | EDC membrane tension = 8.82 MeV/fm² | [M]³ | Nuclear calibration [Cal] |
| σ_brane | 3-brane tension in 5D gravity | [M]⁴ | RS framework |
| Λ₅ | 5D cosmological constant (action convention) | [M]⁵ | Free parameter |
| k | AdS curvature scale = √(-κ₅²Λ₅/6) | [M]¹ | Derived from Λ₅ |
| R_c | Compact dimension radius (RS I) | [M]⁻¹ | Free parameter |
| C | Geometric coefficient in T_* = C·M₅³ | dimensionless | Target of derivation |

## Appendix B: Unit Conversions

```
σ_EDC = 8.82 MeV/fm²
      = 8.82 MeV × (197.3 MeV)² / fm² × fm²   [using 1 fm⁻¹ = 197.3 MeV]
      = 8.82 × 38,927 MeV³
      = 343,337 MeV³
      ≈ 0.343 GeV³

M̄_Pl = 2.435 × 10¹⁸ GeV
M̄_Pl² = 5.929 × 10³⁶ GeV²

σ_EDC / M̄_Pl² = 0.343 / (5.929 × 10³⁶) ≈ 5.8 × 10⁻³⁸ GeV
```
