# PHI HEALING DRONE — CIRCUIT SCHEMATICS

## Avionics and Sensor Circuit Design

---

## MAIN CIRCUIT OVERVIEW

```
SYSTEM BLOCK DIAGRAM:
═══════════════════════════════════════════════════════════════

  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
  │  FPB-5      │────→│  POWER      │────→│  ARDUINO    │
  │  BATTERY    │     │  MANAGEMENT │     │  MEGA 2560  │
  │  12V 50Ah   │     │  5V/3.3V    │     │             │
  └─────────────┘     └─────────────┘     └──────┬──────┘
                                                 │
                    ┌────────────────────────────┼────────────────────────┐
                    │                            │                        │
           ┌────────┴────────┐          ┌────────┴────────┐    ┌────────┴────────┐
           │   FLIGHT        │          │   MEDICAL       │    │   FREQUENCY     │
           │   SENSORS       │          │   SENSORS       │    │   GENERATOR     │
           │                 │          │                 │    │                 │
           │ - MPU6050       │          │ - MAX30102      │    │ - PCM5102A DAC  │
           │ - BMP280        │          │ - DS18B20 x2   │    │ - PAM8403 AMP   │
           │ - NEO-6M GPS   │          │ - AD8232 ECG   │    │ - Transducers   │
           │ - BMP180        │          │ - OLED Display  │    │                 │
           └─────────────────┘          └─────────────────┘    └─────────────────┘
                    │                            │                        │
           ┌────────┴────────┐          ┌────────┴────────┐    ┌────────┴────────┐
           │   MOTORS        │          │   COMMS         │    │   MEDICATION    │
           │                 │          │                 │    │   BAY           │
           │ - ESC1 (M1)     │          │ - ESP8266 WiFi  │    │                 │
           │ - ESC2 (M2)     │          │ - HC-12 Radio   │    │ - Servo 1-3     │
           │ - ESC3 (M3)     │          │ - Buzzer        │    │ - Hinges        │
           │ - ESC4 (M4)     │          │                 │    │ - Release Mech  │
           └─────────────────┘          └─────────────────┘    └─────────────────┘
```

---

## ARDUINO MEGA PIN MAP

```
ARDUINO MEGA 2560 — PIN ALLOCATION:
═══════════════════════════════════════════════════════════════

  ┌──────────────────────────────────────────────────────┐
  │                    DIGITAL PINS                       │
  │                                                      │
  │  Pin 0  (RX0)  ─── Serial (reserved)               │
  │  Pin 1  (TX0)  ─── Serial (reserved)               │
  │  Pin 2  (SDA)  ─── I2C Bus (MPU6050, BMP280)       │
  │  Pin 3  (SCL)  ─── I2C Clock                       │
  │  Pin 4         ─── PCM5102A DIN (Frequency)         │
  │  Pin 5         ─── ESC2 Signal (Motor 2)            │
  │  Pin 6         ─── ESC3 Signal (Motor 3)            │
  │  Pin 7         ─── PCM5102A BCK (Freq Clock)        │
  │  Pin 8         ─── PCM5102A LCK (Freq Word)         │
  │  Pin 9         ─── ESC4 Signal (Motor 4)            │
  │  Pin 10        ─── ESP8266 RX (WiFi)                │
  │  Pin 11        ─── ESP8266 TX (WiFi)                │
  │  Pin 12        ─── Servo 1 (Med Bay Release)        │
  │  Pin 13        ─── Servo 2 (Vial Bay Release)       │
  │  Pin 14        ─── Servo 3 (Wound Care)             │
  │  Pin 15        ─── Buzzer (Audible Alerts)          │
  │  Pin 16        ─── GPS TX → Arduino RX2             │
  │  Pin 17        ─── GPS RX ← Arduino TX2             │
  │  Pin 18        ─── HC-12 TX → Arduino RX3           │
  │  Pin 19        ─── HC-12 RX ← Arduino TX3           │
  │  Pin 20        ─── I2C SDA (expansion)              │
  │  Pin 21        ─── I2C SCL (expansion)              │
  │  Pin 22        ─── DS18B20 Data (Temperature)       │
  │  Pin 23        ─── ESC1 Signal (Motor 1)            │
  │                                                      │
  │                    ANALOG PINS                        │
  │                                                      │
  │  Pin A0        ─── AD8232 Output (ECG)              │
  │  Pin A1        ─── Battery Voltage (divider)        │
  │  Pin A2        ─── Current Sensor (ACS712)          │
  │  Pin A3        ─── Reserved                         │
  │                                                      │
  │                    POWER PINS                        │
  │                                                      │
  │  5V            ─── Sensor Power (regulated)         │
  │  3.3V          ─── ESP8266, BMP280                  │
  │  GND           ─── Common Ground (star)             │
  │  VIN           ─── 12V from FPB-5                   │
  │                                                      │
  └──────────────────────────────────────────────────────┘
```

