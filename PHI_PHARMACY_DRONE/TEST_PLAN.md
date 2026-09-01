# PHI Pharmacy Drone - Test Plan

## 1. Pre-Flight Tests

### 1.1 Structural
| Test | Method | Pass Criteria |
|------|--------|---------------|
| Frame integrity | Visual | No cracks, damage |
| Arm movement | Manual | Smooth, no binding |
| Gripper function | Cycle test | Opens/closes properly |
| Tamper locks | All 20 slots | Lock/unlock correctly |
| Insulation | Visual | No gaps, tears |

### 1.2 Temperature Control
| Test | Method | Pass Criteria |
|------|--------|---------------|
| Refrigerated zone | Ice bath test | Reaches 2C in 5 min |
| Refrigerated range | PID tuning | Maintains 5C +/- 0.5C |
| Ambient zone | Room temp | Maintains 20C +/- 1C |
| Sensor accuracy | Calibrated ref | All 6 sensors within 0.5C |
| Alarm function | Simulate fault | Alert within 10s |

### 1.3 Inventory System
| Test | Method | Pass Criteria |
|------|--------|---------------|
| RFID detection | Tag in each slot | All 20 read correctly |
| Barcode scan | Test barcodes | 100% read accuracy |
| Tamper detection | Open seal | Detects within 1s |
| Presence sensor | Insert/remove | All 20 detect correctly |
| Weight sensor | Calibration weight | +/- 1g accuracy |

### 1.4 Dispensing
| Test | Method | Pass Criteria |
|------|--------|---------------|
| Arm reach | All 20 slots | Reaches all positions |
| Grip force | Force gauge | 100-500g range |
| Barcode verify | Mismatch test | Rejects wrong barcode |
| Photo capture | Test delivery | Photo saved correctly |
| Chain of custody | Full cycle | Log complete |

## 2. Navigation Tests

### 2.1 Flight Performance
| Test | Method | Pass Criteria |
|------|--------|---------------|
| Hover | 5 min hover | Stable, <1m drift |
| Forward flight | 60 km/h cruise | Smooth operation |
| Return to home | Auto RTH | Lands within 2m |
| Obstacle avoidance | Static obstacle | Avoids with 5m margin |
| Weather resistance | 40 km/h wind | Maintains position |

### 2.2 Delivery Navigation
| Test | Method | Pass Criteria |
|------|--------|---------------|
| Route optimization | 5 deliveries | Efficient route |
| GPS accuracy | Known point | Within 2m |
| Last-meter nav | Visual SLAM | Finds delivery point |
| Patient notification | App test | Notification sent |

## 3. Medication Integrity Tests

### 3.1 Temperature Maintenance
| Test | Condition | Pass Criteria |
|------|-----------|---------------|
| Refrigerated 2hr | 2-8C zone | Stays 2-8C |
| Ambient 2hr | 15-25C zone | Stays 15-25C |
| Hot day (35C) | External heat | Maintains range |
| Cold night (-5C) | External cold | Maintains range |
| Power cycle | On/off/on | Temp recovery <10min |

### 3.2 Chain of Custody
| Test | Method | Pass Criteria |
|------|--------|---------------|
| Load verification | Barcode + RFID | Both match |
| Tamper monitoring | Throughout flight | No undetected breaches |
| Delivery verification | Barcode + photo | Both logged |
| Temperature logging | Continuous | Complete log |
| GPS tracking | Full route | Complete trail |

## 4. Safety Tests

| Test | Method | Pass Criteria |
|------|--------|---------------|
| Motor failure | Single motor | Controlled landing |
| Battery failure | Simulated low | Emergency return |
| Comm loss | Disconnect | Auto-return |
| Temp excursion | Simulated | Alert + return |
| Tamper event | Open seal | Alert + photo |
| Controlled substance | Schedule II | Extra verification |

## 5. Endurance Tests

| Test | Duration | Pass Criteria |
|------|----------|---------------|
| Battery endurance | Full flight | 2hr runtime |
| Temperature control | 4 hours | All in range |
| Delivery cycle | 10 deliveries | All successful |
| Continuous monitor | 24 hours | No false alerts |

## Test Sign-Off

| Phase | Tester | Date | Result |
|-------|--------|------|--------|
| Pre-flight | | | |
| Navigation | | | |
| Medication | | | |
| Safety | | | |
| Endurance | | | |
