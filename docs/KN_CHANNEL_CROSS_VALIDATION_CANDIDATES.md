# k(N) Channel Cross-Validation Candidates

**Created:** 2026-01-29
**Purpose:** Catalog of candidate systems where k(N) = 1 + 1/N discrete averaging correction could be tested
**Status:** Candidate list only; no empirical confirmation yet

---

## Overview

The k-channel mechanism predicts that discrete sampling at N symmetric points gives an observable ratio:

```
k(N) = ⟨O⟩_disc / ⟨O⟩_cont = 1 + 1/N
```

This arises when:
1. The observable has Z_N-symmetric anisotropy: O(θ) = c + a·cos(Nθ)
2. Discrete sampling hits the peaks (cos(Nθ_n) = 1)
3. Continuum averaging washes out the cos term

**Goal:** Find N ≠ 6 systems where this ratio can be measured or simulated.

---

## Category I: Wave/Oscillator Rings

### Candidate 1: Ring of Coupled Pendulums

| Field | Value |
|-------|-------|
| **N range** | 3–12 (easily adjustable) |
| **Discrete** | N pendulums at θ_n = 2πn/N |
| **Continuum** | Continuous elastic ring (limit N → ∞) |
| **Observable** | Energy in fundamental anisotropic mode / total energy |
| **Measurement** | Tabletop experiment or simulation (ODE system) |
| **Confidence** | **HIGH** — clean mechanical analog, N easily varied |

**Discrete vs Continuum:**
- Discrete: Measure kinetic energy at N pendulum positions, sum
- Continuum: Integrate energy density over continuous ring

**Expected signal:** Mode energy ratio should show k(N) = 1 + 1/N for N-fold symmetric excitation.

---

### Candidate 2: Circular Array of Coupled Oscillators (Electronic)

| Field | Value |
|-------|-------|
| **N range** | 4–16 (PCB or breadboard) |
| **Discrete** | N LC oscillators coupled in a ring |
| **Continuum** | Transmission line ring (distributed LC) |
| **Observable** | Voltage amplitude ratio at resonance |
| **Measurement** | Circuit simulation (SPICE) or bench prototype |
| **Confidence** | **HIGH** — standard RF engineering, cheap to simulate |

**Key insight:** Lumped-element (discrete) vs distributed (continuum) circuits are textbook.

---

### Candidate 3: Acoustic Resonator Ring

| Field | Value |
|-------|-------|
| **N range** | 3–8 (Helmholtz resonators) |
| **Discrete** | N Helmholtz resonators coupled via tubes |
| **Continuum** | Continuous annular duct |
| **Observable** | Pressure amplitude at anti-nodes |
| **Measurement** | FEM simulation (COMSOL) or 3D-printed prototype |
| **Confidence** | **MED** — more complex fabrication, but well-understood physics |

---

## Category II: Lattice / Solid-State

### Candidate 4: Spin Chain with Periodic BC

| Field | Value |
|-------|-------|
| **N range** | 4–20 (exact diagonalization feasible) |
| **Discrete** | N spins on a ring, Heisenberg or Ising model |
| **Continuum** | Spin-wave theory (magnon dispersion) |
| **Observable** | Ground state energy per site: E_N vs E_∞ |
| **Measurement** | Numerical exact diagonalization or DMRG |
| **Confidence** | **HIGH** — well-studied finite-size scaling |

**Note:** Finite-size corrections in spin chains often scale as 1/N; k-channel predicts specific coefficient.

---

### Candidate 5: Phonons in Ring-Shaped Nanostructures

| Field | Value |
|-------|-------|
| **N range** | 6–60 (carbon nanotube circumference) |
| **Discrete** | Atoms at discrete angular positions |
| **Continuum** | Elastic continuum tube model |
| **Observable** | Specific heat or thermal conductivity anisotropy |
| **Measurement** | MD simulation (LAMMPS) |
| **Confidence** | **MED** — realistic but noisy; N not cleanly variable |

---

### Candidate 6: Josephson Junction Ring

| Field | Value |
|-------|-------|
| **N range** | 3–10 (standard fabrication) |
| **Discrete** | N Josephson junctions in superconducting loop |
| **Continuum** | Continuous weak-link (long junction limit) |
| **Observable** | Critical current modulation with flux |
| **Measurement** | Cryogenic measurement or circuit simulation |
| **Confidence** | **MED** — requires cryo infrastructure; theory well-developed |

**Physics:** Discrete phase slips vs continuous phase winding.

---

## Category III: EM Resonators / Antennas

### Candidate 7: Circular Antenna Array (Phased Array)

| Field | Value |
|-------|-------|
| **N range** | 4–16 (standard array sizes) |
| **Discrete** | N dipoles/monopoles at θ_n = 2πn/N |
| **Continuum** | Continuous current distribution (ring antenna) |
| **Observable** | Array factor gain at broadside |
| **Measurement** | EM simulation (NEC, HFSS) or anechoic chamber |
| **Confidence** | **HIGH** — standard antenna engineering |

**Key ratio:** Discrete array factor vs continuous current integral — directly computable.

---

### Candidate 8: Microwave Cavity with Discrete Ports

