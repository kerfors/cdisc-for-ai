# COSMoS Flattener — Enhancement Brief

**Purpose.** Carry-over brief for a new conversation. Motivates and specifies an enhancement to the `cosmos-bc-dss/` processing track, based on learnings from three real-world case pairs (Glucose, 6MWT, X-Ray).

**Scope.** The interim artefact `cosmos-bc-dss/interim/COSMoS_BC_DSS.xlsx` (1,768 rows, one per BC/DSS, in the `BC_DSS` sheet). Currently produced by the notebooks in `cosmos-bc-dss/notebooks/`. This brief proposes concrete column changes plus a companion sheet. It does not propose abandoning the flat format.

---

## Context — what the current flattener does

The flattener aggregates the COSMoS source:
- BC header (from `cdisc_biomedical_concepts_latest.xlsx`)
- DSS header (from `cdisc_sdtm_dataset_specializations_latest.xlsx`)
- VLM rows (typically 9–14 per DSS) — the variable-level metadata that jointly constrains the recording case

…into **one row per DSS** with ~35 columns in `BC_DSS`. Columns include BC identity, DSS identity, Domain/Domain_Class, Result_Scale, Specimen, Method, location, laterality, evaluator, units, LOINC, Hierarchy_Path, Categories.

**Design value driving the flattening:** both humans and LLMs consume language-like flat rows better than normalised joined tables. One row carries the story of one DSS; no join required to understand what the DSS is. This is a real design value, not a limitation — any enhancement must preserve it.

---

## Theoretical grounding — reification-as-legibility

The design move this brief recommends is consistent with the argument in Kurt Cagle & Chloe Shannon, *Why LLMs Can't Read Your Graph (And What To Do About It)*, Inference Engineer (Substack), 2026-04-21. Key claims from the article, adapted here because they reframe the flattener problem:

**1. LLM "graph reasoning failures" are legibility failures, not reasoning failures.** Flat triple serialisations (the kind `BC_DSS.xlsx` currently approximates at DSS grain) are structurally impoverished compared to natural-language prose. The LLM has been trained to navigate proposition-embedding-proposition structures at every scale — sentence, paragraph, discourse. Raw triples look like nothing in its training corpus.

**2. Natural language is itself a deeply reified graph.** Every ordinary sentence — *"The court ruled that it was unlikely Mary was correct in believing John had said the cat sat on the mat"* — is a five-level propositional embedding. LLMs recognise this pattern and can navigate it. A flat triple serialisation strips all embedding out.

**3. The fix is reification, not normalisation.** Structural enrichment via RDF-star-style annotation (assertions about assertions), named graphs (subgraph framing), provenance/confidence/temporality/scope qualifiers, and prose context around structured data blocks. The article's phrase: *"The fix isn't to bolt symbolic reasoning onto a language model. It's to make knowledge grammatical."*

**4. Two use cases, two serialisations.** The article explicitly argues for maintaining a canonical flat form for machine-reasoning pipelines AND generating LLM-facing serialisations with deeper reification. The article's recommended LLM-delivery format is **DataBooks** — prose narrative with embedded structured data, where the prose provides the reification depth that bare triples lack.

**Implication for cdisc-for-ai.** The repo already has three natural serialisation tiers — they just haven't been named as tiers:

| Tier | Artefact | Consumer | Reification depth |
|---|---|---|---|
| 1. Canonical | COSMoS source xlsx; companion `VLM_Rows` long-format sheet (proposed) | pandas, SPARQL-like queries, validation pipelines | Low (flat, relational) |
| 2. Flat-enriched | `BC_DSS` sheet with the column enhancements proposed below | LLM context-loading, human browsing | Medium (in-row qualifier structure, coverage flags, cross-reference prose) |
| 3. DataBook | `docs/*.html` case stories (Glucose, 6MWT, X-Ray pairs) | LLM-facing analysis, human documentation, architectural reference | High (prose narrative with embedded structured fact blocks) |

The HTML case stories we've built intuitively for human readers are, in the article's framing, exactly the right LLM-delivery format. The flattener enhancement closes the gap at Tier 2 — a mid-reification-depth tier between raw source and full DataBook.

**Design posture.** Every enhancement proposed below is measured against the test: *does this make a fact that was previously flat-serialised into something that reads like a proposition embedded in a larger propositional structure?* Where a current column says `"X-RAY;MRI"` ambiguously, the enhanced form renders it as *"permits X-RAY or MRI as modality"* — structurally a proposition embedded in a description of the DSS, recognisable to the LLM's learned patterns.

