# Structural Design — Hull, Temporal Frame, and Materials

## 1. Design Philosophy

The structural design must accommodate:
1. Normal flight loads (takeoff, landing, maneuvering)
2. Temporal fold loads (metric perturbation during time folding)
3. Temporal fold radiation (electromagnetic and particle radiation during fold)
4. Temporal fold thermal loads (heat dissipation during fold)
5. Emergency loads (hard landing, temporal fold abort, impact)

## 2. Hull Structure

### 2.1 Primary Structure — Carbon Fiber Monocoque

```
Hull cross-section (forward view):

        ┌──────────────────┐
       /                    \
      /      Cabin           \
     /                        \
    │    ┌──────────────┐     │
    │    │  Temporal    │     │
    │    │   Coil       │     │
    │    │   Array      │     │
    │    └──────────────┘     │
     \                      /
      \    Battery Bay    /
       \                  /
        └────────────────┘
```

| Parameter | Value |
|-----------|-------|
| Material | Carbon fiber reinforced polymer (CFRP) |
| Layup | [0/±45/90]₅ quasi-isotropic |
| Thickness | 4 mm (hull skin), 18 mm (hull frame) |
| Tensile strength | 1,500 MPa |
| Compressive strength | 1,200 MPa |
| Young's modulus | 70 GPa |
| Density | 1,600 kg/m³ |
| Temperature rating | -40°C to +120°C |
| Total hull mass | 220 kg |

### 2.2 Secondary Structure — Aluminum Space Frame

```
Space frame specification:
  Material: Aluminum 7075-T6
  Tube diameter: 28 mm
  Wall thickness: 2.2 mm
  Tensile strength: 572 MPa
  Mass: 100 kg
```

### 2.3 Tertiary Structure — Temporal-Reinforced Hull

During temporal fold operations, the temporal fold field provides structural reinforcement:

```
Temporal reinforcement:
  Temporal fold field strength: 0.15 T
  Metric rigidity increase: 15×
  Effective hull strength during temporal fold: 22,500 MPa
  Effective hull stiffness during temporal fold: 1,050 GPa
```

## 3. Temporal Frame

### 3.1 Purpose

The temporal frame is the structural element that supports the temporal coils and transmits temporal fold forces to the hull.

### 3.2 Design

```
Temporal frame (side view):

         C01    C02
        / | \  / | \
      C08  | C03  |  C03
      /    |/   \|    \
    C07 ---+-- TC --+--- C03
      \    |\   /|    /
      C06  | C04  |  C04
        \ | /  \ | /
         C05    C04

TC = Temporal center (fold node location)
```

| Parameter | Value |
|-----------|-------|
| Material | Invar 36 (low thermal expansion) |
| Thermal expansion | 1.2 × 10⁻⁶ /°C |
| Mounting points | 8 (one per coil) + 10 (hull attachment) |
| Alignment accuracy | ±0.008 mm |
| Mass | 55 kg |

### 3.3 Coil Mounting

Each temporal coil is mounted on the temporal frame using a kinematic mount:
- Precise positioning (±0.008 mm)
- Thermal isolation (thermal resistance > 12 K/W)
- Vibration isolation (damping ratio > 0.12)
- Easy removal for maintenance

### 3.4 Temporal Force Transmission

Temporal fold forces are transmitted from the temporal frame to the hull through 10 structural struts:

```
Temporal force path:
  Temporal coils → Temporal frame → Structural struts → Hull frame → Hull skin
```

## 4. Materials Selection

### 4.1 Hull Materials

| Component | Material | Reason |
|-----------|----------|--------|
| Hull skin | CFRP | High strength-to-weight ratio |
| Hull frame | CFRP | High strength-to-weight ratio |
| Space frame | Al 7075-T6 | Good strength, easy to machine |
| Temporal frame | Invar 36 | Low thermal expansion |
| Structural struts | Ti-6Al-4V | High strength, good fatigue life |
| Hull coating | Ceramic TPS | Thermal protection |

### 4.2 Temporal-Relevant Materials

| Component | Material | Reason |
|-----------|----------|--------|
| Temporal coils | YBCO superconductor | High current capacity |
| Coil formers | Al₂O₃ ceramic | Electrical insulation, thermal conductivity |
| Temporal fold field probes | Mu-metal | High magnetic permeability |
| Temporal radar antenna | Copper-clad FR4 | RF performance, lightweight |

### 4.3 Passenger Compartment Materials

| Component | Material | Reason |
|-----------|----------|--------|
| Seats | Carbon fiber / memory foam | Lightweight, comfort |
| Floor | CFRP honeycomb | Lightweight, strong |
| Walls | CFRP / acoustic foam | Structural, noise reduction |
| Windows | Polycarbonate | Impact resistance, UV protection |
| Temporal cocoon | CFRP / lead lining | Temporal fold radiation protection |

## 5. Mass Budget

| Component | Mass (kg) | Percentage |
|-----------|-----------|------------|
| Hull skin (CFRP) | 220 | 21.0% |
| Hull frame (CFRP) | 110 | 10.5% |
| Space frame (Al) | 100 | 9.5% |
| Temporal frame (Invar) | 55 | 5.2% |
| Structural struts (Ti) | 38 | 3.6% |
| Temporal coils (8) | 176 | 16.8% |
| Hull coating (ceramic) | 30 | 2.9% |
| Fasteners, brackets | 41 | 3.9% |
| **Structural total** | **770** | **73.3%** |
| Batteries (4×85 kg) | 340 | 32.4% |
| Electronics, wiring | 55 | 5.2% |
| Life support | 40 | 3.8% |
| Seats, interior | 50 | 4.8% |
| Temporal cocoon | 30 | 2.9% |
| Communication | 18 | 1.7% |
| **Non-structural total** | **280** | **26.7%** |
| **Total dry mass** | **1,050** | **100%** |

## 6. Structural Testing

### 6.1 Test Matrix

| Test | Load | Duration | Acceptance criteria |
|------|------|----------|---------------------|
| Static pull | 2.5g vertical | 5 sec | No permanent deformation |
| Static push | 2.5g horizontal | 5 sec | No permanent deformation |
| Temporal fold simulation | 1.2g equivalent | 60 sec | No damage, full recovery |
| Vibration | 0.5-500 Hz sweep | 10 min/axis | No resonance below 45 Hz |
| Thermal cycling | -40°C to +60°C | 150 cycles | No delamination, no cracking |
| Impact | 15 J at hull surface | 1 ms | No penetration, no internal damage |
| Temporal fold radiation | 0.1 mSv | 60 sec | No degradation of electronics |

### 6.2 Structural Life

| Component | Design life | Inspection interval |
|-----------|-------------|---------------------|
| Hull skin | 5,000 folds | Every 500 folds |
| Hull frame | 5,000 folds | Every 500 folds |
| Space frame | 5,000 folds | Every 1,000 folds |
| Temporal frame | 2,500 folds | Every 250 folds |
| Structural struts | 2,500 folds | Every 250 folds |
| Temporal coils | 500 folds | Every 50 folds |
