# PHI_E_BIKE — Wiring Diagram

## Main System Wiring

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        PHI-E-BIKE SYSTEM WIRING                          │
└─────────────────────────────────────────────────────────────────────────┘

    ┌──────────────────────────────────────────┐
    │        BATTERY PACK 48V 10.4Ah            │
    │        Samsung 35E Cells                  │
    │        Triangle Frame Mount               │
    │                                          │
    │  ┌─────┐                                 │
    │  │BMS  │ ─── Balance leads               │
    │  └──┬──┘                                 │
    │     │                                    │
    │  XT60 CONNECTOR                          │
    │  ┌─────┐                                 │
    │  │+  - │                                 │
    │  └──┬──┘                                 │
    └─────┼────────────────────────────────────┘
          │
          │ 10AWG Red (+)    10AWG Black (-)
          │
    ┌─────┴────────────────────────────────────────────────────┐
    │                   MAIN POWER BUS                          │
    └──┬──────────────┬──────────────────┬────────────────────┘
       │              │                  │
       │              │                  │
  ┌────┴────┐    ┌────┴────┐        ┌────┴────┐
  │  FUSE   │    │CONTROLLER│        │ CHARGER │
  │  30A    │    │ 48V 22A  │        │ 54.6V 2A│
  │  Blade  │    │          │        │ (GX16)  │
  └────┬────┘    └────┬────┘        └─────────┘
       │              │
       │         ┌────┴──────────────────────────────┐
       │         │                                   │
       │         │    E-BIKE CONTROLLER              │
       │         │    ┌─────────────────────────┐    │
       │         │    │                         │    │
       │         │    │  POWER INPUT            │    │
       │         │    │  B+ ──────────────────► │    │
       │         │    │  B- ──────────────────► │    │
       │         │    │                         │    │
       │         │    │  MOTOR OUTPUT           │    │
       │         │    │  Phase A ─────────────► │    │
       │         │    │  Phase B ─────────────► │    │
       │         │    │  Phase C ─────────────► │    │
       │         │    │  Hall 1-5 ────────────► │    │
       │         │    │                         │    │
       │         │    │  SENSOR INPUTS          │    │
       │         │    │  Torque ──────────────► │    │
       │         │    │  Speed ───────────────► │    │
       │         │    │  Throttle ────────────► │    │
       │         │    │                         │    │
       │         │    │  DISPLAY (UART)         │    │
       │         │    │  TX ──────────────────► │    │
       │         │    │  RX ◄────────────────── │    │
       │         │    │                         │    │
       │         │    │  BRAKE CUT-OFFS         │    │
       │         │    │  Left Brake ──────────► │    │
       │         │    │  Right Brake ─────────► │    │
       │         │    │                         │    │
       │         │    └─────────────────────────┘    │
       │         │                                   │
       │         └────┬──────┬──────┬──────┬────────┘
       │              │      │      │      │
       │              │      │      │      │
       │         ┌────┴──┐┌──┴──┐┌──┴──┐┌──┴────┐
       │         │PHI-HARM│ │TORQUE│ │THUMB│ │BRAKE │
       │         │MOTOR  │ │SENSOR│ │THROT│ │LEVERS│
       │         │REAR   │ │      │ │TLE  │ │      │
       │         │500W   │ │      │ │      │ │      │
       │         │48V    │ │      │ │      │ │      │
       │         └───────┘ └─────┘ └─────┘ └──────┘
