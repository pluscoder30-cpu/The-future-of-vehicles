# PHI_HUMANOID_ROBOT — Owner's Manual

## Operating Instructions, Maintenance & Troubleshooting

---

## 1. Safety Warnings

```
⚠️  IMPORTANT SAFETY INFORMATION  ⚠️

READ BEFORE OPERATING THIS ROBOT

DANGER: Risk of serious injury
├── Robot weighs 50 kg (110 lb). Do not attempt to lift.
├── Motors produce up to 14.5 Nm torque. Keep clear of joints.
├── 48V electrical system. Do not open battery compartment.
└── Moving parts at all joints. Keep fingers clear.

WARNING: Risk of minor injury
├── Robot may move unexpectedly during calibration.
├── Pinch points at all joints (covered, but exercise caution).
├── Loud motor noise during operation (>60 dB at 1m).
└── Battery may become warm during charging.

CAUTION: Property damage risk
├── Do not operate on uneven surfaces.
├── Keep away from water and moisture.
├── Do not exceed 5 kg payload.
└── Do not operate in temperatures outside 0-30°C.

KEEP THIS MANUAL FOR FUTURE REFERENCE
```

---

## 2. Before You Begin

### 2.1 Unboxing Checklist

```
□ Robot (assembled)
□ Charger (48V, XT90 connector)
□ Power adapter (for RPi 5)
□ USB cable (USB-C to USB-A)
□ Emergency stop key (2×)
□ Allen key set (metric)
□ Spare fuses (80A ×1, 20A ×2, 10A ×2, 5A ×1)
□ Quick start card
□ This manual
```

### 2.2 Initial Inspection

```
VISUAL INSPECTION:
□ No visible damage to frame
□ All joint covers intact
□ Battery compartment closed
□ Emergency stop buttons functional
□ No loose wires or connectors
□ Foot pads intact
□ Head shell secure
□ Hand fingers move freely
```

### 2.3 Charging

```
CHARGING PROCEDURE:
1. Ensure robot is powered OFF
2. Locate charging port (back of torso, XT90 connector)
3. Connect charger to charging port
4. Connect charger to wall outlet (120V/240V AC)
5. Wait for charger LED to turn green (fully charged)
6. Disconnect charger from robot FIRST, then wall

CHARGE TIMES:
├── 0% to 80%: ~2 hours
├── 0% to 100%: ~2.5 hours
└── Charging indicator: Charger LED (red=charging, green=done)

BATTERY INDICATION:
├── OLED eyes: Battery icon (4 bars)
├── Voice: "Battery at XX percent"
└── App: Real-time SOC display

DO NOT:
├── Charge in direct sunlight
├── Charge below 0°C or above 40°C
├── Use non-approved charger
├── Charge unattended overnight (first 10 charges)
└── Charge if battery is damaged or swollen
```

---

## 3. Powering On

### 3.1 Startup Sequence

```
POWER-ON PROCEDURE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ENSURE AREA IS CLEAR
   ├── Minimum 2m clearance around robot
   ├── No objects in walking path
   └── No people within 2m

2. RELEASE E-STOP
   ├── Twist red buttons on head and torso to release
   ├── Buttons should pop out
   └── If buttons won't release: Check battery connection

3. PRESS POWER BUTTON
   ├── Location: Left side of torso
   ├── Press and hold for 2 seconds
   ├── Power LED turns blue
   └── Robot beeps once (startup tone)

4. WAIT FOR BOOT SEQUENCE
   ├── RPi 5 boots: ~30 seconds
   ├── Coral TPU initializes: ~5 seconds
   ├── Motor calibration: ~10 seconds
   ├── Sensor check: ~5 seconds
   └── Total boot time: ~50 seconds

5. STANDBY STATE
   ├── Robot stands in idle position
   ├── OLED eyes show "ready" animation
   ├── Status LED: Solid green
   └── Robot is ready for commands
```

### 3.2 LED Indicators

```
STATUS LED (torso, front):
├── Solid Green: Ready, all systems nominal
├── Blinking Green: Processing / in motion
├── Solid Yellow: Low battery (<20%)
├── Blinking Yellow: Warning (temperature, proximity)
├── Solid Red: Fault detected
├── Blinking Red: Critical fault, e-stop recommended
└── Off: Power off or e-stop engaged

OLED EYES:
├── Normal: Two white circles (eyes)
├── Speaking: Mouth animation
├── Thinking: Spinning φ-symbol
├── Happy: ^_^ expression
├── Sad: ;_; expression
├── Alert: ! ! expression
├── Low battery: Battery icon
└── Error: X X expression
```

