# PHI PHASE MOTORCYCLE — Mechanical Diagram

## Top View — Frame Layout (2100mm x 750mm)

```
                    FRONT (0mm)
    <--- 1450mm wheelbase --->  <-- 350mm front overhang
    |                           |
    |   [C1] [C2] [C3]          <- 3x front phase coils
    |    0deg  137.5  90deg       (in headlight housing)
    |   /              \
    |  /   FRONT END     \
    | /    [HEADLIGHT]    \
    |/     [LED 7"]        \
    |                       |
    |  [FR WHEEL]           <- 17" hubless, airless tire
    |    |                   |
    |    |                   |
    |    |  [FRONT FORK]     <- Inverted, 43mm, 120mm travel
    |    |  [TRIPLE CLAMP]   |
    |    |                   |
    |    |  [HANDLEBARS]     <- 720mm wide, 7/8"
    |    |  [GRIPS]          |   Twist throttle (R)
    |    |  [BRAKE LEVERS]   |   Phase button (L)
    |    |  [MIRROR L] [M.R] |   OLED display (center)
    |    |                   |
    |    |  [FRAME MAIN]     <- Chromoly monocoque
    |    |  [TANK AREA]      |
    |    |  [96V BATTERY]    <- FPB-10 (240x160x80mm)
    |    |  [BMS]            |   DC-DC converters
    |    |  [FUSE BLOCK]     |   Fuse block
    |    |                   |
    |    |  [RIDER SEAT]     <- 780mm seat height
    |    |  [HARNESS MOUNTS] |   4-point harness
    |    |                   |
    |    |  [COOLANT RADIATOR] <- Side-mounted
    |    |  [WATER PUMP]       |
    |    |                   |
    |    |  [SWINGARM]       <- Aluminum, pivot point
    |    |       |           |
    |    |  [REAR SHOCK]     <- Monoshock, 300mm
    |    |       |           |
    |    |  [RR WHEEL]       <- 17" hubless, hub motor
    |    |    |              |   1500W BLDC
    |    |    |              |
    |   [C4] [C5] [C6]      <- 3x rear phase coils
    |    180  275   45deg      (in taillight housing)
    |    |                   |
    |   [TAIL SECTION]       <- LED taillight
    |   [FRAME ENDS]         |
    |                        |
    +------------------------+
                 REAR (2100mm)
```

## Side View

```
    FRONT                                           REAR
      |<--- 1450mm wheelbase --->|<-- overhang -->|
      |                          |                |
    +-+==========================+================+--+
    |  |  /                     /                 |  |
    |  | / WINDSHIELD          / TAIL              |  |
    |  |/  (polycarbonate)    /                    |  |
    |  |  .----.             /                     |  |
    |  |  |HEAD-|        .--'                      |  |
    |  |  |LIGHT|        |SEAT|                    |  |
    |  |  '----'         '----'                    |  |
    |  |=========================================|  | <- Frame top
    |  |  [RIDER]                              |  |
    |  |   SEAT (780mm)                        |  |
    |  |   HARNESS                             |  |
    |  |=========================================|  | <- Frame bottom
    |  |    |           |         |              |  |
    |  +----|-----------|---------|--------------+  |
    |       |           |         |                 |
    |     [FR]        [RR]       [COOLANT]         |
    |      O           O          [RADIATOR]        |
    |     / \         / \                          |
    |    /   \       /   \                         |
    |   [COIL]    [COIL]                           |
    |   [C1-C3]   [C4-C6]                          |
    |                                              |
    |  Ground Clearance: 130mm                    |
    +----------------------------------------------+

    Coil positions (phi-helical):
    Front:  C1 (center), C2 (137.5deg), C3 (90deg)
    Rear:   C4 (center), C5 (275deg), C6 (45deg)
```

## Frame Detail — Welding Layout

```
    MONOCOQUE FRAME (Chromoly 4130)
    ================================
    
    TOP TUBE
    [=======================================]
         |           |           |
    [CROSS 1]   [CROSS 2]   [CROSS 3]
         |           |           |
    [=======================================]
    BOTTOM TUBE
    
    DOWN TUBES (front)
         /                    \
        /                      \
    [HEAD TUBE]           [ENGINE MOUNT]
    (1 1/8" headset)      (battery bay)
        \                      /
         \                    /
    [=======================================]
    BOTTOM PLATE
    
    SWINGARM PIVOT
    [==============================]
         |                    |
    [PIVOT BOLT]        [PIVOT BOLT]
    (M12 x 1.25)       (M12 x 1.25)
         |                    |
    [==============================]
    
    TAIL SECTION
    [==============================]
         |                    |
    [SHOCK MOUNT]      [TAIL MOUNT]
    (upper)             (rear)
         |                    |
    [==============================]
```

