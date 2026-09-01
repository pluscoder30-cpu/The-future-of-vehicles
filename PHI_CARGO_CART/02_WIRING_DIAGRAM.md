# PHI_CARGO_CART — Wiring Diagram

## Main Power Distribution

```
                    ┌─────────────────────────────────────────────┐
                    │              BATTERY PACK 36V               │
                    │         (10S LiFePO4, 15Ah)                │
                    │  ┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐│
                    │  │3.2││3.2││3.2││3.2││3.2││3.2││3.2││3.2││
                    │  └───┘└───┘└───┘└───┘└───┘└───┘└───┘└───┘│
                    │  ┌───┐┌───┐                               │
                    │  │3.2││3.2│   (10 cells in series)        │
                    │  └───┘└───┘                               │
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
                    │            MAIN POWER BUS 36V          │
                    │  ═══════════════════════════════════════│
                    └──┬──────┬──────┬──────┬──────┬────────┘
                       │      │      │      │      │
                  ┌────┘  ┌───┘  ┌───┘  ┌───┘  ┌───┘
                  │       │      │      │      │
             ┌────┴───┐ ┌─┴────┐ ┌┴────┐ ┌┴────┐ ┌──┴─────┐
             │  ESC   │ │CHARGE│ │ OLED│ │POWER│ │  FUSE  │
             │  25A   │ │PORT  │ │DISP │ │SWITCH│ │  30A   │
             └────┬───┘ └──────┘ └─────┘ └─────┘ └────────┘
                  │
             ┌────┴───┐
             │  HUB   │
             │ MOTOR  │
             │ 500W   │
             │36V     │
             └────────┘
```

## ESC & Motor Wiring

```
                    ┌─────────────────────────┐
                    │     ESC (36V 25A)       │
                    │                         │
                    │  BATTERY+ ◄═══ 36V+     │
                    │  BATTERY- ◄═══ 36V-     │
                    │                         │
                    │  MOTOR U ────────►  Phase U (Blue)
                    │  MOTOR V ────────►  Phase V (Green)
                    │  MOTOR W ────────►  Phase W (Yellow)
                    │                         │
                    │  THROTTLE ◄────────  Remote Signal
                    │  BRAKE    ◄────────  Remote Signal
                    │  HALL U   ◄────────  Hall Sensor U
                    │  HALL V   ◄────────  Hall Sensor V
                    │  HALL W   ◄────────  Hall Sensor W
                    │                         │
                    │  5V OUT  ────────►  Hall Sensor VCC
                    │  GND     ────────►  Common Ground
                    └─────────────────────────┘

    HUB MOTOR:
    ┌─────────────────────────────────────┐
    │           HUB MOTOR (16")           │
    │                                     │
    │    ┌─────────────────────────┐      │
    │    │     STATOR (fixed)      │      │
    │    │                         │      │
    │    │  Coil groups at phi-    │      │
    │    │  harmonic angles:       │      │
    │    │  0°, 137.5°, 275°,     │      │
    │    │  52.5°, 190°, 327.5°,  │      │
    │    │  105°, 242.5°          │      │
    │    │                         │      │
    │    │  8 coil groups total    │      │
    │    │  (phi-harmonic spacing) │      │
    │    └─────────────────────────┘      │
    │                                     │
    │    ┌─────────────────────────┐      │
    │    │     ROTOR (spins)       │      │
    │    │                         │      │
    │    │  N52 magnets arranged   │      │
    │    │  in phi-harmonic ring   │      │
    │    └─────────────────────────┘      │
    │                                     │
    │    Wires: 3 phase + 3 hall sensors  │
    └─────────────────────────────────────┘
```

## Controller & Remote Wiring

```
    ┌─────────────────────────────────────────────────┐
    │              ARDUINO NANO                        │
    │              (OLED Display Driver)               │
    │                                                  │
    │  VIN ◄──── 5V from ESC 5V output                │
    │  GND ────► Common Ground                         │
    │                                                  │
    │  A4 ──── I2C SDA ────► OLED Display SDA         │
    │  A5 ──── I2C SCL ────► OLED Display SCL         │
    │                                                  │
    │  A0 ◄──── Battery Voltage Divider                │
    │         36V ──┬── R1 (33kΩ) ──┬── A0            │
    │               └── R2 (3.3kΩ) ──┴── GND          │
    │                                                  │
    │  D2 ◄──── Power Button (pull-up 10kΩ)           │
    │  D3 ◄──── Brake Signal from ESC                  │
    │                                                  │
    └─────────────────────────────────────────────────┘

    BLUETOOTH REMOTE:
    ┌──────────────────────────┐
    │   Handheld Remote        │
    │                          │
    │   Thumb Throttle ──────► ESC Signal
    │   Trigger Brake  ──────► ESC Signal
    │   Battery LED    ◄───── 3.7V LiPo
    │   Pairing Button         │
    │                          │
    │   Range: 10m Bluetooth   │
    │   Battery: 3.7V 300mAh  │
    └──────────────────────────┘
```

## Power Regulation

```
    36V BATTERY ──────┬──────────────────────────┐
                      │                          │
                 ┌────┴────┐                ┌────┴────┐
                 │  ESC    │                │  CHARGE │
                 │  25A    │                │  PORT   │
                 │  36V→5V │                │  GX16   │
                 │  internal│               │         │
                 └────┬────┘                └────┬────┘
                      │                          │
                 5V BUS                     36V to BMS
                      │
                 ┌────┴────┐
                 │Arduino  │
                 │Nano     │
                 │OLED     │
                 │Voltage  │
                 │Divider  │
                 └─────────┘
```

## Connectors Key

| Symbol | Connector Type |
|--------|----------------|
| ═══ | 12AWG Silicone Wire (power) |
| ─── | 22AWG Silicone Wire (signal) |
| ┌─┐ | Screw Terminal Block |
| └─┘ | JST-PH Connector |
| ─┬─ | Solder Joint |
