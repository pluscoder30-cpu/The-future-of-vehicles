# PHI MOLECULAR ASSEMBLER — MECHANICAL DIAGRAM
## Buildable Documentation | Physical Layout & Assembly

---

## EXPLODED VIEW (Top-Down)

```
                    PHI MOLECULAR ASSEMBLER
                   EXPLODED VIEW (TOP-DOWN)

                    ┌─────────────────────────────────────────┐
                    │              LID (Clear Plastic)         │
                    │         ┌─────────────────────┐         │
                    │         │    viewing window    │         │
                    │         │    (50mm diameter)   │         │
                    │         └─────────────────────┘         │
                    │              200mm x 150mm               │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │           TOP LAYER                      │
                    │    Copper Mesh Field Shaper              │
                    │    (137.5° golden angle pattern)        │
                    │    80mm x 80mm, 1mm wire gauge          │
                    │              1mm thick                   │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         ASSEMBLY CHAMBER                 │
                    │    ┌─────────────────────────────┐      │
                    │    │   Target Material Area       │      │
                    │    │   (metal powders, crystals)  │      │
                    │    │   60mm diameter x 20mm deep  │      │
                    │    └─────────────────────────────┘      │
                    │              20mm deep                   │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         CRYSTAL ARRAY LAYER              │
                    │    ┌─────────────────────────────┐      │
                    │    │  ┌───┐ ┌───┐ ┌───┐ ┌───┐  │      │
                    │    │  │C1 │ │C2 │ │C3 │ │C4 │  │      │
                    │    │  └───┘ └───┘ └───┘ └───┘  │      │
                    │    │  ┌───┐ ┌───┐ ┌───┐ ┌───┐  │      │
                    │    │  │C5 │ │C6 │ │C7 │ │C8 │  │      │
                    │    │  └───┘ └───┘ └───┘ └───┘  │      │
                    │    │  ┌───┐ ┌───┐               │      │
                    │    │  │C9 │ │C10│               │      │
                    │    │  └───┘ └───┘               │      │
                    │    │   BaTiO3 Discs (27mm dia)  │      │
                    │    └─────────────────────────────┘      │
                    │              10mm thick                   │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         ELECTRONICS LAYER                │
                    │    ┌─────────────────────────────┐      │
                    │    │  ┌───────────┐ ┌──────────┐ │      │
                    │    │  │ Arduino   │ │ PAM8403  │ │      │
                    │    │  │ Nano      │ │ Amp      │ │      │
                    │    │  └───────────┘ └──────────┘ │      │
                    │    │  ┌─────┐ ┌─────┐ ┌─────┐   │      │
                    │    │  │Pot  │ │Start│ │Stop │   │      │
                    │    │  │     │ │Btn  │ │Btn  │   │      │
                    │    │  └─────┘ └─────┘ └─────┘   │      │
                    │    │  ┌─────┐ ┌─────┐ ┌─────┐   │      │
                    │    │  │Grn  │ │Yel  │ │Red  │   │      │
                    │    │  │LED  │ │LED  │ │LED  │   │      │
                    │    │  └─────┘ └─────┘ └─────┘   │      │
                    │    └─────────────────────────────┘      │
                    │              15mm thick                   │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │         POWER LAYER                      │
                    │    ┌─────────────────────────────┐      │
                    │    │  ┌───────────┐ ┌──────────┐ │      │
                    │    │  │ 5V Buck   │ │ 12V Jack │ │      │
                    │    │  │ Converter │ │ (Input)  │ │      │
                    │    │  └───────────┘ └──────────┘ │      │
                    │    │  ┌─────────────────────────┐│      │
                    │    │  │  ACS712 Current Sensor  ││      │
                    │    │  └─────────────────────────┘│      │
                    │    └─────────────────────────────┘      │
                    │              10mm thick                   │
                    └───────────────────┬─────────────────────┘
                                        │
                    ┌───────────────────┴─────────────────────┐
                    │              BASE                        │
                    │         Plastic Container                │
                    │         (200mm x 150mm)                 │
                    │              5mm thick                   │
                    └─────────────────────────────────────────┘

    TOTAL HEIGHT: ~60mm
    TOTAL WIDTH: 200mm
    TOTAL DEPTH: 150mm
```

