# Changes — April 2026: instrument identity refactor

**Reference versions:** unchanged from Changes_2026-03 (SDTM CT 2026-03-27, COSMoS 2026-Q1, SDTMIG v3.4 / SDTM v2.0). This release is a restructuring pass on the instrument side of the repository. No upstream data refresh.

## What moved

The instrument identity work now separates three architectural layers that were previously collapsed into one file:

**Test layer.** The file that used to be called `SDTM_Instrument_Identity.xlsx` is actually at TESTCD-within-codelist grain — one row per individual question in a published instrument codelist. It has been renamed `SDTM_Instrument_Test_Identity.xlsx` to say what it is. Contents and columns are unchanged.

**Codelist layer (new).** A new `SDTM_Instrument_Identity.xlsx` now carries the instrument / subscale grain — one row per SDTM CT instrument codelist. Each row anchors to two independent NCIt concepts: the instrument-as-tool (C20993 branch) and the question container that groups the codelist (C211913 branch). These two branches are not structurally linked in NCIt, and the file names that gap rather than hiding it. A new `SDTM_Instrument_Identity_Enrich.ipynb` produces this file, absorbing the matching-cascade and structural-walk logic that lived in the earlier `explore/coa-structure` exploration.

**Consumer wiring.** `Instrument_Findings.xlsx` now carries the dual NCIt anchors (instrument and container) as columns on both its TESTCD sheet and its DSS sheet, joined via `Codelist_TESTCD`. The consumer gains a stable NCIt anchor for every instrument-layer row rather than just a label string.

## Why

Two things drove the refactor.

First, the old name was misleading. "Instrument Identity" suggested instrument-level grain, but the file carried per-question rows. A sibling file at the genuine codelist grain was needed if the repo is going to be coherent about what "identity" means at each layer.

Second, NCIt represents instruments and question containers in separate, structurally disconnected branches. Every design alternative that tries to hide that gap (single NCIt code per row, fuzzy matching to paper over unmatched instruments) introduces silent errors in exchange for cleaner-looking coverage. Explicit dual anchors, plus `Instrument_Match_Method = UNMATCHED` for rows without a clean C20993 match, preserves the gap as information rather than papering over it. Token-overlap fuzzy matching is deliberately excluded — exploratory work showed it produced wrong-version matches (HAMD-17 → HAMD-21, SF-36 → SF-8) that destroy identity.

## Housekeeping

The `coa-structure/` folder has been retired. Its design-rationale doc (`NCIt_Instrument_Identity_Findings.md`) now lives under `sdtm-test-codes/docs/`. Its community-conversation note on COSMoS specification focus lives under `cosmos-bc-dss/docs/`. The probe notebooks and their interim outputs are gone — their logic is now in the production enrichment notebook, their outputs in the corresponding track folders.

## Color convention

The repo's xlsx files use header colors to signal architectural layer: green for TESTCD identity, yellow for COSMoS Dataset Specializations, dark chocolate for instrument identity (C20993), copper for question container / subscale (C211913), grey for neutral keys. The new codelist-grain file uses chocolate and copper prominently; the consumer file adopts the same tones where it pulls the codelist-grain columns in, making the layer visible across files.

## Authoritative current state

File-level current state lives in the README sheet of each machine-actionable xlsx, regenerated on every run. Counts, column inventories, and coverage percentages are point-in-time and belong there rather than in this note.

## References

- Design rationale (dual NCIt anchors, why C20993 is fragile and C211913 is structural): [`sdtm-test-codes/docs/NCIt_Instrument_Identity_Findings.md`](../sdtm-test-codes/docs/NCIt_Instrument_Identity_Findings.md)
- COSMoS specification scope (DSS vs CRF, where COSMoS value concentrates): [`cosmos-bc-dss/docs/COSMoS_Specification_Focus.md`](../cosmos-bc-dss/docs/COSMoS_Specification_Focus.md)
- Previous release: [`Changes_2026-03.md`](Changes_2026-03.md)
