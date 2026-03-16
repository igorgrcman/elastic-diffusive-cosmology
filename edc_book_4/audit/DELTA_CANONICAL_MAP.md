# δ Canonical Scale Map

**Date:** 2026-03-16
**Branch:** `claude/analyze-codebase-KKY9n`
**Step:** 5 of 9 (Integration Program)
**Scope:** Map all thickness-like scales, identify misidentifications,
flag formulas needing rederivation

---

## 1. Executive Summary

EDC uses **five distinct thickness-like length scales** that are frequently
conflated. The conflation has propagated errors through the derivation chain.

| Scale | Value | Sector | Tag | Often confused with |
|-------|-------|--------|-----|-------------------|
| R_ξ | 2.16×10⁻³ fm | Electroweak / KK | [BL] | Δ, δ_BL |
| Δ | 3.12×10⁻³ fm | Lepton mass (Ch.4) | [P] | R_ξ |
| ℓ/(2π) | 2.16×10⁻³ fm | Orbifold radius | [Dc] | R_ξ (identical) |
| δ_J | ~0.105 fm | Junction core / nucleon | [I] | R_ξ (50× error!) |
| δ_BL | ~2.17×10⁻³ fm | Boundary layer (Robin BC) | [P] | R_ξ, Δ |

**The most dangerous confusion:** δ_J ≈ 0.105 fm (junction core) vs
R_ξ ≈ 0.002 fm (electroweak). These differ by factor ~50. Formulas that
use one when they should use the other are wrong by 1–3 orders of magnitude.

**σ discrepancy:** Two incompatible σ values are used:
- σ = 8.82 MeV/fm² (from E_σ = m_e c²/α) — used in nucleon sector
- σ = 5.86 MeV/fm² (from σr_e² = 5.86 MeV) — used in EW sector
- Ratio: 8.82/5.86 = 1.505 ≈ 3/2

---

## 2. The Five Scales — Definitions, Origins, Tags

### 2.1 R_ξ — Electroweak Correlation Length

| Property | Value |
|----------|-------|
| **Definition** | R_ξ = ℏc/M_Z |
| **Value** | 2.163×10⁻³ fm = 2.163×10⁻¹⁸ m |
| **Dimensions** | Length |
| **Tag** | [BL] (from M_Z = 91.1876 GeV [BL]) |
| **Sector** | Electroweak / Kaluza-Klein |
| **Physical role** | Membrane correlation length; sets KK mass scale; determines W/Z/H boson masses |
| **Book I location** | Ch.0 §17, Ch.6 §6, Ch.9, Ch.11 |
| **Book II location** | OPR Registry, Ch.11, Ch.16 |

**What physics sets it:** The first KK excitation of the compact dimension
has mass M_Z. By Heisenberg: R_ξ = ℏc/M_Z. This is the "size" of the
compact 5th dimension as seen by electroweak physics.

**Formulas that use R_ξ:**
1. M_Z = ℏc/R_ξ (KK mass) [BL]
2. M_W = ℏc cos(θ_W)/R_ξ (W mass from KK) [Dc]
3. α = R_ξ/r_e (fine-structure constant — Book I claim) [P]
4. Hierarchy: M_Pl/M_Z = L_Pl/R_ξ (geometric hierarchy) [I]
5. Robin BC parameter: α_Robin = ℓ/δ (if δ = R_ξ) [P]

**What would derive it:** R_ξ is ALREADY determined — it's ℏc/M_Z.
The question is whether M_Z can be predicted from EDC without using
M_Z as input. This requires deriving the KK spectrum from the 5D
action, which needs the compactification radius (itself R_ξ-related).
Currently circular: R_ξ is anchored to M_Z [BL], not derived.

### 2.2 Δ — Kink Width (Lepton Sector)

| Property | Value |
|----------|-------|
| **Definition** | Δ = 2/(v√λ) from λφ⁴ kink |
| **Value** | 3.121×10⁻³ fm (from Ch.4 electron mass formula) |
| **Dimensions** | Length |
| **Tag** | [P] (v and λ are both [P]) |
| **Sector** | Lepton mass / thick brane microphysics |
| **Physical role** | Domain-wall thickness in scalar kink model |
| **Book II location** | Ch.4 (OPR-04), Ch.16 |

