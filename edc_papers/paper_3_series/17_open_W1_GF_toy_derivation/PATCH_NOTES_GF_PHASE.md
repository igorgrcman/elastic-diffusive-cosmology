# Patch Notes: OPEN-W1 — Toy Derivation of G_F Scaling

## Version 0.1 (2026-01-20)

### New Content

1. **Scope and Guardrails (§1)**
   - Clear anti-scope: NOT a fit, NOT a numerical claim
   - Structural derivation goal only

2. **Toy Geometry Setup (§2)**
   - Thick brane with observer-facing layer at y ~ 0
   - Bulk-extending region δ ~ L_frozen
   - Mediator φ(x,y) bulk-propagating scalar

3. **Toy Lagrangian (§3)**
   - L_phi: free 5D scalar [P]/[Def]
   - L_int: localized vertex at y = -δ/2 [P]
   - Bilinear current J(x) abstracted

4. **Integration Out (§4)**
   - Tree-level integration of φ
   - L_eff = -(g_5^2/2m_phi^2) O_overlap J(x)J(x) [Dc]
   - Four-Fermi structure emerges

5. **Suppression Factors (§5)**
   - Overlap integral O_overlap = ∫dξ ∫dy f_a f_b f_phi [OPEN]
   - BC operator O_BC ~ O(P_frozen, P_chir) [OPEN]
   - g_eff = g_5 × O_overlap × O_BC [Def]

6. **Dimensional Analysis (§6)**
   - Check: [G_EDC] = [E]^-2 ✓
   - Table: all ingredients with dimensions and sources

7. **Closure Checklist (§7)**
   - Gap table with 5 closure targets
   - Candidate sources identified

8. **Benchmarks (§8)**
   - PDG G_F as [BL] only — NOT fitted
   - Agreement criterion deferred

### Epistemic Status

| Element | Status | Notes |
|---------|--------|-------|
| L_phi structure | [P]/[Def] | Simplest 5D scalar |
| L_int localization | [P] | Vertex at brane edge |
| L_eff derivation | [Dc] | Standard tree-level |
| O_overlap definition | [Def] | Not computed |
| O_overlap value | [OPEN] | Needs profiles |
| g_5 origin | [OPEN] | Needs 5D action |
| m_phi origin | [OPEN] | Needs KK spectrum |
| G_F = 1.166e-5 GeV^-2 | [BL] | PDG reference |

### What Remains OPEN

1. **Fermion profiles:** f_a(ξ,y), f_b(ξ,y) for electron, neutrino
2. **Mediator profile:** f_phi(ξ,y) in frozen regime
3. **BC operator:** Full O(P_frozen, P_chir) construction
4. **Mass spectrum:** m_phi from Framework KK analysis
5. **Coupling constant:** g_5 from 5D action principle
6. **V-A structure:** Import from Companion V chirality filter

### Dependencies

- Companion V (this series) — chirality filter P_chir

### Build Verification

```
xelatex main.tex ×2
Result: 7 pages, no undefined refs
```
