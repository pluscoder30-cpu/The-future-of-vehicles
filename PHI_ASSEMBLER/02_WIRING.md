# PHI MOLECULAR ASSEMBLER — WIRING DIAGRAM
## Buildable Documentation | Electrical Connections

---

## SYSTEM OVERVIEW

```
                    ┌─────────────────────────────────────────┐
                    │       PHI MOLECULAR ASSEMBLER           │
                    │                                         │
                    │  ┌─────────────────────────────────┐   │
                    │  │       ARDUINO NANO               │   │
                    │  │  ┌───────────────────────────┐  │   │
                    │  │  │ ATmega328P                │  │   │
                    │  │  │ 16MHz Crystal             │  │   │
                    │  │  │ 32KB Flash                │  │   │
                    │  │  │ 2KB SRAM                  │  │   │
                    │  │  └───────────────────────────┘  │   │
                    │  │                                  │   │
                    │  │  GPIO HEADER                    │   │
                    │  │  ┌──────────────────────────┐  │   │
                    │  │  │ D2 ──── LED Status (Grn) │  │   │
                    │  │  │ D3 ──── LED Status (Yel) │  │   │
                    │  │  │ D4 ──── LED Status (Red) │  │   │
                    │  │  │ D5 ──── Button Start     │  │   │
                    │  │  │ D6 ──── Button Stop      │  │   │
                    │  │  │ D9 ──── Audio Out (PWM)  │  │   │
                    │  │  │ A0 ──── Potentiometer    │  │   │
                    │  │  │ A1 ──── Current Sense    │  │   │
                    │  │  └──────────────────────────┘  │   │
                    │  └─────────────────────────────────┘   │
                    │           │                             │
                    │           │ 3.5mm Audio                 │
                    │           │                             │
                    │  ┌────────┴────────┐                   │
                    │  │  PAM8403 AMP    │                   │
                    │  │  2x3W Class D   │                   │
                    │  │  (5V input)     │                   │
                    │  └────────┬────────┘                   │
                    │           │                             │
                    │           │ Speaker Wire               │
                    │           │                             │
                    │  ┌────────┴────────────────────────┐   │
                    │  │    BaTiO3 CRYSTAL ARRAY         │   │
                    │  │    10x Piezoelectric Discs       │   │
                    │  │    (Phi-harmonic pattern)       │   │
                    │  └─────────────────────────────────┘   │
                    │                                         │
                    │  ┌─────────────────────────────────┐   │
                    │  │    COPPER MESH FIELD SHAPER      │   │
                    │  │    (137.5° golden angle)        │   │
                    │  └─────────────────────────────────┘   │
                    │                                         │
                    │  ┌─────────────────────────────────┐   │
                    │  │    POWER SYSTEM                  │   │
                    │  │    12V DC → 5V Buck → Arduino   │   │
                    │  └─────────────────────────────────┘   │
                    └─────────────────────────────────────────┘
```

---

## DETAILED WIRING TABLE

### Arduino Nano GPIO Allocation

| Pin | Function | Connected To | Direction | Notes |
|-----|----------|--------------|-----------|-------|
| D2 | LED Green | Status LED | Output | Assembly complete |
| D3 | LED Yellow | Status LED | Output | Assembly active |
| D4 | LED Red | Status LED | Output | Error/fault |
| D5 | Button Start | Start Button | Input | Pull-up enabled |
| D6 | Button Stop | Stop Button | Input | Pull-up enabled |
| D9 | Audio Out | PAM8403 Input | Output | PWM tone() |
| A0 | Potentiometer | Speed Control | Input | 10kΩ to 3.3V |
| A1 | Current Sense | ACS712 Module | Input | 5A version |
| 5V | Power Rail | Buck Converter | Power | 5V regulated |
| GND | Ground | Common GND | Ground | Star topology |
| VIN | 12V Input | Buck Converter | Power | 12V raw input |

### PAM8403 Amplifier Connections

| Pin | Connected To | Notes |
|-----|--------------|-------|
| VCC | 5V Rail | From buck converter |
| GND | Ground | Common ground |
| L-IN | Arduino D9 | Audio signal (PWM) |
| R-IN | Tied to L-IN | Mono mode |
| L-OUT | Crystal Array + | Speaker wire |
| R-OUT | Crystal Array - | Speaker wire |

### Crystal Array Wiring

