# PHI_FIELD_ROBOT — Operator Manual

## PHI_FIELD_ROBOT | Operator Manual

---

## 1. SAFETY FIRST

### ⚠️ IMPORTANT SAFETY WARNINGS

**READ BEFORE OPERATING**

1. **HIGH VOLTAGE**: Robot operates at 48V DC. Can cause electric shock.
2. **MOVING JOINTS**: 17 motorized joints can cause pinching/crushing injuries.
3. **LITHIUM BATTERY**: Do not short circuit, puncture, or incinerate.
4. **TIPPING**: Do not operate on slopes steeper than 20°.
5. **CHILDREN**: Children under 12 must not approach active robot.

### Required PPE

- Safety glasses (ANSI Z87.1)
- Work gloves (cut-resistant)
- Hearing protection (when within 1m)
- Closed-toe shoes

### Emergency Stop

**Location**: Red mushroom button on top of robot body

**How to use**: Press firmly to stop all motion immediately

**Release**: Pull up to reset (robot will not move until released)

---

## 2. GETTING STARTED

### 2.1 Unboxing

1. Remove robot from shipping box carefully (30 kg)
2. Place on flat, stable surface
3. Verify no shipping damage
4. Remove protective foam from joints
5. Check all covers are secure

### 2.2 Charging

1. Locate charging port (right side of body, covered)
2. Remove port cover
3. Connect charger XT90 connector to robot
4. Plug charger into wall outlet (120V or 240V)
5. Wait for green LED on charger (2.8 hours for full charge)
6. Disconnect charger from robot, then wall

### 2.3 First Power-On

1. Ensure robot is on flat ground
2. Ensure area is clear (1m radius)
3. Press and hold power button (3 seconds)
4. Wait for startup sequence (30 seconds)
5. Status LED will turn blue when ready
6. Robot is now in idle mode

---

## 3. BASIC OPERATION

### 3.1 Remote Control (WiFi)

**Connect to robot WiFi:**
- Network: PHI_FIELD_ROBOT_[SERIAL]
- Password: Printed on robot nameplate

**Open web interface:**
- URL: http://192.168.4.1:8080
- Or use mobile app (available for iOS/Android)

**Web interface controls:**
- Joystick: Left stick for movement
- Arm control: Right stick for arm
- Gripper: Slider for open/close
- Speed: Slider for speed limit
- E-Stop: Red button (software emergency stop)

### 3.2 Movement Controls

| Input | Action |
|-------|--------|
| Forward stick | Walk forward |
| Backward stick | Walk backward |
| Left stick | Turn left |
| Right stick | Turn right |
| Both sticks forward | Walk straight (both legs) |
| Both sticks back | Walk backward (both legs) |

**Speed modes:**
- Slow: 2 km/h (default, safest)
- Normal: 4 km/h (standard)
- Fast: 6 km/h (use with caution)
- Max: 8 km/h (expert only)

### 3.3 Arm Controls

| Input | Action |
|-------|--------|
| Arm stick up | Shoulder pitch up |
| Arm stick down | Shoulder pitch down |
| Arm stick left | Shoulder roll left |
| Arm stick right | Shoulder roll right |
| Arm twist left | Elbow bend |
| Arm twist right | Elbow extend |
| Gripper slider | Open/close gripper |

**Arm presets:**
- Home: Arm folded against body
- Ready: Arm extended forward, 45° up
- Reach: Arm fully extended forward
- Carry: Arm extended forward, 30° up

### 3.4 Camera Views

| Button | View |
|--------|------|
| View 1 | Front camera |
| View 2 | Rear camera |
| View 3 | Left camera |
| View 4 | Right camera |
| View 5 | 360° stitched view |
| View 6 | LIDAR map overlay |

---

## 4. MISSION MODES

### 4.1 Survey Mission

1. Select "Survey" from mission menu
2. Define survey area on map (tap points)
3. Set parameters:
   - Path spacing: 2m, 5m, or 10m
   - Speed: Slow, Normal, or Fast
   - Sensors: Camera, LIDAR, or Both
4. Press "Start Mission"
5. Robot will automatically:
   - Plan phi-A* path
   - Walk survey pattern
   - Collect sensor data
   - Return to start point

### 4.2 Sample Collection

1. Select "Sample" from mission menu
2. Define sample points on map
3. For each point, set:
   - Sample type: Soil, Water, Air
   - Depth: 0-50mm (soil only)
   - Container: Yes/No
4. Press "Start Mission"
5. Robot will:
   - Navigate to each point
   - Deploy arm
   - Collect sample
   - Store in container
   - Return to base

