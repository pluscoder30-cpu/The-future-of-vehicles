# PHI_SKATEBOARD — Electronic Circuit Diagram

## Full Circuit Schematic

```
    ┌─────────────────────────────────────────────────────────────────────────┐
    │                    PHI-SKATEBOARD CIRCUIT                               │
    └─────────────────────────────────────────────────────────────────────────┘

    36V BATTERY (+) ─────┬─────────────────────────────────────────────────────┐
                        │                                                     │
                    ┌───┴───┐                                                 │
                    │FUSE   │ 30A                                            │
                    │BLADE  │                                                │
                    └───┬───┘                                                │
                        │                                                    │
    ┌───────────────────┤  36V POWER BUS                                     │
    │                   │                                                    │
    │   ┌───────────────┴──────────────────────────────────────────────┐     │
    │   │                                                              │     │
    │   │   ┌──────────────────┐    ┌──────────────────────────┐      │     │
    │   │   │                  │    │                          │      │     │
    │   │   │    ESC 500W      │    │    HUB MOTOR             │      │     │
    │   │   │    36V BRUSHLESS │    │    500W 36V 90mm         │      │     │
    │   │   │                  │    │                          │      │     │
    │   │   │  BATTERY+ ◄═══ 36V+   │  Phase U ──────── Blue  │      │     │
    │   │   │  BATTERY- ◄═══ 36V-   │  Phase V ──────── Green │      │     │
    │   │   │                  │    │  Phase W ──────── Yellow │      │     │
    │   │   │  MOTOR U ────────┼────►                          │      │     │
    │   │   │  MOTOR V ────────┼────►  Hall Sensors:           │      │     │
    │   │   │  MOTOR W ────────┼────►  U ←──── HALL U          │      │     │
    │   │   │                  │    │  V ←──── HALL V          │      │     │
    │   │   │  THROTTLE ◄──────┤    │  W ←──── HALL W          │      │     │
    │   │   │  BRAKE    ◄──────┤    │                          │      │     │
    │   │   │                  │    │  VCC ←── 5V (from ESC)   │      │     │
    │   │   │  5V OUT ─────────┼────►  GND ──── GND           │      │     │
    │   │   │                  │    │                          │      │     │
    │   │   └──────────────────┘    └──────────────────────────┘      │     │
    │   │                                                              │     │
    │   └──────────────────────────────────────────────────────────────┘     │
    │                                                                        │
    │                                                                        │
    │   ┌────────────────────────────────────────────────────────────────┐   │
    │   │                    ARDUINO NANO CONTROLLER                      │   │
    │   │                    (Battery Display Driver)                     │   │
    │   │                                                                │   │
    │   │   VIN ◄─── 5V from LM2596 Buck                                │   │
    │   │   GND ────► Common Ground                                      │   │
    │   │                                                                │   │
    │   │   A4 ──── I2C SDA ────► OLED Display SDA                      │   │
    │   │   A5 ──── I2C SCL ────► OLED Display SCL                      │   │
    │   │                                                                │   │
    │   │   A0 ◄──── Battery Voltage Divider                             │   │
    │   │                                                                │   │
    │   │   D2 ◄──── Power Button (pull-up 10kΩ to 5V)                  │   │
    │   │   D3 ◄──── Brake Signal from ESC                               │   │
    │   │                                                                │   │
    │   └────────────────────────────────────────────────────────────────┘   │
    │                                                                        │
    │                                                                        │
    │   ┌────────────────────────────────────────────────────────────────┐   │
    │   │                    POWER REGULATION                            │   │
    │   │                                                                │   │
    │   │   36V ──────► LM2596 Buck ──────► 5V  (for Arduino, OLED)     │   │
    │   │                                                                │   │
    │   │   ┌──────────────────────────────────────────────────────┐    │   │
    │   │   │  VOLTAGE DIVIDER (Battery Monitor)                    │    │   │
    │   │   │                                                      │    │   │
    │   │   │  36V ──┬── R1 (33kΩ) ──┬── A0 (Arduino)            │    │   │
    │   │   │        │                │                            │    │   │
    │   │   │        └── R2 (3.3kΩ) ──┴── GND                    │    │   │
    │   │   │                                                      │    │   │
    │   │   │  V_out = 36V × (3.3k / (33k + 3.3k)) = 3.33V       │    │   │
    │   │   │  Safe for Arduino ADC (max 5V)                       │    │   │
    │   │   └──────────────────────────────────────────────────────┘    │   │
    │   │                                                                │   │
    │   └────────────────────────────────────────────────────────────────┘   │
    │                                                                        │
    │                                                                        │
    │   ┌────────────────────────────────────────────────────────────────┐   │
    │   │                  BATTERY CHARGING                               │   │
    │   │                                                                │   │
    │   │   GX16 4-Pin Charging Port                                     │   │
    │   │   ┌──────────────┐                                             │   │
    │   │   │ Pin 1: B+    │──► 36V+ (through fuse)                     │   │
    │   │   │ Pin 2: B-    │──► 36V- (GND)                               │   │
    │   │   │ Pin 3: NC    │                                              │   │
    │   │   │ Pin 4: NC    │                                              │   │
    │   │   └──────────────┘                                             │   │
    │   │                                                                │   │
    │   │   36V 2A LiFePO4 Charger (external)                           │   │
    │   │   Charge time: 3 hours (0→100%)                                │   │
    │   │                                                                │   │
    │   └────────────────────────────────────────────────────────────────┘   │
    │                                                                        │
    36V BATTERY (-) ─────┴────────────────────────────────────────────────────┘
                                                                              GND
```

