# Part B Methods Evidence Map — PREFER-CMR Methodology Audit
**UEA MRes Clinical Science — Part B Main Research Project**  
*Prepared: 2026-08-22*  
*Student: Md Moied Hosen*  
*Supervisor: Dr Pankaj Garg*

---

## HIERARCHY KEY

| Code | Category | Description |
|------|----------|-------------|
| **A** | **Directly Documented in My Project** | Student's own project records, SPSS data, MASS analysis logs, personal recollection of analysis steps |
| **B** | **Directly Documented in Same-Dataset/Same-Protocol Published Research** | Peer-reviewed PREFER-CMR publications (Archer 2020, Grafton-Clarke 2022, Grafton-Clarke 2025, Elhawaz 2021) — **cited in Part A** |
| **C** | **My Personal Recollection** | Student's memory of analysis steps not captured in records |
| **D** | **Supervisor Confirmation Required** | Cannot be established from A, B, or C; requires Dr Garg confirmation |

> **Critical Principle**: For every methodological detail, identify its category (A/B/C/D) and cite the supporting source. Never present Category B as Category A. Never assume Category B applies to your specific scans without verification.

---

## 1. CMR ACQUISITION PROTOCOL

### 1.1 Scanner and Field Strength

| Detail | Category | Evidence Source | Notes |
|--------|----------|----------------|-------|
| **Scanner manufacturer** | B | Archer et al. (2020) / Grafton-Clarke et al. (2025) — Part A cites these as PREFER-CMR studies | Part A does not explicitly name manufacturer in the extracted text. Archer 2020 (Sci Rep) and Grafton-Clarke 2025 (Open Heart) are PREFER-CMR publications. **Need to verify from full papers** whether scanner is stated (likely Siemens/Philips/GE at NNUH). |
| **Scanner model** | B | Same as above | **Need to verify from full papers** |
| **Field strength** | **A + B** | **Student confirmation**: "NNUH 1.5T scanner" (Research Proposal, Reflective Essay) **Part A**: Consistent with 1.5T clinical CMR | **Category A for your scans** — you confirm 1.5T. Category B supports this as standard for PREFER-CMR. |
| **Site** | A | NNUH (Norfolk and Norwich University Hospital) — Research Proposal, Reflective Essay, Part A | Your scans: NNUH. PREFER-CMR recruitment: NNUH. |

### 1.2a Raw Data Evidence — Cohort Workbook (`AS cohort_Moied.xlsx`, sheet `AS Demo`)

| Detail | Category | Evidence Source | Notes |
|--------|----------|----------------|-------|
| **Cohort size in workbook** | A | `AS cohort_Moied.xlsx` → `AS Demo` sheet | **38 rows of AS cohort data** |
| **Records with key clinical variables** | A | `AS Demo` sheet | Height, Weight, HR, SYS_BP, DIA_BP, CMR DATE: **28/38 records**; BMI: 22/38; BSA: **5/38** |
| **BP variables present** | A | `AS Demo` sheet | `SYS_BP` and `DIA_BP` explicitly present for 28 AS records |
| **Anthropometrics present** | A | `AS Demo` sheet | Height, Weight, BMI for 28 records; BSA for 5 records |
| **BSA formula** | **[VERIFY — ORIGINAL DATA SOURCE / SUPERVISOR CONFIRMATION REQUIRED]** | Not in workbook | Workbook does not establish which BSA formula was used or whether BSA was calculated in-source or imported. Student did not calculate BSA. |
| **BP acquisition protocol** | **[VERIFY / SUPERVISOR CONFIRMATION REQUIRED]** | Not in workbook | Workbook does not establish: automated/manual, device, position, timing relative to CMR, number of readings, missing-data procedure. **BP values in raw dataset = Category A. Exact BP acquisition protocol = Category D.** Published PREFER-CMR literature states brachial systolic/diastolic BP measured before CMR using sphygmomanometer, but do not assume identical protocol for the 5+5 without confirmation. |

### 1.2b Selection of the 5 AS + 5 Controls (Student Workflow)

| Detail | Category | Evidence Source | Notes |
|--------|----------|----------------|-------|
| **AS case selection** | C | Student workflow description | **5 AS participants randomly selected from the available dataset** |
| **Control dataset source** | C | Student workflow description | **Existing research/control dataset provided by supervisor/research team** |
| **Control matching** | C | Student workflow description | **Age-matched to AS participants** |
| **Control selection** | C | Student workflow description | **Five controls randomly selected from the available control dataset** |
| **Recruitment** | C | Student workflow description | **Not performed by student** — dataset provided by supervisor/research team |
| **Randomisation method** | **[VERIFY FROM RECORDS]** | Not documented | Do not claim specific randomisation software, RNG, or sampling algorithm unless verified from records |

### 1.2 Cine Acquisition (LV Volumes, Mass, Function)

