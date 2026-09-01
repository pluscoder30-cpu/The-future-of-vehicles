# PHI_WATER_HOVERCRAFT — Wiring Diagram

## Main Power Distribution

```
                    ┌─────────────────────────────────────────────┐
                    │              BATTERY PACK 48V               │
                    │         (16S LiFePO4, 15Ah)                │
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
                     │  40A    │                 │  Board  │
                     └────┬────┘                 └────┬────┘
                          │                           │
                    ┌─────┴───────────────────────────┴─────┐
                    │            MAIN POWER BUS 48V          │
                    │  ═══════════════════════════════════════│
                    └──┬──────────┬──────────┬──────────┬───┘
                       │          │          │          │
                  ┌────┘     ┌────┘     ┌────┘     ┌───┘
                  │          │          │          │
             ┌────┴───┐ ┌───┴────┐ ┌───┴────┐ ┌───┴────┐
             │LIFT    │ │THRUST  │ │CHARGER │ │POWER   │
             │ESC     │ │ESC     │ │PORT    │ │SWITCH  │
             │30A     │ │20A     │ │(GX16)  │ │        │
             └────┬───┘ └───┬────┘ └────────┘ └────────┘
                  │          │
             ┌────┴───┐ ┌───┴────┐
             │LIFT    │ │THRUST  │
             │MOTOR   │ │MOTOR   │
             │800W    │ │500W    │
             │48V     │ │48V     │
             └────────┘ └────────┘
```

## Lift System Wiring

```
                    ┌─────────────────────────┐
                    │     LIFT ESC (48V 30A)  │
                    │                         │
                    │  BATTERY+ ◄═══ 48V+     │
                    │  BATTERY- ◄═══ 48V-     │
                    │                         │
                    │  MOTOR U ────────►  Phase U (Blue)
                    │  MOTOR V ────────►  Phase V (Green)
                    │  MOTOR W ────────►  Phase W (Yellow)
                    │                         │
                    │  THROTTLE ◄────────  Throttle Signal
                    │                         │
                    │  HALL U   ◄────────  Hall Sensor U
                    │  HALL V   ◄────────  Hall Sensor V
                    │  HALL W   ◄────────  Hall Sensor W
                    │                         │
                    │  5V OUT  ────────►  Hall Sensor VCC
                    │  GND     ────────►  Common Ground
                    └─────────────────────────┘

    LIFT MOTOR + FAN:
    ┌─────────────────────────────────────────────────┐
    │                                                  │
    │    ┌──────────────────────────────┐             │
    │    │      LIFT MOTOR (800W)       │             │
    │    │      48V BLDC, 3000RPM       │             │
    │    └──────────────┬───────────────┘             │
    │                   │                              │
    │    ┌──────────────┴───────────────┐             │
    │    │      COUPLER (set screw)     │             │
    │    └──────────────┬───────────────┘             │
    │                   │                              │
    │    ┌──────────────┴───────────────┐             │
    │    │      CENTRIFUGAL FAN         │             │
    │    │      250mm, 9-blade          │             │
    │    │      Polypropylene           │             │
    │    └──────────────┬───────────────┘             │
    │                   │                              │
    │    ┌──────────────┴───────────────┐             │
    │    │      FAN SHROUD              │             │
    │    │      ABS, 300mm diameter     │             │
    │    └──────────────┬───────────────┘             │
    │                   │                              │
    │    ┌──────────────┴───────────────┐             │
    │    │      AIR DUCTING             │             │
    │    │      150mm, flexible, 2m     │             │
    │    └──────────────┬───────────────┘             │
    │                   │                              │
    │    ┌──────────────┴───────────────┐             │
    │    │      PHI-HARMONIC PORT RING  │             │
    │    │      8 ports at 137.5°       │             │
    │    │      (see 03_MECHANICAL)     │             │
    │    └──────────────────────────────┘             │
    │                                                  │
    └─────────────────────────────────────────────────┘
```

## Thrust System Wiring

