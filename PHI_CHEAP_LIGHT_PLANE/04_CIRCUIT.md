# PHI CHEAP LIGHT PLANE — CIRCUIT

## Avionics Circuit Schematics

---

## FLIGHT COMPUTER — ARDUINO NANO #1 (PRIMARY)

### Complete Pinout and Connections

```
┌─────────────────────────────────────────────────────────────────┐
│                    ARDUINO NANO #1 — PRIMARY FLIGHT COMPUTER     │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                                                          │   │
│  │  ┌────────┐                                              │   │
│  │  │ USB    │  ← Programming + debug                       │   │
│  │  └────────┘                                              │   │
│  │                                                          │   │
│  │  DIGITAL PINS:                                           │   │
│  │                                                          │   │
│  │  D2  ──── BMP280 #1 SDA ──── I2C (4.7kΩ pullup)        │   │
│  │  D3  ──── BMP280 #1 SCL ──── I2C (4.7kΩ pullup)        │   │
│  │  D4  ──── MPU6050 SDA ────── I2C (shared bus)           │   │
│  │  D5  ──── MPU6050 SCL ────── I2C (shared bus)           │   │
│  │  D6  ──── GPS TX → Arduino RX (SoftwareSerial)          │   │
│  │  D7  ──── GPS RX ← Arduino TX (SoftwareSerial)          │   │
│  │  D8  ──── Motor ESC signal ── PWM (20kHz)               │   │
│  │  D9  ──── Rudder servo ────── PWM (50Hz)                │   │
│  │  D10 ──── Aileron L servo ── PWM (50Hz)                 │   │
│  │  D11 ──── Aileron R servo ── PWM (50Hz)                 │   │
│  │  D12 ──── Elevator servo ─── PWM (50Hz)                 │   │
│  │  D13 ──── Status LED ──────── Digital Out               │   │
│  │                                                          │   │
│  │  ANALOG PINS:                                            │   │
│  │                                                          │   │
│  │  A0  ──── Battery voltage ─── Voltage divider            │   │
│  │  A1  ──── Motor current ───── ACS758 output             │   │
│  │  A2  ──── Motor temp ──────── K-type thermocouple       │   │
│  │  A3  ──── Battery temp ────── NTC 10kΩ thermistor       │   │
│  │  A4  ──── OLED SDA ────────── I2C (shared bus)          │   │
│  │  A5  ──── OLED SCL ────────── I2C (shared bus)          │   │
│  │  A6  ──── Airspeed ────────── Pitot tube MPXV7002       │   │
│  │  A7  ──── Throttle pos ────── 10kΩ pot wiper            │   │
│  │                                                          │   │
│  │  POWER:                                                  │   │
│  │                                                          │   │
│  │  VIN ──── 5V from buck converter (24V → 5V, 3A)         │   │
│  │  5V  ──── I2C pullup voltage (if USB powered)           │   │
│  │  GND ──── Common ground bus                              │   │
│  │                                                          │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

### I2C Bus Schematic

```
┌─────────────────────────────────────────────────────────────────┐
│                    I2C BUS (shared D2/D3)                        │
│                                                                  │
│                    5V ─────┬─────┬─────┬─────┬─────┐            │
│                            │     │     │     │     │            │
│                         4.7kΩ  4.7kΩ 4.7kΩ 4.7kΩ 4.7kΩ        │
│                            │     │     │     │     │            │
│  ┌─────────────────────────┼─────┼─────┼─────┼─────┤            │
│  │                         │     │     │     │     │            │
│  │  ┌──────┐  ┌──────┐  ┌─┴──┐ ┌┴───┐ ┌┴───┐ ┌┴───┐          │
│  │  │BMP280│  │MPU6050│  │BMP │ │OLED│ │OLED│ │    │          │
│  │  │#1    │  │      │  │#2  │ │#1  │ │#2  │ │    │          │
│  │  │0x76  │  │0x68  │  │0x76│ │0x3C│ │0x3D│ │    │          │
│  │  └──┬───┘  └──┬───┘  └─┬──┘ └┬───┘ └┬───┘ └┬───┘          │
│  │     │         │         │     │      │      │               │
│  │     └─────────┴─────────┴─────┴──────┴──────┘               │
│  │                   SDA (D2)                                    │
│  │                                                              │
│  │     ┌──────────────────────────────────────┐                 │
│  │     └──────────────────────────────────────┘                 │
│  │                   SCL (D3)                                    │
│  │                                                              │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  NOTE: BMP280 #1 and #2 have different I2C addresses (0x76)    │
│  BMP280 #2 uses AD0 pin tied HIGH (0x77)                       │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

