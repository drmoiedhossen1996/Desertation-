# Part B — Methods Working Draft (Sections 2.1–2.10)
**UEA MRes Clinical Science — Part B Main Research Project**
*Revised working draft — dissertation-ready prose with residual [VERIFY] / [SUPERVISOR CONFIRMATION REQUIRED] markers retained only where genuinely unresolved*
*Prepared: 2026-08-22*
*Student: Md Moied Hosen*
*Supervisor: Dr Pankaj Garg*

> **Drafting note**: Category markers [A/B/C/D] are retained in this working version for audit purposes only and will be removed from the submitted dissertation. Part A reference numbers will be renumbered to the Part B sequence.

---

## 2. METHODS

### 2.1 Study Design and Setting

This was a retrospective case–control analysis of existing cardiovascular magnetic resonance (CMR) data from the PREFER-CMR research programme at Norfolk and Norwich University Hospital (NNUH). The parent PREFER-CMR study was approved by the East of England – Cambridge Central Research Ethics Committee (REC 17/EE/0346), and the present sub-study used de-identified retrospective data covered by that ethical framework [Category A — Research Proposal]. Published PREFER-CMR literature reports a different reference, REC 21/NE/0149; the relationship between the two references has not been established and is addressed in Section 2.10 [SUPERVISOR CONFIRMATION REQUIRED].

The completed component of this analysis comprised LV contouring and 4D-flow CMR analysis in five participants with moderate-to-severe aortic stenosis (AS) and five age-matched healthy controls. Non-invasive pressure–volume (PV) loop reconstruction was part of the original study design (Research Proposal) but was not completed within the timeframe of this dissertation; it is reported in Section 2.8 as planned methodology only.

### 2.2 Study Population and Participant Selection

The Research Proposal specified a target cohort of 30 patients with moderate-to-severe AS recruited into the PREFER-CMR registry, compared against 20 age-matched healthy controls [Category A — planned]. The AS cohort workbook available to the student (`AS cohort_Moied.xlsx`, sheet `AS Demo`) contains 38 AS records, of which 28 have the principal anthropometric, blood-pressure and CMR-date fields populated [Category A — raw data]. This 38-record workbook has not been confirmed as identical to the cohort of 30 AS patients described in published PREFER-CMR work [Category B — Grafton-Clarke et al., 2025, Part A ref 9]; no participant-level linkage between the two has been established.

Five AS participants were randomly selected from the available AS dataset, and five age-matched controls were randomly selected from a control pool provided by the supervisory/research team [Category C — student workflow]. This control dataset was an existing research resource rather than a cohort recruited by the student. The specific randomisation procedure used has not been recorded and is not stated [VERIFY].

The Research Proposal specified inclusion criteria (age ≥18 years; moderate or severe AS by echocardiographic or CMR criteria; diagnostic-quality CMR with brachial blood pressure recorded within 24 hours) and exclusion criteria (prior aortic valve intervention; significant concomitant valvular disease; inadequate image quality) [Category A — planned]. Whether each criterion was individually verified for the five analysed participants has not been separately confirmed, and application of these criteria to the final sample is not presented as established fact [VERIFY].

The resulting sample is a pragmatic, time-limited subset of the available registry data rather than a formally powered cohort; this is addressed in the Limitations.

**Cohort tiers:**

| Tier | n | Source |
|---|---|---|
| Planned target | 30 AS + 20 controls | Category A (planned) |
| Published PREFER-CMR cohort | 30 AS | Category B |
| AS cohort workbook | 38 AS records | Category A |
| Workbook records with key variables complete | 28 AS | Category A |
| Analysed cohort | 5 AS + 5 controls | Category A/C |

### 2.3 CMR Acquisition

