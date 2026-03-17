# SME Guide: Mapping Specimen-based Findings to CDISC Controlled Terminology

| | |
|---|---|
| **Document** | SME curation guide for CT mapping review |
| **Version** | 3.0 |
| **Date** | 2026-03-17 |
| **Companion** | `CT_Mapping_Prompt.md` |

### Version log

| Version | Date | Changes |
|---|---|---|
| 3.0 | 2026-03-17 | First production release. Source_Specimen input column. Sibling rows now amber (visual parity with Partial/Panel). Review notes expanded to seven sections. Consolidated deliverables documented. Version log collapsed. |
| 1.0 | 2025-02-19 | Initial guide |

---

## What this guide is for

An LLM generates candidate CDISC CT mappings for your measurement terms. Your job is to **review, correct, and select** — at two levels:
1. **Concept** — is this the right TESTCD?
2. **Specification** — is this the right DS_Code (specimen, method, scale, units)?

### Companion files

| File | Purpose |
|---|---|
| `CT_Mapping_Prompt.md` | LLM prompt — paste into chat with the reference file |
| `Specimen_Findings.xlsx` | Reference file — single source of truth (produced by Specimen_Findings notebook) |
| `Review_Notes_<Group>.md` | LLM-generated review notes — start here |

### Input: your term list

Excel or structured list with: `Term_Group` (e.g., Chemistry, Hematology), `Term_ID`, and `Term` (verbatim from source). Optional: `Source_Specimen` — a per-term specimen value from the source system (e.g., BLOOD, URINE, SERUM). When present, it feeds specimen resolution in Step 2.

The reference file contains a README sheet — **read it first**. Every value in the LLM output must trace back to this file verbatim.

---

## How the LLM works

The LLM uses clinical domain knowledge, not string matching. It resolves in two steps:

**Step 1 — Concept:** matches each term against NCIt Preferred Terms, synonyms, and definitions in the Test_Identity sheet. Returns all valid TESTCDs, classifies by match type.

**Step 2 — Specification:** for TESTCDs with COSMoS coverage (Has_COSMoS=Yes), resolves specimen/method context against the Measurement_Specs sheet. Specimen precedence: term string > Source_Specimen > Term_Group default. Parses inline spec hints ("Urine - Potassium", "hsCRP (quantitative)") and matches against available DS_Codes.

**Caveats:** The LLM may miss rarely-used TESTCDs, propose semantically close but imprecise matches (review Partials), or be uncertain about panel composition. Specification resolution depends on COSMoS coverage — only a small fraction of TESTCDs have specimen-based DS_Code specifications available. Not all specimen-based domains have DSSs yet; the README sheet documents current coverage.

---

## Review workflow

### Visual signals

The output Excel uses colour to signal review priority:

| Row colour | Match types | Meaning |
|---|---|---|
| Default (column block colours) | Direct | Confirmed concept match — verify but usually accept |
| Amber | Sibling, Partial, Panel | Requires SME decision |
| Red | No_Match | No CT match found — documents the gap |

### Match types

| Type | Meaning | Your action |
|---|---|---|
| **Direct** | Unambiguous concept match | Usually select Yes |
| **Sibling** | Same base analyte, different result property or duplicate encoding | Select if your protocol collects this |
| **Partial** | Uncertain overlap — read rationale | Decide based on protocol intent |
| **Panel** | Named panel, not decomposed | No TESTCD to select; carried forward |
| **No_Match** | No CT match found | Documents the gap |

### Spec_Resolution values

| Value | Meaning | Your action |
|---|---|---|
| **Full** | DS_Code resolved — specimen/method matched | Verify the selected specification |
| **Partial** | DS_Code available but spec hints unresolved | Decide which DS_Code fits your protocol |
| **None** | No COSMoS coverage — TESTCD only | No specification to review |

### How to review

Start with the Review Notes file — it points to rows needing attention. Then work group by group.

> **Two-step workflow:** (1) Decide TESTCD — accept or reject the concept match (Selected=Yes/No). (2) For accepted TESTCDs with multiple DS_Code rows, select the specification(s) matching your protocol. Selected applies per *row* (i.e., per DS_Code), not per TESTCD.

