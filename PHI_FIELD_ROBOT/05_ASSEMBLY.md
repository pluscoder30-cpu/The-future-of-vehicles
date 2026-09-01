# PHI_FIELD_ROBOT — Assembly Guide

## PHI_FIELD_ROBOT | Document 05: Assembly Guide

---

## 1. ASSEMBLY TOOLS REQUIRED

| Tool | Specification | Purpose |
|------|---------------|---------|
| Hex Key Set | M2.5, M3, M4 | All fasteners |
| Torque Wrench | 0.5-5 N·m | Joint bolts |
| Soldering Iron | 600°C, chisel tip | Wire connections |
| Multimeter | CAT III, 600V | Continuity checks |
| Crimping Tool | JST-GH compatible | Connector assembly |
| Heat Gun | 350°C | Heat shrink |
| Blue Threadlocker | Loctite 243 | Thread locking |
| Thermal Paste | 12.5 W/mK | Pi heatsink |
| Cable Ties | Various sizes | Cable management |
| Digital Scale | 0.1g resolution | Weight verification |
| Caliper | 0.01mm resolution | Dimension checks |
| ESD Wrist Strap | 1MΩ resistor | Static protection |
| Safety Glasses | ANSI Z87.1 | Eye protection |
| Work Gloves | Cut-resistant | Hand protection |

---

## 2. ASSEMBLY SEQUENCE

### Phase 1: Frame Preparation (Day 1)

**Step 1.1: Frame Inspection**
```
Time: 30 minutes
Tools: Caliper, visual inspection

Checklist:
□ Verify frame dimensions (400×200×120mm)
□ Check all mounting holes are tapped
□ Inspect anodizing for defects
□ Verify cable routing channels clear
□ Test-fit battery bay covers
□ Confirm thermal paste area is flat
```

**Step 1.2: Install Steel Inserts**
```
Time: 45 minutes
Tools: Soldering iron (300°C), M4×8 bolt (temporary)

Insert Type: M4 heat-set inserts (brass)
Location: 4× leg mount points, 4× arm mount

Procedure:
1. Heat insert with soldering iron (300°C)
2. Press into aluminum frame (pre-drilled hole)
3. Hold for 10 seconds while cooling
4. Remove soldering iron
5. Verify flush with frame surface
6. Repeat for all 8 inserts
```

**Step 1.3: Install Vibration Dampeners**
```
Time: 15 minutes
Tools: None (press-fit)

Locations:
- 4× Pi mount dampeners (silicone 40A)
- 2× IMU mount dampeners
- 2× LIDAR mount dampeners

Procedure:
1. Clean mounting surfaces with IPA
2. Press dampener into recessed pocket
3. Verify flush and centered
```

---

### Phase 2: Electronics Installation (Day 2)

**Step 2.1: Main PCB Mounting**
```
Time: 30 minutes
Tools: M3×6 hex key, ESD strap

Mounting Points: 4× brass standoffs (M3×6)

Procedure:
1. Install ESD wrist strap
2. Screw 4× M3×6 standoffs into frame
3. Place main PCB onto standoffs
4. Secure with 4× M3×6 bolts
5. Verify no shorts (multimeter: GND to VCC = >1kΩ)
6. Connect USB cable to Pi location
```

**Step 2.2: Raspberry Pi 5 Mounting**
```
Time: 20 minutes
Tools: M2.5 hex key, thermal paste

Procedure:
1. Apply thermal paste to Pi CPU (pea-sized dot)
2. Mount Pi to vibration dampeners
3. Connect Pi to main PCB via USB-C
4. Install NVMe HAT on Pi
5. Insert NVMe SSD into HAT
6. Secure with M2.5 bolts
7. Verify Pi boots (connect monitor temporarily)
```

**Step.3: Coral TPU Installation**
```
Time: 10 minutes
Tools: M.2 screw

Procedure:
1. Insert Coral M.2 into Pi 5 M.2 slot
2. Secure with M.2 screw
3. Verify detection (lsusb shows Google Inc.)
4. Install Edge TPU runtime
```

**Step 2.4: Sensor Installation**
```
Time: 45 minutes
Tools: M2.5 hex key, cable ties

IMU (BNO085):
1. Mount to vibration dampener (center of body)
2. Connect I2C cable (300mm)
3. Secure cable with tie

ADS1115 ADC:
1. Mount to main PCB standoffs
2. Connect I2C cable (150mm)
3. Route FSR cables to foot locations

BME280:
1. Mount near electronics bay vent
2. Connect I2C cable (50mm)

GPS Module:
1. Mount antenna on top of body
2. Route SMA cable through frame
3. Connect UART cable to main PCB
```

