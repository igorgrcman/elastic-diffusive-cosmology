# n(A) MAPPING RESEARCH: Coordination as Function of Mass Number

**Created**: 2026-01-31
**Purpose**: Research file for OQ-V3-001 (KINGPIN question)
**Status**: [Open] — no definitive formula found in sources

---

## The Problem

**Question**: What is the coordination number n as a function of mass number A?

**Why critical (kingpin)**:
- LAW-3 (G-N law) contains ε_f term
- ε_f likely depends on n(A) via d(n)
- Without n(A), cannot calculate ε_f(A)
- Cannot verify decay chain predictions
- Cannot predict branching ratios

---

## What Sources Say

### DN-010: Nuclear Saturation Value
**File**: 22826edd_full.md:11793-11830
**Content**: n_opt ≈ 43.3 at saturation density ρ₀ ≈ 0.16 fm⁻³

**Implication**: At equilibrium density, average coordination is ~43

### DN-011: Forbidden Optimum
**File**: 22826edd_full.md:11831-11856
**Content**: 43 is prime, hence forbidden

**Implication**: Nuclei at saturation are inherently frustrated

### No explicit n(A) formula found
**Grep results**: No matches for "n(A) =" or explicit functional form

---

## Candidate Formulas [P]

### Candidate 1: Density-Based Scaling

**Formula**:
```
n(A) = n₀ × (ρ(A)/ρ₀)^(1/3)
```

**Assumptions**:
- n scales with coordination shell size
- ρ(A) = nuclear density for nucleus A
- n₀ ≈ 43 at saturation

**Problems**:
- Nuclear density nearly constant for A > 20
- Would predict n ≈ constant ≈ 43 for all heavy nuclei
- Doesn't explain why some are stable

**Status**: [P] — plausible but problematic

---

### Candidate 2: Geometric Scaling

**Formula**:
```
n(A) = c × A^(1/3)
```

**Rationale**:
- Nuclear radius R ∝ A^(1/3)
- Surface effects scale with A^(2/3)
- Interior coordination might scale differently

**Calibration attempt**:
- If n(208) = 36 (Pb stable because allowed)
- Then c = 36 / 208^(1/3) ≈ 36 / 5.93 ≈ 6.1
- n(238) = 6.1 × 238^(1/3) ≈ 6.1 × 6.20 ≈ 38

**Check**: n(238) ≈ 38 would be forbidden (2 × 19), consistent with U-238 being unstable

**Status**: [P] — interesting, needs verification

---

### Candidate 3: Isospin-Dependent

**Formula**:
```
n(A, Z) = f(A) + g(N-Z)
```

**Rationale**:
- Neutron excess (N-Z) affects nuclear shape
- Shape affects coordination
- β-decay changes N-Z, hence n

**Problems**:
- No source support for this form
- Adds free parameter g

**Status**: [P] — speculative

---

### Candidate 4: Shell-Corrected

**Formula**:
```
n(A) = n_bulk(A) + Δn_shell(Z, N)
```

**Rationale**:
- Magic numbers (Z or N = 2, 8, 20, 28, 50, 82, 126) affect structure
- Shell closure might modify coordination
- Explains why Pb isotopes are stable

**Problems**:
- Requires shell correction table
- Mixes EDC with conventional nuclear physics

**Status**: [P] — plausible hybrid approach

---

## Constraints from Observations

### Constraint 1: Heavy nuclei unstable
If A > 209 and stable, rare → n(A>209) likely forbidden

### Constraint 2: Pb isotopes stable
²⁰⁶Pb, ²⁰⁷Pb, ²⁰⁸Pb all stable → n(206), n(207), n(208) ≈ 36?

### Constraint 3: Primordial nuclei
²³²Th, ²³⁵U, ²³⁸U have t₁/₂ ~ 10⁹ y → deep forbidden but metastable

### Constraint 4: α-decay ΔA = 4
Each α-decay removes 4 mass units
If n(A) = c × A^(1/3), then Δn ≈ c × (1/3) × A^(-2/3) × 4 ≈ small
Need Δn ≈ 1-2 per α-decay to explain chain progression

---

## Test: Candidate 2 Against Decay Chain

Using n(A) = 6.1 × A^(1/3):

| Nuclide | A | A^(1/3) | n(A) | Nearest Allowed | d(n) |
|---------|---|---------|------|-----------------|------|
| ²³⁸U | 238 | 6.20 | 37.8 | 36 | 1.8 |
| ²³⁴Th | 234 | 6.16 | 37.6 | 36 | 1.6 |
| ²³⁰Th | 230 | 6.13 | 37.4 | 36 | 1.4 |
| ²²⁶Ra | 226 | 6.09 | 37.2 | 36 | 1.2 |
| ²²²Rn | 222 | 6.06 | 36.9 | 36 | 0.9 |
| ²¹⁸Po | 218 | 6.02 | 36.7 | 36 | 0.7 |
| ²¹⁴Po | 214 | 5.98 | 36.5 | 36 | 0.5 |
| ²¹⁰Po | 210 | 5.94 | 36.3 | 36 | 0.3 |
| ²⁰⁶Pb | 206 | 5.91 | 36.0 | 36 | 0.0 |

**Result**: With c = 6.1, chain smoothly approaches n = 36 at ²⁰⁶Pb!

**Consistency check**:
- d(n) decreases monotonically ✓
- Endpoint exactly at allowed value ✓
- Explains why chain terminates at Pb ✓

---

## Upgrade Checklist

### [P] → [I]: What would count as inference?

1. Test Candidate 2 against all three chains
2. Check if n(207) ≈ 36 and n(208) ≈ 36
3. See if d(n) correlates with t₁/₂
4. See if branching ratios match d(n) predictions

### [I] → [Der]: What would count as derivation?

1. Derive c = 6.1 from first principles
2. Show why n ∝ A^(1/3) from M-topology
3. Connect to nuclear density ρ(A)
4. Explain shell corrections topologically

---

## Recommended Next Steps

1. **Calculate n(A) for Th-232 and U-235 chains** using Candidate 2
2. **Test d(n) vs lifetime** for α-emitters
3. **Check branching** at ²¹²Bi: does d(n) predict 64:36?
4. **Refine coefficient c** if needed

---

## Current Best Estimate [P]

```
n(A) ≈ 6.1 × A^(1/3)

With:
  n(206) ≈ 36 (allowed)
  n(238) ≈ 38 (forbidden)
  d(n) decreasing along decay chains
```

**Status**: [P] — promising candidate, needs verification
**Confidence**: Medium (consistent with one chain, untested on others)
