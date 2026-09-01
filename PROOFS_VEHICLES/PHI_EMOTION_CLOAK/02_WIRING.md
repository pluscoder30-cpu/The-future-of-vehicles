# PHI EMOTION CLOAK — WIRING DIAGRAM
## Buildable Documentation | Electrical Connections

---

## SYSTEM OVERVIEW

```
                    ┌─────────────────────────────────────────────────┐
                    │           PHI EMOTION CLOAK                     │
                    │  ┌─────────────────────────────────────────┐   │
                    │  │         RASPBERRY PI 4 (4GB)            │   │
                    │  │  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────────┐  │   │
                    │  │  │GPU  │ │CPU  │ │RAM  │ │WiFi/BLE │  │   │
                    │  │  │VideoCore│BCM2711│4GB  │ │802.11ac │  │   │
                    │  │  └──┬──┘ └──┬──┘ └──┬──┘ └────┬────┘  │   │
                    │  │     │       │       │         │        │   │
                    │  │  ┌──┴───────┴───────┴─────────┴──┐     │   │
                    │  │  │       GPIO HEADER              │     │   │
                    │  │  │       (40 pins)                │     │   │
                    │  │  └──────────────────────────────┘     │   │
                    │  └─────────────────────────────────────────┘   │
                    │                    │                           │
                    │                    │ I2C/SPI/UART/I2S          │
                    │                    │                           │
                    │  ┌─────────────────┴──────────────────────┐   │
                    │  │           SENSOR BUS                     │   │
                    │  │    (I2C + SPI + I2S + Analog)           │   │
                    │  └─────────────────┬──────────────────────┘   │
                    │                    │                           │
                    │  ┌─────────────────┼────────────────────────┐ │
                    │  │                 │                        │ │
                    │  │  ┌──────────────┴──────────┐  ┌─────────┴──┐ │
                    │  │  │    EEG SYSTEM           │  │  PPG/GSR   │ │
                    │  │  │    ADS1299 (8-ch)       │  │  Sensors   │ │
                    │  │  │    (SPI: CS0)           │  │  (I2C)     │ │
                    │  │  └──────────────┬──────────┘  └─────────┬──┘ │
                    │  │                 │                        │ │
                    │  │  ┌──────────────┴──────────┐  ┌─────────┴──┐ │
                    │  │  │  Camera System          │  │  Audio     │ │
                    │  │  │  OV2640 NIR (CSI)       │  │  System    │ │
                    │  │  │  FLIR Lepton (SPI: CS1) │  │  (I2S)     │ │
                    │  │  └──────────────┬──────────┘  └─────────┬──┘ │
                    │  │                 │                        │ │
                    │  │  ┌──────────────┴──────────┐  ┌─────────┴──┐ │
                    │  │  │  Projection System      │  │  tDCS      │ │
                    │  │  │  LED/Peltier/Vibration  │  │  Stimulator│ │
                    │  │  │  (GPIO + PWM)           │  │  (UART)    │ │
                    │  │  └─────────────────────────┘  └────────────┘ │
                    │  └──────────────────────────────────────────────┘
                    │                    │
                    │  ┌─────────────────┴──────────────────────┐   │
                    │  │           POWER SYSTEM                  │   │
                    │  │  2x 18650 (6000mAh) + Boost Converter  │   │
                    │  └─────────────────────────────────────────┘   │
                    └─────────────────────────────────────────────────┘
```

---

## DETAILED WIRING TABLE

### SPI Bus (High-Speed Sensors)

| Device | MOSI | MISO | SCLK | CS | VCC | GND |
|--------|------|------|------|----|----|-----|
| ADS1299 EEG | GPIO 10 (MOSI) | GPIO 9 (MISO) | GPIO 11 (SCLK) | GPIO 8 (CE0) | 3.3V | GND |
| FLIR Lepton | GPIO 10 (MOSI) | GPIO 9 (MISO) | GPIO 11 (SCLK) | GPIO 7 (CE1) | 3.3V | GND |

### I2C Bus (Low-Speed Sensors)

| Device | SDA | SCL | Address | VCC | GND |
|--------|-----|-----|---------|-----|-----|
| MAX30102 PPG | GPIO 2 (SDA) | GPIO 3 (SCL) | 0x57 | 3.3V | GND |
| GSR Sensor | GPIO 2 (SDA) | GPIO 3 (SCL) | 0x48 | 3.3V | GND |
| Accelerometer | GPIO 2 (SDA) | GPIO 3 (SCL) | 0x68 | 3.3V | GND |

