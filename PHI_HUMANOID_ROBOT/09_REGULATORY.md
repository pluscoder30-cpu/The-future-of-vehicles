# PHI_HUMANOID_ROBOT — Regulatory Compliance

## FCC, UL, CE & International Compliance Roadmap

---

## 1. Regulatory Landscape

The PHI_HUMANOID_ROBOT falls under multiple regulatory frameworks depending on market and use case. This document covers compliance requirements for US, EU, and international markets.

### 1.1 Applicable Standards Summary

| Standard | Scope | Priority | Status |
|----------|-------|----------|--------|
| FCC Part 15 | Electromagnetic emissions (US) | Critical | Pre-compliance |
| FCC Part 15 Subpart C | Intentional radiator (WiFi/BLE) | Critical | Module-certified |
| IEC 62368-1 | Audio/video/ICT equipment safety | Critical | Design phase |
| IEC 61508 | Functional safety | Critical | Design phase |
| ISO 13482 | Personal care robot safety | High | Design phase |
| ISO 10218-1 | Industrial robot safety | High | Reference |
| UL 3300 | Safety for robots | High | Design phase |
| CE Marking | EU market access | High | Pre-compliance |
| EN 62368-1 | EU audio/ICT safety | High | Design phase |
| EN 301 489 | EU EMC for radio equipment | High | Module-certified |
| EN 300 328 | EU WiFi spectrum | High | Module-certified |
| RoHS | Hazardous substances | Critical | Compliant |
| REACH | Chemical substances | Critical | Compliant |
| WEEE | Waste electronics | Medium | Compliant |
| UN38.3 | Lithium battery transport | Critical | Compliant |

---

## 2. FCC Compliance (United States)

### 2.1 FCC Part 15 — Unintentional Radiator

```
APPLICABILITY:
  The PHI_HUMANOID_ROBOT contains digital electronics that
  may radiate electromagnetic energy. FCC Part 15 Subpart B
  applies to all digital devices.

CLASSIFICATION:
  Class B digital device (residential use)
  
  Limits (at 3m):
  ├── 30-88 MHz: 40 dBµV/m
  ├── 88-216 MHz: 43.5 dBµV/m
  ├── 216-960 MHz: 46 dBµV/m
  └── Above 960 MHz: 54 dBµV/m

COMPLIANCE STRATEGY:
  1. PCB design: 4-layer boards with continuous ground plane
  2. Decoupling: 100nF on every IC power pin
  3. Cable shielding: All external cables shielded
  4. Ferrite beads: On all cable exits
  5. Clock management: Spread-spectrum clocking where possible
  6. Pre-compliance testing: Spectrum analyzer scan before final test

TESTING:
  ├── Radiated emissions: 3m anechoic chamber
  ├── Conducted emissions: LISN + spectrum analyzer
  ├── Pre-compliance: In-house with near-field probes
  └── Full compliance: Accredited lab (e.g., TÜV, Intertek)
```

### 2.2 FCC Part 15 Subpart C — Intentional Radiator

```
WIFI/BLE MODULE:
  Raspberry Pi 5 WiFi: 802.11b/g/n/ac (2.4GHz + 5GHz)
  Bluetooth: BLE 5.0
  
  MODULE CERTIFICATION:
  ├── RPi 5 WiFi module is pre-certified
  ├── FCC ID: 2AXGP-RPI5 (Raspberry Pi Ltd)
  ├── Modular approval per FCC 15.212
  └── Host device inherits module certification IF:
      ├── Antenna gain ≤ module spec
      ├── Antenna placement ≤ module spec
      └── No modifications to RF circuitry

CORAL USB ACCELERATOR:
  Google Coral TPU: USB device (no RF)
  FCC Part 15 Subpart B applies (unintentional radiator)
  No separate RF certification needed.

COMPLIANCE ACTIONS:
  1. Document RPi 5 FCC module ID
  2. Verify antenna configuration matches certification
  3. Include FCC ID label on product
  4. Include FCC compliance statement in user manual:
     "This device complies with Part 15 of the FCC Rules.
      Operation is subject to the following two conditions:
      (1) this device may not cause harmful interference, and
      (2) this device must accept any interference received,
          including interference that may cause undesired operation."
```

### 2.3 FCC Labeling Requirements

```
LABEL CONTENTS:
  ├── FCC ID: 2AXGP-RPI5
  ├── "FCC Part 15 Compliant"
  ├── "Class B Digital Device"
  ├── Manufacturer name
  ├── Model number: PHI_HUMANOID_ROBOT_v1
  └── Made in [country]

LABEL PLACEMENT:
  ├── On robot chassis (permanent, legible)
  ├── In user manual
  ├── On packaging
  └── In product documentation

LABEL SIZE:
  Minimum 3mm height text, permanent marking
```

