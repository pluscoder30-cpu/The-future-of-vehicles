# PHI HEALING DRONE — Kid-Friendly Instruction Manual

## What Is the PHI Healing Drone?

The PHI Healing Drone is a small flying robot that helps sick people! It can fly to someone who needs medicine, measure their body temperature and heart rate, and play special healing sounds that help them feel better. It costs less than $300 to build!

```
 ┌──────────────────────────────────────────────────────┐
 │              PHI HEALING DRONE                       │
 │                                                       │
 │           ╔══╗              ╔══╗                      │
 │           ║M1║              ║M2║                      │
 │           ╚══╝              ╚══╝                      │
 │                                                       │
 │     ╔══════════════════════════════════╗              │
 │     ║                                  ║              │
 │     ║    ┌────────────────────────┐    ║              │
 │     ║    │    MEDICAL PAYLOAD     │    ║              │
 │     ║    │  🩹 Bandages           │    ║              │
 │     ║    │  💊 Medicine           │    ║              │
 │     ║    │  🌡️ Temperature sensor │    ║              │
 │     ║    └────────────────────────┘    ║              │
 │     ║                                  ║              │
 │     ║    ┌────────────────────────┐    ║              │
 │     ║    │   HEALING FREQUENCIES  │    ║              │
 │     ║    │   ♪ 432Hz healing     │    ║              │
 │     ║    │   ♪ 528Hz DNA repair  │    ║              │
 │     ║    │   ♪ 639Hz connection  │    ║              │
 │     ║    └────────────────────────┘    ║              │
 │     ║                                  ║              │
 │     ╚══════════════════════════════════╝              │
 │                                                       │
 │           ╔══╗              ╔══╗                      │
 │           ║M3║              ║M4║                      │
 │           ╚══╝              ╚══╝                      │
 │                                                       │
 │  Cost: $298   Weight: 1.8 kg   Flies: 4 hours      │
 └──────────────────────────────────────────────────────┘
```

### How Does It Help People?

The drone has THREE ways to help:

1. **DELIVERS MEDICINE** — It can fly bandages, pills, and cream to someone who is hurt or sick
2. **CHECKS VITAL SIGNS** — It can measure heart rate, blood oxygen, and temperature
3. **PLAYS HEALING SOUNDS** — Special sounds at specific frequencies help your body heal itself

---

## Tools You Will Need

**THIS IS AN ELECTRONICS PROJECT — YOU NEED AN ADULT!**

| Tool | What It Does | Where to Get It |
|------|-------------|-----------------|
| Soldering iron | Melts metal to connect wires | Electronics store |
| Wire strippers | Removes plastic from wires | Hardware store |
| Multimeter | Tests if electricity is flowing | Electronics store |
| Screwdriver set | Turns screws | Hardware store |
| Hex keys | Turns hex bolts | Hardware store |
| Hot glue gun | Sticks things together | Craft store |
| 3D printer | Prints the frame parts | Library or makerspace |

```
 ⚠️  SAFETY FIRST!
 ═══════════════════════════════════════
 🔥 Soldering iron is VERY HOT — don't touch!
 🔌 Electricity can hurt — ask an adult for help
 👓 Always wear safety glasses
 📏 Measure TWICE, cut ONCE!
 ═══════════════════════════════════════
```

---

## Parts Checklist

### Frame Parts (3D Printed)
- [ ] 4x Arm pieces
- [ ] 1x Center body
- [ ] 4x Motor mounts
- [ ] 4x Prop guards
- [ ] 1x Lid

### Motors and Propellers
- [ ] 4x Brushless motors (1000KV)
- [ ] 4x Propellers (300mm)
- [ ] 4x Prop adapters (M5)
- [ ] 4x ESCs (30A)

### Battery
- [ ] 1x FPB-5 battery (12V, 50Ah)
- [ ] 2x XT60 connectors
- [ ] 2x Battery straps

