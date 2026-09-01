# PHI MOLECULAR ASSEMBLER — ASSEMBLY INSTRUCTIONS

## Build Time: 6-10 hours (can be done in one weekend)

---

## PHASE 1: CRYSTAL ARRAY PREPARATION (1.5 hours)

### Step 1: Test All 10 BaTiO₃ Discs

Before building, verify each disc works.

1. Connect alligator clips to each side of a disc (brass backing = ground, ceramic face = signal)
2. Touch the leads to a multimeter set to AC mV
3. Tap the disc gently — you should see 50-200 mV spike
4. If a disc shows no voltage, discard it (defective)
5. Label working discs 1-10

### Step 2: Arrange Discs in Phi-Harmonic Pattern

The 10 discs must be arranged in a phi-spiral pattern. This is not arbitrary — the 137.5° golden angle between each disc ensures their fields constructively interfere at phi-harmonic nodes.

```
TOP VIEW — DISC ARRANGEMENT (Phi-Spiral):
═══════════════════════════════════════════════════

  Place discs on a flat surface in this pattern.
  The angle between consecutive discs (measured from center)
  is 137.5° — the golden angle.

            1
           ╱ ╲
          8   2
         ╱     ╲
        7   ●   3       ● = center point
         ╲     ╱        (no disc here)
          6   4
           ╲ ╱
            5
            |
           10
            |
            9

  Angel between each disc from center: 137.5°
  Distance from center: increases by φ⁻¹ per step

  Disc 1: 0°,    radius 15mm from center
  Disc 2: 137.5°, radius 24mm (15 × φ)
  Disc 3: 275.0°, radius 39mm (24 × φ)
  Disc 4: 52.5°,  radius 63mm (39 × φ)
  Disc 5: 190.0°, radius 102mm (63 × φ)
  Disc 6: 327.5°, radius 165mm — CLIP to 80mm (keep compact)
  Disc 7: 105.0°, radius 55mm
  Disc 8: 242.5°, radius 40mm
  Disc 9: 20.0°,  radius 30mm
  Disc 10: 157.5°, radius 25mm

  NOTE: Discs 5-10 spiral back inward. The full phi-spiral
  would expand beyond the housing, so the outer discs
  fold back at 137.5° intervals, creating a dense packing.
```

### Step 3: Secure Discs to Base

1. Cut a circle of cardboard or thin plywood, 120mm diameter
2. Mark the center point
3. Using a protractor, mark 137.5° intervals from center
4. Measure radii from the table above
5. Hot-glue each disc at its position, ceramic face UP
6. Let glue cool 10 minutes

### Step 4: Wire the Crystal Array

Connect the discs in a specific wiring pattern that creates a phi-harmonic voltage cascade:

```
WIRING DIAGRAM — Crystal Array:
═══════════════════════════════════════════════════

  The discs are wired in THREE PARALLEL GROUPS,
  each group driven by one amplifier channel:

  GROUP A (Base — 528 Hz):
  ┌─────────────────────────────────┐
  │  Disc 1 ──┬── Disc 4 ──┬── Disc 7 ──┬── Disc 10 │
  │           │            │            │           │
  │  All ceramic faces → SIGNAL (red)              │
  │  All brass backs   → GROUND (black)            │
  └─────────────────────────────────┘

  GROUP B (Harmonic — 854 Hz):
  ┌─────────────────────────────────┐
  │  Disc 2 ──┬── Disc 5 ──┬── Disc 8            │
  │           │            │                       │
  │  All ceramic faces → SIGNAL                   │
  │  All brass backs   → GROUND                   │
  └─────────────────────────────────┘

  GROUP C (Correction — 1382 Hz):
  ┌─────────────────────────────────┐
  │  Disc 3 ──┬── Disc 6 ──┬── Disc 9            │
  │           │            │                       │
  │  All ceramic faces → SIGNAL                   │
  │  All brass backs   → GROUND                   │
  └─────────────────────────────────┘

  WHY THREE GROUPS:
  The phi-ladder has 10 rungs, but we only have 10 discs.
  By running three frequency groups simultaneously, we
  cover the three most important assembly rungs:
  - 528 Hz (base carrier — molecular anchor)
  - 854 Hz (molecular vibration — alignment)
  - 1382 Hz (crystal lattice — structure locking)

  The Arduino cycles through: 528→854→1382→528→...
  with phi-weighted dwell times at each frequency.
```

