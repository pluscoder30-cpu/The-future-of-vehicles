# Personal Mobility Device Regulatory Analysis

## Purpose

This document maps the regulatory landscape for personal mobility devices across BC, USA, UK, and EU to identify **unregulated device categories**, **legal thresholds**, and **propulsion-based classification gaps** relevant to phi-harmonic propulsion systems.

---

## 1. Jurisdiction Overview: What's Regulated vs. What's Not

### British Columbia, Canada

**Legal devices (with conditions):**
| Device | Speed Limit | Power Limit | License/Insurance |
|--------|------------|-------------|-------------------|
| Light e-bike | 25 km/h assist | ≤ 250W | None |
| Standard e-bike | 32 km/h assist | ≤ 500W | None |
| Electric kick scooter (pilot only) | 25 km/h | — | None |
| Mobility scooter / wheelchair | 25 km/h | — | None |
| Limited-speed motorcycle | — | — | Yes (Class 5/7, insurance required) |

**ILLEGAL on public roads (no path to legalization):**
- Electric unicycles (One-Wheels)
- Hoverboards
- Electric skateboards
- Pocket motorcycles
- Any device without fully operable pedals AND CMVSS compliance label

**Key legal insight:** BC's Motor Vehicle Act uses a **positive-list approach** — if a device isn't explicitly authorized by legislation, it's illegal. The 2023 amendment renamed the category to "designated motorized devices" but the whitelist model persists. Fine: $598 for operating an unauthorized device.

**The "unlock trap":** Operating an e-bike or e-scooter in "off-road mode" that exceeds speed cutoffs (32 km/h e-bikes, 25 km/h e-scooters) instantly reclassifies it as a motor vehicle — requiring registration, insurance, and a license.

---

### United States (State-Level Patchwork)

**No federal definition** exists for most personal mobility devices. Classification varies by state:

| Device | California | New York | Texas | Florida | Michigan |
|--------|-----------|----------|-------|---------|----------|
| E-scooter | Legal (15 mph max, bike lanes) | Gray area / restricted in NYC | Legal (bike lanes) | Legal (statewide) | Legal |
| E-skateboard | Legal on roads ≤35 mph | Illegal (NYC Admin Code 19-176.2) | Gray area | Illegal on public roads | Legal (≤25 mph roads, ≤2500W) |
| Hoverboard | Illegal on public roads | Illegal (treated as motor vehicle in NYC) | Gray area | Varies by county | Gray area |
| E-unicycle | Varies | Varies | Varies | Varies | Varies |

**Key US definitions:**
- **NY State VTL 114-d:** "Electric personal assist mobility device" = self-balancing, two non-tandem wheeled device, ≤750W average output, max speed <12.5 mph on paved level surface. **Excluded from "motor vehicle" definition ONLY outside cities >1M population.**
- **Michigan MCL 257.13f:** "Electric skateboard" = wheeled device, floorboard ≤60" × 18", ≤2500W, max speed ≤25 mph on paved surface. Legal on roads with ≤25 mph speed limits.
- **California Vehicle Code §21213:** Motorized scooter = two-wheeled device with handlebars, floorboard for standing, electric motor. Legal on bike paths and roads ≤35 mph.

**States with no explicit legislation (devices exist in legal gray zone):**
- Idaho, Montana, Wyoming, Vermont — no specific PEMD statutes
- These states often default to "motor vehicle" classification, which effectively bans unregistered devices

---

### United Kingdom

**All privately-owned electric mobility devices are ILLEGAL on public roads** (as of 2025/2026):

| Device | Legal Status | Why |
|--------|-------------|-----|
| E-scooter (private) | Illegal | Classified as "motor vehicle" under Road Traffic Act 1988 |
| Hoverboard | Illegal on public roads | Classified as "Powered Transporter" / PLEV |
| Electric skateboard | Illegal on public roads | Same PLEV classification |
| E-unicycle | Illegal on public roads | Same PLEV classification |
| Segway | Illegal on public roads | Same PLEV classification |

**Legal exceptions:**
- Rental e-scooters in government-approved trial zones (limited cities)
- **LZEV category (2025 Transport Bill):** New "Low-speed Zero Emission Vehicle" class allows private e-scooters IF ≤25 km/h, ≤500W continuous, with lights/bell/dual brakes. This is the first legal pathway for private ownership.

**Private property exception:** All devices legal on private land with landowner consent.