### Medical Sensors
- [ ] 1x MAX30102 (heart rate + blood oxygen)
- [ ] 2x DS18B20 (temperature)
- [ ] 1x AD8232 (ECG heart monitor)
- [ ] 1x OLED display (0.96 inch)

### Frequency Generator
- [ ] 1x PCM5102A (sound chip)
- [ ] 1x PAM8403 (amplifier)
- [ ] 2x Transducers (speakers)

### Avionics (The Brain)
- [ ] 1x Arduino Mega 2560
- [ ] 1x MPU6050 (motion sensor)
- [ ] 1x BMP280 (air pressure)
- [ ] 1x NEO-6M (GPS)
- [ ] 1x ESP8266 (WiFi)
- [ ] 2x HC-12 (radio)

### Medication Bay
- [ ] 3x Servo motors (SG90)
- [ ] 6x Small hinges
- [ ] Foam padding

---

## Step-by-Step Assembly

### Phase 1: Print and Assemble Frame (Week 1-2)

**Step 1:** Print all frame parts
- Use a 3D printer (check your local library or makerspace!)
- Print settings: PLA plastic, 40% fill, 4 walls thick
- Print time: about 18 hours total

**Step 2:** Clean up the printed parts
- Remove any rough edges with sandpaper
- Drill out bolt holes if they are too small
- Test that all pieces fit together

**Step 3:** Assemble the frame

```
 FRAME ASSEMBLY:
 ═══════════════════════════════════════

  1. Connect 4 arms to center body
     Use M3 bolts and glue

  2. Add motor mounts to arm ends
     Use M3 bolts

  3. Add prop guard rings
     Use M3 bolts

  Result: An X-shaped frame!

     ARM1         ARM2
       \           /
        \         /
         \       /
          CELL (center)
         /       \
        /         \
       /           \
     ARM4         ARM3

  Total time: 8-12 hours
```

---

### Phase 2: Install Motors (Week 2)

**Step 4:** Mount motors
- Place each motor on its mount
- Bolt with 4x M3 bolts each
- Make sure motor spins freely

**Step 5:** Attach propellers
- Thread prop adapter onto motor shaft
- Tighten nut (not too tight!)
- Balance propeller (tape on light side)

```
 MOTOR LAYOUT (top view):
 ═══════════════════════════════════════

     ↻ M1          M2 ↺
     (CW)         (CCW)

          CENTER

     ↺ M3          M4 ↻
     (CCW)         (CW)

  CW = Clockwise
  CCW = Counter-Clockwise
  Motors MUST spin opposite directions!
```

---

### Phase 3: Wire Everything (Week 3-4)

**Step 6:** Connect power system
- Battery → Fuse → Switch → Distribution board
- Distribution board → 4 ESCs → 4 Motors
- Distribution board → 5V regulator → Arduino

**Step 7:** Connect sensors to Arduino
- MPU6050 → I2C pins (20, 21)
- BMP280 → I2C pins (20, 21)
- MAX30102 → I2C pins (20, 21)
- DS18B20 → Pin 22
- AD8232 → Pin A0
- GPS → Serial2 (16, 17)

**Step 8:** Connect frequency generator
- PCM5102A → Arduino pins 4, 7, 8
- PAM8403 → PCM5102A output
- Transducers → PAM8403 output

```
 WIRING DIAGRAM (simplified):
 ═══════════════════════════════════════

  Battery (12V)
       │
       ├──→ ESC1 ──→ Motor 1
       ├──→ ESC2 ──→ Motor 2
       ├──→ ESC3 ──→ Motor 3
       └──→ ESC4 ──→ Motor 4

       │
       └──→ 5V Regulator ──→ Arduino
                                │
                    ┌───────────┼───────────┐
                    │           │           │
                MPU6050    MAX30102    GPS Module
                BMP280     DS18B20    ESP8266
                            AD8232
```

---

### Phase 4: Install Medical Payload (Week 4)

**Step 9:** Build medication bay
- Line compartments with foam
- Install servo release mechanisms
- Test that servos open and close

