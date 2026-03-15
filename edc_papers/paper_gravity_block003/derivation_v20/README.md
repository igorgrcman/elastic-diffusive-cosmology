# Derivation v20 — Factor & Normalization Audit

**Purpose:** Forensic tracking of all numerical factors in the 5D→4D gravity bridge derivation.

## Scope

This note performs a complete audit of:

1. **Action normalization factor** — the ½ in $S_5 = \frac{M_5^3}{2}\int\sqrt{-g_5}R_5$
2. **Newton constant factor** — the $8\pi$ in $G_N = 1/(8\pi\bar{M}_{\rm Pl}^2)$
3. **Orbifold doubling** — fundamental domain vs full circle
4. **Circumference factor** — $2\pi R$ vs $L$
5. **Warp factor exponent** — cancellation in $\mathcal{I}$

## Key Results

| Planck Convention | $\bar{M}_{\rm Pl}$ (reduced) | $M_{\rm Pl}$ (original) |
|-------------------|------------------------------|-------------------------|
| Value | $2.435 \times 10^{18}$ GeV | $1.221 \times 10^{19}$ GeV |
| $M_5$ result | $8.1 \times 10^{12}$ GeV | $2.4 \times 10^{13}$ GeV |

**Conversion:** $M_5^{\rm (orig)} = (8\pi)^{1/3} M_5^{\rm (red)} \approx 2.94 \times M_5^{\rm (red)}$

## Files

| File | Description |
|------|-------------|
| `main.tex` | Source document |
| `main.pdf` | Compiled output |
| `EDC_BLOCK003_DERIVATION_V20_FACTOR_AUDIT.pdf` | Export copy |
| `REPORT.md` | Build verification report |
| `ACCEPTANCE.md` | Acceptance criteria |

## Checksums

- `main.tex`: `08a0862cc82b6f2b94f22560347992ab`
- `main.pdf`: `956d3832cf1b79f762b314643e7b3c1a`

## Convention Fixed

This note adopts:
- **Reduced Planck mass** $\bar{M}_{\rm Pl} = 2.435 \times 10^{18}$ GeV
- **Interval coordinate** $\xi \in [0, R_\xi]$
- **Bridge relation** $\bar{M}_{\rm Pl}^2 = M_5^3 \mathcal{I}$

With $R_\xi = \hbar c / M_Z$, this yields $M_5 = 8.1 \times 10^{12}$ GeV.
