# PHI SUBMERSIBLE — Wiring Diagram

## System Overview

```
  +------------------+     +------------------+     +------------------+
  |   BATTERY PACK   |---->|   MAIN FUSE      |---->|   SWITCH PANEL   |
  |   36V 20Ah       |     |   60A ANL        |     |   3x Toggle      |
  |   LiFePO4        |     |   (item #26)     |     |   (items #28)    |
  +------------------+     +------------------+     +------------------+


  SWITCH PANEL OUTPUTS:
  =====================

  SW1: THRUSTER (ON/OFF)
  +-----------+
  |  TOGGLE 1 |
  +-----+-----+
        |
        v
  +-----+-----+     +-----------+     +-----------+     +-----------+
  |  ESC      |---->|  MOTOR    |---->|  PROPELLER|     |  HULL     |
  |  36V 30A  |     |  500W IP68|     |  5-BLADE  |     |  GROUND   |
  |  (item#23)|     |  (item#11)|     |  (item#12)|     |  (item#2) |
  +-----------+     +-----------+     +-----------+     +-----------+
        |
        +-----> MOTOR CONTROL WIRES
                (12AWG silicone, color: RED=+, BLACK=-)


  SW2: BALLAST PUMP (ON/OFF)
  +-----------+
  |  TOGGLE 2 |
  +-----+-----+
        |
        v
  +-----+-----+     +-----------+
  |  PUMP     |---->|  BALLAST  |
  |  RELAY    |     |  TANK     |
  |  12V 30A  |     |  (item#7) |
  +-----------+     +-----------+
        |
        +-----> 12V STEP-DOWN CONVERTER
                (36V -> 12V, 10A)


  SW3: LIGHTS (ON/OFF)
  +-----------+
  |  TOGGLE 3 |
  +-----+-----+
        |
        v
  +-----+-----+     +-----------+
  |  LED BAR  |     |  DEPTH    |
  |  20W      |     |  GAUGE    |
  |  (item#26)|     |  (item#24)|
  +-----------+     +-----------+
        |
        +-----> 12V STEP-DOWN CONVERTER
                (36V -> 12V, 5A)


  SAFETY SYSTEMS (ALWAYS ON)
  ==========================
  +-----------+     +-----------+     +-----------+
  |  KILL     |---->|  BUOYANCY |---->|  SURFACE  |
  |  SWITCH   |     |  PUMP     |     |  MARKER   |
  |  MAGNETIC |     |  12V      |     |  LIGHT    |
  |  (item#27)|     |  (item#32)|     |  LED      |
  +-----------+     +-----------+     +-----------+
        |
        +-----> DISCONNECTS ESC + MOTOR
                (cuts power to propulsion)


  GROUND SYSTEM
  =============
  All grounds connect to COMMON GROUND BUS:
  +-------------------------------------------+
  |          COMMON GROUND BUS (copper)        |
  |  Batt(-) -- ESC GND -- Pump GND -- LED GND |
  +-------------------------------------------+
        |
        v
  Hull bond (14AWG green wire to aluminum frame)


  WIRE COLOR CODE
  ===============
  RED    = +36V main power
  BLACK  = Ground / return
  GREEN  = Safety ground / hull bond
  YELLOW = 12V switched (after converter)
  BLUE   = Signal / control wires
  WHITE  = Sensor data lines


  STEP-DOWN CONVERTERS
  ====================
  +-----------+          +-----------+
  | 36V IN    |          | 36V IN    |
  | (from     |          | (from     |
  |  battery) |          |  battery) |
  +-----+-----+          +-----+-----+
        |                       |
  +-----v-----+          +-----v-----+
  | 12V 10A   |          | 12V 5A    |
  | OUTPUT    |          | OUTPUT    |
  +-----+-----+          +-----+-----+
        |                       |
        v                       v
  Ballast pump +         LEDs + depth
  buoyancy pump          gauge


  WATERPROOF CONNECTIONS
  ======================
  All external connections use:
  - Cable glands (PG11, items #30)
  - Marine silicone sealant (item #47)
  - Heat-shrink tubing (marine grade)
  - Dielectric grease on all connectors


  SAFETY NOTES
  ============
  - Kill switch disconnects ALL power from motor
  - Buoyancy pump has independent 12V battery backup
  - All wires rated for underwater (silicone insulation)
  - Fuses protect each circuit branch
  - Test ALL connections before submersion