---

## 4. Basic Operation

### 4.1 Voice Commands

```
VOICE COMMAND LIST:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MOVEMENT:
├── "Walk forward" — Start walking forward at 5 km/h
├── "Walk backward" — Walk backward at 2 km/h
├── "Turn left" — Turn 90° left
├── "Turn right" — Turn 90° right
├── "Run" — Start running at 10 km/h
├── "Stop" — Stop all motion immediately
├── "Stand still" — Return to idle standing
└── "Follow me" — Follow the user (voice tracking)

MANIPULATION:
├── "Pick up [object]" — Grasp specified object
├── "Put down" — Release current grasp
├── "Wave" — Wave hand gesture
├── "Shake hands" — Extend hand for handshake
└── "Point at [direction]" — Point gesture

INFORMATION:
├── "Status" — Report battery, temperature, errors
├── "What do you see?" — Describe visual scene
├── "What time is it?" — Report current time
├── "Where am I?" — Report last known location
└── "Battery" — Report battery percentage

SYSTEM:
├── "Emergency stop" — Stop all motion (alternative to button)
├── "Sleep" — Enter low-power sleep mode
├── "Wake up" — Exit sleep mode
├── "Calibrate" — Enter calibration mode
└── "Restart" — Soft restart (saves state)

 phi-SPECIFIC:
├── "φ-harmonic balance" — Recalibrate balance system
├── "φ-gait optimize" — Reoptimize gait parameters
└── "φ-voice tune" — Adjust voice synthesis parameters
```

### 4.2 App Control

```
MOBILE APP (WiFi):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Connect phone to robot WiFi network
   ├── SSID: PHI_ROBOT_XXXX (last 4 of serial)
   ├── Password: phi12345 (change on first use)

2. Open PHI_HUMANOID app (iOS/Android)

3. Main screen:
   ├── Joystick: Manual joint control
   ├── Walk button: Start/stop walking
   ├── Grasp button: Open/close hands
   ├── Camera feed: Live view from robot eyes
   ├── Status: Battery, temperature, errors
   └── Settings: Speed limits, safety parameters

4. Advanced mode:
   ├── Individual joint control (30 DOF)
   ├── Trajectory recording
   ├── φ-harmonic parameter tuning
   ├── Diagnostic readings
   └── Firmware update
```

### 4.3 Manual Control (Emergency)

```
MANUAL OVERRIDE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

If robot is unresponsive:

1. PRESS E-STOP
   ├── Head button (red, twist to activate)
   ├── Torso button (red, twist to activate)
   └── Both buttons stop all motion

2. WAIT 5 SECONDS
   ├── All motors will free-spin
   ├── Robot may lean or fall
   └── Be prepared to support robot

3. POWER OFF
   ├── Hold power button for 5 seconds
   ├── Or disconnect battery (XT90 connector)
   └── Wait for all LEDs to turn off

4. INSPECT
   ├── Check for damage
   ├── Check for loose connections
   └── Check battery status

5. RESTART
   ├── Follow startup procedure
   ├── If problem persists: See troubleshooting
```

---

## 5. Walking & Movement

### 5.1 Walking Mode

```
WALKING MODE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Starting to walk:
1. Ensure area is clear (2m minimum)
2. Say "Walk forward" or press Walk button
3. Robot will:
   a. Shift weight to right leg
   b. Lift left leg
   c. Step forward (306mm)
   d. Place left foot
   e. Shift weight to left leg
   f. Lift right leg
   g. Step forward (306mm)
   h. Place right foot
   i. Repeat

Walking characteristics:
├── Speed: 5 km/h (adjustable via app)
├── Step height: 76mm
├── Step length: 306mm
├── Cadence: 1.5 Hz (90 steps/min)
├── Turning radius: 611mm
└── Obstacle detection: 1m forward (auto-stop)

Stopping:
├── Say "Stop" — Gradual stop (2 steps)
├── Press Walk button — Gradual stop
├── Press E-stop — Immediate stop
└── Voice: "Emergency stop" — Immediate stop

Walking on slopes:
├── Maximum slope: 5° sustained
├── Maximum step: 100mm
├── Uneven terrain: Reduced speed (2 km/h)
└── Wet surfaces: DO NOT WALK
```

### 5.2 Running Mode

```
RUNNING MODE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Starting to run:
1. Must be in walking mode first
2. Say "Run" or increase speed in app
3. Robot accelerates gradually to 10 km/h

Running characteristics:
├── Speed: 10 km/h (adjustable via app)
├── Flight phase: 20% of gait cycle
├── Impact force: <3× body weight
├── Step frequency: 2.5 Hz
└── Energy consumption: 2× walking mode

Safety:
├── Minimum clear area: 5m forward
├── Maximum slope: 2° (less than walking)
├── No running on stairs
├── No running with payload
└── Automatic slow-down if battery <20%
```