---

## VOLTAGE DIVIDER (Battery Monitoring)

```
┌─────────────────────────────────────────────────────────────────┐
│                    VOLTAGE DIVIDER (A0)                          │
│                                                                  │
│  Battery +24V ──────┬─────────────────────┐                    │
│                     │                     │                    │
│                   ┌─┴─┐                 ┌─┴─┐                  │
│                   │   │ R1              │   │ R2                │
│                   │   │ 90kΩ           │   │ 10kΩ              │
│                   │   │ (9× 10kΩ)      │   │                   │
│                   └─┬─┘                 └─┬─┘                  │
│                     │                     │                    │
│                     ├─────────────────────┼───→ To Arduino A0  │
│                     │                     │     (0-5V range)   │
│                     │                   ┌─┴─┐                  │
│                     │                   │   │ C1               │
│                     │                   │   │ 100nF            │
│                     │                   └─┬─┘                  │
│                     │                     │                    │
│  Battery GND ───────┴─────────────────────┴───                 │
│                                                                  │
│  VOLTAGE CALCULATION:                                            │
│  V_battery = V_A0 × (R1 + R2) / R2                            │
│  V_battery = V_A0 × (90kΩ + 10kΩ) / 10kΩ                     │
│  V_battery = V_A0 × 10                                          │
│                                                                  │
│  Range: 0-5V input → 0-50V battery                             │
│  Resolution: 50V / 1024 = 0.049V per bit                       │
│                                                                  │
│  COMPONENT VALUES:                                               │
│  R1 = 90kΩ (9× 10kΩ 1% resistors in series)                   │
│  R2 = 10kΩ (1% metal film)                                     │
│  C1 = 100nF ceramic (noise filtering)                           │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

---

## CURRENT SENSOR (Motor Current Monitoring)

```
┌─────────────────────────────────────────────────────────────────┐
│                    ACS758 CURRENT SENSOR (A1)                    │
│                                                                  │
│  Motor Power +24V ──────┬─────────────────────┐                │
│                         │                     │                │
│                    ┌────┴────┐                │                │
│                    │  ACS758 │                │                │
│                    │  200A   │                │                │
│                    │  hall-  │                │                │
│                    │  effect │                │                │
│                    │         │                │                │
│                    │  IP+ ───┘                │                │
│                    │  IP- ────────────────────┘                │
│                    │  VOUT ────┬─── 100nF ─── GND              │
│                    │           │                               │
│                    │  VCC ── 5V                                │
│                    │  GND ── GND                               │
│                    └─────────┘                                 │
│                         │                                       │
│                    ┌────▼────┐                                  │
│                    │ Arduino │                                  │
│                    │   A1    │                                  │
│                    └─────────┘                                  │
│                                                                  │
│  ACS758 SPECIFICATIONS:                                          │
│  - Range: 0-200A                                                 │
│  - Sensitivity: 10mV/A                                          │
│  - Offset: VCC/2 = 2.5V (at 0A)                                │
│  - Output: 2.5V + (current × 0.01V)                            │
│  - Arduino reading: (A1_value / 1024) × 5V                     │
│  - Current: (voltage - 2.5V) / 0.01V                           │
│                                                                  │
│  WIRING:                                                         │
│  - IP+ to motor side of power wire                              │
│  - IP- to ESC side of power wire                                │
│  - VOUT to Arduino A1                                           │
│  - Bypass capacitor: 100nF ceramic across VOUT                  │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

---

## TEMPERATURE SENSOR (Motor Temperature)