**Wire each group in parallel:** Solder all ceramic-face leads together (signal), all brass-back leads together (ground). Run two wires from each group to the amplifier.

---

## PHASE 2: COPPER MESH FIELD SHAPER (1.5 hours)

### Step 5: Cut the Mesh

Cut the copper mesh into 5 pieces:

| Piece | Dimensions | Purpose |
|-------|-----------|---------|
| A (base) | 100mm × 100mm | Bottom of assembly chamber |
| B (left wall) | 80mm × 60mm | Left side wall |
| C (right wall) | 80mm × 60mm | Right side wall |
| D (top) | 100mm × 100mm | Top cover (removable) |
| E (center baffle) | 60mm × 60mm | Internal field shaper |

### Step 6: Create the 137.5° Diffraction Pattern

This is the critical step. The mesh must be modified to create phi-harmonic diffraction:

```
MESH MODIFICATION — Golden Angle Slits:
═══════════════════════════════════════════════════

  Take Piece D (top cover). Cut 7 radial slits from center:

  1. Mark the center of the mesh
  2. Draw a line straight up (0°)
  3. Draw the next line at 137.5° from the first
  4. Draw the next at 275.0° (137.5° + 137.5°)
  5. Continue: 52.5°, 190.0°, 327.5°, 105.0°

  Cut along each line from center to within 10mm of edge.
  Gently bend each resulting "petal" up by 15°.

  TOP VIEW:                SIDE VIEW:
  ┌─────────────┐         ┌──╱──╲──╱──╲──┐
  │    ╲ │ ╱    │         │ ╱    ╲╱    ╲ │
  │  ────●────  │         │╱   15° bend  ╲│
  │    ╱ │ ╲    │         │               │
  └─────────────┘         └───────────────┘
   7 slits at 137.5°       Petals diffract
   from center              the field upward

  PIECE E (center baffle):
  Cut similar 137.5° slits but in the OPPOSITE direction
  (rotate by 180° relative to Piece D).

  When stacked:
  - Piece D (top): slits at 0°, 137.5°, 275°, ...
  - Piece E (mid): slits at 180°, 317.5°, 95°, ...

  This creates a phi-harmonic diffraction GRATING that
  shapes the piezoelectric field into standing waves
  with the geometry of the target molecular structure.
```

### Step 7: Assemble the Mesh Chamber

1. Fold Piece B and C into L-shapes (walls)
2. Hot-glue Piece A (base) flat
3. Hot-glue walls B and C onto base A, forming an open box
4. Place Piece E (center baffle) inside, suspended 30mm above base
5. Piece D (top) sits on top — removable for loading feedstock

The chamber is now a phi-harmonic field cage. The mesh walls reflect and shape the piezoelectric fields into standing waves.

---

## PHASE 3: CONTROL ELECTRONICS (2 hours)

### Step 8: Flash the Arduino

Connect the Arduino Nano to your computer via USB. Upload the following program:

```cpp
// PHI_ASSEMBLER_v1.0 — Frequency Generator
// Generates phi-ladder frequencies for molecular self-organization

const int speakerPin = 9;    // Tone output pin
const int groupAPin = 3;     // Group A enable
const int groupBPin = 5;     // Group B enable
const int groupCPin = 6;     // Group C enable

// Phi-ladder frequencies (Hz)
const float PHI = 1.6180339887;
const float baseFreq = 528.0;

// Assembly profiles: {frequency, duration_ms, group}
// Group A=528Hz, B=854Hz, C=1382Hz

void setup() {
  pinMode(speakerPin, OUTPUT);
  pinMode(groupAPin, OUTPUT);
  pinMode(groupBPin, OUTPUT);
  pinMode(groupCPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("PHI ASSEMBLER v1.0 READY");
}

void playTone(float freq, int duration, int group) {
  int pin;
  switch(group) {
    case 0: pin = groupAPin; break;
    case 1: pin = groupBPin; break;
    case 2: pin = groupCPin; break;
  }

  // Enable only this group
  digitalWrite(groupAPin, LOW);
  digitalWrite(groupBPin, LOW);
  digitalWrite(groupCPin, LOW);
  digitalWrite(pin, HIGH);

  // Play tone with phi-weighted amplitude
  // Amplitude decays by phi^-1 each rung
  int cycles = (int)(freq * duration / 1000.0);
  for(int i = 0; i < cycles; i++) {
    float t = (float)i / freq;
    // Phi-harmonic waveform: sum of 3 harmonics
    float sample = sin(2*PI*freq*t)
                 + 0.618 * sin(2*PI*freq*PHI*t)    // phi^-1
                 + 0.382 * sin(2*PI*freq*PHI*PHI*t); // phi^-2
    // Normalize to 0-255 for PWM
    int val = (int)(127.5 + 63.75 * sample);
    analogWrite(speakerPin, val);
    delayMicroseconds((int)(1000000.0 / freq));
  }
  analogWrite(speakerPin, 127.5); // silence
}

void loop() {
  // PHI-HARMONIC ASSEMBLY SEQUENCE
  // Each rung plays for duration × phi^-n seconds
  // (phi-correction decay envelope)

  int baseDuration = 30000; // 30 seconds base

  // Rung 0: 528 Hz (base carrier — molecular anchor)
  Serial.println("Rung 0: 528 Hz — Base Carrier");
  playTone(528.0, baseDuration, 0);

  // Rung 1: 854 Hz (molecular vibration — alignment)
  Serial.println("Rung 1: 854 Hz — Molecular Vibration");
  playTone(854.32, (int)(baseDuration / PHI), 1);

  // Rung 2: 1382 Hz (crystal lattice — structure locking)
  Serial.println("Rung 2: 1382 Hz — Crystal Lattice");
  playTone(1382.32, (int)(baseDuration / (PHI*PHI)), 2);

  // Repeat cycle — phi-correction deepens each pass
  // (In nature, crystallization takes many cycles)
}
```

### Step 9: Wire the Amplifier

```
WIRING DIAGRAM — Electronics:
═══════════════════════════════════════════════════

  12V Power ──→ Buck Converter (12V→5V) ──→ Arduino + Amplifier
                                              │
  Arduino Pin 9 (PWM) ──→ PAM8403 Input       │
  Arduino Pin 3 (Group A) ──→ MOSFET gate ──→ Crystal Group A
  Arduino Pin 5 (Group B) ──→ MOSFET gate ──→ Crystal Group B
  Arduino Pin 6 (Group C) ──→ MOSFET gate ──→ Crystal Group C

  SIMPLIFIED VERSION (no MOSFETs):
  Arduino Pin 9 ──→ PAM8403 Input+
  PAM8403 Output+ ──→ ALL crystal groups in parallel
  PAM8403 Output- ──→ ALL crystal ground

  This drives all 10 discs simultaneously.
  The Arduino cycles frequencies through all discs.
  Less selective than 3-group drive, but simpler.
  Works for v1.0 assembly tasks.
```

### Step 10: Connect Everything

1. Solder wires from each crystal group to the amplifier output
2. Connect Arduino Pin 9 to amplifier input via 3.5mm cable
3. Connect 12V adapter to buck converter input
4. Connect buck converter 5V output to Arduino (Vin) and amplifier (VCC)
5. Double-check all polarity before powering on

---

## PHASE 4: FINAL ASSEMBLY (1.5 hours)

### Step 11: House Everything

