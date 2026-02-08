# Master Blockers Registry

**Generated:** 2026-01-31
**Sources:** 22826edd, 73d92ff5, 98cc5184, 5251e090, ce8dadbd sessions

---

## Summary Statistics

| Source File | Blocked Items | Key Blockers |
|-------------|---------------|--------------|
| 22826edd | 101 | OPR-21, OPR-04, BVP potential |
| 73d92ff5 | 3,034 | Theory maturity gaps |
| 98cc5184 | ~10 | V_B derivation, prefactor |
| 5251e090 | 6 | Power derivation (12,13), quantum corrections |
| ce8dadbd | 19 | G formula powers, geometric factor |

---

## Critical Blockers (RED - Block Quantitative Closure)

### BLOCK-001: BVP Potential V(xi) Derivation
- **what_blocked:** V(xi) potential shape for fermion localization
- **blocks_downstream:**
  - N_bound = 3 claim (generation counting)
  - I_4 overlap integral calculation
  - G_F quantitative closure
  - V-A suppression coefficient C
  - Lepton mass hierarchy quantitative
- **files_where_appears:** 22826edd, 73d92ff5, 98cc5184
- **related_GAP:** GAP-21 (OPR-21)
- **status:** OPEN - requires 5D action -> 1D effective potential derivation
- **closure_requirement:** Derive V(xi) from 5D Dirac + warped metric + junction conditions

### BLOCK-002: delta = R_xi Identification
- **what_blocked:** Thickness scale identification delta = R_xi = hbar*c/M_Z
- **blocks_downstream:**
  - OPR-02 Route C upgrade (Robin BC derivation)
  - kappa parameter determination
  - Unique-scale proof for membrane thickness
- **files_where_appears:** 22826edd:1968, 12143, 12255
- **related_GAP:** GAP-04 (OPR-04)
- **status:** OPEN [P] - cannot upgrade to [Dc] without theorem
- **closure_requirement:** Prove R_xi is the unique scale or provide alternative derivation

### BLOCK-003: G Formula Power Derivation
- **what_blocked:** Powers 12 (R_xi) and 13 (r_e) in G = c^4 R_xi^12 / (128*pi^2*sigma*r_e^13)
- **blocks_downstream:**
  - G upgrade from [I] to [D]
  - Hierarchy explanation mechanistic basis
  - 128*pi^2 geometric factor interpretation
- **files_where_appears:** ce8dadbd:26, 72, 111-129, 143
- **related_GAP:** None assigned yet
- **status:** [I] - identified by fitting, not derived
- **closure_requirement:** Rigorous 5D->4D reduction producing these specific powers

### BLOCK-004: V_B Barrier Height Derivation
- **what_blocked:** V_B ~ 2.6 MeV barrier height for neutron decay
- **blocks_downstream:**
  - tau_n upgrade from [Cal] to [Der]
  - Bounce action first-principles calculation
  - Prefactor A_0 complete derivation
- **files_where_appears:** 22826edd:14182, 26290, 27312; 98cc5184
- **related_GAP:** None assigned (V_B is [Cal])
- **status:** [Cal] - fitted to tau_n = 879s
- **closure_requirement:** Derive V_B from Z3 barrier structure + membrane parameters

### BLOCK-005: g_5 (5D Coupling) Derivation
- **what_blocked:** 5D gauge coupling g_5
- **blocks_downstream:**
  - G_F complete closure (g_5^2 appears in formula)
  - Quantitative I_4 -> G_F chain
- **files_where_appears:** 22826edd, 73d92ff5, 98cc5184
- **related_GAP:** GAP-19 (OPR-19)
- **status:** OPEN
- **closure_requirement:** Derive g_5 from 5D action or identify with known coupling

---

## Major Blockers (YELLOW - Block Partial Claims)

### BLOCK-006: Vortex Pressure Deficit Model
- **what_blocked:** p(r_core) = 0 pressure deficit at vortex core
- **blocks_downstream:**
  - v(r) = sqrt(2GM/r) upgrade from [D conditional] to [D]
  - G derivation mechanistic completion
- **files_where_appears:** 5251e090:42, 101
- **related_GAP:** Plan B completion
- **status:** [P] - postulated, not derived from 5D vortex solution
- **closure_requirement:** Derive pressure deficit from 5D vortex physics

### BLOCK-007: Robin BC Parameter kappa
- **what_blocked:** Robin boundary condition coefficient kappa = m_b/2
- **blocks_downstream:**
  - OPR-02 complete closure
  - BVP eigenvalue precision
- **files_where_appears:** 22826edd:14674, 16849
- **related_GAP:** OPR-02
- **status:** PARTIAL - three routes exist, none fully closed
- **closure_requirement:** Derive kappa from brane-action variation (Route A or B)

### BLOCK-008: PMNS Phase delta_CP
- **what_blocked:** CP-violating phase in PMNS matrix
- **blocks_downstream:**
  - Complete PMNS prediction
  - Leptogenesis connection
- **files_where_appears:** 73d92ff5, 98cc5184
- **related_GAP:** OPR-14
- **status:** [OPEN]
- **closure_requirement:** Derive or constrain delta_CP from Z6 geometry

### BLOCK-009: Domain Size ell
- **what_blocked:** Effective domain size ell ~ 1 fm
- **blocks_downstream:**
  - mu = M_0*ell window validation
  - n = ell/Delta determination
  - BVP spectral closure
