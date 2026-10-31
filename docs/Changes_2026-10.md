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

The conflict flags (NCIt_Code_Conflict, NCIt_Reference_Disagree) still came across on
the test code alone, so a test sharing a mnemonic with a COSMoS-pinned test carried that
test's flags. They now use the same key as the coverage. A blank flag means not
evaluated, and the ReadMe says so.

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

## Exclusion reasons are tested against each release

The reasons for leaving a domain out of a consumer were comments in the notebooks. They
now live in the domain reference, each stated as a claim the published content must
support, and a new analysis track evaluates the claims on every COSMoS release. Its
first run found that two of the March reasons no longer described the content.
Immunogenicity was excluded because, in the March analysis, the antigen target existed only
in the DS code; the target is now a variable of its own, the binding agent. Genomics was excluded as
decomposing by result scale; it decomposes by test detail. Neither decomposes by
specimen, so both exclusions stand, now with reasons that hold. The March wording is
kept in the reasons for reference.

## Each reference file stands on its own

A reader of a Findings file had to know the pipeline to use it: which codelist a
`*_codelist` column names, why a domain is missing, which versions the file was built
on. That knowledge is now in the files.

Each Findings file carries a Codelists sheet: every codelist its columns name, with all
terms, C-codes, definitions and synonyms as SDTM CT publishes them. The set follows the
file's own columns, not a list kept by hand.

A new file, Domain_Coverage, has one row per domain. It says which Findings file holds
the domain, how many of its Dataset Specializations are there, and if none, why: in
scope but without COSMoS content, excluded by a recorded decision, not a Findings
domain, or no consumer rule assigned. The last is stated as a fact, not a decision.
The consumer is computed with the consumers' own rules, then checked against what the
files contain; the run stops if they disagree.

Every ReadMe now starts the same way: purpose, scope, source versions, known gaps,
sheets. The versions come from one pin file. The Findings and coverage runs stop when
the COSMoS pin is older than the newest package in the data. The SDTM CT file carries
no version, so that pin is stated, not checked, and the ReadMe says this too.

A Provenance sheet now carries the source versions as fixed keys, and a content hash per
data sheet, so a program can tell whether the data changed without comparing every sheet:
the file itself changes on every save, the content hash only when the data do.

## Immunogenicity gets its own file

Immunogenicity was excluded from the specimen consumer because its Dataset Specializations
differ by the target an antibody binds, not by specimen. The exclusion was right, but it left
IS without a reference file: a reader looking for the binding agents — allergens,
microorganisms, autoantigens — had to open an interim file. IS now has a consumer of its own,
`Immunogenicity_Findings`. Its Codelists sheet carries in full both codelists SDTMIG binds to
the binding agent: Microorganism, and Binding Agent for Immunogenicity Tests.

The domain reference gains a flag for it. IS stays specimen-based, as the IG places it, so the
new flag is checked first wherever a consumer is assigned. The exclusion from the specimen
consumer stays and is still tested on every release.

Reading the IG for this sharpened three things. The binding agent is part of what is measured:
test and binding agent together should describe the analyte, without other variables. For
antidrug antibodies the binding agent is the study therapy, which CDISC does not control, so
these tests have no binding-agent term by design and no COSMoS specialization yet. And the
test's operational objective (screen, confirm, quantify) stays open: in COSMoS it goes together
with the result scale.

## NCIt synonyms: one separator, more names, shared strings shown

The Codelists sheets carried only the synonyms SDTM CT publishes, the CDISC synonyms. NCIt
often knows a term by more names, and a reader matching free text against the codelists missed
them. Each Codelists sheet now has a second synonym column with the NCIt synonyms that are not
already a CDISC field, kept apart because they carry different authority: CDISC synonyms are part
of the standard; NCIt synonyms are NCI's, and the file they come from does not say where each one
comes from.

