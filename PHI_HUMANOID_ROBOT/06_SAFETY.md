# PHI_HUMANOID_ROBOT — Safety Systems

## Safety Design, Risk Assessment & Emergency Procedures

---

## 1. Safety Philosophy

The PHI_HUMANOID_ROBOT follows a **fail-safe** design philosophy: any single failure mode must result in the robot entering a safe state (stopped, powered down, or limping). No single point of failure can cause uncontrolled motion.

### 1.1 Safety Principles

| Principle | Implementation |
|-----------|---------------|
| Fail-safe | E-stop opens contactor on any fault |
| Redundant | Dual e-stop buttons, dual power buses |
| Graceful degradation | Limb failure → reduce speed → stop |
| Human proximity | Reduce force/speed when humans detected |
| Software watchdog | 2-second timeout → motor disable |
| Hardware watchdog | Independent timer → contactor open |

---

## 2. Emergency Stop System

### 2.1 Hardware E-Stop (Primary)

```
┌─────────────────────────────────────────────────────────────────┐
│                    DUAL REDUNDANT E-STOP                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐                    │
│  │ E-STOP  │    │ E-STOP  │    │ CONTACTOR│                    │
│  │ BUTTON 1│    │ BUTTON 2│    │ (100A)   │                    │
│  │ (Head)  │    │ (Torso) │    │          │                    │
│  │  NC     │    │  NC     │    │  Coil    │                    │
│  │  30A    │    │  30A    │    │  48V     │                    │
│  └────┬────┘    └────┬────┘    └────┬────┘                    │
│       │              │              │                          │
│       └──────────────┼──────────────┘                          │
│                      │ SERIES WIRING                             │
│                      │ Both must be CLOSED                      │
│                      │ for robot to operate                     │
│                      │                                           │
│                      │ If ANY button pressed                    │
│                      │ OR wiring broken                         │
│                      │ OR power lost                            │
│                      │ → Contactor OPENS                        │
│                      │ → ALL 48V POWER CUT                      │
│                      │ → Robot STOPS                            │
│                                                                 │
│  ACTUATION FORCE: 5-10N (easy to press in emergency)           │
│  RELEASE: Twist-to-release (prevents accidental restart)       │
│  PLACEMENT: Head (always reachable) + Torso (chest-level)      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Software E-Stop (Secondary)

```
┌─────────────────────────────────────────────────────────────────┐
│                    SOFTWARE E-STOP LAYERS                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Layer 1: User Command                                          │
│  ├── WiFi app "Emergency Stop" button                          │
│  ├── Voice command: "Emergency stop" / "Stop robot"            │
│  └── Keyboard shortcut: Ctrl+Shift+E                           │
│                                                                 │
│  Layer 2: Software Watchdog                                     │
│  ├── RPi 5 heartbeats to STM32 every 100ms                    │
│  ├── If 2 heartbeats missed (200ms): disable all motors        │
│  ├── If 20 heartbeats missed (2s): open contactor              │
│  └── Independent hardware timer backup                         │
│                                                                 │
│  Layer 3: Sensor Fault Detection                                │
│  ├── Encoder error: Motor deviation >5° → disable motor        │
│  ├── Current spike: >120% rated → disable motor                │
│  ├── Temperature: Motor >80°C → reduce power                   │
│  ├── Temperature: Board >70°C → emergency stop                 │
│  ├── IMU fault: No data for 100ms → enter balance mode         │
│  └── Voltage: <40V (pack low) → enter safe mode                │
│                                                                 │
│  Layer 4: Proximity Detection                                   │
│  ├── Ultrasonic detects object <300mm → reduce speed           │
│  ├── Object <100mm → stop forward motion                       │
│  └── Force sensor >5N unexpected → retract hand                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. Risk Assessment Matrix

### 3.1 Hazard Identification

