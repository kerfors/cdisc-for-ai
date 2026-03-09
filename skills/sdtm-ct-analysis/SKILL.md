---
name: sdtm-ct-analysis
version: "2.1"
date: 2026-03-09
description: >
  Structural analysis of CDISC SDTM Controlled Terminology — discovering the semantic categories
  present in the NCI EVS SDTM Terminology file and generating category profiles.
  Use when the user wants to analyze, categorize, or understand the structure of SDTM CT,
  or wants to make SDTM CT machine-actionable.
changes: >
  v2.1: Prompt 1 refined from real run. Added primary discriminator field to category definitions.
  Added cross-category consumption profiles and specialization hierarchy questions to Section 3.
  v2.0: Simplified from v1.0. Renamed Archetype → Category Profiles. Removed redundancy
  with repo README. Flattened file structure (no references/ subfolder).
---

# SDTM CT Structural Analysis Skill

Two-step inductive analysis of a CDISC SDTM Controlled Terminology file. Takes one publicly available input file, produces outputs across two conversations.

## Input

**File:** NCI EVS SDTM Terminology, tab-delimited text.
Download: `https://evs.nci.nih.gov/ftp1/CDISC/SDTM/SDTM%20Terminology.txt`
(Always resolves to current release. No login required. Save via Cmd+S / Ctrl+S — browsers display rather than download.)

**Filtering:** The full file is ~44,000 rows. Filter to codelist-header rows before analysis:

```python
import pandas as pd

df = pd.read_csv(path, sep='\t', encoding='utf-8', dtype=str)
headers = df[df['Codelist Code'].isna() | (df['Codelist Code'] == '')]
print(f"Codelist headers: {len(headers)} rows")
```

This gives ~1,200 rows — all that is needed for structural categorization.

## Step 1 — Category Discovery (Conversation 1)

Read the prompt from: `prompt_1_discovery.md`

Run against the filtered codelist-header data. **Read the rows into context and reason over them directly.** Do not use the Anthropic API, do not build React artifacts, do not batch-process. This is a reading and reasoning task.

The analysis is inductive — categories emerge from the data. Do not seed with prior categories.

**Outputs — write to files, not to chat (brief summary in chat is fine):**

| File | Content |
|---|---|
| `SDTM_CT_Category_Discovery.md` | Category definitions, full assignment reasoning, structural observations |
| `SDTM_CT_Category_Discovery_assignments.csv` | One row per codelist: `Code`, `CDISC_Submission_Value`, `Codelist_Name`, `Codelist_Extensible`, `Assigned_Category`, `Confidence`, `Note` |

Record the SDTM CT release version (from the source file header or filename) in the output markdown. NCI EVS publishes new releases roughly quarterly — the version makes results reproducible.

**Stop here.** Do not proceed to Step 2 in the same conversation — context limits.

## Step 2 — Category Profiles (Conversation 2)

Read the prompt from: `prompt_2_profiles.md`

Upload the Step 1 Discovery markdown. Run the profile analysis directly — same constraint as Step 1.

**Outputs:**

| File | Content |
|---|---|
| `SDTM_CT_Category_Profiles.md` | Profile table, machine-actionability ranking, gap analysis, sanity check |

## Constraints

These apply to both steps:

1. **Observable data only.** Every category and assignment must be justified by properties visible in the input columns. No clinical domain knowledge to fill gaps.
2. **Full file required.** Alphabetical slices produce skewed results — instrument codelists dominate early alphabet. Use all ~1,200 headers.
3. **Inductive.** If the data supports 8 categories, report 8. If 13, report 13. Do not force a pre-determined count.