All CMR data were acquired retrospectively as part of the PREFER-CMR programme at NNUH on a 1.5 T scanner, and comprised cine imaging together with phase-contrast and 4D-flow CMR [Category A — Research Proposal, Reflective Essay]. The scanner manufacturer and model, and the specific sequence parameters (spatial and temporal resolution, acquisition duration, breath-hold strategy) used for the ten scans analysed here, have not been established from the records available to the student and are not stated [VERIFY]. Published PREFER-CMR-related studies describe general 4D-flow CMR practice [Category B — Part A refs 5, 6, 8, 9], but these figures are not substituted for study-specific parameters that remain unconfirmed.

### 2.4 LV Contouring and Volumetric Analysis

LV short-axis contouring was performed using MASS, with workflow/version information recorded as December 2025 [Category A/C — student workflow]. Endocardial and epicardial contours were generated for each of the five AS cases and five controls. Initial contours were produced automatically by MASS and were subsequently checked and manually corrected by the student [Category C]. Papillary muscles were left within the LV blood pool. A basal slice was excluded from analysis where insufficient LV cavity or endocardial information was present to define the endocardial border reliably [Category C].

Contour quality was reviewed by Dr Rui, who provided feedback; the student corrected the contours accordingly and obtained re-approval [Category C]. This constituted supervisor review of the student's contouring rather than a formal inter-observer or intra-observer reproducibility analysis, and is not described as such.

The apical-slice rule and the specific cardiac phases contoured have not been established from the raw data or MASS workflow records [VERIFY]. Both endocardial and epicardial contours were generated within the CMR workflow; whether both were specifically used by the 4D-flow KE calculation, as opposed to being available more generally within the analysis, has not been separately confirmed [VERIFY] (see Section 2.5).

Where volumetric parameters (LV end-diastolic and end-systolic volume, stroke volume, ejection fraction, LV mass) are reported in the Results, these are derived directly from the completed contours [Category A]. LV mass index requires normalisation to body surface area (BSA); BSA is present in the raw cohort workbook for only 5 of 38 AS records, was not calculated by the student, and its formula or source has not been established [VERIFY].

### 2.5 4D-Flow CMR Analysis

4D-flow analysis is the principal completed component of this dissertation. Analysis was completed for all five AS cases and five controls, and the resulting numerical outputs are recorded in the project's raw-data workbook (`Data of AS cohorts.xlsx`, sheets `Case (Results)` and `Control (Results)`) [Category A].

The analysis was performed using MASS, with workflow/version information recorded as 10 December 2025, and was carried out personally by the student [Category C]. The software provided colour-coded flow visualisation and generated curves for kinetic energy, vorticity and energy loss [Category C]. These outputs were recorded for the full cardiac cycle (FullRR) and for systolic, diastolic, E-wave and A-wave phases, and were produced automatically by the software rather than calculated manually [Category A/C]. The raw case workbook additionally contains time-resolved, multi-slice output blocks for each parameter (`KE-Time-MultiSlice`, `4DF-Vorticity-MultiSlice`, `4DF-Energyloss-MultiSlice`), with trigger-delay information and average, minimum and maximum values across the cardiac cycle [Category A], confirming that the underlying data are time-resolved rather than limited to single summary values.

Whether both endocardial and epicardial LV contours generated during CMR analysis (Section 2.4) were specifically used within the 4D-flow kinetic-energy calculation has not been confirmed [VERIFY]; this is distinguished from the fact that both were available within the overall workflow.

The following technical parameters of the 4D-flow acquisition and processing have not been established and are not reported as known [VERIFY]:

- Acquisition velocity encoding value (VENC)
- The MASS processing algorithm and internal processing parameters
- Region-of-interest and segmentation settings
- The LV boundary definition used internally for the kinetic-energy calculation
- Background-phase correction and other pre-processing steps
- The precise method by which each phase-specific summary was derived from the underlying time-resolved data
- Whether "10 December 2025" corresponds to a formal software version identifier or only a workflow date