| # | Hazard | Severity | Probability | Risk Level | Mitigation |
|---|--------|----------|-------------|------------|------------|
| H-01 | Uncontrolled joint motion | Critical | Low | HIGH | E-stop, current limits, encoder monitoring |
| H-02 | Robot falls on person | Critical | Low | HIGH | Balance system, proximity detection, slow mode |
| H-03 | Pinch point at joints | Serious | Medium | HIGH | Joint covers, force limiting, speed limiting |
| H-04 | Electrical shock (48V) | Serious | Low | MEDIUM | Insulated wiring, IP54, proper grounding |
| H-05 | Battery thermal runaway | Critical | Very Low | MEDIUM | BMS, thermal cutoff, LiFePO4 chemistry |
| H-06 | Sharp edges (frame) | Minor | Medium | LOW | Deburred edges, protective covers |
| H-07 | Noise (motors) | Minor | High | LOW | Motor current limiting, sound dampening |
| H-08 | Tripping hazard (cables) | Minor | Medium | LOW | Internal cable routing, no external cables |
| H-09 | Fire (electronics) | Serious | Very Low | MEDIUM | Fuses, thermal cutoffs, conformal coating |
| H-10 | Entanglement (loose clothing) | Serious | Low | MEDIUM | Warning labels, smooth outer shell |

### 3.2 Risk Matrix

```
                    PROBABILITY
                    Low     Medium    High
              ┌──────────┬──────────┬──────────┐
    Critical  │  HIGH    │  HIGH    │ CRITICAL │
              ├──────────┼──────────┼──────────┤
SEVERITY      │  MEDIUM  │  HIGH    │  HIGH    │
    Serious   │          │          │          │
              ├──────────┼──────────┼──────────┤
    Minor     │  LOW     │  MEDIUM  │  MEDIUM  │
              └──────────┴──────────┴──────────┘
```

---

## 4. Mechanical Safety

### 4.1 Joint Torque Limits

| Joint | Max Torque | Human Equivalent | Limit Method |
|-------|-----------|------------------|--------------|
| Hip | 14.5 Nm | Moderate push | Current limit in ODrive |
| Knee | 14.5 Nm | Moderate push | Current limit in ODrive |
| Ankle | 4.8 Nm | Light push | Current limit in ODrive |
| Shoulder | 4.8 Nm | Light push | Current limit in ODrive |
| Elbow | 4.8 Nm | Light push | Current limit in ODrive |
| Wrist | 1.2 Nm | Finger-strength | Current limit in ODrive |
| Torso | 14.5 Nm | Moderate push | Current limit in ODrive |
| Head | 1.2 Nm | Finger-strength | Current limit in ODrive |
| Fingers | 0.52 Nm | Grip strength | Dynamixel current limit |

### 4.2 Speed Limits

| Condition | Max Speed | Rationale |
|-----------|-----------|-----------|
| Normal walking | 5 km/h | Comfortable human pace |
| Running | 10 km/h | Maximum design speed |
| Human proximity (<2m) | 1 km/h | Safety buffer |
| Human proximity (<500mm) | 0 km/h | Stop |
| Unknown terrain | 2 km/h | Conservative |
| Emergency recovery | 0.5 km/h | Minimal risk |
| Hand manipulation | 30°/s | Prevent pinching |
| Head movement | 60°/s | Prevent whiplash |

### 4.3 Pinch Point Protection

```
JOINT COVER DESIGN:
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  ALL rotating joints are enclosed in φ-ratio TPU covers        │
│  ├── Material: TPU 85A durometer                               │
│  ├── Thickness: 3mm                                             │
│  ├── Coverage: 360° around joint axis                          │
│  ├── Opening: <10mm gap (finger cannot enter)                  │
│  ├── Color: Safety yellow with φ-pattern markings              │
│  └── Attachment: Snap-fit with tool-required removal            │
│                                                                 │
│  MAX GAP SIZES:                                                 │
│  ├── Moving parts: <8mm (finger-proof)                         │
│  ├── Stationary parts: <12mm (child-proof)                     │
│  └── After cover installation: <5mm everywhere                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5. Electrical Safety

### 5.1 Voltage Isolation

```
┌─────────────────────────────────────────────────────────────────┐
│                    VOLTAGE ISOLATION ZONES                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ZONE 1: HIGH VOLTAGE (48V DC)                                 │
│  ├── Battery pack                                              │
│  ├── Main contactor                                            │
│  ├── Power distribution PCB                                    │
│  ├── ODrive VBUS inputs                                        │
│  ├── Buck converter inputs                                     │
│  └── INSULATION: All 48V wiring is color-coded RED             │
│                   and routed in separate conduit                │
│                   from signal wiring                            │
│                                                                 │
│  ZONE 2: MEDIUM VOLTAGE (12V DC)                               │
│  ├── Motor power (12V bus)                                     │
│  ├── Buck converter outputs                                    │
│  └── INSULATION: Color-coded ORANGE                            │
│                                                                 │
│  ZONE 3: LOW VOLTAGE (5V DC)                                   │
│  ├── RPi 5 power                                              │
│  ├── Dynamixel servos                                          │
│  ├── Amplifier                                                 │
│  └── INSULATION: Color-coded YELLOW                            │
│                                                                 │
│  ZONE 4: SIGNAL (3.3V DC)                                      │
│  ├── Sensors                                                   │
│  ├── Encoders                                                  │
│  ├── IMUs                                                      │
│  └── INSULATION: Color-coded GREEN                             │
│                                                                 │
│  ZONE SEPARATION: Minimum 10mm between zones                   │
│  GROUND PLANE: Continuous under all zones                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 5.2 Current Protection