### I2S Bus (Audio)

| Device | BCLK | LRCLK | DIN | DOUT | VCC | GND |
|--------|------|-------|-----|------|-----|-----|
| INMP441 Mic 1 | GPIO 18 | GPIO 19 | GPIO 21 | - | 3.3V | GND |
| INMP441 Mic 2 | GPIO 18 | GPIO 19 | GPIO 20 | - | 3.3V | GND |
| INMP441 Mic 3 | GPIO 18 | GPIO 19 | GPIO 16 | - | 3.3V | GND |
| INMP441 Mic 4 | GPIO 18 | GPIO 19 | GPIO 17 | - | 3.3V | GND |
| PCM5102A DAC | GPIO 18 | GPIO 19 | - | GPIO 21 | 3.3V | GND |

### UART Bus (tDCS Stimulator)

| Signal | GPIO Pin | Device Pin |
|--------|----------|------------|
| TX (Pi → tDCS) | GPIO 14 (TXD) | RX |
| RX (tDCS → Pi) | GPIO 15 (RXD) | TX |
| VCC | 5V | VCC |
| GND | GND | GND |

---

## POWER DISTRIBUTION

```
                    ┌─────────────────────────────────────────────────┐
                    │           POWER FLOW DIAGRAM                     │
                    │                                                 │
                    │   2x 18650 (3.7V, 3000mAh each)                │
                    │   Total: 7.4V, 3000mAh (22.2Wh)                │
                    │                    │                           │
                    │                    ▼                           │
                    │              TP4056 Dual Charger               │
                    │              (7.4V input, balance charge)      │
                    │                    │                           │
                    │                    ▼                           │
                    │              5V/3A Boost Converter             │
                    │              (7.4V → 5V, 15W)                 │
                    │                    │                           │
                    │          ┌─────────┼─────────┐                │
                    │          │         │         │                │
                    │          ▼         ▼         ▼                │
                    │     ┌────────┐ ┌────────┐ ┌────────┐         │
                    │     │Pi 4    │ │Sensors │ │Project │         │
                    │     │3A max  │ │0.5A    │ │1A      │         │
                    │     └────────┘ └────────┘ └────────┘         │
                    │                                                 │
                    │   Total: 4.5A max (within 5V/3A boost limit)  │
                    │   Runtime: 22.2Wh / 15W = 1.5 hours active    │
                    └─────────────────────────────────────────────────┘
```

### Battery Connection

```
18650 Battery Pack (2S)
    │
    ├──[TP4056]──┐
    │             │
    │    ┌────────┴────────┐
    │    │  5V/3A Boost    │
    │    │  Converter      │
    │    │  7.4V → 5V      │
    │    └────────┬────────┘
    │             │
    │             ▼
    │         5V Rail
    │             │
    │    ┌────────┼────────┐
    │    │        │        │
    │    ▼        ▼        ▼
    │ ┌──────┐ ┌──────┐ ┌──────┐
    │ │Pi 4  │ │Sensors│ │Project│
    │ │      │ │      │ │      │
    │ └──────┘ └──────┘ └──────┘
    │
    └──[USB-C]──► Charging (5V/3A)
```

---

## SENSOR WIRING DETAILS

### ADS1299 EEG System (8-Channel)

