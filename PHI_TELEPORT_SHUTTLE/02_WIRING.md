# PHI TELEPORT SHUTTLE — WIRING DIAGRAM

## Electrical Wiring System

All wiring follows experimental aircraft and high-energy physics conventions. High-current paths use 2/0 AWG welding cable. Coil drive paths use 4 AWG. Signal paths use 22-26 AWG shielded twisted pair.

---

## POWER DISTRIBUTION ARCHITECTURE

```
┌──────────────────────────────────────────────────────────────────────────┐
│                     POWER DISTRIBUTION SYSTEM                            │
│                                                                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐                │
│  │ FPB-100  │  │ FPB-100  │  │ FPB-100  │  │ FPB-100  │                │
│  │ BATTERY  │  │ BATTERY  │  │ BATTERY  │  │ BATTERY  │                │
│  │ 100kWh   │  │ 100kWh   │  │ 100kWh   │  │ 100kWh   │                │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘                │
│       │              │              │              │                      │
│       └──────┬───────┴──────┬───────┴──────┬───────┘                      │
│              │              │              │                               │
│         ┌────┴────┐    ┌────┴────┐    ┌────┴────┐                         │
│         │  MAIN   │    │  MAIN   │    │  MAIN   │                         │
│         │ SWITCH  │    │ SWITCH  │    │ SWITCH  │                         │
│         │  600A   │    │  600A   │    │  600A   │                         │
│         └────┬────┘    └────┬────┘    └────┬────┘                         │
│              │              │              │                               │
│    ┌─────────┴──────────────┴──────────────┴─────────┐                    │
│    │              COPPER BUS BAR                      │                    │
│    │         (1/2" × 2" × 30", insulated)             │                    │
│    └──┬────┬────┬────┬────┬────┬────┬────┬────┬────┬──┘                  │
│       │    │    │    │    │    │    │    │    │    │                      │
│      ┌┴┐  ┌┴┐  ┌┴┐  ┌┴┐  ┌┴┐  ┌┴┐  ┌┴┐  ┌┴┐  ┌┴┐  ┌┴┐               │
│      │F│  │F│  │F│  │F│  │F│  │F│  │F│  │F│  │F│  │F│  │F│  │F│        │
│      │U│  │U│  │U│  │U│  │U│  │U│  │U│  │U│  │U│  │U│  │U│  │U│        │
│      │S│  │S│  │S│  │S│  │S│  │S│  │S│  │S│  │S│  │S│  │S│  │S│        │
│      │E│  │E│  │E│  │E│  │E│  │E│  │E│  │E│  │E│  │E│  │E│  │E│        │
│      └┬┘  └┬┘  └┬┘  └┬┘  └┬┘  └┬┘  └┬┘  └┬┘  └┬┘  └┬┘  └┬┘  └┬┘      │
│       │    │    │    │    │    │    │    │    │    │    │    │            │
│      ┌┴──┐┌┴──┐┌┴──┐┌┴──┐┌┴──┐┌┴──┐┌┴──┐┌┴──┐┌┴──┐┌┴──┐┌┴──┐┌┴──┐    │
│      │C01││C02││C03││C04││C05││C06││C07││C08││C09││C10││C11││C12│    │
│      │FLD││FLD││FLD││FLD││FLD││FLD││FLD││FLD││FLD││FLD││FLD││FLD│    │
│      │COI││COI││COI││COI││COI││COI││COI││COI││COI││COI││COI││COI│    │
│      │ L ││ L ││ L ││ L ││ L ││ L ││ L ││ L ││ L ││ L ││ L ││ L │    │
│      └───┘└───┘└───┘└───┘└───┘└───┘└───┘└───┘└───┘└───┘└───┘└───┘    │
│                                                                          │
│    ┌──────────────────────────────────────────────┐                      │
│    │            AUXILIARY BUS                      │                      │
│    │                                               │                      │
│    │  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐     │                      │
│    │  │ 48V  │  │ 48V  │  │ 24V  │  │ 12V  │     │                      │
│    │  │ DCDC │  │ DCDC │  │ DCDC │  │ DCDC │     │                      │
│    │  │ 3kW  │  │ 3kW  │  │ 1.5kW│  │ 800W │     │                      │
│    │  └──┬───┘  └──┬───┘  └──┬───┘  └──┬───┘     │                      │
│    │     │         │         │         │           │                      │
│    │  ┌──┴───┐  ┌──┴───┐  ┌──┴───┐  ┌──┴───┐     │                      │
│    │  │NAVIG │  │SAFETY│  │LIFE  │  │COMMS │     │                      │
│    │  │SYSTEM│  │SYSTEM│  │SUPPORT│  │SYSTEM│     │                      │
│    │  │ 48V  │  │ 48V  │  │ 24V  │  │ 12V  │     │                      │
│    │  └──────┘  └──────┘  └──────┘  └──────┘     │                      │
│    └──────────────────────────────────────────────┘                      │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## FOLD COIL WIRING (Per Coil)

```
┌──────────────────────────────────────────────────────────────────────┐
│              PHI-HARMONIC FOLD COIL (Per Unit)                       │
│                                                                      │
│  ┌────────────────────────────────────────────────────────────┐      │
│  │              POWER INPUT                                    │      │
│  │                                                             │      │
│  │  48V DC ──── ANL 400A ──── 4 AWG ────┬───────────┐        │      │
│  │                                       │           │        │      │
│  │                              ┌────────┴────┐      │        │      │
│  │                              │   ENERGY    │      │        │      │
│  │                              │   STORAGE   │      │        │      │
│  │                              │ 8μF 1kV ×4  │      │        │      │
│  │                              │  parallel    │      │        │      │
│  │                              │  C = 32μF    │      │        │      │
│  │                              └────┬───┬─────┘      │        │      │
│  │                                   │   │            │        │      │
│  │                    ┌──────────────┘   └────────────┘        │      │
│  │                    │                                        │      │
│  │          ┌─────────┴─────────┐                              │      │
│  │          │   FULL-BRIDGE     │                              │      │
│  │          │   INVERTER        │                              │      │
│  │          │                   │                              │      │
│  │          │  ┌──────┐ ┌──────┐│ ← MOSFET 1200V 200A        │      │
│  │          │  │ Q1   │ │ Q2   ││   (1 per arm)              │      │
│  │          │  │ N-ch │ │ N-ch ││                              │      │
│  │          │  └──┬───┘ └──┬───┘│                              │      │
│  │          │     │         │    │                              │      │
│  │          │  ┌──┴───┐ ┌──┴───┐│                              │      │
│  │          │  │ Q3   │ │ Q4   ││                              │      │
│  │          │  │ N-ch │ │ N-ch ││                              │      │
│  │          │  └──────┘ └──────┘│                              │      │
│  │          └─────────┬─────────┘                              │      │
│  │                    │                                        │      │
│  │          ┌─────────┴─────────┐                              │      │
│  │          │   GATE DRIVERS    │                              │      │
│  │          │  Isolated, 5kV    │                              │      │
│  │          │                   │                              │      │
│  │          │  IN ──── HIN ──── PLL ──── Master Osc          │      │
│  │          │  IN ──── LIN ──── PLL ──── Master Osc          │      │
│  │          └───────────────────┘                              │      │
│  │                                                             │      │
│  │          ┌───────────────────┐                              │      │
│  │          │  RESONANT TANK    │                              │      │
│  │          │                   │                              │      │
│  │          │  YBCO Superconducting Coil                      │      │
│  │          │  (Alumina former, 1618 turns)                   │      │
│  │          │  L = 2.4 mH                                     │      │
│  │          │  I_max = 5000 A                                  │      │
│  │          │  T_op = 77K (LN2 cooled)                        │      │
│  │          │                   │                              │      │
│  │          │  Resonant freq:                                    │      │
│  │          │  f₀ = 1/(2π√LC)                                  │      │
│  │          │  f₀ ≈ 161.8 kHz ← Fundamental                    │      │
│  │          │  φ-harmonic: 261.8 kHz                            │      │
│  │          └───────────────────┘                              │      │
│  │                                                             │      │
│  │          ┌───────────────────┐                              │      │
│  │          │  FOLD FIELD       │                              │      │
│  │          │  PROBE            │                              │      │
│  │          │  (Mu-metal)       │                              │      │
│  │          │  0-1T range       │                              │      │
│  │          │  Output: 0-5V     │                              │      │
│  │          └───────────────────┘                              │      │
│  └────────────────────────────────────────────────────────────┘      │
│                                                                      │
│  CRYOGENIC SYSTEM (per coil):                                        │
│  ┌────────────────────────────────────────────────────────────┐      │
│  │  LN2 Dewar (50L) ──── Solenoid Valve ──── Insulated Hose  │      │
│  │                                    │                       │      │
│  │                              ┌─────┴─────┐                │      │
│  │                              │  COIL     │                │      │
│  │                              │  JACKET   │                │      │
│  │                              │  (MLI)    │                │      │
│  │                              └───────────┘                │      │
│  │  Return: LN2 boil-off vent to atmosphere                   │      │
│  └────────────────────────────────────────────────────────────┘      │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## NAVIGATION SYSTEM WIRING

