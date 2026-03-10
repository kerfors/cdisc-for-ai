# COSMoS Flattened: Content and Quality Checks

What the [`interim/COSMoS_BC_DSS.xlsx`](../interim/COSMoS_BC_DSS.xlsx) file contains and what the QC checks found.

## What the file is

COSMoS publishes Biomedical Concepts (BCs) and Dataset Specializations (DSSs) as two separate structures. BCs define the measurement concept. DSSs operationalize it for SDTM — specifying specimen, method, result scale, units, and LOINC codes for a specific domain.

The [Flatten notebook](../notebooks/COSMoS_BC_DSS_Flatten.ipynb) combines both levels into a single flat Excel file: one row per DSS, with BC identity columns carried along. Covers all SDTM domains, not just Laboratory.

## Scope

**1,127 BCs** across 31 SDTM domains. Of these, 705 have at least one DSS. The remaining are either defined but without operational specifications (194), or structural hierarchy nodes grouping other BCs (228).

**1,123 Dataset Specializations** — the operational rows. Each specifies:

- The BC it belongs to (name, definition, NCIt code, TESTCD/TEST)
- Specimen type, method, result scale
- Allowed units and standard unit
- LOINC code(s) where available
- Domain and domain observation class (Findings, Events, Interventions)

## Glucose — example of one BC producing multiple DSSs

One BC — Glucose Measurement (C105585) — produces 8 DSSs in the LB domain:

| DS_Code | Specimen | Method | Result Scale | Units |
|---|---|---|---|---|
| GLUCSER | SERUM | — | Quantitative | mg/dL; g/L; mmol/L |
| GLUCPL | PLASMA | — | Quantitative | mg/dL; g/L; mmol/L |
| GLUCSERPL | SERUM* | — | Quantitative | mg/dL; g/L; mmol/L |
| GLUCBLD | BLOOD | — | Quantitative | mg/dL; mmol/L |
| GLUCURIN | URINE | — | Quantitative | mg/dL; mmol/L; umol/L |
| GLUCPE | INTERSTITIAL FLUID | — | Quantitative | mg/dL; g/L; mmol/L |
| GLUCUA | URINE | TEST STRIP | Qualitative | — |
| GLUCURINPRES | URINE | — | Qualitative | — |

*\*GLUCSERPL specimen is SERUM in source — flagged as QC-07; expected SERUM OR PLASMA per the naming pattern.*

*GLUCPE carries a different TESTCD_NCIt (C163446) than the parent BC's NCIt_Code (C105585) — flagged as QC-14. The remaining 7 DSSs share the BC-level NCIt code.*

## Domain distribution

| Domain | BCs | DSSs | Notable |
|---|---|---|---|
| LB (Laboratory) | 93 | 142 | All 142 have specimen; 135 have LOINC |
| IS (Immunogenicity) | 7 | 290 | Specimen-driven explosion — 7 BCs × many specimen variants |
| RS (Disease Response) | 129 | 135 | Mostly qualitative |
| TS (Trial Summary) | 128 | 129 | Special-purpose, not measurement-related |
| VS (Vital Signs) | 12 | 16 | 15 quantitative |
| EG (ECG) | 33 | 33 | All quantitative, 18 with units |

## QC findings

The [Validate notebook](../notebooks/COSMoS_BC_DSS_Validate.ipynb) runs 15 checks — structural integrity (QC-01 to QC-10) and curation principle compliance (QC-11 to QC-15). No blocking errors. Key findings:

**CT mapping gaps (QC-01, QC-02).** 4 specimen NCIt codes and 3 method terms in COSMoS could not be resolved to SDTM CT submission values. These are source-level gaps — the COSMoS export references NCIt codes that are not in the current SDTM Specimen Type or Method codelists. Unit mapping is complete.

**DSSs without TESTCD (QC-04).** 46 DSSs have no test code in the COSMoS source. These span domains like DS (Disposition), IS (Immunogenicity), DM (Demographics), and PR (Procedures) — domains where the concept may not map to a traditional TESTCD/TEST codelist pair.

**Quantitative DSSs without units (QC-06).** 106 rows classified as quantitative have no Allowed_Units. Spread across 12 domains including MK (25), RP (27), and FT (16). Some of these are genuine gaps; others may reflect early-stage curation.

**Result Scale vocabulary (QC-11a/b).** COSMoS uses "Qualitative" (491 DSSs) and "datetime" (7 DSSs) as result scale values. The [BC Curation Principles](https://cdisc-org.github.io/COSMoS/bc_starter_package/doc/BC%20Curation%20Principles%20and%20Completion%20GLs.xlsx) valid set does not include "Qualitative" (it uses "Nominal" and "Ordinal") or "datetime" (likely maps to "Temporal"). Not errors — but vocabulary alignment between COSMoS source data and the curation principles would help downstream consumers.

**Retired BCs (QC-10).** 4 BCs marked as retired are still in the export.

**Placeholder BCs (QC-12).** 6 BCs have temporary IDs (NEW_*) — NCIt codes not yet assigned.

**TESTCD_NCIt differs from NCIt_Code (QC-14).** 7 DSSs carry a TESTCD-level NCIt code that differs from the parent BC's NCIt_Code. Affected tests: HEIGHT, WEIGHT, INTP (ECG Interpretation), GLUCPE, MICROCY, LENGTH, and HCG. The TESTCD_NCIt column in the interim file makes this visible. The reason for the mismatch is not confirmed — possibly a legacy artefact from pre-COSMoS NCIt assignments. Both codes are valid; NCIt_Code identifies the BC concept, TESTCD_NCIt identifies the specific test.

**Study-level BCs (QC-15).** COSMoS includes Trial Summary parameters and Clinical Trial Attributes as Biomedical Concepts, although these are study-level metadata rather than patient-level observations. The `BC_Scope` column (Subject/Study) makes this transparent. The `sdtm-test-codes` track explicitly excludes TSPARMCD/TSPARM as "study-level metadata, not observation test codes" — a deliberate scope difference between the two tracks. Filter on `BC_Scope=Subject` to get only patient-level content. See [`COSMoS_Study_Design_Questions.md`](COSMoS_Study_Design_Questions.md) for further discussion.

The full QC report is in [`reports/COSMoS_BC_DSS_QC.xlsx`](../reports/COSMoS_BC_DSS_QC.xlsx).

## About

This is an exploratory interim file built with AI assistance. Not an official CDISC product. Source data comes from COSMoS public exports and NCI EVS — all verifiable. The [notebooks](../notebooks/) are documented and reproducible.
