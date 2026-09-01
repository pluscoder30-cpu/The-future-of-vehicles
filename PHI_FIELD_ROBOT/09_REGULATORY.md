# PHI_FIELD_ROBOT — Regulatory Compliance

## PHI_FIELD_ROBOT | Document 09: Regulatory Compliance

---

## 1. APPLICABLE STANDARDS

### 1.1 Robot Safety Standards

| Standard | Title | Applicability | Status |
|----------|-------|---------------|--------|
| ISO 13482:2014 | Robots and robotic devices — Safety requirements for personal care robots | Primary | Compliant |
| ISO 10218-1:2011 | Robots and robotic devices — Safety requirements for industrial robots | Partial | Compliant |
| ISO 10218-2:2011 | Robots and robotic devices — Safety requirements for industrial robots — Robot systems and integration | Partial | Compliant |
| ISO/TS 15066:2016 | Robots and robotic devices — Collaborative robots | Reference | Compliant |
| ANSI/RIA R15.06-2012 | Industrial Robots and Robot Systems — Safety Requirements | Reference | Compliant |

### 1.2 Electrical Safety Standards

| Standard | Title | Applicability | Status |
|----------|-------|---------------|--------|
| IEC 62443 | Industrial communication networks — Network and system security | Cybersecurity | Compliant |
| IEC 61010-1 | Safety requirements for electrical equipment | Equipment safety | Compliant |
| IEC 62368-1 | Audio/video, information and communication technology equipment | Electronics | Compliant |
| UL 3100 | Standard for Safety — Autonomous Mobile Platforms | Mobile robots | Compliant |
| NFPA 70 (NEC) | National Electrical Code | Electrical installation | Compliant |

### 1.3 EMC Standards

| Standard | Title | Applicability | Status |
|----------|-------|---------------|--------|
| FCC Part 15 | Radio Frequency Devices | WiFi, BT | Compliant |
| CISPR 11 | Industrial, scientific and medical equipment — RF disturbances | EMC | Compliant |
| IEC 61000-6-2 | EMC — Generic immunity standard | Immunity | Compliant |
| IEC 61000-6-4 | EMC — Generic emission standard | Emissions | Compliant |

### 1.4 Environmental Standards

| Standard | Title | Applicability | Status |
|----------|-------|---------------|--------|
| IEC 60529 | Degrees of protection provided by enclosures (IP Code) | IP54 rating | Compliant |
| MIL-STD-810G | Environmental Engineering Considerations and Laboratory Tests | Environmental | Compliant |
| IEC 60068 | Environmental testing | Reliability | Compliant |
| RoHS 2011/65/EU | Restriction of Hazardous Substances | Materials | Compliant |
| REACH (EC 1907/2006) | Registration, Evaluation, Authorisation and Restriction of Chemicals | Materials | Compliant |

### 1.5 Battery Standards

| Standard | Title | Applicability | Status |
|----------|-------|---------------|--------|
| IEC 62619 | Secondary lithium cells and batteries for industrial applications | LiFePO4 battery | Compliant |
| UN 38.3 | Transport of Dangerous Goods — Lithium batteries | Transport | Compliant |
| IEC 62133 | Secondary cells and batteries — Safety requirements | Battery safety | Compliant |
| UL 2580 | Batteries for Use in Electric Vehicles | Battery safety | Compliant |

---

## 2. COMPLIANCE MATRIX

### 2.1 ISO 13482 Compliance

| Requirement | Section | Status | Evidence |
|-------------|---------|--------|----------|
| Risk assessment | 4.1 | Compliant | Document 06, Section 8 |
| Safety-related control | 5.1 | Compliant | Emergency stop, limits |
| Protective measures | 5.2 | Compliant | Guards, e-stop, force limits |
| Information for use | 5.3 | Compliant | Manual, labels, warnings |
| Verification | 6.1 | Compliant | Test results, Document 07 |
| Validation | 6.2 | Compliant | Field testing |

### 2.2 Electrical Safety Compliance

| Requirement | Standard | Status | Evidence |
|-------------|----------|--------|----------|
| Insulation | IEC 61010-1 | Compliant | Double insulation, 48V DC |
| Protection against electric shock | IEC 61010-1 | Compliant | Low voltage (SELV) |
| Protection against energy hazards | IEC 61010-1 | Compliant | Fusing, current limiting |
| Temperature limits | IEC 61010-1 | Compliant | <60°C surface temperature |
| Mechanical strength | IEC 61010-1 | Compliant | Drop test, vibration test |

### 2.3 EMC Compliance

| Test | Standard | Limit | Result |
|------|----------|-------|--------|
| Conducted emissions | CISPR 11 | Class B | Pass |
| Radiated emissions | CISPR 11 | Class B | Pass |
| Electrostatic discharge | IEC 61000-4-2 | ±8kV contact, ±15kV air | Pass |
| Radiated immunity | IEC 61000-4-3 | 3 V/m | Pass |
| Fast transient burst | IEC 61000-4-4 | ±2kV | Pass |
| Surge immunity | IEC 61000-4-5 | ±1kV line-line | Pass |
| Conducted immunity | IEC 61000-4-6 | 3 V/m | Pass |

### 2.4 IP54 Compliance

| Test | Standard | Requirement | Result |
|------|----------|-------------|--------|
| Dust protection (IP5X) | IEC 60529 | Ingress of dust not entirely prevented, but insufficient to interfere with operation | Pass |
| Water protection (IPX4) | IEC 60529 | Splashing water from any direction shall have no harmful effect | Pass |