## Fork & Triple Clamp

```
    INVERTED FORK (43mm, 120mm travel)
    ====================================
    
    [HANDLEBARS]
    [========720mm========]
         |           |
    [CLAMP L]    [CLAMP R]
         |           |
    [UPPER TRIPLE CLAMP]
    +===================+
    |    |         |    |
    | [STANCHION]  |    |  <- 43mm inverted
    |    |         |    |     (stanchion up, slider down)
    |    |         |    |
    | [SLIDER]     |    |
    |    |         |    |
    [LOWER TRIPLE CLAMP]
    +===================+
         |           |
    [STEERING STEM]
    [1 1/8" BEARING]
         |
    [HEAD TUBE]
    (on frame)
    
    Trail: 95mm
    Rake: 25 degrees
    Travel: 120mm
```

## Swingarm & Rear Suspension

```
    SWINGARM (Aluminum, single-sided)
    ====================================
    
    [FRAME PIVOT POINT]
    [===M12 BOLT===]
         |
    +----+----+
    |         |
    | [ARM L] | [ARM R]
    |         |
    |    |    |
    |    |    +--[SHOCK MOUNT]
    |    |        (M10 bolt)
    |    |        |
    |    |    [REAR SHOCK]
    |    |    [300mm]
    |    |    [ADJUSTABLE]
    |    |        |
    |    |    [FRAME UPPER MOUNT]
    |    |        |
    |    +--------+
    |         |
    [REAR AXLE]
    [M12 x 1.25]
    [400mm long]
         |
    +----+----+
    |         |
    [HUB MOTOR]
    [1500W]
    [72V BLDC]
    |         |
    [REAR WHEEL]
    [17" AIRLESS]
    
    Travel: 100mm
    Sag: 30% (30mm)
```

## Steering Geometry

```
    STEERING (Conventional Handlebar)
    ===================================
    
    [LEFT GRIP]----[LEFT LEVER]----[PHASE BTN]
                                         |
    [========= HANDLEBAR 720mm =========]
                                         |
    [CLAMP]---[CLAMP]---[CENTER]---[CLAMP]
              |                      |
         [OLED 5"]              [RIGHT GRIP]
         (I2C)                  [THROTTLE]
                                     |
                                [RIGHT LEVER]
                                (front brake)
    
    Handlebar: 7/8" (22.2mm)
    Rise: 30mm
    Sweep: 15 degrees back
    Clamp: 4 x M6 bolts per side
```

## Wheel Assembly Detail

```
    HUBLESS WHEEL (Front)
    =======================
    
    Outer Rim (17" aluminum)
    +=======================+
    |                       |
    |    [AIRLESS TIRE]     |  <- Honeycomb polymer
    |    (honeycomb)        |     No air, no flats
    |                       |
    +---+               +---+
        |   [BEARING]    |
        |  +=========+  |
        |  | 6203-2RS |  |  <- Sealed bearing
        |  +=========+  |
        |               |
        |   [AXLE]      |
        |   (M12 bolt)  |
        |               |
        +---------------+
    
    HUB MOTOR WHEEL (Rear)
    ========================
    
    Outer Rim (17" aluminum)
    +=======================+
    |                       |
    |    [AIRLESS TIRE]     |
    |                       |
    +---+               +---+
        |  [MOTOR]      |
        |  +=========+  |
        |  | BLDC     |  |  <- 1500W hub motor
        |  | 1500W    |  |     Direct drive
        |  | 72V      |  |
        |  | [PH A]   |  |
        |  | [PH B]   |  |
        |  | [PH C]   |  |
        |  +=========+  |
        |               |
        |   [AXLE]      |
        |   (M12 bolt)  |
        |               |
        +---------------+
```

## Cooling System Layout

