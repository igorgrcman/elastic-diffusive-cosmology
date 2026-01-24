# EDC Canonical Notation Policy

**Effective:** 2026-01-24
**Scope:** All EDC papers, books, and companion documents
**Authority:** Aligns Part II (Book) to Paper 2 (DOI: 10.5281/zenodo.18211854) published canon

---

## 1. Canonical 5D Depth Coordinate

| Symbol | Meaning | Units | Domain |
|--------|---------|-------|--------|
| **ξ** (xi) | Physical 5D transverse/depth coordinate | Length | ξ ∈ [0, ∞) or ξ ∈ [0, ℓ] |

**Usage:**
- `ξ` is the ONLY symbol for the physical 5D coordinate in EDC.
- All potentials, profiles, wavefunctions use ξ: `V(ξ)`, `ψ(ξ)`, `f(ξ)`, `m(ξ)`.
- Derivatives: `d/dξ`, `d²/dξ²`.
- Integrals: `∫ ... dξ`.
- Boundary: `ξ = 0` is the observer brane.

**Source:** Paper 2, Postulate 3: "The extra dimension has topology ξ ≅ S¹".

---

## 2. Dimensionless Depth Coordinate

| Symbol | Definition | Domain |
|--------|------------|--------|
| **ξ̃** (`\tilde{\xi}`) | ξ̃ := ξ/ℓ | ξ̃ ∈ [0, 1] |

**Where:**
- `ℓ` is the KK compactification scale or domain size.
- The tilde explicitly marks dimensionless quantities.

**Usage:**
- When rescaling BVP problems: define `ξ̃ := ξ/ℓ`.
- Rescaled potential: `Ṽ(ξ̃) := ℓ² V(ℓξ̃)`.
- Rescaled eigenvalue equation uses ξ̃.

---

## 3. Reserved Symbols (DO NOT USE for 5D depth)

| Symbol | Status | Reason |
|--------|--------|--------|
| **z** | RESERVED | Previously used in drafts; causes confusion with 3D spatial coordinate |
| **ζ** (zeta) | RESERVED | Risk of collision with Riemann zeta function |
| **y** | RESERVED | Common in Randall-Sundrum literature but not EDC canon |

---

## 4. No-Collision Rules

1. **ξ is EXCLUSIVELY the physical 5D depth coordinate.**
   - Never use ξ for coherence length, dimensionless variables, or anything else.

2. **Dimensionless coordinates ALWAYS carry a tilde or hat.**
   - Correct: `ξ̃ := ξ/ℓ`
   - Wrong: `ξ := z/ℓ` (old collision-prone notation)

3. **If a subscript is needed:**
   - `ξ_max` for cutoff (narrative)
   - `ξ_*` for special values (e.g., brane location)

---

## 5. Cross-Paper Compatibility

| Document | Physical 5D coord | Dimensionless | Status |
|----------|-------------------|---------------|--------|
| Paper 2 (published) | ξ | — | CANON |
| Framework v2.0 | ξ | — | CANON |
| Part II (Book) | ξ | ξ̃ | ALIGNED (this policy) |

---

## 6. Code and Filenames

- **Python variables:** May use `xi` or `z` internally for backward compatibility.
- **CSV headers:** May retain `z` if tied to existing data pipelines.
- **LaTeX labels:** Preserve existing `\label{eq:..._z_...}` to avoid ref breakage.

The policy applies to **narrative and mathematical content**, not to legacy code identifiers.

---

## 7. Amendment Process

Any change to this policy requires:
1. Documentation in CHANGELOG.md
2. Update to this file with date stamp
3. Grep verification across all EDC documents

---

**END OF CANON NOTATION POLICY**
