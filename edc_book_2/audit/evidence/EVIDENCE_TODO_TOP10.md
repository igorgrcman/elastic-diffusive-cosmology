# EVIDENCE TODO TOP 10 — Book 2 Evidence Audit

**Branch**: book2-chapter-audit-v1
**Date**: 2026-01-25
**Phase**: E4 (Remediation Priorities)

---

## Severity Legend

| Level | Meaning |
|-------|---------|
| **BLOCKER** | Prevents closure of major physics claim |
| **HIGH** | Affects multiple claims or key derivation |
| **MEDIUM** | Single claim or notation issue |
| **LOW** | Cosmetic or organizational |

---

## TOP 10 BLOCKERS

### 1. OPR-21: I₄ Overlap Integral from BVP — BLOCKER

**Status**: OPEN
**Blocks**: G_F first-principles derivation (22+ claims)
**Location**: CH11, CH14

**Issue**: The overlap integral I₄ = ∫|f_L(ξ)|⁴ dξ requires solving the
BVP for fermion localization profiles f_L(ξ). No such solution exists.

**Required Work**:
- Solve Robin BVP: -∂²f/∂ξ² + V(ξ)f = E·f with f'(0) + αf(0) = 0
- Determine V(ξ) from 5D membrane action (OPR-20 dependency)
- Compute I₄ numerically
- Create REPRO script with hash

**Remediation**: Mark as [OPEN] with explicit OPR-21 reference.

---

### 2. OPR-17: Coupling Map from 5D Action — BLOCKER

**Status**: OPEN
**Blocks**: Electroweak parameter derivations (57+ claims)
**Location**: CH03, CH04

**Issue**: The Z₆ → SU(2)×U(1) coupling map g₅ → (g, g') is stated
but not derived from 5D action variation.

**Required Work**:
- Derive gauge couplings from membrane boundary conditions
- Show how Z₆ discrete symmetry constrains continuous gauge group
- Compute g₅ value from first principles

**Remediation**: Mark coupling map as [P] (postulated), add OPR-17 link.

---

### 3. OPR-20: ℓ and BC from Membrane — BLOCKER

**Status**: PARTIAL (Robin structure proven, but ℓ not derived)
**Blocks**: 26+ claims in CH10, CH13
**Location**: CH10, CH13

**Issue**: The circumference ℓ = 2πR_ξ is geometric, but R_ξ value
requires BVP solution. Robin parameter α ~ ℓ/δ proven but δ teleported.

**Required Work**:
- Derive R_ξ from membrane equilibrium condition
- Close the δ = R_ξ relation (currently teleported at CH10:112)

**Remediation**: Add [OPEN] tag at teleport locations.

---

### 4. OPR-02: KK Truncation → N_gen = 3 — HIGH

**Status**: OPEN
**Blocks**: All three-generation claims (~40)
**Location**: CH05, CH06, CH14

**Issue**: Why exactly 3 fermion generations? Current answer is
"KK truncation" but no explicit counting from topology.

**Required Work**:
- Derive N_bound from BVP eigenvalue count
- Show topological constraint (π₁(M⁵) = Z₃ is stated, not derived)

**Remediation**: Mark N_gen = 3 as [P] with OPR-02 link.

---

### 5. sin²θ_W = 1/4 Notation Clarification — HIGH

**Status**: NEEDS EDIT
**Blocks**: 2 [Der] claims (E-CH11-Der-005, E-CH11-Der-013)
**Location**: CH11:110-112, CH11:322-323

**Issue**: Text states |Z₂|/|Z₆| = 1/4 but standard notation gives
|Z₂| = 2, |Z₆| = 6, so ratio = 1/3. The intended meaning is
"index-4 subgroup" not "order-2 subgroup".

**Required Work**:
- Add clarifying footnote or parenthetical
- Explicitly state: "Z₂ here denotes the index-4 subgroup of Z₆"

**Remediation**: MINIMAL — add 1-line clarification.

---

### 6. G_F Circularity Warning — HIGH

**Status**: NEEDS EXPLICIT STATEMENT
**Blocks**: 1 claim (E-CH11-Dc-012)
**Location**: CH11

**Issue**: G_F = 1.166×10⁻⁵ uses v = 246 GeV, but v depends on G_F
via v = (√2 G_F)^(-1/2). This appears circular.

**Resolution**: NOT circular if v is [BL] input. But this must be
stated explicitly.

**Required Work**:
- Add statement: "v = 246.22 GeV is treated as [BL] input (PDG 2024)"
- Clarify that consistency check (reproducing v) is validation, not derivation

**Remediation**: MINIMAL — add 1-line [BL] tag.

---

### 7. Teleport T1: δ = R_ξ at CH10:112 — HIGH

**Status**: TELEPORTED (no derivation before use)
**Blocks**: Claims depending on brane thickness
**Location**: CH10:112

**Issue**: δ (brane thickness) equated to R_ξ without prior definition
or derivation. First appearance is in formula.

**Required Work**:
- Add forward reference to CH14 where BVP defines δ
- Or add inline definition: "where δ ≡ R_ξ is the brane thickness scale"

**Remediation**: MINIMAL — add 1-line definition.

---

### 8. Teleport T2: m_φ at CH10:104 — HIGH

**Status**: TELEPORTED
**Blocks**: Claims depending on mediator mass
**Location**: CH10:104

**Issue**: Mediator mass m_φ appears without definition.

**Required Work**:
- Add definition: "m_φ is the mass of the 5D gauge-boson mediator"
- Link to derivation in later chapter or mark [P]

**Remediation**: MINIMAL — add 1-line definition with [P] tag.

---

### 9. Teleport T3: α (Robin parameter) at CH10:99 — HIGH

**Status**: TELEPORTED
**Blocks**: Claims depending on boundary condition
**Location**: CH10:99

**Issue**: Robin parameter α used before definition.

**Required Work**:
- Add forward reference: "α is derived in CH13 from junction matching"
- Or add inline summary

**Remediation**: MINIMAL — add 1-line forward reference.

---

### 10. OPR-22: First-Principles G_F — MEDIUM

**Status**: OPEN (depends on OPR-19, OPR-20, OPR-21)
**Blocks**: 1 claim (ultimate closure)
**Location**: CH11

**Issue**: G_F = g₅² ℓ² I₄ / x₁² requires all components derived.
Currently blocked by upstream OPRs.

**Required Work**:
- Solve OPR-19 (g₅ value)
- Solve OPR-20 (ℓ from membrane)
- Solve OPR-21 (I₄ from BVP)
- Then compute G_F and compare to [BL]

**Remediation**: Document dependency chain, mark [OPEN:OPR-22].

---

## Remediation Action Matrix

| Item | Type | LOC Change | Risk |
|------|------|------------|------|
| #5 sin²θ_W notation | ADD | +1 line | LOW |
| #6 G_F circularity | ADD | +1 line | LOW |
| #7 δ teleport | ADD | +1 line | LOW |
| #8 m_φ teleport | ADD | +1 line | LOW |
| #9 α teleport | ADD | +1 line | LOW |
| #1-4, #10 OPR blockers | TAG | +[OPEN] tags | LOW |

**Total minimal remediation**: ~10 lines of text additions.
**Risk**: LOW (no physics changes, only clarifications and tags).

---

## Next Steps

1. Apply #5-#9 minimal remediations (5 one-line edits)
2. Add [OPEN:OPR-XX] tags to blocked claims
3. Run gates (notation, canon, build)
4. Verify 387 pages maintained
5. Update MASTER_AUDIT_LEDGER with EVIDENCE status

---

*Generated: 2026-01-25*
*Evidence Audit Phase E4*