| Circuit | Fuse Rating | Trip Time | Purpose |
|---------|------------|-----------|---------|
| Main 48V bus | 80A | Slow-blow, 5s | Pack-level protection |
| Left limb 12V | 20A | Fast-blow, 100ms | Motor overcurrent |
| Right limb 12V | 20A | Fast-blow, 100ms | Motor overcurrent |
| Logic 5V | 10A | Fast-blow, 50ms | Electronics protection |
| Head 5V | 5A | Fast-blow, 50ms | Head subsystem |
| USB power | 2A | Polyfuse | USB device protection |

### 5.3 Grounding

```
GROUNDING SCHEME:
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  Star ground topology:                                         │
│  All grounds converge at SINGLE POINT on pelvis plate          │
│                                                                 │
│  ┌──────────┐                                                  │
│  │ Battery  │                                                  │
│  │ Negative │                                                  │
│  └────┬─────┘                                                  │
│       │                                                        │
│  ┌────┴─────┐                                                  │
│  │ STAR     │                                                  │
│  │ GROUND   │                                                  │
│  │ POINT    │                                                  │
│  │ (Pelvis) │                                                  │
│  └────┬─────┘                                                  │
│       │                                                        │
│  ┌────┼──────┬──────┬──────┬──────┬──────┐                    │
│  │    │      │      │      │      │      │                    │
│  GND  GND   GND    GND    GND    GND    GND                   │
│  Left Right Left   Right  Torso  Head   Frame                 │
│  Leg  Leg   Arm    Arm                               │
│                                                                 │
│  Earth ground: Optional via 3-prong power connector            │
│  when charging (not during battery operation)                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 6. Battery Safety

### 6.1 LiFePO4 Chemistry Advantages

| Property | LiFePO4 | NMC Li-ion | Lead Acid |
|----------|---------|------------|-----------|
| Thermal runaway | >270°C | >150°C | N/A |
| Cycle life | 2000+ | 500 | 300 |
| Calendar life | 10+ years | 5 years | 3 years |
| Abuse tolerance | High | Medium | High |
| Toxicity | Low | Medium | High |
| Cost (per kWh) | $300 | $150 | $100 |

### 6.2 Battery Management System (BMS)

```
FPB-10 INTERNAL BMS:
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  Cell Balancing: Active balancing circuit                       │
│  ├── Balancing current: 2A per cell                            │
│  ├── Threshold: >50mV imbalance triggers balancing             │
│  └── Method: Shuttle capacitor                                │
│                                                                 │
│  Overcharge Protection:                                         │
│  ├── Cutoff voltage: 3.65V/cell (14.6V per module)            │
│  ├── Triggers MOSFET disconnect at pack level                  │
│  └── Recovery: Automatic when voltage drops below 3.5V        │
│                                                                 │
│  Overdischarge Protection:                                      │
│  ├── Cutoff voltage: 2.5V/cell (10.0V per module)             │
│  ├── Warning at 2.8V/cell (11.2V per module)                  │
│  └── Recovery: Automatic when charging resumes                 │
│                                                                 │
│  Overcurrent Protection:                                        │
│  ├── Discharge limit: 50A per module                           │
│  ├── Short circuit: <100µs response                            │
│  └── Recovery: Automatic after 5 seconds                       │
│                                                                 │
│  Temperature Protection:                                        │
│  ├── Charge cutoff: 0°C to 45°C                               │
│  ├── Discharge cutoff: -20°C to 60°C                          │
│  ├── Thermal runaway monitoring: NTC thermistors per cell group│
│  └── Fan control: Active cooling above 40°C                   │
│                                                                 │
│  Communication:                                                 │
│  ├── CAN bus reporting: SOC, voltage, current, temp           │
│  └── Update rate: 10 Hz                                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. Thermal Safety