| Detail | Category | Evidence Source | Notes |
|--------|----------|----------------|-------|
| **Sequence type** | B | Part A (Ch.2): "Cine imaging: To quantify LV volumes, mass, and function" (Research Proposal); Dyverfeldt consensus (Ref 5) describes standard balanced SSFP cine | Part A Research Proposal lists "Cine Imaging" as part of standardized protocol. Dyverfeldt consensus (Ref 5 in Part A) gives typical parameters. **PREFER-CMR specific cine parameters not explicitly detailed in Part A text.** |
| **Short-axis stack** | B | Research Proposal: "cine (short-axis stack + LVOT views)"; Part A Ch.2: LV volumes from "cine imaging" | Standard short-axis stack from base to apex. **Slice thickness, gap, number of slices — not specified in Part A for PREFER-CMR.** |
| **LVOT views** | B | Research Proposal: "short-axis stack + LVOT views" | Standard 2-chamber, 3-chamber, 4-chamber + LVOT cines. **Not detailed in Part A.** |
| **Spatial resolution (cine)** | B | Dyverfeldt consensus (Part A Table 1): typical ~1.5–3.0 mm for 4D flow; cine typically higher (~1.5–2.0 mm in-plane) | **PREFER-CMR specific cine resolution not in Part A.** |
| **Temporal resolution (cine)** | B | Dyverfeldt consensus: typical 30–40 ms for 4D flow; cine typically 30–50 ms | **PREFER-CMR specific not in Part A.** |
| **Breath-holding** | B | Dyverfeldt consensus: "ECG gating / respiratory control required"; typical breath-hold cine | **PREFER-CMR specific not in Part A.** |
| **ECG gating** | B | Dyverfeldt consensus: "Required for time-resolved reconstruction" | Standard prospective/retrospective ECG gating. **PREFER-CMR specific not in Part A.** |
| **Trigger delay / cardiac phases** | B | Standard cine: 25–30 phases per cardiac cycle | **PREFER-CMR specific not in Part A.** |

### 1.3 Phase-Contrast / 4D Flow Acquisition

| Detail | Category | Evidence Source | Notes |
|--------|----------|----------------|-------|
| **4D flow sequence** | B | Part A Ch.2: "4D flow CMR is a phase-contrast magnetic resonance technique"; Part A Ch.3: Archer 2020, Grafton-Clarke 2022/2025 used 4D flow | **PREFER-CMR specific 4D flow sequence parameters not explicitly detailed in Part A text.** |
| **Spatial resolution (4D flow)** | B | Part A Table 1 (Dyverfeldt consensus): "~1.5–3.0 mm"; Archer 2020 / Grafton-Clarke 2025 likely similar | **PREFER-CMR specific not in Part A.** |
| **Temporal resolution (4D flow)** | B | Part A Table 1: "~30–40 ms" (consensus) | **PREFER-CMR specific not in Part A.** |
| **VENC (Velocity Encoding)** | B | Part A Ch.2: "VENC selection requires balance... particularly relevant in AS, where high transvalvular velocities occur"; Part A Table 1: "Set to expected peak velocity" | **PREFER-CMR specific VENC value not in Part A.** Typical AS: 200–400 cm/s. |
| **Acquisition duration (4D flow)** | B | Part A Table 1: "~5–25 min (protocol dependent)" | **PREFER-CMR specific not in Part A.** |
| **Breath-holding / respiratory control** | B | Part A Ch.2: "Respiratory motion also needs to be controlled or compensated... different approaches can be used depending on the protocol" | **PREFER-CMR specific (free-breathing with navigator? breath-hold?) not in Part A.** |
| **ECG gating (4D flow)** | B | Part A Ch.2: "acquisition is synchronised with the cardiac cycle to produce time-resolved velocity data" | Standard retrospective ECG gating. **PREFER-CMR specific not in Part A.** |
| **Aortic valve plane coverage** | B | Part A Ch.2: "velocity data acquired throughout a volume, allowing measurement planes to be positioned retrospectively" | 3D volume covering LVOT, aortic valve, ascending aorta. **PREFER-CMR specific slab thickness/position not in Part A.** |
| **Contrast administration** | B | Part A Ch.6: "CMR also contributes... tissue characterisation, including late gadolinium enhancement and T1 mapping" — implies contrast used in some PREFER-CMR scans | **Not stated whether 4D flow scans used contrast.** Typically 4D flow is non-contrast. **Need verification.** |
| **Image reconstruction** | B | Part A Ch.2: "Background phase errors... need to be corrected, while concomitant gradient effects may require separate correction. Velocity aliasing can also be corrected during post-processing." | Standard 4D flow reconstruction pipeline. **PREFER-CMR specific reconstruction not detailed.** |

### 1.4 Blood Pressure Measurement

| Detail | Category | Evidence Source | Notes |
|--------|----------|----------------|-------|
| **Method** | **D** | Research Proposal: "brachial cuff blood pressure measurements"; Proposal contingency: "missing blood pressure data, the nearest available reading (≤48 h) will be utilized" | **Your specific protocol for the 5+5 cases: NOT DOCUMENTED.** Category D — need your records or supervisor confirmation. |
| **Timing relative to CMR** | **D** | Research Proposal: "brachial blood pressure recorded within ±24 hours" | **Your specific timing for 5+5: NOT DOCUMENTED.** Category D. |
| **Device (automated/manual)** | **D** | Not in any source | Category D. |
| **Position (supine/seated)** | **D** | Not in any source | Category D — critical for PV-loop accuracy. |
| **Number of measurements / averaging** | **D** | Not in any source | Category D. |