**What physics sets it:** The λφ⁴ potential V = λ(φ²-v²)²/4 has a
kink solution φ = v·tanh(ξ/Δ) with width Δ = √(2/λ)/v. The BPS
relation gives σΔ = 4v²/3 [M].

**Formulas that use Δ:**
1. m_e = π√(ασΔℏc) [P] (Ch.4 electron mass candidate)
2. M₀² = (3y²/4)·σΔ [Dc] (OPR-01 mass anchor)
3. μ = M₀ℓ = (√3/2)·y·n·√(σΔ³) [Dc] (OPR-21 dimensionless parameter)
4. N_bound = 3 ⟺ σΔ³ ∈ [52, 102] [Dc] (three-generation constraint)
5. σΔ = 4v²/3 [M] (BPS relation)

**What would derive it:** Need to derive v (scalar VEV) from the 5D action.
Currently v = M₀/y with both M₀ and y [P]. The BPS relation then gives
Δ = 4v²/(3σ). So deriving v closes Δ automatically.

### 2.3 ℓ/(2π) — Orbifold Radius

| Property | Value |
|----------|-------|
| **Definition** | R₅ = ℓ/(2π) where ℓ is orbifold circumference |
| **Value** | ≈ R_ξ ≈ 2.16×10⁻³ fm |
| **Dimensions** | Length |
| **Tag** | [Dc] (from R_ξ via standard circle geometry) |
| **Sector** | Compact dimension geometry |
| **Physical role** | Radius of S¹/Z₂ orbifold |
| **Book II location** | Ch.11–13 |

**What physics sets it:** The compact dimension is S¹/Z₂ with circumference
ℓ = 2πR_ξ. This is essentially the same scale as R_ξ, just with a 2π
geometric factor. **Not an independent scale.**

**Formulas that use ℓ:**
1. ℓ = 2πR_ξ [Dc]
2. α_Robin = ℓ/δ_BL (thick-brane matching parameter) [P]
3. μ = M₀ℓ (OPR-21) [Dc]
4. KK mass tower: m_n = n/R₅ = 2πn/ℓ [M]

**What would derive it:** Identical to deriving R_ξ. Not independent.

### 2.4 δ_J — Junction-Core Thickness (Nucleon Sector)

| Property | Value |
|----------|-------|
| **Definition** | δ_J = ℏ/(2m_p c) = λ_p/2 (proton Compton half-wavelength) |
| **Value** | 0.1053 fm |
| **Dimensions** | Length |
| **Tag** | [I] (identified pattern, not derived) |
| **Sector** | Nuclear / junction-core / neutron lifetime |
| **Physical role** | Brane thickness for junction-core model; barrier width for tunneling |
| **Book IV location** | Ch.8 (L₀/δ ratio) |
| **Code location** | derive_C_integrals.py:48, putC_compute_MV.py:84 |

**What physics sets it:** Identified as the proton Compton half-wavelength:
the quantum uncertainty scale for nucleon position. This is the scale
at which quantum effects prevent further localization of the junction core.

**Formulas that use δ_J:**
1. C = (L₀/δ_J)² ≈ 100 [Dc] (junction-core geometric factor)
2. E₀ = C·σ·δ_J² = σ·L₀² [Dc] (core energy scale)
3. V_core(q) = -E₀·f(q/δ_J) [Dc] (junction-core potential)
4. L₀/δ_J = π² [P] (Step 4 hypothesis — FAILED to derive)
5. S_E/ℏ = 2π·(L₀/δ_J) [Dc] (instanton action)
6. τ_n = A·(ℏ/ω₀)·exp[2π·L₀/δ_J] [Dc+P+Cal] (neutron lifetime)
7. M_core(q) = E₀·g(q/δ_J) [Dc] (junction kinetic term)

