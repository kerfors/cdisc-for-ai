# sdtm-findings-graph — SDTM Findings consumer, graph-fed

Consumer-facing reference files for Findings, joined from the COSMoS graph
projection and SDTM identity tracks. Sub-typed by structural pattern: specimen,
measurement, instrument. Each sub-type produces a workbook
(`Test_Identity`, `Measurement_Specs`, `Axis_Meaning`) designed for study design,
SoA-to-CDISC mapping, and USDM integration.

This track is the graph-fed canonical Findings consumer, having replaced
the legacy `sdtm-findings/` track retired May 2026.

> **Reference versions** — built on SDTM CT 2026-09-25 and COSMoS BC/DSS
> 2026-07-14. See [`../docs/Changes_2026-10.md`](../docs/Changes_2026-10.md) for
> what changed in the latest release.

## Pipeline position

```
sdtm-test-codes/SDTM_Test_Identity.xlsx ──────────┐
sdtm-domain-reference/SDTM_Domain_Metadata.xlsx ──┤
cosmos-graph/interim/COSMoS_Graph_CT.xlsx ────────┼── sdtm-findings-graph/
consumer-bases/interim/DSS_View.xlsx ─────────────┘                    │
                                                                       │
                              sdtm-findings-graph/machine_actionable/
                                  ├── Specimen_Findings.xlsx
                                  ├── Measurement_Findings.xlsx
                                  └── Instrument_Findings.xlsx
```

## Scope discipline

**In scope.** Editorial decisions a Findings consumer owns: sub-typing
(specimen vs measurement vs instrument), behavioural exclusions (IS, GF,
UR), the LOINC grain decision, the NCIt graph-vs-reference disagreement
surface, the `Allowed_Units` codelist expansion, the wider TESTCD universe
self-join (the coverage-gap framing). Final column shape per sub-type is
designed fresh — not ported from the legacy track.

**Out of scope.** Joins already done by `consumer-bases/`: BC ↔ DSS, the
Variables slot pivot (pin and value_list), AssignedTerms enrichment. Source extraction belongs
to `cosmos-graph/`.

**Read sources.** The consumer reads the graph projection and
`consumer-bases/DSS_View.xlsx`. No other COSMoS source — the historical
`cosmos-bc-dss/interim/COSMoS_BC_DSS.xlsx` flatten was retired May 2026
along with its legacy consumer.

## Notebooks and outputs

| Notebook | Sub-type | Scope | Output |
|---|---|---|---|
| `Specimen_Findings.ipynb` | Specimen | LB, MB, MI, CP, BS, MS, PC, PP (IS, GF, UR excluded) | `machine_actionable/Specimen_Findings.xlsx` |
| `Measurement_Findings.ipynb` | Measurement | VS, EG, MK, CV, RE | `machine_actionable/Measurement_Findings.xlsx` |
| `Instrument_Findings.ipynb` | Instrument | QS, FT, RS | `machine_actionable/Instrument_Findings.xlsx` |
| `Scope_Check.ipynb` | — | Release check, run before the three above | Fails when a domain with CT test codes or COSMoS DSSs is missing from `SDTM_Domain_Metadata.xlsx` or is not a domain code in the CT SDTM Domain Abbreviation codelist (C66734) |

Scope is not listed in code. Each notebook reads it from `SDTM_Domain_Metadata.xlsx`
(`Specimen_Based`, `Measurement`, the `Instrument_Domain_Rules` sheet) and removes the
exclusions it names, with their reasons. A domain classified in the metadata enters
its consumer when content arrives; the domains above are the scope at SDTM CT 2026-09-25
and COSMoS 2026-07-14.

## Inputs (shared)

| File | Track | Content |
|---|---|---|
| [`DSS_View.xlsx`](../consumer-bases/interim/DSS_View.xlsx) | consumer-bases | Joined view: `Test_Identity` (COSMoS-pinned TESTCDs), `Measurement_Specs` (DSS-grain, BC + Coding + Variables slot pivot — pin and value_list) |
| [`SDTM_Test_Identity.xlsx`](../sdtm-test-codes/machine_actionable/SDTM_Test_Identity.xlsx) | sdtm-test-codes | Domain-level test codes with NCIt identity. Used to widen `Test_Identity` beyond DSS_View's COSMoS-pinned subset. |
| [`SDTM_Domain_Metadata.xlsx`](../sdtm-domain-reference/machine_actionable/SDTM_Domain_Metadata.xlsx) | sdtm-domain-reference | Domain metadata. `Observation_Class` joined per row. `Variable_Meaning` rows that apply to the file copied into `Axis_Meaning`. |
| [`COSMoS_Graph_CT.xlsx`](../cosmos-graph/interim/COSMoS_Graph_CT.xlsx) | cosmos-graph | `CodelistTerms` sheet — drives the `Allowed_Units` permissible-value expansion (`ORRESU_codelist` → terms). |