```
┌──────────────────────────────────────────────────────────────────────┐
│                 NAVIGATION WIRING DIAGRAM                             │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────┐        │
│  │         NAVIGATION COMPUTER (Raspberry Pi 4, 8GB)        │        │
│  │                                                          │        │
│  │  POWER:                                                  │        │
│  │    USB-C ◄──── 48V→12V DC-DC (3kW)                      │        │
│  │    12V  ────► Sensor Power (IMU, probes, gyro)           │        │
│  │    5V   ────► Logic Power (displays, GPS)                │        │
│  │    GND  ────► Common Ground Bus                          │        │
│  │                                                          │        │
│  │  GPIO / I2C / SPI:                                       │        │
│  │    GPIO 2 (SDA) ──► I2C Bus (IMU, sensors)              │        │
│  │    GPIO 3 (SCL) ──► I2C Bus                             │        │
│  │    GPIO 7  ──► Fold Node Map Control                     │        │
│  │    GPIO 8  ──► Fold Radar Trigger                        │        │
│  │    GPIO 9  ──► Coherence Sensor Read                     │        │
│  │    GPIO 10 ──► Abort Trigger                             │        │
│  │    GPIO 17 ──► Navigation Display (SPI)                  │        │
│  │    GPIO 22 ──► Altimeter Data                            │        │
│  │    GPIO 23 ──► Fiber Gyro Data                           │        │
│  │    GPIO 24 ──► GPS UART TX                               │        │
│  │    GPIO 25 ──► GPS UART RX                               │        │
│  │    GPIO 26 ──► Status LED (Green)                        │        │
│  │    GPIO 27 ──► Warning LED (Red)                         │        │
│  │                                                          │        │
│  └──────────────────────────────────────────────────────────┘        │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────┐        │
│  │              SENSOR WIRING                                │        │
│  │                                                          │        │
│  │  GPS (u-blox F9P, RTK):                                  │        │
│  │    VCC ──► 5V                                             │        │
│  │    GND ──► GND                                           │        │
│  │    TX  ──► Pi GPIO 25 (UART RX)                          │        │
│  │    RX  ──► Pi GPIO 24 (UART TX)                          │        │
│  │    FIX ──► Pi GPIO 9 (fix status)                        │        │
│  │                                                          │        │
│  │  FOLD RADAR:                                             │        │
│  │    VCC ──► 48V (direct from aux bus)                     │        │
│  │    GND ──► GND                                           │        │
│  │    TRIG ──► Pi GPIO 8                                    │        │
│  │    DATA ──► Pi SPI MOSI                                  │        │
│  │    ANT  ──► Directional antenna (N-type)                 │        │
│  │                                                          │        │
│  │  COHERENCE SENSORS (×4):                                 │        │
│  │    VCC ──► 12V                                            │        │
│  │    GND ──► GND                                           │        │
│  │    OUT ──► Pi ADC (0-5V)                                 │        │
│  │    LOC: Forward, Aft, Port, Starboard hull               │        │
│  │                                                          │        │
│  │  IMU (9-DOF):                                            │        │
│  │    VCC ──► 3.3V                                          │        │
│  │    GND ──► GND                                           │        │
│  │    SDA ──► Pi GPIO 2 (I2C)                               │        │
│  │    SCL ──► Pi GPIO 3 (I2C)                               │        │
│  │    INT ──► Pi GPIO 4                                     │        │
│  │                                                          │        │
│  │  FIBER-OPTIC GYRO:                                       │        │
│  │    VCC ──► 48V                                            │        │
│  │    GND ──► GND                                           │        │
│  │    DATA ──► Pi UART RX                                   │        │
│  │                                                          │        │
│  │  BAROMETRIC ALTIMETER (×2):                              │        │
│  │    VCC ──► 3.3V                                          │        │
│  │    GND ──► GND                                           │        │
│  │    SDA ──► Pi GPIO 2 (I2C)                               │        │
│  │    SCL ──► Pi GPIO 3 (I2C)                               │        │
│  │                                                          │        │
│  └──────────────────────────────────────────────────────────┘        │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## SAFETY SYSTEM WIRING

```
┌──────────────────────────────────────────────────────────────────────┐
│                    SAFETY WIRING DIAGRAM                              │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────┐        │
│  │              SAFETY CONTROLLER (Arduino Mega)            │        │
│  │                                                          │        │
│  │  POWER:                                                  │        │
│  │    VIN ◄──── 48V→12V DC-DC (1.5kW)                      │        │
│  │    5V  ────► Sensor Power                                │        │
│  │                                                          │        │
│  │  FOLD CONTAINMENT PROBES (×4):                           │        │
│  │    A0 ──► Fold Probe 1 (Forward) — 0-5V = 0-1T         │        │
│  │    A1 ──► Fold Probe 2 (Aft)                            │        │
│  │    A2 ──► Fold Probe 3 (Port)                           │        │
│  │    A3 ──► Fold Probe 4 (Starboard)                      │        │
│  │                                                          │        │
│  │  QUENCH SWITCHES (×12):                                  │        │
│  │    D10 ──► Quench SW 1 (Coil C01) ──► Heat Sink Bank   │        │
│  │    D11 ──► Quench SW 2 (Coil C02) ──► Heat Sink Bank   │        │
│  │    D12 ──► Quench SW 3 (Coil C03) ──► Heat Sink Bank   │        │
│  │    D13 ──► Quench SW 4 (Coil C04) ──► Heat Sink Bank   │        │
│  │    D14 ──► Quench SW 5 (Coil C05) ──► Heat Sink Bank   │        │
│  │    D15 ──► Quench SW 6 (Coil C06) ──► Heat Sink Bank   │        │
│  │    D16 ──► Quench SW 7 (Coil C07) ──► Heat Sink Bank   │        │
│  │    D17 ──► Quench SW 8 (Coil C08) ──► Heat Sink Bank   │        │
│  │    D18 ──► Quench SW 9 (Coil C09) ──► Heat Sink Bank   │        │
│  │    D19 ──► Quench SW 10 (Coil C10) ──► Heat Sink Bank  │        │
│  │    D20 ──► Quench SW 11 (Coil C11) ──► Heat Sink Bank  │        │
│  │    D21 ──► Quench SW 12 (Coil C12) ──► Heat Sink Bank  │        │
│  │                                                          │        │
│  │  FIRE DETECTION:                                         │        │
│  │    D22 ──► Smoke Detector 1 (Cabin)                      │        │
│  │    D23 ──► Smoke Detector 2 (Battery Bay)                │        │
│  │    D24 ──► Heat Detector 1 (Electronics Bay)             │        │
│  │    D25 ──► Heat Detector 2 (Battery Bay)                 │        │
│  │    D26 ──► Flame Detector (Cabin)                        │        │
│  │    D27 ──► Gas Detector (Battery Bay)                    │        │
│  │                                                          │        │
│  │  FIRE SUPPRESSION:                                       │        │
│  │    D30 ──► CO₂ Extinguisher Solenoid (Cabin)             │        │
│  │    D31 ──► FM-200 Solenoid (Electronics Bay)             │        │
│  │    D32 ──► N₂ Flood Solenoid (Coil Bay)                  │        │
│  │                                                          │        │
│  │  ABORT SYSTEM:                                           │        │
│  │    D36 ──► Coil Power Cut (all 12 coils)                 │        │
│  │    D37 ──► Fold Power Bus Disconnect                     │        │
│  │    D38 ──► Battery Isolation Relay                       │        │
│  │                                                          │        │
│  │  WARNING:                                                │        │
│  │    D40 ──► Audio Alarm (piezo, 105dB)                    │        │
│  │    D41 ──► Strobe Light (LED, high-intensity)            │        │
│  │    D42 ──► Warning Display (red LED panel)               │        │
│  │                                                          │        │
│  │  EMERGENCY EXITS:                                        │        │
│  │    D44 ──► Exit Release Solenoid (Left)                  │        │
│  │    D45 ──► Exit Release Solenoid (Right)                 │        │
│  │                                                          │        │
│  │  MANUAL OVERRIDE:                                        │        │
│  │    D48 ──► Pilot Abort Button (red, momentary)           │        │
│  │    D49 ──► Copilot Abort Button (red, momentary)         │        │
│  │                                                          │        │
│  └──────────────────────────────────────────────────────────┘        │
│                                                                      │
│  EMERGENCY BEACON:                                                   │
│  ┌──────────────────────────────────────────────────────────┐        │
│  │  ELT (121.5 MHz + 406 MHz)                               │        │
│  │    VCC ◄──── 12V (isolated, battery-backed)              │        │
│  │    GND ────► Chassis GND                                 │        │
│  │    ANT  ────► External antenna                           │        │
│  │    ACT  ◄──── Manual switch + G-switch (auto)            │        │
│  └──────────────────────────────────────────────────────────┘        │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## FOLD COIL CONTROL BUS