- **files_where_appears:** 22826edd:15944, 16235
- **related_GAP:** Part of OPR-21
- **status:** [P/Cal] - not derived from first principles
- **closure_requirement:** Derive ell from 5D geometry or junction physics

### BLOCK-010: Effective Mass M(q)
- **what_blocked:** q-dependent effective mass M(q) in tunneling
- **blocks_downstream:**
  - Bounce action B calculation
  - Prefactor omega determination
- **files_where_appears:** 22826edd:27698, 28520; 98cc5184
- **related_GAP:** None - partially derived
- **status:** [Dc] - M(q) = M_NG(q) + M_core(q) form established
- **closure_requirement:** Full M(q) numerical evaluation with 5D-derived profiles

---

## Moderate Blockers (Pedagogical/Documentation)

### BLOCK-011: Figure Placeholders
- **what_blocked:** 16 figure placeholders in manuscript
- **blocks_downstream:**
  - 6 HIGH priority (conceptual understanding)
  - 10 MEDIUM priority (pedagogical aids)
- **files_where_appears:** 22826edd:11010, 11069
- **related_GAP:** None
- **status:** Documentation issue
- **closure_requirement:** Generate or create figures

### BLOCK-012: z vs xi Notation
- **what_blocked:** Notation collision between Part I (zeta/xi) and Part II (z)
- **blocks_downstream:**
  - Reader confusion
  - Cross-part consistency
- **files_where_appears:** 22826edd:6047, 6217, 6501, 6587
- **related_GAP:** None
- **status:** IN PROGRESS - refactoring underway
- **closure_requirement:** Standardize on xi for 5D depth coordinate

### BLOCK-013: OPR Numbering Gaps
- **what_blocked:** Missing OPR-02,04,05,06,07,08,17,18 in registry
- **blocks_downstream:**
  - Claim tracking completeness
  - Audit trail integrity
- **files_where_appears:** 22826edd:14267
- **related_GAP:** Registry maintenance
- **status:** Partial - some added, gaps remain
- **closure_requirement:** Complete OPR registry entries

---

## Session-Specific Blockers

### From 5251e090 (F_bulk/Gravity)

| blocker | description | status |
|---------|-------------|--------|
| BLOCK-5251-001 | Plan A incomplete (N-body not tested) | Yellow |
| BLOCK-5251-002 | Missing quantum corrections in G formula | Yellow |
| BLOCK-5251-003 | Missing factor involving R_xi/l_P ratio | Red |
| BLOCK-5251-004 | Power 12 for R_xi not derived | Red |
| BLOCK-5251-005 | Power 13 for r_e not derived | Red |
| BLOCK-5251-006 | 128*pi^2 factor not derived | Red |

### From ce8dadbd (Gravity Derivation)

| blocker | description | status |
|---------|-------------|--------|
| BLOCK-CE8D-001 | F_bulk units [m^3/s^4] vs [m/s^2] confusion | RESOLVED |
| BLOCK-CE8D-002 | kappa = 1.6 calibrated not derived | Yellow |
| BLOCK-CE8D-003 | No 5D mechanism produces power 12 | Red |
| BLOCK-CE8D-004 | Dimensional analysis not unique (n+m=-1) | Yellow |
| BLOCK-CE8D-005 | Formula identified not derived | Yellow |

### From 73d92ff5 (Theory Maturity)

| blocker | description | count |
|---------|-------------|-------|
| GAP-1 items | General gaps | 244 |
| GAP-4 items | Scale identification | 106 |
| GAP-5 items | SSB mechanism | 92 |
| GAP-6 items | Yukawa sector | 80 |
| GAP-7 items | Generation structure | 139 |
| tier1 blockers | Critical | 5 |
| tier2 blockers | Major | 62 |
| tier3 blockers | Minor | 1 |

---

## Blocker Dependency Graph

```
BLOCK-001 (V(xi))
    |
    +---> BLOCK-004 (V_B) ---> tau_n closure
    |
    +---> BLOCK-005 (g_5) ---> G_F closure
    |
    +---> N_bound = 3 claim
    |
    +---> I_4 calculation
    |
    +---> BLOCK-007 (kappa)

BLOCK-002 (delta = R_xi)
    |
    +---> BLOCK-007 (kappa Route C)
    |
    +---> OPR-02 closure

BLOCK-003 (G powers)
    |
    +---> BLOCK-006 (vortex) ---> v(r) derivation
    |
    +---> Hierarchy explanation

BLOCK-009 (ell)
    |
    +---> BLOCK-001 (V(xi))
    |
    +---> mu-window validation
```

---

## Resolution Priority

| Priority | Blocker | Impact | Estimated Effort |
|----------|---------|--------|------------------|
| P1 | BLOCK-001 | Unlocks 5+ claims | High (full BVP) |
| P1 | BLOCK-003 | G derivation complete | High (5D calculation) |
| P2 | BLOCK-002 | Scale identification | Medium |
| P2 | BLOCK-004 | tau_n upgrade | Medium |
| P2 | BLOCK-006 | Gravity mechanism | Medium |
| P3 | BLOCK-007 | Robin BC | Low-Medium |
| P3 | BLOCK-009 | Domain size | Low |

---

*Registry generated from JSONL mining reports*
*Total blockers tracked: ~3,200 across all sessions*
*Critical blockers (RED): 5*
*Major blockers (YELLOW): 5*