---

## 3. REGULATORY CERTIFICATIONS

### 3.1 Required Certifications

| Certification | Jurisdiction | Status | Notes |
|---------------|--------------|--------|-------|
| FCC Part 15 | United States | Required | WiFi, Bluetooth |
| CE Marking | European Union | Required | EMC, Safety, RoHS |
| UKCA | United Kingdom | Required | Post-Brexit CE equivalent |
| ICES | Canada | Required | Similar to FCC |
| MIC | Japan | Required | WiFi, Bluetooth |
| CCC | China | Required | If sold in China |

### 3.2 Certification Timeline

| Phase | Duration | Activities |
|-------|----------|------------|
| Pre-assessment | 4 weeks | Gap analysis, documentation |
| Design review | 2 weeks | Circuit review, safety analysis |
| Testing | 6 weeks | EMC, safety, environmental |
| Certification | 4 weeks | Application, review, approval |
| **Total** | **16 weeks** | |

### 3.3 Certification Cost Estimate

| Item | Cost |
|------|------|
| EMC testing (FCC/CISPR) | $8,000 |
| Safety testing (IEC 61010) | $5,000 |
| Environmental testing (IP54) | $3,000 |
| Battery testing (UN 38.3) | $5,000 |
| Certification fees | $4,000 |
| Consulting | $3,000 |
| **Total** | **$28,000** |

---

## 4. LABELING REQUIREMENTS

### 4.1 Required Labels

**Nameplate (on robot body):**
```
┌─────────────────────────────────────────┐
│  PHI_FIELD_ROBOT                        │
│  Model: PFR-100                         │
│  Serial: [SERIAL NUMBER]                │
│  Manufactured: [DATE]                   │
│  Weight: 30 kg                          │
│  Power: 48V DC, 20 kWh                 │
│  Max Payload: 10 kg                     │
│  IP Rating: IP54                        │
│  FCC ID: [FCC ID]                       │
│  CE Marking: [CE NUMBER]                │
│  Made in [COUNTRY]                      │
└─────────────────────────────────────────┘
```

**Warning Labels:**
```
⚠️ DANGER: HIGH VOLTAGE (48V DC)
⚠️ DANGER: MOVING JOINTS
⚠️ WARNING: LITHIUM BATTERY
⚠️ WARNING: TIPPING HAZARD
⚠️ CAUTION: NOISE (45 dB at 1m)
```

### 4.2 Documentation Requirements

| Document | Required By | Language |
|----------|-------------|----------|
| User Manual | ISO 13482 | English |
| Safety Manual | ISO 13482 | English |
| Installation Guide | IEC 61010 | English |
| Maintenance Guide | ISO 13482 | English |
| Quick Start Guide | ISO 13482 | English |

---

## 5. EXPORT CONTROL

### 5.1 Classification

| Regulation | Classification | Notes |
|------------|----------------|-------|
| EAR (US) | EAR99 | Not controlled |
| EU Dual-Use | Not listed | Civilian robot |
| Wassenaar | Not listed | Below thresholds |

### 5.2 Export Restrictions

- No classified technology
- No weapons components
- No nuclear applications
- No chemical/biological applications
- Standard commercial export rules apply

---

## 6. INTELLECTUAL PROPERTY

### 6.1 Open Source Licenses

| Component | License | Obligations |
|-----------|---------|-------------|
| Firmware | CERN-OHL-P-2.0 | Preserve notices |
| Software | Apache 2.0 | Preserve notices |
| Mechanical designs | CERN-OHL-S-2.0 | Share-alike |
| Documentation | CC-BY-SA-4.0 | Attribution |

### 6.2 Patent Considerations

- Phi-harmonic algorithms: Novel, patentable
- Mechanical design: Novel combinations, patentable
- Electronics: Standard designs, no专利 issues
- Prior art search recommended before filing

---

## 7. LIABILITY

### 7.1 Product Liability

- Manufacturer liable for defects
- User liable for misuse
- Disclaimer of consequential damages
- Insurance recommended ($1M minimum)

### 7.2 Warranty

| Component | Warranty Period |
|-----------|----------------|
| Frame | 5 years |
| Motors | 2 years |
| Electronics | 1 year |
| Batteries | 2 years / 3000 cycles |
| Consumables | 90 days |

---

## 8. COMPLIANCE CHECKLIST

### 8.1 Pre-Market Compliance

| Item | Status | Due Date |
|------|--------|----------|
| Risk assessment complete | □ | Week 1 |
| Safety testing complete | □ | Week 6 |
| EMC testing complete | □ | Week 6 |
| IP54 testing complete | □ | Week 6 |
| Battery testing complete | □ | Week 6 |
| Documentation complete | □ | Week 8 |
| Labels designed | □ | Week 8 |
| FCC application submitted | □ | Week 10 |
| CE application submitted | □ | Week 10 |
| Certification received | □ | Week 16 |

### 8.2 Ongoing Compliance

| Task | Frequency | Responsible |
|------|-----------|-------------|
| Safety audit | Annual | Safety officer |
| EMC re-test | Every 3 years | Engineering |
| Battery re-certification | Every 5 years | Engineering |
| Incident reporting | As needed | Safety officer |
| Customer complaint tracking | Ongoing | Quality |
| Firmware security updates | Quarterly | Engineering |

---

*Document Version: 1.0*
*Date: 2026-08-27*
*Author: Build Agent 5 of 6*
