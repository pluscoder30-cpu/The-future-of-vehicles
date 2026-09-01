# PHI SUPER GOGGLES — WIRING DIAGRAM

## Complete Wiring and Interconnection Guide

---

## SYSTEM WIRING OVERVIEW

```
SENSOR BLOCK (8× Triaxial EMF)
┌────────────────────────────────────────────────────────────────┐
│ EMF1 ──[100Ω]──► MUX1-A0                                      │
│ EMF2 ──[100Ω]──► MUX1-A1                                      │
│ EMF3 ──[100Ω]──► MUX1-A2                                      │
│ EMF4 ──[100Ω]──► MUX1-A3                                      │
│ EMF5 ──[100Ω]──► MUX1-A4                                      │
│ EMF6 ──[100Ω]──► MUX1-A5                                      │
│ EMF7 ──[100Ω]──► MUX1-A6                                      │
│ EMF8 ──[100Ω]──► MUX1-A7                                      │
│                                                                │
│ Each sensor: VCC→3.3V (via ferrite), GND→AGND, OUT→MUX       │
└────────────────────────────────────────────────────────────────┘

MULTIPLEXER BLOCK
┌────────────────────────────────────────────────────────────────┐
│ MUX1 (CD74HC4067): COM→ADC1-AIN0, S0-S3→FPGA GPIO[20:23]    │
│ MUX2 (CD74HC4067): COM→ADC1-AIN1, S0-S3→FPGA GPIO[24:27]    │
│ MUX3 (CD74HC4067): COM→ADC2-AIN0, S0-S3→FPGA GPIO[28:31]    │
│ MUX4 (CD74HC4067): COM→ADC2-AIN1, S0-S3→FPGA GPIO[32:35]    │
│ EN lines: MUX1→GPIO[36], MUX2→GPIO[37], MUX3→GPIO[38], MUX4→GPIO[39] │
└────────────────────────────────────────────────────────────────┘

ADC BLOCK
┌────────────────────────────────────────────────────────────────┐
│ ADC1 (ADS1256): AIN0←MUX1, AIN1←MUX2, AIN2←BatMon, AIN3←Temp │
│   SPI: SCLK←GPIO[0], DIN←GPIO[1], DOUT→GPIO[2], DRDY→GPIO[3], CS←GPIO[4] │
│                                                                │
│ ADC2 (ADS1256): AIN0←MUX3, AIN1←MUX4, AIN2←IMU, AIN3←Mic    │
│   SPI: SCLK←GPIO[5], DIN←GPIO[6], DOUT→GPIO[7], DRDY→GPIO[8], CS←GPIO[9] │
│                                                                │
│ VREF: REF5025 (2.5V) → ADC1 VREF                              │
└────────────────────────────────────────────────────────────────┘

FPGA BLOCK (DE10-Lite)
┌────────────────────────────────────────────────────────────────┐
│ GPIO[0:9]    → ADC1 SPI Bus                                    │
│ GPIO[10:19]  → ADC2 SPI Bus                                    │
│ GPIO[20:35]  → MUX Select Lines (S0-S3 × 4)                   │
│ GPIO[36:39]  → MUX Enable Lines                                │
│ GPIO[40:47]  → Button Inputs (active low, 10kΩ pull-up)       │
│ GPIO[48:49]  → Rotary Encoder (A, B)                           │
│ GPIO[50:51]  → Haptic Motors (PWM)                             │
│ GPIO[52]     → Buzzer (PWM)                                    │
│ GPIO[53]     → WS2812B LEDs (data)                             │
│ GPIO[76:79]  → BNO055 IMU (I2C: SDA, SCL, INT, RST)          │
│ HDMI TX      → ADV7533 #1 → Left OLED                         │
│ HDMI TX      → ADV7533 #2 → Right OLED                        │
│ SPI          → SD Card (MOSI, MISO, SCK, CS)                   │
└────────────────────────────────────────────────────────────────┘

POWER BLOCK
┌────────────────────────────────────────────────────────────────┐
│ USB-C PD → TP5100 Charger → FPB-5 Battery (3.7V 8000mAh)        │
│                         → LM2596 #1 → 5V Rail A (Sensors/ADC) │
│                         → LM2596 #2 → 5V Rail B (Displays)    │
│                         → AMS1117 #1 → 3.3V (FPGA)            │
│                         → AMS1117 #2 → 3.3V (Sensors)         │
│                         → AMS1117 #3 → 3.3V (IMU/SD)          │
│                                                                │
│ Ground: AGND + DGND + PGND → Single point at power entry      │
└────────────────────────────────────────────────────────────────┘
```