---

## 2. STUDY POPULATION AND COHORT DEFINITIONS

### 2.1 PREFER-CMR Registry Cohort (Published)

| Detail | Category | Evidence Source | Notes |
|--------|----------|----------------|-------|
| **Registry name** | B | Part A Ch.6: "PREFER-CMR registry"; Research Proposal: "PREFER-CMR registry" | PREFER-CMR = PReserved Ejection Fraction Evaluation and Recognition — by Cardiac Magnetic Resonance |
| **Published AS cohort size** | B | Part A Ch.3 Table 2: Grafton-Clarke 2025 — "AS (PREFER-CMR), n=30"; Reflective Essay: "28 patients recruited into PREFER-CMR registry" | **Discrepancy**: Published paper (Grafton-Clarke 2025) = 30 AS; Reflective Essay = 28 AS. May reflect different timepoints or inclusion criteria. |
| **Published Control cohort size** | B | Research Proposal: "Controls: 20 age-matched healthy control subjects"; Part A Ch.3 Table 2: Grafton-Clarke 2025 does not mention controls; Archer 2020 had healthy volunteers (n=4 in Dyverfeldt 2013 referenced in Ch.5) | **No published PREFER-CMR control cohort size in Part A citations.** |
| **Inclusion criteria (published)** | B | Research Proposal (planned): Age ≥18, mod/sev AS by echo/CMR, diagnostic-quality CMR + BP ±24h | **Published PREFER-CMR inclusion criteria not explicitly detailed in Part A.** |
| **Exclusion criteria (published)** | B | Research Proposal (planned): Prior AVR/TAVI, significant concomitant VHD (≥mod MR/AR), inadequate image quality | **Published PREFER-CMR exclusion criteria not explicitly detailed in Part A.** |
| **Ethics approval (published)** | B | **Part A does not state ethics for PREFER-CMR papers.** Research Proposal: REC 17/EE/0346. **User reports published paper states REC 21/NE/0149.** | **DISCREPANCY IDENTIFIED** — see Section 8. |

### 2.2 Raw Data Evidence — Cohort Workbook (`AS cohort_Moied.xlsx`)

| Detail | Category | Evidence Source | Notes |
|--------|----------|----------------|-------|
| **AS cohort workbook size** | A | `AS cohort_Moied.xlsx` → `AS Demo` sheet | **38 rows** of AS cohort data |
| **Records with complete clinical data** | A | `AS Demo` sheet | 28/38 records have Height, Weight, HR, SYS_BP, DIA_BP, CMR DATE |
| **BSA availability in workbook** | A | `AS Demo` sheet | BSA present for **5/38** records only |

### 2.3 Your Analysed Cohort (5 AS + 5 Controls)

| Detail | Category | Evidence Source | Notes |
|--------|----------|----------------|-------|
| **AS cases analysed** | A | Student confirmation; `Data of AS cohorts.xlsx` → `Case (Results)` | **5 AS cases** with 4D-flow results (identifiers in workbook) |
| **Controls analysed** | A | Student confirmation; `Data of AS cohorts.xlsx` → `Control (Results)` | **5 controls** with 4D-flow results (identifiers in workbook) |
| **AS case selection** | C | Student workflow description | **5 AS participants randomly selected from the available dataset** |
| **Control dataset source** | C | Student workflow description | **Existing research/control dataset provided by supervisor/research team** |
| **Control matching** | C | Student workflow description | **Age-matched to AS participants** |
| **Control selection** | C | Student workflow description | **Five controls randomly selected from the available control dataset** |
| **Recruitment** | C | Student workflow description | **Not performed by student** — dataset provided by supervisor/research team |
| **Randomisation method** | **[VERIFY FROM RECORDS]** | Not documented | Do not claim specific randomisation software, RNG, or sampling algorithm unless verified from records |
| **Overlap with published cohorts** | **D** | Part A cites Grafton-Clarke 2025 (n=30 PREFER-CMR AS) | **Cannot assume your 5 AS are subset of published 30** without participant-level evidence. Category D. |

---

## 3. LV CONTOURING AND CMR ANALYSIS (COMPLETED)

### 3.1 Software and Version

| Detail | Category | Evidence Source | Notes |
|--------|----------|----------------|-------|
| **Software** | A | Student confirmation: MASS software | **Category A** — your direct action. |
| **Version** | A | Student confirmation: MASS vDec2025 | **Category A** — your direct action. |
| **Vendor** | B | MASS = Leiden University Medical Center (LUMC) / Medis Medical Imaging Systems | Known from general knowledge. |

### 3.2 Contouring Workflow

