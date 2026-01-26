# OPR Registry — Book 2 (Authoritative)

**Status**: CANON
**Date**: 2026-01-25
**Branch**: book2-opr-registry-v1

---

## Scale Taxonomy (Canonical Reference)

**Location**: Chapter 16, §16.1 (`\label{sec:ch16_reader_map}`)

| Symbol | Name | Physical Role | Status |
|--------|------|---------------|--------|
| Δ | Kink width | Scalar wall microphysics: φ = v tanh(ξ/Δ) | [M] |
| δ | Boundary-layer | Transport/diffusion regularization for Robin BC | [P] |
| ℓ | Domain support | Sturm-Liouville interval for OPR-21: μ = M₀ℓ | [P] |
| R_ξ | Diffusion scale | Coordinate/correlation length: R_ξ = ℏc/M_Z | [BL] |

**Unit conversion**: 1 fm = 5.0677 GeV⁻¹

### Assumption Labels (A1–A3)

| ID | Assumption | Use Case |
|----|------------|----------|
| (A1) | Δ = δ | Kink width = boundary-layer scale |
| (A2) | δ = R_ξ | Boundary-layer = diffusion scale |
| (A3) | ℓ = nΔ with n = O(1) | Domain size proportional to kink width |

**Rule**: No derivation may silently assume any of (A1)–(A3). Each must be explicitly tagged [P] with assumption label.

### Working Default (WD)

**Path 1 (δ ≠ Δ)** is adopted as the narrative working hypothesis for subsequent chapters.
This is a narrative choice [P], not a derived claim.

### Conditional Tension (Lemma 16.1)

Under joint assumptions (A1)+(A2)+(A3), the OPR-04 result (Δ ~ R_ξ ~ 10⁻³ fm) combined with
OPR-21 requirement (μ ∈ [25,35]) yields μ << 25, creating a **CONDITIONAL TENSION**.

**This is NOT an incompatibility** — relaxing ANY of (A1)–(A3) removes the tension.

---

## Registry Summary

| OPR | Category | Short Name | Status |
|-----|----------|------------|--------|
| OPR-01 | [C] | σ → M₀ anchor | CONDITIONAL [Dc] |
| OPR-02 | [A/B] | Robin α from action | PARTIAL |
| OPR-03 | [T] | π₁(M⁵) topology closure | OPEN |
| OPR-04 | [B] | δ ≡ R_ξ teleport | OPEN |
| OPR-05 | [B/C] | m_φ teleport | OPEN |
| OPR-06 | [C] | P_bulk anchor | OPEN |
| OPR-07 | [N] | Physics-grade numerics | STRONG PARTIAL |
| OPR-08 | [X] | sin²θ_W chain/notation | CLOSED |
| OPR-09 | [L] | π prefactor derivation | OPEN |
| OPR-10 | [L] | (3/2) factor from Z₆ | OPEN |
| OPR-11 | [L] | Koide Q = 2/3 energetics | OPEN |
| OPR-12 | [L] | KK truncation / V(ξ) potential | OPEN |
| OPR-13 | [N] | PMNS mixing angles | YELLOW PARTIAL |
| OPR-14 | [N] | CP phase δ derivation | OPEN |
| OPR-15 | [N] | Dirac/Majorana determination | OPEN |
| OPR-16 | [H] | Pion mass/lifetime | OPEN |
| OPR-17 | [G] | SU(2)_L gauge embedding | OPEN |
| OPR-18 | [M] | CKM/PMNS from overlaps | OPEN |
| OPR-19 | [G] | g₅ value from 5D action | CONDITIONAL [Dc] |
| OPR-20 | [G] | Mediator mass from ξ-geometry | CONDITIONAL [Dc] |
| OPR-21 | [B] | BVP mode profiles | STRONG PARTIAL |
| OPR-22 | [C] | First-principles G_eff | CONDITIONAL [Dc] |

---

## Cleanup Items

| ID | Description | Priority | Status |
|----|-------------|----------|--------|
| CLEANUP-20-LEGACY | Replace deprecated `g₅²ℓ²/x₁²` in ch11/ch12 legacy sections with canonical `g₅²ℓ/x₁²` + forward pointer to OPR-22 | LOW | **DONE** (2026-01-25) |

---

## OPR-01 [C] σ anchor → M₀ derivation

**Short name**: Derive bulk mass amplitude M₀ from membrane tension σ

**Status**: CONDITIONAL [Dc] (Updated 2026-01-25)

**Sprint completed**: book2-opr01-sigma-anchor-v1

**What is derived [Dc]**:
- M₀² = (3y²/4) σΔ — bulk mass amplitude from domain-wall kink theory
- M₀ = (√3/2) y √(σΔ) ≈ 0.866 y √(σΔ)
- μ = M₀ℓ = (√3/2) y n √(σΔ³) — dimensionless parameter for OPR-21

