# COSMoS Flattened: Content and Quality Checks

*Exploratory quality analysis of COSMoS BC and DSS content — starting from Laboratory and expanding across all 31 published domains. Part of the [cdisc-for-ai](https://github.com/kerfors/cdisc-for-ai) project.*

## What the file is

The [Flatten notebook](../notebooks/COSMoS_BC_DSS_Flatten.ipynb) combines the two COSMoS levels — Biomedical Concepts (BCs) and Dataset Specializations (DSSs) — into a single flat Excel file: one row per DSS, BC identity columns carried along. The [Validate notebook](../notebooks/COSMoS_BC_DSS_Validate.ipynb) runs structural QC checks. The [Compare notebook](../notebooks/COSMoS_BC_NCIt_Compare.ipynb) validates definitions and synonyms against the authoritative NCIt source.

Output: [`interim/COSMoS_BC_DSS.xlsx`](../interim/COSMoS_BC_DSS.xlsx) — 1,127 BCs across 31 domains, 1,123 DSSs.

## Glucose — the LB decomposition pattern

One BC — Glucose Measurement (C105585) — produces 8 DSSs in LB, decomposed by specimen and result scale:

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

*\*GLUCSERPL specimen is SERUM in source — flagged as QC-07. GLUCPE carries a different TESTCD_NCIt (C163446) than the parent BC — flagged as QC-14.*

This specimen × scale decomposition is the core LB pattern. The behavioural analysis found it generalises across MB and MI, but differs fundamentally in IS (target-driven) and GF (scale-driven). See [COSMoS_Behavioural_Analysis.md](COSMoS_Behavioural_Analysis.md) for the full picture.

## Domain distribution (top 6 by DSS count)

| Domain | BCs | DSSs | Notable |
|---|---|---|---|
| LB (Laboratory) | 93 | 142 | All have specimen; 135 have LOINC |
| IS (Immunogenicity) | 7 | 290 | Target-driven fan-out — antigen × scale |
| RS (Disease Response) | 129 | 135 | Mostly qualitative; instrument hierarchy |
| TS (Trial Summary) | 128 | 129 | Study-level metadata, not measurements |
| VS (Vital Signs) | 12 | 16 | Location/laterality variants |
| EG (ECG) | 33 | 33 | All qualitative; 18 with units |

## QC summary

17 checks (QC-01 to QC-15), no blocking errors. Full report: [`reports/COSMoS_BC_DSS_QC.xlsx`](../reports/COSMoS_BC_DSS_QC.xlsx).

**CT mapping gaps (QC-01/02/05).** 4 specimen NCIt codes not in SDTM CT: C449/DNA (26 usages), C812/RNA (7), C113243 (2), C95940 (3) — the first two are GF domain specimens encoded as NCIt codes rather than CT terms. 3 method terms not in CT: AUTOPSY, C179788, PINCH DYNAMOMETRY. These are source-level gaps — COSMoS references codes not in the current CT codelists.

**Quantitative DSSs without units (QC-06).** 106 rows across 12 domains. MK (25), RP (27), FT (16) dominate. Mix of genuine gaps and early-stage curation.

**Result Scale vocabulary (QC-11a/b).** COSMoS uses "Qualitative" (491 DSSs) and "datetime" (7) — not in the [BC Curation Principles](https://cdisc-org.github.io/COSMoS/bc_starter_package/doc/BC%20Curation%20Principles%20and%20Completion%20GLs.xlsx) valid set ("Nominal"/"Ordinal" and "Temporal"). Vocabulary alignment would help downstream consumers.

**TESTCD_NCIt ≠ NCIt_Code (QC-14).** 7 DSSs where the TESTCD-level NCIt code differs from the BC identity (HEIGHT, WEIGHT, INTP, GLUCPE, MICROCY, LENGTH, HCG). Both codes valid; legacy pre-COSMoS assignments. Impacts cross-source joins on NCIt_Code.

**Study-level BCs (QC-15).** 193 BCs are TS parameters. Filter on `BC_Scope=Subject` for patient-level content.

## Cross-source comparison against NCIt

The [Compare notebook](../notebooks/COSMoS_BC_NCIt_Compare.ipynb) validates COSMoS definitions and synonyms against NCIt (via [`SDTM_Test_Identity.xlsx`](../../sdtm-test-codes/machine_actionable/SDTM_Test_Identity.xlsx)). Scoped to subject-level Findings BCs — 372 matched. Full report: [`reports/COSMoS_BC_NCIt_Compare.xlsx`](../reports/COSMoS_BC_NCIt_Compare.xlsx).

**Definitions are nearly identical.** 369 of 372 match. 3 editorial divergences (ALBCREAT, HBA1CHGB, TUMERGE).

**Synonyms diverge more.** 242 of 372 match. Of 130 that differ: 78 NCIt supersets (more variant names — expected), 25 COSMoS supersets (potential NCIt enrichment candidates), 25 with unique terms in both directions.

**159 Findings BCs couldn't be compared** — instrument-specific non-extensible codelists (RS, FT, QS) outside the extensible CT scope.

## Planned: LOINC validation

135 LB DSSs carry LOINC codes, not yet validated against LOINC itself.

## Related

- [COSMoS_Behavioural_Analysis.md](COSMoS_Behavioural_Analysis.md) — how BC→DSS patterns differ across domains
- [COSMoS_Domain_Pattern_Inventory.xlsx](COSMoS_Domain_Pattern_Inventory.xlsx) — machine-actionable behavioural reference
- [`reports/COSMoS_BC_NCIt_Compare.xlsx`](../reports/COSMoS_BC_NCIt_Compare.xlsx) — definition and synonym comparison detail

## About

Exploratory work built with AI assistance. Not an official CDISC product. Source data from COSMoS public exports and NCI EVS — all verifiable. [Notebooks](../notebooks/) are documented and reproducible.
