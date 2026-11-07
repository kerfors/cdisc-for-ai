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

## What this says about the method

Each change replaces a list we kept with a rule the standards support, or puts a
published fact beside a test where a consumer had to guess. The IG, SDTM CT and NCIt carry
more than the files used; the work is to read it, say whose it is, and check it on each run.

## Authoritative current state

File-level current state lives in the ReadMe sheet of each machine-actionable xlsx,
regenerated on every run. Counts and column inventories belong there, not in this note.

## References

- IG statements: [`sdtm-domain-reference/notebooks/SDTMIG_Statements.ipynb`](../sdtm-domain-reference/notebooks/SDTMIG_Statements.ipynb)
- NCIt synonyms and parents: [`sdtm-test-codes/notebooks/SDTM_CT_Term_NCIt_Synonyms.ipynb`](../sdtm-test-codes/notebooks/SDTM_CT_Term_NCIt_Synonyms.ipynb)
- Findings consumers: [`sdtm-findings-graph/`](../sdtm-findings-graph/)
- Previous release: [`Changes_2026-10.md`](Changes_2026-10.md)
