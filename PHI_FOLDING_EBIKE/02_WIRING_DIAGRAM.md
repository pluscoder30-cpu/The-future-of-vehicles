# PHI_FOLDING_EBIKE — Wiring Diagram

## Main Power Distribution

```
                    ┌─────────────────────────────────────────────┐
                    │              BATTERY PACK 36V               │
                    │         (10S LiFePO4, 12.5Ah)              │
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
             │CONTROLL│ │CHARGE│ │HEAD │ │TAIL │ │POWER   │
             │ER 15A  │ │PORT  │ │LIGHT│ │LIGHT│ │SWITCH  │
             │36V     │ │(GX16)│ │     │ │     │ │        │
             └────┬───┘ └──────┘ └─────┘ └─────┘ └────────┘
                  │
             ┌────┴───┐
             │  HUB   │
             │ MOTOR  │
             │ 350W   │
             │36V     │
             └────────┘
```

## Controller & Motor Wiring

```
                    ┌─────────────────────────┐
                    │  CONTROLLER (36V 15A)   │
                    │                         │
                    │  BATTERY+ ◄═══ 36V+     │
                    │  BATTERY- ◄═══ 36V-     │
                    │                         │
                    │  MOTOR U ────────►  Phase U (Blue)
                    │  MOTOR V ────────►  Phase V (Green)
                    │  MOTOR W ────────►  Phase W (Yellow)
                    │                         │
                    │  THROTTLE ◄────────  Thumb Throttle
                    │  BRAKE L  ◄────────  Left Brake Lever
                    │  BRAKE R  ◄────────  Right Brake Lever
                    │  PAS     ◄────────  Cadence Sensor
                    │  SPD     ◄────────  Speed Sensor
                    │                         │
                    │  HALL U   ◄────────  Hall Sensor U
                    │  HALL V   ◄────────  Hall Sensor V
                    │  HALL W   ◄────────  Hall Sensor W
                    │                         │
                    │  5V OUT  ────────►  Sensors VCC
                    │  GND     ────────►  Common Ground
                    │                         │
                    │  LCD TX  ────────►  LCD Display RX
                    │  LCD RX  ◄───────  LCD Display TX
                    │  LCD PWR ────────►  LCD VCC (5V)
                    └─────────────────────────┘
```

## LCD Display & Sensors Wiring

```
    ┌─────────────────────────────────────────────────┐
    │              LCD DISPLAY (850C)                  │
    │                                                  │
    │  ┌──────────────────────────────────────────┐   │
    │  │  ██████████████████████████████████████   │   │
    │  │  █  SPEED    ████████████  BATTERY    █   │   │
    │  │  █  25 km/h  ████████████  ████░░░░  █   │   │
    │  │  █                                          │   │
    │  │  █  ASSIST: LEVEL 3/5    ODO: 1234 km  █   │   │
    │  │  ██████████████████████████████████████   │   │
    │  └──────────────────────────────────────────┘   │
    │                                                  │
    │  Connectors:                                    │
    │  TX  ────────► Controller LCD RX               │
    │  RX  ◄─────── Controller LCD TX               │
    │  VCC ────────► 5V from Controller              │
    │  GND ────────► Common Ground                   │
    └─────────────────────────────────────────────────┘

    CADENCE SENSOR:
    ┌─────────────────────────────────────────────────┐
    │              CADENCE SENSOR                      │
    │                                                  │
    │  Mounted on bottom bracket                      │
    │  12 magnets on pedal crank arm                  │
    │  Hall sensor detects rotation                   │
    │                                                  │
    │  Signal ────────► Controller PAS input          │
    │  VCC    ────────► 5V from Controller            │
    │  GND    ────────► Common Ground                 │
    │                                                  │
    │  Output: Square wave, frequency proportional    │
    │  to pedaling speed                              │
    └─────────────────────────────────────────────────┘

    THUMB THROTTLE:
    ┌─────────────────────────────────────────────────┐
    │              THUMB THROTTLE                      │
    │                                                  │
    │  Mounted on right handlebar                     │
    │  Hall-effect, 0-3.3V output                    │
    │                                                  │
    │  Signal ────────► Controller Throttle input     │
    │  VCC    ────────► 5V from Controller            │
    │  GND    ────────► Common Ground                 │
    └─────────────────────────────────────────────────┘
```

## Power Regulation

```
    36V BATTERY ──────┬──────────────────────────┐
                      │                          │
                 ┌────┴────┐                ┌────┴────┐
                 │CONTROLL │                │  CHARGE │
                 │ER       │                │  PORT   │
                 │36V→5V   │                │  GX16   │
                 │internal │                │         │
                 └────┬────┘                └────┬────┘
                      │                          │
                 5V BUS                     36V to BMS
                      │
                 ┌────┴────┐
                 │LCD      │
                 │Display  │
                 │Throttle │
                 │Sensors  │
                 └─────────┘
```

## Wire Colors & Connectors

| Wire | Color | Function | Connector |
|------|-------|----------|-----------|
| Battery + | Red (12AWG) | 36V positive | XT60 |
| Battery - | Black (12AWG) | 36V negative | XT60 |
| Phase U | Blue (12AWG) | Motor phase U | Bullet |
| Phase V | Green (12AWG) | Motor phase V | Bullet |
| Phase W | Yellow (12AWG) | Motor phase W | Bullet |
| Hall U | Red (22AWG) | Hall sensor VCC | JST |
| Hall V | Black (22AWG) | Hall sensor GND | JST |
| Hall W | Blue (22AWG) | Hall sensor U | JST |
| Throttle | Green (22AWG) | Throttle signal | JST |
| PAS | White (22AWG) | Cadence signal | JST |
| Brake L | Yellow (22AWG) | Left brake cutoff | JST |
| Brake R | Orange (22AWG) | Right brake cutoff | JST |
