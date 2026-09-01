# PHI Medical Stretcher Drone - Test Plan

## 1. Pre-Flight Tests

### 1.1 Structural
| Test | Method | Pass Criteria |
|------|--------|---------------|
| Frame integrity | Visual + tap test | No cracks, delamination |
| Motor mounts | Torque check | 15 Nm, no movement |
| Winch cable | Visual inspection | No fraying, kinks |
| Patient harness | Load test (150kg) | No deformation |
| Parachute packing | Inspection | Correctly folded |

### 1.2 Electrical
| Test | Method | Pass Criteria |
|------|--------|---------------|
| Battery voltage | Multimeter | 51.2V +/- 0.5V |
| ESC calibration | BLHeli suite | All 8 responding |
| Motor spin | Manual test | Correct direction, smooth |
| BMS function | Charge/discharge | Balancing active |
| Wiring continuity | Ohmmeter | < 0.1 ohm |

### 1.3 Software
| Test | Method | Pass Criteria |
|------|--------|---------------|
| Firmware version | Status check | v2.0.0 |
| IMU calibration | Auto-cal | Gyro < 0.1 deg/s |
| GPS lock | Status display | RTK fix, 2cm accuracy |
| Communication | Link test | LTE + mesh connected |
| Safety systems | Arm test | All armed correctly |

### 1.4 Medical
| Test | Method | Pass Criteria |
|------|--------|---------------|
| ECG function | Simulator | Waveform displayed |
| SpO2 probe | Calibration check | 98% +/- 2% |
| NIBP cuff | Test measurement | Within 5mmHg |
| Temperature | Ice point test | 0.0C +/- 0.1C |
| O2 supply | Flow test | 2L/min for 30min |

## 2. Ground Tests

### 2.1 Motor Tests
| Test | Condition | Pass Criteria |
|------|-----------|---------------|
| Idle vibration | All motors idle | < 0.1G |
| Single motor | Each motor 50% | Stable hover possible |
| Two motor loss | Random 2 motors | Controlled descent |
| Full throttle | All motors max | < 120 km/h achieved |
| EMI test | Full power | No sensor interference |

### 2.2 Winch Tests
| Test | Method | Pass Criteria |
|------|--------|---------------|
| Lift capacity | 120kg test weight | Successful lift |
| Cable strength | 200kg static load | No failure |
| Extraction speed | Timed lift | 10m in 30s |
| Emergency release | Manual trigger | Releases in < 1s |

## 3. Flight Tests

### 3.1 Basic Flight
| Test | Description | Pass Criteria |
|------|-------------|---------------|
| Hover | 5 min hover at 10m | Stable, < 1m drift |
| Forward flight | 80 km/h cruise | Smooth, < 5 deg tilt |
| Vertical climb | Max climb rate | 5 m/s achieved |
| Descent | Controlled landing | < 0.5 m/s, soft |
| Return to home | Auto RTH | Lands within 2m |

### 3.2 Navigation
| Test | Description | Pass Criteria |
|------|-------------|---------------|
| Waypoint following | 10 waypoints | Within 2m accuracy |
| Obstacle avoidance | Static obstacles | Avoids with 5m margin |
| Dynamic avoidance | Moving obstacle | Detects and reroutes |
| Hospital approach | Auto approach | Lands at designated spot |
| Emergency landing | Simulated failure | Safe landing < 30s |

### 3.3 Medical
| Test | Description | Pass Criteria |
|------|-------------|---------------|
| Patient transport | 100kg dummy | Stable, < 0.5G |
| Vitals monitoring | Simulator | All 6 parameters displayed |
| Alert generation | Simulated emergency | Alert within 5s |
| Medical handoff | Full workflow | Data transmitted to hospital |

### 3.4 Phi-Harmonic
| Test | Description | Pass Criteria |
|------|-------------|---------------|
| Frequency accuracy | Spectrum analyzer | 16.18Hz +/- 0.1Hz |
| Field strength | Gaussmeter | 0.5mT at patient |
| Field uniformity | Multi-point test | +/- 10% variation |
| Adaptive control | Vitals change | Frequency adjusts |

## 4. Environmental Tests

| Test | Condition | Pass Criteria |
|------|-----------|---------------|
| Cold start | -10C | Starts, systems OK |
| Hot operation | +45C | No thermal throttle |
| Rain | IP67 spray | No water ingress |
| Wind | 50 km/h crosswind | Maintains position |
| Night ops | Dark conditions | Full camera visibility |

## 5. Endurance Tests

| Test | Duration | Pass Criteria |
|------|----------|---------------|
| Battery endurance | Full discharge | 60 min flight |
| Continuous monitor | 4 hours | All vitals logged |
| Communication uptime | 24 hours | < 1% packet loss |
| Heating cycling | 100 cycles | No degradation |

## 6. Failure Mode Tests

| Failure | Expected Response | Pass Criteria |
|---------|-------------------|---------------|
| Single motor loss | Thrust redistribution | Continues flight |
| Double motor loss | Emergency landing | Lands safely |
| Battery failure | Emergency land | Lands in 2 min |
| GPS loss | Switch to visual | Maintains position |
| Comm loss | Return to home | Returns autonomously |
| Medical emergency | Divert to hospital | Reroutes immediately |

## Test Sign-Off

| Phase | Tester | Date | Result |
|-------|--------|------|--------|
| Pre-flight | | | |
| Ground | | | |
| Flight | | | |
| Environmental | | | |
| Endurance | | | |
| Failure modes | | | |
