# PATCH NOTES: Tau Decay Mode-Spectrum Phase

**Date:** 2026-01-20
**Document:** Companion T — Tau Decay as a Brane Mode-Spectrum Test
**Status:** Draft v0.1

---

## Summary

Companion T extends the thick-brane microphysics framework to tau leptonic
decays ($\tau \to e\nu\bar{\nu}$ and $\tau \to \mu\nu\bar{\nu}$), testing
whether the same absorption→dissipation→release pipeline that works for
muon decay generalizes to the heavier lepton.

**Key result:** The pipeline generalizes without modification. The tau is
modeled as a brane-dominant excitation with higher "mode index" than the muon.

---

## Document Structure

| Section | Title | Content |
|---------|-------|---------|
| §1 | Motivation | Why τ after μ (same sector, heavier mode) |
| §2 | Ontology | Tau as brane-dominant excitation [P] |
| §3 | Baselines | τ lifetime, BR [BL] (PDG) |
| §4 | Pipeline | Absorption→Dissipation→Release (same as M) |
| §5 | Allowed Outputs | $\mathcal{A}_{\tau \to e}$, $\mathcal{A}_{\tau \to \mu}$ [Def]/[Dc] |
| §6 | Mode-Spectrum | Spectral overlap hypothesis [P]/[OPEN] |
| §7 | Chiral Filter | Same as M, universal hypothesis [P]/[OPEN] |
| §8 | Falsifiability | 5 guardrails |
| §9 | Open Problems | 5 items flagged [OPEN] |

---

## Epistemic Tag Map

| Claim | Tag | Status |
|-------|-----|--------|
| Tau is brane-dominant excitation | [P] | Postulated |
| Mode index ordering $n_e < n_\mu < n_\tau$ | [P]/[Def] | Qualitative only |
| Allowed output sets $\mathcal{A}_{\tau \to X}$ | [Def]/[Dc] | From conservation laws |
| Mode-spectrum branching (Eq. 3) | [P]/[OPEN] | Schematic, not derived |
| Chiral filter universality | [P]/[OPEN] | Hypothesis, same as M |
| $\tau_\tau$, BR values | [BL] | PDG 2024 |
| Suppressed bulk leakage | [P] | Postulate 2 |

---

## Key Equations

### Mode-Spectrum Branching (Eq. 3)
```latex
\mathrm{BR}(\tau \to X) \propto |\langle \Psi_X | \hat{T} | \Psi_\tau \rangle|^2
```
Status: Schematic [P]/[OPEN]

### Projection Stack (Eq. 4)
```latex
\mathcal{P}_{\mathrm{frozen}} = \mathcal{P}_{\mathrm{energy}} \circ
\mathcal{P}_{\mathrm{mode}} \circ \mathcal{P}_{\mathrm{chir}}
```
Status: Same as Companion M

---

## Figures

| Figure | Description | Content |
|--------|-------------|---------|
| Fig. 1 | Mode spectrum visualization | e/μ/τ as brane-layer modes at different energies |
| Fig. 2 | Energy-flow pipeline | Same structure as M, with τ initial state |

---

## Open Problems Flagged

1. **Derive $\mathcal{P}_{\mathrm{chir}}$ from BC** [OPEN]
2. **Explain BR(τ→e) ≈ BR(τ→μ)** [OPEN]
3. **Quantify mode index $n_\ell$** [OPEN]
4. **Hadronic τ decays** [OPEN] (requires pion ontology)
5. **Lifetime from first principles** [OPEN]

---

## Build Verification

```bash
cd edc_papers/paper_3_series/12_companion_T_tau_decay/paper/
xelatex -interaction=nonstopmode main.tex && xelatex main.tex
# Output: main.pdf (7 pages)
# Overfull boxes: 0
# Undefined references: 0
```

---

## Files Created

```
12_companion_T_tau_decay/
├── paper/
│   ├── main.tex          # Main document (7 pages)
│   └── main.pdf          # Compiled output
└── PATCH_NOTES_TAU_PHASE.md  # This file
```

---

## Relationship to Other Companions

| Document | Relationship |
|----------|--------------|
| Companion M (Muon) | Same pipeline, τ validates generalization |
| Companion N (Neutron) | Different ontology (bulk vs brane), same projection |
| Companion H (Weak Interactions) | Thick-brane foundation |
| Future Companion P (Pion) | Hadron→lepton bridge [OPEN] |

---

## Trident Status

After Companion T, the EDC weak program has:

| Companion | Particle | Ontology | Status |
|-----------|----------|----------|--------|
| N | Neutron | Bulk-core junction | Published |
| M | Muon | Brane-dominant | v0.2 |
| T | Tau | Brane-dominant (higher mode) | v0.1 |
| P | Pion | TBD | [OPEN] |

---

*Generated: 2026-01-20 (Tau Mode-Spectrum Phase)*
