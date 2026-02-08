# BRANCHPOINTS SCORECARD (V7.2)

**Created**: 2026-01-31
**Purpose**: Extended branchpoint analysis with hindrance consideration
**Scope**: V7 mandatory branchpoints + new candidates

---

## Scoring Framework

### H-N48-01c (Selection-Rule Gated d(n)) [P]

**Rule**:
1. First, check spin-parity accessibility for each channel
2. If one channel is significantly hindered (H1/H2) and other is favored (H0), hindered channel is suppressed
3. Among equally accessible channels, prefer the one with smaller d(n)_daughter

---

## V7 Mandatory Branchpoints (Revisited)

### BP-1: ²¹²Bi (Th-232 Series)

| Property | α Channel | β⁻ Channel |
|----------|-----------|------------|
| Daughter | ²⁰⁸Tl | ²¹²Po |
| Jπ(P) | 1⁻ | 1⁻ |
| Jπ(D) | 5⁺ | 0⁺ |
| ΔJ | **4** | 1 |
| ΔΠ | Yes | Yes |
| Hindrance | **H2** (highly hindered) | H1 |
| d(n)_D | 0.14 | 0.39 |
| Q (keV) | 6207 | 2252 |
| BR (%) | 35.94 | **64.06** |

**H-N48-01c Analysis**:
- α is H2 (ΔJ = 4, hindered)
- β⁻ is H1 (ΔJ = 1 with parity change)
- Selection rules favor β⁻ → **Consistent**

**Verdict**: ✓ H-N48-01c SUCCESS

---

### BP-2: ²²⁷Ac (U-235 Series)

| Property | α Channel | β⁻ Channel |
|----------|-----------|------------|
| Daughter | ²²³Fr | ²²⁷Th |
| Jπ(P) | 3/2⁻ | 3/2⁻ |
| Jπ(D) | 3/2⁻ | 1/2⁺ |
| ΔJ | 0 | 1 |
| ΔΠ | No | Yes |
| Hindrance | **H0** (favored) | H1 |
| d(n)_D | 0.99 | 1.21 |
| Q (keV) | 5042 | 45 |
| BR (%) | 1.38 | **98.62** |

**H-N48-01c Analysis**:
- α is H0 (favored: ΔJ = 0, no parity change)
- β⁻ is H1 (ΔJ = 1 with parity change)
- Selection rules favor α, but β⁻ dominates
- **Anomaly persists**

**Possible explanations**:
1. β⁻ matrix element is anomalously large
2. α-cluster preformation factor is unusually low
3. Nuclear structure effect beyond simple selection rules

**Verdict**: ✗ H-N48-01c FAILURE (unexplained anomaly)

---

### BP-3: ²¹¹Bi (U-235 Series)

| Property | α Channel | β⁻ Channel |
|----------|-----------|------------|
| Daughter | ²⁰⁷Tl | ²¹¹Po |
| Jπ(P) | 9/2⁻ | 9/2⁻ |
| Jπ(D) | 1/2⁺ | 9/2⁺ |
| ΔJ | **4** | 0 |
| ΔΠ | Yes | Yes |
| Hindrance | **H2** | H1 |
| d(n)_D | 0.09 | 0.32 |
| Q (keV) | 6750 | 574 |
| BR (%) | **99.72** | 0.28 |

**H-N48-01c Analysis**:
- α is H2 (ΔJ = 4, hindered)
- β⁻ is H1 (ΔJ = 0 with parity change)
- Selection rules favor β⁻, but α dominates
- **However**: Q_α >> Q_β by 10×, overcoming hindrance

**Verdict**: ~ PARTIAL (Q-value dominates over selection rules)

---

## New Branchpoint Candidates

### BP-4: At-211 (α/EC competition)

| Property | α Channel | EC Channel |
|----------|-----------|------------|
| Daughter | ²⁰⁷Bi | ²¹¹Po→²¹¹Rn |
| Jπ(P) | 9/2⁻ | 9/2⁻ |
| Jπ(D) | 9/2⁻ | 7/2⁻ |
| ΔJ | 0 | 1 |
| ΔΠ | No | No |
| Hindrance | H0 | H0 |
| BR (%) | 41.80 | **58.20** |

**H-N48-01c Analysis**:
- Both channels are H0 (favored)
- Should check d(n) preference
- EC daughter has A = 211 (same as α daughter → both d ≈ 0.3)
- **Inconclusive** — d(n) provides no discriminating power

**Verdict**: ~ NOT TESTABLE (no d(n) difference)

---

### BP-5: Cf-252 (α/SF competition)

| Property | α Channel | SF Channel |
|----------|-----------|------------|
| Q | 6217 keV | ~200 MeV (fission) |
| BR (%) | **96.90** | 3.10 |

**H-N48-01c Analysis**:
- SF is fundamentally different mechanism (collective, not tunneling)
- Selection rules for α don't apply to SF
- d(n) concept may apply to fission fragments, but that's speculative

**Verdict**: ⊘ OUT OF SCOPE (SF is different physics)

---

## Extended Scorecard Summary

| Branchpoint | V7 Score | V7.2 Score | Mechanism |
|-------------|----------|------------|-----------|
| ²¹²Bi | ✗ (d(n)) | ✓ (hindrance) | H2 vs H1 → H1 wins |
| ²²⁷Ac | ✗ (d(n)) | ✗ (anomaly) | H0 vs H1 → H1 wins (anomalous) |
| ²¹¹Bi | ✓ (d(n)) | ~ (Q-dominated) | H2 vs H1 → H2 wins (Q >> 10×) |
| At-211 | — | ~ (no d(n) diff) | H0 vs H0 → EC wins |
| Cf-252 | — | ⊘ (out of scope) | SF different physics |

### Overall Score for H-N48-01c

| Outcome | Count |
|---------|-------|
| Success | 1 (²¹²Bi) |
| Partial | 1 (²¹¹Bi) |
| Failure | 1 (²²⁷Ac) |
| Not testable | 2 |

**Score**: 1.5/3 testable = **50%** (improvement over V7's 33%)

---

## Revised Rule: H-N48-01d [P]

Based on V7.2 analysis, propose refined rule:

### Statement
> At branchpoints, the dominant channel is determined by:
> 1. **Primary**: Hindrance class (H0 > H1 > H2)
> 2. **Secondary**: Q-value (if hindrance difference < 1 class level)
> 3. **Tertiary**: d(n) (only if both hindrance and Q are similar)

### Formal Rule
```
For channels A and B:

IF H(A) < H(B) by ≥1 level:
    Predict A (less hindered wins)
ELSE IF |Q_A - Q_B| / max(Q) > 0.5:
    Predict channel with higher Q
ELSE:
    Predict channel with smaller d(n)_daughter
```

### Falsification Tests for H-N48-01d

1. **Find branchpoint with H0 vs H0 and large d(n) difference**: d(n) should predict
2. **Find branchpoint with H1 vs H0 where H1 has 10× higher Q**: Q should override hindrance
3. **Check ²²⁷Ac again**: If matrix element data available, verify if β⁻ matrix element is indeed anomalous

---

## Conclusions

1. **Hindrance classification improves prediction** from 33% (V7) to 50% (V7.2)

2. **²²⁷Ac remains anomalous**: Neither hindrance, Q-value, nor d(n) explains β⁻ dominance

3. **d(n) has no independent predictive power**: In all testable cases, hindrance or Q-value determines outcome; d(n) is never the deciding factor

4. **SF is out of scope**: Spontaneous fission follows different physics

