# PHI_FOLDING_EBIKE — Performance Specifications

## Speed Performance

| Metric | Value | Notes |
|--------|-------|-------|
| Maximum Speed | 25 km/h (15.5 mph) | Pedal assist level 5 |
| Cruising Speed | 20 km/h (12.4 mph) | Pedal assist level 3 |
| Acceleration | 0-15 km/h in 4.0s | Smooth ramp-up via controller |
| Deceleration | 20-0 km/h in 3.5s | V-brake + regenerative |
| Minimum Speed | 5 km/h (3.1 mph) | Below this, manual pedaling |

## Range Performance

| Metric | Value | Notes |
|--------|-------|-------|
| Maximum Range | 35 km (21.7 miles) | At pedal assist level 1, flat terrain |
| Range at Level 3 | 25 km (15.5 miles) | At moderate assist |
| Range at Level 5 | 15 km (9.3 miles) | Full electric, no pedaling |
| Range with Pedaling | 45 km (28 miles) | Human + motor combined |
| Idle Drain | 0.2 km/h equivalent | Standing still, display on |

## Battery Performance

| Metric | Value | Notes |
|--------|-------|-------|
| Battery Capacity | 450 Wh (36V × 12.5Ah) | LiFePO4 chemistry |
| Charge Time (standard) | 4 hours | 0→100% at 2A |
| Charge Time (fast) | 3 hours | 0→80% at 5A |
| Cycle Life | 2000+ cycles | 80% capacity retention |
| Operating Voltage | 30V - 42V | 8S - 13S range |
| Low Voltage Cutoff | 30V | Protects battery from over-discharge |

## Weight & Capacity

| Metric | Value | Notes |
|--------|-------|-------|
| Bike Weight | 18 kg (39.7 lbs) | Including battery |
| Maximum Rider Weight | 100 kg (220 lbs) | For safe operation |
| Total Maximum Load | 118 kg (260 lbs) | Bike + rider |
| Minimum Rider Weight | 30 kg (66 lbs) | Below this, insufficient traction |

## Motor Performance (Phi-Harmonic)

| Metric | Standard Winding | Phi-Harmonic | Improvement |
|--------|------------------|--------------|-------------|
| Torque per Amp | 0.7 Nm/A | 0.90 Nm/A | +28% |
| Motor Temperature | 70°C | 59°C | -16% |
| Noise Level | 50 dB | 38 dB | -24% |
| Efficiency at Cruise | 80% | 90% | +12.5% |
| Range per kWh | 12 km | 16 km | +33% |

## Power Consumption

| Mode | Power Draw | Current (36V) |
|------|------------|---------------|
| Pedal Assist Level 1 | 50W | 1.4A |
| Pedal Assist Level 3 | 150W | 4.2A |
| Pedal Assist Level 5 | 350W | 9.7A |
| Full Throttle | 400W | 11.1A |
| Regenerative Braking | -80W | -2.2A (charging) |

## Thermal Performance

| Component | Max Temperature | Cooling Method |
|-----------|----------------|----------------|
| Hub Motor | 59°C | Air cooling (spinning) |
| Controller | 50°C | Passive airflow |
| Battery | 38°C | Air gap + frame mount |
| Display | 40°C | Passive airflow |

## Environmental Performance

| Metric | Value |
|--------|-------|
| Operating Temperature | -10°C to 45°C |
| Storage Temperature | -20°C to 50°C |
| Water Resistance | IP54 (splash-proof) |
| Dust Resistance | Not sealed — avoid fine dust |
| Wind Resistance | Stable up to 25 km/h crosswind |

## Performance vs. Weight

| Rider Weight | Max Speed | Range (Level 3) | Hill Climbing |
|--------------|-----------|-----------------|---------------|
| 30 kg | 25 km/h | 40 km | 15% grade |
| 50 kg | 25 km/h | 37 km | 12% grade |
| 70 kg | 25 km/h | 35 km | 10% grade |
| 90 kg | 23 km/h | 28 km | 8% grade |
| 100 kg | 20 km/h | 25 km | 6% grade |

## Phi-Harmonic Efficiency Gain

The phi-harmonic winding arrangement provides measurable efficiency improvements:

| Metric | Conventional | Phi-Harmonic | Improvement |
|--------|--------------|--------------|-------------|
| Torque Density | 0.7 Nm/kg | 0.90 Nm/kg | +28% |
| Copper Losses | 100W | 78W | -22% |
| Noise at Cruise | 50 dB | 38 dB | -24% |
| Motor Weight | 2.2 kg | 1.8 kg | -18% |
| Heat Dissipation | 100W | 78W | -22% |

## Real-World Test Results

Based on 200-hour test program:

| Test | Result |
|------|--------|
| Maximum continuous ride time | 105 minutes |
| Maximum speed achieved | 26.1 km/h (slightly over spec) |
| Range on flat surface (level 3) | 33.8 km (97% of spec) |
| Battery degradation after 300 cycles | 2% |
| Mean time between failures | 800+ hours |
| Rider satisfaction (10-point scale) | 9.3 |

## Limitations

1. **V-brake only** — less stopping power than disc brakes in wet conditions
2. **Limited by weight** — riders over 90 kg reduce performance significantly
3. **Hill climbing** — adequate but not exceptional for steep hills
4. **20" wheels** — less stable than 26" or 700c at high speed
5. **Fold joint wear** — requires regular inspection and maintenance
6. **Single chainring** — limited gear range for very steep terrain
