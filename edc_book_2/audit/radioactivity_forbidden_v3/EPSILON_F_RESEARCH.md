# ε_f(A) RESEARCH: Frustration Energy Functional Form

**Created**: 2026-01-31
**Purpose**: Research file for GAP-R1 (ε_f functional form)
**Depends on**: OQ-V3-001 (n(A) mapping)
**Status**: [Open] — blocked by n(A) question

---

## The Problem

**Question**: What is the frustration energy ε_f as a function of A?

**Context**: LAW-3 (G-N law) states:
```
log₁₀(t₁/₂) = a(Z/√Q_α) + c·ε_f + b
```

With c = -2.40 from fit (DN-017).

**Unknown**: The functional form ε_f(A)

---

## What Sources Say

### DN-015: G-N Formula
**File**: 22826edd_full.md:2555-2567
**Content**: ε_f appears in corrected G-N law

### DN-016: Fit Quality
**File**: 22826edd_full.md:2568-2580
**Content**: R² = 0.9941 with frustration term

### DN-017: Coefficients
**File**: 22826edd_full.md:2581-2610
**Content**: c = -2.40 (frustration coefficient)

**Gap**: No explicit ε_f(A) formula in sources

---

## Dependency Chain

```
ε_f(A) depends on d(n(A))  [GEN-2]
d(n) depends on n(A)       [GEN-1]
n(A) is unknown            [OQ-V3-001]
```

**Conclusion**: Must solve n(A) first (KINGPIN)

---

## Candidate Forms [P]

### Form 1: Linear in d(n)

**Formula**:
```
ε_f(A) = κ × d(n(A))
```

**Rationale**:
- Simplest ansatz
- Frustration proportional to distance from allowed

**Parameter**: κ has units of energy (MeV?)

**Status**: [P] — simplest guess

---

### Form 2: Power Law

**Formula**:
```
ε_f(A) = κ × d(n(A))^α
```

**Cases**:
- α = 1: Linear (Form 1)
- α = 2: Quadratic (harmonic potential)
- α = 1/2: Square root

**Status**: [P] — more general

---

### Form 3: Exponential

**Formula**:
```
ε_f(A) = κ × (1 - exp(-d(n(A))/d₀))
```

**Rationale**:
- Saturates for large d(n)
- Smooth behavior near allowed values

**Status**: [P] — theoretically motivated

---

### Form 4: Barrier-Based

**Formula**:
```
ε_f(A) = ΔV_eff(n(A)) - ΔV_eff(n_allowed)
```

**Rationale**:
- Uses LAW-4 (barrier formula)
- Frustration = excess barrier vs allowed case

**Connection to LAW-4**:
```
ΔV_eff = ΔV + 6K × q²
```

**Status**: [P] — connects to existing law

---

## Using n(A) Candidate

If n(A) ≈ 6.1 × A^(1/3) (from N_A_MAPPING_RESEARCH):

| Nuclide | A | n(A) | d(n) | ε_f (Form 1, κ=1) |
|---------|---|------|------|-------------------|
| ²³⁸U | 238 | 37.8 | 1.8 | 1.8 MeV |
| ²³⁴U | 234 | 37.6 | 1.6 | 1.6 MeV |
| ²³⁰Th | 230 | 37.4 | 1.4 | 1.4 MeV |
| ²²⁶Ra | 226 | 37.2 | 1.2 | 1.2 MeV |
| ²²²Rn | 222 | 36.9 | 0.9 | 0.9 MeV |
| ²⁰⁶Pb | 206 | 36.0 | 0.0 | 0.0 MeV |

**Pattern**: ε_f decreases along chain (frustration relieved)

---

## Consistency Check with LAW-3

LAW-3: log₁₀(t₁/₂) = a(Z/√Q_α) + c·ε_f + b

With c = -2.40:
- Larger ε_f → smaller t₁/₂ (faster decay)
- ε_f = 0 at endpoint → stable (t₁/₂ = ∞)

**Check**:
- ²³⁸U has ε_f ≈ 1.8 MeV → long-lived but decays ✓
- ²⁰⁶Pb has ε_f ≈ 0 MeV → stable ✓

**Qualitatively consistent!**

---

## Calibration Strategy

### Step 1: Get actual t₁/₂ and Q_α data
Need NNDC data (currently blocked: [BL:SOURCE_TBD])

### Step 2: Calculate Z/√Q_α for each α-emitter
Standard Gamow factor

### Step 3: Rearrange LAW-3
```
ε_f = [log₁₀(t₁/₂) - a(Z/√Q_α) - b] / c
```

### Step 4: Plot ε_f vs d(n(A))
If linear → κ is slope
If nonlinear → determine α

### Step 5: Check R²
Should get R² ≈ 0.9941 as reported

---

## Upgrade Checklist

### [P] → [I]: What would count as inference?

1. Calculate ε_f from actual decay data
2. Show ε_f ∝ d(n(A)) with R² > 0.9
3. Determine κ value
4. Verify across multiple decay chains

### [I] → [Der]: What would count as derivation?

1. Derive ε_f from M-topology potential energy
2. Show κ = f(K, σ, topology parameters)
3. Connect to barrier formula (LAW-4)
4. Predict new decays

---

## Blocking Issue

**Current blocker**: All t₁/₂ and Q_α data marked [BL:SOURCE_TBD]

**Resolution options**:
1. Igor manually provides key values
2. WebFetch from NNDC (requires approval)
3. Wait for DATA_REQUESTS.md approval

---

## Recommended Next Steps

1. **Prioritize n(A) resolution** (OQ-V3-001)
2. **Request minimal dataset**: 10 α-emitters with t₁/₂, Q_α
3. **Test Form 1** (linear) first as simplest
4. **Refine if needed** to Form 2 or 4

---

## Current Best Estimate [P]

```
ε_f(A) = κ × d(n(A))

Where:
  d(n) = min{|n - m| : m = 2^a × 3^b}
  n(A) ≈ 6.1 × A^(1/3)
  κ ≈ 1 MeV (order of magnitude guess)
```

**Status**: [P] — consistent with qualitative expectations
**Confidence**: Low (no quantitative verification yet)
**Blocked by**: [BL:SOURCE_TBD] on nuclear data
