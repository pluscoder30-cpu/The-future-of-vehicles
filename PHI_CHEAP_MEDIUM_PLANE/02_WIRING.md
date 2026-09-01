# PHI_CHEAP_MEDIUM_PLANE — Wiring Diagrams

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    48V MAIN BUS                              │
│              ════════════════════                            │
│         ┌──────┴──────┐    ┌──────┴──────┐                  │
│         │  LEFT BUS   │    │  RIGHT BUS  │                  │
│         │  200A fuse  │    │  200A fuse  │                  │
│         └──────┬──────┘    └──────┬──────┘                  │
│                │                  │                          │
│    ┌───────────┼───────────┐  ┌───┼───────────┐             │
│    │           │           │  │   │           │             │
│  ┌─┴─┐     ┌──┴──┐     ┌─┴─┐┌┴─┐ ┌──┴──┐  ┌─┴─┐         │
│  │BAT│     │ESC-L│     │BAT││BAT│ │ESC-R│  │BAT│         │
│  │ 1 │     │     │     │ 2 ││ 3 │ │     │  │ 4 │         │
│  └───┘     └──┬──┘     └───┘└───┘ └──┬──┘  └───┘         │
│               │                      │                      │
│          ┌────┴────┐            ┌────┴────┐                │
│          │ MOTOR-L │            │ MOTOR-R │                │
│          │  30 kW  │            │  30 kW  │                │
│          └─────────┘            └─────────┘                │
│                                                            │
│    ┌───────────┼───────────┐  ┌───┼───────────┐             │
│    │           │           │  │   │           │             │
│  ┌─┴─┐     ┌──┴──┐     ┌─┴─┐┌┴─┐ ┌──┴──┐  ┌─┴─┐         │
│  │BAT│     │DCDC │     │BAT││BAT│ │DCDC │  │BAT│         │
│  │ 5 │     │48→12│     │ 6 ││ 7 │ │48→12│  │ 8 │         │
│  └───┘     └──┬──┘     └───┘└───┘ └──┬──┘  └───┘         │
│               │                      │                      │
│          ┌────┴────┐            ┌────┴────┐                │
│          │ 12V BUS │            │ 12V BUS │                │
│          │ LEFT    │            │ RIGHT   │                │
│          └────┬────┘            └────┬────┘                │
│               │                      │                      │
│          ┌────┴──────────────────────┴────┐                │
│          │         AVIONICS BUS           │                │
│          │      12V DC, 30A total         │                │
│          └────┬──────────┬──────────┬────┘                │
│               │          │          │                       │
│          ┌────┴───┐ ┌────┴───┐ ┌────┴───┐                │
│          │  GPS   │ │  VHF   │ │INSTRUM │                │
│          │  2A    │ │  5A    │ │  3A    │                │
│          └────────┘ └────────┘ └────────┘                │
└─────────────────────────────────────────────────────────────┘
```

---

## Detailed Wiring Specifications

### 1. MAIN 48V BUS

#### Left 48V Bus
```
BATTERY 1 (48V 20Ah) ──┬── [250A ANL Fuse] ──┬── LEFT MAIN BUS
BATTERY 2 (48V 20Ah) ──┘                     │
BATTERY 5 (48V 20Ah) ──┬── [250A ANL Fuse] ──┘
BATTERY 6 (48V 20Ah) ──┘
                        │
              ┌─────────┴─────────┐
              │  [200A Contactor]  │
              │  Master Relay #1   │
              └─────────┬─────────┘
                        │
              ┌─────────┴─────────┐
              │  [200A Fuse]       │
              └─────────┬─────────┘
                        │
              ┌─────────┴─────────┐
              │  TO ESC-L          │
              │  300A, 48V         │
              └───────────────────┘
```

#### Right 48V Bus
```
BATTERY 3 (48V 20Ah) ──┬── [250A ANL Fuse] ──┬── RIGHT MAIN BUS
BATTERY 4 (48V 20Ah) ──┘                     │
BATTERY 7 (48V 20Ah) ──┬── [250A ANL Fuse] ──┘
BATTERY 8 (48V 20Ah) ──┘
                        │
              ┌─────────┴─────────┐
              │  [200A Contactor]  │
              │  Master Relay #2   │
              └─────────┬─────────┘
                        │
              ┌─────────┴─────────┐
              │  [200A Fuse]       │
              └─────────┬─────────┘
                        │
              ┌─────────┴─────────┐
              │  TO ESC-R          │
              │  300A, 48V         │
              └───────────────────┘