---

## What the three case pairs revealed

### Pair 1 — Glucose (LB, specimen-based Findings)
Files: `docs/Glucose_COSMoS_Story.html`, `docs/Glucose_StudyIntent_Story.html`

**What the flattener handled:** specimen (PLASMA), standard unit (mmol/L), category (CHEMISTRY), LOINC mapping — all captured as flat column values.

**What was lost:** the 12-row VLM detail on LB.LBTESTCD — roles (Topic/Qualifier/Timing), mandatory flags, assigned vs slot status, codelist subsets (`LBFAST` is a slot with NY_NY subset). The interim file carries only aggregate metadata, not the per-variable spec.

**What was out of scope entirely:** the case-specialisation layer (FPG, OGTT 2-hour, OGTT fasting) — the layer where study-design intent composes DSS with external trial-design objects.

### Pair 2 — 6MWT (FT, instrument-based Findings)
Files: `docs/6MWT_COSMoS_Story.html`, `docs/6MWT_NCIt_Story.html`

**What the flattener handled:** the per-DSS template — similar across sub-tests, captured reasonably at flat level.

**What was lost:** the classification structure — instrument family → instrument codelist → tests within codelist. The `Hierarchy_Path` column is a string; it doesn't support traversal. Sibling tests within the same instrument codelist are not addressable at flat level.

**The asymmetry vs Glucose:** Glucose has uniform classification but rich recording-spec variation (8 DSSs per BC). 6MWT has uniform recording spec but rich classification structure. Flattener is tuned for one pattern, awkward for the other.

### Pair 3 — Chest X-Ray (PR procedures + MK findings)
Files: `outputs/XRay_COSMoS_Story.html`, `outputs/XRay_PatientBurden_Story.html`

**What the flattener handled:** DSS identity, Method value_list for MK (X-RAY;MRI), Domain_Class distinction (Interventions vs Findings).

**What was lost or ambiguous:**
- **Cross-domain-class joins.** Same concept (X-Ray, NCIt C38101) appears as identity-pin in PR DSSs (XRAYCHEST pins PRDECOD=X-RAY) and as qualifier-value in MK DSSs (SGBESCR has MKMETHOD value_list including X-RAY). No way to traverse "find all DSSs related to X-Ray concept" in one query.
- **Assigned-vs-slot ambiguity.** `Method = "X-RAY;MRI"` in the flat row is ambiguous — pin or slot? Method = "X-RAY" alone equally ambiguous.
- **Qualifier coverage matrix.** Audit discovered that POSITION (C71148) IS modelled as a VLM slot in 40 DSS rows (31 in EG, 9 in VS with restricted value_lists like `PRONE;SEMI-RECUMBENT;SITTING;STANDING;SUPINE`), but NOT in any imaging DSS (PR/MK/TR/TU — zero rows). The flat file has no way to surface this coverage asymmetry; required custom scripts to detect.
- **Non-generic VLM variables.** RADIATIONCANCER and RADTHERAPHYBREASTCANCER carry 14 VLM rows including PRINDC, PRDOSE, PRDOSU, PRTRTSTT (Treatment Setting codelist C124308), PRTRTINT (Treatment Intent codelist C124307). Invisible in the flat row; looks identical to XRAYCHEST's 9-row flattened row.

**The SoA-burden use case** (driver for this analysis): a burden calculator needs to distinguish "Standing PA Chest X-Ray" from "Supine Portable Chest X-Ray" because burden profiles differ. Both resolve to XRAYCHEST DSS. The discriminator (POSITION) is a CDISC-CT-governed codelist with 17 terms, but unreachable from the flat row.

---

## The tension, stated

**Structurally optimal** target: COSMoS is graph-shaped. Nodes: BC, Hierarchy_Node, TESTCD, DSS, VLM_Row, SDTM_Variable, CT_Codelist, CT_Term, Case_Spec. Edges: isa, covers, instantiates, has_vlm_row, types_to, assigns, permits, restricts_to, specializes. A property graph answers every question the three pairs raised in one or two hops. The long-term "traversable graph" goal stated in `CLAUDE.md` is this target.

