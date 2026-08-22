# Part B Source and Project Status Report
**UEA MRes Clinical Science — Part B Main Research Project**  
*Prepared: 2026-08-22*  
*Student: Md Moied Hosen*  
*Supervisor: Dr Pankaj Garg*

---

## 1. DOCUMENTS SUCCESSFULLY ACCESSED AND READ

### 1.1 Part B Control Files (Repository 3 — `/PART_B/`)
| File | Status | Notes |
|------|--------|-------|
| `PART_B_CURRENT_STATUS.md` | ✅ Read | Cohort status, analysis state, placeholders required |
| `PART_B_SOURCE_HIERARCHY.md` | ✅ Read | 6-level source hierarchy, key rules |
| `PART_B_WRITING_RULES.md` | ✅ Read | 43 writing rules, core standards, integrity requirements |

### 1.2 Final Project Documents (Repository 3 — Root)
| File | Status | Notes |
|------|--------|-------|
| `Research_Proposal_Final.docx` | ✅ Read | Full proposal extracted (1,366 words) |
| `Reflective_essay.docx` | ✅ Read | Full reflective essay extracted |
| `Literature_Review_Final.docx` (SOP formatted) | ✅ Read | Full Part A narrative review extracted (7 chapters, 21 refs) |

### 1.3 Part A Working Materials (Repository 1)
| File | Status | Notes |
|------|--------|-------|
| `Final_4D_Flow_CMR_Narrative_Review_FINAL_corrected.docx` | ⚠️ Available | Same content as final Part A — not yet extracted |
| `citation_map.md` | ✅ Read | 141 citation locations, 21 unique refs |
| `Visuals_Masterplan.md` | ✅ Read | 4 tables, 8 figures planned |
| `reference_list_CORRECT_ORDER.txt` | ⚠️ Summarised | 21 refs in order |
| `references_zotero.ris` | ⚠️ Summarised | 21 refs in RIS format |

### 1.4 UEA Guidance and Exemplars (Repository 2)
| File | Status | Notes |
|------|--------|-------|
| `MRES Handbook-2025-26 Final.pdf` | ❌ Not extracted | PDF binary — requires extraction |
| `Senate-marking-scale-masters-level-dissertations.pdf` | ❌ Not extracted | PDF binary — requires extraction |
| `Rough Guide to the MRes.pdf` | ❌ Not extracted | PDF binary |
| Exemplar dissertations (5652196–5653303) | ❌ Not extracted | PDF binaries |

---

## 2. SOURCE HIERARCHY CONFIRMATION

The **6-level hierarchy** from `PART_B_SOURCE_HIERARCHY.md` is confirmed and will govern all writing:

| Level | Source | Use For |
|-------|--------|---------|
| **1** | UEA official guidance (Repo 2) | Structure, formatting, assessment, word limits |
| **2** | Final project documents (Repo 3) | Research question, aims, hypothesis, study design |
| **3** | Final Part A literature review | Evidence base, knowledge gap, conceptual framework |
| **4** | Research Proposal | Planned methodology, cohort, outcomes *(distinguish planned vs completed)* |
| **5** | Earlier Part A drafts (Repo 1) | Reference tracing only |
| **6** | General academic knowledge | Only when project docs are silent |

**Critical rule**: Research Proposal planned **28 AS + 10 controls**; actual analysis = **5 AS + 5 controls**. Never conflate.

---

## 3. PROJECT STATUS SUMMARY

### 3.1 Cohort Status (from `PART_B_CURRENT_STATUS.md` + Proposal + Reflective Essay + Student Confirmation + Raw Data Evidence)

