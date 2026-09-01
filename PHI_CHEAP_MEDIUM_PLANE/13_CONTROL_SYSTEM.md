# PHI_CHEAP_MEDIUM_PLANE — Control System

## 1. FLIGHT CONTROL SYSTEM OVERVIEW

The PHI_CHEAP_MEDIUM_PLANE uses conventional cable-and-pull-pull control systems for primary flight controls, with electric辅助 for trim and throttle. All controls are mechanically linked with redundant cables.

---

## 2. PRIMARY FLIGHT CONTROLS

### 2.1 Aileron System
```
PILOT STICK ──[PUSH-PULL TUBE]──┬── LEFT AILERON CABLE
(350mm throw)                    │   (through pulleys)
                                 └── RIGHT AILERON CABLE
                                     (through pulleys)

CONTROL RATIO: 1:1 (direct)
DEFLECTION: +/-25 degrees
TRAVEL: 75mm at stick tip per 25 degrees
CABLE: 1/16" 7x19 galvanized
TURNBUCKLES: 4 total (2 per side)
PULLEYS: 6 total (3 per side)
```

#### Aileron Rigging
1. Set stick to neutral (center)
2. Adjust turnbuckles until ailerons are at 0 degrees
3. Check full travel: +/-25 degrees
4. Verify differential: uptravel 25 deg, downtravel 20 deg
5. Safety wire all turnbuckles
6. Check for binding through full range

### 2.2 Elevator System
```
PILOT STICK ──[PUSH-PULL TUBE]──┬── LEFT ELEVATOR CABLE
(PITCH movement)                │   (through pulleys)
                                └── RIGHT ELEVATOR CABLE
                                    (through pulleys)

CONTROL RATIO: 1:1 (direct)
DEFLECTION: +/-25 degrees
TRAVEL: 80mm at stick tip per 25 degrees
CABLE: 1/16" 7x19 galvanized
TURNBUCKLES: 4 total (2 per side)
PULLEYS: 4 total (2 per side)
```

#### Elevator Rigging
1. Set stick to neutral
2. Adjust turnbuckles until elevator is at 0 degrees
3. Check full travel: +/-25 degrees
4. Verify uptravel equals downtravel
5. Safety wire all turnbuckles
6. Check for binding through full range

### 2.3 Rudder System
```
RUDDER PEDALS ──[PUSH-PULL TUBE]──┬── LEFT RUDDER CABLE
(PEDAL movement)                   │   (through pulleys)
                                   └── RIGHT RUDDER CABLE
                                       (through pulleys)

CONTROL RATIO: 1:1 (direct)
DEFLECTION: +/-30 degrees
PEDAL TRAVEL: 200mm per side
CABLE: 1/16" 7x19 galvanized
TURNBUCKLES: 4 total (2 per side)
PULLEYS: 4 total (2 per side)
```

#### Rudder Rigging
1. Set pedals to neutral (center)
2. Adjust turnbuckles until rudder is at 0 degrees
3. Check full travel: +/-30 degrees
4. Verify left travel equals right travel
5. Safety wire all turnbuckles
6. Check for binding through full range
7. Connect nose gear steering (if applicable)

### 2.4 Flap System
```
FLAP HANDLE ──[CABLE]──┬── LEFT FLAP ACTUATOR
(CENTRAL HANDLE)       │   (through pulleys)
                       └── RIGHT FLAP ACTUATOR
                           (through pulleys)

DEFLECTION: 0 to 45 degrees (3 positions)
POSITIONS: 0 (UP), 15 (T/O), 30 (APPR), 45 (LAND)
HANDLE TRAVEL: 150mm total
CABLE: 1/16" 7x19 galvanized
PULLEYS: 4 total
POSITION INDICATOR: Mechanical, in cockpit
```

#### Flap Rigging
1. Set flap handle to 0 (UP)
2. Adjust cables until flaps are at 0 degrees
3. Move handle to 15 degrees (T/O)
4. Verify flaps at 15 degrees
5. Move handle to 30 degrees (APPR)
6. Verify flaps at 30 degrees
7. Move handle to 45 degrees (LAND)
8. Verify flaps at 45 degrees
9. Safety wire all connections

---

## 3. TRIM SYSTEM

