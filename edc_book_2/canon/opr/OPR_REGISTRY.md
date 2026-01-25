# OPR Registry — Book 2 (Authoritative)

**Status**: CANON
**Date**: 2026-01-25
**Branch**: book2-opr-registry-v1

---

## Registry Summary

| OPR | Category | Short Name | Status |
|-----|----------|------------|--------|
| OPR-01 | [C] | σ anchor | OPEN |
| OPR-02 | [A/B] | Robin α from action | OPEN |
| OPR-03 | [T] | π₁(M⁵) topology closure | OPEN |
| OPR-04 | [B] | δ ≡ R_ξ teleport | OPEN |
| OPR-05 | [B/C] | m_φ teleport | OPEN |
| OPR-06 | [C] | P_bulk anchor | OPEN |
| OPR-07 | [N] | Physics-grade numerics | PARTIAL |
| OPR-08 | [X] | sin²θ_W chain/notation | CLOSED |

---

## OPR-01 [C] σ anchor

**Short name**: Independent anchor/constraint for membrane tension σ

**Status**: OPEN

**Missing**:
- No independent measurement, bound, or constraint for σ exists
- σ = m_e³c⁴/(α³ℏ²) = 8.82 MeV/fm² is [Dc], not [Der]
- The value is conditional on hypothesis E_σ = m_e c²/α

**Blocks**:
- E-CH02-Dc-* (frozen regime conditions depend on σ)
- E-CH03-Dc-* (Z₆ program uses σ-dependent energy scales)
- All claims using 70 MeV or 5.856 MeV energy scales

**Where it appears in Book2**:
- CH02: Frozen regime foundations
- CH03: Z₆ program (energy scale derivations)

**Minimum closure deliverable**:
1. Identify an independent observable/constraint channel for σ
2. Provide bound/estimate with external source (cosmological, nuclear, or collider)
3. OR explicitly declare σ as [P] postulate with future-experiment note

**Closure test**:
OPR-01 is CLOSED iff σ is fixed or bounded WITHOUT using any downstream derived result (G_F, τ_n, m_e/m_p, etc.).

**No-smuggling note**:
σ cannot be "derived" by inverting a formula that uses σ as input. Any closure must use truly independent data.

---

## OPR-02 [A/B] Robin α from action

**Short name**: Derive Robin BC parameter α from 5D action/junction conditions

**Status**: OPEN

**Missing**:
- α appears in Robin BC: f'(0) + αf(0) = 0
- CH13 shows Robin structure emerges from junction, but α value not derived
- Connection to Israel junction conditions incomplete

**Blocks**:
- E-CH10-Dc-* (BC-dependent claims)
- E-CH13-Der-004 to E-CH13-Der-010 (partial — structure proven, value not)
- E-CH14-Dc-* (BVP eigenvalue claims)

**Where it appears in Book2**:
- CH10:99 (first use, teleported)
- CH13: OPR-20 closure attempts
- CH14: BVP work package

**Minimum closure deliverable**:
1. Derive α from variation of 5D action with GHY boundary term
2. Show how Israel junction conditions constrain α
3. Express α in terms of known/postulated quantities with explicit tags

**Closure test**:
CLOSED iff α appears as boundary term coefficient in δS = 0 variation AND matches the BC used in BVP chapter with consistent numerical value.

**No-smuggling note**:
α cannot be fitted to match a desired eigenvalue; must emerge from action principle.

---

## OPR-03 [T] π₁(M⁵) topology closure

**Short name**: Formalize topology assumption and its operational role

**Status**: OPEN

**Missing**:
- π₁(M⁵) = Z₃ is stated but not derived from embedding
- Connection to N_gen = 3 is asserted, not proven
- Topological charge conservation not explicitly linked

**Blocks**:
- E-CH06-Dc-* (three generations claims)
- E-CH05-Dc-* (lepton mass relations)
- All N_gen = 3 claims

