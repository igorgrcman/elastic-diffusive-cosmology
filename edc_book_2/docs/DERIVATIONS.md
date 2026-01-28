# DERIVATIONS.md — Mathematical Chain Registry

**Last updated:** 2026-01-28

---

## Format

Each derivation entry follows this structure:
```
### DER-XXX: [Name]
**Status:** [Der]/[Dc]/[I]/[P]/[Cal]
**Depends on:** [list of DER-XXX or assumptions]
**Result:** [equation]
**Location:** [file:line]
**Open issues:** [if any]
```

---

## Core Parameters

### DER-001: Brane Tension σ
**Status:** [Dc] — Conditional on hypothesis E_σ = m_e c²/α
**Depends on:** m_e [BL], α [BL], hypothesis E_σ = m_e c²/α [P]
**Result:**
```
σ = m_e³ c⁴ / (α³ ℏ²) = 8.82 MeV/fm²
```
**Location:** Turning point document TP-2026-01-20
**Open issues:** E_σ = m_e c²/α is [P], needs geometric derivation

### DER-002: Brane Thickness δ
**Status:** [Dc]
**Depends on:** m_p [BL], Compton regularization [P]
**Result:**
```
δ = ℏ / (2 m_p c) = 0.105 fm
```
**Location:** BOOK_SECTION_NEUTRON_LIFETIME.tex:54
**Open issues:** Factor 2 is conventional

### DER-003: Junction Extent L₀
**Status:** [P]
**Depends on:** r_p [BL], δ [DER-002]
**Result:**
```
L₀ = r_p + δ = 0.875 + 0.105 = 0.980 fm
```
**Location:** BOOK_SECTION_NEUTRON_LIFETIME.tex:153-154
**Open issues:** Alternative: L₀/δ = π² from standing wave argument

---

## Neutron Lifetime

### DER-010: Instanton Action
**Status:** [Dc] — Conditional on S¹ junction topology
**Depends on:** κ = 2π [DER-011], L₀/δ [DER-003]
**Result:**
```
S_E/ℏ = κ × (L₀/δ) = 2π × 9.33 ≈ 58.6
```
**Location:** BOOK_SECTION_NEUTRON_LIFETIME.tex:260
**Open issues:** L₀/δ tension (9.33 vs π²)

### DER-011: Topological Winding Factor κ
**Status:** [Dc] — Conditional on S¹ topology
**Depends on:** π₁(S¹) = ℤ [M]
**Result:**
```
κ = 2π (from ∮dθ = 2π for minimal winding Δw = 1)
```
**Location:** BOOK_SECTION_NEUTRON_LIFETIME.tex:128-131
**Open issues:** Need to verify junction has S¹ topology

### DER-012: Attempt Frequency ω₀
**Status:** [P]
**Depends on:** σ [DER-001], M = m_p [P]
**Result:**
```
ω₀ = √(σ/m_p) ≈ 19.1 MeV ≈ 2.9 × 10²² Hz
```
**Location:** BOOK_SECTION_NEUTRON_LIFETIME.tex:219
**Open issues:** M = m_p is assumed, not derived

### DER-013: Neutron Lifetime Formula
**Status:** [Dc/Cal]
**Depends on:** S_E/ℏ [DER-010], ω₀ [DER-012], A [Cal]
**Result:**
```
τ_n = A × (ℏ/ω₀) × exp(S_E/ℏ)

Uncalibrated (A=1): τ_n ≈ 1050 s
Calibrated (A=0.84): τ_n ≈ 879 s
```
**Location:** BOOK_SECTION_NEUTRON_LIFETIME.tex:79-81
**Open issues:** A = 0.84 is [Cal], needs derivation from fluctuation determinant

---

## Topological Pinning Model

### DER-020: Contact Area
**Status:** [Dc]
**Depends on:** δ [DER-002], L₀ [DER-003]
**Result:**
```
A_contact = π δ L₀ = π × 0.105 × 1.0 ≈ 0.33 fm²
```
**Location:** BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex:270-271
**Open issues:** Saddle surface assumption

### DER-021: Geometric Factor f
**Status:** [I]
**Depends on:** δ [DER-002], L₀ [DER-003]
**Result:**
```
f = √(δ/L₀) = √(0.105/1.0) ≈ 0.32
```
**Location:** BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex:298-300
**Open issues:** Penetration depth ratio — needs first-principles derivation

