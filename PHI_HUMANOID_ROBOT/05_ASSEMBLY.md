# PHI_HUMANOID_ROBOT — Assembly Guide

## Step-by-Step Assembly Procedure

---

## 1. Assembly Overview

### 1.1 Estimated Build Time

| Phase | Duration | Tools Required |
|-------|----------|---------------|
| Phase 1: Frame | 8 hours | Hex keys, torque wrench, drill press |
| Phase 2: Leg Actuators | 6 hours | Hex keys, soldering iron, multimeter |
| Phase 3: Arm Assembly | 5 hours | Hex keys, soldering iron |
| Phase 4: Torso + Head | 4 hours | Hex keys, wire strippers |
| Phase 5: Hand Assembly | 4 hours | Precision screwdrivers, tweezers |
| Phase 6: Electrical | 8 hours | Soldering iron, crimping tools, multimeter |
| Phase 7: Software | 12 hours | Computer, USB cables |
| Phase 8: Calibration | 6 hours | Oscilloscope, dyno (optional) |
| **Total** | **53 hours** | — |

### 1.2 Required Tools

| Tool | Purpose | Priority |
|------|---------|----------|
| Metric hex key set (1.5-6mm) | Most fasteners | Critical |
| Torque wrench (1-10 Nm) | Joint bolts | Critical |
| Soldering iron (60W, temp controlled) | Wire connections | Critical |
| Wire strippers (22-8 AWG) | Cable prep | Critical |
| Multimeter (DMM) | Continuity, voltage checks | Critical |
| Crimping tool (XT90, Micro-Fit) | Power connectors | Critical |
| Heat gun | Heat shrink tubing | Important |
| Drill press | Hole drilling | Important |
| Deburring tool | Edge cleanup | Important |
| Flush cutters | Trim leads | Important |
| Tweezers (ESD) | Small components | Important |
| Flux pen | Solder quality | Recommended |
| Oscilloscope | Signal debugging | Recommended |
| USB-UART adapter | Debug console | Recommended |
| Calipers (digital) | Dimension checks | Recommended |

---

## 2. Phase 1: Frame Assembly

### Step 1.1: Pelvis Plate Preparation

```
PARTS NEEDED:
- Pelvis plate (S-02)
- M4×8mm bolts ×8
- M4 washers ×8
- M4 lock nuts ×8

PROCEDURE:
1. Inspect pelvis plate for burrs, deburr if needed
2. Mark hole positions per drawing (φ-ratio spacing)
3. Drill M4 clearance holes (4.5mm) at marked positions
4. Tap M4 threads at motor mount holes
5. Test-fit motor mounting bolts

TORQUE: 2.5 Nm (M4 stainless steel)
```

### Step 1.2: Torso Frame Assembly

```
PARTS NEEDED:
- Main torso tube (S-01)
- Pelvis plate (S-02)
- Gussets (S-15) ×4
- M4×10mm bolts ×12
- M4 washers ×12

PROCEDURE:
1. Position torso tube on pelvis plate (centered)
2. Insert 4 gussets at corners (triangular reinforcement)
3. Bolt gussets to torso tube (M4×10mm)
4. Bolt gussets to pelvis plate (M4×8mm)
5. Check perpendicularity with square
6. Torque all bolts to 2.5 Nm
7. Verify frame is rigid (no flex under 50N lateral load)
```

### Step 1.3: Neck Bracket Installation

```
PARTS NEEDED:
- Neck bracket (S-08)
- M3×6mm bolts ×4
- M3 lock nuts ×4

PROCEDURE:
1. Position neck bracket on top of torso tube
2. Align using φ-ratio reference marks
3. Bolt with M3×6mm, torque to 1.0 Nm
4. Verify neck bracket is level
```

---

## 3. Phase 2: Leg Actuator Assembly

### Step 3.1: Hip Joint Assembly (Left Leg)

