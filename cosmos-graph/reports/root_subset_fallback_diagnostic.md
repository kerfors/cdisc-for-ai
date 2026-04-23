# Root-subset fallback diagnostic

*Generated 2026-04-23 09:58 from `cosmos-graph/scripts/root_subset_fallback_diagnostic.py`. Diagnostic pass scheduled in `docs/COSMoS_Graph_Upstream_Additions.md` §3.5.*

## 1. Summary

- Variables rows scanned: **12,677** (across 1,326 DSSs).
- Assembler resolution: direct **10,626**, compositional **0**, unresolved **2,051**.
- DSSs with at least one unresolved variable: **575**.
- Distinct unresolved variable codes: **103**.
- Post-fix projection: **529** DSSs and **37** distinct codes would remain unresolved after the one-line `var_nn` fix (the residual EVS-gap set).

## 2. Finding

The assembler's compositional fallback (`sdtm-narrative/notebooks/40_assemble_narrative.ipynb` cell 4, `60_assemble_databooks.ipynb` cell 4) looks up `'--' + variable[2:]` in the Root subset of `SDTM_Variable_Identity.xlsx`. The Root subset stores entries **without** a `--` prefix (0 of 174 Root/Variable+Root rows carry `--`), so the compositional key never hits. The entire `'compositional'` resolution tier is structurally inactive today.

- **Direction.** Narrative-layer bug. Fix is one line in `var_nn` — replace `'--' + variable[2:]` with `variable[2:]`.

- **Implication for §2.2.** The 103-unresolved set is a superset of the true EVS gap. Most of it collapses into the bug fix. What remains after the fix is the genuine upstream concern.

## 3. Classification of unresolved codes

After applying the corrected compositional lookup (`variable[2:]` against the Root subset), each unresolved code falls into one of three buckets:

| Bucket | Distinct codes | DSS span (sum) | Variable-row span (sum) |
|---|---:|---:|---:|
| narrative-layer-bug | 66 | 1245 | 1245 |
| evs-root-gap | 37 | 806 | 806 |
| not-compositional | 0 | 0 | 0 |

*DSS span sums per-code DSS counts; a DSS carrying multiple unresolved codes is counted once per code. Not a distinct-DSS count.*

## 4. Worked cases

| Code | Assembler | Bucket | Remainder | Root found | Root NCIt | Root name | DSS count |
|---|---|---|---|---|---|---|---:|
| `RSSTRESN` | unresolved | evs-root-gap | `STRESN` | False |  |  | 104 |
| `MKTESTCD` | unresolved | narrative-layer-bug | `TESTCD` | True | C82503 | Test Code | 50 |
| `MKTEST` | unresolved | narrative-layer-bug | `TEST` | True | C82541 | Test Name | 50 |
| `MKORRES` | unresolved | narrative-layer-bug | `ORRES` | True | C117221 | Original Result or Finding | 50 |
| `MKSTRESC` | unresolved | narrative-layer-bug | `STRESC` | True | C117222 | Character Result or Finding in Standard Format | 50 |
| `ISBDAGNT` | unresolved | evs-root-gap | `BDAGNT` | False |  |  | 290 |

## 5. Per-bucket detail

### 5.1 `narrative-layer-bug` — 66 codes

*These resolve under the corrected compositional lookup. Listed with the suggested root NCIt identity.*

