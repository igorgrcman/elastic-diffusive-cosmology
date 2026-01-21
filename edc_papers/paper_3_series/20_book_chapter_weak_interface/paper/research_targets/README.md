# Research Targets for Chapter 3: The Research Frontier

This directory contains well-posed research problems for EDC Part II, Chapter 3.

## Index of Research Targets

| ID | Title | Priority | Status | Dependencies |
|----|-------|----------|--------|--------------|
| **RT-CH3-001** | V-A Structure from Plenum Inflow | HIGH | OPEN | Ch1 pipeline, Ch2 Z₆ |
| RT-CH3-002 | G_F from 5D Mediator Integration | HIGH | OPEN | RT-001 (mode profiles) |
| RT-CH3-003 | Neutron Lifetime from Peierls Barrier | HIGH | OPEN | Ch2 dislocation model |
| RT-CH3-004 | Lepton Mass Hierarchy from Mode Spectrum | MEDIUM | OPEN | RT-001 |
| RT-CH3-005 | Neutrino Mass from Edge-Mode Dynamics | MEDIUM | OPEN | Ch1 edge-mode ontology |
| RT-CH3-006 | Koide Phase from Z₃ Geometry | LOW | OPEN | Ch2 Z₃ structure |

## Principles for Research Targets

### What Makes a Good Target

1. **Well-posed**: Clear mathematical problem with defined inputs and outputs
2. **EDC-native**: Uses EDC-specific structure, not SM assumptions in disguise
3. **Falsifiable**: Clear criteria for success AND failure
4. **Auditable**: Can verify no circular reasoning or smuggled assumptions

### The "No Smuggling" Rule

Every research target must explicitly distinguish:

- **INPUT**: EDC postulates (5D geometry, Plenum inflow, thick brane, Z₆ lattice)
- **OUTPUT**: Physical predictions (V-A, G_F, lifetimes, mass ratios)

If an "output" is used as an "input" (even implicitly), the derivation is invalid.

### Example: V-A Structure

**WRONG approach:**
```
Input: "Boundary condition P_L ψ = 0"
Output: "V-A structure"
Problem: Chirality selection is ASSUMED, not derived
```

**RIGHT approach:**
```
Input: Plenum inflow direction + 5D Dirac structure + thick brane
Output: One chirality survives at observer boundary → V-A emerges
Verification: No step assumes "weak force couples to left-handed fermions"
```

## Status Definitions

| Status | Meaning |
|--------|---------|
| OPEN | Not yet attempted |
| IN PROGRESS | Active work |
| PARTIAL | Some results, gaps remain |
| SOLVED | Complete derivation with audit |
| FAILED | Attempted, proven impossible |

## File Naming Convention

```
RT-CH3-XXX_SHORT_DESCRIPTION.tex
```

Where XXX is a three-digit number and SHORT_DESCRIPTION uses underscores.

---

*Last updated: January 21, 2026*