**Where it appears in Book2**:
- CH06:341 (teleport — π₁(M⁵) = Z₃)
- CH05: Three generations section

**Minimum closure deliverable**:
1. Derive π₁(M⁵) from manifold construction (or cite source)
2. Show how π₁ = Z₃ implies exactly 3 stable localized modes
3. Document the chain: embedding → π₁ → N_gen

**Closure test**:
CLOSED iff π₁(M⁵) is computed from manifold definition AND N_gen = 3 follows from a mode-counting theorem with explicit assumptions.

**No-smuggling note**:
Cannot assume N_gen = 3 and reverse-engineer topology. Must go topology → mode count.

---

## OPR-04 [B] δ ≡ R_ξ teleport

**Short name**: Define δ precisely and connect to R_ξ with location + conditions

**Status**: OPEN

**Missing**:
- δ (brane thickness) appears at CH10:112 without prior definition
- Relation δ = R_ξ is used but not derived
- R_ξ itself requires BVP solution

**Blocks**:
- E-CH10-Dc-* (claims using brane thickness)
- E-CH11-Dc-* (G_F derivation uses δ in ℓ/δ ratio)
- All claims involving Robin parameter α ~ ℓ/δ

**Where it appears in Book2**:
- CH10:112 (first use, teleported)
- CH11: G_F derivation
- CH13: ℓ/δ ratio in OPR-20 attempts

**Minimum closure deliverable**:
1. Add explicit definition: "δ is the brane thickness scale, defined as..."
2. Derive or state δ = R_ξ relation with conditions
3. Tag as [P] or [Dc] with required inputs

**Closure test**:
CLOSED iff δ has an explicit definition before first use AND δ = R_ξ is either derived or explicitly postulated with justification.

**No-smuggling note**:
δ cannot be chosen to make eigenvalues "come out right"; must have independent definition.

---

## OPR-05 [B/C] m_φ teleport

**Short name**: Define m_φ input/source and how it enters equations

**Status**: OPEN

**Missing**:
- m_φ (mediator mass) appears at CH10:104 without definition
- Source of m_φ value not specified
- Relation to W/Z masses or 5D parameters unclear

**Blocks**:
- E-CH10-Dc-* (electroweak bridge claims)
- E-CH11-Dc-* (G_F derivation if m_φ enters)

**Where it appears in Book2**:
- CH10:104 (first use, teleported)
- Possibly CH11 (propagator expressions)

**Minimum closure deliverable**:
1. Add explicit definition: "m_φ is the mass of the 5D gauge-boson mediator"
2. Specify: is m_φ = M_W? Or a 5D-specific scale?
3. Tag as [BL] (if SM value), [P] (if postulated), or [Dc] (if derived)

**Closure test**:
CLOSED iff m_φ has an explicit definition with tagged source before first use in any equation.

**No-smuggling note**:
If m_φ = M_W is used, must state this is [BL] input, not a prediction.

---

## OPR-06 [C] P_bulk anchor

**Short name**: Canon anchor for bulk pressure symbol and definition

**Status**: OPEN

**Missing**:
- P_bulk / P_∞ appears in bulk-brane conservation statements
- Canonical definition may exist in Framework v2.0 but not propagated
- Sign convention (inflow vs outflow) must match Remark 4.5

**Blocks**:
- E-CH01-Dc-* (junction oscillation claims)
- E-CH02-Dc-* (frozen regime pressure balance)
- Any bulk-brane energy exchange claim

**Where it appears in Book2**:
- CH01: Weak interface (pressure terms)
- CH02: Frozen regime foundations

**Minimum closure deliverable**:
1. Cite Framework v2.0 Remark 4.5 for canonical statement
2. Define P_bulk with correct sign convention
3. Add [BL] or [Dc] tag with source reference

**Closure test**:
CLOSED iff P_bulk is defined with explicit reference to Framework v2.0 canonical statement AND sign convention is consistent throughout Book 2.