**Derivation source**:
- Scalar kink theory [M]: φ(ξ) = v tanh(ξ/Δ), σΔ = 4v²/3
- Yukawa coupling ansatz [P]: M(ξ) = yφ(ξ) = M₀ tanh(ξ/Δ)
- Combined [Dc]: M₀ = yv, eliminate v → M₀² = (3y²/4)σΔ

**Parameters (all [P] postulated)**:
- σ = membrane tension
- Δ = domain-wall thickness
- y = Yukawa coupling
- n = ℓ/Δ domain-size ratio

**Consistency constraint for OPR-21**:
- For μ ∈ [25, 35) (N_bound = 3 window): σΔ³ ∈ [52, 102] with y=1, n=4

**Blocks**:
- E-CH02-Dc-* (frozen regime conditions depend on σ)
- E-CH03-Dc-* (Z₆ program uses σ-dependent energy scales)
- All claims using 70 MeV or 5.856 MeV energy scales

**Where it appears in Book2**:
- CH02: Frozen regime foundations
- CH03: Z₆ program (energy scale derivations)
- **NEW**: CH15 (OPR-01 derivation section) — src/sections/ch15_opr01_sigma_anchor_derivation.tex

**Documentation created (2026-01-25)**:
- `src/sections/ch15_opr01_sigma_anchor_derivation.tex` — Book chapter derivation
- `audit/evidence/OPR01_SIGMA_ANCHOR_REPORT.md` — Evidence chain + claim mapping
- `canon/opr/OPR-01.md` — Canonical OPR document
- `code/opr01_sigma_anchor_check.py` — Numeric sanity script

**Closure test**:
OPR-01 is CLOSED iff M₀ is derived from σ without circular dependency ✓
AND no SM observables used as inputs ✓
AND derivation chain is explicit and tagged ✓

**Current status: CONDITIONAL [Dc]**
- Condition: Domain-wall ansatz for M(ξ) [P]
- Condition: Yukawa coupling mechanism [P]

**Remaining for full [Der]**:
1. Derive σ from independent physics (cosmological, gravitational)
2. Derive Δ from junction stability or brane microphysics
3. Derive y from gauge embedding or naturalness arguments
4. Derive n = ℓ/Δ from domain-size principle

**No-smuggling certification**: ✓ PASS
- Grep verification: No M_W, G_F, v=246GeV, sin²θ_W, α(M_Z), PMNS/CKM, τ_n, CODATA in derivation
- Only used: scalar kink theory [M] + domain-wall ansatz [P] + Yukawa [P]

---

## OPR-02 [A/B] Robin α from action

**Short name**: Derive Robin BC parameter α from 5D action/junction conditions

**Status**: PARTIAL [Dc]+[P] (Updated 2026-01-25)

**CLOSED requires: OPR-04 CLOSED OR λ̃ derivation (BKT route)**

**What is derived [Dc]**:
- Robin BC **form** f' + αf = 0 follows from 5D action variation
- Robin BC **structure** emerges from BKT (brane kinetic term) junction matching
- Three structural expressions for α are derived:
  - α = λ̃m²/2 (from BKT variation) — eq:attemptF_alpha_BKT
  - α ~ κ₅²σℓ (from Israel junction) — eq:attemptG_alpha_tension
  - α = ℓ/δ (from thick-brane matching) — eq:attemptG_alpha_thick

**What requires [P] (one choice needed)**:
- Route A: BKT coefficient λ̃ ~ 2-4 (gives α ~ 8) — requires λ̃ derivation
- Route B: Junction parameters κ₅, σ (requires Part I) — requires σ/κ₅ anchor
- Route C: δ = R_ξ identification (gives α = 2π ≈ 6.3) — **RECOMMENDED [P]**
  - Cannot upgrade to [Dc] until OPR-04 CLOSED (see OPR-04 entry)

**Documentation created**:
- `audit/notation/OPR02_ROBIN_OCCURRENCES.md` — occurrence table
- `audit/evidence/OPR02_DERIVATION_CHAIN.md` — full derivation chain + closure gates
- `audit/evidence/OPR02_CLOSURE_REPORT.md` — closure verdict

**Blocks**:
- E-CH10-Dc-* (BC-dependent claims)
- E-CH13-Der-004 to E-CH13-Der-010 (partial — structure proven, value conditional)
- E-CH14-Dc-* (BVP eigenvalue claims)

**Where it appears in Book2**:
- CH10:99 (first use, teleported)
- CH11: G_F derivation
- CH13: OPR-20 closure attempts (F, G, H, H2)
- CH14: BVP work package

**Upgrade condition to CLOSED**:
1. OPR-04 CLOSED — derive δ = R_ξ from brane microphysics, OR
2. λ̃ derivation — BKT coefficient from membrane stiffness/conductivity
Either route removes the remaining [P] dependency.

