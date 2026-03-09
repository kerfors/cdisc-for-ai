# Making COSMoS Work for Study Design

Open questions on column naming and measurement identifiers — for discussion with the CDISC community.

## Context

The [`cosmos-bc-dss`](../) pipeline flattens the COSMoS two-level structure (Biomedical Concepts → Dataset Specializations) into a [single flat file](../interim/COSMoS_BC_DSS.xlsx). One row per Dataset Specialization, with BC identity carried along — so that anyone implementing SDTM mappings can look up a measurement and see everything needed in one place.

The file is structurally complete and [validated](COSMoS_Content_and_QC.md). What remains are two naming and identity questions that benefit from community input.

## Column naming

The current column names translate COSMoS source fields to more readable forms. But they still use CDISC's own vocabulary: Biomedical Concept, Dataset Specialization, DS_Code. These terms are natural for people who work with COSMoS, but not for a study designer building the laboratory section of a protocol.

From a study design perspective, a Dataset Specialization *is* a measurement specification. The DS_Code (GLUCSER, GLUCBLD) *is* the identifier for a selectable measurement. The BC *is* the measurement concept.

The [`sdtm-test-codes`](../../sdtm-test-codes/) track landed on column names we believe work well — they describe what the data *is* for the consumer, not what the source system calls it. This track needs the same iteration.

Some directions to consider:

- `DS_Code` → something like `Measurement_Code` or `Specification_Code`?
- `DS_Name` → `Measurement_Name`?
- `BC_Name` → `Concept_Name`? Or keep it — BC is becoming known terminology.
- `Domain_Class` → already study-design-neutral, works as-is.

This is not a technical decision — it is a naming decision. The current CDISC vocabulary is precise and correct. The question is whether consumers outside the COSMoS team find it navigable.

## Measurement identifiers

When a study designer builds the laboratory section of a protocol, they select identifiable measurement specifications — sometimes a panel ("Comprehensive Metabolic Panel"), sometimes an individual test ("Glucose in Serum, quantitative"). The thing being selected needs to be unambiguously identifiable.

Consider Glucose Measurement (C105585). One BC, eight DSSs — each a distinct combination of specimen, method, and result scale:

| DS_Code | Specimen | Method | Result Scale |
|---|---|---|---|
| GLUCSER | SERUM | — | Quantitative |
| GLUCPL | PLASMA | — | Quantitative |
| GLUCBLD | BLOOD | — | Quantitative |
| GLUCURIN | URINE | — | Quantitative |
| GLUCUA | URINE | TEST STRIP | Qualitative |
| ... | | | |

The DS mnemonic codes (GLUCSER, GLUCBLD, GLUCURIN) already function as identifiers in practice. They are manually created as meaningful short names — the `vlm_group_id` field in the COSMoS source. But they are not yet formal persistent identifiers in the way that NCIt C-codes identify test concepts or LOINC codes identify pre-coordinated measurements.

An earlier question — whether these codes should receive their own NCIt C-codes — was explored in [community discussion](https://www.linkedin.com/feed/update/urn:li:activity:7423793175795896321/). The conclusion: NCIt C-codes are probably not the right mechanism. NCIt identifies biomedical concepts, not implementation-level specifications. But the underlying need remains. As CDISC's Linda Lander noted: "It would be good to explore options for making vlm_group_id a more formal identifier across industry."

This matters for automation. Study design tools (USDM, OpenStudyBuilder) need to reference specific measurement specifications — not just the abstract concept "Glucose Measurement" but specifically "Glucose in Serum, quantitative, reported in mg/dL or mmol/L." Without persistent identifiers at this level, every sponsor builds their own lookup, and every integration rebuilds the same mapping.

The flat file makes this gap visible by putting the DS codes front and center as the primary key for operational rows.

## About

This is exploratory work built with AI assistance. Not an official CDISC product. The source data comes from COSMoS public exports and NCI EVS — all verifiable. The [notebooks](../notebooks/) and [QC checks](COSMoS_Content_and_QC.md) are documented and reproducible.
