# E4 Patch Report — Minimal Text Clarifications

**Date**: 2026-01-25
**Branch**: book2-opr-registry-v1
**Phase**: E4 (Evidence Remediation)

---

## Summary

| Metric | Value |
|--------|-------|
| Files modified | 1 |
| Lines changed | 3 (1 formula fix, 2 comment lines) |
| Physics content changed | NO |
| Page count impact | Expected: 0 |

---

## Patches Applied

### Patch 1: sin²θ_W Formula Correction (OPR-08)

**File**: `src/sections/11_gf_derivation.tex`
**Lines**: 321-325

**Issue**: Mathematical error in displayed formula. Text claimed:
```
|Z₂|/|Z₆| = 2/6 = 1/4
```
But 2/6 = 1/3, not 1/4.

**Root cause**: The formula conflated two different expressions:
- g'²/g² = |Z₂|/|Z₆| = 2/6 = **1/3** (coupling ratio)
- sin²θ_W = g'²/(g²+g'²) = (1/3)/(4/3) = **1/4** (final result)

**Old text**:
```latex
\sin^2\theta_W(\mu_{\text{lattice}}) = \frac{|\mathbb{Z}_2|}{|\mathbb{Z}_6|}
    = \frac{2}{6} = \frac{1}{4}
```

**New text**:
```latex
\sin^2\theta_W(\mu_{\text{lattice}}) = \frac{|\mathbb{Z}_2|}{|\mathbb{Z}_2| + |\mathbb{Z}_6|}
    = \frac{2}{2+6} = \frac{1}{4}
% Note: This follows from g'^2/g^2 = |Z_2|/|Z_6| = 1/3 and sin^2 theta_W = g'^2/(g^2+g'^2).
% See Theorem \ref{thm:weinberg_angle} in Chapter \ref{ch:z6_program} for full derivation.
```

**Tag used**: N/A (formula correction, not new content)

**Why non-physics drift**:
- No physics claim changed
- Same numerical result (1/4)
- Formula now matches canonical source (Z6_content_full.tex Theorem 4)
- Added cross-reference to derivation source

---

## Patches NOT Needed (Already Addressed)

### OPR-04: δ teleport definition

**Status**: ALREADY ADDRESSED in CH10

**Evidence**: Lines 27, 42, 81, 110-114 of ch10_electroweak_bridge.tex explicitly:
- Define δ as brane thickness: "finite thickness δ ~ r_e ~ 1 fm"
- Tag as [P]: "postulate" and "[P]/[OPEN]"
- Explain relation to R_ξ with caveats
- Include in epistemic status box

### OPR-05: m_φ teleport definition

**Status**: ALREADY ADDRESSED in CH10

**Evidence**: Lines 65, 105-107, 117-120 of ch10_electroweak_bridge.tex explicitly:
- Define m_φ as mediator mass: "mediator mass m_φ = x_1/ℓ"
- Explain origin from BVP eigenvalue
- Tag as [Dc]+[P]

### OPR-06: α (Robin parameter) definition

**Status**: ALREADY ADDRESSED in CH10

**Evidence**: Lines 34, 95-96, 99-102 of ch10_electroweak_bridge.tex explicitly:
- Define Robin BC: "f' + αf = 0"
- State α "encodes junction microphysics—it is not a free parameter to tune"
- Tag as [Dc]
- Provide dimensional analysis: "α ~ ℓ/δ"

### G_F Circularity Warning

**Status**: ALREADY ADDRESSED in CH11

**Evidence**: Lines 310-339 of 11_gf_derivation.tex (Remark rem:ch11_firewall):
- Explicit "The circularity caveat" section
- States v depends on G_F
- Clarifies this is "consistency identity"
- Tags v as [BL] input
- States "The independent EDC content is sin²θ_W = 1/4"

---

## OPR Status Updates

| OPR | Old Status | New Status | Reason |
|-----|------------|------------|--------|
| OPR-04 | OPEN | PARTIAL | Definition exists; derivation from action still OPEN |
| OPR-05 | OPEN | PARTIAL | Definition exists; source determination still OPEN |
| OPR-06 | OPEN | PARTIAL | Definition exists; value derivation still OPEN |
| OPR-08 | OPEN | CLOSED | Formula corrected; notation now unambiguous |

---

## Validation

**Gates**:
- [ ] gate_notation.sh → PENDING
- [ ] gate_canon.sh → PENDING
- [ ] gate_build.sh → PENDING (requires local build)

**Page count**: Expected 387 (no content addition, only formula correction)

---

*Generated: 2026-01-25*
*Evidence Audit Phase E4*
