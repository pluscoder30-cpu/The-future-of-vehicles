# PHI_HOVERBOARD — Wiring Diagram

## Main Power Distribution

```
                    ┌─────────────────────────────────────────────┐
                    │              BATTERY PACK 48V               │
                    │         (16S LiFePO4, 10Ah)                │
                    │  ┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐│
                    │  │3.2││3.2││3.2││3.2││3.2││3.2││3.2││3.2││
                    │  └───┘└───┘└───┘└───┘└───┘└───┘└───┘└───┘│
                    │  ┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐│
                    │  │3.2││3.2││3.2││3.2││3.2││3.2││3.2││3.2││
                    │  └───┘└───┘└───┘└───┘└───┘└───┘└───┘└───┘│
                    └──────────────┬──────────┬──────────────────┘
                                   │          │
                               B+ │          │ B-
                                   │          │
                          ┌────────┘          └────────┐
                          │                           │
                     ┌────┴────┐                 ┌────┴────┐
                     │  FUSE   │                 │  BMS    │
                     │  30A    │                 │  Board  │
                     └────┬────┘                 └────┬────┘
                          │                           │
                    ┌─────┴───────────────────────────┴─────┐
                    │            MAIN POWER BUS 48V          │
                    │  ═══════════════════════════════════════│
                    └──┬──────┬──────┬──────┬──────┬────────┘
                       │      │      │      │      │
                  ┌────┘   ┌──┘   ┌──┘   ┌──┘   └──┐
                  │        │      │      │          │
             ┌────┴───┐ ┌──┴───┐ ┌┴────┐ ┌┴────┐ ┌──┴────┐
             │COIL 1  │ │COIL 2│ │COIL3│ │COIL4│ │COIL 5-8│
             │H-BRIDGE│ │H-BR. │ │H-BR.│ │H-BR.│ │(same)  │
             └────┬───┘ └──┬───┘ └┬────┘ └┬────┘ └──┬────┘
                  │        │      │       │          │
             ┌────┴───┐ ┌──┴───┐ ┌┴────┐ ┌┴────┐ ┌──┴────┐
             │COIL  A │ │COIL B│ │COILC│ │COILD│ │COIL E-│
             │ 137.5° │ │275.0°│ │412.5│ │550.0│ │H (cont)│
             └────────┘ └──────┘ └─────┘ └─────┘ └───────┘
```

## Controller & Sensor Wiring

```
                    ┌─────────────────────┐
                    │    ARDUINO NANO     │
                    │   (ATmega328P)      │
                    │                     │
                    │  D2  ──────────►  MOSFET Driver 1 (COIL A)
                    │  D3  ──────────►  MOSFET Driver 2 (COIL B)
                    │  D4  ──────────►  MOSFET Driver 3 (COIL C)
                    │  D5  ──────────►  MOSFET Driver 4 (COIL D)
                    │  D6  ──────────►  MOSFET Driver 5 (COIL E)
                    │  D7  ──────────►  MOSFET Driver 6 (COIL F)
                    │  D8  ──────────►  MOSFET Driver 7 (COIL G)
                    │  D9  ──────────►  MOSFET Driver 8 (COIL H)
                    │                     │
                    │  A0  ◄──────────  FSR Left Foot Pad
                    │  A1  ◄──────────  FSR Right Foot Pad
                    │  A2  ◄──────────  Current Sensor 1 (Coils A-D)
                    │  A3  ◄──────────  Current Sensor 2 (Coils E-H)
                    │  A4  ◄──────────  Battery Voltage Divider
                    │  A5  ◄──────────  Temperature Sensor (NTC)
                    │                     │
                    │  D10 ──────────►  OLED SDA
                    │  D11 ──────────►  OLED SCL
                    │  D12 ◄──────────  Power Button
                    │  D13 ◄──────────  Emergency Stop Button
                    │                     │
                    │  SDA ◄───┬──────► MPU-6050 #1 (Front)
                    │  SCL ◄───┤       I2C Address: 0x68
                    │          │
                    │          └──────► MPU-6050 #2 (Rear)
                    │                   I2C Address: 0x69
                    │                     │
                    │  VIN ◄──────────  5V from Buck Converter
                    │  GND ──────────►  Common Ground
                    └─────────────────────┘

    ┌──────────────┐    ┌──────────────┐
    │ MPU-6050 #1  │    │ MPU-6050 #2  │
    │ (Front IMU)  │    │ (Rear IMU)   │
    │              │    │              │
    │ VIN→5V       │    │ VIN→5V       │
    │ GND→GND      │    │ GND→GND      │
    │ SDA→A4       │    │ SDA→A4       │
    │ SCL→A5       │    │ SCL→A5       │
    │ INT→D2 (ext) │    │ INT→D3 (ext) │
    └──────────────┘    └──────────────┘
```

## MOSFET H-Bridge Detail (Per Coil)

```
         48V BUS
            │
            │
    ┌───────┴───────┐
    │               │
  ┌─┴─┐           ┌─┴─┐
  │Q1 │ HIGH      │Q2 │ HIGH
  │PMOS│ SIDE     │PMOS│ SIDE
  └─┬─┘           └─┬─┘
    │               │
    ├───────┬───────┤
    │       │       │
  ┌─┴─┐  ┌─┴─┐  ┌─┴─┐
  │COIL│  │COIL│  │COIL│
  │ A  │  │ A  │  │ A  │
  │    │  │    │  │    │
  └─┬─┘  └─┬─┘  └─┬─┘
    │       │       │
    ├───────┴───────┤
    │               │
  ┌─┴─┐           ┌─┴─┐
  │Q3 │ LOW       │Q4 │ LOW
  │NMOS│ SIDE     │NMOS│ SIDE
  └─┬─┘           └─┬─┘
    │               │
    └───────┬───────┘
            │
           GND

    Q1-Q4: IRFZ44N MOSFETs
    Driver: IR2110 half-bridge driver
    
    Control Signals:
    - HIN (from Arduino) → High-side control
    - LIN (from Arduino) → Low-side control
    - PWM frequency: 20 kHz
    - Dead-time: 1µs (prevents shoot-through)
```

## Power Regulation

```
    48V BATTERY ──────┬──────────────────────┐
                      │                      │
                 ┌────┴────┐            ┌────┴────┐
                 │ LM2596  │            │ LM2596  │
                 │ Buck #1 │            │ Buck #2 │
                 │ 48V→12V │            │ 48V→5V  │
                 │ 3A      │            │ 3A      │
                 └────┬────┘            └────┬────┘
                      │                      │
                 12V BUS                 5V BUS
                      │                      │
                 ┌────┴────┐            ┌────┴────┐
                 │MOSFET   │            │Arduino  │
                 │Drivers  │            │Nano     │
                 │(IR2110) │            │MPU-6050 │
                 │         │            │OLED     │
                 │         │            │Sensors  │
                 └─────────┘            └─────────┘
```

## Connectors Key

| Symbol | Connector Type |
|--------|----------------|
| ═══ | 10AWG Silicone Wire (power) |
| ─── | 22AWG Silicone Wire (signal) |
| ─··─ | 26AWG Magnet Wire (coil winding) |
| ┌─┐ | Screw Terminal Block |
| └─┘ | JST-PH Connector |
| ─┬─ | Solder Joint |
