# PHI PLANT DRONE — ASSEMBLY GUIDE

## Step-by-Step Build Instructions

---

## TOOLS REQUIRED

| Tool | Purpose | Cost |
|------|---------|------|
| Soldering iron (40W) | Solder connections | $15 |
| Wire strippers | Strip insulation | $8 |
| Multimeter | Test voltages | $12 |
| Hex key set (M2-M4) | Bolt tightening | $8 |
| Screwdriver set | General assembly | $10 |
| Hot glue gun | Secure components | $8 |
| 3D printer (or service) | Print frame parts | $0-200 |

---

## PHASE 1: FRAME ASSEMBLY (8-10 hours)

### Step 1: Print Frame Parts

Print all frame components:
- Material: PLA 1.75mm
- Layer height: 0.2mm
- Infill: 50% gyroid (heavier payload capacity)
- Walls: 4 perimeters
- Top/Bottom: 5 layers
- **Total print time: ~20 hours**

### Step 2: Assemble Arms to Center Body

1. Apply CA glue to arm joint surfaces
2. Insert arm into center body slot
3. Align arm to 45° from body axis
4. Secure with 2x M3 bolts (10mm)
5. Apply thread locker
6. Repeat for all 4 arms

### Step 3: Install Motor Mounts and Prop Guards

1. Slide motor mount onto arm end
2. Secure with 2x M3 bolts
3. Slide prop guard ring over motor mount
4. Secure with 1x M3 bolt per guard

---

## PHASE 2: MOTOR INSTALLATION (4-6 hours)

### Step 4: Mount Motors

1. Place motor on mount (shaft up)
2. Align motor holes with mount holes
3. Insert 4x M3 bolts (8mm) from bottom
4. Secure with M3 nuts on top
5. Apply thread locker

### Step 5: Attach Propellers

1. Thread prop adapter onto motor shaft
2. Tighten adapter nut to 2 N-m
3. Slide propeller onto adapter
4. Secure with prop nut
5. Balance propeller

---

## PHASE 3: SEED DISPENSER (4-6 hours)

### Step 6: Build Seed Hopper

```
SEED HOPPER ASSEMBLY:
═══════════════════════════════════════════════════════════════

  1. Print hopper (3D file provided)
  2. Clean and smooth interior
  3. Install servo on gate mechanism
  4. Test servo opens/closes gate
  5. Install agitator motor
  6. Test vibration shakes seeds

  ┌────────────────────────────────────┐
  │  HOPPER ASSEMBLY                   │
  │                                    │
  │  ┌──────────────────┐             │
  │  │    HOPPER        │             │
  │  │    (3D printed)  │             │
  │  │                  │             │
  │  │   Seeds go here  │             │
  │  │                  │             │
  │  └────────┬─────────┘             │
  │           │                       │
  │     ┌─────┴─────┐                 │
  │     │   GATE    │                 │
  │     │  (servo)  │                 │
  │     └─────┬─────┘                 │
  │           │                       │
  │     ┌─────┴─────┐                 │
  │     │ AGITATOR  │                 │
  │     └───────────┘                 │
  │                                    │
  └────────────────────────────────────┘
```

### Step 7: Install Seed Dispenser

1. Mount hopper in center body
2. Secure with 4x M3 bolts
3. Connect servo to Arduino Pin 12
4. Connect agitator to Arduino Pin 14
5. Test: load seeds, press button, seeds drop

---

## PHASE 4: WATER SYSTEM (4-6 hours)

### Step 8: Install Water Tank

```
WATER SYSTEM ASSEMBLY:
═══════════════════════════════════════════════════════════════

  1. Mount water tank in center body
  2. Secure with velcro straps
  3. Install pump below tank
  4. Connect tubing: tank → pump → nozzle
  5. Install check valve after pump
  6. Mount nozzle on bottom of drone
  7. Connect pump to relay module
  8. Test: fill tank, activate pump, check spray

  ┌────────────────────────────────────┐
  │  WATER SYSTEM LAYOUT               │
  │                                    │
  │  ┌──────────┐                     │
  │  │  TANK    │                     │
  │  │  500ml   │                     │
  │  └────┬─────┘                     │
  │       │                           │
  │  ┌────┴─────┐                     │
  │  │  PUMP    │                     │
  │  └────┬─────┘                     │
  │       │                           │
  │  ┌────┴─────┐                     │
  │  │  VALVE   │                     │
  │  └────┬─────┘                     │
  │       │                           │
  │  ┌────┴─────┐                     │
  │  │  NOZZLE  │ ← adjustable       │
  │  └──────────┘                     │
  │                                    │
  └────────────────────────────────────┘
```

