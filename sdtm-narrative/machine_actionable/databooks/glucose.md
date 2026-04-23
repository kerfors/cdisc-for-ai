# Glucose — COSMoS DataBook

*BC `C105585` — Glucose Measurement.*
*Generated from `COSMoS_Graph.xlsx` via the template catalogue under `sdtm-narrative/reference/templates/`.*

---

## BC opener

**Glucose Measurement** (C105585) is a *full* biomedical concept in the Laboratory Tests;Chemistry Tests category. It realises 8 dataset specialisations, all in domain `LB` — a specimen-based-findings pattern.

*Definition.* The determination of the amount of glucose present in a sample.

*Result scales available.* Quantitative;Ordinal

---


## DSS `GLUCBLD` — Glucose Concentration in Blood

The **Glucose Concentration in Blood** specialisation (`GLUCBLD`) realises the **Glucose Measurement** biomedical concept as a LB-domain row template. It pins `LBTESTCD = GLUC`. Added to SDTMIG in 3-2.

### Variables (Template 01 band 3a)

| Variable | Natural name | Role | Pinned value | Codelist | Value list |
|---|---|---|---|---|---|
| `LBTESTCD` | Laboratory Test Code | Topic | GLUC | LBTESTCD |  |
| `LBTEST` | Laboratory Test Name | Qualifier | Glucose | LBTEST |  |
| `LBCAT` | Laboratory Test Category | Qualifier | CHEMISTRY |  |  |
| `LBORRES` | Laboratory Test Original Result | Qualifier |  |  |  |
| `LBORRESU` | Laboratory Test Original Result Unit | Qualifier |  | UNIT | mg/dL;mmol/L |
| `LBSTRESC` | Laboratory Test Character Result in Standard Unit | Qualifier |  |  |  |
| `LBSTRESN` | Laboratory Test Numeric Result in Standard Unit | Qualifier |  |  |  |
| `LBSTRESU` | Laboratory Test Result Standard Unit | Qualifier | mmol/L | UNIT |  |
| `LBLOINC` | Laboratory Test LOINC Code | Qualifier |  |  | 2339-0;15074-8 |
| `LBSPEC` | Laboratory Specimen Type | Qualifier | BLOOD | SPECTYPE |  |
| `LBMETHOD` | Laboratory Test Method | Qualifier |  | METHOD |  |
| `LBFAST` | Laboratory Test Fasting Status | Qualifier |  | NY | N;Y |
| `LBDTC` | Laboratory Test Collection Date Time | Timing |  |  |  |

### Measurement-spec attributes (band 3a)

| Attribute | Value |
|---|---|
| Specimen | **BLOOD** *(pinned)* |
| Method | open, codelist `METHOD` |
| Category | **CHEMISTRY** *(pinned)* |
| Orig Unit | open, constrained to `mg/dL;mmol/L` |
| Std Unit | **mmol/L** *(pinned)* |
| Fast | open, constrained to `N;Y` |
| Loinc | open, constrained to `2339-0;15074-8` |

### Flattened row (band 4 stub)

*Flattened row (band 4) — stub rendering from graph; the
`COSMoS_Graph_Flat.xlsx` round-trip file is not yet produced.*

| Field | Value |
|---|---|
| BC_ID | C105585 |
| BC_short_name | Glucose Measurement |
| BC_definition | The determination of the amount of glucose present in a sample. |
| BC_categories | Laboratory Tests;Chemistry Tests |
| BC_type | full |
| result_scales | Quantitative;Ordinal |
| DS_Code | GLUCBLD |
| DS_short_name | Glucose Concentration in Blood |
| Domain | LB |
| sdtmig_since | 3-2 |

## DSS `GLUCPE` — Plasma Equivalent Glucose

The **Plasma Equivalent Glucose** specialisation (`GLUCPE`) realises the **Glucose Measurement** biomedical concept as a LB-domain row template. It pins `LBTESTCD = GLUCPE`. Added to SDTMIG in 3-2.

### Variables (Template 01 band 3a)

