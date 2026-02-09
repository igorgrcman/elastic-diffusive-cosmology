# Smoke-Test Policy — BLOCK-004 v67

## Version: 1.0
## Date: 2026-02-09
## Status: ACTIVE

---

## 1. Purpose

This document defines the criteria for distinguishing between **REAL** (physical) and **SMOKE-TEST** (integration-only) numeric outputs in BLOCK-004 v67.

---

## 2. REAL vs SMOKE Criteria

A `sigma_tilde_value.json` is considered **REAL** only if ALL of the following are true:

| Criterion | Requirement |
|-----------|-------------|
| status | `== "DERIVED"` |
| provenance.derivation_ref | NOT null/empty AND matches pattern `^EDC-COSMO-` |
| provenance.sot_hash | `!= "TBD"` |
| provenance.git_commit | 40-character hex string AND `!= "TBD"` |
| provenance.notes | Contains exact string `PHYSICAL_DERIVATION` (case-sensitive) |

If ANY criterion fails, the payload is classified as **SMOKE-TEST**.

---

## 3. Mode Effects

| Gate Status | Mode | Layer B Numerics | Citation Allowed |
|-------------|------|------------------|------------------|
| TBD | N/A | BLOCKED | NO |
| DERIVED | SMOKE | Allowed (integration test) | NO |
| DERIVED | REAL | Allowed (physical closure) | YES |
| IMPORTED | SMOKE | Allowed (integration test) | NO |
| IMPORTED | REAL | Allowed (physical closure) | YES |

---

## 4. Layer Separation

**Layer A:** Structural derivations, formulas, theorems.
- IMMUTABLE regardless of REAL/SMOKE mode.
- No numeric values from sigma_tilde appear here.
- Firewall patterns remain enforced.

**Layer B:** Numeric evaluations, predictions, tables.
- May contain numeric outputs only when Gate is OPEN (DERIVED/IMPORTED).
- Must display SMOKE-TEST warning banner unless REAL.
- Citation of numeric outputs prohibited unless REAL.

---

## 5. Reader Contract

**WARNING TO READERS:**

Numeric outputs in Layer B are **INTEGRATION SMOKE TESTS** unless the provenance satisfies ALL REAL criteria listed above.

**Do NOT cite numeric outputs** from this document unless:
1. `sigma_tilde_value.json` provenance shows `PHYSICAL_DERIVATION` in notes
2. `derivation_ref` begins with `EDC-COSMO-`
3. All other REAL criteria are satisfied

Smoke-test numerics are for pipeline validation only.

---

## 6. Verification

The `recompute.py` script automatically:
- Detects REAL vs SMOKE mode
- Prints WARNING banner if SMOKE
- Prefixes numeric outputs with `[SMOKE]` or `[REAL]`
- Fails if REAL criteria are claimed but not met

---

## 7. No-Backflow

This policy document does NOT modify:
- `quarantine/sigma_tilde_value.json` (read-only)
- Cosmology lane files
- Any upstream derivation

---

**Layer A immutable. Layer B numerics are integration tests unless REAL.**
