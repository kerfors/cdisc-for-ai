# Changes — September 2026: SDTM CT 2026-09-25 refresh

**Reference versions:** SDTM CT bumped from the 2026-03-27 package to **2026-09-25** (NCI
EVS). The NCIt Thesaurus files used for enrichment were refreshed alongside, because most
concept codes new to this CT release were absent from the earlier copy. COSMoS BC/DSS
2026-07-14 and SDTMIG v3.4 / SDTM v2.0 are unchanged — no newer COSMoS package is on the
public export. This is an upstream data refresh: the pipeline is unchanged, only its
inputs moved. CT was refreshed on its own, so every downstream movement in this release is
attributable to the terminology.

## What moved in the terminology

**Instrument reclassification.** Several global-impression instruments are reclassified
from questionnaire to clinical classification, and one moves the other way; their test
code and test name codelists are renamed to match. Under the SDTMIG v3.4 pin the instrument
identity files follow the rename, routing them to RS or QS. The release also adds a
Clinical Classification (CC) domain abbreviation for the SDTMIG v4.0 model; the repo stays
on v3.4 routing until the IG pin moves.

**Method moving out of test identity.** Two liver fibrosis index tests are retired in
favour of one Liver Fibrosis Score test with the formula carried in the analysis method; a
named bone-age method test is retired in favour of a generic Bone Age Estimation test with
the named method as METHOD; a non-histopathological fibrosis score moves from MI to LB.
Terminology itself is applying the boundary this repo uses between Biomedical Concepts and
Dataset Specializations — the method qualifies how an observation is made, it is not the
observation.

**Corrected submission values under a stable code.** One test code carried two different
submission values under the same NCIt concept — a CD28 label in LB, CD8 in MI, with the
NCIt meaning CD8. The release aligns LB to CD8. An instrument version label is corrected
in the same way. Identifier stable, label corrected: the case for keying on the NCIt code
rather than on the submission value.

**New content.** New body-system test codelists (Endocrine and Hematopoietic System
Findings) are routed by the existing rule that derives the domain from the codelist
submission value, so domain metadata needed no change. New instrument codelists arrive
(EORTC modules, a CGI bipolar version, a self-efficacy scale), and test codes grow across
cell phenotyping, cardiovascular, musculoskeletal, tumor, and genomic findings. Some new
musculoskeletal codes reuse test code mnemonics already used in other domains for
unrelated tests, which `link-semantics/Code_Collision_Check` picks up as test codes with
several NCIt codes — test codes are mnemonics, not identifiers.

## Effect on the COSMoS graph

One COSMoS Dataset Specialization pins a test code that this CT release retires; it
surfaces as a new unresolved concept ID in graph validation. That is COSMoS content
trailing the terminology, not a pipeline failure.

The August note expected the procedure and method terms referenced by the new COSMoS
surgery and radiation value lists to clear with the next CT release. They did not: none
was added in 2026-09-25. They now stand as findings on the COSMoS side rather than draft
alignment. On inspection they are not one kind of gap — most are absent from CT, one
exists in CT but in a different codelist, and one is a CDISC synonym of an existing term
used in place of its submission value.

Instrument category resolution and the instrument parent chains are unchanged; the
August watch item on the terminal grouping containers stays open. The CT Result Scale
codelist is unchanged.

## Authoritative current state

File-level current state lives in the README sheet of each machine-actionable xlsx,
regenerated on every run. Counts, column inventories, and coverage percentages are
point-in-time and belong there rather than in this note.

## References

- Upstream change log: [NCI EVS SDTM Terminology Changes](https://evs.nci.nih.gov/ftp1/CDISC/SDTM/SDTM%20Terminology%20Changes.txt)
- Instrument layer watch item: [`cosmos-graph/docs/COSMoS_Instrument_Layer.md`](../cosmos-graph/docs/COSMoS_Instrument_Layer.md) §8
- Previous release: [`Changes_2026-08.md`](Changes_2026-08.md)
