# PHI CHEAP LIGHT PLANE — WIRING

## Electrical Wiring Diagrams and Harness Specifications

---

## POWER DISTRIBUTION ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PHI CHEAP LIGHT PLANE — POWER BUS                     │
│                                                                          │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐            │
│  │  FPB-20 #1  │   │  FPB-20 #2  │   │  FPB-20 #3  │   │  FPB-20 #4  │            │
│  │  12V     │   │  12V     │   │  12V     │   │  12V     │            │
│  │  100Ah   │   │  100Ah   │   │  100Ah   │   │  100Ah   │            │
│  └────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬─────┘            │
│       │               │               │               │                  │
│       │   ┌───────────┴───────────────┴───────────┐   │                  │
│       │   │         2S2P BATTERY CONFIGURATION     │   │                  │
│       │   │                                       │   │                  │
│       │   │   Series Pair 1:  FPB-20#1 + FPB-20#2 = 24V │   │                  │
│       │   │   Series Pair 2:  FPB-20#3 + FPB-20#4 = 24V │   │                  │
│       │   │   Parallel:  Pair1 || Pair2 = 24V 200Ah│   │                  │
│       │   │                                       │   │                  │
│       │   │   Total: 24V × 200Ah = 4,800 Wh      │   │                  │
│       │   └───────────────────┬───────────────────┘   │                  │
│       │                       │                       │                  │
│       │   ┌───────────────────┴───────────────────┐   │                  │
│       │   │      MAIN POWER BUS (24V DC)           │   │                  │
│       │   │                                       │   │                  │
│       │   │  ┌─────────┐  ┌─────────┐  ┌────────┐ │   │                  │
│       │   │  │ 200A    │  │ BATTERY │  │ VOLTAGE│ │   │                  │
│       │   │  │ ANL     │  │ MONITOR │  │ MONITOR│ │   │                  │
│       │   │  │ FUSE    │  │ (A709)  │  │ (0-50V)│ │   │                  │
│       │   │  └────┬────┘  └────┬────┘  └───┬────┘ │   │                  │
│       │   │       │            │            │      │   │                  │
│       │   └───────┼────────────┼────────────┼──────┘   │                  │
│       │           │            │            │          │                  │
│       │           │            │            │          │                  │
│  ┌────▼───────────▼────────────▼────────────▼──────────▼────────────┐   │
│  │                     MAIN SWITCH PANEL                            │   │
│  │                                                                  │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐       │   │
│  │  │ MASTER   │  │ MOTOR    │  │ AVIONICS │  │ FUEL     │       │   │
│  │  │ SWITCH   │  │ SWITCH   │  │ SWITCH   │  │ PUMP     │       │   │
│  │  │ (300A)   │  │ (100A)   │  │ (20A)    │  │ (N/A)    │       │   │
│  │  │ RED      │  │ YELLOW   │  │ GREEN    │  │ BLUE     │       │   │
│  │  └────┬─────┘  └────┬─────┘  └────┬─────┘  └──────────┘       │   │
│  │       │              │              │                            │   │
│  └───────┼──────────────┼──────────────┼────────────────────────────┘   │
│          │              │              │                                │
│          │              │              │                                │
│  ┌───────▼──────┐ ┌─────▼────────┐ ┌──▼──────────────────────────┐    │
│  │ MOTOR BUS    │ │ AVIONICS BUS │ │ ACCESSORIES BUS              │    │
│  │ 24V 200A     │ │ 24V 20A      │ │ 12V 10A                      │    │
│  │              │ │              │ │                               │    │
│  │ ┌──────────┐│ │ ┌──────────┐│ │ ┌──────────┐ ┌──────────┐    │    │
│  │ │ PHI-HARM ││ │ │ ARDUINO  ││ │ │ COCKPIT  │ │ NAV      │    │    │
│  │ │ MOTOR    ││ │ │ NANO ×2  ││ │ │ LIGHTS   │ │ LIGHTS   │    │    │
│  │ │ CONTROLLER││ │ │          ││ │ │ (LED)    │ │ (LED)    │    │    │
│  │ │ 100A ESC ││ │ │ SENSORS  ││ │ │          │ │          │    │    │
│  │ └──────────┘│ │ │ BMP280   ││ │ └──────────┘ └──────────┘    │    │
│  │             │ │ │ MPU6050  ││ │                               │    │
│  │ ┌──────────┐│ │ │ GPS      ││ │                               │    │
│  │ │ FIELD    ││ │ │          ││ │                               │    │
│  │ │ COILS    ││ │ │ TELEMETRY││ │                               │    │
│  │ │ (4×)     ││ │ │ HC-12    ││ │                               │    │
│  │ └──────────┘│ │ └──────────┘│ │                               │    │
│  └─────────────┘ └─────────────┘ └───────────────────────────────┘    │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## WIRE GAUGE SPECIFICATIONS