**Closure test**:
CLOSED iff α appears as boundary term coefficient in δS = 0 variation WITHOUT any postulated parameter, i.e., purely [Der].

**No-smuggling note**:
α cannot be fitted to match a desired eigenvalue; must emerge from action principle. Current status is no-smuggling compliant: no SM values (M_W, G_F, etc.) used to determine α.

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

**Status**: OPEN (Forensic audit complete 2026-01-25)

**Blocks OPR-02 Route C upgrade**: δ = R_ξ is [P], cannot upgrade until this OPR closes.

**Definitions** (exist but teleported):
- **δ**: Boundary-layer / brane thickness — scale over which Robin BC smooths sharp junction
- **R_ξ**: Diffusion / correlation length — ~10⁻³ fm, anchored to M_Z = ℏc/M_Z

**Symbol collision warning**: δ also denotes CP phase in CKM/PMNS. Context-dependent.

**What exists in Book 2**:
- R_ξ formal definition: [Dc] in Framework v2.0 (correlation length)
- R_ξ numerical value: [BL]+[P] (anchored to M_Z phenomenologically)
- δ = R_ξ identification: [P] in §13.2.8-13.2.11 (Attempts H, H2, H2-plus)
- Three comprehensive audits already in Book 2

**What is MISSING (all OPEN)**:
- Gate (i): Derive R_ξ from 5D action (no M_Z input)
- Gate (ii): Boundary-layer formal theorem (δ = f(R_ξ))
- Gate (iii): Unique-scale proof (R_ξ is only sub-EW scale)
- Gate (iv): δ-robustness demonstration (physics insensitive to ±factor 2)

**Documentation created**:
- `audit/notation/OPR04_DELTA_RXI_OCCURRENCES.md` — occurrence table
- `audit/evidence/OPR04_DERIVATION_CHAIN.md` — derivation chain + proof obligations

**Derivation routes attempted**:
- Route A (Diffusion → BL theorem → δ): BLOCKED — no formal theorem
- Route B (Junction → Robin → scale ID): PARTIAL — final step is [P]
- Route C (S¹ geometry → δ ~ R): PARTIAL — identification not unique

**Blocks**:
- E-CH10-Dc-* (claims using brane thickness)
- E-CH11-Dc-* (G_F derivation uses δ in ℓ/δ ratio)
- All claims involving Robin parameter α ~ ℓ/δ
- **OPR-02**: α = ℓ/δ = 2π requires δ = R_ξ

**Where it appears in Book2**:
- CH10:104,112 (first use, teleported)
- CH11: G_F derivation
- CH13 §13.2.8: Attempt H (introduces δ = R_ξ as [Def])
- CH13 §13.2.10: Attempt H2-plus (strict audit → [P])
- CH13 §13.2.11: Attempt H2 Hard (rigorous provenance)

**Closure test**:
CLOSED iff ONE of Gates (i)-(iv) is satisfied AND δ has explicit definition before first use.

**No-smuggling note**:
- δ cannot be chosen to make eigenvalues "come out right"
- R_ξ value uses M_Z [BL] — this is documented, not hidden
- Current status is no-smuggling compliant: [P] tag is explicit

### OPR-04 Update: Kink Width Derivation (2026-01-25)

**New content in Chapter 16**:
- Δ = 2/(v√λ) derived from λφ⁴ kink profile [M]
- BPS constraint: σΔ = 4v²/3 [M]
- Connection to OPR-01: M₀² = (3y²/4)σΔ [Dc]
- Code validation: `code/opr04_delta_consistency_check.py`

**CONDITIONAL TENSION** (under assumption ℓ = nΔ with n small):

| Source | Δ Value | μ = M₀ℓ | N_bound |
|--------|---------|---------|---------|
| δ = R_ξ (OPR-04 ID) | ~2×10⁻³ fm | ~0.002 (if n~4) | << 3 |
| μ ∈ [25,35] (OPR-21) | ~1-4 fm | 25-35 | = 3 |

**Important**: This tension appears ONLY under the joint assumptions:
1. Δ = δ (kink width = boundary-layer scale)
2. δ = R_ξ (boundary-layer = diffusion scale)
3. ℓ = nΔ with modest n ~ O(1)

**The OPR-21 constraint is μ = M₀ℓ, NOT M₀Δ directly.**

If ℓ ≫ Δ (i.e., domain size much larger than kink width), then μ can reach
the [25,35] window even with Δ ~ R_ξ ~ 10⁻³ fm.

**Resolution paths** (all remain viable):
1. δ ≠ Δ — boundary-layer scale may differ from kink width [P]
2. n ≫ 4 — domain size may be much larger than assumed [P]
3. Derive ℓ independently from 5D action (not as n×Δ)
4. Revisit σ/y combinations that shift the required Δ

**Status**: OPEN — conditional tension documented, resolution paths identified.

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