More names also means more names that point to more than one term. A new sheet, Shared_Strings,
lists every string that names more than one term within a codelist, and says whether the sharing
is already in SDTM CT or comes with the NCIt synonyms. Some sharing was there all along: in the
unit codelist, one abbreviation can name several units. A string that names more than one term
identifies none of them.

NCIt synonyms are now separated by `|` in every file, the separator the NCIt file itself uses.
Before, the repo used three conventions, and a semicolon could not be told apart from the
semicolons some NCIt synonyms contain. The NCIt release the files are built on is now pinned
beside SDTM CT and COSMoS.

## A phrase index for looking up free text

Every consumer that matches free text against the codelists had to decide how to normalise,
and two consumers could get different hits from the same file. Codelist_Phrases states one rule
and lists every published name of every term in that form, with the facts that show why a hit
may be weak: where the name comes from, how many words it has, and how many terms or codelists
share it. It decides nothing. Building it found one name the rule could not handle, the unit %,
and the rule now says what happens to it.

## Codelists bound through value lists

DSS_View carried a variable's codelist only where COSMoS pins a term. Where COSMoS restricts
a variable to a value list, the bound codelist was used to resolve the list's NCIt codes but
not written out. So the Codelists sheets missed codelists that Dataset Specializations bind
only through value lists — in the immunogenicity file, the unit codelist and the codelist of
the test operational objective. DSS_View now writes the bound codelist for value lists too,
and the Findings files carry those codelists in full. A `_codelist` column that is empty on
every row of a file is left out, which removes some empty columns published earlier.

The test operational objective shows terminology moving after an IG is published: SDTMIG
v3.4 lists three values and calls the codelist nonextensible; SDTM CT now has four.

Two things surfaced on the way. Ethnic Group and Race, which COSMoS binds in Demographics,
are not in the pinned SDTM CT; the domain coverage file names them as such instead of
stopping. And the notebooks read the term NA (Not Applicable) in the No Yes Response
codelist, and None in three instrument codelists, as empty values; they are now read as
published. The graph validation report had listed that NA as an unresolvable value-list
member; it no longer does. The ReadMe of each file with such a term now says how to read it,
since any reader using pandas defaults would lose it the same way.

## The IG in its own words on test facets and routing

Matching an activity label against CDISC terminology needs two things the terminology does
not carry by itself: which aspects of a test sit beside the test name rather than in it, and
which domain a kind of test belongs to. SDTMIG v3.4 states both, in prose: the natural-key
section prefers a generic test code with qualifier variables, the LB assumptions list the
aspects of a lab test associated with a LOINC code, and the IS, GF, MB and PC sections say
where binding agents, gene symbols and test details go, and which tests belong to another
domain. SDTMIG_Statements quotes these statements as published, with section, item and page,
and adds the variable-table rows of the variables they name. The selection is ours; the text
is the IG's; nothing is interpreted.

Building it found that the LB assumption on LOINC names position and location among the
aspects of a lab test, while the IG's own LB variable table has neither; they come from the
SDTM model. The file shows these apart from the variables in the table.

## What this says about the method

Every one of these was a place where code stood in for information the standards already
carry, or kept a decision past the point where the evidence for it held. The
standards publish more structure than a pipeline tends to use. Reading it, and checking
the decisions against each release, is the same discipline this repository asks of the
standards themselves.

## Authoritative current state

File-level current state lives in the ReadMe sheet of each machine-actionable xlsx,
regenerated on every run. Counts, column inventories, and coverage percentages are
point-in-time and belong there rather than in this note.

## References

- Domain reference: [`sdtm-domain-reference/`](../sdtm-domain-reference/)
- IG statements: [`sdtm-domain-reference/notebooks/SDTMIG_Statements.ipynb`](../sdtm-domain-reference/notebooks/SDTMIG_Statements.ipynb)
- Release check: [`sdtm-findings-graph/notebooks/Scope_Check.ipynb`](../sdtm-findings-graph/notebooks/Scope_Check.ipynb)
- Previous release: [`Changes_2026-09.md`](Changes_2026-09.md)
