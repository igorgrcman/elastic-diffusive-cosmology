# MISSING LEMMAS: Gap Certificate

**Claim Under Audit:**
> "Proton is a TOPOLOGICAL ENERGY MINIMUM and Steiner 120° geometry is forced by M5 topology + established boundary conditions (BC) in 5D EDC."

**Verdict:** PROOF NOT CLOSED

---

## CRITICAL MISSING LEMMAS

### ML-1: M5 Topology → Z6 Derivation

**Status:** NOT FOUND

**What is needed:**
```
LEMMA (Required): Z6 Symmetry from M5 Brane Topology

Let M⁵ be the 5D bulk manifold with thick-brane Σ embedded.
Let G be the gauge group acting on the order parameter.

Then the boundary conditions on ∂Σ necessarily have Z6 rotational symmetry.

REQUIRED PROOF STEPS:
1. Define the order parameter manifold M
2. Compute the homotopy group π₂(M/G)
3. Show that stable defects (flux tubes) in Σ transform under Z6
4. Derive Z6 from the manifold structure, not as a postulate
```

**What exists instead:**
- Z6 is introduced as Postulate P1 (Z6_content_full.tex:155-166)
- OR derived from Postulate P2 (flux tube interactions) + Kepler-Hales packing
- No derivation from M5 topology exists

**Consequence:** The claim "forced by M5 topology" is UNSUPPORTED.

---

### ML-2: Homotopy Classification of Y-Junction

**Status:** NOT FOUND

**What is needed:**
```
DEFINITION (Required): Y-Junction as Homotopy Class

A Y-junction is a map Φ: S² → M where M is the order parameter manifold,
such that:
1. Φ has winding number (n₁, n₂, n₃) around three asymptotic directions
2. The total winding satisfies n₁ + n₂ + n₃ = 0 (color neutrality)
3. The configuration is classified by an element of π₂(M/G)

REQUIRED PROOF STEPS:
1. Define M explicitly for EDC
2. Compute π₂(M/G) explicitly
3. Show Y-junction is a non-trivial element
4. Prove this element is topologically protected (cannot deform to trivial)
```

**What exists instead:**
- Y-junction is defined geometrically (Z6_content_full.tex:431-435):
  "A Y-junction is a configuration where three defect lines meet at a single point"
- No homotopy group is computed
- No winding number is assigned
- "Topological" appears to mean "protected by Z6 symmetry", not "classified by homotopy"

**Consequence:** The word "TOPOLOGICAL" in the claim is used loosely, not rigorously.

---

### ML-3: Boundary Conditions from M5 Structure

**Status:** NOT FOUND

**What is needed:**
```
LEMMA (Required): BC Emergence from M5

Given the M5 brane structure with metric g_AB and matter content,
the boundary conditions on the thick-brane ∂Σ are uniquely determined.

REQUIRED PROOF STEPS:
1. Write the 5D action S[g, Φ]
2. Derive Euler-Lagrange equations
3. Impose consistency at brane boundary
4. Show that Z6-invariant BC are the unique consistent solution
   (not just a choice)
```

**What exists instead:**
- BC are postulated (Postulate P1)
- The 5D action is not written explicitly in the derivation
- No proof that Z6 is the unique consistent symmetry

**Consequence:** BC are an INPUT, not a DERIVED CONSEQUENCE of M5 structure.

---

### ML-4: Flux Tube Interactions from First Principles

**Status:** NOT FOUND

**What is needed:**
```
LEMMA (Required): Derive Postulate P2

Starting from the 5D EDC action S[g, Φ]:
1. Derive the effective 2D potential V(r) between flux tubes
2. Show V has short-range repulsion (from core overlap)
3. Show V has long-range attraction (from bulk energy minimization)
4. Conclude that V has minimum at characteristic distance r₀

WITHOUT assuming the functional form of V.
```

**What exists instead:**
- Postulate P2 (Z6_content_full.tex:239-253) states the interaction form
- Physical motivation is provided (analogies to superfluids, QCD)
- No derivation from 5D action

**Consequence:** The hexagonal crystallization (L1) depends on a postulate (P2), not a derivation.

---

### ML-5: Proton Uniqueness as Ground State

**Status:** PARTIAL

**What is needed:**
```
THEOREM (Required): Proton is UNIQUE ground state

Among all possible Y-junction configurations:
1. Proton configuration has MINIMUM energy
2. No other configuration has lower or equal energy
3. The proton sector is ISOLATED (finite barrier to other sectors)

REQUIRED: Show no degenerate states exist.
```

**What exists:**
- Theorem L6 shows proton is LOCAL minimum (positive Hessian)
- No proof of GLOBAL uniqueness
- No computation of barrier height to other configurations

**Consequence:** Proton is proven to be A minimum, not THE minimum.

---

## SUMMARY: GAP SEVERITY

| Gap ID | Description | Severity | Impact |
|--------|-------------|----------|--------|
| ML-1 | M5 → Z6 derivation | **CRITICAL** | Main claim unsupported |
| ML-2 | Homotopy classification | **HIGH** | "Topological" is imprecise |
| ML-3 | BC from M5 | **CRITICAL** | BC are postulated |
| ML-4 | Flux tube interactions | **MEDIUM** | Chain depends on postulate |
| ML-5 | Uniqueness of ground state | **LOW** | Local vs global minimum |

---

## HONEST RESTATEMENT OF CLAIM

**Original claim:**
> "Proton is a TOPOLOGICAL ENERGY MINIMUM and Steiner 120° geometry is forced by M5 topology + established boundary conditions in 5D EDC."

**Honest restatement:**
> "Given the postulate of Z6-symmetric boundary conditions (Postulate P1), or given the postulate of flux tube interactions (Postulate P2), the proton Y-junction configuration is a LOCAL energy minimum with Steiner 120° angles (Theorem L6). The stability is protected by the discrete Z6 symmetry, not by homotopy classification."

**Epistemic status:** [Dc] conditional on [P1] or [P2], NOT [Dc] from M5 topology.

---

## PATH TO CLOSURE

To close these gaps and support the original claim:

1. **For ML-1:** Write the explicit 5D action for EDC and derive that Z6 is the unique discrete symmetry compatible with the brane structure.

2. **For ML-2:** Define the order parameter manifold M explicitly, compute π₂(M/G), and show Y-junction corresponds to a non-trivial element.

3. **For ML-3:** Starting from variational principles on the 5D action, derive that BC must have Z6 invariance (not just assume it).

4. **For ML-4:** Derive the flux tube potential V(r) from the 5D field equations, showing repulsion at short range and attraction at long range.

5. **For ML-5:** Compute the full spectrum of Y-junction configurations and show proton is the unique global minimum.

**Estimated difficulty:** HARD. These are research-level problems, not simple derivation gaps.
