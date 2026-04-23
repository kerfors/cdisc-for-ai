# sdtm-narrative — open work

*Forward-looking brief. Carries forward Open Decisions §5–6 from the Step 3 plan (retained under [`archive/COSMoS_Narrative_Layer_Plan.md`](archive/COSMoS_Narrative_Layer_Plan.md)) plus items surfaced during template authoring.*

*cdisc-for-ai, 2026-04.*

---

## 1. Build sequence — 3d in progress

Record doc settles the build order as Tier 3 first: the three case-pair DataBooks drive template validation, Tier 2b paragraph assembly follows.

- **3d in progress.** Notebook `30_assemble_databooks.ipynb` produces markdown DataBooks for Glucose, 6MWT, X-Ray. Build order: Glucose (exercises Templates 01 + 04), 6MWT (Template 02 including the NCIt ancestry band), X-Ray (Templates 03 + 04 together).
- **Template validation happens inside 3d.** Each regenerated DataBook must match the reference HTML story's factual content.
- **3c after 3d.** Notebook `20_assemble_narrative.ipynb` produces the `Narratives` sheet in `COSMoS_Graph_Narrative.xlsx`, one paragraph per DSS, once templates are validated on the three rich cases.
- **3e validation.** `40_validate_narrative.ipynb` round-trips every narrative fact against the graph; flags fabrication; confirms template coverage. Output: `reports/narrative_validation_report.{md,json}`.
- **3f close-out.** Audit in `reports/narrative_layer_audit.md`; `CLAUDE.md` three-layer model updated to name Tier 2b and Tier 3 as first-class artefacts.

## 2. `COSMoS_Graph_Flat.xlsx` band-4 round-trip — not produced

Templates 01/02/03 band 4 (Tier 3 only) and `00_index.md` L103 name `cosmos-graph/interim/COSMoS_Graph_Flat.xlsx` as the source for the flattened-row key-value grid that closes each case page. The file does not exist in `cosmos-graph/interim/`. The assembler in `30_assemble_databooks.ipynb` emits a "round-trip file not yet produced" stub at each band-4 location in the three current DataBooks.

Decision needed: produce `COSMoS_Graph_Flat.xlsx` (re-introduce a flattener or build fresh from the graph sheets) vs. rewire templates' band 4 to read `COSMoS_Graph.xlsx` sheets directly. Favour the former if other consumers will want a flat view; the latter keeps the graph as the single source of truth for band 4.

## 3. §5 — Promotion paths (from Plan Open Decisions)

Three sub-questions, all deferred until Tier 2b templates are validated through 3c.

- **(a) Variable identity location.** Does `sdtm-narrative/reference/SDTM_Variable_Identity.xlsx` stay in this track, or promote to `sdtm-test-codes/machine_actionable/` alongside `SDTM_Test_Identity.xlsx` and `SDTM_Instrument_Identity.xlsx`?
- **(b) Narratives sheet promotion.** Does the `Narratives` sheet stay in `sdtm-narrative/interim/COSMoS_Graph_Narrative.xlsx`, or merge into `cosmos-graph/interim/COSMoS_Graph.xlsx` as a new sheet?
- **(c) Track identity.** Does `sdtm-narrative/` stay as its own delivery track, or fold into `cosmos-graph/` if the Narratives sheet promotes?

## 4. §6 — NCIt enrichment scope

Minimal for first cut: `AssignedTerms` in `COSMoS_Graph_CT.xlsx` already carries NCI CT definitions for 1,170 concept IDs. That is the starting budget. Extended enrichment (synonyms, UMLS, LOINC) lifted only if a specific template needs it and the need survives a read of the HTML story reverse-engineering.

Trigger: a template authored in 3c/3d surfaces a substitution that requires a synonym / UMLS / LOINC lookup not covered by the current identity files.

## 5. Case-specialisation registry location

Template 04 is authored; the registry file it reads is not. Reference story data (`Glucose_StudyIntent_Story.html`, `XRay_PatientBurden_Story.html`) lives inline in HTML, not in a structured file. Three candidate locations:

- `sdtm-narrative/reference/case_specialisations.xlsx` — exploratory home in this track.
- `cosmos-graph/interim/COSMoS_Graph.xlsx` new sheet `Case_Specialisations` — promotion target if the case registry earns first-class graph status.
- Sponsor-local — if case knowledge is sponsor-scope rather than standards-scope, the graph carries only a pointer.

Decision deferred until Glucose_StudyIntent and XRay_PatientBurden Tier 3 DataBooks are built and validated. Tied to §3(a)–(c).

## 6. What's closed

For context, so the items above read as what remains.

- **§3a variable identity.** `SDTM_Variable_Identity.xlsx` built in two passes (Pass A covers 338/449 COSMoS variables; Pass B adds 9 via full-Thesaurus lookup). Compositional fallback covers the remaining 102 without expanding subset scope.
- **§3b template catalogue.** Four templates authored under `reference/templates/` (specimen-based Findings, instrument-based Findings, cross-Domain_Class composition, case-specialisation overlay). Five-band skeleton abstracted in `00_index.md`.
- **§3b design decisions.** Tier 2b grain = per-DSS paragraph; Tier 3 unit = per case pair; build order Tier 3 first; markdown canonical with HTML view. Settled 2026-04-23.
