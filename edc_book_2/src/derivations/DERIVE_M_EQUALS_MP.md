# Derivation Attempt: M = m_p from 5D Action

**Date:** 2026-01-28
**Status:** IN PROGRESS
**Goal:** Derive why the effective mass M in ω₀ = √(σ/M) equals the proton mass m_p

---

## 1. The Problem

In the attempt frequency formula:

$$\omega_0 = \sqrt{\frac{\sigma}{M}}$$

we have PROPOSED [P] that M = m_p. This gives ω₀ ≈ 19 MeV.

**Question:** Can we DERIVE M = m_p from the 5D action?

---

## 2. Naive Estimate (FAILS)

### 2.1 Dimensional Analysis

From brane tension σ and junction size L₀:

$$M_{naive} \sim \frac{\sigma L_0^2}{c^2} = \frac{8.82 \text{ MeV/fm}^2 \times (1 \text{ fm})^2}{c^2} \approx 8.82 \text{ MeV}$$

### 2.2 The Problem

$$\frac{M_{naive}}{m_p} = \frac{8.82}{938} \approx 0.0094 \approx \frac{1}{106}$$

The naive estimate is **~100× too small!**

### 2.3 Implication

If M = σL₀²/c², then:
$$\omega_0 = \sqrt{\frac{\sigma}{M}} = \sqrt{\frac{\sigma c^2}{\sigma L_0^2}} = \frac{c}{L_0} \approx 197 \text{ MeV}$$

This would give τ ~ 9000 s (wrong by factor 10).

**Conclusion:** The naive estimate fails. M must be ~m_p, not σL₀²/c².

---

## 3. Physical Analysis

### 3.1 What is the Collective Coordinate?

The collective coordinate q describes the system's position along the decay path:
- q = 0: neutron state (metastable minimum)
- q = q_barrier: transition state (barrier top)
- q = q_final: proton + e + ν state

### 3.2 What Does M Measure?

M is the **inertia** of motion in q-space:

$$T = \frac{1}{2} M(q) \dot{q}^2$$

This measures how much energy is needed to change q at rate q̇.

### 3.3 Key Insight: Bound State Inertia

The junction is a **bound state** — a localized configuration of brane material.

For a bound state, the inertia of internal rearrangement equals the total rest mass:

$$M = \frac{E_{total}}{c^2}$$

**Analogy:** A ball of clay with mass m. If you squeeze it (internal deformation), the inertia you feel is m, not some smaller quantity.

---

## 4. Derivation from 5D Action

### 4.1 The 5D Action

$$S_{5D} = \int d^4x \, dw \, \sqrt{-g} \left[ \frac{1}{2} g^{AB} \partial_A \phi \partial_B \phi - V(\phi) \right]$$

where φ describes the junction field configuration.

### 4.2 Junction Profile

The junction is a localized configuration:

$$\phi(x, w, t) = \phi_{junction}(x, w; q(t))$$

where q(t) is the collective coordinate.

### 4.3 Kinetic Energy

Substituting into the action:

$$T = \int d^4x \, dw \, \frac{1}{2} \rho(x,w) \left( \frac{\partial \phi}{\partial t} \right)^2$$

Using chain rule:
$$\frac{\partial \phi}{\partial t} = \frac{\partial \phi}{\partial q} \dot{q}$$

So:
$$T = \frac{1}{2} \dot{q}^2 \int d^4x \, dw \, \rho(x,w) \left( \frac{\partial \phi}{\partial q} \right)^2$$

### 4.4 Effective Mass

$$M(q) = \int d^4x \, dw \, \rho(x,w) \left( \frac{\partial \phi}{\partial q} \right)^2$$

This is the **mass integral** — the inertia for collective motion.

### 4.5 Evaluation for Soliton

For a soliton (localized field configuration), standard results give:

$$M = \frac{E_{soliton}}{c^2}$$

where E_soliton is the total energy (rest mass) of the soliton.

**IF the proton is a soliton with E_soliton = m_p c², THEN M = m_p.**

---

## 5. Why E_soliton = m_p c²?

### 5.1 The Soliton Energy

The proton is modeled as a junction soliton. Its energy comes from:

