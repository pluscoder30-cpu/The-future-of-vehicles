# PHI EMOTION CLOAK — PARTS LIST (BOM)
## Buildable Documentation | Parts List

---

## CORE COMPONENTS

| # | Component | Source | Price | Notes |
|---|-----------|--------|-------|-------|
| 1 | Raspberry Pi 4 (4GB) | Amazon | $45.00 | Main processor |
| 2 | nRF52840 BLE Module | Amazon | $14.99 | Low power Bluetooth |
| 3 | ADS1299 8-ch EEG ADC | Amazon | $89.99 | 24-bit, medical grade |
| 4 | MAX30102 PPG Sensor | Amazon | $4.50 | Heart rate/HRV |
| 5 | GSR Sensor (Galvanic) | Amazon | $12.99 | Electrodermal activity |
| 6 | FLIR Lepton 3.5 | Amazon | $199.99 | Thermal camera 320x240 |
| 7 | OV2640 NIR Camera | Amazon | $14.99 | 120fps, near-infrared |
| 8 | INMP441 MEMS Mic Array (x4) | Amazon | $15.96 | I2S, 4x microphones |
| 9 | MAX9814 Mic Amplifier | Amazon | $5.99 | AGC, low noise |
| 10 | I2S DAC (PCM5102A) | Amazon | $8.99 | Audio output |

---

## PROJECTION SYSTEM

| # | Component | Source | Price | Notes |
|---|-----------|--------|-------|-------|
| 11 | WS2812B LED Ring (16x) | Amazon | $9.99 | NeoPixel, RGB |
| 12 | Peltier TEC1-12706 (x4) | Amazon | $24.96 | Thermal patches |
| 13 | LRA Vibration Motors (x6) | Amazon | $17.94 | Linear resonant actuator |
| 14 | TENS Electrode Pads (x4) | Amazon | $12.99 | Skin contact electrodes |
| 15 | Mini Speakers (x2) | Amazon | $7.98 | 8ohm, 2W |
| 16 | tDCS Stimulator Module | Amazon | $34.99 | 1mA, 2-channel |

---

## SENSOR ELECTRODES

| # | Component | Source | Price | Notes |
|---|-----------|--------|-------|-------|
| 17 | Ag/AgCl EEG Electrodes (x8) | Amazon | $24.99 | Dry, forehead |
| 18 | ECG Wrist Band Electrodes | Amazon | $11.99 | Stainless steel |
| 19 | GSR Finger Electrodes (x2) | Amazon | $8.99 | Gold plated |
| 20 | Conductive Gel (100ml) | Amazon | $14.99 | For EEG contact |
| 21 | Electrode Adhesive Pads | Amazon | $9.99 | Pre-gelled, disposable |

---

## HOUSING & GARMENT

| # | Component | Source | Price | Notes |
|---|-----------|--------|-------|-------|
| 22 | Compression Collar | Amazon | $18.99 | Neck worn, black |
| 23 | Finger Clip Mount | Amazon | $9.99 | For GSR sensor |
| 24 | Headband (EEG) | Amazon | $14.99 | Adjustable, 4-channel |
| 25 | Wrist Band (ECG) | Amazon | $8.99 | Velcro, adjustable |
| 26 | 3D Printed Enclosure | Home Depot | $5.00 | Main electronics box |
| 27 | Flexible PCB (Main) | Amazon | $22.99 | Custom layout |
| 28 | Heat Shrink Tubing | Home Depot | $4.99 | Assorted sizes |

---

## POWER & CONNECTIVITY

| # | Component | Source | Price | Notes |
|---|-----------|--------|-------|-------|
| 29 | 18650 Battery (x2) | Amazon | $12.98 | 3.7V, 3000mAh each |
| 30 | 18650 Battery Holder | Amazon | $3.99 | 2-cell series |
| 31 | TP4056 Dual Charger | Amazon | $4.99 | With protection |
| 32 | 5V/3A Boost Converter | Amazon | $6.99 | For Pi 4 |
| 33 | USB-C Cable (1m) | Amazon | $5.99 | For charging |
| 34 | WiFi Antenna (2.4GHz) | Amazon | $4.99 | External, 3dBi |

---

## TOOLS REQUIRED

| Tool | Source | Price | Notes |
|------|--------|-------|-------|
| Soldering Iron (40-60W) | Home Depot | $29.99 | Adjustable temp |
| Solder Wire (60/40) | Home Depot | $6.99 | Lead-free preferred |
| Wire Stripper | Home Depot | $8.99 | 22-30 AWG |
| Flush Cutters | Home Depot | $7.99 | For component leads |
| Multimeter | Home Depot | $14.99 | For continuity check |
| Hot Glue Gun | Home Depot | $9.99 | For securing components |
| Heat Gun | Home Depot | $19.99 | For heat shrink |
| Sewing Needle Kit | Home Depot | $5.99 | For garment work |
| Thread (conductive) | Amazon | $12.99 | For sensor wiring |
| Isopropyl Alcohol (90%) | Home Depot | $4.99 | For cleaning |

---

## COST SUMMARY

| Category | Cost |
|----------|------|
| Core Components | $412.39 |
| Projection System | $108.85 |
| Sensor Electrodes | $70.95 |
| Housing & Garment | $104.94 |
| Power & Connectivity | $38.94 |
| Tools (if needed) | $122.89 |
| **TOTAL (without tools)** | **$736.07** |
| **TOTAL (with tools)** | **$858.96** |

---

## WHERE TO BUY (Quick Links)

1. **Amazon**: Search component names directly
2. **Home Depot**: Tools, sewing supplies
3. **Adafruit**: Alternative for sensors (adafruit.com)
4. **SparkFun**: Alternative for electronics (sparkfun.com)
5. **Digi-Key**: Professional components (digikey.com)
6. **Mouser**: Medical-grade sensors (mouser.com)

---

## NOTES

- All prices are approximate (USD, as of 2026)
- FLIR Lepton is the most expensive component ($200)
- Consider buying used Lepton on eBay ($120-150)
- Conductive thread can replace some wires
- Total build time: ~6 hours (with tools)
- **IMPORTANT**: tDCS device requires caution - see safety warnings

---

## SAFETY WARNING

**tDCS (Transcranial Direct Current Stimulation)**:
- Maximum current: 1mA (DO NOT EXCEED)
- Maximum voltage: 12V
- Session time: 20 minutes max
- Frequency: 1x daily max
- Contraindications: Epilepsy, metal implants, pregnancy
- **ALWAYS** use with supervision
- **ALWAYS** start at 0.5mA
- **ALWAYS** use conductive sponge electrodes

---

**Document**: 01_PARTS_LIST.md
**Vehicle**: PHI EMOTION CLOAK
**Status**: BUILDABLE ✓
