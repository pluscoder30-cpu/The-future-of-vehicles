# PHI AI FIRE DRONE — ASSEMBLY GUIDE

## Step-by-Step Build Instructions (AI-Enhanced)

---

## TOOLS REQUIRED

| Tool | Purpose | Cost |
|------|---------|------|
| Soldering iron (40W) | Solder connections | $15 |
| Wire strippers | Strip insulation | $8 |
| Multimeter | Test voltages | $12 |
| Hex key set (M2-M5) | Bolt tightening | $8 |
| Screwdriver set | General assembly | $10 |
| Hot glue gun | Secure components | $8 |
| 3D printer (or service) | Print frame parts | $0-200 |
| Heat gun | Shrink tubing | $12 |
| MicroSD reader | Flash Pi OS | $5 |

---

## PHASE 1: FRAME ASSEMBLY (10-14 hours)

### Step 1: Print Frame Parts

Print all frame components including AI and retardant mounts:
- Material: PLA 1.75mm
- Layer height: 0.2mm
- Infill: 50% gyroid (heavier frame for fire ops)
- Walls: 4 perimeters

**Print Time Estimate: ~24 hours total**

### Step 2: Assemble Frame

1. Connect 4 arms to center body
2. Install motor mounts
3. Install prop guards
4. Mount retardant tank bracket
5. Mount AI processor bracket

---

## PHASE 2: MOTOR INSTALLATION (4-6 hours)

Same as standard fire drone assembly.

---

## PHASE 3: ELECTRONICS WIRING (14-18 hours)

### Step 9: Install Power Distribution

24V system with 5V/3.3V regulators for avionics and AI.

### Step 10: Wire AI Processor

```
AI PROCESSOR INSTALLATION:
═══════════════════════════════════════════════════════════════

  1. Mount Raspberry Pi Zero 2W
  2. Connect 5V power
  3. Connect serial to Arduino
  4. Mount camera for fire visual
  5. Connect thermal sensor (I2C shared)
  6. Flash AI fire prediction model
  7. Test AI inference
```

### Step 11: Wire Retardant System

```
RETARDANT SYSTEM WIRING:
═══════════════════════════════════════════════════════════════

  Arduino Pin 24 ──→ MOSFET Gate (pump control)
  Arduino Pin 25 ───→ Solenoid valve 1
  Arduino Pin 26 ───→ Solenoid valve 2
  Pump power ──────→ 12V bus (via MOSFET)
  Valve power ─────→ 5V bus
```

---

## PHASE 4: THERMAL SYSTEM (4-6 hours)

### Step 12: Install Thermal Camera

1. Mount MLX90614 on bottom (fire-facing)
2. Mount 1080p camera for visual confirmation
3. Connect to I2C bus and Pi camera port
4. Test thermal readings

---

## PHASE 5: AI SOFTWARE (4-6 hours)

### Step 13: Flash AI System

```
AI SOFTWARE SETUP:
═══════════════════════════════════════════════════════════════

  1. Flash Raspberry Pi OS Lite
  2. Install TensorFlow Lite
  3. Install OpenCV
  4. Copy fire prediction model
  5. Configure thermal sensor interface
  6. Set up drone communication protocol
  7. Test AI with simulated fire data
```

---

## PHASE 6: TESTING (6-8 hours)

### Additional AI Tests

```
AI FIRE SYSTEM TESTS:
═══════════════════════════════════════════════════════════════

  □ Thermal camera detects heat source at 10m
  □ AI predicts spread direction correctly
  □ AI recommends drop zone
  □ Retardant pump activates on AI command
  □ Drone swarm communication works
  □ AI coordinates with second drone
  □ Emergency override stops AI
```
