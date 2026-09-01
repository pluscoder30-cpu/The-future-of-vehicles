# PHI_HUMANOID_ROBOT — System Overview

## PHI_HUMANOID_ROBOT v1.0

**Phi-Harmonic Humanoid Robot — Full-Body Design Document**

---

## 1. Executive Summary

The PHI_HUMANOID_ROBOT is a full-size humanoid robot standing 1600mm tall and weighing 50 kg, designed around phi-harmonic (φ = 1.618033988749895) principles for all mechanical, electrical, and computational systems. It walks bipedally at 5 km/h, runs at 10 km/h, manipulates objects with 5-fingered hands, speaks through phi-synthesized voice, and operates autonomously for 8 hours on a 40 kWh battery pack at a target BOM cost of $3,000.

## 2. Design Philosophy

### 2.1 Phi-Harmonic Principle

Every subsystem is organized using the golden ratio (φ = 1.618...):
- Joint actuators arranged at 137.5° angular offsets (φ-derived)
- Structural members sized in φ-proportional ratios
- Control frequencies at φ-harmonic intervals
- Balance and gait algorithms following Fibonacci-like recursive optimization
- Voice synthesis using φ-modulated waveform generation

### 2.2 Human-Scale Biomimicry

The robot's proportions follow the human body plan with φ-optimized joint placement:
- Torso-to-limb ratio follows φ proportions
- Center of mass at φ-derived height for optimal balance
- Hand span and finger lengths follow φ-sequence sizing

## 3. System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        PHI_HUMANOID_ROBOT                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │  AI CORE     │  │  POWER       │  │  SENSOR      │         │
│  │  RPi5+Coral  │  │  4×FPB-10    │  │  ARRAY       │         │
│  │  TPU         │  │  40kWh       │  │  12 sensors  │         │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘         │
│         │                 │                 │                   │
│  ┌──────┴─────────────────┴─────────────────┴──────┐           │
│  │              PHI-HARMONIC CONTROL BUS            │           │
│  │         (137.5° phi-arranged data rings)         │           │
│  └──────┬─────────────────┬─────────────────┬──────┘           │
│         │                 │                 │                   │
│  ┌──────┴──────┐  ┌──────┴──────┐  ┌──────┴──────┐           │
│  │  LEFT LEG   │  │  TORSO      │  │  RIGHT LEG  │           │
│  │  6 DOF      │  │  2 DOF      │  │  6 DOF      │           │
│  └─────────────┘  └─────────────┘  └─────────────┘           │
│                                                                 │
│  ┌─────────────┐                ┌─────────────┐               │
│  │  LEFT ARM   │                │  RIGHT ARM  │               │
│  │  6 DOF      │                │  6 DOF      │               │
│  └─────────────┘                └─────────────┘               │
│                                                                 │
│  ┌──────────────────────────────────────────────┐             │
│  │  HEAD — 2 DOF (pan/tilt), cameras, audio    │             │
│  └──────────────────────────────────────────────┘             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 4. Key Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| Height | 1600 mm (63.0 in) | Adjustable ±50mm at torso |
| Weight | 50 kg (110 lb) | Including batteries |
| Degrees of Freedom | 30 total | 6+6 legs, 6+6 arms, 2 torso, 2 head |
| Walking Speed | 5 km/h (3.1 mph) | Natural bipedal gait |
| Running Speed | 10 km/h (6.2 mph) | Dynamic running gait |
| Battery Life | 8 hours | Mixed use, 5 km/h walking |
| Battery Pack | 4× FPB-10 | 40 kWh total (10 kWh each) |
| AI Platform | Raspberry Pi 5 + Coral TPU | 4 TOPS edge AI |
| Cameras | 2× stereo camera modules | 1280×800, 60fps, depth sensing |
| Microphones | 4-microphone array | Far-field voice, beamforming |
| Speakers | 2× 3W speakers | Phi-harmonic voice synthesis |
| Hands | 5-fingered grippers | Force-sensing fingertips, 1N resolution |
| BOM Cost | $3,000 target | Excludes assembly labor |

## 5. Document Map

| Doc | Title | Contents |
|-----|-------|----------|
| 00 | Overview | This document — system-level summary |
| 01 | Parts List | Complete parts with quantities and suppliers |
| 02 | Wiring | Full electrical wiring diagrams |
| 03 | Mechanical | Mechanical drawings and dimensions |
| 04 | Circuit | Custom PCB schematics |
| 05 | Assembly | Step-by-step assembly procedure |
| 06 | Safety | Safety systems, emergency stops, risk matrix |
| 07 | Performance | Performance specs, benchmarks, timing |
| 08 | Phi Physics | Phi-harmonic physics derivations |
| 09 | Regulatory | FCC, UL, CE compliance roadmap |
| 10 | Complete BOM | Full bill of materials with pricing |
| 11 | Phi-Harmonic Specs | Detailed phi-harmonic system specs |
| 12 | Power System | Battery, power distribution, thermal |
| 13 | Control System | Software, firmware, control loops |
| README | Quick Start | Build summary and getting started |
| MANUAL | Owner's Manual | Operating instructions and maintenance |

