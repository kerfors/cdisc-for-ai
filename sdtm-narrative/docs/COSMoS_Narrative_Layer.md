# COSMoS Narrative Layer — Design Record

*Decision record for Step 3 of the cosmos-bc-dss rework. Captures the
3b open decisions resolved on 2026-04-23 and will grow into the Step 3
design record at close-out (analogous to
`cosmos-graph/docs/COSMoS_Flattener_Rewrite.md`).*

*cdisc-for-ai, 2026-04-23*

---

## Status

Step 3 in flight. Folder skeleton under `sdtm-narrative/` created per
the plan. 3b template-design decisions settled (this document); 3a
variable-identity build and 3b template-catalogue authoring are the
next moves.

Plan: [`COSMoS_Narrative_Layer_Plan.md`](COSMoS_Narrative_Layer_Plan.md).

## Decisions settled (3b)

### §1 — Tier 2b grain: per-DSS paragraph

One paragraph per DSS (1,326 rows, matches the `DSS` sheet grain).
Per-variable phrases are an assembler intermediate, not a published
grain. The paragraph is the proposition about the DSS; per-variable
phrases are slots inside it.

*Rationale.* The DSS is the unit of clinical legibility — a story is
told about what this specification binds, what it does not bind, what
siblings it has, what case specialisation it carries. Per-variable
grain fragments that proposition and misses the Cagle & Shannon
reification argument the Step 2 brief rests on.

### §2 — Tier 3 unit: one DataBook per case pair

One DataBook per case (Glucose, 6MWT, X-Ray to start). Matches the
grain of the existing HTML stories, which are the ground truth for
what "good" looks like. Domain_Class and structural-type grains stay
available as later aggregation views if needed — not as the first-cut
deliverable.

*Rationale.* The HTML stories are the specification of the template.
Any grain coarser than case-pair loses the cross-domain-class framing
(X-Ray PR+MK) and the case-specialisation framing (Glucose study
intent) that those stories already demonstrate. Template reverse-
engineering needs the grain to match.

### §3 — Build order: Tier 3 first

The three case-pair DataBooks drive the template catalogue; Tier 2b
paragraph assembly follows once templates are validated on rich cases.

*Rationale.* The HTML stories exist. They are the concrete target.
Reverse-engineering the template from a known-good output is less
speculative than inventing a template for 1,326 DSSs and then checking
it. Bulk QC surface arrives later, but the templates QC'd on rich cases
are the ones that will assemble the 1,326 paragraphs without
fabrication.

### §4 — Tier 3 output format: Markdown canonical, HTML view

`.md` is the committed artefact (git-diffable, template-round-trippable,
machine-actionable in the sense the repo uses the term). `.html` is
rendered from the markdown as a view for browser reading — matches
the existing story look and feel, but is not the source of truth.

*Rationale.* Markdown diffs cleanly across regenerations; HTML
templating is verbose and couples prose to CSS. Keeping markdown
canonical lets the DataBooks sit alongside the graph xlsx as
first-class reference files. The HTML render is a cheap downstream.

## Deferred

### §5 — Exploratory-vs-promoted paths

Deferred to Step 3 close-out, as the plan specifies. Three sub-
questions (variable-identity location, Narratives-sheet placement,
folder-track identity) all wait for Tier 2b templates to be validated
before commitment.

### §6 — NCIt enrichment scope

Provisionally: minimal for first cut. `AssignedTerms` already carries
NCI CT definitions for 1,170 concept IDs; that is the starting budget.
Extended enrichment (synonyms, UMLS, LOINC) lifted only if a specific
template needs it and the need survives a read of the HTML story
reverse-engineering.

## Implications for the build

Implied sequencing from these four decisions:

1. **3a — variable identity** runs next, feeding both tiers.
2. **3b — template catalogue** is authored by reverse-engineering from
   the six HTML case-pair stories under `docs/` and `outputs/`. One
   entry per Domain_Class + role pattern, per the plan's §3b
   deliverable shape.
3. **3d — Tier 3 assembly** runs before 3c, producing markdown
   DataBooks for Glucose, 6MWT, X-Ray. Template validation happens
   here.
4. **3c — Tier 2b assembly** runs once templates are validated, emitting
   one paragraph per DSS into
   `sdtm-narrative/interim/COSMoS_Graph_Narrative.xlsx/Narratives`.
5. **3e — validation** and **3f — close-out** as in the plan, with §5
   resolved at that point.

The numbering in the plan (3a → 3f) reflected topic, not time; the
execution order above reflects §3.

## Template catalogue — shape

Settled by the decisions above, restated for clarity. Catalogue lives
under `sdtm-narrative/reference/templates/`, one entry per
Domain_Class + role pattern. Each entry carries:

- **Facts read** from the graph (DSS row, Variables rows, AssignedTerms
  rows, sibling DSSs, instrument parent, case-specialisation pointer).
