# PHI TETHER POD — Mechanical Diagram

## Side View (Deployed)

```
    ANCHOR POINT (ground)
    ======================
    +---+---+---+
    | GROUND   |
    | ANCHOR   |
    | (item#30)|
    +----+-----+
         |
    ANCHOR ROPE (item #31)
    8mm x 30m polypropylene
         |
    +----+-----+
    | TETHER   |
    | WINDER   |
    | (item#2) |
    | 200m cap |
    +----+-----+
         |
    DYNEEMA TETHER (item #1)
    4mm x 200m, 2200kg rated
         |
         |  (guy lines extend here)
         |
    GUY LINES (item #32)
    3mm x 10m, 3 directions
    +--------+--------+
    |        |        |
    |        |        |
    STAKES   POD     STAKES
    (item#33)        (item#33)
         |
         |
    +----+----+
    | SWIVEL  |
    | (item#5)|
    | 360°    |
    +----+----+
         |
    +----+----+
    | QUICK   |
    | RELEASE |
    | HOOK    |
    | (item#3)|
    +----+----+
         |
    +----+----+
    |  POD    |
    |  FRAME  |
    |  (see   |
    |  below) |
    +---------+


## Pod Frame Detail

```
    TOP VIEW:
    +----+===============+----+
    |    |               |    |
    | SEAT               SEAT |
    | PAN    FRAME       PAN  |
    | (item#14)         (item#14)
    |    |               |    |
    |    |   +-------+   |    |
    |    |   |BATTERY|   |    |
    |    |   |(item#18)|  |    |
    |    |   +-------+   |    |
    |    |               |    |
    +----+===============+----+
         |    400mm     |
    
    SIDE VIEW:
         +----+
         |    |
    +----+    +----+
    |    |    |    |
    |    | SEAT    |
    |    | PAN     |
    |    |    |    |
    |    +----+    |
    |    |    |    |
    |    | BATT|   |
    |    |    |    |
    +----+    +----+
         |    |
         +----+
    
    Frame: Aluminum tubing
    - 20mm main (item #7)
    - 15mm secondary (item #8)
    - 3-way + 4-way connectors (items #9-10)


## Seat & Harness

```
    SEAT CROSS-SECTION:
    +-------------------+
    |   EVA FOAM PAD    |
    |   (item #12)      |
    +--------+----------+
             |
    MOLDED PLASTIC SEAT PAN
    (item #14)
    +--------+----------+
             |
    4-POINT HARNESS
    (item #15)
    
    HARNESS LAYOUT:
    
    +---+         +---+
    | L |         | R |
    |   | SHOULDER|   |
    |   | STRAP   |   |
    |   +----+----+   |
    |        |        |
    |   +----+----+   |
    |   |  CHEST  |   |
    |   |  STRAP  |   |
    |   +----+----+   |
    |        |        |
    |   +----+----+   |
    |   |  SEAT   |   |
    |   |  BELT   |   |
    |   +----+----+   |
    |        |        |
    LEGS     |     LEGS


## Tether Connection Detail

```
    DYNEEMA TETHER (item #1)
    4mm, 2200kg rated
    |
    +---- QUICK-RELEASE HOOK (item #3)
    |     Steel, auto-locking
    |     500kg rated
    |
    +---- SWIVEL #1 (item #5)
    |     Ball-bearing, 360°
    |     Prevents tether twist
    |
    +---- CARABINER (item #4)
    |     Steel, 25kN
    |     Auto-locking
    |
    +---- D-RING (on pod frame)
          Welded, 25kN
          Bolted to frame


## Guy Line System

```
    TOP VIEW (3-point anchoring):
    
              STAKE 1 (N)
                 |
                 | 10m
                 |
    STAKE 3 -----+----- STAKE 2
    (SW)    10m  |  10m  (SE)
                 |
                 |
                 POD (center)
    
    STAKE DETAIL (item #33):
    +-------+
    |   Y   |
    |  /|\  |
    | / | \ |
    |/  |  \|
    +---+---+
        |
    Driven 300mm into ground
    
    GUY LINE (item #32):
    3mm cord with tensioner
    Quick-release buckle at pod end


## Winch System Detail

```
    WINCH WINDER (item #2):
    +-------------------+
    |   MANUAL CRANK    |
    |        |          |
    |   +----+----+     |
    |   | DRUM    |     |
    |   | 200m    |     |
    |   | capacity|     |
    |   +----+----+     |
    |        |          |
    |   GEARS |         |
    |   1:10  |         |
    |   ratio |         |
    +----+---+----------+
         |
    WIRELESS RECEIVER
    (item #24)
    +----+---+----------+
    |   RF    |          |
    |   433MHz|          |
    |   300m  |          |
    +--------+----------+
         |
    RELAY MODULE
    +----+---+----------+
    |   WINCH MOTOR     |
    |   12V DC          |
    |   200kg pull      |
    |   (item #23)      |
    +-------------------+
    
    OPERATION:
    - Remote button UP: motor reels in
    - Remote button DOWN: motor reels out
    - Auto-brake holds position when stopped
    - Manual override: crank handle


## Emergency Descent Device

```
    EDD (item #35):
    +-------------------+
    |   SELF-BRAKING    |
    |   DESCENT DEVICE  |
    |   15m cable       |
    |                   |
    |   +----+----+     |
    |   | CABLE |     |
    |   | 2mm   |     |
    |   | steel |     |
    |   +----+----+     |
    |                   |
    |   ACTIVATION:     |
    |   Pull handle     |
    |   (manual)        |
    +-------------------+
    
    ATTACHMENT:
    Pod frame D-ring
         |
    EDD carabiner
         |
    Operator harness


## Height Sensor Mount

```
    SENSOR (item #25):
    ULTRASONIC HC-SR04
    
    MOUNTING:
    +-----------+
    |  SENSOR   |  <-- Points downward
    |  |||||||  |      (measures height)
    +-----+-----+
          |
    MOUNTING BRACKET
    (aluminum, adjustable angle)
          |
    ATTACHED TO POD FRAME
    (bottom center)


## Dimensions Summary

```
    POD WIDTH:          400mm
    POD DEPTH:          300mm
    POD HEIGHT:         300mm (frame only)
    FRAME TUBE:         20mm main, 15mm secondary
    
    TOTAL WEIGHT:       8.2 kg
    - Frame:            2.5 kg
    - Seat + harness:   2.0 kg
    - Tether (200m):    1.5 kg
    - Battery:          1.2 kg
    - Electronics:      0.5 kg
    - Safety gear:      0.5 kg
    
    MAX LOAD:           120 kg (operator)
    MAX HEIGHT:         10m (tether limit)
    DEPLOY TIME:        30 seconds
    PACKED SIZE:        0.4m carry case
    
    TETHER STRENGTH:    2200 kg (Dyneema)
    SAFETY FACTOR:      18.3x (2200/120)
```
