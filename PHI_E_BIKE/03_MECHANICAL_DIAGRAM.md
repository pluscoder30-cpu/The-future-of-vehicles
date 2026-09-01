# PHI_E_BIKE — Mechanical Assembly Diagram

## Side View — Complete Bike with Motor

```
                    HANDLEBAR
                       │
                    ┌──┴──┐
                    │  │  │
                    │  │  │  LCD Display (top)
                    │  │  │
              ┌─────┘  │  └─────┐
              │         │        │
              │    ┌────┴────┐   │
              │    │  STEM   │   │
              │    └────┬────┘   │
              │         │        │
         ┌────┴────┐    │    ┌───┴─────┐
         │  FRONT  │    │    │ REAR    │
         │  WHEEL  │    │    │ WHEEL   │
         │  26"    │    │    │ 26"     │
         │         │    │    │ +MOTOR  │
         │    ○    │    │    │   ○     │
         │   /|\   │    │    │  /|\    │
         │   / \   │    │    │  / \    │
         └────┬────┘    │    └───┬─────┘
              │         │        │
              │    ┌────┴────┐   │
              │    │  FRAME  │   │
              │    │ (triangle)│  │
              │    │         │   │
              │    │ ┌─────┐ │   │
              │    │ │BATT.│ │   │
              │    │ │PACK │ │   │
              │    │ │48V  │ │   │
              │    │ │10.4Ah│ │   │
              │    │ └─────┘ │   │
              │    │         │   │
              │    └────┬────┘   │
              │         │        │
              │    ┌────┴────┐   │
              │    │CRANKSET │   │
              │    │ +TORQUE │   │
              │    │ SENSOR  │   │
              │    └────┬────┘   │
              │         │        │
              │    ┌────┴────┐   │
              │    │ BOTTOM  │   │
              │    │ BRACKET │   │
              │    └─────────┘   │
              │                  │
              │    CONTROLLER    │
              │    (under seat)  │
              │    ┌───────┐     │
              │    │  ╔═╗  │     │
              │    │  ║ ║  │     │
              │    │  ╚═╝  │     │
              │    └───┬───┘     │
              │        │         │
              └────────┴─────────┘
                       
                       SEAT
```

## Rear Hub Motor Detail

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PHI-HARMONIC REAR HUB MOTOR                       │
│                    Cross-Section View                                │
│                                                                     │
│    ┌─────────────────────────────────────────────────────────┐     │
│    │                                                         │     │
│    │                    AXLE (M12)                           │     │
│    │              ┌───────────────────┐                     │     │
│    │              │                   │                     │     │
│    │              │                   │                     │     │
│    │    ┌─────────┴───────────────────┴─────────┐           │     │
│    │    │            OUTER RIM                   │           │     │
│    │    │     ┌─────────────────────────┐       │           │     │
│    │    │     │    SPOKE HOLES (36)     │       │           │     │
│    │    │     │    ┌───────────────┐    │       │           │     │
│    │    │     │    │               │    │       │           │     │
│    │    │     │    │   ROTOR       │    │       │           │     │
│    │    │     │    │   (magnets)   │    │       │           │     │
│    │    │     │    │               │    │       │           │     │
│    │    │     │    │  ┌─────────┐  │    │       │           │     │
│    │    │     │    │  │ STATOR  │  │    │       │           │     │
│    │    │     │    │  │ (coils) │  │    │       │           │     │
│    │    │     │    │  │         │  │    │       │           │     │
│    │    │     │    │  │  ○ ○ ○  │  │    │       │           │     │
│    │    │     │    │  │  ○ ○ ○  │  │    │       │           │     │
│    │    │     │    │  │  ○ ○ ○  │  │    │       │           │     │
│    │    │     │    │  │         │  │    │       │           │     │
│    │    │     │    │  └─────────┘  │    │       │           │     │
│    │    │     │    │               │    │       │           │     │
│    │    │     │    └───────────────┘    │       │           │     │
│    │    │     │                         │       │           │     │
│    │    │     └─────────────────────────┘       │           │     │
│    │    │                                       │           │     │
│    │    └───────────────────────────────────────┘           │     │
│    │                                                         │     │
│    │    WIRE LEADS (10-wire cable)                           │     │
│    │    │ │ │ │ │ │ │ │ │ │                                   │     │
│    │    A B C H1 H2 H3 H4 H5 +5V GND                       │     │
│    │                                                         │     │
│    └─────────────────────────────────────────────────────────┘     │
│                                                                     │
│    Specifications:                                                  │
│    - Outer diameter: 220mm                                          │
│    - Width: 100mm                                                   │
│    - Weight: 2.8 kg                                                 │
│    - Magnets: 12× N48 neodymium, phi-harmonic arrangement          │
│    - Coils: 9× copper windings, 3-phase                             │
│    - Hall sensors: 5× A3144                                         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Torque Sensor Installation

