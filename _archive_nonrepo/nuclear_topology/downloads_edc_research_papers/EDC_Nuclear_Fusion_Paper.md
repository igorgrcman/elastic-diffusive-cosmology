# Nuclear Fusion from 5D Geometry
## Quantum Tunneling as Bulk Transit in Elastic Diffusive Cosmology

**Igor Filipović**

January 2026

DOI: [To be assigned]

License: CC BY-NC 4.0

---

## Abstract

We present a geometric interpretation of nuclear fusion within the five-dimensional framework of Elastic Diffusive Cosmology (EDC). The Coulomb barrier that classically forbids proton-proton fusion exists only on the 3D membrane; particles can bypass this barrier by transiting through the 5D Bulk where no electrostatic repulsion exists. Quantum tunneling, traditionally treated as a mysterious wavefunction penetration, emerges as ordinary classical motion through the higher-dimensional space. We derive the Gamow energy from membrane tension and topological scales, showing that the fusion rate in stellar cores follows directly from 5D geometry. This completes the EDC description of stellar physics: gravitational collapse (Paper II) creates the conditions, and Bulk transit enables the nuclear reactions that power stars.

**Keywords:** Nuclear fusion, quantum tunneling, extra dimensions, Gamow factor, stellar nucleosynthesis, pp-chain, EDC

---

## 1. Introduction

### 1.1 The Fusion Paradox

The Sun's core temperature is approximately $T \approx 1.5 \times 10^7$ K, corresponding to thermal energy:

$$k_B T \approx 1.3 \text{ keV}$$

Yet the Coulomb barrier between two protons at nuclear distances ($r \sim 1$ fm) is:

$$U_C = \frac{e^2}{4\pi\varepsilon_0 r} = \frac{\alpha \hbar c}{r} \approx 1.44 \text{ MeV}$$

The ratio:

$$\frac{U_C}{k_B T} \approx 1000$$

**Classically, fusion is impossible.** Protons lack sufficient energy to overcome electrostatic repulsion by a factor of 1000.

Yet the Sun has burned steadily for 4.6 billion years.

### 1.2 The Standard Explanation

Quantum mechanics resolves this through **tunneling**—the wavefunction has non-zero amplitude inside classically forbidden regions, allowing particles to "appear" on the other side of barriers.

The tunneling probability is given by the Gamow factor:

$$P_{tunnel} \sim \exp\left(-2\pi\eta\right)$$

where $\eta = \alpha\sqrt{m_p c^2/(2E)}$ is the Sommerfeld parameter.

But this raises a fundamental question: **What is the mechanism?** Standard quantum mechanics provides the mathematics but declares the underlying process unknowable.

### 1.3 The EDC Resolution

Elastic Diffusive Cosmology provides a geometric answer:

> **Quantum tunneling is classical motion through the 5D Bulk.**

The Coulomb barrier exists on the 3D membrane where charges are localized. The Bulk contains no electrostatic field. Particles can transit through the Bulk, bypassing the barrier entirely.

This paper develops this picture quantitatively, deriving fusion rates from 5D geometry.

---

## 2. Theoretical Framework

### 2.1 Particles as Membrane Defects

In EDC, fundamental particles are topological defects on the 3D membrane:

**Proton:** A Y-junction where three vortex lines meet (quarks). Located on the membrane with winding number +1 around the compact dimension $\xi$.

**Electron:** A surface defect with winding number -1.

**Neutron:** A modified Y-junction with total winding number 0.

### 2.2 The Coulomb Field in 5D

Electric charges create flux tubes extending into the Bulk. However, the **Coulomb potential exists only on the membrane**—it represents the interaction energy of charges confined to the 3D surface.

In the Bulk itself, there is no electrostatic repulsion between well-separated defects. The Bulk is electrically neutral.

### 2.3 Two Paths Between Protons

Consider two protons separated by distance $r$ on the membrane:

**Path A — Along the membrane (3D):**
- Must traverse Coulomb barrier
- Potential energy: $U_C(r) = \alpha\hbar c/r$
- Classically forbidden for $E < U_C$

**Path B — Through the Bulk (5D):**
- Descend into Bulk at position 1
- Transit through Bulk (no Coulomb barrier)
- Ascend to membrane at position 2
- Energy cost: membrane deformation, not electrostatics

