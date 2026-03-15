# Derivation v22 — KK Conventions Unification

**Purpose:** Resolve the π-factor discrepancy between v15-v20 (R_ξ = ℏc/M_Z) and v21 (R_ξ = πℏc/M_Z) by deriving KK spectra for interval, circle, and orbifold geometries, and establishing a canonical convention for BLOCK-003.

## What This Note Does

1. Derives KK spectral quantization for three geometries:
   - **Case A (Interval):** ξ ∈ [0, L] with Neumann BCs → m_n = nπ/L
   - **Case B (Circle):** S¹ radius R → m_n = n/R
   - **Case C (Orbifold):** S¹/Z₂ radius R → m_n = n/R (equivalent to interval L = πR)

2. Shows the equivalence: L = πR makes all spectra identical

3. Provides a "Conventions Dictionary" mapping between:
   - Definition I: R_ξ = L (interval length) → R_ξ = πℏc/M_Z
   - Definition II: R_ξ = R (circle radius) → R_ξ = ℏc/M_Z

4. Demonstrates that M_5 is the same in both conventions when computed consistently

5. Establishes canonical convention for BLOCK-003 going forward

## What This Note Does NOT Do

- Does NOT modify v15-v21 (they remain as written)
- Does NOT derive M_Z from EDC axioms (still [I]+[BL])
- Does NOT claim any physical difference between conventions

## Key Result

The π difference is **purely definitional**: it depends on whether R_ξ denotes the interval length L or the circle radius R = L/π. Both conventions describe the same physics.

## Canonical Decision

**R_ξ ≡ L (interval length)** is adopted for BLOCK-003 going forward.

With this convention:
- m_gap = π/R_ξ
- R_ξ = πℏc/M_Z = 6.80 × 10⁻¹⁸ m
- M_5 = 4.3 × 10¹² GeV

Previous notes (v15-v20) remain valid under the interpretation R_ξ^(old) = R = L/π.

## Files

| File | Description |
|------|-------------|
| `main.tex` | Source document (63 equation environments) |
| `main.pdf` | Compiled output (10 pages) |
| `EDC_BLOCK003_DERIVATION_V22_KK_CONVENTIONS_UNIFICATION.pdf` | Export copy |
| `REPORT.md` | Build verification report |
| `ACCEPTANCE.md` | Acceptance criteria |
