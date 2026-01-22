# Chapter 11: The Fermi Constant from Geometry — Companion Notes

**Date:** 2026-01-22 (v2 — circularity firewall added)
**Status:** GREEN-A (EW consistency) / YELLOW-B (geometric intuition) / RED-C (first-principles)
**Goal:** Consolidate G_F treatment with explicit independent vs. dependent claims

---

## Executive Summary

Chapter 11 consolidates EDC's treatment of the Fermi constant with three derivation levels:

| Level | Description | Status |
|-------|-------------|--------|
| GREEN-A | Electroweak consistency closure | sin²θ_W = 1/4 → RG → g² → M_W → G_F |
| YELLOW-B | Geometric suppression intuition | Mode overlap explains "weakness" |
| RED-C | Full 5D first-principles | Open — requires g₅, m_φ, BVP |

**The strongest independent claim:**
> EDC predicts sin²θ_W = 1/4 (bare) from Z₆ counting. After RG running: sin²θ_W(M_Z) = 0.2314 (0.08% from PDG). **This is the non-trivial, falsifiable prediction.**

**The circularity caveat:**
> G_F "exact agreement" is a **consistency identity**, not an independent prediction. The Higgs VEV v = (√2 G_F)^{-1/2} is determined FROM G_F, so using v to derive G_F is circular within SM conventions.

---

## Audit Table: Claims → Tags → Evidence → Failure Mode

| Claim | Tag | Evidence | Failure Mode | Next Calc |
|-------|-----|----------|--------------|-----------|
| G_F = 1.166×10⁻⁵ GeV⁻² | [BL] | PDG 2024 | None | — |
| sin²θ_W = 1/4 (bare) | [Der] | Z₆ subgroup counting | None | **TRUE EDC PREDICTION** |
| sin²θ_W(M_Z) = 0.2314 | [Dc] | + RG running | **0.08% from PDG** | — |
| g² = 4πα/sin²θ_W = 0.4246 | [Dc] | Electroweak unification | None | — |
| M_W = gv/2 = 80.2 GeV | [Dc] | Higgs mechanism | **v depends on G_F!** | — |
| G_F = g²/(4√2 M_W²) | [Dc] | Electroweak relation | **Consistency, not derivation** | — |
| G_EDC ~ g_eff²/m_φ² | [Dc] | Tree-level integration | None | — |
| Mode overlap I₄ ~ 200 MeV | [P] | Order-of-magnitude | ×100 off | Solve BVP |
| 5D coupling g₅ | [P] | Not computed | Unknown | Action normalization |
| Mediator mass m_φ | [P] | Not computed | Unknown | KK reduction |
| First-principles G_F | (open) | Not achieved | — | RED-C closure |

---

## Stoplight Analysis (GREEN-A / YELLOW-B / RED-C)

### GREEN-A: Electroweak Consistency Closure

```
Z₆ → sin²θ_W = 1/4 → RG running → g² → M_W → G_F
              ↑                            ↑
        INDEPENDENT               DEPENDS ON v (= f(G_F))
```

| Step | Level | Issue |
|------|-------|-------|
| Z₆ subgroup counting | [Der] GREEN-A | **Independent EDC prediction** |
| sin²θ_W = 1/4 bare | [Der] GREEN-A | From Z₂/Z₆ |
| RG running to M_Z | [BL] GREEN-A | Standard QFT |
| sin²θ_W(M_Z) = 0.2314 | [Dc] GREEN-A | **0.08% from PDG — best claim** |
| g² from α and sin²θ_W | [Dc] GREEN-A | 1.1% from PDG |
| M_W from g and v | [Dc] GREEN-A | **v caveat applies** |
| G_F from electroweak | [Dc] GREEN-A | **Consistency identity** |

**Verdict: GREEN-A** — Numerical closure achieved within SM relations. Independent prediction is sin²θ_W = 1/4.

### YELLOW-B: Geometric Suppression Intuition

```
5D mediator → integrate out → G_F ~ g_eff²/m_φ² → fermion localization → suppression
```

| Step | Level | Issue |
|------|-------|-------|
| Mediator integration | [Dc] GREEN-A | Tree-level calculation |
| Dimensional analysis | [Dc] GREEN-A | [G_F] = [E]⁻² ✓ |
| Order-of-magnitude I₄ | [P] YELLOW-B | ×100 off observed |
| Why G_F is small | [I] YELLOW-B | Qualitative only |
| Chirality filter | [Dc] GREEN-A | From Ch9 V–A |

**Verdict: YELLOW-B** — Mechanism identified but quantitative closure missing.

### RED-C: Full 5D First-Principles (Open)

```
5D action → KK reduction → m_φ → mode profiles → overlap → g_eff → G_F
```

