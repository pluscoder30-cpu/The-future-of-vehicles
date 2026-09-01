# PHI_E_BIKE — Electronic Circuit Diagram

## Complete Circuit Schematic

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        PHI-E-BIKE CIRCUIT                                │
└─────────────────────────────────────────────────────────────────────────┘

    BATTERY 48V (+) ─────┬─────────────────────────────────────────────────┐
                        │                                                  │
                    ┌───┴───┐                                              │
                    │FUSE   │ 30A                                          │
                    │BLADE  │                                              │
                    └───┬───┘                                              │
                        │                                                  │
    48V POWER BUS ──────┤                                                  │
                        │                                                  │
    ┌───────────────────┤                                                  │
    │                   │                                                  │
    │   ┌───────────────┴────────────────────────────────────────────┐    │
    │   │                                                            │    │
    │   │              E-BIKE CONTROLLER (48V 22A)                   │    │
    │   │                                                            │    │
    │   │   ┌──────────────────────────────────────────────────┐    │    │
    │   │   │                                                  │    │    │
    │   │   │  POWER INPUT                                     │    │    │
    │   │   │  B+ ◄──── 48V+ (from fuse)                       │    │    │
    │   │   │  B- ◄──── 48V- (GND)                             │    │    │
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
    │   │   │  H4 ◄──── Yellow (Hall 4)                        │    │    │
    │   │   │  H5 ◄──── White (Hall 5)                         │    │    │
    │   │   │  +5V ────► Hall power                            │    │    │
    │   │   │  GND ────► Hall ground                           │    │    │
    │   │   │                                                  │    │    │
    │   │   │  SENSOR INPUTS                                   │    │    │
    │   │   │  ┌─────────────────────────────────────────┐    │    │    │
    │   │   │  │ TORQUE SENSOR                            │    │    │    │
    │   │   │  │ Signal ◄── White wire ──── BB Sensor     │    │    │    │
    │   │   │  │ +5V   ───► Red wire ────── BB Sensor    │    │    │    │
    │   │   │  │ GND   ───► Black wire ──── BB Sensor    │    │    │    │
    │   │   │  └─────────────────────────────────────────┘    │    │    │
    │   │   │                                                  │    │    │
    │   │   │  ┌─────────────────────────────────────────┐    │    │    │
    │   │   │  │ THROTTLE                                │    │    │    │
    │   │   │  │ Signal ◄── White wire ──── Thumb Throt.  │    │    │    │
    │   │   │  │ +5V   ───► Red wire ────── Thumb Throt.  │    │    │    │
    │   │   │  │ GND   ───► Black wire ──── Thumb Throt.  │    │    │    │
    │   │   │  └─────────────────────────────────────────┘    │    │    │
    │   │   │                                                  │    │    │
    │   │   │  BRAKE CUT-OFFS                                 │    │    │
    │   │   │  ┌─────────────────────────────────────────┐    │    │    │
    │   │   │  │ LEFT BRAKE                              │    │    │    │
    │   │   │  │ Signal ◄── White wire ──── Left Lever   │    │    │    │
    │   │   │  │ +5V   ───► Red wire ────── Left Lever   │    │    │    │
    │   │   │  │ GND   ───► Black wire ──── Left Lever   │    │    │    │
    │   │   │  └─────────────────────────────────────────┘    │    │    │
    │   │   │                                                  │    │    │
    │   │   │  ┌─────────────────────────────────────────┐    │    │    │
    │   │   │  │ RIGHT BRAKE                             │    │    │    │
    │   │   │  │ Signal ◄── White wire ──── Right Lever  │    │    │    │
    │   │   │  │ +5V   ───► Red wire ────── Right Lever  │    │    │    │
    │   │   │  │ GND   ───► Black wire ──── Right Lever  │    │    │    │
    │   │   │  └─────────────────────────────────────────┘    │    │    │
    │   │   │                                                  │    │    │
    │   │   │  DISPLAY (UART)                                  │    │    │
    │   │   │  TX ────────► Blue wire ────► LCD RX            │    │    │
    │   │   │  RX ◄──────── Green wire ──── LCD TX            │    │    │
    │   │   │  +5V ───────► Red wire ────── LCD VCC           │    │    │
    │   │   │  GND ───────► Black wire ──── LCD GND           │    │    │
    │   │   │                                                  │    │    │
    │   │   └──────────────────────────────────────────────────┘    │    │
    │   │                                                            │    │
    │   └────────────────────────────────────────────────────────────┘    │
    │                                                                    │
    │                                                                    │
    │   ┌────────────────────────────────────────────────────────────┐   │
    │   │                  POWER REGULATION                           │   │
    │   │                                                            │   │
    │   │   48V ──┬──► 5V Regulator ──► Controller logic             │   │
    │   │         │                  ──► Hall sensors                 │   │
    │   │         │                  ──► Throttle                     │   │
    │   │         │                  ──► Torque sensor                │   │
    │   │         │                  ──► Brake cut-offs               │   │
    │   │         │                                                  │   │
    │   │         └──► 5V Regulator ──► LCD Display                  │   │
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
    │   │   GX16 4-Pin Charging Port (frame-mounted)                  │   │
    │   │   ┌──────────────┐                                         │   │
    │   │   │ Pin 1: B+    │──► 48V+ (through fuse)                  │   │
    │   │   │ Pin 2: B-    │──► 48V- (GND)                           │   │
    │   │   │ Pin 3: NC    │                                          │   │
    │   │   │ Pin 4: NC    │                                          │   │
    │   │   └──────────────┘                                         │   │
    │   │                                                            │   │
    │   │   48V 2A Li-Ion Charger (external)                          │   │
    │   │   Charge time: 3 hours (0→100%)                             │   │
    │   │   Fast charge: 2 hours (0→80%) with 3A charger             │   │
    │   │                                                            │   │
    │   └────────────────────────────────────────────────────────────┘   │
    │                                                                    │
    │                                                                    │
    │   ┌────────────────────────────────────────────────────────────┐   │
    │   │                  PHI-HARMONIC MOTOR CONTROL                  │   │
    │   │                                                            │   │
    │   │   The controller uses Field-Oriented Control (FOC)         │   │
    │   │   to drive the phi-harmonic motor:                          │   │
    │   │                                                            │   │
    │   │   ┌──────────────────────────────────────────────────┐    │   │
    │   │   │                                                  │    │   │
    │   │   │  Torque Sensor ──► PID ──► Current Controller     │    │   │
    │   │   │       │                     │                     │    │   │
    │   │   │       │                     ▼                     │    │   │
    │   │   │       │              ┌──────────────┐             │    │   │
    │   │   │       │              │ 3-Phase PWM  │             │    │   │
    │   │   │       │              │ Inverter     │             │    │   │
    │   │   │       │              └──────┬───────┘             │    │   │
    │   │   │       │                     │                     │    │   │
    │   │   │       │                     ▼                     │    │   │
    │   │   │       │              ┌──────────────┐             │    │   │
    │   │   │       │              │ Phi-Harmonic │             │    │   │
    │   │   │       └─────────────►│ Hub Motor    │             │    │   │
    │   │   │                      │ (FOC-driven) │             │    │   │
    │   │   │                      └──────────────┘             │    │   │
    │   │   │                                                   │    │   │
    │   │   │  Hall Sensors ──► Commutation ──► Phase Timing     │    │   │
    │   │   │                                                   │    │   │
    │   │   └──────────────────────────────────────────────────┘    │   │
    │   │                                                            │   │
    │   │   PWM Frequency: 20 kHz                                    │   │
    │   │   Control Loop: 1 kHz                                      │   │
    │   │   Current Limit: 22A (adjustable)                          │   │
    │   │                                                            │   │
    │   └────────────────────────────────────────────────────────────┘   │
    │                                                                    │
    BATTERY 48V (-) ─────┴─────────────────────────────────────────────────┘
                                                                  GND