### 7.1 Temperature Monitoring Points

| Sensor Location | Threshold | Action |
|----------------|-----------|--------|
| Motor winding (hip) | >80°C | Reduce current 50% |
| Motor winding (hip) | >100°C | Disable motor |
| Motor winding (knee) | >80°C | Reduce current 50% |
| Motor winding (knee) | >100°C | Disable motor |
| ODrive controller | >70°C | Reduce power |
| ODrive controller | >85°C | Emergency stop |
| Battery pack | >45°C | Reduce charge rate |
| Battery pack | >55°C | Stop charging |
| Battery pack | >60°C | Emergency stop |
| RPi 5 CPU | >80°C | Throttle CPU |
| Ambient inside torso | >50°C | Activate fans |
| Ambient inside torso | >60°C | Emergency stop |

### 7.2 Cooling System

```
ACTIVE COOLING:
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  4× Noctua 40mm fans (5V PWM)                                 │
│  ├── Fan 1: Torso intake (bottom)                              │
│  ├── Fan 2: Torso exhaust (top)                                │
│  ├── Fan 3: Head (processor cooling)                           │
│  └── Fan 4: Battery compartment                                │
│                                                                 │
│  FAN CONTROL:                                                  │
│  ├── Below 40°C: Fans OFF                                     │
│  ├── 40°C - 50°C: Fans at 50% speed                           │
│  ├── 50°C - 60°C: Fans at 100% speed                          │
│  └── Above 60°C: Emergency stop                                │
│                                                                 │
│  PASSIVE COOLING:                                              │
│  ├── Aluminum frame acts as heat sink                          │
│  ├── Thermal pads on motor housings                            │
│  └── φ-ratio fin spacing for optimal convection               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 8. Software Safety

### 8.1 Safety State Machine

```
┌─────────────────────────────────────────────────────────────────┐
│                    SAFETY STATE MACHINE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────┐     ┌──────────┐     ┌──────────┐              │
│  │  SAFE    │────▶│  READY   │────▶│ WALKING  │              │
│  │  STATE   │     │  STATE   │     │  STATE   │              │
│  └──────────┘     └──────────┘     └──────────┘              │
│       ▲                ▲                 │                     │
│       │                │                 │                     │
│       │                │                 ▼                     │
│       │                │            ┌──────────┐              │
│       │                │            │ RUNNING  │              │
│       │                │            │  STATE   │              │
│       │                │            └──────────┘              │
│       │                │                 │                     │
│       │                │    E-STOP       │                     │
│       │                ├─────────────────┤                     │
│       │                │                 │                     │
│       └────────────────┴─────────────────┘                     │
│                                                                 │
│  TRANSITIONS:                                                  │
│  ├── Any → SAFE: E-stop pressed, fault detected, watchdog    │
│  ├── SAFE → READY: E-stop released, self-test passed         │
│  ├── READY → WALKING: User command                            │
│  ├── WALKING → RUNNING: User command + speed >5 km/h         │
│  ├── RUNNING → WALKING: User command or speed <5 km/h        │
│  └── Any → SAFE: Any critical fault                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 8.2 Fault Detection & Response

