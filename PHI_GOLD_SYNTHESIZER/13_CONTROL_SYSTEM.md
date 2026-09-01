# PHI GOLD SYNTHESIZER — CONTROL SYSTEM

## Device Control Architecture

---

## CONTROL SYSTEM OVERVIEW

```
┌─────────────────────────────────────────────────────────────┐
│                    CONTROL ARCHITECTURE                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │ TEMP     │    │ CURRENT  │    │ VOLTAGE  │              │
│  │ SENSORS  │    │ SENSOR   │    │ SENSOR   │              │
│  │ (3×)     │    │ (50A)    │    │ (48V)    │              │
│  └────┬─────┘    └────┬─────┘    └────┬─────┘              │
│       │               │               │                     │
│       └───────────────┼───────────────┘                     │
│                       │                                     │
│                 ┌─────┴─────┐                               │
│                 │  MAIN ECU  │                               │
│                 │  ESP32-S3  │                               │
│                 └─────┬─────┘                               │
│                       │                                     │
│       ┌───────────────┼───────────────┐                     │
│       │               │               │                     │
│  ┌────┴─────┐    ┌────┴─────┐    ┌────┴─────┐              │
│  │ RESONANCE│    │ FEEDSTOCK│    │ DISPLAY  │              │
│  │ CONTROLLER│   │ SYSTEM   │    │ SYSTEM   │              │
│  │ (PLL)    │    │ (Valve)  │    │ (7" LCD) │              │
│  └──────────┘    └──────────┘    └──────────┘              │
│                                                             │
│  COMMUNICATION: I2C, SPI, GPIO, UART                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## PRODUCTION MODES

| Mode | Power | Rate | Description |
|------|-------|------|-------------|
| STANDBY | 15W | 0g/hr | Display on, heater off |
| WARM-UP | 200W | 0g/hr | Heating chamber to temp |
| PRODUCTION | 600W | 10g/hr | Full transmutation |
| HIGH-SPEED | 800W | 14g/hr | Maximum output |
| COOLDOWN | 25W | 0g/hr | Safe shutdown |
| MAINTENANCE | 50W | 0g/hr | Service mode |

---

## TOUCHSCREEN INTERFACE

```
MAIN SCREEN LAYOUT:
═══════════════════════════════════════════════════════════════

  ┌──────────────────────────────────────────────────┐
  │                                                  │
  │   PHI GOLD SYNTHESIZER v1.0                     │
  │   ─────────────────────────────                 │
  │                                                  │
  │   STATUS: ● PRODUCING                           │
  │   MODE:   [STANDBY] [WARM] [RUN] [HIGH] [STOP] │
  │                                                  │
  │   ┌─────────────────────────────────────┐       │
  │   │  CHAMBER TEMP:     1,185°C          │       │
  │   │  COIL TEMP:        72°C             │       │
  │   │  AMBIENT TEMP:     28°C             │       │
  │   │                                     │       │
  │   │  BATTERY SoC:      68%              │       │
  │   │  BATTERY VOLTAGE:  46.8V            │       │
  │   │  CURRENT:          12.5A            │       │
  │   │  POWER:            600W             │       │
  │   │                                     │       │
  │   │  GOLD PRODUCED:    42.5g            │       │
  │   │  PRODUCTION RATE:  10.2 g/hr        │       │
  │   │  RUN TIME:         4h 15m           │       │
  │   │  PURITY:           99.99%           │       │
  │   │                                     │       │
  │   │  FEEDSTOCK LEVEL:  ████████░░ 80%   │       │
  │   │  RESONANCE:        LOCKED           │       │
  │   │  FREQUENCY:        432.0 Hz         │       │
  │   │                                     │       │
  │   └─────────────────────────────────────┘       │
  │                                                  │
  │   [START] [STOP] [SETTINGS] [HISTORY]           │
  │                                                  │
  └──────────────────────────────────────────────────┘
