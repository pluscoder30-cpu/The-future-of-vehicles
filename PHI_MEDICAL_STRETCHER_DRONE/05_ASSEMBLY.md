# PHI Medical Stretcher Drone - Assembly Guide

> **Difficulty**: Hard | **Time**: ~16 hours | **People needed**: 2-3

## What You're Building

You're building a drone that can carry a sick or injured person to the hospital while a doctor watches their heartbeat on a screen. It has 8 spinning rotors (that's a lot!), a winch to lift people up, and a special healing field.

## Before You Start

**Safety rules:**
- Always wear safety glasses when cutting or soldering
- Never work on the battery alone — have an adult nearby
- Keep your fingers away from propellers even when the drone is off
- If you smell something burning, unplug everything immediately

**Tools you'll need:**
- Hex drivers (2mm, 3mm, 4mm, 5mm)
- Screwdriver set
- Soldering iron + solder
- Wire strippers
- Multimeter (for checking electrical connections)
- Torque wrench (5-25 Nm)
- Zip ties and tape

---

## Step 1: Build the Frame (2 hours)

The frame is the skeleton of the drone. Everything attaches to it.

1. Unpack the carbon fiber octocopter frame pieces
2. Lay out all 8 motor arms on a flat surface
3. Bolt each arm to the center plate using the included hardware
4. Tighten bolts in a star pattern (like tightening a car wheel) — this keeps it even
5. Attach the bottom plate to lock everything together
6. **Check:** All 8 arms should be the same length. Wiggle each one — no movement is good!

```
        M1       M2
         \       /
          [CENTER]
         /       \
        M8       M3
       |           |
        M7       M4
         \       /
          [CENTER]
         /       \
        M6       M5
```

## Step 2: Install Motors (1.5 hours)

1. Place one T-Motor U15L on each arm mount
2. Bolt down with 3 screws per motor (hand tight, then 1/4 turn with hex driver)
3. Attach one propeller to each motor
   - Motors 1, 3, 5, 7 spin **clockwise** (marked with a C)
   - Motors 2, 4, 6, 8 spin **counter-clockwise** (marked with CC)
4. **Check:** Spin each prop by hand. They should spin freely and not hit anything.

## Step 3: Wire the ESCs (2 hours)

The ESC (Electronic Speed Controller) is like a mini-computer that tells each motor how fast to spin.

1. Connect one FLAME 180A ESC to each motor (3 wires — doesn't matter which order)
2. Solder the ESC power wires to the power distribution board
3. Connect each ESC signal wire to the flight controller
4. Label every wire with tape: "M1", "M2", etc.
5. **Check:** With battery connected (carefully!), each motor should respond to the flight controller test

## Step 4: Install the Flight Controllers (1 hour)

1. Mount the Pixhawk 6X in the center of the frame using vibration dampeners
2. Mount the Cube Orange+ nearby as backup
3. Connect GPS modules to the Pixhawk (UART1 and UART2 ports)
4. Connect the LiDAR sensor (Ethernet port)
5. Connect all 4 cameras (Ethernet ports)
6. **Check:** Power on — both controllers should light up and show status on their LEDs

## Step 5: Install the Battery (30 minutes)

1. Place the FPB-20 battery in the battery bay
2. Secure with straps — it's heavy (40 kg) so make sure it can't move
3. Connect the main power connector (XT90)
4. Connect both BMS units to the battery
5. **Check:** Battery voltage should read 51.2V on the multimeter

## Step 6: Install the Medical Systems (2 hours)

This is what makes this drone special — it can keep a patient alive!

1. Mount the Medical Monitor Array on the patient platform
2. Connect ECG leads, SpO2 probe, NIBP cuff, temperature probe, and respiratory belt
3. Mount the Life Support Module (O2 tank, AED, IV hooks)
4. Wire everything to the Medical MCU (STM32F4)
5. **Check:** Run the medical diagnostic test — all 6 monitoring channels should show "OK"

## Step 7: Install the Winch System (1.5 hours)

1. Mount the hydraulic winch to the bottom of the frame
2. Route the 10m cable through the guide
3. Attach the trauma-rated patient harness to the cable end
4. Connect the winch motor to a dedicated ESC
5. **Check:** Test the winch with a 50kg weight. It should lift smoothly.

## Step 8: Install Phi-Harmonic Emitters (1 hour)

These special coils create a healing field at 16.18 Hz.

1. Mount 8 Helmholtz coil emitters around the patient platform
2. Connect each emitter to the Phi-Harmonic Controller (ESP32)
3. Wire the controller to the Medical MCU
4. **Check:** Turn on the phi-harmonic system. Use a spectrum analyzer to verify 16.18 Hz output.

## Step 9: Install Communication Systems (1 hour)

1. Mount the 4G/5G LTE modem
2. Mount the 900 MHz mesh radio
3. Connect both to the flight controller
4. Mount antennas (keep them away from carbon fiber — it blocks signals)
5. **Check:** Connect to the ground station. Both LTE and mesh should show "connected."

## Step 10: Install Safety Systems (1 hour)

1. Mount the parachute system on top of the frame
2. Connect the parachute igniter to the safety processor
3. Mount status LEDs (Red=Front, Green=Rear, Blue=Left, Amber=Right)
4. Mount the emergency buzzer
5. **Check:** Test the parachute deployment mechanism (without actually deploying)

## Step 11: Final Wiring & Cable Management (1.5 hours)

1. Route all wires neatly along the frame arms
2. Use zip ties every 10cm to secure wires
3. Make sure no wires can touch propellers
4. Shield all medical sensor wires with foil tape
5. Label every connector
6. **Check:** Visual inspection — no loose wires, no exposed solder joints

## Step 12: Software Setup (1 hour)

1. Flash firmware v2.0.0 to the Pixhawk
2. Flash backup firmware to the Cube Orange+
3. Configure motor directions in PX4
4. Calibrate IMU (place on level surface, wait 5 minutes)
5. Calibrate compass (rotate drone in all directions)
6. Set GPS parameters (RTK mode)
7. Upload hospital database
8. **Check:** All systems should show "green" on the ground station

---

## Final Checklist

| System | Test | Pass? |
|--------|------|-------|
| Frame | All bolts tight, no cracks | [ ] |
| Motors | All 8 spin correctly | [ ] |
| Propellers | No wobble, correct direction | [ ] |
| Battery | 51.2V, charges fully | [ ] |
| Flight controller | GPS lock, IMU calibrated | [ ] |
| Medical monitors | All 6 channels working | [ ] |
| Winch | Lifts 120kg, retracts smoothly | [ ] |
| Phi-harmonic | 16.18 Hz output verified | [ ] |
| Communication | LTE + mesh connected | [ ] |
| Safety | Parachute armed, buzzer works | [ ] |

**Congratulations!** Your PHI Medical Stretcher Drone is ready for testing! 🎉

Next step: Go to `TEST_PLAN.md` to run the full test suite before your first flight.
