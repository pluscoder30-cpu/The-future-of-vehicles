# Energy Systems — Power Distribution and Warp Energy Budget

## 1. System Architecture

The energy system manages power from four FPB-100 batteries to all vehicle subsystems. The primary consumer is the warp coil array.

## 2. Power Distribution

### 2.1 Main Power Bus

```
FPB-100 Unit 1 ──► Warp Bus A ──┐
FPB-100 Unit 2 ──► Warp Bus B ──┤──► Warp Coil Array (8 coils)
FPB-100 Unit 3 ──► Warp Bus C ──┤
FPB-100 Unit 4 ──► Warp Bus D ──┘

Aux Bus ──► Navigation, Life Support, Communication
```

### 2.2 Power Allocation

| Subsystem | Peak Power | Sustained Power | Energy per LY |
|-----------|-----------|-----------------|---------------|
| Warp coil array | 200 MW | 40 MW | 100 kWh |
| Navigation system | 10 kW | 5 kW | 0.005 kWh |
| Life support | 5 kW | 2.5 kW | 0.0025 kWh |
| Communication | 2 kW | 1 kW | 0.001 kWh |
| Warp control electronics | 20 kW | 10 kW | 0.01 kWh |
| Safety systems | 5 kW | 2 kW | 0.002 kWh |
| **Total (excluding coils)** | **42 kW** | **20.5 kWh/LY** | **0.02 kWh/LY** |

### 2.3 Energy Budget per Light-Year

For a 1 LY journey at 10c:

```
Warp energy:           100 kWh
Subsystems:            0.02 kWh
Warp quench reserve:   20 kWh
Metric relaxation:     10 kWh
────────────────────────────────
Total:                130.02 kWh
Remaining (from 400 kWh): 269.98 kWh
Available light-years: 3.07 (at 130.02 kWh each)
```

### 2.4 Energy Conservation

The FPB-100 batteries store 400 kWh total. The warp process conserves energy — the energy used to create the warp is returned to the system during warp collapse. However, some energy is lost to:
- Metric radiation during warp formation: ~3%
- Warp collapse dissipation: ~5%
- Thermal losses in coils: ~2%

Total losses per light-year: ~10%. Net energy consumed per light-year:

```
E_net = 130.02 kWh × 0.10 = 13.0 kWh
```

## 3. Warp Energy Amplification

### 3.1 Resonance Amplification

The warp coils use metric resonance amplification to multiply the input energy:

```
E_warp = E_input × φⁿ
```

With 20 resonance cycles:

```
E_warp = E_input × φ²⁰ ≈ E_input × 15,127
```

This means the 400 kWh battery can provide warp energy equivalent to:

```
E_available = 400 kWh × 15,127 ≈ 6,050,800 kWh
```

### 3.2 Vacuum Polarization Harvesting

During warp, the phi-harmonic field polarizes the quantum vacuum, creating virtual particle-antiparticle pairs that store energy. This energy can be harvested:

```
E_harvested = 10% × E_warp = 605,080 kWh
```

### 3.3 Total Available Energy

```
E_total = E_amplified + E_harvested
        = 6,050,800 + 605,080
        = 6,655,880 kWh
```

## 4. Thermal Management

### 4.1 Heat Sources

| Source | Heat generated per LY |
|--------|----------------------|
| Coil resistance | 2.0 kWh |
| Warp quench | 1.0 kWh |
| Metric radiation | 0.5 kWh |
| Electronics | 0.2 kWh |
| **Total** | **3.7 kWh** |

### 4.2 Heat Dissipation

Heat is dissipated through:
- Radiative cooling (primary): 2.5 kWh per LY
- Convective cooling (secondary): 0.8 kWh per LY
- Thermal mass absorption (tertiary): 0.4 kWh per LY

### 4.3 Thermal Limits

| Component | Maximum temperature | Cooling method |
|-----------|-------------------|----------------|
| Warp coils | 120°C | Liquid nitrogen (77K) |
| Power electronics | 85°C | Air cooling |
| Battery modules | 55°C | Phase-change cooling |
| Hull structure | 60°C | Passive radiation |

## 5. Charging System

```
Input: 480V 3-phase AC, 60 Hz
Charge rate: 200 kW per unit (800 kW total)
Charge time: 30 minutes (0→100%)
Charge standard: PHI-C2 (proprietary)
```