---

## 3. CE Compliance (European Union)

### 3.1 CE Marking Directives

```
APPLICABLE DIRECTIVES:
  ├── 2014/35/EU — Low Voltage Directive (LVD)
  │   ├── Applicable if: Operating voltage 50-1000V AC or 75-1500V DC
  │   ├── PHI_HUMANOID: 48V DC (below LVD threshold)
  │   └── LVD does NOT apply (48V < 75V DC)
  │
  ├── 2014/30/EU — Electromagnetic Compatibility (EMC)
  │   ├── Applies to all electronic equipment
  │   ├── Requires: EN 61000-6-3 (emissions)
  │   ├── Requires: EN 61000-6-2 (immunity)
  │   └── DOES apply to PHI_HUMANOID
  │
  ├── 2014/35/EU — Radio Equipment Directive (RED)
  │   ├── Applies to WiFi/BLE transmitter
  │   ├── Requires: EN 300 328 (WiFi)
  │   ├── Requires: EN 301 489-1 (EMC for radio)
  │   └── Module certification via RPi 5 WiFi
  │
  ├── 2011/65/EU — RoHS
  │   ├── Restriction of hazardous substances
  │   ├── Limits: Pb, Hg, Cd, Cr6+, PBB, PBDE
  │   └── PHI_HUMANOID: Compliant (all components RoHS)
  │
  └── 2012/19/EU — WEEE
      ├── Waste electrical equipment recycling
      ├── Producer registration required
      └── WEEE symbol on product
```

### 3.2 EMC Standards

```
EMISSION STANDARDS:
  EN 61000-6-3: Generic emissions standard for residential
  ├── Radiated: 30MHz-1GHz: 30dBµV/m at 10m
  ├── Conducted: 150kHz-30MHz: 56-46dBµV
  └── Harmonics: EN 61000-3-2 (if >75W input)

IMMUNITY STANDARDS:
  EN 61000-6-2: Generic immunity standard for industrial
  ├── ESD: ±8kV contact, ±15kV air (EN 61000-4-2)
  ├── Radiated immunity: 3V/m, 80MHz-1GHz (EN 61000-4-3)
  ├── EFT: ±1kV on power ports (EN 61000-4-4)
  ├── Surge: ±1kV line-line, ±2kV line-earth (EN 61000-4-5)
  ├── Conducted immunity: 3V, 150kHz-80MHz (EN 61000-4-6)
  └── Power frequency mag: 30A/m (EN 61000-4-8)

TESTING STRATEGY:
  1. Pre-compliance: In-house EMC scanning
  2. Full compliance: Accredited lab (e.g., TÜV SÜD, SGS)
  3. Declaration of Conformity issued
  4. CE mark applied
```

### 3.3 CE Documentation

```
REQUIRED DOCUMENTS:
  ├── Technical file:
  │   ├── Design drawings
  │   ├── Circuit schematics
  │   ├── Bill of materials
  │   ├── Test reports (EMC, safety)
  │   ├── Risk assessment
  │   └── User manual
  │
  ├── EU Declaration of Conformity:
  │   ├── Product identification
  │   ├── Applicable directives and standards
  │   ├── Manufacturer name and address
  │   ├── Authorized EU representative (if outside EU)
  │   ├── Place and date
  │   └── Signature
  │
  └── CE marking:
      ├── CE mark on product
      ├── Minimum 5mm height
      ├── Permanent and legible
      └── Adjacent to manufacturer name/ID
```

---

## 4. Safety Standards

### 4.1 ISO 13482 — Personal Care Robot Safety

```
APPLICABILITY:
  PHI_HUMANOID_ROBOT is a personal care robot if used for:
  ├── Assistance in daily living
  ├── Physical support
  ├── Social interaction
  └── Personal safety

KEY REQUIREMENTS:
  1. Risk assessment per ISO 12100
  2. Mechanical safety:
     ├── Pinch points <8mm gap
     ├── Sharp edges R>0.5mm
     ├── No entrapment zones
     └── Emergency stop within reach
  3. Electrical safety:
     ├── No accessible live parts
     ├── Double insulation or protective earth
     └── Battery safety (UN38.3)
  4. Functional safety:
     ├── Safety-related control system
     ├── Software safety per IEC 61508
     └── SIL rating (target: SIL 2)
  5. Information for use:
     ├── Warning labels
     ├── User manual
     └── Installation instructions

COMPLIANCE STATUS:
  Design phase — requirements integrated into design documents
```

