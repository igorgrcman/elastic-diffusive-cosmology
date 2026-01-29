# STATUS.md — Current State of EDC Book 2

**Last updated:** 2026-01-28

---

## Current Truth

### Core Parameters (Established)

| Parameter | Value | Status | Source |
|-----------|-------|--------|--------|
| σ (brane tension) | 8.82 MeV/fm² | [Dc] | Conditional on E_σ = m_e c²/α |
| δ (brane thickness) | 0.105 fm | [Dc] | ℏ/(2m_p c) |
| L₀ (junction extent) | 0.980 fm | [P] | r_p + δ |
| K (pinning constant) | 0.94 MeV | [Dc/I] | f × σ × A_contact |

### Derived Results

| Result | Value | Observed | Error | Status |
|--------|-------|----------|-------|--------|
| τ_n (free neutron) | ~10³ s | 879 s | O(1) | [Dc/Cal]* |
| τ_n (bound neutron) | >10¹³ s | stable | — | [Dc] |
| B.E.(He-4) | 29 MeV | 28.3 MeV | +3% | [I] |
| B.E.(C-12) | 92.0 MeV | 92.2 MeV | -0.2% | [I] |
| B.E.(O-16) | 127.3 MeV | 127.6 MeV | -0.2% | [I] |
| Be-8 instability | Unstable | Unstable | ✓ | [Dc] |

*Note: τ_n prefactor A ≈ 0.84 is [Cal], not derived.

### Weak Sector (from Paper 3)

| Result | Status | Note |
|--------|--------|------|
| V-A structure | [Dc] | From 5D chirality projection |
| Parity violation | [Dc] | 5D geometry enforces |
| sin²θ_W = 1/4 | [Der] | Geometric (exact at tree level) |
| G_F | [Dc/Cal] | Partial — uses measured v (circular) |

### Topological Pinning Model

| Feature | Status | Note |
|---------|--------|------|
| Allowed coordinations | [I] | n = 2^a × 3^b (geometric constraint) |
| Forbidden n = 43 | [P] | Optimal for nuclear matter but topologically forbidden |
| Frustration-Corrected G-N Law | [I/Cal] | R² = 0.9941, 44.7% improvement |

---

## Known Issues

1. ~~**L₀/δ tension**~~ **RESOLVED [Dc]** — Both valid: π² for static, 9.33 for dynamic. See `docs/L0_DELTA_TENSION_RESOLUTION.md`
2. **Prefactor A**: Calibrated, not derived from fluctuation determinant
3. **G_F derivation**: Uses measured v — need pure 5D derivation
4. **Geometric factor f**: Identified as √(δ/L₀) but not derived from first principles

---

## Key Documents

| Document | Location | Status |
|----------|----------|--------|
| Topological Pinning Model | `src/derivations/BOOK_SECTION_TOPOLOGICAL_PINNING_MODEL.tex` | Active |
| Neutron Lifetime | `src/derivations/BOOK_SECTION_NEUTRON_LIFETIME.tex` | Active |
| Frustration G-N code | `src/derivations/frustration_geiger_nuttall.py` | Complete |

---

## Branch Status

- Current branch: `book-routeC-narrative-cleanup-v1`
- Main branch: `main`
- Ready to merge: NO (documentation incomplete)
