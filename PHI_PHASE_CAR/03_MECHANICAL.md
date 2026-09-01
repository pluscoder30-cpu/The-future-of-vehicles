# PHI PHASE CAR — Mechanical Diagram

## Top View — Chassis Layout (4500mm x 1800mm)

```
                    FRONT (0mm)
    <--- 2800mm wheelbase --->  <-- 900mm front overhang
    |                           |
    |   [FL COIL]  [COIL]  [FR COIL]     137.5deg apart
    |      90deg    0deg    90deg
    |   /                 \
    |  /   FRONT CRUMPLE    \
    | /      ZONE 600mm      \
    |/                        \
    |  [FR WHEEL]    [FL WHEEL]  <- 19" hubless, airless
    |    |                |        tire, 1500W hub motor
    |    |                |
    |    |   COCKPIT      |     <- Steering rack + yoke
    |    |   [DRIVER]     |        7" touchscreen dash
    |    |   [SEAT]       |        15" OLED dashboard
    |    |                |
    |    |   [CENTER      |     <- Phase button (2-hand)
    |    |    CONSOLE]    |        Contactor key
    |    |                |
    |    |   [PASSENGER]  |     <- Passenger seat
    |    |   [SEAT]       |
    |    |                |
    |    | BATTERY BAY    |     <- FPB-20 (320x220x100mm)
    |    | [FPB-20]       |        144V BMS + DC-DC
    |    | [144V BMS]     |        Emergency reserve
    |    | [DC-DC]        |        Fuse block
    |    |                |
    |    | PHASE COILS    |     <- 2x side coils per side
    |    | [SL] [SR]      |        200mm dia, liquid-cooled
    |    |  275deg 0deg   |
    |    |                |
    |  [RR WHEEL]    [RL WHEEL]  <- 19" hubless, airless
    |    |                |        tire, 1500W hub motor
    |    |                |
    |    |   REAR         |     <- Cargo area 400L
    |    |   CRUMPLE      |
    |    |   ZONE 500mm   |
    |   \                  /
    |    \   REAR COILS   /
    |     [RL COIL][RR COIL][CENTER]
    |      315deg  45deg   222.5deg
    |                          |
    +--------------------------+
                 REAR (4500mm)
```

## Front View

```
              1800mm
    |<------------------------>|
    
    +==========================+   <- Roof (1400mm height)
    |  [SIDE COIL L] [SIDE    |
    |        .         .      |   <- Phase coils in body
    |       / \       / \     |      panels, visible as
    |      /   \     /   \    |      phi-trace patterns
    |     |     |   |     |   |
    |  +--+-----+---+-----+--+|   <- Hood line
    |  |  [FL]     [FR]    |  |   <- Front wheels in wells
    |  |   O         O     |  |     (airless tires)
    |  |    \       /      |  |
    |  +-----\-----/-------+  |
    |         \     /          |
    |          [RACK]          |   <- Steering rack
    |                          |
    |    [FRONT CRUMPLE]       |   <- 600mm impact zone
    |    [ZONE + BUMPER]       |
    +==========================+
           Ground: 150mm
```

## Side View

```
    FRONT                                           REAR
      |<--- 2800mm wheelbase --->|<-- overhang -->|
      |                          |                |
    +-+==========================+================+--+
    |  |  /                     /                 |  |
    |  | / HOOD                / TRUNK            |  |
    |  |/  .----.     .-------.                   |  |
    |  |  |WIND-|     |REAR   |                   |  |
    |  |  |SHIELD|    |WINDOW |                   |  |
    |  |  '----'     '-------'                   |  |
    |  |=========================================|  | <- Roof
    |  |  [DRIVER]    [PASSENGER]                 |  |
    |  |   SEAT          SEAT                    |  |
    |  |=========================================|  | <- Floor
    |  |    |                |                    |  |
    |  +----|----------------|--------------------+  |
    |       |                |                       |
    |     [FL]             [RL]                      |
    |      O                 O                       |
    |     / \               / \                      |
    |    /   \             /   \                     |
    |   [COIL]          [COIL]                       |
    |   [C1,C9]         [C7,C11]                     |
    |                                              |
    |  Ground Clearance: 150mm                    |
    +----------------------------------------------+

    Coil positions (phi-harmonic dodecahedral):
    Front:  C1 (0deg), C9 (90deg), C10 (137.5deg)
    Side-L: C4 (180deg), C5 (225deg)
    Side-R: C6 (0deg), C2 (45deg)
    Rear:   C7 (270deg), C11 (315deg), C12 (222.5deg)
    Top:    C3 (top-center), C8 (bottom-center)
```

