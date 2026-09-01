# PHI TETHER POD — Wiring Diagram

## System Overview

```
  +------------------+     +------------------+     +------------------+
  |   BATTERY PACK   |---->|   MAIN FUSE      |---->|   SWITCH PANEL   |
  |   12V 10Ah       |     |   15A blade      |     |   2x Toggle      |
  |   Li-Ion         |     |   (item #22)     |     |   (item #29)     |
  +------------------+     +------------------+     +------------------+


  SWITCH PANEL OUTPUTS:
  =====================

  SW1: WINCH CONTROLLER (ON/OFF)
  +-----------+
  |  TOGGLE 1 |
  +-----+-----+
        |
        v
  +-----+-----+     +-----------+     +-----------+     +-----------+
  |  WINCH    |---->|  WINCH    |---->|  TETHER   |     |  POD      |
  |  CONTROLLER|    |  MOTOR    |     |  WINDER   |     |  LIFTS    |
  |  12V      |     |  12V DC   |     |  (item#2) |     |  /LOWERS  |
  |  (item#23)|     |  200kg    |     |           |     |           |
  +-----------+     +-----------+     +-----------+     +-----------+
        |
        +-----> WIRELESS REMOTE INPUT
                (RF, 300m range, item #24)


  SW2: INSTRUMENTS + LIGHTS (ON/OFF)
  +-----------+
  |  TOGGLE 2 |
  +-----+-----+
        |
        v
  +-----+-----+     +-----------+
  |  HEIGHT   |     |  LED      |
  |  SENSOR   |     |  LIGHT    |
  |  0-10m    |     |  10W      |
  |  (item#25)|     |  (item#27)|
  +-----------+     +-----------+
        |
        +-----> LEVEL INDICATOR
                (item #26)


  WIRELESS REMOTE CONTROL
  ========================
  +-----------+     RF (300m)    +-----------+
  |  HANDHELD |================>|  RECEIVER  |
  |  REMOTE   |   (item #24)    |  (in pod)  |
  |  2-button |                 |  UP/DOWN   |
  +-----------+                 +-----+-----+
                                      |
                                      v
                                +-----------+
                                |  WINCH    |
                                |  RELAY    |
                                +-----+-----+
                                      |
                          +-----------+-----------+
                          |                       |
                          v                       v
                    +-----------+           +-----------+
                    |  REEL UP  |           |  REEL DN  |
                    |  (ascend) |           |  (descend)|
                    +-----------+           +-----------+


  HEIGHT SENSOR
  =============
  +-----------+     +-----------+     +-----------+
  |  ULTRASONIC|---->|  ADC      |---->|  LED      |
  |  HC-SR04   |     |  MODULE   |     |  BAR      |
  |  0-10m     |     |  (in pod) |     |  DISPLAY  |
  |  (item#25) |     |           |     |  (item#26)|
  +-----------+     +-----------+     +-----------+
  Wire: 22AWG, 4-conductor
  Colors: RED=+5V, BLACK=GND, BLUE=TRIG, WHITE=ECHO


  LEVEL INDICATOR
  ===============
  +-----------+     +-----------+
  |  BUBBLE   |     |  LED      |
  |  LEVEL    |     |  RING     |
  |  + TILT   |     |  (item#26)|
  |  SENSOR   |     |           |
  +-----------+     +-----------+
  Wire: 22AWG, 3-conductor


  GROUND SYSTEM
  =============
  +-------------------------------------------+
  |          COMMON GROUND BUS                 |
  |  Batt(-) -- Winch GND -- Sensor GND       |
  +-------------------------------------------+
        |
        v
  Frame ground (14AWG green wire to aluminum)


  WIRE COLOR CODE
  ===============
  RED    = +12V main power
  BLACK  = Ground / return
  GREEN  = Safety ground / frame bond
  YELLOW = +5V (sensor power)
  BLUE   = Signal / control
  WHITE  = Data / feedback


  POWER DISTRIBUTION
  ==================
  +-----------+     +------------------+
  |  BATTERY  |---->|  FUSE BLOCK      |
  |  12V 10Ah |     |  15A blade       |
  +-----------+     +------------------+
        |                       |
        +-----> Winch (10A max) |
        +-----> Sensors (1A)    |
        +-----> Light (2A)      |
        +-----> Level LED (0.5A)|


  WIRE ROUTING
  ============
         BATTERY (in pod frame)
             |
         [main fuse 15A]
             |
      +------+------+
      |   SWITCH    |
      |   PANEL     |
      +------+------+
             |
    +--------+--------+
    |                 |
    v                 v
  WINCH            SENSORS + LIGHT
  CONTROLLER       (dashboard)
    |
    v
  WINCH MOTOR (in winder unit)
    |
    v
  TETHER -> POD


  SAFETY NOTES
  ============
  - Winch has auto-brake (holds position when power off)
  - Emergency descent device is INDEPENDENT (mechanical)
  - Test winch control before EVERY suspension
  - All connections soldered + heat-shrink
  - Fuse protects against winch motor stall
  - Maximum load: 120 kg (operator weight)
  - Never exceed 10m tether extension
