# PHI_GLIDER — Electronic Circuit Diagram

## Complete Circuit Schematic

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        PHI-GLIDER CIRCUIT                                │
└─────────────────────────────────────────────────────────────────────────┘

    BATTERY 36V (+) ─────┬─────────────────────────────────────────────────┐
                        │                                                  │
                    ┌───┴───┐                                              │
                    │FUSE   │ 20A                                          │
                    │BLADE  │                                              │
                    └───┬───┘                                              │
                        │                                                  │
    36V POWER BUS ──────┤                                                  │
                        │                                                  │
    ┌───────────────────┤                                                  │
    │                   │                                                  │
    │   ┌───────────────┴────────────────────────────────────────────┐    │
    │   │                                                            │    │
    │   │              DUAL MOTOR CONTROLLER (36V 20A)                │    │
    │   │                                                            │    │
    │   │   ┌──────────────────────────────────────────────────┐    │    │
    │   │   │                                                  │    │    │
    │   │   │  POWER INPUT                                     │    │    │
    │   │   │  B+ ◄──── 36V+ (from fuse)                       │    │    │
    │   │   │  B- ◄──── 36V- (GND)                             │    │    │
    │   │   │                                                  │    │    │
    │   │   │  MOTOR 1 OUTPUT (LEFT)                           │    │    │
    │   │   │  Phase A ──────► Blue wire ────► Left Motor      │    │    │
    │   │   │  Phase B ──────► Green wire ───► Left Motor      │    │    │
    │   │   │  Phase C ──────► Yellow wire ──► Left Motor      │    │    │
    │   │   │                                                  │    │    │
    │   │   │  MOTOR 2 OUTPUT (RIGHT)                          │    │    │
    │   │   │  Phase A ──────► Blue wire ────► Right Motor     │    │    │
    │   │   │  Phase B ──────► Green wire ───► Right Motor     │    │    │
    │   │   │  Phase C ──────► Yellow wire ──► Right Motor     │    │    │
    │   │   │                                                  │    │    │
    │   │   │  SENSOR INPUTS                                   │    │    │
    │   │   │  ┌─────────────────────────────────────────┐    │    │    │
    │   │   │  │ THROTTLE (pull-cable potentiometer)      │    │    │    │
    │   │   │  │ Signal ◄── White wire ──── Pot           │    │    │    │
    │   │   │  │ +5V   ───► Red wire ────── Pot           │    │    │    │
    │   │   │  │ GND   ───► Black wire ──── Pot           │    │    │    │
    │   │   │  └─────────────────────────────────────────┘    │    │    │
    │   │   │                                                  │    │    │
    │   │   │  ┌─────────────────────────────────────────┐    │    │    │
    │   │   │  │ KILL SWITCH (magnetic lanyard)           │    │    │    │
    │   │   │  │ Signal ◄── White wire ──── Switch        │    │    │    │
    │   │   │  │ +5V   ───► Red wire ────── Switch        │    │    │    │
    │   │   │  │ GND   ───► Black wire ──── Switch        │    │    │    │
    │   │   │  └─────────────────────────────────────────┘    │    │    │
    │   │   │                                                  │    │    │
    │   │   │  ┌─────────────────────────────────────────┐    │    │    │
    │   │   │  │ BATTERY MONITOR                          │    │    │    │
    │   │   │  │ Voltage ◄── Yellow wire ── Battery      │    │    │    │
    │   │   │  │ +5V   ───► Red wire ────── Monitor      │    │    │    │
    │   │   │  │ GND   ───► Black wire ──── Monitor      │    │    │    │
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
    │   │   36V ──┬──► 5V Regulator ──► Controller logic             │   │
    │   │         │                  ──► Throttle pot                 │   │
    │   │         │                  ──► Kill switch                   │   │
    │   │         │                                                  │   │
    │   │         └──► 12V Regulator ──► Battery monitor             │   │
    │   │                                                            │   │
    │   └────────────────────────────────────────────────────────────┘   │
    │                                                                    │
    │                                                                    │
    │   ┌────────────────────────────────────────────────────────────┐   │
    │   │                  CHARGING CIRCUIT                            │   │
    │   │                                                            │   │
    │   │   XT60 Charging Port (frame-mounted)                        │   │
    │   │   ┌──────────────┐                                         │   │
    │   │   │ Pin 1: B+    │──► 36V+ (through fuse)                  │   │
    │   │   │ Pin 2: B-    │──► 36V- (GND)                           │   │
    │   │   └──────────────┘                                         │   │
    │   │                                                            │   │
    │   │   42V 2A Li-Ion Charger (external)                          │   │
    │   │   Charge time: 2 hours (0→100%)                             │   │
    │   │                                                            │   │
    │   └────────────────────────────────────────────────────────────┘   │
    │                                                                    │
    BATTERY 36V (-) ─────┴─────────────────────────────────────────────────┘
                                                                  GND
