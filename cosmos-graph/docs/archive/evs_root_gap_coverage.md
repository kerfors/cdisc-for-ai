# EVS coverage of the 37 root-subset fallback gaps

*Follow-up to `root_subset_fallback_diagnostic.md` §8.
 Read-only pass against `sdtm-test-codes/downloads/Thesaurus.txt` (NCI Thesaurus FLAT).
 Companion CSV: `evs_root_gap_coverage.csv`.*

## 1. What this pass answers

The root-subset diagnostic left 37 codes in the `evs-root-gap` bucket after applying the correct compositional strip. §8 flagged that this bucket conflates two distinct causes. This pass separates them by looking each code up directly in the NCI Thesaurus (which is upstream of the CDISC Variable/Root Variable Terminology subsets used by `SDTM_Variable_Identity.xlsx`).

Variants checked per code: the full variable code (`RSSTRESN`), the two-char-stripped remainder (`STRESN`), the `SDTM-`-prefixed form (`SDTM-RSSTRESN`, `SDTM-STRESN`), and the dash-dash form (`--STRESN`). Match is exact against the pipe-delimited synonym block in `Thesaurus.txt`.

## 2. Result

| Classification | Codes | DSS span | Meaning |
|---|---:|---:|---|
| absent-from-thesaurus | 33 | 778 | No matching Thesaurus concept on any variant. Genuine upstream content gap. |
| root-variable-terminology | 1 | 19 | `SPDEVID` → C117060, flagged Root as the full code. |
| other-cdisc | 2 | 8 | `BEDECOD` → C124297 (codelist anchor, not variable); `PRVIR` → C17255 (Virgin Islands — false-positive). |
| has-non-cdisc-hit | 1 | 1 | `ETHNIC` → C66790 "CDISC SDTM Ethnic Group Terminology" (codelist anchor, Thesaurus row carries no CDISC subset flag). |

Net: **34 codes are true EVS content gaps** (33 absent + ETHNIC not flagged). Three are build-layer edge cases that a sharper identity-build pass could resolve without touching EVS.

## 3. The 33 absent codes

Grouped by pattern:

- **`--STRESN` root missing, domain variants incomplete** (6 codes, 196 DSSs). The Root subset has `--STRESC`, `--STRESU`, `--STRESCFL`, etc. but not `--STRESN`. The full Variable Terminology carries `FASTRESN`, `TRSTRESN`, `ISSTRESN` — but not `RSSTRESN`, `MKSTRESN`, `FTSTRESN`, `GFSTRESN`, `URSTRESN`, `DDSTRESN`. Either publish `--STRESN` at Root or complete the per-domain set.

- **GF (Genetic Findings) domain block** (11 codes, 263 DSSs). `GFSYM`, `GFSYMTYP`, `GFCHROM`, `GFGENLOC`, `GFGENREF`, `GFGENSR`, `GFSEQID`, `GFINHERT`, `GFPRVID`, `GFSTRESN`, `GFCOPYID`. GF is new in SDTMIG 3.4; the Variable-CT catch-up hasn't landed.

- **IS / FT / TR / TU / BE / CM / PR additions** (12 codes, 321 DSSs). `ISBDAGNT` (290 DSSs — the biggest single hit), `FTREASND`, `FTASTDEV`, `TRREASNE`, `TULOCDTL`, `CMRSDISC`, `CMTRTINT`, `CMTRTSTT`, `PRTRTINT`, `PRTRTSTT`, `PRVIRP`, `TUPRVIR`, `TUPRVIRP`. Mostly SDTMIG 3.3 / 3.4 additions; root-level compositional forms (`--TRTINT`, `--TRTSTT`, `--RSDISC`, `--REASND`, `--REASNE`, `--LOCDTL`, `--ASTDEV`) would resolve the set.

- **QS abnormal thresholds** (4 codes, 4 DSSs). `QSANTXHI`, `QSANTXLO`, `QSANVLHI`, `QSANVLLO`.

## 4. The 3 build-layer edge cases

- **SPDEVID** (19 DSSs). Exists in Root subset as the **full code** C117060 "Sponsor Device Identifier", not as a `--DEVID` root remainder. `var_nn` misses it because direct-table lookup excludes Root entries and compositional-table lookup uses the bare remainder `DEVID`. Fix: either store `SPDEVID` as a domain-specific Variable subset entry, or extend `var_nn`'s direct tier to include Root entries whose Variable field carries a domain prefix.

- **BEDECOD** (7 DSSs). Thesaurus has C124297 "CDISC SDTM Biospecimen Events Dictionary Derived Term Terminology" — a **codelist anchor**, not a Variable concept. Not a Variable-CT entry to harvest; treat as genuine gap.

- **ETHNIC** (1 DSS). Thesaurus C66790 "CDISC SDTM Ethnic Group Terminology" — also a codelist anchor, subset column empty. Same treatment.

## 5. NSV question — not the right source

The 2023-04 CDISC Approved Non-Standard Variables list is a registry for supplemental qualifier variables that are *not* in the standard SDTMIG. The 37 codes here are all standard IG variables. Their identity belongs in the CDISC Root Variable Terminology / CDISC Variable Terminology subsets of the NCI Thesaurus, not in the NSV registry. NSV does not close this gap.

## 6. Recommended ask to CDISC / NCI EVS

Promote or add the following to the **CDISC Root Variable Terminology** subset of Thesaurus (bare root form, no `--` prefix in the synonym block):

`STRESN`, `BDAGNT`, `SYM`, `SYMTYP`, `CHROM`, `GENLOC`, `GENREF`, `GENSR`, `SEQID`, `INHERT`, `PRVID`, `REASND`, `REASNE`, `LOCDTL`, `COPYID`, `RSDISC`, `TRTINT`, `TRTSTT`, `ASTDEV`, `VIRP`, `PRVIR`, `PRVIRP`, `ANTXHI`, `ANTXLO`, `ANVLHI`, `ANVLLO`.

That would close ~32 of the 34 unresolved codes and let the narrative assembler reach full compositional identity coverage.
