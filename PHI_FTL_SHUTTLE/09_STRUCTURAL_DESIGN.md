# Structural Design — Hull, Warp Frame, and Materials

## 1. Design Philosophy

The structural design must accommodate:
1. Normal flight loads (takeoff, landing, maneuvering)
2. Warp loads (metric perturbation during FTL travel)
3. Warp radiation (electromagnetic and particle radiation during warp)
4. Warp thermal loads (heat dissipation during warp)
5. Emergency loads (hard landing, warp abort, impact)
6. Interstellar medium impacts (dust, gas at 10c)

## 2. Hull Structure

### 2.1 Primary Structure — Carbon Fiber Monocoque

```
Hull cross-section (forward view):

        ┌─────────────────────┐
       /                       \
      /        Cabin             \
     /                             \
    │    ┌─────────────────┐      │
    │    │   Warp Coil     │      │
    │    │    Array        │      │
    │    └─────────────────┘      │
     \                           /
      \       Battery Bay       /
       \                       /
        └─────────────────────┘
```

| Parameter | Value |
|-----------|-------|
| Material | Carbon fiber reinforced polymer (CFRP) |
| Layup | [0/±45/90]₆ quasi-isotropic |
| Thickness | 5 mm (hull skin), 20 mm (hull frame) |
| Tensile strength | 1,500 MPa |
| Compressive strength | 1,200 MPa |
| Young's modulus | 70 GPa |
| Density | 1,600 kg/m³ |
| Temperature rating | -40°C to +120°C |
| Total hull mass | 280 kg |

### 2.2 Secondary Structure — Aluminum Space Frame

```
Space frame specification:
  Material: Aluminum 7075-T6
  Tube diameter: 30 mm
  Wall thickness: 2.5 mm
  Tensile strength: 572 MPa
  Mass: 120 kg
```

### 2.3 Tertiary Structure — Warp-Reinforced Hull

During warp operations, the warp field provides structural reinforcement:

```
Warp reinforcement:
  Warp field strength: 0.5 T
  Metric rigidity increase: 100×
  Effective hull strength during warp: 150,000 MPa
  Effective hull stiffness during warp: 7,000 GPa
```

### 2.4 Interstellar Medium Shielding

At 10c, interstellar dust and gas become a significant hazard. The hull includes:

```
Interstellar medium shielding:
  Forward shield: Tungsten carbide, 10 mm
  Side shields: Ceramic composite, 5 mm
  Aft shield: Aluminum, 5 mm
  Dust erosion rate: < 0.1 mm per 10 light-years
  Gas heating: Managed by thermal protection system
```

## 3. Warp Frame

### 3.1 Purpose

The warp frame is the structural element that supports the warp coils and transmits warp forces to the hull.

### 3.2 Design

```
Warp frame (top view):

         C01
        / | \
      C08  |  C02
      /    |    \
    C07 --+-- C03
     |\  WC  /|
     | C06 C04 |
     |/    |   \|
      C05 --+--
        \ | /
         C05

WC = Warp center (bubble center)
```

| Parameter | Value |
|-----------|-------|
| Material | Invar 36 (low thermal expansion) |
| Thermal expansion | 1.2 × 10⁻⁶ /°C |
| Mounting points | 8 (one per coil) + 12 (hull attachment) |
| Alignment accuracy | ±0.005 mm |
| Mass | 65 kg |

### 3.3 Coil Mounting

Each warp coil is mounted on the warp frame using a kinematic mount:
- Precise positioning (±0.005 mm)
- Thermal isolation (thermal resistance > 15 K/W)
- Vibration isolation (damping ratio > 0.15)
- Easy removal for maintenance

### 3.4 Warp Force Transmission

Warp forces are transmitted from the warp frame to the hull through 12 structural struts:

```
Warp force path:
  Warp coils → Warp frame → Structural struts → Hull frame → Hull skin
```

## 4. Materials Selection

### 4.1 Hull Materials

| Component | Material | Reason |
|-----------|----------|--------|
| Hull skin | CFRP | High strength-to-weight ratio |
| Hull frame | CFRP | High strength-to-weight ratio |
| Space frame | Al 7075-T6 | Good strength, easy to machine |
| Warp frame | Invar 36 | Low thermal expansion |
| Structural struts | Ti-6Al-4V | High strength, good fatigue life |
| Hull coating | Ceramic TPS | Thermal protection |
| Forward shield | Tungsten carbide | Interstellar medium protection |

### 4.2 Warp-Relevant Materials

| Component | Material | Reason |
|-----------|----------|--------|
| Warp coils | YBCO superconductor | High current capacity |
| Coil formers | Al₂O₃ ceramic | Electrical insulation, thermal conductivity |
| Warp field probes | Mu-metal | High magnetic permeability |
| Warp radar antenna | Copper-clad FR4 | RF performance, lightweight |

## 5. Mass Budget

| Component | Mass (kg) | Percentage |
|-----------|-----------|------------|
| Hull skin (CFRP) | 280 | 23.3% |
| Hull frame (CFRP) | 140 | 11.7% |
| Space frame (Al) | 120 | 10.0% |
| Warp frame (Invar) | 65 | 5.4% |
| Structural struts (Ti) | 45 | 3.8% |
| Warp coils (8) | 280 | 23.3% |
| Hull coating (ceramic) | 35 | 2.9% |
| Forward shield (W) | 25 | 2.1% |
| Fasteners, brackets | 50 | 4.2% |
| **Structural total** | **1,040** | **86.7%** |
| Batteries (4×85 kg) | 340 | 28.3% |
| Electronics, wiring | 65 | 5.4% |
| Life support | 45 | 3.8% |
| Seats, interior | 60 | 5.0% |
| Warp cocoon | 40 | 3.3% |
| Communication | 20 | 1.7% |
| **Non-structural total** | **160** | **13.3%** |
| **Total dry mass** | **1,200** | **100%** |

## 6. Structural Testing

### 6.1 Test Matrix

| Test | Load | Duration | Acceptance criteria |
|------|------|----------|---------------------|
| Static pull | 3g vertical | 5 sec | No permanent deformation |
| Static push | 3g horizontal | 5 sec | No permanent deformation |
| Warp simulation | 2g equivalent | 120 sec | No damage, full recovery |
| Vibration | 0.5-500 Hz sweep | 10 min/axis | No resonance below 40 Hz |
| Thermal cycling | -40°C to +60°C | 200 cycles | No delamination, no cracking |
| Impact | 50 J at hull surface | 1 ms | No penetration, no internal damage |
| Warp radiation | 100 mSv | 120 sec | No degradation of electronics |
| Interstellar medium | 10 J dust impact | 1 ms | No penetration |

### 6.2 Structural Life

| Component | Design life | Inspection interval |
|-----------|-------------|---------------------|
| Hull skin | 100 light-years | Every 10 light-years |
| Hull frame | 100 light-years | Every 10 light-years |
| Space frame | 100 light-years | Every 20 light-years |
| Warp frame | 50 light-years | Every 5 light-years |
| Structural struts | 50 light-years | Every 5 light-years |
| Warp coils | 10 light-years | Every 1 light-year |