| Fault Type | Detection | Response | Recovery |
|-----------|-----------|----------|----------|
| Encoder failure | >5° deviation for 10ms | Disable affected motor | Recalibrate |
| Motor overcurrent | >120% rated for 100ms | Disable affected motor | Restart after cooldown |
| Communication loss | CAN timeout 100ms | Enter balance mode | Reconnect |
| IMU failure | No data 100ms | Enter balance mode | Recalibrate |
| Vision failure | Camera disconnect 500ms | Reduce speed, alert | Reconnect |
| Battery low | SOC <15% | Reduce speed to 1 km/h | Charge |
| Battery critical | SOC <5% | Stop and power down | Charge |
| Temperature high | Sensor >80°C | Reduce power 50% | Cool down |
| Temperature critical | Sensor >100°C | Emergency stop | Cool down |
| Unknown object | Proximity <100mm | Stop forward motion | Navigate around |

---

## 9. User Safety Warnings

```
┌─────────────────────────────────────────────────────────────────┐
│                    SAFETY WARNING LABELS                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  LABEL 1 (Head):                                               │
│  "CAUTION: Robot in operation. Maintain 2m distance."          │
│  "EMERGENCY: Press red button on head to stop."                │
│                                                                 │
│  LABEL 2 (Torso):                                              │
│  "WARNING: 48V electrical system. Do not open."                │
│  "EMERGENCY: Press red button on chest to stop."               │
│                                                                 │
│  LABEL 3 (Back):                                               │
│  "DANGER: Pinch points at all joints. Keep clear."            │
│  "Weight: 50 kg. Do not attempt to lift."                      │
│                                                                 │
│  LABEL 4 (Battery compartment):                                │
│  "CAUTION: LiFePO4 battery. Do not puncture or short."        │
│  "Fire risk: Keep away from open flame."                       │
│                                                                 │
│  LABEL 5 (General):                                            │
│  "φ-HARMONIC HUMANOID ROBOT v1.0"                              │
│  "Not suitable for children under 14."                         │
│  "Adult supervision required during operation."                │
│  "Max payload: 5 kg. Do not exceed."                           │
│  "Operating temperature: 0°C to 30°C."                         │
│  "Do not operate in rain or wet conditions."                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 10. Emergency Procedures

### 10.1 Robot Falling

```
IF ROBOT DETECTS IMMINENT FALL:
1. Enter protective reflex mode
2. Extend arms to break fall (protect head)
3. Bend knees to absorb impact
4. Disable all motors after ground contact
5. Alert user via audio/visual

IF ROBOT HAS FALLEN:
1. All motors disabled (safe state)
2. User must right robot manually
3. Run self-diagnostic before re-enabling
4. Check for damage to frame/sensors
```

### 10.2 Battery Fire

```
IF BATTERY FIRE DETECTED:
1. DO NOT attempt to extinguish LiFePO4 fire with water
2. Evacuate area immediately
3. Use Class D fire extinguisher (lithium)
4. Call emergency services
5. Do not re-enter until area is declared safe

PREVENTION:
1. LiFePO4 chemistry is inherently safe
2. BMS monitors all cells
3. Thermal cutoff at 60°C
4. Ventilation in battery compartment
```

### 10.3 Uncontrolled Motion

```
IF ROBOT MOVES UNCONTROLLABLY:
1. Press E-STOP immediately (both buttons if possible)
2. If E-stop fails: Disconnect battery (pull XT90 connector)
3. Clear area of people and obstacles
4. Do not attempt to physically stop robot (50 kg, strong motors)
5. Wait for complete power-down before approaching

POST-INCIDENT:
1. Do not re-enable robot
2. Investigate root cause
3. Check all ODrive firmware for corruption
4. Recalibrate all motors
5. Full system test before returning to service
```

---

## 11. Maintenance Safety

| Task | Frequency | Safety Precaution |
|------|-----------|-------------------|
| Visual inspection | Before each use | Check for damage, loose bolts |
| Bolt torque check | Monthly | Use torque wrench, power OFF |
| Battery health check | Weekly | BMS report via app |
| Encoder calibration | Monthly | Power off, manual alignment |
| Motor resistance check | Quarterly | Power off, DMM measurement |
| Firmware update | As released | Backup config first |
| Lubrication | Every 200 hours | Power off, food-grade silicone |
| Deep clean | Monthly | Power off, compressed air |

---

*Document: 06_SAFETY.md — PHI_HUMANOID_ROBOT Safety Systems*
*Version: 1.0 | Date: 2026-08-27*