### 4.2 UL 3300 — Safety for Robots

```
APPLICABILITY:
  UL 3300 covers safety requirements for:
  ├── Service robots
  ├── Personal robots
  └── Educational robots

KEY REQUIREMENTS:
  1. Electrical safety:
     ├── Circuit protection (fuses, breakers)
     ├── Insulation requirements
     └── Grounding requirements
  2. Mechanical safety:
     ├── Moving part guards
     ├── Pinch point protection
     └── Stability (tip-over prevention)
  3. Battery safety:
     ├── Overcharge protection
     ├── Overdischarge protection
     ├── Short circuit protection
     └── Thermal runaway prevention
  4. Fire safety:
     ├── Flammability: UL 94 V-1 minimum for enclosures
     ├── PCB flammability: UL 94 V-0
     └── Wiring: UL VW-1 rated
  5. Environmental:
     ├── Operating temperature limits
     ├── Moisture resistance
     └── Altitude limits

COMPLIANCE STATUS:
  Design phase — material selections meeting UL requirements
```

### 4.3 Functional Safety (IEC 61508)

```
APPLICABILITY:
  Safety-critical functions:
  ├── Emergency stop
  ├── Motor current limiting
  ├── Balance control
  └── Collision detection

SIL ASSESSMENT:
  Severity: Serious (injury possible)
  Frequency: Continuous (robot always on)
  Avoidance: Difficult (user may not avoid)
  → SIL 2 required

SIL 2 REQUIREMENTS:
  ├── Hardware:
  │   ├── Diagnostic coverage >90%
  │   ├── Common cause failure (CCF) score >65
  │   ├── Safe failure fraction (SFF) >90%
  │   └── Redundant safety channels
  │
  ├── Software:
  │   ├── V-model development process
  │   ├── Unit testing >95% coverage
  │   ├── Integration testing
  │   └── Verification and validation
  │
  └── Documentation:
      ├── Safety requirements specification
      ├── Design documentation
      ├── Verification reports
      └── Validation reports

COMPLIANCE STRATEGY:
  1. Dual-channel safety architecture (hardware + software watchdog)
  2. Failsafe motor controllers (ODrive with fault detection)
  3. Redundant emergency stop circuit
  4. Formal verification of safety software
  5. Third-party assessment (TÜV or equivalent)
```

---

## 5. Battery Compliance

### 5.1 UN38.3 — Lithium Battery Transport

```
TESTING REQUIRED:
  ├── T.1: Altitude simulation (11.6 kPa)
  ├── T.2: Thermal test (-40°C to +75°C)
  ├── T.3: Vibration (random, 3 hours per axis)
  ├── T.4: Shock (150g, 6ms)
  ├── T.5: External short circuit (0.1Ω, 10 min)
  ├── T.6: Impact/crush (9.1kg, 152mm drop)
  ├── T.7: Overcharge (2× rated current)
  └── T.8: Forced discharge (reverse current)

DOCUMENTATION:
  ├── UN38.3 test summary
  ├── Battery specification
  ├── Safety data sheet (SDS)
  └── Transport documentation

LiFePO4 ADVANTAGE:
  ├── Inherently safer than NMC Li-ion
  ├── Higher thermal stability (800°C vs 150°C)
  ├── No thermal runaway in normal conditions
  └── Lower UN38.3 risk classification
```

### 5.2 IEC 62619 — Secondary Lithium Cells

```
APPLICABILITY:
  Industrial lithium battery safety

KEY REQUIREMENTS:
  ├── Overcharge protection
  ├── Overdischarge protection
  ├── Overcurrent protection
  ├── Short circuit protection
  ├── Thermal protection
  └── Cell balancing

COMPLIANCE:
  FPB-10 battery module includes integrated BMS meeting IEC 62619.
  Battery supplier provides test certificates.
```

---

## 6. Environmental Compliance

### 6.1 RoHS (2011/65/EU)

```
RESTRICTED SUBSTANCES:
  ├── Lead (Pb): <1000 ppm
  ├── Mercury (Hg): <1000 ppm
  ├── Cadmium (Cd): <100 ppm
  ├── Hexavalent chromium (Cr6+): <1000 ppm
  ├── PBB: <1000 ppm
  └── PBDE: <1000 ppm

EXEMPTIONS:
  ├── High-melting-point solder (Pb in electronics): Exemption 7(a)
  ├── Lead in copper alloy: Exemption 6(c)
  └── Lead in solders for server/storage: Exemption 7(a-i)

COMPLIANCE:
  All components sourced from RoHS-compliant suppliers.
  BOM includes RoHS compliance declaration for each component.
```