---

## 6. Manipulation

### 6.1 Grasping Objects

```
GRASPING PROCEDURE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. IDENTIFY OBJECT
   ├── Say "Pick up [object name]"
   ├── Or use app to select object in camera view
   └── Robot will locate object using vision

2. APPROACH
   ├── Robot positions hand near object
   ├── Distance: 100-300mm from object
   └── Hand orientation: Pre-shaped for grasp type

3. GRASP
   ├── Fingers close in Fibonacci sequence
   ├── Thumb + Index → Middle → Ring → Pinky
   ├── Force: Adjustable (default: 5N per finger)
   └── Time: ~500ms per grasp

4. CONFIRM
   ├── FSR sensors verify grasp stability
   ├── If unstable: Regrasp attempt (3 tries)
   ├── If failed: Report "Cannot grasp object"
   └── If successful: Report "Grasped [object]"

5. MANIPULATE
   ├── Hold object at current position
   ├── Or follow voice commands:
   │   ├── "Move left/right/up/down"
   │   ├── "Rotate clockwise/counterclockwise"
   │   └── "Bring to me"
   └── Or use app for manual control

6. RELEASE
   ├── Say "Put down" or press Grasp button
   ├── Fingers open in reverse order
   ├── Pinky → Ring → Middle → Index + Thumb
   └── Object released gently
```

### 6.2 Grasp Types

```
AVAILABLE GRASPS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Power Grasp (default):
├── All 5 fingers wrap around object
├── Force: 10N total (distributed by φ-ratio)
├── Best for: Cylindrical objects (bottles, cups)
└── Object size: 30-100mm diameter

Pinch Grasp:
├── Thumb + Index finger tips
├── Force: 2N per finger
├── Best for: Small objects (keys, pens)
└── Object size: 1-20mm

Tripod Grasp:
├── Thumb + Index + Middle
├── Force: 5N total
├── Best for: Medium objects (phone, remote)
└── Object size: 20-80mm

Hook Grasp:
├── Middle + Ring + Pinky (no thumb)
├── Force: 7N total
├── Best for: Hanging objects (bags, handles)
└── Object size: Variable

Spherical Grasp:
├── All 5 fingers, spread position
├── Force: 8N total
├── Best for: Spherical objects (balls, oranges)
└── Object size: 40-150mm diameter
```

---

## 7. Maintenance

### 7.1 Daily Maintenance

```
BEFORE EACH USE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

□ Visual inspection (1 minute)
  ├── Check frame for damage
  ├── Check joint covers
  ├── Check foot pads
  ├── Check head shell
  └── Check for loose wires

□ Battery check (30 seconds)
  ├── Verify SOC > 20%
  ├── Check charge port (no debris)
  └── Verify charger is available

□ Functional check (2 minutes)
  ├── Power on, verify boot completes
  ├── Check e-stop buttons (press/release)
  ├── Check all joints move (test mode)
  ├── Check camera feed
  ├── Check microphone (speak test)
  └── Check speakers (play test tone)
```

### 7.2 Weekly Maintenance

```
WEEKLY CHECKS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

□ Bolt torque check (5 minutes)
  ├── Hip bolts: 4 Nm
  ├── Knee bolts: 4 Nm
  ├── Shoulder bolts: 2.5 Nm
  ├── Elbow bolts: 2.5 Nm
  ├── Hand bolts: 1.0 Nm
  └── Frame bolts: 2.5 Nm

□ Cable inspection (3 minutes)
  ├── Check for pinched cables at joints
  ├── Check connector security
  ├── Check for worn insulation
  └── Verify cable routing clips intact

□ Sensor check (3 minutes)
  ├── Run diagnostic mode
  ├── Verify all encoders reading
  ├── Verify IMU calibration
  ├── Verify force sensors reading
  └── Verify cameras aligned

□ Cleaning (5 minutes)
  ├── Blow dust from joints with compressed air
  ├── Wipe frame with damp cloth
  ├── Clean camera lenses
  └── Clean OLED displays
```

### 7.3 Monthly Maintenance

