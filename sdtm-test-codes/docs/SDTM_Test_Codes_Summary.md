# SDTM Test Codes — What We Learned

*Findings from an AI-assisted structural analysis of SDTM Controlled Terminology,
focused on test code codelists.*

| | |
|---|---|
| **Date** | March 2026 |
| **CT release** | NCI EVS SDTM Terminology, 2025-09-26 |
| **Categorization** | [`skills/sdtm-ct-analysis/`](../../skills/sdtm-ct-analysis/) — 1,181 codelists → 25 categories |
| **Extraction** | [`notebooks/SDTM_CT_Extract.ipynb`](../notebooks/SDTM_CT_Extract.ipynb) — two passes, 55 domains + 353 instruments |
| **Domain metadata** | [`sdtm-domain-reference/SDTM_Domain_Metadata.xlsx`](../../sdtm-domain-reference/machine_actionable/SDTM_Domain_Metadata.xlsx) — domain assignment authority |
| **Reference files** | [`SDTM_Test_Identity.xlsx`](../machine_actionable/SDTM_Test_Identity.xlsx) — 5,781 domain-level test codes |
| | [`SDTM_Instrument_Identity.xlsx`](../machine_actionable/SDTM_Instrument_Identity.xlsx) — 10,166 instrument-level test codes (353 instruments) |

---

## Summary

An inductive categorization of all 1,181 SDTM CT codelists found 25 structural
categories. 83% of codelists (976) are instrument-specific fixed value sets.
The extensibility flag is the primary machine-actionable discriminator: 56
extensible codelists carry the 5,781 unique domain-level test codes, while 353
non-extensible codelists carry 10,166 instrument-level test codes across QS
(Questionnaires), FT (Functional Tests), and RS (Clinical Classification).

This track now extracts both in a two-pass pipeline and produces two enriched
reference files — one per structural type. Domain assignment uses
`SDTM_Domain_Metadata.xlsx` as the authority for SDTMIG v3.4 domains, with
explicit overrides for body-system sub-codelists and TAUG-origin domains
flagged separately.

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
term and synonyms. Every code has at least one CUI. But only ~35% carry a
standard UMLS CUI — the remaining ~65% have only NCI Metathesaurus CUIs,
limiting direct cross-referencing to SNOMED, MeSH, and LOINC. This gap is
consistent across both domain-level and instrument-level codes.

**Domain assignment is not trivial.** Codelist submission values do not map
cleanly to SDTM domain abbreviations. The `*TESTCD` pattern (LBTESTCD → LB)
works for most domains, but `*CD` pattern codelists (MUSCTSCD, MITSCD, URNSTSCD)
use alternate labels that don't match the SDTMIG domain name. Six body-system
sub-codelists required explicit overrides. Ten TAUG-origin domains are outside
SDTMIG v3.4 scope entirely.

## What would improve things

| Gap | What exists | What is missing |
|---|---|---|
| Codelist pairing | LBTESTCD and LBTEST both exist | No declared TC↔TN relationship |
| Domain ownership | Encoded in display name | No structured domain field |
| Instrument families | TC, TN, OR, STR codelists co-exist | No grouping by instrument |
| Subset relationships | TA-FATS ⊂ FA in the data | No declared subset metadata |

These are not missing data. They are missing connections between data that
already exists.

## Pipeline

Two notebooks, two passes, two outputs:

```
NCI EVS SDTM Terminology
        │
        ▼
SDTM_CT_Extract.ipynb
  ├── Pass 1 (extensible)     → interim/SDTM_CT_Extract.csv
  └── Pass 2 (non-extensible) → interim/SDTM_CT_Instrument_Extract.csv
        │
        ▼
SDTM_CT_NCIt_Enrich.ipynb
  ├── + Thesaurus.FLAT.zip    (synonyms, definitions)
  ├── + nci_code_cui_map.dat  (UMLS CUI, NCIm CUI)
  ├── → machine_actionable/SDTM_Test_Identity.xlsx
  └── → machine_actionable/SDTM_Instrument_Identity.xlsx
```

Domain assignment in the Extract notebook uses `SDTM_Domain_Metadata.xlsx`
(from the `sdtm-domain-reference` track) as the authority, with a four-tier
cascade: Domain_Name match → FA sub-codelist detection → body-system override
→ TAUG fallback.

## Provenance

**Categorization** ([`skills/sdtm-ct-analysis/`](../../skills/sdtm-ct-analysis/)):
Two-prompt AI workflow, public NCI EVS file as sole input. Example output in
[`example-output/`](../../skills/sdtm-ct-analysis/example-output/).

**Extraction** (this track): Two notebooks — Extract applies the
extensibility-based filter (two passes), Enrich adds NCIt and UMLS
cross-references to both.

Both reproducible from the public NCI EVS SDTM Terminology file.
