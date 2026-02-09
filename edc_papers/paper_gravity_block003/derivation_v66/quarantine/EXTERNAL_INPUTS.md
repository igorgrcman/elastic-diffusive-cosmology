# EXTERNAL INPUTS — QUARANTINED

**WARNING:** This file contains experimental values from external sources.
These values are QUARANTINED and must NOT be used in Layer A derivations.

## Provenance

All values in this file are imported from published experimental results and reviews.
They are used ONLY for comparison purposes in Layer B analysis.

---

## Proton Decay Lifetime Lower Bounds

### Super-Kamiokande (SK) Results

| Channel | Lower Bound (90% CL) | Reference | Notes |
|---------|---------------------|-----------|-------|
| p → e⁺ π⁰ | 2.4 × 10³⁴ years | SK 2020 | Primary channel |
| p → μ⁺ π⁰ | 1.6 × 10³⁴ years | SK 2017 | Subdominant |
| p → e⁺ η | 1.0 × 10³⁴ years | SK 2017 | Eta channel |
| p → ν̄ K⁺ | 6.6 × 10³³ years | SK 2014 | Kaon mode |

### PDG 2024 Summary

| Channel | Lower Bound (90% CL) | Source |
|---------|---------------------|--------|
| p → e⁺ π⁰ | > 2.4 × 10³⁴ years | PDG 2024 (SK) |
| p → μ⁺ π⁰ | > 1.6 × 10³⁴ years | PDG 2024 (SK) |
| p (any mode) | > 10³⁴ years | PDG 2024 (combined) |

---

## Hadronic Matrix Elements

### Lattice QCD Estimates (for reference only)

| Parameter | Value | Uncertainty | Source |
|-----------|-------|-------------|--------|
| α_H (proton) | 0.0090 GeV³ | ±0.0015 | RBC/UKQCD 2015 |
| α_H (proton) | 0.0118 GeV³ | ±0.0025 | JLQCD 2017 |
| β_H (proton) | 0.0096 GeV³ | ±0.0020 | RBC/UKQCD 2015 |

**Note:** These are provided for Layer B sensitivity analysis only.
In Layer A, the hadronic factor H_p is kept symbolic.

---

## Reference Scale (for unit conversion only)

| Parameter | Value | Notes |
|-----------|-------|-------|
| M_Z | 91.1876 GeV | PDG 2024 |
| G_F | 1.1663787 × 10⁻⁵ GeV⁻² | PDG 2024 |
| ℏc | 0.1973 GeV·fm | Natural units conversion |

**Note:** These are used ONLY for dimensional analysis in Layer B.
Layer A uses dimensionless ratios only.

---

## Conversion Factors

| Conversion | Value |
|------------|-------|
| 1 year | 3.156 × 10⁷ seconds |
| 1 GeV⁻¹ | 6.582 × 10⁻²⁵ seconds |
| 1 GeV⁻¹ | 2.085 × 10⁻¹⁷ years |

---

## Usage Policy

1. All values in this file are QUARANTINED
2. They may ONLY be referenced in QUARANTINED appendices
3. They must NOT appear in Layer A sections
4. They must NOT influence Layer A derivations
5. grep verification must confirm 0 hits in Layer A

---

## Citation Notes

- SK 2020: Super-Kamiokande Collaboration, Phys. Rev. D 102 (2020)
- SK 2017: Super-Kamiokande Collaboration, Phys. Rev. D 95 (2017)
- SK 2014: Super-Kamiokande Collaboration, Phys. Rev. D 90 (2014)
- PDG 2024: Particle Data Group, Phys. Rev. D 110 (2024)
- RBC/UKQCD 2015: Phys. Rev. D 91 (2015) 054507
- JLQCD 2017: Phys. Rev. D 96 (2017) 014506
