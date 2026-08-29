# Pinned DDS base (cdisc-org/DataExchange-DDS)

Unmodified copies, pinned so the profile differential and its tooling run
against known inputs — same discipline as ../../downloads/.

- `dds.yaml` — the base DDS LinkML model (`id: https://cdisc.org/dds`).
  NOTE: the base model carries NO `version:` field, so the profiling
  spec's R1 version gate cannot bind; the snapshot tool is run with
  `--allow-unversioned-base` and the pin below is the effective version.
- `PROFILING_SPECIFICATION.md` — DDS Profiling Specification v0.1.0.
- `dds_profile_snapshot.py` — the reference snapshot resolver (R1-R7).

Source: https://github.com/cdisc-org/DataExchange-DDS
Pinned at commit d2328345cd0a13d92c6c95e966a63ea85f274491 (2026-08-25,
merge of feature/profiles). Copied 2026-08-29. Do not edit; refresh only
deliberately, re-running snapshot + validation afterwards.
