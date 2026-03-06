# SDTM CT Category Discovery — Prompt 1 of 2

**Version:** 1.0  
**Purpose:** Inductive discovery of structural categories in SDTM Controlled Terminology  
**Input:** SDTM Terminology tab-delimited text file (NCI EVS release), full file filtered to codelist-header rows  
**Output:** Category report — to be used as input to Prompt 2

---

## CONTEXT

You are working with the CDISC SDTM Controlled Terminology file as published by NCI EVS. The file contains codelists — each codelist is a named, bounded set of allowed submission values for one or more SDTM variables.

The relevant columns in the input file are:

| Column | Content |
|---|---|
| `Code` | NCIt C-code for the codelist or term |
| `Codelist Code` | Short codelist identifier (e.g. LBTESTCD) |
| `Codelist Name` | Full display name |
| `CDISC Submission Value` | The actual submission string |
| `Codelist Extensible (Yes/No)` | Whether sponsors can add terms |
| `CDISC Definition` | CDISC's definition of the term or codelist |
| `NCI Preferred Term` | NCIt preferred label |

Codelist-level rows have `Codelist Code` = empty and a value in `CDISC Submission Value` (the codelist mnemonic, e.g. LBTESTCD). Term-level rows have `Codelist Code` populated with the parent codelist's C-code. The input to this analysis should already be filtered to codelist-level rows only.

---

## CONSTRAINT — STAY WITHIN THE DATA

Every category you name and every assignment you make must be justified by properties **directly observable in the input columns**: codelist name, definition, extensibility flag, submission value pattern, or NCIt C-code structure.

Do not use clinical domain knowledge to infer what a codelist "must be for." If you cannot identify the structural signature from the file itself, assign LOW confidence and state what observable property is missing. This constraint is the basis for verifiability — anyone with the same input file should be able to check every assignment independently.

---

Analyze the codelists and **discover the structural categories that are actually present** in this data. Do not use any pre-defined taxonomy.

Work inductively:
1. Examine codelist names, definitions, extensibility flags, and the nature of their terms
2. Identify groupings based on **semantic role** — what the codelist *is for*, not which SDTM domain it belongs to
3. Name and define each category you find
4. Assign every codelist to exactly one category

You are looking for distinctions that matter for machine consumption — categories that behave differently when used by an automated system or AI.

---

## OUTPUT FORMAT

Produce the following, in this order:

### Section 1 — Category Definitions

For each category, one compact block:

```
Category name: [your name for it]
Definition: [one sentence max]
Structural signature: [max 20 words — the key observable properties only]
Count: [number of codelists assigned]
```

List categories in descending order by codelist count. No additional prose.

---

### Section 2 — Full Assignment Table

A table with one row per codelist:

| Codelist_Code | Codelist_Name | Assigned_Category | Confidence | Note |
|---|---|---|---|---|

- `Confidence`: HIGH / MEDIUM / LOW  
- `Note`: required only for MEDIUM/LOW — one sentence on what made assignment uncertain

---

### Section 3 — Structural Observations

Answer each question in **one sentence only**:

1. Which categories were easiest to identify and why?
2. Which codelists were hardest to assign — and what caused the ambiguity?
3. Did any codelists appear to belong to two categories? Name them and the tension in one sentence.
4. What structure is present but invisible in the flat format — what must a consumer infer?
5. Are there codelists whose machine-actionability differs fundamentally from others in the same category?

---

### Section 4 — What would refine this

Max 3 bullet points. One line each — name the external source and what it resolves. No elaboration.

---

## NOTES

- The goal is discovery, not confirmation. If the data does not support 10 categories, report fewer. If it supports 12, report 12.
- Do not merge categories just to produce a tidy result. Keep ambiguity visible.
- Extensibility alone is not sufficient to define a category — explain the *reason* for the extensibility pattern you observe.
- If a large block of codelists shares an obvious structural feature (e.g. all named after a specific instrument program), note this as a potential sub-category rather than merging it silently into a larger group.
- **Sample bias warning**: If the input is an alphabetical slice of the full file (e.g. "A" through "C"), the categories discovered will not represent the full structural diversity of SDTM CT. Instrument codelists dominate the early alphabet. Measurement Test Codes, Reference Vocabularies, Units, Trial Design, and Identity Classifications may be entirely absent from a small slice. State explicitly in your output if the input appears to be a partial slice and which categories are likely absent. For reliable discovery, the full file (all ~1,200 codelist headers) is strongly preferred.
