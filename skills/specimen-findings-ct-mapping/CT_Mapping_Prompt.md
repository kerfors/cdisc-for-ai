# Specimen-based Findings → CDISC CT Mapping Prompt

| | |
|---|---|
| **Document** | LLM prompt for specimen-based Findings CT mapping |
| **Version** | 3.0 |
| **Date** | 2026-03-17 |
| **Companion** | `Lab_SME_Curation_Guide.md` |

### Version log

| Version | Date | Changes |
|---|---|---|
| 3.0 | 2026-03-17 | First production release. Source_Specimen input column. Selected always blank (hardened). Sibling row colour → amber. Three new review notes sections (domain distribution, duplicate detection, source quality). Spec hint precedence explicit. Version log collapsed. |
| 1.0 | 2025-02-19 | Initial prompt |

---

## Reference file

`Specimen_Findings.xlsx` — read the README sheet first. It documents sheets, columns, coverage, and provenance.

---

## Task

Map each measurement term to all valid TESTCDs (Step 1), then resolve to Dataset Specialization level where COSMoS coverage exists (Step 2). Produce one output row per term × TESTCD × DS_Code combination. TESTCDs without COSMoS coverage produce one row (specification columns blank).

Scope: specimen-based Findings — LB, IS, GF, MB, MI, MS, BS, CP, PC, PP, UR.

Not all specimen-based domains have COSMoS DSSs yet — the README sheet documents current coverage. Terms mapping to domains without DSSs get TESTCD-level resolution only.

---

## Approach

This task requires clinical and biomedical knowledge, not mechanical string matching.

For each term:
1. Identify the underlying analyte, biomarker, or clinical concept
2. Search the Test_Identity sheet semantically — use the matching procedure described in the README
3. Verify every candidate against the reference file (Rule 5)
4. For matches with Has_COSMoS=Yes, resolve specification context against Measurement_Specs (Step 2)

Do NOT write a batch-processing script. Work through each term using clinical reasoning.

---

## Step 1 — Concept Resolution

### Rule 1 — Return ALL valid matches
Use the README matching procedure (NCIt PT → Synonyms → Domains → Status) for each candidate. Return every TESTCD where the term's analyte is the subject of measurement.

### Rule 2 — Sibling detection
Strip result-property suffixes from the NCIt PT to find the base analyte:

> Count · Measurement · Ratio · Percentage · Activity · Concentration · Excretion Rate

A TESTCD qualifies as Sibling only if the base analyte is the **sole subject** — numerator only. Ratios with an independent second analyte in the denominator (Leukocytes, Total Cells, Erythrocytes) are excluded unless the term explicitly implies a differential or derived context.

### Rule 3 — Panels stay as panels
Named panels (CBC with differential, SPEP, Vectra DA) → one row, Match_Type `Panel`. Do not decompose. Note expected component TESTCDs in the rationale. Flag protocol-dependent or proprietary composition.

### Rule 4 — Specimen context feeds Step 2
Specimen in the term string, Source_Specimen column, or Term_Group does not restrict TESTCD matching in Step 1 — but it makes specimen-specific result properties (excretion rate, ratio-to-creatinine) relevant Siblings to include. Specimen context is consumed in Step 2 for DS_Code resolution.

### Rule 5 — Never fabricate
Every TESTCD, TEST, NCIt C-code, NCIt Preferred Term, and DS_Code in the output must be copied verbatim from the reference file — exact spelling, punctuation, word order. Do not paraphrase, abbreviate, or reformat.

No match → one `No_Match` row with blank CT columns. If clinical knowledge suggests a match should exist but is absent from the reference file, report `No_Match` and explain the expected concept in the rationale.

### Rule 6 — Duplicate encodings
Two TESTCDs encoding the same analyte under different naming conventions (chemical vs. common name): report the systematic/chemical name as Direct, common name as Sibling. Flag in rationale.

---

## Step 2 — Specification Resolution

Runs inline for each TESTCD match where Has_COSMoS=Yes. Look up the TESTCD in Measurement_Specs.

### Spec hint parsing

Terms may carry inline specification context. Parse before matching. Precedence (highest first):

1. Explicit specimen in the term string ("Urine - Potassium" → URINE)
2. `Source_Specimen` column value (when provided)
3. `Term_Group` default specimen (Urinalysis → URINE)

| Pattern | Extracts | Example |
|---|---|---|
| "Urine - Potassium" | specimen=URINE | Explicit prefix |
| "hsCRP (quantitative)" | scale hint | Method qualifier |
| "HbA1c (IFCC, mmol/mol)" | method=IFCC, unit hint | Inline qualifiers |
| Source_Specimen=URINE | specimen=URINE | Per-term source value |
| Urinalysis group | specimen=URINE | Term_Group default |