---

## SIDE CROSS-SECTION

```
    SIDE VIEW (Cross-Section)

    ◄──────────── 200mm (width) ────────────►

    ▲
    │   ┌─────────────────────────────────────────────┐
    │   │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│ Lid (clear plastic)
    │   │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│ viewing window
    │   ├─────────────────────────────────────────────┤
    │   │ ╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲│ Copper mesh (137.5°)
    │   ├─────────────────────────────────────────────┤
    │   │ ┌─────────────────────────────────────────┐ │ Assembly chamber
    │   │ │   Target Material (metal powders)       │ │ 20mm deep
    │   │ └─────────────────────────────────────────┘ │
    │   ├─────────────────────────────────────────────┤
    │   │ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐│ Crystal array
    │   │ │C1 │ │C2 │ │C3 │ │C4 │ │C5 │ │C6 │ │C7 ││ BaTiO3 discs
    │   │ └───┘ └───┘ └───┘ └───┘ └───┘ └───┘ └───┘│ (27mm dia each)
    │   ├─────────────────────────────────────────────┤
    │   │ ┌───────────┐ ┌──────────┐ ┌─────────────┐│ Electronics
    │   │ │ Arduino   │ │ PAM8403  │ │ Sensors     ││ Arduino + Amp
    │   │ │ Nano      │ │ Amp      │ │ + LEDs      ││ + UI elements
    │   │ └───────────┘ └──────────┘ └─────────────┘│
    │   ├─────────────────────────────────────────────┤
    │   │ ┌───────────┐ ┌──────────┐ ┌─────────────┐│ Power system
    │   │ │ 5V Buck   │ │ 12V Jack │ │ Current     ││ Buck converter
    │   │ │ Converter │ │ (Input)  │ │ Sensor      ││ + connectors
    │   │ └───────────┘ └──────────┘ └─────────────┘│
    │   ├─────────────────────────────────────────────┤
    │   │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│ Base (plastic)
    │   │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│ container
    │   └─────────────────────────────────────────────┘
    ▼
         TOTAL HEIGHT: ~60mm

    LEGEND:
    ░░░ = Plastic housing (lid/base)
    ╱╲  = Copper mesh field shaper
    ┌─┐ = Electronic components
    │C│ = BaTiO3 piezoelectric crystal
    └─┘
```

---

## CRYSTAL ARRAY LAYOUT (Detail)

```
    CRYSTAL ARRANGEMENT (Top View)

                    ┌─────────────────────────────────┐
                    │                                 │
                    │    ╔═════════════════════════╗   │
                    │    ║   ASSEMBLY CHAMBER      ║   │
                    │    ║   (60mm diameter)       ║   │
                    │    ╚═════════════════════════╝   │
                    │                                 │
                    │    ┌───┐ ┌───┐ ┌───┐ ┌───┐     │
                    │    │C1 │ │C2 │ │C3 │ │C4 │     │
                    │    └───┘ └───┘ └───┘ └───┘     │
                    │     │     │     │     │         │
                    │    ┌───┐ ┌───┐ ┌───┐ ┌───┐     │
                    │    │C5 │ │C6 │ │C7 │ │C8 │     │
                    │    └───┘ └───┘ └───┘ └───┘     │
                    │     │     │     │     │         │
                    │    ┌───┐ ┌───┐                   │
                    │    │C9 │ │C10│                   │
                    │    └───┘ └───┘                   │
                    │                                 │
                    └─────────────────────────────────┘

    CRYSTAL SPACING:
    - Center-to-center: 30mm
    - Edge-to-edge: 3mm
    - From chamber center: 25mm radial offset
    - Phi-harmonic spacing: 30mm × φ⁻¹ ≈ 18.5mm offset

    CRYSTAL PAIR WIRING:
    ┌─────────────────────────────────────────────────┐
    │                                                 │
    │   C1 (+) ────┐         ┌──── C2 (+)            │
    │              │         │                        │
    │   C1 (-) ────┴────┬────┴──── C2 (-)            │
    │                   │                             │
    │              Pair 1 (Parallel)                  │
    │                                                 │
    │   C3 (+) ────┐         ┌──── C4 (+)            │
    │              │         │                        │
    │   C3 (-) ────┴────┬────┴──── C4 (-)            │
    │                   │                             │
    │              Pair 2 (Parallel)                  │
    │                                                 │
    │   ... (Pairs 3-5 same pattern) ...              │
    │                                                 │
    │   All pairs connected in SERIES:                │
    │   Pair1(+) → Amp(+)                           │
    │   Pair1(-) → Pair2(+)                         │
    │   Pair2(-) → Pair3(+)                         │
    │   ...                                           │
    │   Pair5(-) → Amp(-) = GND                      │
    │                                                 │
    └─────────────────────────────────────────────────┘
```

