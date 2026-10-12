# Interpretation context: what the record carries so a value can be read

*Written 2026-10-12. COSMoS 2026-07-14, SDTM v2.0, SDTMIG v3.4.*

A recorded value often needs context before it can be read: whether the subject was fasting, the body position, the time since a reference point, the period an instrument asks about. This page records what the data standards carry for that, and how COSMoS uses it. It reads the record side only. How a procedure is carried out, and the operational side of a study (who performs it, where, with what, at what burden and cost), are outside the data standards and outside this repository.

Every number on this page comes from the `Interpretation_Context` sheet and the `Key_Measures` sheet of [`Domain_Behaviour.xlsx`](../domain-behaviour/interim/Domain_Behaviour.xlsx), section 4i of [`Domain_Behaviour.ipynb`](../domain-behaviour/notebooks/Domain_Behaviour.ipynb).

## What is read

All generic variables that the SDTM v2.0 Model gives the role Record Qualifier, Variable Qualifier or Timing: 159. For each, the domains where SDTMIG v3.4 has it (with its Core and codelist), and how COSMoS uses it there. 964 variable × domain pairs; 91 of the generic variables have COSMoS content.

| Model role | Absent from COSMoS | Never assigned | Always assigned | Mixed |
|---|---|---|---|---|
| Record Qualifier | 282 | 77 | 11 | 20 |
| Timing | 282 | 56 | 3 | 2 |
| Variable Qualifier | 134 | 64 | 13 | 20 |

*Never assigned*: COSMoS gives a value list or no value. *Always assigned*: every DSS that carries the variable fixes one value.

The roles do not separate context from identity. Specimen, method, test detail and binding agent are qualifiers too, so *always assigned* includes `LBSPEC`, `ISBDAGNT` and `MITSTDTL`, which identify the observable ([Observables, Phase 1](Observables_Phase1.md)). The sheet also lists record flags such as `--BLFL`, which concern the analysis, not the measurement. The separation shows only in how COSMoS uses each variable.

## What COSMoS does with the context

1. **State of the subject: recorded, never fixed.** `LBFAST` is on 128 of 147 LB DSSs, always as a value list; `--FAST` also in EC and EX. `VSPOS` has a value list on 9 of 78 VS DSSs; `EGPOS` is on 31 of 33 EG DSSs without a value. Never assigned anywhere.
2. **Planned time: absent.** `--TPT`, `--TPTNUM` and `--ELTM` are permissible in 25 SDTMIG v3.4 domains, `--TPTREF` and `--RFTDTC` in 26. None is in any COSMoS DSS. The Timing variables COSMoS does carry are dates, durations and time relative to a reference period.
3. **Time relative to a reference period: recorded as choices.** `--STRF`, `--ENRF`, `--STRTPT` and `--ENRTPT` in AE, CM, MH and SU: value lists. `CMENRF` and `CMENRTPT` are assigned on one CM DSS each; nowhere else.
4. **Evaluation interval: always fixed.** `QSEVINTX` on 6 of 17 QS DSSs, `RSEVINTX` on 7 and `RSEVLINT` on 12 of 157 RS DSSs, each time assigned. Here the interval is part of what the result means.
5. **Location, laterality, method: mixed.** `MILOC` is assigned on all 8 MI DSSs, `PRLOC` on 6 of 16 PR DSSs; elsewhere `--LOC` is a value list or has no value. `--LAT` is never assigned. `MIMETHOD` is assigned on the 7 MI DSSs that carry it; `--METHOD` is mixed in GF, IS, LB and MB, and a value list in TR and TU. The same variable identifies the observable in one domain and is context for reading it in another.

## Reading

Context that only helps to read the value is recorded but not fixed. That is consistent with the standards keeping it beside the value rather than in the concept: fasting, position and time relative to a reference period are what happened, not what was determined. Planned time is not in COSMoS at all; it belongs to a study's schedule, not to a concept.

The evaluation interval is the exception: COSMoS fixes it wherever it occurs. `QSEVINTX`, `RSEVINTX` and `RSEVLINT` are therefore in `Variable_Meaning` as *proposed*, position *open*: no source states whether the interval is part of what is observed. They show in `Axis_Meaning` of [`Instrument_Findings`](../sdtm-findings-graph/machine_actionable/Instrument_Findings.xlsx).

LOINC reads the same context differently: it has separate codes for fasting glucose, for example, where SDTM records fasting beside the value. This is a difference in where the context is put, not a disagreement about what is measured.

## Not read here

The operational side of a study, and the SDTM Trial Design datasets (TA, TE, TV, TD, TM, TI, TS), which describe the planned study rather than the context of a recorded value.

## See also

- [Direction: observables, more expressive reference files, RDF/OWL](Observables_Direction.md)
- [Observables, Phase 2](Observables_Phase2.md)
- [Domain behaviour](https://kerfors.github.io/cdisc-for-ai/analyses/domain-behaviour.html) — the analysis page, regenerated on each COSMoS release