```
┌─────────────────────────────────────────────────────────────────┐
│                    K-TYPE THERMOCOUPLE (A2)                      │
│                                                                  │
│                    ┌─────────────────────────┐                  │
│                    │    K-TYPE THERMOCOUPLE   │                  │
│                    │    (mounted on motor)    │                  │
│                    │                          │                  │
│                    │  Hot junction (motor)     │                  │
│                    │  Cold junction (panel)    │                  │
│                    │                          │                  │
│                    │  Range: -200°C to +1250°C│                  │
│                    │  Accuracy: ±2°C          │                  │
│                    │  Response: 0.5s          │                  │
│                    └──────────┬──────────────┘                  │
│                               │                                 │
│                    ┌──────────▼──────────────┐                  │
│                    │    MAX6675 AMPLIFIER     │                  │
│                    │    (or simple op-amp)    │                  │
│                    │                          │                  │
│                    │  VOUT ────┬── 100nF ── GND                │
│                    │           │                                │
│                    │  VCC ── 5V                                 │
│                    │  GND ── GND                                │
│                    └──────────┬──────────────┘                  │
│                               │                                 │
│                    ┌──────────▼──────────────┐                  │
│                    │    Arduino A2            │                  │
│                    │    (analog input)        │                  │
│                    └─────────────────────────┘                  │
│                                                                  │
│  TEMPERATURE CALCULATION:                                        │
│  - K-type: 41μV/°C                                              │
│  - With MAX6675: 0.25°C resolution                               │
│  - Without amplifier: scale factor = 1250°C / 5V = 250°C/V    │
│                                                                  │
│  WARNING THRESHOLDS:                                             │
│  - Normal: < 80°C                                               │
│  - Caution: 80-100°C (reduce power)                             │
│  - Critical: > 100°C (motor shutdown)                           │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

---

## MOTOR ESC SIGNAL WIRING

```
┌─────────────────────────────────────────────────────────────────┐
│                    ESC SIGNAL WIRING (D8)                        │
│                                                                  │
│                    ┌─────────────────────────┐                  │
│                    │    Arduino D8            │                  │
│                    │    (PWM output)          │                  │
│                    └──────────┬──────────────┘                  │
│                               │                                 │
│                    ┌──────────▼──────────────┐                  │
│                    │    22AWG signal wire     │                  │
│                    │    (shielded, twisted)   │                  │
│                    └──────────┬──────────────┘                  │
│                               │                                 │
│                    ┌──────────▼──────────────┐                  │
│                    │    ESC SIGNAL INPUT      │                  │
│                    │                          │                  │
│                    │    ┌──────┐ ┌──────┐    │                  │
│                    │    │  +5V │ │  GND │    │                  │
│                    │    └──┬───┘ └──┬───┘    │                  │
│                    │       │        │         │                  │
│                    └───────┼────────┼─────────┘                  │
│                            │        │                            │
│                            │        │                            │
│                    ┌───────▼────────▼─────────┐                  │
│                    │    POWER SUPPLY           │                  │
│                    │    (from ESC BEC)         │                  │
│                    │                          │                  │
│                    │    Note: ESC provides     │                  │
│                    │    5V BEC output for      │                  │
│                    │    receiver/servos        │                  │
│                    │    Do NOT connect to      │                  │
│                    │    Arduino VIN simultaneously              │
│                    └──────────────────────────┘                  │
│                                                                  │
│  PWM SIGNAL SPECIFICATIONS:                                      │
│  - Frequency: 20kHz (for brushless ESC)                         │
│  - Throttle off: 1000μs pulse width                             │
│  - Throttle max: 2000μs pulse width                             │
│  - Neutral: 1500μs (for testing)                                │
│  - Deadband: 10μs around neutral                                │
│                                                                  │
│  ARDUINO CODE:                                                   │
│  - Use Servo library for precise PWM control                    │
│  - WriteMicroseconds(1000) = off                                │
│  - WriteMicroseconds(2000) = full throttle                       │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

---

## OLED DISPLAY CONNECTIONS

