# PHI Pharmacy Drone - Assembly Guide

> **Difficulty**: Medium | **Time**: ~10 hours | **People needed**: 2

## What You're Building

You're building a drone that delivers medicine to people's homes! It has 20 temperature-controlled slots for different medications, a robotic arm that picks and delivers them, and a barcode scanner to make sure the right medicine goes to the right person.

## Before You Start

**Safety rules:**
- Always wear safety glasses when cutting or soldering
- Never touch the Peltier modules when they're hot
- Keep medications away from the work area during assembly
- If you smell something burning, unplug everything immediately

**Tools you'll need:**
- Hex drivers (2mm, 2.5mm, 3mm)
- Screwdriver set
- Soldering iron + solder
- Wire strippers
- Multimeter
- Thermal paste (for Peltier modules)
- Thermal camera (optional, for checking temperature zones)

---

## Step 1: Build the Frame (1.5 hours)

1. Unpack the carbon fiber quadcopter frame pieces
2. Bolt the 4 motor arms to the center plate
3. Attach the bottom plate to lock everything together
4. Mount the landing gear
5. **Check:** All 4 arms should be the same length. Frame should be lightweight but rigid.

```
    [MOTOR]     [MOTOR]
        \         /
         [CENTER]
        /         \
    [MOTOR]     [MOTOR]
```

## Step 2: Install Motors & Propellers (1 hour)

1. Place one T-Motor F40 Pro II on each arm mount
2. Bolt down with 3 screws per motor
3. Attach one 10-inch carbon propeller to each motor
   - Motors 1, 3 spin **clockwise** (C)
   - Motors 2, 4 spin **counter-clockwise** (CC)
4. **Check:** Spin each prop by hand. They should spin freely.

## Step 3: Wire the ESCs (1.5 hours)

1. Connect one 45A ESC to each motor (3 wires)
2. Solder ESC power wires to the power distribution board
3. Connect each ESC signal wire to the Pixhawk 6C
4. Label every wire: "M1", "M2", "M3", "M4"
5. **Check:** Power on — each motor should respond to the flight controller test

## Step 4: Install the Flight Controllers (1 hour)

1. Mount the Pixhawk 6C in the center of the frame
2. Mount the Safety Processor (STM32F4) nearby
3. Connect the GPS module (UART1)
4. Connect the Safety Processor (UART2)
5. Connect the LTE modem (UART3)
6. Connect the LiDAR (Ethernet)
7. Mount both navigation cameras
8. **Check:** Power on — both controllers should show green LEDs

## Step 5: Install the Battery (30 minutes)

1. Place the FPB-5 battery in the battery bay
2. Secure with straps
3. Connect the main power connector (XT30)
4. **Check:** Battery voltage should read 25.6V on the multimeter

## Step 6: Build the Temperature Control System (2 hours)

This is what keeps medicines at the right temperature!

**Refrigerated Zone (2-8°C):**
1. Install 2 Peltier cooling modules in the refrigerated compartment
   - Apply thermal paste to the hot side before mounting
   - Attach aluminum heat sinks to the hot side
2. Mount 2 cooling fans
3. Install 4 temperature sensors (NTC 10K thermistors)
4. Connect everything to the temperature controller

**Ambient Zone (15-25°C):**
1. Install the 20W heater
2. Install 2 temperature sensors
3. Connect to the temperature controller

**Insulation:**
1. Line both zones with 25mm medical-grade foam
2. Make sure there are no gaps — cold air will escape!

**Check:** Power on. Refrigerated zone should reach 8°C in 5 minutes. Ambient zone should hold 20°C.

## Step 7: Install the Medication Storage System (2 hours)

1. Mount 20 individual storage bins in the drone body
2. Install one RFID reader per slot (20 total)
3. Mount 2 barcode scanners (one for loading, one for dispensing)
4. Install tamper-evident locks on each slot (20 total)
5. Connect all RFID readers to the I2C multiplexer
6. Connect all locks to the I/O expander
7. **Check:** Insert a test RFID tag in each slot. All 20 should be detected.

```
    ┌─────────────────────────────────────┐
    │         MEDICATION STORAGE          │
    │  ┌───┬───┬───┬───┬───┬───┬───┐     │
    │  │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ ← Refrigerated
    │  ├───┼───┼───┼───┼───┼───┼───┤     │
    │  │ 8 │ 9 │10 │11 │12 │13 │14 │     │
    │  └───┴───┴───┴───┴───┴───┴───┘     │
    │  ┌───┬───┬───┬───┬───┐             │
    │  │15 │16 │17 │18 │19 │20 ← Ambient │
    │  └───┴───┴───┴───┴───┘             │
    └─────────────────────────────────────┘
```

## Step 8: Install the Dispensing Arm (1.5 hours)

This is the robot that picks up medicine and delivers it!

1. Mount the 4-DOF dispensing arm to the drone body
2. Connect all 4 joint motors to the Arm Controller (ESP32)
3. Install the 2-finger parallel gripper
4. Connect the force sensor
5. Mount the delivery confirmation camera
6. **Check:** Power on. Move the arm through its full range. It should reach all 20 slots.

## Step 9: Install Phi-Harmonic Emitters (30 minutes)

1. Mount 2 Helmholtz coil emitters (front and rear)
2. Connect to the Phi-Harmonic Controller
3. **Check:** Turn on the phi-harmonic system. Verify 16.18 Hz output.

## Step 10: Install Safety Systems (30 minutes)

1. Mount the parachute system
2. Connect the parachute igniter to the safety processor
3. Mount the emergency buzzer
4. Mount status LEDs (4 colors)
5. **Check:** Test the parachute mechanism (without deploying)

## Step 11: Final Wiring & Cable Management (1 hour)

1. Route all wires neatly along the frame
2. Use zip ties every 10cm
3. Make sure no wires can touch propellers
4. Label every connector
5. **Check:** Visual inspection — no loose wires, no exposed solder joints

## Step 12: Software Setup (1 hour)

1. Flash firmware to the Pixhawk 6C
2. Configure motor directions
3. Calibrate IMU
4. Calibrate temperature sensors (ice point test for refrigerated zone)
5. Calibrate RFID readers
6. Calibrate barcode scanners
7. Upload medication database
8. **Check:** All systems should show "green" on the ground station

---

## Final Checklist

| System | Test | Pass? |
|--------|------|-------|
| Frame | All bolts tight, no cracks | [ ] |
| Motors | All 4 spin correctly | [ ] |
| Battery | 25.6V, charges fully | [ ] |
| Temperature - Refrigerated | Reaches 8°C in 5 min | [ ] |
| Temperature - Ambient | Holds 20°C ± 1°C | [ ] |
| Storage - RFID | All 20 slots detected | [ ] |
| Storage - Barcode | 100% read accuracy | [ ] |
| Storage - Locks | All 20 lock/unlock | [ ] |
| Dispensing arm | Reaches all 20 slots | [ ] |
| Phi-harmonic | 16.18 Hz output verified | [ ] |
| Navigation | GPS lock, obstacle avoidance | [ ] |
| Safety | Parachute armed, buzzer works | [ ] |

**Congratulations!** Your PHI Pharmacy Drone is ready for testing! 🎉

Next step: Go to `TEST_PLAN.md` to run the full test suite before your first delivery.
