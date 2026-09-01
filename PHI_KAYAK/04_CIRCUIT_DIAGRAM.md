# PHI_KAYAK — Electronic Circuit Diagram

## Complete Circuit Schematic

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        PHI-KAYAK CIRCUIT                                 │
└─────────────────────────────────────────────────────────────────────────┘

    BATTERY 24V (+) ─────┬─────────────────────────────────────────────────┐
                        │                                                  │
                    ┌───┴───┐                                              │
                    │FUSE   │ 15A                                          │
                    │BLADE  │                                              │
                    └───┬───┘                                              │
                        │                                                  │
    24V POWER BUS ──────┤                                                  │
                        │                                                  │
    ┌───────────────────┤                                                  │
    │                   │                                                  │
    │   ┌───────────────┴────────────────────────────────────────────┐    │
    │   │                                                            │    │
    │   │              MOTOR CONTROLLER (24V 15A, waterproof)        │    │
    │   │                                                            │    │
    │   │   ┌──────────────────────────────────────────────────┐    │    │
    │   │   │                                                  │    │    │
    │   │   │  POWER INPUT                                     │    │    │
    │   │   │  B+ ◄──── 24V+ (from fuse)                       │    │    │
    │   │   │  B- ◄──── 24V- (GND)                             │    │    │
    │   │   │                                                  │    │    │
    │   │   │  MOTOR OUTPUT                                    │    │    │
    │   │   │  Phase A ──────► Blue wire ────► Water Jet       │    │    │
    │   │   │  Phase B ──────► Green wire ───► Water Jet       │    │    │
    │   │   │  Phase C ──────► Yellow wire ──► Water Jet       │    │    │
    │   │   │                                                  │    │    │
    │   │   │  SENSOR INPUTS                                   │    │    │
    │   │   │  ┌─────────────────────────────────────────┐    │    │    │
    │   │   │  │ THROTTLE (thumb, waterproof)              │    │    │    │
    │   │   │  │ Signal ◄── White wire ──── Throttle       │    │    │    │
    │   │   │  │ +5V   ───► Red wire ────── Throttle       │    │    │    │
    │   │   │  │ GND   ───► Black wire ──── Throttle       │    │    │    │
    │   │   │  └─────────────────────────────────────────┘    │    │    │
    │   │   │                                                  │    │    │
    │   │   │  ┌─────────────────────────────────────────┐    │    │    │
    │   │   │  │ PADDLE SWITCH (magnetic reed)            │    │    │    │
    │   │   │  │ Signal ◄── White wire ──── Reed Switch   │    │    │    │
    │   │   │  │ +5V   ───► Red wire ────── Reed Switch   │    │    │    │
    │   │   │  │ GND   ───► Black wire ──── Reed Switch   │    │    │    │
    │   │   │  └─────────────────────────────────────────┘    │    │    │
    │   │   │                                                  │    │    │
    │   │   │  OUTPUTS                                         │    │    │
    │   │   │  ┌─────────────────────────────────────────┐    │    │    │
    │   │   │  │ LED INDICATOR (3-color)                   │    │    │    │
    │   │   │  │ Green ◄── Green wire ──► LED              │    │    │    │
    │   │   │  │ Yellow ◄── Yellow wire ──► LED            │    │    │    │
    │   │   │  │ Red    ◄── Red wire ────► LED             │    │    │    │
    │   │   │  │ GND    ◄── Black wire ──► LED             │    │    │    │
    │   │   │  └─────────────────────────────────────────┘    │    │    │
    │   │   │                                                  │    │    │
    │   │   └──────────────────────────────────────────────────┘    │    │
    │   │                                                            │    │
    │   └────────────────────────────────────────────────────────────┘    │
    │                                                                    │
    │                                                                    │
    │   ┌────────────────────────────────────────────────────────────┐   │
    │   │                  POWER REGULATION                           │   │
    │   │                                                            │   │
    │   │   24V ──┬──► 5V Regulator ──► Controller logic             │   │
    │   │         │                  ──► Throttle pot                 │   │
    │   │         │                  ──► Paddle switch                │   │
    │   │         │                  ──► LED indicator                │   │
    │   │                                                            │   │
    │   │   Note: Controller has built-in voltage regulation          │   │
    │   │         No external regulators needed                       │   │
    │   │                                                            │   │
    │   └────────────────────────────────────────────────────────────┘   │
    │                                                                    │
    │                                                                    │
    │   ┌────────────────────────────────────────────────────────────┐   │
    │   │                  CHARGING CIRCUIT                            │   │
    │   │                                                            │   │
    │   │   XT60 Charging Port (stern compartment)                    │   │
    │   │   ┌──────────────┐                                         │   │
    │   │   │ Pin 1: B+    │──► 24V+ (through fuse)                  │   │
    │   │   │ Pin 2: B-    │──► 24V- (GND)                           │   │
    │   │   └──────────────┘                                         │   │
    │   │                                                            │   │
    │   │   29.2V 3A LiFePO4 Charger (external)                      │   │
    │   │   Charge time: 2.5 hours (0→100%)                           │   │
    │   │                                                            │   │
    │   └────────────────────────────────────────────────────────────┘   │
    │                                                                    │
    BATTERY 24V (-) ─────┴─────────────────────────────────────────────────┘
                                                                  GND