**Language-like optimal** format: one row per DSS, each column readable as a fact, semicolon-separated lists for ordered associations within a field. An LLM loads one row and understands one DSS; a human browses without schema knowledge.

**Apparent tension.** A graph doesn't flatten. A flat row doesn't traverse. Previous thinking defaulted to "abandon flat → go multi-sheet normalised → graph-later". But that breaks the language-like consumption contract that motivated the current design.

**Resolution.** The flat row can be MORE structurally expressive without abandoning the one-row-per-DSS contract. The current flat row is flat-but-impoverished — too few columns, several ambiguous. A richer flat row can carry materialised-graph facts as readable values.

---

## Proposed enhancement — richer flat rows + companion structured sheet

### Move 1 — Split every ambiguous qualifier column into a mode/pinned/allowed triple

Current `Method` column conflates three distinct facts: pinned value, slot with value_list, absent. Replace with:

| Column | Values | Meaning |
|---|---|---|
| `Method_Mode` | `pinned` / `slot` / `slot+subset` / `absent` | what kind of fact |
| `Method_Pinned` | single CT term, e.g. `X-RAY` | populated when mode=pinned |
| `Method_Allowed` | semicolon-separated list, e.g. `X-RAY; MRI` | populated when mode=slot or slot+subset |

Apply same pattern to every qualifier slot: Specimen, Method, Position (new, see Move 3), Location, Laterality, Evaluator. Also LBFAST-type flag qualifiers.

**Why it works language-like:** each column is still a readable text value. Filters become precise (`Method_Mode=pinned AND Method_Pinned=X-RAY` answers "DSSs that pin X-ray as modality"). LLM consumption is sharper because the mode column disambiguates.

### Move 2 — Add TWO VLM-content columns: compact grammar + prose narrative

The reification-as-legibility argument makes the case for carrying the VLM in two complementary forms — one compact and machine-parseable, one prose and LLM-native.

**2a. `VLM_Summary` — invented-grammar encoding.**

One string encodes the per-variable spec:

```
XRAYCHEST VLM_Summary:
  PRTRT=slot(text,Y,Y,Collected);
  PRDECOD=pin:X-RAY[PROCEDUR](Y,Y);
  PRLOC=pin:CHEST[LOC](N,N);
  PRPRESP=slot:Y[NY](N,N);
  PROCCUR=slot:N|Y[NY](N,N);
  PRCAT=open(N,N); PRSCAT=open(N,N);
  PRSTDTC=timing(N,N); PRENDTC=timing(N,N)
```

Grammar sketch (to finalise during implementation):
- `<variable>=<mode>[:<value>][<codelist>](<mandatory_var>,<mandatory_val>)`
- Modes: `pin`, `slot`, `slot+subset`, `open`, `timing`
- Value: pinned term, or pipe-separated value_list, or omitted for open
- Codelist: CDISC-CT submission value in brackets
- Mandatory: Y/N pair

This gives a compact, grepable, machine-parseable encoding. Round-trips cleanly to structured form for QC. It is flat-tier-optimal for *content density per token*.

**2b. `VLM_Narrative` — one-paragraph prose description.**

One to three English sentences per row, describing what the DSS asserts, how it constrains the record, and what it does NOT say. Example for XRAYCHEST:

> XRAYCHEST is a COSMoS Dataset Specialization on PR.PRTRT that pins PRDECOD to X-RAY (from the CDISC CT PROCEDUR codelist, C101858) and PRLOC to CHEST (from the CDISC CT LOC codelist, C74456), applicable when the chest X-ray procedure is pre-specified in the protocol (PRPRESP=Y). PRTRT captures the verbatim investigator-reported procedure name as the Topic variable; timing is carried by PRSTDTC and PRENDTC. The DSS does not bind patient position or acquisition view — those qualifiers are not modelled for this imaging procedure.

Example for SGBESCR:

> SGBESCR is a COSMoS Dataset Specialization on MK.MKTESTCD that pins MKTESTCD to SGBESCR and MKTEST to Sharp/Genant Bone Erosion Score (CDISC CT MUSCTSCD codelist, C127269; MUSCTS codelist, C127270), producing an ordinal radiographic damage score on a 0–3.5 scale. The DSS permits either X-RAY or MRI as the acquisition method via a restricted MKMETHOD value_list (codelist C85492 METHOD), and permits RIGHT or LEFT laterality via MKLAT. The DSS does not bind patient position.

