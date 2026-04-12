# COSMoS True Focus: Two Kinds of Specialisation

Note for the community conversation with Linda, Sam, Bess. Scope: where COSMoS value-add actually lives, and what the two specialisation types (Dataset and CRF) cover.

*cdisc-for-ai, April 2026*

---

## The reframing

COSMoS BC/DSS work is often discussed as if it were doing two different things at once: grouping question-level BCs into instruments (upward categorisation) and describing how each question is operationally captured (downward specification). Treating these as one workload blurs where COSMoS is irreplaceable and where it is doing work other published standards already cover.

The architecturally honest picture separates them: upward categorisation is not COSMoS territory, downward specification is exactly COSMoS territory. This note focuses on the second — the specification layer, where COSMoS is the only possible source and where the work should concentrate.

## Two kinds of specialisation

Two specification artifacts exist in CDISC, addressing different moments in the data lifecycle.

### Dataset Specialisation (DSS)

Describes how a concept is represented in the SDTM **submission dataset** — the stored record after collection.

Carries: domain, TESTCD, result scale, units, standard unit, decimal precision, specimen (for lab findings), location and laterality (for measurement findings).

Answers: "how is this value structured when it lands in the SDTM dataset?"

Status: published, in use, part of the current COSMoS package. Example coverage in the flattened view (`COSMoS_BC_DSS.xlsx`) shows DSS content is present and useful for quantitative questions — 6MWT Distance at 1 Minute carries `Result_Scale = Quantitative`, `Allowed_Units = m`, `Decimal_Places = 5` directly.

### CRF Specialisation

Describes how the same concept is represented on the **collection form** — the data entry moment, before the value lands in SDTM.

A draft artifact [`cdisc_crf_specializations_draft.xlsx`](https://cdisc-org.github.io/COSMoS/export/cdisc_crf_specializations_draft.xlsx) is published in the COSMoS GitHub `export/` folder. Based on the PHUSE 2025 paper *CDISC Biomedical Concepts: What are they and why should I care?* (Paper DS04), the CRF / CDASH specialisation structure includes Data Collection Groups (linked to a BC identifier), Data Collection Items (linked to Data Element Concept identifiers), Code Lists, List Values, Pre-populated Values, and SDTM Target mappings (annotation text, SDTM variable list, mapping string).

Based on public information, we understand CRF Specialisations to carry: data collection group and item structure, answer codelist bindings for coded questions, permitted list values, pre-populated values, and explicit mappings to SDTM target variables. Exact scope, delivery mechanism, and release timeline beyond the draft export are best confirmed with the COSMoS working group.

*Note: there is a CDISC webinar on this topic available only to CDISC members, which we have not accessed. The characterisation above is drawn from public GitHub artifacts and publicly available conference papers. Some specifics may not fully reflect current working group direction.*

## Why both matter and neither is sufficient alone

For quantitative instrument questions (numeric answers with units, like 6MWT distance in metres), DSS is sufficient. Units and precision travel unchanged from CRF to dataset. There is no collection-side specification fact that is not also a storage-side fact.

For coded-response instrument questions (the majority case — 148 of 175 materialised rows in the current instrument content are Qualitative, 85% of the set), DSS is **not** sufficient. Scale type gets captured but the answer codelist binding does not. Example: `AIMS0111` (Current Problems Teeth/Dentures) carries `Result_Scale = Qualitative` in the flattened DSS view, but no pointer to the SDTM CT response codelist providing the permitted values. The specification fact that most matters for a coded question — *which codelist is the answer set* — is absent from DSS.

The PHUSE paper's description of Collection Specialisation including `Code Lists` and `List Values` as first-class elements suggests that CRF Specialisations are designed to close exactly this gap, although we have not verified how the current draft handles the 20 materialised QRS instruments specifically.

## Implication for where COSMoS value concentrates

The work that only COSMoS can do, and that no other published CDISC or NCIt artifact covers, is the specification layer. SDTM CT stops at TESTCD identity. NCIt stops at concept identity. Specification content — units, precision, value sets, answer codelist bindings, derivation rules — only exists where COSMoS has materialised it. For the 20 instruments where DSS content is populated and rich, the content is substantive and unreachable elsewhere.

The unfinished specification gap has two parts worth naming separately:

1. **DSS materialisation for more instruments.** 20 of 353 CDISC-coded instruments have any DSS content today. Pace and prioritisation question for the working group.

2. **CRF Specialisation content, draft stage.** The draft export exists but is not yet production; coverage across the 20 materialised DSS instruments is unknown to us. If CRF Specialisations become the home for answer codelist bindings and related form-side content, this closes the coded-question gap that DSS cannot address.

Both gaps are real. Both are specification work. Neither is about hierarchy.

## Questions for the community conversation

Framed as constructive questions rather than gap-pointing:

- What is the current status and release timeline for CRF Specialisations beyond the draft export in the COSMoS GitHub?
- For the 20 instruments with current DSS content, will CRF Specialisations be added in parallel, retrofitted, or treated as a separate workstream?
- Is the draft CRF Specialisation structure described in the PHUSE 2025 paper (Data Collection Groups, Items, Code Lists, List Values, SDTM Target) still the intended model, or has it evolved?
- What is the prioritisation model for materialisation across the remaining 333 instruments, and would depth (complete DSS + CRF content for fewer instruments) be preferable to breadth (shallow coverage across many)?

## Summary

COSMoS's value is on the specification row: describing how clinical concepts are operationally captured in trials. Dataset Specialisation handles the storage side. CRF Specialisation, currently in draft in the COSMoS GitHub, handles the collection side — including the answer codelist bindings that DSS alone cannot carry. Together they cover what no other CDISC or NCIt artifact can cover: the operational specification layer between concept identity and the trial data itself.

Depth over breadth: fewer instruments with complete specification content, rather than many instruments with thin or partial content. That is where COSMoS is irreplaceable.

*References used in this note: COSMoS GitHub repository (<https://github.com/cdisc-org/COSMoS>), draft CRF Specializations export (<https://cdisc-org.github.io/COSMoS/export/cdisc_crf_specializations_draft.xlsx>), PHUSE 2025 Paper DS04 on CDISC Biomedical Concepts (<https://www.lexjansen.com/phuse-us/2025/ds/PAP_DS04.pdf>), CDISC Biomedical Concepts Public Review Webinar 2024 (<https://www.cdisc.org/sites/default/files/pdf/Public%20Review%20Webinar%20052024.pdf>).*
