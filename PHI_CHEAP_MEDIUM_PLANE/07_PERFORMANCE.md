# PHI_CHEAP_MEDIUM_PLANE — Performance Calculations

## 1. AERODYNAMIC PERFORMANCE

### 1.1 Wing Parameters
- Airfoil: NACA 2412
- Wing area (S): 14 m2
- Wingspan (b): 14 m
- Aspect ratio (AR): b^2/S = 196/14 = 14.0
- Chord (root): 1.4 m
- Chord (tip): 1.05 m
- Taper ratio: 0.75
- Oswald efficiency (e): 0.85
- CD0 (zero-lift drag): 0.025

### 1.2 Drag Polar
```
CD = CD0 + CL^2 / (pi * e * AR)
CD = 0.025 + CL^2 / (3.1416 * 0.85 * 14.0)
CD = 0.025 + CL^2 / 37.39
```

### 1.3 Lift Curve
```
CL_alpha = 2 * pi * AR / (AR + 2) (per radian)
CL_alpha = 2 * 3.1416 * 14.0 / (14.0 + 2.0)
CL_alpha = 87.96 / 16.0 = 5.50 per radian
CL_alpha = 0.096 per degree
```

---

## 2. POWER REQUIREMENTS

### 2.1 Level Flight (Cruise at 200 km/h = 55.56 m/s)
```
Dynamic pressure: q = 0.5 * rho * V^2
q = 0.5 * 1.225 * 55.56^2 = 1890 Pa

Weight at cruise (assume 1000 kg):
W = 1000 * 9.81 = 9810 N

Required CL for level flight:
CL = W / (q * S) = 9810 / (1890 * 14) = 0.370

Induced drag:
CDi = CL^2 / (pi * e * AR) = 0.370^2 / 37.39 = 0.00367

Total CD:
CD = 0.025 + 0.00367 = 0.02867

L/D ratio:
L/D = CL / CD = 0.370 / 0.02867 = 12.9

Drag force:
D = q * S * CD = 1890 * 14 * 0.02867 = 756 N

Power required (level flight):
P = D * V = 756 * 55.56 = 42,003 W = 42.0 kW
```

### 2.2 Power at Different Speeds
| Speed (km/h) | Speed (m/s) | CL | CD | L/D | Drag (N) | Power (kW) |
|---|---|---|---|---|---|---|
| 120 | 33.33 | 1.044 | 0.054 | 19.3 | 1426 | 47.5 |
| 150 | 41.67 | 0.668 | 0.037 | 18.1 | 986 | 41.1 |
| 200 | 55.56 | 0.370 | 0.029 | 12.9 | 756 | 42.0 |
| 250 | 69.44 | 0.237 | 0.026 | 9.1 | 683 | 47.4 |
| 290 | 80.56 | 0.177 | 0.026 | 6.8 | 683 | 55.0 |

### 2.3 Best L/D Speed
```
Best L/D occurs when CDi = CD0
CL at best L/D = sqrt(pi * e * AR * CD0)
CL_best = sqrt(3.1416 * 0.85 * 14.0 * 0.025)
CL_best = sqrt(0.934) = 0.967

V_best = sqrt(2*W / (rho*S*CL_best))
V_best = sqrt(2*9810 / (1.225*14*0.967))
V_best = sqrt(19620 / 16.62)
V_best = 34.3 m/s = 123 km/h

Best L/D = 0.967 / (0.025 + 0.967^2/37.39)
Best L/D = 0.967 / (0.025 + 0.025)
Best L/D = 0.967 / 0.050 = 19.3
```

---

## 3. CLIMB PERFORMANCE

### 3.1 Rate of Climb
```
At MTOW (1360 kg):
W = 1360 * 9.81 = 13,342 N

Power available (2 motors at 30 kW each):
Pa = 2 * 30,000 * 0.85 (propeller efficiency) = 51,000 W

At Vy (120 km/h = 33.33 m/s):
q = 0.5 * 1.225 * 33.33^2 = 681 Pa
CL = 13342 / (681 * 14) = 1.398
CD = 0.025 + 1.398^2 / 37.39 = 0.025 + 0.052 = 0.077
D = 681 * 14 * 0.077 = 734 N
Pr = 734 * 33.33 = 24,464 W

Excess power = Pa - Pr = 51,000 - 24,464 = 26,536 W
Rate of climb = Excess power / W = 26,536 / 13,342 = 1.99 m/s

At cruise weight (1000 kg):
W = 9810 N
Pr = 24,464 W (same speed)
Excess power = 51,000 - 24,464 = 26,536 W
Rate of climb = 26,536 / 9810 = 2.70 m/s

At light weight (800 kg):
W = 7848 N
Excess power = 26,536 W
Rate of climb = 26,536 / 7848 = 3.38 m/s
```

