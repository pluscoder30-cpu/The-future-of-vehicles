# PHI FTL TRUCK — CONTROL SYSTEM

## Vehicle Control Architecture

---

## CONTROL SYSTEM OVERVIEW

```
┌─────────────────────────────────────────────────────────────┐
│                    CONTROL ARCHITECTURE                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │ STEERING │    │ THROTTLE │    │ BRAKES   │              │
│  │ SENSOR   │    │ SENSOR   │    │ SENSOR   │              │
│  └────┬─────┘    └────┬─────┘    └────┬─────┘              │
│       │               │               │                     │
│       └───────────────┼───────────────┘                     │
│                       │                                     │
│                 ┌─────┴─────┐                               │
│                 │  MAIN ECU  │                               │
│                 │  STM32H7   │                               │
│                 └─────┬─────┘                               │
│                       │                                     │
│       ┌───────────────┼───────────────┐                     │
│       │               │               │                     │
│  ┌────┴─────┐    ┌────┴─────┐    ┌────┴─────┐              │
│  │ WARP     │    │ POWER    │    │ DISPLAY  │              │
│  │ CONTROLLER│    │ MANAGER  │    │ SYSTEM   │              │
│  │ (DSP)    │    │ (BMS)    │    │ (HUD)    │              │
│  └──────────┘    └──────────┘    └──────────┘              │
│                                                             │
│  COMMUNICATION: CAN Bus (500 kbps)                         │
│  PROTOCOL: ISO 15765-2                                     │
│  BAUD RATE: 500 kbps                                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## ECU SPECIFICATIONS

| Component | Specification |
|-----------|---------------|
| Main ECU | STM32H743VIT6 |
| CPU | ARM Cortex-M7 @ 480 MHz |
| RAM | 1 MB |
| Flash | 2 MB |
| CAN interfaces | 3 |
| ADC | 16-bit, 3.6 MSPS |
| PWM outputs | 24 |
| Operating temp | -40°C to 85°C |

---

## CAN BUS NETWORK

| Node | ID | Function |
|------|----|----------|
| Main ECU | 0x100 | Central control |
| Warp Controller | 0x200 | Field management |
| BMS | 0x300 | Battery monitoring |
| Traction Inverter | 0x400 | Motor control |
| Display | 0x500 | HUD & dashboard |
| ABS | 0x600 | Brake control |
| HVAC | 0x700 | Climate control |
| Dimensional Nav | 0x800 | FTL navigation |

---

## DRIVE MODES

| Mode | Throttle | Warp | Description |
|------|----------|------|-------------|
| ECO | 50% max | Off | Maximum range |
| NORMAL | 75% max | Off | Daily driving |
| SPORT | 100% max | Off | Maximum performance |
| WARP | 100% max | D1-D3 | Low FTL |
| TURBO WARP | 100% max | D4-D6 | High FTL |
| CRAWL | 25% max | Off | Off-road/towing |

---

## WARP CONTROL INTERFACE

```
DIMENSIONAL NAVIGATION CONTROLS:
══════════════════════════════════════════════════════════════

  ┌──────────────────────────────────────────────────┐
  │                                                  │
  │   [D0] [D1] [D2] [D3] [D4] [D5] [D6]          │
  │    ●    ○    ○    ○    ○    ○    ○              │
  │                                                  │
  │   ● = Active dimension                           │
  │   ○ = Available dimension                        │
  │                                                  │
  │   [HOME] [JUMP] [RETURN] [LOCK]                 │
  │                                                  │
  │   HOME: Return to D0 (432 Hz)                   │
  │   JUMP: Initiate dimensional jump               │
  │   RETURN: Emergency return to D0                │
  │   LOCK: Lock current dimension                  │
  │                                                  │
  │   ┌──────────────────────────────────┐          │
  │   │  DIMENSIONAL HUD                 │          │
  │   │                                  │          │
  │   │  Current: D0 (Home)              │          │
  │   │  Freq: 432 Hz                    │          │
  │   │  SoC: 85%                        │          │
  │   │  Warp: OFF                       │          │
  │   │                                  │          │
  │   └──────────────────────────────────┘          │
  │                                                  │
  └──────────────────────────────────────────────────┘
```

---

## SAFETY INTERLOCKS

| Condition | Interlock | Action |
|-----------|-----------|--------|
| SoC < 15% | Warp lock | Prevent jump |
| SoC < 5% | Force return | Emergency D0 |
| Field unstable | Warp lock | Prevent jump |
| Coil fault | Warp lock | Prevent jump |
| Temp > 50°C | Derate | Reduce power |
| Temp > 60°C | Shutdown | Emergency stop |
| Collision detected | Emergency | All stop |

---

## DIAGNOSTIC SYSTEM

```
DIAGNOSTIC MENU:
══════════════════════════════════════════════════════════════

  Access via: Hold HOME + JUMP for 5 seconds

  1. BATTERY STATUS
     - Cell voltages (20 cells)
     - Temperatures (8 sensors)
     - SoC / SoH
     - Cycle count

  2. WARP FIELD STATUS
     - Coil current (6 coils)
     - Field stability
     - Resonance lock
     - Dimensional accuracy

  3. DRIVETRAIN STATUS
     - Motor temperature
     - Inverter status
     - Speed / torque
     - Efficiency

  4. SYSTEM LOG
     - Last 100 events
     - Error codes
     - Jump history
     - Maintenance reminders
```