## Suspension Geometry

```
    FRONT SUSPENSION (MacPherson Strut)
    =====================================
    
         [COILOVER SHOCK 300mm]
              |
              |
    [ANTI-ROLL BAR 22mm] ----+---- [UPPER BALL JOINT]
              |                      |
              |              [STEERING KNUCKLE]
              |                      |
    [LOWER BALL JOINT] ----+---- [HUB MOTOR]
              |                      |
              [CONTROL ARM]          |
              (lower)           [19" WHEEL]
                                   [TIRE]

    Travel: 80mm
    Damping: Electronically adjustable
    Camber: -0.5 deg (adjustable)
    Toe: 0 deg (adjustable)


    REAR SUSPENSION (Double Wishbone)
    ===================================
    
         [COILOVER SHOCK 300mm]
              |
    [ANTI-ROLL BAR 22mm] ----+
              |               |
    [UPPER ARM]       [LOWER ARM]
         |                |
         [UPPER BALL]  [LOWER BALL]
              |                |
              +----[HUB MOTOR]----+
                        |
                   [19" WHEEL]
                   [TIRE]

    Travel: 80mm
    Camber: -1.0 deg (adjustable)
    Toe: +0.2 deg (fixed)
```

## Steering Mechanism

```
    ELECTRIC POWER STEERING RACK
    =============================
    
    [YOKE STEERING WHEEL]
         |
    [COLLAPSIBLE COLUMN]
         |
    [universal joint]
         |
    [ELECTRIC STEERING RACK]
         |                    |
    [TIE ROD L]          [TIE ROD R]
         |                    |
    [INNER TIE]          [INNER TIE]
         |                    |
    [OUTER TIE]          [OUTER TIE]
         |                    |
    [STEERING KNUCKLE]  [STEERING KNUCKLE]
         |                    |
    [FRONT LEFT WHEEL]  [FRONT RIGHT WHEEL]
    
    Ratio: 12:1
    Turns lock-to-lock: 2.8
    Power assist: 70% (phase mode), 40% (normal)
```

## Wheel Assembly Detail

```
    HUBLESS WHEEL (Front)
    =======================
    
    Outer Rim (19" aluminum)
    +===========================+
    |                           |
    |    [AIRLESS TIRE]         |  <- Honeycomb polymer
    |    (honeycomb structure)  |     No air, no flats
    |                           |
    +---+                   +---+
        |   [INNER RACE]    |
        |  +=============+  |
        |  |  BEARING     |  |  <- Phi-harmonic bearing
        |  |  (ceramic)   |  |     (reduced friction)
        |  +=============+  |
        |                   |
        |   [HUB MOUNT]     |  <- Bolt pattern for motor
        |   (4x M8 bolts)   |
        |                   |
        +-------------------+
    
    HUB MOTOR WHEEL (Rear)
    ========================
    
    Outer Rim (19" aluminum)
    +===========================+
    |                           |
    |    [AIRLESS TIRE]         |
    |                           |
    +---+                   +---+
        |  [MOTOR HOUSING]  |
        |  +=============+  |
        |  | BLDC MOTOR   |  |  <- 1500W hub motor
        |  | (72V, 1500W) |  |     Direct drive, no chain
        |  | [PHASE A]    |  |
        |  | [PHASE B]    |  |
        |  | [PHASE C]    |  |
        |  | [HALL SENS]  |  |
        |  +=============+  |
        |                   |
        |   [HUB MOUNT]     |
        |   (6x M10 bolts)  |
        |                   |
        +-------------------+
```