| Cohort Category | Number | Source | Status |
|-----------------|--------|--------|--------|
| **Original Planned/Target (Proposal)** | 30 AS + 20 Controls = 50 | Research Proposal (Section 4.1) | **PLANNED ONLY** |
| **PREFER-CMR Registry / Available** | 28 AS + ~10 Controls = ~38 | Reflective Essay / Proposal contingency / Student confirmation | **AVAILABLE/ELIGIBLE** |
| **AS Cohort Workbook** | 38 AS records | `AS cohort_Moied.xlsx` → `AS Demo` sheet | **Category A** |
| **Records with BP/Anthropometrics** | 28/38 | `AS Demo` sheet | **Category A** |
| **BSA in workbook** | 5/38 | `AS Demo` sheet | **Category A** |
| **Actual Analysed (Completed)** | 5 AS + 5 Controls = 10 | `PART_B_CURRENT_STATUS.md` / Reflective Essay / Student confirmation / Raw data workbooks | **COMPLETED: LV contouring (endo+epi) + 4D-flow analysis (KE, vorticity, energy loss) for 5+5** |

**Key discrepancies to resolve**:
- Proposal says "Target: 30 patients... Controls: 20"
- Reflective Essay says "28 patients recruited into PREFER-CMR registry"
- `PART_B_CURRENT_STATUS.md` says "Planned cohort: 28 AS + 10 controls"
- **Student confirms**: AS cohort workbook has 38 records; 28 with BP/anthropometrics; BSA only 5/38
- **Selection**: AS — 5 randomly selected from available dataset; Controls — existing control dataset provided by supervisor/research team, age-matched, 5 randomly selected from available pool
- **Randomisation method**: [VERIFY FROM RECORDS] — do not claim specific RNG/software
- **Critical**: PV loops **NOT YET GENERATED** — only LV contouring (endo + epi) + 4D-flow analysis completed in MASS vDec2025

### 3.2 Analysis Status

| Component | Status | Details |
|-----------|--------|---------|
| **CMR Acquisition** | ✅ Complete | Retrospective, existing scans from NNUH 1.5T scanner (PREFER-CMR registry) |
| **MASS Contouring / CMR Analysis** | ✅ Complete (5+5) | LV short-axis endo + epi contouring in MASS vDec2025; 5 AS + 5 Controls (selection mechanism [VERIFY SELECTION MECHANISM]) |
| **PV-Loop Reconstruction** | ❌ NOT YET DONE | **Critical**: PV loops not yet generated — this is PLANNED methodology only |
| **4D-Flow Analysis (KE, Vorticity, Energy Loss)** | ✅ **COMPLETED (5+5)** | Actual numerical outputs confirmed present in `Data of AS cohorts.xlsx` — KE, Vorticity, Energy Loss by cardiac phase (FullRR, Systolic, Diastolic, E-Wave, A-Wave). **Methodological details (software, VENC, segmentation) require supervisor confirmation.** |
| **SPSS Statistical Analysis** | ❌ Not Started | Raw data in SPSS; final analysis **not complete** |

### 3.3 What Can Be Written Now (UPDATED — PV loops not yet generated; 4D-flow outputs present)

| Section | Status |
|---------|--------|
| Title, Abstract framework | ✅ Can write |
| Introduction (1.1–1.12) | ✅ Can write (evidence-based from Part A + literature) |
| Research Question / Aim / Objectives / Hypothesis | ✅ Can write (from Proposal, adjusted for actual work — objectives must reflect ONLY completed work: LV contouring + 4D-flow; PV-loop = planned) |
| Study Design / Methodology (2.1–2.21) | 🟡 **Major change**: PV-loop methods = **PLANNED ONLY**. Contouring = completed. **4D-flow analysis = COMPLETED (outputs present); methodology details need supervisor confirmation.** |
| Results Structure / Table Shells | ✅ Can write (with placeholders) — **Table 3 (PV-loop) marked as PLANNED; Table 4 (4D-flow) populated with actual outputs** |
| Discussion Framework (4.1–4.8) | 🟡 Result-independent parts only |
| Strengths / Limitations | ✅ Can write (genuine limitations — small n, PV loops not yet generated, selection mechanism [VERIFY], 4D-flow methodological details [VERIFY]) |
| Conclusion / Abstract (final) | ❌ Must wait for SPSS AND PV-loop generation |

