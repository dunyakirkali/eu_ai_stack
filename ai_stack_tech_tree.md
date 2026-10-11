# AI Industry Stack: Dependency Tree

Arrows read as "is required by" (dependency → dependent). Read top to bottom: the top is the foundation, the bottom is what people actually use.
Green nodes mark where Europe holds a meaningful position.

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

## Legend

- **Green**: strong European position (Zeiss optics, Trumpf lasers, ASML lithography, Arm-adjacent IP, Mistral (inside the Labs node), the EU AI Act as regulator).
- **Orange**: widely considered current bottlenecks (EUV lithography, advanced packaging, HBM, leading-edge fabs, grid power).
  Litho (ASML) is European but rendered orange, because it is the sharpest bottleneck.
- **Dotted arrows**: regulatory influence, not a physical dependency.

## How to read the tree

| Layer | Question it answers |
|-------|---------------------|
| L0 | What has to be dug up or extracted? |
| L1 | What must be refined before it is useful? |
| L2–L3 | What machines and tools make chips possible? |
| L4 | Who designs and builds the chips? |
| L5 | Where do the chips run, and what powers them? |
| L6 | What else do labs need besides compute? |
| L7 | Who trains the models? |
| L8 | How does it reach people? |

## Notes

- Simplified on purpose. Real dependencies are many-to-many (for example, every fab also needs EDA-driven design rules, and HBM makers need their own lithography).
- Company names are illustrative examples of each layer, not an exhaustive list.