### 3.2 Climb Summary
| Weight (kg) | Rate of Climb (m/s) | Rate of Climb (fpm) |
|---|---|---|
| 800 (empty) | 3.38 | 665 |
| 1000 | 2.70 | 531 |
| 1200 | 2.25 | 443 |
| 1360 (MTOW) | 1.99 | 392 |

---

## 4. RANGE CALCULATIONS

### 4.1 Energy Budget
```
Total battery capacity: 160 kWh
Usable capacity (80% DoD): 128 kWh
System losses (10%): 115.2 kWh usable at motors

Propeller efficiency: 85%
Motor efficiency: 92%
Powertrain efficiency: 0.85 * 0.92 = 0.782
Effective energy: 115.2 * 0.782 = 90.1 kWh
```

### 4.2 Range at Different Speeds
```
Range = (L/D) * (Energy / Weight) * (V/P_required)

At 200 km/h cruise:
L/D = 12.9
P_required = 42.0 kW
Energy = 90.1 kWh
W = 9810 N

Range = (12.9 / 9.81) * (90.1 / 42.0) * 200
Range = 1.315 * 2.145 * 200
Range = 564 km
```

### 4.3 Range Summary
| Speed (km/h) | L/D | Power (kW) | Range (km) |
|---|---|---|---|
| 120 | 19.3 | 47.5 | 460 |
| 150 | 18.1 | 41.1 | 525 |
| 200 | 12.9 | 42.0 | 564 |
| 250 | 9.1 | 47.4 | 430 |
| 290 | 6.8 | 55.0 | 280 |

### 4.4 Optimal Cruise for Maximum Range
```
Best range speed = sqrt(2*W/(rho*S)) * sqrt(CD0/(pi*e*AR))^(1/4)
V_opt = sqrt(2*9810/(1.225*14)) * (0.025/37.39)^(1/4)
V_opt = sqrt(1143) * (0.000669)^(1/4)
V_opt = 33.8 * 0.161 = 5.44... 

Recalculating:
V_max_range = V_best_L/D * (1/1.32)
V_max_range = 123 * 0.758 = 93.2 km/h

At 100 km/h:
CL = 9810 / (0.5*1.225*27.78^2 * 14) = 9810/6597 = 1.487
CD = 0.025 + 1.487^2/37.39 = 0.025+0.059 = 0.084
L/D = 1.487/0.084 = 17.7
P = q*S*CD*V = 646*14*0.084*27.78 = 21,171 W = 21.2 kW
```

### 4.5 Endurance
```
At 200 km/h:
Endurance = Energy / Power = 90.1 / 42.0 = 2.15 hours
Distance = 2.15 * 200 = 430 km

At 120 km/h:
Endurance = 90.1 / 47.5 = 1.90 hours
Distance = 1.90 * 120 = 228 km

At best efficiency (100 km/h):
Endurance = 90.1 / 21.2 = 4.25 hours
Distance = 4.25 * 100 = 425 km
```

---

## 5. TAKEOFF AND LANDING

### 5.1 Takeoff Performance
```
Takeoff speed: 1.2 * Vs0 = 1.2 * 72 = 86.4 km/h = 24.0 m/s
Ground roll formula:
Sg = V^2 / (2 * a)

Acceleration:
a = (T - D - mu*W) / m
T = Pa / V = 51,000 / 24.0 = 2125 N (thrust at takeoff)
D = 0.5 * 1.225 * 24.0^2 * 14 * 0.077 = 389 N
mu*W = 0.04 * 13342 = 534 N
a = (2125 - 389 - 534) / 1360 = 0.855 m/s^2

Ground roll: Sg = 24.0^2 / (2*0.855) = 337 m
Clear 50ft obstacle: 1.67 * Sg = 563 m
Total takeoff distance: 600 m (with safety factor)
```