| Circuit | Gauge | Color | Length | Current | Notes |
|---------|-------|-------|--------|---------|-------|
| Battery Main (series) | 4 AWG | Red | 2ft | 200A max | Battery interconnect |
| Battery Parallel | 4 AWG | Red | 3ft | 100A | Series-to-parallel link |
| Main Bus to Switch | 4 AWG | Red | 4ft | 200A | Master switch feed |
| Switch to Motor | 4 AWG | Red | 6ft | 100A | Motor power |
| Switch to Avionics | 12 AWG | Yellow | 4ft | 10A | Avionics feed |
| Arduino to Sensors | 22 AWG | Blue | 2ft | 0.5A | I2C/SPI data |
| Telemetry Radio | 22 AWG | Green | 3ft | 0.5A | Data link |
| LED Lighting | 18 AWG | White | 5ft | 2A | Cockpit/nav lights |
| Battery Monitor | 14 AWG | Orange | 2ft | 15A | Current sensing |
| Ground Bus | 4 AWG | Black | 8ft | 200A | Common ground return |

---

## BATTERY WIRING DETAIL

```
2S2P CONFIGURATION (24V, 200Ah = 4,800Wh)

    ┌─────────────┐         ┌─────────────┐
    │  FPB-20 BATT #1│         │  FPB-20 BATT #2│
    │  12V 100Ah  │         │  12V 100Ah  │
    │  (+)    (-) │         │  (+)    (-) │
    └──┬──────┬───┘         └───┬──────┬──┘
       │      │                 │      │
       │      └─────────────────┘      │
       │        SERIES CONNECTION      │
       │        (24V total)            │
       │                               │
       │      ┌─────────────────┐      │
       │      │  JUMPER CABLE   │      │
       │      │  (4 AWG, 6")   │      │
       │      └─────────────────┘      │
       │                               │
    ┌──┴──────┬───┐         ┌───┬──────┴──┐
    │  FPB-20 BATT #3│         │  FPB-20 BATT #4│
    │  12V 100Ah  │         │  12V 100Ah  │
    │  (+)    (-) │         │  (+)    (-) │
    └──┬──────┬───┘         └───┬──────┬──┘
       │      │                 │      │
       │      └─────────────────┘      │
       │        SERIES CONNECTION      │
       │        (24V total)            │
       │                               │
       │      ┌─────────────────┐      │
       │      │  JUMPER CABLE   │      │
       │      │  (4 AWG, 6")   │      │
       │      └─────────────────┘      │
       │                               │
    ┌──▼───────────────────────────────▼──┐
    │         PARALLEL CONNECTION          │
    │         (24V, 200Ah total)           │
    │                                      │
    │  (+) BUS ───────────────── (+) BUS   │
    │  (-) BUS ───────────────── (-) BUS   │
    │                                      │
    │  4 AWG cables to main switch panel   │
    └──────────────────────────────────────┘
```

---

## SWITCH PANEL WIRING

