# PHI OCEAN VEHICLE — Wiring Diagram

## System Overview

```
  +------------------+     +------------------+     +------------------+
  |   BATTERY PACK   |---->|   MAIN FUSE      |---->|   SWITCH PANEL   |
  |   48V 30Ah       |     |   100A ANL       |     |   4x Toggle      |
  |   LiFePO4        |     |   (item #26)     |     |   (items #33)    |
  +------------------+     +------------------+     +------------------+


  SWITCH PANEL OUTPUTS:
  =====================

  SW1: MAIN PROPULSION (ON/OFF)
  +-----------+
  |  TOGGLE 1 |
  +-----+-----+
        |
        v
  +-----+-----+     +-----------+     +-----------+     +-----------+
  |  ESC      |---->|  MOTOR    |---->|  IMPELLER |     |  JET      |
  |  48V 40A  |     |  1000W    |     |  7-BLADE  |     |  NOZZLE   |
  |  (item#27)|     |  IP68     |     |  (item#14)|     |  (item#15)|
  +-----------+     +-----------+     +-----------+     +-----------+
        |
        +-----> THROTTLE INPUT
                (Hall-effect twist, item #28)


  SW2: NAVIGATION LIGHTS (ON/OFF)
  +-----------+
  |  TOGGLE 2 |
  +-----+-----+
        |
        v
  +-----+-----+     +-----------+
  |  LED NAV  |---->|  BOW: RED |
  |  CIRCUIT  |     |  STERN:   |
  |  12V      |     |  GREEN    |
  |  (item#31)|     |  (item#31)|
  +-----------+     +-----------+
        |
        +-----> 12V STEP-DOWN (48V -> 12V, 5A)


  SW3: INSTRUMENTS (ON/OFF)
  +-----------+
  |  TOGGLE 3 |
  +-----+-----+
        |
        v
  +-----+-----+     +-----------+     +-----------+
  |  GPS      |     |  FISH     |     |  BATTERY  |
  |  MODULE   |     |  FINDER   |     |  MONITOR  |
  |  (item#29)|     |  (item#30)|     |  (item#24)|
  +-----------+     +-----------+     +-----------+
        |
        +-----> 12V STEP-DOWN (48V -> 12V, 3A)


  SW4: BILGE PUMP (ON/AUTO)
  +-----------+
  |  TOGGLE 4 |
  +-----+-----+
        |
        v
  +-----+-----+     +-----------+
  |  BILGE    |---->|  AUTO     |
  |  PUMP     |     |  SWITCH   |
  |  12V 500GPH|    |  (float)  |
  |  (item#47)|     +-----------+
  +-----------+


  STEERING SYSTEM (MECHANICAL + ELECTRICAL)
  ==========================================
  +-----------+     +-----------+     +-----------+
  |  STEERING |---->|  STEERING |---->|  JET      |
  |  WHEEL    |     |  CABLE    |     |  NOZZLE   |
  |  (item#37)|     |  (item#38)|     |  ARTICUL. |
  +-----------+     +-----------+     +-----------+
                                           |
                                    +------+------+
                                    |  SERVO      |
                                    |  ASSIST     |
                                    |  (optional) |
                                    +-------------+


  KILL SWITCH (ALWAYS ACTIVE)
  ============================
  +-----------+     +------------------+
  |  MAGNETIC |---->|  DISCONNECTS     |
  |  LANYARD  |     |  ESC POWER       |
  |  (item#32)|     |  (cuts motor)    |
  +-----------+     +------------------+
        |
        +-----> Also triggers bilge pump ON
                (emergency water removal)


  GROUND SYSTEM
  =============
  +-------------------------------------------+
  |          COMMON GROUND BUS (copper)        |
  |  Batt(-) -- ESC GND -- Pump GND -- Nav GND |
  |  GPS GND -- Fish GND -- Monitor GND        |
  +-------------------------------------------+
        |
        v
  Hull ground (10AWG green wire to aluminum frame)
  Bond all metal fittings to hull ground


  WIRE COLOR CODE
  ===============
  RED    = +48V main power
  BLACK  = Ground / return
  GREEN  = Safety ground / hull bond
  YELLOW = 12V switched (after converter)
  BLUE   = Signal / control wires
  WHITE  = Sensor data lines (GPS, depth)
  ORANGE = Steering servo signal


  STEP-DOWN CONVERTERS
  ====================
  +-----------+          +-----------+          +-----------+
  | 48V IN    |          | 48V IN    |          | 48V IN    |
  +-----+-----+          +-----+-----+          +-----+-----+
        |                       |                       |
  +-----v-----+          +-----v-----+          +-----v-----+
  | 12V 10A   |          | 12V 5A    |          | 12V 3A    |
  +-----+-----+          +-----+-----+          +-----+-----+
        |                       |                       |
        v                       v                       v
  Bilge + nav lights      GPS + fish finder      Battery monitor


  WATERPROOF CONNECTIONS
  ======================
  All connections through hull use:
  - Cable glands (PG16, items #35)
  - Marine sealant (3M 5200, items #50)
  - Heat-shrink tubing (marine grade)
  - Dielectric grease on all connectors
  - Junction boxes for underwater areas


  WIRING GAUGE TABLE
  ==================
  Circuit              | Gauge  | Amps | Wire Color
  ---------------------|--------|------|----------
  Battery to ESC       | 10 AWG | 40A  | Red/Black
  Battery to Fuse      | 8 AWG  | 100A | Red
  ESC to Motor         | 10 AWG | 30A  | Red/Black
  12V Main Bus         | 14 AWG | 10A  | Yellow/Black
  Nav Lights           | 18 AWG | 2A   | Blue/Black
  Instruments          | 18 AWG | 1A   | White/Black
  Bilge Pump           | 14 AWG | 5A   | Red/Black
  Steering Servo       | 22 AWG | 0.5A | Orange/Brown


  SAFETY NOTES
  ============
  - Kill switch disconnects motor but keeps instruments on
  - Bilge pump auto-activates on water detection
  - All circuits fused individually
  - Ground bonding prevents electrical shock in water
  - Test ALL connections with multimeter before launch
  - Run engine out of water for 30 minutes before first use
