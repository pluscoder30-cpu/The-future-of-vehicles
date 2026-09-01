# PHI_FIELD_ROBOT

## Field Autonomous Robot for Outdoor Operations

---

## Quick Facts

| Parameter | Value |
|-----------|-------|
| **Type** | 4-legged quadruped robot |
| **Height** | 600mm (2'0") |
| **Weight** | 30 kg (66 lbs) |
| **Speed** | 8 km/h (5 mph) |
| **Payload** | 10 kg (22 lbs) arm |
| **Battery** | 6 hours (20 kWh) |
| **Cost** | $2,000 target |
| **AI** | Raspberry Pi 5 + Coral TPU |
| **Phi-Harmonic** | Gait, balance, grip, navigation |

---

## Applications

- **Agriculture**: Crop monitoring, soil sampling, targeted spraying
- **Construction**: Site surveying, material transport, inspection
- **Search & Rescue**: Disaster zone exploration, victim detection
- **Environmental**: Water sampling, air quality, wildlife monitoring

---

## Phi-Harmonic Features

- **Gait**: φ-ratio timing for natural, efficient walking
- **Balance**: φ-adaptive IMU filtering and PID control
- **Grip**: φ-compliant force control for delicate objects
- **Navigation**: φ-A* pathfinding with terrain adaptation

---

## Document Set

| Doc | Title | Description |
|-----|-------|-------------|
| 00 | Overview | System overview and architecture |
| 01 | Parts List | Every component with specs |
| 02 | Wiring | Complete electrical diagrams |
| 03 | Mechanical | Frame, joints, dimensions |
| 04 | Circuit | PCB designs, schematics |
| 05 | Assembly | Step-by-step build guide |
| 06 | Safety | Warnings, safe operation |
| 07 | Performance | Benchmarks, test results |
| 08 | Phi Physics | Mathematical foundations |
| 09 | Regulatory | Compliance requirements |
| 10 | Complete BOM | Costed bill of materials |
| 11 | Phi-Harmonic Specs | Gait, balance, grip math |
| 12 | Power System | Battery, BMS, charging |
| 13 | Control System | Software architecture |
| **README** | **Quick Reference** | **This document** |
| MANUAL | Operator Manual | User guide |

---

## Key Specifications

### Locomotion
- 12-DOF quadruped (4 legs × 3 joints)
- 12× 250W brushless DC motors
- Phi-harmonic gait coordination
- Any terrain: stairs, rocks, mud, grass

### Manipulation
- 5-DOF robotic arm
- 10 kg payload at full extension
- Phi-harmonic grip control
- Force-torque sensor at wrist

### Perception
- 4× cameras (360° coverage)
- 1× LIDAR (360° scan)
- 9-axis IMU
- 4× force-sensitive resistors (feet)
- GPS module

### Intelligence
- Raspberry Pi 5 (8GB)
- Google Coral TPU (4 TOPS)
- ROS 2 Humble
- Custom phi-harmonic control stack

### Power
- 2× FPB-10 batteries (10 kWh each)
- 48V main bus
- Smart BMS with phi-balancing
- 6-hour runtime, 3-hour charge

---

## Cost Breakdown

| Category | Cost | % |
|----------|------|---|
| Motors (17×) | $680 | 34% |
| Controllers & Sensors | $420 | 21% |
| AI Compute | $250 | 12.5% |
| Power System | $300 | 15% |
| Mechanical | $200 | 10% |
| Cameras & LIDAR | $100 | 5% |
| Misc | $50 | 2.5% |
| **Total** | **$2,000** | **100%** |

---

## Quick Start

1. Read `06_SAFETY.md` before operation
2. Read `05_ASSEMBLY.md` for build instructions
3. Read `MANUAL.md` for operation guide
4. Charge batteries fully before first use
5. Run self-test routine
6. Begin supervised operation

---

## License

CERN-OHL-P-2.0 (Hardware)
Apache 2.0 (Software)
CC-BY-SA-4.0 (Documentation)

---

*Version: 1.0*
*Date: 2026-08-27*
*Author: Build Agent 5 of 6*
