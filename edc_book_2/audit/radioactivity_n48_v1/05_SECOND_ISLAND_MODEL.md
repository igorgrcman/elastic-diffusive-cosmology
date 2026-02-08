# SECOND ISLAND MODEL (V6)

**Created**: 2026-01-31
**Purpose**: Toy pipeline for n=48 approach + A-table
**Status**: All equations tagged per G10

---

## Toy Pipeline (Symbolic-First)

### Step 1: Allowed Set [Der]
```
S = {n : n = 2^a × 3^b}  [Der from V4]
```
Source: DN-001, 22826edd:2440-2540

### Step 2: Distance Function [Der]
```
d(n) = min_{m ∈ S} |n - m|  [Der]
```
For practical nuclear range, relevant targets are m ∈ {36, 48}.

### Step 3: Coordination Mapping [P]

**Candidate Formula** (AS-N48-001):
```
n(A) = c × A^(1/3)  [P]
```

**Parameter Range** (AS-N48-002):
```
c ∈ [5.5, 8.0]  [P]
```

**Default Choice**:
```
c = 6.1  [P]
```

**Rationale**: c = 6.1 gives n(208) ≈ 36.2, consistent with Pb-208 stability.

### Step 4: Frustration Energy [P]

**Candidate Formula** (AS-N48-003):
```
ε_f(A) = k × d(n(A))  [P]
```

**Parameter Range** (AS-N48-004):
```
k ∈ [0.1, 2.0] (dimensionless or MeV depending on convention)  [P]
```

**Default Choice**:
```
k = 0.94  [P]
```

**Rationale**: Matches pinning constant K ≈ 0.94 MeV from V4 LAW-5.

### Step 5: Half-Life Law Skeleton [I/P]

**Form** (AS-N48-011):
```
log₁₀(t₁/₂) = a × (Z/√Q) + b + c × ε_f  [I/P]
```

Where:
- Z: Atomic number [BL:SOURCE_TBD for specific values]
- Q: Decay Q-value [BL:SOURCE_TBD]
- a, b: G-N coefficients [I from V4 DN-015..017]
- c: Frustration coefficient [P]

---

## A-Table: Coordination Across Mass Range

**Assumptions Used**:
- c = 6.1 (AS-N48-002)
- S = {1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, 54, 64, 72, ...}
- d(n) = min(|n - 36|, |n - 48|) for nuclear range

| A | A^(1/3) | n(A) = 6.1×A^(1/3) | Nearest m ∈ S | d(n) | Comment |
|---|---------|---------------------|---------------|------|---------|
| 208 | 5.93 | 36.2 [P] | 36 | 0.2 | At primary target |
| 238 | 6.20 | 37.8 [P] | 36 | 1.8 | Entering forbidden zone |
| 294 | 6.65 | 40.6 [P] | 36 | 4.6 | Deep forbidden (toward 42) |
| 350 | 7.05 | 43.0 [P] | 48 | 5.0 | Near saturation peak, closer to 48 |
| 400 | 7.37 | 45.0 [P] | 48 | 3.0 | Exiting forbidden (toward 48) |
| 488 | 7.87 | 48.0 [P] | 48 | 0.0 | At secondary target |

**All rows tagged [P]** due to c = 6.1 assumption.

---

## Visualization: Forbidden Wall Crossing

```
n(A) vs A

n
50 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ●(A=488)
48 ════════════════════════════════════════════ ← ALLOWED (n=48)
47 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─●─ ─   ← A=400
   |           FORBIDDEN ZONE              |
45 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
   |                                       |
43 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─●─ ─ ─ ─ ─ ─ ─   ← A=350 (saturation zone)
   |                                       |
42 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   ← MAXIMUM FRUSTRATION
   |                                       |
41 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─●─ ─ ─ ─ ─ ─ ─ ─ ─ ─   ← A=294
   |                                       |
38 ─ ─ ─ ─ ─ ─●─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   ← A=238
   |           FORBIDDEN ZONE              |
37 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
36 ══●═════════════════════════════════════ ← ALLOWED (n=36), A=208

   200   250   300   350   400   450   500 → A
```

---

## Qualitative Trends

### Trend 1: Increasing A Crosses Forbidden Zone
As A increases from 208 to 488:
- n(A) increases from 36.2 to 48.0
- Passes through entire forbidden zone [37, 47]
- Maximum frustration near A ≈ 285 (n ≈ 42)

### Trend 2: Target Switches at A ~ 300
- For A < 285: Closer to n=36 target
- For A > 285: Closer to n=48 target
- Implication: Superheavy elements may stabilize toward n=48

### Trend 3: Relative Lifetimes (Qualitative Only)
- t₁/₂ ∝ exp(frustration) roughly
- **NOT** a quantitative claim — requires [BL] data for Q, Z

---

## Sensitivity to c

| c | n(208) | n(294) | n(488) | Comment |
|---|--------|--------|--------|---------|
| 5.5 | 32.6 | 36.6 | 43.3 | Never reaches 48 |
| 6.1 | 36.2 | 40.6 | 48.0 | Default; hits both targets |
| 7.0 | 41.5 | 46.6 | 55.1 | Overshoots 48 |
| 8.0 | 47.4 | 53.2 | 62.9 | Far overshoot |

**Conclusion**: c ≈ 6.1 is the only value that gives n(Pb-208) ≈ 36 AND n(A~488) ≈ 48.

This constrains c to a narrow window [5.8, 6.4] if both targets are meaningful.

---

## What This Toy Model Does NOT Claim

1. **No specific half-life values** — requires [BL] Q-values
2. **No absolute energy scales** — k is placeholder
3. **No prediction of which A is stable** — only relative trends
4. **No supernova origin** — that would be [P] without donor

---

## Upgrade Requirements

To move from [P] to [I]:
1. Calibrate c against nuclear radii data
2. Calibrate k against G-N fit residuals
3. Compare d(n) predictions to actual half-life ordering

To move from [I] to [Der]:
1. Derive c from nuclear geometry (r = r₀ × A^(1/3))
2. Derive k from 5D barrier formula
3. Show complete derivation chain
