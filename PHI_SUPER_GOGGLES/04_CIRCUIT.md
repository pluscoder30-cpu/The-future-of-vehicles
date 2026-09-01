# PHI SUPER GOGGLES — CIRCUIT DESIGN

## Schematic Details and PCB Layout

---

## PCB ARCHITECTURE

3 PCBs in the system:
1. **Main Board (MB)** — FPGA, ADCs, MUX, power regulation
2. **Sensor Board (SB)** — 8 EMF sensors, analog front-end
3. **Display Board (DB)** — OLED drivers, HDMI bridge

---

## ADC CIRCUIT (ADS1256 × 4)

```
ADS1256 Configuration:
  Clock: Internal 7.68MHz
  Data Rate: 10,000 SPS (configured)
  PGA Gain: 1 (unity, ±2.5V input range)
  Resolution: 16-bit (24-bit ADC, lower 16 used)
  Input Buffer: Enabled
  Reference: External 2.5V (REF5025)

Bypass Capacitors (per ADC):
  100nF on AVDD (ceramic, 0805)
  10nF on DVDD (ceramic, 0805)
  10μF bulk on AVDD (tantalum, 1206)

Anti-Aliasing (per analog input):
  2.2nF C0G cap (0805) to ground
```

---

## MULTIPLEXER CIRCUIT (CD74HC4067 × 4)

```
CD74HC4067 Configuration:
  Channel switch time: <100ns
  Propagation delay: <20ns
  On-resistance: 70Ω typical
  Crosstalk: <-80dB at 10kHz
  Input range: 0 to VCC (0-5V)

Bypass: 0.1μF on VCC
Enable: Active low (GPIO-controlled)
```

---

## VOLTAGE REFERENCE (REF5025)

```
Output: 2.500V ±0.05%
TC: 3 ppm/°C
Noise: 3 μVpp (0.1-10Hz)
Load regulation: 5 ppm/mA

Bypass:
  100nF on VIN
  10μF on VOUT
```

---

## POWER REGULATION

```
LM2596 (5V Rails):
  Input: 3.0-4.2V (battery)
  Output: 5.0V ±2%
  Max Current: 3A
  Efficiency: 85%
  Ripple: <50mVpp
  Filter: 33μH inductor + 330μF electrolytic + 10μF ceramic

AMS1117-3.3 (3.3V Rails):
  Input: 5V
  Output: 3.3V ±1%
  Max Current: 1A
  Dropout: 1.3V
  Bypass: 22μF tantalum + 0.1μF ceramic
```

---

## SENSOR FRONT-END (per channel × 8)

```
Signal Path:
  ML8511 OUT → 100Ω series → MUX-Ax
  Pull-down: 10kΩ to GND
  Bypass: 0.1μF at sensor VCC
  Ferrite: 100Ω@100MHz on VCC line
```

---

## DISPLAY INTERFACE

```
ADV7533 HDMI-to-MIPI Bridge:
  Input: HDMI (4 lanes + clock from FPGA)
  Output: MIPI DSI (2 data lanes + clock)
  Resolution: 1920×1080 @ 60Hz
  Color: 24-bit RGB

Configuration: I2C (address 0x72)
```

---

## PCB SPECIFICATIONS

| Parameter | Main Board | Sensor Board |
|-----------|-----------|-------------|
| Layers | 4 | 2 |
| Dimensions | 100mm × 60mm | 175mm × 55mm |
| Min trace | 0.15mm | 0.2mm |
| Min hole | 0.2mm | 0.3mm |
| Copper | 1oz/0.5oz | 1oz |
| Finish | ENIG | HASL |
| Solder mask | Black | Black |
| Vendor | JLCPCB | JLCPCB |
| Cost | ~$25/order | ~$20/order |

---

## CRITICAL COMPONENT VALUES

| Component | Value | Package | Qty |
|-----------|-------|---------|-----|
| R (pull-up) | 4.7kΩ | 0805 | 8 |
| R (pull-down) | 10kΩ | 0805 | 12 |
| R (series) | 100Ω | 0805 | 8 |
| C (bypass) | 0.1μF | 0805 | 32 |
| C (bypass) | 10nF | 0805 | 8 |
| C (bulk) | 10μF | 1206 | 8 |
| C (bulk) | 100μF | 1210 | 4 |
| L (inductor) | 33μH | 12×12mm | 2 |
| FB (ferrite) | 100Ω | 0805 | 8 |
| D (Schottky) | SS34 | SMA | 4 |
| Q (MOSFET) | SI2302 | SOT-23 | 4 |