```
CRYSTAL ARRAY CONNECTION (Series-Parallel)

Arduino D9 (Audio) ──► PAM8403 ──► Speaker Wire ──┐
                                                    │
                    ┌───────────────────────────────┤
                    │                               │
                    ▼                               ▼
            ┌───────────────┐             ┌───────────────┐
            │  CRYSTAL PAIR │             │  CRYSTAL PAIR │
            │  (Top Layer)  │             │ (Middle Layer)│
            │               │             │               │
            │  ┌───┐ ┌───┐  │             │  ┌───┐ ┌───┐  │
            │  │C1 │ │C2 │  │             │  │C3 │ │C4 │  │
            │  └─┬─┘ └─┬─┘  │             │  └─┬─┘ └─┬─┘  │
            │    │     │    │             │    │     │    │
            │    └──┬──┘    │             │    └──┬──┘    │
            │       │       │             │       │       │
            └───────┼───────┘             └───────┼───────┘
                    │                             │
                    └──────────┬──────────────────┘
                               │
                    ┌──────────┴──────────────────┐
                    │                             │
                    ▼                             ▼
            ┌───────────────┐             ┌───────────────┐
            │  CRYSTAL PAIR │             │  CRYSTAL PAIR │
            │ (Middle Layer)│             │ (Bottom Layer)│
            │               │             │               │
            │  ┌───┐ ┌───┐  │             │  ┌───┐ ┌───┐  │
            │  │C5 │ │C6 │  │             │  │C7 │ │C8 │  │
            │  └─┬─┘ └─┬─┘  │             │  └─┬─┘ └─┬─┘  │
            │    │     │    │             │    │     │    │
            │    └──┬──┘    │             │    └──┬──┘    │
            │       │       │             │       │       │
            └───────┼───────┘             └───────┼───────┘
                    │                             │
                    └──────────┬──────────────────┘
                               │
                               ▼
                    ┌───────────────┐
                    │  CRYSTAL PAIR │
                    │ (Bottom Layer)│
                    │               │
                    │  ┌───┐ ┌───┐  │
                    │  │C9 │ │C10│  │
                    │  └─┬─┘ └─┬─┘  │
                    │    │     │    │
                    │    └──┬──┘    │
                    │       │       │
                    └───────┼───────┘
                            │
                            ▼
                    COMMON GROUND

CRYSTAL WIRING:
- Each pair: Two discs in parallel (+ to +, - to -)
- Pairs connected in series (pair + to pair -)
- Total impedance: ~100Ω (matches PAM8403 output)
- Wire: 18 AWG speaker wire, <30cm per run
```

---

## POWER DISTRIBUTION

```
                    ┌─────────────────────────────────────┐
                    │        POWER FLOW DIAGRAM           │
                    │                                     │
                    │   12V DC Adapter ──► 5V Buck Conv  │
                    │   (12V/1A)          (12V→5V, 2A)   │
                    │                        │           │
                    │                        ▼           │
                    │                   5V Rail          │
                    │                   (max 2A)         │
                    │                        │           │
                    │          ┌─────────────┼──────┐    │
                    │          │             │      │    │
                    │          ▼             ▼      ▼    │
                    │     ┌────────┐   ┌────────┐ ┌───┐ │
                    │     │Arduino │   │PAM8403 │ │LED│ │
                    │     │Nano    │   │Amp     │ │   │ │
                    │     │100mA   │   │500mA   │ │5mA│ │
                    │     └────────┘   └────────┘ └───┘ │
                    │                                     │
                    │   Total: 605mA (within 2A limit)    │
                    └─────────────────────────────────────┘
```

### Power Connections

```
12V DC Adapter (Barrel Jack)
    │
    ├──[5V Buck]──┐
    │   (12V→5V)  │
    │              │
    │    ┌─────────┴─────────┐
    │    │     5V RAIL       │
    │    │    (max 2A)       │
    │    └────┬────┬────┬────┘
    │         │    │    │
    │         ▼    ▼    ▼
    │    ┌──────┐ ┌──────┐ ┌──────┐
    │    │Arduino│ │PAM8403│ │ LEDs │
    │    │ Nano │ │  AMP  │ │      │
    │    └──────┘ └──────┘ └──────┘
    │
    └──[GND]──► Common Ground
```

---

## SENSOR WIRING DETAILS

### Current Sensor (ACS712)

```
ACS712 Module (5A)            Arduino Nano
┌─────────────────────┐      ┌─────────────────┐
│  VCC ───────────────┼──────┼── 5V            │
│  GND ───────────────┼──────┼── GND           │
│  OUT ───────────────┼──────┼── A1 (Analog)   │
│                     │      │                 │
│  IP+ ───────────────┼──────┤ (In-line with   │
│  IP- ───────────────┼──────┤  crystal power) │
└─────────────────────┘      └─────────────────┘

Current Measurement:
- Range: 0-5A
- Sensitivity: 185mV/A
- Zero-current output: 2.5V
- Formula: I = (Vout - 2.5) / 0.185
```

### Potentiometer (Speed Control)

```
10kΩ Potentiometer           Arduino Nano
┌─────────────────────┐      ┌─────────────────┐
│  VCC ───────────────┼──────┼── 5V            │
│  GND ───────────────┼──────┼── GND           │
│  WIPER ─────────────┼──────┼── A0 (Analog)   │
└─────────────────────┘      └─────────────────┘

Control Range:
- Fully CCW: 0 (minimum frequency)
- Centered: 512 (nominal 528 Hz)
- Fully CW: 1023 (maximum frequency)
```

### Status LEDs

