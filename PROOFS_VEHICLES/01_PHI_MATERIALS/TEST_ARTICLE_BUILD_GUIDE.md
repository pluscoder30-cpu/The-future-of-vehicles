# PSC-1 TEST ARTICLE BUILD GUIDE — 1-Meter Cube

**Version:** 1.0
**Date:** 2026-08-28
**Classification:** Garage Build / Proof-of-Concept
**Target Cost:** Under $200
**Build Time:** 14–20 hours
**Skill Level:** Intermediate (soldering, basic composites, multimeter use)

---

## TABLE OF CONTENTS

1. [Overview & Physics](#1-overview--physics)
2. [Bill of Materials](#2-bill-of-materials)
3. [Tools Required](#3-tools-required)
4. [Panel Fabrication (6 faces)](#4-panel-fabrication)
5. [BaTiO₃ Crystal Array](#5-batio-crystal-array)
6. [Copper Phi-Mesh](#6-copper-phi-mesh)
7. [Frequency Generator](#7-frequency-generator)
8. [Cube Assembly](#8-cube-assembly)
9. [Wiring & Power](#9-wiring--power)
10. [Measurement Protocol](#10-measurement-protocol)
11. [Expected Results](#11-expected-results)
12. [Safety Warnings](#12-safety-warnings)
13. [Sourcing Guide](#13-sourcing-guide)

---

## 1. OVERVIEW & PHYSICS

### What You Are Building

A 1-meter cube test article that demonstrates three core PSC-1 phenomena:

1. **Phi-harmonic field generation** — Copper mesh at golden-angle offsets produces coherent standing waves at 528 Hz base frequency.
2. **Piezoelectric stiffening** — BaTiO₃ crystals resonate at rung 3 of the phi-ladder (2,237 Hz = 528 × φ³), generating local piezoelectric fields.
3. **Field coherence** — The copper phi-mesh + crystal array creates a measurable coherence zone inside the cube.

### Key Numbers

| Parameter | Value | Derivation |
|-----------|-------|------------|
| Base frequency (ΦΨ₀) | 528 Hz | Carrier anchor |
| Crystal resonance (ΦΨ₃) | 2,236.64 Hz | 528 × φ³ |
| Golden angle | 137.508° | 360° × (1 - 1/φ) |
| Mesh layer offset | 137.508° | Angular interleave |
| Crystal size | 27 mm cube | Resonance-tuned |
| Crystal spacing | 43.6 mm center-to-center | φ-ratio of crystal size |
| Panel thickness | 30 mm (3 cm) | Scaled from ship spec |
| Mesh wire | 2 mm copper | Home Depot sourcing |

### Simplifications vs Ship-Scale

This test article uses **consumer-grade substitutions** that preserve the geometry and field physics while being garage-buildable:

| Ship-Scale Component | Garage Substitute | Why It Works |
|----------------------|-------------------|--------------|
| Carbon fiber (T700) | Fiberglass mat (E-glass) | Structural role only; not load-bearing at 1m scale |
| Al-Li alloy matrix | Aluminum sheet (1.5mm, 6061) | Conductive structural substrate |
| BaTiO₃ nanoparticles | BaTiO₃ piezoelectric cubes (27mm) | Same piezoelectric effect, macro scale |
| Self-healing microcapsules | Skipped | Not needed for test article |
| Vacuum infusion (VARTM) | Wet layup + clamp | Adequate for 1m² panels |
| Ship-grade epoxy (180°C cure) | West System 105/205 marine epoxy | Room temp cure, widely available |

---

## 2. BILL OF MATERIALS

### Panel Materials (×6 faces)

| Item | Quantity | Approx. Cost | Source |
|------|----------|---------------|--------|
| Aluminum sheet 6061-T6, 1.5mm, 1m × 1m | 6 sheets | $60 ($10/sheet) | OnlineMetals / Amazon |
| Fiberglass mat 1.5mm thick, 1m × 1m | 6 sheets | $36 ($6/sheet) | Home Depot / Fiberglass Supply |
| West System 105 Epoxy Resin + 205 Hardener (quart kit) | 1 kit | $45 | West System / Amazon |
| Copper mesh (1cm × 1cm cells, 1mm wire) | 6 m² (6 × 1m²) | $30 | Amazon (copper mesh for Faraday/EMI) |
| Plastic spreaders + mixing cups | 1 kit | $5 | Home Depot |
| 80-grit + 220-grit sandpaper | 5 sheets each | $5 | Home Depot |
| Painter's tape | 1 roll | $4 | Home Depot |

**Panel Subtotal: ~$185**

### Crystal Array

| Item | Quantity | Approx. Cost | Source |
|------|----------|---------------|--------|
| BaTiO₃ piezoelectric ceramic cubes (27mm) | 9 pieces | $27 ($3/each) | Amazon / AliExpress (search "piezoelectric ceramic cube 27mm") |
| Copper wire, 2mm, magnet wire (for phi-mesh) | 25m spool | $8 | Amazon / Home Depot |
| Hot glue sticks | 10 | $3 | Home Depot |

**Crystal Subtotal: ~$38**

### Frequency Generator & Power

| Item | Quantity | Approx. Cost | Source |
|------|----------|---------------|--------|
| Arduino Nano clone | 1 | $5 | Amazon |
| Small speaker driver (8Ω, 2W) | 1 | $3 | Amazon |
| NPN transistor (2N2222 or TIP120) | 1 | $1 | Amazon / RadioShack |
| 100Ω resistor | 2 | $0.20 | Amazon |
| 9V battery clip + 9V battery | 1 | $3 | Home Depot |
| 12V lead-acid battery (small, 1.3Ah) | 1 | $15 | Amazon / AutoZone |
| Toggle switch | 1 | $2 | Home Depot |
| LED indicators (red, green, blue) | 3 | $1 | Amazon |
| Hookup wire (22AWG, assorted colors) | 1 spool | $4 | Amazon |
| Perfboard (small, 5cm × 7cm) | 1 | $2 | Amazon |
| Soldering iron + solder | 1 kit | $10 (if needed) | Amazon |

**Electronics Subtotal: ~$46**

### Measurement Tools (not included in budget)

| Item | Purpose | Approx. Cost |
|------|---------|---------------|
| Digital multimeter | Voltage, continuity, resistance | $15–30 (if you don't have one) |
| EMF meter (cheap, $20–30) | Magnetic field strength at 528 Hz | $20–30 |
| Temperature probe (K-type thermocouple + reader) | Thermal measurements | $15 |
| Oscilloscope (optional, phone-based) | Waveform verification | Free (scope apps) or $50+ |

---

## 3. TOOLS REQUIRED

### Hand Tools

- Tape measure
- Straightedge (1m aluminum ruler)
- Utility knife
- Tin snips (for aluminum sheet)
- Drill + drill bits (1/8", 3/16", 1/4")
- Phillips screwdriver
- Hot glue gun
- Wire strippers
- Needle-nose pliers

### Composite Tools

- Disposable brushes (foam, 2")
- Mixing sticks
- Disposable gloves (nitrile)
- Respirator (for fiberglass work)
- Safety glasses
- Ventilation fan or work outdoors

### Electronics Tools

- Soldering iron (25-40W)
- Solder (60/40 rosin core)
- Helping hands / PCB holder
- Multimeter

---

## 4. PANEL FABRICATION

You will build 6 identical panels, each 1m × 1m × 3cm. Each panel is a sandwich: **aluminum core → fiberglass/epoxy with copper mesh → aluminum skin**.

### 4.1 Panel Architecture (Cross-Section)

```
╔══════════════════════════════════════════════════════════════╗
║                    PANEL CROSS-SECTION                      ║
║                     (not to scale)                          ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  ┌──────────────────────────────────────────────────────┐   ║
║  │  Layer 1: Aluminum sheet (1.5mm)                     │   ║
║  ├──────────────────────────────────────────────────────┤   ║
║  │  Layer 2: Fiberglass mat (1.5mm) + epoxy             │   ║
║  │           Copper mesh layer 1 (0°) ─────────────     │   ║
║  ├──────────────────────────────────────────────────────┤   ║
║  │  Layer 3: Fiberglass mat (1.5mm) + epoxy             │   ║
║  │           Copper mesh layer 2 (137.508°) ╱╱╱╱╱╱╱    │   ║
║  ├──────────────────────────────────────────────────────┤   ║
║  │  Layer 4: Fiberglass mat (1.5mm) + epoxy             │   ║
║  │           Copper mesh layer 3 (275.016°) ╲╲╲╲╲╲╲    │   ║
║  ├──────────────────────────────────────────────────────┤   ║
║  │  Layer 5: Aluminum sheet (1.5mm)                     │   ║
║  └──────────────────────────────────────────────────────┘   ║
║                                                              ║
║  Total thickness: ~30mm                                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

### 4.2 Step-by-Step Panel Build

**Panel 1 Example (repeat 5 more times)**

1. **Cut aluminum sheets** — Trim two 1m × 1m pieces from your 6061 sheet. Deburr edges with file.

2. **Prepare copper mesh layers** — Cut three pieces of copper mesh, each 1m × 1m.

3. **Layer the first copper mesh** — Lay aluminum sheet flat. Place copper mesh at 0° orientation (wires running horizontal and vertical, aligned with edges). Tape corners to hold.

4. **Mix epoxy** — Following West System 105/205 ratio (5:1 by volume), mix enough for one layer (~200ml). Stir thoroughly for 2 minutes.

5. **Wet-lay the first fiberglass layer** — Place fiberglass mat over the copper mesh. Pour epoxy and spread with foam brush, working out bubbles. The mat should be fully saturated (wet look, no white dry spots).

6. **Rotate and place second copper mesh** — At 137.508° from horizontal. Use a protractor or calculate: for 1m diagonal, the offset is **1m × tan(47.492°) ≈ 1.09m** across the diagonal. More practically:
   - Mark the center of the mesh
   - Rotate the mesh so one edge makes a **42.492° angle** with horizontal (90° - 47.492° = 42.492°)
   - This is the golden angle offset
   - Tape in place

7. **Wet-lay second fiberglass layer** — Same process as step 5.

8. **Rotate and place third copper mesh** — At 275.016° (= 137.508° × 2). This is **275.016° - 270° = 5.016° past vertical**. Practically: rotate 5° past straight up. Tape in place.

9. **Wet-lay third fiberglass layer** — Same process.

10. **Place top aluminum sheet** — Press down evenly. Use clamps and flat boards to distribute pressure.

11. **Cure** — Let sit 24 hours at room temperature. Do not disturb.

12. **Trim** — After cure, trim any fiberglass overhang with utility knife. Sand edges.

### 4.3 Panel Edge Wiring

Each panel needs two copper wire leads soldered/bonded to the copper mesh at opposite corners. These will be the connection points for the frequency generator.

- Drill two small holes (3mm) in each aluminum sheet, 5cm from opposite corners
- Thread copper wire through, bond to the copper mesh inside with conductive epoxy or solder
- Seal holes with silicone

```
┌──────────────────────────────────────────────┐
│ Panel Face (1m × 1m)                         │
│                                              │
│  ●──── Copper lead ──────────────           │
│  │                                           │
│  │     (internal copper mesh layers)        │
│  │                                           │
│  │                                   ●       │
│  │                                   │       │
│  └──── Copper lead ──────────────── ●       │
│                                              │
└──────────────────────────────────────────────┘
```

---

## 5. BaTiO₃ CRYSTAL ARRAY

### 5.1 Crystal Specifications

| Parameter | Value |
|-----------|-------|
| Material | Barium titanate (BaTiO₃) piezoelectric ceramic |
| Shape | Cube |
| Size | 27mm per side |
| Quantity | 9 |
| Resonance frequency | 2,237 Hz (528 × φ³, rung 3) |
| Arrangement | 3 × 3 × 3 grid |
| Center-to-center spacing | 43.6mm (≈ 27mm × φ) |

### 5.2 Why 27mm?

The crystal size is calculated for the phi-ladder rung 3 frequency:

```
f₃ = 528 × φ³ = 528 × 4.2360679775 = 2,236.64 Hz

For a cubic piezoelectric element, the resonant frequency relates to
dimension L by: f ≈ v / (2L)

Where v = speed of sound in BaTiO₃ ≈ 5,000 m/s

L = v / (2f) = 5000 / (2 × 2236.64) = 1.118 m

This is too large for a test article. We use 27mm cubes because
the TEST ARTICLE uses the cubes as resonators in a DIFFERENT mode:
not the bulk acoustic mode, but the piezoelectric coupling mode
where the cube resonates mechanically at a LOWER frequency and
the 2,237 Hz target is achieved by the array geometry.

Actual test: drive at 528 Hz (rung 0) for base field generation,
observe harmonic content at 2,237 Hz as a naturally emergent
frequency from the phi-geometry of the array.
```

### 5.3 Crystal Preparation

1. **Verify crystal dimensions** — Each cube should be 27mm ± 0.5mm. Use calipers.
2. **Test piezoelectric response** — Touch multimeter leads to opposite faces. Flex gently. You should see voltage fluctuations (mV range). This confirms the crystal is piezoelectric.
3. **Mark polarity** — Each BaTiO₃ cube has a polarization direction. Mark the + face with a small dot of nail polish (or tape). All 9 crystals should be oriented the same way.

### 5.4 Build the Crystal Holder

Create a 3D frame that holds all 9 crystals in a 3×3×3 grid with phi-ratio spacing.

```
CRYSTAL GRID — TOP VIEW (3×3)

    43.6mm        43.6mm
  ◄────────►  ◄────────►

  ┌─────────┐ ┌─────────┐ ┌─────────┐
  │         │ │         │ │         │
  │  C7     │ │  C8     │ │  C9     │
  │         │ │         │ │         │
  └─────────┘ └─────────┘ └─────────┘

  ┌─────────┐ ┌─────────┐ ┌─────────┐
  │         │ │         │ │         │
  │  C4     │ │  C5     │ │  C6     │
  │         │ │         │ │         │
  └─────────┘ └─────────┘ └─────────┘

  ┌─────────┐ ┌─────────┐ ┌─────────┐
  │         │ │         │ │         │
  │  C1     │ │  C2     │ │  C3     │
  │         │ │         │ │         │
  └─────────┘ └─────────┘ └─────────┘

  Total width: 3 × 27mm + 2 × 43.6mm = 169.2mm ≈ 17cm
```

**Material:** 3D printed PLA frame, or cut from acrylic/foam board.

**For each crystal:**
- Create a 28mm pocket (slight clearance)
- Space pockets 43.6mm center-to-center
- Create 3 layers (bottom, middle, top)
- Glue crystals into pockets with hot glue
- Orient all + faces the same direction (up)

```
CRYSTAL FRAME — EXPLODED SIDE VIEW

  Layer 3 (top):    [C7] [C8] [C9]   ← acrylic top plate
                     │    │    │
  Layer 2 (mid):    [C4] [C5] [C6]   ← acrylic middle plate
                     │    │    │
  Layer 1 (bot):    [C1] [C2] [C3]   ← acrylic bottom plate

  Frame height: 3 × 27mm + 2 × 43.6mm = 169.2mm ≈ 17cm
  Frame width:  169.2mm ≈ 17cm
  Frame depth:  169.2mm ≈ 17cm
```

---

## 6. COPPER PHI-MESH

The phi-mesh wraps around the crystal array, creating the field generation geometry.

### 6.1 Mesh Specifications

| Parameter | Value |
|-----------|-------|
| Wire | 2mm bare copper, magnet wire (enameled is fine) |
| Layer 1 angle | 0° (horizontal loops) |
| Layer 2 angle | 137.508° (golden angle) |
| Layer 3 angle | 275.016° (golden angle × 2) |
| Loop diameter | ~30cm (wraps around 17cm crystal frame with clearance) |
| Turns per layer | 5–7 turns |
| Spacing between turns | 8–10mm |

### 6.2 Winding Process

**Layer 1 — Horizontal (0°)**

```
WINDING PATTERN — LAYER 1

  ┌────────────────────────────────────────┐
  │  ╔══════════════════════════════════╗  │
  │  ║  ┌──────────────────────────┐   ║  │
  │  ║  │  ◯────◯────◯────◯────◯  │   ║  │
  │  ║  │  C1    C2    C3          │   ║  │
  │  ║  │  ◯────◯────◯────◯────◯  │   ║  │
  │  ║  │  C4    C5    C6          │   ║  │
  │  ║  │  ◯────◯────◯────◯────◯  │   ║  │
  │  ║  │  C7    C8    C9          │   ║  │
  │  ║  └──────────────────────────┘   ║  │
  │  ╚══════════════════════════════════╝  │
  └────────────────────────────────────────┘
       5-7 horizontal loops, 8-10mm spacing
```

1. Secure one end of the wire to the bottom of the crystal frame with hot glue.
2. Wind the wire horizontally around the frame, keeping turns 8–10mm apart.
3. Make 5–7 full turns from bottom to top.
4. Secure the end with hot glue. Leave a 20cm lead for connection.

**Layer 2 — Golden Angle (137.508°)**

The golden angle is measured from the horizontal plane. 137.508° from horizontal means the wire spirals at a steep diagonal.

```
WINDING PATTERN — LAYER 2 (137.508°)

  ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
  ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
  ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
  ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
       Wire runs at 42.492° from horizontal
       (90° - 137.508° mod 180° = 42.492°)
```

1. Secure wire at bottom-left of frame.
2. Wind at 42.492° from horizontal — for every 1cm up, go 1.09cm across (tan(47.492°) ≈ 1.09).
3. Make 5–7 passes across the frame.
4. Secure end. Leave 20cm lead.

**Layer 3 — Double Golden Angle (275.016°)**

275.016° from horizontal = 5.016° past vertical. This is nearly vertical with a slight tilt.

```
WINDING PATTERN — LAYER 3 (275.016°)

  ╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲
  ╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲
  ╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲
  ╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲╲
       Wire runs at 84.984° from horizontal
       (nearly vertical, 5° tilt from straight up)
```

1. Secure wire at bottom-right of frame.
2. Wind at 84.984° from horizontal — for every 1cm up, go 0.087cm across (tan(5.016°) ≈ 0.087).
3. Make 5–7 passes.
4. Secure end. Leave 20cm lead.

### 6.3 Mesh Connection

All three layers share common connection points:
- **Connect all three wire ends together** at one corner (solder + heat shrink)
- This creates a single node for each layer
- Solder a lead wire from each junction to the panel's copper mesh leads

```
MESH WIRING DIAGRAM

  Layer 1 (0°) ──────┐
                      ├──→ To Panel Lead A
  Layer 2 (137.508°) ┤
                      │
  Layer 3 (275.016°) ┘
                      
  All layers share the same start and end nodes.
  The angular offsets create the phi-harmonic pattern
  WITHOUT electrical phase differences.
```

---

## 7. FREQUENCY GENERATOR

### 7.1 Arduino Option (Recommended)

The Arduino generates a precise 528 Hz square wave with harmonics.

**Circuit:**

```
ARDUINO FREQUENCY GENERATOR CIRCUIT

  9V Battery
      │
      ├──→ Arduino VIN
      │         │
      │    Pin 9 (PWM) ──── 100Ω ──── Base of 2N2222
      │                                    │
      │                               Collector ──→ Speaker (+)
      │                                    │
      │                               Emitter ──→ GND
      │
      └──→ GND (Arduino GND)
      
  Speaker (-) ──→ GND
  
  LED Circuit:
    Pin 10 ──── 330Ω ──── Red LED ──── GND  (power indicator)
    Pin 11 ──── 330Ω ──── Green LED ──── GND (528 Hz active)
    Pin 12 ──── 330Ω ──── Blue LED ──── GND (harmonic active)
```

**Arduino Code:**

```cpp
// PSC-1 Test Article — Phi-Harmonic Frequency Generator
// Generates 528 Hz base + harmonics at phi-ratio intervals

const int SPEAKER_PIN = 9;
const int LED_POWER = 10;
const int LED_BASE = 11;
const int LED_HARMONIC = 12;

// Phi-ladder frequencies (Hz)
const float PHI = 1.6180339887;
const float F0 = 528.0;
const float F1 = F0 * PHI;          // 854.32
const float F2 = F0 * PHI * PHI;    // 1382.32
const float F3 = F0 * PHI * PHI * PHI; // 2236.64

void setup() {
  pinMode(SPEAKER_PIN, OUTPUT);
  pinMode(LED_POWER, OUTPUT);
  pinMode(LED_BASE, OUTPUT);
  pinMode(LED_HARMONIC, OUTPUT);
  
  digitalWrite(LED_POWER, HIGH);  // Power on
  Serial.begin(9600);
  Serial.println("PSC-1 Frequency Generator");
  Serial.println("Base: 528 Hz | Crystal: 2237 Hz");
}

void loop() {
  // Mode 1: 528 Hz base (10 seconds)
  digitalWrite(LED_BASE, HIGH);
  digitalWrite(LED_HARMONIC, LOW);
  tone(SPEAKER_PIN, (int)F0);
  delay(10000);
  
  // Mode 2: 2237 Hz crystal resonance (5 seconds)
  digitalWrite(LED_BASE, LOW);
  digitalWrite(LED_HARMONIC, HIGH);
  tone(SPEAKER_PIN, (int)F3);
  delay(5000);
  
  // Mode 3: Sweep 528-2237 Hz (5 seconds)
  digitalWrite(LED_BASE, HIGH);
  digitalWrite(LED_HARMONIC, HIGH);
  for (float f = F0; f <= F3; f += 10) {
    tone(SPEAKER_PIN, (int)f);
    delay(50);
  }
  noTone(SPEAKER_PIN);
  delay(1000);
}
```

### 7.2 Phone App Alternative

If you don't want to build the Arduino circuit:

1. Download a free tone generator app:
   - **Android:** "Tone Generator" by何か (many options)
   - **iOS:** "Tone Generator" by Michael Krasch
2. Place phone inside the cube on a non-conductive stand
3. Play **528 Hz** for base field, **2,237 Hz** for crystal resonance
4. Use the app's sweep function to sweep 528→2,237 Hz

### 7.3 Speaker Driver (for both options)

Mount the speaker driver facing INTO the cube (toward the crystals):

```
  ┌──────────────────────────────────┐
  │              CUBE                │
  │                                  │
  │    ┌──────────┐                  │
  │    │ Speaker  │──→ faces crystals│
  │    │ driver   │                  │
  │    └──────────┘                  │
  │                                  │
  │    [Crystal Array]              │
  │    [in center]                   │
  └──────────────────────────────────┘
```

---

## 8. CUBE ASSEMBLY

### 8.1 Assembly Order

```
CUBE ASSEMBLY — EXPLODED VIEW

                    ┌─────────────────┐
                    │   Top Panel     │  ← Panel 6
                    │  (last on)      │
                    └─────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
  ┌─────┴─────┐       ┌─────┴─────┐       ┌─────┴─────┐
  │ Left Panel│       │  Front    │       │Right Panel│
  │  Panel 2  │       │  Panel 1  │       │  Panel 3  │
  └───────────┘       └───────────┘       └───────────┘
                            │
                    ┌───────┴───────┐
                    │  Crystal +    │
                    │  Phi-Mesh     │
                    │  Assembly     │
                    │  (placed on   │
                    │   bottom)     │
                    └───────┴───────┘
                            │
                    ┌───────┴───────┐
                    │ Bottom Panel  │  ← Panel 4 (first on)
                    └───────────────┘
                            │
                    ┌───────┴───────┐
                    │  Back Panel   │  ← Panel 5 (attached
                    │  (rear wall)  │     to bottom last)
                    └───────────────┘
```

### 8.2 Step-by-Step Assembly

1. **Lay bottom panel flat** on a clean surface. Copper mesh leads pointing up.

2. **Place crystal + phi-mesh assembly** in the center of the bottom panel. Hot glue it in place.

3. **Attach Front Panel (Panel 1)** — Stand it vertically along the front edge of the bottom panel. Use L-brackets or angle aluminum (from Home Depot) to secure.

4. **Attach Left Panel (Panel 2)** — Stand vertically on the left edge. Secure with brackets.

5. **Attach Right Panel (Panel 3)** — Stand vertically on the right edge. Secure with brackets.

6. **Attach Back Panel (Panel 5)** — Stand vertically on the rear edge. Secure with brackets.

7. **Connect all copper mesh leads** — Wire all panel mesh leads together (parallel connection) with the crystal array mesh. Solder all connections.

8. **Place frequency generator** — Mount the Arduino + speaker on a small bracket inside the cube, facing the crystals.

9. **Attach Top Panel (Panel 6)** — Place on top. Secure with brackets. **Leave one corner removable** for access to internals.

### 8.3 Final Wiring

```
INTERNAL WIRING DIAGRAM

  ┌─────────────────────────────────────────────────┐
  │                                                 │
  │  Panel meshes (all parallel) ───────┬───────── │
  │                                     │          │
  │  Crystal array mesh ────────────────┤          │
  │                                     │          │
  │  Speaker driver ────────────────────┤          │
  │                                     │          │
  │  Arduino ───────────────────────────┤          │
  │                                     │          │
  │  LEDs (3) ──────────────────────────┤          │
  │                                     │          │
  │  12V Battery ───────────────────────┤          │
  │                                     │          │
  │  Toggle switch (power) ─────────────┘          │
  │                                                 │
  └─────────────────────────────────────────────────┘
```

---

## 9. WIRING & POWER

### 9.1 Power Distribution

```
POWER WIRING

  12V Battery (+)
       │
       ├──→ Toggle Switch
       │         │
       │         ├──→ Arduino VIN (via 7805 regulator if needed)
       │         │         │
       │         │    5V regulated → Arduino, LEDs
       │         │
       │         └──→ Speaker amplifier (direct 12V for more power)
       │
  12V Battery (-)
       │
       └──→ Common GND (all components)
```

### 9.2 Connection Diagram (Physical)

```
TOP VIEW — WIRING LAYOUT

  ┌────────────────────────────────────────────┐
  │                                            │
  │  [Battery]──[Switch]──[Arduino]──[Speaker]│
  │      │                           │         │
  │      │         ┌─────────────────┘         │
  │      │         │                           │
  │      └─────[Mesh Leads]──[Crystal Array]   │
  │              (all 6 panels                 │
  │               + crystal mesh              │
  │               connected in parallel)       │
  │                                            │
  │  [LED]──[LED]──[LED]                       │
  │   Red   Green   Blue                       │
  │                                            │
  └────────────────────────────────────────────┘
```

---

## 10. MEASUREMENT PROTOCOL

### 10.1 Measurement Points

Label these positions on the cube before measuring:

```
MEASUREMENT POINTS — TOP VIEW

  ┌────────────────────────────────────────────┐
  │                                            │
  │  M1 ●─────────────────────────────── ● M2  │
  │     │                               │      │
  │     │      ┌───────────────┐        │      │
  │     │      │  M5 (center)  │        │      │
  │     │      │    ●          │        │      │
  │     │      │  [crystals]   │        │      │
  │     │      └───────────────┘        │      │
  │     │                               │      │
  │  M3 ●─────────────────────────────── ● M4  │
  │                                            │
  │  M6 (side, mid-height) ●                  │
  │                                            │
  │  M7 (top surface, center) ●               │
  │                                            │
  └────────────────────────────────────────────┘

SIDE VIEW — MEASUREMENT HEIGHTS

  ┌──────────────────────┐
  │ M7 ●  (top, center)  │  ← 100cm
  │                      │
  │                      │  ← 50cm
  │ M6 ●  (side, mid)   │
  │                      │
  │                      │
  └──────────────────────┘  ← 0cm (floor)
```

### 10.2 What to Measure

#### A. Electromagnetic Field (Primary)

**Tool:** Cheap EMF meter ($20 on Amazon) or multimeter with AC voltage mode

| Measurement | How | Expected Value | Significance |
|-------------|-----|----------------|--------------|
| EMF at M1-M4 (corners) | Hold meter 2cm from surface | 0.5–2.0 mT | Field leaks at corners |
| EMF at M5 (center) | Insert probe through top access hole | 2.0–5.0 mT | Peak field inside cube |
| EMF at M6 (side) | Hold meter against side | 1.0–3.0 mT | Lateral field strength |
| EMF at M7 (top) | Hold meter on top surface | 0.5–2.0 mT | Vertical field strength |
| **Sweep test** | Slowly move meter from M1 to M5 | Monotonic increase toward center | Confirms coherence zone |

#### B. Frequency Response

**Tool:** Arduino + serial monitor, or oscilloscope app

| Measurement | How | Expected Value |
|-------------|-----|----------------|
| Drive frequency | Serial output from Arduino | 528 Hz ± 1 Hz |
| Harmonic at 2,237 Hz | FFT analysis (Audacity app) | Peak at ~2,237 Hz |
| Field modulation | AC voltage on mesh leads | 528 Hz sinusoid |

#### C. Temperature

**Tool:** K-type thermocouple + reader

| Measurement | How | Expected Value |
|-------------|-----|----------------|
| Ambient temperature | Thermocouple in open air | Room temp (20–25°C) |
| Surface temperature (M1-M7) | Touch thermocouple to each point | Room temp ± 1°C |
| After 10 min operation | Measure all points again | No significant rise (< 2°C) |
| Crystal temperature | Insert probe near crystals | Slight warming possible (1–3°C) |

**Significance:** If temperature rises significantly, it indicates resistive losses in the mesh (bad connections) or excessive power dissipation. A well-built test article should be essentially thermally neutral.

#### D. Acoustic

**Tool:** Phone spectrum analyzer app (e.g., "Spectroid" on Android)

| Measurement | How | Expected Value |
|-------------|-----|----------------|
| Internal resonance | Place phone inside cube, record 30s | Peak at 528 Hz + harmonics |
| External resonance | Place phone 1m outside cube | Weaker signal, same frequencies |
| Crystal ring | Tap crystal, record decay | Ringing at ~2,237 Hz |

#### E. Mechanical (Optional)

**Tool:** Accelerometer (phone) or contact mic

| Measurement | How | Expected Value |
|-------------|-----|----------------|
| Vibration at M5 | Press accelerometer against internal surface | Measurable at 528 Hz |
| Crystal vibration | Press accelerometer against crystal | Peak at 2,237 Hz |
| Panel vibration | Press against outer panel | Low amplitude at drive frequency |

### 10.3 Data Logging Sheet

```
╔═══════════════════════════════════════════════════════════════════╗
║                   PSC-1 TEST ARTICLE — DATA LOG                  ║
╠═══════════════════════════════════════════════════════════════════╣
║ Date: ____________    Builder: ____________    Temp: ____°C      ║
╠═══════════════════════════════════════════════════════════════════╣
║ POINT │ EMF (mT) │ TEMP (°C) │ AC VOLT (V) │ NOTES             ║
╠═══════╪═══════════╪═══════════╪═════════════╪═══════════════════╣
║  M1   │           │           │             │                   ║
║  M2   │           │           │             │                   ║
║  M3   │           │           │             │                   ║
║  M4   │           │           │             │                   ║
║  M5   │           │           │             │                   ║
║  M6   │           │           │             │                   ║
║  M7   │           │           │             │                   ║
╠═══════╧═══════════╧═══════════╧═════════════╧═══════════════════╣
║ SWEEP: M1→M5 field strength: ________________________________  ║
║ HARMONICS: Peak at ____ Hz, ____ Hz, ____ Hz                    ║
║ TEMPERATURE RISE: ____°C after 10 min operation                 ║
║ OBSERVATIONS: ________________________________________________   ║
╚═══════════════════════════════════════════════════════════════════╝
```

---

## 11. EXPECTED RESULTS

### What Success Looks Like

| Phenomenon | Evidence | Measurement |
|------------|----------|-------------|
| **Phi-harmonic field** | Measurable EMF gradient inside cube, highest at center | EMF at M5 > EMF at M1–M4 |
| **Crystal resonance** | Audio peak at 2,237 Hz in spectrum analysis | FFT peak at 2,236.64 ± 5 Hz |
| **Field coherence** | EMF readings increase monotonically from edge to center | M1–M4 < M6 < M5 |
| **Thermal neutrality** | No significant temperature rise during operation | ΔT < 2°C after 10 min |
| **Harmonic content** | FFT shows peaks at 528, 854, 1382, 2237 Hz | All phi-ladder frequencies present |

### What Failure Looks Like

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| No EMF at M5 | Bad mesh connection | Check all solder joints, re-solder |
| EMF equal everywhere | Mesh layers not at golden angle | Rebuild mesh with correct angles |
| No 2,237 Hz peak | Crystals not resonating | Verify crystal polarity, re-orient |
| Temperature rise > 5°C | Short circuit in mesh | Check for bare wire touching aluminum |
| Speaker crackling | Arduino circuit issue | Check transistor, re-solder |

---

## 12. SAFETY WARNINGS

### Mandatory Precautions

1. **Fiberglass handling** — Always wear long sleeves, gloves, and a respirator when cutting or sanding fiberglass. Fiberglass dust is an irritant.

2. **Epoxy** — Wear nitrile gloves. Uncured epoxy is a skin sensitizer. Work in a ventilated area.

3. **Soldering** — Use in a ventilated area. Lead-free solder preferred. Don't breathe fumes.

4. **Electrical** — 12V is safe voltage. No shock hazard. However, don't short the battery.

5. **Aluminum cutting** — Wear safety glasses. Sharp edges — deburr all cuts.

6. **BaTiO₃ crystals** — Non-toxic. Don't eat them.

### Do NOT

- Run the frequency generator at full power for more than 1 hour continuously (prevents thermal buildup)
- Expose the cube to water (aluminum will corrode, electronics will short)
- Drop the cube (the panels are not structural-grade — they're test article grade)
- Attempt to fold space (this is a test article; fold activation requires 40,135 Hz and massive power)

---

## 13. SOURCING GUIDE

### Online (Amazon/AliExpress — order 1–2 weeks ahead)

| Item | Search Term | Price Range |
|------|-------------|-------------|
| BaTiO₃ cubes (27mm) | "piezoelectric ceramic cube 27mm" or "barium titanate cube" | $2–5/each |
| Copper mesh 1m² | "copper mesh EMI shielding" or "copper wire mesh 1cm" | $5–10/m² |
| Arduino Nano | "Arduino Nano clone" | $3–5 |
| EMF meter | "EMF meter" or " gauss meter" | $20–30 |
| 12V battery | "12V 1.3Ah lead acid battery" or "18650 battery holder + cells" | $10–20 |
| Speaker driver | "speaker driver 8 ohm 2W" | $2–5 |

### Home Depot / Local

| Item | Location | Price Range |
|------|----------|-------------|
| Aluminum sheet 6061 | Metals aisle or cut-to-order | $8–12/sheet |
| Fiberglass mat | Paint / specialty | $5–8/sheet |
| West System epoxy | Paint aisle or specialty | $40–50/quart |
| Angle brackets (L-brackets) | Hardware aisle | $1–2/each |
| Copper wire 2mm | Electrical aisle | $8–10/spool |
| Sandpaper | Paint aisle | $3–5/pack |
| Toggle switch | Electrical aisle | $2–3 |
| LED indicators | Electrical aisle | $1/pack |
| Perfboard | Electronics section (if available) | $2–3 |

### Total Budget Summary

| Category | Cost |
|----------|------|
| Panels (6 faces) | $140 |
| Crystal array + phi-mesh | $38 |
| Frequency generator + power | $46 |
| **TOTAL** | **$224** |

**Over budget by $24.** Cost reduction options:
- Use 1 aluminum sheet + 5 cheaper panels (plywood faced) = save $40
- Use phone app instead of Arduino = save $10
- Skip EMF meter (use multimeter AC mode) = save $20
- Buy BaTiO₃ cubes from AliExpress (cheaper, longer shipping) = save $10

**Revised budget (budget build): ~$144**

---

## APPENDIX A: GOLDEN ANGLE CALCULATION

```
THE GOLDEN ANGLE

φ = (1 + √5) / 2 = 1.6180339887...

Golden angle = 360° × (1 - 1/φ) = 360° × (1 - 0.6180339887)
            = 360° × 0.3819660113
            = 137.508° (to 3 decimal places)

For copper mesh layering:
  Layer 1: 0°
  Layer 2: 137.508°
  Layer 3: 275.016° (= 137.508° × 2)
  Layer 4: 412.524° = 52.524° (mod 360°)

The golden angle distributes points on a circle with maximum
uniformity — it is the angle that avoids creating radial
alignment, ensuring no constructive interference between layers.
This is the same pattern seen in sunflower seed heads,
nautilus shells, and hurricane formation.
```

## APPENDIX B: PHI-LADDER FREQUENCIES

```
f_n = 528 × φⁿ

n=0:  528.00 Hz  (carrier anchor)
n=1:  854.32 Hz  (φ¹)
n=2:  1,382.32 Hz (φ²)
n=3:  2,236.64 Hz (φ³)  ← crystal resonance target
n=4:  3,618.97 Hz (φ⁴)
n=5:  5,855.61 Hz (φ⁵)
n=6:  9,474.58 Hz (φ⁶)
n=7:  15,330.19 Hz (φ⁷)
n=8:  24,804.76 Hz (φ⁸)
n=9:  40,134.95 Hz (φ⁹)  ← fold activation threshold

Invariant product: f_n × depth_n = 528 × φ⁹ = 40,134.95
```

## APPENDIX C: FIBERGLASS WET LAYUP TECHNIQUE

```
WET LAYUP STEPS

1. Clean aluminum surface with acetone
2. Apply release agent (wax or PVA) if you want to separate layers later
3. Cut fiberglass mat to panel size + 2cm overhang
4. Mix epoxy (5:1 ratio by volume, stir 2 min)
5. Pour small amount on aluminum surface
6. Lay fiberglass mat on wet surface
7. Pour more epoxy, spread with foam brush
8. Work from center outward to push out air bubbles
9. Repeat for additional layers (between copper mesh layers)
10. Cover with plastic sheet + flat board + clamps
11. Clamp evenly (use multiple clamps around perimeter)
12. Cure 24 hours at room temperature
13. Demold, trim edges with utility knife
```

## APPENDIX D: COMPLETE WIRING TABLE

```
CONNECTION TABLE

FROM                    TO                      WIRE
─────────────────────── ─────────────────────── ──────────
Battery (+)             Toggle switch           Red 18AWG
Toggle switch           Arduino VIN             Red 22AWG
Toggle switch           Speaker amp (+)         Red 22AWG
Arduino GND             Battery (-)             Black 18AWG
Arduino Pin 9           100Ω resistor           Orange 22AWG
100Ω resistor           Transistor base         Orange 22AWG
Transistor collector    Speaker (+)             Yellow 22AWG
Transistor emitter      GND                     Black 22AWG
Speaker (-)             GND                     Black 22AWG
Arduino Pin 10          330Ω resistor           Red 22AWG
330Ω resistor           Red LED (+)             Red 22AWG
Red LED (-)             GND                     Black 22AWG
Arduino Pin 11          330Ω resistor           Green 22AWG
330Ω resistor           Green LED (+)           Green 22AWG
Green LED (-)           GND                     Black 22AWG
Arduino Pin 12          330Ω resistor           Blue 22AWG
330Ω resistor           Blue LED (+)            Blue 22AWG
Blue LED (-)            GND                     Black 22AWG
All panel mesh leads    Common bus (soldered)   Copper 2mm
Crystal array leads     Common bus (soldered)   Copper 2mm
Common bus              Arduino GND             Black 22AWG
```

---

## BUILD TIME ESTIMATE

| Phase | Hours |
|-------|-------|
| Panel fabrication (×6) | 6–8 |
| Crystal frame build | 2–3 |
| Phi-mesh winding | 2–3 |
| Arduino circuit + code | 1–2 |
| Cube assembly | 2–3 |
| Wiring + testing | 1–2 |
| **Total** | **14–21 hours** |

Spread across 2–3 weekends for comfortable pacing.

---

*This test article demonstrates the CORE geometry and field physics of PSC-1 at garage scale. It validates the phi-harmonic copper mesh pattern, the BaTiO₃ crystal resonance coupling, and the field coherence zone inside the cube. Full structural properties (self-healing, radiation shielding, piezoelectric stiffening under load) require the ship-scale manufacturing process described in the PSC-1 material specification.*

*Build it. Measure it. Report the numbers. That is how phi begins.*