```

### 2. BATTERY GROUP WIRING

#### Group A (Left Motor — Batteries 1, 2, 5, 6)
```
    B1(+) ─────┬─────────────────────────────────────┐
    B1(-) ──┐  │                                     │
            │  │                                     │
    B2(+) ──┤  │                                     │
    B2(-) ──┤  │                                     │
            │  │                                     │
    B5(+) ──┤  │                                     │
    B5(-) ──┤  │                                     │
            │  │                                     │
    B6(+) ──┤  │                                     │
    B6(-) ──┘  │                                     │
               │                                     │
         [PARALLEL BUS BAR]                    [PARALLEL BUS BAR]
               │                                     │
               └──────────┬──────────────────────────┘
                          │
                    [250A ANL FUSE]
                          │
                    [200A CONTACTOR]
                          │
                    ┌─────┴─────┐
                    │  TO ESC-L │
                    └───────────┘

    Total: 4S2P FPB-40 phi-harmonic field plasma = 48V 40Ah = 1920 Wh
```

#### Group B (Right Motor — Batteries 3, 4, 7, 8)
```
    B3(+) ─────┬─────────────────────────────────────┐
    B3(-) ──┐  │                                     │
            │  │                                     │
    B4(+) ──┤  │                                     │
    B4(-) ──┤  │                                     │
            │  │                                     │
    B7(+) ──┤  │                                     │
    B7(-) ──┤  │                                     │
            │  │                                     │
    B8(+) ──┤  │                                     │
    B8(-) ──┘  │                                     │
               │                                     │
         [PARALLEL BUS BAR]                    [PARALLEL BUS BAR]
               │                                     │
               └──────────┬──────────────────────────┘
                          │
                    [250A ANL FUSE]
                          │
                    [200A CONTACTOR]
                          │
                    ┌─────┴─────┐
                    │  TO ESC-R │
                    └───────────┘

    Total: 4S2P FPB-40 phi-harmonic field plasma = 48V 40Ah = 1920 Wh
```

### 3. MOTOR WIRING

#### Motor-Left (3-phase)
```
    ESC-L Output:
    ┌─────────────┐
    │  Phase A ───┼──── Motor Phase A (10 AWG, Red)
    │  Phase B ───┼──── Motor Phase B (10 AWG, White)
    │  Phase C ───┼──── Motor Phase C (10 AWG, Blue)
    │  Hall A  ───┼──── Motor Hall A (18 AWG, Green)
    │  Hall B  ───┼──── Motor Hall B (18 AWG, Yellow)
    │  Hall C  ───┼──── Motor Hall C (18 AWG, Orange)
    │  Temp    ───┼──── Motor Temp (18 AWG, Black/Red)
    │  GND     ───┼──── Motor Case Ground (10 AWG, Green/Yellow)
    └─────────────┘

    Wire length: 800mm max
    Shielding: Braided shield around Hall wires
    Routing: Left side of fuselage, secured every 150mm
```

#### Motor-Right (3-phase)
```
    ESC-R Output:
    ┌─────────────┐
    │  Phase A ───┼──── Motor Phase A (10 AWG, Red)
    │  Phase B ───┼──── Motor Phase B (10 AWG, White)
    │  Phase C ───┼──── Motor Phase C (10 AWG, Blue)
    │  Hall A  ───┼──── Motor Hall A (18 AWG, Green)
    │  Hall B  ───┼──── Motor Hall B (18 AWG, Yellow)
    │  Hall C  ───┼──── Motor Hall C (18 AWG, Orange)
    │  Temp    ───┼──── Motor Temp (18 AWG, Black/Red)
    │  GND     ───┼──── Motor Case Ground (10 AWG, Green/Yellow)
    └─────────────┘

    Wire length: 800mm max
    Shielding: Braided shield around Hall wires
    Routing: Right side of fuselage, secured every 150mm