**UK classification hierarchy:**
```
Powered Transporters (PLEVs)
  └── Motor Vehicles (Road Traffic Act 1988)
        ├── Must meet construction standards
        ├── Must be registered, taxed, insured
        ├── Must have MOT
        └── Cannot currently be registered = effectively banned
```

**Penalties:** Fixed penalty £100-£300, 6 penalty points on license, vehicle seizure.

---

### European Union

**Fragmented national approach** with EU-level harmonization underway:

| Country | E-scooter Legal | Max Speed | Max Power | Min Age | Insurance |
|---------|----------------|-----------|-----------|---------|-----------|
| Germany | Yes | 20 km/h | 500W | 14 | No |
| France | Yes | 25 km/h | — | 12 | No |
| Italy | Yes | 20 km/h | 500W | 14 | No |
| Spain | Yes | 25 km/h | 1000W | 14-16 | No |
| Netherlands | No (RDW approval needed) | — | — | — | — |
| Belgium | Yes | 25 km/h | 1000W | 16 | No |
| Finland | Yes | 25 km/h | 1000W | 15 | No |
| Norway | Yes | 20 km/h | No limit | 12 | Yes (mandatory) |
| Ireland | Yes | 20 km/h | 400W | 16 | No |

**EU-level developments:**
- **2024 EU Motor Insurance Directive:** Mandatory third-party liability insurance for devices exceeding 25 km/h or 25 kg
- **Regulation (EU) 2023/1945:** Creates "Electric Personal Mobility Device (EPMD)" category with type-approval requirements — fully applicable Jan 1, 2025
- **ETSC recommendation:** Universal 20 km/h max for all standing devices
- **EU Batteries Regulation (2023/1542):** Directs Commission to create micromobility device safety rules

**Hoverboards in EU:** Must meet Machinery Directive requirements. No specific vehicle-type-approval category exists yet. Treated as PLEVs — cannot be registered for road use in most member states.

---

## 2. Legal Definition: "Vehicle" vs. "Personal Mobility Device"

The classification boundary is the critical legal lever:

### Standard Vehicle Definition
> "Every device in, on, or by which any person or property is or may be transported or drawn upon a highway" — with self-propulsion via internal combustion or standard electric motor.

### Personal Mobility Device (Where It Gets Interesting)

**BC Motor Vehicle Act:**
- "Vehicle" excludes "designated motorized devices" (e-bikes, e-scooters in pilot, mobility scooters)
- The exclusion requires: fully operable pedals/cranks + CMVSS compliance label + speed ≤ threshold

**NY State VTL 125/126:**
- "Motor vehicle" excludes EPAMDs outside cities >1M population
- Inside NYC, EPAMDs ARE motor vehicles requiring registration (which DMV refuses to grant)

**UK Road Traffic Act 1988:**
- NO exclusion exists for PLEVs — they are motor vehicles, period
- The 2025 LZEV category creates the first carve-out

**EU framework:**
- Type A/B vehicles (≤25 km/h, ≤25 kg) are "micromobility" — not motor vehicles
- Type C/D (>25 km/h or >25 kg) require insurance and potentially registration

---

## 3. What "Bypasses" Means in Legal Terms

A device **bypasses** vehicle regulation when it satisfies ALL of these criteria:

1. **Propulsion type:** NOT internal combustion; may or may not be standard electric motor
2. **Speed threshold:** ≤ 25 km/h (15.5 mph) on paved level surface
3. **Power threshold:** ≤ 500W continuous (most jurisdictions) or ≤ 750W (NY State)
4. **Weight:** ≤ 25 kg (EU insurance threshold)
5. **Design intent:** Personal transport, not cargo/passenger hauling
6. **Auxiliary human power:** Has pedals or requires human propulsion assistance

**Devices that currently bypass regulation:**
- Pedal-assist e-bikes (≤250W, ≤25 km/h)
- Mobility scooters/wheelchairs (medical device classification)
- Electric kick scooters (in pilot jurisdictions)

**Devices that do NOT bypass regulation:**
- Hoverboards (self-balancing, no pedals = "motor vehicle" in UK/BC)
- E-skateboards (no pedals, no handlebars = "motor vehicle" classification)
- E-unicycles (self-balancing, no pedals = motor vehicle)
- Any device exceeding speed/power thresholds

---

## 4. Devices Requiring No License, Registration, or Insurance

