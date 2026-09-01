# PHI_HUMANOID_ROBOT — Complete Bill of Materials

## Full BOM with Pricing, Suppliers & Part Numbers

---

## 1. BOM Summary

| Category | Items | Total Cost | % of BOM |
|----------|-------|-----------|----------|
| Structural Frame | 15 | $474.00 | 10.2% |
| Leg Actuators (12 DOF) | 18 | $660.00 | 14.2% |
| Arm Actuators (12 DOF) | 18 | $500.00 | 10.8% |
| Torso/Head Actuators (4 DOF) | 8 | $200.00 | 4.3% |
| Hand Actuators (12 DOF) | 12 | $216.00 | 4.6% |
| Encoders & Position Sensors | 30 | $269.00 | 5.8% |
| Force & Tactile Sensors | 29 | $382.00 | 8.2% |
| Compute & AI | 16 | $1,395.00 | 30.0% |
| Vision System | 7 | $107.00 | 2.3% |
| Audio System | 8 | $29.00 | 0.6% |
| Power System | 20 | $2,068.00 | 44.5% |
| Cabling & Connectors | 12 | $151.00 | 3.2% |
| Head & Sensing | 9 | $78.00 | 1.7% |
| Cooling & Thermal | 15 | $97.00 | 2.1% |
| Miscellaneous | 5 | $115.00 | 2.5% |
| **TOTAL** | **222** | **$4,641.00** | — |

---

## 2. Volume Pricing Estimates

| Volume | Estimated BOM | Per-Unit Savings | Notes |
|--------|--------------|------------------|-------|
| 1 unit | $4,641 | — | Retail pricing |
| 10 units | $4,100 | $541 (12%) | Small batch |
| 50 units | $3,600 | $1,041 (22%) | Medium batch |
| 100 units | $3,200 | $1,441 (31%) | Production scale |
| 500 units | $2,800 | $1,841 (40%) | Volume discount |
| 1000+ units | $2,500 | $2,141 (46%) | Full production |

---

## 3. Complete Line-Item BOM

### 3.1 Structural Frame

| # | Part Number | Description | Qty | Unit Cost | Ext Cost | Supplier |
|---|------------|-------------|-----|-----------|----------|----------|
| S-01 | PHI-S-001 | Main torso tube, 6061-T6, 80×50mm, L=400mm | 1 | $45.00 | $45.00 | Cut to spec |
| S-02 | PHI-S-002 | Pelvis plate, 6061-T6, 5mm, 200×150mm | 1 | $25.00 | $25.00 | Cut to spec |
| S-03 | PHI-S-003 | Upper leg tube, 6061-T6, 40mm OD, L=300mm | 2 | $12.00 | $24.00 | Misumi |
| S-04 | PHI-S-004 | Lower leg tube, 6061-T6, 35mm OD, L=350mm | 2 | $11.00 | $22.00 | Misumi |
| S-05 | PHI-S-005 | Foot plate, 6061-T6, 4mm, 250×100mm | 2 | $15.00 | $30.00 | Cut to spec |
| S-06 | PHI-S-006 | Upper arm tube, 6061-T6, 30mm OD, L=250mm | 2 | $10.00 | $20.00 | Misumi |
| S-07 | PHI-S-007 | Lower arm tube, 6061-T6, 25mm OD, L=280mm | 2 | $9.00 | $18.00 | Misumi |
| S-08 | PHI-S-008 | Neck bracket, 6061-T6, 3mm, 80×80mm | 1 | $12.00 | $12.00 | Cut to spec |
| S-09 | PHI-S-009 | Head shell, ASA 3D print, 200×180×150mm | 1 | $25.00 | $25.00 | Custom print |
| S-10 | PHI-S-010 | Hand chassis, 6061-T6, 2mm, 120×80mm | 2 | $18.00 | $36.00 | Cut to spec |
| S-11 | PHI-S-011 | Finger link (phalanx), 6061-T6, 10mm dia | 30 | $2.00 | $60.00 | Cut to spec |
| S-12 | PHI-S-012 | Joint bearing flange, 608ZZ mount | 12 | $4.50 | $54.00 | Misumi |
| S-13 | PHI-S-013 | Fastener kit, M3/M4/M5 SS bolts (200 pcs) | 1 | $35.00 | $35.00 | McMaster |
| S-14 | PHI-S-014 | Cable routing clips, nylon P-clips | 40 | $0.50 | $20.00 | McMaster |
| S-15 | PHI-S-015 | Structural gussets, 6061-T6 triangular | 16 | $3.00 | $48.00 | Cut to spec |
| | | | | | **$474.00** | |