```
┌──────────────────────────────────────────────────────────────────────┐
│              FOLD COIL CONTROL BUS                                    │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────┐        │
│  │  MASTER OSCILLATOR (Function Generator ×2)               │        │
│  │                                                          │        │
│  │  CH1: 100 kHz (fundamental) ──► PLL Bank 1-6            │        │
│  │  CH2: 161.8 kHz (φ-harmonic) ──► PLL Bank 7-12          │        │
│  │                                                          │        │
│  │  Output: 5Vpp sine wave                                  │        │
│  │  Sync: 1PPS from GPS PPS output                          │        │
│  └──────────────────────────────────────────────────────────┘        │
│                              │                                       │
│                    ┌─────────┴─────────┐                             │
│                    │  PHASE-LOCK LOOP  │                             │
│                    │  BANK (12× PLL)   │                             │
│                    │                   │                             │
│                    │  Each PLL:        │                             │
│                    │  - Locks to ref   │                             │
│                    │  - PID control    │                             │
│                    │    Kp = 1.0       │                             │
│                    │    Ki = 0.618     │                             │
│                    │    Kd = 0.382     │                             │
│                    │  - Phase output   │                             │
│                    └──┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┐                     │
│                       │ │ │ │ │ │ │ │ │ │ │ │                      │
│                      ┌┴┐┌┴┐┌┴┐┌┴┐┌┴┐┌┴┐┌┴┐┌┴┐┌┴┐┌┴┐┌┴┐┌┴┐       │
│                      │1││2││3││4││5││6││7││8││9││0││1││2│       │
│                      │P││P││P││P││P││P││P││P││P││P││P││P│       │
│                      │L││L││L││L││L││L││L││L││L││L││L││L│       │
│                      │L││L││L││L││L││L││L││L││L││L││L││L│       │
│                      └┬┘└┬┘└┬┘└┬┘└┬┘└┬┘└┬┘└┬┘└┬┘└┬┘└┬┘└┬┘       │
│                       │  │  │  │  │  │  │  │  │  │  │  │         │
│                      ┌┴┐┌┴┐┌┴┐┌┴┐┌┴┐┌┴┐┌┴┐┌┴┐┌┴┐┌┴┐┌┴┐┌┴┐       │
│                      │C││C││C││C││C││C││C││C││C││C││C││C│       │
│                      │0││0││0││0││0││0││0││0││0││1││1││1│       │
│                      │1││2││3││4││5││6││7││8││9││0││1││2│       │
│                      └─┘└─┘└─┘└─┘└─┘└─┘└─┘└─┘└─┘└─┘└─┘└─┘        │
│                       Coil positions (dodecahedral array)            │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## GROUND BUS AND SHIELDING

```
┌──────────────────────────────────────────────────────────────────────┐
│                    GROUND SYSTEM                                      │
│                                                                      │
│  PRIMARY GROUND: Copper Bus Bar (central star point)                 │
│                                                                      │
│  Star Ground Topology:                                               │
│                                                                      │
│         ┌──────────────────┐                                         │
│         │  POWER GND       │ ← Single-point star ground              │
│         │  (copper bus bar │   on insulated standoffs                 │
│         │   center)        │                                         │
│         └────────┬─────────┘                                         │
│                  │                                                   │
│     ┌────────────┼────────────┬────────────┬────────────┐            │
│     │            │            │            │            │             │
│   ┌─┴──┐     ┌──┴──┐     ┌──┴──┐     ┌──┴──┐     ┌──┴──┐          │
│   │PWR │     │COIL │     │NAV  │     │SAF  │     │CHSS │          │
│   │GND │     │GND  │     │GND  │     │GND  │     │GND  │          │
│   └────┘     └─────┘     └─────┘     └─────┘     └─────┘          │
│                                                                      │
│   Power GND: Battery negatives, bus bar returns                      │
│   Coil GND: Fold coil return paths (dedicated)                       │
│   Nav GND: Navigation computer, sensors                              │
│   Saf GND: Safety controller, detectors                              │
│   Chassis GND: Hull, frame, all metalwork                            │
│                                                                      │
│   ALL grounds meet at star point on copper bus bar.                   │
│   NO ground loops. NO daisy-chaining.                                 │
│                                                                      │
│   SHIELDING:                                                          │
│   - Hull: Aluminum Faraday cage (>60 dB, 100kHz-1GHz)               │
│   - RF cable: braided copper shield → chassis GND                    │
│   - Signal cable: foil shield → signal GND                            │
│   - Coil cable: triple-shielded (braid + foil + braid)              │
│   - Navigation bay: mu-metal inner enclosure                         │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## WIRE GAUGE TABLE