| Variable | Natural name | Role | Pinned value | Codelist | Value list |
|---|---|---|---|---|---|
| `LBTESTCD` | Laboratory Test Code | Topic | GLUCPE | LBTESTCD |  |
| `LBTEST` | Laboratory Test Name | Qualifier | Plasma Equivalent Glucose | LBTEST |  |
| `LBCAT` | Laboratory Test Category | Qualifier | CHEMISTRY |  |  |
| `LBORRES` | Laboratory Test Original Result | Qualifier |  |  |  |
| `LBORRESU` | Laboratory Test Original Result Unit | Qualifier |  | UNIT | mg/dL;g/L;mmol/L |
| `LBSTRESC` | Laboratory Test Character Result in Standard Unit | Qualifier |  |  |  |
| `LBSTRESN` | Laboratory Test Numeric Result in Standard Unit | Qualifier |  |  |  |
| `LBSTRESU` | Laboratory Test Result Standard Unit | Qualifier | mmol/L | UNIT |  |
| `LBLOINC` | Laboratory Test LOINC Code | Qualifier |  |  | 99504-3;105272-9 |
| `LBSPEC` | Laboratory Specimen Type | Qualifier | INTERSTITIAL FLUID | SPECTYPE |  |
| `LBMETHOD` | Laboratory Test Method | Qualifier |  | METHOD |  |
| `LBFAST` | Laboratory Test Fasting Status | Qualifier |  | NY | N;Y |
| `LBDTC` | Laboratory Test Collection Date Time | Timing |  |  |  |

### Measurement-spec attributes (band 3a)

| Attribute | Value |
|---|---|
| Specimen | **INTERSTITIAL FLUID** *(pinned)* |
| Method | open, codelist `METHOD` |
| Category | **CHEMISTRY** *(pinned)* |
| Orig Unit | open, constrained to `mg/dL;g/L;mmol/L` |
| Std Unit | **mmol/L** *(pinned)* |
| Fast | open, constrained to `N;Y` |
| Loinc | open, constrained to `99504-3;105272-9` |

### Flattened row (band 4 stub)

*Flattened row (band 4) — stub rendering from graph; the
`COSMoS_Graph_Flat.xlsx` round-trip file is not yet produced.*

| Field | Value |
|---|---|
| BC_ID | C105585 |
| BC_short_name | Glucose Measurement |
| BC_definition | The determination of the amount of glucose present in a sample. |
| BC_categories | Laboratory Tests;Chemistry Tests |
| BC_type | full |
| result_scales | Quantitative;Ordinal |
| DS_Code | GLUCPE |
| DS_short_name | Plasma Equivalent Glucose |
| Domain | LB |
| sdtmig_since | 3-2 |

## DSS `GLUCPL` — Glucose Concentration in Plasma

The **Glucose Concentration in Plasma** specialisation (`GLUCPL`) realises the **Glucose Measurement** biomedical concept as a LB-domain row template. It pins `LBTESTCD = GLUC`. Added to SDTMIG in 3-2.

### Variables (Template 01 band 3a)

| Variable | Natural name | Role | Pinned value | Codelist | Value list |
|---|---|---|---|---|---|
| `LBTESTCD` | Laboratory Test Code | Topic | GLUC | LBTESTCD |  |
| `LBTEST` | Laboratory Test Name | Qualifier | Glucose | LBTEST |  |
| `LBCAT` | Laboratory Test Category | Qualifier | CHEMISTRY |  |  |
| `LBORRES` | Laboratory Test Original Result | Qualifier |  |  |  |
| `LBORRESU` | Laboratory Test Original Result Unit | Qualifier |  | UNIT | mg/dL;g/L;mmol/L |
| `LBSTRESC` | Laboratory Test Character Result in Standard Unit | Qualifier |  |  |  |
| `LBSTRESN` | Laboratory Test Numeric Result in Standard Unit | Qualifier |  |  |  |
| `LBSTRESU` | Laboratory Test Result Standard Unit | Qualifier | mmol/L | UNIT |  |
| `LBLOINC` | Laboratory Test LOINC Code | Qualifier |  |  |  |
| `LBSPEC` | Laboratory Specimen Type | Qualifier | PLASMA | SPECTYPE |  |
| `LBFAST` | Laboratory Test Fasting Status | Qualifier |  | NY | N;Y |
| `LBDTC` | Laboratory Test Collection Date Time | Timing |  |  |  |

### Measurement-spec attributes (band 3a)