### 3.2 Leg Actuators

| # | Part Number | Description | Qty | Unit Cost | Ext Cost | Supplier |
|---|------------|-------------|-----|-----------|----------|----------|
| A-01 | PHI-A-001 | HAA motor, ODrive D6374 150KV, 14.5Nm | 2 | $65.00 | $130.00 | ODrive |
| A-02 | PHI-A-002 | HFE motor, ODrive D6374 150KV, 14.5Nm | 2 | $65.00 | $130.00 | ODrive |
| A-03 | PHI-A-003 | KFE motor, ODrive D6374 150KV, 14.5Nm | 2 | $65.00 | $130.00 | ODrive |
| A-04 | PHI-A-004 | KAA motor, ODrive D5065 270KV, 4.8Nm | 2 | $45.00 | $90.00 | ODrive |
| A-05 | PHI-A-005 | AFE motor, ODrive D5065 270KV, 4.8Nm | 2 | $45.00 | $90.00 | ODrive |
| A-06 | PHI-A-006 | Toe motor, ODrive D5065 270KV, 4.8Nm | 2 | $45.00 | $90.00 | ODrive |
| | | | | | **$660.00** | |

### 3.3 Arm Actuators

| # | Part Number | Description | Qty | Unit Cost | Ext Cost | Supplier |
|---|------------|-------------|-----|-----------|----------|----------|
| A-07 | PHI-A-007 | SAA motor, ODrive D5065 270KV, 4.8Nm | 2 | $45.00 | $90.00 | ODrive |
| A-08 | PHI-A-008 | SFE motor, ODrive D5065 270KV, 4.8Nm | 2 | $45.00 | $90.00 | ODrive |
| A-09 | PHI-A-009 | SHS motor, ODrive D5065 270KV, 4.8Nm | 2 | $45.00 | $90.00 | ODrive |
| A-10 | PHI-A-010 | ELF motor, ODrive D5065 270KV, 4.8Nm | 2 | $45.00 | $90.00 | ODrive |
| A-11 | PHI-A-011 | WFE motor, ODrive M5671 100KV, 1.2Nm | 2 | $35.00 | $70.00 | ODrive |
| A-12 | PHI-A-012 | WRU motor, ODrive M5671 100KV, 1.2Nm | 2 | $35.00 | $70.00 | ODrive |
| | | | | | **$500.00** | |

### 3.4 Torso & Head Actuators

| # | Part Number | Description | Qty | Unit Cost | Ext Cost | Supplier |
|---|------------|-------------|-----|-----------|----------|----------|
| A-13 | PHI-A-013 | Torso yaw motor, ODrive D6374 150KV, 14.5Nm | 1 | $65.00 | $65.00 | ODrive |
| A-14 | PHI-A-014 | Torso pitch motor, ODrive D6374 150KV, 14.5Nm | 1 | $65.00 | $65.00 | ODrive |
| A-15 | PHI-A-015 | Head pan motor, ODrive M5671 100KV, 1.2Nm | 1 | $35.00 | $35.00 | ODrive |
| A-16 | PHI-A-016 | Head tilt motor, ODrive M5671 100KV, 1.2Nm | 1 | $35.00 | $35.00 | ODrive |
| | | | | | **$200.00** | |

### 3.5 Hand Actuators

| # | Part Number | Description | Qty | Unit Cost | Ext Cost | Supplier |
|---|------------|-------------|-----|-----------|----------|----------|
| A-17 | PHI-A-017 | Finger servo, Dynamixel XL330-M288, 0.52Nm | 10 | $18.00 | $180.00 | Robotis |
| A-18 | PHI-A-018 | Thumb servo, Dynamixel XL330-M288, 0.52Nm | 2 | $18.00 | $36.00 | Robotis |
| | | | | | **$216.00** | |

