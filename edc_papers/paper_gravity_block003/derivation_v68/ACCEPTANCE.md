# v68 Acceptance Criteria Checklist

## Date: 2026-03-16

---

## AC1: Task 1 and Task 2 Results Correctly Imported

- [x] σ_BookI ≠ σ_covariant proven (§2.1, Theorem 2.1)
- [x] [σ_cov] = M⁴ stated (§2.1)
- [x] [σ_BookI] = M³ stated (§2.1)
- [x] σ_BookI does not enter σ̃ (Corollary 2.2)
- [x] T_* = 3M₅³/(4πℓ) with [M⁴] (§2.2, Theorem 2.3)
- [x] C = 3/(4π) (§2.2)
- [x] σ̃ = 1 at RS fine-tuning (Corollary 2.4)

**PASS**

## AC2: Plenum Pressure Derivation with Explicit Dimensional Analysis

- [x] Plenum formula σ_BookI = 2πRξ²ρP stated (§3.1, eq. 3)
- [x] Dimensional check: [Rξ²ρP] = M⁻² × M⁵ = M³ (§3.1)
- [x] Proof that this gives σ_BookI [M³], not σ_cov [M⁴] (§3.2)
- [x] Bridging scale candidates listed with status [P] (§3.2)
- [x] T_* expressed in terms of ρP under hypothesis (§3.3, eq. 5)
- [x] Anti-circularity check passed (§3.6)

**PASS**

## AC3: σ̃ Result — Derived or Documented as [OPEN]

- [x] σ̃ = 1 at RS fine-tuning: **DERIVED** [I] (§4)
- [x] σ̃ numerical value: **DOCUMENTED AS [OPEN]** (§4)
- [x] Gap stated precisely: "σ_cov from full EDC 5D action" (§4)
- [x] α₃ tension documented honestly (§4.1)
- [x] Three resolution paths identified (§4.1)

**PASS** (option (b): documented as [OPEN] with exact gap)

## AC4: Deprecation Log Complete for DEF-A through DEF-D

- [x] DEF-A (v48): σ̃ = σ/M̄_Pl⁴ — DEPRECATED, reason stated
- [x] DEF-B (v56): β = σ̃⁴ — DEPRECATED, algebraic error
- [x] DEF-C (v62): σ̃ = σL²/M̄_Pl² — DEPRECATED, gives 10⁻³⁶
- [x] DEF-D (v67): σ̃ = σ/T_* with [M³] — INVALIDATED, dimensional error
- [x] v68 stated as CANONICAL

**PASS**

## AC5: No Circularity — σ̃ Not Derived from α₃

- [x] One-directional chain: 5D Action → T_* → σ̃ → BLOCK-004 (§3.6)
- [x] α₃ does not feed back into ρP, M₅, or ℓ
- [x] No back-calculation from τ_p
- [x] Forbidden feedback table (§8)

**PASS**

## AC6: All Claims Epistemically Tagged

- [x] [Der] for derived results (T_*, σ̃ = 1 at tuning, etc.)
- [x] [I] for mathematical identities (C = 3/(4π), dimensions)
- [x] [Dc] for definitional choices (Route A convention)
- [x] [P] for pending/hypothetical (Plenum → Λ₅, bridging scale)
- [x] [OPEN] for unresolved items (σ_cov, σ̃ numerical)
- [x] [INV] for invalidated claims (v67 σ̃ = 100)
- [x] Full epistemic status table (§7)

**PASS**

## AC7: Layer A Firewall Maintained

- [x] No PDG values
- [x] No Super-Kamiokande bounds
- [x] No experimental calibration
- [x] σ_BookI appears only as negative example
- [x] Guard compliance table with all checks ✓ (§8)

**PASS**

## AC8: Commit with Exact Title and Push

- [ ] Commit title: `derive(edc): canonical v68 sigma-tilde from Plenum pressure balance`
- [ ] Push to branch

**PENDING** (will be done after this checklist)

---

## Overall Assessment

**7/8 PASS, 1 PENDING (commit/push)**

v68 is accepted as the canonical σ̃ document. It honestly documents:
- What IS derived (σ̃ = 1 at RS tuning, structural form)
- What is NOT derived (σ̃ numerical, σ_cov)
- What is invalidated (v67 σ̃ = 100)
- What remains open (Plenum → σ_cov mechanism)