**Concept review:**

1. **Direct** — confirm the TESTCD is what your protocol means. Watch for analytes with multiple forms (free vs. total, intact vs. total).

2. **Sibling** — the key decisions. Select TESTCDs your protocol actually measures. Common patterns: count vs. percentage, measurement vs. ratio, urine-specific result properties, and **duplicate encodings** (same substance under different naming conventions). Select per sponsor convention.

3. **Partial** — read the rationale. The LLM is uncertain; use your protocol knowledge.

4. **Panel** — verify the panel name. Decomposition is a separate operational step.

5. **No_Match** — confirm no CT equivalent exists. May need sponsor-defined extensions.

**Specification review:**

For rows with Has_COSMoS=Yes:

1. **Spec_Resolution=Full** — verify the DS_Code matches your protocol's specimen and method. If multiple DS_Codes survived filtering, select the one(s) your protocol uses.

2. **Spec_Resolution=Partial** — the LLM found DS_Codes but couldn't fully resolve the spec hints. Common reasons: method qualifier COSMoS doesn't carry, unit not in Allowed_Units, ambiguous specimen context. Check the rationale and Review Notes, then select or reject.

3. **Spec_Resolution=None** — no specification exists in COSMoS yet. The TESTCD-level mapping is still valid; specification will come when COSMoS coverage expands.

### Curation rules

- Every Direct, Sibling, or Partial row **must** have `Yes` or `No` in the Selected column. No blanks.
- Selected applies per row — when a TESTCD fans out to multiple DS_Code rows, mark each independently.
- Panel and No_Match rows may be left blank.

---

## FAQ

**Unrecognised TESTCD?** Check the Test_Identity sheet — filter by TESTCD and read the NCIt PT and definition.

**Multiple TESTCDs for one term?** Select all your protocol genuinely collects. "Basophils" in a CBC means the count; if your protocol also reports differential percentages, select the percentage TESTCD too.

**Two TESTCDs seem identical?** Duplicate encoding. Select per sponsor convention; if unsure, prefer the systematic/chemical name.

**What does Has_COSMoS=No mean?** The TESTCD is valid but COSMoS hasn't published a specimen-based specification for it yet. The vast majority of TESTCDs are in this state. The mapping is still useful — it resolves the concept. Specification will follow as COSMoS coverage grows.

**Has_COSMoS=Yes but my protocol's method/unit isn't in the DS_Codes?** This is Spec_Resolution=Partial. The TESTCD mapping is correct but COSMoS doesn't carry a DS_Code matching your exact method or unit. Accept the TESTCD; note the gap for downstream specification. Common example: microscopic counts where no method dimension exists in the available DS_Codes.

**Decompose panels?** Not here. Panel decomposition depends on your laboratory's specific panel definitions.

**Reference file currency?** Check the README sheet generation date. Re-run the Specimen_Findings notebook for newer source data.

---

## Review Notes structure

The LLM produces review notes per Term_Group (per-group during mapping, then consolidated). Seven sections:

1. **Flagged decisions** — mappings involving judgement calls: naming convention gaps, duplicate encodings, domain surprises, ambiguous terms, unresolved spec hints. Read each flag and verify the LLM's reasoning against your protocol intent.
2. **Panel notes** — each Panel term with composition certainty (standard / protocol-dependent / proprietary) and expected component TESTCDs. Verify panel names match your lab's definitions.
3. **No_Match summary** — each unmatched term with a one-line gap reason. Confirm no CT equivalent exists; flag terms needing sponsor-defined extensions.
4. **Spec resolution notes** — terms where Step 2 produced Partial resolution: what matched, what didn't, what you should decide. Focus here for specification gaps.
5. **Domain distribution** — when the group spans multiple SDTM domains, the domain split and any terms that appear misclassified relative to the group label. Informs downstream dataset allocation.
6. **Duplicate source terms** — term pairs resolving to the same TESTCD from different source entries. Feeds back to the source taxonomy owner.
7. **Source quality observations** — naming errors, misclassified terms, generic placeholders. These feed back to the source system owner, not to you as SME reviewer.