---

## MPU6050 CIRCUIT

```
GYROSCOPE / ACCELEROMETER:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │          MPU6050 Module             │
  │                                     │
  │  VCC ───────→ 5V                   │
  │  GND ───────→ GND                  │
  │  SDA ───────→ Arduino Pin 20 (SDA) │
  │  SCL ───────→ Arduino Pin 21 (SCL) │
  │  INT ───────→ Arduino Pin 2        │
  │                                     │
  │  I2C Address: 0x68                 │
  │  Sample Rate: 1kHz                 │
  │  Range: +/- 2000 dps (gyro)       │
  │  Range: +/- 16g (accel)           │
  │                                     │
  └─────────────────────────────────────┘

  Pull-up resistors: 4.7k to 5V on SDA/SCL
  Decoupling: 100nF ceramic on VCC
```

---

## MEDICAL SENSOR CIRCUITS

```
MAX30102 PULSE OXIMETER:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │         MAX30102 Module             │
  │                                     │
  │  VIN ───────→ 3.3V                 │
  │  GND ───────→ GND                  │
  │  SDA ───────→ Arduino Pin 20 (SDA) │
  │  SCL ───────→ Arduino Pin 21 (SCL) │
  │                                     │
  │  I2C Address: 0x57                 │
  │  LED Current: 50mA (adjustable)    │
  │  Sample Rate: 100Hz                │
  │                                     │
  │  Measures:                         │
  │  - SpO2 (blood oxygen)             │
  │  - Heart rate (BPM)                │
  │  - PPG waveform                    │
  │                                     │
  └─────────────────────────────────────┘

DS18B20 TEMPERATURE SENSORS (x2):
═══════════════════════════════════════════════════════════════

  Arduino Pin 22 ──┬──→ DS18B20 #1 (Patient forehead)
                   │
                   └──→ DS18B20 #2 (Patient wrist)

  ┌─────────────────────────────────────┐
  │          DS18B20                    │
  │                                     │
  │  VCC ───────→ 5V                   │
  │  GND ───────→ GND                  │
  │  DATA ──────→ Pin 22 (with 4.7k    │
  │               pull-up to 5V)       │
  │                                     │
  │  Resolution: 12-bit (0.0625°C)     │
  │  Range: -55°C to +125°C           │
  │  Accuracy: +/- 0.5°C              │
  │                                     │
  └─────────────────────────────────────┘

AD8232 ECG MODULE:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │          AD8232 Module              │
  │                                     │
  │  VCC ───────→ 5V                   │
  │  GND ───────→ GND                  │
  │  OUTPUT ────→ Arduino Pin A0       │
  │  LO+ ───────→ Arduino Pin 16      │
  │  LO- ───────→ Arduino Pin 17      │
  │  SDN ───────→ 5V (always on)      │
  │                                     │
  │  Electrodes:                        │
  │  - RA (Right Arm) → Red pad        │
  │  - LA (Left Arm) → Yellow pad      │
  │  - RL (Right Leg) → Green pad      │
  │                                     │
  │  Gain: 100x                        │
  │  Bandwidth: 0.5-40Hz               │
  │  Sample Rate: 200Hz                │
  │                                     │
  └─────────────────────────────────────┘
```

