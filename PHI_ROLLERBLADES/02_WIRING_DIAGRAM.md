# PHI_ROLLERBLADES — Wiring Diagram

## Main Power Distribution (Per Boot)

```
                    ┌─────────────────────────────────────────────┐
                    │              BATTERY PACK 36V               │
                    │         (10S LiFePO4, 5Ah)                 │
                    │  ┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐│
                    │  │3.2││3.2││3.2││3.2││3.2││3.2││3.2││3.2││
                    │  └───┘└───┘└───┘└───┘└───┘└───┘└───┘└───┘│
                    │  ┌───┐┌───┐                               │
                    │  │3.2││3.2│   (10 cells in series)        │
                    │  └───┘└───┘                               │
                    └──────────────┬──────────┬──────────────────┘
                                   │          │
                               B+ │          │ B-
                                   │          │
                          ┌────────┘          └────────┐
                          │                           │
                     ┌────┴────┐                 ┌────┴────┐
                     │  FUSE   │                 │  BMS    │
                     │  10A    │                 │  Board  │
                     └────┬────┘                 └────┬────┘
                          │                           │
                    ┌─────┴───────────────────────────┴─────┐
                    │            MAIN POWER BUS 36V          │
                    │  ═══════════════════════════════════════│
                    └──────┬──────────┬──────────┬──────────┘
                           │          │          │
                      ┌────┘     ┌────┘     ┌────┘
                      │          │          │
                 ┌────┴───┐ ┌───┴────┐ ┌───┴────┐
                 │  ESC   │ │CHARGER │ │POWER   │
                 │ 10A    │ │PORT    │ │SWITCH  │
                 └────┬───┘ └────────┘ └────────┘
                      │
                 ┌────┴───┐
                 │  HUB   │
                 │ MOTOR  │
                 │ 200W   │
                 │36V     │
                 └────────┘
```

## Complete Skate Wiring (Both Boots)

```
    LEFT BOOT:
    ┌─────────────────────────────────────────────────────────┐
    │                                                          │
    │  CALF-MOUNTED BATTERY:                                   │
    │  ┌──────────────────────────────────────────┐           │
    │  │  36V 5Ah LiFePO4                        │           │
    │  │  Nylon pouch, Velcro strap to calf       │           │
    │  │  XT30 connector to boot                  │           │
    │  └────────────────────┬─────────────────────┘           │
    │                       │                                  │
    │                       ▼                                  │
    │  BOOT:                                                   │
    │  ┌──────────────────────────────────────────┐           │
    │  │                                          │           │
    │  │  ┌────────────┐                          │           │
    │  │  │  ESC 10A   │                          │           │
    │  │  │  36V       │                          │           │
    │  │  │            │                          │           │
    │  │  │  BAT+ ◄══ 36V+                        │           │
    │  │  │  BAT- ◄══ 36V-                        │           │
    │  │  │  MOT U/V/W ────► Hub Motor            │           │
    │  │  │  THROTTLE ◄──── Lean Sensor (FSR)     │           │
    │  │  │  HALL U/V/W ◄── Hall Sensors          │           │
    │  │  └────────────┘                          │           │
    │  │                                          │           │
    │  │  ┌────────────┐    ┌────────────┐       │           │
    │  │  │ Arduino    │    │ MPU-6050   │       │           │
    │  │  │ Nano       │◄──►│ IMU        │       │           │
    │  │  │            │    │ (lean      │       │           │
    │  │  │ A0 ◄── FSR │    │  sensor)   │       │           │
    │  │  │ A1 ◄── V batt│   └────────────┘       │           │
    │  │  └────────────┘                          │           │
    │  │                                          │           │
    │  │  ┌────────────┐                          │           │
    │  │  │  HUB MOTOR │                          │           │
    │  │  │  200W 36V  │                          │           │
    │  │  │  80mm wheel│                          │           │
    │  │  │  phi-      │                          │           │
    │  │  │  harmonic  │                          │           │
    │  │  └────────────┘                          │           │
    │  │                                          │           │
    │  └──────────────────────────────────────────┘           │
    │                                                          │
    └─────────────────────────────────────────────────────────┘

    RIGHT BOOT: (identical to left)
    ┌─────────────────────────────────────────────────────────┐
    │  Same components, same wiring                           │
    │  Independent battery and ESC                            │
    │  Synchronized via wireless (Bluetooth)                  │
    └─────────────────────────────────────────────────────────┘
```