```
┌─────────────────────────────────────────────────────────────────┐
│                    OLED DISPLAYS (I2C bus)                       │
│                                                                  │
│                    ┌─────────────────────────┐                  │
│                    │    I2C BUS (shared)      │                  │
│                    │    SDA = D2              │                  │
│                    │    SCL = D3              │                  │
│                    │    VCC = 5V              │                  │
│                    │    GND = GND             │                  │
│                    └──────────┬──────────────┘                  │
│                               │                                 │
│                    ┌──────────┴──────────────┐                  │
│                    │                          │                  │
│               ┌────▼────┐              ┌─────▼────┐            │
│               │ OLED #1 │              │ OLED #2   │            │
│               │ 0.96"   │              │ 0.96"     │            │
│               │ 128×64  │              │ 128×64    │            │
│               │ addr:   │              │ addr:     │            │
│               │ 0x3C    │              │ 0x3D      │            │
│               └─────────┘              └───────────┘            │
│                                                                  │
│  OLED #1 — PRIMARY FLIGHT DISPLAY:                              │
│  ┌────────────────────────────┐                                 │
│  │  ALT:  1250 ft    SPD: 80 │                                 │
│  │  HDG:  270°       BAT: 95%│                                 │
│  │  VS:   +200 fpm   AMP: 45A│                                 │
│  │  TEMP: 65°C       MOTOR:OK│                                 │
│  └────────────────────────────┘                                 │
│                                                                  │
│  OLED #2 — SYSTEM STATUS:                                       │
│  ┌────────────────────────────┐                                 │
│  │  GPS: 12 SAT   FIX: 3D    │                                 │
│  │  LAT: 40.7128° LON: -74.00│                                 │
│  │  HDOP: 1.2     ALT: 1250ft│                                 │
│  │  TELEM: OK      TIME: 1:45│                                 │
│  └────────────────────────────┘                                 │
│                                                                  │
│  DISPLAY LIBRARY: Adafruit SSD1306                              │
│  FONT: Default Adafruit 6×8                                     │
│  UPDATE RATE: 5Hz (every 200ms)                                 │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

---

## GPS MODULE WIRING

```
┌─────────────────────────────────────────────────────────────────┐
│                    GPS MODULE (BN-220, u-blox)                   │
│                                                                  │
│                    ┌─────────────────────────┐                  │
│                    │    BN-220 GPS            │                  │
│                    │    u-blox M8N            │                  │
│                    │    10Hz update rate      │                  │
│                    └──────────┬──────────────┘                  │
│                               │                                 │
│                    ┌──────────▼──────────────┐                  │
│                    │    GPS WIRING            │                  │
│                    │                          │                  │
│                    │    VCC ──── 5V (from     │                  │
│                    │            buck conv)    │                  │
│                    │    GND ──── GND bus      │                  │
│                    │    TX  ──── Arduino D6   │                  │
│                    │    RX  ──── Arduino D7   │                  │
│                    │                          │                  │
│                    │    PPS ──── (not used)   │                  │
│                    │    EXTINT ── (not used)  │                  │
│                    └─────────────────────────┘                  │
│                                                                  │
│  GPS CONFIGURATION:                                              │
│  - Protocol: UBX (binary, efficient)                            │
│  - Baud rate: 9600 (default)                                    │
│  - Update rate: 10Hz                                             │
│  - Messages: NAV-PVT (position, velocity, time)                │
│  - Antenna: external patch antenna (included)                   │
│  - Cold start: 26s (open sky)                                   │
│  - Warm start: 2s                                               │
│  - Accuracy: 2.5m CEP (open sky)                                │
│                                                                  │
│  ANTENNA PLACEMENT:                                              │
│  - Mount on top of fuselage, clear of obstructions              │
│  - Cable: 1m GPS coax (SMA connector)                          │
│  - Ground plane: not required for patch antenna                 │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

---

## TELEMETRY RADIO (HC-12 433MHz)