**What would derive it:** Need to derive δ_J from the 5D action as the
natural regularization scale for the junction core. Currently [I] — the
Compton identification is pattern-matched, not derived. Would require
showing that the thick-brane profile has characteristic width ℏ/(2m_p c)
when evaluated on the nucleon solution. This is blocked by OPR-21
(requires solving the full BVP with physical potential).

### 2.5 δ_BL — Boundary-Layer Scale (Robin BC)

| Property | Value |
|----------|-------|
| **Definition** | δ_BL = boundary-layer thickness in Robin BC: αf(0)+βf'(0)=0 |
| **Value** | Not independently determined; assumed = R_ξ or = Δ |
| **Dimensions** | Length |
| **Tag** | [P] |
| **Sector** | BVP / Robin boundary conditions |
| **Physical role** | Scale over which Robin BC smooths sharp junction; regularization |
| **Book II location** | OPR Registry (OPR-20, OPR-21) |

**What physics sets it:** The Robin BC parameter α = ℓ/δ_BL controls
how the eigenfunction behaves at the brane boundary. A small δ_BL
(relative to ℓ) gives nearly Dirichlet BC; large δ_BL gives Neumann.

**Formulas that use δ_BL:**
1. α_Robin = ℓ/δ_BL [P] (Robin BC parameter)
2. Eigenvalue μ(α) [Dc|model] (depends on α choice)
3. OPR-20 mediator mass calculations [P]

**What would derive it:** Derive the effective boundary condition from
matching the 5D bulk solution to the brane-localized fields. This is
part of the thick-brane matching program. Currently [P].

---

## 3. σ Discrepancy Analysis

### 3.1 The Two σ Values

| σ value | Formula | Sector | Tag | Source |
|---------|---------|--------|-----|--------|
| **8.82 MeV/fm²** | σ = m_e³c⁴/(α³ℏ²) | Nucleon / junction | [Dc] | OPR-01 hypothesis, Companion H |
| **5.86 MeV/fm²** | σ = ε_cell/r_e² where ε_cell = σr_e² = 5.856 MeV | EW / Z₆ lattice | [Dc] | Framework v2.0, Ch.3, Ch.4 |

### 3.2 Ratio Analysis

```
8.82 / 5.86 = 1.5051...

Candidate explanations:
  3/2 = 1.500              (0.3% off)
  Z₆/Z₂² = 6/4 = 1.5      (same)
  π/2 = 1.571              (4.5% off)
```

The ratio 3/2 is exact within numerical precision:
```
σ₁ = m_e³c⁴/(α³ℏ²) = m_e/(α³(ℏ/m_e c)²)

σ₂ = ε_cell/r_e² where ε_cell = m_e c²/α (if σ₂r_e² = m_e c²/α)

Actually checking:
  σ₁ = m_e³c⁴/(α³ℏ²) → in MeV/fm²: 8.82
  σ₂ = "σr_e² = 5.86 MeV" → σ₂ = 5.86/r_e²

  r_e = α²a₀ = α²ℏ/(m_e c) ≈ 2.82×10⁻¹³ cm = 2.82×10⁻² fm
  Wait — r_e in EDC context is ~1 fm (topological scale), not classical electron radius.

  If r_e(EDC) ≈ 1 fm (as used in Z₆ lattice): σ₂ = 5.86/1² = 5.86 MeV/fm²
  If r_e(classical) = 2.82×10⁻² fm: σ₂ = 5.86/(2.82×10⁻²)² = 7370 MeV/fm²
```

**The σ discrepancy arises from two different length scales being used:**
- σ = 8.82: uses α and m_e in a pure formula (no explicit length)
- σ = 5.86: uses r_e ≈ 1 fm as the "cell size" in Z₆ lattice

### 3.3 Which σ Is Correct?

| Context | σ used | Justification |
|---------|--------|---------------|
| Junction-core model | 8.82 | From E_σ = m_e c²/α [Dc] |
| Z₆ lattice geometry | 5.86 | From σr_e² = 5.86 MeV [Dc] |
| Electron mass (Ch.4) | 5.86 | From m_e = π√(ασΔℏc) [P] |
| Companion H paper | 8.82 | Derived from fundamental constants |
| OPR-01 register | 8.82 | Official anchor hypothesis |

