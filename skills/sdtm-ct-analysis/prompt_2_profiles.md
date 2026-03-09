# SDTM CT Category Profiles — Prompt 2 of 2

**Input:** Output from Prompt 1 (Category Discovery), at minimum Sections 1 and 2.
**Output:** Category profiles, machine-actionability analysis, gap analysis, visualization.

---

## Context

You are continuing an analysis of CDISC SDTM Controlled Terminology. In Prompt 1, the codelists were examined inductively and assigned to structural categories. That output is provided below.

Your task: synthesize the categorization into a reference profile — a structured description of each category that humans, AI systems, and automated tools can use to reason correctly about SDTM CT content.

---

## Input

Paste the full Prompt 1 output here (Sections 1 and 2 at minimum):

`[INSERT PROMPT 1 OUTPUT]`

---

## Constraint

Same as Prompt 1: stay within observable data and the Step 1 output. Do not extend with clinical knowledge not present in the input. Gaps belong in the gap analysis, not papered over.

Use the category names exactly as defined in Prompt 1. Do not rename, merge, or split.

---

## Outputs

### Output 1 — Category Profile Table

One row per category. Markdown table.

| Category | Count | Extensibility | SDTM_Variable_Role | NCIt_Relationship | Machine_Actionability | Consumer_Behavior |
|---|---|---|---|---|---|---|

Column definitions:

- **Extensibility**: `Always` / `Never` / `Mixed` — and the *reason*, not just the flag
- **SDTM_Variable_Role**: Which SDTM variable(s) this category populates (e.g. `LBTESTCD / LBTEST`, `LBSPEC`)
- **NCIt_Relationship**: How terms relate to NCIt: `Direct C-code per concept` / `Instrument-defined` / `Concept-backed` / `Administrative` / `None`
- **Machine_Actionability**: What an automated system can do with this category — be specific
- **Consumer_Behavior**: One sentence — the critical thing a consuming system must understand to use this category correctly

### Output 2 — Machine-Actionability Ranking

Numbered list. One line per category: rank, name, one-clause justification. Definition: *a system can reliably determine which term applies using only the CT file and standard ontological relationships, without additional human judgment.*

### Output 3 — Gap Analysis

| Category | Gap (max 10 words) | Who would need to act |
|---|---|---|

Use "Nothing — already self-describing" where no gap exists.

### Output 4 — Prompt 1 Sanity Check

Max 3 bullet points. Flag only genuine issues — miscategorized codelists or real boundary inconsistencies. If nothing material, say so in one sentence.

## Notes

- If Prompt 1 left assignments as LOW confidence, reflect that uncertainty in the profile — do not treat as definitive.
- The Consumer_Behavior column is the most important. A developer or AI system reading it should know what to do differently for this category.
- Output 3 is intended for CDISC community discussion — constructive technical observation, not criticism.