```
┌─────────────────────────────────────────────────────────────────┐
│                    HC-12 TELEMETRY RADIO                         │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  AIRCRAFT SIDE (Arduino Nano #2)                          │   │
│  │                                                          │   │
│  │  ┌──────────┐         ┌──────────┐                      │   │
│  │  │ ARDUINO  │         │ HC-12    │                      │   │
│  │  │ NANO #2  │         │ RADIO    │                      │   │
│  │  │          │         │          │                      │   │
│  │  │ D6 ──────┼─────────┤ RXD      │                      │   │
│  │  │ D7 ──────┼─────────┤ TXD      │                      │   │
│  │  │ 5V ──────┼─────────┤ VCC      │                      │   │
│  │  │ GND ─────┼─────────┤ GND      │                      │   │
│  │  │          │         │          │                      │   │
│  │  │          │         │ SET ──5V │ (active: config mode)│   │
│  │  │          │         │          │                      │   │
│  │  └──────────┘         └────┬─────┘                      │   │
│  │                            │                             │   │
│  │                       ┌────┴────┐                        │   │
│  │                       │ANTENNA  │                        │   │
│  │                       │(wire,   │                        │   │
│  │                       │ 173mm)  │                        │   │
│  │                       └─────────┘                        │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  GROUND STATION (Laptop + USB-Serial adapter)            │   │
│  │                                                          │   │
│  │  ┌──────────┐         ┌──────────┐                      │   │
│  │  │ USB-SERIAL│        │ HC-12    │                      │   │
│  │  │ ADAPTER   │        │ RADIO    │                      │   │
│  │  │           │        │          │                      │   │
│  │  │ TX ───────┼────────┤ RXD      │                      │   │
│  │  │ RX ───────┼────────┤ TXD      │                      │   │
│  │  │ 5V ───────┼────────┤ VCC      │                      │   │
│  │  │ GND ──────┼────────┤ GND      │                      │   │
│  │  │           │        │          │                      │   │
│  │  │           │        │ SET ──5V │ (active)             │   │
│  │  └──────────┘        └────┬─────┘                      │   │
│  │                           │                             │   │
│  │                      ┌────┴────┐                        │   │
│  │                      │ANTENNA  │                        │   │
│  │                      │(wire,   │                        │   │
│  │                      │ 173mm)  │                        │   │
│  │                      └─────────┘                        │   │
│  │                                                          │   │
│  │  ┌──────────┐                                           │   │
│  │  │ LAPTOP   │                                           │   │
│  │  │ (ground  │                                           │   │
│  │  │ station) │                                           │   │
│  │  └──────────┘                                           │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  HC-12 CONFIGURATION:                                            │
│  - Frequency: 433.92MHz                                          │
│  - Baud rate: 9600                                               │
│  - Power: +20dBm (100mW)                                        │
│  - Range: 1.8km (urban), 5km (open field)                      │
│  - Modulation: GFSK                                             │
│  - Data format: 8N1 (8 data, no parity, 1 stop)                │
│  - Air data rate: 5000 bps                                       │
│  - Antenna: 173mm quarter-wave wire                             │
│                                                                  │
│  TELEMETRY DATA FORMAT (JSON):                                  │
│  {"alt":1250,"spd":80,"hdg":270,"bat":95,"amp":45,            │
│   "tmp":65,"gps":[40.7128,-74.0060],"fix":3}                   │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

---

## WARNING SYSTEM

```
┌─────────────────────────────────────────────────────────────────┐
│                    WARNING SYSTEM (piezo buzzers)                 │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                                                          │   │
│  │  ┌──────────┐  ┌──────────┐                             │   │
│  │  │ BUZZER   │  │ BUZZER   │                             │   │
│  │  │ #1 (cockpit)│ #2 (tail)│                             │   │
│  │  │ 5V piezo │  │ 5V piezo │                             │   │
│  │  └────┬─────┘  └────┬─────┘                             │   │
│  │       │              │                                   │   │
│  │       └──────┬───────┘                                   │   │
│  │              │                                           │   │
│  │         ┌────▼────┐                                      │   │
│  │         │ Arduino │                                      │   │
│  │         │ D8      │ (shared with ESC signal)             │   │
│  │         │         │ (or use separate pin)                │   │
│  │         └─────────┘                                      │   │
│  │                                                          │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  WARNING TONES:                                                  │
│  - Low battery: 3 short beeps, pause, repeat                    │
│  - Over temp: continuous rapid beeping                          │
│  - Stall: 2 short beeps, pause, repeat                         │
│  - GPS lost: long beep, pause, repeat                          │
│  - Motor fault: continuous tone                                 │
│                                                                  │
└────────────────────────────────────────────────────────────────────┘
```

---

## COMPLETE CIRCUIT SCHEMATIC (Simplified)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    COMPLETE CIRCUIT — SIMPLIFIED                        │
│                                                                          │
│  ┌──────────┐                                                            │
│  │ BATTERY  │                                                            │
│  │ 24V      │                                                            │
│  │ 200Ah    │                                                            │
│  └──┬───────┘                                                            │
│     │                                                                    │
│     ├──── 200A ANL FUSE ──── 300A MASTER SWITCH ────┬───────────────┐  │
│     │                                               │               │  │
│     │                                               │               │  │
│  ┌──▼──────────────┐                          ┌─────▼─────┐    ┌───▼───┐ │
│  │ MOTOR BUS       │                          │AVIONICS   │    │LIGHTS │ │
│  │ 24V, 100A       │                          │BUS 24V    │    │12V    │ │
│  │                 │                          │           │    │       │ │
│  │ ┌─────────────┐ │                          │ ┌───────┐ │    │ ┌───┐ │ │
│  │ │ 100A ANL    │ │                          │ │20A ANL│ │    │ │LED│ │ │
│  │ │ FUSE        │ │                          │ │ FUSE  │ │    │ │NAV│ │ │
│  │ └──────┬──────┘ │                          │ └───┬───┘ │    │ └───┘ │ │
│  │        │        │                          │     │     │    │       │ │
│  │   ┌────▼────┐   │                          │  ┌──▼──┐  │    │       │ │
│  │   │  MOTOR  │   │                          │  │5V   │  │    │       │ │
│  │   │  SWITCH │   │                          │  │BUCK │  │    │       │ │
│  │   │  (100A) │   │                          │  │CONV │  │    │       │ │
│  │   └────┬────┘   │                          │  └──┬──┘  │    │       │ │
│  │        │        │                          │     │     │    │       │ │
│  │   ┌────▼────┐   │                          │  ┌──▼──┐  │    │       │ │
│  │   │  ESC    │   │                          │  │ARDU-│  │    │       │ │
│  │   │  100A   │   │                          │  │INO  │  │    │       │ │
│  │   │  80V    │   │                          │  │NANO │  │    │       │ │
│  │   └────┬────┘   │                          │  │ #1  │  │    │       │ │
│  │        │        │                          │  └──┬──┘  │    │       │ │
│  │   ┌────▼────┐   │                          │     │     │    │       │ │
│  │   │ MOTOR   │   │                          │  ┌──▼──┐  │    │       │ │
│  │   │ 50kW    │   │                          │  │BMP280│ │    │       │ │
│  │   │ OUTRUN  │   │                          │  │MPU6050│ │    │       │ │
│  │   └────┬────┘   │                          │  │GPS   │ │    │       │ │
│  │        │        │                          │  │OLED  │ │    │       │ │
│  │   ┌────▼────┐   │                          │  │HC-12 │ │    │       │ │
│  │   │ PHI     │   │                          │  └──────┘ │    │       │ │
│  │   │ COILS   │   │                          │           │    │       │ │
│  │   │ 4×      │   │                          │           │    │       │ │
│  │   └─────────┘   │                          │           │    │       │ │
│  │                 │                          │           │    │       │ │
│  └─────────────────┘                          └───────────┘    └───────┘ │
│                                                                          │
│  GROUND BUS: All GND points connected to common ground bus             │
│  (4 AWG copper bar bolted to fuselage longeron)                         │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## PCB LAYOUT NOTES

### Arduino Protoboard Layout

```
┌─────────────────────────────────────────┐
│           ARDUINO NANO PROTOBOARD        │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │         ARDUINO NANO            │   │
│  │                                 │   │
│  │  D2 ──── 4.7kΩ ──── 5V (I2C)  │   │
│  │  D3 ──── 4.7kΩ ──── 5V (I2C)  │   │
│  │                                 │   │
│  │  A0 ──── voltage divider        │   │
│  │  A1 ──── 100nF cap ──── GND    │   │
│  │  A2 ──── 100nF cap ──── GND    │   │
│  │                                 │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │         COMPONENTS               │   │
│  │                                 │   │
│  │  R1 (90kΩ): 9× 10kΩ in series  │   │
│  │  R2 (10kΩ): 1× 10kΩ metal film │   │
│  │  C1 (100nF): ceramic            │   │
│  │  C2 (100nF): ceramic            │   │
│  │  C3 (10μF): electrolytic        │   │
│  │                                 │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │         CONNECTORS               │   │
│  │                                 │   │
│  │  J1: Power input (2-wire)       │   │
│  │  J2: I2C bus (4-pin)            │   │
│  │  J3: GPS (4-pin)                │   │
│  │  J4: ESC signal (3-pin)         │   │
│  │  J5: Servos (3-pin × 4)        │   │
│  │  J6: Analog inputs (8-pin)      │   │
│  │                                 │   │
│  └─────────────────────────────────┘   │
│                                         │
└─────────────────────────────────────────┘
```

---

## CIRCUIT PROTECTION

| Protection | Component | Value | Purpose |
|------------|-----------|-------|---------|
| Main fuse | ANL 200A | 200A | Battery short circuit |
| Motor fuse | ANL 100A | 100A | Motor/ESC fault |
| Avionics fuse | ANL 20A | 20A | Avionics short |
| ESD protection | TVS diode | 5V | Arduino input protection |
| Reverse polarity | Schottky diode | 40V 1A | Power input protection |
| Noise filtering | Ferrite bead | 100MHz | Signal line filtering |
| Decoupling | Ceramic cap | 100nF | IC power filtering |
