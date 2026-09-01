# PHI Surgical Assist Drone - Test Plan

## 1. Pre-Procedure Tests

### 1.1 Structural
| Test | Method | Pass Criteria |
|------|--------|---------------|
| Frame integrity | Visual | No cracks, corrosion |
| Enclosed rotors | Spin test | No contact with shroud |
| Arm joints | Manual movement | Smooth, no play |
| Gripper mechanism | Cycle test | 6 slots accessible |
| Brake system | Engage/release | <100ms response |

### 1.2 Electrical
| Test | Method | Pass Criteria |
|------|--------|---------------|
| Battery charge | Voltage check | 25.6V +/- 0.2V |
| Motor response | Individual spin | All 4 responding |
| Arm servos | Joint test | All 6 moving |
| Force sensor | Calibration | 0.1N accuracy |
| UV-C output | Radiometer | 40mW/cm2 |

### 1.3 Sterile Field
| Test | Method | Pass Criteria |
|------|--------|---------------|
| UV-C intensity | UV meter | 254nm, 40mW/cm2 |
| Ionization | Particle counter | 10^6 ions/cm3 |
| HEPA flow | Anemometer | 100 CFM |
| Particle count | OPC | <10 particles/m3 |
| Auto-sterilize | Cycle test | 30s complete cycle |

### 1.4 Calibration
| Test | Method | Pass Criteria |
|------|--------|---------------|
| Camera stereo | Calibration target | Epipolar <1 pixel |
| EM tracker | Reference frame | 0.1mm accuracy |
| Arm IK | Simulation | 0.1mm reach target |
| Phi-harmonic | Spectrum analyzer | 16.18Hz +/- 0.1Hz |

## 2. Positioning Tests

### 2.1 Visual Servoing
| Test | Method | Pass Criteria |
|------|--------|---------------|
| Target lock | Surgical site | Locks in <1s |
| Position hold | 5 min hold | <0.5mm drift |
| Re-positioning | New target | <2s to acquire |
| Stereo depth | Depth target | <1mm error |

### 2.2 Arm Positioning
| Test | Method | Pass Criteria |
|------|--------|---------------|
| Reach accuracy | 20 targets | <0.1mm RMSE |
| Force control | 0.1-50N range | Within 5% |
| Collision detect | Obstacle approach | Stops at 5cm |
| Emergency stop | Button press | <100ms response |

## 3. Surgical Simulation Tests

### 3.1 Instrument Management
| Test | Method | Pass Criteria |
|------|--------|---------------|
| Instrument swap | 6 instruments | <2s per swap |
| Grip security | Shake test | No slippage |
| Force feedback | Surgeon feedback | Realistic feel |
| Surgical hold | 30 min hold | <0.5mm drift |

### 3.2 Phi-Harmonic Healing
| Test | Method | Pass Criteria |
|------|--------|---------------|
| Frequency accuracy | Spectrum analyzer | 16.18Hz +/- 0.1Hz |
| Field coverage | Multi-probe | 30cm radius uniform |
| Adaptive control | Tissue impedance | Frequency adjusts |
| Healing progress | Simulation | Progresses to 100% |

## 4. Safety Tests

### 4.1 Emergency Procedures
| Test | Method | Pass Criteria |
|------|--------|---------------|
| Emergency stop | Button/voice | All motion stops |
| Brake engage | Force fault | <100ms, locked |
| Motor failure | Single/double | Safe ceiling dock |
| Battery failure | Simulated | Auto-dock |
| Comm loss | Disconnect | Auto-dock |
| Sterile breach | Particle surge | Alert + resterilize |

### 4.2 IEC 60601-1 Compliance
| Test | Standard | Pass Criteria |
|------|----------|---------------|
| Electrical safety | 60601-1 | Leakage <0.1mA |
| EMG immunity | 60601-1-2 | No malfunction |
| Mechanical | 60601-1 | No sharp edges |
| Biocompatibility | ISO 10993 | Patient contact safe |

## 5. Endurance Tests

| Test | Duration | Pass Criteria |
|------|----------|---------------|
| Continuous surgical assist | 4 hours | All systems nominal |
| Sterile field maintain | 8 hours | <20 particles/m3 |
| Battery endurance | Full cycle | 4+ hours runtime |
| Phi-harmonic output | 4 hours | Stable frequency |

## Test Sign-Off

| Phase | Tester | Date | Result |
|-------|--------|------|--------|
| Pre-procedure | | | |
| Positioning | | | |
| Surgical sim | | | |
| Safety | | | |
| Endurance | | | |