**Status**: STRONG PARTIAL (Updated 2026-01-25)

**Progress**:
- 2 REPRO scripts complete in `repro/scripts/`:
  - `repro_sin2_z6_verify.py` → E-CH11-Der-005, E-CH11-Der-013
  - `repro_sin2_rg_running.py` → E-CH04-Dc-012 (SUPPORTING)
- 1 REPRO stub: `code/repro/repro_i4_overlap_stub.py` (blocked by OPR-21)
- Verification infrastructure: `run_all.sh`, `tools/repro_gate.py`
- Checksums recorded in `repro/output/checksums.sha256`

**Closure criteria met**:
- ✅ At least 1 REPRO script with claim mapping
- ✅ Deterministic outputs with SHA256 hashes
- ✅ Gate script for verification
- ✅ Manifest documenting script → claim → output

**Remaining for CLOSED**:
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

**Status**: CLOSED (Updated 2026-01-25)

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

## OPR-09 [L] π prefactor derivation

**Short name**: Derive the π prefactor in candidate electron mass formula

**Status**: OPEN

**Missing**:
- The candidate formula m_e = π√(ασΔℏc) uses π as a geometric prefactor
- This π is postulated, not derived from action or boundary conditions
- Possible routes: WKB phase quantization, defect geometry, mode normalization

**Blocks**:
- E-CH05-P-001 (electron mass candidate)

**Where it appears in Book2**:
- CH05 §5.1 (eq:electron_candidate)

**Minimum closure deliverable**:
1. Explicit integral or phase calculation producing π
2. Connection to thick-brane potential V(z) or WKB ground state
3. Derivation without fitting to m_e value

**Closure test**:
CLOSED iff π appears as output of a definite integral (e.g., ∫₀^∞ ... dz = π) or quantization condition with explicit assumptions.

**No-smuggling note**:
π cannot be chosen to make m_e come out right; must emerge from geometry.

---

## OPR-10 [L] (3/2) factor from Z₆

**Short name**: Derive the (3/2) = |Z₃|/|Z₂| factor in muon/electron ratio

**Status**: OPEN

**Missing**:
- The candidate ratio m_μ/m_e = (3/2)/α uses (3/2) as group-theoretic input
- This is suggestive (Z₆ ≃ Z₂×Z₃ structure) but not derived from energetics
- No action-level or oscillator-spectrum derivation exists

**Blocks**:
- E-CH05-P-004 (muon/electron ratio candidate)

**Where it appears in Book2**:
- CH05 §5.2 (eq:muon_ratio_candidate)

**Minimum closure deliverable**:
1. Show that Z₆ mode spectrum gives (3/2) mass ratio factor
2. OR derive from oscillator harmonic structure in ξ-dimension
3. Connection to group representation theory energetics

**Closure test**:
CLOSED iff (3/2) = |Z₃|/|Z₂| emerges from mode-counting or energy-level theorem with explicit Z₆ structure.

**No-smuggling note**:
(3/2) cannot be fitted from observed masses; must come from Z₆ mathematics.

---

## OPR-11 [L] Koide Q = 2/3 energetics

**Short name**: Derive the Koide constraint Q = 2/3 from Z₆ energy minimization

**Status**: OPEN

**Missing**:
- Koide relation Q = (m_e+m_μ+m_τ)/(√m_e+√m_μ+√m_τ)² = 2/3 holds empirically
- Identification Q = |Z₂|/|Z₃| is suggestive but not derived
- No energetic argument shows why D/A = √2 ratio is forced

**Blocks**:
- E-CH05-P-005 (Koide constraint)
- E-CH05-P-006 (Z₆ identification)

**Where it appears in Book2**:
- CH05 §5.3 (eq:koide_ch4, eq:koide_z6)

**Minimum closure deliverable**:
1. Show Z₆ energy functional has minimum at Q = 2/3
2. Derive D/A = √2 from mode degeneracy or symmetry
3. Prove Q = |Z₂|/|Z₃| is not coincidence but structural

**Closure test**:
CLOSED iff Q = 2/3 emerges from energy minimization with Z₆ symmetry constraint.

**No-smuggling note**:
Q value cannot be imposed; must be output of variational principle.

---

## OPR-12 [L] KK tower truncation / V(ξ) potential

**Short name**: Derive thick-brane potential V(ξ) and show n≥3 modes are unstable

**Status**: OPEN

**Missing**:
- The effective potential V(ξ) that determines mode localization is not derived
- No WKB action S_n calculation for mode lifetimes exists
- No proof that modes n=0,1,2 are stable while n≥3 are unstable/non-normalizable

**Blocks**:
- E-CH06-P-004 (KK truncation mechanism)
- E-CH06-I-002 (mode indices n=0,1,2)
- All claims depending on "exactly three generations" from dynamics

