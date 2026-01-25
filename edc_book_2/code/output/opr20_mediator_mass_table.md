# OPR-20 Mediator Mass Sanity Check Results

**Date**: 2026-01-25
**Status**: PASS

## Eigenvalue Table (Flat Potential V=0)

| BC Type | κ₀ | κₗ | x₁ | x₂ |
|---------|-----|-----|------|------|
| Neumann-Neumann | 0.0 | 0.0 | 3.1416 | 6.2832 |
| Neumann-Dirichlet | 0.0 | 10000000000.0 | 4.7124 | 7.8540 |
| Dirichlet-Neumann | 10000000000.0 | 0.0 | 4.7124 | 7.8540 |
| Dirichlet-Dirichlet | 10000000000.0 | 10000000000.0 | N/A | N/A |
| Robin (κ=1) | 1.0 | 1.0 | 3.6732 | 6.5846 |
| Robin (κ=2) | 2.0 | 2.0 | 4.0575 | 6.8512 |
| Robin (κ=5) | 5.0 | 5.0 | 4.7613 | 7.4637 |
| Robin (κ=10) | 10.0 | 10.0 | 5.3073 | 8.0671 |

## Mass Scaling (Neumann-Neumann, x₁ = π)

| ℓ (fm) | ℓ (GeV⁻¹) | m₁ (GeV) | m₁ (MeV) |
|--------|-----------|----------|----------|
| 0.0010 | 0.0051 | 619.9247 | 619924.7496 |
| 0.0100 | 0.0507 | 61.9925 | 61992.4750 |
| 0.1000 | 0.5068 | 6.1992 | 6199.2475 |
| 1.0000 | 5.0677 | 0.6199 | 619.9247 |

## Robustness vs κ

| κ | x₁ | x₁/π |
|---|-----|------|
| 0.10 | 3.203994 | 1.019863 |
| 0.50 | 3.431014 | 1.092126 |
| 1.00 | 3.673194 | 1.169214 |
| 2.00 | 4.057516 | 1.291547 |
| 5.00 | 4.761289 | 1.515565 |
| 10.00 | 5.307325 | 1.689374 |
| 50.00 | 6.042646 | 1.923434 |
| 100.00 | 6.160138 | 1.960833 |

## No-Smuggling Certification

- ✓ No M_W, M_Z, G_F, v, sin²θ_W used as inputs
- ✓ All parameters tagged [P] or [BL]
- ✓ Eigenvalue structure is mathematical, not fitted
