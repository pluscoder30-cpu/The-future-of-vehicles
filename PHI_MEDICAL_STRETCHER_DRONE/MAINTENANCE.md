# PHI Medical Stretcher Drone - Maintenance Manual

## 1. Safety Precautions

### Before Any Maintenance
1. Power off drone completely
2. Disconnect battery
3. Wait 5 minutes for capacitors to discharge
4. Wear ESD protection when handling electronics
5. Follow lockout/tagout procedures

### Battery Safety
- Store at 40-60% charge
- Never expose to temperatures above 60C
- Use fireproof bag during charging
- Dispose of damaged batteries immediately
- Keep away from flammable materials

## 2. Maintenance Schedule

### 2.1 Post-Flight (After Every Mission)
```
Duration: 10 minutes
Tools: None required

Checklist:
[ ] Visual inspection of frame
[ ] Check for damage, cracks, dents
[ ] Inspect propellers for nicks, cracks
[ ] Verify motor mounts secure
[ ] Check battery connector
[ ] Inspect winch cable
[ ] Verify medical equipment clean
[ ] Check phi-harmonic emitters
[ ] Clean camera lenses
[ ] Download flight logs
```

### 2.2 Weekly Maintenance
```
Duration: 30 minutes
Tools: Hex drivers, torque wrench, multimeter

Checklist:
[ ] Torque check: motor mounts (15 Nm)
[ ] Torque check: propeller bolts (8 Nm)
[ ] Battery capacity test
[ ] Motor resistance measurement
[ ] ESC calibration verification
[ ] Sensor calibration check
[ ] Communication link test
[ ] Safety system arm test
[ ] Winch function test
[ ] Clean airframe
```

### 2.3 Monthly Maintenance
```
Duration: 2 hours
Tools: Full tool kit, calibration equipment

Checklist:
[ ] Complete motor inspection
[ ] ESC firmware update (if available)
[ ] Flight controller calibration
[ ] GPS antenna inspection
[ ] Camera calibration
[ ] Medical equipment calibration
  - ECG: Simulator test
  - SpO2: Calibration check
  - NIBP: Accuracy verification
  - Temperature: Ice point check
[ ] Phi-harmonic frequency verification
[ ] Battery deep cycle test
[ ] Parachute repack (if deployed)
[ ] Structural inspection (UV dye)
[ ] Electrical connection inspection
[ ] Firmware update
```

### 2.4 Quarterly Maintenance
```
Duration: 8 hours
Tools: Complete workshop equipment

Checklist:
[ ] Complete disassembly inspection
[ ] Frame ultrasonic inspection
[ ] Motor bearing inspection
[ ] Motor rewinding (if needed)
[ ] ESC capacitor inspection
[ ] Battery capacity degradation test
[ ] Winch cable replacement (if worn)
[ ] Full medical equipment service
  - ECG: Full calibration
  - SpO2: LED replacement check
  - NIBP: Cuff replacement
  - O2: Cylinder hydrostatic test
[ ] Phi-harmonic emitter coil inspection
[ ] All connectors cleaned and re-greased
[ ] Waterproofing inspection (IP67)
[ ] Emergency systems full test
```

### 2.5 Annual Overhaul
```
Duration: 2 days
Tools: Complete workshop + specialized equipment

Checklist:
[ ] Complete disassembly
[ ] Frame replacement (if >500 flights)
[ ] All motors replaced
[ ] All ESCs replaced
[ ] Battery replacement
[ ] Flight controller replacement
- Parachute repack (annual requirement)
[ ] Complete medical equipment overhaul
[ ] Phi-harmonic system recalibration
[ ] Full system integration test
[ ] Certification renewal
[ ] Flight testing (10 hours)
```

## 3. Component Replacement

### 3.1 Motor Replacement
```
Tools: 3mm hex driver, 5mm hex driver
Time: 15 minutes per motor

Procedure:
1. Remove propeller (counter-clockwise)
2. Disconnect ESC connector
3. Remove 4 motor mount bolts
4. Install new motor
5. Reconnect ESC
6. Install propeller
7. Verify rotation direction
8. Calibrate ESC
```