| Detail | Category | Evidence Source | Notes |
|--------|----------|----------------|-------|
| **Endocardial contouring** | A | Student confirmation: "LV short Axis contouring (LV endo + Epi)" | **Category A** — your direct action. |
| **Epicardial contouring** | A | Student confirmation: "LV short Axis contouring (LV endo + Epi)" | **Category A** — your direct action. |
| **Initial contour generation** | C | Student workflow description | **AI-generated by MASS** (auto-contouring) |
| **Manual correction** | C | Student workflow description | **Yes — manually checked AI contours and corrected where necessary** |
| **Papillary muscle handling** | C | Student workflow description | **Left within the LV blood pool** during contouring |
| **Basal slice handling** | C | Student workflow description | **Excluded when insufficient LV cavity/endocardial information to reliably define LV endocardium** |
| **Apex rule** | **[VERIFY FROM RAW DATA/MASS WORKFLOW]** | Not established | Exact apical-slice rule not yet established by student |
| **Cardiac phases analysed** | **[VERIFY FROM RAW DATA/MASS WORKFLOW]** | Not established | Student not certain whether all cine phases or defined subset |
| **Quality control / supervisor review** | C | Student workflow description | **Dr Rui performed quality checking/review of contouring and provided feedback; student corrected contours per feedback and obtained re-approval** |
| **Formal reproducibility analysis** | — | Student workflow description | **NOT performed** — do NOT describe as inter-observer or intra-observer reproducibility analysis |
| **Training** | C | Reflective Essay: "Dr. Garg and his team... sat down with me to teach me how to use the MASS software step by step" | **Category C** — your recollection of training. |

### 3.3 Derived CMR Parameters (from Contouring)

| Parameter | Category | Evidence Source | Notes |
|-----------|----------|----------------|-------|
| **LV end-diastolic volume (LVEDV)** | A | Derived from your contouring | Will be in SPSS. |
| **LV end-systolic volume (LVESV)** | A | Derived from your contouring | Will be in SPSS. |
| **LV stroke volume (LVSV)** | A | Derived from your contouring | Will be in SPSS. |
| **LV ejection fraction (LVEF)** | A | Derived from your contouring | Will be in SPSS. |
| **LV mass (LVM)** | A | Derived from your contouring (endo+epi) | Will be in SPSS. Papillary muscle handling affects this. |
| **LV mass index (LVMi)** | A | Derived from LVM / BSA | BSA needed — **Category C/D** (how was BSA calculated?). |
| **Aortic flow / stroke volume (PC-MRI)** | **B/D** | Research Proposal: "Phase-Contrast MRI: To measure stroke volume at the aortic root" | **Your 5+5: NOT CONFIRMED if PC-MRI analysed.** Category B (protocol planned) or D. |

---

## 4. PV-LOOP RECONSTRUCTION (PLANNED — NOT YET GENERATED)

> **STATUS: PLANNED METHODOLOGY ONLY** — Must be described as **planned** in Methods, not completed.

| Detail | Category | Evidence Source | Notes |
|--------|----------|----------------|-------|
| **Software / Implementation** | **D** | **Not in any published PREFER-CMR paper** (Part A Ch.5: "direct studies combining these measurements in AS are currently limited"; PV-loop validation in HF not AS) | **Category D — Supervisor confirmation REQUIRED.** Options: MASS PV-loop module? Custom Python/MATLAB (Seemann/Arvidsson)? Commercial (Circle CVI, etc.)? |
| **Algorithm / Model** | **D** | Part A Ch.5: Seemann 2019 (time-varying elastance + brachial BP + CMR volumes); Arvidsson 2023 (validation in HF) | **Category D — Need supervisor to confirm which implementation.** |
| **Inputs required** | B (planned) | Part A Ch.5 / Seemann 2019: LV volume curve (CMR), brachial BP, valve timing, time-varying elastance model | **Planned inputs** — your CMR volumes + BP (Category A/D) + valve timing ([VERIFY]) + model assumptions (Category D). |
| **Brachial BP source** | **D** | See Section 1.4 | BP values present in raw dataset (Category A); exact acquisition protocol = [VERIFY / SUPERVISOR CONFIRMATION REQUIRED]. |
| **Valve timing method** | **[VERIFY FROM MASS/RAW DATA/PUBLISHED PROTOCOL]** | Student workflow description | **Student does not recall whether MASS auto-generated valve timing/flow curve, or whether they manually selected frames from cine/PC-MRI/4D-flow. Cannot establish which source determined final aortic valve opening/closing timings.** Do not assume MASS auto-determined, manual selection, cine alone, or PC-MRI alone unless independently verified. |
| **Emax estimation** | **D** | Seemann 2019: single-beat estimation; Arvidsson 2023: multi-beat or single-beat | **Category D — Supervisor must confirm approach.** |
| **V0 (volume intercept) handling** | **D** | Seemann 2019 / Arvidsson 2023: assumed or estimated | **Category D.** |
| **Arterial elastance (Ea) calculation** | **D** | Seemann 2019: end-systolic pressure / stroke volume | **Category D.** |
| **Output parameters** | B (planned) | Part A Ch.5 / Proposal: SW, PVA, PE, SW/PVA (efficiency), Ea, Emax | **Planned outputs** — not yet generated. |
| **Validation for AS** | B | Part A Ch.5: "validation was performed in only four patients with advanced heart failure... accuracy and clinical usefulness of non-invasive PV loops in AS therefore require direct investigation" | **Critical limitation** — no published validation in AS. Must be stated. |

---

## 5. 4D-FLOW ANALYSIS (KE, Vorticity, Energy Loss) — **ACTUAL OUTPUTS PRESENT**

