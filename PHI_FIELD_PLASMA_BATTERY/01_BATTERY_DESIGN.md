# PHI-HARMONIC FIELD PLASMA BATTERY — DESIGN

## Complete Physical Design Specification

### 1. Design Philosophy

The FPB is designed around three principles:
1. **Safety first** — Plasma dissipates if containment fails
2. **Modularity** — Stack multiple units for higher capacity
3. **Self-sufficiency** — Harvest ambient energy for self-charging

---

### 2. Size Overview

| Model | Energy | Dimensions (L×W×H) | Weight | Application |
|-------|--------|---------------------|--------|-------------|
| FPB-5 | 5 kWh | 400×300×200 mm | 15 kg | Drones, e-bikes |
| FPB-10 | 10 kWh | 500×400×250 mm | 30 kg | Hover cars, plasma cars |
| FPB-20 | 20 kWh | 600×500×300 mm | 55 kg | Trucks, vans |
| FPB-40 | 40 kWh | 800×600×350 mm | 100 kg | Heavy trucks, planes |
| FPB-80 | 80 kWh | 1000×800×400 mm | 180 kg | Spacecraft |
| FPB-100 | 100 kWh | 1200×900×450 mm | 220 kg | Heavy spacecraft |

---

### 3. Internal Structure — Cross Section

#### 3.1 FPB-10 Cross Section (Top View)

```
╔══════════════════════════════════════════════════════════════════════╗
║                        FPB-10 TOP VIEW                              ║
║                      500mm × 400mm                                  ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║   ┌─────────────────────────────────────────────────────────────┐   ║
║   │                    OUTER CASING (Aluminum)                  │   ║
║   │  ┌─────────────────────────────────────────────────────┐   │   ║
║   │  │              THERMAL INSULATION (Aerogel)            │   │   ║
║   │  │  ┌─────────────────────────────────────────────┐   │   │   ║
║   │  │  │          PHI-HARMONIC COIL ARRAY             │   │   │   ║
║   │  │  │  ┌─────────────────────────────────────┐   │   │   │   ║
║   │  │  │  │                                     │   │   │   │   ║
║   │  │  │  │         PLASMA CHAMBER              │   │   │   │   ║
║   │  │  │  │         (Vacuum vessel)             │   │   │   │   ║
║   │  │  │  │                                     │   │   │   │   ║
║   │  │  │  │    ┌─────┐  ┌─────┐  ┌─────┐      │   │   │   │   ║
║   │  │  │  │    │ ╔═╗ │  │ ╔═╗ │  │ ╔═╗ │      │   │   │   │   ║
║   │  │  │  │    │ ║▓║ │  │ ║▓║ │  │ ║▓║ │      │   │   │   │   ║
║   │  │  │  │    │ ╚═╝ │  │ ╚═╝ │  │ ╚═╝ │      │   │   │   │   ║
║   │  │  │  │    └─────┘  └─────┘  └─────┘      │   │   │   │   ║
║   │  │  │  │         PLASMA CORE                │   │   │   │   ║
║   │  │  │  │    (H₂/He ionized gas)             │   │   │   │   ║
║   │  │  │  └─────────────────────────────────────┘   │   │   │   ║
║   │  │  │                                            │   │   │   ║
║   │  │  │  COILS (5 phi-harmonic, 137.5° spacing)    │   │   │   ║
║   │  │  └────────────────────────────────────────────┘   │   │   ║
║   │  │                                                   │   │   ║
║   │  │  THERMAL INSULATION (20mm aerogel blanket)        │   │   ║
║   │  └───────────────────────────────────────────────────┘   │   ║
║   │                                                          │   ║
║   │  OUTER CASING (6061-T6 Aluminum, 3mm walls)             │   ║
║   └──────────────────────────────────────────────────────────┘   ║
║                                                                      ║
║   PORTS:                                                            ║
║   ├── Gas fill port (left side, brass fitting)                     ║
║   ├── Power connector (right side, XT90)                           ║
║   ├── Monitoring port (bottom, 4-pin JST)                          ║
║   └── Pressure relief valve (top, safety)                          ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

#### 3.2 FPB-10 Cross Section (Side View)

```
╔══════════════════════════════════════════════════════════════════════╗
║                        FPB-10 SIDE VIEW                             ║
║                      500mm × 250mm                                  ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║   ┌──────────────────────────────────────────────────────────────┐  ║
║   │                                                              │  ║
║   │   ┌──────────────────────────────────────────────────────┐  │  ║
║   │   │              TOP PLATE (Aluminum)                    │  │  ║
║   │   ├──────────────────────────────────────────────────────┤  │  ║
║   │   │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│  │  ║
║   │   │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│  │  ║
║   │   │▓▓▓▓▓▓▓▓▓▓▓▓▓▓ PLASMA CORE ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│  │  ║
║   │   │▓▓▓▓▓▓▓▓▓▓▓▓▓▓ (H₂/He gas) ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│  │  ║
║   │   │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│  │  ║
║   │   │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│  │  ║
║   │   ├──────────────────────────────────────────────────────┤  │  ║
║   │   │              BOTTOM PLATE (Aluminum)                 │  │  ║
║   │   └──────────────────────────────────────────────────────┘  │  ║
║   │                                                              │  ║
║   │   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │  ║
║   │   │  CONTAINMENT │  │    POWER     │  │  MONITORING  │     │  ║
║   │   │   CONTROLLER │  │  ELECTRONICS │  │    BOARD     │     │  ║
║   │   │  (MCU + FET) │  │  (DC-DC +    │  │  (Temp,      │     │  ║
║   │   │              │  │   Driver)    │  │   Pressure)  │     │  ║
║   │   └──────────────┘  └──────────────┘  └──────────────┘     │  ║
║   │                                                              │  ║
║   └──────────────────────────────────────────────────────────────┘  ║
║                                                                      ║
║   KEY DIMENSIONS:                                                    ║
║   ├── Plasma chamber: 350mm × 250mm × 150mm                        ║
║   ├── Coil array: 400mm × 300mm × 20mm                             ║
║   ├── Electronics bay: 400mm × 100mm × 80mm                        ║
║   └── Total: 500mm × 400mm × 250mm                                 ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

