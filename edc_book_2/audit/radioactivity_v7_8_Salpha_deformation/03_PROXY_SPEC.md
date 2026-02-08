# V7.8 PROXY SPECIFICATION

**Created**: 2026-01-31
**Purpose**: Define S_α and deformation proxies for mediation analysis

---

## Overview

V7.7 established that g < 0 is most consistent with prefactor (S_α) enhancement. V7.8 tests this by adding independent proxies:

1. **Deformation proxy**: Tests whether d(n) is confounded with nuclear deformation
2. **S_α proxy**: Tests whether d(n) effect is mediated by preformation probability

---

## Proxy 1: Deformation Proxy

### Selection: Royer Deformation Index (proxy_deform)

**Definition**:
```
proxy_deform = |N - 126| × |Z - 82| / 1000
```

**Physical meaning**:
- Distance from doubly-magic Pb-208 (N=126, Z=82)
- Nuclei far from shell closures are typically more deformed
- Product term captures combined shell distance effect
- Scaled by 1000 for numerical convenience

**Justification**:
- Deformation β₂ correlates strongly with shell distance
- Po, At, Rn (near Pb-208) are nearly spherical (β₂ ≈ 0)
- Heavy actinides (U, Pu, Cm) are well-deformed (β₂ ≈ 0.2-0.3)
- Shell distance captures this trend without external lookup

**Alternative considered**: Direct β₂ from FRDM
- Requires external data file
- Created interface for future use (data/proxies/proxy_deformation.csv)

### Validation

| Nuclide | N | Z | |N-126| | |Z-82| | proxy_deform | Expected β₂ |
|---------|---|---|--------|--------|--------------|-------------|
| Po-210 | 126 | 84 | 0 | 2 | 0.000 | ~0 (spherical) |
| Ra-226 | 138 | 88 | 12 | 6 | 0.072 | ~0.1 |
| U-238 | 146 | 92 | 20 | 10 | 0.200 | ~0.22 |
| Cm-248 | 152 | 96 | 26 | 14 | 0.364 | ~0.28 |
| Fm-256 | 156 | 100 | 30 | 18 | 0.540 | ~0.30 |

**Correlation with literature β₂**: Expected r > 0.8 [I]

---

## Proxy 2: S_α Proxy (Preformation Factor)

### Selection: Royer Preformation Estimate (proxy_Salpha)

**Definition** (from Royer 2010 systematics):
```
log₁₀(P_α) = a₀ + a₁×Z + a₂×N + a₃×A
```

For actinides (Z > 82):
```
log₁₀(P_α) = -2.52 + 0.0121×Z - 0.0087×N + 0.0023×A
```

**Physical meaning**:
- P_α = α-preformation probability (probability α-cluster exists)
- Royer formula captures systematics from fits to experimental reduced widths
- Values typically range from P_α ≈ 0.01 to 0.3

**Justification**:
- Empirical formula validated against experimental spectroscopic factors
- Applies to all nuclides in dataset (no missing data)
- Independent of d(n) by construction (uses only Z, N, A)

**Alternative considered**: Buck cluster model S_α
- More theoretically grounded
- But incomplete coverage (missing many nuclides)
- Created interface for future use (data/proxies/proxy_Salpha.csv)

### Validation

| Nuclide | Z | N | A | log₁₀(P_α) | P_α |
|---------|---|---|---|------------|-----|
| Po-210 | 84 | 126 | 210 | -1.42 | 0.038 |
| Ra-226 | 88 | 138 | 226 | -1.51 | 0.031 |
| U-238 | 92 | 146 | 238 | -1.48 | 0.033 |
| Pu-240 | 94 | 146 | 240 | -1.39 | 0.041 |
| Cm-248 | 96 | 152 | 248 | -1.41 | 0.039 |
| Fm-256 | 100 | 156 | 256 | -1.31 | 0.049 |

**Note**: log₁₀(P_α) is directly used as proxy_Salpha in models.

---

## Availability and Missingness

### Derived Proxies (No External Data)

| Proxy | Coverage | Missing | Reason |
|-------|----------|---------|--------|
| proxy_deform | 106/106 (100%) | 0 | Derived from Z, N |
| proxy_Salpha | 106/106 (100%) | 0 | Royer formula |

**No missing data** — both proxies are computable for all nuclides.

### External Proxies (Future Enhancement)

| Proxy | Expected Coverage | Source |
|-------|-------------------|--------|
| beta2_FRDM | ~100/106 (94%) | FRDM2012 tables |
| Salpha_Buck | ~40/106 (38%) | Cluster model papers |
| E2plus_keV | ~52/106 (49%) | ENSDF (even-even only) |

---

## Correlation Structure

### Expected Correlations (to verify)

| Pair | Expected r | Reason |
|------|------------|--------|
| proxy_deform vs A | ~0.8 | Heavier = more deformed |
| proxy_deform vs d(n) | ~0.7 | Both scale with A |
| proxy_Salpha vs Z | ~0.5 | Royer formula has Z term |
| proxy_Salpha vs d(n) | ~0.3-0.5 | Unknown; test determines |

### Key Test

If proxy_deform or proxy_Salpha are highly correlated with d(n), we must test whether g survives their inclusion.

---

## Model Implications

### If proxy_deform kills g:
- d(n) was proxying deformation
- Update mechanism: "deformation mediates decay, not topology"
- Status change: [P] prefactor mechanism → [Collapse]

### If proxy_Salpha kills g:
- d(n) was proxying preformation
- Actually supports V7.7: "d(n) acts through S_α"
- Status change: [P] → [I] (mediation confirmed)

### If both keep g stable:
- d(n) captures something beyond standard proxies
- "Topological frustration" interpretation strengthened
- Status change: [P] → more robust [P]

---

## Implementation

### Formulas for Dataset Augmentation

```python
# Deformation proxy
N = A - Z
proxy_deform = abs(N - 126) * abs(Z - 82) / 1000

# Royer S_α proxy (log scale)
proxy_Salpha = -2.52 + 0.0121 * Z - 0.0087 * N + 0.0023 * A
```

### Output Columns

| Column | Type | Description |
|--------|------|-------------|
| proxy_deform | float | Shell distance product / 1000 |
| proxy_Salpha | float | log₁₀(P_α) from Royer |
| proxy_deform_source | string | "D4" (derived) |
| proxy_Salpha_source | string | "D3" (Royer 2010) |

