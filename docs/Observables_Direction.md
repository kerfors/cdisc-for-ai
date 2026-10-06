# Direction: observables, more expressive reference files, RDF/OWL

*Written 2026-10-01. Updated as the steps are done; last update 2026-10-06.*

Three steps, in order: find out what identifies an observable in the CDISC standards and whether a conclusion can be drawn; then make the Excel reference files express it; later, move towards RDF/OWL.

## Where we stand (COSMoS 2026-07-14, SDTM CT 2026-09-25)

[`domain-behaviour/Domain_Behaviour.ipynb`](../domain-behaviour/notebooks/Domain_Behaviour.ipynb) re-derives, per domain, which variables distinguish the Dataset Specializations (DSSs) of one Biomedical Concept (BC). An axis is counted when the assigned value of the variable differs between the DSSs. Where only the value list differs, it is counted separately. Of 83 BCs that fan out into more than one DSS:

| Axis | Assigned value differs (BCs) | Domains | Only the value list differs (BCs) | Domains |
|---|---|---|---|---|
| specimen | 29 | LB, GF, IS | 0 | |
| scale (some DSSs with units, some without) | 20 | LB, MB, GF, IS | n/a | |
| test detail (TSTDTL) | 18 | GF, MI, MB, IS | n/a | |
| category (CAT/SCAT) | 15 | LB, RS, CM, MH, PR | 3 | SU |
| method | 9 | LB, GF, IS | 0 | |
| binding agent (BDAGNT) | 6 | IS | n/a | |
| location (LOC/LAT/POS) | 4 | PR | 7 | VS, EC, MK, PR |
| evaluator | 0 | | 10 | RS, TR, TU |
| none (no assigned value differs) | 20 | AE, EC, MK, SU, TR, TS, TU, VS | | |

Until 2026-10-06 the two columns were counted together. That made evaluator look like an axis in RS, TR and TU, and location look like one in VS.

Other findings from the same run:
- Only LB fans out primarily by specimen. MB fans out by scale and test detail, MI by test detail, GF by test detail, IS by binding agent.
- Every DSS in LB, MB, MI, IS and GF carries a specimen; in UR only 10% do.
- The March 2026 exclusion reasons for IS ("target only in the DS code") and GF ("scale-driven") no longer described the content; both are restated in the `Consumer_Exclusions` sheet of [`SDTM_Domain_Metadata.xlsx`](../sdtm-domain-reference/machine_actionable/SDTM_Domain_Metadata.xlsx) and hold now.

## Reading (not yet tested; revised 2026-10-06)

The axes do not fall into two clean groups. The test is the line between Biomedical Concept and Dataset Specialization: does the attribute change the observation itself, or only where and how an unchanged observation is filed?

- **Observation-changing:** specimen, binding agent, test detail, method, scale — glucose in serum vs urine, IgE against cockroach vs peanut are different observables. Mostly the specimen-based domains.
- **Category carries more than one thing.** In RS the assigned category is the response criteria (RECIST 1.1, Lugano classification, RANO), and that changes the observation. In LB it is the laboratory grouping (chemistry or hematology versus urinalysis) and follows the specimen. In CM and MH it is what a form pre-specifies, which is collection context. The variable does not tell which of these it carries.
- **Evaluator is not an axis.** In RS, TR and TU no evaluator value is assigned on any DSS; only the value lists differ. In RS the DSSs of one BC are separated by the response criteria in the category. In TR and TU no assigned value separates them, only the DS code.
- **Location:** an assigned location differs only in PR (imaging procedures by body location). In VS only the value list for position differs, and position is a state of the subject (see below).
- **Not a variable at all:** who rates. The same kind of assessment can be patient-reported, parent- or observer-reported, or clinician-rated, and that changes the observation. SDTM CT encodes it in the instrument's class — questionnaire or clinical classification — rather than in a variable. The instrument reclassifications in SDTM CT 2026-09-25 follow the rater wherever NCIt states it.
- **Recorded with the result, not part of the observable:** the subject's state at the time of observation — fasting, time after a challenge, body position. It changes how a result is interpreted, not what is measured. COSMoS records fasting status as an allowed value list on most laboratory specializations, never as a value that tells one specialization from another. A name search in LOINC shows separate codes for fasting glucose (for example 1556-0), so LOINC and COSMoS seem to differ here. Step 1 reads this properly and states the difference.

Working formulation: an observable = a BC plus its observation-changing axes. A COSMoS DSS bundles those with collection choices, and domains differ in which kind dominates. This supports specifying observables on the BC rather than the DSS, as explored for glucose in [`Glucose_Siblings_BC_DSS_Proposal.html`](../cosmos-bc-dss/docs/Glucose_Siblings_BC_DSS_Proposal.html), but it is a reading of the data, not something the data states. The axes above are named after SDTM variables, and a variable does not say what the distinction means. The meaning has to be named separately from the variable that carries it.

## Step 1 — test the observable reading

Read and record what the standards publish. No classification by our own judgement.

- For each variable and domain, record what the assigned values carry (for example: `RSCAT` carries the response criteria), with the source. Include who rates, which CT carries in the instrument class. Record this as data, not in code.
- Where the published sources do not settle whether a distinction changes the observation, record it as undecided, with both readings. It is not decided here.
- Bring the fan-out axes together with the observable key in the observables notebooks in [`cosmos-bc-dss/`](../cosmos-bc-dss/) (`COSMoS_Observable_Derivation`). The two should agree, or the difference should be stated.
- Compare with LOINC's axes (component, property, system, scale, method) using `COSMoS_Observable_LOINC_Check` and its LOINC cache. State where LOINC and COSMoS differ; do not resolve it.
- One pass over the BCs that fan out. Then say what the standards publish about what identifies an observable, and where they are silent or inconsistent.
- Related open question: what the specimen-based Findings consumer is for — "specimen is the decomposition axis" (fits LB only) or "observation made on a specimen" (fits LB, MB, MI, IS, GF). MB and MI stay in it for now.

## Step 2 — make the Excel reference files more expressive

Once observables have a working definition, state it in the files instead of leaving it implicit:
- an observable key per DSS;
- the identifying axes as named columns, not only inside the variable pivots;
- continue the pattern of the October 2026 corrections: identity keyed on NCIt codes rather than mnemonics (the TESTCD + NCIt join fix), reasons stated as data (`Consumer_Exclusions`), classifications read from what CT publishes (instrument class, C66734 domain codes).

## Step 3 — towards RDF/OWL

The long-run aim: publish the reference files as RDF/OWL that expresses the behaviour of the standards, related to established ontologies. By then the files would carry the distinctions that need predicates: link kinds from [`link-semantics/`](../link-semantics/), the observable structure from step 1, and identity on NCIt codes.

## See also

- [Who rates?](https://kerfors.github.io/cdisc-for-ai/examples/who-rates.html) — worked example (early, exploratory): the instrument reclassifications in SDTM CT 2026-09-25, today's representation against an explicit graph
- [Domain behaviour](https://kerfors.github.io/cdisc-for-ai/analyses/domain-behaviour.html) — the analysis page behind the table above, regenerated on each COSMoS release
- [`Changes_2026-10.md`](Changes_2026-10.md) — the corrections that led here
