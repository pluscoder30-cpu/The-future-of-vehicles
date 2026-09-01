# PHI AI FIRE DRONE — PERFORMANCE SPECIFICATIONS

## Flight and AI Fire Performance Data

---

## FLIGHT PERFORMANCE

| Parameter | Value |
|-----------|-------|
| Max Speed | 45 km/h |
| Cruise Speed | 30 km/h |
| Hover Time (empty) | 3.5 hours |
| Hover Time (2kg payload) | 3.0 hours |
| Range | 20 km |
| Max Altitude | 120m AGL |
| Wind Resistance | 30 km/h |

---

## AI FIRE DETECTION PERFORMANCE

| Metric | Value |
|--------|-------|
| Thermal Detection Range | 100m |
| Fire Size Detection | > 0.5m² |
| Temperature Accuracy | ±2°C |
| AI Spread Prediction Accuracy | ~80% |
| AI Drop Zone Accuracy | ±3m |
| Inference Time | <200ms |

---

## AI SWARM COORDINATION

```
MULTI-DRONE FIRE FIGHTING:
═══════════════════════════════════════════════════════════════

  AI COORDINATION PROTOCOL:

  Lead Drone:
  ├── Receives thermal data from all drones
  ├── Builds fire map
  ├── Predicts spread
  ├── Assigns sectors
  └── Coordinates drops

  Wing Drones:
  ├── Report thermal data to lead
  ├── Execute assigned drops
  ├── Report retardant status
  └── Receive new assignments

  SWARM CAPACITY:
  ├── Minimum: 2 drones
  ├── Optimal: 4-6 drones
  └── Maximum: 10 drones

  COMMUNICATION:
  ├── Drone-to-drone: 433MHz telemetry
  ├── Data rate: 9600 bps
  ├── Update rate: 1 Hz
  └── Range: 1km between drones
```

---

## RETARDANT PERFORMANCE

| Parameter | Value |
|-----------|-------|
| Tank Capacity | 2 liters |
| Flow Rate | 2L/min |
| Spray Width | 3m |
| Drop Pattern | Line, spot, or surround |
| Retardant Type | Water + surfactant |
| AI Optimization | Trajectory, timing, amount |

---

## MISSION PROFILE

```
AI FIRE SUPPRESSION MISSION:
═══════════════════════════════════════════════════════════════

  Phase 1: Patrol (continuous)
  - Grid patrol at 30m AGL
  - Thermal scanning active
  - AI monitors for anomalies

  Phase 2: Fire Detection
  - Thermal trigger > 50°C
  - AI confirms fire (visual + thermal)
  - AI classifies fire size

  Phase 3: AI Assessment
  - AI predicts fire spread
  - AI calculates optimal drop zone
  - AI recommends retardant amount

  Phase 4: Suppression (human approved)
  - Operator approves drop
  - Drone positions above drop zone
  - AI controls retardant release
  - AI monitors fire response

  Phase 5: Monitoring
  - AI tracks remaining heat
  - AI detects re-ignition
  - AI recommends additional drops if needed

  Phase 6: Report
  - AI generates fire report
  - Drone returns to base
  - Retardant refilled
  - Ready for next mission
```
