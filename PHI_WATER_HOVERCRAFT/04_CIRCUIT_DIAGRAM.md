# PHI_WATER_HOVERCRAFT — Electronic Circuit Diagram

## Main Power Distribution

```
    48V BATTERY (+) ──┬── FUSE 40A ──┬── LIFT ESC 30A ── LIFT MOTOR 800W
                      │              │
                      │              └── THRUST ESC 20A ── THRUST MOTOR 500W
                      │
                      ├── CHARGER PORT (GX16)
                      │
                      └── POWER SWITCH (60A)

    48V BATTERY (-) ──┴── BMS ──┬── Common GND
                                └── All ESCs, sensors
```

## Lift System Circuit

```
    ┌─────────────────────────────────────────┐
    │  LIFT ESC (48V 30A Brushless)           │
    │                                         │
    │  BATTERY+ ◄═══ 48V+                     │
    │  BATTERY- ◄═══ 48V-                     │
    │  MOTOR U  ────► Phase U (Blue)          │
    │  MOTOR V  ────► Phase V (Green)         │
    │  MOTOR W  ────► Phase W (Yellow)        │
    │  THROTTLE ◄──── Lever throttle signal   │
    │  HALL U/V/W ◄── Hall sensors            │
    │  5V OUT   ────► Hall sensor VCC         │
    │  GND      ────► Common ground           │
    └─────────────────────────────────────────┘

    LIFT MOTOR ── coupler ── CENTRIFUGAL FAN (250mm)
                                │
                           AIR DUCTING (150mm)
                                │
                     PHI-HARMONIC PORT RING
                     (8 ports at 137.5°)
                                │
                           NYLON SKIRT
                           (air cushion)
```

## Thrust System Circuit

```
    ┌─────────────────────────────────────────┐
    │  THRUST ESC (48V 20A Brushless)         │
    │                                         │
    │  BATTERY+ ◄═══ 48V+                     │
    │  BATTERY- ◄═══ 48V-                     │
    │  MOTOR U  ────► Phase U (Blue)          │
    │  MOTOR V  ────► Phase V (Green)         │
    │  MOTOR W  ────► Phase W (Yellow)        │
    │  THROTTLE ◄──── Same lever throttle     │
    │  HALL U/V/W ◄── Hall sensors            │
    └─────────────────────────────────────────┘

    THRUST MOTOR ── THRUST BEARING ── PROPELLER (300mm)
                                            │
                                     PROPELLER GUARD
                                            │
                                       RUDDER (mechanical)
```

## Throttle Wiring

```
    HALL-EFFECT LEVER THROTTLE:
    ┌─────────────────────────────────────┐
    │  Signal ──┬──► Lift ESC Throttle    │
    │           └──► Thrust ESC Throttle  │
    │  VCC (5V) ◄── from Lift ESC        │
    │  GND ──────► Common Ground         │
    └─────────────────────────────────────┘

    Both ESCs receive same signal (lift + thrust linked)
```

## Battery Monitor Circuit

```
    48V ──┬── R1 (47kΩ) ──┬── Arduino A0
           │               │
           └── R2 (4.7kΩ) ──┴── GND

    V_out = 48V × (4.7k / (47k + 4.7k)) = 4.36V
    Safe for Arduino ADC (max 5V)
```

## Component Summary

| Component | Value | Rating | Qty |
|-----------|-------|--------|-----|
| Lift ESC | 48V 30A | 1440W max | 1 |
| Thrust ESC | 48V 20A | 960W max | 1 |
| Lift Motor | 800W 48V BLDC | 3000RPM | 1 |
| Thrust Motor | 500W 48V BLDC | 2800RPM | 1 |
| Throttle | Hall-effect lever | 0-3.3V | 1 |
| Fuse | 40A blade | Automotive | 1 |
| Power Switch | 60A rocker | Panel mount | 1 |
| Charger | 48V 5A LiFePO4 | CC/CV | 1 |
| Voltage Divider R1 | 47kΩ | 1/4W | 1 |
| Voltage Divider R2 | 4.7kΩ | 1/4W | 1 |
