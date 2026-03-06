# SDTM CT Category Discovery — Step 1 Output

**Input:** NCI EVS SDTM Terminology (tab-delimited text)  
**Codelist headers analyzed:** 1,181  
**Full file rows:** 46,011  
**Analysis date:** 2026-03-06  

---

## Section 1 — Category Definitions

Categories discovered inductively from codelist names, definitions, extensibility flags, and submission value patterns. No pre-defined taxonomy was used.

```
Category name: INSTRUMENT_TC_TN
Definition: Paired test code / test name codelists for scored instruments — questionnaires, clinical classification scales, and functional tests.
Structural signature: Submission value ends TC or TN; name contains "Questionnaire", "Clinical Classification", or "Functional Test"; extensible=No.
Count: 706
```

```
Category name: INSTRUMENT_ITEM_RESPONSE
Definition: Fixed enumeration of allowed values for individual items within a scored instrument (ORRES and STRESC value sets).
Structural signature: Submission value ends OR or STR; name contains "ORRES for…TN/TC" or "STRESC for…TN/TC"; extensible=No.
Count: 158
```

```
Category name: MEASUREMENT_TEST_CODE
Definition: Open, extensible test code and test name codelists for continuous or categorical measurement domains — lab, vitals, physiologic exams, findings about, genomic, PK, microbiology, device properties, and related parameter lists.
Structural signature: Name contains "Test Code", "Test Name", "Parameter Code", "Parameter Name", "Dictionary Derived Term", "Analytical Method", or "Test Detail"; extensible=Yes.
Count: 140
```

```
Category name: RESULT_VALUE_SET
Definition: Enumerated allowed values for result or response variables — grades, classifications, status responses, outcome enumerations.
Structural signature: Name ends with "Response", "Responses", "Result", "Results", "Status", "Outcome", "Grade", "Classification", "Type", "Index", or "Complexity"; extensible varies (mostly No for fixed scales, Yes for open response lists).
Count: 109
```

```
Category name: ADMINISTRATION_LOGISTICS
Definition: Codelists governing process, workflow, and logistics of study conduct — routes, dosage forms, frequencies, treatment settings, completion status, contact roles.
Structural signature: Name contains "Route of Administration", "Dosage Form", "Frequency", "Completion", "Reason For Treatment", "Treatment", "Mode of", "Evaluator", "Contact Role", or "Reference Range Indicator"; extensible varies.
Count: 21
```

```
Category name: REFERENCE_VOCABULARY
Definition: Large open enumerations of external scientific or anatomical nomenclature — microorganism names, anatomical locations, procedures, specimen types, taxonomic parameters.
Structural signature: Name contains "Microorganism", "Anatomical Location", "Procedure", "Specimen Type", "Specimen Condition", "Directionality", "Laterality", "Portion/Totality", or "Position"; extensible=Yes; typically very large term sets.
Count: 13
```

```
Category name: DOMAIN_GROUPING
Definition: Category and subcategory codelists used to group observations within SDTM domains (QSCAT, FTCAT, DSCAT, etc.).
Structural signature: Name starts with "Category of", "Category for", or "Subcategory for"; extensible varies.
Count: 11
```

```
Category name: UNIT
Definition: Units of measure — general, domain-specific, and PK-normalized variants.
Structural signature: Name contains "Unit" or submission value is UNIT, AGEU, VSRESU, or starts with PK Units; extensible=Yes.
Count: 7
```

```
Category name: SUBJECT_CHARACTERISTIC
Definition: Fixed-value demographic and identity attribute codelists — sex, race, ethnicity, employment, marital status, gender identity.
Structural signature: Name contains "Sex", "Race", "Ethnic", "Employment Status", "Marital Status", "Relationship to Subject", "Gender Identity", "Sexual Orientation", "Never/Current/Former", "Menopause Status", "Fitzpatrick Skin", or "Skin Type".
Count: 6
```

```
Category name: TRIAL_DESIGN
Definition: Codelists describing study design parameters, regulatory metadata, and SDTM version identifiers.
Structural signature: Name contains "Trial Blinding", "Trial Intent", "Trial Phase", "Trial Type", "Trial Summary", "Intervention Model", "Control Type", "Observational Study", "Protocol Milestone", "Epoch", "SDTM Version", "CDISC Therapeutic Area", or "FDA Technical Specification".
Count: 5
```

```
Category name: ASSAY_AND_PROCESS_METADATA
Definition: Codelists describing configuration metadata for assays and instruments — binding agents, device identifier parameter names, test operational objectives.
Structural signature: Name contains "Binding Agent", "Device Identifier", or "Test Operational Objective"; extensible varies; small codelists.
Count: 4
```

