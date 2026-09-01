# PHI_SCOOTER — Electronic Circuit Diagram

## Complete Circuit Schematic

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        PHI-SCOOTER CIRCUIT                               │
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
    │   │              E-SCOOTER CONTROLLER (36V 15A)                │    │
    │   │                                                            │    │
    │   │   ┌──────────────────────────────────────────────────┐    │    │
    │   │   │                                                  │    │    │
    │   │   │  POWER INPUT                                     │    │    │
    │   │   │  B+ ◄──── 36V+ (from fuse)                       │    │    │
    │   │   │  B- ◄──── 36V- (GND)                             │    │    │
    │   │   │                                                  │    │    │
    │   │   │  MOTOR OUTPUT                                    │    │    │
    │   │   │  Phase A ──────► Blue wire ────► Hub Motor       │    │    │
    │   │   │  Phase B ──────► Green wire ───► Hub Motor       │    │    │
    │   │   │  Phase C ──────► Yellow wire ──► Hub Motor       │    │    │
    │   │   │                                                  │    │    │
    │   │   │  HALL SENSORS                                    │    │    │
    │   │   │  H1 ◄──── Red (Hall 1)                           │    │    │
    │   │   │  H2 ◄──── Blue (Hall 2)                          │    │    │
    │   │   │  H3 ◄──── Green (Hall 3)                         │    │    │
    │   │   │  +5V ────► Hall power                            │    │    │
    │   │   │  GND ────► Hall ground                           │    │    │
    │   │   │                                                  │    │    │
    │   │   │  SENSOR INPUTS                                   │    │    │
    │   │   │  ┌─────────────────────────────────────────┐    │    │    │
    │   │   │  │ THROTTLE                                │    │    │    │
    │   │   │  │ Signal ◄── White wire ──── Thumb Throt.  │    │    │    │
    │   │   │  │ +5V   ───► Red wire ────── Thumb Throt.  │    │    │    │
    │   │   │  │ GND   ───► Black wire ──── Thumb Throt.  │    │    │    │
    │   │   │  └─────────────────────────────────────────┘    │    │    │
    │   │   │                                                  │    │    │
    │   │   │  BRAKE CUT-OFFS                                 │    │    │
    │   │   │  ┌─────────────────────────────────────────┐    │    │    │
    │   │   │  │ FRONT BRAKE                             │    │    │    │
    │   │   │  │ Signal ◄── White wire ──── Front Lever   │    │    │    │
    │   │   │  │ +5V   ───► Red wire ────── Front Lever   │    │    │    │
    │   │   │  │ GND   ───► Black wire ──── Front Lever   │    │    │    │
    │   │   │  └─────────────────────────────────────────┘    │    │    │
    │   │   │                                                  │    │    │
    │   │   │  ┌─────────────────────────────────────────┐    │    │    │
    │   │   │  │ REAR BRAKE                              │    │    │    │
    │   │   │  │ Signal ◄── White wire ──── Rear Lever    │    │    │    │
    │   │   │  │ +5V   ───► Red wire ────── Rear Lever    │    │    │    │
    │   │   │  │ GND   ───► Black wire ──── Rear Lever    │    │    │    │
    │   │   │  └─────────────────────────────────────────┘    │    │    │
    │   │   │                                                  │    │    │
    │   │   │  DISPLAY (UART)                                  │    │    │
    │   │   │  TX ────────► Blue wire ────► LED RX            │    │    │
    │   │   │  RX ◄──────── Green wire ──── LED TX            │    │    │
    │   │   │  +5V ───────► Red wire ────── LED VCC           │    │    │
    │   │   │  GND ───────► Black wire ──── LED GND           │    │    │
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
    │   │         │                  ──► Hall sensors                 │   │
    │   │         │                  ──► Throttle                     │   │
    │   │         │                  ──► Brake cut-offs               │   │
    │   │         │                                                  │   │
    │   │         └──► 5V Regulator ──► LED Display                  │   │
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
    │   │   DC Jack 5.5×2.1mm (deck-mounted)                         │   │
    │   │   ┌──────────────┐                                         │   │
    │   │   │ Center: B+   │──► 36V+ (through fuse)                  │   │
    │   │   │ Sleeve: B-   │──► 36V- (GND)                           │   │
    │   │   └──────────────┘                                         │   │
    │   │                                                            │   │
    │   │   42V 2A Li-Ion Charger (external)                          │   │
    │   │   Charge time: 3 hours (0→100%)                             │   │
    │   │   Fast charge: 2 hours (0→80%) with 3A charger             │   │
    │   │                                                            │   │
    │   └────────────────────────────────────────────────────────────┘   │
    │                                                                    │
    BATTERY 36V (-) ─────┴─────────────────────────────────────────────────┘
                                                                  GND
```

## Component Values Summary

| Component | Value | Rating | Quantity |
|-----------|-------|--------|----------|
| Hub Motor | Phi-harmonic, 350W | 36V, 3-phase | 1 |
| Controller | KT-Libraries | 36V, 15A max | 1 |
| Battery | Li-Ion Samsung | 36V, 7.8Ah | 1 |
| Thumb Throttle | Hall effect | 0.8-4.2V | 1 |
| LED Display | Simple 3-mode | UART | 1 |
| Brake Levers | Mechanical | Cut-off switch | 2 |
| Fuse | Blade type | 20A, 36V DC | 1 |
| Charger | Li-Ion | 42V, 2A | 1 |
| XT60 Connector | Yellow | 60A rated | 1 |
| DC Jack | 5.5×2.1mm | Charging port | 1 |
