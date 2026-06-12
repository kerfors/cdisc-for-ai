# COSMoS Graph Validation Report

_Generated: 2026-06-12_

Inputs: `COSMoS_Graph.xlsx`, `COSMoS_Graph_CT.xlsx`


## Summary

| Check | Status | Count |
| --- | --- | --- |
| enumeration_validation | PASS | 0 |
| referential_integrity | PASS | 0 |
| bc_parents_bc_id_referential_integrity | PASS | 0 |
| bc_parents_parent_bc_id_referential_integrity | PASS | 0 |
| bc_categories_bc_id_referential_integrity | PASS | 0 |
| bc_categories_vocabulary_closure | PASS | 0 |
| coding_bc_id_referential_integrity | PASS | 0 |
| data_element_concepts_bc_id_referential_integrity | PASS | 0 |
| value_list_codelist_binding_integrity | PASS | 0 |
| value_list_resolution_summary | INFO | 2713 |
| value_list_unresolved_members | INFO | 4 |
| schema_column_coverage | FAIL | 13 |
| vlm_source_hyphen_detail | INFO | 4 |
| empty_reification_quad_rows | INFO | 315 |
| dss_without_any_edge | INFO | 4 |
| ct_unresolved_concept_ids | FAIL | 4 |
| pinned_term_not_in_bound_codelist | INFO | 0 |


## Details

### enumeration_validation — PASS (0)

_no details_


### referential_integrity — PASS (0)

_no details_


### bc_parents_bc_id_referential_integrity — PASS (0)

_no details_


### bc_parents_parent_bc_id_referential_integrity — PASS (0)

_no details_


### bc_categories_bc_id_referential_integrity — PASS (0)

_no details_


### bc_categories_vocabulary_closure — PASS (0)

_no details_


### coding_bc_id_referential_integrity — PASS (0)

_no details_


### data_element_concepts_bc_id_referential_integrity — PASS (0)

_no details_


### value_list_codelist_binding_integrity — PASS (0)

_no details_


### value_list_resolution_summary — INFO (2713)

| metric | count |
| --- | --- |
| total_value_list_rows | 2713 |
| all_resolved | 2205 |
| partial | 4 |
| none_resolved | 0 |
| no_codelist | 502 |
| codelist_not_in_ct | 2 |
| unique_unresolvable_pairs | 4 |


### value_list_unresolved_members — INFO (4)

| codelist | member | row_count |
| --- | --- | --- |
| NY | NA | 2 |
| METHOD | AUTOPSY | 1 |
| PROCEDUR | RADIOSURGERY | 1 |
| PROCEDUR | STEREOTACTIC BODY RADIATION THERAPY | 1 |


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


### empty_reification_quad_rows — INFO (315)

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


### ct_unresolved_concept_ids — FAIL (4)

| source | concept_id | context | variable_uses_count |
| --- | --- | --- | --- |
| Codelists | C66790 | codelist_concept_id | 1 |
| Codelists | C74457 | codelist_concept_id | 1 |
| Variables | C132388 | assigned_term_concept_id | 2 |
| Variables | C171439 | assigned_term_concept_id | 2 |


### pinned_term_not_in_bound_codelist — INFO (0)

_no details_