| Attribute | Value |
|---|---|
| Specimen | **PLASMA** *(pinned)* |
| Category | **CHEMISTRY** *(pinned)* |
| Orig Unit | open, constrained to `mg/dL;g/L;mmol/L` |
| Std Unit | **mmol/L** *(pinned)* |
| Fast | open, constrained to `N;Y` |
| Loinc | open |

### Case specialisations refining this DSS (Template 04)

#### Case specialisation — ID001: Fasting Plasma Glucose (FPG)

Parent DSS: `GLUCPL`  
Case type: recording-child  

**Inside-DSS pinning (overlay on parent):**
- `LBFAST` = **Y** — pinned on a slot the DSS already reserves

Rationale: Fasting sample carries the clinical diagnostic intent

*Source: `docs/Glucose_StudyIntent_Story.html`*

#### Case specialisation — ID002: OGTT 2-Hour Plasma Glucose

Parent DSS: `GLUCPL`  
Case type: recording-child  
Composes with: OGTT 75g oral challenge (SoA-scheduling parent, study-design object)  

**Inside-DSS pinning (overlay on parent):**
- `LBFAST` = **N** — post-challenge sample

Rationale: Post-challenge sample under OGTT 75g protocol

*Source: `docs/Glucose_StudyIntent_Story.html`*

#### Case specialisation — ID003: OGTT Fasting (Pre-Challenge) Plasma Glucose

Parent DSS: `GLUCPL`  
Case type: recording-child  
Composes with: OGTT 75g oral challenge (same SoA-scheduling parent as ID002)  

**Inside-DSS pinning (overlay on parent):**
- `LBFAST` = **Y** — pre-challenge baseline

Rationale: Pre-challenge baseline under OGTT 75g protocol

*Source: `docs/Glucose_StudyIntent_Story.html`*

### Flattened row (band 4 stub)

*Flattened row (band 4) — stub rendering from graph; the
`COSMoS_Graph_Flat.xlsx` round-trip file is not yet produced.*

| Field | Value |
|---|---|
| BC_ID | C105585 |
| BC_short_name | Glucose Measurement |
| BC_definition | The determination of the amount of glucose present in a sample. |
| BC_categories | Laboratory Tests;Chemistry Tests |
| BC_type | full |
| result_scales | Quantitative;Ordinal |
| DS_Code | GLUCPL |
| DS_short_name | Glucose Concentration in Plasma |
| Domain | LB |
| sdtmig_since | 3-2 |

## DSS `GLUCSER` — Glucose Concentration in Serum

The **Glucose Concentration in Serum** specialisation (`GLUCSER`) realises the **Glucose Measurement** biomedical concept as a LB-domain row template. It pins `LBTESTCD = GLUC`. Added to SDTMIG in 3-2.

### Variables (Template 01 band 3a)

| Variable | Natural name | Role | Pinned value | Codelist | Value list |
|---|---|---|---|---|---|
| `LBTESTCD` | Laboratory Test Code | Topic | GLUC | LBTESTCD |  |
| `LBTEST` | Laboratory Test Name | Qualifier | Glucose | LBTEST |  |
| `LBCAT` | Laboratory Test Category | Qualifier | CHEMISTRY |  |  |
| `LBORRES` | Laboratory Test Original Result | Qualifier |  |  |  |
| `LBORRESU` | Laboratory Test Original Result Unit | Qualifier |  | UNIT | mg/dL;g/L;mmol/L |
| `LBSTRESC` | Laboratory Test Character Result in Standard Unit | Qualifier |  |  |  |
| `LBSTRESN` | Laboratory Test Numeric Result in Standard Unit | Qualifier |  |  |  |
| `LBSTRESU` | Laboratory Test Result Standard Unit | Qualifier | mmol/L | UNIT |  |
| `LBLOINC` | Laboratory Test LOINC Code | Qualifier |  |  |  |
| `LBSPEC` | Laboratory Specimen Type | Qualifier | SERUM | SPECTYPE |  |
| `LBFAST` | Laboratory Test Fasting Status | Qualifier |  | NY | N;Y |
| `LBDTC` | Laboratory Test Collection Date Time | Timing |  |  |  |

### Measurement-spec attributes (band 3a)

| Attribute | Value |
|---|---|
| Specimen | **SERUM** *(pinned)* |
| Category | **CHEMISTRY** *(pinned)* |
| Orig Unit | open, constrained to `mg/dL;g/L;mmol/L` |
| Std Unit | **mmol/L** *(pinned)* |
| Fast | open, constrained to `N;Y` |
| Loinc | open |

