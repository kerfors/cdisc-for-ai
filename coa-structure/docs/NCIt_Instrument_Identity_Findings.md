# NCIt Instrument Identity — Probe Findings

**Date:** 2026-04-12  
**Context:** Exploration of whether NCIt structural classes can provide machine-actionable instrument identity for SDTM CT instrument codelists.  
**Branch:** `explore/coa-structure`  
**Status:** Findings only. No architectural proposal.

---

## What we tested

Whether two NCIt structural classes — C20993 ("Research or Clinical Assessment Tool") and C211913 ("CDISC QRS Instruments Questions") — can serve as anchors for machine-actionable instrument identity linked to SDTM CT codelists.

SDTM CT contains 359 instrument codelists (TESTCD lists for QS, FT, RS domains). Each codelist groups the test codes for one assessment instrument. The question: can we reliably link each codelist to its instrument identity in NCIt?

## What we found

### Three disconnected NCIt branches

NCIt holds instrument-related content in three separate branches with no machine-traversable links between them:

| Branch | What it holds | Link to SDTM CT codelists |
|---|---|---|
| **C20993** — Research or Clinical Assessment Tool | 2,208 descendants. Mix of instrument type categories (Questionnaire, Scale, Score, Index...) and individual instrument concepts. Depths 1–4. | None. Name matching only. |
| **C211913** — CDISC QRS Instruments Questions | 365 question containers, each grouping NCIt question concepts | Structural — walk children, match to TESTCD NCIt codes → codelist. 97% coverage, 1:1. |
| **CDISC Terminology** branch | Codelist-level NCIt codes (e.g., C67153 for "ADAS-Cog CDISC Version Test Code") | These codes are NOT descendants of C20993 or C211913. Dead end for structural linking. |

### C211913 → Codelist: structural and reliable

354 of 365 question containers (97%) map 1:1 to a codelist by walking their NCIt children and matching against TESTCD NCIt codes. No name matching needed. This is the strongest structural link available.

However, C211913 gives you **question grouping**, not **instrument identity**. The container says "these questions belong together" but does not carry the instrument's identity (what assessment tool, what version, what type).

### C20993 → Codelist: name matching only, fragile

C20993 carries the instrument identity we want — instrument name, type, definition. But there is no structural link to SDTM CT codelists. The only bridge is matching codelist names against C20993 preferred terms.

Results by matching strategy:

| Strategy | Additional matches | Cumulative | Rate |
|---|---|---|---|
| Exact name match | 206 | 206 | 57.4% |
| Suffix stripping (remove "Questionnaire", "Scale", etc.) | 42 | 248 | 69.1% |
| Normalized (punctuation, whitespace) | 10 | 258 | 71.9% |
| Token overlap (Jaccard ≥ 0.45) | ~90 | ~348 | ~97% |

The token overlap matches are problematic. They include wrong-version and wrong-instrument matches:

- HAMD-17 → HAMD-21 (different item count)
- SF-36 → SF-8 (different form)
- PHQ-8 → PHQ-4 (different form)
- EORTC QLQ disease modules → EORTC QLQ-C30 Core (module matched to core)
- PedsQL "Version 3" → "Version 3.0" (likely same, but flagged)

These are precisely the errors that destroy instrument identity. Name similarity ≠ same instrument.

### What remains unmatched

5–9 codelists have no reasonable C20993 candidate at all (e.g., Trail Making Test, Fatigue Severity Scale, Borg CR10 Scale, Mini-Mental State Examination, Neuropathic Pain Scale). These instruments exist in clinical practice but are absent from C20993.

## The structural problem

CDISC uses NCIt for three different purposes in the instrument space:

1. **Terminology codes** — individual test codes and codelist codes (CDISC Terminology branch)
2. **Question structure** — grouping questions by instrument (C211913)
3. **Instrument classification** — what type of tool, what it measures (C20993)

These three are stored in disconnected NCIt branches. There are no role relationships, parent-child links, or cross-references connecting them. The only way to bridge them is name matching — which is inherently fragile and cannot distinguish instrument versions or variants.

This is not a data quality problem that can be fixed by improving matching algorithms. It is a structural gap in how instrument identity is represented in NCIt.

## Coverage context

For broader context on the identity vs. measurement specification gap:

- 4,183 TESTCDs across all Findings domains have NCIt concept identity (from the green track SDTM_Test_Identity work)
- Only 104 TESTCDs have COSMoS measurement specifications (Dataset Specializations)
- At the instrument level: question-container structural coverage is 97%, but instrument-type identity coverage is 72% (clean) to ~97% (with fragile fuzzy matching)

## What this does NOT say

- This does not evaluate whether C20993 or C211913 content is wrong. The content may be correct — the problem is the lack of structural links.
- This does not propose a solution. Possible directions exist (external ontologies, explicit cross-references in NCIt, a curated mapping table) but were not tested.
- This does not assess COSMoS BC categories (--CAT/--SCAT). That is a related but separate question.

## Artifacts

All probe outputs are in `coa-structure/interim/`:

- `CoA_Instrument_Mapping_Probe.csv` — 359 rows, one per codelist. Current matching state (258 matched, 101 unmatched).
- `C20993_Instrument_Hierarchy.csv` — 2,208 rows, full C20993 descendant tree.
- `C211913_Question_Containers.csv` — 365 rows, question containers with structural codelist mapping.
- `Token_Overlap_Review.csv` — 101 rows, the unmatched codelists with best token-overlap candidates and review flags.

Notebook: `coa-structure/notebooks/CoA_Instrument_Identity_Probe.ipynb`