### 4.3 Inspection

1. Select "Inspect" from mission menu
2. Define inspection targets
3. Set parameters:
   - Photo interval: 1-10 seconds
   - Video: Yes/No
   - LIDAR scan: Yes/No
4. Press "Start Mission"
5. Robot will:
   - Navigate to each target
   - Capture images/video
   - Create 3D scan
   - Generate report

### 4.4 Follow Mode

1. Select "Follow" from mission menu
2. Operator walks ahead of robot
3. Robot follows operator at safe distance
4. Maintains 2m following distance
5. Automatically avoids obstacles
6. Stops if operator stops

### 4.5 Return to Base

1. Select "Return" from mission menu
2. Robot will:
   - Calculate path to charging station
   - Navigate autonomously
   - Dock for charging
   - Notify when complete

---

## 5. ADVANCED FEATURES

### 5.1 Phi-Harmonic Gait Modes

The robot uses phi-harmonic coordination for natural, efficient movement.

**Standard Gait (default):**
- Best for flat terrain
- Most energy efficient
- Smoothest movement

**Adaptive Gait:**
- Automatically adjusts to terrain
- Better for rough ground
- Slightly less efficient

**Climb Gait:**
- For stairs and steep slopes
- More power, slower speed
- Maximum stability

**Quiet Gait:**
- Reduced noise (35 dB)
- Slower speed (2 km/h)
- For wildlife observation

### 5.2 Arm Presets

The arm can store custom positions:

**To save a preset:**
1. Move arm to desired position
2. Press and hold "Save" button
3. Select preset slot (1-5)
4. Release button

**To recall a preset:**
1. Press "Recall" button
2. Select preset slot
3. Arm moves to stored position

### 5.3 Autonomous Navigation

**Map building:**
1. Select "Build Map" mode
2. Drive robot around area
3. Robot builds occupancy grid map
4. Save map when complete

**Navigation on saved map:**
1. Select "Navigate" mode
2. Tap destination on map
3. Robot plans phi-A* path
4. Robot navigates autonomously
5. Avoids obstacles automatically

### 5.4 Data Collection

**Sensor logging:**
- All sensor data logged to NVMe SSD
- Includes: images, LIDAR, IMU, GPS, FSR
- Timestamped and geotagged
- Export via USB or WiFi

**Data formats:**
- Images: JPEG (compressed), PNG (raw)
- LIDAR: PCD (point cloud)
- IMU: CSV (time series)
- GPS: GPX (tracks)

---

## 6. MAINTENANCE

### 6.1 Daily Checks

Before each use:
- □ Visual inspection (no damage)
- □ Battery level (>50%)
- □ Emergency stop functional
- □ Camera lenses clean
- □ LIDAR lens clean
- □ Foot pads intact
- □ No loose bolts

### 6.2 Weekly Maintenance

- □ Check bolt torque (all joints)
- □ Clean foot pads (IPA wipe)
- □ Check cable condition
- □ Verify WiFi range
- □ Test emergency stop

### 6.3 Monthly Maintenance

- □ Re-calibrate IMU
- □ Check bearing smoothness
- □ Clean air filter
- □ Update firmware
- □ Backup data

### 6.4 Battery Care

- Keep charged between 20-80% for daily use
- Full charge before long storage
- Store at 50% charge if not using for >1 month
- Avoid extreme temperatures
- Use only approved charger

### 6.5 Foot Pad Replacement

When tread is worn (typically 500 km):
1. Power down robot
2. Remove M4 bolt from foot
3. Pull old foot pad off
4. Press new foot pad on
5. Secure with M4 bolt
6. Verify FSR reading

---

## 7. TROUBLESHOOTING

### 7.1 Common Issues

| Issue | Possible Cause | Solution |
|-------|---------------|----------|
| Robot won't power on | Battery depleted | Charge battery |
| | Emergency stop pressed | Release e-stop |
| | Power button not held long enough | Hold 3 seconds |
| Robot moves erratically | IMU calibration lost | Re-calibrate IMU |
| | Low battery | Charge battery |
| | Motor fault | Check motor connections |
| Arm won't move | Arm disabled | Enable arm in settings |
| | Payload too heavy | Reduce payload |
| | Motor fault | Check motor connections |
| Cameras not working | Cable loose | Re-seat CSI/USB cables |
| | Power issue | Check 12V bus |
| | Software issue | Restart camera node |
| LIDAR not scanning | USB connection | Re-seat USB cable |
| | Power issue | Check 12V bus |
| | Obstruction | Clear LIDAR path |
| WiFi connection poor | Distance too far | Move closer |
| | Interference | Change WiFi channel |
| | Antenna issue | Check antenna connection |
| Robot tips over | Slope too steep | Use on flatter terrain |
| | Speed too high | Reduce speed |
| | Payload offset | Balance payload |

