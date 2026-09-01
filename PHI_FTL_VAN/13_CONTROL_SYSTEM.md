# PHI FTL VAN — CONTROL SYSTEM

## Vehicle Control Architecture

---

## DRIVE MODES

| Mode | Throttle | Warp | Description |
|------|----------|------|-------------|
| ECO | 50% max | Off | Maximum range |
| NORMAL | 75% max | Off | Daily driving |
| CARGO | 60% max | Off | Cargo transport |
| SPORT | 100% max | Off | Maximum performance |
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
  │   │  SoC: 90%                        │          │
  │   │  Warp: OFF                       │          │
  │   │  Cargo: 3,200 kg / 6,000 kg     │          │
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
| Cargo shift detected | Warp lock | Prevent jump |
| Cargo overload | Warning | Alert driver |
| Temp > 50°C | Derate | Reduce power |
| Temp > 60°C | Shutdown | Emergency stop |
| Collision detected | Emergency | All stop |