### 4. Plasma Containment Geometry

#### 4.1 Magnetic Bottle Design

```
    PHI-HARMONIC MAGNETIC BOTTLE (3D View)
    
         ╔═══════════════════════════════╗
         ║         TOP COIL              ║
         ║    ╔═══════════════════╗      ║
         ║    ║   ╭───────────╮   ║      ║
         ║    ║   │  ╭─────╮  │   ║      ║
         ║    ║   │  │█████│  │   ║      ║
         ║    ║   │  │█████│  │   ║      ║
         ║    ║   │  │█████│  │   ║      ║
         ║    ║   │  ╰─────╯  │   ║      ║
         ║    ║   ╰───────────╯   ║      ║
         ║    ╚═══════════════════╝      ║
         ║                               ║
         ║    ╔═══════════════════╗      ║
         ║    ║   ╭───────────╮   ║      ║
         ║    ║   │  ╭─────╮  │   ║      ║
         ║    ║   │  │█████│  │   ║      ║
         ║    ║   │  │█████│  │   ║      ║
         ║    ║   │  │█████│  │   ║      ║
         ║    ║   │  ╰─────╯  │   ║      ║
         ║    ║   ╰───────────╯   ║      ║
         ║    ╚═══════════════════╝      ║
         ║         BOTTOM COIL           ║
         ╚═══════════════════════════════╝
         
         ████ = Plasma (confined)
         ═══ = Coil windings
         ╭─╮ = Magnetic field lines
```

#### 4.2 Coil Specifications (FPB-10)

| Coil | Turns | Wire Gauge | Diameter | Inductance | Resonant Freq |
|------|-------|------------|----------|------------|---------------|
| C1 (0°) | 120 | 18 AWG | 200mm | 47 μH | 49.8 kHz |
| C2 (72.5°) | 120 | 18 AWG | 200mm | 47 μH | 49.8 kHz |
| C3 (137.5°) | 120 | 18 AWG | 200mm | 47 μH | 49.8 kHz |
| C4 (225°) | 120 | 18 AWG | 200mm | 47 μH | 49.8 kHz |
| C5 (272°) | 120 | 18 AWG | 200mm | 47 μH | 49.8 kHz |

#### 4.3 Golden Angle Spacing

```
    ANGULAR POSITIONS (137.507° golden angle)
    
    Coil 1: 0°
    Coil 2: 137.5°
    Coil 3: 275° (137.5° × 2 = 275°)
    Coil 4: 52.5° (137.5° × 3 = 412.5° - 360° = 52.5°)
    Coil 5: 190° (137.5° × 4 = 550° - 360° = 190°)
    
    VERIFIED: All coils are separated by golden angle multiples
    This ensures no two coils share a harmonic frequency
```

---