```

## Throttle Circuit (Pull-Cable Potentiometer)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    THROTTLE CIRCUIT                                  │
│                                                                     │
│    ┌─────────────────────────────────────────────────────────┐     │
│    │                                                         │     │
│    │    PULL-CABLE MECHANISM                                 │     │
│    │                                                         │     │
│    │    ┌─────────────┐                                      │     │
│    │    │  THROTTLE   │                                      │     │
│    │    │  LEVER      │                                      │     │
│    │    │  (left hand)│                                      │     │
│    │    │             │                                      │     │
│    │    │  Pull to    │                                      │     │
│    │    │  increase   │                                      │     │
│    │    │  power      │                                      │     │
│    │    │             │                                      │     │
│    │    │  ┌───────┐  │                                      │     │
│    │    │  │ POT   │  │                                      │     │
│    │    │  │ 10kΩ  │  │                                      │     │
│    │    │  └───┬───┘  │                                      │     │
│    │    │      │      │                                      │     │
│    │    └──────┼──────┘                                      │     │
│    │           │                                              │     │
│    │           │    POTentiometer Wiring:                     │     │
│    │           │                                              │     │
│    │           │    5V ──┬── R1 (1kΩ) ──┬── Signal ──► Controller│ │
│    │           │        │              │                      │     │
│    │           │        └── POT 10kΩ ──┘                      │     │
│    │           │              │                               │     │
│    │           │              └── GND                          │     │
│    │           │                                              │     │
│    │           │    Output: 0.8V (off) to 4.2V (full)         │     │
│    │           │    Update rate: 50 Hz                        │     │
│    │           │                                              │     │
│    └───────────┼──────────────────────────────────────────────┘     │
│                │                                                    │
│                └──────► TO CONTROLLER (Throttle Input)              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Kill Switch Circuit

```
┌─────────────────────────────────────────────────────────────────────┐
│                    KILL SWITCH CIRCUIT                                │
│                                                                     │
│    ┌─────────────────────────────────────────────────────────┐     │
│    │                                                         │     │
│    │    MAGNETIC LANYARD SWITCH                               │     │
│    │                                                         │     │
│    │    ┌─────────────┐                                      │     │
│    │    │  LANYARD    │                                      │     │
│    │    │  (attached  │                                      │     │
│    │    │   to pilot) │                                      │     │
│    │    │             │                                      │     │
│    │    │  ┌───────┐  │                                      │     │
│    │    │  │MAGNET │  │                                      │     │
│    │    │  │       │  │                                      │     │
│    │    │  └───┬───┘  │                                      │     │
│    │    │      │      │                                      │     │
│    │    │  ┌───┴───┐  │                                      │     │
│    │    │  │REED   │  │                                      │     │
│    │    │  │SWITCH │  │                                      │     │
│    │    │  └───┬───┘  │                                      │     │
│    │    │      │      │                                      │     │
│    │    └──────┼──────┘                                      │     │
│    │           │                                              │     │
│    │           │    Switch Wiring:                             │     │
│    │           │                                              │     │
│    │           │    5V ──┬── REED SWITCH ──┬── Signal ──► Controller│ │
│    │           │        │                  │                  │     │
│    │           │        └── R (10kΩ) ──────┘                  │     │
│    │           │                  │                           │     │
│    │           │                  └── GND                      │     │
│    │           │                                              │     │
│    │           │    Normal: Lanyard attached → Signal HIGH     │     │
│    │           │    Emergency: Lanyard pulled → Signal LOW     │     │
│    │           │    Controller cuts motor immediately          │     │
│    │           │                                              │     │
│    └───────────┼──────────────────────────────────────────────┘     │
│                │                                                    │
│                └──────► TO CONTROLLER (Kill Switch Input)           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Component Values Summary

| Component | Value | Rating | Quantity |
|-----------|-------|--------|----------|
| Left Motor | Phi-harmonic, 200W | 36V, 1000KV | 1 |
| Right Motor | Phi-harmonic, 200W | 36V, 1000KV | 1 |
| Controller | Dual-channel | 36V, 20A total | 1 |
| Battery | Li-Ion Samsung | 36V, 6Ah | 1 |
| Throttle | Pull-cable pot | 10kΩ | 1 |
| Kill Switch | Magnetic lanyard | Reed switch | 1 |
| Battery Monitor | LED bar graph | 36V compatible | 1 |
| Fuse | Blade type | 20A, 36V DC | 1 |
| Charger | Li-Ion | 42V, 2A | 1 |
| XT60 Connector | Yellow | 60A rated | 1 |
| Propellers | 10×6, carbon fiber | - | 4 (2 spare) |