```
┌─────────────────────────────────────────────────────────────────────┐
│                    BOTTOM BRACKET TORQUE SENSOR                      │
│                                                                     │
│    BEFORE (standard bottom bracket):                                │
│                                                                     │
│    ┌─────────────┐     ┌─────────────┐                             │
│    │   LEFT      │     │   RIGHT     │                             │
│    │   CRANK     │     │   CRANK     │                             │
│    │             │     │             │                             │
│    └──────┬──────┘     └──────┬──────┘                             │
│           │                   │                                      │
│    ┌──────┴───────────────────┴──────┐                             │
│    │         BOTTOM BRACKET          │                             │
│    │         (square taper)          │                             │
│    └─────────────────────────────────┘                             │
│                                                                     │
│                                                                     │
│    AFTER (with torque sensor):                                      │
│                                                                     │
│    ┌─────────────┐     ┌─────────────┐                             │
│    │   LEFT      │     │   RIGHT     │                             │
│    │   CRANK     │     │   CRANK     │                             │
│    │             │     │             │                             │
│    └──────┬──────┘     └──────┬──────┘                             │
│           │                   │                                      │
│    ┌──────┴───────────────────┴──────┐                             │
│    │      TORQUE SENSOR BB           │                             │
│    │      ┌─────────────────┐        │                             │
│    │      │ 12 magnets      │        │                             │
│    │      │ Hall array      │        │                             │
│    │      │ Signal output ──┼────────┼──► To Controller            │
│    │      └─────────────────┘        │                             │
│    └─────────────────────────────────┘                             │
│                                                                     │
│    Installation:                                                    │
│    1. Remove old bottom bracket                                     │
│    2. Clean BB shell threads                                        │
│    3. Apply grease to torque sensor threads                         │
│    4. Thread sensor into BB shell (reverse thread on left)          │
│    5. Tighten to 35-40 Nm                                           │
│    6. Connect signal wire to controller                             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Controller Mounting

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CONTROLLER MOUNTING (under seat)                   │
│                                                                     │
│    ┌─────────────────────────────────────────────────────────┐     │
│    │                                                         │     │
│    │                    SEAT POST                             │     │
│    │                        │                                │     │
│    │                   ┌────┴────┐                           │     │
│    │                   │  SEAT   │                           │     │
│    │                   └────┬────┘                           │     │
│    │                        │                                │     │
│    │    ┌───────────────────┼───────────────────┐            │     │
│    │    │                   │                   │            │     │
│    │    │         ┌─────────┴─────────┐         │            │     │
│    │    │         │                   │         │            │     │
│    │    │         │    CONTROLLER     │         │            │     │
│    │    │         │    (in aluminum   │         │            │     │
│    │    │         │     heat-sink     │         │            │     │
│    │    │         │     enclosure)    │         │            │     │
│    │    │         │                   │         │            │     │
│    │    │         │  ┌─────────────┐  │         │            │     │
│    │    │         │  │ BATTERY IN  │  │         │            │     │
│    │    │         │  │ MOTOR OUT   │  │         │            │     │
│    │    │         │  │ SENSOR IN   │  │         │            │     │
│    │    │         │  │ DISPLAY OUT │  │         │            │     │
│    │    │         │  └─────────────┘  │         │            │     │
│    │    │         │                   │         │            │     │
│    │    │         └───────────────────┘         │            │     │
│    │    │                                       │            │     │
│    │    │    MOUNT: 2× stainless steel hose     │            │     │
│    │    │    clamps through seat post holes      │            │     │
│    │    │                                       │            │     │
│    │    └───────────────────────────────────────┘            │     │
│    │                                                         │     │
│    └─────────────────────────────────────────────────────────┘     │
│                                                                     │
│    Wire routing:                                                    │
│    - Battery wire runs down seat tube to controller                 │
│    - Motor wire runs along chainstay to controller                  │
│    - Display wire runs along top tube to handlebar                  │
│    - Throttle wire runs along top tube to handlebar                 │
│    - Brake wires run along top tube to handlebar                    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Battery Mounting

```
┌─────────────────────────────────────────────────────────────────────┐
│                    BATTERY MOUNTING (triangle frame)                  │
│                                                                     │
│    ┌─────────────────────────────────────────────────────────┐     │
│    │                                                         │     │
│    │                    TOP TUBE                              │     │
│    │    ═══════════════════════════════════════════════       │     │
│    │                   ╱                 ╲                    │     │
│    │                  ╱                   ╲                   │     │
│    │                 ╱    ┌─────────────┐   ╲                  │     │
│    │                ╱     │             │    ╲                 │     │
│    │               ╱      │   BATTERY   │     ╲                │     │
│    │              ╱       │   PACK      │      ╲               │     │
│    │             ╱        │   48V       │       ╲              │     │
│    │            ╱         │   10.4Ah    │        ╲             │     │
│    │           ╱          │             │         ╲            │     │
│    │          ╱           │  (triangle  │          ╲           │     │
│    │         ╱            │   shape)    │           ╲          │     │
│    │        ╱             │             │            ╲         │     │
│    │       ╱              └─────────────┘             ╲        │     │
│    │      ╱                                           ╲       │     │
│    │     ╱                     │                       ╲      │     │
│    │    ╱                      │                        ╲     │     │
│    │   ╱                       │                         ╲    │     │
│    │  ╱                        │                          ╲   │     │
│    │ ╱         DOWN TUBE       │       SEAT STAY           ╲  │     │
│    │╱═══════════════════════════╧══════════════════════════╲ │     │
│    │                                                         │     │
│    │    MOUNTING:                                            │     │
│    │    1. Aluminum bracket (included with battery)          │     │
│    │    2. 4× M5 bolts through bracket into frame           │     │
│    │    3. Rubber垫片 between bracket and frame              │     │
│    │    4. Velcro straps for secondary security              │     │
│    │    5. Bungee cords for vibration dampening              │     │
│    │                                                         │     │
│    └─────────────────────────────────────────────────────────┘     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Frame Measurements