```
Category name: GENERAL_FLAG
Definition: Cross-domain binary or near-binary flag codelists used wherever a simple indicator is needed (No/Yes/Unknown, Not Done, Normal/Abnormal).
Structural signature: Name is "No Yes Response", "Not Done", or "Normal Abnormal Response"; extensible=No; very small term sets (2–4 terms).
Count: 1
```

---

## Section 2 — Full Assignment Table

See companion file: `SDTM_CT_Category_Discovery_assignments.csv`

Columns: `Code`, `CDISC_Submission_Value`, `Codelist_Name`, `Codelist_Extensible`, `Assigned_Category`, `Confidence`, `Note`

Summary:
- HIGH confidence: 1,092 (92.5%)
- MEDIUM confidence: 89 (7.5%)
- LOW confidence: 0

The MEDIUM confidence cases fall into three patterns:
1. Extensible result value sets where the open-ended nature creates semantic overlap with MEASUREMENT_TEST_CODE (e.g., ONCRSR, HESTRESC, LBSTRESC)
2. Method and process qualifier codelists (METHOD, QRSMTHOD) that could belong to either MEASUREMENT_TEST_CODE or ASSAY_AND_PROCESS_METADATA
3. General flag codelists (NY, ND, NORMABNM, NRIND) that are cross-domain utilities not clearly in any category

---

## Section 3 — Structural Observations

**1. Which categories were easiest to identify and why?**

INSTRUMENT_TC_TN and INSTRUMENT_ITEM_RESPONSE were trivially identifiable: the naming convention is completely systematic (suffix TC/TN/OR/STR, instrument name in the codelist name, extensible=No), leaving no ambiguity for the 864 codelists in these two categories.

**2. Which codelists were hardest to assign — and what caused the ambiguity?**

The result-vs-measurement boundary was the main source of ambiguity: codelists like LBSTRESC, ONCRSR, HESTRESC, and EGSTRESC are extensible=Yes result value sets whose definitions describe "standardized character results," placing them structurally between RESULT_VALUE_SET (they are values for a result field) and MEASUREMENT_TEST_CODE (they are open extensible vocabularies used as test-domain companions).

**3. Did any codelists appear to belong to two categories?**

Yes — LBSTRESC, ONCRSR, EGSTRESC, MSSTRESC, and HESTRESC straddle RESULT_VALUE_SET and MEASUREMENT_TEST_CODE: they are extensible=Yes result value enumerations that co-occur with domain test code codelists and are consumed as a unit by the same downstream systems, yet their semantic role is "allowed result values" not "test identifiers."

**4. What structure is present but invisible in the flat format — what must a consumer infer?**

The TC/TN pairing relationship is invisible: a consuming system must infer that LBTESTCD and LBTEST are two views of the same set, that each instrument's TC/TN pair is co-dependent, and that ORRES/STRESC codelists for a given instrument item are the allowed-values complement to that instrument's TC/TN pair. None of these relationships are encoded in any column; they must be reconstructed from naming conventions alone.

**5. Are there codelists whose machine-actionability differs fundamentally from others in the same category?**

Within MEASUREMENT_TEST_CODE, LBTESTCD (2,475 terms) and MBTESTCD (556 terms) are far larger than domain-specific test code codelists (e.g., CVTESTCD ~190 terms, VSTESTCD ~76 terms), meaning lookup behavior, collision risk, and matching complexity differ substantially despite identical structural category assignment. Within RESULT_VALUE_SET, closed single-domain grades (AJCCGRD, 5 terms) behave completely differently from open extensible multi-domain response lists (LOC — Anatomical Location, classified as REFERENCE_VOCABULARY — but similar open codelists in RESULT_VALUE_SET like SEVRS, 5 terms).

---

## Section 4 — What would refine this

- **CDISC SDTM IG variable binding table**: Would resolve which codelists are bound to specific SDTM variables (TESTCD, TEST, ORRES, STRESC, QSCAT, etc.) — eliminating the TC/TN/ORRES inference ambiguity and making the pairing relationship explicit.
- **NCI EVS concept hierarchy for C-codes**: Would allow identification of parent-child relationships between codelists (e.g., FATESTCD as a parent class with disease-specific FA codelists as children) — currently invisible in the flat file.
- **Term count per codelist**: Would allow separation of large reference vocabularies (MICROORG, LOC, LBTESTCD) from structurally similar but small enumerations within REFERENCE_VOCABULARY and MEASUREMENT_TEST_CODE, enabling machine-actionability ranking within categories.