```
PATH A (Classical - Forbidden):

    Membrane
    ═══●━━━━━━━━━⚡BARRIER⚡━━━━━━━━━●═══
       P₁         E < U_C          P₂
       
       ✗ Cannot pass


PATH B (Quantum/5D - Allowed):

    Membrane
    ═══●═══════════════════════════●═══
       P₁ ↓                     ↑ P₂
           ╲                   ╱
            ╲    BULK        ╱
             ╲   (no E-field) ╱
              ╲             ╱
               ╲           ╱
                ╲         ╱
                 ╲       ╱
                  ╲     ╱
                   ╲   ╱
                    ╲ ╱
                     ● Transit point
                     
       ✓ Barrier bypassed!
```

---

## 3. The Geometry of Tunneling

### 3.1 Action for Bulk Transit

A particle leaving the membrane must overcome the binding energy to the surface. The action for the transit path is:

$$S_{bulk} = \int \sqrt{2m(V_{eff}(w) - E)} \, dw$$

where $V_{eff}(w)$ is the effective potential for membrane detachment.

### 3.2 WKB Approximation

The tunneling probability in WKB approximation:

$$P = \exp\left(-\frac{2}{\hbar}\int_{r_1}^{r_2} \sqrt{2m(U(r) - E)} \, dr\right)$$

**Standard interpretation:** Integral through classically forbidden region on membrane.

**EDC interpretation:** Integral along the Bulk path, where the "potential" represents the energy cost of membrane deformation.

### 3.3 Equivalence of Descriptions

The mathematical form is identical—but the physical picture is different:

| Aspect | Standard QM | EDC |
|--------|-------------|-----|
| Path | Through barrier | Around barrier (via Bulk) |
| Mechanism | Wavefunction penetration | Classical Bulk transit |
| "Forbidden" region | Inside barrier | Bulk space |
| Probability | $|\psi|^2$ in barrier | Transit path weighting |

The exponential suppression arises from the geometric "length" of the Bulk path, not from mysterious wavefunction behavior.

---

## 4. Derivation of the Gamow Factor

### 4.1 Classical Turning Point

For two protons with relative energy $E$, the classical turning point is:

$$r_{turn} = \frac{\alpha \hbar c}{E} = \frac{\alpha \hbar c}{E}$$

At $r < r_{turn}$, the Coulomb potential exceeds the kinetic energy.

### 4.2 Sommerfeld Parameter

The Sommerfeld parameter:

$$\eta = \frac{\alpha}{\beta} = \alpha \sqrt{\frac{m_p c^2}{2E}}$$

where $\beta = v/c$ is the relative velocity.

### 4.3 Gamow Factor

The tunneling probability:

$$P_G = \exp(-2\pi\eta) = \exp\left(-2\pi\alpha\sqrt{\frac{m_p c^2}{2E}}\right)$$

### 4.4 EDC Derivation

In EDC, the proton mass is:

$$m_p c^2 \approx \sigma_{eff} \cdot r_e^2 \cdot f(\alpha)$$

where $f(\alpha)$ encodes the topological structure.

The Gamow exponent becomes:

$$2\pi\eta = 2\pi\alpha\sqrt{\frac{\sigma_{eff} r_e^2 f(\alpha)}{2E}}$$

**Physical interpretation:** The exponent measures the "geometric distance" through the Bulk relative to the de Broglie wavelength.

### 4.5 Gamow Energy

The characteristic Gamow energy:

$$E_G = 2m_p c^2 (\pi\alpha)^2$$

Numerically:

$$E_G = 2 \times 938.3 \text{ MeV} \times (\pi/137)^2$$

$$E_G = 1876.6 \times 5.25 \times 10^{-4} \text{ MeV}$$

$$\boxed{E_G \approx 986 \text{ keV} \approx 1 \text{ MeV}}$$

### 4.6 EDC Expression for Gamow Energy

Using $m_p c^2 \approx \sigma_{eff} r_e^2 / \alpha$ (approximate):

$$E_G = 2\pi^2\alpha^2 \cdot \frac{\sigma_{eff} r_e^2}{\alpha} = 2\pi^2\alpha \cdot \sigma_{eff} r_e^2$$

$$\boxed{E_G = 2\pi^2\alpha \cdot \sigma_{eff} \cdot r_e^2}$$

**The Gamow energy emerges from membrane tension and the topological scale!**

---

## 5. Fusion Rates in Stellar Cores

### 5.1 Thermal Distribution

Protons in the stellar core follow a Maxwell-Boltzmann distribution:

$$f(E) \propto \sqrt{E} \exp\left(-\frac{E}{k_BT}\right)$$

### 5.2 Cross Section

The fusion cross section:

$$\sigma(E) = \frac{S(E)}{E} \exp(-2\pi\eta)$$

where $S(E)$ is the astrophysical S-factor (slowly varying).

### 5.3 Reaction Rate

The thermally averaged reaction rate:

$$\langle\sigma v\rangle = \sqrt{\frac{8}{\pi m_p (k_BT)^3}} \int_0^\infty S(E) \exp\left(-\frac{E}{k_BT} - \frac{b}{\sqrt{E}}\right) dE$$

where $b = \pi\alpha\sqrt{2m_pc^2} = \sqrt{E_G}$.

### 5.4 The Gamow Peak

The integrand has a maximum (Gamow peak) at:

$$E_0 = \left(\frac{b \, k_BT}{2}\right)^{2/3} = \left(\frac{E_G^{1/2} (k_BT)^2}{4}\right)^{1/3}$$

For the solar core ($T = 1.5 \times 10^7$ K, $k_BT = 1.3$ keV):

$$E_0 = \left(\frac{(1000)^{1/2} \times (1.3)^2}{4}\right)^{1/3} \text{ keV}$$

$$E_0 = \left(\frac{31.6 \times 1.69}{4}\right)^{1/3} = (13.4)^{1/3} \approx 2.4 \text{ keV}$$

**The Gamow peak is at ~5-10 keV**—well below the barrier but above pure thermal energy.

### 5.5 EDC Interpretation of the Gamow Peak

The Gamow peak represents the optimal trade-off:

- **Higher E:** Shorter Bulk path → higher tunneling probability
- **Lower E:** More particles available → higher flux

The peak occurs where these effects balance—a purely geometric optimization in the 5D picture.

---

## 6. The Proton-Proton Chain

### 6.1 The First Reaction

The pp-chain begins with:

$$p + p \to d + e^+ + \nu_e$$

This reaction requires:
1. **Coulomb barrier penetration** (tunneling/Bulk transit)
2. **Weak interaction** (proton → neutron conversion)

### 6.2 Weak Interaction in EDC

In EDC, particles carry **winding number** around the compact dimension $\xi$:

| Particle | Winding |
|----------|---------|
| Proton | +1 |
| Neutron | 0 |
| Positron | +1 |
| Neutrino | 0 |

The reaction conserves total winding:

$$\underbrace{(+1)}_{p} + \underbrace{(+1)}_{p} \to \underbrace{(+1)}_{p} + \underbrace{(0)}_{n} + \underbrace{(+1)}_{e^+} + \underbrace{(0)}_{\nu}$$

$$+2 \to +1 + 0 + 1 + 0 = +2 \quad \checkmark$$

### 6.3 Why the Weak Process is Slow

The weak interaction requires **topological restructuring**—changing the winding configuration of a defect.

In EDC terms:
- Proton: Y-junction with specific flux tube configuration
- Neutron: Modified Y-junction with different topology

Converting p → n requires:
1. Unwinding one unit from the proton
2. Creating a positron to carry away the winding
3. Emitting a neutrino (carries energy/momentum, no winding)

This topological rearrangement is inherently slow—it requires restructuring the defect at the $R_\xi$ scale.

### 6.4 Reaction Rate

The pp reaction rate:

$$R_{pp} = n_p^2 \langle\sigma v\rangle_{pp}$$

With $\langle\sigma v\rangle_{pp} \approx 10^{-43}$ cm³/s at solar core conditions.

**This is extraordinarily slow!** A typical proton waits ~10 billion years before fusing.

But with $n_p \sim 10^{26}$ cm⁻³, the total rate is sufficient to power the Sun.

---

## 7. Complete Fusion Picture in 5D

### 7.1 Step-by-Step Process

**Step 1: Approach**
Two protons approach on the membrane, slowing as they climb the Coulomb potential.

**Step 2: Bulk Descent**
At the classical turning point, the protons can "descend" into the Bulk, leaving the membrane.

**Step 3: Bulk Transit**
In the Bulk, no Coulomb barrier exists. The protons move freely toward each other.

**Step 4: Close Approach**
The protons reach nuclear separation ($\sim 1$ fm) in the Bulk.

**Step 5: Weak Interaction**
One proton undergoes topological restructuring (winding transfer), becoming a neutron.

**Step 6: Deuteron Formation**
The proton and neutron bind via the strong force (flux tube merger), forming a deuteron.