### 3.4 What Must Wait for SPSS Analysis

| Item | Placeholder Required |
|------|---------------------|
| Final statistical analysis | `[STATISTICAL ANALYSIS TO BE FINALIZED]` |
| Numerical results (means, medians, CIs) | `[INSERT DESCRIPTIVE STATISTICS]` |
| Group comparisons | `[INSERT GROUP COMPARISON]` |
| p-values | `[INSERT P-VALUE]` |
| Effect sizes | `[INSERT EFFECT SIZE]` |
| 4D-flow results (KE, Vorticity, Energy Loss) | Numerical outputs present in workbook — to be transferred to SPSS for final analysis; final Results tables will report these values with `[INSERT FINAL STATISTICAL TEST RESULTS]` |
| Correlations | `[INSERT CORRELATION IF PERFORMED]` |
| Findings-dependent Discussion | `[RESULT-DEPENDENT DISCUSSION]` |
| Final Abstract / Conclusion | Must wait |

---

## 4. UNRESOLVED METHODOLOGICAL ISSUES

### 4.1 Issues Requiring Your Recollection / Project Records

| Issue | Detail Needed | Priority | Status |
|-------|---------------|----------|--------|
| **CMR Acquisition Parameters** | Scanner manufacturer/model; sequence parameters; spatial/temporal resolution; VENC for 4D-flow; phase-contrast parameters | HIGH | ❓ OPEN |
| **Blood Pressure Source** | Brachial cuff vs. arterial line; timing relative to CMR (±24h?); protocol for missing BP | HIGH | ❓ OPEN |
| **MASS Software Version** | **Confirmed**: MASS vDec2025 | HIGH | ✅ RESOLVED |
| **LV Contouring Workflow** | Endocardial/epicardial; **papillary muscle inclusion/exclusion; basal slice handling; apex handling; cardiac phases analysed; manual correction steps; training/QC; repeat contouring** | HIGH | ⚠️ PARTIAL — Need papillary muscle, basal slice, apex, phases, QC details |
| **Valve Timing Method** | How aortic valve open/close determined (cine? phase-contrast?); software used | HIGH | ❓ OPEN |
| **PV-Loop Reconstruction Software** | **NOT YET DONE** — this is PLANNED methodology. Need to confirm: will use MASS? Custom script? Seemann/Arvidsson implementation? | CRITICAL | 🔄 PLANNED ONLY |
| **PV-Loop Algorithm Details** | Time-varying elastance model; assumptions; Emax estimation; V0 handling; arterial elastance (Ea) calculation | HIGH | 🔄 PLANNED ONLY |
| **4D-Flow Analysis Workflow** | Software (CAAS? GTFlow? MASS 4D-flow module?); segmentation method; KE/vEL calculation; LV vs aortic measurement; output units | HIGH | ❓ OPEN — only if 4D-flow data available |
| **Quality Control** | Inter/intra-observer variability; exclusion criteria for poor quality; missing data handling | MEDIUM | ❓ OPEN |
| **Participant Selection Mechanism** | **NOT CONFIRMED** — earlier described as random but withdrawn; must be established from records | HIGH | [VERIFY SELECTION MECHANISM] |

### 4.2 Issues Requiring Supervisor Confirmation

| Issue | Why Supervisor Needed |
|-------|----------------------|
| **PV-Loop Software/Algorithm** | **Critical**: PV loops not yet generated. Need to agree on: software (MASS? custom? Seemann/Arvidsson implementation?); algorithm details; validation approach for AS population |
| **Ethics Confirmation** | REC reference (17/EE/0346) covers parent PREFER-CMR; confirm sub-study coverage | 
| **Cohort Definitions** | Confirm official "planned cohort" (30+20 vs 28+10) for dissertation transparency |
| **4D-Flow Availability** | Confirm which of the 5+5 had usable 4D-flow data |
| **Statistical Approach** | Confirm if original plan (t-test/Mann-Whitney) still appropriate for n=5/group; also — what analysis for PV-loop data once generated? |
| **PV-Loop Generation Timeline** | When will PV loops be generated? Impacts dissertation timeline and what can be claimed as "completed" |

