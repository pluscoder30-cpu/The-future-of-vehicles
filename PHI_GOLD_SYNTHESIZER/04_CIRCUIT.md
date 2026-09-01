# PHI GOLD SYNTHESIZER — CIRCUIT DESIGN

## Control Circuits

---

## FPB-5 BATTERY MANAGEMENT CIRCUIT

```
┌─────────────────────────────────────────────────────────────┐
│                    FPB-5 BMS CIRCUIT                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │ Cell 1   │───►│ ADC 1    │───►│          │              │
│  │ 3.0V     │    │ 12-bit   │    │          │              │
│  └──────────┘    └──────────┘    │          │              │
│  ┌──────────┐    ┌──────────┐    │  ESP32   │    ┌──────┐ │
│  │ Cell 2   │───►│ ADC 2    │───►│  S3      │───►│ I2C  │ │
│  │ 3.0V     │    │ 12-bit   │    │          │    │ Bus  │ │
│  └──────────┘    └──────────┘    │          │    └──────┘ │
│  ┌──────────┐    ┌──────────┐    │          │              │
│  │ Cell 3   │───►│ ADC 3    │───►│          │              │
│  │ 3.0V     │    │ 12-bit   │    └──────────┘              │
│  └──────────┘    └──────────┘                               │
│       ...            ...                                    │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │ Cell 16  │───►│ ADC 16   │───►│ TEMP     │              │
│  │ 3.0V     │    │ 12-bit   │    │ SENSORS  │              │
│  └──────────┘    └──────────┘    │ (3× NTC) │              │
│                                  └──────────┘              │
│                                                             │
│  BALANCE RESISTORS: 100Ω per cell (phi-spaced: φ×100Ω)    │
│  CURRENT SENSOR: 100A Hall effect (ACS758)                 │
│  FAULT RELAY: Normally open, closes on fault               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## PHI-HARMONIC RESONANCE CIRCUIT

```
┌─────────────────────────────────────────────────────────────┐
│                 RESONANCE FIELD CONTROLLER                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │ FPB-5    │───►│ H-BRIDGE │───►│ COIL 1   │              │
│  │ 48V DC   │    │ DRIVER   │    │ 432μH    │              │
│  │          │    │ (IR2110) │    │ 432Hz    │              │
│  └──────────┘    └──────────┘    └──────────┘              │
│       │               │               │                     │
│       │         ┌──────────┐          │                     │
│       │         │   PLL    │          │                     │
│       └────────►│ CD4046   │◄─────────┘                     │
│                 │          │                                │
│                 │  Phase   │    ┌──────────┐               │
│                 │ Locked   │───►│ COIL 2-3 │               │
│                 │ Loop     │    │ (phased) │               │
│                 └──────────┘    └──────────┘               │
│                      │                                     │
│                 ┌──────────┐                               │
│                 │ FREQ DIV │                               │
│                 │ CD4020   │                               │
│                 │ ÷1, ÷φ   │                               │
│                 └──────────┘                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## COIL DRIVER CIRCUIT (per coil)

```
┌─────────────────────────────────────────────────────────────┐
│                    H-BRIDGE DRIVER                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│     48V Rail                                                │
│      │                                                      │
│      ├──► IRFP260N (Q1) ──┬──► RESONANCE COIL              │
│      │                     │                                │
│      ├──► IRFP260N (Q2) ──┘                                │
│      │                                                      │
│      │    IR2110 Gate Driver                                │
│      │    ┌──────────────┐                                  │
│      │    │   IR2110     │                                  │
│      │    │  ┌────────┐  │                                  │
│      ├───►│  │ HO  LO │  │◄── PWM from ESP32               │
│      │    │  └────────┘  │                                  │
│      │    └──────────────┘                                  │
│      │                                                      │
│      └──► CURRENT SENSE (0.01Ω) ──► ADC                    │
│                                                             │
│  GATE RESISTORS: 10Ω (phi-spaced: φ×10 = 16.2Ω)           │
│  BOOTSTRAP CAP: 1μF ceramic                                │
│  DEAD TIME: 500ns (prevents shoot-through)                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## TEMPERATURE MONITORING CIRCUIT

```
┌─────────────────────────────────────────────────────────────┐
│                  TEMPERATURE SENSORS                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CHAMBER (K-type thermocouple):                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │ K-Type   │───►│ MAX6675  │───►│ SPI      │              │
│  │ TC       │    │ Converter│    │ ESP32    │              │
│  │ 0-1200°C │    │ 12-bit   │    │          │              │
│  └──────────┘    └──────────┘    └──────────┘              │
│                                                             │
│  COIL TEMPERATURE (NTC 10kΩ):                               │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │ NTC 10k  │───►│ Voltage  │───►│ ADC      │              │
│  │ -40-125°C│    │ Divider  │    │ ESP32    │              │
│  └──────────┘    └──────────┘    └──────────┘              │
│                                                             │
│  AMBIENT (NTC 10kΩ):                                        │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │ NTC 10k  │───►│ Voltage  │───►│ ADC      │              │
│  │ -40-125°C│    │ Divider  │    │ ESP32    │              │
│  └──────────┘    └──────────┘    └──────────┘              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## COMPONENT VALUES

| Component | Value | Tolerance |
|-----------|-------|-----------|
| BMS ADC | 12-bit, 100kSPS | ±0.5% |
| Balance resistors | 100Ω (φ×100 = 161.8Ω) | ±1% |
| PLL crystal | 432 kHz (÷1000) | ±10ppm |
| Coil 1 inductance | 432μH (phi-harmonic) | ±5% |
| Coil 2 inductance | 699μH (φ×432) | ±5% |
| Coil 3 inductance | 1131μH (φ²×432) | ±5% |
| Gate resistors | 10Ω (phi-spaced) | ±5% |
| Bootstrap caps | 1μF ceramic | ±10% |
| Filter caps | 470μF/63V electrolytic | ±20% |
| Decoupling caps | 100nF ceramic | ±10% |
| Current sense | 0.01Ω, 5W | ±1% |
| Voltage divider | 10kΩ/2.2kΩ | ±1% |

---

## PCB LAYOUT NOTES

| Layer | Use |
|-------|-----|
| Top | Signal traces, component placement |
| Inner 1 | Ground plane (solid) |
| Inner 2 | Power plane (48V, 12V) |
| Bottom | High-current traces, thermal relief |

| Parameter | Value |
|-----------|-------|
| PCB Size | 200mm × 150mm, 4-layer |
| Copper Weight | 2oz (inner), 3oz (outer) |
| Min Trace Width | 0.2mm (signal), 2mm (power) |
| Via Size | 0.3mm drill, 0.6mm pad |
| Board Material | FR4, 1.6mm |