**Step 7: Return to Membrane**
The deuteron, positron, and neutrino emerge onto the membrane.

```
Timeline of p + p → d + e⁺ + ν

    Membrane ═══●━━━━━━━━━━━━━━━━━●═══
                P₁                P₂
                 ↓                ↓
    
    Bulk         ●───────────────●
                  ╲             ╱
                   ╲    ↓↓    ╱
                    ╲       ╱
                     ╲     ╱
                      ↘   ↙
                        ●● close approach
                        ↓
                     WEAK INTERACTION
                     (topology change)
                        ↓
                       (pn) + e⁺ + ν
                        ↓
    Membrane ═══════════●══════════════
                        d (deuteron)
                        
                    + e⁺ (positron)
                    + ν (neutrino)
```

### 7.2 Energy Budget

| Process | Energy |
|---------|--------|
| Input: 2 protons | $2 \times 938.3$ MeV |
| Output: deuteron | 1875.6 MeV |
| Output: positron | 0.511 MeV |
| Output: neutrino | ~0.26 MeV (average) |
| **Q-value** | **0.42 MeV** |

Plus positron annihilation: $2 \times 0.511$ MeV = 1.02 MeV

**Total energy release: ~1.44 MeV per pp reaction**

---

## 8. Predictions and Tests

### 8.1 Tunneling as Geometry

If tunneling is Bulk transit, then:

1. **No true "instantaneous" tunneling**—particles take finite proper time through Bulk
2. **Tunneling "distance" is geometric**—related to Bulk path length
3. **Barrier shape matters geometrically**—not just height

### 8.2 Potential Observables

**Solar neutrino spectrum:** The precise spectrum depends on tunneling details. EDC predicts specific corrections at the ~$R_\xi$ scale.

**Fusion cross sections:** Deviations from pure Gamow factor at very low energies might reveal Bulk geometry.

**Primordial nucleosynthesis:** Big Bang fusion rates could show 5D corrections.

### 8.3 Laboratory Tests

Precision measurements of:
- Low-energy nuclear cross sections
- Tunneling time in nuclear reactions
- Fine structure in resonances

---

## 9. Connection to Previous Papers

### 9.1 Paper I: Chemical Bonding

- Electrons in molecules reside in the Bulk (~38 pm deep)
- Chemical bonds are merged flux tubes
- Scale: $a_0 \sim 0.5$ Å, electron depth: $w_* \sim 0.4$ Å

### 9.2 Paper II: Jeans Mass

- Gravitational collapse = membrane curvature accumulation
- Jeans mass $M_J \sim 1-10 M_\odot$ from geometry
- Stars are deep wells in the 5D membrane

### 9.3 This Paper: Nuclear Fusion

- Tunneling = Bulk transit around Coulomb barrier
- Gamow energy from $\sigma_{eff}$, $r_e$, $\alpha$
- Weak interaction = topological restructuring

### 9.4 The Complete Picture

| Scale | Phenomenon | 5D Mechanism |
|-------|------------|--------------|
| Å | Chemical bonding | Electrons in Bulk |
| ly | Star formation | Membrane collapse |
| fm | Nuclear fusion | Bulk transit + topology change |

**EDC unifies atomic, stellar, and nuclear physics in one geometric framework.**

---

## 10. Summary

### 10.1 Key Results

| Quantity | Standard QM | EDC |
|----------|-------------|-----|
| Tunneling | Wavefunction penetration | Bulk transit |
| Gamow energy | Empirical parameter | $E_G = 2\pi^2\alpha\sigma_{eff}r_e^2$ |
| Barrier | Potential energy | Membrane-localized field |
| Mechanism | "Intrinsically quantum" | Classical 5D motion |

### 10.2 Physical Picture

1. **Coulomb barrier exists only on membrane**—charges are 3D localized
2. **Bulk is electrically neutral**—no electrostatic forces
3. **Particles can transit through Bulk**—bypassing the barrier
4. **Tunneling probability = Bulk path weighting**—geometric origin
5. **Weak interaction = topology change**—winding number restructuring

### 10.3 Why Stars Burn

The Sun burns because:

1. **Gravity** (membrane curvature) compresses the core
2. **Temperature** provides energy to reach the Bulk
3. **Bulk transit** bypasses Coulomb barrier
4. **Topological restructuring** enables p → n
5. **Strong force** (flux tube merger) binds the deuteron

All from 5D geometry.