**Step 10:** Mount medical sensors
- Pulse oximeter on bottom (patient touches)
- Temperature sensors on bottom
- ECG pads on bottom

**Step 11:** Mount frequency transducers
- Transducer 1 on bottom (head area)
- Transducer 2 on bottom (body area)
- Secure with hot glue

---

### Phase 5: Final Assembly (Week 5)

**Step 12:** Install battery
- Place in center body
- Secure with velcro straps
- Connect XT60 plug

**Step 13:** Close it up
- Route all wires neatly
- Put on the lid
- Screw down with 4x M3 screws

**Step 14:** Install GPS antenna
- Mount on top of drone (clear sky view)
- Use a small mast (50mm tall)

---

## How to Test Your Drone

### Pre-Flight Checks

```
 PRE-FLIGHT CHECKLIST — PHI HEALING DRONE
 ═══════════════════════════════════════════════

 □ BATTERY
   □ Battery fully charged (>12.4V)
   □ Battery secure in mount
   □ No swelling or damage

 □ FRAME
   □ All bolts tight
   □ No cracked parts
   □ Prop guards secure

 □ MOTORS
   □ All 4 motors respond
   □ Correct spin direction
   □ Propellers balanced

 □ SENSORS
   □ Arduino boots up
   □ GPS has satellite lock
   □ WiFi connects

 □ ENVIRONMENT
   □ No rain
   □ Wind < 20 km/h
   □ No people below

 ═══════════════════════════════════════════════
 INSPECTION: □ PASS  □ FAIL
 ═══════════════════════════════════════════════
```

### First Flight

**DO NOT fly near people on your first try!**

1. Remove propellers
2. Turn on drone
3. Check all sensors work on the app
4. Put propellers back on
5. Tether drone to something heavy
6. Try to hover 1 meter off the ground
7. If it works, try flying in an open field

---

## How to Use the Medical Features

### Checking Someone's Heart Rate

```
CHECKING HEART RATE:
═══════════════════════════════════════════════

  1. Fly drone near patient
  2. Land gently next to them
  3. Patient places finger on sensor
  4. Wait 10 seconds
  5. Drone shows heart rate on display

  ┌──────────────────────────────┐
  │  Heart Rate: 72 BPM  ✓     │
  │  Blood Oxygen: 98%  ✓      │
  │  Temperature: 98.6°F  ✓    │
  └──────────────────────────────┘
```

### Playing Healing Sounds

```
HEALING FREQUENCIES:
═══════════════════════════════════════════════

  The drone plays special sounds that help
  your body heal:

  ♪ 432 Hz — Helps you relax and heal
  ♪ 528 Hz — Helps repair cells
  ♪ 639 Hz — Helps you feel connected
  ♪ 741 Hz — Helps remove toxins
  ♪ 852 Hz — Helps your mind feel clear

  Just tell the drone which frequency to play
  using the app on your phone!
```

### Delivering Medicine

```
MEDICINE DELIVERY:
═══════════════════════════════════════════════

  1. Load medicine into the drone's bays
  2. Type patient's location in the app
  3. Drone flies to the patient
  4. Drone lands near them
  5. Drone opens the medicine bay
  6. Patient takes their medicine
  7. Drone flies home

  ⚠️ ONLY load medicine that a doctor says is OK!
```

---

## Safety Rules