### 3.1 Electric Trim
```
┌─────────────────────────────────────────────────────────────┐
│                    ELECTRIC TRIM SYSTEM                       │
│                                                              │
│  TRIM SWITCH ──[ELECTRIC]── LINEAR ACTUATOR                 │
│  (3-position)              (12V, 10mm/s)                    │
│                               │                              │
│                          ┌────┴────┐                        │
│                          │ ELEVATOR│                        │
│                          │ TRIM TAB│                        │
│                          └─────────┘                        │
│                                                              │
│  TRIM RANGE: +/-10 degrees                                  │
│  TRIM SPEED: 10mm per second                                │
│  ACTUATOR FORCE: 50N                                        │
│  POSITION FEEDBACK: 10K potentiometer                       │
│  DISPLAY: LED indicator in cockpit                          │
│                                                              │
│  TRIM SETTINGS:                                              │
│  - Full nose up: heavy load, slow flight                    │
│  - Neutral: normal cruise                                   │
│  - Full nose down: light load, fast flight                  │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Trim Control
- Switch location: Center console, within easy reach
- Switch type: 3-position momentary (UP/NEUTRAL/DOWN)
- Indicator: LED bar showing trim position
- Manual override: Push elevator fully forward/back to override trim

### 3.3 Trim Settings
| Phase | Trim Setting | Notes |
|---|---|---|
| Takeoff | 2 degrees nose up | For rotation |
| Climb | 1-2 degrees nose up | For climb attitude |
| Cruise | Neutral | For level flight |
| Approach | 1 degree nose up | For slow flight |
| Landing | 2-3 degrees nose up | For flare |
| Emergency | Full nose up | For stall recovery |

---

## 4. THROTTLE SYSTEM

### 4.1 Dual Throttle Quadrant
```
┌─────────────────────────────────────────────────────────────┐
│                    DUAL THROTTLE QUADRANT                     │
│                                                              │
│  LEFT THROTTLE ──[ELECTRIC]── ESC-L                        │
│  (DUAL HANDLE)    (SIGNAL)     (MOTOR-L)                    │
│                                                              │
│  RIGHT THROTTLE ──[ELECTRIC]── ESC-R                       │
│  (DUAL HANDLE)    (SIGNAL)     (MOTOR-R)                    │
│                                                              │
│  THROTTLE TYPE: Electric signal (PWM)                       │
│  THROTTLE RANGE: 0 to 100%                                 │
│  HANDLE TRAVEL: 100mm total                                │
│  SPLIT THROTTLE: Yes (independent control)                 │
│  SYNCHRONIZER: Optional electric sync                      │
│                                                              │
│  THROTTLE POSITIONS:                                        │
│  - Idle: 0% (motors off)                                   │
│  - Cruise: 60-70% (normal cruise)                          │
│  - Max: 100% (takeoff/climb)                               │
│  - Reverse: Not available (regenerative only)              │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 Throttle Quadrant Details
| Parameter | Value |
|---|---|
| Type | Dual, side-by-side |
| Handles | 2 (Left, Right) |
| Travel | 100mm |
| Detents | Idle, Cruise, Max |
| Sync mode | Electric (optional) |
| Material | Aluminum, anodized |
| Mounting | Center console |
| Connection | 10K potentiometer to MCU |

### 4.3 Throttle Modes
| Mode | Description |
|---|---|
| Split | Independent left/right throttle |
| Sync | Both throttles move together |
| Single | Left throttle controls both motors |
| Emergency | Right throttle disabled, left controls both |

---

## 5. CONTROL LIMITS AND INTERLOCKS

### 5.1 Control Travel Limits
| Control | Neutral | Max Travel | Stop Type |
|---|---|---|---|
| Aileron | 0 deg | +/-25 deg | Hard stop |
| Elevator | 0 deg | +/-25 deg | Hard stop |
| Rudder | 0 deg | +/-30 deg | Hard stop |
| Flaps | 0 deg | 0-45 deg | Mechanical detent |
| Trim | 0 deg | +/-10 deg | Limit switch |

### 5.2 Speed Limits (V-Speeds)
| Speed | Value | Restriction |
|---|---|---|
| Vne | 290 km/h | Never exceed |
| Vno | 230 km/h | Max structural cruise |
| Va | 160 km/h | Maneuvering speed |
| Vfe | 130 km/h | Max flap extended |
| Vs0 | 72-100 km/h | Stall speed (flaps) |
| Vs1 | 89-116 km/h | Stall speed (clean) |

### 5.3 Control Interlocks
| Condition | Interlock |
|---|---|
| Flaps >15 deg | Speed must be <130 km/h |
| Gear (if retractable) | Not applicable (fixed gear) |
| Throttle idle | Caution: motor stop |
| Trim limit | Automatic cutoff at end |

---

## 6. CONTROL SYSTEM COMPONENTS

### 6.1 Push-Pull Tubes
| Parameter | Value |
|---|---|
| Material | 6061-T6 aluminum |
| Diameter | 3/4" (19mm) |
| Wall thickness | 0.065" (1.65mm) |
| Length | 1500mm max |
| Ends | Rod end bearings (Heim joints) |
| Attachment | AN3 bolts, castle nuts, cotter pins |

### 6.2 Control Cables
| Parameter | Value |
|---|---|
| Type | 7x19 galvanized aircraft cable |
| Diameter | 1/16" (1.6mm) |
| Breaking strength | 480 kg (1056 lb) |
| Turnbuckle | 1/16"Nicopress |
| Cable swage | Nicopress tool |
| Pulley | 1" single, aluminum |
| Cable tension | 10-15 lb (adjustable) |