**Why two forms, not one.** The article's reification claim is that LLMs navigate propositional structures — "a thing is said to be true, and something further is said about that saying" — more fluently than flat structures. `VLM_Narrative` renders each DSS as a miniature reified description: the DSS asserts X about variable V, the DSS constrains W to a codelist, the DSS does not address Q. This is the structural shape the model's learned probability landscape is trained on.

`VLM_Summary` remains because it round-trips to structured form for validation, enables quick pattern filters, and carries more information per token. `VLM_Narrative` is what the LLM will actually read and reason over. Having both is cheap (both derive from the same VLM rows in one notebook pass) and gives both consumer classes what they need.

**Generation approach.** `VLM_Narrative` is template-assembled per DSS from the VLM rows, with templates per domain-class and per qualifier pattern. It is not LLM-generated — deterministic assembly from source facts, so QC round-trips and no hallucination risk. Templates will evolve as new patterns are encountered (one template per Domain_Class to start: Findings, Interventions, Events, Special-Purpose).

**2c. Render SDTM variable names and codelist names as natural-English concepts in `VLM_Narrative`.**

This is the single largest legibility win in the enhancement. SDTM variable tokens (`LBFAST`, `MKMETHOD`, `PRTRT`, `MKPOS`) appear in CDISC documentation but not at scale in the LLM's broad training corpus. Their natural-English concept names (*fasting status*, *method of measurement*, *reported name of procedure*, *position of subject*) appear in general clinical prose millions of times. The same fact, rendered in either token, invokes very different regions of the model's learned probability landscape.

Applied to the XRAYCHEST narrative:

*Tier 2a — VLM_Summary (compact, SDTM-lingo, round-trippable):*
```
PRTRT=slot(text,Y,Y,Collected);
PRDECOD=pin:X-RAY[PROCEDUR](Y,Y);
PRLOC=pin:CHEST[LOC](N,N);
PRPRESP=slot:Y[NY](N,N); …
```

*Tier 2b — VLM_Narrative without generalisation (what 2b above proposed):*
> XRAYCHEST is a COSMoS Dataset Specialization on PR.PRTRT that pins PRDECOD to X-RAY (from the CDISC CT PROCEDUR codelist) and PRLOC to CHEST (from the CDISC CT LOC codelist), applicable when PRPRESP=Y. PRTRT captures the verbatim investigator-reported procedure name as Topic; timing is carried by PRSTDTC and PRENDTC.

*Tier 2b — VLM_Narrative with generalisation (Move 2c):*
> XRAYCHEST is a COSMoS Dataset Specialization for recording chest X-ray procedures. It fixes the *standardised procedure name* to "X-Ray" (from the CDISC Procedure vocabulary) and the *anatomical location* to "Chest" (from the CDISC Anatomical Location vocabulary), applicable when the procedure is pre-specified in the protocol. The *verbatim reported procedure name* is captured as the Topic variable; procedure *start and end times* are recorded. The DSS does not address *patient position* or *acquisition view*.

**Canonical source for the mapping.** The NCIt Variable Terminology (CDISC Variable Terminology and CDISC Root Variable Terminology subsets of NCIt Thesaurus) carries curator-assigned natural-language names for every SDTM variable — authoritative, governed, not interpreted. Examples already verified in the repo's `Thesaurus.txt`:

| SDTM variable | NCIt code | Natural-English name |
|---|---|---|
| `PRTRT` | C117511 | Reported Name of Procedure |
| `PRDECOD` | (CDISC Var Term) | Standardized Procedure Term |
| `PRLOC` | (CDISC Var Term) | Anatomical Location of Procedure |
| `LBFAST` | (CDISC Var Term) | Fasting Status |
| `MKMETHOD` | (CDISC Var Term) | Method of Test or Examination |
| `MKPOS` | (CDISC Var Term) | Position of Subject |
| `VSPOS` | (CDISC Var Term) | Vital Signs Position |

For codelists, the natural name is the codelist header Name (already in the SDTM CT file). The rendering convention in narrative is *CDISC &lt;Header Name&gt; vocabulary* — e.g., `PROCEDUR` → *CDISC Procedure vocabulary*, `LOC` → *CDISC Anatomical Location vocabulary*, `POSITION` → *CDISC Body Position vocabulary*.