> **Correction from raw data evidence (PART_B_RAW_DATA_EVIDENCE.md):** 4D-flow outputs are **not merely planned** — actual numerical results for KE, vorticity and energy loss are present for 5 AS cases and 5 controls in the workbook `Data of AS cohorts.xlsx`.

### 5.1 Acquisition (from Published PREFER-CMR Protocol)

| Detail | Category | Evidence Source | Notes |
|--------|----------|----------------|-------|
| **4D flow acquisition in PREFER-CMR** | B | Part A Ch.3: Grafton-Clarke 2025 (PREFER-CMR, n=30) used 4D flow; Archer 2020 (n=18 severe AS) used 4D flow; Grafton-Clarke 2022 (n=11) used 4D flow with CAAS | **Published PREFER-CMR studies acquired 4D flow.** |
| **4D flow software (published)** | B | Part A Ch.2: Grafton-Clarke 2022 used "CAAS MR Solutions" semi-automated pipeline; Archer 2020 used manual analysis (likely GTFlow or CAAS) | **Your analysis software: NOT CONFIRMED.** |
| **4D flow processing (published)** | B | Part A Ch.2: "Background phase errors... corrected... concomitant gradient effects... aliasing correction... segmentation... measurement planes positioned" | Standard pipeline. **Your processing: NOT CONFIRMED.** |

### 5.2 Raw Data Evidence — 4D-Flow Workbook (`Data of AS cohorts.xlsx`)

| Detail | Category | Evidence Source | Notes |
|--------|----------|----------------|-------|
| **4D-flow results present for 5+5** | A | `Data of AS cohorts.xlsx` → sheets `Case (Results)` (5 AS), `Control (Results)` (5 controls) | **Actual numerical outputs confirmed present.** Not planned — completed for the analysed subset. |
| **Outcome variables** | A | `Case (Results)` / `Control (Results)` sheets | **KE**, **Vorticity**, **Energy loss** — each subdivided by cardiac phase |
| **Cardiac phases reported** | A | Result sheets | **FullRR, Systolic, Diastolic, E-Wave, A-Wave** — phase-specific outputs |
| **Units (raw output)** | A | Result sheets | **Energy / KE**: µJ/ml | **Vorticity**: 1/s (s⁻¹) | **Energy loss**: µW |
| **Time-resolved raw output** | A | `Final Raw data (Case)` sheet | Blocks: `KE-Time-MultiSlice`, `4DF-Vorticity-MultiSlice`, `4DF-Energyloss-MultiSlice`; includes `Trigger delay [ms]`, `Energy [µJ/ml]`, `Energyloss [µW]`; average/min/max with time-delay/index info |
| **AS case identifiers (anonymised for dissertation)** | A | `Case (Results)` sheet | 5 records (PXG4-MR-0071-20240411, RXL820231018145906, RXL820231019103947, RXL820231019111559, RXL820231019114613) — **must be anonymised as AS01–AS05 in dissertation** |
| **Control identifiers (anonymised for dissertation)** | A | `Control (Results)` sheet | 5 records (RXL820250326111530, RXL820250326112003, RXL820251021130852, RXL820250922092535, RXL820250921234156) — **must be anonymised as Control01–Control05** |
| **LV endocardial time-series** | A | `Final Raw data (Case)` → `LV Endo` series | Detailed time-series for FullRR, Systolic, Diastolic, E-Wave, A-Wave with avg/min/max and time-delay/index |
| **Working statistical tests in workbook** | A | Sheets `T test (Case vs Control)` and `mann whitney` section | **WORKING ANALYSIS ONLY** — do not treat as final; final analysis must come from completed SPSS |

### 5.3 Your 4D-Flow Analysis — Methodological Details (Student Workflow + Raw Data)

| Detail | Category | Evidence Source | Notes |
|--------|----------|----------------|-------|
| **Actual 4D-flow analysis performed** | A | Student workflow + raw workbook | **Yes — completed for 5 AS + 5 controls; outputs in `Data of AS cohorts.xlsx`** |
| **Software used** | C | Student workflow description | **MASS** (version date: 10 Dec 2025) |
| **Analysis performed by** | C | Student workflow description | **Student personally performed the 4D-flow analysis** |
| **LV segmentation/contouring** | C | Student workflow description | **LV endocardial and epicardial contours** used |
| **Software visualisation** | C | Student workflow description | **Colour-coded flow visualisation displayed** |
| **Software outputs generated** | C | Student workflow description | **Curves for KE, vorticity, energy loss** |
| **Outputs recorded** | A | Raw workbook `Data of AS cohorts.xlsx` | **KE, vorticity, energy loss** for 5 AS + 5 controls |
| **Phase-specific outputs** | A | Raw workbook | **FullRR, Systolic, Diastolic, E-Wave, A-Wave** — automatically produced by software, not manually calculated |
| **Units (raw output)** | A | Raw workbook | **KE/Energy: µJ/ml | Vorticity: s⁻¹ | Energy loss: µW** |
| **Time-resolved blocks** | A | Raw workbook | **KE-Time-MultiSlice, 4DF-Vorticity-MultiSlice, 4DF-Energyloss-MultiSlice** with trigger delay, avg/min/max, time-delay/index |
| **Acquisition VENC** | **[VERIFY]** | Not in workbooks / student workflow | Student does not know VENC |
| **Exact MASS processing algorithm** | **[VERIFY]** | Not in workbooks / student workflow | Student does not know exact algorithm |
| **Exact software processing parameters** | **[VERIFY]** | Not in workbooks / student workflow | Student does not know detailed parameters |
| **Detailed ROI/segmentation settings** | **[VERIFY]** | Not in workbooks / student workflow | Student does not know exact settings |
| **Exact LV boundary definition for KE** | **[VERIFY]** | Not in workbooks / student workflow | Student does not know internal LV boundary definition used by software |
| **Preprocessing/background phase correction** | **[VERIFY]** | Not in workbooks / student workflow | Student does not know correction details |
| **Algorithm for phase-specific summary derivation** | **[VERIFY]** | Not in workbooks / student workflow | Student does not know how FullRR/Systolic/Diastolic/E-Wave/A-Wave derived from time-series |
| **Software version beyond recorded date** | **[VERIFY]** | Not in workbooks / student workflow | Student only knows version date: 10 Dec 2025 |
| **Published PREFER-CMR 4D-flow methodology** | B | Part A: Grafton-Clarke 2022 (CAAS), Archer 2020, Garcia 2019, Aliabadi 2025 | May be used to establish protocol parameters where directly relevant, but do not claim published parameter was definitely used in these cases unless evidence supports this |

