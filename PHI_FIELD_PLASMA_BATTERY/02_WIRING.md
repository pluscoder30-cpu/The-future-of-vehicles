# PHI-HARMONIC FIELD PLASMA BATTERY — WIRING DIAGRAM

## Complete Electrical Schematic

---

## System Overview

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    PHI-HARMONIC PLASMA BATTERY - WIRING                     ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  ┌────────────────────────────────────────────────────────────────────────┐  ║
║  │                         POWER INPUT BUS                                │  ║
║  │  (From harvesting: piezo, thermo, RF, solar)                          │  ║
║  │                                                                        │  ║
║  │  Vibration ──▶ Piezo ──┐                                              │  ║
║  │  Thermal ──▶ Thermo ───┤                                              │  ║
║  │  EMF ──▶ Coil ─────────┤                                              │  ║
║  │  Solar ──▶ Panel ──────┤                                              │  ║
║  │                        │                                              │  ║
║  │                   ┌────▼────┐                                          │  ║
║  │                   │ RECTIFI-│                                          │  ║
║  │                   │ ER +    │                                          │  ║
║  │                   │ FILTER  │                                          │  ║
║  │                   └────┬────┘                                          │  ║
║  │                        │                                               │  ║
║  └────────────────────────┼───────────────────────────────────────────────┘  ║
║                           │                                                 ║
║                           ▼                                                 ║
║  ┌────────────────────────────────────────────────────────────────────────┐  ║
║  │                    MAIN POWER BUS (48V DC)                             │  ║
║  │                                                                        │  ║
║  │        ┌──────────────┬──────────────┬──────────────┐                 │  ║
║  │        │              │              │              │                  │  ║
║  │        ▼              ▼              ▼              ▼                  │  ║
║  │   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐             │  ║
║  │   │DC-DC    │   │CONTAIN- │   │POWER    │   │MONITOR- │             │  ║
║  │   │CONVERT  │   │MENT     │   │OUTPUT   │   │ING      │             │  ║
║  │   │(48V→48V)│   │CONTROL  │   │STAGE    │   │CIRCUIT  │             │  ║
║  │   └────┬────┘   └────┬────┘   └────┬────┘   └────┬────┘             │  ║
║  │        │              │              │              │                  │  ║
║  │        ▼              ▼              ▼              ▼                  │  ║
║  │   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐             │  ║
║  │   │ BATTERY │   │ COIL    │   │ LOAD    │   │ DISPLAY │             │  ║
║  │   │ CHARGE  │   │ ARRAY   │   │ OUTPUT  │   │ + LED   │             │  ║
║  │   │ CIRCUIT │   │ (5 coils)│  │ (XT90)  │   │ STATUS  │             │  ║
║  │   └─────────┘   └─────────┘   └─────────┘   └─────────┘             │  ║
║  │                                                                        │  ║
║  └────────────────────────────────────────────────────────────────────────┘  ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## Coil Array Wiring (The Golden Spiral)

