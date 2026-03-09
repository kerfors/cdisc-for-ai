# SDTM Test Codes — What We Learned

*Findings from an AI-assisted structural analysis of SDTM Controlled Terminology,
focused on test code codelists.*

| | |
|---|---|
| **Date** | March 2026 |
| **CT release** | NCI EVS SDTM Terminology, 2025-09-26 |
| **Categorization** | [`skills/sdtm-ct-analysis/`](../../skills/sdtm-ct-analysis/) — 1,181 codelists → 25 categories |
| **Extraction** | [`notebooks/SDTM_CT_Extract.ipynb`](../notebooks/SDTM_CT_Extract.ipynb) — 55 domains, 6,255 records |
| **Reference file** | [`machine_actionable/SDTM_Test_Identity.xlsx`](../machine_actionable/SDTM_Test_Identity.xlsx) — 5,781 enriched test codes |

---

## Summary

An inductive categorization of all 1,181 SDTM CT codelists found 25 structural
categories. 83% of codelists (976) are instrument-specific fixed value sets.
The 56 domain-level test code codelists that carry the 5,781 unique measurement
test codes are structurally distinguished by a single property: they are
extensible. This is the machine-actionable dispatch signal — but it is not
surfaced in the published file structure.

Four structural relationships exist in the data but are not declared: codelist
pairing (TC↔TN), domain ownership, instrument family grouping, and codelist
subset relationships. Publishing these as machine-traversable metadata would
make the CT substantially more useful for automated systems — without changing
the terminology itself.

---

## Key findings

**Extensibility separates domain-level from instrument-specific.** Both share
"Test Code" in the codelist name. Both use TC/TN pairing. The only reliable
discriminator is the extensibility flag: 56 extensible (domain-level) vs 353
non-extensible (instrument-specific). A consuming system that filters on name
pattern alone will conflate the two.

**22 of 55 domains are strict subsets of another.** All 20 TA-specific Findings
About codelists are complete subsets of the generic FA codelist. Holter ECG is
a subset of ECG. Detected generically through set comparison — no hardcoded
rules. CDISC does not publish these relationships.

**396 test codes appear in multiple domain codelists.** Cross-domain membership
is common but invisible in the flat file — a consumer processing one domain at
a time will miss that the same NCIt concept serves multiple contexts.

**100% NCIt coverage, but a CUI gap.** Every test code has an NCIt preferred
term and synonyms. Every code has at least one CUI. But only 34.9% carry a
standard UMLS CUI — the remaining 65.1% have only NCI Metathesaurus CUIs,
limiting direct cross-referencing to SNOMED, MeSH, and LOINC.

## What would improve things

| Gap | What exists | What is missing |
|---|---|---|
| Codelist pairing | LBTESTCD and LBTEST both exist | No declared TC↔TN relationship |
| Domain ownership | Encoded in display name | No structured domain field |
| Instrument families | TC, TN, OR, STR codelists co-exist | No grouping by instrument |
| Subset relationships | TA-FATS ⊂ FA in the data | No declared subset metadata |

These are not missing data. They are missing connections between data that
already exists.

## Provenance

**Categorization** ([`skills/sdtm-ct-analysis/`](../../skills/sdtm-ct-analysis/)):
Two-prompt AI workflow, public NCI EVS file as sole input. Example output in
[`example-output/`](../../skills/sdtm-ct-analysis/example-output/).

**Extraction** (this track): Two notebooks — Extract applies the
extensibility-based filter, Enrich adds NCIt and UMLS cross-references.

Both reproducible from the public NCI EVS SDTM Terminology file.
