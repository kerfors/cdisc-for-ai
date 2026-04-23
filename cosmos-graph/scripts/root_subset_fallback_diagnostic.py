"""Root-subset fallback diagnostic — §3.5 of COSMoS_Graph_Upstream_Additions.md.

Reproduces the narrative assembler's two-tier variable-identity resolution pass,
enumerates the unresolved set, and classifies each unresolved code into one of:

    narrative-layer-bug   remainder IS present in SDTM_Variable_Identity Root subset
    evs-root-gap          remainder is NOT present in Root subset
    not-compositional     domain prefix cannot be plainly two-char-stripped

Inputs
    cosmos-graph/interim/COSMoS_Graph.xlsx                Variables, DSS
    sdtm-narrative/reference/SDTM_Variable_Identity.xlsx  Variable_Identity

Outputs
    cosmos-graph/reports/root_subset_fallback_diagnostic.md   narrative report
    cosmos-graph/reports/root_subset_fallback_diagnostic.csv  one row per unresolved code

Run from repo root:
    python cosmos-graph/scripts/root_subset_fallback_diagnostic.py
"""

from __future__ import annotations

from pathlib import Path
from datetime import datetime

import pandas as pd


REPO = Path(__file__).resolve().parents[2]
GRAPH_XLSX = REPO / "cosmos-graph" / "interim" / "COSMoS_Graph.xlsx"
IDENT_XLSX = REPO / "sdtm-narrative" / "reference" / "SDTM_Variable_Identity.xlsx"
REPORT_MD = REPO / "cosmos-graph" / "reports" / "root_subset_fallback_diagnostic.md"
REPORT_CSV = REPO / "cosmos-graph" / "reports" / "root_subset_fallback_diagnostic.csv"

# Domain prefixes that are not plain two-char strippable in the compositional sense.
# SE/SV/TA/TE/TI/TS/TV are trial-design domains; CO is comments; RELREC is relationship;
# SUPP-- is the supplemental qualifier family. For these, a `--REMAINDER` root lookup
# is not the intended identity path.
NON_COMPOSITIONAL_PREFIXES = frozenset({"SE", "SV", "TA", "TE", "TI", "TS", "TV", "CO"})
NON_COMPOSITIONAL_FULL = frozenset({"RELREC"})


def load_inputs() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    variables = pd.read_excel(GRAPH_XLSX, sheet_name="Variables")
    dss = pd.read_excel(GRAPH_XLSX, sheet_name="DSS")
    ident = pd.read_excel(IDENT_XLSX, sheet_name="Variable_Identity")
    return variables, dss, ident


def build_resolver(ident: pd.DataFrame):
    """Return the three lookups: assembler-direct, assembler-root (as coded), corrected-root.

    The assembler code (sdtm-narrative/notebooks/40_assemble_narrative.ipynb cell 4,
    60_assemble_databooks.ipynb cell 4) splits the identity table by Subset and looks
    up `'--' + variable[2:]` in the Root half. SDTM_Variable_Identity stores Root
    entries WITHOUT a `--` prefix, so that key never hits. The corrected lookup drops
    the `--` prefix.
    """
    direct = (
        ident[ident["Subset"] != "Root"]
        .drop_duplicates(subset=["Variable"], keep="first")
        .set_index("Variable")
    )
    root = (
        ident[ident["Subset"].isin(["Root", "Variable+Root"])]
        .drop_duplicates(subset=["Variable"], keep="first")
        .set_index("Variable")
    )
    return direct, root


def resolve_assembler(var: str, direct: pd.DataFrame, root: pd.DataFrame) -> str:
    """Reproduce the assembler's lookup verbatim — including the '--' prefix bug."""
    if var in direct.index:
        return "direct"
    if len(var) > 2 and ("--" + var[2:]) in root.index:
        return "compositional"
    return "unresolved"


