# STATUS.md — EDC_Project Workspace State

**Last updated:** 2026-01-29

---

## Current State by Domain

### Book 1 (EDC Theory Book v17.49)

| Aspect | Status |
|--------|--------|
| Version | v17.49 (stable) |
| Build | Complete |
| Active development | NO |

**Notes:** Published reference. Contains core theory, confinement proof, Y-junction model.

---

### Book 2 (Active Development)

| Aspect | Status |
|--------|--------|
| Branch | `book-routeC-narrative-cleanup-v1` |
| Ready to merge | NO (documentation incomplete) |
| Active derivations | Topological Pinning Model, Neutron Lifetime |

**Current Results:**

| Result | Value | Observed | Error | Status |
|--------|-------|----------|-------|--------|
| tau_n (free) | ~10^3 s | 879 s | O(1) | [Dc/Cal]* |
| tau_n (bound) | >10^13 s | stable | — | [Dc] |
| B.E.(He-4) | 29 MeV | 28.3 MeV | +3% | [I] |
| B.E.(C-12) | 92.0 MeV | 92.2 MeV | -0.2% | [I] |
| B.E.(O-16) | 127.3 MeV | 127.6 MeV | -0.2% | [I] |
| Be-8 instability | Unstable | Unstable | check | [Dc] |

*Note: tau_n prefactor A ~ 0.84 is [Cal], not derived.

**Known Issues:**
1. ~~L_0/delta tension~~ **RESOLVED** [Dc] — Both values valid in context (see `docs/L0_DELTA_TENSION_RESOLUTION.md`)
2. Prefactor A not derived from fluctuation determinant
3. G_F derivation uses measured v (circular)

---

### Papers

| Paper | Status | Key Content |
|-------|--------|-------------|
| Paper 2 | Complete | Frozen boundary criterion, C = 4pi/3 |
| Paper 3 | Complete | Neutron lifetime WKB, weak sector, sin^2(theta_W) = 1/4 |
| Companion F | Published | Proton Y-junction backbone |
| Companion G | Published | n-p mass difference |
| Companion H | Published | Weak interactions |
| Companion N | PLANNED | Neutron backbone (plan in CANON_BUNDLE Section 14) |

---

### Infrastructure

| Item | Status |
|------|--------|
| Workspace CANON_BUNDLE | Created 2026-01-28 |
| WORKSPACE_MAP | Created 2026-01-28 |
| CONCEPT_INDEX | Created 2026-01-28 |
| Root CLAUDE.md | TODO |
| Book 2 Canon Bundle | Operational |
| Book 2 pre-commit hooks | Implemented |

---

## Verified Findings (Do NOT Re-derive)

| Finding | Status | Source |
|---------|--------|--------|
| m_p/m_e = 6pi^5 | [Der] | Turning points |
| alpha^-1 = 6pi^5/(4pi+5/6) | [Der] | Turning points |
| Delta_m_np = 8m_e/pi | [Der] | Turning points |
| sigma = m_e^3 c^4/(alpha^3 hbar^2) | [Dc] | Turning points |
| Frozen criterion (Route A + B) | [Dc] | Paper 2 |
| Step function C = 4pi/3 | [Der] | Paper 2 |
| sin^2(theta_W) = 1/4 | [Der] | Paper 3 |
| Y-junction 120deg Steiner | [Der] | Book 1, Companion F |

---

## Quick Reference

**Proton:** Y-junction, 3 arms at 120deg, S^3 x S^3 x S^3, W = +1, STABLE

**Neutron:** Asymmetric Y-junction, theta = 60deg, q = 1/3, W = 0, METASTABLE

**Brane:** "Glass window" — LEFT (5D bulk) -> RIGHT (3D observable)

**Causality:** 5D is CAUSE, 3D is EFFECT. One-way.

---

*Last updated: 2026-01-28*
