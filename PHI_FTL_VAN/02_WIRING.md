# PHI FTL VAN — WIRING DIAGRAM

## Complete Electrical Wiring

---

## MAIN POWER BUS

```
FPB-80 BATTERY (80V, 190Ah)
    │
    ├──► HV MAIN CONTACTOR (380A)
    │        │
    │        ├──► WARP FIELD COIL ARRAY (5× coils)
    │        │
    │        └──► PHASE DRIVE INVERTER (380V 3-phase)
    │                 │
    │                 └──► TRACTION MOTOR (180kW)
    │
    ├──► DC-DC CONVERTER (80V → 12V, 28A)
    │        │
    │        ├──► AUXILIARY BATTERY (12V, 80Ah)
    │        │        │
    │        │        ├──► HEADLIGHTS (100W)
    │        │        ├──► TAILLIGHTS (72W)
    │        │        ├──► DASHBOARD (18W)
    │        │        ├──► HVAC (600W)
    │        │        ├──► DIMENSIONAL DISPLAY (25W)
    │        │        ├──► CARGO LIGHTS (60W)
    │        │        └──► ACCESSORIES (45W)
    │        │
    │        └──► CHARGE CONTROLLER (80V/36A)
    │                 │
    │                 └──► CCS2 CHARGE PORT
    │
    └──► BMS MODULE (20S BALANCE)
             │
             ├──► CELL MONITORING (20 cells)
             ├──► TEMPERATURE SENSORS (6×)
             ├──► CURRENT SENSOR (450A shunt)
             └──► FAULT RELAY
```

---

## WARP FIELD WIRING

```
FPB-80 RESONANCE EMITTER
    │
    ├──► WARP COIL 1 (Front-Left)    ── 432Hz
    ├──► WARP COIL 2 (Front-Right)   ── 432Hz
    ├──► WARP COIL 3 (Mid-Left)      ── 432Hz
    ├──► WARP COIL 4 (Mid-Right)     ── 432Hz
    └──► WARP COIL 5 (Rear-Center)   ── 432Hz
             │
             └──► RESONANCE STABILIZER
                      │
                      ├──► DIMENSIONAL TUNER (7-band)
                      │        │
                      │        └──► DIMENSIONAL HUD DISPLAY
                      │
                      └──► FIELD EMITTER NODES (7×)
                               │
                               └──► 120° ARC COVERAGE EACH
```

---

## FUSE MAP

| Fuse | Rating | Circuit |
|------|--------|---------|
| F1 | 380A | HV Main |
| F2 | 180A | Warp Coils |
| F3 | 90A | Traction Motor |
| F4 | 28A | DC-DC Converter |
| F5 | 15A | Headlights |
| F6 | 10A | Dashboard |
| F7 | 10A | HVAC |
| F8 | 10A | Cargo Lights |
| F9 | 5A | Dimensional Display |
| F10 | 5A | Accessories |
