# Making COSMoS Behavioural Patterns Visible

Insights from analysing 1,127 Biomedical Concepts and 1,123 Dataset Specializations across 31 SDTM domains — and how these patterns relate to the COSMoS model as described in the CDISC GitHub repository.

*cdisc-for-ai project — March 2026*

---

## 1. What the COSMoS Model Describes

The COSMoS data model, maintained in the CDISC GitHub repository as LinkML schemas (`cosmos_bc_model.yaml` and `cosmos_sdtm_bc_model.yaml`), defines a two-layered architecture:

- A **conceptual/abstract layer** — Biomedical Concepts (BCs) that provide standards-agnostic semantic definition, largely based on NCIt concepts.
- An **implementation layer** — SDTM Dataset Specializations (DSSs) that provide value level definition facilitating metadata-driven automation.

The model is intentionally generic. One BC schema and one DSS schema serve all domains — from laboratory tests through vital signs, questionnaires, adverse events, concomitant medications, and trial summary parameters. This flexibility is a design feature: the same model can accommodate SDTM, CDASH, and potentially other standards like HL7 FHIR.

The CDISC description frames BCs as covering "a wide range of topics, including demographics, laboratory tests, vital signs, concomitant medications, procedures, adverse events, and medical history" — presented uniformly, as a single class of objects.

## 2. What the Data Actually Shows

When you flatten and analyse the full BC and DSS content, a different picture emerges. The BC→DSS relationship means fundamentally different things depending on which domain you are in.

In **LB**, a BC like Glucose fans out into 8 DSSs decomposed by specimen and result scale. Each DSS carries a distinct LOINC code, units, and method — a complete measurement specification. The DSS adds operational specificity to the concept.

In **QS/FT**, each BC is a single question within a standardised instrument (EQ-5D-5L, ADAS-Cog), mapping 1:1 to its DSS. The DSS adds almost nothing. The value is in the BC hierarchy — instrument → subscale → question — not in the implementation layer.

In **IS**, 7 BCs explode into 290 DSSs. The fan-out is not by specimen (constant: SERUM/PLASMA/BLOOD) but by target antigen — 46 different allergens for IgE alone, times quantitative/qualitative pairs. The target identity is encoded in the DS_Code mnemonic but does not exist as a separate column in the model.

