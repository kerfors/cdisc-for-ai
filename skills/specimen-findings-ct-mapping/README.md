# Specimen-based Findings CT Mapping

Maps measurement terms to CDISC controlled terminology in two levels: concept identity (TESTCD) and measurement specification (DS_Code). Designed for SoA tables, lab vendor catalogs, panel definitions, or protocol amendments.

## Scope

Specimen-based Findings domains — LB, IS, GF, MB, MI, MS, BS, CP, PC, PP, UR. These share the analyte + specimen + method → result pattern.

For how structural types relate to behavioural patterns across domains, see [`SDTM_Domain_Overview.md`](../../SDTM_Domain_Overview.md).

## How it works

1. **Concept resolution** — resolve a term to TESTCD(s) using semantic matching against NCIt identity (preferred term, synonyms, definition)
2. **Specification resolution** — where COSMoS coverage exists, resolve to DS_Code level: specimen, method, result scale, units, LOINC

Uses clinical reasoning, not string matching. Returns all valid matches for SME review.

## Reference file

[`Specimen_Findings.xlsx`](../../sdtm-findings/machine_actionable/Specimen_Findings.xlsx) — produced by the [`sdtm-findings`](../../sdtm-findings/) consumer track. Two sheets: Test_Identity (concept level) and Measurement_Specs (specification level).

## Files

| File | Audience | Content |
|---|---|---|
| [`SKILL.md`](SKILL.md) | Claude | Skill definition — scope, inputs, steps, output format |
| [`CT_Mapping_Prompt.md`](CT_Mapping_Prompt.md) | Claude | Matching rules, output specification, constraints |
| [`Lab_SME_Curation_Guide.md`](Lab_SME_Curation_Guide.md) | SME reviewer | Review workflow, curation rules, FAQ |
| [`specimen-findings-ct-mapping.zip`](specimen-findings-ct-mapping.zip) | Installation | Packaged skill bundle (all files above + reference file) |

## Installation

Upload the `.zip` bundle to a Claude Project, or add the individual files to project knowledge together with `Specimen_Findings.xlsx`.

## Status

Exploratory. Produces candidate mappings for SME review, not validated production output.
