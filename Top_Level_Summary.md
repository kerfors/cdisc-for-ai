# cdisc-for-ai — Top-Level Summary

## What we are doing

Making CDISC SDTM Controlled Terminology, NCIt, and COSMoS Biomedical Concepts and Dataset Specializations more consumable for AI, rule engines, and humans. Existing standards, made more reachable. Not a new standard.

The guiding architectural principle: **One Graph, Many Views.** Flat reference files are projections of graph-shaped relationships in the standards. Making those relationships explicit — putting related data side by side in rows — is the contribution.

## Four tracks of work

**Identity (`sdtm-test-codes` track).** SDTM CT and NCIt enriched into machine-actionable test-identity files. `SDTM_Test_Identity.xlsx` and `SDTM_Instrument_Identity.xlsx` are the output. `Codelist_Cross_References.xlsx` is the May-2026 addition; declares semantic relations between codelists (PROCEDUR ↔ METHOD seed) and emits mechanical Term_Diff for the canonical lookup of clinical abbreviations to CDISC submission values.

**Measurement-spec graph (`cosmos-graph` track).** COSMoS BCs and DSSs as a lossless graph projection. `COSMoS_Graph.xlsx` carries the BC/DSS/Variables/AssignedTerms/Coding sheets at native grain. `Codelist_Coverage.xlsx` is the May-2026 addition; codelist-forward projection that preserves the bare codelist bindings the wide-format pivot loses.

**Joined denormalised views (`consumer-bases` track).** Wide and long projections that put related data side by side in traversable rows. `DSS_View.xlsx` is the wide one-row-per-DSS pivot, now carrying `observation_class` joined from SDTM_Domain_Metadata. `DSS_Variables_View.xlsx` is the long-format complement at one-row-per-VLM-row grain. `PR_DSS_Reachability.xlsx` is the procedure-forward projection.

**Findings-shaped consumer artefacts (`sdtm-findings-graph` track).** Domain-shaped joined views (`Specimen_Findings`, `Measurement_Findings`, `Instrument_Findings`) that pre-join the implicit relationships at behavioural-pattern grain.

## Case-study walkthroughs

Three case pairs in [`docs/`](docs/) trace single clinical cases through the SDTM CT + NCIt + COSMoS stack:

- **Glucose** (Findings; LB) — `Glucose_COSMoS_Story.html` (recording view) and `Glucose_StudyIntent_Story.html` (what study-design assembly adds on top of GLUCPL).
- **6MWT** (COA; QS / FT / RS) — `6MWT_NCIt_Story.html` (NCIt identity layer) and `6MWT_COSMoS_Story.html` (what COSMoS records and what it leaves to composition and classification).
- **Chest X-Ray** (PR + MK / TR / TU) — `XRay_COSMoS_Story.html` traces a single clinical concept through two SDTM domain classes (procedure on the PR side, measurements off the image on the Findings side) and shows what COSMoS records of each.

Each pair shows what the standards already carry and where the gap to clinical use sits.

## Behavioural analysis

A repo-level analysis of how the BC-to-DSS relationship behaves across SDTM domains. Ten behavioural groups cluster into five identity patterns; the analysis explains why a Dataset Specialization means different things in different domains. See [`docs/Identity_Needs_by_Behavioural_Group.md`](docs/Identity_Needs_by_Behavioural_Group.md) and the full analysis in [`cosmos-bc-dss/docs/COSMoS_Behavioural_Analysis.md`](cosmos-bc-dss/docs/COSMoS_Behavioural_Analysis.md).

## Public artefact set

The machine-actionable xlsx outputs of the four tracks, the three case-study pairs above, and the behavioural-analysis notes. Together a public reference set; each artefact stands on its own; they cite each other where the cross-references are useful.

The cdisc-for-ai work is sponsor-agnostic. Indications are recorded as documented in the clinical literature, not filtered by any portfolio. Every claim traces to a publicly verifiable reference.

Repository: `https://github.com/kerfors/cdisc-for-ai`
