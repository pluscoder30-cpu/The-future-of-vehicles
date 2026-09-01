# PHI GOLD SYNTHESIZER — ASSEMBLY GUIDE

## Step-by-Step Build Instructions

---

## PHASE 1: CHASSIS ASSEMBLY (8-12 hours)

### Step 1: Chassis Preparation
```
1. Lay main chassis on flat surface (500×400×600mm)
2. Verify phi-spaced cross members (61.8mm spacing)
3. Drill mounting holes for chamber bracket
4. Install vibration dampeners on bottom (4× Sorbothane feet)
5. Attach fold-down handles to sides (2×)
```

### Step 2: Internal Mounting Points
```
1. Install chamber support bracket (center)
2. Mount resonance coil standoffs (3× phi-spaced)
3. Install battery cradle in side compartment
4. Mount control electronics standoffs (front panel)
5. Install cooling fan mounts (rear panel)
```

### Step 3: Panel Preparation
```
1. Front panel: Cut touchscreen opening (165×100mm)
2. Front panel: Cut status ring opening (80mm diameter)
3. Front panel: Cut button holes (Start/Stop, Mode, E-Stop)
4. Rear panel: Cut IEC inlet opening (48×28mm)
5. Rear panel: Cut exhaust vent opening (65mm diameter)
6. Top panel: Cut hopper opening (85mm diameter)
7. Bottom panel: Cut output valve opening (25mm diameter)
```

---

## PHASE 2: TRANSMUTATION CHAMBER (10-14 hours)

### Step 4: Chamber Assembly
```
1. Install zirconia ceramic liner inside Inconel body
2. Verify liner sits flush (no gaps)
3. Install 4× feedthrough ports on chamber body
4. Install viewport (sapphire, 30mm)
5. Apply graphite gasket to chamber lid rim
6. Test lid seal (finger-tight, then 1/4 turn)
```

### Step 5: Chamber Mounting
```
1. Mount chamber on support bracket (center of chassis)
2. Secure with 4× M6 bolts (phi-spaced pattern)
3. Verify chamber is level (±0.5°)
4. Connect feedthrough ports to internal plumbing
5. Install insulation blanket around chamber
```

### Step 6: Feedstock System
```
1. Mount hopper on top panel (500ml capacity)
2. Install vibratory feeder motor under hopper
3. Connect feedstock funnel from hopper to chamber
4. Install particle size screen (100 mesh)
5. Mount magnetic stirrer inside hopper
6. Test feedstock flow rate (adjust valve)
```

---

## PHASE 3: RESONANCE ARRAY (12-16 hours)

### Step 7: Coil Winding
```
WINDING PROCEDURE FOR EACH COIL:
═══════════════════════════════════════════════════════════════

  COIL 1 (432Hz):
  ──────────────
  Wire: 12 AWG enameled copper
  Turns: 120
  Inner Diameter: 150mm
  Height: 45mm
  Inductance Target: 432μH ±5%
  
  1. Secure ceramic former in lathe
  2. Wind 120 turns, even spacing
  3. Tape every 20 turns with Kapton
  4. Leave 100mm leads
  5. Test inductance with LCR meter
  6. Apply varnish coating

  COIL 2 (699Hz):
  ──────────────
  Wire: 14 AWG enameled copper
  Turns: 93
  Inner Diameter: 150mm
  Height: 35mm
  Inductance Target: 699μH ±5%

  COIL 3 (1131Hz):
  ───────────────
  Wire: 16 AWG enameled copper
  Turns: 75
  Inner Diameter: 150mm
  Height: 28mm
  Inductance Target: 1131μH ±5%
```

### Step 8: Coil Installation
```
1. Mount Coil 1 (432μH) around chamber (outermost)
2. Mount Coil 2 (699μH) around chamber (middle)
3. Mount Coil 3 (1131μH) around chamber (innermost)
4. Verify phi-spaced gaps (15mm between coils)
5. Secure all coils with ceramic brackets
6. Route coil leads to driver boards
```

### Step 9: Driver Board Assembly
```
1. Assemble 3× H-bridge driver boards (IR2110 + IRFP260N)
2. Install gate drive transformers (1:1, 5μH)
3. Mount bootstrap capacitors (1μF ceramic)
4. Connect gate resistors (10Ω)
5. Wire 48V power to each driver
6. Connect PWM signals from ESP32
7. Install current sense resistors (0.01Ω)
```