```
┌─────────────────────────────────────────────────────────────────────┐
│                    FRAME DIMENSIONS (standard 26" MTB)               │
│                                                                     │
│                    ┌──────────────────────────────┐                │
│                    │         TOP TUBE             │                │
│                    │      (horizontal)            │                │
│                    │         580mm                │                │
│                    └──────────┬───────────────────┘                │
│                               │                                     │
│          ┌────────────────────┼────────────────────┐                │
│          │                    │                    │                │
│     ┌────┴────┐          ┌────┴────┐          ┌────┴────┐          │
│     │ HEAD    │          │ SEAT    │          │ BOTTOM  │          │
│     │ TUBE    │          │ TUBE    │          │ BRACKET │          │
│     │ 150mm   │          │ 480mm   │          │ (width  │          │
│     │         │          │         │          │  68mm)  │          │
│     └────┬────┘          └────┬────┘          └────┬────┘          │
│          │                    │                    │                │
│          │                    │                    │                │
│     ┌────┴────┐          ┌────┴────┐          ┌────┴────┐          │
│     │ CHAIN   │          │ SEAT    │          │ CHAIN   │          │
│     │ STAY    │          │ STAY    │          │ STAY    │          │
│     │ 420mm   │          │ 420mm   │          │ 420mm   │          │
│     │ (left)  │          │         │          │ (right) │          │
│     └────┬────┘          └────┬────┘          └────┬────┘          │
│          │                    │                    │                │
│     ┌────┴────┐          ┌────┴────┐          ┌────┴────┐          │
│     │ REAR    │          │ SEAT    │          │ REAR    │          │
│     │ DROPOUT │          │ POST    │          │ DROPOUT │          │
│     │ (left)  │          │         │          │ (right) │          │
│     │ M10     │          │ 27.2mm  │          │ M12     │          │
│     │ axle    │          │         │          │ motor   │          │
│     └─────────┘          └─────────┘          │ axle    │          │
│                                               └─────────┘          │
│                                                                     │
│    Wheelbase: 1080mm                                                │
│    Standover height: 760mm (size M)                                 │
│    Stack: 600mm                                                     │
│    Reach: 420mm                                                     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```