**Build path.** Extend the existing NCIt identity enrichment in `sdtm-test-codes/` (currently scoped to TESTCDs) to also cover variables, by selecting Thesaurus rows with subset `CDISC Variable Terminology` or `CDISC Root Variable Terminology`. Output: an `SDTM_Variable_Identity.xlsx` or equivalent join table carrying `<variable, NCIt_code, natural_name>`. The flattener notebook then joins this table when assembling `VLM_Narrative` to substitute SDTM tokens with natural names.

**Round-trip contract is preserved.** Tier 1 (`VLM_Rows`) and Tier 2a (`VLM_Summary`) keep `LBFAST`, `MKMETHOD`, `PRDECOD` — these are the identifiers. Tier 2b (`VLM_Narrative`) and Tier 3 (DataBooks) use *fasting status*, *method*, *standardised procedure name* — these are the concept names. Parsers operate on Tier 1/2a; LLMs read Tier 2b/3. No information is lost; each tier is optimal for its consumer.

**Trade-off, noted.** Natural-English names are longer than SDTM tokens. `VLM_Narrative` cells will be larger than `VLM_Summary` cells. Acceptable — the narrative tier trades density for legibility by design.

### Move 3 — Add coverage-status columns for qualifier dimensions that vary per DSS

Add columns `Position_Status`, `View_Status`, `Contrast_Status`, `Fasting_Status`, with values `pinned` / `slot` / `slot+subset` / `absent`. These make what a DSS DOESN'T say into first-class facts.

Example: POSITION coverage across known DSS classes

| DSS | Domain | Domain_Class | Position_Status |
|---|---|---|---|
| XRAYCHEST | PR | Interventions | absent |
| CTSCANCHEST | PR | Interventions | absent |
| SGBESCR | MK | Findings | absent |
| LDIAM | TR | Findings | absent |
| DIABP | VS | Findings | slot+subset |
| HR | VS | Findings | slot+subset |
| AVCOND | EG | Findings | slot |

Now "which imaging DSSs lack position binding" is `Position_Status=absent AND Domain_Class IN (Interventions, Findings imaging)` — one filter. The architectural gap the X-Ray burden story identified becomes a standing report, not a custom script.

**Start with POSITION** since it motivated this analysis. Expand to other qualifier dimensions as they are surfaced by new case pairs.

### Move 4 — Add cross-reference columns, with reified descriptions

Preserve relations as materialised-in-row values. Each cross-reference column comes in two flavours: a compact code list for filtering, AND a reified description for LLM consumption.

| Compact column | Narrative column | Example compact / narrative |
|---|---|---|
| `Sibling_DSSs_Same_BC` | `Sibling_DSSs_Same_BC_Narrative` | `XRAY; CTSCAN; CTSCANCHEST; MRI; MRIBRAIN; RADIATIONCANCER; RADTHERAPHYBREASTCANCER` / *"The X-Ray Imaging BC (NCIt C38101) is instantiated as eight PR DSSs: XRAY (unconstrained location), XRAYCHEST (location pinned to CHEST), CTSCAN, CTSCANCHEST, MRI, MRIBRAIN (location pinned to BRAIN), plus two radiation-therapy DSSs that share PRTRT as vlm_source."* |
| `Same_Concept_Other_Domains` | `Same_Concept_Other_Domains_Narrative` | `SGBESCR(MK); LDIAM(TR)` / *"The X-Ray concept also appears as a permitted MKMETHOD value in MK Sharp/Genant and Sharp/Van der Heijde scoring DSSs (one of two allowed methods, alongside MRI) and as one of 15 permitted TRMETHOD values in TR RECIST 1.1 measurement DSSs. In MK and TR the concept is a qualifier on the measurement; in PR it is the measurement identity itself."* |
| `Sibling_Tests_In_Instrument` | `Parent_Instrument_Narrative` | `TENMW101; TENMW102; TENMW103; …` / *"This test code belongs to the 10-Meter Walk/Run Functional Test instrument codelist (C141657), alongside TENMW101 through TENMWnnn — tests that share the instrument framing and its administration protocol but differ in the specific measurement."* |
| `Case_Specializations` | `Case_Specializations_Narrative` | `ID001=FPG; ID002=OGTT-2H; ID003=OGTT-FASTING` / *"Three protocol-specific case specialisations are authored over this DSS: Fasting Plasma Glucose (ID001, pins LBFAST=Y); OGTT 2-Hour Plasma Glucose (ID002, pins LBFAST=N and binds LBTPTREF to a protocol-defined challenge event); OGTT Fasting Baseline (ID003, pins LBFAST=Y and binds LBTPTREF to the same challenge event)."* (populated when a case-spec registry exists) |

