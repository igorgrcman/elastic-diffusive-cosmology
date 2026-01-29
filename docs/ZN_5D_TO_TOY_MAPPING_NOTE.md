# Z_N 5D → Toy Functional Mapping Note

**Date:** 2026-01-29
**Source:** `edc_papers/_shared/derivations/zn_toy_functional_from_5d_action.tex`
**Status:** [Dc] — Derived Conditional (heuristic gauge-fixing)

---

## Summary

Maps the 5D brane-world action to the 1D toy functional for Z_N anisotropy:

**5D Action:**
```
S_5D = S_bulk + S_brane + S_GHY
```

**Toy Functional:**
```
E[u] = (T/2)∫(u')²dθ + λ Σₙ W(u(θₙ))
```

---

## Mapping Dictionary

| Toy Parameter | 5D Origin | Mechanism |
|---------------|-----------|-----------|
| T (tension)   | σ/R       | Brane tension / ring radius |
| λ (coupling)  | κ₅²τₙ     | Israel junction × defect stress |
| u(θ)          | h(θ)      | Metric perturbation at ring |
| W(u)          | φ(u)²     | Localized potential at fixed points |

---

## Key Result

The 1/N scaling of anisotropy amplitude emerges naturally:
- Gradient energy scales as N² (faster variation)
- Discrete anchors contribute N terms
- Balance gives a₁ ∝ 1/N

---

## Epistemic Status

- **Stage 1-2 (Geometry, Gradient):** [Der] — Standard dimensional reduction
- **Stage 3 (Israel junction):** [Dc] — Requires specific gauge choices
- **Overall mapping:** [Dc] — Physical identification is heuristic

---

## References

- Full derivation: `edc_papers/_shared/derivations/zn_toy_functional_from_5d_action.tex`
- Toy model: `edc_papers/_shared/derivations/zn_anisotropy_normalization_from_action.tex`
- 5D pipeline: Companion C (Book 2)
