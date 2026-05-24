# COSMoS Content and Quality Checks

*Exploratory quality analysis of COSMoS BC and DSS content — starting from Laboratory and expanding across all 32 published domains. Part of the [cdisc-for-ai](https://github.com/kerfors/cdisc-for-ai) project.*

## What this analyses

The two COSMoS levels — Biomedical Concepts (BCs) and Dataset Specializations (DSSs) — projected into a multi-sheet traversable graph by [`cosmos-graph/`](../../cosmos-graph/) (output [`interim/COSMoS_Graph.xlsx`](../../cosmos-graph/interim/COSMoS_Graph.xlsx)). The [Compare notebook](../notebooks/COSMoS_BC_NCIt_Compare.ipynb) validates definitions and synonyms against the authoritative NCIt source.

Scope at the 2026-03 package: 1,345 BCs across 32 domains, 1,326 DSSs.

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
| IS (Immunogenicity) | 7 | 290 | Target-driven fan-out — antigen × scale |
| LB (Laboratory) | 97 | 146 | All have specimen; 136 have LOINC |
| RS (Disease Response) | 129 | 135 | Mostly qualitative; instrument hierarchy |
| **RE (Respiratory)** | **135** | **135** | **New in 2026-03** — pulmonary function and respiratory mechanics |
| TS (Trial Summary) | 128 | 129 | Study-level metadata, not measurements |
| **VS (Vital Signs)** | **74** | **78** | **Major expansion in 2026-03** (was 12/16); location/laterality variants |

## QC summary

17 checks (QC-01 to QC-15), no blocking errors. Full report: [`reports/COSMoS_BC_DSS_QC.xlsx`](../reports/COSMoS_BC_DSS_QC.xlsx).

**CT mapping gaps (QC-01/02/05).** 4 specimen NCIt codes not in SDTM CT: C449/DNA (26 usages), C812/RNA (7), C113243 (2), C95940 (3) — the first two are GF domain specimens encoded as NCIt codes rather than CT terms. 3 method terms not in CT: AUTOPSY, C179788, PINCH DYNAMOMETRY. These are source-level gaps — COSMoS references codes not in the current CT codelists.

**Quantitative DSSs without units (QC-06).** 133 rows across 14 domains (was 106 across 12). RP (27), MK (25), FT (16), RE (15), VS (12) dominate. The +27 increase comes entirely from the new RE and expanded VS content shipping without `Allowed_Units` — worth flagging upstream.

**Retired BCs included in output (QC-10).** 20 BCs (was 4). The 2026-03 cycle retired 16 additional BCs but kept them in the export. Most of the new retirements are DS-domain disposition outcomes (Adverse Event, Dead, Lost To Follow-Up, Physician Decision, Lack of Efficacy, Failure to Meet Randomization Criteria, etc.) — looks like a coordinated rework. Consumers should not consume `[RETIRED]` BCs.

**Result Scale vocabulary (QC-11a/b).** COSMoS uses "Qualitative" (502 DSSs) and "datetime" (7) — not in the [BC Curation Principles](https://cdisc-org.github.io/COSMoS/bc_starter_package/doc/BC%20Curation%20Principles%20and%20Completion%20GLs.xlsx) valid set ("Nominal"/"Ordinal" and "Temporal"). Vocabulary alignment would help downstream consumers.

**TESTCD_NCIt ≠ NCIt_Code (QC-14).** 7 DSSs where the TESTCD-level NCIt code differs from the BC identity (HEIGHT, WEIGHT, INTP, GLUCPE, MICROCY, LENGTH, HCG). Both codes valid; legacy pre-COSMoS assignments. Impacts cross-source joins on NCIt_Code.

**Study-level BCs (QC-15).** 193 BCs are TS parameters. Filter on `BC_Scope=Subject` for patient-level content.

## Cross-source comparison against NCIt

The [Compare notebook](../notebooks/COSMoS_BC_NCIt_Compare.ipynb) validates COSMoS definitions and synonyms against NCIt (via [`SDTM_Test_Identity.xlsx`](../../sdtm-test-codes/machine_actionable/SDTM_Test_Identity.xlsx)). Scoped to subject-level Findings BCs — **566 matched** (up from 372 in the previous package, +52%). The comparable pool grew from 531 to 727 as the 2026-03 SDTM CT package closed coverage gaps. Full report: [`reports/COSMoS_BC_NCIt_Compare.xlsx`](../reports/COSMoS_BC_NCIt_Compare.xlsx).

**Definitions are nearly identical.** 564 of 566 match (99.6%). Only **one** editorial divergence remains: HBA1CHGB (C111207), where COSMoS uses "glycosylated hemoglobin" and NCIt uses the more precise "glycated hemoglobin A1C". The two earlier divergences are gone — ALBCREAT was harmonized at the source, and TUMERGE was retired entirely as part of the broader SDTM CT consolidation.

**Synonyms diverge more.** 432 of 566 match. Of the rest: 82 NCIt supersets (more variant names — expected), 25 COSMoS supersets (potential NCIt enrichment candidates), 25 with unique terms in both directions, 2 where COSMoS is empty but NCIt has synonyms. The COSMoS-superset and bidirectional-unique counts are unchanged from the previous cycle — no investment was made on these in 2026-03.

**161 Findings BCs couldn't be compared** — instrument-specific non-extensible codelists (RS:114, FT:23, QS:13, plus a few VS and IE) outside the extensible CT scope. Same domain mix as before; backlog essentially unchanged.

## Planned: LOINC validation

135 LB DSSs carry LOINC codes, not yet validated against LOINC itself.

## Related

- [COSMoS_Behavioural_Analysis.md](COSMoS_Behavioural_Analysis.md) — how BC→DSS patterns differ across domains
- [COSMoS_Domain_Pattern_Inventory.xlsx](COSMoS_Domain_Pattern_Inventory.xlsx) — machine-actionable behavioural reference
- [`reports/COSMoS_BC_NCIt_Compare.xlsx`](../reports/COSMoS_BC_NCIt_Compare.xlsx) — definition and synonym comparison detail

## About

Exploratory work built with AI assistance. Not an official CDISC product. Source data from COSMoS public exports and NCI EVS — all verifiable. [Notebooks](../notebooks/) are documented and reproducible.
