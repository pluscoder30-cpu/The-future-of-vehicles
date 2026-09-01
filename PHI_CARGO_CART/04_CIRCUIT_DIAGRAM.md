# PHI_CARGO_CART — Electronic Circuit Diagram

## Full Circuit Schematic

```
    ┌─────────────────────────────────────────────────────────────────────────┐
    │                    PHI-CARGO_CART CIRCUIT                                │
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
    │   │   │    ESC 25A       │    │    HUB MOTOR             │      │     │
    │   │   │    36V BRUSHLESS │    │    500W 36V 16"          │      │     │
    │   │   │                  │    │                          │      │     │
    │   │   │  BATTERY+ ◄══ 36V+   │  Phase U ──────── Blue   │      │     │
    │   │   │  BATTERY- ◄══ 36V-   │  Phase V ──────── Green  │      │     │
    │   │   │                  │    │  Phase W ──────── Yellow │      │     │
    │   │   │  MOTOR U ────────┼────►                          │      │     │
    │   │   │  MOTOR V ────────┼────►  Hall Sensors:           │      │     │
    │   │   │  MOTOR W ────────┼────►  U ←──── HALL U          │      │     │
    │   │   │                  │    │  V ←──── HALL V          │      │     │
    │   │   │  THROTTLE ◄──────┤    │  W ←──── HALL W          │      │     │
    │   │   │  BRAKE    ◄──────┤    │                          │      │     │
    │   │   │                  │    │  VCC ←── 5V (ESC)        │      │     │
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
    │   │   VIN ◄─── 5V from ESC                                         │   │
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
    │   │   36V 5A LiFePO4 Charger (external)                           │   │
    │   │   Charge time: 4 hours (0→100%)                                │   │
    │   │                                                                │   │
    │   └────────────────────────────────────────────────────────────────┘   │
    │                                                                        │
    36V BATTERY (-) ─────┴────────────────────────────────────────────────────┘
                                                                              GND
```

## Component Values Summary

| Component | Value | Rating | Quantity |
|-----------|-------|--------|----------|
| ESC | 36V 25A Brushless | 900W max | 1 |
| Hub Motor | 500W 36V 16" | 13.9A nominal | 1 |
| Hall Sensors | Internal to motor | 3-phase | 3 |
| Bluetooth Remote | 2.4GHz | 10m range | 1 |
| Controller | Arduino Nano | ATmega328P | 1 |
| OLED Display | SSD1306 | 128×64 I2C | 1 |
| Voltage Divider R1 | 33kΩ | 1/4W | 1 |
| Voltage Divider R2 | 3.3kΩ | 1/4W | 1 |
| Fuse | 30A blade | Automotive | 1 |
| Power Switch | 60A rocker | Panel mount | 1 |
| Charger | 36V 5A LiFePO4 | CC/CV | 1 |
