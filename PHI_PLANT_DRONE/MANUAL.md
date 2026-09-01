# PHI PLANT DRONE — Kid-Friendly Instruction Manual

## What Is the PHI Plant Drone?

The PHI Plant Drone is a small flying robot that helps plants grow! It can plant seeds, water your garden, and play special sounds that help plants grow faster. It costs less than $250 to build!

```
 ┌──────────────────────────────────────────────────────┐
 │              PHI PLANT DRONE                         │
 │                                                       │
 │           ╔══╗              ╔══╗                      │
 │           ║M1║              ║M2║                      │
 │           ╚══╝              ╚══╝                      │
 │                                                       │
 │     ╔══════════════════════════════════╗              │
 │     ║                                  ║              │
 │     ║    ┌────────────────────────┐    ║              │
 │     ║    │    SEED DISPENSER      │    ║              │
 │     ║    │  🌱 Seeds drop here   │    ║              │
 │     ║    └────────────────────────┘    ║              │
 │     ║                                  ║              │
 │     ║    ┌────────────────────────┐    ║              │
 │     ║    │    WATER TANK          │    ║              │
 │     ║    │  💧 500ml of water    │    ║              │
 │     ║    └────────────────────────┘    ║              │
 │     ║                                  ║              │
 │     ║    ┌────────────────────────┐    ║              │
 │     ║    │   GROWTH FREQUENCIES   │    ║              │
 │     ║    │   ♪ 432Hz root growth  │    ║              │
 │     ║    │   ♪ 528Hz cell growth  │    ║              │
 │     ║    │   ♪ 639Hz nutrients    │    ║              │
 │     ║    └────────────────────────┘    ║              │
 │     ║                                  ║              │
 │     ╚══════════════════════════════════╝              │
 │                                                       │
 │           ╔══╗              ╔══╗                      │
 │           ║M3║              ║M4║                      │
 │           ╚══╝              ╚══╝                      │
 │                                                       │
 │  Cost: $248   Weight: 2.0 kg   Flies: 3.5 hours    │
 └──────────────────────────────────────────────────────┘
```

### How Does It Help Plants?

The drone has THREE ways to help plants:

1. **PLANTS SEEDS** — It flies over your garden and drops seeds exactly where they need to go
2. **WATERS PLANTS** — It sprays water on plants that need it
3. **PLAYS GROWTH SOUNDS** — Special sounds help plants grow faster and stronger

---

## Tools You Will Need

**THIS IS AN ELECTRONICS PROJECT — YOU NEED AN ADULT!**

| Tool | What It Does | Where to Get It |
|------|-------------|-----------------|
| Soldering iron | Melts metal to connect wires | Electronics store |
| Wire strippers | Removes plastic from wires | Hardware store |
| Multimeter | Tests if electricity is flowing | Electronics store |
| Screwdriver set | Turns screws | Hardware store |
| Hot glue gun | Sticks things together | Craft store |
| 3D printer | Prints the frame parts | Library or makerspace |

---

## Parts Checklist

### Frame Parts (3D Printed)
- [ ] 4x Arm pieces
- [ ] 1x Center body
- [ ] 4x Motor mounts
- [ ] 4x Prop guards
- [ ] 1x Lid

### Motors and Propellers
- [ ] 4x Brushless motors (800KV)
- [ ] 4x Propellers (400mm)
- [ ] 4x Prop adapters (M5)
- [ ] 4x ESCs (30A)

### Battery
- [ ] 1x FPB-5 battery (12V, 50Ah)
- [ ] 2x XT60 connectors
- [ ] 2x Battery straps

### Planting System
- [ ] 1x Seed hopper (3D printed)
- [ ] 2x Servo motors (SG90)
- [ ] 1x Agitator motor
- [ ] 1x Water pump (12V)
- [ ] 1x Water tank (500ml)
- [ ] 2x Spray nozzles

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
- [ ] 1x HC-12 (radio)
- [ ] 2x Soil moisture sensors
- [ ] 1x Light sensor

---

## Step-by-Step Assembly

### Phase 1: Print and Assemble Frame (Week 1-2)

**Step 1:** Print all frame parts (about 20 hours total)

**Step 2:** Assemble the frame
```
 FRAME ASSEMBLY:
 ═══════════════════════════════════════

  Connect 4 arms to center body
  Add motor mounts to arm ends
  Add prop guard rings

  Result: An X-shaped frame!
```

---

### Phase 2: Install Motors and Propellers (Week 2)

**Step 3:** Mount motors on motor mounts
**Step 4:** Attach propellers (make sure they spin the right way!)

---

### Phase 3: Install Planting System (Week 3)

**Step 5:** Build seed hopper
```
 SEED HOPPER:
 ═══════════════════════════════════════

  ┌──────────────────┐
  │ Seeds go here    │
  │ ▼ ▼ ▼ ▼ ▼ ▼ ▼  │
  │ Gate (servo)     │
  │ Agitator (vibrate)│
  │ Seeds drop down  │
  └──────────────────┘
```