---

## PHASE 5: ELECTRONICS (8-10 hours)

### Step 9: Install Power Distribution

1. Install 30A fuse holder near battery
2. Connect battery to fuse to switch
3. Connect switch to power distribution
4. Connect ESCs to distribution
5. Install 5V buck regulator
6. Connect Arduino to 5V rail
7. Install 3.3V regulator for ESP8266

### Step 10: Wire Arduino and Sensors

Follow pin allocation in `04_CIRCUIT.md`:
1. Mount Arduino on standoffs
2. Connect I2C bus (MPU6050, BMP280, BH1750, OLED)
3. Connect ESC signal wires
4. Connect GPS to Serial2
5. Connect HC-12 to Serial3
6. Connect ESP8266 to SoftwareSerial
7. Connect soil moisture sensors to A0, A1
8. Connect battery voltage divider to A2

### Step 11: Wire Frequency Generator

1. Mount PCM5102A near transducers
2. Connect I2S pins to Arduino
3. Connect DAC to amplifier
4. Connect amplifier to transducers
5. Mount transducers on bottom of drone

---

## PHASE 6: FINAL ASSEMBLY (4-6 hours)

### Step 12: Install Battery

1. Place FPB-5 in center body
2. Secure with velcro straps
3. Connect XT60 plug
4. Verify power LED on Arduino

### Step 13: Close Center Body

1. Route all wires neatly
2. Secure with zip ties
3. Place lid on body
4. Install 4x M3 screws

### Step 14: Install GPS Antenna

1. Mount on top of drone (clear sky view)
2. Use 50mm mast
3. Secure with hot glue

---

## PHASE 7: TESTING (4-6 hours)

### Step 15: Pre-Power Checks

```
PRE-POWER CHECKLIST:
═══════════════════════════════════════════════════════════════

  □ No short circuits
  □ All solder joints solid
  □ Battery voltage > 12.0V
  □ All connectors secure
  □ Propellers removed for initial test
  □ Motors secure
  □ Water tank empty (no leaks)
  □ Seed hopper empty

  □ PASS / □ FAIL
```

### Step 16: System Tests

1. Power on, verify Arduino boots
2. Test each motor individually
3. Test seed dispenser (dry run)
4. Test water pump (no water first)
5. Test frequency generator
6. Test GPS lock
7. Test WiFi connection
8. Test telemetry link

### Step 17: Flight Test

1. Install propellers
2. Tether drone for first hover
3. Test hover stability
4. Test GPS hold
5. Test position hold

### Step 18: Planting Test

1. Fill seed hopper with test seeds
2. Fly over test area
3. Activate seed dispenser
4. Verify seeds drop correctly
5. Fill water tank
6. Test water spray
7. Verify coverage area

---

## TROUBLESHOOTING

| Problem | Cause | Fix |
|---------|-------|-----|
| Motors won't spin | ESC not calibrated | Recalibrate ESC |
| Drone wobbles | IMU not calibrated | Recalibrate MPU6050 |
| Seeds won't drop | Gate stuck | Lubricate gate, check servo |
| Water won't spray | Pump clogged | Clean pump, check tubing |
| Frequency no output | DAC not initialized | Check I2S wiring |
| GPS won't lock | Antenna blocked | Move antenna to top |

---

## WEIGHT CHECKLIST

| Component | Target Weight |
|-----------|---------------|
| Frame | 502g |
| Motors (4x) | 280g |
| ESCs (4x) | 80g |
| Propellers (4x) | 60g |
| Battery (FPB-5) | 850g |
| Arduino + sensors | 65g |
| Seed dispenser | 80g |
| Water system (empty) | 90g |
| Frequency generator | 50g |
| Wiring and hardware | 80g |
| **Total** | **2,137g** |

**Target: Under 2,500g (5.5 lbs) with full payload**
