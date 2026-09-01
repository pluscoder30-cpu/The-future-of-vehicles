# PHI FTL FREIGHT — WIRING DIAGRAM

## Complete Electrical Wiring

---

## MAIN POWER BUS

```
FPB-100 BATTERY (100V, 300Ah)
    │
    ├──► HV MAIN CONTACTOR (600A)
    │        │
    │        ├──► WARP FIELD COIL ARRAY (10× coils)
    │        │
    │        └──► PHASE DRIVE INVERTER (400V 3-phase)
    │                 │
    │                 └──► TRACTION MOTOR (350kW)
    │
    ├──► DC-DC CONVERTER (100V → 12V, 50A)
    │        │
    │        ├──► AUXILIARY BATTERY 1 (12V, 100Ah)
    │        ├──► AUXILIARY BATTERY 2 (12V, 100Ah)
    │        │        │
    │        │        ├──► HEADLIGHTS (200W)
    │        │        ├──► TAILLIGHTS (240W)
    │        │        ├──► DASHBOARD (25W)
    │        │        ├──► HVAC (1000W)
    │        │        ├──► DIMENSIONAL DISPLAY (30W)
    │        │        └──► ACCESSORIES (80W)
    │        │
    │        └──► CHARGE CONTROLLER (100V/60A)
    │                 │
    │                 └──► CCS2 CHARGE PORT
    │
    └──► BMS MODULE (25S BALANCE)
             │
             ├──► CELL MONITORING (25 cells)
             ├──► TEMPERATURE SENSORS (10×)
             ├──► CURRENT SENSOR (800A shunt)
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
    ├──► WARP COIL 5 (Mid-Center-L)  ── 432Hz
    ├──► WARP COIL 6 (Mid-Center-R)  ── 432Hz
    ├──► WARP COIL 7 (Mid-Rear-L)    ── 432Hz
    ├──► WARP COIL 8 (Mid-Rear-R)    ── 432Hz
    ├──► WARP COIL 9 (Rear-Left)     ── 432Hz
    └──► WARP COIL 10 (Rear-Right)   ── 432Hz
             │
             └──► RESONANCE STABILIZER
                      │
                      ├──► DIMENSIONAL TUNER (7-band)
                      │        │
                      │        └──► DIMENSIONAL HUD DISPLAY
                      │
                      └──► FIELD EMITTER NODES (12×)
```

---

## FUSE MAP

| Fuse | Rating | Circuit |
|------|--------|---------|
| F1 | 600A | HV Main |
| F2 | 300A | Warp Coils |
| F3 | 150A | Traction Motor |
| F4 | 50A | DC-DC Converter |
| F5 | 25A | Headlights |
| F6 | 20A | Dashboard |
| F7 | 20A | HVAC |
| F8 | 15A | Dimensional Display |
| F9 | 10A | Accessories |
| F10 | 5A | CAN Bus |