```
PARTS NEEDED:
- Pelvis plate (installed)
- HAA motor: ODrive D6374 150KV
- HFE motor: ODrive D6374 150KV
- AS5048A encoder ×2
- 608ZZ bearing ×2
- Bearing flange ×2
- M5×12mm bolts ×8
- M4×8mm bolts ×4
- Upper leg tube (S-03)
- Encoder magnets ×2

PROCEDURE:
1. Install bearing flange #1 (HAA axis) on pelvis plate
   - Press-fit 608ZZ bearing into flange
   - Bolt flange to pelvis (M5×12mm, 4 Nm)
   
2. Mount HAA motor to bearing flange
   - Align motor shaft with bearing center
   - Bolt motor to flange (M4×8mm, 2.5 Nm)
   - Verify 137.5° offset from HFE reference axis
   
3. Install encoder magnet on HAA motor shaft
   - Center magnet on shaft end
   - Verify air gap: 1mm ±0.5mm
   
4. Mount AS5048A encoder PCB
   - Position perpendicular to magnet
   - Secure with M2×4mm screws
   
5. Install bearing flange #2 (HFE axis)
   - Perpendicular to HAA axis
   - Press-fit bearing, bolt to pelvis
   
6. Mount HFE motor to bearing flange
   - Align shaft perpendicular to HAA shaft
   - Bolt motor to flange (M4×8mm, 2.5 Nm)
   
7. Install upper leg tube
   - Slide tube over HFE motor shaft
   - Bolt tube to HFE motor output flange (M5×12mm, 4 Nm)
   - Verify tube is perpendicular to pelvis plate
```

### Step 3.2: Knee Joint Assembly (Left Leg)

```
PARTS NEEDED:
- Upper leg tube (installed)
- KFE motor: ODrive D6374 150KV
- KAA motor: ODrive D5065 270KV
- AS5048A encoder ×2
- Lower leg tube (S-04)
- Bearing flange ×2

PROCEDURE:
1. Install KFE motor at bottom of upper leg tube
   - Bolt to flange (M4×8mm, 2.5 Nm)
   - Verify 137.5° offset from KAA reference axis
   
2. Install KAA motor
   - Perpendicular to KFE axis
   - Bolt to mounting bracket (M4, 2.5 Nm)
   
3. Attach lower leg tube to KFE motor output
   - Bolt (M5×12mm, 4 Nm)
   - Verify alignment
   
4. Install encoders on both joints
   - Magnets centered, air gap 1mm
   - PCBs perpendicular to magnets
```

### Step 3.3: Ankle/Toe Assembly (Left Leg)

```
PARTS NEEDED:
- Lower leg tube (installed)
- AFE motor: ODrive D5065 270KV
- TOE motor: ODrive D5065 270KV
- Foot plate (S-05)
- Rubber foot pad (M-01)
- AS5048A encoder ×2

PROCEDURE:
1. Install AFE motor at bottom of lower leg tube
   - Bolt to flange (M4×8mm, 2.5 Nm)
   
2. Install TOE motor
   - Parallel to AFE (137.5° offset for clearance)
   
3. Bolt foot plate to TOE motor output
   - M4×8mm bolts, 2.5 Nm
   - Verify foot plate is level when ankle is at 0°
   
4. Attach rubber pad to foot plate
   - Adhesive bonding + M3×6mm screws at corners
   
5. Install encoders
```

### Step 3.4: Right Leg Assembly

```
Repeat Steps 3.1-3.3 for right leg, mirroring all components.
Note: All right-leg ODrive CAN IDs are offset by +1 from left leg.
```

---

## 4. Phase 3: Arm Assembly

### Step 4.1: Shoulder Assembly (Left Arm)

```
PARTS NEEDED:
- Torso frame (installed)
- SAA motor: ODrive D5065 270KV
- SFE motor: ODrive D5065 270KV
- SHS motor: ODrive D5065 270KV
- AS5048A encoder ×3
- Upper arm tube (S-06)

PROCEDURE:
1. Bolt shoulder mounting plate to torso
   - M5×12mm, 4 Nm
   
2. Install SAA motor (outermost)
   - 137.5° offset from SFE reference
   
3. Install SFE motor (middle)
   - Perpendicular to SAA
   
4. Install SHS motor (innermost)
   - Perpendicular to both SAA and SFE
   - 275° offset (2×137.5°) from SAA reference
   
5. Attach upper arm tube to SHS motor output
   - M4×8mm, 2.5 Nm
   
6. Install all 3 encoders
```

