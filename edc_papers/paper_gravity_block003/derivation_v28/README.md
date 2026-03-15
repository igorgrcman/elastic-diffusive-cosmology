# Derivation v28 — λ-Pinning from Self-Adjointness + Topological Quantization

**BLOCK-003 Gravity Program**

## One-Line Summary

Derives self-adjoint extension structure [D], shows topological mechanisms quantize λ = c_λ n [Dc/P], reducing gap freedom from continuous to discrete.

## Key Results

### Track A: Self-Adjointness [D]

1. **Robin BC is legitimate SA extension**:
   $$\psi'(L) = m_b \psi(L)$$

2. **Extension parameter**:
   $$b = m_b L \in [0, \infty)$$

3. **Physical constraint**: $b \geq 0$ (unitarity + positivity)

4. **SA does NOT quantize** $b$

### Track B: Topological Quantization [Dc/P]

1. **Chern-Simons mechanism**: λ = |k|/(2π), k ∈ Z
2. **Axionic holonomy**: λ = c_ax · n, n ∈ Z+
3. **Orbifold normalization**: λ = π n

**General form**:
$$\lambda = c_\lambda \cdot n, \quad n \in \mathbb{Z}^+, \quad c_\lambda \in \{1/(2\pi), 1, \pi, 2\pi\}$$

### Combined Result

$$m_{\mathrm{gap}}(n) = \frac{x_1(c_\lambda n \beta)}{L}$$

where β = σL²/M̄_Pl² and x_1 solves tan(x) = -b/x.

## Epistemic Status

| Component | Tag | Status |
|-----------|-----|--------|
| SA extension theory | [D] | Derived |
| b = m_b L as SA parameter | [D] | Derived |
| Integer n from topology | [D] | Derived |
| Coefficient c_λ | [OPEN] | Mechanism-dependent |
| Prefactor β | [OPEN] | Requires L, σ |
| Gap m_gap | [I]+[BL] | Not upgraded |

## Files

| File | Description |
|------|-------------|
| `main.tex` | LaTeX source (100 equations) |
| `main.pdf` | Compiled PDF (19 pages) |
| `EDC_BLOCK003_DERIVATION_V28_LAMBDA_PINNING_DERIVATION.pdf` | Export |
| `recompute.py` | Numerical verification (15 checks) |
| `README.md` | This file |
| `REPORT.md` | Build report |
| `ACCEPTANCE.md` | Acceptance criteria |

## Building

```bash
xelatex main.tex && xelatex main.tex && xelatex main.tex
python3 recompute.py
```

## What This Note Achieves

- Derives SA structure of Robin BC [D]
- Shows b is continuous from pure SA theory [D]
- Derives topological quantization mechanisms for λ [Dc/P]
- Reduces gap freedom from continuous to discrete [Dc]

## What This Note Does NOT Achieve

- Does not uniquely determine c_λ [OPEN]
- Does not derive β = σL²/M̄_Pl² [OPEN]
- Does not upgrade gap to [D] or [Dc]

---

*Generated: 2026-02-03*