**Step 2.5: LIDAR Installation**
```
Time: 20 minutes
Tools: M3 hex key

Procedure:
1. Mount LIDAR bracket to rear panel
2. Secure RPLIDAR A1M8 to bracket (3× M3×4)
3. Connect USB cable
4. Route cable through frame to USB hub
5. Verify scan data (rplidar_ros)
```

**Step 2.6: Camera Installation**
```
Time: 30 minutes
Tools: M2.5 hex key

Procedure:
1. Mount 4× camera brackets to body
2. Secure cameras with M2.5×4 bolts
3. Connect CSI cables to Pi (cameras 1-2)
4. Connect USB cables for cameras 3-4
5. Verify all 4 cameras detected
6. Test 360° coverage
```

---

### Phase 3: Power System (Day 3)

**Step 3.1: DC-DC Converter Installation**
```
Time: 30 minutes
Tools: Thermal paste, M3 hex key

Procedure:
1. Apply thermal paste to converter bottoms
2. Mount converters to heatsink
3. Secure with M3 bolts
4. Connect input wires (48V bus)
5. Connect output wires (24V, 5V, 12V buses)
6. Verify output voltages (multimeter)
```

**Step 3.2: Emergency Stop Installation**
```
Time: 15 minutes
Tools: 16mm wrench

Procedure:
1. Insert emergency stop button through panel cutout
2. Secure with mounting nut (16mm wrench)
3. Connect NC contact to solid-state relay
4. Connect relay to 48V bus
5. Test: press button → power cut → release → power restore
```

**Step 3.3: Battery Bay Assembly**
```
Time: 30 minutes
Tools: M3 hex key

Procedure:
1. Install 4× rail guides per bay
2. Install spring-loaded latches
3. Test battery insertion/removal
4. Verify XT90 connector alignment
5. Install XT30 data connector
```

---

### Phase 4: Leg Assembly (Day 4-5)

**Step 4.1: Single Leg Assembly**
```
Time: 2 hours per leg (8 hours total)
Tools: M3, M4 hex keys, torque wrench

For EACH leg (×4):

1. HIP YAW ASSEMBLY:
   □ Insert 2× flanged bearings into hip yaw housing
   □ Install hip yaw motor (M2006 PAP)
   □ Align motor shaft with bearing bore
   □ Secure with 4× M3×8 bolts (torque: 0.5 N·m)
   □ Verify smooth rotation (no binding)

2. HIP PITCH ASSEMBLY:
   □ Insert 2× flanged bearings into hip pitch housing
   □ Install hip pitch motor
   □ Align and secure with 4× M3×8 bolts
   □ Verify rotation range (-30° to +90°)

3. FEMUR ATTACHMENT:
   □ Slide femur (upper leg) onto hip yaw shaft
   □ Secure with M4×12 bolt + nylon lock nut
   □ Torque to 1.0 N·m
   □ Verify femur aligned with body frame

4. KNEE ASSEMBLY:
   □ Insert 2× flanged bearings into knee housing
   □ Install knee motor
   □ Secure with 4× M3×8 bolts
   □ Attach tibia (lower leg) to knee motor shaft
   □ Secure with M4×12 bolt + nylon lock nut
   □ Verify rotation range (0° to +135°)

5. FOOT ATTACHMENT:
   □ Press silicone foot pad onto tibia end
   □ Verify FSR seated in pocket
   □ Secure with M4×8 bolt
   □ Test FSR reading (should change with pressure)
```

**Step 4.2: Leg-to-Body Attachment**
```
Time: 30 minutes per leg (2 hours total)
Tools: M4 hex key, torque wrench

Procedure:
1. Align leg mount with frame insert
2. Insert 4× M4×8 bolts
3. Torque to 2.0 N·m (in star pattern)
4. Verify leg free to move (no binding)
5. Repeat for all 4 legs
```

**Step 4.3: CAN Bus Connection**
```
Time: 30 minutes
Tools: Cable ties

Procedure:
1. Connect CAN cables to each motor (daisy-chain)
2. Route cables through leg frame channels
3. Secure with cable ties (every 50mm)
4. Connect to main PCB CAN1 connector
5. Verify CAN communication (test each motor)
```

---

### Phase 5: Arm Assembly (Day 6)