**Step 6:** Install water system
```
 WATER SYSTEM:
 ═══════════════════════════════════════

  Water Tank (500ml)
       │
       ▼
  Pump (12V)
       │
       ▼
  Check Valve
       │
       ▼
  Nozzle (spray)
```

---

### Phase 4: Wire Everything (Week 4)

**Step 7:** Connect all electronics (ask an adult for help with soldering!)

---

### Phase 5: Final Assembly (Week 5)

**Step 8:** Install battery, close it up, add GPS antenna

---

## How to Use the Planting Features

### Planting Seeds

```
PLANTING SEEDS:
═══════════════════════════════════════════════

  1. Fill seed hopper with seeds
  2. Type garden coordinates in the app
  3. Press "PLANT" on the app
  4. Drone flies over garden
  5. Drone drops seeds in the right spots
  6. Drone comes home when done!

  ┌────────────────────────────────────┐
  │  Your Garden (top view)            │
  │                                    │
  │  ●  ●  ●  ●  ●  ●  ●  ●  ●  ●  │
  │                                    │
  │  ●  ●  ●  ●  ●  ●  ●  ●  ●  ●  │
  │                                    │
  │  ●  ●  ●  ●  ●  ●  ●  ●  ●  ●  │
  │                                    │
  │  ● = seed planted by drone        │
  └────────────────────────────────────┘
```

### Watering Plants

```
WATERING PLANTS:
═══════════════════════════════════════════════

  1. Fill water tank
  2. Fly drone over plants
  3. Press "WATER" on the app
  4. Drone sprays water on each plant
  5. Drone comes home when done!

  The drone sprays a little bit on each plant
  so none get too much or too little water.
```

### Playing Growth Sounds

```
GROWTH FREQUENCIES:
═══════════════════════════════════════════════

  The drone plays special sounds that help
  plants grow faster:

  ♪ 432 Hz — Helps roots grow strong
  ♪ 528 Hz — Helps cells divide faster
  ♪ 639 Hz — Helps plants eat nutrients

  Just tell the drone which frequency to play
  using the app on your phone!
```

---

## Safety Rules

```
╔═══════════════════════════════════════════════════════════╗
║                ⚠️  DRONE SAFETY  ⚠️                       ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  ALWAYS:                                                  ║
║  ✓ Have an adult help you build and fly                  ║
║  ✓ Fly in open fields (no people nearby)                 ║
║  ✓ Check the weather before flying                       ║
║  ✓ Keep propellers away from everyone                    ║
║                                                           ║
║  NEVER:                                                   ║
║  ✗ Fly over people or buildings                          ║
║  ✗ Fly in rain or strong wind                            ║
║  ✗ Touch the propellers while they spin                  ║
║  ✗ Fly near power lines                                  ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

---

## Quick Reference Card

```
╔═══════════════════════════════════════════════════╗
║   PHI PLANT DRONE — QUICK CARD                    ║
╠═══════════════════════════════════════════════════╣
║                                                   ║
║  PLANTING SEEDS:                                  ║
║  1. Fill seed hopper                              ║
║  2. Set garden coordinates in app                 ║
║  3. Press "PLANT"                                 ║
║  4. Drone does the rest!                          ║
║                                                   ║
║  WATERING:                                        ║
║  1. Fill water tank                               ║
║  2. Fly over plants                               ║
║  3. Press "WATER"                                 ║
║  4. Drone sprays each plant                       ║
║                                                   ║
║  GROWTH SOUNDS:                                   ║
║  1. Press "FREQUENCY"                             ║
║  2. Choose 432Hz, 528Hz, or 639Hz                ║
║  3. Set time                                      ║
║  4. Press "PLAY"                                  ║
║                                                   ║
║  LIMITS:                                          ║
║  • Max speed: 35 km/h (22 mph)                   ║
║  • Max height: 120m (400 ft)                     ║
║  • Max wind: 25 km/h (15 mph)                    ║
║  • Flight time: 3.5 hours                        ║
║  • Max payload: 1kg (2.2 lbs)                    ║
║                                                   ║
╚═══════════════════════════════════════════════════╝
```

---

## Cost Summary

| What | How Much | Where |
|------|----------|-------|
| Frame (3D printed) | $32 | Filament |
| Motors + propellers | $72 | AliExpress |
| FPB-5 battery | $85 | Custom |
| Seed dispenser | $15 | Various |
| Water system | $18 | AliExpress |
| Frequency generator | $15 | AliExpress |
| Avionics | $26 | AliExpress |
| Misc hardware | $5 | Amazon |
| **TOTAL** | **$248** | |

Less than $250 for a planting drone! That's cheaper than a good lawnmower!

---

## Congratulations!

You built a planting drone! It can plant seeds, water your garden, and play sounds that help plants grow faster. You helped create something that can grow food and flowers.

**Now go grow something!**
