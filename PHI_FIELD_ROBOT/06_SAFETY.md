# PHI_FIELD_ROBOT — Safety Manual

## PHI_FIELD_ROBOT | Document 06: Safety Manual

---

## 1. SAFETY WARNINGS

### 1.1 DANGER — Electrical Hazard

```
⚠️ DANGER: HIGH VOLTAGE

The PHI_FIELD_ROBOT operates at 48V DC nominal.
This voltage can cause electric shock and burns.

• Never touch battery terminals with bare hands
• Never work on electrical system while powered
• Always disconnect both batteries before servicing
• Use insulated tools when working on power system
• Wear safety glasses and gloves at all times

Battery chemistry: LiFePO4 (Lithium Iron Phosphate)
• Do not short circuit
• Do not puncture
• Do not incinerate
• Do not expose to temperatures above 60°C
• Do not disassemble batteries
• Store in fireproof container if damaged
```

### 1.2 DANGER — Moving Parts

```
⚠️ DANGER: MOVING JOINTS

The PHI_FIELD_ROBOT has 17 motorized joints that can move
unexpectedly and with significant force.

• Keep hands, clothing, and hair away from joints
• Never step on or near the robot while powered
• Maintain 1m clearance when robot is active
• Use emergency stop immediately if person is at risk
• Children must not approach active robot
• Do not ride on or attach objects to moving robot

Joint forces:
• Hip/Knee: Up to 3.0 N·m (peak)
• Arm: Up to 1.0 N·m (continuous)
• Gripper: Up to 20N grip force

These forces can cause:
• Pinching injuries
• Bruising
• Broken fingers (gripper)
• Fractures (if caught in leg mechanism)
```

### 1.3 WARNING — Battery Safety

```
⚠️ WARNING: LITHIUM BATTERY

LiFePO4 batteries are generally safe but can be dangerous
if mishandled.

Do NOT:
• Short circuit terminals
• Overcharge (BMS prevents this normally)
• Over-discharge (BMS prevents this normally)
• Expose to fire
• Crush or puncture
• Use non-approved charger
• Mix old and new batteries
• Leave charging unattended for extended periods

Signs of battery damage:
• Swelling or bulging
• Hissing or venting gas
• Burning smell
• Discoloration
• Electrolyte leakage

If battery damage is suspected:
1. Press emergency stop immediately
2. Move robot to open, ventilated area
3. Do not touch damaged battery
4. Do not attempt to charge
5. Contact emergency services if fire
6. Use Class D fire extinguisher (lithium metal)
```

### 1.4 WARNING — Tipping Hazard

```
⚠️ WARNING: TIPPING

The robot can tip over on steep slopes or uneven terrain.

• Maximum slope: 30° static, 20° dynamic
• Do not operate on slopes steeper than 20°
• Do not place heavy loads on arm while on slope
• Do not walk robot near cliff edges
• Monitor battery level (low battery = unstable gait)

Anti-tip protection:
• IMU detects tipping angle
• Firmware automatically stops motion if angle >25°
• Emergency stop triggers at 35° angle
• Operator can manually trigger stop at any time
```

---

## 2. PERSONAL PROTECTIVE EQUIPMENT

### 2.1 Required PPE

| PPE | Specification | When |
|-----|---------------|------|
| Safety Glasses | ANSI Z87.1, impact rated | Always when robot is active |
| Work Gloves | Cut-resistant, ANSI A4 | When handling robot |
| Hearing Protection | NRR 25+ dB | When within 1m of active robot |
| Closed-toe Shoes | Steel-toe recommended | Always in work area |
| ESD Wrist Strap | 1MΩ resistor | When working on electronics |

### 2.2 Prohibited PPE

- Loose clothing (can catch in joints)
- Ties or scarves (entanglement hazard)
- Jewelry on hands or wrists (pinch hazard)
- Headphones (cannot hear robot warning sounds)

---

## 3. SAFE OPERATION PROCEDURES

### 3.1 Pre-Operation Checklist

```
□ Visual inspection complete (no damage)
□ All covers secured
□ Battery charged (>50%)
□ Emergency stop functional
□ Area clear of people (1m radius)
□ Area clear of obstacles
□ Terrain suitable (slope <20°)
□ Weather conditions acceptable (no rain)
□ Communication link active (if remote)
□ Operator trained and authorized
```

### 3.2 Operation Rules

**Rule 1: Always Maintain Line of Sight**
- Keep robot within visual range at all times
- If using cameras only, ensure adequate lighting
- Never operate robot where you cannot see it

