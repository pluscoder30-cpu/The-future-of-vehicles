# PHI FTL TRUCK — WIRING DIAGRAM

## Complete Electrical Wiring

---

## MAIN POWER BUS

```
FPB-80 BATTERY (80V, 200Ah)
    │
    ├──► HV MAIN CONTACTOR (400A)
    │        │
    │        ├──► WARP FIELD COIL ARRAY (6× coils)
    │        │
    │        └──► PHASE DRIVE INVERTER (380V 3-phase)
    │                 │
    │                 └──► TRACTION MOTOR (200kW)
    │
    ├──► DC-DC CONVERTER (80V → 12V, 30A)
    │        │
    │        ├──► AUXILIARY BATTERY (12V, 100Ah)
    │        │        │
    │        │        ├──► HEADLIGHTS (120W)
    │        │        ├──► TAILLIGHTS (72W)
    │        │        ├──► DASHBOARD (15W)
    │        │        ├──► HVAC (500W)
    │        │        ├──► DIMENSIONAL DISPLAY (25W)
    │        │        └──► ACCESSORIES (50W)
    │        │
    │        └──► CHARGE CONTROLLER (80V/40A)
    │                 │
    │                 └──► CCS2 CHARGE PORT
    │
    └──► BMS MODULE (20S BALANCE)
             │
             ├──► CELL MONITORING (20 cells)
             ├──► TEMPERATURE SENSORS (8×)
             ├──► CURRENT SENSOR (500A shunt)
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
    ├──► WARP COIL 5 (Rear-Left)     ── 432Hz
    └──► WARP COIL 6 (Rear-Right)    ── 432Hz
             │
             └──► RESONANCE STABILIZER
                      │
                      ├──► DIMENSIONAL TUNER (7-band)
                      │        │
                      │        └──► DIMENSIONAL HUD DISPLAY
                      │
                      └──► FIELD EMITTER NODES (8×)
                               │
                               └──► 120° ARC COVERAGE EACH
```

---

## SIGNAL WIRING

| Circuit | Gauge | Color | Notes |
|---------|-------|-------|-------|
| HV Main | 50mm² | Orange | Shielded |
| HV Coils | 25mm² | Orange/White | Per coil |
| 12V Main | 10AWG | Red | From DC-DC |
| 12V Ground | 10AWG | Black | Chassis ground |
| CAN Bus | Twisted pair | Green/White | 500kbps |
| Sensor | 22AWG | Blue | Shielded |
| Signal | 18AWG | Yellow | General |

---

## GROUNDING

```
CHASSIS GROUND BAR
    │
    ├──► FPB-80 negative terminal
    ├──► DC-DC converter negative
    ├──► All 12V component negatives
    ├──► Warp coil ground returns
    └──► Signal ground (star ground)
```

---

## FUSE MAP

| Fuse | Rating | Circuit |
|------|--------|---------|
| F1 | 400A | HV Main |
| F2 | 200A | Warp Coils |
| F3 | 100A | Traction Motor |
| F4 | 30A | DC-DC Converter |
| F5 | 15A | Headlights |
| F6 | 10A | Dashboard |
| F7 | 10A | HVAC |
| F8 | 5A | Dimensional Display |
| F9 | 5A | Accessories |
| F10 | 3A | CAN Bus |
