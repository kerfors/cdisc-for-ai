# Changes — November 2026: the IG and NCIt, read further

**Reference versions:** unchanged — SDTM CT 2026-09-25 (NCI EVS), COSMoS BC/DSS
2026-07-14, SDTMIG v3.4 / SDTM v2.0, NCIt FLAT 2026-09-29. No upstream data moved.

Using the files to match study activity labels to CDISC terms showed where they stopped
short. Some of it the standards already publish and the files did not carry: an IG
description of a variable, a codelist the IG binds to it, NCI's own grouping of tests.
This release reads those.

## The IG's notes on every test facet

SDTMIG_Statements quoted the IG's notes for a hand-picked set of variables. The test
condition variables were not in the set, although the IG describes them — for the
immunogenicity domain it names stimulating agents as the example. The selection is now a
rule: the CDISC Notes of every Findings variable that describes a test beside its name
(test condition and its agent, test detail, binding agent, operational objective, and the
IS measurement basis) are quoted, and the run fails if one is missing. A quoted Notes
statement now always brings its own variable into the Variables sheet, also when its text
does not name it.

## Positions cite the statements

Where a position in Variable_Meaning rests on a variable's IG notes, it now cites the
statement by its ID, as it already did for the assumptions. For the IS test detail and
operational objective the citation was there in words but had no ID to resolve.

## Codelists the IG names

The Codelists sheet of a Findings file carried the codelists COSMoS names. The IG names
some that COSMoS does not — the test condition codelist is one. The specimen and
immunogenicity files now carry, for their domains, every codelist the IG variable table
gives for a test facet variable. Terms come from the same SDTM CT file the graph is built
from; a codelist found in both must have the same terms, or the run stops.
referenced_by says which: the COSMoS column, the IG variable, or both.

Since the kind of facet was added, the rule also follows our own positions: every Findings
file carries the codelist the IG gives for each variable that has a Kind other than record,
the test code excepted, since the tests have their own sheet. For ECG this brings the method
and lead codelists, which COSMoS does not name: it has the method variable without a value and
no lead variable. A variable that gets a position brings its codelist with it.

## NCI's hierarchy beside the test

The immunogenicity file now carries the NCIt parents of each test. NCI groups these tests
by antibody class — autoantibody, alloantibody, antidrug, and others — and that grouping is
a published fact, not ours. It is NCI's classification, not CDISC's. Its fit differs by
domain; for lab tests it has not been reliable. So it is added for IS only, and the file
checks it against the test's own wording: no test where the two disagree, a few where the
wording says more than the hierarchy. The ReadMe states both, and the run fails if they
ever contradict.

## What the repository does not read

The README now describes the codetables in the words of the CT page: relationships
between terms in different codelists — the responses or units that go with a test — that
the CT publication files do not show. Relationships of this kind are in the Findings files,
from COSMoS, in the value-list and unit columns. They are COSMoS's specifications, not the
codetables, which are still not read here.

## Where NCI places the organisms

A consumer matching activity labels cannot carry the whole microorganism codelist. NCI's
hierarchy could let it carry a group instead. A new report in domain-behaviour reads
that hierarchy above every MICROORG term. Bacteria and most RNA viruses reach a family.
DNA viruses, fungi, protozoa and helminths do not: there NCI groups by genome type or by
higher taxa, and some groupings are not taxonomy at all. NCIt publishes no rank, so
"family" is read from the name; the report marks that reading as ours.

## What the lab, cell phenotype and PK domains hold

SDTMIG_Statements quoted where the IG sends a kind of test for the immunogenicity, genomics,
microbiology and response domains, but nothing on what LB, CP, PC and PP hold, apart from the
IS assumption that sends flow cytometry to CP. It now quotes the description of each of these
domains, and their first assumptions where they state scope. The PP description says its
parameters are derived from the PC concentrations, and its first assumption calls it a derived
dataset. That is the IG on one domain, not a classification: elsewhere the IG decides derived or
collected per value. The Variables sheet now also says why its codelist submission values are
empty: they are empty in the published variable table.

