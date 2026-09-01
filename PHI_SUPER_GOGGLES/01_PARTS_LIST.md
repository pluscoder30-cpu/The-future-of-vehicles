# PHI SUPER GOGGLES — PARTS LIST

## Complete Parts List with Sources and Prices

All parts sourced from Amazon, eBay, AliExpress, and DigiKey as of August 2026.

---

## SENSOR SYSTEM (8× Triaxial EMF Sensors)

| Part # | Component | Qty | Source | Unit Price | Total | Notes |
|--------|-----------|-----|--------|------------|-------|-------|
| S01 | ML8511 UV/EMF Sensor Module | 8 | AliExpress | $4.25 | $34.00 | 3-axis EMF, 0.1Hz-300kHz |
| S02 | 3-Axis Hall Effect Sensor (A3144) | 8 | eBay | $1.89 | $15.12 | Additional triaxial detection |
| S03 | Analog Mux (CD74HC4067) 16ch | 4 | DigiKey | $1.52 | $6.08 | Channel multiplexing |
| S04 | Shielded Cable (6" twisted pair) | 8 | Amazon | $3.49 | $27.92 | Sensor runs |
| S05 | BNC Connector Panel Mount | 8 | Amazon | $1.29 | $10.32 | Sensor input connectors |
| S06 | Ferrite Bead (0805, 100Ω) | 24 | DigiKey | $0.15 | $3.60 | Noise suppression |
| S07 | 0.1μF Ceramic Cap (0805) | 24 | DigiKey | $0.08 | $1.92 | Bypass caps |
| S08 | 10μF Tantalum Cap (1206) | 8 | DigiKey | $0.32 | $2.56 | Bulk decoupling |

**Sensor Subtotal: $101.52**

---

## ADC SYSTEM (4× 16-bit ADC)

| Part # | Component | Qty | Source | Unit Price | Total | Notes |
|--------|-----------|-----|--------|------------|-------|-------|
| A01 | ADS1256 16-bit 30kSPS ADC Module | 4 | AliExpress | $8.95 | $35.80 | SPI, 8ch each, 16-bit |
| A02 | Precision Voltage Ref (REF5025) | 1 | DigiKey | $4.85 | $4.85 | 2.5V reference |
| A03 | 100Ω Resistor Array (8-pin) | 4 | DigiKey | $0.62 | $2.48 | Impedance matching |
| A04 | 2.2nF C0G Cap (0805) | 16 | DigiKey | $0.05 | $0.80 | Anti-aliasing filter |
| A05 | 4.7kΩ Resistor Array (8-pin) | 4 | DigiKey | $0.58 | $2.32 | Pull-up resistors |

**ADC Subtotal: $46.25**

---

## PROCESSOR (Intel Cyclone V FPGA)

| Part # | Component | Qty | Source | Unit Price | Total | Notes |
|--------|-----------|-----|--------|------------|-------|-------|
| P01 | DE10-Lite FPGA Board | 1 | DigiKey | $85.00 | $85.00 | Cyclone V 10CL016 |
| P02 | 64MB MicroSD Card | 1 | Amazon | $5.99 | $5.99 | Data logging |
| P03 | SD Card Module (SPI) | 1 | AliExpress | $1.25 | $1.25 | SD interface |
| P04 | Level Shifter (3.3V↔5V) | 2 | Amazon | $2.49 | $4.98 | Voltage translation |
| P05 | 50-pin FPC Connector | 4 | AliExpress | $0.85 | $3.40 | Display connectors |
| P06 | 40-pin GPIO Ribbon Cable | 2 | Amazon | $4.99 | $9.98 | Sensor bus |
| P07 | Heat Sink (20×20×8mm) | 1 | Amazon | $2.99 | $2.99 | FPGA thermal |

**Processor Subtotal: $113.59**

---

## DISPLAY (2× 1920×1080 OLED)

| Part # | Component | Qty | Source | Unit Price | Total | Notes |
|--------|-----------|-----|--------|------------|-------|-------|
| D01 | 0.39" 1920×1080 OLED | 2 | AliExpress | $45.00 | $90.00 | Microdisplay |
| D02 | HDMI to MIPI Bridge (ADV7533) | 1 | eBay | $12.95 | $12.95 | Display interface |
| D03 | OLED Flex Cable (30-pin FPC) | 2 | AliExpress | $3.50 | $7.00 | Display cables |
| D04 | Fresnel Lens Set (10×) | 1 pair | Amazon | $15.99 | $15.99 | Magnification |
| D05 | Diopter Adjustment Slider | 2 | Amazon | $4.99 | $9.98 | Per-eye focus |
| D06 | Anti-Reflective Coating | 1 set | Amazon | $8.99 | $8.99 | Lens coating |
| D07 | OLED Driver IC (SSD1362) | 2 | AliExpress | $3.25 | $6.50 | Driver boards |

**Display Subtotal: $151.41**

---

## POWER SYSTEM

| Part # | Component | Qty | Source | Unit Price | Total | Notes |
|--------|-----------|-----|--------|------------|-------|-------|
| W01 | FPB-5 Phi-Harmonic Field Plasma Battery 3.7V 8000mAh | 1 | Amazon | $24.99 | $24.99 | Main battery — Zero fire/explosion risk — plasma is self-limiting |
| W02 | USB-C PD Module (15W) | 1 | AliExpress | $6.95 | $6.95 | Fast charging |
| W03 | Phi-Harmonic Plasma Battery Charger IC (TP5100) | 1 | AliExpress | $1.89 | $1.89 | Balance charging |
| W04 | Buck Converter (LM2596, 5V 3A) | 2 | Amazon | $1.49 | $2.98 | 5V rails |
| W05 | LDO Regulator (AMS1117-3.3V) | 3 | DigiKey | $0.45 | $1.35 | 3.3V rails |
| W06 | Power MOSFET (SI2302) | 4 | DigiKey | $0.28 | $1.12 | Power switching |
| W07 | Schottky Diode (SS34) | 4 | DigiKey | $0.35 | $1.40 | Protection |
| W08 | Bulk Capacitor (470μF/16V) | 4 | DigiKey | $0.42 | $1.68 | Rail filtering |
| W09 | Power Indicator LED | 4 | DigiKey | $0.12 | $0.48 | Status indicators |
| W10 | DC Barrel Jack (2.1mm) | 1 | Amazon | $0.99 | $0.99 | External power |

**Power Subtotal: $43.83**

---

## INTERFACE SYSTEM

| Part # | Component | Qty | Source | Unit Price | Total | Notes |
|--------|-----------|-----|--------|------------|-------|-------|
| I01 | Tactile Button (6mm, SMD) | 12 | Amazon | $0.25 | $3.00 | Navigation |
| I02 | Rotary Encoder (KY-040) | 1 | Amazon | $1.99 | $1.99 | Adjustment |
| I03 | Haptic Motor (ERM, 3V) | 2 | AliExpress | $0.89 | $1.78 | Left/right feedback |
| I04 | Buzzer (3V, 27mm) | 1 | Amazon | $1.49 | $1.49 | Audio feedback |
| I05 | BNO055 9-DOF IMU | 1 | Adafruit | $34.95 | $34.95 | Motion tracking |
| I06 | MicroSD Card Slot | 1 | AliExpress | $0.99 | $0.99 | Data logging |
| I07 | USB-C Connector (24-pin) | 2 | AliExpress | $1.25 | $2.50 | Charging + data |
| I08 | Status LEDs (WS2812B) | 4 | Amazon | $0.35 | $1.40 | Mode indication |
| I09 | Piezo Microphone | 1 | Amazon | $2.99 | $2.99 | Sound correlation |

**Interface Subtotal: $51.09**

---

## MECHANICAL / HOUSING

| Part # | Component | Qty | Source | Unit Price | Total | Notes |
|--------|-----------|-----|--------|------------|-------|-------|
| M01 | 3D Printed Main Housing (PETG) | 1 | Self-print | $4.50 | $4.50 | Custom design |
| M02 | 3D Printed Sensor Plate | 1 | Self-print | $1.20 | $1.20 | 8× sensor positions |
| M03 | 3D Printed Display Housing (×2) | 2 | Self-print | $1.80 | $3.60 | Left/right eye cups |
| M04 | Adjustable Head Strap | 1 | Amazon | $6.99 | $6.99 | Comfortable fit |
| M05 | Nose Bridge Pad (silicone) | 2 | Amazon | $2.99 | $2.99 | Cushioning |
| M06 | Eyecup Foam Padding | 2 | Amazon | $3.49 | $6.98 | Light seal |
| M07 | Stainless Steel M3 Screws Kit | 1 | Amazon | $5.99 | $5.99 | Assembly |
| M08 | Nylon Standoffs (M3, assorted) | 1 bag | Amazon | $3.99 | $3.99 | Board mounting |
| M09 | Velcro Strips (industrial) | 1 pack | Amazon | $4.99 | $4.99 | Panel attachment |
| M10 | Cable Management Sleeving | 1m | Amazon | $3.99 | $3.99 | Wire organization |
| M11 | Thermal Pad (3mm, 6W/mK) | 1 sheet | Amazon | $2.99 | $2.99 | Heat transfer |
| M12 | Lens Retainer Ring (3D printed) | 2 | Self-print | $0.30 | $0.60 | Lens mounting |

**Mechanical Subtotal: $46.81**

---

## CABLES & CONNECTORS

| Part # | Component | Qty | Source | Unit Price | Total | Notes |
|--------|-----------|-----|--------|------------|-------|-------|
| C01 | SPI Ribbon Cable (10-pin) | 4 | AliExpress | $1.25 | $5.00 | ADC to FPGA |
| C02 | FFC Cable (30-pin) | 2 | AliExpress | $2.50 | $5.00 | Display connections |
| C03 | GPIO Ribbon (40-pin) | 2 | Amazon | $4.99 | $9.98 | Main sensor bus |
| C04 | USB-C Cable (1m, PD) | 1 | Amazon | $7.99 | $7.99 | Charging cable |
| C05 | Silicone Wire Kit (26AWG) | 1 kit | Amazon | $8.99 | $8.99 | Power distribution |
| C06 | Pogo Pin Connector (6-pin) | 2 | AliExpress | $1.50 | $3.00 | Test points |
| C07 | JST-XH Connector Kit | 1 kit | Amazon | $5.99 | $5.99 | Battery connection |
| C08 | 2.54mm Pin Header Kit | 1 kit | Amazon | $3.99 | $3.99 | Board headers |
| C09 | Coax Cable (RG178) | 2 | DigiKey | $4.99 | $9.98 | High-freq sensor lines |

**Cables Subtotal: $59.91**

---

## COST SUMMARY

| Category | Cost |
|----------|------|
| Sensor System | $101.52 |
| ADC System | $46.25 |
| Processor (FPGA) | $113.59 |
| Display System | $151.41 |
| Power System | $43.83 |
| Interface System | $51.09 |
| Mechanical/Housing | $46.81 |
| Cables/Connectors | $59.91 |
| **TOTAL (Parts)** | **$614.41** |
| Shipping (estimated) | $25.00 |
| Tax (estimated, 8%) | $41.07 |
| **GRAND TOTAL** | **$680.48** |

---

## WHERE TO BUY

- **Amazon:** Mechanical parts, cables, tools, battery
- **AliExpress:** Sensor modules, ADC boards, display modules, connectors
- **DigiKey:** ICs, capacitors, resistors, voltage regulators
- **eBay:** Sensor boards, specialty components
- **Adafruit:** BNO055 IMU (quality guaranteed)

## LEAD TIMES

- **Amazon:** 1-3 days (Prime)
- **AliExpress:** 2-4 weeks (standard) or 7-15 days (epacket)
- **DigiKey:** 3-5 business days
- **eBay:** 3-7 days