**Rule 2: Always Have Emergency Stop Ready**
- Keep finger near e-stop button
- Know location of all e-stop buttons (robot + remote)
- Test e-stop at start of each session

**Rule 3: Never Approach Moving Robot**
- Maintain 1m clearance minimum
- Never reach into robot's workspace
- Never attempt to "help" a stuck robot manually

**Rule 4: Respect Load Limits**
- Arm payload: 10kg maximum
- Total robot weight: 30kg + 10kg payload
- Never exceed rated loads

**Rule 5: Stop if Uncertain**
- If anything seems wrong, press e-stop
- Investigate before resuming
- When in doubt, power down

### 3.3 Operating Environment

**Temperature:**
- Operating: -10°C to 45°C (14°F to 113°F)
- Storage: -20°C to 60°C (-4°F to 140°F)
- Battery charging: 0°C to 45°C (32°F to 113°F)

**Humidity:**
- Operating: 0-90% RH (non-condensing)
- Storage: 0-95% RH

**Precipitation:**
- Light rain: Acceptable (IP54 rated)
- Heavy rain: Not recommended
- Snow: Acceptable with caution
- Ice: Not recommended (slip hazard)

**Terrain:**
- Grass, dirt, gravel: Suitable
- Concrete, asphalt: Suitable
- Sand: Suitable (reduced speed)
- Mud: Suitable with caution
- Rocks: Suitable with caution
- Stairs: Capable (max 150mm step)
- Water: Not rated (avoid puddles >50mm depth)

---

## 4. EMERGENCY PROCEDURES

### 4.1 Emergency Stop Procedure

```
1. PRESS emergency stop button (mushroom head)
2. VERIFY robot has stopped completely
3. DO NOT approach until motion ceases
4. ASSESS situation before releasing e-stop
5. If person injured: Call emergency services
6. If fire: Evacuate and call fire department
7. If battery damage: Do not touch, ventilate area
```

### 4.2 Fire Emergency

```
1. Press emergency stop
2. Evacuate area (minimum 10m)
3. Call fire department (911)
4. Do NOT attempt to extinguish lithium battery fire
5. Use Class D extinguisher ONLY if trained
6. If fire spreads: Evacuate, let burn
7. Do not re-enter until cleared by fire department
```

### 4.3 Electrical Shock

```
1. Press emergency stop (if safe to do so)
2. Do NOT touch the person if still in contact with source
3. Disconnect power if possible without risk
4. Call emergency services (911)
5. Administer first aid if trained
6. Do not move injured person unless in immediate danger
```

### 4.4 Mechanical Injury

```
1. Press emergency stop immediately
2. Do NOT attempt to free person by reversing robot
3. If limb caught: Do NOT pull
4. Loosen bolts if necessary to free person
5. Call emergency services for serious injuries
6. Apply pressure to wounds
7. Keep victim calm and warm
```

---

## 5. CHILD SAFETY

### 5.1 Restrictions

- **Children under 16 must NOT operate robot**
- **Children under 12 must NOT approach active robot**
- **Children must be supervised by adults near robot**
- **Robot must be powered down when children are present in work area**

### 5.2 Child-Proof Features

- Emergency stop button requires deliberate press
- Power switch requires tool to access
- Battery bays have child-proof latches
- Gripper has force limit (20N max)
- Robot announces movement with audible warning

---

## 6. OPERATOR TRAINING

### 6.1 Required Training

| Module | Duration | Content |
|--------|----------|---------|
| Safety Basics | 2 hours | PPE, warnings, emergency procedures |
| Robot Controls | 4 hours | Start/stop, gait modes, arm control |
| Emergency Response | 2 hours | E-stop, fire, injury response |
| Maintenance Safety | 2 hours | Safe shutdown, lockout/tagout |
| Field Operations | 4 hours | Terrain, weather, load limits |
| **Total** | **14 hours** | |

### 6.2 Certification

- All operators must pass written exam (80% minimum)
- All operators must demonstrate practical skills
- Certification valid for 12 months
- Re-certification required after any incident
- Certification records maintained by safety officer

---

## 7. MAINTENANCE SAFETY

### 7.1 Lockout/Tagout Procedure

```
BEFORE ANY MAINTENANCE:

1. Notify all personnel
2. Press emergency stop
3. Power down robot (hold power button 5 seconds)
4. Disconnect both batteries (XT90 connectors)
5. Wait 5 minutes (capacitors discharge)
6. Verify zero voltage (multimeter)
7. Apply lockout tag to emergency stop
8. Apply lockout tag to battery bays
9. Begin maintenance only after verification
```

