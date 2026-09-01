# PHI CHEAP SHUTTLE — WIRING DIAGRAM

## Electrical Wiring System

All wiring follows automotive and experimental aircraft conventions. High-current paths use 4 AWG welding cable. Signal paths use 22-26 AWG silicone wire.

---

## POWER DISTRIBUTION ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────────────┐
│                     POWER DISTRIBUTION SYSTEM                       │
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐           │
│  │  FPB-20     │  │  FPB-20     │  │  FPB-20     │  │  FPB-20     │           │
│  │ BATTERY  │  │ BATTERY  │  │ BATTERY  │  │ BATTERY  │           │
│  │ 12V/100Ah│  │ 12V/100Ah│  │ 12V/100Ah│  │ 12V/100Ah│           │
│  │  10kWh   │  │  10kWh   │  │  10kWh   │  │  10kWh   │           │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘           │
│       │              │              │              │                  │
│       └──────┬───────┴──────────────┴──────┬───────┘                  │
│              │                              │                          │
│         ┌────┴────┐                    ┌────┴────┐                    │
│         │  MAIN   │                    │  MAIN   │                    │
│         │ SWITCH  │                    │ SWITCH  │                    │
│         │  400A   │                    │  400A   │                    │
│         │ (left)  │                    │ (right) │                    │
│         └────┬────┘                    └────┬────┘                    │
│              │                              │                          │
│    ┌─────────┴──────────────────────────────┴─────────┐               │
│    │                  4 AWG BUS BAR                   │               │
│    │              (Copper, 1/4" × 1")                  │               │
│    └──────┬──────────┬──────────┬──────────┬──────────┘               │
│           │          │          │          │                          │
│      ┌────┴───┐ ┌────┴───┐ ┌────┴───┐ ┌────┴───┐                    │
│      │  ANL   │ │  ANL   │ │  ANL   │ │  ANL   │                    │
│      │ FUSE   │ │ FUSE   │ │ FUSE   │ │ FUSE   │                    │
│      │ 150A   │ │ 150A   │ │ 150A   │ │ 150A   │                    │
│      └────┬───┘ └────┬───┘ └────┬───┘ └────┬───┘                    │
│           │          │          │          │                          │
│      ┌────┴───┐ ┌────┴───┐ ┌────┴───┐ ┌────┴───┐                    │
│      │THRUST │ │THRUST │ │THRUST │ │THRUST │                        │
│      │  #1   │ │  #2   │ │  #3   │ │  #4   │                        │
│      │ DRIVE │ │ DRIVE │ │ DRIVE │ │ DRIVE │                        │
│      └───────┘ └───────┘ └───────┘ └───────┘                        │
│                                                                      │
│    ┌──────────────────────────────────────────┐                      │
│    │            AVIONICS BUS                   │                      │
│    │                                           │                      │
│    │  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐ │                      │
│    │  │12V→5V│  │12V→5V│  │12V→5V│  │12V→  │ │                      │
│    │  │BUCK  │  │BUCK  │  │BUCK  │  │3.3V  │ │                      │
│    │  │ 3A   │  │ 3A   │  │ 3A   │  │LDO   │ │                      │
│    │  └──┬───┘  └──┬───┘  └──┬───┘  └──┬───┘ │                      │
│    │     │         │         │         │      │                      │
│    │  ┌──┴───┐  ┌──┴───┐  ┌──┴───┐  ┌──┴───┐│                      │
│    │  │FLIGHT│  │SENSOR│  │COMMS │  │RELAY ││                      │
│    │  │COMPUT│  │POWER │  │POWER │  │DRIVE ││                      │
│    │  │ 5V   │  │ 3.3V │  │ 5V   │  │ 12V  ││                      │
│    │  └──────┘  └──────┘  └──────┘  └──────┘│                      │
│    └──────────────────────────────────────────┘                      │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## THRUSTER WIRING (Per Thruster)

