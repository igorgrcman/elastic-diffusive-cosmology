# Provenance Seal — sigma_tilde_value.json

## Version: 3.0 (Epistemic Correction)
## Date: 2026-03-15
## Status: CALIBRATED (retracted from DERIVED)

---

## 1. Cryptographic Seal

| Attribute | Value |
|-----------|-------|
| File | `sigma_tilde_value.json` |
| Algorithm | SHA-256 |
| Hash | `f736c07dd82bb10cdfa5bb99c5ec16700774e4198605a4686a558b1b90f96030` |
| Previous hash (v2.0) | `1724182407e50f0e69e1027a9c47867c731aefcb5072ff80eae4fe37a03004f6` |

---

## 2. Content Summary

| Field | Value | Changed? |
|-------|-------|----------|
| `sigma_tilde.status` | CALIBRATED | **Yes** (was DERIVED) |
| `sigma_tilde.value.central` | 100.0 | No |
| `sigma_tilde.value.plus` | 10.0 | No |
| `sigma_tilde.value.minus` | 10.0 | No |
| `uncertainty.units` | dimensionless | No |
| `t_star.status` | STRUCTURAL_ONLY | **Yes** (was DERIVED) |
| `provenance.method` | alpha3_calibration | **Yes** (was 5D_brane_world_derivation) |
| `provenance.epistemic_tags` | calibrated, from_alpha3_requirement, warped_geometry_negative_c4cb6f8 | **Yes** |
| `provenance.notes` | CALIBRATED... PHYSICAL_DERIVATION retracted | **Yes** |

---

## 3. Correction Record

### What changed (v2.0 → v3.0)

The PHYSICAL_DERIVATION claim has been **retracted**. The warped geometry
derivation program (commit `c4cb6f8`, branch `archive/nuclear-topology-discovery`)
proved that:

1. The geometric coefficient C in T_* = C·M₅³ is **not a pure number** — it
   depends on the bulk cosmological constant Λ₅ (a free parameter)
2. With C = O(1), σ̃ ~ 10⁻¹⁸, not 100 (hierarchy between nuclear and Planck scales)
3. σ̃ = 100 is **not derivable** from standard 5D warped geometry

The value σ̃ = 100 most likely originates from the requirement α₃ = 1/σ̃ ≈ 0.01
(strong coupling at KK/GUT scale), making it a **calibration** [Cal], not a
derivation [D].

### Governing documents

- `edc_book_4/derivations/WARPED_GEOMETRY_C_DERIVATION.md` (commit `c4cb6f8`)
- `edc_book_4/audit/COSMOLOGY_LANE_REPORT.md` (commit `cf93bcf`)
- `edc_book_4/audit/SIGMA_TILDE_EPISTEMIC_CORRECTION.md` (this correction)

---

## 4. PHYSICAL_DERIVATION Assertion — RETRACTED

**Previous claim (v2.0):** "The sigma_tilde value is derived from first-principles
5D brane-world physics, not from fitting to external data."

**Retraction (v3.0):** This claim is not supported by the documented derivation
chain. The TSTAR_DERIVATION_5D.md provides only a structural form (T_* = C·M₅³)
with C tagged [P] (pending). The intermediate quantities T_* and σ_dimensional
are null. The warped geometry derivation program confirmed C cannot be determined
as a pure number. The PHYSICAL_DERIVATION assertion is withdrawn.

**New status:** CALIBRATED — σ̃ = 100 is a calibrated value consistent with
α₃ = 1/σ̃ at the KK/GUT scale. The structural framework (T_* ∝ M₅³) is intact
but does not produce a numeric value.

---

## 5. Layer A Firewall Compliance

| Check | Status | Notes |
|-------|--------|-------|
| No external data references | PASS | Unchanged |
| No detector references | PASS | Unchanged |
| No simulation data | PASS | Unchanged |
| No measurement anchors | PASS | Unchanged |
| No external anchors | **QUALIFIED** | α₃ = 1/σ̃ is a calibration target |
| Layer A unchanged | PASS | Algebraic structure intact |

**Note:** The firewall check "No external anchors" is now QUALIFIED rather than
PASS, because σ̃ = 100 originates from a calibration requirement (α₃ ≈ 0.01),
not from a closed derivation. The algebraic chain σ̃ → α₃ → M_X → τ_p remains
structurally sound.

---

## 6. Consumer Instructions

Consumers (e.g., BLOCK-004 v67) MUST:

1. Copy this file to `quarantine/sigma_tilde_value.json`
2. Verify SHA-256 hash matches: `f736c07dd82bb10cdfa5bb99c5ec16700774e4198605a4686a558b1b90f96030`
3. Treat as READ-ONLY
4. Never write back to cosmology lane
5. **Note CALIBRATED status** — σ̃ = 100 is [Cal], not [D]
6. Propagated results (α₃, M_X, g_X, τ_p) inherit [Cal] tag from σ̃

---

## 7. No-Backflow Statement

```
cosmology_sigma_tilde_lane/ → consumer/quarantine/
                            ONE-WAY ONLY
```

Information flows from cosmology lane TO consumers.
Consumers MUST NOT modify or write back.

---

**Sealed by epistemic audit 2026-03-15. CALIBRATED status. PHYSICAL_DERIVATION retracted.**