For the instrument sub-type, when added:

| File | Track | Content |
|---|---|---|
| `SDTM_Instrument_Identity.xlsx` | sdtm-test-codes | One row per instrument codelist; dual NCIt anchors (C20993 instrument + C211913 container). |
| `SDTM_Instrument_Test_Identity.xlsx` | sdtm-test-codes | Test codes within instrument codelists, with NCIt identity. |

## File structure

Specimen and measurement outputs are three-sheet workbooks:

- **`Test_Identity`** — one row per TESTCD. Concept-level identity.
- **`Measurement_Specs`** — one row per Dataset Specialization. Variant-level
  measurement detail (specimen, method, scale, units, coding). In
  `Specimen_Findings` (LB, MB, MI) also an observable key per DSS, built from
  `Axis_Meaning`: `Observable_Key` (`bc_id | component | system | scale | method`,
  NCIt codes except scale), `Observable_Key_Label`, `Key_Shared_With`,
  `Key_Positions`. Scale uses units present or absent; its per-DSS reading is open.
- **`Axis_Meaning`** — our position on what the axis columns of `Measurement_Specs`
  mean for the observable: the rows of `Variable_Meaning` in
  `SDTM_Domain_Metadata.xlsx` that apply to the file (Position, Basis, Status),
  with the columns each row refers to. Not a published fact; the basis note for
  each row is in `Variable_Meaning`. A variable without a row: no position taken.

Link key between sheets: TESTCD + NCIt code. TESTCD alone is a mnemonic, reused
across domains for unrelated tests (MCH in LB and MB, MV in MK and RE); COSMoS
coverage is joined on both. The two-step
structure matches the mapping workflow: first resolve a term to a concept,
then select the specific measurement variant.

Instrument output is a five-sheet workbook — adds `BC_Categories` and
`BC_Parents` to the three-sheet base. The two extra sheets carry COSMoS's
search-tag mechanism and the BC parent-child traversal explicitly. They
are needed because instrument grouping operates outside the BC parent
chain — the instrument-level BC and the wrapper concepts (e.g., `6 Minute
Walk Functional Test` C115789 vs. `6MWT Functional Test Question` C115409)
sit in disjoint NCIt trees connected only through shared category tags.
The two-sheet skeleton would force consumers to derive these joins; the
two extra sheets make them addressable directly. See
[`6MWT_COSMoS_Story.html`](../docs/archive/case-studies-2026-04/6MWT_COSMoS_Story.html) and
[`6MWT_NCIt_Story.html`](../docs/archive/case-studies-2026-04/6MWT_NCIt_Story.html) (archived April 2026 snapshots).

Column shape inside each sheet is designed fresh per sub-type, leveraging
DSS_View's native columns (snake_case, `bc_*` prefixes for BC identity,
`Coding_<system>` for external codings, `<remainder>_value` /
`<remainder>_ncit` / `<remainder>_codelist` / `<remainder>_value_list` / `<remainder>_value_list_ncit` for Variable slot pivots).
Legacy column names are not preserved.

Header colour convention (per repo standard): green = TESTCD / SDTM-CT-side,
yellow = COSMoS-side, chocolate = instrument (NCIt C20993), copper =
container (NCIt C211913), grey = keys, blue = our position (`Axis_Meaning`,
as `Variable_Meaning` in `SDTM_Domain_Metadata.xlsx`).

## Behavioural exclusions

Sub-typing follows the March 2026 analysis, archived in
[`docs/archive/behavioural-analysis-2026-03/`](../docs/archive/behavioural-analysis-2026-03/COSMoS_Behavioural_Analysis.md).
The exclusions and their reasons are recorded in the `Consumer_Exclusions`
sheet of `SDTM_Domain_Metadata.xlsx`, each reason stated as testable claims;
[`domain-behaviour/`](../domain-behaviour/) evaluates them on every COSMoS release.
As they stand now:

- **Specimen sub-type — IS excluded.** Decomposes by target, not specimen:
  the DSSs of one BC differ by binding agent (`BDAGNT`). The March 2026
  analysis found the target only in `DS_Code`.
- **Specimen sub-type — GF excluded.** Decomposes by test detail (`TSTDTL`),
  not specimen. The March 2026 analysis recorded it as scale-driven.
- **Specimen sub-type — UR excluded.** Zero decomposition despite the
  `Specimen_Based` metadata flag. Behaviourally identical to
  Domain-specific Findings.
- **Measurement sub-type — no exclusions.** EG was excluded until
  2026-10-01 (all BCs marked `Qualitative` with units present on a sizeable
  share). Since the COSMoS 2026-05-26 package its scales are Nominal (no
  units) or Quantitative (with units), so the reason no longer holds.

## Consumer-owed design decisions

Decisions the consumer owns, surfaced once and applied uniformly across
sub-types where they fire:

- **LOINC grain.** DSS_View carries LOINC at BC grain (`Coding_http://loinc.org/`,
  `Coding_https://loinc.org`) and at DSS grain (`LOINC_value` from the
  Variables slot pivot, when a domain pins a `<DOM>LOINC` variable). The consumer
  chooses BC-only, DSS-only, or coalesce. Decision documented in each
  sub-type notebook header.
- **NCIt graph/reference disagreement.** DSS_View flags TESTCDs where the
  graph and the reference disagree on the NCIt concept (TUMERGE, TUSPLIT —
  TU sub-type, out of scope here). Surface or filter is decided in the
  measurement and instrument builds.
- **`Allowed_Units` expansion.** `ORRESU_codelist` carries a codelist
  submission value; the consumer expands it against
  `COSMoS_Graph_CT.xlsx::CodelistTerms` to produce the permissible-value
  list per DSS.
- **TESTCD universe widening.** DSS_View's `Test_Identity` is
  COSMoS-pinned-only. The consumer self-joins `SDTM_Test_Identity.xlsx` to
  widen to the full sub-type-scoped universe — this is what supports the
  coverage-gap framing.
- **Domain class join.** `SDTM_Domain_Metadata.Observation_Class` is joined
  per row. The view does not carry it.

## Coverage gap and sponsor content

Identity coverage and measurement-spec coverage are two different things.
Specimen domains have substantial SDTM CT identity (thousands of TESTCDs
across LB, MB, and the rest of the in-scope set) but only a small subset
has COSMoS Dataset Specializations. The remainder carries standardized
identity (TESTCD, NCIt concept, synonyms, definition) but no operationalized
measurement detail (specimen, method, units, LOINC).

For laboratory tests in particular, sponsors often maintain internal lab
catalogues that already carry exactly this operational detail. The
`Test_Identity` sheet provides the standardized anchor: TESTCD and NCIt
code are the join keys. Where COSMoS publishes DSSs, use them. Where it
has not, sponsors map their internal catalogue against `Test_Identity` to
bridge their operational content to the CDISC identity layer.

## Folder layout

- `notebooks/` — Jupyter notebooks, one per sub-type. The processing logic.
- `machine_actionable/` — Final outputs. The deliverables.
- `reports/` — QC and parity reports (added per sub-type as built).
- `docs/` — Per-sub-type design notes if needed; the README otherwise.

Folders not present:

- `downloads/` — N/A. Reads only repo artefacts.
- `interim/` — N/A initially. Added if a sub-type spawns a reusable
  intermediate worth keeping visible.
- `pre-2026-03/`, `diffs/` — N/A initially. Added when the first release
  boundary is taken.

## Cross-references

- [`consumer-bases/`](../consumer-bases/) — upstream view track. Owns the
  join layer this consumer reads.
- [`cosmos-graph/`](../cosmos-graph/) — upstream graph track. Owns source
  projection and CT enrichment.
- [`COSMoS_Behavioural_Analysis.md`](../docs/archive/behavioural-analysis-2026-03/COSMoS_Behavioural_Analysis.md) — behavioural rationale for sub-typing and exclusions (March 2026, archived).
- Repo-root [`CLAUDE.md`](../CLAUDE.md) — repo conventions.