```
    PHI-HARMONIC COIL ARRAY WIRING
    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │                    COIL ARRAY (Top View)                    │
    │                                                             │
    │                      Coil 1 (0°)                            │
    │                          │                                  │
    │                    ┌─────┴─────┐                            │
    │               ┌────┤           ├────┐                       │
    │          ┌────┤    │     ●     │    ├────┐                  │
    │          │    │    │   CENTER  │    │    │                  │
    │     ┌────┤    │    │           │    │    ├────┐             │
    │  Coil 5   │    │    │           │    │    │   Coil 2        │
    │  (272°)   │    │    │           │    │    │  (137.5°)      │
    │     │    │    │    │           │    │    │    │             │
    │     └────┤    │    │           │    │    ├────┘             │
    │          │    │    │           │    │    │                  │
    │          └────┤    │           │    ├────┘                  │
    │               │    │           │    │                       │
    │               └────┤           ├────┘                       │
    │                    │           │                            │
    │                    └─────┬─────┘                            │
    │                          │                                  │
    │                      Coil 4 (225°)     Coil 3 (72.5°)      │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
    
    WIRING:
    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   POWER BUS (48V) ──────────────────────────────────────   │
    │        │           │           │           │           │     │
    │        ▼           ▼           ▼           ▼           ▼     │
    │   ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐  ┌──────┐│
    │   │  FET   │  │  FET   │  │  FET   │  │  FET   │  │ FET  ││
    │   │  Q1    │  │  Q2    │  │  Q3    │  │  Q4    │  │  Q5  ││
    │   └───┬────┘  └───┬────┘  └───┬────┘  └───┬────┘  └──┬───┘│
    │       │           │           │           │           │     │
    │       ▼           ▼           ▼           ▼           ▼     │
    │   ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐  ┌──────┐│
    │   │ COIL 1 │  │ COIL 2 │  │ COIL 3 │  │ COIL 4 │  │COIL 5││
    │   │ 47μH   │  │ 47μH   │  │ 47μH   │  │ 47μH   │  │ 47μH ││
    │   └───┬────┘  └───┬────┘  └───┬────┘  └───┬────┘  └──┬───┘│
    │       └───────────┴───────────┴───────────┴───────────┘     │
    │                        │                                     │
    │                       GND                                    │
    │                                                             │
    │   MCU PWM SIGNALS:                                          │
    │   PA0 ──▶ Q1 Gate (Coil 1)                                 │
    │   PA1 ──▶ Q2 Gate (Coil 2)                                 │
    │   PA2 ──▶ Q3 Gate (Coil 3)                                 │
    │   PA3 ──▶ Q4 Gate (Coil 4)                                 │
    │   PA4 ──▶ Q5 Gate (Coil 5)                                 │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

---

## STM32F407 MCU Pinout

```
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   STM32F407 MCU CONNECTIONS                                  │
    │                                                             │
    │   PA0 ──▶ PWM1 (Coil 1)                                    │
    │   PA1 ──▶ PWM2 (Coil 2)                                    │
    │   PA2 ──▶ PWM3 (Coil 3)                                    │
    │   PA3 ──▶ PWM4 (Coil 4)                                    │
    │   PA4 ──▶ PWM5 (Coil 5)                                    │
    │                                                             │
    │   PA5 ◀── Temperature sensor (NTC)                         │
    │   PA6 ◀── Pressure sensor (capacitive)                     │
    │   PA7 ◀── Plasma density sensor (RF)                       │
    │                                                             │
    │   PB0 ──▶ Gas valve control                                 │
    │   PB1 ──▶ Fault relay                                       │
    │   PB2 ──▶ Status LED                                        │
    │                                                             │
    │   PB6 ──▶ I2C SDA (INA219 current sensor)                  │
    │   PB7 ──▶ I2C SCL (INA219 current sensor)                  │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

---

## Protection Circuits

```
    PROTECTION FEATURES
    
    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   OVERCURRENT:  250A trip, <1ms response                   │
    │   OVERVOLTAGE:  62V clamping (TVS diode)                   │
    │   UNDERVOLTAGE: 36V cutoff (shutdown)                      │
    │   TEMPERATURE:  80°C cutoff (reduce power)                 │
    │   PRESSURE:     High/Low alarm (gas valve control)         │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
```

---

## Connector Pinout

```
    XT90 POWER CONNECTOR:
    ┌─────────────────────────────────┐
    │  ┌──────┐      ┌──────┐        │
    │  │  +   │      │  -   │        │
    │  │(Red) │      │(Black)│       │
    │  └──────┘      └──────┘        │
    │   48V DC        GND            │
    └─────────────────────────────────┘

    JST-SH DIAGNOSTIC CONNECTOR (4-pin):
    Pin 1: 3.3V (sensor power)
    Pin 2: SDA (I2C data)
    Pin 3: SCL (I2C clock)
    Pin 4: GND
```

---

## Wire Colors

| Color | Purpose |
|-------|---------|
| **Red** | 48V power |
| **Black** | GND |
| **Yellow** | PWM signal (Coil 1) |
| **Orange** | PWM signal (Coil 2) |
| **Green** | PWM signal (Coil 3) |
| **Blue** | PWM signal (Coil 4) |
| **Purple** | PWM signal (Coil 5) |

---

**Document**: 02_WIRING.md
**Vehicle**: PHI_FIELD_PLASMA_BATTERY
**Status**: BUILDABLE ✓
**Version**: 2.0 (Standardized)
