# domain-behaviour — how does each domain behave?

`domain-behaviour/` re-derives, from the published COSMoS content, the behaviour that
the Findings consumers' scope decisions rest on, and reports where content and
decisions disagree. It is the March 2026 behavioural analysis
([`docs/archive/behavioural-analysis-2026-03/`](../docs/archive/behavioural-analysis-2026-03/))
made reproducible: run it on every COSMoS release and compare with the previous run.

It reports only. Scope and classification stay in
[`SDTM_Domain_Metadata.xlsx`](../sdtm-domain-reference/machine_actionable/SDTM_Domain_Metadata.xlsx):
the `Domains` flags and the `Consumer_Exclusions` sheet, whose claims this notebook tests.
It also checks the hand-kept `Variable_Meaning` sheet (our position, section 4f): keys and fixed lists only.
Nothing reads from this track.

The notebook also publishes the result as a page,
[`docs/analyses/domain-behaviour.html`](../docs/analyses/domain-behaviour.html), linked
from the [landing page](https://kerfors.github.io/cdisc-for-ai/) and rewritten on every run.

## Notebook and output

| Notebook | Output |
|---|---|
| [`notebooks/Domain_Behaviour.ipynb`](notebooks/Domain_Behaviour.ipynb) | [`interim/Domain_Behaviour.xlsx`](interim/Domain_Behaviour.xlsx) |

| Sheet | Grain | Content |
|---|---|---|
| `Domain_Profile` | domain | Size, fan-out, primary axis, scale mix, variable shares; metadata class and consumer status |
| `Fanout_Axes` | BC with more than one DSS | Which axes distinguish its DSSs |
| `Key_Compare` | BC with more than one DSS | The fan-out axes against the observable key of `COSMoS_Observable_Derivation` |
| `Variable_Evidence` | variable × domain | What COSMoS, SDTM CT, the SDTM v2.0 Model and SDTMIG v3.4 publish about each variable that differs between the DSSs of one BC |
| `Consumer_Key_Compare` | key group that differs | The observable key of `Specimen_Findings` against the derivation's key, for the same DSSs |
| `IG_Assumptions` | numbered SDTMIG v3.4 domain assumption | Assumptions in our Findings domains that name one of our variables, quoted as extracted |
| `LOINC_Compare` | BC with more than one DSS and a LOINC code | The fan-out axes against the LOINC axes that differ between its DSSs |
| `LBCAT_LOINC_Class` | LBCAT × LOINC class | LB DSSs with a LOINC code, by assigned category and LOINC class |
| `Rater_Evidence` | instrument codelist | CT class and the phrases in the NCIt definition that name who completes or rates it |
| `Rater_COSMoS_EVAL` | `--EVAL` / `--EVALID` × assigned value | DSSs and BCs in QS, FT, RS |
| `Rater_Class_Moves` | instrument whose class changed | Class in the prior and current SDTM CT, with the rater phrases in its NCIt definition |
| `Scale_Units` | domain × published result-scale combination | DSSs with and without units; flags |
| `Exclusion_Claims` | claim in `Consumer_Exclusions` | Holds or not, with the evidence |
| `Unclassified_Content` | domain | Domains with DSSs but no consumer class |
| `Key_Measures`, `Pins` | — | Measures for the release diff (`PRIOR_FILE`); input versions |

## Axes

An axis is a variable whose value can differ between the DSSs of one BC: specimen,
method, binding agent, test detail, location, category, evaluator. An axis is counted
when the assigned value differs; where only the value list differs, it is reported in
`Axes_Value_List_Only`. `scale` is read from
units — some DSSs of the BC carry units, others do not. Units, codelists, LOINC codes
and result values follow from the axes and are not counted.

## Inputs

- `cosmos-graph/interim/COSMoS_Graph.xlsx` (DSS, BC, Variables, DataElementConcepts)
- `consumer-bases/interim/DSS_View.xlsx` (`Measurement_Specs`)
- `sdtm-domain-reference/machine_actionable/SDTM_Domain_Metadata.xlsx`
  (`Domains`, `Instrument_Domain_Rules`, `Consumer_Exclusions`, `Variable_Meaning`)
- `cosmos-bc-dss/reports/COSMoS_Observable_Derivation.xlsx` (`DSS_Coordinates`)
- `sdtm-findings-graph/machine_actionable/Specimen_Findings.xlsx` (`Measurement_Specs`: the consumer's observable key, LB, MB, MI)
- `cosmos-bc-dss/reports/COSMoS_Observable_LOINC_Check.xlsx` (`Axis_Compare`; LOINC axes per pinned code)
- `sdtm-test-codes/downloads/SDTM_Terminology.txt` (codelist names and definitions)
- `sdtm-domain-reference/downloads/SDTM_v2.0.csv`, `SDTMIG_v3.4.csv` (CDISC variable tables: role, qualified variables, CDISC Notes; gitignored)
- `sdtm-domain-reference/downloads/Approved-Non-Standard-Variable-Registry_2026-04-03.xlsx` (CDISC NSV registry; gitignored)
- `sdtm-domain-reference/downloads/SDTMIG v3.4-FINAL_2022-07-21.pdf` (the SDTMIG document, for the domain Assumptions; gitignored; read with pypdf, needs `cryptography`)
- `sdtm-test-codes/machine_actionable/SDTM_Instrument_Identity.xlsx` (`Instruments`)
- `sdtm-test-codes/downloads/Thesaurus.txt` (NCIt parents and definitions; gitignored, filled by the CT release run)
- optional: a prior `SDTM_Terminology.txt` (`CT_PRIOR_FILE`) for the instrument class moves

Runs after `consumer-bases/` in a COSMoS refresh; see the release run order in
[`docs/Data_Flow.md`](../docs/Data_Flow.md).
