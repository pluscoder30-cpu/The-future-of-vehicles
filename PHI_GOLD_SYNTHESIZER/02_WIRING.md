# PHI GOLD SYNTHESIZER — WIRING DIAGRAM

## Complete Electrical Wiring

---

## MAIN POWER BUS

```
FPB-5 BATTERY (48V, 50Ah)
    │
    ├──► HV MAIN CONTACTOR (60A)
    │        │
    │        ├──► PHI-HARMONIC RESONANCE ARRAY (3× coils)
    │        │        │
    │        │        ├──► COIL 1 (432Hz — base resonance)
    │        │        ├──► COIL 2 (699Hz — φ harmonic)
    │        │        └──► COIL 3 (1131Hz — φ² harmonic)
    │        │
    │        └──► CHAMBER HEATER (200W)
    │
    ├──► DC-DC CONVERTER (48V → 12V, 10A)
    │        │
    │        ├──► CONTROLLER (ESP32-S3, 3W)
    │        │        │
    │        │        ├──► TOUCHSCREEN DISPLAY (5W)
    │        │        ├──► STATUS RING (WS2812B, 3W)
    │        │        ├──► RELAY MODULE (2W)
    │        │        ├──► CURRENT SENSOR (1W)
    │        │        ├──► VOLTAGE SENSOR (1W)
    │        │        ├──► BUZZER (1W)
    │        │        └──► STATUS LEDs (6×, 1W)
    │        │
    │        ├──► COOLING FANS (2× 120mm, 4W each)
    │        ├──► VIBRATORY FEEDER (2W)
    │        ├──► FEEDSTOCK VALVE (5W)
    │        ├──► OUTPUT SOLENOID (5W)
    │        └──► CHAMBER LIGHT (1W)
    │
    └──► BMS MODULE (16S BALANCE)
             │
             ├──► CELL MONITORING (16 cells)
             ├──► TEMPERATURE SENSORS (3× NTC)
             ├──► CURRENT SENSOR (100A shunt)
             └──► FAULT RELAY
```

---

## PHI-HARMONIC RESONANCE WIRING

```
FPB-5 RESONANCE EMITTER
    │
    ├──► PLL OSCILLATOR (432Hz base)
    │        │
    │        └──► FREQUENCY DIVIDER (CD4020)
    │                 │
    │                 ├──► 432Hz ──► COIL DRIVER 1 (IR2110 + H-Bridge)
    │                 │                    │
    │                 │                    └──► RESONANCE COIL 1 (432μH)
    │                 │
    │                 ├──► 699Hz ──► COIL DRIVER 2 (IR2110 + H-Bridge)
    │                 │                    │
    │                 │                    └──► RESONANCE COIL 2 (699μH)
    │                 │
    │                 └──► 1131Hz ► COIL DRIVER 3 (IR2110 + H-Bridge)
    │                                    │
    │                                    └──► RESONANCE COIL 3 (1131μH)
    │
    └──► PHASE-LOCKED LOOP (CD4046)
             │
             └──► FEEDBACK FROM CHAMBER SENSORS
                      │
                      └──► AUTO-TUNE TO RESONANT PEAK
```

---

## FEEDSTOCK FEED WIRING

```
CONTROLLER (ESP32-S3)
    │
    ├──► RELAY 1 ──► VIBRATORY FEEDER (12V, 50Hz)
    │                    │
    │                    └──► HOPPER VIBRATION
    │
    ├──► RELAY 2 ──► FEEDSTOCK VALVE (12V solenoid)
    │                    │
    │                    └──► CONTROLS FLOW INTO CHAMBER
    │
    └──► RELAY 3 ──► MAGNETIC STIRRER (12V)
                         │
                         └──► MIXES FEEDSTOCK IN HOPPER
```

---

## GOLD OUTPUT WIRING

```
CONTROLLER (ESP32-S3)
    │
    ├──► RELAY 4 ──► OUTPUT SOLENOID (12V)
    │                    │
    │                    └──► OPENS OUTPUT VALVE
    │
    └──► SENSOR ──► COLLECTION TRAY (weight)
                         │
                         └──► DIGITAL SCALE INTERFACE
```

---

## SIGNAL WIRING

| Circuit | Gauge | Color | Notes |
|---------|-------|-------|-------|
| HV Main | 12mm² | Orange | Shielded |
| HV Coils | 8mm² | Orange/White | Per coil |
| 12V Main | 14AWG | Red | From DC-DC |
| 12V Ground | 14AWG | Black | Chassis ground |
| Signal | 22AWG | Blue | Sensor lines |
| I2C | 24AWG | Green/White | Display, DAC |
| SPI | 22AWG | Yellow/White | ADC, sensors |
| RS-485 | Twisted pair | Purple/Grey | BMS comms |

---

## FUSE MAP

| Fuse | Rating | Circuit |
|------|--------|---------|
| F1 | 60A | HV Main |
| F2 | 40A | Resonance Coils |
| F3 | 20A | Chamber Heater |
| F4 | 10A | DC-DC Converter |
| F5 | 5A | Cooling Fans |
| F6 | 3A | Controller + Display |
| F7 | 3A | Feedstock System |
| F8 | 2A | Sensors & LEDs |

---

## GROUNDING PLAN

```
CHASSIS GROUNDING:
═══════════════════════════════════════════════════════════════

  All metal components grounded to chassis via dedicated
  ground bus bar (6mm² tinned copper braid).

  ┌──────────────────────────────────────────────────┐
  │                                                  │
  │   FPB-5 NEGATIVE ──► GROUND BUS BAR            │
  │                          │                       │
  │   ├──► CHAMBER BODY      │                       │
  │   ├──► CHASSIS           │                       │
  │   ├──► COIL FRAMES       │                       │
  │   ├──► SHIELDING         │                       │
  │   └──► EXTERNAL GROUND   │                       │
  │        (3-prong plug)    │                       │
  │                                                  │
  │   Ground resistance: <0.1Ω                      │
  │                                                  │
  └──────────────────────────────────────────────────┘
```