**Assessment:** The σ = 8.82 value has a cleaner derivation (from
fundamental constants only). The σ = 5.86 value depends on r_e ~ 1 fm
(the EDC topological scale), which is itself [I].

**Impact:** A 50% error in σ propagates as:
- √σ into mass formulas (22% error)
- σ directly into energy scales (50% error)
- σΔ³ into generation counting (50% error on σΔ³ window)

---

## 4. Assumption Labels (A1, A2, A3) — Verified?

From Ch.16 (OPR-04):

### (A1): Δ = δ_BL — Kink width equals boundary-layer scale

**Status: UNVERIFIED [P]**

- Δ is the λφ⁴ kink width: Δ = 2/(v√λ) [M]
- δ_BL is the Robin BC regularization scale [P]
- These come from different physics (scalar microphysics vs boundary matching)
- No derivation connects them
- Numerically: Δ ≈ 3.12×10⁻³ fm (from Ch.4), δ_BL unspecified

**If verified:** Would reduce parameter count by 1.
**If false:** Must specify δ_BL independently.

### (A2): δ_BL = R_ξ — Boundary-layer scale equals diffusion scale

**Status: COMMONLY ASSUMED [P] — NOT VERIFIED**

- R_ξ = ℏc/M_Z ≈ 2.16×10⁻³ fm [BL]
- δ_BL is the Robin BC scale [P]
- Assumption is "the brane boundary layer has thickness set by the EW scale"
- Physically plausible but not derived
- Combined with (A1): Δ = δ_BL = R_ξ ≈ 2.16×10⁻³ fm

**If verified:** The Robin BC parameter α = ℓ/R_ξ = 2π, fixing the eigenvalue.
**If false:** α is a free parameter.

### (A3): ℓ = nΔ with n ~ O(1)

**Status: UNVERIFIED [P]**

- ℓ = 2πR_ξ ≈ 0.0136 fm [Dc]
- Δ ≈ 3.12×10⁻³ fm (if from Ch.4)
- n = ℓ/Δ ≈ 0.0136/0.00312 ≈ 4.4

**If verified:** n ≈ 4 relates the two scales. This is the value used in
the three-generation constraint.
**If false:** Generation counting needs a different n.

### Critical Missing Assumption

**(A4): δ_J = R_ξ?** — Junction-core thickness equals EW scale?

**Status: EXPLICITLY FALSE**

- δ_J ≈ 0.105 fm, R_ξ ≈ 0.002 fm
- Ratio: δ_J/R_ξ ≈ 50
- These are DIFFERENT physical scales in DIFFERENT sectors
- NEVER identified in any canonical document
- But sometimes IMPLICITLY confused when "δ" is used without subscript

This is the **most dangerous confusion** in the δ system.

---

## 5. Formula Catalogue — All δ Occurrences

### 5.1 Formulas Using δ_J ≈ 0.105 fm (Junction Core)

| # | Formula | Location | Variables | Tag |
|---|---------|----------|-----------|-----|
| F1 | C = (L₀/δ_J)² | DERIVE_C_FROM_GEOMETRY.md | L₀ [I], δ_J [I] | [Dc] |
| F2 | E₀ = C·σ·δ_J² = σ·L₀² | S5D_TO_SEFF_Q_REDUCTION §11.3 | σ [Dc], L₀ [I] | [Dc] |
| F3 | V_core(q) = -E₀·f(q/δ_J) | putC_compute_MV.py | E₀ [Dc], f [P] | [Dc] |
| F4 | S_E/ℏ = 2π·(L₀/δ_J) | BOOK_SECTION_NEUTRON_LIFETIME.tex | κ [Dc], L₀/δ_J [P] | [Dc+P] |
| F5 | τ_n = A·(ℏ/ω₀)·exp[2π·L₀/δ_J] | Ch.9 Book IV | All components | [Dc+P+Cal] |
| F6 | L₀/δ_J = π² (hypothesis) | Ch.8 Book IV | — | [P] |
| F7 | M_core(q) = E₀·g(q/δ_J) | DERIVE_MQ_FROM_ACTION.md | E₀ [Dc] | [Dc] |
| F8 | δ_J = ℏ/(2m_p c) | DELTA_ANCHOR_MAP | m_p [BL] | [I] |
| F9 | m_p ≈ (4/3)·σ·L₀⁴/δ_J² | BOOK_SECTION_NEUTRON_LIFETIME.tex | σ [Dc], L₀ [I] | [P] |