**Why the reified narrative matters.** Compact lists (`SGBESCR(MK); LDIAM(TR)`) are filter-friendly but epistemically flat — the reader doesn't know whether X-Ray plays the same role in MK and TR as it does in the current DSS. The narrative form embeds the role: *qualifier on the measurement in MK, qualifier in TR, measurement identity in PR*. That embedding is a proposition about a proposition — the exact shape the LLM's learned language patterns navigate best.

**Why keep both compact and narrative.** Compact for pandas filtering and programmatic consumers; narrative for LLM consumption. One pass through the VLM rows produces both. Same data, two serialisations, different reification depths — the two-use-cases-two-serialisations principle applied at column grain.

### Move 5 — Add a companion `VLM_Rows` sheet (structured long-format)

Not a replacement for the flat row — an additional sheet for programmatic consumers who want to do pandas-style analysis. Shape identical to the COSMoS DSS source with `package_date`, `bc_id`, `domain`, `vlm_group_id`, `sdtm_variable`, `role`, `assigned_value`, `codelist`, `value_list`, `mandatory_variable`, `mandatory_value`, `data_type`, `origin_type`, `origin_source`.

This is essentially preserving the source structure as a companion view. Enables queries like "all VLM rows where codelist=C71148" (all POSITION bindings across all DSSs) that the flat row can't cheaply answer even with Move 3.

**Two views of the same underlying data, optimised for two different readers**: flat BC_DSS for language-model and human consumption; structured VLM_Rows for programmatic analysis. Both derived from the same source in one notebook pass.

### Move 6 — Add a Coverage_Matrix sheet (derived pivot)

Optional third sheet: DSS × observed-qualifier pivot. Rows are DSS codes. Columns are every qualifier variable that appears in any DSS's VLM (PRDECOD, MKMETHOD, VSPOS, LBFAST, …). Cell values: `pin:<value>` / `slot:<codelist>` / `slot+subset:<value_list>` / `—`.

Turns the audit I had to write scripts for into a standing artefact. One glance at the POSITION column shows which domains bind it.

---

## Implementation notes

### Non-destructive migration

- Existing columns stay unchanged where unambiguous (BC identity, domain, unit metadata).
- Ambiguous columns (Method, Specimen, etc.) get the mode/pinned/allowed triple added; the original column can stay as a compatibility shim for one release if downstream consumers read it directly.
- New columns are additive.
- Consumer tracks (`sdtm-findings/`, `sdtm-domain-reference/`) may need adjustments to read from the new mode columns, but the structural grain (one row per DSS) is unchanged — most joins will work.

### Source-of-truth

All new columns and the companion `VLM_Rows` sheet are derived in a single pass over `cosmos-bc-dss/downloads/cdisc_sdtm_dataset_specializations_latest.xlsx`. The VLM-row grain is already there; the current notebook just collapses it. The enhancement is to collapse *smarter* and also emit the long-format view.

### QC

- For each DSS, verify VLM_Summary round-trips to the source VLM (emit → parse → compare).
- For each qualifier coverage column, verify cell values are consistent with the mode/pinned/allowed triple.
- Coverage_Matrix counts reconcile with VLM_Rows aggregations.

### Notebook conventions (per `CLAUDE.md`)

- Generate .ipynb via Python's json module.
- 4-space indentation.
- Build cells as dicts, use json.dump(indent=1, ensure_ascii=False).
- Clear markdown cells explaining each transformation step.
- No fabricated data — every column derives from actual COSMoS source rows.

### Documentation

- Update `cosmos-bc-dss/README.md` to describe the new sheets and columns.
- Update the `README` sheet inside the xlsx with a mode/pinned/allowed legend, a VLM_Summary grammar guide, and a `VLM_Narrative` template catalogue.
- Add a short doc in `cosmos-bc-dss/docs/` explaining the design rationale — why richer-flat instead of normalised, citing the three case pairs and the reification-as-legibility argument from the Inference Engineer article.

---

## Formal three-tier serialisation strategy

The enhancement is part of a broader serialisation architecture that should be explicitly named in repo documentation. Each tier serves a distinct consumer with a distinct reification depth:

