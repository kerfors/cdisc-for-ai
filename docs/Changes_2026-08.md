# Changes — August 2026: COSMoS 2026-07-14 refresh

**Reference versions:** SDTM CT 2026-03-27 (NCI EVS) and SDTMIG v3.4 / SDTM v2.0 unchanged
— the June 2026 CT quarterly release did not happen, so the CT pin is still current.
COSMoS BC/DSS bumped from the 2026-05-26 package to **2026-07-14**. Like the June release,
this is an upstream data refresh: the pipeline is unchanged, only its inputs moved.

## Upstream refresh — COSMoS package 2026-07-14

Where the May package was a metadata backfill on a stable concept set, the July package is
a content release: both layers grow. The Biomedical Concepts side gains a large Subject
Characteristics expansion (demographic, socioeconomic, and birth-and-family concepts), the
PASI Fredriksson question set and the AJCC v7 staging chain on the QRS-classification
side, hepatitis serology, and breast-cancer procedure and imaging concepts. The Dataset
Specialization group set grows for the first time since March, concentrated in SC, IS
(per-allergen IgE groups — the known maximum fan-out under a single BC grows again), RS,
and PR.

Two specialization groups move from RP to SC with their identifiers and Biomedical
Concepts intact — a clean upstream instance of the BC/DSS boundary: the observation is
unchanged, only where it is filed moved.

The graph track and every downstream consumer (`consumer-bases`, `sdtm-findings-graph`)
were rebuilt on the new package. Graph validation introduced no new failures; the new
surgery and radiation value lists reference a handful of procedure terms not yet in the
pinned SDTM CT, which surface as unresolved value-list members and should clear when the
next CT release lands. Track-local detail, including the BC and DSS movement and the
downstream propagation, is in
[`cosmos-graph/docs/COSMoS_Refresh_2026-07-14.md`](../cosmos-graph/docs/COSMoS_Refresh_2026-07-14.md).

## Instrument watch item: carried, not closed

The May release recorded a watch item on the new QRS grouping tier (the Cognitive
Assessment Tool and Clinical or Research Functional Assessment Tool containers, then
terminal). The July package does not wire them up: both containers remain terminal, each
with its single instrument child, and the new PASI / AJCC material arrives in a different
assessment family without using the tier. The companion notebooks (50/51) confirmed this
as the one-run check they were built to be; the watch item stays open in
[`cosmos-graph/docs/COSMoS_Instrument_Layer.md`](../cosmos-graph/docs/COSMoS_Instrument_Layer.md) §8.

## Ingestion-source decision recorded

The question of whether to switch `cosmos-graph` ingestion from the published flat export
to the nested LinkML/API form was settled by test and recorded in
[`docs/COSMoS_Ingestion_Source.md`](COSMoS_Ingestion_Source.md): the cumulative nested
form is member-gated, the public flat export loses nothing the pipeline needs, so the
ingest stays on the public export. This refresh applied that decision unchanged. A
possible switch from the downloaded xlsx to the export CSV (same content, cleaner
parsing) was deliberately kept out of this release so that data movement and pipeline
movement never share a diff.

## Authoritative current state

File-level current state lives in the README sheet of each machine-actionable xlsx,
regenerated on every run. Counts, column inventories, and coverage percentages are
point-in-time and belong there rather than in this note.

## References

- Refresh detail: [`cosmos-graph/docs/COSMoS_Refresh_2026-07-14.md`](../cosmos-graph/docs/COSMoS_Refresh_2026-07-14.md)
- Instrument layer watch item: [`cosmos-graph/docs/COSMoS_Instrument_Layer.md`](../cosmos-graph/docs/COSMoS_Instrument_Layer.md) §8
- Ingestion-source decision: [`docs/COSMoS_Ingestion_Source.md`](COSMoS_Ingestion_Source.md)
- Previous release: [`Changes_2026-06.md`](Changes_2026-06.md)