**Step 5.1: Shoulder Assembly**
```
Time: 1 hour
Tools: M3, M4 hex keys

Procedure:
1. Mount shoulder pitch motor to body frame
2. Attach shoulder roll motor to pitch motor output
3. Verify alignment (90° between axes)
4. Secure all bolts to torque spec
```

**Step 5.2: Arm Links**
```
Time: 1 hour
Tools: M4 hex key

Procedure:
1. Attach upper arm link to shoulder roll motor
2. Secure with M4×12 bolt
3. Mount elbow pitch motor to upper arm end
4. Attach lower arm link to elbow motor
5. Secure with M4×12 bolt
```

**Step 5.3: Wrist and Gripper**
```
Time: 1 hour
Tools: M3 hex key

Procedure:
1. Mount wrist pitch motor to lower arm end
2. Attach force-torque sensor to wrist motor
3. Mount gripper assembly to F/T sensor
4. Connect gripper motor
5. Test gripper open/close
```

**Step 5.4: Arm Calibration**
```
Time: 30 minutes
Tools: None (software)

Procedure:
1. Power on arm motors
2. Run zero-position routine
3. Verify all joints at home position
4. Test forward kinematics (command positions)
5. Test inverse kinematics (command end-effector)
6. Calibrate force-torque sensor (zero load)
```

---

### Phase 6: Final Assembly (Day 7)

**Step 6.1: Cable Management**
```
Time: 2 hours
Tools: Cable ties, spiral wrap

Procedure:
1. Route all CAN cables through body channels
2. Route power cables separately from signal cables
3. Secure every 50mm with cable ties
4. Add spiral wrap to bundled cables
5. Verify no cables near moving parts
6. Check all connectors seated
```

**Step 6.2: Cover Installation**
```
Time: 30 minutes
Tools: M3 hex key

Procedure:
1. Install electronics bay cover (with gasket)
2. Install battery bay covers (with latches)
3. Verify all covers flush and sealed
4. Test cover removal for battery swap
```

**Step 6.3: Final Checks**
```
Time: 1 hour
Tools: Multimeter, visual inspection

Electrical Checks:
□ Verify 48V bus voltage (48V ±1V)
□ Verify 24V bus voltage (24V ±0.5V)
□ Verify 5V bus voltage (5.0V ±0.1V)
□ Verify 12V bus voltage (12V ±0.2V)
□ Check all CAN buses (120Ω termination)
□ Verify I2C communication (all devices)
□ Test emergency stop (power cut in <10ms)
□ Verify all cameras detected
□ Verify LIDAR scanning
□ Verify GPS lock

Mechanical Checks:
□ All bolts torqued to spec
□ All joints move freely (no binding)
□ All legs reach full range of motion
□ Arm reaches full workspace
□ Gripper opens/closes smoothly
□ Battery bays functional
□ All covers secure
□ No rattles or loose parts
```

---

## 3. ASSEMBLY VERIFICATION CHECKLIST

### 3.1 Pre-Power Checklist

| Item | Check | Status |
|------|-------|--------|
| All bolts torqued | Visual/torque wrench | □ |
| No loose wires | Shake test | □ |
| No shorts | Multimeter (GND to VCC) | □ |
| CAN termination | 120Ω end-to-end | □ |
| I2C pull-ups | 4.7kΩ present | □ |
| Emergency stop | Functioning | □ |
| Battery polarity | Correct (XT90) | □ |
| Thermal paste | Applied to Pi | □ |
| ESD protection | Installed | □ |
| Cable routing | Clear of moving parts | □ |

### 3.2 Power-On Sequence

```
Step 1: Remove emergency stop button
Step 2: Wait 5 seconds (BMS boot)
Step 3: Verify 48V bus active (multimeter)
Step 4: Wait for Pi 5 to boot (30 seconds)
Step 5: Verify ROS 2 running (ros2 topic list)
Step 6: Verify all motors detected (CAN scan)
Step 7: Verify all sensors detected (I2C scan)
Step 8: Run self-test routine
Step 9: Calibrate IMU (figure-8 motion)
Step 10: Run phi-harmonic gait test
```

### 3.3 Functional Tests

