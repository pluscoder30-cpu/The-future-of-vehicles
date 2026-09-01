# PHI_KAYAK — Wiring Diagram

## Main System Wiring

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        PHI-KAYAK SYSTEM WIRING                           │
└─────────────────────────────────────────────────────────────────────────┘

    ┌──────────────────────────────────────────┐
    │        BATTERY PACK 24V 10Ah              │
    │        LiFePO4, sealed                   │
    │        Waterproof box (stern)            │
    │                                          │
    │  ┌─────┐                                 │
    │  │BMS  │                                 │
    │  └──┬──┘                                 │
    │     │                                    │
    │  XT60 CONNECTOR                          │
    │  ┌─────┐                                 │
    │  │+  - │                                 │
    │  └──┬──┘                                 │
    └─────┼────────────────────────────────────┘
          │
          │ 12AWG Red (+)    12AWG Black (-)
          │
    ┌─────┴────────────────────────────────────────────────────┐
    │                   MAIN POWER BUS                          │
    └──┬──────────────┬──────────────────┬────────────────────┘
       │              │                  │
       │              │                  │
  ┌────┴────┐    ┌────┴────┐        ┌────┴────┐
  │  FUSE   │    │CONTROLLER│        │ CHARGER │
  │  15A    │    │ 24V 15A  │        │ 29.2V 3A│
  │  Blade  │    │ Waterproof│        │ (XT60)  │
  └────┬────┘    └────┬────┘        └─────────┘
       │              │
       │         ┌────┴──────────────────────────────┐
       │         │                                   │
       │         │    MOTOR CONTROLLER               │
       │         │    ┌─────────────────────────┐    │
       │         │    │                         │    │
       │         │    │  POWER INPUT            │    │
       │         │    │  B+ ──────────────────► │    │
       │         │    │  B- ──────────────────► │    │
       │         │    │                         │    │
       │         │    │  MOTOR OUTPUT           │    │
       │         │    │  Phase A ─────────────► │    │
       │         │    │  Phase B ─────────────► │    │
       │         │    │  Phase C ─────────────► │    │
       │         │    │                         │    │
       │         │    │  INPUTS                 │    │
       │         │    │  Throttle ────────────► │    │
       │         │    │  Paddle Switch ────────► │    │
       │         │    │                         │    │
       │         │    │  OUTPUTS                 │    │
       │         │    │  LED Indicator ────────► │    │
       │         │    │                         │    │
       │         │    └─────────────────────────┘    │
       │         │                                   │
       │         └────┬──────┬──────┬────────────────┘
       │              │      │      │
       │              │      │      │
       │         ┌────┴──┐┌──┴──┐┌──┴────┐
       │         │MOTOR  │ │THROT│ │PADLE  │
       │         │200W   │ │TLE  │ │SWITCH │
       │         │24V    │ │      │ │       │
       │         │Water  │ │      │ │       │
       │         │Jet    │ │      │ │       │
       │         └───────┘ └─────┘ └──────┘
