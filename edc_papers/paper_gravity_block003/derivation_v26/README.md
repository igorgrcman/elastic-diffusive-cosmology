# Derivation v26 — Gap Derivability Program

**Purpose:** Establish what EDC must provide to derive the KK mass gap from first principles, rather than identifying it with M_Z.

## Central Question

Under what conditions can m_gap be tagged **[D]** (fully derived) rather than **[I]+[BL]** (identified with measured M_Z)?

## Gap Derivability Criteria

| Criterion | Requirement | Tag |
|-----------|-------------|-----|
| GDC-1 | m_gap from EDC-internal only (no external mass) | [D] |
| GDC-2 | m_gap from M_Pl alone (no EW input) | [Dc] |
| GDC-3 | m_gap identified with M_Z, M_W, or v_EW | [I]+[BL] |

## Mechanism Introduced

**Brane-localized mass term** modifies boundary conditions:
- Bulk action + brane mass at ξ=L
- Variational principle → Robin BC: ψ'(L) = m_b·ψ(L)
- Transcendental spectrum: tan(m_n L) = -m_b/m_n

## Key Results

| Property | Status |
|----------|--------|
| Spectral mechanism | [D] (derived) |
| Transcendental equation | [D] (derived) |
| Gap bounds: π/2L < m_gap < π/L | [D] (derived) |
| Compactification scale L | [OPEN] |
| Brane mass m_b | [OPEN] |
| **Overall gap status** | [I]+[BL] (unchanged) |

## Numerical Demonstration

The script `recompute.py` verifies:
- Root-finding for transcendental equation
- First 3 modes for mb·L ∈ {0, 0.1, 1, 10, 100}
- Gap pinning: m_gap·L transitions from π to π/2

```bash
python3 recompute.py
```

Output: ALL 11 CHECKS PASSED

## Path to GDC-2

To upgrade from [I]+[BL] to [Dc]:
- EDC must derive L or m_b·L using only M_Pl

## Path to GDC-1

To achieve full [D]:
- Both L and m_b must be EDC-derivable with no external scales

## Files

| File | Description |
|------|-------------|
| `main.tex` | Source document (82 equation environments) |
| `main.pdf` | Compiled output (16 pages) |
| `EDC_BLOCK003_DERIVATION_V26_GAP_DERIVABILITY_PROGRAM.pdf` | Export copy |
| `recompute.py` | Python verification script |
| `REPORT.md` | Build verification report |
| `ACCEPTANCE.md` | Acceptance criteria |

## What This Note Does NOT Claim

- We do **not** claim to have derived the gap
- We do **not** close BLOCK-003 in any new way
- We **do** map precisely what is needed for closure

This is a **program note**, not a result note.
