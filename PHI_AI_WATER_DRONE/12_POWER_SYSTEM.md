# PHI AI WATER DRONE — POWER SYSTEM

## FPB-5 Battery and Power Distribution (AI-Enhanced)

---

## FPB-5 BATTERY

Same as standard PHI Water Drone — 12V, 50Ah, 600Wh.

---

## POWER CONSUMPTION

| Component | Voltage | Current | Power |
|-----------|---------|---------|-------|
| Motors (4x) | 12V | 10A total | 120W |
| Arduino | 5V | 200mA | 1W |
| Water Sensors | 5V | 50mA | 0.25W |
| AI System | 5V | 540mA | 2.7W |
| Filtration Pump | 12V | 1.5A | 18W |
| Frequency Gen | 5V | 100mA | 0.5W |
| **Total (flight)** | | | **124W** |
| **Total (cleaning)** | | | **142W** |

---

## FLIGHT TIME

```
HOVER ENDURANCE:
═══════════════════════════════════════════════════════════════

  Battery: 600Wh
  Hover power: 124W (without pump)
  Cleaning power: 142W (with pump)
  Efficiency: 0.85

  Hover time: 510/124 = 4.1 hours
  Cleaning time: 510/142 = 3.6 hours

  Conservative: 3.5 hours hover, 3.0 hours cleaning
```

---

## AI POWER MANAGEMENT

```
AI POWER STATES:
═══════════════════════════════════════════════════════════════

  SURVEY: AI mapping contamination
  ├── Power: 2.7W
  ├── Use: During water survey
  └── Camera: Active for water color analysis

  CLEANING: AI guiding filtration
  ├── Power: 2.7W
  ├── Use: During cleaning operations
  └── Pump: AI-controlled duty cycle

  COORDINATION: Multi-drone comms
  ├── Power: 2.7W + radio
  ├── Use: Multi-drone operations
  └── Data sharing active
```