### 3.2 Battery Replacement
```
Tools: None (hot-swap design)
Time: 2 minutes

Procedure:
1. Power off drone
2. Disconnect old battery ( XT90 connector)
3. Connect new battery
4. Power on, verify voltage
5. Run battery diagnostics
```

### 3.3 Propeller Replacement
```
Tools: 5mm hex driver
Time: 5 minutes per propeller

Procedure:
1. Remove 2 propeller bolts
2. Remove old propeller
3. Install new propeller (match direction)
4. Torque bolts to 8 Nm
5. Verify no wobble
```

### 3.4 Medical Sensor Replacement
```
Tools: Anti-static mat, precision tools
Time: 30 minutes per sensor

Procedure:
1. Power off medical MCU
2. Disconnect sensor cable
3. Remove sensor mounting
4. Install new sensor
5. Reconnect cable
6. Run calibration procedure
7. Verify accuracy
```

## 4. Troubleshooting

### 4.1 Motor Issues
| Symptom | Likely Cause | Solution |
|---------|--------------|----------|
| Motor not spinning | ESC failure | Replace ESC |
| Excessive vibration | Bent shaft | Replace motor |
| Overheating | Bearing failure | Replace motor |
| Low thrust | Worn propeller | Replace propeller |

### 4.2 Battery Issues
| Symptom | Likely Cause | Solution |
|---------|--------------|----------|
| Low capacity | Cell degradation | Replace battery |
| Voltage sag | High internal resistance | Replace battery |
| Won't charge | BMS fault | Check BMS, replace if needed |
| Overheating | Short circuit | Do not use, dispose safely |

### 4.3 Navigation Issues
| Symptom | Likely Cause | Solution |
|---------|--------------|----------|
| No GPS lock | Antenna issue | Check antenna connection |
| Drift | IMU needs calibration | Run calibration |
| Wrong position | GPS interference | Check for interference sources |
| Avoidance fails | LiDAR blocked | Clean LiDAR sensor |

### 4.4 Medical Issues
| Symptom | Likely Cause | Solution |
|---------|--------------|----------|
| No ECG signal | Bad lead contact | Reposition leads |
| Inaccurate SpO2 | Low perfusion | Wait for stable reading |
| BP error | Cuff too loose | Reposition cuff |
| Temp drift | Sensor aging | Recalibrate |

## 5. Spare Parts Inventory

### Critical Spares (Keep on hand)
| Part | Quantity | Lead Time |
|------|----------|-----------|
| Motors | 4 | 21 days |
| ESCs | 4 | 14 days |
| Propellers | 8 sets | 14 days |
| Battery | 2 | 30 days |
| Flight controller | 1 | 14 days |
| GPS module | 1 | 14 days |
| Medical sensors | 1 set | 30 days |

### Consumables
| Item | Frequency |
|------|-----------|
| Propellers | Every 50 flights |
| Winch cable | Every 200 flights |
| Motor bearings | Every 500 hours |
| Battery | Every 500 cycles |
| Parachute | Every deployment or annually |

## 6. Documentation

### Required Logs
- Flight log (after every flight)
- Maintenance log (after every service)
- Medical calibration log (monthly)
- Battery cycle log (continuous)
- Incident report (as needed)

### Record Retention
- Flight logs: 7 years
- Medical records: 10 years
- Maintenance records: Life of aircraft
- Incident reports: Permanent

## 7. Tools Required

### Basic Toolkit
- Hex drivers: 2mm, 2.5mm, 3mm, 4mm, 5mm
- Torque wrench: 5-25 Nm
- Multimeter
- Wire strippers
- Soldering iron
- Heat gun

### Specialized Tools
- Motor balancer
- ESC programming box
- GPS simulator
- Medical simulator
- Phi-harmonic spectrum analyzer
- LiDAR alignment tool

## 8. Contact Information

| Service | Contact |
|---------|---------|
| Technical Support | [PHONE] |
| Warranty Service | [PHONE] |
| Medical Equipment | [PHONE] |
| Emergency Parts | [PHONE] |
