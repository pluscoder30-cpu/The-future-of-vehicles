# PHI FOOD DRONE — ASSEMBLY GUIDE

## Step-by-Step Build Instructions

---

## TOOLS REQUIRED

| Tool | Purpose | Cost |
|------|---------|------|
| Soldering iron | Solder connections | $15 |
| Wire strippers | Strip insulation | $8 |
| Multimeter | Test voltages | $12 |
| Hex keys | Bolt tightening | $8 |
| Screwdrivers | Assembly | $10 |
| Hot glue gun | Secure components | $8 |
| 3D printer | Print frame | $0-200 |

---

## PHASE 1: FRAME (8-10 hours)

### Step 1: Print Frame Parts
- Material: PLA 1.75mm
- Infill: 50% gyroid
- Total print time: ~20 hours

### Step 2: Assemble Frame
1. Connect 4 arms to center body with M3 bolts
2. Install motor mounts on arm ends
3. Install prop guards

---

## PHASE 2: MOTORS (4-6 hours)

### Step 3: Mount Motors
1. Place motor on mount
2. Secure with 4x M3 bolts
3. Verify spin direction

### Step 4: Attach Propellers
1. Thread prop adapter
2. Attach propeller
3. Balance propeller

---

## PHASE 3: SEED SYSTEM (4-6 hours)

### Step 5: Build Seed Dispenser

```
SEED DISPENSER ASSEMBLY:
═══════════════════════════════════════════════════════════════

  1. Print 3 seed hoppers
  2. Install servo on each gate
  3. Connect agitator motors
  4. Mount in center body
  5. Test each channel separately

  ┌────────────────────────────────────┐
  │  Load herb seeds → Test drop       │
  │  Load veg seeds → Test drop        │
  │  Load flower seeds → Test drop     │
  └────────────────────────────────────┘
```

---

## PHASE 4: NUTRIENT SYSTEM (3-4 hours)

### Step 6: Install Nutrient Tank
1. Mount tank in center body
2. Install pump below tank
3. Connect tubing to nozzle
4. Test pump with water

---

## PHASE 5: ELECTRONICS (8-10 hours)

### Step 7: Wire Power System
1. Install fuse and switch
2. Connect ESCs to power distribution
3. Install 5V and 3.3V regulators

### Step 8: Wire Arduino and Sensors
Follow pin allocation in `04_CIRCUIT.md`

### Step 9: Wire Frequency Generator
1. Connect PCM5102A to Arduino
2. Connect amplifier
3. Mount transducers on bottom

---

## PHASE 6: FINAL ASSEMBLY (4-6 hours)

### Step 10: Install Battery
1. Place FPB-5 in center body
2. Secure with velcro straps
3. Connect XT60

### Step 11: Close and Test
1. Route wires neatly
2. Attach lid
3. Full system test

---

## PHASE 7: TESTING (4-6 hours)

### Pre-Power Check

```
PRE-POWER CHECKLIST:
═══════════════════════════════════════════════════════════════

  □ No short circuits
  □ Battery voltage > 12.0V
  □ All connectors secure
  □ Propellers removed
  □ Water system empty
  □ Seeds loaded for test

  □ PASS / □ FAIL
```

### System Tests
1. Motor spin test
2. Seed dispenser test
3. Nutrient pump test
4. Frequency generator test
5. GPS lock test
6. WiFi connection test

### Flight Test
1. Tethered hover
2. GPS hold test
3. Seed drop test (in test area)
4. Nutrient spray test