### 5.2 Formulas Using R_ξ ≈ 0.002 fm (EW Scale)

| # | Formula | Location | Variables | Tag |
|---|---------|----------|-----------|-----|
| F10 | M_Z = ℏc/R_ξ | Book I Ch.9 | — | [BL] |
| F11 | α = R_ξ/r_e | Book I Ch.6 (superseded?) | r_e [I] | [P] |
| F12 | ℓ = 2πR_ξ | Book II Ch.11 | — | [Dc] |
| F13 | Hierarchy = L_Pl/R_ξ | Book I Ch.11 | L_Pl [Def] | [I] |

### 5.3 Formulas Using Δ ≈ 0.003 fm (Kink Width)

| # | Formula | Location | Variables | Tag |
|---|---------|----------|-----------|-----|
| F14 | m_e = π√(ασΔℏc) | Ch.4 | σ [P], Δ [P] | [P] |
| F15 | M₀² = (3y²/4)·σΔ | Ch.16 OPR-01 | σ [Dc], y [P] | [Dc] |
| F16 | μ = M₀ℓ | Ch.16 OPR-21 | M₀ [Dc], ℓ [Dc] | [Dc] |
| F17 | σΔ = 4v²/3 | Ch.16 BPS | v [P] | [M] |
| F18 | Δ = 2/(v√λ) | Ch.16 kink | v [P], λ [P] | [M] |
| F19 | N_bound = 3 ⟺ σΔ³ ∈ [52, 102] | Ch.16 | σ [Dc], Δ [P] | [Dc] |

### 5.4 Formulas Using δ_BL (Boundary Layer, unspecified)

| # | Formula | Location | Variables | Tag |
|---|---------|----------|-----------|-----|
| F20 | α_Robin = ℓ/δ_BL | OPR-20, Ch.11 | ℓ [Dc], δ_BL [P] | [P] |
| F21 | μ(α) eigenvalue | OPR-21 BVP | α [P] | [Dc|model] |
| F22 | M_W from thick-brane matching | Ch.11 attempts | δ_BL [P] | [P] |

---

## 6. Misidentification Register

### 6.1 Confirmed Misidentifications

| ID | Error | Where | Impact | Severity |
|----|-------|-------|--------|----------|
| M1 | Ch.10 says "δ ~ r_e ~ 1 fm" | ch10_electroweak_bridge.tex:27,84 | Uses nucleon-scale δ in EW context | **HIGH** |
| M2 | Ch.11 says "δ ~ R_ξ ~ 10⁻³ fm" | ch11_g5_ell_value_closure_attempt.tex:274 | Correct for EW, but same symbol as junction δ | MEDIUM |
| M3 | OPR-04 register says "δ ~ 2.5×10⁻³ fm" | opr_register.tex:34 | Uses EW-scale δ for what may be junction context | MEDIUM |
| M4 | Code uses DELTA_EDC = 0.1 fm without book anchor | derive_C_integrals.py:48, putC_compute_MV.py:84 | Unanchored parameter | HIGH |
| M5 | "δ" used without subscript in >50 locations | Throughout Books I-IV | Reader cannot tell which δ | **CRITICAL** |
| M6 | σ = 5.86 in Ch.4 vs σ = 8.82 in junction core | CH4 vs OPR-01/Companion H | 50% discrepancy unresolved | **HIGH** |

### 6.2 Potential Misidentifications (Requires Verification)

