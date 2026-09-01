# PHI FTL CARGO TRUCK — CIRCUIT DESIGN

## Control Circuits

---

## WARP FIELD CONTROL CIRCUIT

```
┌─────────────────────────────────────────────────────────────┐
│                 WARP FIELD CONTROLLER                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │ FPB-100  │───►│ H-BRIDGE │───►│ WARP     │              │
│  │ 100V DC  │    │ DRIVER   │    │ COIL 1-8 │              │
│  │          │    │ (IGBT)   │    │ 432Hz    │              │
│  └──────────┘    └──────────┘    └──────────┘              │
│       │               │               │                     │
│       │         ┌──────────┐          │                     │
│       │         │   DSP    │          │                     │
│       └────────►│ TMS320   │◄─────────┘                     │
│                 │          │                                │
│                 │  Phase   │    ┌──────────┐               │
│                 │ Locked   │───►│ COIL 2-8 │               │
│                 │ Loop     │    │ (phased) │               │
│                 └──────────┘    └──────────┘               │
│                      │                                     │
│                 ┌──────────┐                               │
│                 │ DIM TUNER │                               │
│                 │ 7-band   │                               │
│                 │ selector │                               │
│                 └──────────┘                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## COMPONENT VALUES

| Component | Value | Tolerance |
|-----------|-------|-----------|
| BMS ADC | 16-bit, 1MSPS | ±0.1% |
| Balance resistors | 50Ω (φ×50 = 80.9Ω) | ±1% |
| CAN bus resistor | 120Ω | ±1% |
| Warp coil inductance | 432μH (phi-harmonic) | ±5% |
| PLL crystal | 432 kHz (÷1000) | ±10ppm |
| Filter caps | 150μF (φ-spaced) | ±20% |
