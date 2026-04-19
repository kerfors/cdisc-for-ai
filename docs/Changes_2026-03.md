# Changes — 2026-03 release update

Summary of what moved when the repository was rebuilt against the March 2026 source releases.

**Reference versions**

- SDTM CT: NCI EVS package **2026-03-27**
- COSMoS BC/DSS: package **2026-Q1**
- SDTMIG: **v3.4** (unchanged)

Per-track diff CSVs are kept under `*/diffs/pre-2026-03__current/` for anyone wanting to reproduce the deltas. The pre-update baselines are preserved in `pre-2026-03/` folders next to each affected output.

## SDTM CT (sdtm-test-codes)

Source: `SDTM_Test_Identity.xlsx` and `SDTM_Instrument_Identity.xlsx` rebuilt from the new NCI EVS package.

| File | Added | Removed | Changed |
|---|---:|---:|---:|
| SDTM_Test_Identity (domain-level TESTCDs) | 108 | 4 | 39 |
| SDTM_Instrument_Identity (instrument TESTCDs) | 145 | 0 | 160 |

The 4 removed domain-level TESTCDs are retired terms (e.g. Pepsinogen A/C splits, TUMERGE, TUSPLIT, ASGMGIND, CD8TGP — verified that no downstream notebook hardcodes them). The 39 changed rows are mostly definition or synonym refreshes from NCIt; key identity fields (NCIt_Code, TESTCD) are stable.

## COSMoS BC/DSS (cosmos-bc-dss)

Source: COSMoS 2026-Q1 BC and DSS exports re-flattened.

| Metric | Before | After | Delta |
|---|---:|---:|---:|
| Total BCs | 1,127 | 1,345 | +218 |
| Total Dataset Specializations | 1,123 | 1,326 | +203 |
| BCs with DSS | 705 | 903 | +198 |
| SDTM domains with DSS coverage | 31 | 32 | +1 |
| Findings BCs | 535 | 731 | +196 |
| Findings DSSs | 924 | 1,125 | +201 |

Domain-level highlights:

- **RE — Respiratory System Findings (new domain in COSMoS).** First-time COSMoS coverage: 152 BCs / 135 DSSs. The domain has been part of SDTMIG since v3.3 but was missing from `SDTM_Domain_Metadata.xlsx`; this release adds the RE row (Findings, Measurement structural type).
- **VS — Vital Signs.** Major expansion: 12 → 74 BCs, 16 → 78 DSSs.
- **LB — Laboratory Tests.** 93 → 97 BCs, 142 → 146 DSSs (incremental).
- **DS, MK, RP, RS** — small additions only.
- All other domains unchanged in BC/DSS count.

Most-used category tags this cycle include *Pulmonary Function Test* (107), *Vital Signs* (88), *Hematology Tests* (54), *Body Measurements* (46, new), and the *Respiratory System Findings* category reflected via the new RE domain. Several categories that previously appeared in my top-20-by-frequency summary — *Blood Cell Counts* (37), *Disease Response* (39), *Electrocardiogram Findings* (35) — dropped out of that view as other categories grew faster this cycle, but the tags themselves are unchanged on the BCs that carry them. COSMoS categories are a flat tag list, not a hierarchy, so there is no "top-level" designation.

Retired BCs: 4 → 20 (full disposition tracked in `COSMoS_Content_and_QC.md` QC-10).

NCIt comparison: matched BC definitions 372 → 566, definition-text matches 369 → 564, divergences 3 → 1. TUMERGE retired upstream, ALBCREAT now consolidated to a single LOINC (14959-1, **needs sponsor validation**), HBA1CHGB still divergent (glycosylated vs glycated).

## SDTM Findings (sdtm-findings)

Consumer files rebuilt from the new sources. Numbers reflect both the SDTM CT additions and the COSMoS expansion.