The IS description and its first and third assumptions are now quoted too. Until now only
assumption 2 said which antibodies go to IS: those raised against an allergen, a microorganism
or a self-antigen. Assumption 1 covers immune responses a therapy provoked, and assumption 3
covers all other induced humoral responses, with antibodies against HLA proteins as its example.

The VS and CV descriptions are now quoted too, with the first CV assumption. VS holds
measurements such as blood pressure, temperature, respiration, height and weight; CV holds
findings of cardiovascular diagnostic procedures, and the conduct of the procedure goes to PR.
The EG description is quoted too: ECG data, including the position of the subject, the method
of evaluation, all cycle measurements and all findings, with an overall interpretation if
collected or derived.

## How the IG describes ECG, vital signs and cardiovascular tests

SDTMIG_Statements quoted what EG, VS and CV hold, but not what the IG says about their tests.
It now quotes the EG assumptions on test codes: the method of QT correction is part of the
test name in controlled terminology, and the sponsor names the tests of its own QT correction
models. Also quoted: the separate test codelists for 10-second and Holter ECGs, and the EG, VS
and CV assumptions on the qualifiers that would not generally be used, and the VS codetable
that links some vital sign tests to qualifier codelists. EG recommends that --LOINC not be
used; CV lists it among the qualifiers that would generally not be used. The EG notes on
position, method and lead are quoted as published; their examples are not always CT terms
("12-LEAD STANDARD" against the term 12 LEAD STANDARD, "LEAD 1" against LEAD I). The EG
assumptions on beat-level, aggregate and repeated records are quoted as record statements:
they say what identifies the record.

The EG examples heading is printed with a hyphen, not a dash, so the last EG assumption ran
on into the examples; an Assumptions block now ends there too. The first VS assumption
(VSLOINC) is not quoted: in the text read from the PDF, the markers of items 1 and 2 come
before both texts.

## The variable tables, as published

The CDISC variable tables were read in several places, each for what it needed. A new file in
sdtm-domain-reference, SDTM_Variables, now carries them for the general observation classes:
the SDTM v2.0 Model variables, and every SDTMIG v3.4 domain variable with what the Model says
about its generic variable. The Model says what a Variable Qualifier qualifies: the test code
(--TSTDTL, --BDAGNT, --TSTCND), the specimen or location (--LAT, --DIR), the result (units,
reference ranges) or another qualifier (--EVALID qualifies --EVAL). A Record Qualifier qualifies
the record and names no variable: --SPEC, --METHOD, --POS, --LEAD and --FAST are all Record
Qualifiers. Where a domain says more, as LB Assumption 8 does, the IG statements say so.

The Model gives some variables an NCIt concept: --POS is Body Position During Assessment, --SPEC
Biospecimen Type, --LEAD Electrical Lead Recording. The file carries the concept and its NCIt
parents; --METHOD, --LOC and --TSTDTL have none.

Read across all domains, the IG sometimes gives a variable a role other than the Model's: among
them the route of administration, the LOINC code, the MI test detail and the VS laterality.

SDTMIG_Statements now also lists the generic forms a statement names, such as --SPEC, --FAST and
--LOINC in the EG assumption on qualifiers that would not generally be used.

Domain_Behaviour now reads the variable tables from this file. Its interpretation-context sheet
matched variables by name and so also listed Special-Purpose and Trial Design variables that
share a suffix with a generic variable, such as the demographics collection date. These datasets
are not of the general observation classes, and the Model describes them with their own
variables; they are no longer listed. The interpretation-context page says what changed.

Each Findings file now carries the variables of its own domains from this file in a
Domain_Variables sheet: the candidates for facets. A facet is a value, beyond the test code, that
describes the planned observation. Result Qualifiers and Identifiers are left out, by the Model's
role: no published source ties them to describing a test. A consumer sees there what the Model says
each qualifier qualifies — the test code, the specimen or location, a result, another qualifier,
or only the record — without opening another file. For ECG, for example: position, method and lead
are Record Qualifiers; only the test name qualifies the test code. That position, method and lead
describe the test is our position, not the IG's.