```

### 4. 12V DISTRIBUTION

#### Left 12V Bus
```
    [48V→12V DC-DC #1]
         │
         ├──── [20A CB] ──── LEFT 12V BUS
         │                   │
         │    ┌──────────────┼──────────────┐
         │    │              │              │
         │  [10A CB]      [10A CB]       [5A CB]
         │    │              │              │
         │  ELT          VHF Radio      GPS
         │  (5A)         (5A)          (2A)
         │
         ├──── [10A CB] ──── LEFT LIGHTING
         │    │
         │  Landing light (7A)
         │
         └──── [5A CB] ──── LEFT INSTRUMENTS
              │
              Airspeed (0.5A)
              Altimeter (0.5A)
              VSI (0.5A)
              Compass (0.1A)
```

#### Right 12V Bus
```
    [48V→12V DC-DC #2]
         │
         ├──── [20A CB] ──── RIGHT 12V BUS
         │                   │
         │    ┌──────────────┼──────────────┐
         │    │              │              │
         │  [10A CB]      [10A CB]       [5A CB]
         │    │              │              │
         │  Turn Coord    Heading Ind    Battery
         │  (2A)         (2A)          Monitor (1A)
         │
         ├──── [5A CB] ──── RIGHT LIGHTING
         │    │
         │  Nav light (3A)
         │
         └──── [5A CB] ──── CHARGING PORT
              │
              Charge indicator (0.5A)
```

### 5. GROUND SYSTEM

```
    ┌─────────────────────────────────────────────────┐
    │                 GROUND BUS                       │
    │            ================                      │
    │                                                  │
    │  MOTOR-L GND ─────┐                              │
    │  MOTOR-R GND ─────┤                              │
    │  ESC-L GND   ─────┤                              │
    │  ESC-R GND   ─────┤                              │
    │  DCDC #1 GND ─────┤                              │
    │  DCDC #2 GND ─────┼──── MAIN GROUND BUS         │
    │  FRAME GND   ─────┤     (Copper strap,          │
    │  BAT(-) GND  ─────┤      2" wide)               │
    │  INSTRUMENTS ─────┤                              │
    │  LIGHTING    ─────┤                              │
    │  COMM        ─────┘                              │
    │                                                  │
    │  Connection: Bolted, star washer,              │
    │              zinc-plated copper lug              │
    └─────────────────────────────────────────────────┘

    Ground wire specs:
    - Main ground bus: 2" copper strap, 0.05" thick
    - Motor grounds: 10 AWG green/yellow
    - Instrument grounds: 18 AWG black
    - Frame ground: 10 AWG with star washer to bare metal
```

---

## Wire Sizing Summary

| Circuit | AWG | Current | Length | Voltage Drop | Color |
|---|---|---|---|---|---|
| 48V Battery to ESC | 10 | 200A | 1.5m | 0.48V (1.0%) | Red/Black |
| 48V Bus interconnect | 8 | 100A | 2.0m | 0.32V (0.7%) | Red/Black |
| 48V to DCDC | 12 | 15A | 1.0m | 0.06V (0.1%) | Red/Black |
| 12V Bus main | 12 | 20A | 1.5m | 0.12V (1.0%) | Red/Black |
| 12V to instruments | 18 | 2A | 1.0m | 0.01V (0.1%) | Red/Black |
| Motor phase wires | 10 | 150A | 0.8m | 0.24V (0.5%) | Red/White/Blue |
| Motor Hall wires | 18 | 0.5A | 0.8m | <0.01V | Green/Yellow/Orange |
| Ground bus | 10 | 200A | 0.5m | 0.12V | Green/Yellow |

---

## Connector Types

| Location | Connector | Rating | Source |
|---|---|---|---|
| Battery terminal | Anderson 175A | 175A continuous | Amazon |
| Battery parallel | Copper bus bar | 400A | AliExpress |
| ESC power input | XT150 | 150A continuous | Amazon |
| ESC motor output | Bullet 8mm | 200A | AliExpress |
| 12V distribution | Anderson 50A | 50A continuous | Amazon |
| Instrument panel | D-sub 25-pin | 5A per pin | Aircraft Spruce |
| Sensor connections | JST-XH | 3A per pin | Amazon |

---

## Wire Routing Rules

1. **Separation**: 48V and 12V wires separated by minimum 50mm
2. **Shielding**: All sensor wires shielded, shield grounded at one end only
3. **Securing**: Wire bundles secured every 150mm with Adel clamps
4. **Chafing**: Grommets at all metal hole pass-throughs
5. **Heat**: Wires routed away from motors (minimum 100mm)
6. **Service loops**: 50mm service loop at each connection point
7. **Labeling**: Every wire labeled at both ends with heat-shrink labels
8. **Color coding**: Red = positive, Black = negative, Green/Yellow = ground
9. **Bundling**: Maximum 12 wires per bundle
10. **Documentation**: Full wiring schematic posted in cockpit