```
┌─────────────────────────────────────────────────────────────────┐
│                    SWITCH PANEL (cockpit left side)              │
│                                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐       │
│  │ MASTER   │  │ MOTOR    │  │ AVIONICS │  │ RADIO    │       │
│  │ SWITCH   │  │ SWITCH   │  │ SWITCH   │  │ SWITCH   │       │
│  │          │  │          │  │          │  │          │       │
│  │  ┌────┐  │  │  ┌────┐  │  │  ┌────┐  │  │  ┌────┐  │       │
│  │  │ON  │  │  │  │ON  │  │  │  │ON  │  │  │  │ON  │  │       │
│  │  │OFF │  │  │  │OFF │  │  │  │OFF │  │  │  │OFF │  │       │
│  │  └────┘  │  │  └────┘  │  │  └────┘  │  │  └────┘  │       │
│  │  RED     │  │  YELLOW  │  │  GREEN   │  │  BLUE    │       │
│  │  300A    │  │  100A    │  │  20A     │  │  5A      │       │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘       │
│       │              │              │              │              │
│       │   ┌──────────┴──────────────┴──────────────┘              │
│       │   │                                                       │
│       │   │   ┌───────────────────────────────────┐               │
│       │   │   │        SWITCH WIRING               │               │
│       │   │   │                                    │               │
│       │   │   │  MASTER: 24V IN → 24V OUT (300A)  │               │
│       │   │   │  MOTOR:  24V IN → 24V OUT (100A)  │               │
│       │   │   │  AVIO:   24V IN → 24V OUT (20A)   │               │
│       │   │   │  RADIO:  12V IN → 12V OUT (5A)    │               │
│       │   │   │                                    │               │
│       │   │   └───────────────────────────────────┘               │
│       │   │                                                       │
│       │   │   ┌───────────────────────────────────┐               │
│       │   │   │        EMERGENCY KILL SWITCH       │               │
│       │   │   │                                    │               │
│       │   │   │  RED MOMENTARY PUSHBUTTON          │               │
│       │   │   │  Connected to:                     │               │
│       │   │   │  - Main contactor coil (24V)       │               │
│       │   │   │  - Cuts ALL power instantly        │               │
│       │   │   │  - Spring-return to OFF            │               │
│       │   │   │                                    │               │
│       │   │   └───────────────────────────────────┘               │
│       │   │                                                       │
└───────┼───┼───────────────────────────────────────────────────────┘
        │   │
        │   └─── TO MAIN POWER BUS
        │
        └─────── TO BATTERY BANK (24V)
```

---

## MOTOR WIRING DETAIL

