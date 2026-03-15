# Derivation v27 — Brane Mass from Brane Tension

**BLOCK-003 Gravity Program**

## One-Line Summary

Derives $m_b = \lambda\sigma/M_5^3$ from dimensional and action-level arguments, proposes topological pinning candidate for discrete $\lambda$.

## Key Results

1. **Primary Relation** [Dc]:
   $$m_b = \lambda \frac{\sigma}{M_5^3}$$

2. **Control Parameter** [Dc]:
   $$b = m_b L = \lambda \frac{\sigma L^2}{\bar{M}_{\mathrm{Pl}}^2}$$

3. **Topological Pinning Candidate** [P]:
   $$\lambda = \pi n \quad \text{or} \quad \lambda = 2\pi n, \quad n \in \mathbb{Z}^+$$

4. **Gap Status**: Remains [I]+[BL] until $\lambda$ and $L$ are fixed

## Epistemic Tags

| Component | Tag | Status |
|-----------|-----|--------|
| Dimensional scaling $m_b \propto \sigma/M_5^3$ | [D] | Derived |
| Relation $m_b = \lambda\sigma/M_5^3$ | [Dc] | 1 free parameter |
| Topological pinning | [P] | Postulated/candidate |
| Compactification $L$ | [I]+[BL] | Identified |
| Gap $m_{\mathrm{gap}}$ | [I]+[BL] | Not upgraded |

## Files

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source |
| `main.pdf` | Compiled PDF (19 pages) |
| `EDC_BLOCK003_DERIVATION_V27_MB_FROM_SIGMA_PINNING.pdf` | Export |
| `recompute.py` | Numerical verification |
| `README.md` | This file |
| `REPORT.md` | Build report |
| `ACCEPTANCE.md` | Acceptance criteria |

## Building

```bash
xelatex main.tex && xelatex main.tex && xelatex main.tex
python3 recompute.py
```

## Verification

```bash
python3 recompute.py  # ALL 12 CHECKS PASSED
```

## Connection to v26

This note builds on v26's transcendental spectrum:
- v26: $\tan(m_n L) = -m_b/m_n$ with Robin BC [D]
- v27: $m_b = \lambda\sigma/M_5^3$ connects $m_b$ to brane tension [Dc]

---

*Generated: 2026-02-03*