### Step 10: PLL & Frequency Control
```
1. Build PLL oscillator circuit (CD4046)
2. Set VCO center frequency to 432Hz
3. Connect frequency divider (CD4020)
4. Wire divider outputs to coil drivers:
   - ÷1 → 432Hz (Coil 1)
   - ÷0.618 → 699Hz (Coil 2)
   - ÷0.382 → 1131Hz (Coil 3)
5. Connect feedback from chamber sensors
6. Test PLL lock-on to resonance peak
```

---

## PHASE 4: COOLING SYSTEM (4-6 hours)

### Step 11: Heat Exchanger
```
1. Mount copper heat exchanger on chamber exterior
2. Connect thermal paste between chamber and exchanger
3. Install 2× 120mm cooling fans (rear panel)
4. Route airflow across heat exchanger fins
5. Install exhaust vent with filter
6. Mount thermal fuse on chamber (130°C auto-reset)
```

### Step 12: Temperature Sensors
```
1. Install K-type thermocouple on chamber (feedthrough)
2. Mount NTC thermocouple on coil assembly
3. Mount NTC thermocouple in ambient air
4. Connect all sensors to MAX6675 converter (K-type)
5. Connect NTC sensors to voltage dividers
6. Test all sensor readings on display
```

---

## PHASE 5: GOLD COLLECTION (3-4 hours)

### Step 13: Output System
```
1. Mount collection tray below chamber output
2. Install separator mesh (200 mesh) in tray
3. Connect output funnel from chamber to tray
4. Mount 12V solenoid valve on output line
5. Install discharge chute to catch basin
6. Test output flow rate
```

---

## PHASE 6: CONTROL ELECTRONICS (6-8 hours)

### Step 14: Main Controller
```
1. Mount ESP32-S3 on control PCB
2. Connect I2C bus to display
3. Connect SPI bus to temperature converters
4. Wire current sensor (ACS758) to ADC
5. Wire voltage sensor (ZMPT101B) to ADC
6. Connect relay module (4-channel)
7. Wire status LEDs (6× RGB)
8. Connect piezo buzzer
9. Mount emergency stop button (NC contact)
```

### Step 15: Display & Interface
```
1. Mount 7" touchscreen on front panel
2. Connect to ESP32-S3 via I2C
3. Mount WS2812B status ring (24-LED)
4. Connect to ESP32-S3 via GPIO
5. Mount Start/Stop button (illuminated)
6. Mount Mode selector (3-position rotary)
7. Mount USB-C port (data + 5V power)
8. Test all display elements
```

### Step 16: Power Distribution
```
1. Mount IEC C14 inlet on rear panel
2. Install main fuse holder (60A)
3. Wire DC-DC converter (48V→12V)
4. Connect all 12V circuits to fuse box
5. Wire BMS module to battery
6. Connect all grounds to chassis bus bar
7. Route all cables through wire loom
8. Secure with cable ties (phi-spaced: 61.8mm)
```

---

## PHASE 7: FINAL ASSEMBLY (4-6 hours)

### Step 17: Wiring & Routing
```
1. Connect all remaining wiring
2. Route cables away from heat sources
3. Apply RF shielding copper tape to signal wires
4. Verify all connections with multimeter
5. Check for shorts to chassis
6. DO NOT ENERGIZE until Phase 8 complete
```

### Step 18: Panel Installation
```
1. Install front panel (display + buttons)
2. Install rear panel (inlet + exhaust)
3. Install side panels (battery compartment + ventilation)
4. Install top panel (hopper access)
5. Install bottom panel (output access)
6. Verify all panels are secure
```

### Step 19: Battery Installation
```
1. Slide FPB-5 into side compartment cradle
2. Lock with retention clips
3. Connect HV cables (12mm² orange)
4. Connect BMS CAN bus
5. Verify all connections with multimeter
6. DO NOT ENERGIZE until software loaded
```

### Step 20: Software & Calibration
```
1. Flash ESP32-S3 with firmware
2. Connect to WiFi for configuration
3. Calibrate temperature sensors
4. Calibrate current/voltage sensors
5. Calibrate resonance frequencies (auto-tune)
6. Run self-test sequence
7. Verify gold output quality (99.99%)
```

---

## ASSEMBLY TOOLS REQUIRED

| Tool | Purpose |
|------|---------|
| Torque wrench | Bolt tightening |
| Multimeter | Electrical testing |
| LCR meter | Coil inductance measurement |
| Oscilloscope | Resonance calibration |
| Soldering iron | PCB assembly |
| Wire strippers | Cable preparation |
| Drill press | Panel holes |
| Calipers | Dimensional verification |
| Clamp set | Component holding |
| Heat gun | Heat shrink tubing |