```
ADS1299 Module               Raspberry Pi 4
┌─────────────────────┐     ┌─────────────────────┐
│  VDD ───────────────┼─────┼── 3.3V              │
│  GND ───────────────┼─────┼── GND               │
│  DIN (MOSI) ────────┼─────┼── GPIO 10 (MOSI)    │
│  DOUT (MISO) ───────┼─────┼── GPIO 9 (MISO)     │
│  SCLK ──────────────┼─────┼── GPIO 11 (SCLK)    │
│  CS ────────────────┼─────┼── GPIO 8 (CE0)      │
│  DRDY ──────────────┼─────┼── GPIO 25 (IRQ)     │
│                     │     │                     │
│  IN1+ (Ch1) ────────┼─────┼── EEG Electrode 1   │
│  IN1- (Ch1) ────────┼─────┼── EEG Reference     │
│  IN2+ (Ch2) ────────┼─────┼── EEG Electrode 2   │
│  IN2- (Ch2) ────────┼─────┼── EEG Reference     │
│  IN3+ (Ch3) ────────┼─────┼── EEG Electrode 3   │
│  IN3- (Ch3) ────────┼─────┼── EEG Reference     │
│  IN4+ (Ch4) ────────┼─────┼── EEG Electrode 4   │
│  IN4- (Ch4) ────────┼─────┼── EEG Reference     │
│  IN5+ (Ch5) ────────┼─────┼── EEG Electrode 5   │
│  IN5- (Ch5) ────────┼─────┼── EEG Reference     │
│  IN6+ (Ch6) ────────┼─────┼── EEG Electrode 6   │
│  IN6- (Ch6) ────────┼─────┼── EEG Reference     │
│  IN7+ (Ch7) ────────┼─────┼── EEG Electrode 7   │
│  IN7- (Ch7) ────────┼─────┼── EEG Reference     │
│  IN8+ (Ch8) ────────┼─────┼── EEG Electrode 8   │
│  IN8- (Ch8) ────────┼─────┼── EEG Reference     │
│  BIAS ──────────────┼─────┼── EEG Bias           │
│  SRB1 ──────────────┼─────┼── Common Reference   │
│  SRB2 ──────────────┼─────┼── Common Reference   │
└─────────────────────┘     └─────────────────────┘
```

### FLIR Lepton Thermal Camera

```
FLIR Lepton Module           Raspberry Pi 4
┌─────────────────────┐     ┌─────────────────────┐
│  VDD ───────────────┼─────┼── 3.3V              │
│  GND ───────────────┼─────┼── GND               │
│  MOSI ──────────────┼─────┼── GPIO 10 (MOSI)    │
│  MISO ──────────────┼─────┼── GPIO 9 (MISO)     │
│  SCLK ──────────────┼─────┼── GPIO 11 (SCLK)    │
│  CS ────────────────┼─────┼── GPIO 7 (CE1)      │
│  RESET ─────────────┼─────┼── GPIO 24            │
│  PWR_DWN ───────────┼─────┼── GPIO 27            │
│  INT ───────────────┼─────┼── GPIO 22 (IRQ)     │
└─────────────────────┘     └─────────────────────┘
```

### OV2640 NIR Camera

```
OV2640 Module                Raspberry Pi 4
┌─────────────────────┐     ┌─────────────────────┐
│  VCC ───────────────┼─────┼── 3.3V              │
│  GND ───────────────┼─────┼── GND               │
│  SDA ───────────────┼─────┼── GPIO 2 (SDA)      │
│  SCL ───────────────┼─────┼── GPIO 3 (SCL)      │
│  D0-D7 ─────────────┼─────┼── CSI Connector     │
│  PCLK ──────────────┼─────┼── CSI Clock         │
│  VSYNC ─────────────┼─────┼── CSI Vsync         │
│  HREF ──────────────┼─────┼── CSI Href          │
│  XCLK ──────────────┼─────┼── CSI Xclk          │
│  PWDN ──────────────┼─────┼── GPIO 0            │
│  RESET ─────────────┼─────┼── GPIO 1            │
└─────────────────────┘     └─────────────────────┘
```

### Audio System (4-Mic Array + Speaker)

```
INMP441 Microphones (x4)      Raspberry Pi 4
┌─────────────────────┐     ┌─────────────────────┐
│  Mic 1:             │     │                     │
│  VDD ───────────────┼─────┼── 3.3V              │
│  GND ───────────────┼─────┼── GND               │
│  SCK ───────────────┼─────┼── GPIO 18 (BCLK)    │
│  WS ────────────────┼─────┼── GPIO 19 (LRCLK)   │
│  SD ────────────────┼─────┼── GPIO 21 (DIN)     │
│                     │     │                     │
│  Mic 2:             │     │                     │
│  SD ────────────────┼─────┼── GPIO 20           │
│                     │     │                     │
│  Mic 3:             │     │                     │
│  SD ────────────────┼─────┼── GPIO 16           │
│                     │     │                     │
│  Mic 4:             │     │                     │
│  SD ────────────────┼─────┼── GPIO 17           │
└─────────────────────┘     └─────────────────────┘

PCM5102A DAC (Audio Output)
┌─────────────────────┐     ┌─────────────────────┐
│  VCC ───────────────┼─────┼── 3.3V              │
│  GND ───────────────┼─────┼── GND               │
│  BCK ───────────────┼─────┼── GPIO 18 (BCLK)    │
│  LCK ───────────────┼─────┼── GPIO 19 (LRCLK)   │
│  DIN ───────────────┼─────┼── GPIO 21 (DOUT)    │
│  SCK ───────────────┼─────┼── 3.3V (via 1kΩ)    │
│  FMT ───────────────┼─────┼── GND (I2S mode)    │
│  DEMP ──────────────┼─────┼── GND                │
│  XMT ───────────────┼─────┼── 3.3V (unmute)     │
│  LOUT ──────────────┼─────┼── Speaker L         │
│  ROUT ──────────────┼─────┼── Speaker R         │
└─────────────────────┘     └─────────────────────┘
```

