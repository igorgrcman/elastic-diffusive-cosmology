# σ̃ Export Contract

## Version: 1.0
## Date: 2026-02-08

---

## 1. File Format

The export file `sigma_tilde_value.json` must:

- Conform to `sigma_tilde_schema.json` (JSON Schema Draft 2020-12)
- Be valid JSON with UTF-8 encoding
- Contain no trailing whitespace or BOM

---

## 2. Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `schema_version` | string | Version of this schema |
| `created_utc` | string | ISO8601 timestamp |
| `sigma_tilde` | object | Dimensionless brane tension |
| `t_star` | object | Characteristic scale |
| `sigma_dimensional` | object | Dimensional brane tension |
| `provenance` | object | Derivation audit trail |
| `firewall` | object | Layer A compliance |

---

## 3. Field Semantics

### sigma_tilde
- `value`: The dimensionless ratio σ/T_* (null if TBD)
- `uncertainty`: Interval [lo, hi] in dimensionless units
- `status`: One of "TBD", "DERIVED", "IMPORTED"

### t_star
- `definition_ref`: Path to TSTAR_DEFINITION.md
- `value`: Characteristic energy scale (null if TBD)
- `units`: Physical dimension string
- `status`: Derivation status

### sigma_dimensional
- `value`: Dimensional brane tension (null if TBD)
- `units`: Physical units (e.g., "MeV/fm^2")
- `status`: Derivation status

### provenance
- `method`: Description of derivation method
- `epistemic_tags`: Array of epistemic markers
- `parent_hashes`: Object mapping version IDs to hashes
- `sot_hash`: Source of Truth hash for this export
- `repo_commit`: Git commit at generation time
- `notes`: Free-form notes

### firewall
- `layer`: Must be "A" (Layer A only)
- `forbidden_gate_pass`: Must be false

---

## 4. Interface APIs

### A-APIσ1 (Provider)

**Role:** Cosmology lane provides σ̃

**Contract:**
- Generates `sigma_tilde_value.json` conforming to schema
- Sets `firewall.layer = "A"`
- Sets `firewall.forbidden_gate_pass = false`
- Populates provenance with valid hashes

### A-APIσ2 (Consumer)

**Role:** BLOCK-004 consumes σ̃

**Contract:**
- Reads `sigma_tilde_value.json` as read-only
- Validates against schema before use
- Uses `sigma_tilde.value` in closure formulas
- Does NOT modify the file

### A-APIσ3 (Propagation)

**Role:** Closure chain propagation

**Contract:**
- σ̃ → α₃ = 1/σ̃
- σ̃ → M_X = C_X μ* σ̃^{1/2}
- σ̃ → g_X = √(4π/σ̃)
- σ̃ → τ_p = f(σ̃⁴)

---

## 5. No-Backflow Statement

**CRITICAL:** Information flows ONE WAY only.

```
Cosmology → sigma_tilde_value.json → BLOCK-004
         A-APIσ1              A-APIσ2
```

BLOCK-004 MUST NOT:
- Write to sigma_tilde_value.json
- Modify σ̃ based on τ_p predictions
- Import values back to cosmology lane
- Override firewall settings

Any violation breaks the derivation chain integrity.

---

## 6. Validation

Before consumption, BLOCK-004 must verify:

1. File exists at expected path
2. JSON parses without error
3. All required fields present
4. `firewall.layer == "A"`
5. `firewall.forbidden_gate_pass == false`
6. `provenance.sot_hash` matches expected

---

## 7. Status Values

| Status | Meaning |
|--------|---------|
| `TBD` | Value not yet derived |
| `DERIVED` | Value derived from first principles |
| `IMPORTED` | Value imported from external source |

---

**Contract Hash:** TBD (to be set on first production export)