Published PREFER-CMR-related work describes 4D-flow processing pipelines, including a semi-automated approach using CAAS MR Solutions [Category B — Grafton-Clarke et al., 2022, Part A ref 6] and manual 4D-flow analysis [Category B — Archer et al., 2020, Part A ref 8]. These are cited for methodological context only; they are not presented as the software or parameters used in the student's analysis unless independently confirmed.

### 2.6 Outcome Measures

The completed primary outcomes of this analysis were the 4D-flow-derived haemodynamic energetic parameters:

1. Kinetic energy (KE) — the energy associated with the motion of blood, reported in µJ/ml
2. Vorticity — a measure of the local rotational characteristic of the flow field, reported in s⁻¹
3. Energy loss — dissipation of mechanical energy within the blood flow, reported in µW

Vorticity describes a rotational flow characteristic and is distinct from energy loss; the two are not interchangeable and are reported separately. Each outcome was assessed over the full cardiac cycle (FullRR) and over systolic, diastolic, E-wave and A-wave phases [Category A].

Secondary volumetric and functional CMR parameters (LV end-diastolic volume, end-systolic volume, stroke volume, ejection fraction, LV mass) are reported where their derivation from the completed contouring is directly supported (Section 2.4). Parameters specified only in the original Research Proposal, but not demonstrably derived from the analysed dataset, are not reported as completed outcomes.

### 2.7 Blood Pressure Data

Systolic and diastolic brachial blood pressure values (`SYS_BP`, `DIA_BP`) were already present in the AS cohort dataset as received by the student and were not personally measured or entered [Category A]. No systolic or diastolic blood pressure values were missing among the five analysed AS cases [Category A].

The blood-pressure acquisition protocol — measurement method (automated or manual), device, patient position, number of readings, timing relative to the CMR scan, and the parent study's handling of missing values — has not been established from the records available to the student [VERIFY]. Published PREFER-CMR-related literature indicates that brachial blood pressure was measured before CMR using a sphygmomanometer [Category B]; this provides methodological context but is not presented as confirmed participant-level methodology for the five analysed cases.

### 2.8 Planned Non-Invasive Pressure–Volume Loop Methodology

Non-invasive PV-loop reconstruction, and derivation of stroke work (SW), pressure–volume area (PVA) and myocardial efficiency (SW/PVA), formed part of the original study design but was not completed for the present dissertation. **No PV-loop values were generated or included in the present results.**

The planned approach follows the non-invasive framework described by Seemann et al. (2019) and Arvidsson et al. (2023) [Category B — Part A refs 20, 19], combining CMR-derived LV volume curves, brachial blood pressure and aortic valve timing within a time-varying elastance model. The specific software or algorithmic implementation to be used remains [SUPERVISOR CONFIRMATION REQUIRED]. Non-invasive PV-loop reconstruction has been validated against invasive measurements principally in heart-failure populations [Category B — Part A refs 19, 20]; direct validation in AS has not been established in the literature reviewed in Part A [Category B — Part A Chapter 5], and this is addressed further in the Discussion.

Determination of aortic valve opening and closing timing, a required input for this planned reconstruction, has not yet been established. The student does not know whether MASS displayed an automatically generated valve-timing curve, or whether valve timing was to be derived from cine imaging, phase-contrast flow curves or 4D-flow data; no specific method is assumed [VERIFY]. This unresolved issue relates specifically to the planned PV-loop component and does not affect the completed 4D-flow analysis reported in Section 2.5.

### 2.9 Statistical Analysis

The Research Proposal specified an independent-samples t-test, or Mann-Whitney U test where data were not normally distributed, with significance defined as p<0.05, for comparison of the originally planned cohort of 30 AS patients and 20 controls [Category A — planned]. This approach was designed for a substantially larger sample than the five participants per group analysed here.