### 7.2 Error Codes

| Code | Meaning | Action |
|------|---------|--------|
| E001 | CAN bus error | Check CAN cables |
| E002 | Motor overcurrent | Reduce load, check motor |
| E003 | IMU failed | Re-calibrate IMU |
| E004 | Battery low | Charge immediately |
| E005 | Pi watchdog | Restart system |
| E006 | E-stop active | Release e-stop |
| E007 | Arm collision | Check arm workspace |
| E008 | LIDAR obstructed | Clear path |
| E009 | FSR error | Re-calibrate FSRs |
| E010 | Over-temperature | Reduce load, check cooling |

### 7.3 Emergency Procedures

**If robot tips over:**
1. Stay clear of robot
2. Press emergency stop (if safe)
3. Wait for motion to stop
4. Do not attempt to right robot manually
5. Use remote control to right robot (if functional)
6. If not functional, contact support

**If battery smokes:**
1. Move away immediately
2. Do not touch robot
3. Call emergency services if fire
4. Do not attempt to extinguish lithium fire
5. Ventilate area

**If person caught in robot:**
1. Press emergency stop immediately
2. Do not pull person free
3. Loosen bolts if necessary to free person
4. Call emergency services for injuries
5. Administer first aid if trained

---

## 8. SPECIFICATIONS

### 8.1 Physical

| Parameter | Value |
|-----------|-------|
| Height | 600mm (23.6 in) |
| Length | 400mm (15.75 in) |
| Width | 200mm (7.87 in) |
| Weight | 30 kg (66 lbs) |
| Ground Clearance | 150mm (5.9 in) |

### 8.2 Performance

| Parameter | Value |
|-----------|-------|
| Walking Speed | 8 km/h (5 mph) max |
| Step Height | 150mm (6 in) |
| Gap Crossing | 300mm (12 in) |
| Slope (static) | 30° |
| Slope (dynamic) | 20° |
| Arm Payload | 10 kg (22 lbs) |
| Arm Reach | 500mm (20 in) |
| Battery Life | 6 hours |
| Charge Time | 3 hours |

### 8.3 Environmental

| Parameter | Value |
|-----------|-------|
| Operating Temp | -10°C to 45°C |
| Storage Temp | -20°C to 60°C |
| Humidity | 0-90% RH |
| IP Rating | IP54 |
| Noise | 45 dB at 1m |

---

## 9. CONTACT AND SUPPORT

### 9.1 Support Channels

- **Email**: support@phi-robot.com
- **Phone**: 1-800-PHI-BOT
- **Web**: https://phi-robot.com/support
- **Forum**: https://forum.phi-robot.com

### 9.2 Warranty

| Component | Warranty |
|-----------|----------|
| Frame | 5 years |
| Motors | 2 years |
| Electronics | 1 year |
| Batteries | 2 years / 3000 cycles |
| Consumables | 90 days |

### 9.3 Returns

1. Contact support for RMA number
2. Pack robot securely
3. Include RMA number on shipping label
4. Ship to address provided
5. Repair/replacement within 2 weeks

---

## 10. QUICK REFERENCE CARD

```
┌─────────────────────────────────────────────────────────────┐
│              PHI_FIELD_ROBOT QUICK REFERENCE                 │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  POWER ON:    Hold power button 3 seconds                   │
│  POWER OFF:   Hold power button 5 seconds                   │
│  E-STOP:      Press red mushroom button                     │
│  E-STOP RESET: Pull up red mushroom button                  │
│                                                              │
│  WiFi: PHI_FIELD_ROBOT_[SERIAL]                             │
│  Web UI: http://192.168.4.1:8080                            │
│                                                              │
│  ERROR CODES:                                                │
│  E001=CAN  E002=MOTOR  E003=IMU  E004=BATTERY              │
│  E005=PI   E006=E-STOP E007=ARM  E008=LIDAR                │
│  E009=FSR  E010=TEMP                                          │
│                                                              │
│  EMERGENCY: Press E-STOP → Wait → Assess → Call 911 if      │
│             needed                                           │
│                                                              │
│  MAINTENANCE: Daily visual, Weekly bolts, Monthly calibrate │
│                                                              │
│  SUPPORT: support@phi-robot.com | 1-800-PHI-BOT            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

*Manual Version: 1.0*
*Date: 2026-08-27*
*Author: Build Agent 5 of 6*