def classify(var: str, direct: pd.DataFrame, root: pd.DataFrame) -> dict:
    """Classify a variable code that the assembler failed to resolve.

    Returns a dict with fields:
        variable_code       input code
        domain_prefix       first two chars
        remainder           var[2:] (may be empty)
        direct_hit          bool — present in direct table
        root_hit_corrected  bool — remainder present in Root table under corrected key
        bucket              narrative-layer-bug | evs-root-gap | not-compositional
        suggested_root_ncit NCIt code of the root hit if bucket == narrative-layer-bug
        suggested_root_name natural name of the root hit if bucket == narrative-layer-bug
    """
    d_hit = var in direct.index
    prefix = var[:2]
    remainder = var[2:]

    # not-compositional first: if the domain prefix is a special case, the compositional
    # fallback is not the intended resolution path.
    if var in NON_COMPOSITIONAL_FULL or prefix in NON_COMPOSITIONAL_PREFIXES:
        return {
            "variable_code": var,
            "domain_prefix": prefix,
            "remainder": remainder,
            "direct_hit": d_hit,
            "root_hit_corrected": False,
            "bucket": "not-compositional",
            "suggested_root_ncit": "",
            "suggested_root_name": "",
        }

    if len(var) <= 2:
        # Two-char variables cannot be compositionally decomposed.
        return {
            "variable_code": var,
            "domain_prefix": prefix,
            "remainder": remainder,
            "direct_hit": d_hit,
            "root_hit_corrected": False,
            "bucket": "not-compositional",
            "suggested_root_ncit": "",
            "suggested_root_name": "",
        }

    if remainder in root.index:
        r_row = root.loc[remainder]
        return {
            "variable_code": var,
            "domain_prefix": prefix,
            "remainder": remainder,
            "direct_hit": d_hit,
            "root_hit_corrected": True,
            "bucket": "narrative-layer-bug",
            "suggested_root_ncit": str(r_row["NCIt_Code"]) if pd.notna(r_row["NCIt_Code"]) else "",
            "suggested_root_name": str(r_row["Natural_Name"]) if pd.notna(r_row["Natural_Name"]) else "",
        }

    return {
        "variable_code": var,
        "domain_prefix": prefix,
        "remainder": remainder,
        "direct_hit": d_hit,
        "root_hit_corrected": False,
        "bucket": "evs-root-gap",
        "suggested_root_ncit": "",
        "suggested_root_name": "",
    }


