# Part B — Introduction Draft (Sections 1.1–1.12)
**UEA MRes Clinical Science — Part B Main Research Project**  
*Draft based on locked evidence map and detailed outline*  
*Prepared: 2026-08-22*  
*Student: Md Moied Hosen*  
*Supervisor: Dr Pankaj Garg*

> **Drafting notes**: Category markers [A/B/C/D] retained for audit trail; remove in final version. All Part A references cited by Part A ref number; will be renumbered to Part B Vancouver sequence.

---

## 1. INTRODUCTION

### 1.1 Clinical Context: Aortic Stenosis and Pressure Overload

Aortic stenosis (AS) is the most common valvular heart disease requiring intervention in high-income countries, with prevalence increasing steeply after age 65.^[1] The disease imposes chronic pressure overload on the left ventricle (LV), triggering concentric hypertrophic remodelling to maintain systolic wall stress and preserve ejection fraction (EF).^[2] While this adaptive response initially sustains forward flow, it carries an energetic price: myocardial oxygen demand rises, diastolic filling deteriorates, and the coronary perfusion gradient becomes compromised.^[3] Patients may develop symptoms of heart failure, angina, or syncope even while EF remains "preserved" by conventional thresholds.^[4]

Current guideline severity grading relies on Doppler echocardiography (peak velocity, mean gradient, aortic valve area by continuity equation) and, when discordant, invasive catheterisation.^[1] These volumetric and gradient-based indices, however, do not capture the total mechanical energy expenditure of the LV. Two patients with identical gradients and EF may have markedly different energetic profiles depending on LV geometry, arterial load, and haemodynamic efficiency.^[5] This gap motivates approaches that quantify not only pump function but mechanical work and efficiency.

### 1.2 Myocardial Energetics Framework: Pressure–Volume Loops

The pressure–volume (PV) loop is the reference framework for beat-to-beat LV mechanics and energetics. From a single loop, one derives stroke work (SW) — the external mechanical work of ejection — and pressure–volume area (PVA), a correlate of total mechanical energy per beat; their ratio (SW/PVA) estimates myocardial mechanical efficiency.^[6] The potential energy (PE) component of PVA represents the non-ejection work of isovolumic contraction and relaxation.

Historically, routine PV-loop assessment has been limited by the need for invasive high-fidelity LV catheterisation.^[7] This restricts serial assessment and excludes many patients who would benefit from energetic phenotyping.

### 1.3 Non-Invasive CMR-Derived PV Loops: Principle and Validation

Cardiovascular magnetic resonance (CMR) enables non-invasive PV-loop reconstruction by integrating cine-derived LV volume curves with brachial blood pressure and aortic valve timing within a time-varying elastance model.^[8,9] The method yields patient-specific estimates of SW, PVA, PE, and SW/PVA without catheterisation.

Foundational validation studies demonstrated experimental and in vivo agreement of non-invasive PV loops with invasive reference measures in heart failure populations.^[8] Subsequent human validation against invasive LV pressures confirmed fidelity of the algorithm in heart failure with reduced and preserved ejection fraction.^[9] **However, direct validation in AS cohorts is lacking.**^[10] The fixed outflow obstruction, eccentric hypertrophy, and pressure-recovery phenomena in AS introduce specific assumptions about arterial elastance (Ea), the volume intercept (V₀), and end-systolic pressure estimation that have not been directly tested in this population.

### 1.4 4D-Flow CMR Haemodynamic Energetics

Four-dimensional flow CMR (4D-flow) acquires three-directional, time-resolved velocity data throughout a 3D volume, enabling retrospective placement of measurement planes and quantification of advanced haemodynamic parameters.^[11] In AS, 4D-flow provides peak velocity, pressure gradient, and valve area measurements independent of Doppler alignment assumptions.^[12,13]

Beyond conventional haemodynamics, 4D-flow quantifies blood-flow kinetic energy (KE), vorticity, and viscous energy loss (VEL). LV intracavitary KE — partitioned into systolic, diastolic, E-wave, and A-wave components — reflects the energy cost of filling and ejection.^[14] Aortic VEL and vorticity capture the energy dissipated by turbulent flow through the stenotic valve.^[15,16]

**A critical distinction must be maintained:** 4D-flow measures *blood-flow* energy (KE, vorticity, VEL), whereas PV loops quantify *myocardial* mechanical energy (SW, PVA, efficiency). These are related but not equivalent; flow energy should not be equated with myocardial work.^[10,14]

### 1.5 Knowledge Gap

Despite growing literature on non-invasive PV loops^[8,9] and 4D-flow energetics^[12–16] as separate fields, no study has combined both in the same AS cohort. The PREFER-CMR registry (Norfolk and Norwich University Hospital) acquired CMR cine, phase-contrast 4D-flow, and brachial blood pressure in a prospective AS cohort, providing a unique opportunity to evaluate myocardial and flow energetics concurrently.^[17–19]

Key unresolved questions include:
1. Whether non-invasive PV-loop indices (SW, PVA, SW/PVA) are feasible and physiologically plausible in moderate-to-severe AS
2. How 4D-flow haemodynamic energetics (KE, vorticity, VEL by cardiac phase) differ between AS and healthy controls
3. Whether flow energetic indices correlate with myocardial energetic indices in the same patients
4. The validation status of non-invasive PV loops in AS — a gap highlighted by the absence of AS-specific invasive comparator studies

### 1.6 Study Rationale

