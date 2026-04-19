# The Instrument Identity Pattern: Generalizing Beyond QRS

*Follow-up to the Tamer Chowdhury conversation, April 2026*

## What the QRS work delivered

Every SDTM CT instrument codelist now resolves to two independent NCIt anchors: **C20993** for the instrument-as-tool (identity) and **C211913** for the question container that groups the codelist (structure). The two branches are not linked to each other in NCIt; keeping them as separate prefixed columns names the gap rather than papering over it. Coverage on the latest rebuild: ~97% structural (C211913 via parent-child walks), ~70% clean name-match to C20993. Rows without a clean match get `Instrument_Match_Method = UNMATCHED` — honest, not inflated by fuzzy guesses. Output is one row per codelist as a machine-actionable xlsx with a README sheet carrying provenance and match discipline.

See [`sdtm-test-codes/docs/NCIt_Instrument_Identity_Findings.md`](../sdtm-test-codes/docs/NCIt_Instrument_Identity_Findings.md) for the full rationale and [`sdtm-test-codes/machine_actionable/SDTM_Instrument_Identity.xlsx`](../sdtm-test-codes/machine_actionable/SDTM_Instrument_Identity.xlsx) for the artefact.

## Why the pattern generalizes

- **Structural signals already exist in NCI EVS.** Extensibility, NCIt hierarchy membership, codelist code structure — all in the published CT files. Applying the pattern does not require new metadata; it requires the decision to make the linkages explicit.
- **Name-based matching is fragile, but disciplinable.** Token-overlap produces wrong-version errors (HAMD-17 → HAMD-21, SF-36 → SF-8). Exact + suffix-strip + normalized cascade runs clean at ~70% on QRS and can be calibrated per domain. The `UNMATCHED` flag preserves honesty.
- **Dual-anchor columns travel well.** When a CDISC concept has multiple NCIt branches describing different facets, explicit prefixed columns read consistently across reference files, consumer files, and downstream automation.

## Where "for all" could go

| Scope | What is there today | What the pattern would add |
|---|---|---|
| COA beyond QRS (PRO, ClinRO, ObsRO) | NCIt hierarchies exist in C20993 | Codelist-level exposure with dual anchors |
| Specimen-based Findings (LB, MB, MI) | 4,183 TESTCDs with NCIt identity | Dataset-specialization-grain anchors where COSMoS gaps exist |
| All SDTM CT extensible codelists | Codelist concept codes exist but are opaque | Layer-encoded anchors per domain |
| CDASH / ADaM / SEND | Concept codes with same disconnected-branch patterns | Cross-standard alignment |

## What it takes, per target area

A one-pass extraction (analogue of `SDTM_CT_Extract`), an enrichment notebook that walks the relevant NCIt branches, a machine-actionable xlsx following the repo's layer-encoded color convention, and a short rationale doc naming what the matching logic does and does not claim. The matching is the hard part; the plumbing is repeatable.

## Open questions

- Which tier has most pull for CDISC working groups right now?
- Is "match method flagged per row" acceptable as a standard, or does it read as incomplete content to consumers expecting 100% coverage?
- Is there appetite to publish these as companion artefacts to each CT release, rather than as community side-projects?