```
┌─────────────────────────────────────────────────────────────────┐
│                    MOTOR WIRING (50kW Brushless Outrunner)       │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                   MOTOR CONTROLLER (ESC)                  │   │
│  │                   100A, 80V, 3-phase                      │   │
│  │                                                          │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐              │   │
│  │  │  INPUT+  │  │  INPUT-  │  │  SIGNAL  │              │   │
│  │  │ (24V+)   │  │ (24V-)   │  │ (PWM)    │              │   │
│  │  └────┬─────┘  └────┬─────┘  └────┬─────┘              │   │
│  │       │              │              │                     │   │
│  └───────┼──────────────┼──────────────┼─────────────────────┘   │
│          │              │              │                          │
│          │              │              │                          │
│  ┌───────▼──────┐ ┌─────▼──────┐ ┌────▼──────────────────┐     │
│  │  4 AWG RED   │ │  4 AWG BLK │ │  22 AWG SIGNAL         │     │
│  │  (24V+)      │ │  (24V-)    │ │  (PWM from Arduino)    │     │
│  │  from motor  │ │  from motor│ │  3-wire: +5V, GND, SIG │     │
│  │  switch      │ │  switch    │ │                         │     │
│  └──────────────┘ └────────────┘ └─────────────────────────┘     │
│          │              │              │                          │
│          │              │              │                          │
│  ┌───────▼──────────────▼──────────────▼──────────────────┐     │
│  │                   BRUSHLESS MOTOR                        │     │
│  │                   50kW, 80V, 12-pole                    │     │
│  │                                                          │     │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐              │     │
│  │  │  PHASE A │  │  PHASE B │  │  PHASE C │              │     │
│  │  │ (RED)    │  │ (YELLOW) │  │ (BLUE)   │              │     │
│  │  │ 10 AWG   │  │ 10 AWG   │  │ 10 AWG   │              │     │
│  │  └──────────┘  └──────────┘  └──────────┘              │     │
│  │                                                          │     │
│  │  ┌──────────┐  ┌──────────┐                             │     │
│  │  │  HALL A  │  │  HALL B  │  ┌──────────┐              │     │
│  │  │ (GREEN)  │  │ (YELLOW) │  │  HALL C  │              │     │
│  │  │ 22 AWG   │  │ 22 AWG   │  │ (BLUE)   │              │     │
│  │  └──────────┘  └──────────┘  │ 22 AWG   │              │     │
│  │                               └──────────┘              │     │
│  │                                                          │     │
│  │  ┌──────────┐                                           │     │
│  │  │  TEMP    │  K-Type thermocouple                      │     │
│  │  │  SENSOR  │  to Arduino analog input                  │     │
│  │  └──────────┘                                           │     │
│  └──────────────────────────────────────────────────────────┘     │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

---

## PHI-HARMONIC FIELD COIL WIRING

```
┌─────────────────────────────────────────────────────────────────┐
│              PHI-HARMONIC FIELD COIL SYSTEM (4× coils)          │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                   PHI CONTROLLER PCB                       │   │
│  │                   (built on proto board)                   │   │
│  │                                                          │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐              │   │
│  │  │ MOSFET   │  │ MOSFET   │  │ MOSFET   │              │   │
│  │  │ IRFP4110 │  │ IRFP4110 │  │ IRFP4110 │              │   │
│  │  │ #1       │  │ #2       │  │ #3       │              │   │
│  │  └────┬─────┘  └────┬─────┘  └────┬─────┘              │   │
│  │       │              │              │                     │   │
│  │  ┌────▼─────┐  ┌────▼─────┐  ┌────▼─────┐              │   │
│  │  │ IR2113   │  │ IR2113   │  │ IR2113   │              │   │
│  │  │ GATE DRV │  │ GATE DRV │  │ GATE DRV │              │   │
│  │  │ #1       │  │ #2       │  │ #3       │              │   │
│  │  └────┬─────┘  └────┬─────┘  └────┬─────┘              │   │
│  │       │              │              │                     │   │
│  │  ┌────▼─────┐  ┌────▼─────┐  ┌────▼─────┐              │   │
│  │  │ PWM IN   │  │ PWM IN   │  │ PWM IN   │              │   │
│  │  │ (Arduino)│  │ (Arduino)│  │ (Arduino)│              │   │
│  │  └──────────┘  └──────────┘  └──────────┘              │   │
│  │                                                          │   │
│  └──────────────────────────────────────────────────────────┘   │
│          │              │              │                          │
│          │              │              │                          │
│  ┌───────▼──────┐ ┌─────▼──────┐ ┌────▼──────────────────┐     │
│  │  COIL #1     │ │  COIL #2    │ │  COIL #3               │     │
│  │  Litz Wire   │ │  Litz Wire  │ │  Litz Wire             │     │
│  │  14 AWG      │ │  14 AWG     │ │  14 AWG                │     │
│  │  T130-2 Core │ │  T130-2 Core│ │  T130-2 Core           │     │
│  │  φ-tuned     │ │  φ-tuned    │ │  φ-tuned               │     │
│  │  turns: 161  │ │  turns: 100 │ │  turns: 62             │     │
│  └──────────────┘ └─────────────┘ └────────────────────────┘     │
│          │              │              │                          │
│          └──────────────┼──────────────┘                          │
│                         │                                         │
│                  ┌──────▼──────┐                                  │
│                  │  COMMON GND │                                  │
│                  │  (4 AWG)    │                                  │
│                  └─────────────┘                                  │
│                                                                    │
│  COIL SPECIFICATIONS:                                             │
│  - Wire: Litz wire 14 AWG (low skin-effect losses)              │
│  - Core: Ferrite T130-2 toroid                                   │
│  - Turns ratio: φ (161:100:62)                                   │
│  - Resonant frequency: 161.8 kHz base                            │
│  - Capacitor: 0.47μF 400V across each coil                      │
│  - Peak current: 50A per coil                                    │
│  - Duty cycle: 50% PWM at 20kHz carrier                          │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