This project leverages the PREFER-CMR registry dataset to address these gaps through an exploratory analysis. The registry's standardised acquisition protocol (cine + 4D-flow + brachial BP) enables both non-invasive PV-loop reconstruction (planned) and 4D-flow energetic analysis (completed for a subset). The work is hypothesis-generating, not definitive, given the small analysed cohort.

### 1.7 Aim

To evaluate myocardial energetic burden (via non-invasive CMR-derived PV loops) and 4D-flow haemodynamic energetics (kinetic energy, vorticity, viscous energy loss) in patients with moderate-to-severe aortic stenosis compared to age-matched healthy controls.

### 1.8 Objectives

| # | Objective | Status |
|---|-----------|--------|
| 1 | Quantify LV volumes, mass, and function via MASS contouring in 5 AS cases and 5 age-matched controls | **Completed** [Category A] |
| 2 | Quantify 4D-flow haemodynamic energetics (KE, vorticity, energy loss by cardiac phase: FullRR, systolic, diastolic, E-wave, A-wave) in the same 5+5 cohort | **Completed** [Category A] |
| 3 | Reconstruct non-invasive PV loops and derive SW, PVA, PE, SW/PVA (efficiency), Ea, Emax | **Planned / Not yet completed** [Category D] |
| 4 | Compare AS vs controls for all completed energetic parameters (4D-flow) | **Partial — 4D-flow completed; PV-loops planned** |
| 5 | Explore associations between 4D-flow and PV-loop energetic indices | **Planned** (requires PV-loop completion) |

### 1.9 Hypotheses

| # | Hypothesis | Testable with Current Data |
|---|------------|---------------------------|
| H₁ | AS patients have higher LV blood-flow KE, vorticity, and energy loss than controls across all cardiac phases (FullRR, systolic, diastolic, E-wave, A-wave) | **Yes** — 4D-flow outputs present for 5 AS + 5 controls [Category A] |
| H₂ | AS patients have altered myocardial energetic indices (SW, PVA, SW/PVA) vs controls | **Planned** — requires PV-loop generation |
| H₃ | 4D-flow haemodynamic energetic parameters correlate with PV-loop myocardial energetic parameters | **Planned** — requires both completed |

### 1.10 Study Design Overview

Retrospective case-control analysis of existing PREFER-CMR registry data (NNUH, 1.5T scanner). Ethics approval: REC 17/EE/0346 per Research Proposal [Category A — planned]; **note discrepancy with published PREFER-CMR REC 21/NE/0149** [Category D — Supervisor confirmation required].

**Completed work:**
- CMR contouring and 4D-flow analysis were performed using MASS (December 2025 workflow/version information). Initial contours were generated by the software and subsequently checked and manually corrected. Contour quality was reviewed by Dr Rui, following which corrections were made and the contours were re-reviewed.
- The completed 4D-flow analysis produced kinetic energy (KE), reported in µJ/ml; vorticity, reported in s⁻¹; and energy loss, reported in µW. Outputs were available for FullRR, systolic, diastolic, E-wave, and A-wave. These are directly supported by the raw-data workbook.
- Aortic valve timing methodology: [VERIFY FROM MASS/RAW DATA/PUBLISHED PROTOCOL].
- 4D-flow acquisition VENC: [VERIFY].

**Planned work:**
- Non-invasive PV-loop reconstruction (software/algorithm: [Category D — Supervisor confirmation required])
- Final statistical analysis in SPSS (approach for n=5/group: [Category D — Supervisor/statistician confirmation required])

### 1.11 Cohort Definitions and Transparency

Transparency regarding cohort derivation is essential for this exploratory work:

| Cohort | Size | Derivation |
|--------|------|------------|
| **Planned (Proposal)** | 30 AS + 20 Controls | Research Proposal target [Category A — planned] |
| **PREFER-CMR Published** | 30 AS | Grafton-Clarke 2025 (Part A [9]) [Category B] |
| **AS Cohort Workbook** | 38 AS records | `AS cohort_Moied.xlsx` [Category A] |
| **Available (complete clinical data)** | 28 AS | Workbook records with Height, Weight, HR, SYS_BP, DIA_BP, CMR DATE [Category A] |
| **Analysed AS** | 5 | Randomly selected from available dataset [Category C] |
| **Control Dataset** | Existing pool | Provided by supervisor/research team [Category C] |
| **Analysed Controls** | 5 | Age-matched; randomly selected from available control pool [Category C] |

[SUPERVISOR CONFIRMATION REQUIRED: REC 17/EE/0346 is reported in the Research Proposal, whereas published PREFER-CMR literature reports REC 21/NE/0149. The applicable approval for this specific dissertation analysis must be confirmed before the final dissertation is submitted.]

BSA was present in the AS cohort workbook for 5/38 records; the formula/software used to generate these values was not established from the available raw data [VERIFY].

The 5+5 analysed subset may constitute a pragmatic/time-limited subset rather than a strictly random sample from the full registry. Randomisation method: [VERIFY FROM RECORDS]. Selection bias is acknowledged in Limitations.

### 1.12 Scope of This Dissertation

Part B reports:
- **Completed**: LV contouring workflow and volumetric/functional results; 4D-flow energetic analysis (KE, vorticity, energy loss by phase) with descriptive and comparative statistics
- **Planned**: Non-invasive PV-loop reconstruction methodology and anticipated outputs; association analyses between flow and myocardial energetics

Part B does **not** reproduce the Part A literature review. Part A evidence is cross-referenced by section where it supports the Introduction rationale. All methodology descriptions explicitly distinguish completed work from planned work using the Category A/B/C/D classification established in the project evidence map.

---