1. **Surface energy:** σ × (surface area) ~ σ L₀² ~ 9 MeV
2. **Topological energy:** from winding/flux configuration
3. **Binding energy:** from non-linear interactions

### 5.2 The Missing Factor ~100

The surface energy alone gives ~9 MeV. The proton mass is 938 MeV.

**Where does the factor ~100 come from?**

Possibilities:
- **Multiple windings:** N ~ 100 flux quanta
- **Bulk energy contribution:** energy from 5D volume, not just surface
- **Strong interaction analog:** QCD gives ~99% of proton mass from gluon field energy

### 5.3 The QCD Analogy

In QCD, the proton mass comes mostly from gluon field energy, not quark masses:
- Quark masses: ~10 MeV
- Proton mass: 938 MeV
- Ratio: ~100×

**Hypothesis:** In EDC, the junction mass similarly comes from "flux field energy" in the 5D bulk, not just brane surface tension.

### 5.4 Bulk Energy Estimate

If the junction involves flux tubes extending into the bulk:

$$E_{bulk} \sim \sigma_{bulk} \times V_{bulk}$$

With V_bulk ~ L₀³ and σ_bulk ~ σ/L₀:

$$E_{bulk} \sim \sigma L_0^2$$

This still gives ~9 MeV. The enhancement must come from elsewhere.

---

## 6. Alternative Approach: Use the Relation m_p/m_e = 6π⁵

### 6.1 From Turning Point Document

The relation m_p/m_e = 6π⁵ ≈ 1836.12 has been identified [I] in EDC.

If this is geometric in origin, then m_p is determined by:

$$m_p = 6\pi^5 \times m_e = 6\pi^5 \times 0.511 \text{ MeV} = 938.3 \text{ MeV}$$

### 6.2 Implication for M

If m_p is geometrically determined, then the soliton energy is:

$$E_{soliton} = m_p c^2 = 6\pi^5 m_e c^2$$

And the effective mass is:

$$M = m_p = 6\pi^5 m_e$$

### 6.3 Status

This doesn't DERIVE M = m_p from first principles — it uses the identified relation m_p/m_e = 6π⁵.

**Status:** [I] → [P] — identified pattern used as input.

---

## 7. A More Direct Argument

### 7.1 Physical Reasoning

The collective coordinate q describes the **internal state** of the nucleon (neutron vs proton configuration).

Changing q means rearranging the nucleon's internal structure. This rearrangement involves the **entire nucleon mass**.

**Analogy:** Rotating a rigid body. The moment of inertia involves the total mass, even though only the orientation changes.

### 7.2 Formal Statement

For a bound state with total mass M_total, the effective mass for internal rearrangement is:

$$M_{eff} = M_{total} = m_p$$

This is because the internal degrees of freedom are **coupled** to the total mass.

### 7.3 Status

This is a **physical argument**, not a mathematical derivation from the action.

**Status:** [P] — proposed with physical justification.

---

## 8. Summary of Attempts

| Approach | Result | Status |
|----------|--------|--------|
| Naive (σL₀²) | M ~ 9 MeV (wrong) | ✗ FAILS |
| Soliton mass integral | M = E_soliton/c² | [Dc] conditional |
| E_soliton = m_p | Requires m_p input | [P] |
| m_p/m_e = 6π⁵ | Uses identified relation | [I] |
| Physical argument | Bound state inertia = total mass | [P] |

---

## 9. Honest Assessment

### 9.1 What We Can Say

1. **M ≠ σL₀²/c²** — the naive estimate fails by factor ~100
2. **M = E_soliton/c²** — follows from soliton theory [Dc]
3. **E_soliton = m_p c²** — requires additional input [P] or [I]

### 9.2 What We Cannot Say

We CANNOT derive M = m_p purely from σ, L₀, δ without additional input about the soliton energy.

### 9.3 The Gap

The gap is: **Why does the junction soliton have energy m_p c²?**

This is equivalent to: **Why does the proton have the mass it has?**

This is a DEEPER question that we are not answering here.

---

## 10. Conclusion

$$\boxed{M = m_p \quad \text{[P] — justified but not derived from } \sigma, L_0, \delta \text{ alone}}$$

