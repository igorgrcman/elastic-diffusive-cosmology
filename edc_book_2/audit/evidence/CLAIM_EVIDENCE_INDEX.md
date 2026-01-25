# CLAIM EVIDENCE INDEX — Book 2 Evidence Audit

**Branch**: book2-chapter-audit-v1
**Date**: 2026-01-25
**Phase**: E1 (Evidence Index)

---

## Summary Statistics

| Category | Count |
|----------|-------|
| **[Der] (Fully Derived)** | 12 |
| **[Dc] (Derived-Conditional)** | 184 |
| **[M]/[Def] (Mathematical/Definition)** | 5 |
| **TOTAL Claims** | **201** |

### By Chapter

| Chapter | [Der] | [Dc] | [M]/[Def] | Total |
|---------|-------|------|-----------|-------|
| CH01 | 0 | 3 | 0 | 3 |
| CH02 | 0 | 8 | 0 | 8 |
| CH03 | 0 | 33 | 0 | 33 |
| CH04 | 0 | 24 | 0 | 24 |
| CH05 | 0 | 3 | 0 | 3 |
| CH06 | 0 | 13 | 0 | 13 |
| CH07 | 0 | 24 | 0 | 24 |
| CH08 | — | — | — | — |
| CH09 | 0 | 2 | 0 | 2 |
| CH10 | 0 | 8 | 0 | 8 |
| CH11 | 2 | 22 | 0 | 24 |
| CH12 | 0 | 18 | 0 | 18 |
| CH13 | 10 | 25 | 0 | 35 |
| CH14 | 0 | 1 | 5 | 6 |

---

## [Der] Claims (Fully Derived) — 12 Total

### CH11: G_F Derivation

| ID | Location | Statement | Equation | Status |
|----|----------|-----------|----------|--------|
| E-CH11-Der-005 | 11_gf:110-112 | sin²θ_W = 1/4 from Z₆ subgroup counting | eq:ch11_sin2_input | PROVEN |
| E-CH11-Der-013 | 11_gf:322-323 | sin²θ_W(μ_lattice) = \|Z₂\|/\|Z₆\| = 1/4 | eq:ch11_sin2_input | PROVEN |

### CH13: OPR-20 Attempts

| ID | Location | Statement | Equation | Status |
|----|----------|-----------|----------|--------|
| E-CH13-Der-001 | attemptE:150 | ℓ = 2πR_ξ from circumference definition | ch11_E_ell_derivation | PROVEN |
| E-CH13-Der-002 | attemptE:184 | 2π factor from circumference geometry | — | PROVEN |
| E-CH13-Der-003 | attemptE:198 | 2π factor upgraded [P]→[Der] | — | PROVEN |
| E-CH13-Der-004 | attemptG:283 | Robin BC from action variation | attemptG_alpha_from_variation | PROVEN |
| E-CH13-Der-005 | attemptG:284 | α ~ ℓ/δ from inner/outer matching | — | PROVEN |
| E-CH13-Der-006 | attemptG:285 | Dimensional relation α = ℓ·α_phys | attemptG_alpha_relation | PROVEN |
| E-CH13-Der-007 | attemptF:252 | Junction → Robin structure | — | PROVEN |
| E-CH13-Der-008 | attemptC:250 | Negative closure: standard BC route | — | PROVEN |
| E-CH13-Der-009 | forensic:46 | BC route negative closure | — | PROVEN |
| E-CH13-Der-010 | attemptH2_hard:317 | Robin structure established | — | PROVEN |

---

## Critical [Dc] Claims (Tier-1 Physics)

### Electroweak Parameters (CH03-CH04)

| ID | Statement | Condition | Status |
|----|-----------|-----------|--------|
| E-CH03-Dc-032 | sin²θ_W = 1/4 (8% from exp) | IF Z₆ coupling map accepted | CONDITIONAL |
| E-CH04-Dc-008 | g² = 4πα(M_Z)/sin²θ_W = 0.4246 | IF sin²θ_W known | CONDITIONAL |
| E-CH04-Dc-012 | sin²θ_W(M_Z) = 0.2314 via RG | IF bare value 1/4 + SM RG | CONDITIONAL |
| E-CH04-Dc-017 | τ_n ≈ 830s (6% from exp) | IF WKB + barrier params | CONDITIONAL |

### Flavor Structure (CH05-CH07)

| ID | Statement | Condition | Status |
|----|-----------|-----------|--------|
| E-CH06-Dc-008 | m_ν/m_e ~ exp(-Δξ/κ⁻¹) | IF edge mode profiles | CONDITIONAL |
| E-CH07-Dc-002 | CKM hierarchy λ,λ²,λ³ | IF overlap model + separation | CONDITIONAL |
| E-CH07-Dc-007 | δ = 60° from Z₂ selection | IF phase cancellation | CONDITIONAL |

### Fermi Constant (CH11)

| ID | Statement | Condition | Status |
|----|-----------|-----------|--------|
| E-CH11-Dc-012 | G_F = 1.166×10⁻⁵ via EW | IF sin²θ_W + v known | CONDITIONAL |
| E-CH11-Dc-014 | G_F = G₅ ∫\|f_L\|⁴ dξ | IF mode profiles known | CONDITIONAL |

---

## Open Problems Linked to Claims

| OPR | Description | Blocking Claims |
|-----|-------------|-----------------|
| OPR-02 | KK truncation → N_gen=3 | E-CH05-Dc-*, E-CH14-* |
| OPR-17 | Coupling map from 5D action | E-CH03-Dc-*, E-CH04-Dc-* |
| OPR-19 | g₅ value derivation | E-CH11-Dc-* |
| OPR-20 | ℓ and BC from membrane | E-CH10-Dc-*, E-CH13-* |
| OPR-21 | I₄ overlap from BVP | E-CH11-Dc-014, E-CH14-* |
| OPR-22 | First-principles G_F | E-CH11-Dc-012 |

---

## Key Findings

1. **NO [Der] in CH01-CH10**: All foundation chapters use [Dc] (conditional)
2. **[Der] concentrated in CH11 + CH13**: sin²θ_W derivation + closure attempt proofs
3. **Most claims are IF-THEN structures**: Depend on postulated inputs (profiles, coupling maps)
4. **Circularity warning**: G_F numerical closure uses v which depends on G_F

---

*Generated: 2026-01-25*
*Evidence Audit Phase E1*
