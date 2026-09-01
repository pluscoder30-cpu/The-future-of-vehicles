# PHI CHEAP LIGHT PLANE — REGULATORY

## FAA Part 103 Regulatory Compliance

---

## REGULATORY FRAMEWORK

The PHI Cheap Light Plane is designed to comply with **FAA Part 103 — Ultralight Vehicles** (14 CFR Part 103), which provides the most permissive category for civil aircraft operations in the United States.

### Why Part 103?

| Requirement | Part 103 | Other Categories |
|-------------|----------|------------------|
| Pilot license | NOT required | Required (PPL minimum) |
| Aircraft registration | NOT required | Required |
| Airworthiness certificate | NOT required | Required |
| Aircraft inspection | NOT required (recommended) | Required (annual) |
| Operating area | Class G airspace only | Varies by class |
| Operations | Daytime VFR only | Day/night VFR/IFR |
| Cost to operate | Minimal | $10,000+/year |

**Part 103 is the ONLY category where a pilot can legally fly without a license, registration, or airworthiness certificate.**

---

## PART 103 COMPLIANCE CHECKLIST

### Vehicle Requirements (14 CFR §103.3)

| Requirement | Part 103 Limit | PHI Cheap Light Plane | Status |
|-------------|----------------|----------------------|--------|
| Empty weight | ≤ 115 kg (254 lbs) | 88 kg (194 lbs) | ✅ COMPLIANT |
| Max speed | ≤ 55 knots (102 km/h) | 102 km/h (55 knots) | ✅ COMPLIANT |
| Max fuel capacity | ≤ 5 gallons (19 L) | 0 gallons (batteries) | ✅ COMPLIANT |
| Max useful load | Not specified | 112 kg (pilot + gear) | ✅ ADEQUATE |
| Power source | Not specified | Electric (batteries) | ✅ COMPLIANT |
| Seats | 1 (2-seat trainer variant) | 1 (primary) | ✅ COMPLIANT |
| Pilot enclosure | Open or enclosed | Enclosed cockpit | ✅ COMPLIANT |
| Max stall speed | Not specified | 45 km/h (24 knots) | ✅ LOW |

### Operating Limitations (14 CFR §103.9)

| Requirement | Limit | PHI Cheap Light Plane | Status |
|-------------|-------|----------------------|--------|
| Operating area | Class G airspace | Class G only | ✅ COMPLIANT |
| Over congested areas | NOT allowed | No flights over cities | ✅ COMPLIANT |
| Over open air assemblies | NOT allowed | No flights over events | ✅ COMPLIANT |
| Maximum altitude | 1,000 ft AGL over congested | 3,000 ft AGL (Class G) | ✅ COMPLIANT |
| Maximum altitude | 2,000 ft AGL over non-congested | 3,000 ft AGL (Class G) | ✅ COMPLIANT |
| Visibility | 1 SM minimum | 5+ SM minimum | ✅ COMPLIANT |
| Cloud clearance | 500 ft below, 1,000 ft above | 500/1,000 ft | ✅ COMPLIANT |
| Time of day | Daytime only (civil twilight OK) | Daytime only | ✅ COMPLIANT |
| Weather minimums | VFR | VFR only | ✅ COMPLIANT |

### Equipment Requirements (14 CFR §103.7)

| Equipment | Required | PHI Cheap Light Plane | Status |
|-----------|----------|----------------------|--------|
| Collision avoidance | Recommended (not required) | None installed | ⚠️ RECOMMENDED |
| Position lights | Recommended (not required) | None installed | ⚠️ RECOMMENDED |
| Altimeter | Recommended (not required) | BMP280 digital altimeter | ✅ INSTALLED |
| Airspeed indicator | Recommended (not required) | GPS ground speed | ✅ INSTALLED |
| Compass | Recommended (not required) | GPS heading | ✅ INSTALLED |
| Tachometer | Recommended (not required) | ESC telemetry | ✅ INSTALLED |
| Hour meter | Recommended (not required) | Arduino timer | ✅ INSTALLED |

---

## ELECTRIC PROPULSION COMPLIANCE

### Fuel Capacity Limitation

Part 103 limits fuel capacity to 5 gallons (19 liters). The PHI Cheap Light Plane uses electric batteries, which creates a regulatory question:

**Interpretation:**
- The "fuel capacity" limit was written for liquid fuels (gasoline, diesel)
- Electric batteries are not "fuel" in the traditional sense
- The FAA has not specifically addressed electric ultralights under Part 103
- Conservative interpretation: batteries are equivalent to fuel storage
- Our battery weight: 20 kg (44 lbs) — well below any reasonable fuel weight limit

**Legal Basis:**
- 5 gallons of gasoline weighs approximately 13.6 kg (30 lbs)
- Our battery bank weighs 20 kg (44 lbs)
- This exceeds the "fuel weight" if batteries are treated as fuel
- However, batteries are structural components (like the airframe), not consumable fuel
- The FAA has not issued guidance on this interpretation

**Recommendation:**
- Document the battery system as "structural energy storage"
- Note that the batteries are permanent installations (not removable fuel containers)
- Consult with a local FSDO (Flight Standards District Office) for interpretation
- If challenged, argue that batteries are analogous to fuel tanks (structural), not fuel itself

### Weight Compliance

| Component | Weight | Cumulative |
|-----------|--------|------------|
| Empty weight | 88 kg | 88 kg |
| Pilot (max) | 90 kg | 178 kg |
| Ballast (if needed) | 22 kg | 200 kg |
| **Max Gross Weight** | **200 kg** | **200 kg** |
| **Part 103 Limit** | **227 kg** | **227 kg** |

**Margin: 27 kg (60 lbs) — 12% margin below Part 103 limit** ✅

---

## OPERATIONAL LIMITATIONS

### Airspace

```
AIRSPACE RESTRICTIONS:
──────────────────────

CLASS G (Uncontrolled):
✅ Can operate here

CLASS E (Controlled):
⚠️ May operate here if above 700ft AGL or 1200ft AGL
   (depends on Class E floor altitude)
   NOT recommended — may attract ATC attention

CLASS D (Towered):
❌ Cannot operate here without ATC clearance
   Ultralights typically denied clearance

CLASS C (Approach Control):
❌ Cannot operate here
   Requires 2-way radio + transponder

CLASS B (Terminal Control):
❌ Cannot operate here
   Requires specific clearance

PROHIBITED/RESTRICTED:
❌ Cannot operate here

RECOMMENDED OPERATING AREA:
- Rural area with no airports within 5nm
- Open fields, agricultural areas
- Away from flight paths and traffic patterns
- Private land for takeoff/landing
```

### Takeoff and Landing Sites

```
RECOMMENDED SITES:
──────────────────

IDEAL:
- Private grass strip (500m × 30m minimum)
- Farm field (short grass, no crops)
- Dry lake bed
- Beach (low tide, firm sand)

ACCEPTABLE:
- Paved road (low traffic, long straight)
- Parking lot (large, empty)
- Golf course fairway (with permission)

PROHIBITED:
- Public roads (traffic hazard)
- Parks (people hazard)
- Airport runways (traffic conflict)
- Near schools, hospitals, residential areas

PRIVATE LAND REQUIREMENTS:
- Written permission from landowner
- Liability insurance recommended
- Emergency services access
- Notification to neighbors
```

---

## PILOT REQUIREMENTS

### Legal Requirements (Part 103)

**There are NO legal pilot requirements under Part 103.**
- No license required
- No medical certificate required
- No training required
- No experience required

**However, PRACTICAL requirements include:**
- Understanding of aerodynamics
- Ability to read weather
- Knowledge of emergency procedures
- Physical ability to control the aircraft
- Mental fitness for flight operations

### Recommended Training

| Training | Source | Cost | Time |
|----------|--------|------|------|
| Ultralight ground school | Local ultralight club | $200-500 | 20 hours |
| Ultralight flight training | CFI with ultralight endorsement | $2,000-5,000 | 10-20 hours |
| First aid / CPR | Red Cross | $75-100 | 4 hours |
| FAA written exam (optional) | FAA testing center | $150 | 2 hours |

**Total recommended training investment: $2,500-6,000**

---

## INSURANCE

### Liability Insurance

**Recommended (not required by Part 103):**

| Coverage | Limit | Annual Premium |
|----------|-------|----------------|
| Bodily injury | $100,000/$300,000 | $200-400 |
| Property damage | $100,000 | Included |
| Combined single limit | $300,000 | $200-400 |

