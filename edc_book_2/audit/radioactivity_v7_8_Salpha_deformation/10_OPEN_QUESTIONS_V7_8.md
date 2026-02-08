# V7.8 OPEN QUESTIONS — TOP 10 KINGPINS

**Created**: 2026-01-31
**Purpose**: Updated blockers with V7.8 resolution status

---

## Status Summary

| V7.7 Kingpin | V7.8 Status | Resolution |
|--------------|-------------|------------|
| Independent S_α | Partially addressed | Royer proxy tested, marginal |
| Deformation proxy | **RESOLVED** | Shell distance proxy tested; absorbed by d(n) |
| Pairing residuals | Open | Not tested |
| Shell proximity | Partially in proxy | proxy_deform includes shell distance |
| Isomer comparison | Open | Not tested |
| T-dependence | Open | Not testable |
| α-Anisotropy | Open | Experimental |
| Charge radii | Open | Experimental |
| Superheavy | Open | Data limited |
| Mechanism discrimination | Partially addressed | Deformation ruled out as sole driver |

---

## Updated Kingpin List

### Kingpin 1: True β₂ Deformation (Reduced Priority)

**V7.7 Status**: Blocker
**V7.8 Status**: **Partially Resolved**

**What we did**: Tested shell-distance proxy: |N-126|×|Z-82|/1000
**Finding**: proxy_deform becomes non-significant when d(n) included (p = 0.67)
**Implication**: d(n) captures deformation-related variance and more

**Remaining uncertainty**: True β₂ from FRDM might behave differently
**Priority**: **MEDIUM** (proxy test passed; true β₂ would strengthen)

---

### Kingpin 2: Independent S_α Measurements (Still High Priority)

**V7.7 Status**: Blocker
**V7.8 Status**: **Partially Addressed**

**What we did**: Tested Royer S_α proxy
**Finding**: proxy_Salpha marginally significant (p = 0.05) with d(n); doesn't mediate d(n) effect
**Implication**: Royer formula captures some independent variance but isn't the mechanism

**Remaining uncertainty**: Experimental S_α from reactions might correlate with d(n)
**Priority**: **HIGH** (would definitively test prefactor hypothesis)

---

### Kingpin 3: Pairing Residuals

**V7.7 Status**: Open
**V7.8 Status**: **Open**

**What's needed**: Fine-grained pairing energy residuals (beyond even-odd classification)
**Why it matters**: Pairing affects S_α and could correlate with d(n)

**Priority**: MEDIUM

---

### Kingpin 4: Shell Closure Proximity

**V7.7 Status**: Open
**V7.8 Status**: **Partially in Proxy**

**What we did**: proxy_deform = |N-126|×|Z-82| explicitly includes shell distances
**Finding**: Absorbed by d(n)
**Implication**: Shell distance alone doesn't explain d(n)

**Priority**: LOW (addressed by proxy)

---

### Kingpin 5: Isomer Comparison

**V7.7 Status**: Open
**V7.8 Status**: **Open**

**What's needed**: Compare d(n) correlation in ground state vs isomers
**Why it matters**: Would test if effect is configuration-dependent

**Priority**: MEDIUM

---

### Kingpin 6: Temperature Dependence

**V7.7 Status**: Open
**V7.8 Status**: **Open (Not Addressable)**

**Why it remains**: Nuclear decay rates are T-independent (quantum tunneling)
**Implication**: Cannot use T-dependence to distinguish mechanisms

**Priority**: LOW (not testable)

---

### Kingpin 7: α-Anisotropy Measurements

**V7.7 Status**: Open
**V7.8 Status**: **Open**

**What's needed**: Angular distribution of α-particles for high-d(n) vs low-d(n) nuclei
**Why it matters**: Would test M1 domain mixing mechanism

**Priority**: MEDIUM (experimental requirement)

---

### Kingpin 8: Charge Radius Anomalies

**V7.7 Status**: Open
**V7.8 Status**: **Open**

**What's needed**: Precision charge radii for transuranics
**Why it matters**: Would test M6 core-mantle mechanism

**Priority**: LOW (specialized data)

---

### Kingpin 9: Superheavy Extension

**V7.7 Status**: Open
**V7.8 Status**: **Open**

**What's needed**: α-decay data for Z > 100 (Md, No, Lr, etc.)
**Why it matters**: Higher d(n) values, approach n = 48

**Priority**: MEDIUM (data availability limited)

---

### Kingpin 10: Causal Mechanism

**V7.7 Status**: [P]
**V7.8 Status**: **Strengthened [P]**

**What V7.8 showed**: d(n) is not just deformation proxy
**What remains**: Establishing causation (how does coordination affect decay?)

**Priority**: HIGH (theoretical development needed)

---

## New Kingpins from V7.8

### Kingpin 11: Alternative S_α Measures

**Rationale**: Royer proxy is marginal (p = 0.05); different S_α estimates might behave differently
**Candidates**:
- Buck cluster model S_α
- Spectroscopic factors from reactions
- Shell model calculations

**Priority**: HIGH

### Kingpin 12: Collinearity Diagnostics

**Rationale**: d(n) and proxy_deform are highly correlated (r = 0.97); SE inflation in M5/M7
**What's needed**: VIF analysis, ridge regression, PCA approach
**Why it matters**: Confirms that d(n) significance isn't artifact

**Priority**: MEDIUM

---

## Priority Matrix

| Priority | Kingpins |
|----------|----------|
| HIGH | K2 (S_α experimental), K10 (causation), K11 (alt S_α) |
| MEDIUM | K3 (pairing), K5 (isomers), K7 (anisotropy), K9 (SHE), K12 (collinearity) |
| LOW | K1 (true β₂, partial), K4 (shell, addressed), K6 (T-dep), K8 (radii) |

---

## What V7.8 Resolved

| Question | Resolution |
|----------|------------|
| Is d(n) just deformation? | **No** — proxy absorbed by d(n) |
| Is d(n) mediated by Royer S_α? | **No** — g unchanged when proxy added |
| Is d(n) robust? | **Yes** — g = -1.71, p < 0.001 in full model |
| Is the sign consistent? | **Yes** — all models have g < 0 |

---

## Path to [Der] Upgrade

To upgrade the topological frustration mechanism from [P] to [Der]:

1. ✓ Robust regression (V7.5, V7.8)
2. ✓ Permutation test (V7.5)
3. ✓ Cross-validation (V7.5)
4. ✓ Deformation control (V7.8)
5. ⬜ Independent S_α confirmation (K2/K11)
6. ⬜ Causal mechanism demonstration (K10)
7. ⬜ Superheavy validation (K9)

Current status: 4/7 complete → **Strong [P], approaching [I]**