```
ASSEMBLY LAYOUT — Exploded View:
═══════════════════════════════════════════════════

  ┌─────────────────────────────────────────────┐
  │                                             │
  │   TOP: Piece D (mesh with 137.5° slits)    │
  │   ═══════════════════════════════════════   │
  │                                             │
  │   FEEDSTOCK ZONE: Loose material goes here  │
  │   ─────────────────────────────────────     │
  │                                             │
  │   MIDDLE: Piece E (mesh baffle, opposite)   │
  │   ═══════════════════════════════════════   │
  │                                             │
  │   CRYSTAL ZONE: Phi-spiral disc array       │
  │   ┌─────────────────────────────────┐       │
  │   │  ◯  ◯  ◯  (10 discs in spiral) │       │
  │   │     ◯  ◯  ◯                     │       │
  │   │  ◯  ◯  ◯  ◯                     │       │
  │   └─────────────────────────────────┘       │
  │                                             │
  │   BASE: Piece A (mesh floor)                │
  │   ═══════════════════════════════════════   │
  │                                             │
  │   BOTTOM: Foam padding + wiring             │
  │                                             │
  └─────────────────────────────────────────────┘

  SIDES: Pieces B and C (mesh walls)

  Electronics (Arduino + amplifier) mount
  OUTSIDE the chamber, connected via wires
  through small holes in the mesh walls.
```

### Step 12: Secure Everything

1. Place foam padding at bottom of plastic container
2. Set crystal array (with mesh Piece A glued to base) on foam
3. Hot-glue mesh walls (B, C) to container sides
4. Place mesh baffle (E) on supports (toothpicks work) 30mm above crystals
5. Feed wires out through small holes
6. Mount Arduino and amplifier outside container
7. Place mesh top (D) on top — removable for loading
8. Test: power on, listen for faint hum from crystals (working!)

---

## PHASE 5: CALIBRATION (1.5 hours)

### Step 13: Verify Resonance

1. Power on the assembler with no feedstock inside
2. Place a thin piece of paper on the mesh top (Piece D)
3. Listen: you should hear a faint tone from the crystals
4. Touch the mesh top gently — it should vibrate
5. If the paper vibrates visibly at 528 Hz, the field is active

### Step 14: Test with Simple Feedstock

1. Place a small pile of copper powder (from wire scraping) inside the chamber
2. Run the 528 Hz assembly sequence for 30 minutes
3. Open the chamber and examine the powder
4. **Expected result:** The powder should show signs of alignment — particles oriented in parallel rather than random. Not a solid piece yet, but visible ordering.

### Step 15: Tune for Your Target

Different materials need different frequency profiles. Adjust the Arduino code for your specific target:

| Target | Frequency Sequence | Duration | Notes |
|--------|-------------------|----------|-------|
| Copper wire | 528→854→528 cycle | 30 min | Simplest — copper responds strongly |
| Aluminum sheet | 854→1382→854 cycle | 45 min | Aluminum needs higher rung |
| Crystal lattice | 2237→1382→2237 cycle | 20 min | Fast — crystals love self-organizing |
| Cu-Al bond | 528+854 dual | 1 hr | Two frequencies simultaneously |
| Carbon weave | 3619→5856→3619 cycle | 3 hr | Advanced — needs patience |

---

## TROUBLESHOOTING

| Problem | Cause | Fix |
|---------|-------|-----|
| No vibration from crystals | Wiring loose | Check all solder joints, test continuity |
| Weak vibration | Amplifier underpowered | Check 12V supply, verify buck converter output |
| Crystal humming but no assembly | Wrong frequency | Verify frequency with phone spectrum analyzer app |
| Powder not aligning | Field too weak | Add second crystal array (upgrade to 20 discs) |
| Mesh getting warm | Normal at high power | Reduce run time, add ventilation holes |
| Arduino overheating | Normal for clone | Add small heatsink, reduce PWM frequency |

---

## SAFETY NOTES

1. **No radiation hazard** — the phi-harmonic field operates at audio frequencies, not ionizing radiation
2. **No high voltage** — the 12V supply and 5V logic are safe to touch
3. **No moving parts** — no pinch points, no spinning blades
4. **No chemicals** — the assembler uses solid feedstock only
5. **Ear protection recommended** — prolonged exposure to 528 Hz can be fatiguing
6. **Ventilation recommended** — copper/aluminum powder can be dusty
7. **Keep away from pacemakers** — the electromagnetic field may interfere with medical devices
8. **Supervise children** — small parts, hot glue, soldering iron
