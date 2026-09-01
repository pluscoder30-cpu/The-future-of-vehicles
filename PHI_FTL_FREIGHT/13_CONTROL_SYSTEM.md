# PHI FTL FREIGHT — CONTROL SYSTEM

## Vehicle Control Architecture

---

## DRIVE MODES

| Mode | Throttle | Warp | Description |
|------|----------|------|-------------|
| ECO | 40% max | Off | Maximum range |
| NORMAL | 65% max | Off | Daily driving |
| FREIGHT | 50% max | Off | Heavy freight |
| HAUL | 80% max | Off | Maximum performance |
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
  │   [HOME] [JUMP] [RETURN] [LOCK]                 │
  │                                                  │
  │   ┌──────────────────────────────────┐          │
  │   │  DIMENSIONAL HUD                 │          │
  │   │                                  │          │
  │   │  Current: D0 (Home)              │          │
  │   │  Freq: 432 Hz                    │          │
  │   │  SoC: 95%                        │          │
  │   │  Warp: OFF                       │          │
  │   │  Freight: 35,000 kg / 50,000 kg │          │
  │   │  Air Brake: 120 PSI             │          │
  │   │  Trailer: COUPLED               │          │
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
| Freight shift detected | Warp lock | Prevent jump |
| Freight overload | Warning | Alert driver |
| Air brake low | Warning | Alert driver |
| Trailer disconnect | Warp lock | Prevent jump |
| Temp > 50°C | Derate | Reduce power |
| Temp > 60°C | Shutdown | Emergency stop |
| Collision detected | Emergency | All stop |
