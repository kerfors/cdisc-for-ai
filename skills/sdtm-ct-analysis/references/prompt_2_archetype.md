# SDTM CT Archetype Table — Prompt 2 of 2

**Version:** 1.0  
**Purpose:** Generate a structured archetype table and machine-actionability analysis from discovered categories  
**Input:** Output from Prompt 1 (Category Discovery), specifically Sections 1 and 2  
**Output:** Archetype table + machine-actionability analysis

---

## CONTEXT

You are continuing an analysis of CDISC SDTM Controlled Terminology. In the previous step (Prompt 1), the codelists were examined inductively and assigned to structural categories. That output is provided below.

Your task is to synthesize that categorization into a reference archetype — a structured description of each category that can be used by humans, AI systems, and automated tools to reason correctly about SDTM CT content.

---

## INPUT

Paste the full output from Prompt 1 here — at minimum Sections 1 (Category Definitions) and 2 (Assignment Table).

`[INSERT PROMPT 1 OUTPUT]`

---

## CONSTRAINT — STAY WITHIN THE DATA

The archetype table and all analysis must be grounded in properties observable in the input data and the Step 1 output. Do not extend category definitions with clinical knowledge not present in the input file. Where the data is insufficient to make a strong claim, say so explicitly — those gaps belong in the gap analysis, not papered over with assumed domain knowledge.

---

Using only the categories and assignments from Prompt 1 — do not add or remove categories — produce the following:

---

### Output 1 — Archetype Table

One row per category. Render as a markdown table.

| Category | Codelist_Count | Extensibility | SDTM_Variable_Role | NCIt_Relationship | Machine_Actionability | Archetype_Behavior |
|---|---|---|---|---|---|---|

Column definitions:

- **Extensibility**: `Always` / `Never` / `Mixed` — and the *reason*, not just the flag
- **SDTM_Variable_Role**: Which SDTM variable(s) codelists in this category populate (e.g. `LBTESTCD / LBTEST`, `QSTEST`, `LBSPEC`)
- **NCIt_Relationship**: How terms in this category relate to NCIt concepts: `Direct C-code per concept` / `Instrument-defined` / `Concept-backed` / `Administrative` / `None`
- **Machine_Actionability**: What an automated system can do with this category — be specific: `Semantic concept matching via NCIt` / `Exact string lookup by instrument identity` / `Qualifier slot-filling` / etc.
- **Archetype_Behavior**: One sentence — the critical thing a consumer system must understand to use this category correctly without breaking

---

### Output 2 — Machine-Actionability Ranking

Produce as a simple numbered list. One line per category: rank, name, one-clause justification. No prose paragraph. Definition: *a system can reliably determine which term applies using only the CT file and standard ontological relationships, without additional human judgment.*

---

### Output 3 — Gap Analysis

Table only — one row per category, Gap column max 10 words, keep it a phrase not a sentence.

| Category | Gap | Who would need to act |
|---|---|---|

Use "Nothing — already self-describing" where no gap exists.

---

### Output 4 — Prompt 1 Sanity Check

Max 3 bullet points total. Flag only genuine issues — miscategorized codelists or real category boundary inconsistencies. If nothing material to flag, say so in one sentence and stop.

---

## NOTES

- Use the category names exactly as defined in Prompt 1. Do not rename, merge, or split.
- If Prompt 1 left some assignments as LOW confidence, reflect that uncertainty in the archetype row — do not treat uncertain assignments as definitive.
- The Archetype_Behavior column is the most important column in Output 1. It should be actionable: a developer or AI system reading it should know what to do differently for this category compared to others.
- Output 3 is intended for CDISC community discussion — write it at the level of a constructive technical observation, not a criticism.