**Where it appears in Book2**:
- CH06 §5.4 Mechanism B (eq:ch5_lifetime, eq:ch5_truncation_cond)

**Minimum closure deliverable**:
1. Derive V(ξ) from EDC thick-brane action
2. Compute WKB action S_n for n = 0,1,2,3,4
3. Show τ₀, τ₁, τ₂ ≫ t_obs while τ₃ < t_Planck
4. OR show n≥3 modes are non-normalizable (different argument)

**Closure test**:
CLOSED iff explicit calculation shows exactly 3 stable modes from V(ξ) derived from EDC geometry.

**No-smuggling note**:
Cannot assume V(ξ) has 3 minima; must derive it. Cannot fit barrier height to make 3 modes stable.

---

## OPR-13 [N] PMNS mixing angles derivation

**Short name**: Derive PMNS mixing angles from EDC geometry

**Status**: OPEN (YELLOW partial — θ₂₃ derived, θ₁₂/θ₁₃ identified)

**Missing**:
- θ₂₃ ≈ 45° derived from Z₆ geometry (Attempt 2) [Dc] ← CLOSED
- θ₁₂ structure identified (rank-2 baseline) but value not derived [I]
- θ₁₃ structure identified (reactor perturbation ε = λ/√2) but origin not derived [I]
- No first-principles calculation of θ₁₂⁰ or ε from EDC action

**Blocks**:
- E-CH07-Dc-* (PMNS angle claims)
- All claims depending on PMNS matrix derivation

**Where it appears in Book2**:
- CH07: Neutrinos as Edge Modes (Attempts 1-4)
- Attempt 2: Z₆ overlap model (θ₂₃ derivation)
- Attempt 4: Rank-2 + ε structure (θ₁₂, θ₁₃ identified)

**Minimum closure deliverable**:
1. Geometric derivation of θ₁₂⁰ from Z₆ structure
2. Derive ε = λ/√2 from boundary conditions or overlap integrals
3. Show CP phase δ emerges from Z₂ selection

**Closure test**:
CLOSED iff all three PMNS angles are derived from EDC geometry without fitting to observed values.

**No-smuggling note**:
Cannot fit angles to PDG values; must derive from geometry.

---

## OPR-14 [N] CP phase δ derivation

**Short name**: Derive CP-violating phase δ from EDC structure

**Status**: OPEN (RED)

**Missing**:
- No mechanism for complex phases in PMNS matrix identified
- δ ≈ 60° (observed) not explained
- Connection to Z₂ matter/antimatter distinction unclear

**Blocks**:
- E-CH07-Dc-* (CP phase claims)
- Any claim about CP violation origin in neutrino sector

**Where it appears in Book2**:
- CH07: Neutrinos as Edge Modes (line 620)
- Not addressed in any Attempt (1-4)

**Minimum closure deliverable**:
1. Identify source of complex phases in overlap integrals
2. Connect to Z₂ or Z₆ structure
3. Derive δ value or range

**Closure test**:
CLOSED iff CP phase δ emerges from EDC geometry with explicit mechanism.

**No-smuggling note**:
Cannot postulate δ = 60°; must derive from structure.

---

## OPR-15 [N] Dirac/Majorana determination

**Short name**: Determine if EDC neutrinos are Dirac or Majorana

**Status**: OPEN (RED)

**Missing**:
- Edge-mode ontology accommodates both Dirac and Majorana
- No mechanism distinguishes between the two
- No prediction for neutrinoless double-beta decay

**Blocks**:
- E-CH07-Dc-* (neutrino nature claims)

**Where it appears in Book2**:
- CH07: Neutrinos as Edge Modes, §6.8 (line 658-686)

**Minimum closure deliverable**:
1. Determine if edge-mode self-conjugacy is forced or forbidden
2. Predict Majorana mass scale if applicable
3. State falsifiable prediction for 0νββ decay

**Closure test**:
CLOSED iff EDC predicts either Dirac or Majorana with testable consequence.

**No-smuggling note**:
Cannot claim both compatible as "prediction"; must commit to one or derive distinguishing observable.

---

## OPR-16 [H] Pion mass/lifetime

**Short name**: Derive pion mass and lifetime from EDC geometry

**Status**: OPEN

**Missing**:
- No EDC mechanism for pion as bound quark state
- m_π and τ_π not addressed in current framework
- Requires quark confinement mechanism from 5D

**Blocks**:
- E-CH08-case-pion claims

**Where it appears in Book2**:
- 08_case_pion.tex:101 (mentioned as not attempted)

**Minimum closure deliverable**:
1. EDC model for quark confinement
2. Pion as qq̄ bound state in 5D
3. Derive m_π, τ_π from geometry

**Closure test**:
CLOSED iff pion properties emerge from EDC geometry without QCD input.

---

## OPR-17 [G] SU(2)_L gauge embedding

