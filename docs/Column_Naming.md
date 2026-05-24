# Column Naming

## Why this document exists

Column names in `cdisc-for-ai` have grown by accretion. Each track (`cosmos-graph`, `consumer-bases`, `sdtm-findings-graph`, the retired `sdtm-findings`) made local choices about casing, suffixes, and whether to stay source-faithful or to translate. The result is readable in any one file but inconsistent across the repo. This document does not catalogue the existing columns — a full inventory dates fast and creates maintenance burden. It establishes the principles that future renames and new columns should follow, with worked examples covering the cases that actually come up.

The trigger was the `ds_id` column. Its values are CDISC mnemonics (`VS_SYSBP`, `LB_GLUC`). The suffix `_id` claims properties — uniqueness, persistence, machine-addressability — that those values do not have. Renaming to `ds_code` is a truthful labeling move. The principles below generalise that move.

## Principles

**1. The suffix should describe what the value IS, not what we wish it were.** This is the load-bearing principle. A column called `ds_id` invites consumers to treat the value as a stable identifier; a column called `ds_code` signals that the value is a human-facing mnemonic from a controlled set, with no guarantee of uniqueness across domains and no persistence contract across versions. Truthful suffixes prevent downstream code from being built on assumptions the data does not support.

**2. Architectural layer is encoded by colour in xlsx headers, not by column name.** The repo already carries layer identity in the green/yellow/chocolate/copper/grey palette (Identity / COSMoS DSS / Instrument C20993 / Container C211913 / Neutral). Prefixing column names with `cosmos_`, `evs_`, or `ncit_` to repeat that information adds verbosity without adding signal in the spreadsheets where readers actually look. Layer prefixes are reserved for the cases where the same logical column appears at two layers in the same sheet and disambiguation would otherwise be impossible (the `Instrument_NCIt_*` / `Container_NCIt_*` split is the model — colour distinguishes them, but the prefix is still needed because both could otherwise be called `NCIt_Code`).

**3. Source-faithful at upstream layers; consumer-friendly at consumer layers.** `cosmos-graph` is not strictly source-faithful — it already translates `vlm_group_id` to `ds_id` (and now `ds_code`). The graph layer's job is accurate projection of COSMoS into a normal-form schema, which means it can rename for clarity but should not invent new vocabulary. Consumer files (`consumer-bases`, `sdtm-findings-graph`) are explicitly allowed to translate further — flattening, renaming for readability, dropping internal grouping artefacts. The rule of thumb: a column that originated upstream keeps its upstream name unless the consumer's audience would be misled by it.

**4. Casing follows the value's origin, not the file's track.** CDISC traditional variable names (`TESTCD`, `ORRES`, `STDTC`) keep their uppercase form. They are not strings we coined; they are names the standard already published. Repo-coined column names use `snake_case`. Mixed forms (`NCIt_Code`, `Observation_Class`) are tolerated where they have settled into established files — renaming them in place would create churn out of proportion to the gain — but new columns should pick uppercase-if-CDISC or snake_case-if-coined, not the mixed form.

**5. Accurate naming is a step toward, not a substitute for, machine-addressability.** Renaming `ds_id` to `ds_code` does not solve the question of how DSS instances are addressed (URIs, NCIt at DSS level, some other scheme — open upstream). The point of the rename is to stop the column from making a claim the values cannot support. The day a real DSS identifier exists, it will live in a new column called `ds_id` or `dss_uri`, and `ds_code` will sit beside it as the human-facing mnemonic.

## Suffix vocabulary

The suffixes the repo uses, with the meaning they carry once this convention is in force:

- `_id` — unique, persistent identifier. Machine-addressable. Example: `bc_id` (COSMoS Biomedical Concept identifier — actually unique and stable).
- `_code` — mnemonic from a controlled set. Human-readable, not guaranteed unique across contexts, not a stable identifier. Example: `ds_code` (the CDISC dataset-specialisation mnemonic).
- `_ncit_code` (or `_ncit`) — an NCI Thesaurus C-code. A specific, well-defined identifier scheme; worth distinguishing from generic `_code` because the addressability contract is stronger.
- `_label` or `_preferred_term` — the human-readable name attached to a code. `_preferred_term` is preferred when the value comes from NCIt's `Preferred Term` slot specifically; `_label` is the generic fallback.
- `_terms` — a value list, typically a codelist of submission values. Plural matters: it signals that the cell may hold more than one value.

CDISC traditional names (`TESTCD`, `TEST`, `CAT`, `STDTC`, `ORRES`, `ORRESU`) sit outside this suffix system. They are accepted as published.

## Worked examples

**`ds_id` → `ds_code`.** The values are CDISC mnemonics (`VS_SYSBP`, `LB_GLUC`). They are not unique across the dataset universe (the same mnemonic can occur in different observation classes in principle), they are not persistent identifiers, and they have no addressable form. `_code` is the truthful suffix. Affects `cosmos-graph/notebooks/10_flatten_schema_driven.ipynb`, `consumer-bases/notebooks/10_dss_view.ipynb` and `20_dss_variables_view.ipynb`, the three `sdtm-findings-graph/` consumer notebooks (which read it through), plus README and doc references.

**`bc_id` stays.** The values are actual COSMoS BC identifiers — unique, persistent, machine-addressable. The `_id` suffix is accurate. No rename.

**`TESTCD` stays uppercase.** It is a CDISC-published variable name, not something the repo coined. Renaming to `testcd` or `test_code` would erase the signal that this column corresponds directly to the standard.

**`Instrument_NCIt_Code` / `Container_NCIt_Code`.** These keep their layer prefix because both refer to NCIt codes but at different grains (C20993 instrument tree vs C211913 question container tree). Colour distinguishes them visually (chocolate vs copper); the prefix distinguishes them in any context where colour is not available — code, joins, prose. The `NCIt` casing is the established mixed form; new sibling columns should match it for local consistency rather than reverting to `snake_case` mid-file.

**`Allowed_Units_Terms` is plural.** The cell holds a list (the codelist expanded per row when narrower than the 50-value threshold). `_terms` plural is the signal. A singular `_term` or `_code` would imply scalar content and mislead consumers writing flatten logic.

**Mixed-form legacy columns (`NCIt_Code`, `Observation_Class`, `Preferred_Term`).** These are repo-coined names that pre-date this convention. A coordinated rewrite is not worth the churn — every consumer notebook, every join, every README example would need touching for a benefit (uniform casing) that is aesthetic rather than correctness. The policy is migrate-on-next-touch: when a file containing these columns is being modified for other reasons, the rename rides along on that work. CDISC-published names (`TESTCD`, `ORRES`, `STDTC`) are never migrated — they are not repo-coined and the mixed form is the standard's form.

## Scope of application

This convention applies to:

- new columns in any track,
- columns being renamed for accuracy (`ds_id` → `ds_code` is the immediate case),
- the column documentation in README sheets and `docs/`.

It does not force retroactive rewrites of columns that have no accuracy problem. The goal is to stop inconsistency from growing and let the repo converge over time. Mixed-form legacy names migrate on next touch — when a file containing them is being modified for other reasons, the rename rides along. Accuracy renames (the suffix lies about what the value is, principle 1) are the priority case and warrant their own scoped work; casing migrations are opportunistic. Each rename should have a reason that points back to a principle here.