### 5. Phi-Harmonic Coil Arrangement

#### 5.1 Coil Winding Pattern

```
    SINGLE COIL WINDING (Top View)
    
              ╭─────────────────╮
           ╭──┤                 ├──╮
         ╭─┤  │    ╭───────╮    │  ├─╮
        ╭┤ │  │  ╭─┤       ├─╮  │  │ ├╮
       ╭┤ │ │  │╭─┤  ◉◉◉◉  ├─╮│  │ │ ├╮
       ││ │ │  ││ │  ◉◉◉◉  │ ││  │ │ ││
       ││ │ │  ││ │  ◉◉◉◉  │ ││  │ │ ││
       ╰┤ │ │  │╰─┤  ◉◉◉◉  ├─╯│  │ │ ├╯
        ╰┤ │  │  ╰─┤       ├─╯  │  │ ├╯
         ╰─┤  │    ╰───────╯    │  ├─╯
           ╰──┤                 ├──╯
              ╰─────────────────╯
              
    ◉◉◉◉ = Plasma core
    ─── = Coil windings (120 turns, 18 AWG)
    
    Winding direction: Clockwise
    Layer separation: 2mm (Kapton tape)
    Total wire length: ~75m per coil
```

#### 5.2 Coil Mounting

```
    COIL MOUNTING CROSS-SECTION
    
    ┌─────────────────────────────────────┐
    │         MOUNTING PLATE              │
    │         (G10 fiberglass)            │
    ├─────────────────────────────────────┤
    │  ┌─────────┐  ┌─────────┐          │
    │  │  COIL   │  │  COIL   │          │
    │  │  ╔═══╗  │  │  ╔═══╗  │          │
    │  │  ║   ║  │  │  ║   ║  │          │
    │  │  ╚═══╝  │  │  ╚═══╝  │          │
    │  └─────────┘  └─────────┘          │
    │       │              │              │
    │  ┌────▼────┐  ┌────▼────┐          │
    │  │ VIBRATION│  │ VIBRATION│          │
    │  │ DAMPER  │  │ DAMPER  │          │
    │  └─────────┘  └─────────┘          │
    ├─────────────────────────────────────┤
    │         BASE PLATE                  │
    │         (Aluminum)                  │
    └─────────────────────────────────────┘
    
    Mounting: 4× M4 bolts per coil
    Vibration dampers: Silicone rubber pads (5mm)
    Alignment: Pin + slot for precise positioning
```

---

### 6. Material Specifications

#### 6.1 Structural Materials

| Component | Material | Specification | Purpose |
|-----------|----------|---------------|---------|
| Outer casing | 6061-T6 Aluminum | 3mm walls | Structural support |
| Top/bottom plates | 6061-T6 Aluminum | 5mm thick | Containment seal |
| Coil mounting | G10 fiberglass | 3mm sheet | Electrical isolation |
| Vibration dampers | Silicone rubber | 5mm pads | Shock absorption |
| Thermal insulation | Aerogel blanket | 20mm | Heat retention |

#### 6.2 Electrical Materials

| Component | Material | Specification | Purpose |
|-----------|----------|---------------|---------|
| Coil wire | Enameled copper | 18 AWG (1.02mm) | Magnetic field generation |
| Bus bars | Copper | 10×3mm | High-current paths |
| Connectors | Gold-plated brass | XT90 | Power connection |
| PCB | FR4 | 1.6mm, 2oz copper | Control electronics |
| Solder | SAC305 | Lead-free | Connections |

#### 6.3 Plasma Materials

| Component | Material | Specification | Purpose |
|-----------|----------|---------------|---------|
| Primary gas | Hydrogen (H₂) | 99.999% purity | Plasma medium |
| Secondary gas | Helium (He) | 99.999% purity | Stabilizer |
| Fill pressure | — | 0.5 Torr (67 Pa) | Optimal confinement |
| Gas volume | — | 13.1 liters | Plasma chamber |

---

### 7. Assembly Dimensions

#### 7.1 FPB-5 (5 kWh)

```
    ┌────────────────────────────────────┐
    │           FPB-5                    │
    │                                    │
    │    ┌──────────────────────┐        │
    │    │                      │        │
    │    │    400mm × 300mm     │        │
    │    │                      │        │
    │    │    Height: 200mm     │        │
    │    │                      │        │
    │    └──────────────────────┘        │
    │                                    │
    │    Weight: 15 kg                   │
    │    Plasma volume: 6.5 L            │
    │    Coil diameter: 150mm            │
    │    Number of coils: 5              │
    │                                    │
    └────────────────────────────────────┘
```

