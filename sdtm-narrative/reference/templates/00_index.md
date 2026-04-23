# COSMoS Narrative Layer — Template Catalogue

*Catalogue of prose templates used to assemble Tier 2b (per-DSS paragraph)
and Tier 3 (case-pair DataBook) narratives from the COSMoS graph.
Reverse-engineered from the six HTML case-pair stories under `docs/`.*

*cdisc-for-ai, 2026-04-23*

---

## Status

3b in flight. Four templates identified from the six reference stories;
authoring one markdown entry per template. Templates are catalogue-
level specifications, not code — they describe what facts the
assembler reads, what prose it emits, and what substitutions and
traversals it performs.

Catalogue entries:

- [`01_specimen_based_findings.md`](01_specimen_based_findings.md) —
  LB, MB, MI, CP, BS, MS, PC, PP. Reference story:
  `docs/Glucose_COSMoS_Story.html`.
- [`02_instrument_based_findings.md`](02_instrument_based_findings.md) —
  QS, FT, RS. Reference stories: `docs/6MWT_COSMoS_Story.html` (DSS
  grain) and `docs/6MWT_NCIt_Story.html` (NCIt composition ancestry).
- [`03_cross_domain_class.md`](03_cross_domain_class.md) — one BC
  binding DSSs across two Domain_Class values. Reference story:
  `docs/XRay_COSMoS_Story.html` (MK + PR).
- [`04_case_specialisation.md`](04_case_specialisation.md) — overlay
  pattern: a DSS refined by a case-specialisation registry entry.
  Reference stories: `docs/Glucose_StudyIntent_Story.html` and
  `docs/XRay_PatientBurden_Story.html`.

Grain decisions settled in
[`../../docs/COSMoS_Narrative_Layer.md`](../../docs/COSMoS_Narrative_Layer.md):
§1 per-DSS paragraph for Tier 2b; §2 per case pair for Tier 3. Same
catalogue drives both tiers — paragraph templates are a subset of
DataBook templates.

## Common skeleton

All four templates share a five-band skeleton, with bands 4 and 5
optional per pattern. Band 1 and band 3 are the Tier 2b paragraph;
bands 2, 4, 5 promote the paragraph into a Tier 3 DataBook.

1. **Prose opener.** One sentence naming the DSS, the BC it realises,
   and the clinical object of the proposition. Slot-filled from
   `DSS.DS_Code`, `DSS.DS_Name`, parent `BC.BC_ID`, parent `BC.BC_Name`.
2. **Legend band** *(Tier 3 only)*. Node-type key for the tree view
   that follows. Values are literal strings from the story CSS:
   `cosmos-bc`, `sdtm-ct`, `cosmos-dss`, `cosmos-dss-iv`,
   `flattened-row`, `test-identity-row`, `measurement-specs-row`,
   `case-spec`, `ext-ref`, `ncit-class`, `ncit-container`, `ncit-instr`,
   `retired`.
3. **Tree traversal.** The DSS as an embedding proposition, with the
   variables it pins, the slots it leaves open, the attributes it
   carries (Specimen, Method, Result Scale, Allowed Units, Standard
   Unit, LOINC, vlm_source, SDTMIG since). Template-specific slots
   vary by pattern — see each entry.
4. **Flattened row** *(Tier 3 only)*. The same DSS rendered as the
   machine-actionable row shape (fields verbatim from
   `COSMoS_Graph_Flat.xlsx`). Establishes round-trip between the
   narrative and the flattened reference file.
5. **Registry-need band** *(Tier 3 only)*. The argument the story
   makes about what the COSMoS graph does not yet formalise — a
   specimen-test qualification registry, an instrument composition
   registry, a case-specialisation registry, a burden-aware overlay
   registry. Frames the gap, does not fill it.

Bands 1 and 3 collapse into the Tier 2b paragraph. Bands 2, 4, 5
elevate the paragraph into a DataBook entry.

## Natural-English substitutions — two-tier rule

All templates resolve SDTM variable codes to natural language using
`sdtm-narrative/reference/SDTM_Variable_Identity.xlsx`. The file
covers 347 of 449 COSMoS variables directly (77%); the remaining 102
are prefix-composed root forms (`MKMETHOD`, `FTDTC`, `GFTESTCD`, etc.)
which NCIt's Variable Terminology subsets do not enumerate per domain.

**Tier 1 — direct lookup.** If `variable` appears in the identity
table with a non-root `subset` value, use `natural_name` and
`definition` from that row.

**Tier 2 — compositional fallback.** If no direct hit, strip the
leading two characters (the domain prefix) and look up the remainder
against rows where `subset = Root`. Assemble the natural name as
domain-scoped root — e.g. `MKMETHOD` → the MK domain's `--METHOD`,
natural-name *"method of measurement"*. The definition comes from the
root row; the domain prefix is prepended to the name if the surrounding
prose needs domain context.

This folds identity coverage to 100% without expanding the NCIt-subset
scope of the identity file. It also matches how SDTMIG actually
models these variables — as root plus domain prefix, not as standalone
identities.

## Read-only inputs (every template)

- `cosmos-bc-dss/interim/COSMoS_Graph.xlsx` — sheets `BC`, `DSS`,
  `Variables`, `AssignedTerms`, `Categories`, `Codelists`.
- `cosmos-bc-dss/interim/COSMoS_Graph_Flat.xlsx` — flattened rows
  for band 4 (Tier 3 only).
- `sdtm-narrative/reference/SDTM_Variable_Identity.xlsx` —
  variable-to-natural-name substitution table.
- `sdtm-test-codes/machine_actionable/SDTM_Test_Identity.xlsx` —
  TESTCD identity for opener-band proposition.
- `sdtm-test-codes/downloads/Thesaurus.txt` — NCIt definitions
  where `AssignedTerms` lacks them.

## Write targets

Per the design record §4, markdown is canonical. HTML is a rendered
view, not a source of truth.

- Tier 2b paragraphs → `sdtm-narrative/interim/COSMoS_Graph_Narrative.xlsx`,
  sheet `Narratives`, one row per DSS. Paragraph text in column
  `VLM_Narrative`.
- Tier 3 DataBooks → `sdtm-narrative/machine_actionable/databooks/<case>.md`
  (canonical) plus `<case>.html` (rendered view).