**Short name**: Derive or postulate SU(2)_L as brane-localized vs bulk gauge

**Status**: OPEN

**Missing**:
- Where/how SU(2)_L is embedded in 5D geometry
- Brane-localized vs bulk gauge choice
- Origin of gauge coupling from 5D action

**Blocks**:
- E-CH09-Dc-* (V-A structure depends on gauge ontology)
- E-CH10-Dc-* (electroweak bridge)
- OPR-20a (mediator identity)

**Where it appears in Book2**:
- 09_va_structure.tex:1050-1127 (main discussion)
- ch10_electroweak_bridge.tex:43, 309, 483
- ch11_opr20_attemptH1_mediator_identity.tex (extensive references)

**Minimum closure deliverable**:
1. Decide: brane-localized SU(2)_L or bulk gauge
2. Derive coupling normalization from 5D action
3. Connect to W/Z mass generation

**Closure test**:
CLOSED iff SU(2)_L embedding is derived from manifold structure.

---

## OPR-18 [M] CKM/PMNS from overlaps

**Short name**: Derive mixing matrices from generational mode overlaps

**Status**: OPEN

**Missing**:
- CKM matrix from quark mode overlaps
- PMNS matrix from lepton mode overlaps
- Phase origins (CP violation)

**Blocks**:
- E-CH07-Dc-* (CKM claims)
- OPR-13 (PMNS angles - related)

**Where it appears in Book2**:
- 09_va_structure.tex:1130
- 07_ckm_cp.tex (implicit dependency)

**Minimum closure deliverable**:
1. Overlap integral calculation for 3 generations
2. Derive CKM angles from geometry
3. Connect to CP phases

**Closure test**:
CLOSED iff CKM/PMNS elements emerge from mode overlap integrals.

---

## OPR-19 [G] g₅ value from 5D action

**Short name**: Derive the 5D gauge coupling g₅ from action normalization

**Status**: CONDITIONAL [Dc] (Updated 2026-01-25)

**Sprint completed**: book2-opr19-g5-derivation-v1

**What is derived [Dc]**:
- Dimensional reduction formula: 1/g₄² = (1/g₅²) ∫₀^ℓ dξ |f_n(ξ)|²
- Warp factor cancellation for F_μν F^μν term: √(-G) · G^{μα} G^{νβ} = 1
- Weight function W(ξ) = 1 (flat measure)
- Dimensional analysis: [g₅] = L^{1/2}, [g₄] = 1

**Derivation source**:
- 5D gauge action with canonical normalization [M]
- Warped metric ansatz ds² = e^{2A(ξ)} η_μν dx^μ dx^ν + dξ² [P]
- KK mode decomposition [Dc]

**Parameters (remain [P] postulated)**:
- A(ξ) = warp factor
- ℓ = domain size
- f_n(ξ) = mode profiles (conditional on BVP boundary conditions)

**Documentation created (2026-01-25)**:
- `src/sections/ch17_opr19_g5_from_action.tex` — Book chapter derivation
- `audit/evidence/OPR19_G5_DERIVATION_REPORT.md` — Evidence chain + failure modes
- `canon/opr/OPR-19.md` — Canonical OPR document
- `code/opr19_g5_sanity.py` — Dimensional consistency sanity script

**Blocks**:
- E-CH08-P-004 (G₅ coupling)
- E-CH11-Dc-* (G_F mode overlap pathway)
- OPR-22 (first-principles G_F)

**Where it appears in Book2**:
- **NEW**: CH17 (OPR-19 derivation section) — src/sections/ch17_opr19_g5_from_action.tex
- 11_gf_derivation.tex:438-468 (main discussion)
- CH3_electroweak_parameters.tex:704, 726

**Closure test**:
OPR-19 is CLOSED iff dimensional reduction formula is derived ✓
AND warp factor handling is explicit ✓
AND no SM observables used as inputs ✓

**Current status: CONDITIONAL [Dc]**
- Condition: Warped metric ansatz A(ξ) [P]
- Condition: Domain size ℓ [P]
- Condition: Mode profiles f_n(ξ) depend on BVP (OPR-21)

**Remaining for full [Der]**:
1. Derive A(ξ) from brane-bulk matching (OPEN-19-1)
2. Derive ℓ from first principles (OPEN-19-2)
3. Include brane-localized kinetic terms if present (OPEN-19-3)

**No-smuggling certification**: ✓ PASS
- Grep verification: No M_W, G_F, v=246GeV, sin²θ_W in derivation
- Only used: 5D gauge action [M] + warped metric ansatz [P] + KK decomposition [Dc]

---

## OPR-20 [G] Mediator mass from ξ-geometry

**Short name**: Derive mediator mass m_med from Sturm-Liouville eigenvalue problem

**Status**: CONDITIONAL [Dc] (Updated 2026-01-25)