---

## HOUSING LAYOUT

```
    HOUSING TOP VIEW (Lid Removed)

    ◄──────────── 200mm ────────────►

    ▲
    │   ┌─────────────────────────────────────────────┐
    │   │                                             │
    │   │   ┌─────────────────────────────────────┐   │
    │   │   │                                     │   │
    │   │   │         ASSEMBLY CHAMBER            │   │
    │   │   │         (60mm diameter)             │   │
    │   │   │         Target material goes here   │   │
    │   │   │                                     │   │
    │   │   └─────────────────────────────────────┘   │
    │   │                                             │
    │   │   ┌───────┐ ┌───────┐ ┌───────┐           │
    │   │   │ START │ │ STOP  │ │ SPEED │           │
    │   │   │  BTN  │ │  BTN  │ │  POT  │           │
    │   │   └───────┘ └───────┘ └───────┘           │
    │   │                                             │
    │   │   ┌─────┐ ┌─────┐ ┌─────┐                 │
    │   │   │ GRN │ │ YEL │ │ RED │                 │
    │   │   │ LED │ │ LED │ │ LED │                 │
    │   │   └─────┘ └─────┘ └─────┘                 │
    │   │                                             │
    │   │   ┌─────────────────────────────────────┐   │
    │   │   │     12V DC INPUT (Barrel Jack)      │   │
    │   │   └─────────────────────────────────────┘   │
    │   │                                             │
    │   └─────────────────────────────────────────────┘
    ▼
         150mm (depth)

    LAYOUT NOTES:
    - Assembly chamber centered in housing
    - Controls on front panel for easy access
    - Status LEDs visible from front
    - Power input on back panel
    - Copper mesh sits above chamber (removable)
    - Lid clips on with friction fit
```

---

## ASSEMBLY STACK ORDER

```
    ASSEMBLY SEQUENCE (Bottom to Top)

    STEP 1: Base
    ┌─────────────────────────────────────────┐
    │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│  Plastic container
    │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│  (200mm x 150mm)
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 2: Power Layer
    ┌─────────────────────────────────────────┐
    │ ┌───────────┐ ┌──────────┐ ┌──────────┐│
    │ │ 5V Buck   │ │ 12V Jack │ │ ACS712   ││  Power system
    │ │ Converter │ │ (Input)  │ │ Sensor   ││  (hot glue secure)
    │ └───────────┘ └──────────┘ └──────────┘│
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 3: Electronics Layer
    ┌─────────────────────────────────────────┐
    │ ┌───────────┐ ┌──────────┐             │
    │ │ Arduino   │ │ PAM8403  │             │  Control system
    │ │ Nano      │ │ Amp      │             │  (header soldered)
    │ └───────────┘ └──────────┘             │
    │ ┌─────┐ ┌─────┐ ┌─────┐               │
    │ │Pot  │ │Start│ │Stop │               │  UI elements
    │ │     │ │Btn  │ │Btn  │               │  (panel mounted)
    │ └─────┘ └─────┘ └─────┘               │
    │ ┌─────┐ ┌─────┐ ┌─────┐               │
    │ │Grn  │ │Yel  │ │Red  │               │  Status LEDs
    │ │LED  │ │LED  │ │LED  │               │  (panel mounted)
    │ └─────┘ └─────┘ └─────┘               │
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 4: Crystal Array
    ┌─────────────────────────────────────────┐
    │ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐   │
    │ │C1 │ │C2 │ │C3 │ │C4 │ │C5 │ │C6 │   │  10x BaTiO3
    │ └───┘ └───┘ └───┘ └───┘ └───┘ └───┘   │  piezoelectric discs
    │ ┌───┐ ┌───┐ ┌───┐ ┌───┐               │  (27mm diameter)
    │ │C7 │ │C8 │ │C9 │ │C10│               │
    │ └───┘ └───┘ └───┘ └───┘               │
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 5: Assembly Chamber
    ┌─────────────────────────────────────────┐
    │ ┌─────────────────────────────────────┐ │
    │ │   Target Material Area               │ │  Chamber walls
    │ │   (60mm diameter, 20mm deep)         │ │  (3D printed ring)
    │ │   Fill with: metal powders,          │ │
    │ │   crystal seeds, wire fragments      │ │
    │ └─────────────────────────────────────┘ │
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 6: Copper Mesh
    ┌─────────────────────────────────────────┐
    │ ╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲│  Copper mesh
    │ ╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱│  (137.5° angle)
    └─────────────────────────────────────────┘
              │
              ▼
    STEP 7: Lid
    ┌─────────────────────────────────────────┐
    │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│  Clear plastic lid
    │░░░░░░░░░░░░ viewing window ░░░░░░░░░░░░│  (50mm diameter)
    │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│  Friction fit
    └─────────────────────────────────────────┘
```