### 3.6 Encoders

| # | Part Number | Description | Qty | Unit Cost | Ext Cost | Supplier |
|---|------------|-------------|-----|-----------|----------|----------|
| E-01 | PHI-E-001 | Leg encoder, AS5048A, 14-bit magnetic | 12 | $8.00 | $96.00 | AMS/TE |
| E-02 | PHI-E-002 | Arm encoder, AS5048A, 14-bit magnetic | 12 | $8.00 | $96.00 | AMS/TE |
| E-03 | PHI-E-003 | Torso encoder, AS5048A, 14-bit magnetic | 2 | $8.00 | $16.00 | AMS/TE |
| E-04 | PHI-E-004 | Head encoder, AS5048A, 14-bit magnetic | 2 | $8.00 | $16.00 | AMS/TE |
| E-05 | PHI-E-005 | Body IMU, BNO085, 9-DoF | 1 | $25.00 | $25.00 | Bosch |
| E-06 | PHI-E-006 | Head IMU, BNO055, 9-DoF | 1 | $20.00 | $20.00 | Bosch |
| | | | | | **$269.00** | |

### 3.7 Force/Tactile Sensors

| # | Part Number | Description | Qty | Unit Cost | Ext Cost | Supplier |
|---|------------|-------------|-----|-----------|----------|----------|
| F-01 | PHI-F-001 | Foot pressure PCB, 4× FSR406 + ADC | 2 | $15.00 | $30.00 | Custom |
| F-02 | PHI-F-002 | Hand force sensor, FSR402 | 10 | $6.00 | $60.00 | Interlink |
| F-03 | PHI-F-003 | Hip torque sensor, strain gauge, 200Nm | 2 | $35.00 | $70.00 | Custom |
| F-04 | PHI-F-004 | Knee torque sensor, strain gauge, 150Nm | 2 | $35.00 | $70.00 | Custom |
| F-05 | PHI-F-005 | Shoulder torque sensor, strain gauge, 80Nm | 2 | $30.00 | $60.00 | Custom |
| F-06 | PHI-F-006 | Elbow torque sensor, strain gauge, 40Nm | 2 | $30.00 | $60.00 | Custom |
| F-07 | PHI-F-007 | Current monitor, INA260, I2C | 8 | $4.00 | $32.00 | TI |
| | | | | | **$382.00** | |

### 3.8 Compute & AI

| # | Part Number | Description | Qty | Unit Cost | Ext Cost | Supplier |
|---|------------|-------------|-----|-----------|----------|----------|
| C-01 | PHI-C-001 | Raspberry Pi 5, 8GB | 1 | $80.00 | $80.00 | Raspberry Pi |
| C-02 | PHI-C-002 | Coral USB Accelerator, 4 TOPS | 1 | $60.00 | $60.00 | Google Coral |
| C-03 | PHI-C-003 | NVMe SSD, 256GB M.2 2230 | 1 | $30.00 | $30.00 | WD/Samsung |
| C-04 | PHI-C-004 | RPi5 active cooler | 1 | $5.00 | $5.00 | Raspberry Pi |
| C-05 | PHI-C-005 | ODrive S1 motor controller | 6 | $120.00 | $720.00 | ODrive |
| C-06 | PHI-C-006 | ODrive Pro motor controller | 2 | $200.00 | $400.00 | ODrive |
| C-07 | PHI-C-007 | Dynamixel U2D2 comm hub | 1 | $50.00 | $50.00 | Robotis |
| C-08 | PHI-C-008 | STM32H7 microcontroller | 2 | $25.00 | $50.00 | ST Micro |
| | | | | | **$1,395.00** | |

### 3.9 Vision

| # | Part Number | Description | Qty | Unit Cost | Ext Cost | Supplier |
|---|------------|-------------|-----|-----------|----------|----------|
| V-01 | PHI-V-001 | Stereo camera, Arducam 1280×800 MIPI | 2 | $35.00 | $70.00 | Arducam |
| V-02 | PHI-V-002 | Multi-camera HAT | 1 | $25.00 | $25.00 | Arducam |
| V-03 | PHI-V-003 | MIPI flex cable, 15-pin, 200mm | 4 | $3.00 | $12.00 | Arducam |
| | | | | | **$107.00** | |

