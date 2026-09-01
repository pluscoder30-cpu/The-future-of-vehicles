# PHI AI FIRE DRONE — POWER SYSTEM

## FPB-10 Battery System (AI-Enhanced)

---

## FPB-10 BATTERY SYSTEM

Two FPB-5 batteries in series for 24V system:

| Parameter | Value |
|-----------|-------|
| Configuration | 2x FPB-5 in series |
| Nominal Voltage | 24.0V |
| Capacity | 50Ah |
| Energy | 1200Wh |
| Weight | 1700g |
| Max Discharge | 30A continuous |
| Cost | $170 |

---

## POWER CONSUMPTION

### Flight Mode

| Component | Voltage | Current | Power |
|-----------|---------|---------|-------|
| Motors (4x) | 24V | 12A total | 288W |
| Arduino | 5V | 200mA | 1W |
| Sensors | 5V | 100mA | 0.5W |
| Thermal Camera | 3.3V | 25mA | 0.08W |
| AI System | 5V | 540mA | 2.7W |
| Retardant Pump | 12V | 2A | 24W (when active) |
| **Total (flight)** | | | **292W** |
| **Total (dropping)** | | | **316W** |

### Hover Time

```
HOVER ENDURANCE:
═══════════════════════════════════════════════════════════════

  Battery capacity: 1200Wh
  Hover power: 292W
  Efficiency factor: 0.85

  Effective capacity: 1200 × 0.85 = 1020Wh

  Hover time = 1020Wh / 292W = 3.49 hours

  With 2kg retardant payload:
  Additional motor power: ~40W
  Total hover power: 332W
  Hover time = 1020 / 332 = 3.07 hours

  Conservative estimate: 3.0 hours
```

---

## AI POWER MANAGEMENT

```
AI POWER STATES:
═══════════════════════════════════════════════════════════════

  PATROL: AI thermal scanning active
  ├── Power: 2.7W (camera + inference)
  ├── Use: During patrol operations
  └── Duration: Most of mission

  SUPPRESSION: AI controlling retardant
  ├── Power: 2.7W + pump overhead
  ├── Use: During fire suppression
  └── Duration: 5-15 minutes per fire

  COORDINATION: AI communicating with swarm
  ├── Power: 2.7W + radio overhead
  ├── Use: Multi-drone operations
  └── Duration: Variable
```