**Sprint completed**: book2-opr20-mediator-mass-v1

**What is derived [Dc]**:
- Sturm-Liouville equation from 5D gauge action: -d²f_n/dξ² + V(ξ)f_n = m_n²f_n
- Dimensionless eigenvalue **definition**: x_n := m_n·ℓ  ⟺  m_n = x_n/ℓ
- **Critical**: x_n = x_n(κ, V) depends on BVP solution — NOT a universal formula
- Mediator mass definition: m_med = m_1 (first massive mode)
- Effective contact strength: C_eff = g_5² ℓ / x_1² (invariant structure)
- Connection to OPR-19: g_4² = g_5²/ℓ from mode normalization ∫|f|²dξ = ℓ

**Derivation source**:
- 5D gauge action [M] (standard field theory)
- Warped metric ansatz [P] with warp cancellation from OPR-19
- KK mode decomposition [Dc]
- Sturm-Liouville theory [M]

**Parameters (remain [P] postulated)**:
- V(ξ) = effective potential
- ℓ = domain size
- κ₀, κ_ℓ = Robin BC parameters

**Documentation created (2026-01-25)**:
- `src/sections/ch18_opr20_mediator_mass_from_eigenvalue.tex` — Book chapter derivation
- `audit/evidence/OPR20_MEDIATOR_MASS_DERIVATION_REPORT.md` — Evidence chain + failure modes
- `canon/opr/OPR-20.md` — Canonical OPR document
- `code/opr20_mediator_mass_sanity.py` — Numerical sanity script

**Blocks**:
- E-CH08-Dc-002 (L_eff structure)
- E-CH10-Dc-* (electroweak bridge)
- OPR-22 (first-principles G_F)

**Where it appears in Book2**:
- **NEW**: CH18 (OPR-20 derivation section) — src/sections/ch18_opr20_mediator_mass_from_eigenvalue.tex
- 11_gf_derivation.tex:495-499, 606
- ch10_electroweak_bridge.tex (main discussion)

**Closure test**:
OPR-20 is CLOSED iff Sturm-Liouville eigenvalue structure is derived ✓
AND mass formula m_n = x_n/ℓ is established ✓
AND no SM observables used as inputs ✓

**Current status: CONDITIONAL [Dc]**
- Condition: Potential V(ξ) [P] — not derived from action
- Condition: Domain size ℓ [P] — not derived
- Condition: BC parameters κ [P] — structural form from OPR-21, value [P]

**Remaining for full [Der]**:
1. Derive V(ξ) from 5D action (gauge analog of OPR-21 L2) — OPEN-20-1
2. Derive BC parameter κ from Israel junction for gauge field — OPEN-20-2
3. Derive ℓ from first principles — OPEN-20-3 (shared with OPR-19)

**No-smuggling certification**: ✓ PASS
- Grep verification: No M_W, G_F, v=246GeV, sin²θ_W in derivation
- Only used: 5D gauge action [M] + Sturm-Liouville theory [M] + OPR-19 infrastructure

---

## OPR-21 [B] BVP mode profiles

**Short name**: Solve boundary value problem for fermion localization

**Status**: STRONG PARTIAL (infrastructure complete, physics inputs OPEN)

**Completed (2026-01-25)**:
- L1: Domain definition — ESTABLISHED [M]
- L3: Robin BC form — ESTABLISHED [M]
- L4: Sturm-Liouville self-adjointness — ESTABLISHED [M]
- L5: Toy model validation — ESTABLISHED [M]
- Infrastructure: `code/opr21_bvp_demo.py` validated

**Still missing**:
- L2: V(ξ) derivation from 5D action — OPEN
- L3.2: BC parameter derivation from Israel junction — OPEN
- Physical N_bound computation — OPEN (blocked by L2)

**Blocks**:
- E-CH08-OPEN-003 (mode profiles)
- E-CH08-P-003 (mode overlap mechanism)
- OPR-22 (first-principles G_F)

**Where it appears in Book2**:
- 11_gf_derivation.tex:501-519, 577, 607
- ch12_bvp_workpackage.tex (setup)
- ch14_bvp_closure_pack.tex (detailed work)
- canon/opr/OPR-21.md (lemma chain)

**Deliverables created (2026-01-25)**:
1. `canon/opr/OPR-21.md` — Lemma chain document
2. `code/opr21_bvp_demo.py` — Infrastructure validation script
3. `audit/evidence/OPR21_BVP_FOUNDATION_REPORT.md` — Sprint report

**Minimum closure deliverable**:
1. Derive V(ξ) from EDC action (complete L2)
2. Derive BC parameters from Israel junction (complete L3.2)
3. Solve BVP numerically with physical inputs
4. Show N_bound = 3 robustly

**Closure test**:
CLOSED iff numerical mode profiles are computed for derived V(ξ) and I₄ is determined.

---