### 4.3 Issues Dependent on SPSS Analysis

| Issue | Resolution |
|-------|------------|
| **Normality Testing** | Shapiro-Wilk on n=5/group — likely underpowered; may need non-parametric |
| **Final Statistical Tests** | Choice depends on distribution, variance homogeneity, missing data |
| **Effect Sizes** | Cohen's d, rank-biserial, or other — calculated from actual data |
| **Correlation Analyses** | Only if n and data support; Spearman vs Pearson |
| **Exploratory Associations** | KE/vEL vs PV-loop parameters — only if both available in same subjects |

---

## 5. PART B SECTION-BY-SECTION WRITING PLAN

Following the workflow in `PART_B_WRITING_RULES.md` (PHASE 1–13):

### PHASE 1: Source and Methodology Audit ✅ **THIS REPORT**

### PHASE 2: Part B Detailed Outline
- Map UEA structure to required sections
- Define table/figure shells
- Set cross-referencing strategy with Part A

### PHASE 3: Introduction (Sections 1.1–1.12)
**Strategy**: Concise clinical background → energetic framework → knowledge gap → study rationale  
**Sources**: Part A (cross-ref), Knaapen 2007, Seemann 2019, Arvidsson 2023, Vahanian 2021, Garg 2024  
**Key distinctions**: Myocardial (SW, PVA, efficiency) vs Flow (KE, vEL) energetics; invasive vs non-invasive PV validation populations

### PHASE 4: Aim / Objectives / Hypothesis
**From Proposal**, adjusted for actual completed work:
- **Aim**: Evaluate myocardial energetics in mod-sev AS using non-invasive CMR PV-loops (+ 4D-flow where available)
- **Objectives**: Only those actually performed (quantify SW, PVA, efficiency; compare AS vs controls; exploratory 4D-flow)
- **Hypotheses**: Retain only those testable with completed analysis

### PHASE 5: Methods (Sections 2.1–2.21) — **UPDATED**
**Critical Rule**: Describe **what actually happened**, not what was planned  
**Status for each method**:
- **CMR Acquisition**: DOCUMENTED AS DONE (retrospective, PREFER-CMR, 1.5T)
- **LV Contouring (MASS vDec2025)**: DOCUMENTED AS DONE (endo+epi, 5+5, selection mechanism [VERIFY SELECTION MECHANISM])
- **PV-Loop Reconstruction**: **PLANNED ONLY** — not yet generated. Must be clearly labelled as planned methodology.
- **4D-Flow Analysis**: UNKNOWN — depends on data availability
- **Statistical Analysis**: PLANNED (t-test/Mann-Whitney per Proposal) — to be confirmed for n=5/group

**Format**: For each method → `DOCUMENTED AS DONE` | `PLANNED BUT NOT CONFIRMED` | `NOT DONE` | `UNKNOWN`  
**Placeholders**: `[VERIFY]` for uncertain details; `[SUPERVISOR CONFIRMATION REQUIRED]` for PV-loop software/algorithm

### PHASE 6: Results Framework (Sections 3.1–3.5)
**Structure only** — table shells with `[INSERT DATA]` placeholders:
- Table 1: Participant Characteristics (n=5 per group)
- Table 2: CMR-Derived Parameters (volumes, mass, EF, gradients)
- Table 3: PV-Loop-Derived Parameters (SW, PVA, PE, Efficiency)
- Table 4: 4D-Flow Parameters — **only if data exist**
- Figure shells: Flowchart, contouring workflow, PV-loop workflow, 4D-flow workflow

