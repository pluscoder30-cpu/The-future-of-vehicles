# PHI Surgical Assist Drone - Assembly Guide

> **Difficulty**: Medium | **Time**: ~12 hours | **People needed**: 2

## What You're Building

You're building a drone that hovers over a surgeon's operating table, holds surgical tools, and keeps everything sterile. It mounts to the ceiling and can switch instruments in less than 2 seconds. Think of it as a robot helper for surgery!

## Before You Start

**Safety rules:**
- Always wear safety glasses when cutting or soldering
- Never look directly at UV-C lamps when they're on
- Keep fingers away from the robotic arm joints
- Wear an ESD wrist strap when handling electronics

**Tools you'll need:**
- Hex drivers (1.5mm, 2mm, 2.5mm, 3mm)
- Precision screwdriver set
- Soldering iron + solder
- Wire strippers
- Multimeter
- Torque wrench (2-10 Nm)

---

## Step 1: Build the Frame (1.5 hours)

The frame is medical-grade aluminum — lightweight but strong.

1. Unpack the anodized aluminum frame pieces
2. Bolt the 4 motor arms to the center hub
3. Attach the enclosed rotor shrouds to each arm
   - The shrouds have HEPA filters built in — don't touch the filter media!
4. Bolt the bottom plate to the center hub
5. **Check:** All 4 arms should be the same length. Shrouds should be fully enclosed.

```
    [SHROUD]     [SHROUD]
        \           /
         [CENTER]
        /           \
    [SHROUD]     [SHROUD]
```

## Step 2: Install Motors & Propellers (1 hour)

1. Place one T-Motor F80 Pro in each shroud
2. Bolt down with 3 screws per motor
3. Attach one 8-inch enclosed propeller to each motor
   - Motors 1, 3 spin **clockwise** (C)
   - Motors 2, 4 spin **counter-clockwise** (CC)
4. **Check:** Spin each prop by hand inside the shroud. It should NOT touch the shroud.

## Step 3: Wire the ESCs (1.5 hours)

1. Connect one medical-grade ESC to each motor (3 wires)
2. Solder ESC power wires to the power distribution board
3. Connect each ESC signal wire to the Pixhawk Mini
4. Label every wire: "M1", "M2", "M3", "M4"
5. **Check:** Power on — each motor should respond to the flight controller test

## Step 4: Install the Flight Controllers (1 hour)

1. Mount the Pixhawk Mini in the center of the frame
2. Mount the Arm Controller (STM32H7) near the robotic arm
3. Connect the EM Tracker to UART1
4. Connect the Arm Controller to UART2
5. Connect the Safety Processor to UART3
6. Connect the stereo camera to SPI1
7. **Check:** Power on — both controllers should show green LEDs

## Step 5: Install the Battery (30 minutes)

1. Place the FPB-5 battery in the battery bay
2. Secure with the magnetic mounting bracket
3. Connect the main power connector (XT30)
4. **Check:** Battery voltage should read 25.6V on the multimeter

## Step 6: Install the Robotic Arm (2 hours)

This is the most important part — it holds the surgical instruments!

1. Mount the 6-DOF robotic arm to the bottom of the frame
2. Connect all 6 joint motor cables to the Arm Controller
3. Connect the force/torque sensor (SPI3)
4. Install the quick-change instrument gripper at the end of the arm
5. Connect the gripper motor and instrument detect sensors
6. Wire the mechanical brake (fail-safe: power off = brake engaged)
7. **Check:** Power on the arm controller. Move each joint through its full range of motion.

```
    [FRAME]
       |
    [ARM BASE] --- Joint 1 (rotation)
       |
    [SHOULDER] --- Joint 2
       |
    [ELBOW] --- Joint 3
       |
    [WRIST ROLL] --- Joint 4
       |
    [WRIST PITCH] --- Joint 5
       |
    [WRIST YAW] --- Joint 6
       |
    [GRIPPER] --- 6 instrument slots
```

## Step 7: Install the Sterile Field System (1.5 hours)

This keeps the surgical area clean and free of germs.

1. Mount the UV-C LED array around the instrument area
2. Mount the ionization emitters (4 positions)
3. Connect both to the Sterile Field Controller (ESP32)
4. Install the HEPA filter in the air intake
5. Mount the particle counter sensor
6. **Check:** Power on the sterile system. UV-C should show 40mW/cm2 with a UV meter.

## Step 8: Install the Phi-Harmonic Emitters (1 hour)

These coils create healing fields at specific frequencies.

1. Mount 4 Helmholtz coil pairs around the surgical area
2. Connect each pair to the Phi-Harmonic Controller (ESP32)
3. Wire the tissue impedance sensor (I2C)
4. **Check:** Turn on the phi-harmonic system. Verify 16.18 Hz on a spectrum analyzer.

## Step 9: Install Navigation Sensors (1 hour)

1. Mount the stereo camera module (60mm baseline)
2. Mount the EM tracker sensor near the surgical field
3. Connect both to the flight controller
4. Mount the IMU (already built into Pixhawk)
5. **Check:** Run visual servoing test — the drone should lock onto a target in under 1 second.

## Step 10: Install the Ceiling Dock Mount (30 minutes)

1. Mount the magnetic docking station to the ceiling rail
2. Install the inductive power coil
3. Install the optical data link
4. Connect both to the hospital power supply
5. **Check:** Dock the drone. It should engage the magnetic lock and start charging.

## Step 11: Final Wiring & Cable Management (1 hour)

1. Route all wires neatly along the frame
2. Use medical-grade cable ties (no sharp edges!)
3. Shield all sensor wires
4. Label every connector
5. **Check:** Visual inspection — no loose wires, no exposed solder joints

## Step 12: Software Setup (1 hour)

1. Flash firmware to the Pixhawk Mini
2. Flash arm control firmware to the STM32H7
3. Configure motor directions
4. Calibrate cameras with a calibration target
5. Calibrate the force/torque sensor
6. Set up voice command recognition
7. **Check:** All systems should show "green" on the ground station

---

## Final Checklist

| System | Test | Pass? |
|--------|------|-------|
| Frame | All bolts tight, shrouds intact | [ ] |
| Motors | All 4 spin, no shroud contact | [ ] |
| Battery | 25.6V, charges via dock | [ ] |
| Flight controller | IMU calibrated, GPS ready | [ ] |
| Robotic arm | All 6 joints move, gripper works | [ ] |
| Sterile field | UV-C 40mW/cm2, particles <10/m3 | [ ] |
| Phi-harmonic | 16.18 Hz output verified | [ ] |
| Visual servoing | Target lock <1s | [ ] |
| Ceiling dock | Magnetic lock, inductive charging | [ ] |
| Safety | Brake engages, emergency stop works | [ ] |

**Congratulations!** Your PHI Surgical Assist Drone is ready for testing! 🎉

Next step: Go to `TEST_PLAN.md` to run the full test suite before your first procedure.