### 3.10 Audio

| # | Part Number | Description | Qty | Unit Cost | Ext Cost | Supplier |
|---|------------|-------------|-----|-----------|----------|----------|
| U-01 | PHI-U-001 | MEMS microphone, INMP441, I2S | 4 | $3.00 | $12.00 | Adafruit |
| U-02 | PHI-U-002 | Speaker, 3W, 8Ω, 40mm | 2 | $4.00 | $8.00 | Parts Express |
| U-03 | PHI-U-003 | Class-D amplifier, MAX98357A, I2S | 1 | $4.00 | $4.00 | Adafruit |
| U-04 | PHI-U-004 | Audio codec, WM8960, I2S, 24-bit | 1 | $5.00 | $5.00 | Wolfson |
| | | | | | **$29.00** | |

### 3.11 Power System

| # | Part Number | Description | Qty | Unit Cost | Ext Cost | Supplier |
|---|------------|-------------|-----|-----------|----------|----------|
| P-01 | PHI-P-001 | FPB-10 battery, 48V/10kWh LiFePO4 | 4 | $450.00 | $1,800.00 | Custom |
| P-02 | PHI-P-002 | 48V→12V buck, 10A, 95% eff | 2 | $25.00 | $50.00 | Mean Well |
| P-03 | PHI-P-003 | 48V→5V buck, 6A, 95% eff | 2 | $20.00 | $40.00 | Mean Well |
| P-04 | PHI-P-004 | 48V→3.3V LDO, 1A, low-noise | 4 | $6.00 | $24.00 | TI TPS7A47 |
| P-05 | PHI-P-005 | Main contactor, 48V/100A, latching | 1 | $35.00 | $35.00 | TE |
| P-06 | PHI-P-006 | E-stop relay, 48V/30A, NC, failsafe | 2 | $8.00 | $16.00 | Panasonic |
| P-07 | PHI-P-007 | Fuse holder + blade fuses | 6 | $3.00 | $18.00 | Littelfuse |
| P-08 | PHI-P-008 | Battery wiring harness, 8AWG silicone | 1 | $25.00 | $25.00 | Custom |
| P-09 | PHI-P-009 | Power distribution PCB, 4-layer | 1 | $40.00 | $40.00 | Custom fab |
| P-10 | PHI-P-010 | Thermal management kit | 1 | $20.00 | $20.00 | Various |
| | | | | | **$2,068.00** | |

### 3.12 Cabling & Connectors

| # | Part Number | Description | Qty | Unit Cost | Ext Cost | Supplier |
|---|------------|-------------|-----|-----------|----------|----------|
| K-01 | PHI-K-001 | CAN bus cable, shielded 2-conductor | 10m | $2.00 | $20.00 | Molex |
| K-02 | PHI-K-002 | JST-SH connectors, 4-pin | 50 | $0.30 | $15.00 | JST |
| K-03 | PHI-K-003 | Molex Micro-Fit connectors, 4-pin | 30 | $1.50 | $45.00 | Molex |
| K-04 | PHI-K-004 | XT90 connectors, 90A | 4 | $4.00 | $16.00 | Amass |
| K-05 | PHI-K-005 | FFC cables, 15-pin, 200mm | 10 | $2.00 | $20.00 | Generic |
| K-06 | PHI-K-006 | Finger flex cable, 6-conductor, 80mm | 10 | $1.00 | $10.00 | Custom |
| K-07 | PHI-K-007 | Cable sleeve, 6mm braided PET | 5m | $3.00 | $15.00 | Various |
| K-08 | PHI-K-008 | Zip ties, nylon, 200mm | 200 | $0.05 | $10.00 | Generic |
| | | | | | **$151.00** | |

### 3.13 Head & Sensing

