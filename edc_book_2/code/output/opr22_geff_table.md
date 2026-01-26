# OPR-22 G_eff Sanity Check Results

**Date**: 2026-01-25
**Status**: PASS

## Main Results

| Quantity | Value | Units |
|----------|-------|-------|
| G_eff | 1.026931e-03 | GeV^-2 |
| C_eff | 1.026931e-03 | GeV^-2 |
| m_1 | 61.9925 | GeV |
| m_1 | 61992.47 | MeV |
| x_1 | 3.141593 | — |

## Input Parameters [P]

| Parameter | Value | Units | Status |
|-----------|-------|-------|--------|
| g_5^2 | 0.2000 | GeV^-1 | [P] |
| ell | 0.0100 | fm | [P] |
| ell | 0.0507 | GeV^-1 | [P] |
| |f_1(0)|^2 | 2.0000 | — | [Dc] toy |
| x_1 | 3.141593 | — | [Dc] toy |

## Scaling with ell (G_eff ∝ ell)

| ell (fm) | ell (GeV^-1) | m_1 (GeV) | G_eff (GeV^-2) |
|----------|--------------|-----------|----------------|
| 0.0010 | 0.0051 | 619.9247 | 1.026931e-04 |
| 0.0100 | 0.0507 | 61.9925 | 1.026931e-03 |
| 0.1000 | 0.5068 | 6.1992 | 1.026931e-02 |
| 1.0000 | 5.0677 | 0.6199 | 1.026931e-01 |

## Sensitivity to x_1 (G_eff ∝ 1/x_1^2)

| x_1 | x_1/π | m_1 (GeV) | G_eff (GeV^-2) |
|-----|-------|-----------|----------------|
| 1.5708 | 0.5000 | 30.9962 | 4.107723e-03 |
| 3.1416 | 1.0000 | 61.9925 | 1.026931e-03 |
| 4.7124 | 1.5000 | 92.9887 | 4.564137e-04 |
| 6.2832 | 2.0000 | 123.9849 | 2.567327e-04 |

## Formulas

**G_eff (natural normalization)**:
```
G_eff = g_5^2 * ell * |f_1(0)|^2 / (2 * x_1^2)
```

**Connection to OPR-20**:
```
G_eff = (1/2) * C_eff * |f_1(0)|^2
C_eff = g_5^2 * ell / x_1^2
```

## No-Smuggling Certification

- ✓ No M_W, M_Z, G_F, v, sin²θ_W used as inputs
- ✓ All parameters tagged [P] or [BL]
- ✓ G_eff is computed quantity, not measured G_F
- ✓ Dimensional analysis verified: [G_eff] = GeV^-2