```
    COOLING SYSTEM (Phase Coils)
    =============================
    
    [RADIATOR] <--SIDE MOUNTED
         |
    [WATER PUMP] (12V, 3L/min)
         |
         +--[COIL C1]--[COIL C2]--[COIL C3]--+
         |                                    |
         +--[COIL C4]--[COIL C5]--[COIL C6]--+
         |                                    |
         +--[TEMP SENSOR 1]--[TEMP SENSOR 2]--+
         |                                    |
         +------------------------------------+
         |
    [RETURN TO RADIATOR]
    
    Cutoff: 90C (thermal relay)
    Max operating: 65C
    Coolant: 50/50 glycol-water
    Capacity: 0.5 liters
```

## Phase Coil Mounting Detail

```
    COIL MOUNT (Per coil, 6 total)
    ================================
    
    [FAIRING PANEL]
         |
    [MOUNTING RING] (aluminum, CNC or drilled)
         |
         +--[VIBRATION ISOLATOR] (rubber grommet)
         |
    [COIL FORM] (PVC pipe 8" OD)
         |
    [COIL WINDING] (Litz wire, 90 turns)
         |
    [COPPER FOIL SHIELD] (3" wrap, grounded)
         |
    [CAPACITOR BANK] (soldered to coil leads)
         |
    [WATER COOLING CHANNEL] (silicone hose, inline)
         |
    [CONNECTOR TO DRIVER] (XT60 pair)
    
    Mounting: 2x M6 bolts per coil
    Alignment: Phi-angle marked on ring
    Cooling: Series liquid loop
    Total weight per coil: 0.5 kg
```

## Rider Ergonomics

```
    RIDING POSITION (Sport-Touring)
    ================================
    
                    [HEAD]
                      |
                 [SHOULDERS]
                /            \
           [LEFT ARM]      [RIGHT ARM]
              |                |
         [LEFT GRIP]      [THROTTLE]
         [BRAKE LEV]      [BRAKE LEV]
              |                |
         [TORSO]          (upright, 15deg forward lean)
              |
         [HIPS]----[SEAT 780mm]
              |
         [LEFT LEG]     [RIGHT LEG]
              |                |
         [LEFT PEG]     [RIGHT PEG]
         [MID-SET]      [MID-SET]
              |                |
         [LEFT TOE]     [RIGHT TOE]
    
    Seat height: 780mm (+/- 30mm adjustable)
    Handlebar width: 720mm
    Footpeg position: Mid-set (sport-touring)
    Rider weight range: 50-120 kg
```

## Bolt Torque Specs

| Fastener | Size | Torque | Lock |
|----------|------|--------|------|
| Front axle | M12 x 1.25 | 75 Nm | Blue Loctite |
| Rear axle | M12 x 1.25 | 80 Nm | Blue Loctite |
| Swingarm pivot | M12 x 1.25 | 70 Nm | Nylock nut |
| Triple clamp pinch | M6 x 1.0 | 10 Nm | Blue Loctite |
| Handlebar clamp | M6 x 1.0 | 10 Nm | Blue Loctite |
| Front brake rotor | M6 x 1.0 | 12 Nm | Lock washer |
| Rear brake rotor | M6 x 1.0 | 12 Nm | Lock washer |
| Coil mount | M6 x 1.0 | 8 Nm | Lock washer |
| Frame gusset | M8 x 1.25 | 25 Nm | Nylock nut |
| Footpeg mount | M8 x 1.25 | 30 Nm | Nylock nut |

## Weight Distribution

```
    FRONT: 42% / REAR: 58% (without rider)
    ==========================================
    
    Front axle load: 12 kg (vehicle)
    Rear axle load: 16 kg (vehicle) + motor
    
    With rider (75 kg):
    Front: 12 + 25 = 37 kg
    Rear:  16 + 50 = 66 kg
    
    Total: 28 kg vehicle + 75 kg rider = 103 kg
    
    Ground clearance: 130mm
    Center of gravity: 550mm above ground (with rider)
```

## Folded Dimensions

```
    STORAGE/TRANSPORT MODE
    ========================
    
    [FOLDED: 1.5m x 0.6m x 0.5m]
    
    Handlebars: Fold flat (2 bolts each side)
    Seat: Collapses (quick-release)
    Wheels: Stay attached
    
    +------ 1500mm ------+
    |                    |  ^
    |  [FOLDED BARS]     |  |
    |  [SEAT DOWN]       |  600mm
    |  [WHEELS INLINE]   |  |
    |                    |  v
    +--------------------+
                    500mm depth
```
