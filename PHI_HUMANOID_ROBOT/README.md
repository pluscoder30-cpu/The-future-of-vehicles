# PHI_HUMANOID_ROBOT

## Phi-Harmonic Humanoid Robot v1.0

---

## Quick Start

The PHI_HUMANOID_ROBOT is a full-size humanoid robot (1600mm, 50kg, 30 DOF) built around the golden ratio (φ = 1.618...) for all mechanical, electrical, and computational systems.

### Key Specs

| Parameter | Value |
|-----------|-------|
| Height | 1600mm (5'3") |
| Weight | 50 kg (110 lb) |
| Degrees of Freedom | 30 |
| Walking Speed | 5 km/h |
| Running Speed | 10 km/h |
| Battery Life | 8 hours |
| Battery | 4× FPB-10 (40 kWh) |
| AI | Raspberry Pi 5 + Coral TPU |
| Cost Target | $3,000 BOM |

### Phi-Harmonic Features

- **Joint actuators**: 137.5° angular offset (φ × 90°)
- **Balance system**: Fibonacci recursive PID gains
- **Gait optimization**: φ-phase offset, φ² stride length
- **Hand dexterity**: Fibonacci finger coordination sequence
- **Voice synthesis**: φ-modulated formant structure

---

## Repository Structure

```
PHI_HUMANOID_ROBOT/
├── 00_OVERVIEW.md          # System-level summary
├── 01_PARTS_LIST.md        # Complete parts with suppliers
├── 02_WIRING.md            # Electrical wiring diagrams
├── 03_MECHANICAL.md        # Mechanical drawings & dimensions
├── 04_CIRCUIT.md           # Custom PCB schematics
├── 05_ASSEMBLY.md          # Step-by-step assembly guide
├── 06_SAFETY.md            # Safety systems & risk assessment
├── 07_PERFORMANCE.md       # Performance benchmarks
├── 08_PHI_PHYSICS.md       # Phi-harmonic physics derivations
├── 09_REGULATORY.md        # FCC, UL, CE compliance
├── 10_COMPLETE_BOM.md      # Full bill of materials
├── 11_PHI_HARMONIC_SPECS.md # Detailed φ-harmonic specs
├── 12_POWER_SYSTEM.md      # Battery & power distribution
├── 13_CONTROL_SYSTEM.md    # Software & firmware architecture
├── README.md               # This file
└── MANUAL.md               # Owner's manual
```

---

## Build Summary

### Total Build Time
~53 hours (8 phases)

### Required Skills
- Mechanical assembly (hex keys, torque wrench)
- Electrical wiring (soldering, crimping)
- Software setup (Linux, Python, firmware)
- System calibration (balance, gait, hands)

### Critical Path
1. Frame assembly (8h)
2. Actuator installation (11h)
3. Electrical wiring (8h)
4. Software setup (12h)
5. Calibration (6h)

---

## Cost Breakdown

| Category | Cost | % |
|----------|------|---|
| Power System | $2,068 | 44.5% |
| Compute/AI | $1,395 | 30.0% |
| Actuators | $1,576 | 33.9% |
| Sensors | $651 | 14.0% |
| Structure | $474 | 10.2% |
| Other | $480 | 10.3% |
| **Total BOM** | **$4,641** | — |

**Target at volume (100+ units): $3,000**

---

## Phi-Harmonic Integration

Every subsystem uses the golden ratio (φ = 1.618...) as its organizing principle:

| System | φ-Application |
|--------|--------------|
| Joint actuators | 137.5° angular offset |
| Balance | Fibonacci recursive gains |
| Gait | φ-phase offset, φ² stride |
| Hands | Fibonacci finger order |
| Voice | φ-formant spacing |
| Structure | φ-ratio member sizing |
| Holes | φ-spiral pattern |

---

## Getting Started

1. Read `00_OVERVIEW.md` for system architecture
2. Review `01_PARTS_LIST.md` for component sourcing
3. Follow `05_ASSEMBLY.md` for build procedure
4. Configure software per `13_CONTROL_SYSTEM.md`
5. Calibrate per `05_ASSEMBLY.md` Phase 8

---

## Safety

⚠️ **This is a 50 kg robot with powerful motors.**

- Always use e-stop before approaching
- Keep 2m distance during operation
- Adult supervision required
- Not suitable for children under 14
- See `06_SAFETY.md` for complete safety information

---

*PHI_HUMANOID_ROBOT v1.0 — Built on the Golden Ratio*
*Document: README.md | Date: 2026-08-27*