- **Prose form emitted** as markdown fragments with named slots.
- **Natural-English substitutions** applied via
  `SDTM_Variable_Identity.xlsx` (variable → natural name, definition).
- **Traversals required** (siblings, cross-domain-class,
  instrument parent, case specialisation).

Same catalogue drives Tier 2b (paragraph, per DSS) and Tier 3
(DataBook, per case pair). Paragraph templates are a subset of
DataBook templates — the case DataBook composes multiple paragraph-
scope templates into a story.

## 3a findings — variable identity coverage

Pass A (two primary subsets): 338 / 449 COSMoS variables covered.
Pass B (full-Thesaurus lookup, 3a-bis): +9 rows (2 from CDASH Variable
Terminology, 7 from concepts with no Variable Terminology subset flag).
Final: **347 / 449 = 77 %** of COSMoS variables carry direct NCIt
identity.

The remaining 102 unresolved COSMoS variables are almost all
**prefix-composed root variables** — domain-instantiated forms like
`MKMETHOD`, `FTDTC`, `GFTESTCD`, `URMETHOD`. NCIt's Variable Terminology
subsets do not enumerate every domain × root combination; they provide
the root forms (`--METHOD`, `--DTC`, `--TESTCD` — already in Pass A
under `Subset = Root`) and expect compositional assembly at the
consumer.

**Implication for 3b (template catalogue).** The natural-name
substitution rule should be two-tier:

1. Direct hit. If the variable is in the identity table with a non-root
   subset, use its `Natural_Name`.
2. Compositional fallback. If not, strip the leading two characters
   and look up the remainder against the Root-subset identity. Assemble
   the natural name as domain-scoped root (e.g. `MKMETHOD` → the MK
   domain's `--METHOD`, natural name *"method"*).

This folds identity coverage back to 100 % without expanding the
NCIt-subset scope of the identity file itself. It also matches how
SDTMIG actually models these variables — as root + domain prefix, not
as standalone identities.

## 3b findings — template catalogue drafted

Four templates authored under `sdtm-narrative/reference/templates/`,
one per Domain_Class + role pattern identified across the six HTML
case-pair stories:

- `01_specimen_based_findings.md` — LB, MB, MI, CP, BS, MS, PC, PP.
  Grounded in `docs/Glucose_COSMoS_Story.html`.
- `02_instrument_based_findings.md` — QS, FT, RS. Grounded in
  `docs/6MWT_COSMoS_Story.html` (DSS grain) and
  `docs/6MWT_NCIt_Story.html` (instrument composition ancestry).
- `03_cross_domain_class.md` — composition rule for BCs whose DSSs
  span multiple Domain_Class values. Grounded in
  `docs/XRay_COSMoS_Story.html` (MK + PR).
- `04_case_specialisation.md` — overlay pattern for study-intent,
  patient-burden, and other case registries. Grounded in
  `docs/Glucose_StudyIntent_Story.html` and
  `docs/XRay_PatientBurden_Story.html`.

Each entry documents the four catalogue sections required by the
plan: facts read from the graph, prose form emitted (markdown
fragments with named slots), natural-English substitutions (two-tier
rule, direct identity / compositional fallback), traversals required.
A five-band common skeleton is abstracted in `00_index.md`:
(1) prose opener, (2) legend, (3) tree traversal, (4) flattened row,
(5) registry-need band. Bands 2/4/5 are Tier 3 only; bands 1/3
collapse into the Tier 2b paragraph.

Two templates carry composition rules rather than standalone prose:
Template 03 wraps Templates 01/02 for cross-Domain_Class BCs;
Template 04 overlays on top of a parent-DSS Template 01/02 rendering.
This matches the HTML stories — `StudyIntent` and `PatientBurden` are
not rewrites of `COSMoS`, they are overlays.

**Registry-need inventory.** Four distinct registry gaps emerged
across the templates — specimen-test qualification, instrument
composition, cross-domain composition, case specialisations. The
first three are framed in bands 5 of Templates 01-03; the fourth
*is* Template 04's output shape. Template 04's own registry location
(xlsx under `sdtm-narrative/reference/` vs. promoted sheet in
`COSMoS_Graph.xlsx` vs. sponsor-local) stays deferred under §5.

## Open items for the next working session

- Start 3d: notebook `60_assemble_databooks.ipynb`. First DataBook
  targets are the three cases the catalogue was reverse-engineered
  from (Glucose, 6MWT, X-Ray). Build order: Glucose (exercises
  Templates 01 + 04), 6MWT (exercises Template 02 including the
  NCIt ancestry band), X-Ray (exercises Template 03 + 04 together).
- Template validation happens as part of 3d — each DataBook
  regenerated from the graph via the catalogue must match the
  reference HTML story's factual content.
