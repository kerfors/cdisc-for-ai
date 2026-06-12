# Changes — June 2026: COSMoS 2026-05-26 refresh and instrument tooling

**Reference versions:** SDTM CT 2026-03-27 (NCI EVS) and SDTMIG v3.4 / SDTM v2.0 unchanged; COSMoS BC/DSS bumped from the 2026-03-31 package to **2026-05-26**. Unlike the May release, this is an upstream data refresh — the pipeline is unchanged, only its inputs moved.

## Upstream refresh — COSMoS package 2026-05-26

The first COSMoS data refresh since the March package. The Biomedical Concepts file gains a handful of new concepts, including a new QRS / Functional Assessment grouping tier (the C222259 "Cognitive Assessment Tool" and C222260 "Clinical or Research Functional Assessment Tool" containers) and two RECIST tumor assessments. The Dataset Specialization group set is unchanged, but the package backfills provenance and typing that were previously blank — `origin_type`, `origin_source`, `data_type`, and `length` are now populated across the variable rows — and normalises the LOINC coding-system URI from `https://loinc.org` to `http://loinc.org/`.

The graph track and every downstream consumer (`consumer-bases`, `sdtm-findings-graph`) were rebuilt on the new package. Graph validation introduced no new failures and cleared one (a pinned term that the package brought into its bound codelist). Downstream value movement is modest and concentrated where the source backfill landed — unit value-lists and a few result scales. Track-local detail, including the BC and DSS diffs and the downstream propagation, is in [`cosmos-graph/docs/COSMoS_Refresh_2026-05-26.md`](../cosmos-graph/docs/COSMoS_Refresh_2026-05-26.md).

## Instrument category and parent-chain tooling

Two companion notebooks in `cosmos-graph/` operationalise the instrument identifier asymmetry described in `COSMoS_Instrument_Layer.md` §5 — that the `BC_Categories` tokens grouping a QRS instrument are search labels, not addressable identifiers. `50_instrument_category_resolution` resolves instrument category tokens to a BC identity by exact `bc_short_name` then unique `bc_synonyms` match, shipping a status enum rather than a bare mapping. `51_instrument_parent_chain` walks the instrument-scope `BC_Parents` chains and flags terminal (unwired) parents. Both carry a version-bump diff cell, so each package's change to the instrument layer is a one-run check.

The work follows CDISC's Knowledge Base article [*Searching CDISC Biomedical Concepts*](https://www.cdisc.org/kb/articles/cdisc-published/searching-cdisc-biomedical-concepts), which establishes the `categories` attribute — not the NCIt hierarchy — as the recommended way to retrieve all BCs of a QRS instrument. The 2026-05-26 package's new grouping tier, together with the 6MWT container rename and reparenting it triggered, is recorded as a watch item in `COSMoS_Instrument_Layer.md` §8: the new parent containers are currently terminal (not yet wired up to their own parent), and the structure is expected to evolve in the next package.

## Authoritative current state

File-level current state lives in the README sheet of each machine-actionable xlsx, regenerated on every run. Counts, column inventories, and coverage percentages are point-in-time and belong there rather than in this note.

## References

- Refresh detail: [`cosmos-graph/docs/COSMoS_Refresh_2026-05-26.md`](../cosmos-graph/docs/COSMoS_Refresh_2026-05-26.md)
- Instrument layer and the 2026-05-26 watch item: [`cosmos-graph/docs/COSMoS_Instrument_Layer.md`](../cosmos-graph/docs/COSMoS_Instrument_Layer.md) §8
- CDISC guidance: [*Searching CDISC Biomedical Concepts*](https://www.cdisc.org/kb/articles/cdisc-published/searching-cdisc-biomedical-concepts)
- Previous release: [`Changes_2026-05.md`](Changes_2026-05.md)