```
MONTHLY CHECKS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

□ Encoder calibration (10 minutes)
  ├── Enter calibration mode
  ├── Verify each encoder reads 0° at home position
  ├── Recalibrate if offset > 0.5°
  └── Record calibration values

□ Motor resistance check (15 minutes)
  ├── Power OFF, disconnect battery
  ├── Measure motor phase resistance (DMM)
  ├── Compare to spec:
  │   ├── D6374: 0.3Ω ± 10%
  │   ├── D5065: 0.5Ω ± 10%
  │   └── M5671: 1.2Ω ± 10%
  └── Record values

□ Battery health check (5 minutes)
  ├── Check cycle count via app
  ├── Check capacity fade estimation
  ├── Check internal resistance
  └── Record battery health score

□ Firmware update check (5 minutes)
  ├── Check for ODrive firmware updates
  ├── Check for RPi software updates
  ├── Check for Coral TPU model updates
  └── Update if available

□ Lubrication (10 minutes)
  ├── Apply food-grade silicone to joint bearings
  ├── Wipe excess
  └── Verify smooth joint motion
```

### 7.4 Battery Care

```
BATTERY MAINTENANCE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DO:
├── Charge regularly (don't let SOC drop below 10%)
├── Store at 50% SOC if not using for >1 week
├── Charge in cool environment (15-25°C optimal)
├── Use only approved charger
└── Cycle battery fully (0-100%) once per month

DO NOT:
├── Deep discharge (below 5% SOC)
├── Leave fully charged for extended periods (>1 week)
├── Charge in extreme temperatures (<5°C or >40°C)
├── Use non-approved charger
├── Expose to water or moisture
├── Puncture, crush, or disassemble battery
└── Dispose of in household waste

BATTERY REPLACEMENT:
├── When: Health score < 80% or cycle count > 2000
├── How: Contact manufacturer for replacement module
├── Cost: ~$450 per module (at retail)
└── Disposal: Return to manufacturer for recycling
```

---

## 8. Troubleshooting

### 8.1 Common Issues

```
ISSUE: Robot won't power on
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECK:
1. Is battery charged? (Check charger LED)
2. Is e-stop released? (Twist red buttons)
3. Is power button held for 2+ seconds?
4. Is battery connected? (Check XT90 connector)
5. Is main fuse intact? (Check 80A fuse)

IF NOT RESOLVED:
├── Try different battery module
├── Check power distribution PCB
├── Check contactor (should click on power-on)
└── Contact support

ISSUE: Robot falls over
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECK:
1. Is surface flat and level?
2. Is battery weight centered?
3. Are all joint covers intact?
4. Is IMU calibrated?
5. Are foot pads intact?

IF NOT RESOLVED:
├── Recalibrate balance: "φ-harmonic balance"
├── Check IMU mounting (BNO085)
├── Check foot pressure sensors
├── Adjust CG by repositioning batteries
└── Contact support

ISSUE: Robot walks erratically
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECK:
1. Are all encoders reading correctly?
2. Are motor torques within spec?
3. Is gait calibration current?
4. Are foot sensors reading correctly?
5. Is surface level?

IF NOT RESOLVED:
├── Recalibrate gait: "φ-gait optimize"
├── Check encoder alignment
├── Check motor resistance
├── Check CAN bus connections
└── Contact support

ISSUE: Voice commands not recognized
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECK:
1. Is room quiet? (<60 dB background)
2. Are you within 3m of robot?
3. Is microphone array unobstructed?
4. Is voice recognition enabled?
5. Is language set correctly?

IF NOT RESOLVED:
├── Reposition closer to robot
├── Speak clearly and slowly
├── Check microphone connections
├── Restart voice service
└── Contact support

ISSUE: Camera feed not working
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECK:
1. Are camera cables connected?
2. Is camera HAT detected?
3. Are camera lenses clean?
4. Is Coral TPU detected?
5. Is vision service running?

IF NOT RESOLVED:
├── Reseat camera cables
├── Check RPi camera interface (raspi-config)
├── Clean camera lenses
├── Restart vision service
└── Contact support
```

### 8.2 Error Codes

```
ERROR CODES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

E001: Motor overcurrent
├── Cause: Excessive load on joint
├── Action: Reduce payload, check joint for obstruction
└── Severity: High (motor protection active)

E002: Encoder failure
├── Cause: Encoder disconnected or faulty
├── Action: Check encoder wiring, recalibrate
└── Severity: High (motor disabled)

E003: IMU failure
├── Cause: IMU disconnected or faulty
├── Action: Check IMU wiring, recalibrate
└── Severity: High (balance system affected)

E004: Battery low
├── Cause: SOC < 15%
├── Action: Charge immediately
└── Severity: Medium (speed reduced)

E005: Temperature high
├── Cause: Motor or board temperature > 70°C
├── Action: Reduce speed, allow cooling
└── Severity: Medium (power reduced)

E006: Communication loss
├── Cause: CAN bus timeout
├── Action: Check CAN wiring, restart system
└── Severity: High (motor control affected)

E007: Balance fault
├── Cause: IMU data inconsistent
├── Action: Recalibrate balance, check IMU
└── Severity: High (fall risk)

E008: Vision failure
├── Cause: Camera or Coral TPU error
├── Action: Check camera cables, restart vision
└── Severity: Low (navigation affected)

E009: Emergency stop active
├── Cause: E-stop button pressed
├── Action: Release e-stop (twist buttons)
└── Severity: Informational

E010: Software fault
├── Cause: Software exception
├── Action: Restart system
└── Severity: Medium (system restart required)
```