### 6.2 REACH

```
APPLICABILITY:
  Registration, Evaluation, Authorization, and Restriction of Chemicals

KEY ACTIONS:
  1. SVHC (Substances of Very High Concern) screening:
     ├── Check all materials against ECHA SVHC list
     ├── Update screening quarterly
     └── Current status: No SVHCs identified in BOM
  2. Communication:
     ├── Provide SVHC information to customers
     └── Include in product documentation
```

### 6.3 WEEE (2012/19/EU)

```
PRODUCER OBLIGATIONS:
  ├── Register with WEEE compliance scheme
  ├── Apply WEEE symbol (crossed-out wheelie bin) to product
  ├── Finance collection and recycling
  └── Report placed-on-market quantities

LABELING:
  WEEE symbol on product and packaging
  "Do not dispose of in household waste"
```

---

## 7. International Market Requirements

### 7.1 Market-Specific Requirements

| Market | Certification | Standards | Timeline |
|--------|--------------|-----------|----------|
| USA | FCC Part 15 | FCC, UL 3300 | Phase 1 |
| EU | CE Marking | EN 61000-6-2/3, EN 300 328 | Phase 1 |
| UK | UKCA Marking | BS EN 61000-6-2/3 | Phase 1 |
| Canada | ISED | RSS-247, CAN/CSA-C22.2 | Phase 2 |
| Japan | MIC/TELEC | ARIB STD-T66 | Phase 2 |
| China | SRRC/CCC | GB 4943.1, GB 9254 | Phase 2 |
| Australia | RCM | AS/NZS CISPR 32 | Phase 2 |
| South Korea | KC | KN 32, KN 35 | Phase 3 |

### 7.2 Country-of-Origin Labeling

```
REQUIRED ON ALL PRODUCTS:
  "Made in [Country]"
  
  For US market:
  ├── 19 U.S.C. §1304 — Country of origin marking
  ├── CBP rulings on robot classification
  └── Marking must be legible, permanent, in English

PLACEMENT:
  ├── On robot chassis (permanent marking)
  ├── On packaging
  └── In product documentation
```

---

## 8. Compliance Roadmap

### 8.1 Phase 1: Pre-Compliance (Months 1-6)

```
ACTIONS:
  □ Complete design review for EMC
  □ Perform pre-compliance EMC testing
  □ Verify RoHS compliance of all components
  □ Document UN38.3 battery test results
  □ Draft user manual with safety warnings
  □ Create technical file
  □ Select accredited test lab
```

### 8.2 Phase 2: Certification (Months 6-12)

```
ACTIONS:
  □ Submit for FCC Part 15 testing
  □ Submit for CE EMC testing (EN 61000-6-2/3)
  □ Submit for CE RED testing (WiFi/BLE)
  □ Complete UL 3300 safety assessment
  □ Complete ISO 13482 risk assessment
  □ Issue EU Declaration of Conformity
  □ Apply FCC ID and CE marking
```

### 8.3 Phase 3: Market Entry (Months 12-18)

```
ACTIONS:
  □ Register with WEEE compliance scheme
  □ Register as RoHS producer
  □ Submit for UKCA marking (UK)
  □ Begin additional market certifications
  □ Establish recall process
  □ Create compliance documentation archive
```

---

## 9. Labeling Summary

```
┌─────────────────────────────────────────────────────────────────┐
│                    PRODUCT LABEL (example)                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                                                          │  │
│  │  PHI_HUMANOID_ROBOT v1.0                                 │  │
│  │                                                          │  │
│  │  FCC ID: 2AXGP-RPI5                                     │  │
│  │  FCC Part 15 Compliant — Class B Digital Device          │  │
│  │                                                          │  │
│  │  [CE Mark] [UKCA Mark] [WEEE Symbol]                     │  │
│  │                                                          │  │
│  │  Input: 48V DC, 20A max                                  │  │
│  │  Battery: LiFePO4, 48V, 10kWh (×4)                      │  │
│  │                                                          │  │
│  │  Manufacturer: [Company Name]                             │  │
│  │  [Address]                                               │  │
│  │                                                          │  │
│  │  Made in [Country]                                       │  │
│  │  Serial No: PHI-XXXXXXXX                                 │  │
│  │                                                          │  │
│  │  WARNING: See user manual for safety instructions.       │  │
│  │  Not suitable for children under 14.                     │  │
│  │  Adult supervision required during operation.            │  │
│  │                                                          │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

*Document: 09_REGULATORY.md — PHI_HUMANOID_ROBOT Regulatory Compliance*
*Version: 1.0 | Date: 2026-08-27*
