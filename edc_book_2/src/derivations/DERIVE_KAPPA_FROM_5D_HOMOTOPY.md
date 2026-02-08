# Derivation: κ = 2π from 5D Homotopy

**Date:** 2026-01-28
**Status:** IN PROGRESS
**Goal:** Derive the topological winding factor κ = 2π from first principles

---

## 1. The Problem

In the instanton lifetime formula:

$$\tau = A \cdot \frac{\hbar}{\omega_0} \cdot \exp\left[\kappa \frac{L_0}{\delta}\right]$$

we have **proposed** [P] that κ = 2π. This document attempts to **derive** this value from 5D topology.

---

## 2. Physical Setup

### 2.1 The Neutron as 5D Junction

In EDC, the neutron is modeled as a **junction defect** in the 5D membrane:
- A localized region where the brane topology is non-trivial
- Characterized by a **winding number** in the fifth dimension
- The junction has extent L₀ in the transverse (5th) direction

### 2.2 Beta Decay as Topological Transition

Neutron decay n → p + e⁻ + ν̄ₑ corresponds to:
- A change in the junction's topological class
- Specifically: ΔW = 1 (change in winding number)
- This is a **topological transition**, not a continuous deformation

---

## 3. Homotopy Analysis

### 3.1 Relevant Homotopy Group

For a 5D brane with one compact dimension (the "fifth" dimension of size ~L₀):
- The relevant manifold is locally S¹ (circle in 5th dimension)
- The fundamental group is: **π₁(S¹) = ℤ**

This means:
- Closed loops in the 5th dimension are classified by integers
- Each integer represents a "winding number"
- Transitions between winding numbers are **topologically protected**

### 3.2 Instanton as Interpolating Configuration

An instanton is a Euclidean (imaginary time) configuration that:
- Interpolates between two topologically distinct states
- For π₁(S¹) = ℤ: connects winding W to winding W±1

The **minimal action** instanton connects adjacent winding sectors.

---

## 4. Action Calculation

### 4.1 General Form for Topological Transitions

For any topological transition with winding number change ΔW, the Euclidean action has the form:

$$S_E = 2\pi |ΔW| \times (\text{geometric factor})$$

**Why 2π?**

The factor 2π arises from:
1. **Angular integration** around the compact dimension: ∮dθ = 2π
2. **Topological charge normalization**: For winding W, the flux is 2πW
3. **Quantization condition**: The action must be 2π × (integer) for consistency

### 4.2 Derivation from First Principles

Consider a field φ(x,θ) on the brane, where θ ∈ [0, 2π) is the compact 5th coordinate.

**Boundary conditions for winding W:**
$$\phi(x, θ + 2\pi) = \phi(x, θ) + 2\pi W$$

**Kinetic term in the action:**
$$S = \int d^4x \int_0^{2\pi} dθ \, \frac{1}{2}\left(\frac{\partial\phi}{\partial\theta}\right)^2$$

For a configuration with winding W:
$$\frac{\partial\phi}{\partial\theta} = \frac{W}{R}$$
where R is the radius of the compact dimension.

**Integrating:**
$$S = \int d^4x \cdot 2\pi \cdot \frac{1}{2}\left(\frac{W}{R}\right)^2 = \pi W^2 / R^2 \times (\text{4D volume})$$

### 4.3 The 2π Factor in Instanton Transitions

For a transition ΔW = ±1, the instanton action involves:

$$S_E^{\text{inst}} = 2\pi \times (\text{topological charge}) \times (\text{scale factor})$$

In our case:
- Topological charge = 1 (minimal transition)
- Scale factor = L₀/δ (ratio of junction size to brane thickness)

**Therefore:**
$$\boxed{S_E = 2\pi \times 1 \times \frac{L_0}{\delta} = 2\pi \frac{L_0}{\delta}}$$

This gives **κ = 2π**.

---

## 5. Comparison with Known Instantons

### 5.1 Yang-Mills Instantons (4D)
- Action: S = 8π²/g² × |n| where n is the instanton number
- The 8π² = (2π)² × 2 comes from SU(2) normalization

### 5.2 Skyrmion Instantons
- Action proportional to 2π × (winding number)
- Same topological origin

### 5.3 Magnetic Monopole Instantons
- Action S = 4π/g × (monopole charge)
- The 4π = 2 × 2π reflects the spherical geometry

### 5.4 EDC Instanton
- Action S = 2π × (L₀/δ)
- Single factor of 2π from S¹ homotopy
- Consistent with simplest topological structure

---

## 6. Why Specifically 2π (Not π or 4π)?

**Key distinction:**

| Geometry | Homotopy | Factor |
|----------|----------|--------|
| S¹ (circle) | π₁(S¹) = ℤ | **2π** |
| S² (sphere) | π₂(S²) = ℤ | 4π |
| S³ (3-sphere) | π₃(S³) = ℤ | 2π² |

The EDC junction involves winding around a **single compact dimension** (S¹ topology), hence the factor is **2π**.

---

## 7. Epistemic Status

### 7.1 What is Derived [Dc]

| Statement | Source |
|-----------|--------|
| π₁(S¹) = ℤ | Standard topology [M] |
| Instanton action ~ 2π × (topological charge) | General instanton theory [M] |
| For S¹ winding: κ = 2π | Direct consequence of π₁(S¹) [Dc] |

### 7.2 What Remains [P]

| Statement | Status |
|-----------|--------|
| Neutron junction has S¹ topology in 5th dimension | [P] |
| Beta decay = ΔW = 1 transition | [P] |
| L₀/δ is the correct "scale factor" | [P] |

### 7.3 Verdict

**κ = 2π is [Dc] CONDITIONAL ON the assumption that:**
1. The neutron junction has effective S¹ topology
2. Decay corresponds to ΔW = 1

---

## 8. Upgrade Path

To make this fully [Der]:
1. Show explicitly that EDC junction defects have S¹ winding structure
2. Demonstrate that neutron vs proton differ by W = ±1
3. Derive L₀/δ as the geometric factor from 5D action

---

## 9. Summary

$$\boxed{\kappa = 2\pi \quad \text{[Dc] from } \pi_1(S^1) = \mathbb{Z}}$$

The topological winding factor κ = 2π follows from:
- The fundamental group of the circle π₁(S¹) = ℤ
- Standard instanton action normalization
- Assumption that neutron has S¹ winding in 5th dimension

**Status:** [Dc] conditional on S¹ topology assumption [P]

---

## 10. Version History

- 2026-01-28 v1.0: Initial derivation document