---

## PROJECTION SYSTEM WIRING

### LED Ring (Facial Illumination)

```
WS2812B LED Ring (16 LEDs)    Raspberry Pi 4
┌─────────────────────┐     ┌─────────────────────┐
│  VCC ───────────────┼─────┼── 5V                │
│  GND ───────────────┼─────┼── GND               │
│  DIN ───────────────┼─────┼── GPIO 12 (PWM)     │
│                     │     │                     │
│  (Series connection:│     │                     │
│   DIN → DOUT → DIN)│     │                     │
└─────────────────────┘     └─────────────────────┘
```

### Peltier Thermal Patches (x4)

```
Peltier TEC1-12706           Raspberry Pi 4
┌─────────────────────┐     ┌─────────────────────┐
│  Patch 1 (Forehead):│     │                     │
│  + ─────────────────┼─────┼── MOSFET 1 (GPIO 5) │
│  - ─────────────────┼─────┼── GND               │
│                     │     │                     │
│  Patch 2 (Cheeks):  │     │                     │
│  + ─────────────────┼─────┼── MOSFET 2 (GPIO 6) │
│  - ─────────────────┼─────┼── GND               │
│                     │     │                     │
│  Patch 3 (Neck):    │     │                     │
│  + ─────────────────┼─────┼── MOSFET 3 (GPIO 13)│
│  - ─────────────────┼─────┼── GND               │
│                     │     │                     │
│  Patch 4 (Wrists):  │     │                     │
│  + ─────────────────┼─────┼── MOSFET 4 (GPIO 26)│
│  - ─────────────────┼─────┼── GND               │
└─────────────────────┘     └─────────────────────┘

Note: Use N-channel MOSFETs (IRF540N) for switching
      Add 10kΩ pull-down on gate
      Add flyback diode across each Peltier
```

### Vibration Motors (x6)

```
LRA Vibration Motors          Raspberry Pi 4
┌─────────────────────┐     ┌─────────────────────┐
│  Motor 1:           │     │                     │
│  + ─────────────────┼─────┼── GPIO 23 (PWM)     │
│  - ─────────────────┼─────┼── GND               │
│                     │     │                     │
│  Motor 2:           │     │                     │
│  + ─────────────────┼─────┼── GPIO 24 (PWM)     │
│  - ─────────────────┼─────┼── GND               │
│                     │     │                     │
│  Motor 3:           │     │                     │
│  + ─────────────────┼─────┼── GPIO 25 (PWM)     │
│  - ─────────────────┼─────┼── GND               │
│                     │     │                     │
│  Motor 4:           │     │                     │
│  + ─────────────────┼─────┼── GPIO 27 (PWM)     │
│  - ─────────────────┼─────┼── GND               │
│                     │     │                     │
│  Motor 5:           │     │                     │
│  + ─────────────────┼─────┼── GPIO 28 (PWM)     │
│  - ─────────────────┼─────┼── GND               │
│                     │     │                     │
│  Motor 6:           │     │                     │
│  + ─────────────────┼─────┼── GPIO 29 (PWM)     │
│  - ─────────────────┼─────┼── GND               │
└─────────────────────┘     └─────────────────────┘
```

### tDCS Stimulator

```
tDCS Module                   Raspberry Pi 4
┌─────────────────────┐     ┌─────────────────────┐
│  VCC ───────────────┼─────┼── 5V                │
│  GND ───────────────┼─────┼── GND               │
│  RX ────────────────┼─────┼── GPIO 14 (TXD)     │
│  TX ────────────────┼─────┼── GPIO 15 (RXD)     │
│  ENABLE ────────────┼─────┼── GPIO 4            │
│  CURRENT_SET ───────┼─────┼── GPIO 27 (PWM)     │
│                     │     │                     │
│  Electrode + ───────┼─────┼── Anode Pad         │
│  Electrode - ───────┼─────┼── Cathode Pad       │
└─────────────────────┘     └─────────────────────┘
```