```

## Motor Wiring Detail

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PHI-HARMONIC WATER JET                            │
│                    200W, 24V Brushless                               │
│                                                                     │
│    ┌─────────────────────────────────────────────────────────┐     │
│    │                                                         │     │
│    │                    JET HOUSING                           │     │
│    │              ┌───────────────────┐                     │     │
│    │              │                   │                     │     │
│    │    WATER ──► │   ┌───────────┐   │ ──► WATER OUT       │     │
│    │    INTAKE    │   │           │   │     (thrust)        │     │
│    │              │   │  IMPELLER │   │                     │     │
│    │              │   │  (phi-    │   │                     │     │
│    │              │   │  harmonic │   │                     │     │
│    │              │   │  5 blade) │   │                     │     │
│    │              │   │           │   │                     │     │
│    │              │   │  ┌─────┐  │   │                     │     │
│    │              │   │  │MOTOR│  │   │                     │     │
│    │              │   │  │200W │  │   │                     │     │
│    │              │   │  │24V  │  │   │                     │     │
│    │              │   │  └─────┘  │   │                     │     │
│    │              │   │           │   │                     │     │
│    │              │   └───────────┘   │                     │     │
│    │              │                   │                     │     │
│    │              └───────────────────┘                     │     │
│    │                                                         │     │
│    │    MOTOR LEADS (3-wire, waterproof):                    │     │
│    │    ┌────┬────┬────┐                                     │     │
│    │    │ A  │ B  │ C  │                                     │     │
│    │    │Phs │Phs │Phs │                                     │     │
│    │    └──┬─┴──┬─┴──┬─┘                                     │     │
│    │       │    │    │                                        │     │
│    │       └────┴────┘                                        │     │
│    │             3-pin waterproof connector                   │     │
│    │             (to controller)                              │     │
│    │                                                         │     │
│    └─────────────────────────────────────────────────────────┘     │
│                                                                     │
│    Specifications:                                                  │
│    - Jet housing diameter: 50mm                                     │
│    - Impeller diameter: 45mm                                        │
│    - Number of blades: 5 (phi-harmonic spacing)                     │
│    - Blade material: ABS (3D printed)                               │
│    - Motor KV: 800                                                  │
│    - Thrust: 3.5 kg at full power                                   │
│    - Weight: 0.8 kg (motor + housing)                               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Control Wiring

```
┌─────────────────────────────────────────────────────────────────────┐
│                    KAYAK CONTROL INTERFACE                            │
│                                                                     │
│    ┌─────────────────────────────────────────────────────────┐     │
│    │                                                         │     │
│    │                    COCKPIT AREA                          │     │
│    │                                                         │     │
│    │    ┌─────────────────────────────────────────────┐     │     │
│    │    │                                             │     │     │
│    │    │  ┌───────────┐      ┌───────────┐          │     │     │
│    │    │  │  THROTTLE │      │ LED       │          │     │     │
│    │    │  │  (right   │      │ INDICATOR │          │     │     │
│    │    │  │   hand)   │      │           │          │     │     │
│    │    │  │           │      │  Green:   │          │     │     │
│    │    │  │  Thumb    │      │  Good     │          │     │     │
│    │    │  │  press to │      │  Yellow:  │          │     │     │
│    │    │  │  increase │      │  Medium   │          │     │     │
│    │    │  │  power    │      │  Red:     │          │     │     │
│    │    │  │           │      │  Low      │          │     │     │
│    │    │  │  ┌─────┐  │      │           │          │     │     │
│    │    │  │  │ POT │  │      └─────┬─────┘          │     │     │
│    │    │  │  └──┬──┘  │            │                │     │     │
│    │    │  │     │     │            │                │     │     │
│    │    │  └─────┼─────┘            │                │     │     │
│    │    │        │                  │                │     │     │
│    │    └────────┼──────────────────┼────────────────┘     │     │
│    │             │                  │                       │     │
│    │             ▼                  ▼                       │     │
│    │        TO CONTROLLER       TO CONTROLLER              │     │
│    │        (Throttle Input)    (LED Output)               │     │
│    │                                                         │     │
│    └─────────────────────────────────────────────────────────┘     │
│                                                                     │
│                                                                     │
│    ┌─────────────────────────────────────────────────────────┐     │
│    │                                                         │     │
│    │                    PADDLE SWITCH                         │     │
│    │                    (safety switch)                       │     │
│    │                                                         │     │
│    │    ┌─────────────────────────────────────────────┐     │     │
│    │    │                                             │     │     │
│    │    │    PADDLE HOLDER (in cockpit)                │     │     │
│    │    │    ┌─────────────────────────────────────┐  │     │     │
│    │    │    │                                     │  │     │     │
│    │    │    │  ┌───────────┐                     │  │     │     │
│    │    │    │  │  MAGNETIC │                     │  │     │     │
│    │    │    │  │  REED     │                     │  │     │     │
│    │    │    │  │  SWITCH   │                     │  │     │     │
│    │    │    │  └─────┬─────┘                     │  │     │     │
│    │    │    │        │                           │  │     │     │
│    │    │    └────────┼───────────────────────────┘  │     │     │
│    │    │             │                              │     │     │
│    │    │    Paddle inserted = Motor ENABLED          │     │     │
│    │    │    Paddle removed = Motor DISABLED          │     │     │
│    │    │                                             │     │     │
│    │    │    Safety Feature:                           │     │     │
│    │    │    If paddle is lost, motor stops            │     │     │
│    │    │    Prevents runaway kayak                     │     │     │
│    │    │                                             │     │     │
│    │    └─────────────────────────────────────────────┘     │     │
│    │                                                         │     │
│    └─────────────────────────────────────────────────────────┘     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Connector Types

| Connection | Connector | Wire Gauge | Color Code |
|------------|-----------|------------|------------|
| Battery to Controller | XT60 | 12AWG | Red (+), Black (-) |
| Motor Phase A | Waterproof bullet | 14AWG | Blue |
| Motor Phase B | Waterproof bullet | 14AWG | Green |
| Motor Phase C | Waterproof bullet | 14AWG | Yellow |
| Throttle | Waterproof JST | 22AWG | Red, Black, White |
| Paddle Switch | Waterproof JST | 22AWG | Red, Black |
| LED Indicator | Waterproof JST | 22AWG | Red, Green, Yellow |
| Charger | XT60 | 12AWG | Red (+), Black (-) |

## Waterproofing Notes

All connections must be waterproof:
- Use IP67-rated connectors
- Apply marine sealant around all through-hull fittings
- Use cable glands for all wire pass-throughs
- Seal all connectors with heat shrink + silicone
- Test for leaks before launching