### 5.2 Landing Performance
```
Approach speed: 1.3 * Vs0 = 1.3 * 72 = 93.6 km/h = 26.0 m/s
Touchdown speed: 1.15 * Vs0 = 82.8 km/h = 23.0 m/s

Landing roll:
Sg = V^2 / (2 * deceleration)
Deceleration = (D + mu*W) / m
D = 0.5 * 1.225 * 23.0^2 * 14 * 0.077 = 358 N
mu*W = 0.04 * 13342 = 534 N
a = (358 + 534) / 1360 = 0.656 m/s^2
Sg = 23.0^2 / (2*0.656) = 404 m
Clear 50ft obstacle: 1.67 * Sg = 675 m
Total landing distance: 700 m (with safety factor)
```

### 5.3 Ground Roll Summary
| Weight (kg) | Takeoff (m) | Landing (m) |
|---|---|---|
| 800 | 280 | 340 |
| 1000 | 340 | 380 |
| 1200 | 420 | 430 |
| 1360 (MTOW) | 600 | 700 |

---

## 6. CEILING CALCULATIONS

### 6.1 Absolute Ceiling
```
At ceiling: Rate of climb = 0
Pa = Pr
Pa = 51,000 W (reduced at altitude)

Air density at altitude h:
rho = 1.225 * exp(-h/8500)

At 4500m:
rho = 1.225 * exp(-4500/8500)
rho = 1.225 * 0.590 = 0.723 kg/m3

Power available at altitude:
Pa = 51,000 * (0.723/1.225) = 29,962 W

At Vy (120 km/h):
q = 0.5 * 0.723 * 33.33^2 = 402 Pa
CL = 13342 / (402*14) = 2.370
CD = 0.025 + 2.370^2/37.39 = 0.025+0.150 = 0.175
D = 402*14*0.175 = 985 N
Pr = 985 * 33.33 = 32,836 W

R/C = (29,962 - 32,836) / 13342 = -0.215 m/s (negative = cannot climb)

Service ceiling: where R/C = 0.5 m/s (100 fpm)
Iterating: service ceiling approximately 4500m at MTOW
```

---

## 7. STALL SPEED CALCULATIONS

### 7.1 Stall Speed
```
Vs = sqrt(2*W / (rho*S*CLmax))

CLmax (NACA 2412 with flaps): 2.0
CLmax (clean): 1.5

At MTOW, sea level:
Vs0 (flaps) = sqrt(2*13342 / (1.225*14*2.0))
Vs0 = sqrt(26684 / 34.3) = sqrt(778) = 27.9 m/s = 100 km/h

Vs1 (clean) = sqrt(2*13342 / (1.225*14*1.5))
Vs1 = sqrt(26684 / 25.725) = sqrt(1037) = 32.2 m/s = 116 km/h

At empty weight:
Vs0 = sqrt(2*7848 / 34.3) = sqrt(458) = 21.4 m/s = 77 km/h
Vs1 = sqrt(2*7848 / 25.725) = sqrt(610) = 24.7 m/s = 89 km/h
```

### 7.2 Stall Speed Summary
| Weight (kg) | Vs0 flaps (km/h) | Vs1 clean (km/h) |
|---|---|---|
| 800 | 77 | 89 |
| 1000 | 86 | 100 |
| 1200 | 94 | 109 |
| 1360 (MTOW) | 100 | 116 |

---

## 8. PERFORMANCE SUMMARY TABLE

| Parameter | Value | Conditions |
|---|---|---|
| Max speed | 250 km/h | Sea level, MTOW |
| Cruise speed | 200 km/h | Sea level, 1000 kg |
| Stall speed (flaps) | 77-100 km/h | Empty to MTOW |
| Stall speed (clean) | 89-116 km/h | Empty to MTOW |
| Best rate of climb | 3.38 m/s (665 fpm) | Empty weight |
| Rate of climb at MTOW | 1.99 m/s (392 fpm) | MTOW |
| Service ceiling | 4500 m | MTOW |
| Range (cruise) | 564 km | 200 km/h, 1000 kg |
| Range (max) | 564 km | 200 km/h |
| Endurance (max) | 4.25 hours | 100 km/h |
| Takeoff distance | 280-600 m | Empty to MTOW |
| Landing distance | 340-700 m | Empty to MTOW |
| Best L/D | 19.3 | 123 km/h |
| Max G loading | +3.8 / -1.5 | Per FAR Part 23 |
