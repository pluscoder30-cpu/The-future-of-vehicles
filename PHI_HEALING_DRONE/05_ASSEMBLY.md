# PHI HEALING DRONE — ASSEMBLY GUIDE

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
| Needle-nose pliers | Bend wires | $6 |
| Heat gun | Shrink tubing | $12 |

---

## PHASE 1: FRAME ASSEMBLY (8-12 hours)

### Step 1: Print Frame Parts

Print all frame components using these settings:
- Material: PLA 1.75mm
- Layer height: 0.2mm
- Infill: 40% gyroid
- Walls: 4 perimeters
- Top/Bottom: 5 layers
- Supports: Yes (for overhangs > 45°)

**Print Time Estimate:**
- 4x Arm: 2 hours each = 8 hours
- 1x Center body: 4 hours
- 4x Motor mount: 30 min each = 2 hours
- 4x Prop guard: 45 min each = 3 hours
- 1x Lid: 1 hour
- **Total: ~18 hours print time**

### Step 2: Clean and Prepare Parts

1. Remove all supports with pliers
2. Sand rough edges with 200-grit sandpaper
3. Test fit all joints
4. Drill out any tight bolt holes (M3 drill bit)
5. Dry-fit complete frame before gluing

### Step 3: Assemble Arms to Center Body

```
ARM ATTACHMENT:
═══════════════════════════════════════════════════════════════

  1. Apply CA glue to arm joint surfaces
  2. Insert arm into center body slot
  3. Align arm to 45° from body axis
  4. Secure with 2x M3 bolts (10mm)
  5. Apply thread locker to bolt threads
  6. Repeat for all 4 arms

  ┌──────────────────────────────────────┐
  │                                      │
  │         ARM1    ARM2                 │
  │           ╲    ╱                     │
  │            ╲  ╱                      │
  │             ╲╱                       │
  │     ARM4 ──CELL── ARM3              │
  │             ╱╲                       │
  │            ╱  ╲                      │
  │           ╱    ╲                     │
  │                                      │
  └──────────────────────────────────────┘

  CRITICAL: Arms must be exactly 45° apart
  for proper flight balance.
```

### Step 4: Install Motor Mounts

1. Slide motor mount onto arm end
2. Align mount holes with arm holes
3. Secure with 2x M3 bolts
4. Apply thread locker
5. Verify mount is perpendicular to arm

### Step 5: Install Prop Guards

1. Slide prop guard ring over motor mount
2. Align with mounting tabs
3. Secure with 1x M3 bolt per guard
4. Verify 25mm clearance from prop tips

---

## PHASE 2: MOTOR INSTALLATION (4-6 hours)

### Step 6: Mount Motors

```
MOTOR INSTALLATION:
═══════════════════════════════════════════════════════════════

  1. Place motor on mount (shaft up)
  2. Align motor holes with mount holes
  3. Insert 4x M3 bolts (8mm) from bottom
  4. Secure with M3 nuts on top
  5. Apply thread locker to all bolts
  6. Verify motor spins freely

  Motor Orientation (TOP VIEW):
  ┌──────────────────────────────────────┐
  │                                      │
  │    M1 (CW)              M2 (CCW)    │
  │      ↻                    ↺          │
  │                                      │
  │              CENTER                  │
  │                                      │
  │    M3 (CCW)              M4 (CW)    │
  │      ↺                    ↻          │
  │                                      │
  └──────────────────────────────────────┘

  M1 and M4 spin clockwise (CW)
  M2 and M3 spin counter-clockwise (CCW)
```

### Step 7: Attach Propellers

1. Thread prop adapter onto motor shaft
2. Tighten adapter nut to 2 N-m torque
3. Slide propeller onto adapter
4. Secure with prop nut
5. Balance propeller (tape on light side)
6. Repeat for all 4 motors

### Step 8: Connect ESCs to Motors

1. Solder 3 motor phase wires to ESC
2. Use heat shrink on each connection
3. Secure ESC to arm with zip ties
4. Route signal wire along arm to center body
5. Leave 50mm slack at center body for service

---

## PHASE 3: ELECTRONICS WIRING (10-14 hours)

### Step 9: Install Power Distribution

```
POWER WIRING SEQUENCE:
═══════════════════════════════════════════════════════════════

  1. Install 30A fuse holder near battery
  2. Connect battery positive to fuse input
  3. Connect fuse output to main switch
  4. Connect switch output to power distribution board
  5. Connect 4x ESC power wires to distribution
  6. Connect battery negative to common ground point
  7. Connect ESC grounds to common ground point

  WIRE ROUTING:
  ┌──────────────────────────────────────┐
  │                                      │
  │  Battery ──→ Fuse ──→ Switch ──→    │
  │                                      │
  │  ┌──→ ESC1 ──→ Motor 1              │
  │  ├──→ ESC2 ──→ Motor 2              │
  │  ├──→ ESC3 ──→ Motor 3              │
  │  └──→ ESC4 ──→ Motor 4              │
  │                                      │
  └──────────────────────────────────────┘
```

### Step 10: Wire Arduino and Sensors

Follow the pin allocation table in `04_CIRCUIT.md`:

1. Mount Arduino Mega on standoffs in center body
2. Connect I2C bus (SDA, SCL) to sensor headers
3. Connect ESC signal wires to PWM pins
4. Connect GPS to Serial2
5. Connect HC-12 to Serial3
6. Connect ESP8266 to SoftwareSerial
7. Connect medical sensors to appropriate pins
8. Connect battery voltage divider to A1
9. Connect current sensor to A2

### Step 11: Wire Frequency Generator

