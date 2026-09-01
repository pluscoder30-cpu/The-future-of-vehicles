# Structural Design — Hull, Fold-Node Frame, and Materials

## 1. Design Philosophy

The structural design must accommodate:
1. Normal flight loads (takeoff, landing, maneuvering)
2. Fold loads (metric perturbation during teleportation)
3. Fold radiation (electromagnetic and particle radiation during fold)
4. Fold thermal loads (heat dissipation during fold)
5. Emergency loads (hard landing, fold abort, impact)

## 2. Hull Structure

### 2.1 Primary Structure — Carbon Fiber Monocoque

```
Hull cross-section (forward view):

        ┌─────────────┐
       /               \
      /    Cabin        \
     /                   \
    │    ┌─────────┐    │
    │    │ Fold    │    │
    │    │ Coil    │    │
    │    │ Array   │    │
    │    └─────────┘    │
     \                 /
      \   Battery   /
       \  Bay      /
        └─────────┘
```

| Parameter | Value |
|-----------|-------|
| Material | Carbon fiber reinforced polymer (CFRP) |
| Layup | [0/±45/90]₄ quasi-isotropic |
| Thickness | 3 mm (hull skin), 15 mm (hull frame) |
| Tensile strength | 1,500 MPa |
| Compressive strength | 1,200 MPa |
| Young's modulus | 70 GPa |
| Density | 1,600 kg/m³ |
| Temperature rating | -40°C to +120°C |
| Total hull mass | 180 kg |

### 2.2 Secondary Structure — Aluminum Space Frame

The aluminum space frame provides:
- Structural attachment points for all subsystems
- Load paths for fold forces
- Ground handling points (landing gear, hoist points)
- Collision energy absorption

```
Space frame specification:
  Material: Aluminum 7075-T6
  Tube diameter: 25 mm
  Wall thickness: 2 mm
  Tensile strength: 572 MPa
  Mass: 85 kg
```

### 2.3 Tertiary Structure — Fold-Reinforced Hull

During fold operations, the fold field provides structural reinforcement. The fold field creates a **metric rigidity** that makes the hull effectively rigid:

```
Fold reinforcement:
  Fold field strength: 0.1 T
  Metric rigidity increase: 10×
  Effective hull strength during fold: 15,000 MPa
  Effective hull stiffness during fold: 700 GPa
```

This fold reinforcement allows the hull to be lighter than would otherwise be necessary for the fold loads.

## 3. Fold-Node Frame

### 3.1 Purpose

The fold-node frame is the structural element that supports the fold coils and transmits fold forces to the hull. It is designed to:
- Support the 12 fold coils in precise alignment
- Transmit fold forces (up to 4.2g equivalent) to the hull
- Maintain fold coil alignment during all operations
- Provide thermal isolation between coils and hull

### 3.2 Design

```
Fold-node frame (top view):

         C01
        / | \
      C12  |  C02
      /    |    \
    C11 --+-- C03
     |\  FC  /|
     | C10 C04 |
     |/    |   \|
    C09 --+-- C05
      \    |    /
      C08  |  C06
        \ | /
         C07

FC = Fold center (primary fold node location)
```

| Parameter | Value |
|-----------|-------|
| Material | Invar 36 (low thermal expansion) |
| Thermal expansion | 1.2 × 10⁻⁶ /°C |
| Mounting points | 12 (one per coil) + 8 (hull attachment) |
| Alignment accuracy | ±0.01 mm |
| Mass | 45 kg |

### 3.3 Coil Mounting

Each fold coil is mounted on the fold-node frame using a **kinematic mount** that provides:
- Precise positioning (±0.01 mm)
- Thermal isolation (thermal resistance > 10 K/W)
- Vibration isolation (damping ratio > 0.1)
- Easy removal for maintenance

### 3.4 Fold Force Transmission

Fold forces are transmitted from the fold-node frame to the hull through 8 structural struts:

```
Fold force path:
  Fold coils → Fold-node frame → Structural struts → Hull frame → Hull skin
```

The structural struts are designed to:
- Transmit fold forces (up to 100 kN per strut)
- Absorb fold vibration (damping ratio > 0.05)
- Provide thermal isolation (thermal resistance > 5 K/W)
- Allow limited movement (±2 mm) for fold alignment

## 4. Materials Selection

### 4.1 Hull Materials

| Component | Material | Reason |
|-----------|----------|--------|
| Hull skin | CFRP | High strength-to-weight ratio |
| Hull frame | CFRP | High strength-to-weight ratio |
| Space frame | Al 7075-T6 | Good strength, easy to machine |
| Fold-node frame | Invar 36 | Low thermal expansion |
| Structural struts | Ti-6Al-4V | High strength, good fatigue life |
| Hull coating | Ceramic TPS | Thermal protection |

### 4.2 Fold-Relevant Materials

| Component | Material | Reason |
|-----------|----------|--------|
| Fold coils | YBCO superconductor | High current capacity |
| Coil formers | Al₂O₃ ceramic | Electrical insulation, thermal conductivity |
| Fold field probes | Mu-metal | High magnetic permeability |
| Fold radar antenna | Copper-clad FR4 | RF performance, lightweight |

### 4.3 Passenger Compartment Materials

| Component | Material | Reason |
|-----------|----------|--------|
| Seats | Carbon fiber / memory foam | Lightweight, comfort |
| Floor | CFRP honeycomb | Lightweight, strong |
| Walls | CFRP / acoustic foam | Structural, noise reduction |
| Windows | Polycarbonate | Impact resistance, UV protection |
| Fold cocoon | CFRP / lead lining | Fold radiation protection |

## 5. Mass Budget

| Component | Mass (kg) | Percentage |
|-----------|-----------|------------|
| Hull skin (CFRP) | 180 | 21.4% |
| Hull frame (CFRP) | 95 | 11.3% |
| Space frame (Al) | 85 | 10.1% |
| Fold-node frame (Invar) | 45 | 5.4% |
| Structural struts (Ti) | 30 | 3.6% |
| Fold coils (12) | 144 | 17.1% |
| Hull coating (ceramic) | 25 | 3.0% |
| Fasteners, brackets | 36 | 4.3% |
| **Structural total** | **640** | **76.2%** |
| Batteries (4×85 kg) | 340 | 40.5% |
| Electronics, wiring | 45 | 5.4% |
| Life support | 35 | 4.2% |
| Seats, interior | 40 | 4.8% |
| Fold cocoon | 25 | 3.0% |
| Communication | 15 | 1.8% |
| **Non-structural total** | **200** | **23.8%** |
| **Total dry mass** | **840** | **100%** |

## 6. Structural Testing

### 6.1 Test Matrix

| Test | Load | Duration | Acceptance criteria |
|------|------|----------|---------------------|
| Static pull | 2.5g vertical | 5 sec | No permanent deformation |
| Static push | 2.5g horizontal | 5 sec | No permanent deformation |
| Fold simulation | 4.2g equivalent | 3.8 sec | No damage, full recovery |
| Vibration | 0.5-500 Hz sweep | 10 min/axis | No resonance below 50 Hz |
| Thermal cycling | -40°C to +60°C | 100 cycles | No delamination, no cracking |
| Impact | 10 J at hull surface | 1 ms | No penetration, no internal damage |
| Fold radiation | 100 mSv | 3.8 sec | No degradation of electronics |

### 6.2 Structural Life

| Component | Design life | Inspection interval |
|-----------|-------------|---------------------|
| Hull skin | 10,000 folds | Every 1,000 folds |
| Hull frame | 10,000 folds | Every 1,000 folds |
| Space frame | 10,000 folds | Every 2,000 folds |
| Fold-node frame | 5,000 folds | Every 500 folds |
| Structural struts | 5,000 folds | Every 500 folds |
| Fold coils | 1,000 folds | Every 100 folds |