| Code | Prefix | Remainder | DSS count | Root NCIt | Root name | Domains |
|---|---|---|---:|---|---|---|
| `ISTSTDTL` | IS | `TSTDTL` | 73 | C117062 | Measurement, Test or Examination Detail | IS |
| `MKORRES` | MK | `ORRES` | 50 | C117221 | Original Result or Finding | MK |
| `MKSTRESC` | MK | `STRESC` | 50 | C117222 | Character Result or Finding in Standard Format | MK |
| `MKTEST` | MK | `TEST` | 50 | C82541 | Test Name | MK |
| `MKTESTCD` | MK | `TESTCD` | 50 | C82503 | Test Code | MK |
| `MKDTC` | MK | `DTC` | 49 | C82515 | Collection Date Time | MK |
| `MKLOC` | MK | `LOC` | 49 | C13717 | Anatomic Site | MK |
| `MKLAT` | MK | `LAT` | 48 | C25185 | Laterality | MK |
| `GFCAT` | GF | `CAT` | 38 | C25372 | Category | GF |
| `GFDTC` | GF | `DTC` | 38 | C82515 | Collection Date Time | GF |
| `GFMETHOD` | GF | `METHOD` | 38 | C82535 | Test Method | GF |
| `GFORRES` | GF | `ORRES` | 38 | C117221 | Original Result or Finding | GF |
| `GFSPEC` | GF | `SPEC` | 38 | C70713 | Biospecimen Type | GF |
| `GFSTRESC` | GF | `STRESC` | 38 | C117222 | Character Result or Finding in Standard Format | GF |
| `GFTEST` | GF | `TEST` | 38 | C82541 | Test Name | GF |
| `GFTESTCD` | GF | `TESTCD` | 38 | C82503 | Test Code | GF |
| `GFTSTDTL` | GF | `TSTDTL` | 38 | C117062 | Measurement, Test or Examination Detail | GF |
| `MKMETHOD` | MK | `METHOD` | 31 | C82535 | Test Method | MK |
| `FTCAT` | FT | `CAT` | 23 | C25372 | Category | FT |
| `FTDTC` | FT | `DTC` | 23 | C82515 | Collection Date Time | FT |
| `FTSTRESC` | FT | `STRESC` | 23 | C117222 | Character Result or Finding in Standard Format | FT |
| `FTTEST` | FT | `TEST` | 23 | C82541 | Test Name | FT |
| `FTTESTCD` | FT | `TESTCD` | 23 | C82503 | Test Code | FT |
| `MKORRESU` | MK | `ORRESU` | 21 | C82586 | Original Result Unit | MK |
| `MKSTRESU` | MK | `STRESU` | 21 | C82587 | Standard Result Unit | MK |
| `RSORRESU` | RS | `ORRESU` | 19 | C82586 | Original Result Unit | RS |
| `FTSCAT` | FT | `SCAT` | 17 | C25692 | Subcategory | FT |
| `GFANMETH` | GF | `ANMETH` | 15 | C117039 | Analysis Method | GF |
| `RPLAT` | RP | `LAT` | 13 | C25185 | Laterality | RP |
| `RPLOC` | RP | `LOC` | 13 | C13717 | Anatomic Site | RP |
| `FALNKID` | FA | `LNKID` | 12 | C117050 | Record Link Identifier | FA |
| `RSEVLINT` | RS | `EVLINT` | 12 | C82534 | Evaluation Interval | RS |
| `RSSCAT` | RS | `SCAT` | 12 | C25692 | Subcategory | RS |
| `URCAT` | UR | `CAT` | 10 | C25372 | Category | UR |
| `URDTC` | UR | `DTC` | 10 | C82515 | Collection Date Time | UR |
| `URORRES` | UR | `ORRES` | 10 | C117221 | Original Result or Finding | UR |
| `URSTRESC` | UR | `STRESC` | 10 | C117222 | Character Result or Finding in Standard Format | UR |
| `URTEST` | UR | `TEST` | 10 | C82541 | Test Name | UR |
| `URTESTCD` | UR | `TESTCD` | 10 | C82503 | Test Code | UR |
| `BECAT` | BE | `CAT` | 7 | C25372 | Category | BE |
| `BEPARTY` | BE | `PARTY` | 7 | C117052 | Accountable Party | BE |
| `BESPEC` | BE | `SPEC` | 7 | C70713 | Biospecimen Type | BE |
| `BETERM` | BE | `TERM` | 7 | C82571 | Reported Event Term | BE |
| `FTORRESU` | FT | `ORRESU` | 7 | C82586 | Original Result Unit | FT |
| `FTSTRESU` | FT | `STRESU` | 7 | C82587 | Standard Result Unit | FT |
| `RSEVINTX` | RS | `EVINTX` | 7 | C117044 | Evaluation Interval Text | RS |
| `URLAT` | UR | `LAT` | 7 | C25185 | Laterality | UR |
| `URLOC` | UR | `LOC` | 7 | C13717 | Anatomic Site | UR |
| `MHLLT` | MH | `LLT` | 6 | C71886 | MedDRA Lowest Level Term | MH |
| `MHLLTCD` | MH | `LLTCD` | 6 | C117048 | MedDRA Low Level Term Code | MH |
| `MHPTCD` | MH | `PTCD` | 6 | C117056 | MedDRA Preferred Term Code | MH |
| `QSEVINTX` | QS | `EVINTX` | 6 | C117044 | Evaluation Interval Text | QS |
| `URMETHOD` | UR | `METHOD` | 6 | C82535 | Test Method | UR |
| `GFORRESU` | GF | `ORRESU` | 5 | C82586 | Original Result Unit | GF |
| `GFSTRESU` | GF | `STRESU` | 5 | C82587 | Standard Result Unit | GF |
| `MKEVAL` | MK | `EVAL` | 3 | C51824 | Evaluator | MK |
| `URORRESU` | UR | `ORRESU` | 3 | C82586 | Original Result Unit | UR |
| `URSTRESU` | UR | `STRESU` | 3 | C82587 | Standard Result Unit | UR |
| `FAMETHOD` | FA | `METHOD` | 2 | C82535 | Test Method | FA |
| `MKEVALID` | MK | `EVALID` | 2 | C117043 | Evaluator Identifier | MK |
| `URDIR` | UR | `DIR` | 2 | C54215 | Directionality | UR |
| `DDORRESU` | DD | `ORRESU` | 1 | C82586 | Original Result Unit | DD |
| `DDSTRESU` | DD | `STRESU` | 1 | C82587 | Standard Result Unit | DD |
| `QSMETHOD` | QS | `METHOD` | 1 | C82535 | Test Method | QS |
| `RSLOC` | RS | `LOC` | 1 | C13717 | Anatomic Site | RS |
| `VSMETHOD` | VS | `METHOD` | 1 | C82535 | Test Method | VS |