| Field | Value |
|-------|-------|
| **N range** | 3–8 (practical port count) |
| **Discrete** | N coupling ports at symmetric positions |
| **Continuum** | Uniform coupling slot |
| **Observable** | Q-factor or transmission coefficient |
| **Measurement** | VNA measurement or CST/HFSS simulation |
| **Confidence** | **MED** — Q-factor has many contributions; isolation needed |

---

### Candidate 9: Optical Ring Resonator with Discrete Couplers

| Field | Value |
|-------|-------|
| **N range** | 2–6 (typical integrated photonics) |
| **Discrete** | N evanescent couplers at discrete points |
| **Continuum** | Distributed coupling (prism or tapered fiber) |
| **Observable** | Finesse or extinction ratio |
| **Measurement** | Photonic simulation (Lumerical) or chip measurement |
| **Confidence** | **MED** — clean physics but fabrication-limited N range |

---

## Category IV: Other Physics Analogs

### Candidate 10: Lattice QCD Temporal Discretization

| Field | Value |
|-------|-------|
| **N range** | N_t = 8–64 (typical lattice sizes) |
| **Discrete** | N_t time slices in Euclidean path integral |
| **Continuum** | Continuum limit a → 0 |
| **Observable** | Hadron mass extrapolation: m(N_t) vs m(∞) |
| **Measurement** | Re-analyze existing LQCD data |
| **Confidence** | **LOW** — many systematics; k-channel not dominant effect |

**Caution:** LQCD finite-size effects are well-studied with different scaling forms.

---

### Candidate 11: Crystal Field Splitting (d-orbitals)

| Field | Value |
|-------|-------|
| **N range** | 4 (tetrahedral), 6 (octahedral), 8 (cubic) |
| **Discrete** | N ligands at discrete positions |
| **Continuum** | Spherically-averaged potential |
| **Observable** | Energy splitting ratio (e.g., Δ_oct vs Δ_tet) |
| **Measurement** | Spectroscopy data (tabulated) |
| **Confidence** | **LOW** — ratio is 4/9, not 1+1/N; different physics |

**Note:** This is a negative control — crystal field theory gives different ratios.

---

### Candidate 12: Discrete Fourier Transform Aliasing

| Field | Value |
|-------|-------|
| **N range** | Any (numerical) |
| **Discrete** | N-point DFT of cos(Nθ) |
| **Continuum** | Continuous Fourier integral |
| **Observable** | Power at DC (m=0) vs total power |
| **Measurement** | Trivial numerical test |
| **Confidence** | **HIGH** — mathematical identity, not physics |

**Purpose:** Sanity check that k(N) formula is correct numerically before physical tests.

---

## Summary Table

| # | Candidate | N range | Confidence | Best for |
|---|-----------|---------|------------|----------|
| 1 | Coupled pendulums | 3–12 | HIGH | Tabletop demo |
| 2 | LC oscillator ring | 4–16 | HIGH | Circuit simulation |
| 3 | Acoustic resonators | 3–8 | MED | FEM validation |
| 4 | Spin chain | 4–20 | HIGH | Numerical benchmark |
| 5 | Nanotube phonons | 6–60 | MED | MD simulation |
| 6 | Josephson ring | 3–10 | MED | Cryo experiment |
| 7 | Antenna array | 4–16 | HIGH | EM simulation |
| 8 | Microwave cavity | 3–8 | MED | RF measurement |
| 9 | Optical ring | 2–6 | MED | Photonics simulation |
| 10 | Lattice QCD | 8–64 | LOW | Data re-analysis |
| 11 | Crystal field | 4,6,8 | LOW | Negative control |
| 12 | DFT aliasing | Any | HIGH | Numerical sanity |

---

## Recommended First Tests

**Tier 1 (cheapest, highest confidence):**
1. **DFT aliasing (#12)** — 10 lines of Python, confirms math
2. **Spin chain (#4)** — exact diagonalization, N = 3–10
3. **LC oscillator ring (#2)** — SPICE simulation

**Tier 2 (moderate effort):**
4. **Coupled pendulums (#1)** — tabletop or ODE simulation
5. **Antenna array (#7)** — NEC2 is free software

---

## EDC-Safe Framing

When presenting k-channel cross-validation tests:

**DO say:**
- "The k(N) = 1 + 1/N formula is a mathematical result about discrete vs continuum averaging"
- "We test whether physical systems with Z_N symmetry exhibit this ratio"
- "This validates the mathematical mechanism, not specific EDC predictions"
- "Analog systems provide sanity checks for the averaging interpretation"

**DO NOT say:**
- "EDC predicts antenna array behavior" (overclaim)
- "k-channel is confirmed by spin chains" (conflation)
- "These experiments prove EDC" (category error)

**Correct framing:**
> "The discrete averaging mechanism underlying EDC's k-channel correction can be tested in analog systems. If the ratio k(N) = 1 + 1/N appears in independent physical contexts, this supports the mathematical interpretation without claiming those systems are described by EDC."

---

## Cross-References

- k-channel derivation: `edc_papers/_shared/lemmas/zn_discrete_averaging_lemma.tex`
- Robustness summary: `edc_papers/_shared/boxes/zn_kchannel_robustness_box.tex`
- EDC applications: `docs/ZN_CORRECTION_CHANNEL.md`
- Universality audit: `docs/ZN_CHANNEL_UNIVERSALITY_AUDIT.md`

---

*Document created 2026-01-29. No empirical tests performed yet.*