### Flattened row (band 4 stub)

*Flattened row (band 4) — stub rendering from graph; the
`COSMoS_Graph_Flat.xlsx` round-trip file is not yet produced.*

| Field | Value |
|---|---|
| BC_ID | C105585 |
| BC_short_name | Glucose Measurement |
| BC_definition | The determination of the amount of glucose present in a sample. |
| BC_categories | Laboratory Tests;Chemistry Tests |
| BC_type | full |
| result_scales | Quantitative;Ordinal |
| DS_Code | GLUCSER |
| DS_short_name | Glucose Concentration in Serum |
| Domain | LB |
| sdtmig_since | 3-2 |

## DSS `GLUCSERPL` — Glucose Concentration in Serum or Plasma

The **Glucose Concentration in Serum or Plasma** specialisation (`GLUCSERPL`) realises the **Glucose Measurement** biomedical concept as a LB-domain row template. It pins `LBTESTCD = GLUC`. Added to SDTMIG in 3-2.

### Variables (Template 01 band 3a)

| Variable | Natural name | Role | Pinned value | Codelist | Value list |
|---|---|---|---|---|---|
| `LBTESTCD` | Laboratory Test Code | Topic | GLUC | LBTESTCD |  |
| `LBTEST` | Laboratory Test Name | Qualifier | Glucose | LBTEST |  |
| `LBCAT` | Laboratory Test Category | Qualifier | CHEMISTRY |  |  |
| `LBORRES` | Laboratory Test Original Result | Qualifier |  |  |  |
| `LBORRESU` | Laboratory Test Original Result Unit | Qualifier |  | UNIT | mg/dL;g/L;mmol/L |
| `LBSTRESC` | Laboratory Test Character Result in Standard Unit | Qualifier |  |  |  |
| `LBSTRESN` | Laboratory Test Numeric Result in Standard Unit | Qualifier |  |  |  |
| `LBSTRESU` | Laboratory Test Result Standard Unit | Qualifier | mmol/L | UNIT |  |
| `LBLOINC` | Laboratory Test LOINC Code | Qualifier |  |  | 14749-6;2345-7 |
| `LBSPEC` | Laboratory Specimen Type | Qualifier | SERUM | SPECTYPE |  |
| `LBFAST` | Laboratory Test Fasting Status | Qualifier |  | NY | N;Y |
| `LBDTC` | Laboratory Test Collection Date Time | Timing |  |  |  |

### Measurement-spec attributes (band 3a)

| Attribute | Value |
|---|---|
| Specimen | **SERUM** *(pinned)* |
| Category | **CHEMISTRY** *(pinned)* |
| Orig Unit | open, constrained to `mg/dL;g/L;mmol/L` |
| Std Unit | **mmol/L** *(pinned)* |
| Fast | open, constrained to `N;Y` |
| Loinc | open, constrained to `14749-6;2345-7` |

### Flattened row (band 4 stub)

*Flattened row (band 4) — stub rendering from graph; the
`COSMoS_Graph_Flat.xlsx` round-trip file is not yet produced.*

| Field | Value |
|---|---|
| BC_ID | C105585 |
| BC_short_name | Glucose Measurement |
| BC_definition | The determination of the amount of glucose present in a sample. |
| BC_categories | Laboratory Tests;Chemistry Tests |
| BC_type | full |
| result_scales | Quantitative;Ordinal |
| DS_Code | GLUCSERPL |
| DS_short_name | Glucose Concentration in Serum or Plasma |
| Domain | LB |
| sdtmig_since | 3-2 |

## DSS `GLUCUA` — Glucose Presence in Urine by Test Strip

The **Glucose Presence in Urine by Test Strip** specialisation (`GLUCUA`) realises the **Glucose Measurement** biomedical concept as a LB-domain row template. It pins `LBTESTCD = GLUC`. Added to SDTMIG in 3-2.

### Variables (Template 01 band 3a)