### What IS established:
- M = E_soliton/c² [Dc] from soliton theory
- The physical argument that internal rearrangement inertia = total mass

### What is NOT established:
- Derivation of E_soliton = m_p c² from 5D geometry alone
- This would require understanding why m_p = 6π⁵ m_e

### Status Unchanged

ω₀ = √(σ/m_p) remains **[P]** — the M = m_p identification is physically motivated but not derived.

---

## 11. NEW APPROACH: m_p from Pure 5D Geometry

### 11.1 The Dimensional Search

What combination of σ, L₀, δ gives m_p?

| Combination | Result | vs m_p |
|-------------|--------|--------|
| σ L₀² | 8.5 MeV | ×110 too small |
| σ L₀³/δ | 84 MeV | ×11 too small |
| **σ L₀⁴/δ²** | **739 MeV** | **×1.27 too small** |

### 11.2 The Discovery

$$\sigma \frac{L_0^4}{\delta^2} = 8.82 \times \frac{(0.980)^4}{(0.105)^2} = 739 \text{ MeV}$$

Ratio to m_p: 938/739 = **1.27 ≈ 4/3**

### 11.3 Candidate Formula

$$\boxed{m_p = \frac{4}{3} \cdot \sigma \frac{L_0^4}{\delta^2}}$$

Check: (4/3) × 739 = **985 MeV** (error 5%)

### 11.4 Alternative: L₀/δ = π² exactly

If L₀ = π²δ (suspected geometric relation):

$$m_p = \sigma \cdot \pi^8 \cdot \delta^2 = 8.82 \times 9488 \times 0.011 = 922 \text{ MeV}$$

Error: 1.7% without any additional factor!

### 11.5 Physical Interpretation

$$m_p \sim \sigma L_0^2 \times \left(\frac{L_0}{\delta}\right)^2$$

- **σL₀²** = surface energy (2D brane contribution)
- **(L₀/δ)²** = enhancement from **5D depth structure**

The junction is NOT a 2D surface — it has **depth** into the 5th dimension that contributes to mass!

### 11.6 Connection to EM Projection (Chapter 5)

Just as E and B are projections of the unified F_AB:

| EM | Mass |
|----|------|
| 5D: F_AB unified | 5D: Junction has volume L₀³ |
| 3D: E from F_wi, B from F_ij | 3D: See only surface L₀² |
| Projection factor: c | Mass factor: (L₀/δ)² |

### 11.7 The 4/3 Factor

This factor appears in:
- EM mass of charged sphere: m = (4/3)(e²/R)/(4πε₀c²)
- Volume/surface ratio for spheres
- Some relativistic corrections

**Hypothesis:** 4/3 arises from spherical geometry of junction.

### 11.8 Updated Status

$$m_p = \frac{4}{3} \sigma \frac{L_0^4}{\delta^2} \quad \text{[I] — identified pattern}$$

This is NOT a full derivation, but:
- Uses ONLY EDC parameters (σ, L₀, δ)
- Reproduces m_p to 5%
- Has physical interpretation (5D depth)
- Factor 4/3 may have geometric origin

---

## 12. Revised Path Forward

### Option A: Accept as [I]
The formula m_p = (4/3)σL₀⁴/δ² is an identified pattern. Combined with M = E_soliton/c², this gives M = m_p with geometric motivation.

### Option B: Derive 4/3
Show that the junction has spherical geometry, leading to the 4/3 factor.

### Option C: Derive L₀/δ = π²
If L₀/δ = π² exactly, then m_p = σπ⁸δ² without the 4/3 factor.

---

## 13. Summary

| Before | After |
|--------|-------|
| M = m_p [P] arbitrary | M = m_p [I] with geometric formula |
| No connection to σ, L₀, δ | m_p ≈ (4/3)σL₀⁴/δ² |
| QCD analogy | Pure 5D interpretation |

**Progress:** M = m_p now has **geometric motivation** from 5D, though not a complete derivation.

---

## 14. Version History

- 2026-01-28 v1.0: Initial derivation attempt
- 2026-01-28 v1.1: Added 5D geometric approach (m_p ~ σL₀⁴/δ²)
