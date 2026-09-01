# PHI FTL TRUCK — CIRCUIT DESIGN

## Control Circuits

---

## FPB-80 BATTERY MANAGEMENT CIRCUIT

```
┌─────────────────────────────────────────────────────────────┐
│                    FPB-80 BMS CIRCUIT                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │ Cell 1   │───►│ ADC 1    │───►│          │              │
│  │ 3.2V     │    │ 16-bit   │    │          │              │
│  └──────────┘    └──────────┘    │          │              │
│  ┌──────────┐    ┌──────────┐    │  STM32   │    ┌──────┐ │
│  │ Cell 2   │───►│ ADC 2    │───►│  F407    │───►│ CAN  │ │
│  │ 3.2V     │    │ 16-bit   │    │          │    │ Bus  │ │
│  └──────────┘    └──────────┘    │          │    └──────┘ │
│  ┌──────────┐    ┌──────────┐    │          │              │
│  │ Cell 3   │───►│ ADC 3    │───►│          │              │
│  │ 3.2V     │    │ 16-bit   │    └──────────┘              │
│  └──────────┘    └──────────┘                               │
│       ...            ...                                    │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │ Cell 20  │───►│ ADC 20   │───►│ TEMP     │              │
│  │ 3.2V     │    │ 16-bit   │    │ SENSORS  │              │
│  └──────────┘    └──────────┘    │ (8× NTC) │              │
│                                  └──────────┘              │
│                                                             │
│  BALANCE RESISTORS: 50Ω per cell (phi-spaced: φ×50Ω)      │
│  CURRENT SENSOR: 500A Hall effect                          │
│  FAULT RELAY: Normally open, closes on fault               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## WARP FIELD CONTROL CIRCUIT

```
┌─────────────────────────────────────────────────────────────┐
│                 WARP FIELD CONTROLLER                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │ FPB-80   │───►│ H-BRIDGE │───►│ WARP     │              │
│  │ 80V DC   │    │ DRIVER   │    │ COIL 1   │              │
│  │          │    │ (IGBT)   │    │ 432Hz    │              │
│  └──────────┘    └──────────┘    └──────────┘              │
│       │               │               │                     │
│       │         ┌──────────┐          │                     │
│       │         │   DSP    │          │                     │
│       └────────►│ TMS320   │◄─────────┘                     │
│                 │          │                                │
│                 │  Phase   │    ┌──────────┐               │
│                 │ Locked   │───►│ COIL 2-6 │               │
│                 │ Loop     │    │ (phased) │               │
│                 └──────────┘    └──────────┘               │
│                      │                                     │
│                 ┌──────────┐                               │
│                 │ DIM TUNER │                               │
│                 │ 7-band   │                               │
│                 │ selector │                               │
│                 └──────────┘                               │
│                                                             │
│  PHASE LOCKED LOOP:                                        │
│  ┌──────────────────────────────────────────┐              │
│  │  Reference: 432 Hz crystal oscillator    │              │
│  │  VCO: 432-7752 Hz (7 bands)             │              │
│  │  Phase detector: XOR gate               │              │
│  │  Loop filter: 2nd order, φ-damped       │              │
│  │  Lock range: ±2%                        │              │
│  │  Capture range: ±0.5%                   │              │
│  └──────────────────────────────────────────┘              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## DIMENSIONAL NAVIGATION CIRCUIT

```
┌─────────────────────────────────────────────────────────────┐
│               DIMENSIONAL NAVIGATION SYSTEM                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │ DIM TUNER │───►│ DISPLAY  │───►│ HUD      │              │
│  │ 7-band   │    │ DRIVER   │    │ PROJECTOR│              │
│  │ selector │    │          │    │          │              │
│  └──────────┘    └──────────┘    └──────────┘              │
│       │                                       │             │
│       │          ┌──────────┐                 │             │
│       └─────────►│ GPS/IMU  │◄────────────────┘             │
│                  │ FUSION   │                               │
│                  │ (reality │                               │
│                  │  anchor) │                               │
│                  └──────────┘                               │
│                                                             │
│  DIMENSION SELECTOR:                                       │
│  ┌──────────────────────────────────────────┐              │
│  │  D0: 432 Hz  (Home)        [HOME]        │              │
│  │  D1: 699 Hz  (Phi-aligned) [φ]           │              │
│  │  D2: 1131 Hz (Golden spiral) [SPIRAL]    │              │
│  │  D3: 1830 Hz (Fractal)     [FRACTAL]     │              │
│  │  D4: 2961 Hz (Standing wave)[WAVE]       │              │
│  │  D5: 4791 Hz (Cascade)     [CASCADE]     │              │
│  │  D6: 7752 Hz (Source field) [SOURCE]      │              │
│  └──────────────────────────────────────────┘              │
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
| Gate driver resistors | 10Ω | ±5% |
