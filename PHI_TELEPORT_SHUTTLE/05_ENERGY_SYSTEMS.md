# Energy Systems — Power Distribution and Fold Energy Budget

## 1. System Architecture

The energy system manages power from four FPB-100 batteries to all vehicle subsystems. The primary consumer is the fold coil array, but navigation, life support, and communication also draw power.

## 2. Power Distribution

### 2.1 Main Power Bus

```
FPB-100 Unit 1 ──► Fold Bus A ──┐
FPB-100 Unit 2 ──► Fold Bus B ──┤──► Coil Array (12 coils)
FPB-100 Unit 3 ──► Fold Bus C ──┤
FPB-100 Unit 4 ──► Fold Bus D ──┘

Aux Bus ──► Navigation, Life Support, Communication
```

### 2.2 Power Allocation

| Subsystem | Peak Power | Sustained Power | Energy per Fold |
|-----------|-----------|-----------------|-----------------|
| Fold coil array | 200 MW | 40 MW | 86.7 kWh |
| Navigation system | 5 kW | 2 kW | 0.002 kWh |
| Life support | 3 kW | 1.5 kW | 0.001 kWh |
| Communication | 1 kW | 0.5 kW | 0.0005 kWh |
| Fold control electronics | 10 kW | 5 kW | 0.004 kWh |
| Safety systems | 2 kW | 1 kW | 0.0008 kWh |
| **Total (excluding coils)** | **21 kW** | **10 kW** | **0.008 kWh** |

### 2.3 Energy Budget per Fold

For a typical 10 km fold:

```
Fold energy:           86.7 kWh
Subsystems:            0.008 kWh
Fold quench reserve:   15.0 kWh
Metric relaxation:      5.0 kWh
────────────────────────────────
Total:                106.7 kWh
Remaining:            293.3 kWh
Available folds:        3.75 (at 106.7 kWh each)
```

### 2.4 Energy Conservation

The FPB-100 batteries store 400 kWh total. The fold process conserves energy — the energy used to create the fold is returned to the system during fold collapse. However, some energy is lost to:

- Metric radiation during fold formation: ~5%
- Fold collapse dissipation: ~8%
- Thermal losses in coils: ~3%

Total losses per fold: ~16%. Net energy consumed per fold:

```
E_net = 106.7 kWh × 0.16 = 17.1 kWh
```

## 3. Fold Energy Amplification

### 3.1 Resonance Amplification

The fold coils use **metric resonance amplification** to multiply the input energy. Each resonance cycle amplifies the fold field by a factor of φ:

```
E_fold = E_input × φⁿ
```

where n is the number of resonance cycles. With 10 cycles:

```
E_fold = E_input × φ¹⁰ ≈ E_input × 122.99
```

This means the 400 kWh battery can provide fold energy equivalent to:

```
E_available = 400 kWh × 122.99 ≈ 49,196 kWh
```

### 3.2 Amplification Limits

The amplification is limited by:
- Coil heating (maximum 10 cycles before thermal limit)
- Phase coherence (more than 15 cycles causes phase drift)
- Fold stability (more than 20 cycles risks fold collapse)

Practical limit: 10-15 resonance cycles.

### 3.3 Amplification Efficiency

The amplification efficiency is:

```
η_amp = E_fold / E_input = φⁿ × η_coil
```

where η_coil ≈ 0.97 (coil efficiency). For n=10:

```
η_amp = 122.99 × 0.97 ≈ 119.3
```

This means 1 kWh of battery energy produces 119.3 kWh of fold energy.

## 4. Thermal Management

### 4.1 Heat Sources

| Source | Heat generated per fold |
|--------|------------------------|
| Coil resistance | 2.6 kWh |
| Fold quench | 1.5 kWh |
| Metric radiation | 0.8 kWh |
| Electronics | 0.3 kWh |
| **Total** | **5.2 kWh** |

### 4.2 Heat Dissipation

Heat is dissipated through:
- Radiative cooling (primary): 3.5 kWh per fold
- Convective cooling (secondary): 1.2 kWh per fold
- Thermal mass absorption (tertiary): 0.5 kWh per fold

### 4.3 Thermal Limits

| Component | Maximum temperature | Cooling method |
|-----------|-------------------|----------------|
| Fold coils | 120°C | Liquid nitrogen (77K) |
| Power electronics | 85°C | Air cooling |
| Battery modules | 55°C | Phase-change cooling |
| Hull structure | 60°C | Passive radiation |

## 5. Charging System

### 5.1 Charge Specification

```
Input: 480V 3-phase AC, 60 Hz
Charge rate: 200 kW per unit (800 kW total)
Charge time: 30 minutes (0→100%)
Charge standard: PHI-C2 (proprietary)
Charge connector: 6-pin, keyed, interlocked
```

### 5.2 Charge Sequence

```
Phase 1: Pre-charge check (2 min)
  - Verify all four units are at same state of charge
  - Check plasma density in each unit
  - Verify phi-harmonic confinement field

Phase 2: Bulk charge (25 min)
  - All four units charge in parallel
  - Constant current, increasing voltage
  - Plasma density increases proportionally

Phase 3: Top-off (3 min)
  - Constant voltage, decreasing current
  - Plasma reaches full density
  - Confinement field reaches full strength

Phase 4: Verification (1 min)
  - Full capacity test (brief pulse discharge)
  - Verify all units within 2% of each other
  - Ready for fold operations
```

### 5.3 Emergency Charge

In emergencies, the vehicle can charge from:
- Standard wall outlet (120V, 15A): 12 hours
- Standard wall outlet (240V, 30A): 2 hours
- Generator (10 kW): 40 minutes
- Solar array (1 kW): 16 hours