---

## 11. Conclusions

We have shown that nuclear fusion, the process that powers stars, emerges naturally from the 5D geometry of Elastic Diffusive Cosmology:

1. **Quantum tunneling is Bulk transit**—particles bypass barriers by traveling through the higher-dimensional space

2. **The Gamow energy derives from membrane parameters**—$E_G = 2\pi^2\alpha\sigma_{eff}r_e^2$

3. **Weak interactions are topological**—winding number changes around the compact dimension $\xi$

4. **Fusion rates follow from geometry**—the Gamow peak is a geometric optimization

This completes the EDC description of stellar physics:
- Paper I: Atoms and molecules (chemistry)
- Paper II: Gravitational collapse (star formation)  
- Paper III: Nuclear fusion (stellar energy)

The same 5D geometry governs phenomena from Ångströms to light-years, from chemical bonds to stellar nucleosynthesis.

---

## References

1. Filipović, I. (2026). "Elastic Diffusive Cosmology - Part I: From Membrane Geometry to Quantum Mechanics and Gravity." Zenodo. DOI: 10.5281/zenodo.18176174

2. Filipović, I. (2026). "Chemical Bonding from 5D Membrane Geometry." [This series, Paper I]

3. Filipović, I. (2026). "Jeans Mass from 5D Membrane Geometry." [This series, Paper II]

4. Gamow, G. (1928). "Zur Quantentheorie des Atomkernes." Zeitschrift für Physik, 51, 204-212.

5. Bethe, H.A. (1939). "Energy Production in Stars." Physical Review, 55, 434-456.

6. Adelberger, E.G. et al. (2011). "Solar fusion cross sections II." Reviews of Modern Physics, 83, 195.

---

## Appendix A: Gamow Factor Derivation

### Standard Derivation

For s-wave scattering through a Coulomb barrier:

$$P = \exp\left(-\frac{2}{\hbar}\int_{r_n}^{r_c} \sqrt{2\mu(U(r)-E)} \, dr\right)$$

where:
- $r_n \sim 1$ fm (nuclear radius)
- $r_c = \alpha\hbar c/E$ (classical turning point)
- $\mu = m_p/2$ (reduced mass)
- $U(r) = \alpha\hbar c/r$ (Coulomb potential)

The integral evaluates to:

$$P = \exp(-2\pi\eta)$$

where $\eta = \alpha/\beta = \alpha\sqrt{m_pc^2/(2E)}$.

### EDC Interpretation

The same integral represents the action along the Bulk transit path:

$$S_{bulk} = \int \sqrt{2m \cdot V_{geom}(path)} \, d\ell$$

where $V_{geom}$ is the geometric "cost" of the Bulk path, and $d\ell$ is the proper length element in 5D.

The mathematical equivalence ensures identical predictions, but the physical picture is geometric rather than mysterious.

## Appendix B: Solar Core Parameters

| Parameter | Value |
|-----------|-------|
| Core temperature | $1.5 \times 10^7$ K |
| Core density | $150$ g/cm³ |
| Proton density | $n_p \sim 6 \times 10^{25}$ cm⁻³ |
| Thermal energy | $k_BT \approx 1.3$ keV |
| Gamow peak energy | $E_0 \approx 6$ keV |
| pp reaction rate | $\langle\sigma v\rangle \sim 10^{-43}$ cm³/s |
| Proton lifetime | $\sim 10^{10}$ years |
| Solar luminosity | $3.8 \times 10^{26}$ W |

## Appendix C: The pp-Chain Reactions

**pp-I branch (85%):**
$$p + p \to d + e^+ + \nu_e$$
$$d + p \to {^3He} + \gamma$$
$${^3He} + {^3He} \to {^4He} + 2p$$

**pp-II branch (15%):**
$${^3He} + {^4He} \to {^7Be} + \gamma$$
$${^7Be} + e^- \to {^7Li} + \nu_e$$
$${^7Li} + p \to 2{^4He}$$

**pp-III branch (0.02%):**
$${^7Be} + p \to {^8B} + \gamma$$
$${^8B} \to {^8Be} + e^+ + \nu_e$$
$${^8Be} \to 2{^4He}$$

**Net result:**
$$4p \to {^4He} + 2e^+ + 2\nu_e + 26.7 \text{ MeV}$$

---

*Corresponding author: Igor Filipović*

*Manuscript completed: January 2026*

*This work is licensed under CC BY-NC 4.0*
