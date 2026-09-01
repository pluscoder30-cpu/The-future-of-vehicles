# PHI SUPER GOGGLES — MECHANICAL DESIGN

## 3D Printed Housing and Mechanical Specifications

---

## OVERALL DIMENSIONS

```
Width: 185mm
Height: 65mm
Depth: 55mm
Weight: 340g (with battery)
Display Area: 38mm × 22mm per eye
```

---

## COMPONENT PLACEMENT (EXPLODED VIEW)

```
Layer 1 (Innermost): OPTICS
  Left OLED + Lens + Eyecup
  Right OLED + Lens + Eyecup
  Diopter adjustment sliders

Layer 2: ELECTRONICS
  DE10-Lite FPGA (central)
  4× ADS1256 ADC (flanking FPGA)
  4× CD74HC4067 MUX (near sensors)
  ADV7533 HDMI bridge (near displays)
  BNO055 IMU (center, vibration-isolated)

Layer 3: SENSORS + POWER
  8× EMF Sensors (perimeter, shielded)
  FPB-5 Battery 8000mAh (rear, centered) — Zero fire/explosion risk — plasma is self-limiting
  Power regulation board

Layer 4 (Outermost): STRUCTURE
  Main housing shell
  Head strap attachment points
  Button panels
  Heat sink mounting
```

---

## SENSOR PLACEMENT — PHI-HARMONIC SPACING

```
Sensor positions (mm from left):
  S1: 0mm    S2: 12mm   S3: 31mm   S4: 62mm
  S5: 103mm  S6: 123mm  S7: 148mm  S8: 173mm

Spacing follows φ-recursive ratios.
Y position: 32mm from bottom (centerline)
Z position: Protruding 3mm from front surface
```

### Sensor Housing Detail

```
Dimension: 14mm × 10mm × 8mm
Material: PETG (RF-transparent)
Mounting: Snap-fit into sensor plate
Cable: 6" shielded twisted pair
Shielding: Ferrite sleeve for EMI
```

---

## DISPLAY OPTICS

```
Eye relief: 22mm (glasses-compatible)
Lens focal length: 18mm (Fresnel)
OLED size: 0.39" diagonal (1920×1080)
Effective FOV: 65° horizontal
Magnification: 10×
Diopter range: -5D to +3D
```

---

## BATTERY COMPARTMENT

```
Dimensions: 71mm × 36mm × 22mm
Panel: Removable, 4× thumbscrews (tool-free)
Sealing: Silicone gasket (splash-proof)
Connectors: USB-C (charging), DC Jack (backup)
```

---

## HEAD STRAP SYSTEM

```
Material: 38mm elastic nylon webbing
Adjustment: Velcro + slider buckle
Rear pad: 80mm × 60mm, padded foam
Attachment: 4× D-rings on main housing
Tension: Adjustable 2-8 kg
Head circumference: 52-62 cm
```

---

## THERMAL MANAGEMENT

```
FPGA Heat Dissipation:
  TDP: 7.5W
  Thermal Pad: 3mm, 6W/mK
  Heat Sink: 20×20×8mm aluminum, 15°C/W
  Active Cooling: 5mm blower fan (0.5W, 3000 RPM)

Temperature Limits:
  FPGA junction: 85°C warning, 95°C shutdown
  Surface: 45°C max (user comfort)
```

---

## 3D PRINTING SPECIFICATIONS

| Part | Material | Layer | Infill | Walls | Time | Filament |
|------|----------|-------|--------|-------|------|----------|
| Main Housing | PETG | 0.2mm | 30% | 3 | 8h | 150g |
| Sensor Plate | PETG | 0.16mm | 40% | 4 | 4h | 80g |
| Display Housing | PLA | 0.2mm | 35% | 3 | 3h each | 50g each |
| Eyecup | TPU 95A | 0.12mm | 20% | 2 | 1h each | 15g each |
| Diopter Ring | PLA | 0.12mm | 100% | 2 | 30min | 8g each |

**Total filament: ~900g ($37)**

---

## ERGONOMIC CONSIDERATIONS

1. **Weight Distribution:** Battery counterweights front-heavy optics
2. **Pressure Points:** Foam padding distributes force
3. **Ventilation:** Bottom vents prevent lens fogging
4. **Glasses Compatibility:** 22mm eye relief
5. **Balance Point:** 15mm forward of ear canal
6. **Maximum Session:** 60 minutes comfortable
