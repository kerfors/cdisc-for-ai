# SDTM CT Category Discovery — Prompt 1 of 2

**Input:** SDTM Terminology tab-delimited text file (NCI EVS), filtered to codelist-header rows (~1,200 rows).
**Output:** Category report — used as input to Prompt 2.

---

## Context

You are working with the CDISC SDTM Controlled Terminology file. Each codelist is a named, bounded set of allowed submission values for one or more SDTM variables.

Relevant columns:

| Column | Content |
|---|---|
| `Code` | NCIt C-code for the codelist |
| `Codelist Code` | Short codelist identifier (e.g. LBTESTCD) |
| `Codelist Name` | Full display name |
| `CDISC Submission Value` | The actual submission string |
| `Codelist Extensible (Yes/No)` | Whether sponsors can add terms |
| `CDISC Definition` | CDISC's definition |
| `NCI Preferred Term` | NCIt preferred label |

The input should already be filtered to codelist-level rows (where `Codelist Code` is empty).

---

## Constraint — stay within the data

Every category and assignment must be justified by properties **directly observable in the input columns**: codelist name, definition, extensibility flag, submission value pattern, or NCIt C-code structure.

Do not use clinical domain knowledge to infer what a codelist "must be for." If the structural signature is unclear, assign LOW confidence and state what is missing.

---

## Task

Analyze the codelists and discover the structural categories actually present. Work inductively:

1. Examine names, definitions, extensibility flags, and the nature of terms
2. Identify groupings based on **semantic role** — what the codelist *is for*, not which SDTM domain it belongs to
3. Name and define each category
4. Assign every codelist to exactly one category

Look for distinctions that matter for machine consumption — categories that behave differently when used by an automated system.

---

## Output format

### Section 1 — Category Definitions

For each category, one compact block:

```
Category name: [name]
Definition: [one sentence]
Structural signature: [max 20 words — key observable properties]
Primary discriminator: [the single property a consuming system would use to identify this category]
Count: [number of codelists assigned]
```

Descending order by count. No additional prose.

### Section 2 — Full Assignment Table

| Codelist_Code | Codelist_Name | Assigned_Category | Confidence | Note |
|---|---|---|---|---|

- `Confidence`: HIGH / MEDIUM / LOW
- `Note`: required only for MEDIUM/LOW — one sentence on what made assignment uncertain

### Section 3 — Structural Observations

Answer each in **one sentence only**:

1. Which categories were easiest to identify and why?
2. Which codelists were hardest to assign — what caused the ambiguity?
3. Did any codelists appear to belong to two categories? Name them and the tension.
4. What structure is present but invisible in the flat format — what must a consumer infer?
5. Are there codelists whose machine-actionability differs fundamentally from others in the same category?
6. Which categories share a machine-consumption profile despite different naming signatures? (Same extensibility, same variable role, same relationship to NCIt — but assigned to different categories based on name pattern.)
7. Do any categories appear to be specializations or subsets of another category rather than peers?

### Section 4 — What would refine this

Max 3 bullet points. One line each — name the external source and what it resolves.