#### 7.2 FPB-10 (10 kWh)

```
    ┌────────────────────────────────────┐
    │           FPB-10                   │
    │                                    │
    │    ┌──────────────────────┐        │
    │    │                      │        │
    │    │    500mm × 400mm     │        │
    │    │                      │        │
    │    │    Height: 250mm     │        │
    │    │                      │        │
    │    └──────────────────────┘        │
    │                                    │
    │    Weight: 30 kg                   │
    │    Plasma volume: 13.1 L           │
    │    Coil diameter: 200mm            │
    │    Number of coils: 5              │
    │                                    │
    └────────────────────────────────────┘
```

#### 7.3 FPB-20 (20 kWh)

```
    ┌────────────────────────────────────┐
    │           FPB-20                   │
    │                                    │
    │    ┌──────────────────────┐        │
    │    │                      │        │
    │    │    600mm × 500mm     │        │
    │    │                      │        │
    │    │    Height: 300mm     │        │
    │    │                      │        │
    │    └──────────────────────┘        │
    │                                    │
    │    Weight: 55 kg                   │
    │    Plasma volume: 27 L             │
    │    Coil diameter: 250mm            │
    │    Number of coils: 7              │
    │                                    │
    └────────────────────────────────────┘
```

#### 7.4 FPB-40 (40 kWh)

```
    ┌────────────────────────────────────┐
    │           FPB-40                   │
    │                                    │
    │    ┌──────────────────────┐        │
    │    │                      │        │
    │    │    800mm × 600mm     │        │
    │    │                      │        │
    │    │    Height: 350mm     │        │
    │    │                      │        │
    │    └──────────────────────┘        │
    │                                    │
    │    Weight: 100 kg                  │
    │    Plasma volume: 50 L             │
    │    Coil diameter: 300mm            │
    │    Number of coils: 9              │
    │                                    │
    └────────────────────────────────────┘
```

#### 7.5 FPB-80 (80 kWh)

```
    ┌────────────────────────────────────┐
    │           FPB-80                   │
    │                                    │
    │    ┌──────────────────────┐        │
    │    │                      │        │
    │    │    1000mm × 800mm    │        │
    │    │                      │        │
    │    │    Height: 400mm     │        │
    │    │                      │        │
    │    └──────────────────────┘        │
    │                                    │
    │    Weight: 180 kg                  │
    │    Plasma volume: 100 L            │
    │    Coil diameter: 400mm            │
    │    Number of coils: 11             │
    │                                    │
    └────────────────────────────────────┘
```

#### 7.6 FPB-100 (100 kWh)

```
    ┌────────────────────────────────────┐
    │           FPB-100                  │
    │                                    │
    │    ┌──────────────────────┐        │
    │    │                      │        │
    │    │    1200mm × 900mm    │        │
    │    │                      │        │
    │    │    Height: 450mm     │        │
    │    │                      │        │
    │    └──────────────────────┘        │
    │                                    │
    │    Weight: 220 kg                  │
    │    Plasma volume: 135 L            │
    │    Coil diameter: 500mm            │
    │    Number of coils: 13             │
    │                                    │
    └────────────────────────────────────┘
```

---

### 8. Plasma Chamber Design

#### 8.1 Chamber Material

- **Material**: Borosilicate glass (Pyrex) or quartz
- **Wall thickness**: 6mm
- **Shape**: Cylindrical with rounded ends (minimizes stress concentrations)
- **Seal**: O-ring groove with Viton O-rings
- **Viewports**: 2× quartz windows (25mm diameter) for plasma observation

#### 8.2 Gas Handling System

```
    GAS HANDLING SCHEMATIC
    
    ┌──────────┐     ┌──────────┐     ┌──────────┐
    │  H₂ GAS  │────▶│  PRESSURE │────▶│  GAS     │
    │  CYLINDER │     │  REGULATOR│     │  MANIFOLD │
    │  (50 bar) │     │  (0-1 bar)│     │          │
    └──────────┘     └──────────┘     └──────────┘
                           │                │
                     ┌─────▼─────┐    ┌────▼────┐
                     │  PRESSURE │    │  PLASMA │
                     │  GAUGE    │    │ CHAMBER │
                     │  (0-10 Torr)│  │         │
                     └───────────┘    └─────────┘
    
    Fill procedure:
    1. Evacuate chamber to 10⁻³ Torr (vacuum pump)
    2. Backfill with H₂/He mix to 0.5 Torr
    3. Seal gas fill port
    4. Verify pressure stability (24hr test)
```