```
LED Connections              Arduino Nano
┌─────────────────────┐      ┌─────────────────┐
│  Green LED:         │      │                 │
│  + ─────────────────┼──────┼── D2 (220Ω)     │
│  - ─────────────────┼──────┼── GND           │
│                     │      │                 │
│  Yellow LED:        │      │                 │
│  + ─────────────────┼──────┼── D3 (220Ω)     │
│  - ─────────────────┼──────┼── GND           │
│                     │      │                 │
│  Red LED:           │      │                 │
│  + ─────────────────┼──────┼── D4 (220Ω)     │
│  - ─────────────────┼──────┼── GND           │
└─────────────────────┘      └─────────────────┘

Note: Each LED needs a 220Ω current-limiting resistor
```

### Start/Stop Buttons

```
Button Connections           Arduino Nano
┌─────────────────────┐      ┌─────────────────┐
│  Start Button:      │      │                 │
│  Pin 1 ─────────────┼──────┼── D5            │
│  Pin 2 ─────────────┼──────┼── GND           │
│                     │      │ (Internal pull-up│
│  Stop Button:       │      │  enabled)       │
│  Pin 1 ─────────────┼──────┼── D6            │
│  Pin 2 ─────────────┼──────┼── GND           │
└─────────────────────┘      └─────────────────┘

Note: Buttons use internal pull-up resistors
      Press = LOW (active low)
```

---

## COPPER MESH FIELD SHAPER WIRING

```
MESH GEOMETRY (Top View)

The copper mesh is NOT wired electrically — it shapes the
piezoelectric field passively through its geometry.

MESH LAYOUT (137.5° golden angle):
    ┌─────────────────────────────────────────┐
    │                                         │
    │   ╱╲   ╱╲   ╱╲   ╱╲   ╱╲   ╱╲   ╱╲    │
    │  ╱  ╲ ╱  ╲ ╱  ╲ ╱  ╲ ╱  ╲ ╱  ╲ ╱  ╲   │
    │ ╱ 137.5°╲  ╲    ╲    ╲    ╲    ╲    ╲  │
    │╱────────╲──╲────╲────╲────╲────╲────╲ │
    │╲────────╱──╱────╱────╱────╱────╱────╱ │
    │ ╲ 137.5°╱  ╱    ╱    ╱    ╱    ╱    ╱  │
    │  ╲  ╱ ╲  ╱ ╲  ╱ ╲  ╱ ╲  ╱ ╲  ╱ ╲  ╱   │
    │   ╲╱   ╲╱   ╲╱   ╲╱   ╲╱   ╲╱   ╲╱    │
    │                                         │
    └─────────────────────────────────────────┘

MESH SPECIFICATION:
- Material: Copper wire mesh
- Wire gauge: 1mm (18 AWG equivalent)
- Opening: 2mm
- Cut angle: 137.5° (golden angle) from horizontal
- Size: 80mm × 80mm (fits inside housing)
- Thickness: 1mm (single layer)

MESH PLACEMENT:
- Positioned between crystal array and target material
- Centered over crystal array
- Distance from crystals: 10-20mm (adjustable)
- No electrical connection required
```

---

## GPIO PIN MAP

| GPIO | Function | Connected To | Direction |
|------|----------|--------------|-----------|
| D2 | LED Green | Status indicator | Output |
| D3 | LED Yellow | Status indicator | Output |
| D4 | LED Red | Status indicator | Output |
| D5 | Start Button | Start switch | Input (pull-up) |
| D6 | Stop Button | Stop switch | Input (pull-up) |
| D9 | Audio Output | PAM8403 amplifier | Output (PWM) |
| A0 | Potentiometer | Speed control | Input (analog) |
| A1 | Current Sense | ACS712 module | Input (analog) |

---

## POWER PINS

| Pin | Voltage | Current | Notes |
|-----|---------|---------|-------|
| 5V (from Buck) | 5V | 2A max | Regulated from 12V |
| VIN (12V direct) | 12V | 500mA | For buck converter input |
| GND | 0V | - | Common ground |

---

## WIRING BEST PRACTICES

1. **Audio Shielding**: Wrap audio wire in foil to prevent interference with crystal array
2. **Power Filtering**: Add 100nF ceramic cap across Arduino VIN and GND
3. **Crystal Wiring**: Use twisted pairs for each crystal to reduce EMI
4. **Ground Star**: All grounds connect at a single point near the buck converter
5. **Wire Length**: Keep crystal wires under 20cm for minimal signal loss
6. **Current Sensing**: Mount ACS712 inline with crystal power for monitoring

---

## CONTINUITY CHECK LIST

Before powering on, verify:

- [ ] All GND pins connected together
- [ ] 5V rail to Arduino VIN (NOT 5V pin when using VIN)
- [ ] No shorts between 5V and GND
- [ ] Crystal array wires not touching copper mesh
- [ ] Amplifier output connected to crystal array
- [ ] Buttons pull-up resistors enabled in firmware
- [ ] LED resistors installed (220Ω)
- [ ] Current sensor in correct orientation

---

**Document**: 02_WIRING.md
**Vehicle**: PHI MOLECULAR ASSEMBLER
**Status**: BUILDABLE ✓
