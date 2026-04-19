# COSMoS True Focus: Two Kinds of Specialisation

Note drafted for community conversation (Linda, Sam, Bess) about where COSMoS value-add lives, and what the two specialisation types (Dataset and CRF) cover.

*cdisc-for-ai, April 2026*

---

## Scope

COSMoS BC/DSS work is often discussed as doing two different things at once: grouping question-level BCs into instruments (upward categorisation) and describing how each question is operationally captured (downward specification). Separating the two clarifies where COSMoS is irreplaceable and where it duplicates other published standards. This note focuses on the specification layer — where COSMoS is the only possible source.

## Two kinds of specialisation

Two specification artifacts exist in CDISC, addressing different moments in the data lifecycle.

### Dataset Specialisation (DSS)

Describes how a concept is represented in the SDTM **submission dataset** — the stored record after collection.

Carries: domain, TESTCD, result scale, units, standard unit, decimal precision, specimen (for lab findings), location and laterality (for measurement findings).

Answers: "how is this value structured when it lands in the SDTM dataset?"

Status: published, in use, part of the current COSMoS package. Example: 6MWT Distance at 1 Minute carries `Result_Scale = Quantitative`, `Allowed_Units = m`, `Decimal_Places = 5` in the flattened DSS view (`COSMoS_BC_DSS.xlsx`).

### CRF Specialisation

Describes how the same concept is represented on the **collection form** — the data entry moment, before the value lands in SDTM.

A draft artifact [`cdisc_crf_specializations_draft.xlsx`](https://cdisc-org.github.io/COSMoS/export/cdisc_crf_specializations_draft.xlsx) is published in the COSMoS GitHub `export/` folder. Based on the PHUSE 2025 paper *CDISC Biomedical Concepts: What are they and why should I care?* (Paper DS04), the structure includes Data Collection Groups (linked to a BC identifier), Data Collection Items (linked to Data Element Concept identifiers), Code Lists, List Values, Pre-populated Values, and SDTM Target mappings (annotation text, SDTM variable list, mapping string).

CRF Specialisations are understood to carry: data collection group and item structure, answer codelist bindings for coded questions, permitted list values, pre-populated values, and explicit mappings to SDTM target variables. Exact scope, delivery mechanism, and release timeline beyond the draft export are best confirmed with the COSMoS working group.

*Note: a CDISC webinar on this topic exists for CDISC members; the characterisation here is drawn from public GitHub artifacts and conference papers and may not fully reflect current working group direction.*

## Why both matter

For **quantitative** instrument questions (numeric answers with units, like 6MWT distance in metres), DSS is sufficient. Units and precision travel unchanged from CRF to dataset.

For **coded-response** instrument questions — 148 of 175 materialised rows (85%) in the current instrument content — DSS is **not** sufficient. Scale type is captured but the answer codelist binding is not. Example: `AIMS0111` (Current Problems Teeth/Dentures) carries `Result_Scale = Qualitative` but no pointer to the SDTM CT response codelist providing the permitted values. The specification fact that most matters for a coded question — *which codelist is the answer set* — is absent from DSS.

The PHUSE paper's description of Collection Specialisation including `Code Lists` and `List Values` as first-class elements suggests CRF Specialisations are designed to close exactly this gap, though coverage across the 20 materialised DSS instruments has not been verified.

## Where COSMoS value concentrates

Specification content — units, precision, value sets, answer codelist bindings, derivation rules — only exists where COSMoS has materialised it. SDTM CT stops at TESTCD identity; NCIt stops at concept identity. For the 20 instruments with populated DSS content, the content is substantive and unreachable elsewhere.

Two gaps are worth naming separately:

1. **DSS materialisation for more instruments.** 20 of 353 CDISC-coded instruments have any DSS content today. Pace and prioritisation question for the working group.
2. **CRF Specialisation content, draft stage.** Draft export exists but is not production; coverage across the 20 materialised DSS instruments is unknown. If CRF Specialisations become the home for answer codelist bindings and related form-side content, this closes the coded-question gap DSS cannot address.

Depth over breadth: fewer instruments with complete specification content, rather than many with thin or partial content. That is where COSMoS is irreplaceable.

## Questions for the community conversation

- Status and release timeline for CRF Specialisations beyond the draft export?
- For the 20 instruments with current DSS content, will CRF Specialisations be added in parallel, retrofitted, or treated as a separate workstream?
- Is the draft CRF Specialisation structure described in the PHUSE 2025 paper (Data Collection Groups, Items, Code Lists, List Values, SDTM Target) still the intended model?
- Prioritisation model for the remaining 333 instruments — depth vs breadth?

---

*References: COSMoS GitHub repository (<https://github.com/cdisc-org/COSMoS>), draft CRF Specializations export (<https://cdisc-org.github.io/COSMoS/export/cdisc_crf_specializations_draft.xlsx>), PHUSE 2025 Paper DS04 (<https://www.lexjansen.com/phuse-us/2025/ds/PAP_DS04.pdf>), CDISC Biomedical Concepts Public Review Webinar 2024 (<https://www.cdisc.org/sites/default/files/pdf/Public%20Review%20Webinar%20052024.pdf>).*