### 5.2 `evs-root-gap` — 37 codes

*The two-char-stripped remainder is genuinely absent from the Root subset. Candidates for a CDISC / NCI EVS content ask.*

| Code | Prefix | Remainder | DSS count | Root NCIt | Root name | Domains |
|---|---|---|---:|---|---|---|
| `ISBDAGNT` | IS | `BDAGNT` | 290 |  |  | IS |
| `RSSTRESN` | RS | `STRESN` | 104 |  |  | RS |
| `MKSTRESN` | MK | `STRESN` | 47 |  |  | MK |
| `GFSYM` | GF | `SYM` | 33 |  |  | GF |
| `GFSYMTYP` | GF | `SYMTYP` | 33 |  |  | GF |
| `GFCHROM` | GF | `CHROM` | 28 |  |  | GF |
| `GFGENLOC` | GF | `GENLOC` | 28 |  |  | GF |
| `GFGENREF` | GF | `GENREF` | 28 |  |  | GF |
| `GFGENSR` | GF | `GENSR` | 28 |  |  | GF |
| `GFSEQID` | GF | `SEQID` | 26 |  |  | GF |
| `FTSTRESN` | FT | `STRESN` | 23 |  |  | FT |
| `SPDEVID` | SP | `DEVID` | 19 |  |  | GF,LB |
| `GFINHERT` | GF | `INHERT` | 18 |  |  | GF |
| `GFPRVID` | GF | `PRVID` | 18 |  |  | GF |
| `FTREASND` | FT | `REASND` | 17 |  |  | FT |
| `GFSTRESN` | GF | `STRESN` | 16 |  |  | GF |
| `BEDECOD` | BE | `DECOD` | 7 |  |  | BE |
| `FTASTDEV` | FT | `ASTDEV` | 6 |  |  | FT |
| `GFCOPYID` | GF | `COPYID` | 5 |  |  | GF |
| `URSTRESN` | UR | `STRESN` | 5 |  |  | UR |
| `TRREASNE` | TR | `REASNE` | 4 |  |  | TR |
| `TULOCDTL` | TU | `LOCDTL` | 3 |  |  | TU |
| `CMRSDISC` | CM | `RSDISC` | 2 |  |  | CM |
| `CMTRTINT` | CM | `TRTINT` | 2 |  |  | CM |
| `CMTRTSTT` | CM | `TRTSTT` | 2 |  |  | CM |
| `PRTRTINT` | PR | `TRTINT` | 2 |  |  | PR |
| `PRTRTSTT` | PR | `TRTSTT` | 2 |  |  | PR |
| `DDSTRESN` | DD | `STRESN` | 1 |  |  | DD |
| `ETHNIC` | ET | `HNIC` | 1 |  |  | DM |
| `PRVIR` | PR | `VIR` | 1 |  |  | TU |
| `PRVIRP` | PR | `VIRP` | 1 |  |  | TU |
| `QSANTXHI` | QS | `ANTXHI` | 1 |  |  | QS |
| `QSANTXLO` | QS | `ANTXLO` | 1 |  |  | QS |
| `QSANVLHI` | QS | `ANVLHI` | 1 |  |  | QS |
| `QSANVLLO` | QS | `ANVLLO` | 1 |  |  | QS |
| `TUPRVIR` | TU | `PRVIR` | 1 |  |  | TU |
| `TUPRVIRP` | TU | `PRVIRP` | 1 |  |  | TU |

