# EU AI

A small project to understand where Europe sits in the AI industry stack.

## Inspiration

This started from Stubb's talk (click the thumbnail to watch, it opens at 13:14):

[![Stubb's talk](https://img.youtube.com/vi/TU9JRW27vrQ/hqdefault.jpg)](https://www.youtube.com/watch?v=TU9JRW27vrQ&t=794s)

## Approach

1. **Visualize the stack.** Map the AI industry as a dependency tree, like a civilization tech tree. It runs from raw materials (rare elements, metals) through chip machines, chips, data centres and frontier labs, up to applications and end users. The diagram is embedded below and lives in [`ai_stack_tech_tree.md`](ai_stack_tech_tree.md).
2. **Look at the EU companies that contribute to it.** With the stack laid out, place European companies on the layers they serve, and see where Europe is strong and where it depends on others. The diagram already highlights a few starting points, such as lithography, optics, lasers, chip IP and frontier labs. See [`eu_companies_by_layer.md`](eu_companies_by_layer.md) for the 451 companies found so far, with a confidence rating on each.

## The stack

Arrows read as "is required by". Green marks a strong European position, orange a current bottleneck, and dotted arrows regulatory influence.

```mermaid
flowchart TD
    %% ---------- L0: Raw materials ----------
    subgraph L0["L0 · Raw materials"]
        Quartz["High-purity quartz / silicon"]
        Minor["Gallium · Germanium · Tungsten · Cobalt"]
        Rare["Rare earths · Neon · Helium"]
        Cu["Copper · Aluminium · Steel"]
        Water["Ultra-pure water"]
        Fuel["Gas · Coal · Uranium · Sun · Wind"]
    end

    %% ---------- L1: Materials processing ----------
    subgraph L1["L1 · Materials processing"]
        Wafers["Silicon wafers"]
        Chem["Photoresists · Specialty chemicals · Gases"]
        Magnets["Magnets · Substrates · Interconnect metals"]
    end

    %% ---------- L2: Components & tools ----------
    subgraph L2["L2 · Machine subsystems"]
        Optics["Precision optics"]
        Laser["Lasers · EUV light source"]
        Parts["Vacuum · Stages · Sensors"]
    end

    subgraph L3["L3 · Chip machines & design tools"]
        Litho["Lithography: EUV / DUV"]
        Etch["Deposition · Etch · Metrology"]
        EDA["EDA software"]
        IP["Chip IP: Arm · Interface IP"]
    end

    %% ---------- L4: Chips ----------
    subgraph L4["L4 · Chip design & manufacturing"]
        Design["Chip designers: GPU / TPU / ASIC"]
        Fab["Foundries / Fabs"]
        HBM["HBM memory"]
        Pkg["Advanced packaging: CoWoS"]
    end

    %% ---------- L5: Systems ----------
    subgraph L5["L5 · Systems & infrastructure"]
        Servers["Servers · Racks"]
        Net["Networking · Optics"]
        Power["Power generation · Grid"]
        Cool["Cooling · Buildings"]
        DC["Data centres"]
        Cloud["Hyperscalers · Neoclouds"]
    end

    %% ---------- L6: Data & talent ----------
    subgraph L6["L6 · Data & talent"]
        Web["Web / licensed / synthetic data"]
        Labels["Human labelling · RLHF"]
        Talent["Research talent"]
        Reg["Regulation: EU AI Act"]
    end

    %% ---------- L7: Frontier ----------
    subgraph L7["L7 · Frontier labs"]
        Labs["Anthropic · OpenAI · Google DeepMind · Meta · Mistral · xAI"]
        Models["Foundation models"]
        Open["Open-weight models"]
    end

    %% ---------- L8: Delivery ----------
    subgraph L8["L8 · Delivery & applications"]
        Inference["Inference providers · APIs"]
        Tools["Dev tools · Agents · Frameworks"]
        Apps["AI-native apps"]
        Ent["Enterprise adoption"]
        Users["End users"]
    end

    %% ---------- Edges ----------
    Quartz --> Wafers
    Minor --> Chem
    Minor --> Fab
    Rare --> Magnets
    Rare --> Chem
    Cu --> Magnets
    Cu --> Servers
    Cu --> Power
    Water --> Fab
    Fuel --> Power

    Wafers --> Fab
    Chem --> Fab
    Magnets --> Parts
    Magnets --> Servers

    Optics --> Litho
    Laser --> Litho
    Parts --> Litho
    Parts --> Etch

    Litho --> Fab
    Etch --> Fab
    EDA --> Design
    IP --> Design

    Design --> Fab
    Fab --> Pkg
    HBM --> Pkg
    Fab --> HBM
    Pkg --> Servers
    Design --> Servers

    Servers --> DC
    Net --> DC
    Power --> DC
    Cool --> DC
    DC --> Cloud

    Cloud --> Labs
    Web --> Labs
    Labels --> Labs
    Talent --> Labs
    Reg -.constrains.-> Labs
    Reg -.constrains.-> Apps

    Labs --> Models
    Models --> Open
    Models --> Inference
    Open --> Inference
    Cloud --> Inference

    Inference --> Tools
    Tools --> Apps
    Models --> Apps
    Apps --> Ent
    Apps --> Users
    Ent --> Users

    %% ---------- Styling ----------
    classDef eu fill:#d4f4dd,stroke:#2e8b57,color:#111
    classDef bottleneck fill:#ffe0b2,stroke:#e65100,color:#111
    class Optics,Laser,IP,Labs,Reg eu
    class Litho,Pkg,HBM,Power,Fab bottleneck
```

## Files

| File | What it is |
|------|------------|
| `ai_stack_tech_tree.md` | Mermaid dependency tree of the AI stack, with EU strengths (green) and bottlenecks (orange) |
| `companies.json` | Source of truth: 451 European companies with layer, location, role, confidence and notes |
| `build.py` | Regenerates the three files below from `companies.json` (`python3 build.py`) |
| `eu_companies_by_layer.md` | The companies as one table per layer |
| `eu_companies.geojson` | Map of those companies at their headquarters. GitHub renders it as an interactive map |
| `eu_map.html` | Same map as a standalone page with clustering, a toggle per layer and a low-confidence filter. Open it locally, GitHub shows only the source |

## Viewing the diagram

The diagram renders inline on GitHub. In VS Code, use a Mermaid preview extension.

## Status

The stack diagram is a simplified first pass. The company list is not exhaustive, and most entries are not yet verified against live sources (see the confidence column).