---

## 6. STATISTICAL ANALYSIS

| Detail | Category | Evidence Source | Notes |
|--------|----------|----------------|-------|
| **Planned tests (Proposal)** | B | Research Proposal: "independent samples t-test (or Mann-Whitney U test if data is not normally distributed)" | **Planned for n=30+20.** |
| **Appropriateness for n=5/group** | **D** | **Critical issue** — t-test underpowered at n=5; normality testing (Shapiro-Wilk) unreliable at n=5 | **Category D — Supervisor/statistician confirmation REQUIRED.** |
| **Actual tests to be used** | **D** | Not yet determined | **Category D — Depends on SPSS analysis (normality, variance, missing data).** |
| **Effect size measures** | **D** | Not in Proposal | **Category D — Cohen's d? Rank-biserial? Cliff's delta?** |
| **Correlation analysis** | B (planned) | Research Proposal: "correlated with PV loop energetic parameters" | **Planned only.** Category D for actual execution. |
| **Significance threshold** | B | Research Proposal: "p-value of <0.05" | Standard. |
| **Multiple testing correction** | **D** | Not in Proposal | **Category D — Needed?** (3 primary outcomes: SW, PVA, efficiency). |
| **Software** | A | Research Proposal: SPSS | **Category A — confirmed.** |

---

## 7. ETHICS AND GOVERNANCE

### 7.1 Ethics Discrepancy

| Source | REC Reference | Category | Notes |
|--------|--------------|----------|-------|
| **Research Proposal** | 17/EE/0346 | A | "East of England - Cambridge Central Research Ethics Committee" |
| **Published PREFER-CMR paper (user report)** | 21/NE/0149 | B (reported) | User states published paper cites different REC |
| **Resolution** | **D** | **D** | **SUPERVISOR CONFIRMATION REQUIRED** — Are these: (a) different study phases? (b) amendment? (c) different cohorts? (d) error in one source? |

### 7.2 Your Sub-Study Coverage

| Detail | Category | Evidence Source | Notes |
|--------|----------|----------------|-------|
| **Sub-study covered by parent ethics** | **D** | Research Proposal: "This sub-study uses de-identified retrospective data and is covered by the original ethical framework" | **Category D — Supervisor must confirm** which REC applies and that sub-study is covered. |
| **Data anonymisation** | A | Research Proposal: "Data will be anonymized with a study ID key stored separately" | **Planned** — confirm implemented. |
| **Data storage** | A | Research Proposal: "secure university drives... restricted-access" | **Planned** — confirm implemented. |

---

## 8. EVIDENCE MAP SUMMARY — METHODS SECTION STRUCTURE

### For Each Methods Subsection, Use This Template:

```
2.x [Subsection Title]

[Description of what was DONE (Category A) or PLANNED (Category B/D)]

Category A details: [your records/recollection]
Category B details: [PREFER-CMR publication citations — cite as (Author, Year)]
Category C details: [your recollection — mark as [RECOLLECTION]]
Category D details: [SUPERVISOR CONFIRMATION REQUIRED]
```

### Example Application:

#### 2.7 CMR Acquisition

> All participants underwent CMR at NNUH on a 1.5T scanner (Category A — student confirmation of site and field strength; Category B — consistent with PREFER-CMR publications [Archer et al., 2020; Grafton-Clarke et al., 2025]). The standardised PREFER-CMR protocol included balanced SSFP cine imaging in short-axis stack and long-axis views for LV volumes, mass, and function (Category B — Research Proposal; Grafton-Clarke et al., 2025). Phase-contrast 4D flow CMR was acquired prospectively as part of the PREFER-CMR protocol (Category B — Grafton-Clarke et al., 2025; Archer et al., 2020). Specific sequence parameters (spatial resolution, temporal resolution, VENC, breath-hold strategy) for the PREFER-CMR protocol are documented in the primary publications [Archer et al., 2020; Grafton-Clarke et al., 2025] (Category B). **Whether the individual scans for the 5+5 analysed cohort used identical parameters requires verification (Category D — [SUPERVISOR CONFIRMATION REQUIRED]).** BP values present in raw dataset (Category A); exact BP acquisition protocol = [VERIFY / SUPERVISOR CONFIRMATION REQUIRED].

