# cdisc-for-ai — Top-Level Summary

## What we are doing

Making CDISC SDTM Controlled Terminology, NCIt, and COSMoS Biomedical Concepts and Dataset Specializations more consumable for AI, rule engines, and humans. Existing standards, made more reachable. Not a new standard.

The guiding architectural principle: **One Graph, Many Views.** Flat reference files are projections of graph-shaped relationships in the standards. Making those relationships explicit — putting related data side by side in rows — is the contribution.

## Four tracks of work

**Identity (`sdtm-test-codes` track).** SDTM CT and NCIt enriched into machine-actionable test-identity files. `SDTM_Test_Identity.xlsx` and `SDTM_Instrument_Identity.xlsx` are the output. `Codelist_Cross_References.xlsx` is the May-2026 addition; declares semantic relations between codelists (PROCEDUR ↔ METHOD seed) and emits mechanical Term_Diff for the canonical lookup of clinical abbreviations to CDISC submission values.

**Measurement-spec graph (`cosmos-graph` track).** COSMoS BCs and DSSs as a lossless graph projection. `COSMoS_Graph.xlsx` carries the BC/DSS/Variables/AssignedTerms/Coding sheets at native grain. `Codelist_Coverage.xlsx` is the May-2026 addition; codelist-forward projection that preserves the bare codelist bindings the wide-format pivot loses.

**Joined denormalised views (`consumer-bases` track).** Wide and long projections that put related data side by side in traversable rows. `DSS_View.xlsx` is the wide one-row-per-DSS pivot, now carrying `observation_class` joined from SDTM_Domain_Metadata. `DSS_Variables_View.xlsx` is the long-format complement at one-row-per-VLM-row grain. `PR_DSS_Reachability.xlsx` is the procedure-forward projection.

**Findings-shaped consumer artefacts (`sdtm-findings-graph` track).** Domain-shaped joined views (`Specimen_Findings`, `Measurement_Findings`, `Instrument_Findings`) that pre-join the implicit relationships at behavioural-pattern grain.

## Investigational thread (this work)

A fifth thread: sponsor-agnostic clinical-knowledge reference maps, applied to one modality family at a time, that surface the gap between clinical truth and standards coverage.

Three families completed (MRI of liver disease, DXA for osteoporosis, hand and foot X-ray for RA structural progression) plus a repo-level Procedure-Options Inventory across them. Four reusable prompts (family-map, inventory, integration, plus the X-ray case study HTMLs as the architectural worked example) govern the work.

Cite-checking against PubMed, FDA, ACR, AASLD, EASL, QIBA, and ESGAR/SAR primary sources is a hard gate at every stage. No sponsor inputs.

## What we have learned

**The two-layer separation generalises.** Clinical truth (Sheet 1) vs COSMoS coverage (Sheet 2) holds across families authored independently. The "Architectural observation flag" tier — DSS exists but with a modelling decision worth surfacing — is the most informative output and where the productive COSMoS authoring conversation lives.

**Three structural patterns recur in every family.**

1. **PR-side modality × anatomy authoring is uneven and limited to chest/brain.** Three right-grain PR DSSs exist at 2026-Q1: `CTSCANCHEST`, `MRIBRAIN`, `XRAYCHEST`. None of the 21 procedures across the three families targets chest or brain, which is why the inventory's universal finding ("none has a PR DSS at right grain") holds.
2. **METHOD value_list pattern over-promises substitutability.** MK Sharp DSSs accept X-RAY;MRI; TR/TU accept 15 imaging methods. Modality difference is reduced to a per-record qualifier choice when it is sometimes a clinically meaningful identity difference.
3. **Composite-score modelling is unsolved.** mTSS, FRAX, LI-RADS Category have no current COSMoS pattern, despite being the actual reported endpoints in registration submissions.

**The PROCEDUR/METHOD codelist split is a structural finding.** Modern imaging sub-modes — `DXA SCAN`, `ULTRASOUND`, `MAMMOGRAPHY`, `MAGNETIC RESONANCE ELASTOGRAPHY` (MRE), `DIFFUSION WEIGHTED MRI` (DWI), `MAGNETIC RESONANCE CHOLANGIOPANCREATOGRAPHY` (MRCP) — have governed METHOD terms but are absent from PROCEDUR. PR-side DSS authoring is blocked behind CDISC CT governance work that is itself out of consumer-bases scope. The canonical abbreviation-to-submission-value mapping is in `Codelist_Cross_References.xlsx Term_Diff`.

**The COSMoS template is reusable; population is editorial work.** The DSS pattern (VLM group, pinned values, value-list-restricted slots, bound codelists) generalises. Adding cases is editorial work, not architectural work — but two structural extensions are still needed before the template covers procedure → findings → burden end-to-end: a burden-qualifier slot pattern on the procedure side, and a composite-indicator pattern.

**Procedure-forward and codelist-forward traversal are now first-class.** The investigational thread surfaced gaps in the consumer-bases architecture (measurement-forward traversal was well-supported; the other two directions were reconstructed manually). The May-2026 upstream-improvements work added five additive projections — `Codelist_Coverage`, `DSS_Variables_View`, `PR_DSS_Reachability`, `Codelist_Cross_References`, plus the `observation_class` column on `DSS_View` — closing the asymmetry. The next inventory and integration runs read deterministically against these projections rather than reconstructing each time.

## Where we are heading

A single named entity — call it Activity Specification — that ties together procedure identity, reachable findings DSSs, and burden-relevant qualifier values. Given an identifier, the same entity is referenced by USDM Activity in protocol design, drives burden roll-up at SoA level, and decomposes deterministically into PR records plus Findings records at SDTM-population time.

Today this integration is sponsor logic. The endpoint is for the standards layer to be the integrator instead.

The three structural pieces that remain:

- A **burden-qualifier slot pattern** on the procedure side (POSITION binding to PR DSSs; view, contrast, preparation, setting modelled as governed slots). Closes the gap the X-ray case study identified for one procedure and the inventory generalised across 21.
- A **composite-indicator DSS pattern** between procedure and findings sides. Covers mTSS, FRAX, LI-RADS Category, and similar derived indices that are the actual reported endpoints in registration trials.
- A **record-to-record link pattern** (PR record matched to Findings records by timing, subject, RELREC) named in SDTM but not modelled in COSMoS today.

All three are tractable. All three benefit every future case rather than the case being authored. None requires inventing new standards work — they extend the COSMoS template along axes the consumer-side work has now made visible.

## Public artefact set

Three family maps, the inventory, the four prompts, the X-ray case study HTMLs. Together a complete public reference for the COSMoS authoring conversation. Each artefact stands on its own; they cite each other where the cross-references are useful.

The cdisc-for-ai work is sponsor-agnostic. Indications are recorded as documented in the clinical literature, not filtered by any portfolio. Every claim traces to a publicly verifiable reference.

Repository: `https://github.com/kerfors/cdisc-for-ai`