---

## COPPER MESH GEOMETRY

```
    MESH CUTTING TEMPLATE

    Starting with 80mm x 80mm copper mesh:

    Step 1: Mark golden angle (137.5°)
    ┌─────────────────────────────────────────┐
    │                                         │
    │            137.5°                       │
    │           ╱                             │
    │          ╱                              │
    │         ╱                               │
    │        ╱                                │
    │       ╱                                 │
    │      ╱                                  │
    │     ╱                                   │
    │    ╱                                    │
    │   ╱                                     │
    │  ╱                                      │
    │ ╱                                       │
    │╱                                        │
    └─────────────────────────────────────────┘

    Step 2: Cut at 137.5° angle
    Result: Rhombus-shaped mesh piece

    Step 3: Layer 2 pieces at 137.5° rotation
    ┌─────────────────────────────────────────┐
    │                                         │
    │   Piece 1: ─────╲                      │
    │                   ╲─────                │
    │                                         │
    │   Piece 2: ─────╱                      │
    │                   ╱─────                │
    │                                         │
    │   Combined: ╳ (X-pattern)              │
    │                                         │
    └─────────────────────────────────────────┘

    Step 4: Secure layers with copper wire ties
    - 4 tie points at corners
    - Do NOT use solder (impedes field)
```

---

## DIMENSIONS SUMMARY

| Dimension | Value | Notes |
|-----------|-------|-------|
| Housing Width | 200mm | Plastic container |
| Housing Depth | 150mm | Plastic container |
| Housing Height | 60mm | All layers stacked |
| Assembly Chamber | 60mm dia | 20mm deep |
| Crystal Discs | 27mm dia | 0.5mm thick BaTiO3 |
| Copper Mesh | 80mm x 80mm | 1mm wire gauge |
| Viewing Window | 50mm dia | Clear lid cutout |
| Weight | 1.8 kg | Total assembly |
| Power Input | 12V DC | Barrel jack |

---

## MATERIALS SPECIFICATION

| Component | Material | Grade | Notes |
|-----------|----------|-------|-------|
| Housing | PLA/Resin | - | 3D printed |
| Lid | Clear Acrylic | - | Laser cut |
| Crystal Discs | BaTiO3 | - | PZT equivalent |
| Copper Mesh | Copper Wire | - | 1mm gauge |
| Chamber Ring | PLA/Resin | - | 3D printed |
| Base Plate | Aluminum | - | Heat spreader |

---

## TOOLS REQUIRED (Mechanical)

| Tool | Purpose | Notes |
|------|---------|-------|
| 3D Printer | Housing, chamber ring | PLA or Resin |
| Scissors | Cut copper mesh | Sharp, fine tip |
| Ruler + Protractor | Measure 137.5° angle | Accurate marking |
| Hot Glue Gun | Secure components | Low-temp preferred |
| Sandpaper (400 grit) | Smooth 3D prints | Post-processing |
| File Set | Deburr holes | For panel mounting |

---

**Document**: 03_MECHANICAL.md
**Vehicle**: PHI MOLECULAR ASSEMBLER
**Status**: BUILDABLE ✓
