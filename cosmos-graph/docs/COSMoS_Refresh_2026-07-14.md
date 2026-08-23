# Graph refresh — COSMoS package 2026-07-14

**Reference versions:** COSMoS BC/DSS bumped **2026-05-26 → 2026-07-14**. SDTM CT (NCI EVS
2026-03-27) and SDTMIG v3.4 / SDTM v2.0 unchanged — the June 2026 CT quarterly did not
happen, so the CT pin is still current. CRF Specializations draft again held out of scope.
This is an upstream data refresh, not a projection change — the flatten and downstream
notebooks are unchanged; only their inputs moved.

## What moved in the source

Where 2026-05-26 was a metadata backfill on a stable concept set, 2026-07-14 is the
opposite: a **content release**. Both layers grow substantially and the field-level churn
on surviving rows is small.

**BC — 125 new concepts, no removals.** The additions cluster: a large Subject
Characteristics expansion (demographic, socioeconomic, birth-and-family, and
disease-exposure concepts — Birth Country, Gender Identity, Employment Status, insurance
and student indicators, exposure geography); the PASI Fredriksson (PASI03) question set
and the AJCC Cancer Staging Manual 7th Edition classification chain (T/N/M/Anatomic
Stage/Residual Tumor plus containers) on the QRS-classification side; hepatitis B/C
serology and other lab concepts; and breast-cancer procedure and imaging concepts
(Photography, Scintigraphy). Churn on surviving BCs is surgical: three parent moves —
PET (C17007) and CT (C17204) reparented under a Tomography node (C38093), Estimated Date
of Delivery (C81247) gaining a parent — plus a handful of category, synonym, and
result-scale corrections.

**DSS — the group set grows for the first time since March: +151 groups, −2.** The
additions land in SC (the Subject Characteristics expansion, one group per new BC), IS
(per-allergen "Mast 7-Class" groups, all under C181398 allergen-specific IgE — the known
maximum fan-out grows again), RS (AJCC v7 and PASI03 component groups plus Disease
Recurrence Indicator), PR (imaging and breast-cancer surgery: CT abdomen/pelvis, PET,
photography, scintigraphy, prespecified and free-text surgery groups), MB (hepatitis
serology concentration/presence pairs), and single groups in MH, LB, MI, TU.

**The two removals are domain moves, not retirements.** `EDLVRDTC` and `EGESTAGE` leave
RP and reappear in SC with the same `vlm_group_id` and the same BCs (C81247, C122188).
The observation is untouched; only where it is filed moved — a live upstream instance of
the BC/DSS boundary rule. Anything keying on `(domain, vlm_group_id)` sees RP shrink by
two groups.

## Rebuild results

The graph track and every consumer rebuilt cleanly on the new package; the pipeline is
unchanged.

**Validation (notebook 30):** no new failures. The two long-standing FAIL checks
(`schema_column_coverage`, `ct_unresolved_concept_ids`) are byte-identical to the May run.
The value-list resolution summary grows with the content: the new breast-cancer surgery
and radiation value lists reference several PROCEDUR members (and AUTOPSY in METHOD) that
are not in the pinned SDTM CT 2026-03-27 — expected, since the package post-dates the CT
release it will eventually align with; these surface as unresolved members, not failures.

**Instrument category resolution (notebook 50):** no status transitions on existing
tokens — in particular the 6MWT long-form label remains unresolved (the rename fragility
recorded in `COSMoS_Instrument_Layer.md` §8 did not propagate into the category tokens).
Seven new tokens arrive with the PASI03 and AJCC v7 chains; the PASI names resolve by
exact name or synonym, the AJCC long-form classification labels join the unresolved set —
the same label-vs-identifier gap, now on the classification side.

**Instrument parent chains (notebook 51):** the §8 watch item did **not** resolve.
C222259 and C222260 are still terminal (`parent_bc_id` empty) in 2026-07-14, each still
carrying exactly one instrument child. The expected wiring back to C81250 has not
arrived; the watch item stays open. The new PASI03 / AJCC v7 material sits in the
Clinical or Research Assessment Classification family and does not use the new tier.

**Downstream:** `consumer-bases` and the three `sdtm-findings-graph` consumers rebuilt on
the new graph. The growth propagates exactly along the domain split above — the specimen
consumer picks up the LB/MB/MI groups, the instrument consumer the RS chains, and the
measurement consumer is untouched. PR reachability gains the new imaging and surgery
groups. Row-level counts are point-in-time and live in each file's README sheet.

## Still pending after this note

CRF Specializations deferred (see `COSMoS_Open_Work.md`). `sdtm-test-codes` and
`sdtm-domain-reference` were not re-run — SDTM CT did not move this pass. The per-DSS
instance YAML under `cosmos-bc-dss/downloads/cosmos_yaml/` was again not refreshed; it is
not on the refresh path. The ingestion-source decision (public flat export, not the
member-gated API) is recorded in `docs/COSMoS_Ingestion_Source.md` and was applied
unchanged here.