```
┌─────────────────────────────────────────────────────────────┐
│                PHI-HARMONIC PLASMA THRUSTER                  │
│                    (Per Unit)                                │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              POWER INPUT                            │    │
│  │                                                     │    │
│  │  12V DC ──── ANL 150A ──── 4 AWG ────┬───────┐    │    │
│  │                                       │       │    │    │
│  │                              ┌────────┴────┐  │    │    │
│  │                              │   ENERGY    │  │    │    │
│  │                              │   STORAGE   │  │    │    │
│  │                              │  1.0μF 1kV  │  │    │    │
│  │                              │  ×2 parallel│  │    │    │
│  │                              └────┬───┬────┘  │    │    │
│  │                                   │   │       │    │    │
│  │                    ┌──────────────┘   └───────┘    │    │
│  │                    │                               │    │
│  │          ┌─────────┴─────────┐                     │    │
│  │          │    FULL-BRIDGE    │                     │    │
│  │          │    INVERTER       │                     │    │
│  │          │                   │                     │    │
│  │          │  ┌──────┐ ┌──────┐│                     │    │
│  │          │  │Q1    │ │Q2    ││ ← IRFP460 MOSFETs  │    │
│  │          │  │N-ch  │ │N-ch  ││   (500V 20A)       │    │
│  │          │  └──┬───┘ └──┬───┘│                     │    │
│  │          │     │         │    │                     │    │
│  │          │  ┌──┴───┐ ┌──┴───┐│                     │    │
│  │          │  │Q3    │ │Q4    ││ ← IRFP460 MOSFETs  │    │
│  │          │  │N-ch  │ │N-ch  ││                     │    │
│  │          │  └──────┘ └──────┘│                     │    │
│  │          └─────────┬─────────┘                     │    │
│  │                    │                               │    │
│  │          ┌─────────┴─────────┐                     │    │
│  │          │   GATE DRIVERS    │                     │    │
│  │          │    IR2110 ×2      │                     │    │
│  │          │                   │                     │    │
│  │          │  IN ──── HIN ──── PWM ──── Arduino     │    │
│  │          │  IN ──── LIN ──── PWM ──── Arduino     │    │
│  │          └───────────────────┘                     │    │
│  │                                                    │    │
│  │          ┌───────────────────┐                     │    │
│  │          │  RESONANT TANK    │                     │    │
│  │          │                   │                     │    │
│  │          │  Litz Wire Coil   │                     │    │
│  │          │  (T106-2 Core)    │                     │    │
│  │          │  N = 47 turns     │                     │    │
│  │          │  L ≈ 2.3mH       │                     │    │
│  │          │                   │                     │    │
│  │          │  ┌──────────────┐ │                     │    │
│  │          │  │ 0.1μF ×4     │ │                     │    │
│  │          │  │ (2kV film)   │ │                     │    │
│  │          │  │ parallel     │ │                     │    │
│  │          │  │ C = 0.4μF    │ │                     │    │
│  │          │  └──────────────┘ │                     │    │
│  │          │                   │                     │    │
│  │          │  f₀ = 1/(2π√LC)  │                     │    │
│  │          │  f₀ ≈ 161.8 kHz  │ ← Phi-harmonic freq │    │
│  │          └───────────────────┘                     │    │
│  │                                                    │    │
│  │          ┌───────────────────┐                     │    │
│  │          │   PLASMA TUBE     │                     │    │
│  │          │  (Quartz, 50mm)   │                     │    │
│  │          │                   │                     │    │
│  │          │  Ignition Coil    │                     │    │
│  │          │  12V → 15kV       │                     │    │
│  │          │  (Auto salvage)   │                     │    │
│  │          │                   │                     │    │
│  │          │  Grid: SS 40-mesh │                     │    │
│  │          │  Cathode: W wire  │                     │    │
│  │          └───────────────────┘                     │    │
│  │                                                    │    │
│  │          ┌───────────────────┐                     │    │
│  │          │  EXHAUST NOZZLE   │                     │    │
│  │          │  (Copper, φ-ratio)│                     │    │
│  │          │                   │                     │    │
│  │          │  Throat: 15mm     │                     │    │
│  │          │  Exit: 24.27mm    │                     │    │
│  │          │  (φ-ratio expansion)│                    │    │
│  │          └───────────────────┘                     │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  SERVO (Thrust Vectoring):                                 │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Servo Motor (25kg, metal gear)                     │    │
│  │  Signal: PWM from Arduino (pin D2-D5)               │    │
│  │  Power: 12V from Avionics Bus                       │    │
│  │  Range: ±15° vectoring                              │    │
│  │  Rate: 60°/sec                                      │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## AVIONICS WIRING

```
┌─────────────────────────────────────────────────────────────────────┐
│                    AVIONICS WIRING DIAGRAM                           │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────┐       │
│  │               ARDUINO MEGA 2560 (Flight Computer)        │       │
│  │                                                          │       │
│  │  POWER:                                                  │       │
│  │    VIN ◄──── 12V from Avionics Bus (via 12V→5V Buck)    │       │
│  │    5V  ────► Sensor Power (GPS, IMU, Altimeter)          │       │
│  │    3.3V ───► BMP388 Altimeter VCC                        │       │
│  │    GND ────► Common Ground Bus                           │       │
│  │                                                          │       │
│  │  ANALOG INPUTS (A0-A15):                                 │       │
│  │    A0 ──► Battery 1 Voltage Divider (10kΩ/2.2kΩ)       │       │
│  │    A1 ──► Battery 2 Voltage Divider                      │       │
│  │    A2 ──► Battery 3 Voltage Divider                      │       │
│  │    A3 ──► Battery 4 Voltage Divider                      │       │
│  │    A4 ──► Thruster 1 Current (ACS712 30A)               │       │
│  │    A5 ──► Thruster 2 Current (ACS712 30A)               │       │
│  │    A6 ──► Thruster 3 Current (ACS712 30A)               │       │
│  │    A7 ──► Thruster 4 Current (ACS712 30A)               │       │
│  │    A8 ──► Temperature Sensor 1 (LM35)                   │       │
│  │    A9 ──► Temperature Sensor 2 (LM35)                   │       │
│  │    A10 ──► Temperature Sensor 3 (LM35)                  │       │
│  │    A11 ──► Temperature Sensor 4 (LM35)                  │       │
│  │                                                          │       │
│  │  DIGITAL I/O:                                            │       │
│  │    D0  ──► (Reserved — Serial RX)                       │       │
│  │    D1  ──► (Reserved — Serial TX)                       │       │
│  │    D2  ──► Servo 1 PWM (Thruster 1 Vector)              │       │
│  │    D3  ──► Servo 2 PWM (Thruster 2 Vector)              │       │
│  │    D4  ──► Servo 3 PWM (Thruster 3 Vector)              │       │
│  │    D5  ──► Servo 4 PWM (Thruster 4 Vector)              │       │
│  │    D6  ──► Thruster 1 MOSFET Gate (PWM)                 │       │
│  │    D7  ──► Thruster 2 MOSFET Gate (PWM)                 │       │
│  │    D8  ──► Thruster 3 MOSFET Gate (PWM)                 │       │
│  │    D9  ──► Thruster 4 MOSFET Gate (PWM)                 │       │
│  │    D10 ──► Relay 1 (Thruster 1 Enable)                  │       │
│  │    D11 ──► Relay 2 (Thruster 2 Enable)                  │       │
│  │    D12 ──► Relay 3 (Thruster 3 Enable)                  │       │
│  │    D13 ──► Relay 4 (Thruster 4 Enable)                  │       │
│  │    D22 ──► Buzzer 1 (Warning)                           │       │
│  │    D23 ──► Buzzer 2 (Altitude Alert)                    │       │
│  │    D24 ──► LED Green (Systems OK)                       │       │
│  │    D25 ──► LED Red (Warning)                            │       │
│  │    D26 ──► LED Yellow (Caution)                         │       │
│  │    D27 ──► Parachute Deploy Solenoid                    │       │
│  │    D28 ──► Emergency Ignition Button                    │       │
│  │                                                          │       │
│  │  COMMUNICATIONS:                                         │       │
│  │    Serial0 (D0/D1) ──► USB (Programming)                │       │
│  │    Serial1 (D18/D19) ──► GPS Module (9600 baud)         │       │
│  │    Serial2 (D16/D17) ──► HC-12 Telemetry (9600 baud)    │       │
│  │    Serial3 (D14/D15) ──► VHF Radio (9600 baud)          │       │
│  │    SDA (D20) ──► I2C Bus (IMU, OLED, Altimeter)         │       │
│  │    SCL (D21) ──► I2C Bus                                │       │
│  │                                                          │       │
│  │  SPI BUS:                                                │       │
│  │    MOSI (D51) ──► SD Card Module (Data Logging)         │       │
│  │    MISO (D50) ──► SD Card Module                        │       │
│  │    SCK  (D52) ──► SD Card Module                        │       │
│  │    SS   (D53) ──► SD Card Module (CS)                   │       │
│  │                                                          │       │
│  └──────────────────────────────────────────────────────────┘       │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────┐       │
│  │               SENSOR WIRING                               │       │
│  │                                                          │       │
│  │  GPS MODULE (BN-880):                                    │       │
│  │    VCC ──► 5V (Arduino)                                  │       │
│  │    GND ──► GND                                           │       │
│  │    TX  ──► D19 (Serial1 RX)                              │       │
│  │    RX  ──► D18 (Serial1 TX)                              │       │
│  │    SDA ──► D20 (I2C)                                     │       │
│  │    SCL ──► D21 (I2C)                                     │       │
│  │                                                          │       │
│  │  IMU (MPU-9250):                                         │       │
│  │    VCC ──► 3.3V                                          │       │
│  │    GND ──► GND                                           │       │
│  │    SDA ──► D20 (I2C)                                     │       │
│  │    SCL ──► D21 (I2C)                                     │       │
│  │    INT ──► D2 (Interrupt)                                 │       │
│  │                                                          │       │
│  │  BAROMETRIC ALTIMETER (BMP388):                          │       │
│  │    VCC ──► 3.3V                                          │       │
│  │    GND ──► GND                                           │       │
│  │    SDA ──► D20 (I2C)                                     │       │
│  │    SCL ──► D21 (I2C)                                     │       │
│  │                                                          │       │
│  │  OLED DISPLAY (1.3" I2C):                                │       │
│  │    VCC ──► 5V                                             │       │
│  │    GND ──► GND                                           │       │
│  │    SDA ──► D20 (I2C)                                     │       │
│  │    SCL ──► D21 (I2C)                                     │       │
│  │                                                          │       │
│  └──────────────────────────────────────────────────────────┘       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## GROUND BUS AND SHIELDING

```
┌─────────────────────────────────────────────────────────────┐
│                  GROUND SYSTEM                               │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  PRIMARY GROUND: Aluminum Frame                     │    │
│  │                                                     │    │
│  │  All ground connections use ring terminals crimped  │    │
│  │  and bolted directly to aluminum frame with star    │    │
│  │  washers (scratch-through anodize).                 │    │
│  │                                                     │    │
│  │  Ground Wire: 10 AWG green/yellow, minimum          │    │
│  │  Ground Points: Every subsystem, minimum 2 per unit │    │
│  │                                                     │    │
│  │  Star Ground Topology:                              │    │
│  │                                                     │    │
│  │         ┌──────────────┐                             │    │
│  │         │  POWER GND   │ ← Single-point star        │    │
│  │         │  (center of  │   ground on aluminum        │    │
│  │         │  bus bar)    │   floor pan                 │    │
│  │         └──────┬───────┘                             │    │
│  │                │                                     │    │
│  │    ┌───────────┼───────────┬───────────┐             │    │
│  │    │           │           │           │             │    │
│  │  ┌─┴─┐      ┌─┴─┐      ┌─┴─┐      ┌─┴─┐           │    │
│  │  │PWR│      │SIG│      │RF │      │CHS│           │    │
│  │  │GND│      │GND│      │GND│      │GND│           │    │
│  │  └───┘      └───┘      └───┘      └───┘           │    │
│  │                                                     │    │
│  │  Power GND: Battery negatives, ANL fuse returns     │    │
│  │  Signal GND: Arduino, sensors, displays              │    │
│  │  RF GND: VHF radio, telemetry, GPS shield            │    │
│  │  Chassis GND: Frame, shell, fasteners                │    │
│  │                                                     │    │
│  │  ALL grounds meet at star point on floor pan.        │    │
│  │  NO ground loops. NO daisy-chaining.                 │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  SHIELDING:                                                 │
│  - RF cable: braided shield connected to chassis GND       │
│  - Signal cable: foil shield connected to signal GND       │
│  - Power cable: unshielded (high current, low freq)        │
│  - GPS: shielded enclosure (aluminum foil wrap)            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## WIRE GAUGE TABLE

| Circuit | Wire Gauge | Color | Current | Notes |
|---------|-----------|-------|---------|-------|
| Battery Main Bus | 4 AWG | Red/Black | 150A | Welding cable |
| Thruster Feed | 4 AWG | Red | 150A | Per thruster |
| Thruster Return | 4 AWG | Black | 150A | Per thruster |
| Avionics Feed | 10 AWG | Red | 15A | To buck converters |
| Avionics Return | 10 AWG | Black | 15A | To star ground |
| Servo Power | 14 AWG | Red/Black | 5A | Per servo pair |
| Signal (Analog) | 22 AWG | Yellow | <1A | Shielded twisted pair |
| Signal (Digital) | 22 AWG | Various | <1A | Ribbon cable |
| I2C Bus | 24 AWG | SDA/SCL | <100mA | Twisted pair |
| Serial | 24 AWG | TX/RX | <100mA | Twisted pair |
| Ground Bus | 10 AWG | Green/Yellow | 15A | Star ground |
| Ignition Coil | 16 AWG | Red/Black | 5A | Short runs only |
| HV Coil Lead | 7mm Silicone | Red | 15kV | High-voltage rated |

---

## CONNECTOR TYPES

| Connector | Location | Pins | Rating |
|-----------|----------|------|--------|
| XT90 | Battery to Bus | 2 | 90A continuous |
| XT60 | Thruster to Bus | 2 | 60A continuous |
| JST-XH | Servo connections | 3 | 3A |
| Anderson SB50 | Main disconnect | 2 | 50A |
| DB9 | Data ports | 9 | Signal only |
| Aviation XLR | Intercom | 3 | Audio |
| MC4 | Solar input | 2 | 30A |
| banana plug | Test points | 2 | 20A |

---

## WIRING COLOR CODE

| Color | Function |
|-------|----------|
| Red | +12V DC Power |
| Black | DC Ground/Return |
| Green/Yellow | Chassis Ground |
| Blue | +5V Regulated |
| Purple | +3.3V Regulated |
| Yellow | Analog Signal |
| White | Digital Signal |
| Orange | PWM Signal |
| Pink | I2C SDA |
| Gray | I2C SCL |
| Brown | Serial TX |
| Violet | Serial RX |
| Green | Status LED |
| Red/White | Warning LED |