| Variable | Natural name | Role | Pinned value | Codelist | Value list |
|---|---|---|---|---|---|
| `LBTESTCD` | Laboratory Test Code | Topic | GLUC | LBTESTCD |  |
| `LBTEST` | Laboratory Test Name | Qualifier | Glucose | LBTEST |  |
| `LBCAT` | Laboratory Test Category | Qualifier | URINALYSIS |  |  |
| `LBORRES` | Laboratory Test Original Result | Qualifier |  |  |  |
| `LBSTRESC` | Laboratory Test Character Result in Standard Unit | Qualifier |  |  |  |
| `LBLOINC` | Laboratory Test LOINC Code | Qualifier | 25428-4 |  |  |
| `LBSPEC` | Laboratory Specimen Type | Qualifier | URINE | SPECTYPE |  |
| `LBMETHOD` | Laboratory Test Method | Qualifier | TEST STRIP | METHOD |  |
| `LBFAST` | Laboratory Test Fasting Status | Qualifier |  | NY | N;Y |
| `LBDTC` | Laboratory Test Collection Date Time | Timing |  |  |  |

### Measurement-spec attributes (band 3a)

| Attribute | Value |
|---|---|
| Specimen | **URINE** *(pinned)* |
| Method | **TEST STRIP** *(pinned)* |
| Category | **URINALYSIS** *(pinned)* |
| Fast | open, constrained to `N;Y` |
| Loinc | **25428-4** *(pinned)* |

### Flattened row (band 4 stub)

*Flattened row (band 4) — stub rendering from graph; the
`COSMoS_Graph_Flat.xlsx` round-trip file is not yet produced.*

| Field | Value |
|---|---|
| BC_ID | C105585 |
| BC_short_name | Glucose Measurement |
| BC_definition | The determination of the amount of glucose present in a sample. |
| BC_categories | Laboratory Tests;Chemistry Tests |
| BC_type | full |
| result_scales | Quantitative;Ordinal |
| DS_Code | GLUCUA |
| DS_short_name | Glucose Presence in Urine by Test Strip |
| Domain | LB |
| sdtmig_since | 3-2 |

## DSS `GLUCURIN` — Glucose Concentration in Urine

The **Glucose Concentration in Urine** specialisation (`GLUCURIN`) realises the **Glucose Measurement** biomedical concept as a LB-domain row template. It pins `LBTESTCD = GLUC`. Added to SDTMIG in 3-2.

### Variables (Template 01 band 3a)

| Variable | Natural name | Role | Pinned value | Codelist | Value list |
|---|---|---|---|---|---|
| `LBTESTCD` | Laboratory Test Code | Topic | GLUC | LBTESTCD |  |
| `LBTEST` | Laboratory Test Name | Qualifier | Glucose | LBTEST |  |
| `LBCAT` | Laboratory Test Category | Qualifier | CHEMISTRY |  |  |
| `LBORRES` | Laboratory Test Original Result | Qualifier |  |  |  |
| `LBORRESU` | Laboratory Test Original Result Unit | Qualifier |  | UNIT | mg/dL;mmol/L;umol/L |
| `LBSTRESC` | Laboratory Test Character Result in Standard Unit | Qualifier |  |  |  |
| `LBSTRESN` | Laboratory Test Numeric Result in Standard Unit | Qualifier |  |  |  |
| `LBSTRESU` | Laboratory Test Result Standard Unit | Qualifier | mmol/L | UNIT |  |
| `LBLOINC` | Laboratory Test LOINC Code | Qualifier |  |  | 15076-3;2350-7 |
| `LBSPEC` | Laboratory Specimen Type | Qualifier | URINE | SPECTYPE |  |
| `LBFAST` | Laboratory Test Fasting Status | Qualifier |  | NY | N;Y |
| `LBDTC` | Laboratory Test Collection Date Time | Timing |  |  |  |

### Measurement-spec attributes (band 3a)

| Attribute | Value |
|---|---|
| Specimen | **URINE** *(pinned)* |
| Category | **CHEMISTRY** *(pinned)* |
| Orig Unit | open, constrained to `mg/dL;mmol/L;umol/L` |
| Std Unit | **mmol/L** *(pinned)* |
| Fast | open, constrained to `N;Y` |
| Loinc | open, constrained to `15076-3;2350-7` |

### Flattened row (band 4 stub)

*Flattened row (band 4) — stub rendering from graph; the
`COSMoS_Graph_Flat.xlsx` round-trip file is not yet produced.*