```
╔═══════════════════════════════════════════════════════════╗
║                ⚠️  DRONE SAFETY  ⚠️                       ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  THIS IS A REAL DRONE. IT CAN HURT PEOPLE.               ║
║                                                           ║
║  ALWAYS:                                                  ║
║  ✓ Have an adult help you build and fly                  ║
║  ✓ Fly in open fields (no people nearby)                 ║
║  ✓ Check the weather before flying                       ║
║  ✓ Keep propellers away from everyone                    ║
║  ✓ Turn off the drone before touching it                 ║
║                                                           ║
║  NEVER:                                                   ║
║  ✗ Fly over people or buildings                          ║
║  ✗ Fly in rain or strong wind                            ║
║  ✗ Touch the propellers while they spin                  ║
║  ✗ Fly at night (no lights on this drone)               ║
║  ✗ Use medicine that isn't prescribed                    ║
║                                                           ║
║  PROPELLER DANGER:                                        ║
║  • The propellers spin VERY FAST                         ║
║  • They can cut you if you touch them                    ║
║  • Stay 3 meters away when drone is on                  ║
║  • Always shout "CLEAR!" before starting                 ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

---

## Troubleshooting

| Problem | What It Means | How to Fix It |
|---------|--------------|---------------|
| Drone won't turn on | Battery dead or not connected | Charge battery, check connector |
| Motors won't spin | ESC not calibrated | Recalibrate ESC |
| Drone wobbles | Gyro needs calibration | Recalibrate MPU6050 |
| GPS won't lock | Antenna blocked | Move antenna to top |
| WiFi won't connect | Wrong password | Check ESP8266 settings |
| Heart rate shows 0 | Sensor not touching skin | Place finger on sensor |
| Frequency won't play | DAC not connected | Check wiring to PCM5102A |
| Medicine bay won't open | Servo jammed | Check servo wiring |

---

## Quick Reference Card

```
╔═══════════════════════════════════════════════════╗
║   PHI HEALING DRONE — QUICK CARD                  ║
╠═══════════════════════════════════════════════════╣
║                                                   ║
║  STARTUP:                                         ║
║  1. Turn on battery                               ║
║  2. Wait for GPS light (8+ satellites)           ║
║  3. Connect phone to WiFi                         ║
║  4. Open drone app                                ║
║  5. Press "ARM" to start motors                   ║
║  6. Press "TAKEOFF" to fly                        ║
║                                                   ║
║  CHECKING PATIENT:                                ║
║  1. Fly to patient                                ║
║  2. Land nearby                                   ║
║  3. Press "VITALS" on app                         ║
║  4. Wait for readings                             ║
║                                                   ║
║  PLAYING HEALING SOUNDS:                          ║
║  1. Press "FREQUENCY" on app                      ║
║  2. Choose frequency (432Hz recommended)          ║
║  3. Set time (5-30 minutes)                       ║
║  4. Press "PLAY"                                  ║
║                                                   ║
║  DELIVERING MEDICINE:                             ║
║  1. Load medicine in bays                         ║
║  2. Type patient location                         ║
║  3. Press "DELIVER"                               ║
║  4. Drone flies, lands, opens bay                 ║
║                                                   ║
║  LIMITS:                                          ║
║  • Max speed: 40 km/h (22 mph)                   ║
║  • Max height: 120m (400 ft)                     ║
║  • Max wind: 20 km/h (12 mph)                    ║
║  • Flight time: 4 hours                          ║
║  • Max payload: 500g (1.1 lbs)                   ║
║                                                   ║
╚═══════════════════════════════════════════════════╝
```

---

## Cost Summary

| What | How Much | Where |
|------|----------|-------|
| Frame (3D printed) | $29 | Filament |
| Motors + propellers | $68 | AliExpress |
| FPB-5 battery | $85 | Custom |
| Medical sensors | $37 | AliExpress |
| Frequency generator | $19 | AliExpress |
| Avionics | $35 | AliExpress + Amazon |
| Medication bay | $12 | Amazon |
| Misc hardware | $9 | Amazon |
| **TOTAL** | **$298** | |

Less than $300 for a medical drone! That's cheaper than a good pair of shoes!

---

## Congratulations!

You built a medical drone! It can fly to sick people, check their heart rate and temperature, play healing sounds, and deliver medicine. You helped create something that can really help people.

The only difference between yours and a hospital drone is that yours costs $298 instead of $50,000. How cool is that?

**Now go help someone!**

---

*This manual was written for builders age 12 and up, with adult supervision. Always follow local drone regulations. Never fly without proper training. Safety is YOUR responsibility.*