## OPR-22 [C] First-principles G_eff

**Short name**: Derive effective contact strength G_eff from 5D mediator exchange

**Status**: CONDITIONAL [Dc] (Updated 2026-01-25)

**Sprint completed**: book2-opr22-geff-derivation-v1

**What is derived [Dc]**:
- Effective 4D coupling: g_eff,n = g₅ f_n(0) for brane-localized current
- Four-fermion operator from integrating out first massive mode
- G_eff = g₅² ℓ |f₁(0)|² / (2 x₁²) in natural normalization
- Connection to OPR-20: G_eff = (1/2) C_eff |f₁(0)|²
- Dimensional verification: [G_eff] = L² = GeV⁻²

**Key distinction**: G_eff is the EDC-computed quantity; G_F is the measured value [BL]. We derive G_eff without using G_F as input.

**Derivation source**:
- 5D gauge-fermion action [M]
- KK mode decomposition [Dc]
- Brane-localized current ansatz [P] (Working Default)
- OPR-19 normalization + OPR-20 eigenvalue structure [Dc]

**Parameters (remain [P] postulated)**:
- g₅ = 5D gauge coupling
- ℓ = domain size
- V(ξ) = effective potential
- κ₀, κₗ = Robin BC parameters

**Documentation created (2026-01-25)**:
- `src/sections/ch19_opr22_geff_from_exchange.tex` — Book chapter derivation
- `audit/evidence/OPR22_GEFF_DERIVATION_REPORT.md` — Evidence chain + conventions
- `canon/opr/OPR-22.md` — Canonical OPR document
- `code/opr22_geff_sanity.py` — Dimensional consistency sanity script

**Blocks**:
- All quantitative G_F claims (now upgraded to CONDITIONAL [Dc])

**Where it appears in Book2**:
- **NEW**: CH19 (OPR-22 derivation section) — src/sections/ch19_opr22_geff_from_exchange.tex
- 11_gf_derivation.tex:568, 578, 608, 633 (legacy references)

**Depends on**:
- OPR-19 (g₅ → g₄ reduction) — CONDITIONAL [Dc]
- OPR-20 (mediator mass m₁ = x₁/ℓ) — CONDITIONAL [Dc]
- OPR-21 (BVP profiles, f₁(0)) — STRONG PARTIAL

**Closure test**:
OPR-22 is CLOSED iff G_eff is derived from 5D action ✓
AND no SM observables used as inputs ✓
AND dimensional analysis verified ✓

**Current status: CONDITIONAL [Dc]**
- Condition: g₅ value [P]
- Condition: ℓ value [P]
- Condition: V(ξ) and BC parameters [P]
- Condition: Brane-localized current [P] (WD)

**Remaining for full [Der]**:
1. ~~Extract f₁(0) from BVP (OPEN-22-1)~~ **RESOLVED** (2026-01-25)
2. Derive g₅ from UV completion (OPEN-22-2)
3. Derive ℓ from first principles (OPEN-22-3)
4. Compute f₁(0) for physical V(ξ) (OPEN-22-4) — PARTIAL (toy verified)
5. Include brane kinetic term corrections (OPEN-22-5)

**OPEN-22-1 Resolution** (2026-01-25):
- Brane amplitude extraction: |f₁(0)|² now computed from BVP mode profiles
- Normalization bridge: Natural ↔ Unit conversion documented
- Toy limit verified: |f₁(0)|² = 2.002 vs expected 2.0 (0.1% error)
- Evidence: `code/opr22_f1_brane_amplitude_extract.py`, `code/output/opr22_f1_brane_amplitude_report.md`

**No-smuggling certification**: ✓ PASS
- Grep verification: No M_W, G_F, v=246GeV, sin²θ_W in derivation
- Only used: 5D action [M] + KK decomposition [Dc] + brane localization [P]

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
| OPR-09 | ~3 (π-dependent in CH05) |
| OPR-10 | ~3 ((3/2)-dependent in CH05) |
| OPR-11 | ~3 (Koide-dependent in CH05) |
| OPR-12 | ~8 (KK truncation in CH06) |
| OPR-13 | ~10 (PMNS angles in CH07) |
| OPR-14 | ~3 (CP phase in CH07) |
| OPR-15 | ~2 (Dirac/Majorana in CH07) |
| OPR-16 | ~3 (pion properties) |
| OPR-17 | ~57 (gauge embedding) |
| OPR-18 | ~15 (mixing matrices) |
| OPR-19 | ~20 (g₅ coupling) |
| OPR-20 | ~25 (mediator mass) |
| OPR-21 | ~30 (BVP profiles) |
| OPR-22 | ~10 (first-principles G_F) |

*Note: Claims may be blocked by multiple OPRs. Exact crosswalk in OPR_CLAIM_CROSSWALK.md*

---

*Registry is CANON. Amendments require branch + review + merge.*