```

---

## STATUS RING INDICATORS

| Color | Pattern | Meaning |
|-------|---------|---------|
| Green (solid) | Steady | Production running normally |
| Green (pulse) | Slow blink | Warm-up in progress |
| Blue (solid) | Steady | Standby, ready to start |
| Blue (pulse) | Slow blink | Cooldown in progress |
| Yellow (solid) | Steady | Low feedstock warning |
| Yellow (pulse) | Fast blink | High temperature warning |
| Red (solid) | Steady | Error — check display |
| Red (pulse) | Fast blink | Emergency stop active |
| White (pulse) | Slow blink | Charging battery |
| Off | — | Power off |

---

## SAFETY INTERLOCKS

| Condition | Interlock | Action |
|-----------|-----------|--------|
| SoC < 20% | Production lock | Prevent start |
| SoC < 10% | Force stop | Auto-shutdown |
| Chamber temp > 1,250°C | Over-temp | Auto-shutdown |
| Coil temp > 100°C | Over-temp | Reduce power |
| No feedstock | Feed lock | Prevent start |
| Chamber lid open | Lid interlock | Prevent start |
| E-Stop pressed | Emergency | All systems off |
| Current > 55A | Over-current | Main fuse blow |
| Resonance unlocked | Resonance lock | Prevent production |
| Cooling fan fail | Thermal lock | Auto-shutdown |

---

## CONTROL SEQUENCE

```
PRODUCTION SEQUENCE:
═══════════════════════════════════════════════════════════════

  1. STANDBY
     │
     ├─► Load feedstock (manual or auto)
     ├─► Verify all sensors OK
     ├─► Check battery SoC > 20%
     └─► Press START
         │
         ▼
  2. WARM-UP (15 minutes)
     │
     ├─► Chamber heater ON
     ├─► Monitor temperature rise
     ├─► Wait for 1,200°C
     └─► Auto-transition to PRODUCTION
         │
         ▼
  3. PRODUCTION (2-4 hours)
     │
     ├─► Resonance coils ON
     ├─► Auto-tune to resonance peak
     ├─► Feedstock valve opens
     ├─► Monitor transmutation progress
     ├─► Display gold production rate
     └─► Auto-transition to COOLDOWN when:
         - Feedstock empty, or
         - User presses STOP, or
         - SoC < 20%
         │
         ▼
  4. COOLDOWN (30 minutes)
     │
     ├─► Resonance coils OFF
     ├─► Chamber heater OFF
     ├─► Cooling fans ON max
     ├─► Wait for 50°C
     └─► Auto-transition to STANDBY
```

---

## DATA LOGGING

| Metric | Sample Rate | Storage |
|--------|-------------|---------|
| Chamber temperature | 1 Hz | SD card |
| Coil temperatures | 1 Hz | SD card |
| Battery SoC | 0.1 Hz | SD card |
| Current draw | 1 Hz | SD card |
| Gold produced | 0.01 Hz | SD card |
| Resonance frequency | 1 Hz | SD card |
| Run time | Continuous | SD card |
| Error events | On occurrence | SD card |

---

## WIFI CONNECTIVITY

| Feature | Description |
|---------|-------------|
| AP Mode | Direct connection for setup |
| STA Mode | Connect to home WiFi |
| Web Interface | Browser-based monitoring |
| MQTT | IoT integration |
| OTA Updates | Firmware over-the-air |
| Remote Monitoring | Check status from phone |

---

## CALIBRATION

| Parameter | Method | Frequency |
|-----------|--------|-----------|
| Temperature sensors | Ice bath (0°C) + boiling water (100°C) | Every 100 hours |
| Current sensor | Known load test | Every 100 hours |
| Voltage sensor | Reference voltage | Every 100 hours |
| Resonance frequency | Auto-tune against chamber | Every run |
| Gold purity | XRF analysis (external) | Every 500 hours |
| Production rate | Weight measurement | Every run |