| File / Sheet | Added | Removed | Changed |
|---|---:|---:|---:|
| Specimen_Findings · Test_Identity | 76 | 2 | 56 |
| Specimen_Findings · Measurement_Specs | 4 | 0 | 3 |
| Measurement_Findings · Test_Identity | 1 | 0 | 369 |
| Measurement_Findings · Measurement_Specs | 62 | 0 | 0 |

Net coverage:

- Specimen-based TESTCDs: 4,109 → **4,183**; with COSMoS DSSs: 100 → **104**.
- LB TESTCDs: 2,474 → **2,505**.
- The 369 changed rows on Measurement_Findings · Test_Identity are almost entirely the COSMoS_DSS_Count and COSMoS_Categories fields shifting after the VS expansion — the underlying TESTCDs are stable.

Instrument findings track was not rebuilt in this round.

## Architectural decision: Measurement_Findings shape

The 2026-Q1 VS expansion and RE addition collapsed Measurement Findings to ~98% flat 1:1 rows (5 fan-out BCs across 291 total). This prompted a review of whether `Measurement_Findings.xlsx` should remain two-sheet (Test_Identity + Measurement_Specs, same as `Specimen_Findings.xlsx`) or collapse to single-sheet.

**Decision: hold the two-sheet shape.** The rationale for two-sheet is separation of identity (green-track NCIt columns) from specification (yellow-track COSMoS columns) — a semantic separation by source and column-set, not by row population. The original sparsity argument is weakened (Measurement_Specs is now a near-complete left-join rather than a filtered subset), but the identity/specification distinction and cross-track consumer consistency with Specimen_Findings still hold. No file shape change; `Measurement_Findings.xlsx` is regenerated with the new data only. The behavioural characterisation for VS shifts from "subject-level measurements with location decomposition" to "flat measurement catalog with residual location variants" and is updated in `cosmos-bc-dss/docs/COSMoS_Behavioural_Analysis.md`.

## Consumer file column addition: COSMoS_Category

Added `COSMoS_Category` (SDTM `--CAT` submission value) to both sheets of `Specimen_Findings.xlsx` and `Measurement_Findings.xlsx`, aligning with the same column added to `Instrument_Findings.xlsx` on 8 April. Inserted in Test_Identity between `COSMoS_BC_Name` and `COSMoS_Categories` (SDTM-side single-value before COSMoS-side multi-value), and in Measurement_Specs between `DS_Name` and `Domain`. `COSMoS_Subcategory` not added — 0% populated across all in-scope domains.

Population:

- Specimen_Findings · Test_Identity: 88 of 4,183 rows (all LB-covered TESTCDs; CHEMISTRY, HEMATOLOGY, URINALYSIS)
- Specimen_Findings · Measurement_Specs: 136 of 160 rows (all LB; MB/MI 0%)
- Measurement_Findings · Test_Identity: 0 of 334 rows (VS/MK/RE/CV all empty in current COSMoS package)
- Measurement_Findings · Measurement_Specs: 0 of 128 rows

The empty column in Measurement_Findings is intentional — kept for cross-track architectural alignment and to light up automatically if COSMoS populates `--CAT` for measurement domains in a future release. README bullets in both files note the current emptiness.

## Reference / metadata

- `SDTM_Domain_Metadata.xlsx`: 56 → 57 rows (RE added).
- Structural Types table in `sdtm-domain-reference/README.md`: Measurement Findings 4 → 5.

## Reproducing

Each track contains a `*_Diff_vs_pre_2026_03.ipynb` notebook (kept where still present) and a `pre-2026-03/` baseline folder. Re-running the source notebooks regenerates the current outputs; the diff notebooks compare current against the baseline and write the CSVs in `diffs/pre-2026-03__current/`.

---

*Subsequent: the file named above as `SDTM_Instrument_Identity.xlsx` was renamed to `SDTM_Instrument_Test_Identity.xlsx` and a new codelist-grain `SDTM_Instrument_Identity.xlsx` was added in April 2026 as part of the instrument identity refactor. See [`Changes_2026-04.md`](Changes_2026-04.md).*
