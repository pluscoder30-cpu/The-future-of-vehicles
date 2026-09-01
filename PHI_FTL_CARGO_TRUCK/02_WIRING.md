# PHI FTL CARGO TRUCK — WIRING DIAGRAM

## Complete Electrical Wiring

---

## MAIN POWER BUS

```
FPB-100 BATTERY (100V, 250Ah)
    │
    ├──► HV MAIN CONTACTOR (500A)
    │        │
    │        ├──► WARP FIELD COIL ARRAY (8× coils)
    │        │
    │        └──► PHASE DRIVE INVERTER (400V 3-phase)
    │                 │
    │                 └──► TRACTION MOTOR (280kW)
    │
    ├──► DC-DC CONVERTER (100V → 12V, 40A)
    │        │
    │        ├──► AUXILIARY BATTERY (12V, 150Ah)
    │        │        │
    │        │        ├──► HEADLIGHTS (160W)
    │        │        ├──► TAILLIGHTS (144W)
    │        │        ├──► DASHBOARD (20W)
    │        │        ├──► HVAC (800W)
    │        │        ├──► DIMENSIONAL DISPLAY (25W)
    │        │        └──► ACCESSORIES (60W)
    │        │
    │        └──► CHARGE CONTROLLER (100V/50A)
    │                 │
    │                 └──► CCS2 CHARGE PORT
    │
    └──► BMS MODULE (25S BALANCE)
             │
             ├──► CELL MONITORING (25 cells)
             ├──► TEMPERATURE SENSORS (8×)
             ├──► CURRENT SENSOR (600A shunt)
             └──► FAULT RELAY
```

---

## WARP FIELD WIRING

```
FPB-100 RESONANCE EMITTER
    │
    ├──► WARP COIL 1 (Front-Left)    ── 432Hz
    ├──► WARP COIL 2 (Front-Right)   ── 432Hz
    ├──► WARP COIL 3 (Mid-Front-L)   ── 432Hz
    ├──► WARP COIL 4 (Mid-Front-R)   ── 432Hz
    ├──► WARP COIL 5 (Mid-Rear-L)    ── 432Hz
    ├──► WARP COIL 6 (Mid-Rear-R)    ── 432Hz
    ├──► WARP COIL 7 (Rear-Left)     ── 432Hz
    └──► WARP COIL 8 (Rear-Right)    ── 432Hz
             │
             └──► RESONANCE STABILIZER
                      │
                      ├──► DIMENSIONAL TUNER (7-band)
                      │        │
                      │        └──► DIMENSIONAL HUD DISPLAY
                      │
                      └──► FIELD EMITTER NODES (10×)
```

---

## FUSE MAP

| Fuse | Rating | Circuit |
|------|--------|---------|
| F1 | 500A | HV Main |
| F2 | 250A | Warp Coils |
| F3 | 120A | Traction Motor |
| F4 | 40A | DC-DC Converter |
| F5 | 20A | Headlights |
| F6 | 15A | Dashboard |
| F7 | 15A | HVAC |
| F8 | 10A | Dimensional Display |
| F9 | 10A | Accessories |
| F10 | 5A | CAN Bus |