| Device | BC | USA | UK | EU |
|--------|----|----|----|-----|
| Pedal-assist e-bike (≤250W) | ✅ No | ✅ Most states | ✅ As bicycle | ✅ Most countries |
| Throttle e-bike (≤500W, ≤32 km/h) | ✅ No | ✅ Most states | ✅ As moped (some) | ⚠️ Varies |
| Mobility scooter | ✅ No | ✅ ADA protected | ✅ As pedestrian aid | ✅ No |
| E-scooter (≤25 km/h, ≤500W) | ⚠️ Pilot only | ⚠️ Varies by state | ⚠️ Rental only (LZEV emerging) | ⚠️ Varies |
| Hoverboard | ❌ Illegal | ⚠️ Varies | ❌ Illegal (private) | ❌ Most countries |
| E-skateboard | ❌ Illegal | ⚠️ Varies (legal in MI, CA) | ❌ Illegal | ⚠️ Varies |
| E-unicycle | ❌ Illegal | ⚠️ Varies | ❌ Illegal | ⚠️ Varies |

---

## 5. Propulsion Classification Gap

### The Regulatory Assumption

All current vehicle law assumes propulsion comes from ONE of:
1. **Human power** (bicycle, walking)
2. **Internal combustion engine** (car, motorcycle)
3. **Standard electric motor** (EV, e-bike)

The law was written before non-standard propulsion existed. The key insight:

> **Devices using non-standard propulsion (not ICE, not conventional electric motor) may fall outside standard vehicle categories because the statutes don't contemplate them.**

### Classification Categories That DON'T Exist Yet

| Proposed Category | Description | Current Legal Status |
|-------------------|-------------|---------------------|
| Field-effect propulsion | No moving parts, electromagnetic field interaction | **Unclassified** — not in any statute |
| Acoustic levitation drive | Sound wave-based lift/thrust | **Unclassified** |
| Plasma-assisted propulsion | Ionized gas channel for thrust | **Unclassified** |
| Gravitational manipulation | PHI-harmonic field resonance | **Unclassified** |

These propulsion types don't fit "motor vehicle" definitions because:
- No "motor" in the conventional sense
- No "engine" (combustion or electric)
- No "mechanical propulsion" in most statutory definitions
- The UK's "motor vehicle" = "propelled by any power other than muscular power" is the broadest catch-all
- BC's "motor vehicle" = "vehicle propelled by any mechanical power" could arguably exclude non-mechanical propulsion

### The PHI-Harmonic Propulsion Classification

A phi-harmonic propulsion system would need to be classified as:

1. **Not a "motor vehicle"** if propulsion is field-based rather than mechanically transmitted
2. **Possibly a "personal mobility device"** if speed/power thresholds are met
3. **Potentially unregulated entirely** if no jurisdiction has contemplated the propulsion type

**Legal strategy implications:**
- In BC: If the device lacks "fully operable pedals" and isn't on the whitelist → illegal regardless of propulsion type
- In UK: The "power other than muscular power" catch-all would likely capture it
- In USA: State-by-state analysis needed; some states (MI, CA) have specific wattage/speed thresholds that don't specify motor type
- In EU: The type-approval framework assumes electric motors; non-electric field propulsion would need new categories

---

## 6. Key Thresholds Summary

| Threshold | Value | Where Defined |
|-----------|-------|---------------|
| Speed: unregulated | ≤ 25 km/h (15.5 mph) | BC, EU, most US states |
| Power: unregulated | ≤ 250-500W continuous | BC (250W light / 500W standard), EU (500W Germany) |
| Weight: insurance trigger | > 25 kg | EU 2024 Motor Insurance Directive |
| Speed: insurance trigger | > 25 km/h | EU 2024 Motor Insurance Directive |
| Speed: reclassification | > 32 km/h (e-bike), > 25 km/h (e-scooter) | BC "unlock trap" |
| Population: motor vehicle | > 1M | NY State VTL 126(a-1) |

---

## 7. Research Gaps & Opportunities

1. **No jurisdiction has addressed non-mechanical propulsion** — all statutes assume motors/engines
2. **UK's "power other than muscular" is the broadest** — hardest to bypass
3. **BC's positive-list approach** means new device types need explicit legislation
4. **US state patchwork** creates opportunities in states with specific wattage/speed thresholds but no motor-type requirement
5. **EU is moving toward harmonization** — window for classification influence is closing
6. **Private property is universally legal** — all devices can be used on private land
7. **Medical device classification** (mobility scooters) provides a template for bypassing vehicle regulation through medical necessity framing

---

*Last updated: August 2026*
*Sources: BC Motor Vehicle Act, NY State VTL, UK Road Traffic Act 1988, EU Regulation 2023/1945, ETSC recommendations, provincial/state government websites*
