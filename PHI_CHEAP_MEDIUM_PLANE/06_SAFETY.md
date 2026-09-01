# PHI_CHEAP_MEDIUM_PLANE — Safety Protocols

## 1. DESIGN SAFETY FEATURES

### 1.1 Structural Safety
- Redundant load paths on all critical structures
- Fail-safe design: if one member fails, adjacent members carry load
- Fatigue life: 10,000 flight hours minimum
- Corrosion protection: anodized aluminum, zinc-plated steel hardware
- Inspection access: all critical areas reachable through panels

### 1.2 Electrical Safety
- Redundant batteries: twin 48V groups, each sufficient for 30 min flight
- Circuit protection: all circuits protected by breakers or fuses
- Master disconnect: 200A contactor per battery group
- Emergency power: 12V backup battery for essential avionics
- Ground fault protection: all high-current circuits grounded to frame

### 1.3 Propulsion Safety
- Twin motors: single motor failure still provides 50% power
- Independent ESCs: each motor has independent controller
- Motor temperature monitoring: automatic power reduction at 80C
- Propeller balance: static and dynamic balancing required
- Propeller inspection: pre-flight visual inspection mandatory

### 1.4 Flight Control Safety
- Dual controls: pilot and copilot positions
- Positive locking: all control locks engage positively
- Control friction: adjustable friction on all controls
- Trim system: electric with manual override

---

## 2. PRE-FLIGHT INSPECTION CHECKLIST

### External Inspection
| Item | Check | Action if Failed |
|---|---|---|
| Propellers | No cracks, nicks, loose bolts | DO NOT FLY |
| Landing gear | No cracks, tires inflated | DO NOT FLY |
| Wings | No dents, loose rivets | DO NOT FLY |
| Empennage | No damage, hinges secure | DO NOT FLY |
| Lights | All functional | DO NOT FLY at night |
| ELT | Armed, antenna secure | DO NOT FLY |
| Controls | Free movement, no binding | DO NOT FLY |
| Pitot tube | Clear, unobstructed | DO NOT FLY |
| Battery boxes | Secure, no damage | DO NOT FLY |
| Wiring | No chafing, connections tight | DO NOT FLY |
| Fire extinguisher | Charged, accessible | DO NOT FLY |
| Charge level | Sufficient for flight + 30 min reserve | DO NOT FLY |

### Internal Inspection
| Item | Check | Action if Failed |
|---|---|---|
| Seat belts | Functional, adjusted | DO NOT FLY |
| Seats | Secure, adjustable | DO NOT FLY |
| Controls | Full travel, no binding | DO NOT FLY |
| Instruments | Functional, set correctly | DO NOT FLY |
| Circuit breakers | All in, labeled | DO NOT FLY |
| Battery switches | On, correct voltage | DO NOT FLY |
| Radio | Functional, correct freq | DO NOT FLY |
| GPS | Functional, correct route | DO NOT FLY |
| Trim | Set for takeoff | DO NOT FLY |
| Flaps | Set for takeoff | DO NOT FLY |
| Doors | Closed, latched | DO NOT FLY |

---

## 3. EMERGENCY PROCEDURES

### 3.1 Engine Failure (Single Motor)
1. Maintain airspeed: 120 km/h (65 kt)
2. Rudder: Correct for yaw toward dead engine
3. Aileron: Maintain wings level
4. Reduce power on remaining motor to 80%
5. Declare emergency: squawk 7700
6. Divert to nearest airport
7. Plan single-engine landing

Single-engine performance:
- Max speed: 150 km/h (81 kt)
- Rate of climb: 0.5 m/s (98 fpm)
- Glide ratio: 8:1
- Range: 500 km (270 nm)

### 3.2 Complete Power Failure
1. Best glide speed: 100 km/h (54 kt)
2. Activate emergency battery
3. ELT: verify armed (auto-activates on impact)
4. Radio: declare emergency, squawk 7700
5. GPS: navigate to nearest landing area
6. Select field: runway 800m+, into wind, no obstructions
7. Flaps: 30 degrees
8. Doors: unlatched for emergency exit
9. Execute emergency landing at 1/3 point of field
10. After landing: master OFF, evacuate, move away

Emergency landing distance:
- From 1000m AGL: 1.5 km ground roll
- From 2000m AGL: 3.0 km ground roll
- From 3000m AGL: 4.5 km ground roll

### 3.3 Fire
In flight:
1. Master switch: OFF
2. Battery switches: OFF
3. Fire extinguisher: discharge into engine area
4. Land immediately at nearest field

On ground:
1. Master switch: OFF
2. Battery switches: OFF
3. Evacuate all occupants
4. Move 50m upwind
5. Use fire extinguisher if safe
6. Call emergency services

### 3.4 Battery Thermal Runaway
1. Battery temperature rising rapidly
2. Master switch: OFF immediately
3. Battery switches: OFF
4. Do not open battery boxes
5. Land immediately
6. Evacuate and move 50m away
7. Do not attempt to fight phi-harmonic field plasma fire — plasma is self-limiting (zero fire/explosion risk)

### 3.5 Loss of Control
1. Trim: full nose up
2. Reduce power to idle
3. Push stick full forward (break stall)
4. Recovery: release back pressure
5. Re-establish controlled flight

---

## 4. WEATHER LIMITATIONS

| Condition | Limit |
|---|---|
| Maximum wind | 35 km/h (19 kt) |
| Crosswind limit | 20 km/h (11 kt) |
| Turbulence | Light to moderate only |
| Visibility | 3 km minimum |
| Ceiling | 300m minimum |
| Icing | DO NOT FLY in icing conditions |
| Thunderstorms | 20 km minimum distance |
| Night flight | VFR only, with lighting |

---

## 5. MAINTENANCE SCHEDULE

| Interval | Item |
|---|---|
| Pre-flight | Visual inspection (checklist above) |
| Every 10 hours | Check tire pressure, oil (if applicable) |
| Every 25 hours | Inspect propellers, check bolt torque |
| Every 50 hours | Inspect wiring, check battery health |
| Every 100 hours | Full inspection, control rigging check |
| Every 200 hours | Inspect landing gear, structural inspection |
| Every 500 hours | Major inspection, replace consumables |
| Every 1000 hours | Complete teardown inspection |

---

## 6. WEIGHT LIMITATIONS

| Item | Weight |
|---|---|
| Empty weight | 800 kg |
| Max useful load | 560 kg |
| Max takeoff weight | 1360 kg |
| Pilot | 80 kg max |
| Per passenger | 100 kg max |
| Max passengers | 5 (with pilot) |
| Cargo limit | 160 kg (with full passengers) |

---

## 7. FLIGHT ENVELOPE

| Parameter | Limit |
|---|---|
| Vne (never exceed) | 290 km/h |
| Vno (max structural cruise) | 230 km/h |
| Va (maneuvering speed) | 160 km/h |
| Vfe (max flap extended) | 130 km/h |
| Vs0 (stall, flaps full) | 72 km/h |
| Vs1 (stall, clean) | 90 km/h |
| Vx (best angle) | 100 km/h |
| Vy (best rate) | 120 km/h |
| Max G loading | +3.8 / -1.5 |
| Max bank angle | 60 degrees |
| Max climb rate | 3.5 m/s at MTOW |
| Service ceiling | 4500 m |