```

## Torque Sensor Circuit

```
┌─────────────────────────────────────────────────────────────────────┐
│                    TORQUE SENSOR CIRCUIT                              │
│                    (Bottom Bracket Type)                             │
│                                                                     │
│    ┌─────────────────────────────────────────────────────────┐     │
│    │                                                         │     │
│    │    PEDALS                                               │     │
│    │    ┌─────┐                                             │     │
│    │    │ LEFT│                                             │     │
│    │    │CRANK│                                             │     │
│    │    └──┬──┘                                             │     │
│    │       │                                                │     │
│    │    ┌──┴──┐                                             │     │
│    │    │     │    TORQUE SENSOR                            │     │
│    │    │  ┌──┴─────────────────────┐                       │     │
│    │    │  │  ┌─────────────────┐   │                       │     │
│    │    │  │  │   12× Magnets   │   │                       │     │
│    │    │  │  │   (on spindle)  │   │                       │     │
│    │    │  │  │                 │   │                       │     │
│    │    │  │  │  ○ ○ ○ ○ ○ ○  │   │                       │     │
│    │    │  │  │  ○ ○ ○ ○ ○ ○  │   │                       │     │
│    │    │  │  │                 │   │                       │     │
│    │    │  │  └─────────────────┘   │                       │     │
│    │    │  │                        │                       │     │
│    │    │  │  ┌─────────────────┐   │                       │     │
│    │    │  │  │   Hall Array    │   │                       │     │
│    │    │  │  │   (3× A3144)    │   │                       │     │
│    │    │  │  │                 │   │                       │     │
│    │    │  │  │  H1 H2 H3       │   │                       │     │
│    │    │  │  │  │  │  │        │   │                       │     │
│    │    │  │  └──┼──┼──┼────────┘   │                       │     │
│    │    │  │     │  │  │            │                       │     │
│    │    │  └─────┼──┼──┼────────────┘                       │     │
│    │    │        │  │  │                                    │     │
│    │    └────────┼──┼──┼────────────                        │     │
│    │             │  │  │                                    │     │
│    │             │  │  │    Signal Processing               │     │
│    │             │  │  │    ┌─────────────────────────┐     │     │
│    │             │  │  │    │                         │     │     │
│    │             │  │  │    │  H1 ──┐                 │     │     │
│    │             │  │  │    │  H2 ──┼──► XOR Gate     │     │     │
│    │             │  │  │    │  H3 ──┘    │            │     │     │
│    │             │  │  │    │            ▼            │     │     │
│    │             │  │  │    │     ┌──────────┐       │     │     │
│    │             │  │  │    │     │ Frequency│       │     │     │
│    │             │  │  │    │     │ Counter  │       │     │     │
│    │             │  │  │    │     └────┬─────┘       │     │     │
│    │             │  │  │    │          │             │     │     │
│    │             │  │  │    │          ▼             │     │     │
│    │             │  │  │    │   ┌──────────────┐    │     │     │
│    │             │  │  │    │   │  Torque      │    │     │     │
│    │             │  │  │    │   │  Signal Out  │    │     │     │
│    │             │  │  │    │   │  (analog)    │    │     │     │
│    │             │  │  │    │   └──────┬───────┘    │     │     │
│    │             │  │  │    │          │             │     │     │
│    │             │  │  │    └──────────┼─────────────┘     │     │
│    │             │  │  │               │                   │     │
│    │             │  │  │               ▼                   │     │
│    │             │  │  │          TO CONTROLLER            │     │
│    │             │  │  │          (Torque Input)           │     │
│    │             │  │  │                                   │     │
│    │             │  │  │    ┌─────────────────────────┐   │     │
│    │             │  │  │    │   POWER                  │   │     │
│    │             │  │  │    │   +5V ──► Sensor VCC     │   │     │
│    │             │  │  │    │   GND ──► Sensor GND     │   │     │
│    │             │  │  │    └─────────────────────────┘   │     │
│    │             │  │  │                                   │     │
│    │             │  │  └───────────────────────────────────┘     │
│    │             │  │                                            │
│    │             │  │    Output: 0.5V - 4.5V                     │     │
│    │             │  │    0.5V = no pedal force                    │     │
│    │             │  │    4.5V = maximum pedal force               │     │
│    │             │  │    Update rate: 100 Hz                       │     │
│    │             │  │                                              │     │
│    │             │  └──────────────────────────────────────────────┘     │
│    │             │                                                      │
│    │             └──────► BOTTOM BRACKET SHELL                          │
│    │                        (threaded into frame)                       │
│    │                                                                    │
│    └────────────────────────────────────────────────────────────────────┘     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Component Values Summary

| Component | Value | Rating | Quantity |
|-----------|-------|--------|----------|
| Hub Motor | Phi-harmonic, 500W | 48V, 3-phase | 1 |
| Controller | KT-Libraries | 48V, 22A max | 1 |
| Battery | Li-Ion Samsung 35E | 48V, 10.4Ah | 1 |
| Torque Sensor | BB type | 0.5-4.5V output | 1 |
| LCD Display | KT-LCD3 | UART, waterproof | 1 |
| Thumb Throttle | Hall effect | 0.8-4.2V | 1 |
| Brake Levers | Mechanical | Cut-off switch | 2 |
| Fuse | Blade type | 30A, 48V DC | 1 |
| Charger | Li-Ion | 54.6V, 2A | 1 |
| XT60 Connector | Yellow | 60A rated | 1 |
| GX16 Connector | 4-pin aviation | Charging port | 1 |