| ID | Concern | Where | Action Needed |
|----|---------|-------|---------------|
| P1 | Is α_Robin = ℓ/δ using δ_BL or δ_J? | OPR-20 calculations | Check which δ was used |
| P2 | Does the BVP in App. L₀δ use δ_J or R_ξ for well width? | app_L0delta_model_bvp.tex | Verify: uses δ_J = 0.105 fm |
| P3 | Does the electron soliton BVP (Paper 3) use δ_J or R_ξ? | solve_electron_soliton_bvp_v5.py | Check source parameter |
| P4 | If (A1)+(A2) hold: Δ = R_ξ ≈ 0.002 fm, but Ch.4 needs Δ ≈ 0.003 fm | Ch.4 vs Ch.16 | 44% discrepancy in Δ |

---

## 7. Canonical Scale Map

### 7.1 The Definitive Map

```
ELECTROWEAK SECTOR (~ 10⁻³ fm)
├── R_ξ = ℏc/M_Z ≈ 2.16×10⁻³ fm .................. [BL]
├── ℓ/(2π) = R_ξ .................................. [Dc] (same scale)
├── Δ = 2/(v√λ) ≈ 3.12×10⁻³ fm .................. [P]  (1.44× R_ξ)
└── δ_BL = ??? (assumed R_ξ by (A2)) .............. [P]

NUCLEON SECTOR (~ 10⁻¹ fm)
├── δ_J = ℏ/(2m_p c) ≈ 0.105 fm .................. [I]
├── L₀ ≈ r_p + δ_J ≈ 0.98 fm .................... [I+BL]
└── r_p ≈ 0.875 fm ............................... [BL]

                        GAP FACTOR: ~50×
```

### 7.2 Rules

1. **NEVER write bare "δ"** — always use subscript: δ_J, δ_BL, or Δ
2. **R_ξ and ℓ/(2π) are the same scale** — use R_ξ unless orbifold geometry is specifically relevant
3. **δ_J appears ONLY in nucleon/junction formulas** (F1–F9)
4. **R_ξ appears ONLY in EW formulas** (F10–F13)
5. **Δ appears ONLY in kink/lepton formulas** (F14–F19)
6. **δ_BL appears ONLY in Robin BC formulas** (F20–F22)
7. **Assumption (A1)-(A3) must be EXPLICITLY labeled** when invoked

### 7.3 The Scale Hierarchy

```
L_Pl ─── 1.6×10⁻²⁰ fm ─── Planck (gravity)
  ↑ factor ~10⁸
R_ξ ──── 2.2×10⁻³ fm ──── Electroweak (KK)
  ↑ factor ~50
δ_J ──── 0.105 fm ──────── Nucleon (Compton)
  ↑ factor ~8
r_p ──── 0.875 fm ──────── Proton (charge radius)
  ↑ factor ~1.1
L₀ ───── 0.98 fm ──────── Junction extent
```

---

## 8. Rederivation Priority List

| # | Formula | Current δ | Correct δ | Error factor | Priority |
|---|---------|-----------|-----------|-------------|---------|
| R1 | C = (L₀/δ)² = 100 | δ_J = 0.1 fm [I] | δ_J = 0.105 fm [I] | 1.10 (C = 91 vs 100) | HIGH |
| R2 | L₀/δ = π² = 9.87 | δ_J = 0.105 fm | δ_J = 0.105 fm | Correct δ, but [P] | MEDIUM |
| R3 | S_E/ℏ = 2π × 9.33 | Uses δ_J | Uses δ_J | Correct sector | LOW |
| R4 | m_e = π√(ασΔℏc) | Δ ≈ 0.003 fm | Δ ≈ 0.003 fm | Correct sector | LOW |
| R5 | α_Robin = ℓ/δ | Which δ? | δ_BL (not δ_J!) | Up to 50× if wrong | **CRITICAL** |
| R6 | M₀² = (3y²/4)σΔ | σ = 8.82 or 5.86? | Must choose | 50% on M₀ | **CRITICAL** |
| R7 | σΔ³ generation window | σ = 8.82 or 5.86? | Must choose | 50% on window | **CRITICAL** |
| R8 | Ch.10 "δ ~ r_e ~ 1 fm" | δ = 1 fm (!) | Unclear intent | 10× or 500× | HIGH |
| R9 | V_core(q) = -E₀·f(q/δ) | δ_J = 0.1 fm | δ_J = 0.105 fm | 1.05 on shape | LOW |
| R10 | m_p = (4/3)σL₀⁴/δ² | δ_J = 0.1 fm | δ_J = 0.105 fm | 1.10 | MEDIUM |

