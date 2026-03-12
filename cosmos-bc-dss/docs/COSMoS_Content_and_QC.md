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

## Internal validation

The [Validate notebook](../notebooks/COSMoS_BC_DSS_Validate.ipynb) runs 17 checks (QC-01 to QC-15). No blocking errors. Full report: [`reports/COSMoS_BC_DSS_QC.xlsx`](../reports/COSMoS_BC_DSS_QC.xlsx).

| Check | Description | Severity | Count |
|---|---|---|---|
| QC-01 | CT unmapped: Specimen | ERROR | 4 |
| QC-02 | CT unmapped: Method | WARNING | 3 |
| QC-03 | CT unmapped: Unit | PASS | 0 |
| QC-04 | DSSs with no TESTCD | INFO | 46 |
| QC-05 | Specimen present but Specimen_NCIt blank | WARNING | 38 |
| QC-06 | Quantitative DSSs without units | WARNING | 106 |
| QC-07 | GLUCSERPL specimen mismatch | WARNING | 1 |
| QC-08 | Multi-result DSS (same TESTCD+Domain+Specimen) | INFO | 32 |
| QC-09 | BC_only_no_DS count by category | INFO | 194 |
| QC-10 | Retired BCs in export | WARNING | 4 |
| QC-11a | Result_Scale "Qualitative" not in curation principles | WARNING | 491 |
| QC-11b | Result_Scale "datetime" not in curation principles | WARNING | 7 |
| QC-11c | Result_Scale unexpected values | PASS | 0 |
| QC-12 | Placeholder BC_IDs (NEW_*) | INFO | 6 |
| QC-13 | Preferred term not stripped from synonyms | WARNING | 5 |
| QC-14 | TESTCD_NCIt differs from NCIt_Code | INFO | 7 |
| QC-15 | BC_Scope=Study (trial-level metadata) | INFO | 193 |

### Key findings

**CT mapping gaps (QC-01, QC-02, QC-05).** 4 specimen NCIt codes and 3 method terms could not be resolved to SDTM CT submission values. 38 DSSs have specimen text but no Specimen_NCIt as a result. Unit mapping is complete. These are source-level gaps — COSMoS references NCIt codes not in the current SDTM CT codelists.

**Quantitative DSSs without units (QC-06).** 106 rows across 12 domains. MK (25), RP (27), FT (16) dominate. Mix of genuine gaps and early-stage curation.

**Result Scale vocabulary (QC-11a/b).** COSMoS uses "Qualitative" (491 DSSs) and "datetime" (7) which don't appear in the [BC Curation Principles](https://cdisc-org.github.io/COSMoS/bc_starter_package/doc/BC%20Curation%20Principles%20and%20Completion%20GLs.xlsx) valid set ("Nominal"/"Ordinal" and "Temporal" respectively). Not errors — vocabulary alignment between source and curation principles would help downstream consumers.

**TESTCD_NCIt differs from NCIt_Code (QC-14).** 7 DSSs where the TESTCD-level NCIt code differs from the BC identity: HEIGHT, WEIGHT, INTP, GLUCPE, MICROCY, LENGTH, HCG. Both codes are valid; likely legacy pre-COSMoS assignments. Impacts cross-source joins on NCIt_Code.

**Study-level BCs (QC-15).** 193 BCs are trial-level metadata (TS parameters), not patient-level observations. `BC_Scope` column distinguishes them. The `sdtm-test-codes` track deliberately excludes these — filter on `BC_Scope=Subject` for patient-level content.

**Other findings.** 4 retired BCs still in export (QC-10). 6 placeholder BC_IDs with NEW_* prefix (QC-12). 5 BCs with preferred term not stripped from synonyms (QC-13). 46 DSSs without TESTCD in non-test-code domains (QC-04). 32 multi-result DSSs dominated by IS specimen variants (QC-08).

## Cross-source comparison against NCIt

The [Compare notebook](../notebooks/COSMoS_BC_NCIt_Compare.ipynb) validates COSMoS definitions and synonyms against the authoritative NCIt source (via [`SDTM_Test_Identity.xlsx`](../../sdtm-test-codes/machine_actionable/SDTM_Test_Identity.xlsx)). Scoped to subject-level Findings BCs — 372 matched to extensible SDTM CT test codes. Full report: [`reports/COSMoS_BC_NCIt_Compare.xlsx`](../reports/COSMoS_BC_NCIt_Compare.xlsx).

**Definitions are nearly identical.** 369 of 372 match. 3 differ: ALBCREAT (COSMoS adds "protein", specifies "urine sample"), HBA1CHGB ("glycosylated" vs "glycated"), TUMERGE (reworded). Editorial divergences, not pipeline artifacts.

**Synonyms diverge more.** 242 of 372 match. Of the 130 that differ: 78 are NCIt supersets (NCIt carries more variant names — expected), 25 are COSMoS supersets (curated additions not in NCIt — potential NCIt enrichment candidates), 25 have unique terms in both directions.

**159 Findings BCs couldn't be compared** — their TESTCDs come from non-extensible instrument-specific codelists (RS: 114, FT: 23, QS: 13) outside the green file's scope. 5 of these are QC-14 cases where the NCIt_Code mismatch prevents the join.

## Planned: LOINC validation

135 LB dataset specializations carry LOINC codes. These have not yet been validated against LOINC itself — confirming that the LOINC code matches the specimen, method, and scale specified in the DSS. The [LOINC web services](http://xml4pharmaserver.com/WebServices/LOINC_webservices.html) provide the lookup needed to cross-check these programmatically.

## About

This is an exploratory interim file built with AI assistance. Not an official CDISC product. Source data comes from COSMoS public exports and NCI EVS — all verifiable. The [notebooks](../notebooks/) are documented and reproducible.
