# COSMoS Graph Validation Report

_Generated: 2026-11-25_

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
| value_list_resolution_summary | INFO | 3279 |
| value_list_unresolved_members | INFO | 7 |
| schema_column_coverage | FAIL | 13 |
| vlm_source_hyphen_detail | INFO | 4 |
| empty_reification_quad_rows | INFO | 705 |
| dss_without_any_edge | INFO | 4 |
| ct_unresolved_concept_ids | FAIL | 18 |
| pinned_term_not_in_bound_codelist | FAIL | 26 |


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


### value_list_resolution_summary — INFO (3279)

| metric | count |
| --- | --- |
| total_value_list_rows | 3279 |
| all_resolved | 2554 |
| partial | 4 |
| none_resolved | 0 |
| no_codelist | 719 |
| codelist_not_in_ct | 2 |
| unique_unresolvable_pairs | 7 |


### value_list_unresolved_members — INFO (7)

| codelist | member | row_count |
| --- | --- | --- |
| LOC | ABDOMEN | 1 |
| METHOD | AUTOPSY | 1 |
| PROCEDUR | LYMPH NODE DISSECTION | 1 |
| PROCEDUR | RADIOSURGERY | 1 |
| PROCEDUR | SIMPLE MASTECTOMY | 1 |
| PROCEDUR | STEREOTACTIC BODY RADIATION THERAPY | 1 |
| PROCEDUR | TOTAL MASTECTOMY | 1 |


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


### empty_reification_quad_rows — INFO (705)

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


### ct_unresolved_concept_ids — FAIL (18)

| source | concept_id | context | variable_uses_count |
| --- | --- | --- | --- |
| Codelists | C66790 | codelist_concept_id | 1 |
| Codelists | C74457 | codelist_concept_id | 1 |
| Variables | C126289 | assigned_term_concept_id | 1 |
| Variables | C132388 | assigned_term_concept_id | 2 |
| Variables | C15221 | assigned_term_concept_id | 1 |
| Variables | C15265 | assigned_term_concept_id | 1 |
| Variables | C15271 | assigned_term_concept_id | 1 |
| Variables | C15281 | assigned_term_concept_id | 1 |
| Variables | C15284 | assigned_term_concept_id | 1 |
| Variables | C15328 | assigned_term_concept_id | 1 |
| Variables | C157425 | assigned_term_concept_id | 2 |
| Variables | C171439 | assigned_term_concept_id | 2 |
| Variables | C172954 | assigned_term_concept_id | 2 |
| Variables | C181502 | assigned_term_concept_id | 2 |
| Variables | C229123 | assigned_term_concept_id | 2 |
| Variables | C229124 | assigned_term_concept_id | 2 |
| Variables | C47850 | assigned_term_concept_id | 2 |
| Variables | C52006 | assigned_term_concept_id | 1 |


### pinned_term_not_in_bound_codelist — FAIL (26)

| issue_type | ds_id | variable_name | codelist_concept_id | codelist_submission_value | assigned_term_concept_id | assigned_term_value |
| --- | --- | --- | --- | --- | --- | --- |
| pinned_term_not_in_bound_codelist | DEPTHLIVER | GITESTCD | C128682 | GASTROCD | C25333 | DEPTH |
| pinned_term_not_in_bound_codelist | DEPTHLIVER | GITEST | C128681 | GASTRO | C25333 | Depth |
| pinned_term_not_in_bound_codelist | LENGTHLIVER | GITESTCD | C128682 | GASTROCD | C25334 | LENGTH |
| pinned_term_not_in_bound_codelist | LENGTHLIVER | GITEST | C128681 | GASTRO | C25334 | Length |
| pinned_term_not_in_bound_codelist | WIDTHLIVER | GITESTCD | C128682 | GASTROCD | C25345 | WIDTH |
| pinned_term_not_in_bound_codelist | WIDTHLIVER | GITEST | C128681 | GASTRO | C25345 | Width |
| pinned_term_not_in_bound_codelist | DEPTHSPLEEN | HMTESTCD | C228168 | HMTESTCD | C25333 | DEPTH |
| pinned_term_not_in_bound_codelist | DEPTHSPLEEN | HMTEST | C228167 | HMTEST | C25333 | Depth |
| pinned_term_not_in_bound_codelist | LENGTHSPLEEN | HMTESTCD | C228168 | HMTESTCD | C25334 | LENGTH |
| pinned_term_not_in_bound_codelist | LENGTHSPLEEN | HMTEST | C228167 | HMTEST | C25334 | Length |
| pinned_term_not_in_bound_codelist | VOLSPLEEN | HMTESTCD | C228168 | HMTESTCD | C74720 | VOLUME |
| pinned_term_not_in_bound_codelist | VOLSPLEEN | HMTEST | C228167 | HMTEST | C74720 | Volume |
| pinned_term_not_in_bound_codelist | WIDTHSPLEEN | HMTESTCD | C228168 | HMTESTCD | C25345 | WIDTH |
| pinned_term_not_in_bound_codelist | WIDTHSPLEEN | HMTEST | C228167 | HMTEST | C25345 | Width |
| pinned_term_not_in_bound_codelist | LMNDEXAMBREAST | MITESTCD | C132263 | MITSCD | C124446 | LMNDEXAM |
| pinned_term_not_in_bound_codelist | LMNDEXAMBREAST | MITEST | C132262 | MITS | C124446 | Number of Lymph Nodes Examined |
| pinned_term_not_in_bound_codelist | LMNDPNUMBREAST | MITESTCD | C132263 | MITSCD | C124447 | LMNDPNUM |
| pinned_term_not_in_bound_codelist | LMNDPNUMBREAST | MITEST | C132262 | MITS | C124447 | Number of Lymph Nodes Positive |
| pinned_term_not_in_bound_codelist | ULTRASOUND | PRDECOD | C101858 | PROCEDUR | C17230 | ULTRASOUND IMAGING |
| pinned_term_not_in_bound_codelist | ULTRASOUNDELAST | PRDECOD | C101858 | PROCEDUR | C172563 | ULTRASONOGRAPHIC ELASTOGRAPHY |
| pinned_term_not_in_bound_codelist | DEPTHKIDNEY | URTESTCD | C129942 | URNSTSCD | C25333 | DEPTH |
| pinned_term_not_in_bound_codelist | DEPTHKIDNEY | URTEST | C129941 | URNSTS | C25333 | Depth |
| pinned_term_not_in_bound_codelist | VOLKIDNEY | URTESTCD | C129942 | URNSTSCD | C74720 | VOLUME |
| pinned_term_not_in_bound_codelist | VOLKIDNEY | URTEST | C129941 | URNSTS | C74720 | Volume |
| pinned_term_not_in_bound_codelist | WIDTHKIDNEY | URTESTCD | C129942 | URNSTSCD | C25345 | WIDTH |

_showing first 25 of 26 — full list in JSON sidecar_