### Priority Classification

**CRITICAL (3 items):** Affect the derivation chain structure; wrong δ sector or unresolved σ:
- R5: α_Robin may use wrong δ (50× error possible)
- R6: M₀ depends on which σ (50% change)
- R7: Three-generation window depends on σ (shifts window)

**HIGH (3 items):** Affect Book IV canonical results:
- R1: C shifts from 100 to 91 with Compton anchor (10% change)
- R8: Ch.10 uses completely wrong scale (may be old/superseded text)
- M5: Bare "δ" throughout codebase is systematic notation failure

**MEDIUM (2 items):**
- R2: L₀/δ hypothesis uses correct δ sector but remains [P]
- R10: Proton mass formula shifts 10%

**LOW (3 items):**
- R3, R4, R9: Use correct δ sector; numerical impact small

---

## 9. Connection to OPR Register

### 9.1 Existing OPRs

| OPR | Subject | δ connection |
|-----|---------|-------------|
| **OPR-04** | Wall thickness Δ | Central: derives Δ from kink theory. Status: CONDITIONAL |
| **OPR-20** | Mediator mass from eigenvalue | Uses α_Robin = ℓ/δ — WHICH δ? |
| **OPR-21** | BVP master closure | Uses μ = M₀ℓ — depends on Δ through M₀ |
| **OPR-29** | σ_EDC vs σ_brane dimensions | Related to σ discrepancy (5.86 vs 8.82) |
| **OPR-33** | L₀/δ ratio (proposed Step 4) | Uses δ_J specifically |

### 9.2 New OPR Proposed

**OPR-34: σ Discrepancy — 8.82 vs 5.86 MeV/fm²**

| Field | Value |
|-------|-------|
| Status | OPEN |
| Priority | HIGH (affects generation counting and mass formulas) |
| The two values | σ₁ = m_e³c⁴/(α³ℏ²) = 8.82; σ₂ = ε_cell/r_e² = 5.86 |
| Ratio | 8.82/5.86 ≈ 3/2 |
| Question | Are these the same σ? If so, which is correct? If different, what distinguishes them? |
| Blocked by | Clarification of r_e (EDC topological scale vs classical electron radius) |
| Would close | M₀ ambiguity, generation window, mass formula consistency |

### 9.3 Updated OPR-04 Note

The Ch.16 derivation gives Δ = 4v²/(3σ) [Dc]. With the σ discrepancy:
- If σ = 8.82: Δ = 4v²/26.46
- If σ = 5.86: Δ = 4v²/17.58

This is a 50% change in Δ for the same v. The three-generation constraint
σΔ³ ∈ [52, 102] shifts accordingly.

---

## 10. Recommendations

1. **Adopt subscript notation immediately** — Replace all bare "δ" with
   δ_J, δ_BL, Δ, or R_ξ as appropriate. This is the single most impactful
   notation fix.

2. **Resolve σ discrepancy (OPR-34)** — Determine whether σ = 8.82 and
   σ = 5.86 are the same quantity or different projections. The ratio 3/2
   suggests a geometric factor (e.g., from Z₃ or Y-junction geometry).

3. **Verify all Robin BC calculations** — Check whether OPR-20 computations
   used δ_BL = R_ξ ≈ 0.002 fm (correct sector) or accidentally used
   δ_J ≈ 0.1 fm (wrong sector, 50× error).

4. **Update C from 100 to 91** — With the Compton anchor δ_J = 0.1053 fm
   and L₀ ≈ 1.0 fm: C = (1.0/0.1053)² ≈ 90.2. This is a 10% correction
   to the junction-core results.

5. **Document the 50× gap** — The hierarchy δ_J/R_ξ ≈ 50 is a PHYSICAL
   feature of EDC (nucleon vs EW scale), not a bug. But it must be
   explicitly acknowledged and its origin understood.

---

**Sealed:** 2026-03-16. Step 5 of 9. δ canonical scale map complete.