## ESC Internal Block Diagram

```
    ┌─────────────────────────────────────────────────────┐
    │                ESC BLOCK DIAGRAM                     │
    │                                                     │
    │   36V IN ──┬──► Voltage Regulator ──► 5V (hall)     │
    │            │                                        │
    │            │   ┌─────────────────────┐              │
    │            │   │   MCU (STM32 or     │              │
    │            │   │   ATmega)           │              │
    │            │   │                     │              │
    │            │   │  ◄── Throttle PWM   │              │
    │            │   │  ◄── Brake Signal   │              │
    │            │   │  ◄── Hall U/V/W     │              │
    │            │   │  ──► Gate Drivers   │              │
    │            │   └─────────┬───────────┘              │
    │            │             │                          │
    │            │   ┌─────────┴───────────┐              │
    │            │   │  3-PHASE INVERTER    │              │
    │            │   │                     │              │
    │            │   │  Q1  Q3  Q5 (high)  │              │
    │            │   │  │   │   │          │              │
    │            │   │  ├───┼───┤          │              │
    │            │   │  │   │   │          │              │
    │            │   │  Q2  Q4  Q6 (low)   │              │
    │            │   │  │   │   │          │              │
    │            │   │  U   V   W ──────►  Motor Phases   │
    │            │   └─────────────────────┘              │
    │            │                                        │
    │            └──► Regenerative Braking Circuit         │
    │                                                     │
    └─────────────────────────────────────────────────────┘
```

## Component Values Summary

| Component | Value | Rating | Quantity |
|-----------|-------|--------|----------|
| ESC | 36V 500W Brushless | 15A continuous | 1 |
| Hub Motor | 500W 36V 90mm | 13.9A nominal | 1 |
| Hall Sensors | Internal to motor | 3-phase | 3 |
| Bluetooth Remote | 2.4GHz | 10m range | 1 |
| Controller | Arduino Nano | ATmega328P | 1 |
| OLED Display | SSD1306 | 128×64 I2C | 1 |
| Buck Converter | LM2596 | 36V→5V, 3A | 1 |
| Voltage Divider R1 | 33kΩ | 1/4W | 1 |
| Voltage Divider R2 | 3.3kΩ | 1/4W | 1 |
| Fuse | 30A blade | Automotive | 1 |
| Power Switch | 60A rocker | Panel mount | 1 |
