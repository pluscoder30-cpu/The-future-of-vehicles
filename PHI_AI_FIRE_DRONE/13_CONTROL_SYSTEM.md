# PHI AI FIRE DRONE — CONTROL SYSTEM

## Avionics, AI, and Fire Autonomy

---

## SYSTEM ARCHITECTURE

```
DUAL-PROCESSOR ARCHITECTURE:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────────────────────────┐
  │                    ARDUINO MEGA 2560                     │
  │                    (Flight Controller)                   │
  │                                                         │
  │  Flight Control ──── Motor Output ──── ESCs            │
  │  Sensor Fusion ───── GPS/IMU/Baro                      │
  │  Retardant Control ─ Pump/Valve PWM                    │
  │  AI Communication ── Serial to Pi Zero                 │
  └─────────────────────────────────────────────────────────┘
                              │
                              │ Serial (115200 baud)
                              │
  ┌─────────────────────────────────────────────────────────┐
  │                 RASPBERRY PI ZERO 2W                     │
  │                 (AI Fire Processor)                      │
  │                                                         │
  │  Thermal Analysis ──── Fire Detection ──── Spread Model │
  │  Visual Confirmation ── Camera ────────── OpenCV       │
  │  Swarm Coordination ── Drone-to-Drone ── Protocol      │
  │  Drop Optimization ─── Trajectory Calc ── AI Engine    │
  └─────────────────────────────────────────────────────────┘
```

---

## FLIGHT MODES

| Mode | Description | AI Role | Control |
|------|-------------|---------|---------|
| PATROL | Grid search pattern | Thermal scanning | Auto |
| INVESTIGATE | Check anomaly | AI confirms fire | Auto |
| SUPPRESS | Fire fighting | AI guides drops | AI + Human |
| SWARM | Multi-drone ops | AI coordinates | AI + Human |
| RTB | Return to base | None | Auto |
| EMERGENCY | Motor shutdown | None | None |

---

## AI FIRE MISSION FLOW

```
AI FIRE SUPPRESSION MISSION:
═══════════════════════════════════════════════════════════════

  1. PATROL: Drone patrols grid autonomously
  2. DETECT: AI thermal scan triggers on heat
  3. CONFIRM: AI visual + thermal confirms fire
  4. ASSESS: AI classifies fire size and type
  5. PREDICT: AI models fire spread (5-min outlook)
  6. RECOMMEND: AI suggests drop zone and amount
  7. APPROVE: Human operator confirms drop plan
  8. EXECUTE: AI guides drone to position
  9. DROP: AI controls retardant release
  10. MONITOR: AI tracks fire response
  11. FOLLOW-UP: AI recommends additional action
  12. REPORT: AI generates mission summary
```

---

## SWARM COMMUNICATION

```
DRONE-TO-DRONE PROTOCOL:
═══════════════════════════════════════════════════════════════

  ┌──────────────────────────────────────────────────────┐
  │  SWARM PACKET (433MHz telemetry)                    │
  │                                                      │
  │  Byte 0-1: Header (0xFF 0xAA)                      │
  │  Byte 2: Drone ID (1-10)                            │
  │  Byte 3: Role (0=lead, 1=wing)                     │
  │  Byte 4-7: Fire GPS Lat (float)                    │
  │  Byte 8-11: Fire GPS Lon (float)                   │
  │  Byte 12-13: Fire temp (0.1°C)                     │
  │  Byte 14: Fire size (m²)                           │
  │  Byte 15-16: Retardant remaining (mL)              │
  │  Byte 17: Battery SoC (%)                          │
  │  Byte 18: AI spread direction (degrees)            │
  │  Byte 19: AI spread rate (m/min)                   │
  │  Byte 20: Assigned sector (0-7)                    │
  │  Byte 21: Status (patrol/drop/return)              │
  │  Byte 22-23: Checksum (CRC16)                      │
  └──────────────────────────────────────────────────────┘

  Total: 24 bytes per packet
  Rate: 1 packet/second
  Drones supported: 10
```