### Resolution logic

1. Filter Measurement_Specs rows for the matched TESTCD
2. If specimen context available → narrow to matching Specimen value
3. If method/scale/unit hints available → further narrow or rank
4. Report all surviving DS_Codes

### Spec_Resolution values

| Value | Meaning |
|---|---|
| `Full` | Term resolved to specific DS_Code(s) — specimen/method context matched |
| `Partial` | DS_Codes available but spec hints could not be fully resolved — flag for SME |
| `None` | Has_COSMoS=No — TESTCD-level only, no specification available |

When a spec hint doesn't match any DSS cleanly (method COSMoS doesn't carry, unit not in Allowed_Units), report Spec_Resolution=Partial and preserve the hint in the rationale. Protocol intent should not be silently dropped.

---

## Match types

| Type | When to use |
|---|---|
| `Direct` | Term unambiguously refers to this specific test |
| `Sibling` | Same base analyte, different result property or duplicate encoding (Rule 6) |
| `Panel` | Term is a named panel — not decomposed |
| `Partial` | A specific candidate TESTCD exists but overlap is uncertain; explain in rationale |
| `No_Match` | No candidate TESTCD can be identified in the reference file |

---

## Output specification

Excel file. One row per Term × TESTCD × DS_Code. TESTCDs without COSMoS coverage get one row with blank specification columns. Sort order: Group → Term → Match_Type (Direct, Sibling, Panel, Partial, No_Match) → DS_Code.

| Column | Block | Content |
|---|---|---|
| `Term_Group` | Blue | Group label as given |
| `Term_ID` | Blue | Identifier as given |
| `Term` | Blue | Original term verbatim |
| `Source_Specimen` | Blue | Specimen from source system (when provided) |
| `Match_Count` | Green | Total rows for this term (across all TESTCDs and DS_Codes) — supports filtering |
| `TESTCD` | Green | From Test_Identity — blank for Panel and No_Match |
| `TEST` | Green | From Test_Identity — blank for Panel and No_Match |
| `NCIt_Code` | Green | From Test_Identity — blank for Panel and No_Match |
| `NCIt_Preferred_Term` | Green | The matching evidence — blank for Panel and No_Match |
| `SDTM_Domains` | Green | From Test_Identity — blank for Panel and No_Match |
| `Has_COSMoS` | Green | From Test_Identity — blank for Panel and No_Match |
| `DS_Code` | Yellow | From Measurement_Specs — blank if Has_COSMoS=No, Panel, or No_Match |
| `DS_Name` | Yellow | From Measurement_Specs — the full specialization name |
| `Specimen` | Yellow | From Measurement_Specs |
| `Method` | Yellow | From Measurement_Specs |
| `Result_Scale` | Yellow | From Measurement_Specs |
| `Allowed_Units` | Yellow | From Measurement_Specs |
| `LOINC_Code` | Yellow | From Measurement_Specs |
| `Spec_Resolution` | Yellow | Full / Partial / None |
| `Match_Type` | Grey | See table above |
| `Match_Rationale` | Grey | Brief rationale: why this TESTCD matches this term. No_Match, Panel, and Partial may need multiple sentences. |
| `Selected` | Grey | Always blank. Never pre-populate with Y, N, or any value. This column exists exclusively for SME curation decisions. |

**Row colours:** No_Match = red · Sibling = amber · Partial = amber · Panel = amber · Direct follows column block colours.

### Review notes

Companion markdown (`Review_Notes_<Group>.md`) per Term_Group:

1. **Flagged decisions** — judgement calls the SME should verify: naming convention gaps, duplicate encodings, domain surprises, ambiguous terms, unresolved spec hints. Omit straightforward matches.
2. **Panel notes** — each Panel term, composition certainty (standard / protocol-dependent / proprietary), expected component TESTCDs.
3. **No_Match summary** — each unmatched term with a one-line gap reason.
4. **Spec resolution notes** — terms where Step 2 produced Partial resolution: what matched, what didn't, what the SME should decide.
5. **Domain distribution** — when the group contains terms mapping to multiple SDTM domains, list the domain split and flag terms that appear misclassified relative to the group label.
6. **Duplicate source terms** — term pairs within the group that resolve to the same TESTCD from different source entries. List Term_IDs, names, and whether the duplication is exact (same concept) or near (different measurement forms of the same analyte).
7. **Source quality observations** — naming errors, terms misclassified relative to their group, generic placeholders requiring study-specific definition, structural taxonomy issues. These feed back to the source system owner, not the SME reviewer.
