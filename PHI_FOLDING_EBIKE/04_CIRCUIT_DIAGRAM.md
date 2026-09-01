# PHI_FOLDING_EBIKE — Electronic Circuit Diagram

## Full Circuit Schematic

```
    ┌─────────────────────────────────────────────────────────────────────────┐
    │                    PHI-FOLDING_EBIKE CIRCUIT                             │
    └─────────────────────────────────────────────────────────────────────────┘

    36V BATTERY (+) ─────┬─────────────────────────────────────────────────────┐
                        │                                                     │
                    ┌───┴───┐                                                 │
                    │FUSE   │ 30A                                            │
                    │BLADE  │                                                │
                    └───┬───┘                                                │
                        │                                                    │
    ┌───────────────────┤  36V POWER BUS                                     │
    │                   │                                                    │
    │   ┌───────────────┴──────────────────────────────────────────────┐     │
    │   │                                                              │     │
    │   │   ┌──────────────────┐    ┌──────────────────────────┐      │     │
    │   │   │                  │    │                          │      │     │
    │   │   │  CONTROLLER      │    │    HUB MOTOR             │      │     │
    │   │   │  36V 15A         │    │    350W 36V              │      │     │
    │   │   │  BRUSHLESS       │    │                          │      │     │
    │   │   │                  │    │  Phase U ──────── Blue   │      │     │
    │   │   │  BATTERY+ ◄══ 36V+   │  Phase V ──────── Green  │      │     │
    │   │   │  BATTERY- ◄══ 36V-   │  Phase W ──────── Yellow │      │     │
    │   │   │                  │    │                          │      │     │
    │   │   │  MOTOR U ────────┼────►                          │      │     │
    │   │   │  MOTOR V ────────┼────►  Hall Sensors:           │      │     │
    │   │   │  MOTOR W ────────┼────►  U ←──── HALL U          │      │     │
    │   │   │                  │    │  V ←──── HALL V          │      │     │
    │   │   │  THROTTLE ◄──────┤    │  W ←──── HALL W          │      │     │
    │   │   │  BRAKE L  ◄──────┤    │                          │      │     │
    │   │   │  BRAKE R  ◄──────┤    │  VCC ←── 5V (controller)│      │     │
    │   │   │  PAS      ◄──────┤    │  GND ──── GND           │      │     │
    │   │   │  SPEED    ◄──────┤    │                          │      │     │
    │   │   │                  │    └──────────────────────────┘      │     │
    │   │   │  LCD TX  ────────┼────► LCD Display RX                  │     │
    │   │   │  LCD RX  ◄───────┤────  LCD Display TX                  │     │
    │   │   │                  │                                      │     │
    │   │   └──────────────────┘                                      │     │
    │   │                                                              │     │
    │   └──────────────────────────────────────────────────────────────┘     │
    │                                                                        │
    │                                                                        │
    │   ┌────────────────────────────────────────────────────────────────┐   │
    │   │                    SENSOR WIRING                                │   │
    │   │                                                                │   │
    │   │   CADENCE SENSOR (bottom bracket):                             │   │
    │   │   ┌──────────────┐                                             │   │
    │   │   │ 12 magnets   │                                             │   │
    │   │   │ on crank arm │                                             │   │
    │   │   │              │                                             │   │
    │   │   │ Signal ────► Controller PAS                                │   │
    │   │   │ VCC (5V) ◄── Controller 5V                                │   │
    │   │   │ GND ──────► Common Ground                                 │   │
    │   │   └──────────────┘                                             │   │
    │   │                                                                │   │
    │   │   THUMB THROTTLE (right handlebar):                            │   │
    │   │   ┌──────────────┐                                             │   │
    │   │   │ Hall-effect   │                                             │   │
    │   │   │ 0-3.3V       │                                             │   │
    │   │   │              │                                             │   │
    │   │   │ Signal ────► Controller Throttle                           │   │
    │   │   │ VCC (5V) ◄── Controller 5V                                │   │
    │   │   │ GND ──────► Common Ground                                 │   │
    │   │   └──────────────┘                                             │   │
    │   │                                                                │   │
    │   │   BRAKE LEVERS (left + right):                                 │   │
    │   │   ┌──────────────┐                                             │   │
    │   │   │ Microswitch   │                                             │   │
    │   │   │ (normally open)│                                            │   │
    │   │   │              │                                             │   │
    │   │   │ Left  ────► Controller Brake L                             │   │
    │   │   │ Right ────► Controller Brake R                             │   │
    │   │   │ VCC (5V) ◄── Controller 5V (pull-up)                      │   │
    │   │   │ GND ──────► Common Ground                                 │   │
    │   │   └──────────────┘                                             │   │
    │   │                                                                │   │
    │   │   SPEED SENSOR (rear wheel):                                   │   │
    │   │   ┌──────────────┐                                             │   │
    │   │   │ Hall sensor   │                                             │   │
    │   │   │ on fork       │                                             │   │
    │   │   │              │                                             │   │
    │   │   │ Signal ────► Controller Speed                              │   │
    │   │   │ VCC (5V) ◄── Controller 5V                                │   │
    │   │   │ GND ──────► Common Ground                                 │   │
    │   │   └──────────────┘                                             │   │
    │   │                                                                │   │
    │   └────────────────────────────────────────────────────────────────┘   │
    │                                                                        │
    │                                                                        │
    │   ┌────────────────────────────────────────────────────────────────┐   │
    │   │                  LIGHTING                                       │   │
    │   │                                                                │   │
    │   │   HEADLIGHT: 1000 lumen, USB rechargeable                      │   │
    │   │   ┌──────────────┐                                             │   │
    │   │   │  Self-contained │                                           │   │
    │   │   │  (no wiring to controller)                                 │   │
    │   │   │  Mounts on handlebar                                       │   │
    │   │   └──────────────┘                                             │   │
    │   │                                                                │   │
    │   │   TAIL LIGHT: Red, flashing, USB rechargeable                  │   │
    │   │   ┌──────────────┐                                             │   │
    │   │   │  Self-contained │                                           │   │
    │   │   │  (no wiring to controller)                                 │   │
    │   │   │  Mounts on seatpost                                        │   │
    │   │   └──────────────┘                                             │   │
    │   │                                                                │   │
    │   └────────────────────────────────────────────────────────────────┘   │
    │                                                                        │
    36V BATTERY (-) ─────┴────────────────────────────────────────────────────┘
                                                                              GND
```

## Component Values Summary

| Component | Value | Rating | Quantity |
|-----------|-------|--------|----------|
| Controller | 36V 15A Brushless | 540W max | 1 |
| Hub Motor | 350W 36V | 9.7A nominal | 1 |
| Hall Sensors | Internal to motor | 3-phase | 3 |
| Cadence Sensor | 12-magnet | Hall effect | 1 |
| Thumb Throttle | 36V | 0-3.3V | 1 |
| Brake Levers | With microswitch | Normally open | 2 |
| Speed Sensor | Hall effect | On fork | 1 |
| LCD Display | 850C | 5-level assist | 1 |
| Charger | 36V 2A LiFePO4 | CC/CV | 1 |
| Fuse | 30A blade | Automotive | 1 |
| Power Switch | 60A rocker | Panel mount | 1 |