---

## 9. Specifications

```
TECHNICAL SPECIFICATIONS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHYSICAL:
├── Height: 1600 mm (63.0 in)
├── Weight: 50 kg (110 lb)
├── Width: 600 mm (shoulder to shoulder)
├── Depth: 400 mm (front to back)
├── Foot size: 250 mm × 100 mm
└── IP rating: IP54 (splash-proof)

PERFORMANCE:
├── Walking speed: 5 km/h (3.1 mph)
├── Running speed: 10 km/h (6.2 mph)
├── Battery life: 8 hours (mixed use)
├── Grasp force: 10 N (5 fingers)
├── Payload: 5 kg
├── DOF: 30
└── Noise: <60 dB at 1m

BATTERY:
├── Chemistry: LiFePO4
├── Voltage: 48V (nominal)
├── Capacity: 40 kWh (4 × 10 kWh)
├── Charge time: 2.5 hours
├── Cycle life: 2000+ cycles
└── Weight: 12 kg (4 × 3 kg)

COMPUTE:
├── Processor: Raspberry Pi 5 (8GB)
├── AI accelerator: Coral TPU (4 TOPS)
├── Storage: 256GB NVMe SSD
├── Connectivity: WiFi, Bluetooth, CAN bus
└── OS: Ubuntu Server 24.04

SENSORS:
├── Cameras: 2× stereo (1280×800, 60fps)
├── Microphones: 4× MEMS array (48kHz, 24-bit)
├── IMU: 2× 9-DoF (BNO085 + BNO055)
├── Encoders: 28× 14-bit magnetic
├── Force sensors: 14× FSR
├── Proximity: 2× ToF + 2× ultrasonic
└── Temperature: 2× precision (±0.1°C)

ENVIRONMENTAL:
├── Operating temp: 0°C to 30°C
├── Storage temp: -20°C to 50°C
├── Humidity: 10% to 80% RH
├── Max slope: 5° sustained
├── Max step: 100 mm
└── Altitude: 0 to 2000 m
```

---

## 10. Warranty & Support

```
WARRANTY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Coverage: 1 year from purchase date
├── Frame and structure: 2 years
├── Motors and actuators: 1 year
├── Electronics: 1 year
├── Battery: 1 year (or 500 cycles, whichever first)
├── Software: Lifetime updates

Not covered:
├── Physical damage from misuse
├── Water damage
├── Unauthorized modifications
├── Normal wear (foot pads, joint covers)
└── Battery degradation below 80% capacity

SUPPORT:
├── Email: support@phi-humanoid.com
├── Phone: 1-800-PHI-BOT (1-800-744-268)
├── Web: phi-humanoid.com/support
├── Forum: community.phi-humanoid.com
└── Documentation: docs.phi-humanoid.com

REPAIR:
├── Self-repair: Allowed (voids warranty for modified parts)
├── Authorized repair: Contact support for RMA
├── Parts available: Yes (see parts list)
└── Turnaround: 2-4 weeks
```

---

## 11.φ-Harmonic Quick Reference

```
φ-HARMONIC CONSTANTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Golden Ratio: φ = 1.618033988749895...
Golden Angle: 137.5°
Inverse: 1/φ = 0.618033988749895...
Squared: φ² = 2.618033988749895...
Cubed: φ³ = 4.23606797749979...

Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

φ-APPLICATIONS IN THIS ROBOT:
├── Joint motor offset: 137.5°
├── Balance gain scaling: φ^(n/2)
├── Gait phase offset: 68.76°
├── Stride length: H/φ³
├── Finger activation order: Fibonacci sequence
├── Voice formant spacing: φ×F0
├── Structural member ratios: ≈φ
└── Hole patterns: φ-spiral
```

---

*Document: MANUAL.md — PHI_HUMANOID_ROBOT Owner's Manual*
*Version: 1.0 | Date: 2026-08-27*
