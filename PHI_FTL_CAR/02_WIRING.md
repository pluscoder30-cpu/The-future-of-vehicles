# PHI FTL CAR — WIRING DIAGRAM

## Complete Electrical Wiring

---

## MAIN POWER BUS

```
FPB-80 BATTERY (80V, 180Ah)
    │
    ├──► HV MAIN CONTACTOR (350A)
    │        │
    │        ├──► WARP FIELD COIL ARRAY (4× coils)
    │        │
    │        └──► PHASE DRIVE INVERTER (380V 3-phase)
    │                 │
    │                 └──► TRACTION MOTOR (150kW)
    │
    ├──► DC-DC CONVERTER (80V → 12V, 25A)
    │        │
    │        ├──► AUXILIARY BATTERY (12V, 60Ah)
    │        │        │
    │        │        ├──► HEADLIGHTS (100W)
    │        │        ├──► TAILLIGHTS (48W)
    │        │        ├──► DASHBOARD (20W)
    │        │        ├──► HVAC (800W)
    │        │        ├──► DIMENSIONAL DISPLAY (25W)
    │        │        ├──► AUDIO (120W)
    │        │        └──► ACCESSORIES (40W)
    │        │
    │        └──► CHARGE CONTROLLER (80V/32A)
    │                 │
    │                 └──► CCS2 CHARGE PORT
    │
    └──► BMS MODULE (20S BALANCE)
             │
             ├──► CELL MONITORING (20 cells)
             ├──► TEMPERATURE SENSORS (6×)
             ├──► CURRENT SENSOR (400A shunt)
             └──► FAULT RELAY
```

---

## WARP FIELD WIRING

```
FPB-80 RESONANCE EMITTER
    │
    ├──► WARP COIL 1 (Front-Left)    ── 432Hz
    ├──► WARP COIL 2 (Front-Right)   ── 432Hz
    ├──► WARP COIL 3 (Rear-Left)     ── 432Hz
    └──► WARP COIL 4 (Rear-Right)    ── 432Hz
             │
             └──► RESONANCE STABILIZER
                      │
                      ├──► DIMENSIONAL TUNER (7-band)
                      │        │
                      │        └──► DIMENSIONAL HUD DISPLAY
                      │
                      └──► FIELD EMITTER NODES (6×)
                               │
                               └──► 120° ARC COVERAGE EACH
```

---

## SIGNAL WIRING

| Circuit | Gauge | Color | Notes |
|---------|-------|-------|-------|
| HV Main | 35mm² | Orange | Shielded |
| HV Coils | 20mm² | Orange/White | Per coil |
| 12V Main | 12AWG | Red | From DC-DC |
| 12V Ground | 12AWG | Black | Chassis ground |
| CAN Bus | Twisted pair | Green/White | 500kbps |
| Sensor | 22AWG | Blue | Shielded |
| Signal | 18AWG | Yellow | General |

---

## FUSE MAP

| Fuse | Rating | Circuit |
|------|--------|---------|
| F1 | 350A | HV Main |
| F2 | 180A | Warp Coils |
| F3 | 80A | Traction Motor |
| F4 | 25A | DC-DC Converter |
| F5 | 15A | Headlights |
| F6 | 10A | Dashboard |
| F7 | 10A | HVAC |
| F8 | 10A | Audio |
| F9 | 5A | Dimensional Display |
| F10 | 5A | Accessories |
