# PHI FTL CAR — CONTROL SYSTEM

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
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## DRIVE MODES

| Mode | Throttle | Warp | Description |
|------|----------|------|-------------|
| ECO | 45% max | Off | Maximum range |
| NORMAL | 70% max | Off | Daily driving |
| SPORT | 100% max | Off | Maximum performance |
| COMFORT | 60% max | Off | Passenger comfort |
| WARP | 100% max | D1-D3 | Low FTL |
| TURBO WARP | 100% max | D4-D6 | High FTL |

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
  │   ┌──────────────────────────────────┐          │
  │   │  DIMENSIONAL HUD                 │          │
  │   │                                  │          │
  │   │  Current: D0 (Home)              │          │
  │   │  Freq: 432 Hz                    │          │
  │   │  SoC: 88%                        │          │
  │   │  Warp: OFF                       │          │
  │   │  Passengers: 4                   │          │
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
| Door open | Warp lock | Prevent jump |
| Seatbelt unfastened | Warning | Alert driver |
| Temp > 50°C | Derate | Reduce power |
| Temp > 60°C | Shutdown | Emergency stop |
| Collision detected | Emergency | All stop |
