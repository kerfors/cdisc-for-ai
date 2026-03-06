---
name: sdtm-ct-analysis
description: >
  Structural analysis of CDISC SDTM Controlled Terminology — discovering the semantic categories
  present in the NCI EVS SDTM Terminology file and generating a machine-actionability archetype table.
  Use this skill whenever the user wants to analyze, categorize, or understand the structure of SDTM CT;
  asks what types of codelists are in SDTM CT; wants to know how different SDTM CT categories behave
  for AI or automated systems; or provides an SDTM CT file for structural analysis.
  Also use when the user asks about making SDTM CT machine-actionable, or wants to run the
  discovery → archetype workflow on a CT file.
---

# SDTM CT Structural Analysis Skill

This skill runs a two-step inductive analysis of a CDISC SDTM Controlled Terminology file. It takes one publicly available input file and produces three output artifacts across two conversations.

**What you will get:**

| Conversation | Input | Output files | What it contains |
|---|---|---|---|
| 1 — Discovery | `SDTM_Terminology.txt` | `SDTM_CT_Category_Discovery.md` | Category definitions, structural observations, refinement notes |
| 1 — Discovery | `SDTM_Terminology.txt` | `SDTM_CT_Category_Discovery_assignments.csv` | One row per codelist — category, confidence, note |
| 2 — Archetype | `SDTM_CT_Category_Discovery.md` | `SDTM_CT_Archetype_Table.md` | One row per category — archetype behavior, machine-actionability, gap analysis |

**Why three files, not one?**

The CSV (1,181 rows) and the Discovery markdown are both Step 1 outputs — the CSV is the machine-readable assignment table, the markdown is the reasoning behind it. The Archetype Table (one row per category, ~10–12 rows) is the synthesis in Step 2. Keeping them separate means each artifact is independently usable: the CSV can be loaded into a spreadsheet, the Discovery markdown is citable as-is, and the Archetype Table is the reference document for consuming systems.

**Why two conversations?**

Step 1 puts all 1,181 codelist headers plus the full analysis into context. Adding Step 2 reasoning in the same conversation risks hitting context limits. Start a new conversation for Step 2, upload the Discovery markdown, and ask for the archetype analysis.

The analysis is exploratory — categories emerge from the data, not from a pre-defined taxonomy.

---

## Workflow

### Before starting: get the input file

**Preferred format: tab-delimited text (`.txt`)**

NCI EVS publishes SDTM CT in multiple formats. The `.txt` file is preferred over Excel — no binary parsing, no version-stamped sheet names, no extra dependencies.

**Direct download URL:**
```
https://evs.nci.nih.gov/ftp1/CDISC/SDTM/SDTM%20Terminology.txt
```

This always resolves to the current release. Ask the user to download this file and provide the local path. **Note:** Opening this URL in a browser will display the file as text rather than downloading it. To save it: press **Cmd+S** (Mac) or **Ctrl+S** (Windows), or right-click anywhere in the page content and choose "Save As". Do not right-click the address bar — that gives a different menu.

> **Note for Claude Code users:** The EVS server can be reached programmatically. A pre-step script can fetch the file automatically:
> ```bash
> curl -o SDTM_Terminology.txt "https://evs.nci.nih.gov/ftp1/CDISC/SDTM/SDTM%20Terminology.txt"
> ```
> In Claude.ai the download must be done manually — the EVS domain is not accessible from the sandbox.

**Loading and filtering:**

The full file is ~44,000 rows (codelists + all their terms). Filter to codelist-header rows only before running Step 1 — this reduces to ~1,200 rows, which is all that is needed for structural categorization.

```python
import pandas as pd

df = pd.read_csv(path, sep='\t', encoding='utf-8', dtype=str)

# Codelist header rows have 'Codelist Code' empty (they ARE the codelist, not a member)
headers = df[df['Codelist Code'].isna() | (df['Codelist Code'] == '')]
print(f"Codelist headers: {len(headers)} rows")
print(f"Columns: {list(df.columns)}")
```

Expected columns: `Code`, `Codelist Code`, `Codelist Extensible (Yes/No)`, `Codelist Name`, `CDISC Submission Value`, `CDISC Synonym(s)`, `CDISC Definition`, `NCI Preferred Term`

> **Sample bias warning**: An alphabetical slice of the full file will produce skewed results — instrument codelists dominate the early alphabet. Measurement Test Codes, Reference Vocabularies, Units, Trial Design, and Identity Classifications may be entirely absent. Always use the full file for reliable discovery.

---

### Step 1 — Discovery

Read the full prompt from: `references/prompt_1_discovery.md`

Run it against the filtered codelist-header data. **Run this analysis directly — read the filtered rows into context and reason over them yourself. Do NOT use the Anthropic API, do NOT build React artifacts, do NOT batch-process via external calls.** The 1,181 filtered rows fit in context and Claude can analyze them directly. This is a reading and reasoning task, not a pipeline task.