def run() -> None:
    variables, dss, ident = load_inputs()
    direct, root = build_resolver(ident)

    # Join variables to DSS for domain context
    var_full = variables.merge(
        dss[["ds_id", "domain"]], on="ds_id", how="left", validate="many_to_one"
    )
    var_full = var_full[var_full["variable_name"].notna()].copy()

    # Assembler-level resolution
    var_full["resolution"] = var_full["variable_name"].map(
        lambda v: resolve_assembler(v, direct, root)
    )

    # Post-fix resolution projection (what the assembler would return with the
    # one-line fix in var_nn). Used to predict the residual has_unresolved count.
    direct_set = set(direct.index)
    root_set = set(root.index)

    def resolve_corrected(var: str) -> str:
        if var in direct_set:
            return "direct"
        if len(var) > 2 and var[2:] in root_set:
            return "compositional-corrected"
        return "unresolved"

    var_full["resolution_post_fix"] = var_full["variable_name"].map(resolve_corrected)

    total_rows = len(var_full)
    by_res = var_full["resolution"].value_counts().to_dict()
    dss_with_unresolved = (
        var_full[var_full["resolution"] == "unresolved"]["ds_id"].nunique()
    )
    dss_with_unresolved_post_fix = (
        var_full[var_full["resolution_post_fix"] == "unresolved"]["ds_id"].nunique()
    )
    codes_unresolved_post_fix = (
        var_full[var_full["resolution_post_fix"] == "unresolved"]["variable_name"].nunique()
    )

    # Distinct unresolved codes with DSS count
    unresolved = (
        var_full[var_full["resolution"] == "unresolved"]
        .groupby("variable_name")
        .agg(
            dss_count=("ds_id", "nunique"),
            row_count=("ds_id", "size"),
            roles=("role", lambda s: ",".join(sorted(set(s.dropna().astype(str))))),
            domains=("domain", lambda s: ",".join(sorted(set(s.dropna().astype(str))))),
        )
        .reset_index()
        .rename(columns={"variable_name": "variable_code"})
    )

    # Classify every unresolved code
    classifications = unresolved["variable_code"].map(
        lambda v: classify(v, direct, root)
    )
    class_df = pd.DataFrame(list(classifications))
    out = unresolved.merge(class_df, on="variable_code", how="left")

    out = out[
        [
            "variable_code",
            "domain_prefix",
            "remainder",
            "direct_hit",
            "root_hit_corrected",
            "bucket",
            "suggested_root_ncit",
            "suggested_root_name",
            "dss_count",
            "row_count",
            "roles",
            "domains",
        ]
    ].sort_values(["bucket", "dss_count", "variable_code"], ascending=[True, False, True])

    REPORT_CSV.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(REPORT_CSV, index=False)

    # Bucket aggregates
    bucket_summary = (
        out.groupby("bucket")
        .agg(
            distinct_codes=("variable_code", "nunique"),
            total_dss=("dss_count", "sum"),
            total_rows=("row_count", "sum"),
        )
        .reset_index()
    )
    bucket_totals = {r["bucket"]: r for _, r in bucket_summary.iterrows()}

    # Domain aggregates within each bucket
    domain_within_bucket = (
        out.groupby(["bucket", "domain_prefix"])
        .agg(codes=("variable_code", "nunique"), dss=("dss_count", "sum"))
        .reset_index()
        .sort_values(["bucket", "dss"], ascending=[True, False])
    )

    # Worked-case traces
    worked = ["RSSTRESN", "MKTESTCD", "MKTEST", "MKORRES", "MKSTRESC", "ISBDAGNT"]
    worked_rows = []
    for w in worked:
        r_assembler = resolve_assembler(w, direct, root)
        c = classify(w, direct, root) if r_assembler == "unresolved" else {
            "bucket": f"resolved-{r_assembler}",
            "remainder": w[2:] if len(w) > 2 else "",
            "root_hit_corrected": False,
            "suggested_root_ncit": "",
            "suggested_root_name": "",
        }
        dss_hit = var_full[var_full["variable_name"] == w]["ds_id"].nunique()
        worked_rows.append(
            {
                "code": w,
                "assembler": r_assembler,
                "bucket": c["bucket"],
                "remainder": c.get("remainder", ""),
                "root_found": c.get("root_hit_corrected", False),
                "root_ncit": c.get("suggested_root_ncit", ""),
                "root_name": c.get("suggested_root_name", ""),
                "dss_count": dss_hit,
            }
        )
    worked_df = pd.DataFrame(worked_rows)

    # Markdown report
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    md = []
    md.append("# Root-subset fallback diagnostic\n")
    md.append(
        f"*Generated {now} from `cosmos-graph/scripts/root_subset_fallback_diagnostic.py`. "
        "Diagnostic pass scheduled in `docs/COSMoS_Graph_Upstream_Additions.md` §3.5.*\n"
    )

    md.append("## 1. Summary\n")
    md.append(
        f"- Variables rows scanned: **{total_rows:,}** (across {var_full['ds_id'].nunique():,} DSSs)."
    )
    md.append(
        f"- Assembler resolution: direct **{by_res.get('direct', 0):,}**, "
        f"compositional **{by_res.get('compositional', 0):,}**, "
        f"unresolved **{by_res.get('unresolved', 0):,}**."
    )
    md.append(
        f"- DSSs with at least one unresolved variable: **{dss_with_unresolved:,}**."
    )
    md.append(
        f"- Distinct unresolved variable codes: **{len(out):,}**."
    )
    md.append(
        f"- Post-fix projection: **{dss_with_unresolved_post_fix:,}** DSSs and "
        f"**{codes_unresolved_post_fix:,}** distinct codes would remain unresolved "
        "after the one-line `var_nn` fix (the residual EVS-gap set).\n"
    )

    md.append("## 2. Finding\n")
    md.append(
        "The assembler's compositional fallback "
        "(`sdtm-narrative/notebooks/40_assemble_narrative.ipynb` cell 4, "
        "`60_assemble_databooks.ipynb` cell 4) looks up `'--' + variable[2:]` "
        "in the Root subset of `SDTM_Variable_Identity.xlsx`. "
        "The Root subset stores entries **without** a `--` prefix "
        "(0 of 174 Root/Variable+Root rows carry `--`), so the compositional "
        "key never hits. The entire `'compositional'` resolution tier is "
        "structurally inactive today.\n"
    )
    md.append(
        "- **Direction.** Narrative-layer bug. Fix is one line in `var_nn` — "
        "replace `'--' + variable[2:]` with `variable[2:]`.\n"
    )
    md.append(
        "- **Implication for §2.2.** The 103-unresolved set is a superset of "
        "the true EVS gap. Most of it collapses into the bug fix. What remains "
        "after the fix is the genuine upstream concern.\n"
    )

    md.append("## 3. Classification of unresolved codes\n")
    md.append(
        "After applying the corrected compositional lookup (`variable[2:]` against the "
        "Root subset), each unresolved code falls into one of three buckets:\n"
    )
    md.append("| Bucket | Distinct codes | DSS span (sum) | Variable-row span (sum) |")
    md.append("|---|---:|---:|---:|")
    for b in ("narrative-layer-bug", "evs-root-gap", "not-compositional"):
        r = bucket_totals.get(b, {"distinct_codes": 0, "total_dss": 0, "total_rows": 0})
        md.append(
            f"| {b} | {int(r['distinct_codes'])} | {int(r['total_dss'])} | {int(r['total_rows'])} |"
        )
    md.append("")
    md.append(
        "*DSS span sums per-code DSS counts; a DSS carrying multiple unresolved codes is "
        "counted once per code. Not a distinct-DSS count.*\n"
    )

    md.append("## 4. Worked cases\n")
    md.append("| Code | Assembler | Bucket | Remainder | Root found | Root NCIt | Root name | DSS count |")
    md.append("|---|---|---|---|---|---|---|---:|")
    for _, r in worked_df.iterrows():
        md.append(
            f"| `{r['code']}` | {r['assembler']} | {r['bucket']} | `{r['remainder']}` | "
            f"{r['root_found']} | {r['root_ncit']} | {r['root_name']} | {r['dss_count']} |"
        )
    md.append("")

    md.append("## 5. Per-bucket detail\n")
    for b in ("narrative-layer-bug", "evs-root-gap", "not-compositional"):
        sub = out[out["bucket"] == b]
        md.append(f"### 5.{['narrative-layer-bug','evs-root-gap','not-compositional'].index(b)+1} `{b}` — {len(sub)} codes\n")
        if b == "narrative-layer-bug":
            md.append(
                "*These resolve under the corrected compositional lookup. "
                "Listed with the suggested root NCIt identity.*\n"
            )
        elif b == "evs-root-gap":
            md.append(
                "*The two-char-stripped remainder is genuinely absent from the Root "
                "subset. Candidates for a CDISC / NCI EVS content ask.*\n"
            )
        else:
            md.append(
                "*Trial-design / relationship / comments domains (SE, SV, TA, TE, TI, TS, TV, "
                "CO, RELREC) and two-char codes. Compositional fallback is not the intended "
                "resolution path.*\n"
            )
        if len(sub) == 0:
            md.append("_(empty)_\n")
            continue
        md.append("| Code | Prefix | Remainder | DSS count | Root NCIt | Root name | Domains |")
        md.append("|---|---|---|---:|---|---|---|")
        for _, r in sub.iterrows():
            md.append(
                f"| `{r['variable_code']}` | {r['domain_prefix']} | `{r['remainder']}` | "
                f"{int(r['dss_count'])} | {r['suggested_root_ncit']} | "
                f"{r['suggested_root_name']} | {r['domains']} |"
            )
        md.append("")

    md.append("## 6. Per-bucket domain distribution\n")
    md.append("| Bucket | Domain | Distinct codes | DSS span |")
    md.append("|---|---|---:|---:|")
    for _, r in domain_within_bucket.iterrows():
        md.append(
            f"| {r['bucket']} | {r['domain_prefix']} | {int(r['codes'])} | {int(r['dss'])} |"
        )
    md.append("")

    md.append("## 7. Conclusion\n")
    nb = int(bucket_totals.get("narrative-layer-bug", {"distinct_codes": 0})["distinct_codes"])
    eg = int(bucket_totals.get("evs-root-gap", {"distinct_codes": 0})["distinct_codes"])
    nc = int(bucket_totals.get("not-compositional", {"distinct_codes": 0})["distinct_codes"])
    md.append(
        f"- **{nb} of {nb+eg+nc} unresolved codes collapse into the narrative-layer bug fix.** "
        "§2.2 of `COSMoS_Graph_Upstream_Additions.md` over-reported the upstream concern."
    )
    md.append(
        f"- **{eg} codes are true EVS Root-subset gaps** — worth a CDISC / NCI EVS ask."
    )
    md.append(
        f"- **{nc} codes are not-compositional** — trial-design / comments / relationship / "
        "two-char variables. Not an upstream issue; their identity resolution goes through "
        "the direct tier or is out of scope."
    )
    md.append(
        "- **Recommendation.** Fix `var_nn` in `sdtm-narrative/notebooks/40_assemble_narrative.ipynb` "
        "cell 4 and `60_assemble_databooks.ipynb` cell 4 "
        "(`'--' + variable[2:]` → `variable[2:]`). Re-run the narrative assembler; "
        "`has_unresolved` count should drop to the evs-root-gap set only."
    )
    md.append(
        "- **Upstream additions document.** §2.2 and §3.5 should be updated to reflect that "
        "the bulk of the finding was a narrative-layer regression, with a residual EVS-gap "
        "list to carry forward."
    )
    md.append("")

    md.append("## 8. Caveats on the evs-root-gap bucket\n")
    md.append(
        "A handful of codes in §5.2 are not genuine Root-subset gaps — they are "
        "**direct-tier Variable_Identity gaps** that the plain two-char strip miscategorises:\n"
    )
    md.append(
        "- `ETHNIC` — prefix `ET`, domain `DM`. `ETHNIC` is a full DM variable, not a "
        "compositional form. Absent from the direct table. A direct-tier identity-build "
        "concern, not an EVS Root concern."
    )
    md.append(
        "- Any evs-root-gap row where the `domain_prefix` does not match the `domains` "
        "column is suspect in the same way. Filter the CSV with "
        "`domain_prefix != domains.split(',')[0]` to see these."
    )
    md.append(
        "\nThe diagnostic faithfully applies the approved plain two-char strip and lets "
        "these fall into evs-root-gap for visibility. A follow-up classification pass "
        "could split this bucket into `true-evs-root-gap` and `direct-tier-gap`. Out of "
        "scope for §3.5, but worth capturing for a future identity-build iteration.\n"
    )

    REPORT_MD.parent.mkdir(parents=True, exist_ok=True)
    REPORT_MD.write_text("\n".join(md))

    print(f"Wrote {REPORT_MD}")
    print(f"Wrote {REPORT_CSV}")
    print()
    print("Bucket summary:")
    print(bucket_summary.to_string(index=False))
    print()
    print("Worked cases:")
    print(worked_df.to_string(index=False))


if __name__ == "__main__":
    run()
