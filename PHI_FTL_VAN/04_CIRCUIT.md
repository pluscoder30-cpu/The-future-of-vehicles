# PHI FTL VAN — CIRCUIT DESIGN

## Control Circuits

---

## WARP FIELD CONTROL CIRCUIT

```
┌─────────────────────────────────────────────────────────────┐
│                 WARP FIELD CONTROLLER                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │ FPB-80   │───►│ H-BRIDGE │───►│ WARP     │              │
│  │ 80V DC   │    │ DRIVER   │    │ COIL 1-5 │              │
│  │          │    │ (IGBT)   │    │ 432Hz    │              │
│  └──────────┘    └──────────┘    └──────────┘              │
│       │               │               │                     │
│       │         ┌──────────┐          │                     │
│       │         │   DSP    │          │                     │
│       └────────►│ TMS320   │◄─────────┘                     │
│                 │          │                                │
│                 │  Phase   │    ┌──────────┐               │
│                 │ Locked   │───►│ COIL 2-5 │               │
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
| Filter caps | 100μF (φ-spaced) | ±20% |
