# OPEN QUESTIONS V7.7 — TOP 10 KINGPINS

**Created**: 2026-01-31
**Purpose**: Blockers preventing [Der] upgrades
**Status**: [Open]

---

## Kingpin 1: Independent S_α Measurements

**Question**: Do independently measured S_α values correlate with d(n)?

**Current status**: V7.4-V7.7 infer S_α from decay rate residuals. No direct S_α data used.

**Data needed**:
- Spectroscopic factors from (p,t) or (d,⁶Li) reactions
- α-cluster formation probabilities from knockout experiments
- Theoretical S_α from shell model or cluster calculations

**Upgrade path**:
- Obtain S_α values for 20+ nuclides in dataset
- Regress S_α on d(n)
- If r > 0.5: upgrade prefactor mechanism to [I]

**Blocker**: S_α data not in BL whitelist

---

## Kingpin 2: Deformation Proxy

**Question**: Does nuclear deformation (β₂) correlate with d(n)?

**Current status**: Deformation not controlled in any model.

**Risk**: d(n) may proxy for deformation, which affects S_α independently.

**Data needed**:
- Deformation parameters β₂ for actinides
- Source: FRDM or HFB tables

**Upgrade path**:
- Add β₂ as covariate
- If g persists: d(n) is not just deformation proxy
- If g vanishes: deformation is confounding

**Blocker**: β₂ not in BL whitelist

---

## Kingpin 3: Pairing Residuals

**Question**: Does residual pairing energy correlate with d(n)?

**Current status**: Parity classes (EE/EO/OE/OO) control gross pairing. Residual δ(pairing) not controlled.

**Data needed**:
- Pairing gap Δ from mass models
- Odd-even staggering parameters

**Upgrade path**:
- Add pairing residual as covariate
- Test if g changes

**Blocker**: Fine-grained pairing data not in BL whitelist

---

## Kingpin 4: Shell Closure Proximity

**Question**: Does proximity to magic numbers confound d(n) effect?

**Current status**: No explicit shell variable. Hindrance (H1/H2) captures some shell physics.

**Data needed**:
- Distance to nearest magic N, Z
- Subshell closure indicators

**Upgrade path**:
- Add |N - N_magic| and |Z - Z_magic| as covariates
- Test g stability

**Blocker**: Requires defining relevant magic numbers for actinides

---

## Kingpin 5: Isomer Comparison

**Question**: Do isomers of same nuclide show different d(n) correlation?

**Current status**: Only ground-state α-decay analyzed.

**Significance**: If isomers (different configuration, same A) show different residuals, supports structural mechanism.

**Data needed**:
- Isomer half-lives with α-branching
- Spin/parity of isomers

**Upgrade path**:
- Add isomer subset
- Test if residual pattern differs

**Blocker**: Limited isomer α-decay data

---

## Kingpin 6: Temperature Dependence

**Question**: Does the d(n) effect have any T-dependence?

**Current status**: All data at room temperature (or astrophysical inferences).

**Significance**: T-dependence would indicate classical (activated) component, supporting crystal analogy.

**Data needed**:
- α-decay rates at different temperatures (if measurable)
- Astrophysical r-process data at high T

**Upgrade path**:
- If T-dependent: classical S_α contribution
- If T-independent: purely quantum

**Blocker**: Nuclear decays generally T-independent (quantum tunneling)

---

## Kingpin 7: α-Anisotropy Measurements

**Question**: Is α-emission anisotropic for high-d(n) nuclei?

**Current status**: Isotropy assumed. No angular distribution data.

**Significance**: Anisotropy would support M1 (domain mixing) mechanism.

**Data needed**:
- Angular distribution of α-particles for select nuclides
- Comparison: low-d(n) vs high-d(n)

**Upgrade path**:
- If anisotropic: M1 mechanism active
- If isotropic: M1 disfavored

**Blocker**: Specialized experiments required

---

## Kingpin 8: Charge Radius Anomalies

**Question**: Do charge radii show anomalies correlated with d(n)?

**Current status**: Not tested.

**Significance**: Anomalous radii would support M6 (core-mantle) mechanism.

**Data needed**:
- Measured charge radii for actinides
- Comparison with liquid drop predictions

**Upgrade path**:
- Correlate radius anomaly with d(n)
- If correlated: M6 active

**Blocker**: Limited high-precision radius data for transuranics

---

## Kingpin 9: Superheavy Extension

**Question**: Does d(n) effect persist for Z > 100?

**Current status**: Dataset ends at Fm (Z = 100).

**Significance**: Superheavy elements probe higher d(n) values and n approaching 48.

**Data needed**:
- α-decay data for Md, No, Lr, Rf...
- Limited availability, large uncertainties

**Upgrade path**:
- Extend dataset to Z = 104-108
- Test if g persists or changes sign

**Blocker**: Sparse data, short half-lives

---

## Kingpin 10: Mechanism Discrimination

**Question**: Can we distinguish M1/M2/M3/M4/M5/M6 empirically?

**Current status**: All mechanisms are [I] or [P]. No definitive test.

**What's needed**:
- Multiple independent observables (anisotropy, radii, isomers, exotic decays)
- Systematic comparison across forbidden zone

**Upgrade path**:
- Design targeted experiments for each mechanism
- Accumulate discriminating evidence

**Blocker**: Requires experimental program beyond data analysis

---

## Priority Ranking

| Rank | Kingpin | Impact | Feasibility |
|------|---------|--------|-------------|
| 1 | Independent S_α | High | Medium |
| 2 | Deformation proxy | High | Medium |
| 3 | Shell proximity | Medium | High |
| 4 | Isomer comparison | Medium | Medium |
| 5 | Pairing residuals | Medium | Medium |
| 6 | α-Anisotropy | High | Low |
| 7 | Charge radii | Medium | Low |
| 8 | Superheavy | Medium | Low |
| 9 | Mechanism discrimination | High | Low |
| 10 | T-dependence | Low | Low |

---

## Summary

| Status | Count |
|--------|-------|
| Data blockers | 6 (S_α, β₂, pairing, radii, anisotropy, SHE) |
| Method blockers | 2 (mechanism, T-dependence) |
| Partially addressable | 2 (shell, isomers) |

**Bottom line**: Upgrading prefactor mechanism from [P] to [I] or [Der] requires independent S_α data or deformation control — neither currently in BL whitelist.