The final statistical approach for the present sample has not yet been determined. Formal normality testing is unreliable at n=5 per group, and the choice between parametric and non-parametric methods, the appropriate effect-size measure, and whether adjustment for multiple comparisons is warranted remain to be confirmed with the supervisory team and, where appropriate, statistical support [SUPERVISOR CONFIRMATION REQUIRED]. The raw-data workbook contains exploratory working sheets labelled "T test (Case vs Control)" and "mann whitney"; these represent preliminary working analysis only and are not the final statistical analysis for this dissertation. This subsection will be replaced with the completed statistical methodology — tests performed, assumptions checked, effect sizes, significance threshold, handling of missing data, and software version — once the final SPSS analysis is available.

### 2.10 Ethics and Data Management

The parent PREFER-CMR study was approved by the East of England – Cambridge Central Research Ethics Committee (REC 17/EE/0346) [Category A — Research Proposal]. Published PREFER-CMR literature reports REC 21/NE/0149. Whether this reflects a different study phase, an amendment, a different cohort, or an inconsistency between sources has not been established, and the applicable approval for the present analysis is [SUPERVISOR CONFIRMATION REQUIRED] before final submission.

The Research Proposal specified that data would be anonymised with a study-identifier key held separately on restricted-access storage, with analysis datasets retained on secure university storage [Category A — planned]. Whether these arrangements were fully implemented for the specific files used in the present analysis has not been separately audited [VERIFY]. The raw-data workbook used for this analysis contains scan accession identifiers for the ten analysed participants; these are not reproduced in this dissertation, and participants are referred to using anonymised study labels (AS01–AS05, Control01–Control05) throughout the Results.

---

## FINAL AUDIT TABLE

| Item | Status |
|---|---|
| **Completed and directly evidenced (Category A)** | Analysed cohort size (5 AS + 5 controls); BP values present with no missing data in the 5 AS cases; 4D-flow numerical outputs (KE, vorticity, energy loss) by phase (FullRR, systolic, diastolic, E-wave, A-wave); units (µJ/ml, s⁻¹, µW); raw workbook cohort tiers (38 records; 28 with key variables; 5 with BSA) |
| **Supported by published PREFER-CMR evidence (Category B)** | General PREFER-CMR acquisition context (NNUH, 1.5T, cine + 4D-flow); non-invasive PV-loop validation in heart failure (not AS); CAAS/manual 4D-flow processing examples from related PREFER-CMR studies |
| **Based on student workflow/recollection (Category C)** | Selection process description; MASS contouring workflow (AI-generated, manually corrected); papillary muscle and basal-slice handling; Dr Rui review process; 4D-flow analysis personally performed; software workflow dates (Dec 2025 / 10 Dec 2025) |
| **Still requires verification [VERIFY]** | Scanner manufacturer/model and exact acquisition parameters; apical-slice rule; cardiac phases contoured; whether endo+epi contours were both used in the KE calculation; VENC; 4D-flow processing algorithm/ROI/segmentation/LV boundary definition; BP acquisition protocol; BSA formula; randomisation procedure; data-management implementation audit |
| **Planned but not completed (Category D)** | Non-invasive PV-loop reconstruction (software, algorithm, SW/PVA/efficiency values); aortic valve timing method; final statistical test selection; REC discrepancy resolution |

### Genuinely Outstanding Items Requiring Resolution Before Final Submission

1. **Ethics REC discrepancy** (17/EE/0346 vs 21/NE/0149) — supervisor confirmation required
2. **PV-loop software/algorithm and timeline** — supervisor decision required
3. **Aortic valve timing methodology** — required only if/when PV-loop work proceeds
4. **Statistical approach for n=5/group** — supervisor/statistician input required; final SPSS analysis pending
5. **4D-flow technical parameters** (VENC, algorithm, ROI/segmentation, LV boundary definition) — may require supervisor or MASS documentation to resolve
6. **Scanner manufacturer/model and CMR sequence parameters** — may require PACS/protocol records
7. **BSA formula** — original data source unknown
8. **Whether endo+epi contours were both used in the 4D-flow KE calculation** — MASS workflow clarification needed

Results Framework (Section 3) has not been drafted, per instruction.