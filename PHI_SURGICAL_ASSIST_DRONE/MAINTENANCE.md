# PHI Surgical Assist Drone - Maintenance Manual

## 1. Safety Precautions

### Before Any Maintenance
1. Ensure drone is docked at ceiling mount
2. Engage mechanical brake
3. Disconnect power (inductive dock)
4. Wait 5 minutes for capacitors
5. Follow lockout/tagout procedures

### Sterile Field Safety
- UV-C causes skin/eye damage - never look directly
- Ionizers produce ozone - ensure ventilation
- Never open UV-C housing while powered
- Replace UV-C lamps per schedule

## 2. Maintenance Schedule

### 2.1 After Each Procedure (5 minutes)
```
[ ] Auto-sterilize cycle completed
[ ] Visual inspection of arm and gripper
[ ] Check instrument slots clean
[ ] Verify UV-C intensity (indicator)
[ ] Download procedure log
[ ] Check battery level
```

### 2.2 Daily (15 minutes)
```
[ ] Full diagnostic check
[ ] Camera calibration verification
[ ] Force sensor zero check
[ ] Arm joint movement test
[ ] Gripper open/close test
[ ] Sterile field particle count
[ ] Phi-harmonic frequency check
[ ] Brake function test
```

### 2.3 Weekly (1 hour)
```
[ ] Arm calibration with reference
[ ] Force sensor full calibration
[ ] UV-C intensity measurement
[ ] Ionizer output check
[ ] HEPA filter pressure drop
[ ] Motor inspection
[ ] ESC calibration
[ ] Firmware update check
[ ] CEILING DOCK INSPECTION
```

### 2.4 Monthly (4 hours)
```
[ ] Complete system diagnostic
[ ] Arm joint bearing inspection
[ ] Gripper mechanism service
[ ] UV-C lamp hours check (>5000h = replace)
[ ] HEPA filter replacement (if needed)
[ ] Battery capacity test
[ ] Phi-harmonic emitter coil inspection
[ ] Full sterile field validation
[ ] IEC 60601-1 spot checks
```

### 2.5 Quarterly (1 day)
```
[ ] Full disassembly inspection
[ ] Arm joint replacement (if worn)
[ ] Gripper mechanism overhaul
[ ] UV-C lamp replacement
[ ] Ionizer electrode cleaning
[ ] Complete calibration cycle
[ ] Battery deep cycle test
[ ] Safety system full test
[ ] Documentation update
```

### 2.6 Annual (2 days)
```
[ ] Complete system overhaul
[ ] All joints serviced
[ ] All sensors recalibrated
[ ] All lamps replaced
[ ] Battery replaced
[ ] Firmware reflash
[ ] IEC 60601-1 recertification
[ ] Flight test (10 hours)
[ ] Full integration test
```

## 3. Component Replacement

### 3.1 UV-C Lamp Replacement
```
Tools: UV protective gloves, goggles
Time: 30 minutes

Procedure:
1. Power off system
2. Wait 10 minutes (cool down)
3. Remove UV-C housing cover
4. Disconnect old lamp
5. Install new lamp (254nm, 40mW/cm2)
6. Reconnect
7. Replace cover
8. Test intensity with radiometer
9. Reset lamp hour counter
```

### 3.2 Arm Joint Service
```
Tools: Precision screwdriver set, torque wrench
Time: 2 hours per joint

Procedure:
1. Power off, engage brake
2. Remove arm cover
3. Inspect joint bearing
4. Replace bearing if worn
5. Re-grease with medical-grade lubricant
6. Reassemble
7. Calibrate joint
8. Test full range of motion
```

### 3.3 Gripper Mechanism
```
Tools: Anti-static mat, precision tools
Time: 1 hour

Procedure:
1. Remove gripper assembly
2. Inspect all 6 instrument slots
3. Clean contact surfaces
4. Replace worn spring if needed
5. Test grip force
6. Reinstall and calibrate
```

## 4. Troubleshooting

| Symptom | Likely Cause | Solution |
|---------|--------------|----------|
| Arm won't move | Brake engaged | Check brake signal |
| Poor positioning | Camera misaligned | Recalibrate cameras |
| Force error | Sensor drift | Recalibrate force sensor |
| Sterile breach | UV-C lamp worn | Check/replace lamp |
| Phi-harmonic off | Emitter fault | Check emitter connections |
| Won't dock | Magnet alignment | Adjust dock position |
| Low battery | Inductive coil | Check coil alignment |

## 5. Spare Parts Inventory

| Part | Quantity | Lead Time |
|------|----------|-----------|
| UV-C lamps | 4 | 7 days |
| Arm joints | 2 | 14 days |
| Gripper springs | 6 | 7 days |
| Force sensor | 1 | 21 days |
| Camera module | 1 | 14 days |
| Battery | 1 | 30 days |
| HEPA filters | 4 | 7 days |
| Ionizer electrodes | 2 | 14 days |

## 6. Documentation

Required logs:
- Pre-procedure checklist (after each use)
- Maintenance log (after each service)
- Calibration log (monthly)
- UV-C lamp hours (continuous)
- Battery cycles (continuous)
- Incident reports (as needed)

## 7. Tools Required

### Basic
- Hex drivers: 1.5mm, 2mm, 2.5mm, 3mm
- Torque wrench: 2-10 Nm
- Multimeter
- ESD mat and wrist strap

### Specialized
- UV radiometer (254nm)
- Particle counter
- Force/torque calibration rig
- Camera calibration target
- Phi-harmonic spectrum analyzer
- Arm calibration fixture
