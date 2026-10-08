# Observables, Phase 2: the reference files say what identifies an observable

*Written 2026-10-08. COSMoS 2026-07-14, SDTM CT 2026-09-25. Findings consumers only.*

Phase 2 of the [observables direction](Observables_Direction.md) (Step 2): state in the Excel reference files what [Phase 1](Observables_Phase1.md) settled, instead of leaving it implicit. Phase 1 settled the core axes at the level of the variable, not a key for every DSS, so Phase 2 was kept narrow: the variable level in all three Findings consumers, and a key per DSS for LB, MB and MI only.

Every number on this page comes from a cell: the `axis-meaning-code`, `observable-key-code` and summary cells in the three notebooks of [`sdtm-findings-graph/`](../sdtm-findings-graph/), and section 4h of [`Domain_Behaviour.ipynb`](../domain-behaviour/notebooks/Domain_Behaviour.ipynb) with its `Key_Measures` sheet.

## What the files now say

**`Axis_Meaning`, in all three Findings consumers.** The rows of `Variable_Meaning` in [`SDTM_Domain_Metadata.xlsx`](../sdtm-domain-reference/machine_actionable/SDTM_Domain_Metadata.xlsx) that apply to the file, with Position, Basis and Status, and the `Measurement_Specs` columns each row refers to. It says which columns identify the observable, which are open, and on what basis. It is our position, not a published fact; the basis notes stay in `Variable_Meaning`.

| File | Rows | Of which open |
|---|---|---|
| `Specimen_Findings` | 8 | `LBCAT`, `LBFAST` |
| `Measurement_Findings` | 2 | `VSPOS` |
| `Instrument_Findings` | 4 | `RSCAT`, `QSEVAL`, `RSEVAL` |

**A key per DSS for LB, MB and MI, in `Specimen_Findings`.** Four columns in `Measurement_Specs`:

- `Observable_Key`: `bc_id | component | system | scale | method`, as NCIt codes except scale, built from the `Axis_Meaning` rows. The test code (`--TESTCD`, the Topic variable) is the base of the component.
- `Observable_Key_Label`: the same key in submission values.
- `Key_Shared_With`: the other DSSs with the same key.
- `Key_Positions`: which `Axis_Meaning` rows the key was built from, and their status.

| Domain | DSSs | Keys |
|---|---|---|
| LB | 147 | 145 |
| MB | 14 | 14 |
| MI | 8 | 8 |
| Total | 169 | 167 |

2 keys are shared, by two DSSs each; they are listed in `Key_Shared_With`, as COSMoS publishes them.

**A check of the key against the derivation.** `COSMoS_Observable_Derivation` builds its own key per DSS, with its own rules. Section 4h of `Domain_Behaviour` compares the two for the 169 DSSs: 167 consumer keys, 167 derivation keys, 0 groups that differ (`Consumer_Key_Compare`, empty). The two keys read scale differently but group the DSSs the same way.

## What the key does not say

**Scale is read as units present or absent.** The rule that scale separates observables is accepted; how to read it per DSS is not. Phase 1 found two proxies, units present and the `--ORRES` data type, and neither is right throughout. The key uses the one the consumer file supports and writes it as a token, `UNITS` or `NO_UNITS`, which names the reading, not a scale. An example: the Allred total score for estrogen receptor (`ESTRCPTATOTSCORE`, MI) is `NO_UNITS`, while the derivation's data type reading says Quantitative. `Key_Positions` marks the reading as open. Without scale, concentration and presence in urine (glucose, protein and others) would share a key.

**MB and MI: test code and test detail only.** `Variable_Meaning` has no rows for `MBSPEC`, `MISPEC`, `MBMETHOD` and `MIMETHOD`: they never separate sibling DSSs, so Phase 1 did not read them. The key shows `-` for system and method there, even where COSMoS assigns a value. This does not change the grouping, since every key starts with the BC. It matters when keys are compared across BCs.

**COSMoS assignments as published.** The key carries what COSMoS assigns, including any assignment errors; it does not correct them.

## Considered and not done

**A key for the measurement domains (VS, EG, RE, MK).** Few BCs there have more than one DSS (`bcs_fanning_out` in `Key_Measures`: VS 4, MK 1, EG 0, RE 0), and those are separated only by location value lists. A key would mostly repeat the BC. What it could add is identity across domains, where a BC is published in more than one; but the system part would need a position on `--LOC`, which has no row with a basis.

**An instrument anchor in `Instrument_Findings`.** The anchor is already there: `Instrument_NCIt_Code`, the class category term in the NCIt instrument branch, on 171 of 197 DSSs (`Instrument_Match_Method` = `class-category-term`; 26 `not_applicable`). The test code of an instrument comes from a codelist of that instrument, so it already ties a question to its instrument. An anchor adds grouping, not identity.

**A concept for the open rows.** Category, rater, the analysis method `GFANMETH`, `GFSYMTYP` and subject state stay columns only, marked open in `Axis_Meaning`. The standards are silent on them (Phase 1), so there is no basis yet to give them a position.

## What comes next

Not decided. Extending the key beyond LB, MB and MI needs first a reading of what is published for the identifying variables that never separate sibling DSSs (`MBSPEC`, `MISPEC`, `--LOC` and others), so they can get rows with a basis. That is evidence work of the Phase 1 kind. The per-DSS reading of scale is open and waits for the next COSMoS release. Events and Interventions get the Phase 1 pass after that release.
