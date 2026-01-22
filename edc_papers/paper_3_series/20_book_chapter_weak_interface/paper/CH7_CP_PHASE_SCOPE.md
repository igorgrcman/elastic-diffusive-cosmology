# CH7 CP Phase Scope Document

**Date:** 2026-01-22
**Purpose:** Document file locations and key labels for CKM/CP Attempt 3

## File Locations

| File | Purpose |
|------|---------|
| `sections/07_ckm_cp.tex` | Main Ch7 content |
| `code/ckm_attempt2_1.py` | Non-uniform spacing model |
| `code/ckm_attempt2_2.py` | Wolfenstein structure analysis |
| `CH7_CKM_ATTEMPT2_2_NOTES.md` | Attempt 2.2 documentation |

## Key Labels in 07_ckm_cp.tex

### Section Labels
- `\label{sec:ch7_ckm}` — Main chapter
- `\label{sec:ch7_baseline}` — CKM baseline facts
- `\label{sec:ch7_dft_baseline}` — Attempt 1: DFT baseline
- `\label{sec:ch7_comparison}` — PDG comparison
- `\label{sec:ch7_breaking}` — Breaking requirements
- `\label{sec:ch7_attempt2}` — Attempt 2: Overlap model
- `\label{sec:ch7_attempt2_1}` — Attempt 2.1: Non-uniform spacing
- `\label{sec:ch7_attempt2_2}` — Attempt 2.2: Prefactor analysis
- `\label{sec:ch7_cp}` — CP Violation section
- `\label{sec:ch7_summary}` — Summary and Stoplight

### Equation Labels
- `\label{eq:ch7_ckm_def}` — CKM matrix definition
- `\label{eq:ch7_ckm_pdg}` — PDG values
- `\label{eq:ch7_dft_def}` — DFT definition
- `\label{eq:ch7_wolfenstein}` — Wolfenstein parametrization
- `\label{eq:ch7_wolfenstein_full}` — Full Wolfenstein with (rho, eta)
- `\label{eq:ch7_jarlskog}` — Jarlskog invariant J
- `\label{eq:ch7_overlap_def}` — Overlap integral definition
- `\label{eq:ch7_overlap_exp}` — Exponential overlap form
- `\label{eq:ch7_vub_pred}` — V_ub prediction from Attempt 2.1
- `\label{eq:ch7_vub_ratio}` — V_ub overshoot ratio
- `\label{eq:ch7_overshoot_expected}` — Expected overshoot = 1/|rho-i*eta|

### Table Labels
- `\label{tab:ch7_ckm_comparison}` — DFT vs PDG comparison
- `\label{tab:ch7_overlap_scaling}` — Overlap model scaling
- `\label{tab:ch7_attempt2_2}` — Attempt 2.2 Wolfenstein comparison
- `\label{tab:ch7_verdict}` — Chapter stoplight table

### Postulate Labels
- `\label{post:ch7_z3_quarks}` — Z3 symmetric quark mixing
- `\label{post:ch7_overlap_ansatz}` — Localized profile ansatz
- `\label{post:ch7_nonuniform}` — Non-uniform generation spacing

## Current CP Status (RED/open)

From `tab:ch7_verdict`:
- **CP factor (rho, eta) derivation**: RED (open)
- **CP violation phase delta**: RED (open)
- **Jarlskog invariant**: RED (open)

From section `sec:ch7_cp`:
- Currently states "Not Addressed"
- Lists potential mechanisms (complex Z6 phases, asymmetric BCs, CP-violating Plenum terms)
- All marked "speculative and remain (open)"

## Quantitative Targets for Attempt 3

### Already Achieved (from Attempts 2.1, 2.2)
- Magnitude hierarchy: lambda, lambda^2, lambda^3 (GREEN)
- |V_ub| ~ A*lambda^3 structure (GREEN)
- Prefactor 2.5x overshoot = 1/|rho-i*eta| mapping (YELLOW)

### Missing (RED/open)
1. **|rho - i*eta| ~ 0.38** — derive from 5D mechanism
2. **delta ~ 1.2 rad (68 deg)** — CKM CP phase
3. **J ~ 3.0e-5** — Jarlskog invariant (rephasing-invariant)

### Success Criteria

**Track A (no free params):**
- Use only: Z6/Z3 structure, Delta z/(2kappa) from earlier, localization profiles, plenum inflow
- If physical CP phase emerges: YELLOW/GREEN
- If not possible: tight negative result (RED)

**Track B (one Cal param):**
- Calibrate on ONE of: delta, J, or |rho-i*eta|
- MUST produce independent prediction not used in calibration
- If no prediction: RED ("not predictive")

## Key Physics Constraints

### Rephasing Invariance
Any proposed CP phase must survive field redefinitions:
- V_ij -> e^{i*phi_i} V_ij e^{-i*phi_j'}
- Only rephasing-invariant quantities (like J) are physical
- If phase can be removed by redefinition -> not physical CP -> RED

### PDG Values (BL)
- lambda = 0.22500 +/- 0.00067
- A = 0.826 +/- 0.015
- rho_bar = 0.159 +/- 0.010
- eta_bar = 0.348 +/- 0.010
- delta = 1.144 +/- 0.027 rad (65.6 +/- 1.5 deg)
- J = (3.08 +/- 0.14) x 10^-5

## Option Menu for Attempt 3

1. **O1: Complex z-shift / oscillatory bulk phase**
   - Overlap with exp(i*k*z) oscillation
   - Check if k*Delta_z gives realistic delta

2. **O2: Two-path interference**
   - CKM = sum of two overlap channels
   - Relative phase from Z6 sector

3. **O3: Boundary condition phase**
   - Domain wall / MIT-bag matching
   - Check if produces rephasing-invariant J

4. **O4: Discrete symmetry breaking (Z6 = Z2 x Z3)**
   - Complex cube roots + Z2 signs
   - Test if CP arises without new params

5. **O5: Holonomy/Berry phase**
   - Z3 cycle in internal space
   - Generation index as path variable

6. **O6: Mediator-induced complex mixing**
   - Integrate out heavy layer with complex mixing
   - Check if phase survives rephasing
