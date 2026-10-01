# Changes — October 2026: corrections at SDTM CT 2026-09-25

**Reference versions:** unchanged — SDTM CT 2026-09-25 (NCI EVS), COSMoS BC/DSS
2026-07-14, SDTMIG v3.4 / SDTM v2.0. No upstream data moved. This release corrects the
pipeline.

Reviewing the September refresh, we found the pipeline making the mistakes this repository
describes in the standards. In a few places it guessed a classification that SDTM CT
already publishes. In one join it used a test code as if it were an identifier. Each
correction below replaces a guess with something CDISC publishes, or a mnemonic with an
identifier.

## Instrument class is read from the terminology

Instrument codelists were routed to QS, FT or RS by looking for a word in the codelist
name: Questionnaire, Functional Test, Clinical Classification. A new instrument in this
CT release is called a "Check-list" and matched no word, so it was published without a
domain. Two older instruments were routed to the wrong domain: their names contain
"Questionnaire" as part of the instrument's own name, while they are clinical
classifications.

The class is already in CT. Every instrument codelist's NCI Preferred Term begins with it
("CDISC Questionnaire …", "CDISC Clinical Classification …"), and the instruments are
listed in the category codelists for questionnaires, functional tests and clinical
classifications. Routing now reads the Preferred Term first, uses the name only where the
Preferred Term carries no class, and stops the run when neither works.

## Domain codes are read from the terminology

Where a domain-level test code codelist did not match a domain name in the repo's
domain reference, the domain code was cut out of the codelist's submission value. That
produced codes that are not SDTM domains — "GASTRO" and "INTEGU". CT publishes the
domain codes and their names in the SDTM Domain Abbreviation codelist: GI for
Gastrointestinal System Findings, IG for Integumentary System Findings. A derived code is
now accepted only if it is in that codelist; otherwise the codelist name is matched to a
published domain name; otherwise the run stops.

That rule surfaced one codelist with no domain at all: Physical Properties, a set of test
codes (color, diameter, ulceration and others) that several domains reuse. It is now
recorded in the domain reference as cross-domain rather than given an invented domain
code.

## Codes are mnemonics — here too

The Findings consumers joined COSMoS coverage on the test code alone. So Mycobacterium
chelonae (MCH in MB) carried the Dataset Specialization of Mean Corpuscular Hemoglobin
(MCH in LB). Bringing RE into scope would have done the same to Muscle Volume (MV in MK)
with Minute Volume (MV in RE) — the collision the September note itself pointed out.
Coverage is now joined on the test code together with its NCIt code.

## Scope comes from the domain reference, checked every release

Each consumer carried its own list of domains. The lists were written once and never
revisited, so the Respiratory domain — classified as a measurement domain in the March
behavioural analysis, with COSMoS content since the March package — was never in the
measurement consumer. Scope is now derived from the domain reference minus exclusions
that each notebook names with a reason. A new release check stops a refresh when a domain
that has test codes or Dataset Specializations is missing from the domain reference or is
not a published domain code.

Running that check brought ten more findings domains into the domain reference, all
published in the Domain Abbreviation codelist: body-system findings such as nervous,
endocrine and gastrointestinal, ophthalmic examinations, and the device and tobacco
product testing domains. They get their observation class now. A consumer class waits
until published COSMoS content shows how they behave — the same evidence that justified
RE.

## ECG returns to the measurement consumer

ECG was kept out of the measurement consumer because all its concepts were marked
Qualitative while many carried units. Since the COSMoS 2026-05-26 package that is no
longer the case: ECG concepts are Nominal without units or Quantitative with units. The
term "Qualitative" has gone from COSMoS altogether, in line with CDISC's own curation
principles. The exclusion reason no longer holds, so ECG is in.

## What this says about the method

Every one of these was a place where code stood in for information the standards already
carry, or kept a decision past the point where the evidence for it held. The
standards publish more structure than a pipeline tends to use. Reading it, and checking
the decisions against each release, is the same discipline this repository asks of the
standards themselves.

## Authoritative current state

File-level current state lives in the README sheet of each machine-actionable xlsx,
regenerated on every run. Counts, column inventories, and coverage percentages are
point-in-time and belong there rather than in this note.

## References

- Domain reference: [`sdtm-domain-reference/`](../sdtm-domain-reference/)
- Release check: [`sdtm-findings-graph/notebooks/Scope_Check.ipynb`](../sdtm-findings-graph/notebooks/Scope_Check.ipynb)
- Previous release: [`Changes_2026-09.md`](Changes_2026-09.md)