### Step 4.2: Elbow + Wrist Assembly (Left Arm)

```
PARTS NEEDED:
- Upper arm tube (installed)
- ELF motor: ODrive D5065 270KV
- WFE motor: ODrive M5671 100KV
- WRU motor: ODrive M5671 100KV
- Lower arm tube (S-07)
- Hand chassis (S-10)

PROCEDURE:
1. Install ELF motor at bottom of upper arm tube
   - Bolt (M4×8mm, 2.5 Nm)
   
2. Attach lower arm tube to ELF motor output
   - Bolt (M4×8mm, 2.5 Nm)
   
3. Install WFE motor at bottom of lower arm tube
   - 137.5° offset from WRU reference
   
4. Install WRU motor
   - Perpendicular to WFE
   
5. Attach hand chassis to WRU motor output
   - M3×6mm, 1.0 Nm
   
6. Install all encoders
```

### Step 4.3: Right Arm Assembly

```
Repeat Steps 4.1-4.2 for right arm, mirroring all components.
```

---

## 5. Phase 4: Torso & Head Assembly

### Step 5.1: Torso Actuator Installation

```
PARTS NEEDED:
- Torso yaw motor: ODrive D6374 150KV
- Torso pitch motor: ODrive D6374 150KV
- ODrive Pro (dual channel)

PROCEDURE:
1. Install torso yaw motor inside torso frame
   - Central axis, bolt to pelvis-torso interface
   - 137.5° offset from pitch reference
   
2. Install torso pitch motor
   - Perpendicular to yaw axis
   
3. Mount ODrive Pro in torso cavity
   - Secure with M3 bolts, leave access panel
```

### Step 5.2: Head Assembly

```
PARTS NEEDED:
- Head pan motor: ODrive M5671 100KV
- Head tilt motor: ODrive M5671 100KV
- ODrive Pro (dual channel)
- Head shell (S-09)
- Stereo cameras ×2
- Microphone array ×4
- Speakers ×2
- OLED displays ×2
- BNO055 IMU
- All head sensors

PROCEDURE:
1. Install head pan motor on neck bracket
   - Bolt (M3×6mm, 1.0 Nm)
   
2. Install head tilt motor
   - Perpendicular to pan axis, 137.5° offset
   
3. Mount head shell on tilt motor output
   - Bolt (M3×6mm, 1.0 Nm)
   
4. Install cameras in eye positions
   - Stereo pair, 65mm baseline (φ×40mm)
   - Secure with M2 screws
   
5. Mount microphone array in top of head
   - Square pattern, 40mm spacing
   
6. Install speakers in ear positions
   - Secure with friction fit + adhesive
   
7. Mount OLED displays in eye sockets
   - I2C address 0x3C (left) and 0x3D (right)
   
8. Install BNO055 IMU on head PCB
   - I2C address 0x50
   
9. Install head sensors (ToF, temp, ultrasonic)
```

---

## 6. Phase 5: Hand Assembly

### Step 6.1: Finger Assembly (×5 per hand)

```
PARTS NEEDED (per finger):
- Dynamixel XL330-M288 servo
- Finger phalanx links ×3 (S-11)
- FSR402 force sensor
- M2×4mm screws ×6
- Silicone fingertip cap

PROCEDURE:
1. Mount XL330 servo in hand chassis
   - M2×4mm screws
   
2. Attach phalanx links to servo horn
   - First phalanx (proximal) to servo output
   - Second phalanx (middle) via pin joint
   - Third phalanx (distal) via pin joint
   
3. Install FSR402 in fingertip
   - Adhesive mounting + silicone cap
   
4. Route finger wiring through phalanx channels
   - 6-conductor flex cable
   - 80mm length
   
5. Repeat for all 5 fingers

FINGER SEQUENCE (φ-order):
├── Thumb: XL330 ID 1 (or 6 for right)
├── Index: XL330 ID 2 (or 7)
├── Middle: XL330 ID 3 (or 8)
├── Ring: XL330 ID 4 (or 9)
└── Pinky: XL330 ID 5 (or 10)
```