**No-smuggling note**:
P_bulk cannot be adjusted to balance equations; must have independent thermodynamic meaning.

---

## OPR-07 [N] Physics-grade numerics

**Short name**: At least one REPRO script with hashed outputs supporting a physics claim

**Status**: PARTIAL (Updated 2026-01-25)

**Progress**:
- 1 REPRO script complete: `repro_sin2_z6_verify.py` (sin²θ_W = 1/4)
- 1 REPRO stub: `repro_i4_overlap_stub.py` (blocked by OPR-21)
- Output hash recorded: `afb13677d8e2fd22564da90eb701c340a4994b8dd8dc0f08ba199462ad1ae472`

**Remaining**:
- I₄ overlap integral (blocked by OPR-21)
- τ_n WKB barrier calculation
- Lepton mass BVP eigenvalues

**Blocks**:
- Any claim tagged "verified numerically" without script
- E-CH14-Dc-* (BVP claims if they cite numerical results)
- E-CH11-Dc-* (G_F if overlap integral cited)

**Where it appears in Book2**:
- CH14: BVP work package (references toy figure)
- Potentially CH11, CH04 (if numerical checks mentioned)

**Minimum closure deliverable**:
1. Create at least 1 REPRO script in code/repro/
2. Script must reproduce a table/figure/value cited in Book 2
3. Output must be deterministic with SHA256 hash recorded
4. Script must fail loudly if inputs missing (OPR reference)

**Closure test**:
CLOSED iff at least one script in code/repro/ produces output matching a cited claim, with hash recorded in NUMERICS_REPRO_LEDGER.md.

**No-smuggling note**:
REPRO scripts must use inputs tagged [BL]/[P]/[I], not fitted parameters disguised as derivations.

---

## OPR-08 [X] sin²θ_W chain/notation

**Short name**: Ensure first introduction + dependency chain is documented

**Status**: OPEN

**Missing**:
- sin²θ_W = 1/4 appears in CH11 as [Der] from Z₆ counting
- But the notation |Z₂|/|Z₆| = 1/4 is non-standard (order vs index)
- Reader cannot trace the full chain without clarification

**Blocks**:
- E-CH11-Der-005, E-CH11-Der-013 (sin²θ_W derivation claims)
- E-CH04-Dc-* (electroweak parameters using sin²θ_W)

**Where it appears in Book2**:
- CH03: Z₆ program (introduces Z₆)
- CH04: Electroweak parameters (uses sin²θ_W)
- CH11:110-112, 322-323 (derivation statements)

**Minimum closure deliverable**:
1. Add 1-line clarification: "Z₂ here denotes the index-4 subgroup of Z₆"
2. OR correct notation to avoid confusion
3. Document first introduction location and dependency chain

**Closure test**:
CLOSED iff sin²θ_W = 1/4 has unambiguous notation AND a reader can trace from Z₆ definition to the result without "magic steps".

**No-smuggling note**:
sin²θ_W = 0.25 (bare) vs 0.2314 (running) must be distinguished; cannot claim both as "derived".

---

## Appendix: OPR → Claim Count Estimates

| OPR | Estimated Blocked Claims |
|-----|--------------------------|
| OPR-01 | ~40 (σ-dependent) |
| OPR-02 | ~26 (BC-dependent) |
| OPR-03 | ~40 (N_gen-dependent) |
| OPR-04 | ~15 (δ-dependent) |
| OPR-05 | ~8 (m_φ-dependent) |
| OPR-06 | ~10 (P_bulk-dependent) |
| OPR-07 | ~5 (numerics-cited) |
| OPR-08 | ~4 (sin²θ_W-dependent) |

*Note: Claims may be blocked by multiple OPRs. Exact crosswalk in OPR_CLAIM_CROSSWALK.md*

---

*Registry is CANON. Amendments require branch + review + merge.*