#### 2.9 MASS Analysis / 2.10 LV Contouring

> LV endocardial and epicardial contours were drawn on short-axis cine images using MASS software (version Dec 2025) (Category A — student confirmation). Contouring was performed for 5 AS cases and 5 healthy controls from the available PREFER-CMR cohort. **Selection:** AS — 5 randomly selected from available dataset (Category C); Controls — existing control dataset provided by supervisor/research team, age-matched, 5 randomly selected from available pool (Category C). Randomisation method: [VERIFY FROM RECORDS]. **Contouring workflow (Category C):** AI-generated contours manually checked and corrected; papillary muscles left in blood pool; basal slice excluded when insufficient LV cavity information; supervisor (Dr Rui) review/feedback/re-approval (NOT formal inter/intra-observer reproducibility). **Apex rule and cardiac phases analysed: [VERIFY FROM RAW DATA/MASS WORKFLOW].**

#### 2.11 PV-Loop Reconstruction

> **Non-invasive PV-loop reconstruction is planned but has not yet been performed (Category D — PLANNED METHODOLOGY ONLY).** The planned approach follows the Seemann/Arvidsson framework (Category B — Seemann et al., 2019; Arvidsson et al., 2023) combining CMR-derived LV volume curves, brachial blood pressure, and a time-varying elastance model to estimate LV pressure throughout the cardiac cycle. **The specific software implementation, algorithm details (Emax estimation, V0 handling, arterial elastance calculation), and validation approach for the AS population require supervisor confirmation (Category D — [SUPERVISOR CONFIRMATION REQUIRED]).** Published validation has been performed in heart failure populations (Category B — Arvidsson et al., 2023); direct validation in AS is lacking (Category B — Part A Ch.5). **Valve timing method: [VERIFY FROM MASS/RAW DATA/PUBLISHED PROTOCOL] — student cannot establish whether MASS auto-generated, manual selection from cine/PC-MRI/4D-flow, or which source determined final timings.**

#### 2.15 4D-Flow Analysis

> **4D-flow analysis for kinetic energy (KE), vorticity, and energy loss has been performed and numerical outputs are present for 5 AS cases and 5 controls (Category A — `Data of AS cohorts.xlsx` sheets `Case (Results)`, `Control (Results)`).** Results include phase-specific outputs (FullRR, Systolic, Diastolic, E-Wave, A-Wave) with units: Energy/KE µJ/ml, Vorticity 1/s, Energy loss µW (Category A). Published PREFER-CMR studies acquired 4D flow data and used CAAS MR Solutions for semi-automated analysis (Category B — Grafton-Clarke et al., 2022). **The specific software version, acquisition VENC, segmentation/ROI procedure, phase-summary derivation, valve-timing integration, and LV boundary definitions for KE are NOT established by the workbooks and require supervisor confirmation (Category D — [SUPERVISOR CONFIRMATION REQUIRED]).** LV intracavitary KE interpretation follows Elhawaz et al. (2021) (Category B); energy loss/vorticity interpretation follows Garcia et al. (2019) and Aliabadi et al. (2025) (Category B).

---

## 9. IMMEDIATE ACTIONS REQUIRED

### From Student (Category A/C) — **UPDATED PER RAW DATA EVIDENCE & STUDENT WORKFLOW**
| Action | Details |
|--------|---------|
| **0. Selection mechanism** | **RESOLVED (Category C):** AS: 5 randomly selected from available dataset. Controls: existing control dataset provided by supervisor/research team; age-matched; 5 randomly selected from available control dataset. Randomisation method: [VERIFY FROM RECORDS]. Do not describe as recruitment by student. |
| **1. BP protocol** | **Category A:** SYS_BP/DIA_BP values present in raw dataset for the 5 AS cases. **Category D [VERIFY / SUPERVISOR CONFIRMATION REQUIRED]:** exact acquisition protocol (automated/manual, device, position, timing, readings, missing-data handling). Published PREFER-CMR literature provides context but not confirmation for these 5+5 cases. |
| **2. Contouring details** | **Category C (resolved):** Papillary muscles → left in blood pool. Basal slice → excluded when insufficient LV cavity. Manual correction → yes, AI contours checked and corrected. QC → Dr Rui review/feedback/re-approval (NOT formal inter/intra-observer reproducibility). **Category [VERIFY FROM RAW DATA/MASS WORKFLOW]:** Apex rule, cardiac phases analysed. |
| **3. Valve timing method** | **[VERIFY FROM MASS/RAW DATA/PUBLISHED PROTOCOL]:** Student cannot establish whether MASS auto-generated, manual selection from cine/PC-MRI/4D-flow, or which source determined final timings. |
| **4. 4D-flow methodology** | **Category A/C (resolved):** Analysis performed in MASS (10 Dec 2025) by student; LV endo/epi contours used; software generated KE, vorticity, energy loss for FullRR/Systolic/Diastolic/E-Wave/A-Wave; outputs recorded in workbook. **Category [VERIFY]:** VENC, exact algorithm, processing parameters, ROI settings, LV boundary definition for KE, preprocessing, phase-summary derivation algorithm, full software version. |
| **5. Controls** | **Category C (resolved):** Existing control dataset provided by supervisor/research team; age-matched; 5 randomly selected from available pool. Not recruited by student. |
| **6. BSA calculation** | **[VERIFY — ORIGINAL DATA SOURCE / SUPERVISOR CONFIRMATION REQUIRED]:** BSA present in raw dataset for 5/38 records. Student did not calculate BSA. Formula/software unknown. Do not assume Mosteller, Du Bois, MASS, Excel, or SPSS. |