---

## SENSOR WIRING

```
┌─────────────────────────────────────────────────────────────────┐
│                    SENSOR WIRING TO ARDUINO NANO                 │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                   ARDUINO NANO #1 (PRIMARY)               │   │
│  │                   Flight Computer                         │   │
│  │                                                          │   │
│  │  PIN ASSIGNMENTS:                                        │   │
│  │                                                          │   │
│  │  D2  ──────── BMP280 #1 SDA (altitude primary)          │   │
│  │  D3  ──────── BMP280 #1 SCL (altitude primary)          │   │
│  │  D4  ──────── MPU6050 SDA (attitude)                     │   │
│  │  D5  ──────── MPU6050 SCL (attitude)                     │   │
│  │  D6  ──────── GPS TX → Arduino RX (position)            │   │
│  │  D7  ──────── GPS RX ← Arduino TX                        │   │
│  │  D8  ──────── Motor ESC signal (PWM)                     │   │
│  │  D9  ──────── Rudder servo PWM                           │   │
│  │  D10 ──────── Aileron L servo PWM                        │   │
│  │  D11 ──────── Aileron R servo PWM                        │   │
│  │  D12 ──────── Elevator servo PWM                         │   │
│  │  D13 ──────── Status LED                                 │   │
│  │                                                          │   │
│  │  A0  ──────── Battery voltage (divider)                  │   │
│  │  A1  ──────── Motor current (ACS758)                     │   │
│  │  A2  ──────── Motor temperature (K-type)                 │   │
│  │  A3  ──────── Battery temperature (NTC)                  │   │
│  │  A4  ──────── OLED SDA                                  │   │
│  │  A5  ──────── OLED SCL                                  │   │
│  │  A6  ──────── Airspeed (optional, pitot)                 │   │
│  │  A7  ──────── Throttle position (pot)                   │   │
│  │                                                          │   │
│  │  VIN ──────── 5V from buck converter                     │   │
│  │  GND ──────── Common ground bus                          │   │
│  │                                                          │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                   ARDUINO NANO #2 (BACKUP)                │   │
│  │                   Monitoring / Telemetry                   │   │
│  │                                                          │   │
│  │  PIN ASSIGNMENTS:                                        │   │
│  │                                                          │   │
│  │  D2  ──────── BMP280 #2 SDA (altitude backup)           │   │
│  │  D3  ──────── BMP280 #2 SCL (altitude backup)           │   │
│  │  D6  ──────── HC-12 Telemetry RX                         │   │
│  │  D7  ──────── HC-12 Telemetry TX                         │   │
│  │  D8  ──────── Piezo buzzer (warnings)                    │   │
│  │  D13 ──────── Status LED                                 │   │
│  │                                                          │   │
│  │  A0  ──────── Battery voltage (backup)                   │   │
│  │  A1  ──────── Battery current (backup)                   │   │
│  │                                                          │   │
│  │  VIN ──────── 5V from buck converter                     │   │
│  │  GND ──────── Common ground bus                          │   │
│  │                                                          │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

---

## GROUND BUS AND SHIELDING

```
┌─────────────────────────────────────────────────────────────────┐
│                    GROUND BUS SYSTEM                             │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                   GROUND BUS BAR                          │   │
│  │                   (4 AWG copper, bolted to frame)         │   │
│  │                                                          │   │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐       │   │
│  │  │ BATTERY │ │  MOTOR  │ │ AVIONICS│ │ SHIELD  │       │   │
│  │  │ GND     │ │  GND    │ │ GND     │ │ GND     │       │   │
│  │  │ (4 AWG) │ │ (4 AWG) │ │(12 AWG) │ │(22 AWG) │       │   │
│  │  └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘       │   │
│  │       │            │            │            │             │   │
│  │       └────────────┼────────────┼────────────┘             │   │
│  │                    │            │                          │   │
│  │              ┌─────▼────────────▼─────┐                   │   │
│  │              │    FRAME GROUND POINT   │                   │   │
│  │              │    (spruce + copper     │                   │   │
│  │              │     strap to frame)     │                   │   │
│  │              └─────────────────────────┘                   │   │
│  │                                                          │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  SHIELDING:                                                     │
│  - GPS antenna cable: shielded coax, grounded at frame          │
│  - VHF radio: shielded coax, grounded at radio                  │
│  - HC-12 telemetry: shielded twisted pair                       │
│  - Motor phases: shielded cable, grounded at ESC               │
│  - All signal wires: twisted pair, routed away from power       │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

