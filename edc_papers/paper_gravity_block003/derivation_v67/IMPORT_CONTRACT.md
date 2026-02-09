# σ̃ Import Contract — BLOCK-004 v67

## Version: 1.0
## Date: 2026-02-09
## Status: READ-ONLY IMPORT

---

## 1. Import Source

| Field | Value |
|-------|-------|
| Source lane | `cosmology_sigma_tilde_lane/` |
| Import method | P76 copy-in (Option 1) |
| Target location | `quarantine/sigma_tilde_value.json` |
| Provenance | `quarantine/PROVENANCE_LINK.md` |

---

## 2. Interface APIs

### A-APIσ1 (Provider)

**Role:** Cosmology lane provides σ̃

**Contract:**
- Generates `sigma_tilde_value.json` conforming to schema
- Sets firewall compliance fields
- Populates provenance with hash chain

### A-APIσ2 (Consumer)

**Role:** BLOCK-004 consumes σ̃

**Contract:**
- Reads `quarantine/sigma_tilde_value.json` as **read-only**
- Validates against schema before use
- Uses `sigma_tilde.value` in closure formulas (when DERIVED)
- Does NOT modify the file

### A-APIσ3 (Propagation)

**Role:** Closure chain propagation

**Contract:**
- σ̃ → α₃ = 1/σ̃
- σ̃ → M_X = C_X μ* σ̃^{1/2}
- σ̃ → g_X = √(4π/σ̃)
- σ̃ → τ_p = f(σ̃⁴)

---

## 3. No-Backflow Statement

**CRITICAL:** Information flows ONE WAY only.

```
Cosmology Lane → quarantine/sigma_tilde_value.json → BLOCK-004 v67
              A-APIσ1                              A-APIσ2
```

**BLOCK-004 MUST NOT:**
- Write to sigma_tilde_value.json
- Modify σ̃ based on τ_p predictions
- Import values back to cosmology lane
- Override firewall settings

Any violation breaks the derivation chain integrity.

---

## 4. Closure Mode

| Condition | Mode |
|-----------|------|
| `status == "TBD"` | CONDITIONAL CLOSURE (template) |
| `status == "DERIVED"` | NUMERICAL CLOSURE |
| `status == "IMPORTED"` | NUMERICAL CLOSURE (external) |

**Current status:** CONDITIONAL CLOSURE (awaiting derivation)

---

## 5. Quarantine Policy

The `quarantine/` folder contains:
- `sigma_tilde_value.json` — The imported export artifact
- `PROVENANCE_LINK.md` — Hash verification and source tracking

**Policy:**
- Contents are treated as external input
- Validation required before use
- No numerics propagate to Layer A until DERIVED status

---

## 6. Activation Semantics

**See:** `ACTIVATION_GATE.md` for full specification.

| Status | Layer A | Layer B |
|--------|---------|---------|
| TBD | Unchanged | BLOCKED (SKIP_NUMERIC_CLOSURE_TBD) |
| DERIVED | Unchanged | ACTIVE |
| IMPORTED | Unchanged | ACTIVE |

**Key principle:** Layer A structural derivations are always valid. Layer B numeric computations activate only when σ̃ value is available.

---

## 7. References

| Document | Location |
|----------|----------|
| Activation gate | `ACTIVATION_GATE.md` |
| Export contract | `cosmology_sigma_tilde_lane/SIGMA_TILDE_EXPORT_CONTRACT.md` |
| Schema | `cosmology_sigma_tilde_lane/sigma_tilde_schema.json` |
| T_* definition | `cosmology_sigma_tilde_lane/TSTAR_DEFINITION.md` |
| T_* derivation | `cosmology_sigma_tilde_lane/TSTAR_DERIVATION_5D.md` |

---

**No numerics here.** Template mode remains active until cosmology lane provides DERIVED status.
