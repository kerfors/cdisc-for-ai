# Data flow

*Moved from the root README, 2026-09-30.*

Two views. The first shows how the reference files and consumer outputs are built. The second shows the analysis work, which reads from the same files but feeds nothing back.

### Reference files and consumer outputs

```mermaid
graph TD
    subgraph Sources
        EVS["NCI EVS SDTM CT"]
        COS["COSMoS exports"]
    end

    subgraph sdtm-test-codes
        TI["SDTM_Test_Identity.xlsx"]
        ITI["SDTM_Instrument_Test_Identity.xlsx"]
        II["SDTM_Instrument_Identity.xlsx"]
    end

    subgraph cosmos-graph
        CG["COSMoS_Graph.xlsx"]
        CGC["COSMoS_Graph_CT.xlsx"]
    end

    subgraph sdtm-domain-reference
        DM["SDTM_Domain_Metadata.xlsx"]
    end

    subgraph consumer-bases
        DV["DSS_View.xlsx"]
    end

    subgraph sdtm-findings-graph
        SF["Specimen_Findings.xlsx"]
        MF["Measurement_Findings.xlsx"]
        IF["Instrument_Findings.xlsx<br/>(four-sheet)"]
    end

    EVS --> TI
    EVS --> ITI
    EVS --> II
    EVS --> DM
    EVS --> CGC
    COS --> CG

    CG --> DV
    CGC --> DV
    TI --> DV

    DV --> SF
    DV --> MF
    DV --> IF
    DM --> SF
    DM --> MF
    DM --> IF
    II --> IF
    ITI --> IF
```

### Analysis

```mermaid
graph TD
    COS["COSMoS exports"]
    CGX["cosmos-graph<br/>COSMoS_Graph.xlsx, COSMoS_Graph_CT.xlsx"]
    STC["sdtm-test-codes<br/>Test and Instrument Identity, Codelist_Cross_References"]
    USDM["usdm-rdf<br/>usdm_v4.ttl"]

    subgraph cosmos-bc-dss
        BA["Behavioural_Analysis.md"]
        DPI["Domain_Pattern_Inventory.xlsx"]
    end

    subgraph link-semantics
        LKA["Link_Kind_Audit.xlsx"]
        CCC["Code_Collision_Check.xlsx"]
        LS["Link_Semantics.md"]
    end

    COS --> BA
    COS --> DPI

    CGX --> LKA
    STC --> LKA
    CGX --> CCC
    STC --> CCC
    USDM --> CCC

    LKA --> LS
    CCC --> LS
```

For how the analytical layers fit together, see [`SDTM_Domain_Overview.md`](../SDTM_Domain_Overview.md).
