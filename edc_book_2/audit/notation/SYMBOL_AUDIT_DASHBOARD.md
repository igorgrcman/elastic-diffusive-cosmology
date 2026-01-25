# Symbol Audit Dashboard

Authority: Published artifacts (Framework v2.0, Paper 2, Companions A–H)
Generated: 2026-01-24
Status: PHASE C COMPLETE — Ready for remediation

---

## Executive Summary

| Metric | Count |
|--------|-------|
| **Total violations detected** | **61** |
| Registered in ledger (VR-###) | 26 |
| MUST-FIX | 25 |
| TODO-REVIEW | 1 |
| Files affected | 8 |

**Gate Status**: ❌ **FAIL** — 61 violations block notation gate

---

## Violation Breakdown by Type

| Category | Symbol Pattern | Count | Priority |
|----------|---------------|-------|----------|
| A: M_5 → \mathcal{M}^5 | Manifold topology | 10 | HIGH |
| B: M_5 → M_{5,Pl} | Mass scale | 9 | HIGH |
| C: z/Δz → ξ/Δξ | 5D depth coordinate | 41 | HIGH |
| D: Documentation | Comment update | 1 | LOW |

---

## Violation Breakdown by File

| File | M_5 (manifold) | M_5 (mass) | z/Δz | Total | VR IDs |
|------|----------------|------------|------|-------|--------|
| 05_three_generations.tex | 10 | 0 | 0 | 10 | VR-001 to VR-007 |
| 06_neutrinos_edge_modes.tex | 0 | 0 | 15 | 15 | VR-013 to VR-019 |
| 07_ckm_cp.tex | 0 | 0 | 10 | 10 | VR-020 to VR-023 |
| 09_va_structure.tex | 0 | 0 | 15 | 15 | VR-024 |
| 11_gf_derivation.tex | 0 | 2 | 0 | 2 | VR-008 |
| ch11_opr20_attemptD*.tex | 0 | 3 | 0 | 3 | VR-009 to VR-010 |
| ch11_opr20_attemptF*.tex | 0 | 0 | 2 | 2 | VR-025 |
| ch14_bvp_closure_pack.tex | 0 | 4 | 2 | 6 | VR-011 to VR-012 |
| 02_frozen_regime_foundations.tex | 0 | 0 | 0 | 1 | VR-026 (doc) |

---

## Top 10 Highest-Risk Collisions

| Rank | Collision | Risk | Files | Action |
|------|-----------|------|-------|--------|
| 1 | z as 5D depth in (x^μ, z) | HIGH | 09_va_structure, ch11_attemptF | z → ξ |
| 2 | Δz as 5D separation | HIGH | 06_neutrinos, 07_ckm | Δz → Δξ |
| 3 | M_5 in π₁(M_5) topology | HIGH | 05_three_generations | M_5 → \mathcal{M}^5 |
| 4 | M_5 in g²/M_5² mass | HIGH | 11_gf_derivation | M_5 → M_{5,Pl} |
| 5 | M_5 as "5D Planck mass" | HIGH | ch11_attemptD, ch14 | M_5 → M_{5,Pl} |
| 6 | f(z) profile functions | MED | 06_neutrinos, 07_ckm | f(z) → f(ξ) |
| 7 | z_H horizon coordinate | MED | 06_neutrinos | z_H → ξ_H |
| 8 | Δz_{12}, Δz_{23} | MED | 07_ckm | Δz → Δξ |
| 9 | V(ξ) = V_warp(z) mixed | HIGH | ch14 | Unify to ξ |
| 10 | ξ as coherence length | LOW | Paper 2 legacy | Use ξ_GL |

---

## Remediation Plan

### Phase D1: Unambiguous M_5 → \mathcal{M}^5 (Manifold)

**Files**: `05_three_generations.tex`

All 10 occurrences are in topology context (π₁(M_5)). Context is unambiguous.

**Fix pattern**:
```latex
% OLD
\pi_1(M_5)
% NEW
\pi_1(\mathcal{M}^5)
```

### Phase D2: Unambiguous M_5 → M_{5,Pl} (Mass)

**Files**: `11_gf_derivation.tex`, `ch11_opr20_attemptD*.tex`, `ch14_bvp_closure_pack.tex`

All 9 occurrences are in mass formula context. Context is unambiguous.

**Fix pattern**:
```latex
% OLD
G_5 \sim g_5^2/M_5^2
% NEW
G_5 \sim g_5^2/M_{5,\mathrm{Pl}}^2
```

### Phase D3: z → ξ for 5D Coordinate

**Files**: `06_neutrinos_edge_modes.tex`, `07_ckm_cp.tex`, `09_va_structure.tex`, `ch11_opr20_attemptF*.tex`

~41 occurrences. Context requires case-by-case verification but pattern is clear.

**Fix patterns**:
```latex
% OLD
\Delta z, z_H, f(z), \Psi(x^\mu, z)
% NEW
\Delta\xi, \xi_H, f(\xi), \Psi(x^\mu, \xi)
```

---

## Verification Checklist

After each remediation commit:

- [ ] Run `python3 tools/symbol_audit.py` — confirm violation count decreased
- [ ] Run `./tools/gate_notation.sh` — confirm forbidden patterns eliminated
- [ ] Run full build `latexmk -xelatex src/main.tex` — confirm 0 errors
- [ ] Verify page count = 387 (unchanged)
- [ ] Update REPLACEMENT_RISK_LEDGER.md (move entries to Completed)
- [ ] Update this dashboard with new counts

---

## Timeline

| Phase | Scope | Status |
|-------|-------|--------|
| Phase A | Canon memory documents | ✅ COMPLETE |
| Phase B | Master symbol table | ✅ COMPLETE |
| Phase C | Context-aware audit | ✅ COMPLETE |
| Phase D | Remediation | 🔲 PENDING |

---

## Files Created/Updated This Session

| File | Purpose | Status |
|------|---------|--------|
| canon/SYMBOL_MASTER_TABLE.md | Authoritative symbol dictionary | ✅ NEW |
| canon/SYMBOL_DECISION_PROTOCOL.md | Classification protocol | ✅ NEW |
| canon/SYMBOL_COLLISION_MAP.md | Collision registry | ✅ NEW |
| audit/notation/REPLACEMENT_RISK_LEDGER.md | VR entries added | ✅ UPDATED |
| audit/notation/SYMBOL_AUDIT_DASHBOARD.md | This file | ✅ NEW |

---

## Canon Memory Persistence

The following documents ensure future CC sessions cannot "forget" notation rules:

1. **SYMBOL_MASTER_TABLE.md** — Complete symbol dictionary
2. **SYMBOL_DECISION_PROTOCOL.md** — Classification flowchart
3. **SYMBOL_COLLISION_MAP.md** — Known collisions + resolutions
4. **NOTATION_POLICY.md** — Binding rules

All files include "Authority: Published artifacts; canon immutable; Book 2 must conform."

---

## Version History

| Date | Change | By |
|------|--------|-----|
| 2026-01-24 | Initial creation — Phase C complete | Claude |