---

## FREQUENCY GENERATOR CIRCUIT

```
PCM5102A DAC + PAM8403 AMPLIFIER:
═══════════════════════════════════════════════════════════════

  Arduino Pin 4 (PWM)
       │
       │ I2S Signal
       ▼
  ┌─────────────────────────────────────┐
  │          PCM5102A DAC               │
  │                                     │
  │  VCC ───────→ 5V                   │
  │  GND ───────→ GND                  │
  │  DIN ───────→ Arduino Pin 4        │
  │  BCK ───────→ Arduino Pin 7        │
  │  LCK ───────→ Arduino Pin 8        │
  │  SCK ───────→ GND (auto clock)     │
  │  FMT ───────→ GND (I2S format)     │
  │  DEMP ──────→ GND (no de-emph)     │
  │  XSMT ──────→ 5V (unmute)          │
  │  LOUT ──────→ Amplifier IN+        │
  │  ROUT ──────→ Amplifier IN-        │
  │                                     │
  │  Resolution: 32-bit                 │
  │  Sample Rate: 44.1kHz              │
  │  THD+N: -93dB                      │
  │                                     │
  └─────────────────────────────────────┘
       │
       │ Audio Signal (line level)
       ▼
  ┌─────────────────────────────────────┐
  │          PAM8403 Amplifier          │
  │                                     │
  │  VCC ───────→ 5V                   │
  │  GND ───────→ GND                  │
  │  IN+ ───────→ DAC LOUT             │
  │  IN- ───────→ DAC ROUT             │
  │  OUT+ ──────→ Transducer 1         │
  │  OUT- ──────→ Transducer 2         │
  │                                     │
  │  Gain: 30dB                        │
  │  Output: 3W per channel            │
  │  THD: 0.5%                         │
  │                                     │
  └─────────────────────────────────────┘
       │
       │ Amplified Signal
       ▼
  ┌─────────────────────────────────────┐
  │       TRANSDUCERS (2x 40mm)        │
  │                                     │
  │  Transducer 1: Head/Neck area      │
  │  Transducer 2: Body/Torso area     │
  │                                     │
  │  Impedance: 8 ohm                  │
  │  Power: 2W each                    │
  │  Frequency: 20Hz-20kHz             │
  │                                     │
  │  PHI-HARMONIC FREQUENCIES:         │
  │  ────────────────────────────────  │
  │  432Hz - Healing fundamental       │
  │  528Hz - DNA repair                │
  │  639Hz - Connection                │
  │  741Hz - Expression                │
  │  852Hz - Intuition                 │
  │                                     │
  └─────────────────────────────────────┘
```

---

## MEDICATION BAY CIRCUIT

```
SERVO CONTROL FOR MEDICATION RELEASE:
═══════════════════════════════════════════════════════════════

  Arduino Pin 12 ──→ Servo 1 (Medication Bay)
  Arduino Pin 13 ──→ Servo 2 (Vial Bay)
  Arduino Pin 14 ──→ Servo 3 (Wound Care)

  ┌─────────────────────────────────────┐
  │          SG90 SERVO (x3)            │
  │                                     │
  │  Red ───────→ 5V (from BEC)        │
  │  Brown ─────→ GND                  │
  │  Orange ────→ Arduino Signal Pin   │
  │                                     │
  │  Torque: 1.8 kg·cm                 │
  │  Speed: 0.1s/60°                   │
  │  Angle: 0-180°                     │
  │                                     │
  │  Servo 1: Opens medication bay     │
  │  Servo 2: Releases individual vial │
  │  Servo 3: Activates wound care     │
  │                                     │
  └─────────────────────────────────────┘

  Safety interlock: Servos only activate
  when drone is stationary AND within
  1m of patient (ultrasonic confirmation)
```

