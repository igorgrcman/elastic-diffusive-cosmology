# CH08 OPEN Questions Ledger

**Date:** 2026-01-25
**Branch:** book2-ch08-openq-remediation-v1
**File:** `sections/11_gf_derivation.tex`
**Chapter Title:** The Fermi Constant from Geometry

---

## Summary

| Risk | Count | Description |
|------|-------|-------------|
| RED | 3 | First-principles derivation blocked by OPR-19,20,21,22 |
| YELLOW | 2 | Mode overlap mechanism qualitative only |
| GREEN | 3 | Properly documented OPEN items |

---

## OPEN Items Catalog

### CH08-OPEN-001: G₅ Not Derived (RED)

| Field | Value |
|-------|-------|
| **File** | 11_gf_derivation.tex |
| **Lines** | 438-461 |
| **Text** | "the 5D coupling $G_5$ is **not defined** from first principles" |
| **Risk** | RED |
| **Linked Claim** | E-CH08-P-004 |
| **Blocking OPR** | OPR-19 |
| **Remediation** | DOCUMENT-OPEN (already properly tagged) |

### CH08-OPEN-002: Mediator Mass Not Derived (RED)

| Field | Value |
|-------|-------|
| **File** | 11_gf_derivation.tex |
| **Lines** | 495-499 |
| **Text** | "Mediator mass $m_\phi$ from KK reduction" |
| **Risk** | RED |
| **Linked Claim** | E-CH08-P-005 |
| **Blocking OPR** | OPR-20 |
| **Remediation** | DOCUMENT-OPEN (already properly tagged) |

### CH08-OPEN-003: Mode Profiles from BVP (RED)

| Field | Value |
|-------|-------|
| **File** | 11_gf_derivation.tex |
| **Lines** | 501-506, 515-519 |
| **Text** | "Mode profiles $f_L(\xi)$ from thick-brane BVP... OPR-21" |
| **Risk** | RED |
| **Linked Claim** | E-CH08-P-006 |
| **Blocking OPR** | OPR-21 |
| **Remediation** | DOCUMENT-OPEN (already properly tagged) |

### CH08-OPEN-004: First-Principles G_F (RED)

| Field | Value |
|-------|-------|
| **File** | 11_gf_derivation.tex |
| **Lines** | 577-578, 608, 633 |
| **Text** | "First-principles $G_F$: **OPEN** (OPR-22)" |
| **Risk** | RED |
| **Linked Claim** | E-CH08-OPEN-001 |
| **Blocking OPR** | OPR-22 |
| **Remediation** | DOCUMENT-OPEN (already properly tagged) |

### CH08-OPEN-005: Mode Overlap Qualitative Only (YELLOW)

| Field | Value |
|-------|-------|
| **File** | 11_gf_derivation.tex |
| **Lines** | 470-482 |
| **Text** | "Mode overlap mechanism provides **qualitative understanding**... The mode overlap is [P]" |
| **Risk** | YELLOW |
| **Linked Claim** | E-CH08-P-003 |
| **Blocking OPR** | OPR-21 (for quantitative upgrade) |
| **Remediation** | DOCUMENT-OPEN (already properly tagged as YELLOW-B) |

### CH08-OPEN-006: I₄ Estimate Illustrative Only (YELLOW)

| Field | Value |
|-------|-------|
| **File** | 11_gf_derivation.tex |
| **Lines** | 449-461 |
| **Text** | "Naive estimate (illustrative only)... agreement is **not meaningful** because $g_5$ and $M_{5,\text{Pl}}$ are not derived" |
| **Risk** | YELLOW |
| **Linked Claim** | E-CH08-I-002 |
| **Blocking OPR** | OPR-19 |
| **Remediation** | DOCUMENT-OPEN (already properly documented) |

### CH08-OPEN-007: Figure Placeholders (GREEN)

| Field | Value |
|-------|-------|
| **File** | 11_gf_derivation.tex |
| **Lines** | 238-259, 374-397 |
| **Text** | "[FIGURE PLACEHOLDER]" |
| **Risk** | GREEN |
| **Linked Claim** | N/A (editorial) |
| **Blocking OPR** | NONE (local) |
| **Remediation** | FIX-NOTATION (add actual figures when ready) |

