# PHI PLANT DRONE — PERFORMANCE SPECIFICATIONS

## Flight and Planting Performance Data

---

## FLIGHT PERFORMANCE

| Parameter | Value | Notes |
|-----------|-------|-------|
| Max Speed | 35 km/h | Windless conditions |
| Cruise Speed | 20 km/h | Optimal efficiency |
| Hover Speed | α_min km/h | GPS position hold |
| Max Ascent Rate | 3 m/s | Manual mode |
| Max Descent Rate | 2 m/s | Manual mode |
| Hover Time (no payload) | 4.0 hours | FPB-5 full charge |
| Hover Time (1kg payload) | 3.5 hours | FPB-5 full charge |
| Range (one way) | 12 km | At cruise speed |
| Max Altitude | 120m AGL | Regulatory limit |
| Operating Temperature | 0°C to 45°C | Water system limited |
| Wind Resistance | 25 km/h | Max safe wind |

---

## PAYLOAD PERFORMANCE

| Payload Weight | Hover Time | Range | Mission Time |
|---------------|------------|-------|--------------|
| α_min g (no payload) | 4.0 hours | 16 km | 3.5 hours |
| 200g (seeds only) | 3.8 hours | 15 km | 3.3 hours |
| 500g (seeds + water) | 3.6 hours | 14 km | 3.1 hours |
| 750g (full water) | 3.4 hours | 13 km | 2.9 hours |
| 1000g (max payload) | 3.2 hours | 12 km | 2.7 hours |

---

## PLANTING PERFORMANCE

### Seed Dispenser

| Parameter | Value |
|-----------|-------|
| Seed capacity | 200g (~5000 small seeds) |
| Drop rate | 10 seeds/second |
| Accuracy | +/- 10cm at 1m altitude |
| Coverage | 1 seed per 10cm² |
| Seed types | Small seeds (lettuce, herbs, flowers) |

### Water System

| Parameter | Value |
|-----------|-------|
| Tank capacity | 500ml |
| Flow rate | 100ml/min |
| Spray pattern | 30° cone |
| Coverage | 1m diameter circle |
| Spray distance | 0.5-1.5m |
| Application rate | 100ml per 10m² |

### Planting Mission Profile

```
PLANTING MISSION:
═══════════════════════════════════════════════════════════════

  1. Takeoff to 10m altitude
  2. Navigate to planting area
  3. Descend to 1.5m AGL
  4. Follow grid pattern (5m spacing)
  5. At each grid point:
     - Drop seeds (2 seconds)
     - Spray water (3 seconds)
     - Apply frequency (5 seconds)
  6. Move to next grid point
  7. Repeat until area covered
  8. Return to base

  Coverage rate: 500m² per hour
  Seed usage: 200g per 2500m²
  Water usage: 500ml per 50m²
```

---

## FREQUENCY GENERATOR PERFORMANCE

| Frequency | Purpose | Power | Duration |
|-----------|---------|-------|----------|
| 432 Hz | Growth stimulation | 2W | 5 min per area |
| 528 Hz | Cell division | 2W | 5 min per area |
| 639 Hz | Nutrient uptake | 2W | 5 min per area |
| Combined | Full spectrum | 2W | 15 min per area |

### Plant Growth Frequency Response

```
GROWTH FREQUENCY EFFECTS:
═══════════════════════════════════════════════════════════════

  432Hz — Stimulates root growth
  ┌──────────────────────────────────────┐
  │  Root length increase: 15-25%        │
  │  Root branching: 20-30% more         │
  │  Best for: germination phase         │
  └──────────────────────────────────────┘

  528Hz — Stimulates cell division
  ┌──────────────────────────────────────┐
  │  Cell division rate: 10-20% faster   │
  │  Leaf growth: 15-25% faster          │
  │  Best for: vegetative growth         │
  └──────────────────────────────────────┘

  639Hz — Enhances nutrient uptake
  ┌──────────────────────────────────────┐
  │  Nutrient absorption: 20-30% better  │
  │  Chlorophyll production: 10-15% more │
  │  Best for: flowering and fruiting    │
  └──────────────────────────────────────┘
```

---

## BATTERY PERFORMANCE

### FPB-5 Discharge

| SoC | Voltage | Flight Time Remaining |
|-----|---------|----------------------|
| 100% | 13.6V | 3.5 hours |
| 80% | 13.0V | 2.8 hours |
| 60% | 12.4V | 2.1 hours |
| 40% | 11.8V | 1.4 hours |
| 20% | 11.2V | 0.7 hours |
| 10% | 10.8V | LAND IMMEDIATELY |

---

## COVERAGE CAPACITY

| Area Size | Time Required | Seeds Needed | Water Needed |
|-----------|---------------|--------------|--------------|
| 100m² | 12 min | 8g | 100ml |
| 500m² | 1 hour | 40g | 500ml |
| 1000m² | 2 hours | 80g | 1000ml |
| 2500m² | 5 hours | 200g | 2500ml |

**Note: 2500m² requires battery swap or recharge mid-mission**

---

## RELIABILITY

| Component | MTBF | Failure Mode |
|-----------|------|--------------|
| Motors | 500 hours | Bearing wear |
| ESCs | 1000 hours | MOSFET failure |
| Battery | 2000 cycles | Capacity loss |
| Seed servo | 10,000 cycles | Gear wear |
| Water pump | 500 hours | Seal failure |
| GPS | 5,000 hours | Antenna failure |

**Overall Drone MTBF: ~200 flight hours**