### 7.2 Battery Service

```
BATTERY REMOVAL:

1. Power down robot completely
2. Disconnect XT90 connectors (both batteries)
3. Wait 5 minutes
4. Release battery bay latch
5. Slide battery out using rail guides
6. Place in fireproof container
7. Label with date and condition

BATTERY INSTALLATION:

1. Verify battery condition (no damage)
2. Verify voltage (48V ±1V)
3. Slide battery into bay (rail guides)
4. Secure latch
5. Connect XT90 connector
6. Verify BMS status LED (green = OK)
7. Repeat for second battery
```

### 7.3 Joint Service

```
MOTOR REPLACEMENT:

1. Lockout/tagout robot
2. Disconnect battery
3. Remove leg from body (4× M4 bolts)
4. Disconnect CAN cable from motor
5. Remove motor mounting bolts (4× M3)
6. Remove motor from joint housing
7. Install new motor (reverse steps)
8. Torque all bolts to spec
9. Reconnect CAN cable
10. Re-attach leg to body
11. Test joint movement manually
12. Power on and test motor
```

---

## 8. RISK ASSESSMENT

### 8.1 Risk Matrix

| Hazard | Severity | Likelihood | Risk Level | Mitigation |
|--------|----------|-----------|------------|------------|
| Electric shock (48V) | Serious | Low | Medium | Insulated tools, e-stop |
| Pinch injury (joints) | Moderate | Medium | Medium | Clearance zone, PPE |
| Battery fire | Catastrophic | Very Low | Medium | BMS, fireproof storage |
| Tipping | Serious | Low | Low | IMU monitoring, slope limits |
| Tripping (cables) | Minor | Medium | Low | Cable management |
| Noise exposure | Minor | High | Medium | Hearing protection |
| Eye injury | Serious | Low | Low | Safety glasses |
| Crush injury (arm) | Serious | Low | Medium | Force limits, clearance |

### 8.2 Safety Features Summary

| Feature | Type | Description |
|---------|------|-------------|
| Emergency Stop | Hardware | Mushroom button, NC contact, <10ms response |
| Motor Current Limiting | Firmware | Per-motor overcurrent protection |
| Joint Torque Limits | Firmware | Software torque limits per joint |
| IMU Tipping Detection | Firmware | Auto-stop at 25° tilt |
| Battery BMS | Hardware | Overcharge, overdischarge, overcurrent, temp |
| Thermal Shutdown | Firmware | Pi/CPU temperature monitoring |
| Watchdog Timer | Hardware | System reset if firmware hangs |
| Audible Warning | Firmware | Beep before movement |
| LED Status | Firmware | Visual status indication |
| Force Limits | Firmware | Arm/gripper force limits |

---

## 9. INCIDENT REPORTING

### 9.1 Reportable Incidents

- Any injury to person
- Any property damage
- Any near-miss
- Any robot damage
- Any battery incident
- Any fire or smoke
- Any electrical incident
- Any unplanned shutdown

### 9.2 Reporting Procedure

```
1. Ensure safety of all personnel
2. Administer first aid if needed
3. Preserve scene (do not clean up)
4. Notify supervisor immediately
5. Complete incident report form (within 24 hours)
6. Investigate root cause
7. Implement corrective actions
8. Share lessons learned
```

---

## 10. COMPLIANCE

### 10.1 Applicable Standards

| Standard | Description | Status |
|----------|-------------|--------|
| ISO 13482 | Personal care robots safety | Compliant |
| ISO 10218 | Industrial robot safety | Partially applicable |
| IEC 62443 | Industrial cybersecurity | Recommended |
| NFPA 70 | National Electrical Code | Compliant |
| UL 3100 | Safety for mobile robots | Recommended |

### 10.2 Safety Documentation

| Document | Location | Last Updated |
|----------|----------|--------------|
| This Safety Manual | 06_SAFETY.md | 2026-08-27 |
| Risk Assessment | This document, Section 8 | 2026-08-27 |
| Emergency Procedures | This document, Section 4 | 2026-08-27 |
| Training Records | Maintained by safety officer | Ongoing |
| Incident Reports | Maintained by safety officer | Ongoing |

---

*Document Version: 1.0*
*Date: 2026-08-27*
*Author: Build Agent 5 of 6*
