# PHI SYNTHETIC WINGS — Mechanical Diagram

## Wing Layout (Top View, Deployed)

```
                         WING SPAN: 12m
    |<------------------------------------------------------>|
    
    LEFT WING                                    RIGHT WING
    ==============================================  ==============================================
    
              PHI TAPER (root chord 2.0m, tip chord 1.236m)
              Taper ratio = 1/phi = 0.618
    
    ROOT                                                    ROOT
    (2.0m)                                                  (2.0m)
    +--+                                                  +--+
    |  |                                                  |  |
    |  |    SPAR 1: 15mm carbon (main)                    |  |
    |  |----+---------+---------+---------+--------        |  |
    |  |    |         |         |         |                |  |
    |  |    |  SPAR 2 |  SPAR 3 |  SPAR 4 |                |  |
    |  |    | 10mm CF | 10mm CF | 10mm CF |                |  |
    |  |----+---------+---------+---------+--------        |  |
    |  |                                                  |  |
    |  |    FLAP (trailing edge)                           |  |
    |  |================================================  |  |
    |  |    (hinged, 1/3 chord)                           |  |
    +--+                                                  +--+
    |  |                                                  |  |
    |  |    TIP                                            |  |
    |  |   (1.236m)                                        |  |
    +--+                                                  +--+
    
              68.75° SWEEP (half golden angle)


## Wing Cross-Section (NACA-style)

```
    PHI AIRFOIL PROFILE:
    
    Leading edge
         \
          \    ____________________
           \__/                    \___
            |    PHI LIFT SURFACE     \___
            |    (cambered, 12%)           |
            |                              |
            |______________________________/
           /
          /    FLAP (hinged, 30% chord)
         /
    
    Chord length:
    ROOT:  2000mm (2.0m)
    TIP:   1236mm (1.236m)
    
    Max thickness: 12% chord at 30% chord station


## Spar Layout (Front View)

```
    WING FRONT VIEW (looking at wing tip):
    
    15mm main spar
    +---+
    |   |  <-- 10mm spar 2
    +---+---+
        |   |  <-- 10mm spar 3
        +---+---+
            |   |  <-- 10mm spar 4
            +---+
    
    Spar spacing at PHI intervals:
    Spar 1: 0mm (root)
    Spar 2: 382mm (1/phi^2 * span)
    Spar 3: 618mm (1/phi * span)
    Spar 4: 1000mm (1/phi^3 * span)
    
    Total spars: 5 (1 main + 4 secondary)
    Material: Roll-wrapped carbon fiber
    Connectors: Aluminum step (15mm-to-10mm)


## Flap Mechanism Detail

```
    HINGE POINT:
    +-------------------+
    |   WING SKIN       |
    |   (ripstop nylon) |
    +--------+----------+
             |
    PIANO HINGE (item #13)
    continuous, nylon
    +--------+----------+
             |
    FLAP SECTION (30% chord)
    +--------+----------+
    |                    |
    |   FLAP SURFACE     |
    |   (ripstop nylon)  |
    |                    |
    +--------+----------+
             |
    PUSH ROD (item #11)
    3mm steel, 200mm
    +--------+----------+
             |
    BELLCRANK (item #12)
    aluminum, dual-arm
    +--------+----------+
             |
    SERVO (item #9)
    35kg waterproof
    +--------+----------+
    
    Travel: 0° to 45° deflection
    Rate: 60°/sec


## Wing Fold Mechanism

```
    DEPLOYED:                    FOLDED:
    
    |<--12m-->|                 |
    ===========                 |==|
                               |  |
                               |==|
                               |  |
                               |==|
    
    FOLD JOINT (at 1.2m from root):
    +-------------------+
    |   OUTER WING      |
    +--------+----------+
             |
    HINGE PIN (item #4)
    8mm steel, 200mm
    +--------+----------+
             |
    INNER WING (root)
    +--------+----------+
    
    LOCKING MECHANISM:
    - Spring-loaded pin
    - Pull-ring to release
    - Auto-locks when deployed
    - Manual pull to fold


## Harness & Body Interface

```
    HUMAN FIGURE (front view):
    
         HEAD
          |
    ======|======  <-- SHOULDER STRAP (item #16)
    |     |     |
    |   CHESTRAP |
    |   (item #17)|
    |     |     |
    |     |     |
    |    LEG    |
    |   STRAPS  |
    |  (item#18)|
    |     |     |
    |     |     |
    LEGS  |    LEGS
    
    WING ATTACHMENT:
    +---+     +---+
    | L |     | R |
    | W |     | W |
    | I |     | I |
    | N |     | N |
    | G |     | G |
    +---+     +---+
      |         |
    D-RING   D-RING
    (item#20) (item#20)
      |         |
    CARABINER CARABINER
    (item#19) (item#19)
      |         |
    +-----------+
    |  MAIN     |
    |  HARNESS  |
    |  (item#15)|
    +-----------+


## Propulsion Mount (Rear)

```
    REAR VIEW:
    +---------------------------+
    |                           |
    |   MOTOR MOUNT             |
    |   (item #36)              |
    |   aluminum bracket        |
    |        |                  |
    |   +----+----+             |
    |   |  MOTOR  |             |
    |   |  400W   |             |
    |   |  36V    |             |
    |   | (item#34)|            |
    |   +----+----+             |
    |        |                  |
    |   PROPELLER               |
    |   12x6 folding            |
    |   (item #35)              |
    |   carbon fiber            |
    |                           |
    +---------------------------+
    
    Motor position: rear center
    Thrust axis: aligned with CG
    Folding props reduce drag in glide mode


## Wing Rib Spacers (3D Printed)

```
    PHI PROFILE TEMPLATE:
    (item #7, 24 total)
    
    +--+
    | /|     Each rib defines the airfoil
    |/ |     shape at its spar station.
    |  |     PHI taper means each rib
    |  |     is slightly different.
    |  |
    |  |     Rib heights (mm):
    |  |     Station 1: 240mm (12% of 2.0m)
    |  |     Station 2: 200mm
    +--+     Station 3: 170mm
             Station 4: 148mm (12% of 1.236m)
    
    Material: PLA or PETG
    Layer height: 0.2mm
    Infill: 20%
    Print time: ~3 hours each
```

## Dimensions Summary

```
    WING SPAN:           12m (deployed)
    WING SPAN FOLDED:    1.2m
    ROOT CHORD:          2.0m
    TIP CHORD:           1.236m
    WING AREA:           19.42 m²
    SWEEP ANGLE:         68.75°
    TAPER RATIO:         0.618 (1/phi)
    ASPECT RATIO:        7.41
    
    STRUCTURE WEIGHT:    12 kg (wings + harness)
    BATTERY WEIGHT:      2 kg
    PILOT WEIGHT:        75-90 kg
    TOTAL FLYING WEIGHT: 89-104 kg
    
    STALL SPEED:         6.5 m/s (23.4 km/h)
    CRUISE SPEED:        35 km/h
    MAX SPEED:           90 km/h (dive)
    RANGE:               120 km
    FLIGHT TIME:         4 hours sustained
```
