# PHI WATER DRONE — MECHANICAL DESIGN

## Frame Design

---

## FRAME OVERVIEW

```
FRAME TOP VIEW:
═══════════════════════════════════════════════════════════════

         450mm
  ←───────────────────────→
  ┌────────────────────────┐
  │    ╔══╗          ╔══╗  │
  │    ║M1║          ║M2║  │
  │    ╚══╝          ╚══╝  │
  │   ┌────────────────┐   │
  │   │    CENTER      │   │  278mm (450/phi)
  │   │    BODY        │   │
  │   │  ┌────┐┌────┐  │   │
  │   │  │FILT││TANK│  │   │
  │   │  └────┘└────┘  │   │
  │   └────────────────┘   │
  │    ╔══╗          ╔══╗  │
  │    ║M3║          ║M4║  │
  │    ╚══╝          ╚══╝  │
  └────────────────────────┘

  Arm: 165mm, Body: 180x180x55mm
```

---

## FILTRATION SYSTEM

```
3-STAGE FILTRATION:
═══════════════════════════════════════════════════════════════

  ┌────────────────────────────────────┐
  │  STAGE 1: MESH FILTER             │
  │  Removes: debris, leaves, bugs    │
  │  Mesh size: 100 microns           │
  │                                    │
  │  STAGE 2: CARBON FILTER           │
  │  Removes: chemicals, odors        │
  │  Capacity: 100 liters             │
  │                                    │
  │  STAGE 3: UV STERILIZATION        │
  │  Kills: bacteria, algae           │
  │  Power: 3W UV LED                 │
  │  Exposure: 30 seconds             │
  │                                    │
  │  Processing rate: 1 liter/min     │
  │  Tank capacity: 500ml             │
  └────────────────────────────────────┘
```

---

## WATER SENSORS

```
WATER QUALITY SENSORS:
═══════════════════════════════════════════════════════════════

  ┌────────────────────────────────────┐
  │  pH SENSOR                         │
  │  Range: 0-14 pH                   │
  │  Accuracy: +/- 0.1 pH            │
  │  Optimal: 6.5-8.5 (natural water) │
  │                                    │
  │  TURBIDITY SENSOR                  │
  │  Range: 0-4000 NTU               │
  │  Accuracy: +/- 5%                 │
  │  Clean water: < 10 NTU           │
  │                                    │
  │  TEMPERATURE SENSOR                │
  │  Range: -55 to +125°C            │
  │  Accuracy: +/- 0.5°C             │
  └────────────────────────────────────┘
```