1. Mount PCM5102A DAC module near transducers
2. Connect I2S pins to Arduino
3. Connect DAC output to PAM8403 input
4. Connect amplifier output to transducers
5. Mount transducers on drone body
6. Secure all wires with zip ties

### Step 12: Wire Medication Bay

1. Mount 3 servos in medication bay
2. Connect servo power to 5V rail
3. Connect servo signal wires to Arduino
4. Install release mechanisms on servo horns
5. Test servo operation (0-180°)

---

## PHASE 4: MEDICAL PAYLOAD (6-8 hours)

### Step 13: Install Medical Sensors

```
SENSOR PLACEMENT:
═══════════════════════════════════════════════════════════════

  BOTTOM OF DRONE (patient contact side):

  ┌──────────────────────────────────────┐
  │                                      │
  │   ┌──────┐                ┌──────┐  │
  │   │SpO2  │                │Temp  │  │
  │   │Sensor│                │Sensor│  │
  │   └──────┘                └──────┘  │
  │                                      │
  │          ┌──────────┐               │
  │          │   ECG    │               │
  │          │  Pads    │               │
  │          └──────────┘               │
  │                                      │
  └──────────────────────────────────────┘

  Mount with double-sided foam tape
  Ensure sensors protrude 2-3mm below frame
  for patient contact
```

### Step 14: Install Medication Bay

1. Line bay with foam padding
2. Install medication compartments
3. Mount servo release mechanisms
4. Test release mechanism with dummy payloads
5. Verify smooth operation

### Step 15: Install Frequency Transducers

1. Mount transducer 1 on bottom (head area)
2. Mount transducer 2 on bottom (body area)
3. Connect to amplifier output
4. Secure with hot glue
5. Test at 432Hz (should feel vibration)

---

## PHASE 5: AVIONICS (6-8 hours)

### Step 16: Install Flight Controller

1. Mount Arduino on vibration-dampened standoffs
2. Secure MPU6050 to center of frame (rigid mount)
3. Mount BMP280 with vent to atmosphere
4. Install GPS on mast (50mm above body)
5. Connect all sensors per wiring diagram

### Step 17: Install Communication Systems

1. Mount ESP8266 in center body
2. Route antenna outside frame
3. Mount HC-12 with antenna
4. Install buzzer on frame exterior
5. Test WiFi connection
6. Test telemetry range

### Step 18: Install Display

1. Mount OLED on bottom of drone (patient-visible)
2. Connect to I2C bus
3. Program display to show status:
   - "READY" - drone ready
   - "DELIVERING" - medication in transit
   - "HEALING" - frequency therapy active
   - "RETURNING" - returning to base
   - "LOW BATTERY" - warning

---

## PHASE 6: FINAL ASSEMBLY (4-6 hours)

### Step 19: Install Battery

1. Place battery in center body
2. Secure with velcro straps
3. Connect XT60 connector
4. Verify power LED on Arduino
5. Check voltage reading on display

### Step 20: Close Center Body

1. Route all wires neatly
2. Secure loose wires with zip ties
3. Place lid on center body
4. Install 4x M3 screws
5. Verify no pinched wires

### Step 21: Final Connections

1. Connect all ESC signal wires
2. Connect all sensor wires
3. Connect frequency generator
4. Connect medication servos
5. Verify all connections with multimeter

---

## PHASE 7: TESTING (4-6 hours)

### Step 22: Pre-Power Checks

```
PRE-POWER CHECKLIST:
═══════════════════════════════════════════════════════════════

  □ No short circuits (check with multimeter)
  □ All solder joints solid
  □ No bare wires touching
  □ Battery voltage > 12.0V
  □ All connectors secure
  □ No pinched wires
  □ Propellers removed for initial test
  □ Motors secure
  □ Frame structural integrity OK

  □ PASS / □ FAIL
```

### Step 23: Power-On Test

1. Turn on main switch
2. Verify Arduino boots (LED blinks)
3. Verify sensors initialize
4. Verify WiFi connects
5. Verify telemetry link

### Step 24: Motor Test (No Propellers)

1. Arm motors via remote
2. Test each motor individually
3. Verify correct rotation direction
4. Test throttle response
5. Verify all ESCs respond

### Step 25: Flight Test

1. Install propellers
2. Tether drone for first hover
3. Test hover stability
4. Test position hold
5. Test GPS return-to-home

### Step 26: Medical System Test

1. Test pulse oximeter (own finger)
2. Test temperature sensors
3. Test ECG (own chest)
4. Test frequency generator output
5. Test medication release mechanism
6. Test OLED display

---

## ASSEMBLY TROUBLESHOOTING

| Problem | Cause | Fix |
|---------|-------|-----|
| Motor won't spin | ESC not calibrated | Recalibrate ESC |
| Drone drifts | IMU not calibrated | Recalibrate MPU6050 |
| GPS won't lock | Antenna blocked | Move antenna to top |
| WiFi won't connect | Wrong password | Check ESP8266 config |
| Sensors show 0 | Wiring error | Check I2C connections |
| Frequency no output | DAC not initialized | Check I2S wiring |
| Servo jitters | Noise on signal line | Add 100uF capacitor |
| Low hover time | Battery not fully charged | Charge fully before flight |

---

## WEIGHT CHECKLIST

| Component | Target Weight |
|-----------|---------------|
| Frame | 380g |
| Motors (4x) | 200g |
| ESCs (4x) | 80g |
| Propellers (4x) | 40g |
| Battery (FPB-5) | 850g |
| Arduino + sensors | 60g |
| Medical payload | 120g |
| Frequency generator | 50g |
| Wiring and hardware | 70g |
| **Total** | **1,850g** |

**Target: Under 2,000g (4.4 lbs)**