---

## SENSOR WIRING DETAIL

Each EMF sensor (ML8511) has 4 connections:

```
ML8511 Pinout:
  VCC (1) ──[Ferrite 100Ω]── 3.3V Rail
  GND (2) ── AGND
  OUT (3) ──[100Ω]── MUX-Ax
  EN  (4) ── 3.3V (always enabled)

Bypass: 0.1μF ceramic cap from VCC to GND (at sensor)
```

---

## ADC SPI BUS

```
DE10-Lite GPIO ──────────── ADS1256
GPIO[0]        ──── SCLK ── SCLK
GPIO[1]        ──── MOSI ── DIN
GPIO[2]        ──── MISO ── DOUT
GPIO[3]        ──── DRDY ── DRDY (active low)
GPIO[4]        ──── CS   ── CS (active low)

SPI Mode: 1 (CPOL=0, CPHA=1)
Max Clock: 20 MHz
```

---

## DISPLAY INTERFACE

```
FPGA HDMI ──► ADV7533 ──► MIPI DSI ──► OLED (30-pin FPC)
  TX0±, TX1±, TX2±, CLK±    (2 data lanes)

Display Parameters:
  Resolution: 1920×1080 per eye
  Refresh: 60Hz
  Color: 24-bit RGB
```

---

## IMU (BNO055) WIRING

```
GPIO[76] (I2C_SDA) ──── SDA (4.7kΩ pull-up to 3.3V)
GPIO[77] (I2C_SCL) ──── SCL (4.7kΩ pull-up to 3.3V)
3.3V Rail ───────────── VCC
AGND ────────────────── GND
GPIO[78] ────────────── INT
GPIO[79] ────────────── RST

I2C Address: 0x28, Speed: 400 kHz
```

---

## BUTTON WIRING

```
GPIO[40] ──── BTN_UP (10kΩ pull-up to 3.3V)
GPIO[41] ──── BTN_DOWN
GPIO[42] ──── BTN_LEFT
GPIO[43] ──── BTN_RIGHT
GPIO[44] ──── BTN_SELECT
GPIO[45] ──── BTN_BACK
GPIO[46] ──── BTN_MODE
GPIO[47] ──── BTN_BRIGHT

All: Momentary, normally open, active low
Debounce: 20ms software

Rotary Encoder:
GPIO[48] ──── CLK (10kΩ pull-up)
GPIO[49] ──── DT (10kΩ pull-up)
```

---

## GROUNDING STRATEGY

```
                    ┌─────────────┐
                    │ Power Entry │
                    │   Point     │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
         ┌────┴────┐  ┌───┴───┐  ┌────┴────┐
         │  AGND   │  │  DGND │  │  PGND   │
         │ (Analog)│  │(Digital)│ │ (Power) │
         └─────────┘  └───────┘  └─────────┘

Rules:
1. All grounds meet at ONE point
2. Never connect AGND and DGND at multiple points
3. Use star grounding topology
4. Keep analog traces away from digital traces
```

---

## WIRING COLOR CODE

| Color | Purpose |
|-------|---------|
| Red | 5V Power |
| Orange | 3.3V Power |
| Yellow | Signal (analog) |
| Green | Signal (digital) |
| Blue | SPI SCLK |
| Purple | SPI MOSI/MISO |
| White | I2C SDA |
| Gray | I2C SCL |
| Black | Ground |
| Brown | Battery positive |

---

## WIRING CHECKLIST

- [ ] All 8 EMF sensors connected to MUX1
- [ ] MUX1 COM → ADC1 AIN0
- [ ] MUX2 COM → ADC1 AIN1
- [ ] ADC1 SPI → FPGA GPIO[0:4]
- [ ] ADC2 SPI → FPGA GPIO[5:9]
- [ ] MUX select → FPGA GPIO[20:35]
- [ ] MUX enable → FPGA GPIO[36:39]
- [ ] All buttons with pull-ups to GPIO[40:47]
- [ ] Rotary encoder to GPIO[48:49]
- [ ] Haptic motors to GPIO[50:51]
- [ ] Buzzer to GPIO[52]
- [ ] LEDs to GPIO[53]
- [ ] BNO055 via I2C to GPIO[76:79]
- [ ] Left OLED via ADV7533 to FPGA HDMI
- [ ] Right OLED via ADV7533 to FPGA HDMI
- [ ] SD card via SPI to FPGA
- [ ] USB-C for charging
- [ ] Battery via JST-XH
- [ ] All power rails verified (5V, 3.3V)
- [ ] Ground continuity verified
- [ ] No shorts between power and ground