```

## Paddle Switch Circuit

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PADDLE SWITCH CIRCUIT                              │
│                                                                     │
│    ┌─────────────────────────────────────────────────────────┐     │
│    │                                                         │     │
│    │    PADDLE HOLDER (in cockpit)                            │     │
│    │    ┌─────────────────────────────────────────────┐     │     │
│    │    │                                             │     │     │
│    │    │  ┌───────────┐                              │     │     │
│    │    │  │  MAGNETIC │                              │     │     │
│    │    │  │  REED     │                              │     │     │
│    │    │  │  SWITCH   │                              │     │     │
│    │    │  └─────┬─────┘                              │     │     │
│    │    │        │                                    │     │     │
│    │    └────────┼────────────────────────────────────┘     │     │
│    │             │                                          │     │
│    │             │    Switch Wiring:                         │     │
│    │             │                                          │     │
│    │             │    5V ──┬── REED SWITCH ──┬── Signal ──► Controller│ │
│    │             │        │                  │              │     │
│    │             │        └── R (10kΩ) ──────┘              │     │
│    │             │                  │                       │     │
│    │             │                  └── GND                  │     │
│    │             │                                          │     │
│    │             │    Normal: Paddle inserted → Signal HIGH  │     │
│    │             │    Emergency: Paddle removed → Signal LOW │     │
│    │             │    Controller cuts motor immediately      │     │
│    │             │                                          │     │
│    │             │    SAFETY FEATURE:                        │     │
│    │             │    If paddle is lost overboard,           │     │
│    │             │    motor stops automatically.             │     │
│    │             │    Prevents runaway kayak.                │     │
│    │             │                                          │     │
│    └─────────────┼──────────────────────────────────────────┘     │
│                  │                                                │
│                  └──────► TO CONTROLLER (Paddle Switch Input)     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## LED Indicator Circuit

```
┌─────────────────────────────────────────────────────────────────────┐
│                    LED INDICATOR CIRCUIT                              │
│                                                                     │
│    ┌─────────────────────────────────────────────────────────┐     │
│    │                                                         │     │
│    │    3-COLOR LED INDICATOR (waterproof)                    │     │
│    │                                                         │     │
│    │    ┌─────────────────────────────────────────────┐     │     │
│    │    │                                             │     │     │
│    │    │  ┌───────────┐  ┌───────────┐  ┌───────────┐│     │     │
│    │    │  │  GREEN    │  │  YELLOW   │  │  RED      ││     │     │
│    │    │  │  LED      │  │  LED      │  │  LED      ││     │     │
│    │    │  └─────┬─────┘  └─────┬─────┘  └─────┬─────┘│     │     │
│    │    │        │              │              │      │     │     │
│    │    │        └──────┬───────┴──────┬───────┘      │     │     │
│    │    │               │              │              │     │     │
│    │    └───────────────┼──────────────┼──────────────┘     │     │
│    │                    │              │                     │     │
│    │                    │              │                     │     │
│    │    LED Wiring:      │              │                     │     │
│    │                                                         │     │
│    │    Controller Green ◄── Green wire ──┐                  │     │
│    │    Controller Yellow ◄── Yellow wire ─┼──► Common Anode  │     │
│    │    Controller Red    ◄── Red wire ────┤                  │     │
│    │    GND               ◄── Black wire ──┘                  │     │
│    │                                                         │     │
│    │    LED States:                                           │     │
│    │                                                         │     │
│    │    GREEN:    Battery > 50% — Full power available       │     │
│    │    YELLOW:   Battery 20-50% — Reduced power available   │     │
│    │    RED:      Battery < 20% — Low battery warning        │     │
│    │    FLASHING: Motor fault — Check connections            │     │
│    │    OFF:      Motor disabled — Insert paddle             │     │
│    │                                                         │     │
│    └─────────────────────────────────────────────────────────┘     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Component Values Summary

| Component | Value | Rating | Quantity |
|-----------|-------|--------|----------|
| Motor | Phi-harmonic, 200W | 24V, 800KV | 1 |
| Controller | Waterproof | 24V, 15A max | 1 |
| Battery | LiFePO4, sealed | 24V, 10Ah | 1 |
| Thumb Throttle | Waterproof | 0.8-4.2V | 1 |
| Paddle Switch | Magnetic reed | IP67 | 1 |
| LED Indicator | 3-color, waterproof | - | 1 |
| Fuse | Blade type | 15A, 24V DC | 1 |
| Charger | LiFePO4 | 29.2V, 3A | 1 |
| XT60 Connector | Yellow | 60A rated | 1 |
| Impeller | 5-blade, ABS | phi-harmonic | 1 |
| Jet Housing | ABS pipe | 50mm diameter | 1 |
| Through-Hull Fittings | ABS | 50mm | 2 |