---

## 7. Phase 6: Electrical Assembly

### Step 7.1: Power Wiring

```
PROCEDURE:
1. Install power distribution PCB in torso
   - Mount on standoffs, secure with M3 bolts
   
2. Connect battery pack
   - Route 8 AWG cables from battery compartment
   - Solder XT90 connectors
   - Connect to power distribution PCB
   - Verify polarity (V+ = Red, V- = Black)
   
3. Wire buck converters
   - 48V→12V #1 → Left limb bus
   - 48V→12V #2 → Right limb bus
   - 48V→5V #1 → Logic bus (RPi, sensors)
   - 48V→5V #2 → Logic bus (redundant)
   
4. Wire emergency stop
   - Series NC buttons → contactor coil
   - Verify: pressing either button opens contactor
   - Verify: releasing buttons restores power (if enabled)
   
5. Wire fuses
   - 80A main fuse
   - 20A per limb
   - 10A for logic
   
6. Install 3.3V LDOs for sensors
   - One per sensor group
   - Decoupling: 10µF + 100nF at each LDO
```

### Step 7.2: CAN Bus Wiring

```
PROCEDURE:
1. Run CAN trunk line from torso
   - Shielded 2-conductor cable
   - 120Ω characteristic impedance
   
2. Connect ODrive controllers
   - Left leg: ODrives #1-3 (CAN IDs 0, 2, 9)
   - Right leg: ODrives #4-6 (CAN IDs 1, 3, 10)
   - Left arm: ODrives #7-9 (CAN IDs 4, 5, 12)
   - Right arm: ODrives #10-12 (CAN IDs 6, 7, 13)
   - Torso: ODrive Pro (CAN ID 8)
   - Head: ODrive Pro (CAN ID 11)
   
3. Install 120Ω termination at ONE end of trunk
   - Remove jumper at other end
   
4. Connect CAN-to-USB adapter for RPi 5
   - MCP2515 HAT or USB-CAN adapter
   
5. Shield drain: Connect at ONE end only (RPi end)
```

### Step 7.3: I2C/SPI Wiring

```
PROCEDURE:
1. Run I2C bus from RPi 5
   - 4.7kΩ pull-ups to 3.3V on SDA and SCL
   - Max bus length: 1m
   - Connect: IMUs, INA260s, OLEDs, codec
   
2. Run SPI bus from RPi 5
   - Short runs (<300mm) to STM32 co-processor
   - STM32 multiplexes to encoders and ADCs
   
3. Run I2S bus for audio
   - Short runs (<200mm) from RPi to microphones
   - Shielded cable for amplifier
   
4. Run MIPI CSI for cameras
   - 200mm flex cables
   - Route away from power cables
```

### Step 7.4: Sensor Wiring

```
PROCEDURE:
1. Wire foot pressure sensors
   - 4× FSR406 per foot
   - Voltage divider: 3.3V → FSR → 10kΩ → GND
   - Vout to ADS1256 AIN pins
   
2. Wire hand force sensors
   - 5× FSR402 per hand (fingertips)
   - Same voltage divider topology
   - Route through arm to sensor hub
   
3. Wire joint torque sensors
   - Strain gauge bridge → ADS1256
   - Excitation: 3.3V via 100Ω
   - Signal: differential, ±10mV full scale
   
4. Wire temperature sensors
   - TMP117 on I2C bus
   - Thermal pad to motor housings
   
5. Wire proximity sensors
   - VL53L0X on I2C bus (head)
   - MaxBotix ultrasonic (analog to ADC)
```

---

## 8. Phase 7: Software Installation

### Step 8.1: RPi 5 Initial Setup

```
PROCEDURE:
1. Flash NVMe SSD
   - Install Ubuntu Server 24.04 LTS (arm64)
   - Boot from NVMe
   
2. Install dependencies
   sudo apt update && sudo apt upgrade -y
   sudo apt install -y python3-pip python3-venv git cmake
   pip3 install odrive numpy scipy pyserial
   
3. Install Coral TPU driver
   echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
   curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
   sudo apt update && sudo apt install -y libedgetpu1-std python3-pycoral
   
4. Clone PHI_HUMANOID_ROBOT software repository
   git clone https://github.com/user/phi-humanoid-software.git
   cd phi-humanoid-software
   pip3 install -r requirements.txt
```

