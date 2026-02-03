# Derivation v21 — KK Mass Gap to R_xi Identification

**Purpose:** Derive the Kaluza-Klein mass spectrum and show how R_xi can be determined from the first KK mass gap, upgrading the epistemic status of R_xi = hbar*c/M_Z from pure [BL] to [I]+[BL].

## What This Note Does

1. Derives the KK mode equation for 5D graviton on flat interval
2. Solves for three boundary condition types:
   - BC1 (Neumann-Neumann): m_n = n*pi/R_xi — **physically relevant**
   - BC2 (Dirichlet-Dirichlet): m_n = n*pi/R_xi (no zero mode)
   - BC3 (Mixed): m_n = (2n+1)*pi/(2*R_xi) (no zero mode)
3. Defines mass gap m_gap = m_1 = pi/R_xi
4. Derives inversion: R_xi = pi/m_gap
5. Identifies m_gap with M_Z (best metrological proxy)
6. Computes M_5 from the closure formula

## What This Note Does NOT Do

- Does NOT derive the Standard Model
- Does NOT prove m_gap = M_Z (this is an identification [I])
- Does NOT derive R_xi from EDC axioms (remains NO-GO)

## Key Results

| Quantity | Value | Tag |
|----------|-------|-----|
| Mass gap relation | m_gap = pi/R_xi | [D] |
| Inversion | R_xi = pi*hbar*c/M_Z | [I]+[BL] |
| R_xi | 6.80 x 10^-18 m | [I]+[BL] |
| M_5 | 4.3 x 10^12 GeV | [D] |

## Files

| File | Description |
|------|-------------|
| `main.tex` | Source document (42 equation environments) |
| `main.pdf` | Compiled output |
| `EDC_BLOCK003_DERIVATION_V21_KK_GAP_TO_RXI.pdf` | Export copy |
| `REPORT.md` | Build verification report |
| `ACCEPTANCE.md` | Acceptance criteria |

## Conventions

Matches v20:
- Reduced Planck mass: G_N = 1/(8*pi*M_Pl_bar^2)
- Interval coordinate: xi in [0, R_xi]
- Flat warp factor: A(xi) = 0
- Bridge: M_Pl_bar^2 = M_5^3 * I with I = R_xi

## Note on Factor pi

This note uses R_xi = pi*hbar*c/M_Z (identifying m_gap = M_Z), while v15-v20 used R_xi = hbar*c/M_Z. The difference is a factor of pi in R_xi and ~0.68 in M_5. Both give M_5 ~ 10^12-10^13 GeV.