In **MH**, 1 BC produces 11 DSSs — free text format, prespecified format, and 9 disease-specific conditions (Alzheimer's, Essential Tremor, Visual Hallucinations). These are not measurement variants. They are protocol decisions about which conditions to pre-populate in the CRF.

In **EG**, 33 BCs map 1:1 to their DSSs, all marked Qualitative — despite ECG being inherently quantitative measurements. 18 DSSs have units populated despite the Qualitative scale.

The model schema is the same in every case. The semantics are not.

## 3. The Behavioural Gap

The COSMoS model describes **structure** (BC has attributes, DSS has variables and value-level metadata) but not **behaviour** (what the BC→DSS relationship means for a given domain, what decomposition axes apply, what a consumer should expect from the data).

This is not a criticism — it is a consequence of a generic, flexible model. But it means that consumers of COSMoS data need a behavioural layer to use it effectively. Without understanding that LB decomposes by specimen while IS decomposes by target, a consumer treats both as "Findings with fan-out" and builds the wrong file structure, the wrong mapping logic, or the wrong query.

The cdisc-for-ai project addresses this gap by making the behavioural patterns explicit — classifying domains by how they actually behave, not just by their observation class.

---

## 4. Ten Behavioural Groups

Analysis of BC-to-DSS ratios, decomposition axes, and column population patterns reveals ten distinct behavioural groups across the 31 COSMoS domains. The groups differ in what a row represents, which columns carry information, and what consumer file structure is appropriate.

| Behavioural Group | Domains | What a Row Represents | Primary Axis | Consumer File Shape |
|---|---|---|---|---|
| Specimen Findings | LB, MB, MI, CP, BS | One measurement spec: TESTCD at a specific specimen × scale | Specimen | Two sheets: Test_Identity + Measurement_Specs. Implemented. |
| Immunogenicity Findings | IS | One antibody class × target antigen × scale | Target/Analyte | Needs own structure. Target not a separate COSMoS column. |
| Genomics Findings | GF | One genomics assessment by scale and method | Result Scale | Could use two-sheet but different primary axis than LB. |
| Measurement Findings | VS, EG, MK, CV | One subject-level measurement. VS has location variants. | Location (VS only) | Single sheet. Location/laterality as optional columns. |
| Instrument Findings | QS, FT, RS | One question/item within a standardised instrument | Hierarchy (grouping) | Single sheet with hierarchy columns. |
| Domain-specific Findings | DD, RP, SC, SR, UR | One domain-specific assessment, no decomposition | None (1:1) | Single sheet. Coverage value only. |
| Clinical Assessment | FA, TR, TU, IE | One finding about an event/intervention/tumour | Method (TR/TU) | Single sheet. Needs RELREC context for full value. |
| Events | AE, DS, MH, BE, ... | One event type or prespecified variant | Context/Prespecified | Single sheet. Protocol-driven variants. |
| Interventions | CM, EX, PR, SU, ... | One intervention type or substance/procedure subtype | Context/Subtype | Single sheet. Protocol-driven specialisation. |
| Trial Design | TS | One study-level parameter (BC_Scope=Study) | None | Out of scope for subject-level files. |

---

## 5. Six Decomposition Axes

Not all fan-out is the same. Six distinct axes drive BC-to-DSS decomposition, each with different architectural implications for consumer files.

| Axis | Active In | What It Means |
|---|---|---|
| Specimen | LB (primary, 27 BCs), MB, MI, GF (NCIt-encoded) | Same TESTCD measured in different body fluids or tissues. Each variant can have different LOINC, units, and clinical interpretation. |
| Result Scale | GF (primary, 8 BCs), LB (secondary, 9 BCs), IS | Same measurement as quantitative value vs qualitative interpretation. |
| Method | GF (secondary), MB, MI, TR, TU, MK, SR | Same measurement by different analytical techniques. NOT a decomposition driver in LB (0 of 93 BCs). |
| Target/Analyte | IS only | Same antibody class against different antigens. Encoded in DS_Code mnemonic, not a separate column. Creates up to 92:1 fan-out. |
| Location/Laterality | VS (4 BCs), MK (1 BC) | Same measurement at different body sites or sides. Different from Specimen — where on the body, not what sample. |
| Context/Prespecified | MH, SU, CM, PR, AE, RS | Protocol-driven specialisation: which conditions, substances, or criteria systems to collect. |

The first five axes answer **"how is this measured?"** — they decompose a concept into operational measurement specifications. The sixth axis answers **"what does the protocol care about?"** — it encodes study design decisions, not measurement variability.

---

## 6. Findings Domains in Detail

The Findings observation class contains 22 of the 31 COSMoS domains and accounts for the majority of BCs and DSSs. It is also where the behavioural differences are most pronounced — six of the ten behavioural groups are Findings subgroups.

### Specimen Findings — validated scope

The Specimen_Findings.xlsx consumer file covers domains where specimen is the structural decomposition axis. Two-sheet structure: Test_Identity (one row per TESTCD with NCIt identity and categories) and Measurement_Specs (one row per specimen × scale variant with LOINC and units). TESTCD links the two sheets.

**LB (Laboratory)** — 93 BCs, 142 DSSs. The core case. 30 BCs fan out, driven by specimen (27 BCs) and scale (9 BCs). Method is NOT a decomposition driver (0 BCs) despite being populated on 4 DSSs. LOINC on 135 of 142 DSSs.

**MB (Microbiology Specimen)** — 6 BCs, 7 DSSs. 1 BC fans out. All DSSs have specimen and method. 3 have LOINC. Sparse but structurally identical to LB.

**MI (Microscopic Findings)** — 3 BCs, 7 DSSs. 2 BCs fan out. All DSSs have specimen and method. No LOINC. All qualitative.

**CP, BS** — In SDTM CT (Test_Identity rows from green track) but no COSMoS DSSs yet. Sheet 1 only.

**Known edge cases:** 5 LB BCs (HEIGHT, WEIGHT, INTP, MICROCY, HCG) have TESTCD_NCIt ≠ BC NCIt_Code — legacy pre-COSMoS NCIt assignments, structurally correct, flagged as QC-14. Only 4 of 142 LB DSSs have method populated — method is metadata for LB, not a decomposition axis.

### Excluded from Specimen Findings — and why

**IS (Immunogenicity)** — Target-driven, not specimen-driven. 7 BCs → 290 DSSs. Specimen is constant (SERUM/PLASMA/BLOOD). Fan-out by antigen/allergen target, up to 92:1 for IgE. Allergen-induced IgE has 46 targets × quant/qual pairs plus RAST score variants. The target identity is encoded in the DS_Code mnemonic (e.g., ARIGEABACA = Allergen-induced IgE Antibody for American Cockroach Antigen) but not available as a separate filterable column. A consumer file would need to extract target as an explicit column. All 290 DSSs have specimen and method. 185 have units. No LOINC.

**GF (Genomics)** — Scale-driven, not specimen-driven. All 10 BCs fan out (max 6:1). Scale is the primary decomposition axis (8 BCs), method secondary (3 BCs). Specimen is encoded as NCIt codes (C449, C812) rather than controlled terminology terms, unlike every other specimen-based domain — a legacy convention. Only 1 of 38 DSSs has units. No LOINC codes.

**UR (Urinalysis)** — Zero decomposition. 10 BCs, all 1:1 with DSS. Single specimen value (URINE) on 1 row, single method (MRI) on 1 row. No LOINC, no units. Classified as Specimen-based in SDTM but behaviourally identical to Domain-specific Findings.

### Measurement Findings

Subject-level measurements without specimen decomposition. Single-sheet consumer file with location/laterality as optional columns.

**VS (Vital Signs)** — 12 BCs, 16 DSSs. 4 BCs fan out via _EXT variants (SYSBP/DIABP/PULSE/HR) adding location (7 arteries) and laterality (LEFT/RIGHT). 8 BCs remain 1:1. Method on 1 DSS only. 8 have units. No LOINC. The _EXT pattern is about where on the body, not what sample — a fundamentally different axis from specimen.

**EG (ECG)** — 33 BCs, all 1:1. All marked Qualitative — unexpected for ECG which produces quantitative interval/amplitude measurements. 18 DSSs have units despite the Qualitative scale. No LOINC. This may be a COSMoS modelling choice (ECG interpretations are qualitative assessments of quantitative data) or a data artefact worth verifying.

**MK (Musculoskeletal)** — 49 BCs, 50 DSSs. 1 BC fans out (Sharp Genant joint scoring: foot joints vs hand joints — anatomical location decomposition). 14 have method. 20 have units. No LOINC.

### Instrument Findings

Standardised instruments where the BC hierarchy (instrument → subscale → question) is the structural contribution, not measurement decomposition. Single-sheet consumer file with hierarchy columns.

**QS (Questionnaires)** — 17 BCs, all 1:1. Hierarchy depth 2–3. Instruments: CES, EQ-5D-5L, TTS. 16 qualitative, 1 quantitative. 1 has method. No LOINC.

**FT (Functional Tests)** — 23 BCs, all 1:1. Hierarchy depth 3. Instruments: 6MWT, ADAS-Cog. All quantitative. 7 have units. No LOINC.

**RS (Disease Response)** — 129 BCs, 135 DSSs. 4 BCs fan out by response criteria system: Overall Response, Target Response, Non-Target Response, and New Lesion Indicator each have RECIST 1.1 / Lugano / RANO variants. Hierarchy depth 1–3. Many parent instruments (AIMS, APACHE II, ATLAS, BPRS, etc.). 132 qualitative. This is the only instrument domain with meaningful fan-out.

### Domain-specific Findings

Flat 1:1 domains. No decomposition. Consumer value is domain coverage — knowing what BCs exist.

**RP (Reproductive System)** — 96 BCs, all 1:1. Largest flat Findings domain. 34 quantitative, 55 qualitative. 8 have units.

**DD (Death Details)** — 13 BCs, all 1:1. 1 quantitative, 12 qualitative.

**SR (Skin Response)** — 12 BCs, all 1:1. 3 have method. 6 quantitative, 6 qualitative.

**SC (Subject Characteristics)** — 2 BCs, all 1:1.

**UR (Urinalysis)** — 10 BCs, all 1:1. Classified as Specimen-based but behaviourally flat (see exclusion rationale above).

### Clinical Assessment Findings

Findings about events, interventions, or tumours. Cross-domain links via RELREC. Standalone consumer file has limited utility without linked parent records.

**FA (Findings About)** — 12 BCs, 1:1. 2 have method. All qualitative.

**TR (Tumor/Lesion Results)** — 4 BCs → 9 DSSs. All have method. Fan-out by method and anatomical context. 4 have units. 2 quantitative, 7 qualitative.

**TU (Tumor/Lesion Identification)** — 5 BCs → 10 DSSs. 6 have method. All qualitative.

**IE (Inclusion/Exclusion)** — 2 BCs, 1:1. All qualitative.

---

## 7. Non-Findings Groups

### Events

BCs model event types. Where prespecified variants exist, they represent protocol-driven choices.

**MH (Medical History)** — 1 BC → 11 DSSs. Free text + prespecified + 9 disease-specific conditions (Alzheimer's, Essential Tremor, Visual Hallucinations, etc.). The protocol decides which conditions to pre-populate.

**AE (Adverse Events)** — 1 BC → 2 DSSs. Free text format + prespecified format.

**DS (Disposition)** — 18 BCs, all 1:1. Disposition event types.

**BE (Biospecimen Events)** — 7 BCs, all 1:1.

### Interventions

Fan-out by substance types, procedure body regions, or protocol specialisations.

**SU (Substance Use)** — 3 BCs → 12 DSSs. Alcohol → Beer/Wine/Spirits. Caffeine → Coffee/Cola/Tea. Tobacco → Cigarette/Cigar/Pipe.

**CM (Concomitant Medications)** — 1 BC → 4 DSSs. Free text + prespecified + 2 disease-specific variants (breast cancer, prior cancer).

**PR (Procedures)** — 4 BCs → 8 DSSs. Each modality has general + region variant: CT → Chest CT, MRI → Brain MRI, X-Ray → Chest X-Ray, Radiation → Breast Cancer Radiation.

**EC (Exposure as Collected)** — 1 BC → 2 DSSs. Treatment name + study-specific variant.

**EX (Exposure)** — 1 BC, 1 DSS. Flat.

### Special-Purpose and Trial Design

**DM (Demographics)** — 5 BCs, 1:1. Fixed demographic attributes.

**TS (Trial Summary)** — 128 BCs → 129 DSSs. Study-level metadata (SPONSOR, ACTSUB, SENDTC, etc.). BC_Scope = Study. Excluded from subject-level consumer files.

---

## 8. 194 BCs Without Dataset Specializations

194 BCs have no DSS at all (BC_Type = full_no_ds). These are predominantly parent-level grouping concepts — instruments, assessment classifications, functional test definitions — with Ordinal result scale (122 of 194). They provide hierarchy structure but no operational specifications. 173 have Hierarchy_Path values, confirming their role as grouping nodes rather than leaf-level observations.

---

## 9. Summary

The COSMoS model provides a correct, intentionally generic schema for Biomedical Concepts and Dataset Specializations. One BC class and one DSS class serve all 31 SDTM domains. This generality enables flexibility and extensibility to future standards.

But the uniform schema masks significant behavioural differences. The BC→DSS relationship means measurement decomposition in LB, hierarchy grouping in QS, target explosion in IS, and protocol-driven specialisation in MH. Consumers of COSMoS data — whether human or machine — need to understand these patterns to build the right file structures, the right mapping logic, and the right queries.

This analysis identifies ten behavioural groups, six decomposition axes, and a fundamental distinction between measurement fan-out ("how is this measured?") and context fan-out ("what does the protocol care about?"). The contribution of the cdisc-for-ai project is making these patterns visible and machine-actionable — not by changing the COSMoS model, but by adding the behavioural layer that consumers need to use it effectively.