| Field | Value |
|---|---|
| BC_ID | C105585 |
| BC_short_name | Glucose Measurement |
| BC_definition | The determination of the amount of glucose present in a sample. |
| BC_categories | Laboratory Tests;Chemistry Tests |
| BC_type | full |
| result_scales | Quantitative;Ordinal |
| DS_Code | GLUCURIN |
| DS_short_name | Glucose Concentration in Urine |
| Domain | LB |
| sdtmig_since | 3-2 |

## DSS `GLUCURINPRES` — Glucose Presence in Urine

The **Glucose Presence in Urine** specialisation (`GLUCURINPRES`) realises the **Glucose Measurement** biomedical concept as a LB-domain row template. It pins `LBTESTCD = GLUC`. Added to SDTMIG in 3-2.

### Variables (Template 01 band 3a)

| Variable | Natural name | Role | Pinned value | Codelist | Value list |
|---|---|---|---|---|---|
| `LBTESTCD` | Laboratory Test Code | Topic | GLUC | LBTESTCD |  |
| `LBTEST` | Laboratory Test Name | Qualifier | Glucose | LBTEST |  |
| `LBCAT` | Laboratory Test Category | Qualifier | URINALYSIS |  |  |
| `LBORRES` | Laboratory Test Original Result | Qualifier |  |  |  |
| `LBSTRESC` | Laboratory Test Character Result in Standard Unit | Qualifier |  |  |  |
| `LBLOINC` | Laboratory Test LOINC Code | Qualifier | 2349-9 |  |  |
| `LBSPEC` | Laboratory Specimen Type | Qualifier | URINE | SPECTYPE |  |
| `LBFAST` | Laboratory Test Fasting Status | Qualifier |  | NY | N;Y |
| `LBDTC` | Laboratory Test Collection Date Time | Timing |  |  |  |

### Measurement-spec attributes (band 3a)

| Attribute | Value |
|---|---|
| Specimen | **URINE** *(pinned)* |
| Category | **URINALYSIS** *(pinned)* |
| Fast | open, constrained to `N;Y` |
| Loinc | **2349-9** *(pinned)* |

### Flattened row (band 4 stub)

*Flattened row (band 4) — stub rendering from graph; the
`COSMoS_Graph_Flat.xlsx` round-trip file is not yet produced.*

| Field | Value |
|---|---|
| BC_ID | C105585 |
| BC_short_name | Glucose Measurement |
| BC_definition | The determination of the amount of glucose present in a sample. |
| BC_categories | Laboratory Tests;Chemistry Tests |
| BC_type | full |
| result_scales | Quantitative;Ordinal |
| DS_Code | GLUCURINPRES |
| DS_short_name | Glucose Presence in Urine |
| Domain | LB |
| sdtmig_since | 3-2 |

---

## BC-scope sibling summary

**Sibling DSSs under the same BC:**

- `GLUCBLD` — Glucose Concentration in Blood (domain LB)
- `GLUCPE` — Plasma Equivalent Glucose (domain LB)
- `GLUCPL` — Glucose Concentration in Plasma (domain LB)
- `GLUCSER` — Glucose Concentration in Serum (domain LB)
- `GLUCSERPL` — Glucose Concentration in Serum or Plasma (domain LB)
- `GLUCUA` — Glucose Presence in Urine by Test Strip (domain LB)
- `GLUCURIN` — Glucose Concentration in Urine (domain LB)
- `GLUCURINPRES` — Glucose Presence in Urine (domain LB)

> ### Registry gap — specimen-test qualification
>
> The COSMoS graph models **Glucose Measurement** at the BC level and its
> 8 specialisations at the DSS level, but does not
> carry a first-class registry of *which test–specimen–method
> combinations are clinically meaningful*. The sibling DSSs are
> the practical evidence such combinations exist; the graph
> represents them only as separate DSS rows, not as a qualified
> proposition.
>
> A registry of shape *(BC, TESTCD, specimen, method, result_scale,
> qualified_by)* would make specimen–test qualification machine-
> actionable.

> ### Registry gap — case specialisations
>
> The cases above are encoded inline in this notebook from the
> reference HTML stories. A registry of shape
> *(case_spec_id, parent_dss, case_type, composes_with, rationale,
> ext_ref)* would lift these from story prose into machine-
> actionable first-class content.