| # | Part Number | Description | Qty | Unit Cost | Ext Cost | Supplier |
|---|------------|-------------|-----|-----------|----------|----------|
| H-01 | PHI-H-001 | OLED display, 0.96", 128×64, I2C | 2 | $8.00 | $16.00 | Adafruit |
| H-02 | PHI-H-002 | ToF sensor, VL53L0X, I2C | 2 | $8.00 | $16.00 | ST Micro |
| H-03 | PHI-H-003 | Light sensor, TSL2591, I2C | 1 | $6.00 | $6.00 | Adafruit |
| H-04 | PHI-H-004 | Temp sensor, TMP117, I2C | 2 | $5.00 | $10.00 | TI |
| H-05 | PHI-H-005 | Ultrasonic, MaxBotix MB1240 | 2 | $15.00 | $30.00 | MaxBotix |
| | | | | | **$78.00** | |

### 3.14 Cooling

| # | Part Number | Description | Qty | Unit Cost | Ext Cost | Supplier |
|---|------------|-------------|-----|-----------|----------|----------|
| T-01 | PHI-T-001 | Cooling fan, 40mm, 5V PWM, Noctua | 4 | $15.00 | $60.00 | Noctua |
| T-02 | PHI-T-002 | Heatsink kit, aluminum, various | 8 | $3.00 | $24.00 | Various |
| T-03 | PHI-T-003 | Thermal paste, Noctua NT-H1 | 1 | $8.00 | $8.00 | Noctua |
| T-04 | PHI-T-004 | Thermal pad, 1.5mm, 50×50mm | 1 | $5.00 | $5.00 | Generic |
| | | | | | **$97.00** | |

### 3.15 Miscellaneous

| # | Part Number | Description | Qty | Unit Cost | Ext Cost | Supplier |
|---|------------|-------------|-----|-----------|----------|----------|
| M-01 | PHI-M-001 | Rubber foot pads, 60A neoprene | 2 | $10.00 | $20.00 | Custom |
| M-02 | PHI-M-002 | Joint covers, TPU 3D print | 30 | $2.00 | $60.00 | Custom print |
| M-03 | PHI-M-003 | EVA foam padding, 5mm sheet | 1 | $15.00 | $15.00 | Generic |
| M-04 | PHI-M-004 | Silicone gaskets, 2mm | 10 | $1.00 | $10.00 | Custom |
| M-05 | PHI-M-005 | Aluminum nameplate, laser engraved | 1 | $10.00 | $10.00 | Custom |
| | | | | | **$115.00** | |

---

## 4. BOM Cost Breakdown (Visual)

```
COST DISTRIBUTION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Power System    ████████████████████████████████████████████ 44.5%  $2,068
Compute/AI      ████████████████████████████████              30.0%  $1,395
Leg Actuators   ██████████████                                14.2%  $660
Arm Actuators   ███████████                                   10.8%  $500
Structural      ██████████                                    10.2%  $474
Force Sensors   ████████                                       8.2%  $382
Encoders        ██████                                         5.8%  $269
Hand Actuators  █████                                          4.6%  $216
Torso/Head      ████                                           4.3%  $200
Cabling         ███                                            3.2%  $151
Vision          ██                                             2.3%  $107
Cooling         ██                                             2.1%  $97
Misc            ██                                             2.5%  $115
Head/Sensing    █                                              1.7%  $78
Audio           █                                              0.6%  $29

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL                                                    100%   $4,641
```

---

## 5. Critical Long-Lead Items

| Item | Lead Time | Risk | Mitigation |
|------|-----------|------|------------|
| FPB-10 battery | 8-12 weeks | High | Pre-order 6 months ahead |
| ODrive S1 | 2-4 weeks | Medium | Stock 2 spares |
| ODrive Pro | 2-4 weeks | Medium | Stock 1 spare |
| Coral USB TPU | 1-2 weeks | Low | Multiple suppliers |
| Raspberry Pi 5 | 1-2 weeks | Low | Authorized distributors |
| AS5048A encoder | 2-3 weeks | Low | AMS direct |
| Custom PCBs | 2-3 weeks | Medium | JLCPCB (fast turn) |
| 6061-T6 tubing | 1-2 weeks | Low | Misumi stock |
| Dynamixel XL330 | 1-2 weeks | Low | Robotis stock |

---

*Document: 10_COMPLETE_BOM.md — PHI_HUMANOID_ROBOT Complete Bill of Materials*
*Version: 1.0 | Date: 2026-08-27*
