# CLAIM EVIDENCE INDEX — Book 2 Evidence Audit

**Branch**: book2-ch07-openq-remediation-v1
**Date**: 2026-01-25
**Phase**: E3 (Post-CH07 Remediation)

---

## Summary Statistics

| Category | Count |
|----------|-------|
| **[Der] (Fully Derived)** | 12 |
| **[Dc] (Derived-Conditional)** | 184 |
| **[M]/[Def] (Mathematical/Definition)** | 5 |
| **TOTAL Claims** | **202** |

*Note: CH05 claims marked with 5* are [P] (provisional candidates), not [Der] or [Dc].*

### By Chapter

| Chapter | [Der] | [Dc] | [M]/[Def] | Total |
|---------|-------|------|-----------|-------|
| CH01 | 0 | 3 | 0 | 3 |
| CH02 | 0 | 8 | 0 | 8 |
| CH03 | 0 | 33 | 0 | 33 |
| CH04 | 0 | 24 | 0 | 24 |
| CH05 | 0 | 2 | 5* | 7 |
| CH06 | 0 | 1 | 9* | 10 |
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

### Lepton Mass Candidates (CH05)

| ID | Statement | Condition | Status |
|----|-----------|-----------|--------|
| E-CH05-P-001 | m_e = π√(ασΔℏc) | IF π derived [OPR-09] | [P] |
| E-CH05-P-002 | σ = 5.86 MeV/fm² | IF σ anchored [OPR-01] | [Dc] |
| E-CH05-P-003 | Δ = 3.121×10⁻³ fm | IF Δ = R_ξ [OPR-04] | [Dc] |
| E-CH05-P-004 | m_μ/m_e = (3/2)/α | IF (3/2) derived [OPR-10] | [P] |
| E-CH05-P-005 | Q = 2/3 (Koide) | IF Q from Z₆ [OPR-11] | [P] |
| E-CH05-P-006 | Q = \|Z₂\|/\|Z₃\| | IF energetics proven [OPR-11] | [P] |
| E-CH05-P-007 | m_τ from Koide | Not independent (constraint) | [P] |

### Three Generations (CH06)

| ID | Statement | Condition | Status |
|----|-----------|-----------|--------|
| E-CH06-Dc-001 | Hexagonal → Z₆ symmetry | IF energy min packing [Dc] | [Dc]/[P] |
| E-CH06-M-001 | Z₆ = Z₂ × Z₃ | Pure group theory | [M] |
| E-CH06-I-001 | \|Z₃\| = 3 ↔ N_gen = 3 | Identification only [OPR-03] | [I] |
| E-CH06-P-001 | Z₂ → matter/antimatter | Structural interpretation | [P] |
| E-CH06-P-002 | Z₃ → generation index | Structural interpretation | [P] |
| E-CH06-P-003 | Three-well V(ξ) toy model | Pedagogical, not derived | [P] |
| E-CH06-P-004 | KK truncation τ_n ~ exp(S_n/ℏ) | IF V(ξ) derived [OPR-12] | [P] |
| E-CH06-P-005 | π₁(M⁵) = Z₃ | IF bulk topology computed [OPR-03] | [P] |
| E-CH06-I-002 | Mode n=0,1,2 → (e,μ,τ) | Numerical match [OPR-03] | [I] |
| E-CH06-BL-001 | N_gen = 3 (LEP) | Experimental input | [BL] |

### Neutrino Edge Modes (CH07) — *Remediated 2026-01-25*

| ID | Statement | Condition | Status | OPEN-ID |
|----|-----------|-----------|--------|---------|
| E-CH07-P-001 | Neutrino as edge mode (post:ch6_neutrino_edge) | Ontological postulate (OPR-12) | [P] OPEN | 001, 006 |
| E-CH07-Dc-001 | m_ν/m_e ~ exp(-Δξ/κ⁻¹) (prop:ch6_suppression) | IF edge mode profiles (OPR-12) | [Dc] OPEN | 008 |
| E-CH07-I-001 | Three flavors ↔ \|Z₃\| = 3 (post:ch6_three_nu) | Identification (OPR-03) | [I] OPEN | 003, 010 |
| E-CH07-Dc-002 | Left-handed selection from BC (cor:ch6_left_nu) | IF Ch.9 BC established | [Dc] ✓ | — |
| E-CH07-P-002 | PMNS from wavefunction overlap (eq:ch6_pmns_overlap) | Mechanism postulate (OPR-13) | [P] OPEN | 016, 029 |
| E-CH07-Dc-003 | θ₂₃ ≈ 45° from Z₆ geometry (Attempt 2, A3) | From geometry | **[Dc] GREEN ✓** | 013 (DONE) |
| E-CH07-Dc-004 | DFT baseline falsified (sin²θ₁₃ = 1/3 vs 0.022) | Negative result | **[Dc] ✓** | 028 (DONE) |
| E-CH07-I-002 | Rank-2 + ε structure for PMNS (Attempt 4) | Structure identification (OPR-13) | [I] YELLOW | 021, 027 |
| E-CH07-Dc-005 | ε = λ/√2 predicts θ₁₃ (Attempt 4.1) | Uses λ [BL], 15% error (OPR-13) | **[BL→Dc] YELLOW** | 014 |
| E-CH07-Dc-006 | θ₁₂ = arctan(1/√2) (Attempt 4.2) | Pure geometry, 8.6% error (OPR-13) | **[Dc] YELLOW** | 012, 031 |

*CH07 Remediation: 32 OPEN-IDs catalogued; 12 DONE, 20 OPEN with OPR links. See `audit/chapters/CH07_OPEN_QUESTIONS_LEDGER.md`.*

### Fermi Constant (CH11)

| ID | Statement | Condition | Status |
|----|-----------|-----------|--------|
| E-CH11-Dc-012 | G_F = 1.166×10⁻⁵ via EW | IF sin²θ_W + v known | CONDITIONAL |
| E-CH11-Dc-014 | G_F = G₅ ∫\|f_L\|⁴ dξ | IF mode profiles known | CONDITIONAL |

---

## Open Problems Linked to Claims

| OPR | Description | Blocking Claims |
|-----|-------------|-----------------|
| OPR-01 | σ anchor | E-CH05-P-002 |
| OPR-02 | Robin α from action | E-CH10-Dc-*, E-CH13-Der-*, E-CH14-* |
| OPR-03 | π₁(M⁵) topology | E-CH05-P-007, E-CH06-I-001, E-CH06-P-005, E-CH07-I-001 |
| OPR-04 | δ ≡ R_ξ teleport | E-CH05-P-003 |
| OPR-09 | π prefactor derivation | E-CH05-P-001 |
| OPR-10 | (3/2) factor from Z₆ | E-CH05-P-004 |
| OPR-11 | Koide Q = 2/3 energetics | E-CH05-P-005, E-CH05-P-006 |
| OPR-12 | KK truncation / V(ξ) | E-CH06-P-004, E-CH06-I-002 |
| OPR-13 | PMNS mixing angles | E-CH07-I-002, E-CH07-Dc-003 to E-CH07-Dc-006 |
| OPR-14 | CP phase δ derivation | E-CH07-* (CP phase claims) |
| OPR-15 | Dirac/Majorana determination | E-CH07-* (neutrino nature) |
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