```
                    ┌─────────────────────────┐
                    │    THRUST ESC (48V 20A) │
                    │                         │
                    │  BATTERY+ ◄═══ 48V+     │
                    │  BATTERY- ◄═══ 48V-     │
                    │                         │
                    │  MOTOR U ────────►  Phase U (Blue)
                    │  MOTOR V ────────►  Phase V (Green)
                    │  MOTOR W ────────►  Phase W (Yellow)
                    │                         │
                    │  THROTTLE ◄────────  Throttle Signal
                    │                         │
                    │  HALL U/V/W ◄─────  Hall Sensors
                    │                         │
                    └─────────────────────────┘

    THRUST MOTOR + PROPELLER:
    ┌─────────────────────────────────────────────────┐
    │                                                  │
    │    ┌──────────────────────────────┐             │
    │    │      THRUST MOTOR (500W)     │             │
    │    │      48V BLDC, 2800RPM       │             │
    │    └──────────────┬───────────────┘             │
    │                   │                              │
    │    ┌──────────────┴───────────────┐             │
    │    │      THRUST BEARING          │             │
    │    │      (thrust washers)        │             │
    │    └──────────────┬───────────────┘             │
    │                   │                              │
    │    ┌──────────────┴───────────────┐             │
    │    │      PROPELLER               │             │
    │    │      300mm, 2-blade, folding │             │
    │    └──────────────┬───────────────┘             │
    │                   │                              │
    │    ┌──────────────┴───────────────┐             │
    │    │      PROPELLER GUARD         │             │
    │    │      Wire cage, 350mm        │             │
    │    └──────────────────────────────┘             │
    │                                                  │
    └─────────────────────────────────────────────────┘
```

## Throttle & Control Wiring

```
    ┌─────────────────────────────────────────────────┐
    │              THROTTLE ASSEMBLY                    │
    │                                                  │
    │    ┌──────────────────────────────────────────┐ │
    │    │  Hall-effect lever throttle               │ │
    │    │                                          │ │
    │    │  Signal ────┬──► Lift ESC Throttle       │ │
    │    │             └──► Thrust ESC Throttle     │ │
    │    │                                          │ │
    │    │  VCC (5V) ◄── from Lift ESC              │ │
    │    │  GND ──────► Common Ground               │ │
    │    └──────────────────────────────────────────┘ │
    │                                                  │
    │    Both ESCs receive same throttle signal        │
    │    Lift and thrust increase together             │
    │                                                  │
    └─────────────────────────────────────────────────┘

    RUDDER:
    ┌─────────────────────────────────────────────────┐
    │              RUDDER ASSEMBLY                     │
    │                                                  │
    │    ┌──────────────────────────────────────────┐ │
    │    │  Aluminum plate on pivot                 │ │
    │    │  Connected to foot pedals via cables     │ │
    │    │                                          │ │
    │    │  Left pedal ──── Cable ────► Rudder left │ │
    │    │  Right pedal ─── Cable ────► Rudder right│ │
    │    │                                          │ │
    │    │  No electronics — pure mechanical        │ │
    │    └──────────────────────────────────────────┘ │
    │                                                  │
    └─────────────────────────────────────────────────┘
```

## Power Regulation

```
    48V BATTERY ──────┬──────────────────────────┐
                      │                          │
                 ┌────┴────┐                ┌────┴────┐
                 │  FUSE   │                │  CHARGE │
                 │  40A    │                │  PORT   │
                 └────┬────┘                │  GX16   │
                      │                     └────┬────┘
                      │                          │
                 48V BUS                     48V to BMS
                      │
                 ┌────┴────┐
                 │ LIFT    │
                 │ ESC     │
                 │ 30A     │
                 └─────────┘
```

## Connectors Key

| Symbol | Connector Type |
|--------|----------------|
| ═══ | 10AWG Silicone Wire (power) |
| ─── | 18AWG Silicone Wire (motor) |
| ─··─ | 22AWG Silicone Wire (signal) |
| ┌─┐ | Screw Terminal Block |
| └─┘ | JST-PH Connector |
| ─┬─ | Solder Joint |
