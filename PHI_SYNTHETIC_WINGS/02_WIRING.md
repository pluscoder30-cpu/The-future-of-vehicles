# PHI SYNTHETIC WINGS — Wiring Diagram

## System Overview

```
  +------------------+     +------------------+     +------------------+
  |   BATTERY PACK   |---->|   MAIN FUSE      |---->|   CONTROL BOARD  |
  |   36V 5Ah        |     |   20A blade      |     |   Arduino-based  |
  |   (item #21)     |     |   (item #37)     |     |   (item #26)     |
  +------------------+     +------------------+     +------------------+


  CONTROL BOARD
  ==============
  +-------------------------------------------+
  |          ARDUINO FLIGHT CONTROLLER         |
  |                                           |
  |  INPUTS:              OUTPUTS:            |
  |  - Throttle (A0)      - Servo 1 (D3)     |
  |  - Pot L-Wing (A1)    - Servo 2 (D5)     |
  |  - Pot R-Wing (A2)    - Servo 3 (D6)     |
  |  - Kill Switch (D2)   - Servo 4 (D9)     |
  |  - IMU SDA (A4)       - Motor ESC (D10)  |
  |  - IMU SCL (A5)       - LED Status (D11) |
  |  - Barometer (SPI)    - Buzzer (D12)     |
  +-------------------------------------------+
        |                       |
        v                       v
  SENSOR INPUTS           ACTUATOR OUTPUTS


  SERVO WIRING (4 CHANNELS)
  =========================

  LEFT WING FLAP (SERVO 1)
  +-----------+     +-----------+     +-----------+
  |  ARDUINO  |---->|  SERVO 1  |---->|  LEFT     |
  |  Pin D3   |     |  35kg     |     |  FLAP     |
  |  PWM      |     |  (item#9) |     |  HINGE    |
  +-----------+     +-----------+     +-----------+
        |
  Wire: 22AWG, 3-conductor
  Colors: ORANGE=signal, RED=+5V, BROWN=GND


  RIGHT WING FLAP (SERVO 2)
  +-----------+     +-----------+     +-----------+
  |  ARDUINO  |---->|  SERVO 2  |---->|  RIGHT    |
  |  Pin D5   |     |  35kg     |     |  FLAP     |
  |  PWM      |     |  (item#9) |     |  HINGE    |
  +-----------+     +-----------+     +-----------+


  LEFT WING PITCH (SERVO 3)
  +-----------+     +-----------+     +-----------+
  |  ARDUINO  |---->|  SERVO 3  |---->|  LEFT     |
  |  Pin D6   |     |  35kg     |     |  PITCH    |
  |  PWM      |     |  (item#9) |     |  CONTROL  |
  +-----------+     +-----------+     +-----------+


  RIGHT WING PITCH (SERVO 4)
  +-----------+     +-----------+     +-----------+
  |  ARDUINO  |---->|  SERVO 4  |---->|  RIGHT    |
  |  Pin D9   |     |  35kg     |     |  PITCH    |
  |  PWM      |     |  (item#9) |     |  CONTROL  |
  +-----------+     +-----------+     +-----------+


  THROTTLE INPUT
  ==============
  +-----------+     +-----------+
  |  HALL     |---->|  ARDUINO  |
  |  EFFECT   |     |  Pin A0   |
  |  THUMB    |     |  Analog   |
  |  (item#29)|     +-----------+
  +-----------+
  Wire: 22AWG, 3-conductor
  Colors: ORANGE=signal, RED=+5V, BROWN=GND


  MOTOR ESC
  =========
  +-----------+     +-----------+     +-----------+
  |  ARDUINO  |---->|  ESC      |---->|  MOTOR    |
  |  Pin D10  |     |  36V 20A  |     |  400W     |
  |  PWM      |     |  (item#37)|     |  (item#34)|
  +-----------+     +-----------+     +-----------+
        |
  Wire: 14AWG silicone (motor to ESC)
        22AWG signal (Arduino to ESC)


  KILL SWITCH
  ===========
  +-----------+     +-----------+
  |  MAGNETIC |---->|  ARDUINO  |
  |  LANYARD  |     |  Pin D2   |
  |  (item#30)|     |  INPUT    |
  +-----------+     +-----------+
        |
  When disconnected -> Arduino cuts ALL servo + ESC signals
  Wire: 22AWG, 2-conductor


  SENSOR WIRING
  =============

  IMU (GY-521 / MPU6050)
  +-----------+     +-----------+
  |  MPU6050  |---->|  ARDUINO  |
  |  IMU      |     |  SDA (A4) |
  |  6-axis   |     |  SCL (A5) |
  +-----------+     +-----------+
  Wire: 22AWG, 4-conductor (I2C)
  Colors: RED=+5V, BLACK=GND, BLUE=SDA, WHITE=SCL


  BAROMETRIC ALTIMETER (BMP280)
  +-----------+     +-----------+
  |  BMP280   |---->|  ARDUINO  |
  |  Altimeter|     |  SPI bus  |
  |  0-5000m  |     |  (D13-10) |
  +-----------+     +-----------+
  Wire: 22AWG, 5-conductor (SPI)


  WING ANGLE FEEDBACK
  ====================
  +-----------+     +-----------+
  |  10kΩ     |---->|  ARDUINO  |
  |  POT      |     |  A1 (L)   |
  |  (item#28)|     |  A2 (R)   |
  +-----------+     +-----------+
  Wire: 22AWG, 3-conductor per pot
  Colors: RED=+5V, BLACK=GND, BLUE=signal


  LED STATUS
  ==========
  +-----------+     +-----------+
  |  ARDUINO  |---->|  WS2812B  |
  |  Pin D11  |     |  RGB LED  |
  |  Data     |     |  (item#31)|
  +-----------+     +-----------+
  Wire: 22AWG, 3-conductor
  Colors: RED=+5V, BLACK=GND, GREEN=data


  POWER DISTRIBUTION
  ==================
  +-----------+     +------------------+
  |  BATTERY  |---->|  POWER BOARD     |
  |  36V 5Ah  |     |  (splitter)      |
  +-----------+     +------------------+
        |                       |
        +-----> 36V to ESC      |
        +-----> 5V BEC to Arduino (via ESC)
        +-----> 5V to servos (via Arduino 5V pin)
        +-----> 5V to sensors (via Arduino 5V pin)


  WIRE COLOR CODE
  ===============
  RED    = +36V main power
  ORANGE = +5V servo/signal power
  BLACK  = Ground / return
  BROWN  = Ground (servo convention)
  GREEN  = I2C data / status LED
  BLUE   = I2C clock / sensor data
  WHITE  = SPI data / analog signal
  YELLOW = PWM signal


  WIRE ROUTING
  ============
         BATTERY (chest mount)
             |
         [main fuse 20A]
             |
      +------+------+
      |   POWER     |
      |   BOARD     |
      +------+------+
             |
    +--------+--------+
    |                 |
    v                 v
  ARDUINO          ESC + MOTOR
  (chest)          (rear mount)
    |
    +---> Servo 1 (left wing)
    +---> Servo 2 (right wing)
    +---> Servo 3 (left pitch)
    +---> Servo 4 (right pitch)
    +---> IMU (chest)
    +---> Altimeter (chest)
    +---> LED (chest)


  SAFETY NOTES
  ============
  - Kill switch cuts ALL signals (servos go limp, motor stops)
  - All wires secured with cable ties every 150mm
  - Strain relief at all connector points
  - Test ALL connections before first flight
  - Calibrate potentiometers with wings deployed
  - Verify kill switch operation before EVERY flight
