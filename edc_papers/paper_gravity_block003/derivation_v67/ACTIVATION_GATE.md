# Activation Gate — BLOCK-004 v67

## Version: 1.1
## Date: 2026-02-09
## Status: ACTIVE (DERIVED)

---

## 1. Purpose

The Activation Gate controls when Layer B numerical computations may proceed based on the status of `sigma_tilde_value.json`.

**Key Principle:** Layer A remains unchanged regardless of status. Layer B may compute only when status is DERIVED.

---

## 2. State Machine

```
                    ┌─────────────┐
                    │    TBD      │
                    │  (initial)  │
                    └──────┬──────┘
                           │
                           │ cosmology lane derives σ̃
                           │ (external update)
                           ▼
                    ┌─────────────┐
                    │   DERIVED   │
                    │  (active)   │
                    └─────────────┘
```

### States

| State | Description | Layer A | Layer B |
|-------|-------------|---------|---------|
| `TBD` | Awaiting derivation | Unchanged | BLOCKED |
| `DERIVED` | Value available | Unchanged | ACTIVE |
| `IMPORTED` | External source | Unchanged | ACTIVE |

---

## 3. Activation Semantics

### 3.1 When status == "TBD"

- All structural checks PASS
- Emit explicit note: `SKIP_NUMERIC_CLOSURE_TBD`
- Layer B computations are SKIPPED (not failed)
- No numeric values propagate
- Mode: CONDITIONAL CLOSURE

### 3.2 When status == "DERIVED"

- All structural checks PASS
- Validate value structure:
  - `value.central` exists and is float > 0
  - `value.plus` exists and is float >= 0
  - `value.minus` exists and is float >= 0
  - `uncertainty.units` == "dimensionless"
- Validate provenance:
  - `provenance.derivation_ref` exists
  - `provenance.git_commit` exists
  - `provenance.sot_hash` exists and != "TBD"
- Layer B computations PROCEED
- Mode: NUMERICAL CLOSURE

### 3.3 When status == "IMPORTED"

- Same validation as DERIVED
- Additional: `provenance.import_source` must exist
- Layer B computations PROCEED
- Mode: NUMERICAL CLOSURE (external)

---

## 4. Layer Separation

**CRITICAL:** The Activation Gate enforces strict layer separation.

| Layer | Contents | Affected by Gate |
|-------|----------|------------------|
| Layer A | Structural derivations, formulas, theorems | NO |
| Layer B | Numeric evaluations, predictions, tables | YES |

**Layer A remains unchanged regardless of sigma_tilde status.**

This means:
- All BOX formulas remain valid
- All scaling relations remain valid
- All sensitivity analyses remain valid
- Only numeric plug-in values change

---

## 5. No-Backflow Statement

**CRITICAL:** The Activation Gate is READ-ONLY.

```
sigma_tilde_value.json → Activation Gate → Layer B Computations
                              │
                              └── READ-ONLY (no writes)
```

**The gate MUST NOT:**
- Modify `sigma_tilde_value.json`
- Change status field
- Update provenance
- Write any data back to quarantine

**The gate MAY ONLY:**
- Read `sigma_tilde_value.json`
- Parse and validate structure
- Report status via PASS/SKIP/FAIL
- Enable/disable Layer B computations

---

## 6. Validation Checks (P77a)

The following checks are implemented in `recompute.py`:

| Check | Description | TBD | DERIVED |
|-------|-------------|-----|---------|
| P77a-001 | ACTIVATION_GATE.md exists | PASS | PASS |
| P77a-002 | Status field valid | PASS | PASS |
| P77a-003 | TBD mode skip note | PASS | N/A |
| P77a-004 | value.central validation | N/A | PASS |
| P77a-005 | value.plus validation | N/A | PASS |
| P77a-006 | value.minus validation | N/A | PASS |
| P77a-007 | uncertainty.units check | PASS | PASS |
| P77a-008 | provenance.derivation_ref | N/A | PASS |
| P77a-009 | provenance.git_commit | N/A | PASS |
| P77a-010 | provenance.sot_hash valid | N/A | PASS |

---

## 7. References

| Document | Purpose |
|----------|---------|
| `IMPORT_CONTRACT.md` | Interface contract |
| `quarantine/sigma_tilde_value.json` | Data source |
| `quarantine/PROVENANCE_LINK.md` | Hash chain |

---

**Layer A unchanged; Layer B may compute only when DERIVED.**
