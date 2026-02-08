# DATA GAPS (V7.2)

**Created**: 2026-01-31
**Purpose**: Document missing BL data and prioritize future acquisition
**Status**: 32 nuclides complete; gaps identified for expansion

---

## Gap Categories

### Priority 1: More H1/H2 Nuclides (Critical)

**Problem**: Only 3 H1 nuclides in α32; zero H2 nuclides.

**Impact**: Cannot reliably estimate hindrance effect on G-N residuals.

**Needed**:
| Class | Current Count | Target | Gap |
|-------|---------------|--------|-----|
| H0 | 29 | 20-25 | OK |
| H1 | 3 | 8-10 | **+5-7** |
| H2 | 0 | 3-5 | **+3-5** |

**Candidate H1/H2 nuclides**:
| Nuclide | Jπ(P) | Jπ(D) | ΔJ | ΔΠ | Class | Status |
|---------|-------|-------|----|----|-------|--------|
| ²¹³Bi | 9/2⁻ | 1/2⁻? | 4 | N | H2 | [BL:NEEDED] |
| ²¹⁷Bi | 9/2⁻ | ? | ? | ? | ? | [BL:NEEDED] |
| ²¹⁵At | 9/2⁻ | 9/2⁺ | 0 | Y | H1 | [BL:NEEDED] |
| ²¹⁹At | 9/2⁻ | ? | ? | ? | ? | [BL:NEEDED] |

---

### Priority 2: High-Qα Nuclides (High)

**Problem**: Only 3 nuclides with Qα > 7 MeV; need better coverage.

**Impact**: Limited ability to test G-N law at high-Q end.

**Current distribution**:
| Qα Range | Count | Target |
|----------|-------|--------|
| < 5 MeV | 9 | 8-10 |
| 5-6 MeV | 13 | 10-12 |
| 6-7 MeV | 7 | 8-10 |
| 7-8 MeV | 2 | **5-7** |
| > 8 MeV | 1 | **3-5** |

**Candidate high-Qα nuclides**:
| Nuclide | Qα (MeV) | Status |
|---------|----------|--------|
| ²¹¹Po | 7.59 | [BL:AVAILABLE] |
| ²¹³Po | 8.54 | [BL:AVAILABLE] |
| ²¹⁸Rn | 7.26 | [BL:AVAILABLE] |
| ²¹⁶At | 7.95 | [BL:AVAILABLE] |
| ²¹⁸At | 6.87 | [BL:AVAILABLE] |

---

### Priority 3: Superheavy Element Data (Medium)

**Problem**: No BL data for A > 252 in current dataset.

**Impact**: Cannot test n = 48 target predictions.

**Available SHE data (limited quality)**:
| Nuclide | Z | A | t₁/₂ | Qα | Quality |
|---------|---|---|------|-----|---------|
| ²⁸⁸Fl | 114 | 288 | ~0.5 s | ~10 MeV | Uncertain |
| ²⁸⁹Fl | 114 | 289 | ~2.6 s | ~10 MeV | Uncertain |
| ²⁹³Og | 118 | 293 | ~0.7 ms | ~11.7 MeV | Very uncertain |
| ²⁹⁴Og | 118 | 294 | ~0.7 ms | ~11.7 MeV | Very uncertain |

**Status**: [BL:UNCERTAIN] — SHE data is preliminary and may not meet V7.2 quality standards.

---

### Priority 4: Daughter Jπ Verification (Low)

**Problem**: Some daughter Jπ values assumed from even-even standard.

**Impact**: Minor; affects hindrance classification accuracy.

**Nuclides to verify**:
| Parent | Daughter | Assumed Jπ | Status |
|--------|----------|------------|--------|
| ²³⁰Th | ²²⁶Ra | 0⁺ | [BL:S1] ✓ |
| ²⁴²Pu | ²³⁸U | 0⁺ | [BL:S1] ✓ |
| ²⁴⁸Cm | ²⁴⁴Pu | 0⁺ | [BL:S1] ✓ |
| ²⁵²Cf | ²⁴⁸Cm | 0⁺ | [BL:S2] ✓ |

**Result**: All verified; no gaps in daughter Jπ.

---

### Priority 5: Quantitative Hindrance Factors (Future)

**Problem**: Using categorical H0/H1/H2 instead of continuous hindrance factors.

**Impact**: Loss of precision in hindrance correction.

**Needed**: Spectroscopic hindrance factors (HF) from α-spectroscopy literature.

**Data source**:
- Rasmussen (1959) systematic
- Modern compilations (e.g., ENSDF α-decay evaluations)

**Status**: [BL:SOURCE_TBD] — Would require literature review beyond NuDat.

---

## Gap Summary Table

| Gap | Priority | Impact on V7.2 | Resolution |
|-----|----------|----------------|------------|
| More H1/H2 nuclides | Critical | Hindrance model underpowered | Expand dataset |
| High-Qα nuclides | High | G-N coverage incomplete | Add 5-8 nuclides |
| SHE data | Medium | Cannot test n=48 | Await better BL |
| Daughter Jπ | Low | None (all verified) | N/A |
| Hindrance factors | Future | Categorical → continuous | Literature review |

---

## Recommended Actions

### Immediate (V7.3 scope)

1. **Add 5 H1 candidates**: Focus on odd-odd or odd-A nuclides with parity change
2. **Add 5 high-Qα nuclides**: Po-211, Po-213, At-216, Rn-218, etc.
3. **Total target**: α40-45 dataset

### Medium-term

1. **Compile hindrance factors**: Build HF table from literature for all α32+
2. **Replace H0/H1/H2 with continuous HF**: Re-run regression with log(HF)

### Long-term

1. **Monitor SHE synthesis**: Update dataset as IUPAC-approved SHE data becomes available
2. **Test n=48 prediction**: When A > 300 data is reliable

---

## Blocked Analyses

The following analyses cannot proceed without gap resolution:

| Analysis | Blocking Gap | Severity |
|----------|--------------|----------|
| Hindrance class regression | Only 3 H1, 0 H2 | High |
| n=48 target test | No A > 252 | Medium |
| Continuous HF model | No HF compilation | Low |