### DER-022: Pinning Constant K
**Status:** [Dc/I]
**Depends on:** f [DER-021], σ [DER-001], A_contact [DER-020]
**Result:**
```
K = f × σ × A_contact = 0.32 × 8.82 × 0.33 ≈ 0.93 MeV
```
**Location:** BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex:306-312
**Open issues:** Phenomenological check: 0.7-0.8 MeV needed

### DER-023: Allowed Coordinations
**Status:** [I]
**Depends on:** Y-junction trivalent constraint [P], quantum doubling [P]
**Result:**
```
n = 2^a × 3^b for a,b ≥ 0
Allowed: {6, 8, 9, 12, 24, 36, 48, 72, ...}
Forbidden: {5, 7, 11, 13, 37, 41, 43, 47, ...}
```
**Location:** BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex:60-95
**Open issues:** Geometric argument needs formalization

### DER-024: Bound Neutron Lifetime Enhancement
**Status:** [Dc]
**Depends on:** K [DER-022], S_E/ℏ [DER-010]
**Result:**
```
At saddle point q_barrier ≈ 0.5:
ΔV_eff ≈ ΔV + 6K × q_barrier² ≈ 1.3 + 5.6 × 0.25 ≈ 2.7 MeV
S_eff/ℏ ≈ 60 × √(2.7/1.3) ≈ 86
τ_bound > 10¹³ s
```
**Location:** BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex:373-387
**Open issues:** q_barrier = 0.5 assumed (saddle point)

---

## Frustration-Corrected Geiger-Nuttall Law

### DER-030: Frustration Energy Interpolation
**Status:** [I]
**Depends on:** n_eff(A) interpolation [P]
**Result:**
```
n_eff(A) = 6 + 37(1 - e^(-(A-20)/80))
ε_f(A) = |E/A(n_eff) - E/A(n_allowed)|
```
**Location:** BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex:686-689
**Open issues:** Interpolation is phenomenological

### DER-031: Frustration-Corrected G-N Formula
**Status:** [I/Cal]
**Depends on:** ε_f(A) [DER-030], standard G-N [BL]
**Result:**
```
log₁₀(t½) = 1.63 × Z/√Q - 2.40 × ε_f - 42.1
R² = 0.9941 (vs 0.9822 standard)
44.7% improvement in MAE
```
**Location:** BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex:681-699
**Open issues:** Coefficients a, c, b are [Cal]

---

## Weak Sector (Paper 3 Results)

### DER-040: V-A Structure
**Status:** [Dc]
**Depends on:** 5D chirality projection [P]
**Result:** V-A structure emerges from 5D geometry
**Location:** Paper 3, weak sector section
**Open issues:** None

### DER-041: Parity Violation
**Status:** [Dc]
**Depends on:** 5D geometry [P]
**Result:** Parity violation enforced by 5D structure
**Location:** Paper 3, weak sector section
**Open issues:** None

### DER-042: Weinberg Angle
**Status:** [Der]
**Depends on:** Geometric embedding [P]
**Result:**
```
sin²θ_W = 1/4 (exact at tree level)
```
**Location:** Paper 3
**Open issues:** Radiative corrections not included

### DER-043: Fermi Coupling G_F
**Status:** [Dc/Cal] — CIRCULAR
**Depends on:** measured v [BL] — THIS IS THE PROBLEM
**Result:** Partial derivation, but uses measured Higgs VEV
**Location:** Paper 3
**Open issues:** Need pure 5D derivation without circular input

---

## Dependency Graph Summary

```
[BL] m_e, m_p, α, r_p
        ↓
    [P] E_σ = m_e c²/α
        ↓
    [Dc] σ = 8.82 MeV/fm² (DER-001)
        ↓
    [Dc] δ, L₀ (DER-002, DER-003)
        ↓
    ├── [Dc] S_E/ℏ ≈ 60 (DER-010)
    │       ↓
    │   [Dc/Cal] τ_n ≈ 879 s (DER-013)
    │
    └── [Dc/I] K ≈ 0.94 MeV (DER-022)
            ↓
        [Dc] τ_bound → ∞ (DER-024)
        [I] B.E.(He-4), B.E.(C-12), B.E.(O-16)
        [I/Cal] Frustration G-N Law (DER-031)
```

**No cycles detected.**