### 6.3 Control Stops
| Location | Type | Travel |
|---|---|---|
| Aileron | Hard stop at wing | +/-25 deg |
| Elevator | Hard stop at tail | +/-25 deg |
| Rudder | Hard stop at tail | +/-30 deg |
| Flap | Mechanical detent | 0/15/30/45 deg |
| Trim | Limit switch | +/-10 deg |

---

## 7. DUAL CONTROLS

### 7.1 Pilot and Copilot Stations
```
┌─────────────────────────────────────────────────────────────┐
│                    COCKPIT LAYOUT                             │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │                    INSTRUMENT PANEL                  │    │
│  │  [AS] [AL] [VS] [HC] [TC] [HD] [CO] [GPS]        │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌──────────────────────┬──────────────────────┐           │
│  │      LEFT SEAT       │      RIGHT SEAT      │           │
│  │      (PILOT)         │      (COPILOT)       │           │
│  │                      │                      │           │
│  │  [CONTROL STICK]     │  [CONTROL STICK]     │           │
│  │  [RUDDER PEDALS]     │  [RUDDER PEDALS]     │           │
│  │  [THROTTLE L]        │  [THROTTLE R]        │           │
│  │  [FLAP HANDLE]       │                      │           │
│  │  [TRIM SWITCH]       │  [TRIM SWITCH]       │           │
│  │  [MASTER SWITCH]     │                      │           │
│  │  [RADIO]             │                      │           │
│  └──────────────────────┴──────────────────────┘           │
│                                                              │
│  DUAL CONTROL CONNECTIONS:                                  │
│  - Ailerons: Connected (both sticks)                       │
│  - Elevator: Connected (both sticks)                       │
│  - Rudder: Connected (both pedals)                         │
│  - Throttle: Independent (split)                           │
│  - Flaps: Left only (pilot)                                │
│  - Trim: Both positions                                    │
│  - Brakes: Left only (pilot)                               │
└─────────────────────────────────────────────────────────────┘
```

### 7.2 Dual Control Rigging
- Both sticks connected via push-pull tubes
- Equal travel on both sides
- No binding in either position
- Both sticks move together when one is moved
- Emergency disconnect: Pull red knob to disconnect copilot controls

---

## 8. CONTROL SYSTEM INSPECTION

### 8.1 Pre-Flight Control Check
```
CONTROL CHECK PROCEDURE:

1. AILERONS:
   - Move stick full left → ailerons correct (left up, right down)
   - Move stick full right → ailerons correct (left down, right up)
   - Check for binding
   - Verify travel: +/-25 degrees

2. ELEVATOR:
   - Move stick full forward → elevator down 25 degrees
   - Move stick full aft → elevator up 25 degrees
   - Check for binding
   - Verify travel: +/-25 degrees

3. RUDDER:
   - Push left pedal → rudder left 30 degrees
   - Push right pedal → rudder right 30 degrees
   - Check for binding
   - Verify travel: +/-30 degrees

4. FLAPS:
   - Move flap handle to 0 (UP) → flaps at 0 degrees
   - Move flap handle to 15 (T/O) → flaps at 15 degrees
   - Move flap handle to 30 (APPR) → flaps at 30 degrees
   - Move flap handle to 45 (LAND) → flaps at 45 degrees
   - Verify detents at each position

5. TRIM:
   - Move trim switch UP → elevator tab moves nose up
   - Move trim switch DOWN → elevator tab moves nose down
   - Verify trim indicator matches position
   - Check for full range: +/-10 degrees

6. THROTTLE:
   - Move left throttle to IDLE → motor at minimum
   - Move left throttle to MAX → motor at maximum
   - Move right throttle to IDLE → motor at minimum
   - Move right throttle to MAX → motor at maximum
   - Verify independent operation
```

### 8.2 Maintenance Intervals
| Interval | Action |
|---|---|
| Pre-flight | Visual check, full movement check |
| Every 25 hours | Check cable tension, lubricate pulleys |
| Every 50 hours | Inspect cables for fraying, check turnbuckles |
| Every 100 hours | Full control rigging check, replace cables if worn |
| Every 200 hours | Inspect push-pull tubes, check rod end bearings |
| Every 500 hours | Complete overhaul, replace all cables and bearings |

---

## 9. CONTROL SYSTEM SPECIFICATIONS SUMMARY

| System | Type | Travel | Cables | Force |
|---|---|---|---|---|
| Aileron | Cable | +/-25 deg | 1/16" 7x19 | 5-10 lb |
| Elevator | Cable | +/-25 deg | 1/16" 7x19 | 5-10 lb |
| Rudder | Cable | +/-30 deg | 1/16" 7x19 | 8-15 lb |
| Flaps | Cable | 0-45 deg | 1/16" 7x19 | 10-15 lb |
| Trim | Electric | +/-10 deg | Wire | 0 lb (electric) |
| Throttle | Electric | 0-100% | Wire | 0 lb (electric) |