## 6. System Block Diagram

```
                    ┌─────────────────────────┐
                    │     HEAD SUBSYSTEM      │
                    │  ┌─────────┐ ┌────────┐ │
                    │  │Stereo   │ │4-Mic   │ │
                    │  │Cameras  │ │Array   │ │
                    │  │2× 60fps │ │        │ │
                    │  └────┬────┘ └───┬────┘ │
                    │       │          │      │
                    │  ┌────┴────┐ ┌───┴────┐ │
                    │  │2× 3W    │ │IMU 9DoF│ │
                    │  │Speakers │ │        │ │
                    │  └────┬────┘ └───┬────┘ │
                    └───────┼──────────┼──────┘
                            │          │
                    ┌───────┴──────────┴──────┐
                    │    AI CORE (RPi 5)      │
                    │  ┌──────────┐           │
                    │  │Coral TPU │ ← 4 TOPS  │
                    │  │(USB)     │           │
                    │  └──────────┘           │
                    │  ┌──────────┐           │
                    │  │WiFi/BLE  │           │
                    │  │          │           │
                    │  └──────────┘           │
                    └───┬────┬────┬────┬──────┘
                        │    │    │    │
              ┌─────────┘    │    │    └─────────┐
              │              │    │              │
    ┌─────────┴──┐  ┌────────┴──┐ ┌────────┐  ┌─┴──────────┐
    │ LEFT LEG   │  │LEFT ARM   │ │RIGHT   │  │RIGHT LEG   │
    │            │  │           │ │ARM     │  │            │
    │ HAA/HFE/KFE│  │ SAA/SFE/  │ │SAA/SFE/│  │HAA/HFE/KFE│
    │ KAA/AFE/   │  │ SHS/ELF/  │ │SHS/ELF/│  │KAA/AFE/   │
    │ TOE (6)    │  │ WFE/WRU   │ │WFE/WRU │  │TOE (6)    │
    │            │  │  (6)      │ │(6)     │  │            │
    │ Force      │  │ Force     │ │Force   │  │Force       │
    │ Sensors(3) │  │ Sensors(6)│ │Sensors(6│  │Sensors(3)  │
    └────────────┘  └───────────┘ └────────┘  └────────────┘
              │              │    │              │
              └──────────────┴────┴──────────────┘
                        POWER BUS
                   ┌─────────────────┐
                   │  4× FPB-10      │
                   │  48V / 40kWh    │
                   │  BMS + Thermal   │
                   └─────────────────┘
```

## 7. Phi-Harmonic Integration Points

| System | Phi-Harmonic Method | Implementation |
|--------|-------------------|----------------|
| Joint Actuators | 137.5° motor mounting angles | Each joint pair offset by φ×90° |
| Balance | Fibonacci feedback gains | Recursive gain scheduling |
| Gait | φ-optimized stride timing | Left/right phase offset = φ mod 1 |
| Hand Dexterity | φ-sequence finger coordination | Fibonacci-order finger sequencing |
| Voice Synthesis | φ-modulated formants | Golden-ratio frequency modulation |
| Structural | φ-ratio beam dimensions | Member lengths in φ-proportional series |

## 8. Operating Environments

| Parameter | Specification |
|-----------|--------------|
| Indoor Temperature | 10°C to 35°C |
| Outdoor Temperature | 0°C to 30°C (no rain) |
| Humidity | 10% to 80% RH, non-condensing |
| Floor Surface | Flat, level, indoor flooring |
| Max Slope | 5° sustained, 15° momentary |
| Max Step Height | 100mm (4 inches) |
| Dust/Water Rating | IP54 (splash-proof) |

## 9. Development Timeline

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| Phase 1: Mechanical | 4 weeks | Frame, joints, structure |
| Phase 2: Electrical | 3 weeks | Wiring, PCBs, power |
| Phase 3: Firmware | 3 weeks | Motor control, sensors |
| Phase 4: Software | 4 weeks | AI, gait, perception |
| Phase 5: Integration | 2 weeks | System bring-up |
| Phase 6: Testing | 2 weeks | Validation, calibration |
| **Total** | **18 weeks** | **Working robot** |

---

*Document: 00_OVERVIEW.md — PHI_HUMANOID_ROBOT System Overview*
*Version: 1.0 | Date: 2026-08-27*