### PHASE 7: Discussion Framework (Sections 4.1–4.8)
**Result-independent sections** (4.5–4.8, parts of 4.2–4.4):  
- Strengths (novelty, CMR rigor, non-invasive approach)  
- Limitations (n=5/group, selection bias, retrospective, single-centre, contouring operator-dependence, PV-loop assumptions, 4D-flow resolution sensitivity, statistical power)  
- Future research  
- Clinical relevance framework

**Result-dependent sections** (4.1–4.4): Framework only until SPSS complete

### PHASE 8: SPSS Analysis
**Your task** — with statistician input per PDP  
**Output**: Complete descriptive stats, group comparisons, correlations, assumption checks

### PHASE 9: Results Completion
- Populate all tables/figures with actual numbers
- Write Results narrative (3.1–3.5) using evidence-based language
- No "significant/higher/correlated" without statistical support

### PHASE 10: Results-Dependent Discussion
- 4.1 Principal Findings (traceable to actual results)
- 4.2 Interpretation (physiological context)
- 4.3 Comparison with Literature (specific studies, not generic)
- 4.4 Physiological Interpretation (myocardial vs flow energetics distinction)

### PHASE 11: Conclusion
- Supported by actual findings only
- No overstatement

### PHASE 12: Abstract
- Structured: Background, Methods, Results, Conclusions
- Written last

### PHASE 13: Full Dissertation Consistency Audit
- Cohort: planned vs available vs analysed
- Methods: planned vs completed
- Statistics: planned vs performed
- Results: all numbers traceable to SPSS
- Discussion: all interpretations traceable to results
- References: all real, correctly cited (Vancouver/AMA, Part B numbering)
- Part A/B: no unnecessary repetition
- Terminology: consistent
- Ethics: accurate
- Figures/Tables: accurate and referenced
- Conclusions: supported by findings

---

## 6. IMMEDIATE NEXT STEPS

### For You (Student)
1. **Provide methodological details** for the 4.1 issues above (recollection/project records)
2. **Confirm PV-loop software/workflow** with Dr Garg → resolve `[SUPERVISOR CONFIRMATION REQUIRED]`
3. **Complete SPSS analysis** with statistician input
4. **Confirm 4D-flow data availability** per participant

### For Supervisor
1. Confirm PV-loop reconstruction software and algorithm
2. Confirm official "planned cohort" numbers for dissertation
3. Confirm ethics coverage for sub-study
4. Advise on statistical approach for n=5/group

### For Us (Collaborative)
1. **Next session**: Begin PHASE 2 — Detailed Part B Outline
2. **Then**: PHASE 3 — Introduction (sections 1.1–1.12)
3. Work sequentially — one section at a time with quality audit after each

---

## 7. KEY PRINCIPLES TO MAINTAIN THROUGHOUT

| Principle | Implementation |
|-----------|----------------|
| **Accuracy > Completeness** | Never invent data, methods, or results |
| **Planned ≠ Completed** | Every method: distinguish documented vs planned |
| **Myocardial ≠ Flow Energetics** | SW/PVA/efficiency = myocardial; KE/vEL = blood flow |
| **Evidence-Based Claims** | Every scientific claim → appropriate citation (guideline > systematic review > primary study) |
| **Part B ≠ Part A** | Cross-reference Part A; don't reproduce |
| **UK English, MRes Level** | Precise, concise, analytical — no filler |
| **Placeholders Until Data** | `[INSERT...]`, `[VERIFY]`, `[SUPERVISOR CONFIRMATION REQUIRED]` |

---

## 8. REFERENCE MANAGEMENT

- **Part B has independent reference numbering** (Vancouver/AMA, order of first appearance)
- **21 references from Part A** available — will be renumbered for Part B
- **Citation style**: Superscript numerical; up to 6 authors; DOI format matching Part A
- **During drafting**: Use temporary author-name citations `(Vahanian)`, `(Knaapen)` etc.
- **After Introduction complete**: Convert to numbered style

---

*Report prepared for sequential Part B development. Next step: PHASE 2 — Detailed Part B Outline.*