> **Standing rule**: PV-loop reconstruction remains **PLANNED / NOT COMPLETED** in all documents unless the student provides evidence of personally generating PV loops and deriving SW, PVA and efficiency. The Research Proposal must not be converted into completed methodology anywhere in Part B.

### From Supervisor (Category D)
| Action | Details |
|--------|---------|
| **1. PV-loop software/algorithm** | Confirm: MASS PV module? Custom code? Seemann/Arvidsson implementation? Commercial? |
| **2. PV-loop timeline** | When will loops be generated? Before dissertation submission? |
| **3. Ethics REC discrepancy** | 17/EE/0346 vs 21/NE/0149 — explain difference |
| **4. Statistics for n=5/group** | Appropriate tests? Non-parametric? Exact methods? Bayesian? |
| **5. 4D-flow software access** | CAAS/GTFlow/MASS 4D available for your analysis? |
| **6. Official planned cohort** | 30+20 (Proposal) vs 28+10 (Status doc) — which to state? |

---

## 10. CITATIONS FOR CATEGORY B EVIDENCE

Use these Part A reference numbers when citing PREFER-CMR publications in Methods:

| Part A Ref | Citation | PREFER-CMR Relevance |
|------------|----------|---------------------|
| [8] | Archer G, Elhawaz A, Barker N, et al. Validation of four-dimensional flow cardiovascular magnetic resonance for aortic stenosis assessment. *Sci Rep*. 2020;10(1):10569. | 4D flow vs TTE vs invasive; 18 severe AS; acquisition/analysis methods |
| [6] | Grafton-Clarke C, Njoku P, Aben J, et al. Validation of aortic valve pressure gradient quantification using semi-automated 4D flow CMR pipeline. *BMC Res Notes*. 2022;15(1):151. | Semi-automated CAAS pipeline; 11 severe AS; invasive validation |
| [9] | Grafton-Clarke C, Assadi H, Li R, et al. Four-dimensional flow provides incremental diagnostic value over echocardiography in aortic stenosis. *Open Heart*. 2025;12(1):e003081. | **PREFER-CMR registry, n=30 AS**; 4D flow vs CWD; intervention outcome |
| [17] | Elhawaz A, Archer G, Zafar H, et al. Left ventricular blood flow kinetic energy is associated with the six-minute walk test and left ventricular remodelling post valvular intervention in aortic stenosis. *Quant Imaging Med Surg*. 2021;11(4):1470-1482. | LV blood-flow KE (4D flow); 18 severe AS; pre/post intervention |
| [5] | Dyverfeldt P, Bissell M, Barker A, et al. 4D flow cardiovascular magnetic resonance consensus statement. *J Cardiovasc Magn Reson*. 2015;17(1):72. | Consensus acquisition/analysis standards (not PREFER-CMR specific) |
| [19] | Arvidsson P, Green P, Watson W, et al. Non-invasive left ventricular pressure-volume loops from cardiovascular magnetic resonance imaging and brachial blood pressure: validation using pressure catheter measurements. *EHJ Imaging*. 2023;1(2):qyad035. | PV-loop validation in HF (not AS) |
| [20] | Seemann F, Arvidsson P, Nordlund D, et al. Noninvasive Quantification of Pressure–Volume Loops From Brachial Pressure and Cardiovascular Magnetic Resonance. *Circ Cardiovasc Imaging*. 2019;12(1):e008493. | PV-loop method development/validation in HF |

---

## 11. WRITING RULES FOR METHODS SECTION

1. **Never write "We performed X" for Category B/D items.** Use: "The PREFER-CMR protocol included X [Ref]" or "X is planned [SUPERVISOR CONFIRMATION REQUIRED]."
2. **Explicitly label planned vs completed:** "LV contouring was performed..." (done) vs "PV-loop reconstruction will be performed..." (planned).
3. **Cite Category B evidence with Part A reference numbers** (which will become Part B numbers after renumbering).
4. **Flag every Category D item** with `[SUPERVISOR CONFIRMATION REQUIRED]` in draft.
5. **Flag every Category C item** with `[RECOLLECTION]` in draft.
6. **Maintain cohort distinctions** throughout: Planned (30+20) / Available (28+~10) / Analysed (5+5).
7. **Distinguish myocardial vs flow energetics** terminology consistently (SW/PVA/efficiency vs KE/vEL).

---

*This evidence map is the authoritative reference for writing the Part B Methods section. Update as Category D items are resolved.*