The prompt asks for four output sections:
1. Category definitions (name, definition, structural signature, count)
2. Full assignment table (Codelist_Code, Codelist_Name, Assigned_Category, Confidence, Note)
3. Structural observations (5 specific questions — this is the analytically rich section)
4. What external information would sharpen the analysis

**Important**: Do not seed the analysis with the 10 categories from prior work. The discovery should be genuinely inductive. If the AI finds 8 categories, or 13, that is valid output.

Save the Step 1 output as `SDTM_CT_Category_Discovery.md` and stop. **Do not proceed to Step 2 in the same conversation** — Step 2 takes the saved file as input in a new conversation. Running both steps in one conversation will exceed context limits.

---

### Step 2 — Archetype Table

Read the full prompt from: `references/prompt_2_archetype.md`

Paste the Step 1 output (Sections 1 and 2) into the `[INSERT PROMPT 1 OUTPUT]` placeholder. **Run this analysis directly — reason over the Step 1 output yourself. Do NOT use the Anthropic API, do NOT build artifacts.**

The prompt generates four outputs:
1. Archetype table — one row per category, including `Archetype_Behavior` (the critical column)
2. Machine-actionability ranking with justifications
3. Gap analysis table — what would need to change in CDISC publishing for full machine-actionability
4. Sanity check on Step 1 assignments

---

### Step 3 — Deliver

Write output directly to files — do not print the full analysis content to the chat. A brief summary in the chat is fine (category count, confidence breakdown, one key finding), but the full content goes in the file.

**Conversation 1 delivers two files:**

`SDTM_CT_Category_Discovery.md` — all four sections of the Step 1 output. This is the reasoning artifact — what categories were found and why. Present for download.

`SDTM_CT_Category_Discovery_assignments.csv` — one row per codelist, 1,181 rows. This is produced at the end of Step 1 when every codelist has been assigned. It is a Step 1 output, not Step 2 — the assignment work happens during discovery, not during archetype synthesis. Columns: `Code`, `CDISC_Submission_Value`, `Codelist_Name`, `Codelist_Extensible`, `Assigned_Category`, `Confidence`, `Note`. Do not skip this file.

**Conversation 2 delivers one file:**

`SDTM_CT_Archetype_Table.md` — all four Step 2 outputs. This is the synthesis artifact — one row per category, plus machine-actionability ranking, gap analysis, and sanity check. Present for download.

If the user wants an Excel version of the archetype table, generate it with openpyxl — one sheet, one row per category, columns matching the archetype table.

---

## Key decisions and their rationale

**Why filter to codelist headers?** Term-level rows add volume but not structural information for categorization. The codelist name, definition, extensibility flag, and NCIt C-code at the header level contain everything needed. Terms are needed for specific analyses (e.g. NCIt coverage per term) but not for this structural categorization task.

**Why inductive, not pre-defined categories?** The 10-category taxonomy from prior work is a hypothesis, not ground truth. Running discovery inductively produces a result that can honestly be shared with the CDISC community as "what we found," not "what we expected to find." The two may converge — that's a meaningful finding too.

**Why two prompts, not one?** Step 1 output is a citable artifact — the discovery reasoning should be inspectable before it gets synthesized into a table. Also prevents the archetype table from back-influencing the category assignments.

---

## Design philosophy — staying within the data

This skill is deliberately self-contained. It takes a publicly available file (NCI EVS SDTM Terminology) and derives conclusions strictly from what is observable in that file: codelist names, definitions, extensibility flags, submission values, and NCIt C-codes.

This is intentional. The common objection to AI-assisted standards analysis is "AI just invents things." The counter is architectural: give the AI well-structured input, constrain it to reason only from what is present, and require it to cite the observable property that supports each classification decision. The output is then verifiable — anyone with the same input file can check every assignment.

The two prompts enforce this:
- Prompt 1 prohibits pre-seeded categories and requires a structural signature (observable properties) for every category named
- Prompt 2 requires Archetype_Behavior to be grounded in what the consuming system can actually observe, not assumed clinical knowledge

The gap analysis (Prompt 2, Output 3) is where the limits become productive: it identifies what additional information *would* be needed for fully automated reasoning — making the boundaries of what AI can reliably do explicit rather than glossed over.

---

## References

- `references/prompt_1_discovery.md` — Full Prompt 1 text
- `references/prompt_2_archetype.md` — Full Prompt 2 text

**Input file:** NCI EVS SDTM Terminology (tab-delimited text)
Direct URL: `https://evs.nci.nih.gov/ftp1/CDISC/SDTM/SDTM%20Terminology.txt`
Always resolves to the current release. No login required.