---

## WIRE ROUTING

```
┌─────────────────────────────────────────────────────────────────┐
│                    WIRE ROUTING (TOP VIEW)                       │
│                                                                  │
│                    ┌──────────┐                                  │
│                    │PROPELLER │                                  │
│                    └────┬─────┘                                  │
│                         │                                        │
│          ┌──────────────┼──────────────────────┐                │
│          │              │                      │                │
│          │    ┌─────────▼─────────┐            │                │
│          │    │  MOTOR (front)    │            │                │
│          │    │  4AWG power wires │            │                │
│          │    │  10AWG phase wires│            │                │
│          │    │  22AWG hall wires │            │                │
│          │    └─────────┬─────────┘            │                │
│          │              │                      │                │
│          │    ┌─────────▼─────────┐            │                │
│          │    │  PHI COILS        │            │                │
│          │    │  4AWG power wires │            │                │
│          │    │  14AWG coil wires │            │                │
│          │    └─────────┬─────────┘            │                │
│          │              │                      │                │
│          │    ┌─────────▼─────────┐            │                │
│          │    │  ESC CONTROLLER   │            │                │
│          │    │  4AWG in, 10AWG out│           │                │
│          │    └─────────┬─────────┘            │                │
│          │              │                      │                │
│          │    ┌─────────▼─────────┐            │                │
│          │    │  FUSELAGE WIRE    │            │                │
│          │    │  CHANNEL          │            │                │
│          │    │  (inside left     │            │                │
│          │    │   longeron)       │            │                │
│          │    │                   │            │                │
│          │    │  Wires run along  │            │                │
│          │    │  left longeron    │            │                │
│          │    │  secured with     │            │                │
│          │    │  zip ties every   │            │                │
│          │    │  150mm            │            │                │
│          │    └─────────┬─────────┘            │                │
│          │              │                      │                │
│          │    ┌─────────▼─────────┐            │                │
│          │    │  COCKPIT PANEL    │            │                │
│          │    │  Switches         │            │                │
│          │    │  Instruments      │            │                │
│          │    │  Throttle         │            │                │
│          │    └─────────┬─────────┘            │                │
│          │              │                      │                │
│          │    ┌─────────▼─────────┐            │                │
│          │    │  BATTERY BAY      │            │                │
│          │    │  (behind cockpit) │            │                │
│          │    │  4AWG main buses  │            │                │
│          │    └───────────────────┘            │                │
│          │                                     │                │
│          └─────────────────────────────────────┘                │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

---

## WIRE ROUTING RULES

1. **Separation:** Power wires (4AWG) routed minimum 50mm from signal wires (22AWG)
2. **Shielding:** GPS and VHF coax cables grounded at one end only
3. **Securement:** All wires zip-tied every 150mm to longeron or former
4. **Chafe protection:** Grommets at all wood-to-wire contact points
5. **Service loops:** 100mm service loop at each connector
6. **Color coding:**
   - RED: Battery positive (+24V)
   - BLACK: Battery negative / ground
   - YELLOW: Switched power (post-switch)
   - GREEN: Signal/data
   - BLUE: Sensor connections
   - WHITE: Lighting
   - ORANGE: Current sensing
7. **Fuse protection:** Each sub-circuit fused at 1.5× expected current
8. **Emergency kill:** Red momentary switch cuts all power via main contactor