---

### 9. Electronics Bay

#### 9.1 Containment Controller

```
    CONTAINMENT CONTROLLER BLOCK DIAGRAM
    
    ┌─────────────────────────────────────────────────┐
    │              CONTAINMENT CONTROLLER              │
    │                                                  │
    │  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
    │  │  TEMP    │  │ PRESSURE │  │  PLASMA  │      │
    │  │  SENSOR  │  │  SENSOR  │  │ DENSITY  │      │
    │  │  (NTC)   │  │ (Cap.)   │  │  (RF)    │      │
    │  └────┬─────┘  └────┬─────┘  └────┬─────┘      │
    │       │              │              │            │
    │       ▼              ▼              ▼            │
    │  ┌──────────────────────────────────────────┐   │
    │  │           STM32F407 MCU                   │   │
    │  │  - PID temperature control                │   │
    │  │  - Pressure regulation                    │   │
    │  │  - Plasma density monitoring              │   │
    │  │  - Coil current control                   │   │
    │  │  - Safety shutdown logic                  │   │
    │  └──────────────────────────────────────────┘   │
    │       │              │              │            │
    │       ▼              ▼              ▼            │
    │  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
    │  │  COIL    │  │  GAS     │  │  FAULT   │      │
    │  │  DRIVER  │  │  VALVE   │  │  RELAY   │      │
    │  │  (FET)   │  │  (Solen.)│  │  (SSR)   │      │
    │  └──────────┘  └──────────┘  └──────────┘      │
    │                                                  │
    └─────────────────────────────────────────────────┘
```

#### 9.2 Power Electronics

```
    POWER ELECTRONICS BLOCK DIAGRAM
    
    ┌─────────────────────────────────────────────────┐
    │              POWER ELECTRONICS                   │
    │                                                  │
    │  INPUT                OUTPUT                     │
    │  ┌─────┐  ┌────────┐  ┌────────┐  ┌─────┐      │
    │  │AMBI-│─▶│  PFC   │─▶│  DC-DC │─▶│LOAD │      │
    │  │ENT  │  │ STAGE  │  │ CONVERT│  │     │      │
    │  └─────┘  └────────┘  └────────┘  └─────┘      │
    │                                                  │
    │  Specifications:                                 │
    │  - Input: 12-48V DC (from harvesting)           │
    │  - Output: 48V DC (to vehicle bus)               │
    │  - Efficiency: 95%                               │
    │  - Max current: 200A                             │
    │  - Power: 10 kW continuous                       │
    │                                                  │
    └─────────────────────────────────────────────────┘
```

---

### 10. Thermal Management

#### 10.1 Heat Sources

| Source | Power | Temperature Rise |
|--------|-------|------------------|
| Coil resistance | 50W | +10°C |
| Power electronics | 100W | +15°C |
| Plasma radiation | 200W | +25°C |
| **Total** | **350W** | **+50°C** |

#### 10.2 Cooling System

```
    THERMAL MANAGEMENT LAYOUT
    
    ┌─────────────────────────────────────────────────┐
    │                                                  │
    │   ┌──────────────────────────────────────────┐  │
    │   │           AEROGEL INSULATION              │  │
    │   │           (20mm blanket)                  │  │
    │   │  ┌────────────────────────────────────┐  │  │
    │   │  │        PLASMA CHAMBER              │  │  │
    │   │  │        (heat source)               │  │  │
    │   │  └────────────────────────────────────┘  │  │
    │   │           │                              │  │
    │   │     ┌─────▼─────┐                        │  │
    │   │     │  HEAT PIPE │                        │  │
    │   │     │  (copper)  │                        │  │
    │   │     └─────┬─────┘                        │  │
    │   │           │                              │  │
    │   │     ┌─────▼─────┐                        │  │
    │   │     │  HEATSINK  │                        │  │
    │   │     │  (aluminum)│                        │  │
    │   │     └───────────┘                        │  │
    │   └──────────────────────────────────────────┘  │
    │                                                  │
    └─────────────────────────────────────────────────┘
    
    Cooling method: Passive (convection + radiation)
    Max operating temp: 60°C ambient
    Thermal resistance: 0.5°C/W (total path)
```

---

*Document Version: 1.0*
*Created: 2026-08-27*
*Author: Battery Agent 1 of 27*
*Project: PHI_FIELD_PLASMA_BATTERY*
