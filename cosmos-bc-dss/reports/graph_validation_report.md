# COSMoS Graph Validation Report

_Generated: 2026-04-22_

Inputs: `COSMoS_Graph.xlsx`, `COSMoS_Graph_CT.xlsx`


## Summary

| Check | Status | Count |
| --- | --- | --- |
| enumeration_validation | PASS | 0 |
| referential_integrity | PASS | 0 |
| schema_column_coverage | FAIL | 13 |
| vlm_source_hyphen_detail | INFO | 4 |
| empty_reification_quad_rows | INFO | 313 |
| dss_without_any_edge | INFO | 4 |
| ct_unresolved_concept_ids | FAIL | 6 |
| pinned_term_not_in_bound_codelist | FAIL | 1 |


## Details

### enumeration_validation — PASS (0)

_no details_


### referential_integrity — PASS (0)

_no details_


### schema_column_coverage — FAIL (13)

| issue | name |
| --- | --- |
| xlsx_column_not_in_schema | assigned_term_concept_id |
| xlsx_column_not_in_schema | assigned_term_value |
| xlsx_column_not_in_schema | codelist_concept_id |
| xlsx_column_not_in_schema | codelist_submission_value |
| xlsx_column_not_in_schema | dec_id |
| xlsx_column_not_in_schema | is_nonstandard |
| xlsx_column_not_in_schema | variable_name |
| schema_slot_not_in_xlsx | assigned_term |
| schema_slot_not_in_xlsx | codelist |
| schema_slot_not_in_xlsx | data_element_concept_id |
| schema_slot_not_in_xlsx | is_non_standard |
| schema_slot_not_in_xlsx | name |
| schema_slot_not_in_xlsx | relationship |


### vlm_source_hyphen_detail — INFO (4)

| ds_id | domain | source | ds_short_name |
| --- | --- | --- | --- |
| SAR2ABDET | MB | MB-MBTESTCD | SARS-CoV-2 Antibody Detection |
| SAR2RNAQNTCYC | MB | MB-MBTESTCD | SARS-CoV-2 RNA Quantification Cycle Number |
| SAR2RNAVIRAL | MB | MB-MBTESTCD | SARS-CoV-2 RNA Viral Load |
| SARSCOV2DET | MB | MB-MBTESTCD | SARS-CoV-2 Detection |


### empty_reification_quad_rows — INFO (313)

| note |
| --- |
| Variables rows without a reification quad; not counted in Relationships sheet |


### dss_without_any_edge — INFO (4)

| ds_id |
| --- |
| BRTHDTC |
| ETHNIC |
| RACE |
| SEX |


### ct_unresolved_concept_ids — FAIL (6)

| source | concept_id | context | variable_uses_count |
| --- | --- | --- | --- |
| Codelists | C66790 | codelist_concept_id | 1 |
| Codelists | C74457 | codelist_concept_id | 1 |
| Variables | C132388 | assigned_term_concept_id | 2 |
| Variables | C171439 | assigned_term_concept_id | 2 |
| Variables | C94525 | assigned_term_concept_id | 4 |
| Variables | C96642 | assigned_term_concept_id | 4 |


### pinned_term_not_in_bound_codelist — FAIL (1)

| issue_type | ds_id | variable_name | codelist_concept_id | codelist_submission_value | assigned_term_concept_id | assigned_term_value |
| --- | --- | --- | --- | --- | --- | --- |
| pinned_term_not_in_bound_codelist | OXYSAT | VSSTRESU | C66770 | VSRESU | C105484 | fraction of 1 |

