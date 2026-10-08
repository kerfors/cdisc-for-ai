# domain-behaviour — how does each domain behave?

`domain-behaviour/` re-derives, from the published COSMoS content, the behaviour that
the Findings consumers' scope decisions rest on, and reports where content and
decisions disagree. It is the March 2026 behavioural analysis
([`docs/archive/behavioural-analysis-2026-03/`](../docs/archive/behavioural-analysis-2026-03/))
made reproducible: run it on every COSMoS release and compare with the previous run.

It reports only. Scope and classification stay in
[`SDTM_Domain_Metadata.xlsx`](../sdtm-domain-reference/machine_actionable/SDTM_Domain_Metadata.xlsx):
the `Domains` flags and the `Consumer_Exclusions` sheet, whose claims this notebook tests.
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
| `Variable_Evidence` | variable × domain | What COSMoS and SDTM CT publish about each variable that differs between the DSSs of one BC |
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
  (`Domains`, `Instrument_Domain_Rules`, `Consumer_Exclusions`)
- `cosmos-bc-dss/reports/COSMoS_Observable_Derivation.xlsx` (`DSS_Coordinates`)
- `cosmos-bc-dss/reports/COSMoS_Observable_LOINC_Check.xlsx` (`Axis_Compare`; LOINC axes per pinned code)
- `sdtm-test-codes/downloads/SDTM_Terminology.txt` (codelist names and definitions)
- `sdtm-test-codes/machine_actionable/SDTM_Instrument_Identity.xlsx` (`Instruments`)
- `sdtm-test-codes/downloads/Thesaurus.txt` (NCIt parents and definitions; gitignored, filled by the CT release run)
- optional: a prior `SDTM_Terminology.txt` (`CT_PRIOR_FILE`) for the instrument class moves

Runs after `consumer-bases/` in a COSMoS refresh; see the release run order in
[`docs/Data_Flow.md`](../docs/Data_Flow.md).