## Lean Sensor Wiring

```
    ┌─────────────────────────────────────────────────────────┐
    │              LEAN-TO-ACTIVATE SYSTEM                     │
    │                                                          │
    │  FSR (Force Sensitive Resistor) in toe area:            │
    │  ┌──────────────────────────────────────────┐           │
    │  │                                          │           │
    │  │  FSR ──┬── R1 (10kΩ) ──┬── Arduino A0   │           │
    │  │        │                │                 │           │
    │  │        └── 5V          └── GND           │           │
    │  │                                          │           │
    │  │  Output: 0-5V proportional to pressure   │           │
    │  │  Threshold: >2.5V = "lean forward"       │           │
    │  │                                          │           │
    │  └──────────────────────────────────────────┘           │
    │                                                          │
    │  IMU (MPU-6050) for lean angle detection:               │
    │  ┌──────────────────────────────────────────┐           │
    │  │                                          │           │
    │  │  SDA ──── Arduino A4                     │           │
    │  │  SCL ──── Arduino A5                     │           │
    │  │  VCC ◄── 5V                              │           │
    │  │  GND ──── GND                            │           │
    │  │  INT ──── Arduino D2                     │           │
    │  │                                          │           │
    │  │  Detects: Forward lean angle             │           │
    │  │  Threshold: >10° forward = "go"          │           │
    │  │                                          │           │
    │  └──────────────────────────────────────────┘           │
    │                                                          │
    │  COMBINED LOGIC:                                         │
    │  Motor activates when: FSR > 2.5V AND lean > 10°        │
    │  Motor stops when: FSR < 1.0V OR lean < 5°              │
    │                                                          │
    └─────────────────────────────────────────────────────────┘
```

## Inter-Boot Communication

```
    ┌─────────────────────────────────────────────────────────┐
    │              BLUETOOTH SYNCHRONIZATION                    │
    │                                                          │
    │  LEFT BOOT (Master):                                    │
    │  ┌──────────────────────────────────────────┐           │
    │  │  HC-05 Bluetooth Module                  │           │
    │  │  TX ──── Arduino D10                     │           │
    │  │  RX ◄─── Arduino D11                     │           │
    │  │  VCC ◄── 5V                              │           │
    │  │  GND ──── GND                            │           │
    │  └────────────────────┬─────────────────────┘           │
    │                       │                                  │
    │                       │ Wireless (2.4GHz)               │
    │                       │                                  │
    │  RIGHT BOOT (Slave):                                    │
    │  ┌────────────────────┴─────────────────────┐           │
    │  │  HC-05 Bluetooth Module                  │           │
    │  │  TX ──── Arduino D10                     │           │
    │  │  RX ◄─── Arduino D11                     │           │
    │  │  VCC ◄── 5V                              │           │
    │  │  GND ──── GND                            │           │
    │  └──────────────────────────────────────────┘           │
    │                                                          │
    │  SYNCHRONIZATION:                                        │
    │  Left boot sends throttle level to right boot           │
    │  Both motors receive same throttle command              │
    │  Ensures equal power to both feet                       │
    │                                                          │
    └─────────────────────────────────────────────────────────┘
```

## Connectors Key

| Symbol | Connector Type |
|--------|----------------|
| ═══ | 16AWG Silicone Wire (power) |
| ─── | 22AWG Silicone Wire (signal) |
| ┌─┐ | Solder Joint (heat-shrink insulated) |
| └─┘ | XT30 Connector |
| ─┬─ | JST-PH Connector |