---

## BATTERY MONITORING

```
VOLTAGE AND CURRENT SENSING:
═══════════════════════════════════════════════════════════════

  Battery Voltage Divider:
  ┌─────────────────────────────────────┐
  │                                     │
  │  12V ──→ R1 (10k) ──┬──→ Arduino A1│
  │                      │              │
  │                   R2 (3.3k)         │
  │                      │              │
  │                     GND             │
  │                                     │
  │  Vout = 12V × (3.3k / 13.3k)      │
  │       = 2.97V (safe for Arduino)   │
  │                                     │
  └─────────────────────────────────────┘

  Current Sensor (ACS712 20A):
  ┌─────────────────────────────────────┐
  │                                     │
  │  Battery+ ──→ ACS712 ──→ ESC Bus   │
  │                                     │
  │  VOUT ───────→ Arduino A2          │
  │  VCC ───────→ 5V                   │
  │  GND ───────→ GND                  │
  │                                     │
  │  Sensitivity: 100mV/A              │
  │  Range: 0-20A                       │
  │  Zero current: 2.5V output         │
  │                                     │
  └─────────────────────────────────────┘
```

---

## COMMUNICATION CIRCUITS

```
ESP8266 WIFI MODULE:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │          ESP8266 Module             │
  │                                     │
  │  VCC ───────→ 3.3V (NOT 5V!)      │
  │  GND ───────→ GND                  │
  │  TX ────────→ Arduino Pin 10 (RX)  │
  │  RX ────────→ Arduino Pin 11 (TX)  │
  │  CH_PD ─────→ 3.3V                 │
  │  RST ───────→ Pin 19 (reset)       │
  │  GPIO0 ─────→ 3.3V (normal mode)   │
  │                                     │
  │  Baud: 115200                       │
  │  Mode: Station + AP                 │
  │  Protocol: TCP                      │
  │                                     │
  └─────────────────────────────────────┘

HC-12 TELEMETRY RADIO:
═══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────┐
  │          HC-12 Module               │
  │                                     │
  │  VCC ───────→ 5V                   │
  │  GND ───────→ GND                  │
  │  TXD ───────→ Arduino Pin 18 (RX)  │
  │  RXD ───────→ Arduino Pin 19 (TX)  │
  │  SET ───────→ Pin 23 (config mode) │
  │                                     │
  │  Frequency: 433MHz                  │
  │  Baud: 9600                         │
  │  Range: 1km (open air)             │
  │  Power: 20mW                        │
  │                                     │
  └─────────────────────────────────────┘
```

---

## COMPLETE SCHEMATIC TABLE

| Component | Pins | I2C Address | Voltage | Current |
|-----------|------|-------------|---------|---------|
| Arduino Mega | - | - | 5V | 200mA |
| MPU6050 | 20,21 | 0x68 | 3.3V | 5mA |
| BMP280 | 20,21 | 0x76 | 3.3V | 1mA |
| MAX30102 | 20,21 | 0x57 | 3.3V | 10mA |
| AD8232 | A0 | Analog | 5V | 5mA |
| DS18B20 x2 | 22 | 1-Wire | 5V | 1.5mA |
| NEO-6M GPS | 16,17 | Serial | 3.3V | 45mA |
| ESP8266 | 10,11 | Serial | 3.3V | 80mA |
| HC-12 | 18,19 | Serial | 5V | 20mA |
| PCM5102A | 4,7,8 | I2S | 5V | 20mA |
| PAM8403 | Analog | - | 5V | 500mA |
| SG90 Servo x3 | 12,13,14 | PWM | 5V | 250mA |
| OLED | 20,21 | 0x3C | 5V | 20mA |
| Buzzer | 15 | - | 5V | 30mA |