| Test | Procedure | Pass Criteria |
|------|-----------|---------------|
| Leg Movement | Command each joint ±30° | Smooth, no binding |
| Gait Test | Walk forward 1m | Stable, 8 km/h capable |
| Arm Test | Command each joint ±45° | Smooth, accurate |
| Grip Test | Pick up 1kg object | Secure grip, no slip |
| Camera Test | Display all 4 views | Clear, 30fps |
| LIDAR Test | Scan room | 360°, 8000 pts/sec |
| GPS Test | Wait for fix | <30 seconds |
| Battery Test | Run until 20% | Accurate estimation |
| Emergency Stop | Press during walk | Stop in <10ms |
| Sleep Mode | Enter/exit sleep | Clean transitions |

---

## 4. BREAK-IN PROCEDURE

### 4.1 Initial Calibration (1 hour)

```
1. IMU Calibration:
   - Place robot on flat surface
   - Run calibration routine (figure-8 motion)
   - Verify quaternion output (0,0,0,1) when level

2. Motor Calibration:
   - Run zero-position routine for all 17 motors
   - Verify encoder readings match physical positions
   - Calibrate torque constants

3. FSR Calibration:
   - Calibrate zero-force reading (robot in air)
   - Calibrate full-scale (robot standing, known weight)
   - Verify linear response

4. Force-Torque Calibration:
   - Zero all axes (no load)
   - Apply known weight (1kg) and verify
   - Repeat for all 6 axes
```

### 4.2 Gait Tuning (2 hours)

```
1. Stand Test:
   - Command stand pose
   - Verify all 4 feet on ground
   - Check weight distribution (FSR readings)
   - Adjust if uneven

2. Slow Walk Test:
   - Walk at 1 km/h
   - Observe gait stability
   - Adjust phi-harmonic parameters if needed

3. Speed Ramp:
   - Gradually increase to 8 km/h
   - Monitor stability
   - Note maximum stable speed

4. Terrain Test:
   - Walk on grass
   - Walk on gravel
   - Walk up 10° slope
   - Step over 50mm obstacle
   - Adjust gait for each terrain
```

### 4.3 Arm Tuning (1 hour)

```
1. Reach Test:
   - Command arm to all workspace boundaries
   - Verify no collisions with body
   - Adjust limits if needed

2. Payload Test:
   - Pick up 1kg at full extension
   - Verify no sagging or vibration
   - Test 5kg, 10kg loads

3. Precision Test:
   - Pick up small object (20mm)
   - Place in specific location
   - Verify accuracy (±5mm)
```

---

## 5. TROUBLESHOOTING

### 5.1 Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Motor not responding | CAN cable loose | Check JST-GH connector |
| IMU giving wrong values | Calibration failed | Re-run calibration |
| Pi not booting | Power supply issue | Check 5V converter output |
| LIDAR not scanning | USB connection | Re-seat USB cable |
| Camera black | CSI cable loose | Re-seat FFC cable |
| Battery not charging | BMS fault | Check BMS status LEDs |
| Emergency stop stuck | Button mechanical | Check button contacts |
| Arm jitters | PID tuning | Adjust PID gains |
| Gait unstable | IMU drift | Re-calibrate IMU |
| High current draw | Short circuit | Check for shorts with multimeter |

### 5.2 Error Codes

| Code | Meaning | Action |
|------|---------|--------|
| E001 | CAN bus error | Check CAN cables and termination |
| E002 | Motor overcurrent | Check motor windings and load |
| E003 | IMU communication failed | Check I2C cable and address |
| E004 | Battery undervoltage | Charge battery immediately |
| E005 | Pi watchdog timeout | Check Pi power and thermal |
| E006 | Emergency stop active | Release e-stop button |
| E007 | Arm collision detected | Check arm workspace limits |
| E008 | LIDAR obstruction | Clear LIDAR path |
| E009 | FSR calibration error | Re-calibrate FSRs |
| E010 | Temperature overlimit | Reduce load, check cooling |

---

## 6. MAINTENANCE SCHEDULE

| Interval | Task | Tools |
|----------|------|-------|
| Every use | Visual inspection | None |
| Weekly | Check bolt torque | Hex key set |
| Monthly | Clean foot pads | IPA, cloth |
| Monthly | Check cable condition | Visual |
| Quarterly | Re-calibrate IMU | Software |
| Quarterly | Check bearing smoothness | Manual rotation |
| Semi-annual | Replace vibration dampeners | M2.5 hex key |
| Semi-annual | Clean LIDAR lens | Lens cloth |
| Annual | Full re-calibration | Full test suite |
| Annual | Replace foot pads | M4 hex key |
| As needed | Update firmware | USB connection |
| As needed | Replace cables | Soldering iron |

---

*Document Version: 1.0*
*Date: 2026-08-27*
*Author: Build Agent 5 of 6*