```

## Motor Wiring Detail

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PHI-HARMONIC HUB MOTOR                           │
│                    500W, 48V, 26" Wheel                             │
│                                                                     │
│    ┌─────────────────────────────────────────────────────────┐     │
│    │                                                         │     │
│    │   PHI-HARMONIC ROTOR (magnets at 137.5° spacing)       │     │
│    │                                                         │     │
│    │           ┌───────────────────┐                         │     │
│    │           │    ╱╲   ╱╲   ╱╲   │                         │     │
│    │           │   ╱  ╲ ╱  ╲ ╱  ╲  │                         │     │
│    │           │  ╱ 1  ╲╱ 2  ╲╱ 3 ╲ │                         │     │
│    │           │ ╱  137.5°  275.0°╲ │                         │     │
│    │           │╱                  ╲│                         │     │
│    │           │╲   ╱╲   ╱╲   ╱╲  ╱│                         │     │
│    │           │ ╲ ╱  ╲ ╱  ╲ ╱  ╲╱ │                         │     │
│    │           │  ╲╱ 4  ╲╱ 5  ╲╱ 6 │                         │     │
│    │           │   412.5°  550.0°   │                         │     │
│    │           │                    │                         │     │
│    │           │  12 magnets total  │                         │     │
│    │           │  arranged in phi   │                         │     │
│    │           │  golden pattern    │                         │     │
│    │           └───────────────────┘                         │     │
│    │                                                         │     │
│    │   STATOR (3-phase coils)                                │     │
│    │                                                         │     │
│    │   Phase A ──────────────── Coil A ──── Coil A'          │     │
│    │   Phase B ──────────────── Coil B ──── Coil B'          │     │
│    │   Phase C ──────────────── Coil C ──── Coil C'          │     │
│    │                                                         │     │
│    └─────────────────────────────────────────────────────────┘     │
│                                                                     │
│    MOTOR LEADS (10-wire cable):                                     │
│    ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐           │
│    │ A  │ B  │ C  │ H1 │ H2 │ H3 │ H4 │ H5 │ +5V │ GND │           │
│    │Phs │Phs │Phs │Hall│Hall│Hall│Hall│Hall│     │     │           │
│    └──┬─┴──┬─┴──┬─┴──┬─┴──┬─┴──┬─┴──┬─┴──┬─┴──┬─┴──┬─┘           │
│       │    │    │    │    │    │    │    │    │    │                │
│       └────┴────┴────┴────┴────┴────┴────┴────┴────┘                │
│                          10-pin connector                           │
│                          (to controller)                            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Controller Pinout

```
┌─────────────────────────────────────────────────────────────────────┐
│                    E-BIKE CONTROLLER PINOUT                          │
│                    48V 22A, KT-compatible                           │
│                                                                     │
│    ┌─────────────────────────────────────────────────────────┐     │
│    │                                                         │     │
│    │   POWER           MOTOR           SENSOR               │     │
│    │   ┌──────┐        ┌──────┐        ┌──────┐             │     │
│    │   │B+ B- │        │A B C │        │H1-5 +5V│             │     │
│    │   └──┬───┘        └──┬───┘        └──┬───┘             │     │
│    │      │               │               │                  │     │
│    └──────┼───────────────┼───────────────┼──────────────────┘     │
│           │               │               │                         │
│           │               │               │                         │
│    ┌──────┴──────┐  ┌─────┴─────┐  ┌─────┴─────┐                  │
│    │             │  │           │  │           │                  │
│    │  Battery    │  │  Hub      │  │  Hall     │                  │
│    │  Pack       │  │  Motor    │  │  Sensors  │                  │
│    │  XT60       │  │  3-Phase  │  │  (in      │                  │
│    │  Connector  │  │  + Hall   │  │   motor)  │                  │
│    │             │  │           │  │           │                  │
│    └─────────────┘  └───────────┘  └───────────┘                  │
│                                                                     │
│                                                                     │
│    DISPLAY          THROTTLE        BRAKE CUT-OFFS                 │
│    ┌──────┐        ┌──────┐        ┌──────┐                       │
│    │TX RX │        │Signal│        │L+ L- │                       │
│    │GND +5V│        │GND +5V│        │R+ R- │                       │
│    └──┬───┘        └──┬───┘        └──┬───┘                       │
│       │               │               │                            │
│    ┌──┴───┐        ┌──┴───┐        ┌──┴───┐                       │
│    │      │        │      │        │      │                       │
│    │ LCD  │        │Thumb │        │Mech. │                       │
│    │Display│        │Throt.│        │Brakes│                       │
│    │      │        │      │        │      │                       │
│    └──────┘        └──────┘        └──────┘                       │
│                                                                     │
│                                                                     │
│    TORQUE SENSOR       CADENCE SENSOR                              │
│    ┌──────┐           ┌──────┐                                     │
│    │Signal│           │Signal│                                     │
│    │GND +5V│           │GND +5V│                                     │
│    └──┬───┘           └──┬───┘                                     │
│       │                  │                                         │
│    ┌──┴───┐           ┌──┴───┐                                     │
│    │      │           │      │                                     │
│    │BB    │           │BB    │                                     │
│    │Sensor│           │Sensor│                                     │
│    │      │           │      │                                     │
│    └──────┘           └──────┘                                     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## LCD Display Wiring

```
    CONTROLLER                    LCD DISPLAY (KT-LCD3)
    ┌─────────┐                   ┌─────────┐
    │         │                   │         │
    │    TX ──┼───────────────────┼── RX    │
    │    RX ──┼───────────────────┼── TX    │
    │   +5V ──┼───────────────────┼── +5V   │
    │   GND ──┼───────────────────┼── GND   │
    │         │                   │         │
    └─────────┘                   └─────────┘
    
    Communication: UART, 9600 baud
    Display shows:
    - Speed (km/h)
    - Battery level (bars)
    - Assist level (1-5)
    - Trip distance (km)
    - Total distance (km)
    - Power output (W)
    - Temperature (°C)
```

## Connector Types

| Connection | Connector | Wire Gauge | Color Code |
|------------|-----------|------------|------------|
| Battery to Controller | XT60 | 10AWG | Red (+), Black (-) |
| Motor Phase A | Bullet 4mm | 12AWG | Blue |
| Motor Phase B | Bullet 4mm | 12AWG | Green |
| Motor Phase C | Bullet 4mm | 12AWG | Yellow |
| Motor Hall Sensors | 6-pin JST | 22AWG | Multi-color |
| Throttle | 3-pin JST | 22AWG | Red, Black, White |
| Brake Cut-off | 2-pin JST | 22AWG | Red, Black |
| LCD Display | 5-pin JST | 24AWG | Multi-color |
| Torque Sensor | 3-pin JST | 22AWG | Red, Black, White |
| Charger | GX16 4-pin | 16AWG | Red (+), Black (-) |