### Step 8.2: ODrive Firmware Flash

```
PROCEDURE:
1. Connect ODrive to RPi via USB
   odrive-find
   odrive usb Canterbury
   odrive backup configuration
   
2. Flash firmware
   odrive flash --firmware v0.6.6
   
3. Configure each ODrive
   odrive config-controller velocity-gain 0.5
   odrive config-controller position-gain 20.0
   odrive config-controller torque-gain 0.1
   
4. Set CAN IDs
   odrive config-set can_node_id <ID>
   
5. Repeat for all 14 ODrives (12 + 2 Pro)
```

### Step 8.3: Motor Calibration

```
PROCEDURE:
1. For each motor, run calibration sequence
   odrive run-state machine enter STATE_MOTOR_CALIBRATION
   
2. Verify resistance measurement matches spec
   D6374: ~0.3Ω
   D5065: ~0.5Ω
   M5671: ~1.2Ω
   
3. Verify inductance measurement matches spec
   D6374: ~0.4mH
   D5065: ~0.3mH
   M5671: ~0.5mH
   
4. Run encoder offset calibration
   odrive run-state machine enter STATE_ENCODER_OFFSET_CALIBRATION
   
5. Verify encoder offset is within ±5°
   
6. Set zero position
   Move joint to reference position
   odrive axis.request_state = AXIS_STATE_IDLE
   odrive axis.encoder.set_zero_count()
```

---

## 9. Phase 8: System Calibration

### Step 9.1: Balance Calibration

```
PROCEDURE:
1. Place robot on flat surface, powered on, standing
2. Read BNO085 IMU: accel, gyro, mag
3. Record static lean angle: should be <2° in all axes
4. If lean exists, adjust CG by repositioning batteries
5. Record balance PID gains (initial values):
   - Kp = 0.5
   - Ki = 0.1
   - Kd = 0.05
6. Fine-tune during walking tests
```

### Step 9.2: Gait Calibration

```
PROCEDURE:
1. Enter safe mode (reduced speed)
2. Command walking gait at 0.5 km/h
3. Monitor foot pressure sensors during gait cycle
4. Adjust:
   - Stride length: 300mm (initial)
   - Step height: 50mm (initial)
   - Cadence: 1.5 Hz (initial)
5. Record gait parameters in calibration log
6. Increase speed incrementally to 5 km/h
```

### Step 9.3: Hand Calibration

```
PROCEDURE:
1. Command each finger to open (0°) and close (90°)
2. Record servo position at each endpoint
3. Calibrate force sensors:
   - 0N: record ADC value
   - 5N: apply calibrated weight, record ADC value
   - Linear fit: Force = m × ADC + b
4. Test grasp: pick up various objects (ball, cup, pen)
5. Adjust grip force limits: max 10N per finger
```

---

## 10. Assembly Checklist

```
□ Frame assembled and rigid
□ All actuators installed and wiring routed
□ All encoders installed and magnets aligned
□ CAN bus connected and terminated
□ I2C/SPI buses connected and pull-ups installed
□ Power distribution wired and fuses installed
□ Emergency stop tested (both buttons)
□ Battery pack connected and BMS verified
□ RPi 5 booted and Coral TPU detected
□ All ODrives firmware flashed and configured
□ Motor calibration completed for all 30 DOF
□ Encoder calibration completed
□ Balance calibration completed
□ Gait calibration completed (walking at 5 km/h)
□ Hand calibration completed
□ Audio system tested (microphones + speakers)
□ Camera system tested (stereo vision)
□ Eye displays working
□ Cooling fans operational
□ All sensors reading correctly
□ IP54 sealing verified
```

---

*Document: 05_ASSEMBLY.md — PHI_HUMANOID_ROBOT Assembly Guide*
*Version: 1.0 | Date: 2026-08-27*