## The kind of facet

Variable_Meaning gains a Kind column: the kind of facet each variable carries — observable,
practice, record, or open — beside the Position that says whether it makes a different
observable. A facet is a value, beyond the test code, that describes the planned observation;
the definition and the two rules that follow from it are on the observables direction page.
Kind is our position, as Position is, and each row states its reason. The domain-behaviour
checks hold the two together: a position in the key goes with observable, a position outside
the observable with practice or record.

The ECG variables now have rows: the position of the subject, the planned time and its
reference, who reads and repetitions as practice; the method as observable; the lead open. All
are proposed, with the position open, since the IG names no facets for ECG beyond the test name
and units. COSMoS does not use several of these variables. A row can now rest on the IG variable
table alone, and the Findings file shows it as not in COSMoS.

The analysis method of the lab domain now has a row too. SDTM CT puts the formulas for the
estimated glomerular filtration rate there, not in the test code, and LB Assumption 8 names the
variable among the aspects of a lab test. Its kind is observable, since a calculation method is a
facet; whether it changes the observable stays open. With the row, its codelist enters the specimen
file and the phrase index, so a formula named in a label can be found.

The domain metadata file is kept by hand. It now has a Provenance sheet like the generated files,
with a content hash per sheet, written by a small notebook after each edit; the domain-behaviour run
stops when a hash no longer matches its sheet.

## Facets folded into the test code

SDTM CT sometimes puts a facet into the test code itself. The IG says so once: the QT
correction method is in the ECG test name. The phrase index (Codelist_Phrases) now lists the test
terms where the published content points to this, each with its evidence: an IG statement
that quotes the test code; a test name of the form "head, tail" with other terms of the same
head; a tail that is a term of a facet codelist; a tail found in an analysis method codelist.
It gives candidates, not verdicts.

Most tails name something no SDTM variable holds: aggregate or single beat in ECG, free or
intact forms in the lab, end diastole or systole in cardiovascular imaging. Only one tail is a
term of a facet codelist (fibronectin in plasma). For ECG, CT now has the beat in two places:
in the test name and in the ECG analysis method codelist, which SDTMIG v3.4 does not name. The
estimated glomerular filtration rate goes the other way: the formula is not in the test code but
in the analysis method variable of the lab domain.

## Strings that name more than one test

The phrase index covered the codelists the Findings files carry, not the test codelists. A label
looked up against the tests meets the same problem: a string that names more than one test
identifies none of them. The phrase index now has a second sheet with every such string in the test
codelists of the Findings domains. They all cross codelists: TAT is one lab test code and a synonym of
another; EGFR is a receptor test code and, written eGFR, a synonym of the estimated glomerular
filtration rate; MCH is a haematology and a microbiology test code; CMV a microbiology and a muscle
test code. More come with the NCIt synonyms. Strings outside SDTM CT, such as visit labels, are not
covered.

## What this says about the method

Each change replaces a list we kept with a rule the standards support, or puts a
published fact beside a test where a consumer had to guess. The IG, SDTM CT and NCIt carry
more than the files used; the work is to read it, say whose it is, and check it on each run.

## Authoritative current state

File-level current state lives in the ReadMe sheet of each machine-actionable xlsx,
regenerated on every run. Counts and column inventories belong there, not in this note.

## References

- IG statements: [`sdtm-domain-reference/notebooks/SDTMIG_Statements.ipynb`](../sdtm-domain-reference/notebooks/SDTMIG_Statements.ipynb)
- Variable tables: [`sdtm-domain-reference/notebooks/SDTM_Variables.ipynb`](../sdtm-domain-reference/notebooks/SDTM_Variables.ipynb)
- NCIt synonyms and parents: [`sdtm-test-codes/notebooks/SDTM_CT_Term_NCIt_Synonyms.ipynb`](../sdtm-test-codes/notebooks/SDTM_CT_Term_NCIt_Synonyms.ipynb)
- Findings consumers: [`sdtm-findings-graph/`](../sdtm-findings-graph/)
- Previous release: [`Changes_2026-10.md`](Changes_2026-10.md)