| Circuit | Wire Gauge | Color | Current | Notes |
|---------|-----------|-------|---------|-------|
| Battery Main Bus | 2/0 AWG | Red/Black | 500A | Welding cable |
| Coil Feed (per coil) | 4 AWG | Red | 300A | Superconductor leads |
| Coil Return | 4 AWG | Black | 300A | Dedicated return |
| Quench Bus | 4 AWG | Orange | 500A | Emergency dump |
| Aux Bus (48V) | 2 AWG | Red/Black | 80A | To DC-DC converters |
| Navigation Power | 10 AWG | Red | 15A | To nav computer |
| Safety Power | 10 AWG | Red | 15A | To safety controller |
| Life Support | 12 AWG | Red | 8A | To O₂, fans, sensors |
| Communication | 14 AWG | Red | 5A | To radios |
| Signal (Analog) | 22 AWG | Yellow | <1A | Shielded twisted pair |
| Signal (Digital) | 22 AWG | Various | <1A | Ribbon cable |
| I2C Bus | 24 AWG | SDA/SCL | <100mA | Twisted pair |
| Serial | 24 AWG | TX/RX | <100mA | Twisted pair |
| Ground Bus | 10 AWG | Green/Yellow | 15A | Star ground |
| HV Coil Lead | 8mm Silicone | Red | 5000A | Superconductor feed |
| LN2 Control | 16 AWG | Blue | 2A | Solenoid valve |