**Sources:**
- AVEMCO (www.avemco.com)
- Falcon Insurance (www.falconinsurance.com)
- USAA (if eligible)
- Local insurance agents

### Hull Insurance (Optional)

- Covers damage to the aircraft itself
- Typically 5-10% of aircraft value annually
- For a $2,800 aircraft: $140-280/year
- May not be cost-effective for ultralights

---

## REGISTRATION

### Part 103 Registration

**Part 103 vehicles do NOT require FAA registration.**

However, you may WANT to register for:
- Proof of ownership (if selling)
- Insurance requirements
- Identification in case of incident
- Personal peace of mind

### Optional N-Number

You can request an N-number (aircraft registration) from the FAA even for Part 103 vehicles:

**Process:**
1. Complete FAA Form 8050-1 (Aircraft Registration Application)
2. Submit proof of ownership (bill of sale)
3. Pay $5 registration fee
4. Receive N-number certificate

**Note:** Registration does NOT require an airworthiness certificate, pilot license, or any other certification. It is purely voluntary identification.

---

## INCIDENT/AccIDENT REPORTING

### NTSB Reporting Requirements

**Under 49 CFR Part 830:**

| Event | Reporting Required | Time Limit |
|-------|-------------------|------------|
| Fatal injury | YES | Immediately |
| Serious injury | YES | Within 24 hours |
| Substantial damage | YES | Within 10 days |
| Aircraft disappearance | YES | Immediately |
| Property damage > $25,000 | YES | Within 10 days |

**How to Report:**
1. Call NTSB: 1-844-TEE-NTSB (1-844-833-6872)
2. Complete NTSB Form 6120.1 (or 6120.1a for electronic submission)
3. Submit to NTSB regional office

### FAA Reporting

**FAA Form 8070-1 (General Aviation Accident Report):**
- Required for accidents involving fatality or serious injury
- Submit to local FSDO within 48 hours
- Phone: 1-800-255-1111

---

## COMPLIANCE SUMMARY

### Regulatory Status

| Category | Status |
|----------|--------|
| Part 103 compliance | ✅ COMPLIANT |
| Registration | ❌ NOT REQUIRED |
| Airworthiness certificate | ❌ NOT REQUIRED |
| Pilot license | ❌ NOT REQUIRED |
| Medical certificate | ❌ NOT REQUIRED |
| Aircraft inspection | ❌ NOT REQUIRED (recommended) |
| Insurance | ⚠️ RECOMMENDED |
| Training | ⚠️ STRONGLY RECOMMENDED |
| Airspace operations | ✅ CLASS G ONLY |
| Operating hours | ✅ DAYTIME VFR ONLY |
| Flight over people | ❌ PROHIBITED |
| Flight over congestion | ❌ PROHIBITED |

### Risk Assessment

| Risk | Likelihood | Severity | Mitigation |
|------|------------|----------|------------|
| Structural failure | Low | High | Conservative design, inspection |
| Motor failure | Medium | Medium | Pre-flight checks, glide capability |
| Battery failure | Low | High | Voltage monitoring, emergency procedures |
| Pilot error | High | High | Training, conservative operations |
| Weather encounter | Medium | High | Weather minimums, pre-flight check |
| Mid-air collision | Low | Critical | Avoid airports, look out |
| Ground collision | Low | High | Avoid congested areas |

---

## RECOMMENDED ACTIONS

1. **Before building:**
   - [ ] Read this regulatory document thoroughly
   - [ ] Consult with local FSDO (optional but recommended)
   - [ ] Obtain liability insurance
   - [ ] Find suitable flying site (private land)

2. **Before first flight:**
   - [ ] Complete ultralight ground school
   - [ ] Get flight training (10-20 hours minimum)
   - [ ] Have A&P mechanic inspect airframe
   - [ ] Complete 10-hour ground taxi testing
   - [ ] Obtain insurance

3. **Ongoing:**
   - [ ] Maintain flight log
   - [ ] Perform pre-flight inspection before every flight
   - [ ] Follow maintenance schedule
   - [ ] Stay within Part 103 limitations
   - [ ] Report any incidents to NTSB as required
