---
name: specimen-findings-ct-mapping
version: "1.2"
date: 2026-03-26
description: Map specimen-based Findings terms (LB, MB, MI, CP, BS) to CDISC controlled terminology — resolving to TESTCD and, where COSMoS coverage exists, to Dataset Specialization level.
---

# Specimen-based Findings CT Mapping Skill

Maps specimen-based Findings terms to CDISC controlled terminology in two levels: concept identity (TESTCD) and measurement specification (DS_Code). Single conversation.

### Version log

| Version | Date | Changes |
|---|---|---|
| 1.2 | 2026-03-26 | Domain scope aligned with behavioural analysis (LB, MB, MI, CP, BS). Test_Identity scoped to in-scope TESTCDs only. Multi-domain TESTCD flagging added (Rule 7). |
| 1.1 | 2026-03-13 | Reference file changed to Specimen_Findings.xlsx. Domain scope driven by Domain_Metadata. COSMoS summary specimen-scoped. New Measurement_Specs columns. |
| 1.0 | 2025-02-19 | Initial skill. Two-level resolution (TESTCD → DS_Code). Evolved from standalone SoA_CT_Mapping_Prompt v1.3. |

## Scope

Specimen-based Findings — domains where specimen is the structural decomposition axis.
Scope from COSMoS behavioural analysis (see COSMoS_Behavioural_Analysis.md).

| Domain | Content |
|---|---|
| LB | Laboratory |
| MB | Microbiology Specimen |
| MI | Microscopic Findings |
| CP | Cell Phenotype |
| BS | Biospecimen Findings |

**Excluded:** IS (target-driven, not specimen-driven), GF (scale-driven, NCIt-encoded specimen),
UR (zero decomposition despite metadata flag), MS/PC/PP (no COSMoS coverage).

Some TESTCDs belong to both specimen and measurement domains (e.g., OXYSAT in LB and VS).
These appear in the reference file and are flagged for SME review when matched — the same
concept may require different SDTM domain assignment depending on the collection method.

## Inputs

**Reference file:** `Specimen_Findings.xlsx` (produced by `sdtm-findings/notebooks/Specimen_Findings.ipynb`).

| Sheet | Level | Key | Used for |
|---|---|---|---|
| Test_Identity | Concept | TESTCD | Step 1 — what concept? |
| Measurement_Specs | Specification | DS_Code | Step 2 — which variant? |

Read the README sheet first. Every output value must trace to this file verbatim.

**Term list:** Excel or structured list with three columns:

| Column | Content | Example |
|---|---|---|
| `Term_Group` | Grouping label — may carry default specimen context | Chemistry, Urinalysis |
| `Term_ID` | Source system identifier | C-001, row number |
| `Term` | Measurement term string to resolve | Glucose, Urine - Potassium |

Column names are generic — the skill works for SoA tables, lab vendor catalogs, panel definitions, or protocol amendments. The `Term_Group` default specimen is a hint, not a constraint; explicit specimen in the `Term` string overrides it.

## Steps

Read the prompt from: `CT_Mapping_Prompt.md`

Upload the reference file and term list. **Work through each term using clinical reasoning — do not batch-script.**

### Step 1 — Concept Resolution

Resolve each term to TESTCD(s) against the Test_Identity sheet. Semantic matching: NCIt PT → synonyms → definitions. Return all valid matches, classify by match type (Direct, Sibling, Panel, Partial, No_Match).

### Step 2 — Specification Resolution

For TESTCDs where Has_COSMoS=Yes, resolve specimen/method context against the Measurement_Specs sheet:
- Explicit specimen in the term string ("Urine - Potassium" → URINE)
- Term_Group default specimen (Urinalysis → URINE)
- Method/scale/unit hints parsed from the term ("hsCRP (quantitative)")

Step 2 runs inline per term, not as a separate pass.

## Outputs

**Excel file** — one row per Term × TESTCD × DS_Code. TESTCDs without COSMoS coverage produce one row with blank specification columns. Sort: Group → Term → Match_Type → DS_Code.

| Column block | Columns |
|---|---|
| Input (blue) | Term_Group, Term_ID, Term |
| Concept match (green) | Match_Count, TESTCD, TEST, NCIt_Code, NCIt_Preferred_Term, SDTM_Domains, Has_COSMoS |
| Specification (yellow) | DS_Code, DS_Name, Specimen, Method, Result_Scale, Allowed_Units, LOINC_Code, Spec_Resolution |
| Classification (grey) | Match_Type, Match_Rationale, Selected |

Specification columns are populated only where Has_COSMoS=Yes. `Spec_Resolution` indicates resolution depth: Full (term resolved to specific DS_Code), Partial (DS_Code narrowed but spec hints unresolved), None (no COSMoS coverage — TESTCD only).

**Review notes** — companion markdown per Term_Group. Flagged decisions, panel notes, No_Match summary. Start SME review here.

## Companion files

| File | Audience | Purpose |
|---|---|---|
| `CT_Mapping_Prompt.md` | LLM | Matching rules, output specification |
| `Lab_SME_Curation_Guide.md` | SME reviewer | Review workflow, curation rules, FAQ |

## Constraints

1. **Semantic reasoning, not scripting.** Clinical domain knowledge drives matching. Scripted regex will miss semantic relationships.
2. **Never fabricate.** Every TESTCD, TEST, NCIt code, and DS_Code must be copied verbatim from the reference file.
3. **All valid matches.** Return every qualifying TESTCD per term, not just the first.
4. **Coverage gap is explicit.** TESTCDs without COSMoS coverage get TESTCD-level resolution only — specification columns blank, Spec_Resolution=None.