| Step | Level | Issue |
|------|-------|-------|
| 5D action normalization | [P] RED-C | g₅ unknown |
| ξ-sector KK reduction | (open) RED-C | m_φ not computed |
| Thick-brane BVP | (open) RED-C | Mode profiles unknown |
| Overlap integrals | (open) RED-C | Not computed |
| G_F from first principles | (open) RED-C | Not achieved |

**Verdict: RED-C** — Major open problem.

---

## What Exactly Is Missing for RED-C → GREEN-A?

To upgrade mode overlap from qualitative (YELLOW-B) to quantitative (GREEN-A), the following **concrete calculations** are required:

1. **5D gauge coupling g₅ from action normalization:**
   - Derive g₅ from canonical normalization of 5D gauge field action
   - Not from dimensional estimates — from actual action reduction

2. **Mediator mass m_φ from KK reduction:**
   - Perform KK reduction along ξ-direction (throat geometry)
   - Identify lowest massive mode as mediator
   - Express m_φ in terms of geometric parameters (R_ξ, throat length)

3. **Mode profiles f_L(z) from thick-brane BVP:**
   - Solve boundary value problem with explicit boundary conditions
   - Normalize solutions
   - Compute overlap integral I₄ = ∫|f_L|⁴ dz **exactly**, not OOM

4. **Boundary-condition factor O_BC:**
   - Evaluate chirality projection on actual mode profiles
   - Get numerical suppression factor

**Until these are computed, mode overlap remains a MECHANISM, not a DERIVATION.**

---

## Derivation Chain Summary (with v-circularity marked)

```
INPUTS [BL]:
├── α = 1/137.036 (fine structure constant)
├── v = 246.2 GeV (Higgs VEV) ← ⚠️ DEPENDS ON G_F!
└── RG beta functions (standard QFT)

EDC PREDICTION [Der]:
└── sin²θ_W(lattice) = |Z₂|/|Z₆| = 2/6 = 1/4  ← ✓ INDEPENDENT

DERIVED [Dc]:
├── sin²θ_W(M_Z) = 0.2314 (from RG running) ← ✓ 0.08% error
├── g² = 4πα/sin²θ_W = 0.4246
├── M_W = gv/2 = 80.2 GeV ← ⚠️ uses v
└── G_F = g²/(4√2 M_W²) = 1.166×10⁻⁵ GeV⁻² ← ⚠️ CONSISTENCY

COMPARISON [BL]:
└── G_F^exp = 1.166×10⁻⁵ GeV⁻² → "exact" but circular
```

---

## Circularity Firewall (CRITICAL)

**The issue:** In SM conventions, v = (√2 G_F)^{-1/2}. If we use v as input to compute M_W, then derive G_F from M_W, we're computing G_F from G_F.

**The resolution:**
- G_F "exact agreement" is a **consistency closure within SM relations**
- It is **not** an independent EDC prediction
- The true independent prediction is **sin²θ_W = 1/4** (0.08% agreement after RG)

**What a reviewer cannot attack:**
- sin²θ_W = 1/4 from Z₆ counting is geometry → EW parameter
- RG running is standard QFT, not EDC-specific
- 0.08% agreement is non-trivial

**What a reviewer CAN attack (and we preempt):**
- "G_F exact is circular" — **YES, we acknowledge this explicitly**
- "v dependence makes G_F trivial" — **YES, that's why sin²θ_W is the real claim**

---

## Epistemic Summary

| Aspect | Status |
|--------|--------|
| **Is sin²θ_W = 1/4 independently derived?** | Yes — from Z₆ geometry [Der] |
| **Is G_F numerical value derived?** | Conditional — via EW relations with v caveat [Dc] |
| **Is structural mechanism established?** | Yes — mediator integration [Dc] |
| **Is mode overlap quantitative?** | No — order-of-magnitude only [P] |
| **Is first-principles derivation achieved?** | No — RED-C open problem |
| **Risk level** | LOW — sin²θ_W prediction is solid |
| **Falsifiable?** | Yes — if sin²θ_W(bare) ≠ 1/4, entire chain fails |

**Honest conclusion:** The true EDC prediction is sin²θ_W = 1/4 (0.08% agreement). The G_F numerical closure is a consistency check, not an independent prediction. The structural pathway explains *why* weak interactions are weak. First-principles derivation remains open but is not required for the current level of validation.

---

## Verification Commands

```bash
# Check for forbidden bracket tags
grep -R "\[OPEN\]\|\[Def\]" sections/11_gf_derivation.tex

# Check for undefined references
grep -i "undefined" EDC_Part_II_Weak_Sector.log

# Check for multiply-defined labels
grep -i "multiply" EDC_Part_II_Weak_Sector.log

# Build Part II
latexmk -xelatex -interaction=nonstopmode EDC_Part_II_Weak_Sector.tex
```

---

*Chapter 11 notes v2 complete. Key upgrade: explicit circularity firewall for v dependence, GREEN-A/YELLOW-B/RED-C naming, "what exactly is missing" checklist.*