## Cooling System Layout

```
    DUAL-LOOP COOLING SYSTEM
    ==========================
    
    LOOP 1: PHASE COILS (glycol-water mix)
    =========================================
    [RADIATOR 1] <--FRONT
         |
    [WATER PUMP 1] (12V, 5L/min)
         |
         +--[COIL C1]--[COIL C2]--[COIL C3]--+
         |                                    |
         +--[COIL C4]--[COIL C5]--[COIL C6]--+
         |                                    |
         +--[COIL C7]--[COIL C8]--[COIL C9]--+
         |                                    |
         +--[COIL C10]-[COIL C11]-[COIL C12]-+
         |                                    |
         +--[TEMP SENSOR 1]--[TEMP SENSOR 2]--+
         |                                    |
         +------------------------------------+
         |
    [RETURN TO RADIATOR]
    
    LOOP 2: DRIVE MOTORS (separate loop)
    ========================================
    [RADIATOR 2] <--SIDE
         |
    [WATER PUMP 2] (12V, 3L/min)
         |
    [FL MOTOR]---[FR MOTOR]---[RL MOTOR]---[RR MOTOR]
         |
    [TEMP SENSOR 3]
         |
    [RETURN TO RADIATOR 2]
    
    Cutoff: 90C (thermal relay)
    Max operating: 65C
    Coolant: 50/50 glycol-water
```

## Phase Coil Mounting Detail

```
    COIL MOUNT (Per coil, 12 total)
    ================================
    
    [BODY PANEL]
         |
    [MOUNTING BRACKET] (aluminum L-angle)
         |
         +--[VIBRATION ISOLATOR] (rubber grommet)
         |
    [COIL FORM] (PVC pipe 12" OD)
         |
    [COIL WINDING] (Litz wire, 120 turns)
         |
    [COPPER FOIL SHIELD] (4" wrap, grounded)
         |
    [CAPACITOR BANK] (soldered to coil leads)
         |
    [WATER COOLING CHANNEL] (silicone hose, inline)
         |
    [CONNECTOR TO DRIVER] (XT60 pair)
    
    Mounting: 3x M6 bolts per coil
    Alignment: Phi-angle marked on bracket
    Cooling: Series liquid loop
    Total weight per coil: 1.0 kg
```

## Bolt Torque Specs

| Fastener | Size | Torque | Lock |
|----------|------|--------|------|
| Wheel bolts | M10 x 1.25 | 85 Nm | Blue Loctite |
| Hub motor mount | M10 x 1.25 | 80 Nm | Blue Loctite |
| Suspension upper | M12 x 1.75 | 110 Nm | Nylock nut |
| Suspension lower | M12 x 1.75 | 110 Nm | Nylock nut |
| Coil mount | M6 x 1.0 | 10 Nm | Lock washer |
| Body panel | M5 x 0.8 | 5 Nm | Nylon lock nut |
| Seat mount | M8 x 1.25 | 35 Nm | Nylock nut |
| Steering rack | M10 x 1.5 | 65 Nm | Nylock nut |
| Battery clamp | M8 x 1.25 | 25 Nm | Lock washer |

## Weight Distribution

```
    FRONT: 45% / REAR: 55% (without passengers)
    =============================================
    
    Front axle load: 74 kg (vehicle) + passengers
    Rear axle load: 91 kg (vehicle) + passengers
    
    With 2 front passengers (150 kg total):
    Front: 74 + 100 = 174 kg
    Rear:  91 + 50  = 141 kg
    
    Ground clearance: 150mm all around
    Center of gravity: 450mm above ground
```
