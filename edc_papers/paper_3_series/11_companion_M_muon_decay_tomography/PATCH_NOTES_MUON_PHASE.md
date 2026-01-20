# PATCH NOTES: Muon Decay Tomography Phase

**Date:** 2026-01-20
**Document:** Companion M — Muon Decay as Thick-Brane Tomography
**Status:** Draft v0.2 (stabilization patch applied)

---

## Summary

This companion applies the thick-brane microphysics framework to muon decay
($\mu^- \to e^- + \nu_\mu + \bar{\nu}_e$), demonstrating that the same
absorption→dissipation→release pipeline works for:

1. **Neutron decay** (bulk-core junction) — established in Companion N
2. **Muon decay** (brane-dominant excitation) — this document

The key new element is the **Chiral Filter** component of the frozen projection
operator, which provides a geometric interpretation of weak interaction chirality
selection.

---

## Document Structure

| Section | Title | Content |
|---------|-------|---------|
| §1 | Motivation | Why μ-decay = pure brane test (no baryonic topology) |
| §2 | Thick-Brane Pipeline | Muon as brane-dominant excitation [P] |
| §3 | Energy Bookkeeping | Ledger structure without bulk contribution |
| §4 | Selection Rules | Allowed outputs $\mathcal{A}_\mu = \{e^-, \nu_\mu, \bar{\nu}_e\}$ |
| §5 | Frozen Projection | Chiral filter decomposition [P]/[OPEN] |
| §6 | Falsifiability | 6 guardrails for model testing |

---

## Epistemic Tag Map

| Claim | Tag | Status |
|-------|-----|--------|
| Muon is brane-dominant excitation | [P] | Postulated, not derived |
| Energy ledger structure | [Def]/[Dc] | Defined, follows from conservation |
| Allowed output set $\mathcal{A}_\mu$ | [Def]/[Dc] | Derived from conservation laws |
| Chiral filter $\mathcal{P}_{\mathrm{chir}}$ | [P]/[OPEN] | Postulated, mechanism open |
| $\tau_\mu = 2.197 \times 10^{-6}$ s | [BL] | Baseline (PDG) |
| Forbidden channels (branching ratios) | [BL] | Baseline (experimental limits) |
| No bulk escape in muon decay | [P] | Postulated (consistency with ontology) |

---

## Key Equations

### Chiral Filter Decomposition (Eq. 2)
```latex
\mathcal{P}_{\mathrm{frozen}} = \mathcal{P}_{\mathrm{energy}} \circ
\mathcal{P}_{\mathrm{mode}} \circ \mathcal{P}_{\mathrm{chir}}
```

### Energy Ledger (Eq. 1)
```latex
m_\mu c^2 = E_{e^-} + E_{\nu_\mu} + E_{\bar{\nu}_e} + E_{\mathrm{other}}
```

---

## Figures

| Figure | Description | Styles Used |
|--------|-------------|-------------|
| Fig. 1 | Muon ontology (brane-dominant vs bulk junction) | `bulk region`, `brane region`, `observer region`, `particle`, `neutrino` |
| Fig. 2 | Energy flow diagram with chiral filter | `brane box`, `process box`, `output box`, `edc flow`, `phase label` |

---

## Open Problems Flagged

1. **Derive $\mathcal{P}_{\mathrm{chir}}$ from boundary conditions** [OPEN]
2. **Map $\Gamma_{\mathrm{eff}}$ to brane microphysics** [OPEN]
3. **Extend to tau decay** [OPEN]
4. **Test pion decay ($\pi \to \mu\nu$)** [OPEN]

---

## Build Verification

```bash
cd edc_papers/paper_3_series/11_companion_M_muon_decay_tomography/paper/
xelatex -interaction=nonstopmode main.tex && xelatex main.tex
# Output: main.pdf (8 pages)
```

---

## Stabilization Patch (v0.2) — 2026-01-20

### Changes Made

| Item | Before | After |
|------|--------|-------|
| Branching ratio | "≈ 100% [BL]" | "dominant channel [BL]; rare radiative modes exist" |
| Forbidden channels table | Single "EDC interpretation" column | Separated: Exp. limit [BL] + EDC interpretation [P]/[OPEN] |
| Chiral filter box | "emerges from geometry" | "we propose... consistent with... [P]/[OPEN]" |
| Bulk escape | "cannot escape" | "suppressed leakage; negligible at leading order [P]" |
| PDG reference | None | Added \cite{PDG2024} with τ_μ, BR limits |
| P_chir math hook | None | Added §5.3 with BC sketch (Eq. 4) [P]/[OPEN] |

### Epistemic Tag Updates

| Claim | Old Tag | New Tag |
|-------|---------|---------|
| LFV channels interpretation | implicit | [P]/[OPEN] explicit |
| Mode mismatch hypothesis | "Mode incompatibility" | "Mode mismatch hypothesis [P]/[OPEN]" |
| Chiral filter mechanism | "emerges" | "we hypothesize... [P]/[OPEN]" |
| Bulk leakage | "[P] cannot" | "[P] suppressed, negligible at leading order" |

### New Content

**§5.3 Formal Sketch: Boundary as Chiral Projector**
- Schematic boundary condition: $(1 - i\gamma^5 \hat{n}\cdot\gamma)\psi|_{y=+\delta/2} = 0$
- Explicitly marked [P]/[OPEN]
- MIT-bag-like analogy mentioned
- Status: plausibility argument, not proof

### Build Result

- Pages: 8 (was 5)
- Overfull boxes: 0
- Undefined references: 0

---

## Files Created

```
11_companion_M_muon_decay_tomography/
├── paper/
│   ├── main.tex          # Main document (8 pages after v0.2)
│   └── main.pdf          # Compiled output
└── PATCH_NOTES_MUON_PHASE.md  # This file
```

---

## Relationship to Other Companions

| Document | Relationship |
|----------|--------------|
| Companion N (Neutron Junction) | Same pipeline, different ontology (bulk vs brane) |
| Companion H (Weak Interactions) | Thick-brane foundation; H is published, not modified |
| Framework v2.0 | Three-layer ontology definition |

---

## Next Steps

1. **Tau decay companion** — Apply same framework to $\tau \to \ell + \nu + \bar{\nu}$
2. **Pion decay test** — Hadron→lepton transition via $\pi^+ \to \mu^+ + \nu_\mu$
3. **Chiral filter derivation** — Attempt geometric construction from $y = +\delta/2$ boundary

---

*Generated: 2026-01-20 (Muon Decay Tomography Phase)*