### 5.3 `not-compositional` — 0 codes

*Trial-design / relationship / comments domains (SE, SV, TA, TE, TI, TS, TV, CO, RELREC) and two-char codes. Compositional fallback is not the intended resolution path.*

_(empty)_

## 6. Per-bucket domain distribution

| Bucket | Domain | Distinct codes | DSS span |
|---|---|---:|---:|
| evs-root-gap | IS | 1 | 290 |
| evs-root-gap | GF | 11 | 261 |
| evs-root-gap | RS | 1 | 104 |
| evs-root-gap | MK | 1 | 47 |
| evs-root-gap | FT | 3 | 46 |
| evs-root-gap | SP | 1 | 19 |
| evs-root-gap | BE | 1 | 7 |
| evs-root-gap | CM | 3 | 6 |
| evs-root-gap | PR | 4 | 6 |
| evs-root-gap | TU | 3 | 5 |
| evs-root-gap | UR | 1 | 5 |
| evs-root-gap | QS | 4 | 4 |
| evs-root-gap | TR | 1 | 4 |
| evs-root-gap | DD | 1 | 1 |
| evs-root-gap | ET | 1 | 1 |
| narrative-layer-bug | MK | 12 | 424 |
| narrative-layer-bug | GF | 12 | 367 |
| narrative-layer-bug | FT | 8 | 146 |
| narrative-layer-bug | UR | 12 | 88 |
| narrative-layer-bug | IS | 1 | 73 |
| narrative-layer-bug | RS | 5 | 51 |
| narrative-layer-bug | BE | 4 | 28 |
| narrative-layer-bug | RP | 2 | 26 |
| narrative-layer-bug | MH | 3 | 18 |
| narrative-layer-bug | FA | 2 | 14 |
| narrative-layer-bug | QS | 2 | 7 |
| narrative-layer-bug | DD | 2 | 2 |
| narrative-layer-bug | VS | 1 | 1 |

## 7. Conclusion

- **66 of 103 unresolved codes collapse into the narrative-layer bug fix.** §2.2 of `COSMoS_Graph_Upstream_Additions.md` over-reported the upstream concern.
- **37 codes are true EVS Root-subset gaps** — worth a CDISC / NCI EVS ask.
- **0 codes are not-compositional** — trial-design / comments / relationship / two-char variables. Not an upstream issue; their identity resolution goes through the direct tier or is out of scope.
- **Recommendation.** Fix `var_nn` in `sdtm-narrative/notebooks/40_assemble_narrative.ipynb` cell 4 and `60_assemble_databooks.ipynb` cell 4 (`'--' + variable[2:]` → `variable[2:]`). Re-run the narrative assembler; `has_unresolved` count should drop to the evs-root-gap set only.
- **Upstream additions document.** §2.2 and §3.5 should be updated to reflect that the bulk of the finding was a narrative-layer regression, with a residual EVS-gap list to carry forward.

## 8. Caveats on the evs-root-gap bucket

A handful of codes in §5.2 are not genuine Root-subset gaps — they are **direct-tier Variable_Identity gaps** that the plain two-char strip miscategorises:

- `ETHNIC` — prefix `ET`, domain `DM`. `ETHNIC` is a full DM variable, not a compositional form. Absent from the direct table. A direct-tier identity-build concern, not an EVS Root concern.
- Any evs-root-gap row where the `domain_prefix` does not match the `domains` column is suspect in the same way. Filter the CSV with `domain_prefix != domains.split(',')[0]` to see these.

The diagnostic faithfully applies the approved plain two-char strip and lets these fall into evs-root-gap for visibility. A follow-up classification pass could split this bucket into `true-evs-root-gap` and `direct-tier-gap`. Out of scope for §3.5, but worth capturing for a future identity-build iteration.
