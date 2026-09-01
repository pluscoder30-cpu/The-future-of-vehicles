# PHI Pharmacy Drone - Maintenance Manual

## 1. Safety Precautions

### Before Any Maintenance
1. Power off drone completely
2. Disconnect battery
3. Remove all medications
4. Clean and sanitize all surfaces
5. Follow controlled substance protocols if applicable

### Temperature System Safety
- Peltier modules get hot - allow 10min cooldown
- Never touch UV-C lamps (if installed)
- Use thermal gloves when handling cold components
- Check for refrigerant leaks (if applicable)

## 2. Maintenance Schedule

### 2.1 After Each Delivery (5 minutes)
```
[ ] Visual inspection of frame
[ ] Check all 20 slots for debris
[ ] Clean dispensing arm
[ ] Verify tamper seals intact
[ ] Check temperature readings
[ ] Download delivery log
[ ] Charge battery if <80%
```

### 2.2 Daily (20 minutes)
```
[ ] Full diagnostic check
[ ] Temperature calibration verification
[ ] RFID reader test (all 20 slots)
[ ] Barcode scanner calibration
[ ] Dispensing arm range of motion
[ ] Gripper force test
[ ] Camera lens cleaning
[ ] Phi-harmonic frequency check
```

### 2.3 Weekly (1 hour)
```
[ ] Peltier module inspection
[ ] Heater function test
[ ] Insulation integrity check
[ ] Arm joint lubrication
[ ] Gripper mechanism service
[ ] All sensors calibration
[ ] Firmware update check
[ ] Complete slot cleaning
```

### 2.4 Monthly (4 hours)
```
[ ] Peltier efficiency test
[ ] Temperature sensor calibration
[ ] RFID antenna alignment
[ ] Barcode scanner deep clean
[ ] Arm joint bearing inspection
[ ] Battery capacity test
[ ] Phi-harmonic emitter coil check
[ ] Full sterile field validation
[ ] Tamper lock mechanism service
```

### 2.5 Quarterly (1 day)
```
[ ] Complete system overhaul
[ ] Peltier module replacement (if degraded)
[ ] Insulation replacement (if compressed)
[ ] Arm joint replacement (if worn)
[ ] All sensors recalibrated
[ ] Battery deep cycle test
[ ] Full navigation test
[ ] Safety system full test
[ ] Documentation update
```

### 2.6 Annual (2 days)
```
[ ] Complete system overhaul
[ ] All Peltier modules replaced
[ ] All heaters replaced
[ ] All insulation replaced
[ ] All joints serviced
[ ] Battery replaced
[ ] Firmware reflash
[ ] Full recertification
[ ] Flight test (10 hours)
```

## 3. Component Replacement

### 3.1 Peltier Module Replacement
```
Tools: Thermal paste, screwdriver
Time: 30 minutes

Procedure:
1. Power off, remove battery
2. Remove refrigerated zone cover
3. Disconnect old Peltier wires
4. Remove mounting screws
5. Clean old thermal paste
6. Apply new thermal paste
7. Install new Peltier module
8. Reconnect wires
9. Replace cover
10. Test cooling performance
```

### 3.2 Temperature Sensor Replacement
```
Tools: Soldering iron, replacement sensor
Time: 15 minutes per sensor

Procedure:
1. Power off
2. Locate faulty sensor
3. Desolder old sensor
4. Solder new sensor
5. Calibrate against reference
6. Verify reading accuracy
```

### 3.3 Dispensing Arm Service
```
Tools: Precision screwdriver set, lubricant
Time: 1 hour

Procedure:
1. Power off, remove medications
2. Remove arm cover
3. Inspect all joints
4. Lubricate with medical-grade grease
5. Check gear wear
6. Replace worn gears
7. Reassemble
8. Calibrate range of motion
9. Test grip force
```

### 3.4 Tamper Lock Replacement
```
Tools: Screwdriver, replacement lock
Time: 10 minutes per lock

Procedure:
1. Power off
2. Remove slot cover
3. Disconnect old lock
4. Remove mounting
5. Install new lock
6. Reconnect
7. Test lock/unlock
8. Verify audit trail
```

## 4. Troubleshooting

| Symptom | Likely Cause | Solution |
|---------|--------------|----------|
| Temp out of range | Peltier failure | Replace Peltier |
| RFID not reading | Antenna misaligned | Recalibrate antenna |
| Barcode won't scan | Lens dirty | Clean lens |
| Arm won't reach | Joint worn | Lubricate/replace joint |
| Gripper weak | Spring worn | Replace spring |
| Tamper false alarm | Sensor drift | Recalibrate sensor |
| Battery low fast | Cell degradation | Replace battery |
| Navigation drift | GPS antenna | Check antenna connection |

## 5. Spare Parts Inventory

| Part | Quantity | Lead Time |
|------|----------|-----------|
| Peltier modules | 4 | 14 days |
| Temperature sensors | 6 | 7 days |
| RFID readers | 4 | 14 days |
| Barcode scanner | 1 | 14 days |
| Arm joints | 2 | 21 days |
| Gripper springs | 4 | 7 days |
| Tamper locks | 10 | 14 days |
| Battery | 1 | 30 days |
| Insulation kit | 2 | 7 days |

## 6. Documentation

Required logs:
- Delivery log (after each flight)
- Maintenance log (after each service)
- Temperature log (continuous)
- Tamper event log (as needed)
- Chain of custody (as needed)

## 7. Tools Required

### Basic
- Hex drivers: 2mm, 2.5mm, 3mm
- Torque wrench: 2-5 Nm
- Multimeter
- Soldering iron
- Thermal paste

### Specialized
- Temperature calibrator (ice point + boiling point)
- RFID tester
- Barcode verifier
- Force gauge (for gripper)
- Phi-harmonic spectrum analyzer
- Thermal camera (for insulation check)