### CH08-OPEN-008: Open Items Listed in Reader Map (GREEN)

| Field | Value |
|-------|-------|
| **File** | 11_gf_derivation.tex |
| **Lines** | 155-159 |
| **Text** | "Open (not addressed): First-principles $G_F$... mediator mass... BVP solution" |
| **Risk** | GREEN |
| **Linked Claim** | N/A (navigation) |
| **Blocking OPR** | NONE (local) |
| **Remediation** | DOCUMENT-OPEN (already properly documented) |

---

## OPR Cross-Reference Issues

### CRITICAL: OPR Registry Missing OPR-16 through OPR-22

| OPR | Usage in CH08 | Registry Status |
|-----|---------------|-----------------|
| OPR-19 | g₅ value (lines 463, 568, 605) | **MISSING** |
| OPR-20 | Mediator mass (lines 568, 606) | **MISSING** |
| OPR-21 | BVP mode profiles (lines 519, 568, 577, 607) | **MISSING** |
| OPR-22 | First-principles G_F (lines 568, 578, 608, 633) | **MISSING** |

**Action Required:** Add OPR-16 through OPR-22 to `canon/opr/OPR_REGISTRY.md`

---

## Symbol Collision Check

| Symbol | CH08 Usage | Potential Collision |
|--------|------------|---------------------|
| δ | Brane thickness (line 52) | CP phase δ in CKM (different chapter) |
| Δ | Not used | N/A |
| ξ | 5th dimension (consistent) | No collision |
| λ | Decay scale (line 432) | Wolfenstein λ (different chapter) |
| θ | θ_W Weinberg angle (consistent) | No collision |

**Verdict:** No in-chapter symbol collisions. Cross-chapter δ/λ usage is contextually separated.

---

## Claims Extraction (Top-10)

| Claim-ID | Label/Location | Statement | Tag | OPR |
|----------|----------------|-----------|-----|-----|
| E-CH08-Der-001 | thm:ch11_GF | G_F from EW relations | [Der] | — |
| E-CH08-Dc-001 | eq:ch11_GF_derived | G_F = 1.166×10⁻⁵ GeV⁻² | [Dc] | — |
| E-CH08-Dc-002 | eq:ch11_Leff | L_eff = -g₅²/(2m_φ²) × O_overlap × JJ | [Dc] | OPR-19,20 |
| E-CH08-Dc-003 | eq:ch11_I4_exact | I₄ = m₀ (for exponential profile) | [Dc] | — |
| E-CH08-P-001 | eq:ch11_L_phi | Mediator Lagrangian | [P] | OPR-20 |
| E-CH08-P-002 | eq:ch11_geff | g_eff = g₅ × O_overlap × O_BC | [P] | OPR-19 |
| E-CH08-P-003 | sec:ch11_overlap | Mode overlap mechanism | [P] | OPR-21 |
| E-CH08-P-004 | rem:ch11_firewall | G_F is consistency, not prediction | [P] | — |
| E-CH08-I-001 | eq:ch11_GEDC | G_EDC ~ g_eff²/m_φ² | [I] | — |
| E-CH08-BL-001 | eq:ch11_GF_value | G_F = 1.1663787×10⁻⁵ GeV⁻² | [BL] | — |

---

## Blocking Set Summary

| OPR | OPEN Items Blocked | Claim Count |
|-----|-------------------|-------------|
| OPR-19 | CH08-OPEN-001, CH08-OPEN-006 | 2 |
| OPR-20 | CH08-OPEN-002 | 1 |
| OPR-21 | CH08-OPEN-003, CH08-OPEN-005 | 2 |
| OPR-22 | CH08-OPEN-004 | 1 |

**Total RED blockers:** 4 (all require OPR closure for GREEN upgrade)

---

## Verdict

CH08 is **epistemically well-documented**. All OPEN items are explicitly tagged with correct risk levels and OPR cross-references. The only hygiene issue is that OPR-19 through OPR-22 are not in the registry — this must be fixed.