**Tier 1 — Canonical / low reification.**
- `cosmos-bc-dss/downloads/*.xlsx` (COSMoS source)
- `cosmos-bc-dss/interim/COSMoS_BC_DSS.xlsx` — `VLM_Rows` sheet (proposed companion long-format)
- Consumer: pandas pipelines, validation scripts, graph loaders, programmatic QC
- Shape: normalised relational, one fact per row, machine-friendly joins

**Tier 2 — Flat-enriched / medium reification.**
- `cosmos-bc-dss/interim/COSMoS_BC_DSS.xlsx` — `BC_DSS` sheet with the column enhancements proposed in Moves 1-6
- Consumer: LLM context-loading for bulk analysis, human spreadsheet browsing, downstream consumer tracks (`sdtm-findings/`, `sdtm-domain-reference/`)
- Shape: one row per DSS, rich columns including `VLM_Summary` (compact grammar) and `VLM_Narrative` (prose), mode/pinned/allowed triples, coverage-status flags, reified cross-reference columns

**Tier 3 — DataBook / high reification.**
- `docs/*.html` case stories (Glucose_COSMoS_Story, Glucose_StudyIntent_Story, 6MWT_COSMoS_Story, 6MWT_NCIt_Story, XRay_COSMoS_Story, XRay_PatientBurden_Story, future additions)
- Consumer: LLM-facing architectural analysis, human documentation, design reviews, curator onboarding
- Shape: prose narrative with embedded structured fact blocks (VLM tables, codelist chip-rows, NCIt-hyperlinked concept codes) — the paradigmatic "DataBook" shape described in the Inference Engineer article

**Why name the tiers.** Each tier has a different acceptance test. Tier 1 is correct if it round-trips to source. Tier 2 is correct if each row's enriched columns are derivable from source and QC-verified. Tier 3 is correct if the narrative is accurate against source AND the narrative does not fabricate facts. Naming the tiers makes the QC expectations explicit per artefact class.

**Relation to the long-term graph goal.** The `CLAUDE.md` statement that the long-term goal is "a traversable graph; flat files are today's delivery format" should be amended: the traversable graph IS the union of Tier 1 (canonical structured) and Tier 3 (reified narrative), with Tier 2 as the LLM-optimised projection in between. Tier 3 is not a stopgap; it is the LLM-facing face of the graph.

---

## Design principle, one line

> The flat-row principle is right. The current columns are too few and too ambiguous to carry what COSMoS actually says. Enrich the row with reified structure — grammar-encoded in `VLM_Summary`, prose-encoded in `VLM_Narrative`, reified cross-references — so each row reads as a proposition about a DSS rather than a flat record of a DSS. Make knowledge grammatical.

---

## Reference artefacts (for the implementer)

- `cosmos-bc-dss/downloads/cdisc_sdtm_dataset_specializations_latest.xlsx` — DSS source (sheet: `SDTM Dataset Specializations`, 32 columns, one row per VLM entry)
- `cosmos-bc-dss/downloads/cdisc_biomedical_concepts_latest.xlsx` — BC source
- `cosmos-bc-dss/interim/COSMoS_BC_DSS.xlsx` — current flattened interim (to be enhanced)
- `docs/Glucose_COSMoS_Story.html` — Pair 1 reference
- `docs/Glucose_StudyIntent_Story.html` — Pair 1 reference, case-specialisation layer
- `docs/6MWT_COSMoS_Story.html` — Pair 2 reference
- `docs/6MWT_NCIt_Story.html` — Pair 2 reference
- `outputs/XRay_COSMoS_Story.html` — Pair 3 reference (not yet in repo due to branch sync)
- `outputs/XRay_PatientBurden_Story.html` — Pair 3 reference, SoA burden gap

---

*Brief authored 2026-04-21 from the conversation that audited the three case pairs and surfaced the POSITION coverage gap in imaging DSSs. Updated 2026-04-22 to incorporate the reification-as-legibility argument from Kurt Cagle & Chloe Shannon, "Why LLMs Can't Read Your Graph (And What To Do About It)", The Inference Engineer (Substack), 2026-04-21 — which reframes the flat-vs-normalised tension as a legibility-vs-reification question and validates the direction of the proposed enhancements while suggesting deeper reification via prose narrative columns, natural-English generalisation of SDTM variable names in the narrative tier, and a named DataBook tier.*
