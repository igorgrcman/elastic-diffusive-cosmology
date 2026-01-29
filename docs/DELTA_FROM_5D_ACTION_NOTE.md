# δ from 5D Action: Executive Summary

**Created:** 2026-01-29
**Source:** `edc_papers/_shared/derivations/delta_from_5d_action_proton_scale.tex`
**Status:** [Dc] — Derived Conditional (proton identification is postulate)

---

## Main Result

```
δ = ℏ/(2 m_p c) = 0.533 GeV⁻¹ = 0.105 fm
```

**In words:** The brane thickness is half the proton Compton wavelength.

---

## Derivation Chain

1. **5D action → 1D mode equation** [Der]: KK reduction gives -d²w/dχ² + V(χ)w = λw
2. **Potential scaling** [Dc]: Depth V₀ ~ 1/δ², width ~ δ
3. **Ground state energy**: E₀ = c_E/δ where c_E = O(1)
   - **Scaling** [Der]: The 1/δ dependence is dimensional/robust
   - **Coefficient** [Dc]: c_E depends on ω = √(V''/M_eff); harmonic gives c_E = 1/2
4. **Proton = bound mode** [P]: Postulate identifying proton with localized fermion
5. **Match m_p = E₀** [Dc]: Gives δ = c_δ/m_p with c_δ = 1/2 from harmonic approx

---

## Assumptions (Explicit)

1. Thick brane structure [P]
2. Proton identified as bound fermionic mode [P]
3. Single-scale dominance [Dc]
4. Harmonic approximation for coefficient [Dc]

---

## What Is Derived

- **δ ~ 1/m_p scaling** [Der]: Robust from dimensional analysis given bound-state picture
- **Coefficient c_δ = 1/2** [Dc]: From harmonic approximation (E₀ = ω/2, ω ~ 1/δ)
- **Numerical value δ = 0.533 GeV⁻¹** [Dc]: Depends on c_δ

---

## What Remains Open

- **Potential shape V(χ)** from 5D bulk EOM (currently ansatz)
- **Exact coefficient c_δ**: Requires V''(0) from action — why 1/2 vs 1/3 vs 1/π?
- **Proton mass derivation** (currently input, not output)
- **Topological justification** for proton = bound mode identification

---

## Verdict

**Status:** YELLOW [Dc] — Principled but model-dependent

**Upgrade path to GREEN:** Derive V(χ) explicitly; compute exact bound state; justify proton identification from topology.

---

*This note provides a "front door" summary. Full derivation in LaTeX source.*
