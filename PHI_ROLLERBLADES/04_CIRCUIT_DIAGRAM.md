# PHI_ROLLERBLADES — Electronic Circuit Diagram

## Per-Boot Circuit

```
    ┌─────────────────────────────────────────────────────────────┐
    │                    PHI-ROLLERBLADE CIRCUIT (per boot)        │
    └─────────────────────────────────────────────────────────────┘

    36V BATTERY (+) ──┬── FUSE 10A ── ESC 10A ── HUB MOTOR 200W
                      │
                      ├── LM2596 Buck ── 5V ── Arduino Nano
                      │                    ── MPU-6050 IMU
                      │                    ── OLED Display
                      │
                      └── CHARGING PORT (XT30)

    36V BATTERY (-) ──┴── BMS ── Common GND
```

## ESC & Motor Wiring

```
    ┌─────────────────────────────────────────┐
    │  ESC (36V 10A Brushless)                │
    │                                         │
    │  BATTERY+ ◄═══ 36V+                     │
    │  BATTERY- ◄═══ 36V-                     │
    │  MOTOR U  ────► Phase U (Blue)          │
    │  MOTOR V  ────► Phase V (Green)         │
    │  MOTOR W  ────► Phase W (Yellow)        │
    │  THROTTLE ◄──── Arduino D9 (PWM)        │
    │  HALL U/V/W ◄── Hall sensors            │
    │  5V OUT   ────► Hall sensor VCC         │
    │  GND      ────► Common ground           │
    └─────────────────────────────────────────┘
```

## Arduino Controller Wiring

```
    ┌─────────────────────────────────────────────────────────────┐
    │              ARDUINO NANO (per boot)                         │
    │                                                              │
    │  VIN ◄─── 5V from LM2596 Buck                              │
    │  GND ────► Common Ground                                     │
    │                                                              │
    │  A0 ◄──── FSR (lean sensor) — via voltage divider           │
    │  A1 ◄──── Battery Voltage Divider                           │
    │                                                              │
    │  D2 ◄──── MPU-6050 INT                                      │
    │  D3 ◄──── Power Button (optional)                           │
    │  D9 ──── PWM ────► ESC Throttle                             │
    │                                                              │
    │  D10 ──── I2C SDA ────► MPU-6050 SDA                       │
    │  D11 ──── I2C SCL ────► MPU-6050 SCL                       │
    │                ├───────► OLED SDA (optional)                │
    │                └───────► OLED SCL (optional)                │
    │                                                              │
    │  D12 ──── HC-05 Bluetooth TX                                 │
    │  D13 ◄─── HC-05 Bluetooth RX                                 │
    │                                                              │
    └─────────────────────────────────────────────────────────────┘
```

## Sensor Wiring

```
    FSR (Force Sensitive Resistor):
    ┌─────────────────────────────────────────┐
    │  5V ──┬── FSR ──┬── A0 (Arduino)       │
    │        │         │                       │
    │        └── 10kΩ ──┴── GND               │
    │                                          │
    │  Output: 0-5V proportional to pressure  │
    │  Threshold: >2.5V = "lean forward"      │
    └─────────────────────────────────────────┘

    MPU-6050 IMU:
    ┌─────────────────────────────────────────┐
    │  VCC ◄── 5V                              │
    │  GND ──── GND                            │
    │  SDA ──── Arduino D10 (A4)               │
    │  SCL ──── Arduino D11 (A5)               │
    │  INT ──── Arduino D2                     │
    │                                          │
    │  Detects: Forward lean angle             │
    │  Threshold: >10° forward = "go"          │
    └─────────────────────────────────────────┘

    Battery Voltage Divider:
    ┌─────────────────────────────────────────┐
    │  36V ──┬── 33kΩ ──┬── A1 (Arduino)     │
    │         │           │                    │
    │         └── 3.3kΩ ──┴── GND             │
    │                                          │
    │  V_out = 36V × (3.3k / 36.3k) = 3.28V  │
    └─────────────────────────────────────────┘
```

## Inter-Boot Bluetooth Communication

```
    LEFT BOOT (Master):
    ┌─────────────────────────────────────────┐
    │  HC-05 Bluetooth Module                  │
    │  TX ──── Arduino D12                    │
    │  RX ◄─── Arduino D13                    │
    │  VCC ◄── 5V                              │
    │  GND ──── GND                            │
    └──────────────────┬──────────────────────┘
                       │
                       │ Wireless (2.4GHz)
                       │
    RIGHT BOOT (Slave):
    ┌──────────────────┴──────────────────────┐
    │  HC-05 Bluetooth Module                  │
    │  TX ──── Arduino D12                    │
    │  RX ◄─── Arduino D13                    │
    │  VCC ◄── 5V                              │
    │  GND ──── GND                            │
    └─────────────────────────────────────────┘

    Protocol:
    Left boot sends throttle byte (0-255)
    Right boot receives and applies same throttle
    Sync rate: 50Hz
```

## Component Summary

| Component | Value | Rating | Qty |
|-----------|-------|--------|-----|
| ESC | 36V 10A Brushless | 360W max | 2 |
| Hub Motor | 200W 36V 80mm | 5.6A nominal | 2 |
| Arduino Nano | ATmega328P | 5V | 2 |
| MPU-6050 | 6-axis IMU | I2C | 2 |
| FSR | Force Sensitive Resistor | 40mm round | 2 |
| HC-05 | Bluetooth Module | 2.4GHz | 2 |
| LM2596 | Buck Converter | 36V→5V, 3A | 2 |
| OLED | SSD1306 128×64 | I2C | 1 |
| Fuse | 10A blade | Automotive | 2 |
| XT30 | Battery Connector | 30A | 4 |
