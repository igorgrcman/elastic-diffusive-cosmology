# BRANCHING RULES V5

**Created**: 2026-01-31
**Purpose**: Formalized branching hypotheses H1-H5
**Source**: Decay chain observations, mechanism catalog

---

## Hypothesis Registry

### H1: Proximity Rule
- **Statement**: As d(n) → 0, α-branching increases
- **Mechanism**: M3 (α-clusterization) becomes dominant near allowed n
- **Test Case**: Compare ²¹²Bi (d=0.4) vs ²²⁷Ac (d=1.2)
- **Observed**:
  - ²¹²Bi: α 36% (d=0.4)
  - ²²⁷Ac: α 1.4% (d=1.2)
- **Status**: [P] consistent with data
- **Falsification**: Find counter-example where α↓ as d↓

### H2: Asymmetry Rule
- **Statement**: β⁻ preferred when N/Z asymmetry is high
- **Mechanism**: M2 (defect-mediated) reduces asymmetry
- **Test Case**: Heavy actinides with N >> Z
- **Observed**: Early chain steps favor β⁻
- **Status**: [P]
- **Falsification**: β⁻ suppressed despite high asymmetry

### H3: Cluster Preformation Rule
- **Statement**: α-branching enhanced for N=Z or 4n nuclei
- **Mechanism**: M3 (α-cluster preformed)
- **Test Case**: Compare even-even vs odd-A nuclei
- **Observed**: Even-even have higher α-branches
- **Status**: [I]
- **Falsification**: Odd-A with higher α-branch than even-even neighbor

### H4: Energy Threshold Rule
- **Statement**: α-decay requires Q_α > ε_f threshold
- **Mechanism**: Barrier height depends on frustration
- **Test Case**: Low-Q_α emitters with high ε_f
- **Observed**: Long half-lives for high ε_f, low Q_α
- **Status**: [Der] from LAW-4
- **Falsification**: Fast α-decay despite low Q_α and high ε_f

### H5: Metastability Rule
- **Statement**: Isomeric states may have different d(n) and branching
- **Mechanism**: M4 (metastable structures)
- **Test Case**: Ground state vs isomer branching ratios
- **Observed**: Some isomers have anomalous ratios
- **Status**: [P]
- **Falsification**: Isomers always match ground state ratios

---

## Branching Decision Tree

```
START: Nucleus with A, Z, N, n(A)
  |
  ├─ Is n(A) allowed (= 2^a × 3^b)?
  │   ├─ YES → Stable (no decay needed)
  │   └─ NO → Continue
  |
  ├─ Calculate d(36) and d(48)
  │   └─ d(n) = min(d(36), d(48))
  |
  ├─ Is Q_α > ε_f(n)?
  │   ├─ YES → α-channel open
  │   └─ NO → α-channel suppressed
  |
  ├─ Is N/Z > 1.5?
  │   ├─ YES → β⁻ favored (H2)
  │   └─ NO → Compare α vs β⁻
  |
  ├─ Is d(n) < 1?
  │   ├─ YES → α likely dominant (H1)
  │   └─ NO → β⁻ likely dominant
  |
  └─ Final branching: Weighted by ε_f, Q_α, asymmetry
```

---

## Test Cases from Chains

### Case 1: ²¹²Bi (Th-232 chain)
| Parameter | Value |
|-----------|-------|
| A | 212 |
| n(A) | 36.4 [P] |
| d(n) | 0.4 |
| N/Z | 1.54 |
| α% | 36% |
| β⁻% | 64% |
| **Result** | H1 partial, H2 active |

### Case 2: ²¹¹Bi (U-235 chain)
| Parameter | Value |
|-----------|-------|
| A | 211 |
| n(A) | 36.3 [P] |
| d(n) | 0.3 |
| N/Z | 1.54 |
| α% | 99.7% |
| β⁻% | 0.3% |
| **Result** | H1 dominant (d very small) |

### Case 3: ²²⁷Ac (U-235 chain)
| Parameter | Value |
|-----------|-------|
| A | 227 |
| n(A) | 37.2 [P] |
| d(n) | 1.2 |
| N/Z | 1.54 |
| α% | 1.4% |
| β⁻% | 98.6% |
| **Result** | H2 dominant (d > 1) |

### Case 4: ²¹⁴Bi (U-238 chain)
| Parameter | Value |
|-----------|-------|
| A | 214 |
| n(A) | 36.5 [P] |
| d(n) | 0.5 |
| N/Z | 1.55 |
| α% | 0.02% |
| β⁻% | 99.98% |
| **Result** | H2 dominant (despite small d) |

---

## Anomaly Analysis

### Anomaly 1: ²¹⁴Bi vs ²¹¹Bi
Both have similar d(n) (~0.3-0.5) but very different α-branching.

| Nuclide | d(n) | α% | Explanation |
|---------|------|-----|-------------|
| ²¹¹Bi | 0.3 | 99.7% | H1 dominant |
| ²¹⁴Bi | 0.5 | 0.02% | H2 overrides (Q_α issue?) |

**Possible Resolution**: Q_α for ²¹⁴Bi may be below ε_f threshold (H4)

### Anomaly 2: ²¹²Bi intermediate
Neither pure α nor pure β⁻.

**Interpretation**: At d ≈ 0.4, H1 and H2 comparable strength, giving mixed branching.

---

## Quantitative Model [P]

Proposed branching ratio formula:
```
BR(α) / BR(β⁻) = exp(-A × d(n) + B × (Q_α - ε_f) - C × (N/Z - 1))
```

where:
- A ~ 2-3: Proximity factor
- B ~ 0.5 MeV⁻¹: Energy factor
- C ~ 2-4: Asymmetry factor

**Status**: [P] - Needs calibration with full branching dataset

---

## Falsification Summary

| Hypothesis | Test | Threshold | Status |
|------------|------|-----------|--------|
| H1 | α% vs d(n) correlation | r < 0.7 | Pending |
| H2 | β⁻% vs N/Z correlation | r < 0.7 | Pending |
| H3 | Even-even vs odd-A | Reversed pattern | [I] |
| H4 | Q_α vs t₁/₂ | G-N fails | [Der] |
| H5 | Isomer anomalies | No anomalies found | Pending |

---

## Data Requirements

For complete validation:
1. Branching ratios for 20+ branch points
2. Q_α values for all α-emitters
3. N/Z ratios (trivially available)
4. Isomer branching ratios (5+ cases)
5. Ground-state spins and parities