---

## GPIO PIN MAP

| GPIO | Function | Connected To | Direction |
|------|----------|--------------|-----------|
| 0 | Camera PWDN | OV2640 | Output |
| 1 | Camera RESET | OV2640 | Output |
| 2 | I2C SDA | PPG, GSR, IMU | Bidirectional |
| 3 | I2C SCL | PPG, GSR, IMU | Output |
| 4 | tDCS ENABLE | tDCS Module | Output |
| 5 | Peltier 1 | MOSFET Gate | Output |
| 6 | Peltier 2 | MOSFET Gate | Output |
| 7 | SPI CS1 | FLIR Lepton | Output |
| 8 | SPI CS0 | ADS1299 | Output |
| 9 | SPI MISO | ADS1299, FLIR | Input |
| 10 | SPI MOSI | ADS1299, FLIR | Output |
| 11 | SPI SCLK | ADS1299, FLIR | Output |
| 12 | LED Ring | WS2812B | Output |
| 13 | Peltier 3 | MOSFET Gate | Output |
| 14 | UART TX | tDCS RX | Output |
| 15 | UART RX | tDCS TX | Input |
| 16 | Mic 3 | INMP441 | Input |
| 17 | Mic 4 | INMP441 | Input |
| 18 | I2S BCLK | Mics, DAC | Output |
| 19 | I2S LRCLK | Mics, DAC | Output |
| 20 | Mic 2 | INMP441 | Input |
| 21 | I2S DIN/DOUT | Mics, DAC | Bidirectional |
| 22 | FLIR INT | FLIR Lepton | Input |
| 23 | Vibration 1 | LRA Motor | Output |
| 24 | FLIR RESET | FLIR Lepton | Output |
| 25 | Vibration 2 | LRA Motor | Output |
| 26 | Peltier 4 | MOSFET Gate | Output |
| 27 | Vibration 3 | LRA Motor | Output |
| 28 | Vibration 4 | LRA Motor | Output |
| 29 | Vibration 5 | LRA Motor | Output |
| 30 | Vibration 6 | LRA Motor | Output |

---

## POWER PINS

| Pin | Voltage | Current | Notes |
|-----|---------|---------|-------|
| 5V (Pin 2,4) | 5V | 3A max | From boost converter |
| 3.3V (Pin 1,17) | 3.3V | 50mA max | From Pi's LDO |
| GND (Multiple) | 0V | - | Common ground |

---

## WIRING BEST PRACTICES

1. **I2C Pull-ups**: Always include 4.7kΩ pull-ups on SDA and SCL to 3.3V
2. **Bypass Caps**: Add 100nF ceramic capacitors on each sensor's VCC pin
3. **Wire Length**: Keep SPI wires under 15cm to prevent signal degradation
4. **Power Filtering**: Add 100µF bulk capacitor near power input
5. **Ground Plane**: Use ground plane or star ground topology
6. **Shielding**: Wrap SPI wires in foil if display shows noise
7. **EMI**: Keep analog sensors away from digital switching circuits

---

## CONTINUITY CHECK LIST

Before powering on, verify:

- [ ] All GND pins connected together
- [ ] 3.3V rail to all sensor VCC pins
- [ ] 5V rail to Pi 4 and projection system
- [ ] No shorts between 3.3V and GND
- [ ] I2C SDA not shorted to SCL
- [ ] SPI MOSI/MISO not shorted
- [ ] UART TX/RX not swapped
- [ ] tDCS electrodes isolated (no short)
- [ ] Peltier MOSFETs properly oriented
- [ ] Battery polarity correct

---

## SAFETY CHECKLIST

Before using tDCS:

- [ ] Maximum current set to 1mA
- [ ] Electrodes properly placed (anode on forehead, cathode on shoulder)
- [ ] Conductive sponge electrodes wet with saline
- [ ] No metal implants in stimulation area
- [ ] User does not have epilepsy
- [ ] User is not pregnant
- [ ] Session timer set to 20 minutes max
- [ ] Emergency stop button accessible

---

**Document**: 02_WIRING.md
**Vehicle**: PHI EMOTION CLOAK
**Status**: BUILDABLE ✓