---

## CONNECTOR TYPES

| Connector | Location | Pins | Rating |
|-----------|----------|------|--------|
| Anderson SB350 | Battery to Bus | 2 | 350A continuous |
| Anderson SB175 | Coil Feed | 2 | 175A continuous |
| XT90 | Aux Bus | 2 | 90A continuous |
| N-Type | RF (radar, comms) | 1 | 500MHz, 500W |
| BNC | Signal test points | 1 | 50MHz, signal |
| D-Sub 25 | Safety bus | 25 | Signal + low power |
| MIL-DTL-38999 | Navigation | Various | Environmental sealed |
| Aviation XLR | Intercom | 3 | Audio |

---

## WIRING COLOR CODE

| Color | Function |
|-------|----------|
| Red | +48V / +12V DC Power |
| Black | DC Ground/Return |
| Green/Yellow | Chassis Ground |
| Blue | +5V Regulated |
| Purple | +3.3V Regulated |
| Orange | Quench/Emergency |
| Yellow | Analog Signal |
| White | Digital Signal |
| Pink | I2C SDA |
| Gray | I2C SCL |
| Brown | Serial TX |
| Violet | Serial RX |
| Green | Status LED |
| Red/White | Warning LED |
| Blue/White | Fold Drive Signal |
| Clear | Cryogenic (LN2) |
