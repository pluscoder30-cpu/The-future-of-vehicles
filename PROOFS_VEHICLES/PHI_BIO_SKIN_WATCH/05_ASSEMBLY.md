# PHI BIO-SKIN WATCH — ASSEMBLY GUIDE
## Buildable Documentation | Step-by-Step Instructions

---

## BEFORE YOU START

### Safety Rules
1. **Wear safety glasses** when soldering
2. **Unplug** the soldering iron when not in use
3. **Work in a well-ventilated area** (solder fumes)
4. **Keep water away** from electronics
5. **Ask an adult** if you're unsure about anything

### Tools You'll Need
- Soldering iron (25-60W, adjustable temperature)
- Solder wire (60/40 or lead-free)
- Wire stripper (26-30 AWG)
- Flush cutters
- Tweezers (ESD safe)
- Magnifying lamp or headset
- Multimeter
- Hot glue gun
- Isopropyl alcohol (90%)
- Cotton swabs

### Time Needed
- **Total**: 4-5 hours
- **Sections**: Can be done in 1-hour chunks
- **Drying time**: 24 hours (adhesive)

---

## STEP 1: PREPARE THE CASE (30 minutes)

### 1.1 Print the Case
```
3D Print Settings:
- Material: PLA or Resin
- Layer Height: 0.1mm (for smooth finish)
- Infill: 100% (solid for waterproofing)
- Support: Yes (for internal channels)
- Post-process: Sand with 400-grit, then 800-grit
```

### 1.2 Clean the Case
1. Remove all support material
2. Wash with soap and water
3. Dry completely
4. Wipe with isopropyl alcohol
5. Let dry 10 minutes

### 1.3 Test Fit
1. Place Raspberry Pi Zero in case
2. Should fit snugly (not tight)
3. File any tight spots gently
4. Mark where wires will go

---

## STEP 2: SOLDER POWER SYSTEM (45 minutes)

### 2.1 Prepare Wires
```
Wire lengths needed:
- Red: 3cm (battery +)
- Black: 3cm (battery -)
- Red: 5cm (3.3V rail)
- Black: 5cm (ground rail)
- Red: 4cm (Qi coil +)
- Black: 4cm (Qi coil -)
```

### 2.2 Connect TP4056 Charger
```
TP4056 Module:
┌─────────────────────────┐
│  IN+   IN-   OUT+  OUT- │
│   │     │     │     │   │
│   ▼     ▼     ▼     ▼   │
│  Qi+  Qi-   Bat+  Bat- │
└─────────────────────────┘

Connections:
1. Solder Qi coil wires to IN+ and IN-
2. Solder battery wires to OUT+ and OUT-
3. Do NOT connect battery yet!
```

### 2.3 Add Voltage Regulator
```
MCP1700 LDO:
┌─────────────────┐
│  IN   GND   OUT │
│   │    │    │   │
│   ▼    ▼    ▼   │
│ Bat+  GND  3.3V│
└─────────────────┘

Connections:
1. Solder TP4056 OUT+ to MCP1700 IN
2. Solder GND to GND
3. Solder MCP1700 OUT to 3.3V rail
```

### 2.4 Add Capacitors
```
Add 100nF capacitor:
- Across MCP1700 IN and GND
- Across MCP1700 OUT and GND

Add 10µF capacitor:
- Across battery + and - (bulk storage)
```

### 2.5 Test Power
1. Connect battery (red to +, black to -)
2. Measure 3.3V output with multimeter
3. Should be 3.3V ±0.1V
4. If not, check connections!

---

## STEP 3: INSTALL RASPBERRY PI (30 minutes)

### 3.1 Prepare Pi Zero
1. Solder GPIO header (if not pre-soldered)
2. Remove unnecessary components (optional)
3. Clean flux residue with isopropyl

### 3.2 Connect Power
```
Pi Zero Power Pins:
- Pin 1: 3.3V (connect to 3.3V rail)
- Pin 6: GND (connect to ground rail)
- Pin 2: 5V (leave unconnected - not needed)

Solder wires:
1. 3.3V rail → Pi Pin 1
2. Ground rail → Pi Pin 6
```

### 3.3 Mount in Case
1. Place Pi in case (GPIO header facing up)
2. Hot glue corners to secure
3. Do NOT glue GPIO pins!
4. Verify Pi is flat and level

---

## STEP 4: SOLDER I2C SENSORS (60 minutes)

### 4.1 Prepare Sensor Wires
```
I2C Bus wires:
- SDA: 6 wires (one to each sensor)
- SCL: 6 wires (one to each sensor)
- VCC: 6 wires (3.3V to each sensor)
- GND: 6 wires (ground to each sensor)

Total: 24 wires (6 sensors × 4 wires)
```

### 4.2 Solder MAX30102 (Heart Rate)
```
MAX30102 Module:
┌─────────────────────┐
│  VCC  GND  SDA  SCL │
│   │    │    │    │   │
│   ▼    ▼    ▼    ▼   │
│ 3.3V  GND  GPIO2 GPIO3│
└─────────────────────┘

1. Solder VCC to 3.3V rail
2. Solder GND to ground rail
3. Solder SDA to GPIO 2
4. Solder SCL to GPIO 3
5. Solder INT to GPIO 7 (for interrupts)
```

### 4.3 Solder ADS1115 (ADC)
```
ADS1115 Module:
┌─────────────────────┐
│  VDD  GND  SDA  SCL │
│  A0   A1   A2   A3  │
│   │    │    │    │   │
│   ▼    ▼    ▼    ▼   │
│ 3.3V  GND GPIO2 GPIO3│
│  Glu  Cor  (R)  (R)  │
└─────────────────────┘

1. Solder VDD to 3.3V rail
2. Solder GND to ground rail
3. Solder SDA to GPIO 2 (shared I2C)
4. Solder SCL to GPIO 3 (shared I2C)
5. Solder A0 to glucose sensor output
6. Solder A1 to cortisol sensor output
7. A2, A3: Leave unconnected (reserved)
```

### 4.4 Solder Remaining Sensors
```
Repeat for each sensor:
- MCP9808 (Temperature): I2C address 0x18
- BME280 (Environment): I2C address 0x76
- MPU6050 (IMU): I2C address 0x68
- VEML6075 (UV): I2C address 0x10

All share SDA (GPIO 2) and SCL (GPIO 3)
```

### 4.5 Add Pull-Up Resistors
```
Add 4.7kΩ pull-up resistors:
- One on SDA line (to 3.3V)
- One on SCL line (to 3.3V)

These are required for I2C to work!
```

---

## STEP 5: SOLDER DISPLAY (30 minutes)

### 5.1 Prepare Display Wires
```
Display wires needed:
- DIN (MOSI): 3cm
- CLK (SCLK): 3cm
- CS: 3cm
- DC: 3cm
- RST: 3cm
- VCC: 2cm
- GND: 2cm
```

### 5.2 Connect Display
```
SSD1351 Display:
┌─────────────────────┐
│ VCC GND DIN CLK CS │
│  DC  RST           │
│  │   │   │   │  │ │ │
│  ▼   ▼   ▼   ▼  ▼ ▼ ▼│
│3.3V GND GPIO10 11 8│
│          MOSI SCLK CE0│
└─────────────────────┘

Connections:
1. VCC → 3.3V rail
2. GND → ground rail
3. DIN → GPIO 10 (MOSI)
4. CLK → GPIO 11 (SCLK)
5. CS → GPIO 8 (CE0)
6. DC → GPIO 24
7. RST → GPIO 25
```

### 5.3 Test Display
1. Power on the Pi
2. Run test script (see MANUAL.md)
3. Display should show test pattern
4. If not, check solder joints!

---

## STEP 6: SOLDER BLE MODULE (20 minutes)

### 6.1 Connect nRF52840
```
nRF52840 BLE Module:
┌─────────────────────┐
│  VCC  GND  TX   RX  │
│   │    │    │    │   │
│   ▼    ▼    ▼    ▼   │
│ 3.3V  GND GPIO14 15 │
│              TXD  RXD│
└─────────────────────┘

Connections:
1. VCC → 3.3V rail
2. GND → ground rail
3. TX → GPIO 15 (RXD)
4. RX → GPIO 14 (TXD)
```

### 6.2 Configure BLE
1. Flash nRF52840 with BLE firmware
2. Set device name: "PHI-BIO-WATCH"
3. Set pairing code: 123456
4. Test connection from phone

---

## STEP 7: APPLY SELF-CLEANING SURFACE (45 minutes)

### 7.1 Prepare Surface
1. Clean display with isopropyl alcohol
2. Let dry completely (10 minutes)
3. Ensure no dust particles

### 7.2 Apply TiO2 Layer
```
TiO2 Nanoparticle Application:
1. Shake TiO2 spray bottle vigorously
2. Hold 15cm from surface
3. Apply thin, even coat
4. Let dry 15 minutes
5. Apply second coat
6. Let dry 15 minutes
```

### 7.3 Apply Fluoropolymer
```
Fluoropolymer Coating:
1. Apply thin layer with brush
2. Cover entire display area
3. Avoid drips
4. Let dry 30 minutes
5. Cure with UV light (optional)
```

### 7.4 Test Hydrophobicity
1. Drop water on surface
2. Should form perfect beads
3. Water should roll off easily
4. If not, reapply coating

---

## STEP 8: ASSEMBLE CASE (30 minutes)

### 8.1 Install Sensor Layer
1. Place sensors in case (check alignment)
2. Hot glue sensor edges to secure
3. Route wires neatly
4. Ensure no wire pinch points

### 8.2 Install Display
1. Place display in case
2. Connect display cable
3. Hot glue display edges
4. Verify display is flush

### 8.3 Close Case
1. Apply UV adhesive to case edges
2. Press top and bottom together
3. Cure with UV light (2 minutes)
4. Wipe excess adhesive

### 8.4 Install Band
1. Slide band through lugs
2. Insert clasp pins
3. Test band adjustment
4. Ensure secure fit

---

## STEP 9: FINAL TESTING (30 minutes)

### 9.1 Power Test
1. Place on Qi charger
2. LED should light up (charging)
3. Wait 5 minutes
4. Remove from charger
5. Pi should boot automatically

### 9.2 Sensor Test
Run sensor test script:
```python
# Test all sensors
python3 test_sensors.py
```

Expected output:
```
MAX30102: OK (Heart rate detected)
ADS1115: OK (ADC reading)
MCP9808: OK (25.3°C)
BME280: OK (Temp/Humidity/Pressure)
MPU6050: OK (Accelerometer/Gyro)
VEML6075: OK (UV index)
Display: OK (Test pattern)
BLE: OK (Connected)
```

### 9.3 Self-Cleaning Test
1. Touch display with oily finger
2. Wait 30 seconds
3. Drop water on surface
4. Oil should be removed
5. Display should be clean

### 9.4 Water Resistance Test
1. Run under faucet for 30 seconds
2. Dry with towel
3. Verify no water inside
4. Check all functions work

---

## STEP 10: CALIBRATION (20 minutes)

### 10.1 Heart Rate Calibration
1. Wear watch on wrist
2. Hold still for 30 seconds
3. Compare with known heart rate
4. Adjust offset if needed

### 10.2 Temperature Calibration
1. Place in room with known temperature
2. Compare MCP9808 reading
3. Adjust offset if needed

### 10.3 UV Calibration
1. Go outside on sunny day
2. Compare with UV index app
3. Adjust offset if needed

---

## TROUBLESHOOTING

### Problem: Pi won't boot
- Check power connections
- Verify 3.3V output
- Check SD card (if used)
- Re-flash firmware

### Problem: Display blank
- Check SPI connections
- Verify GPIO pins
- Run display test script
- Check for cold solder joints

### Problem: Sensors not reading
- Check I2C connections
- Verify pull-up resistors
- Run I2C scanner
- Check sensor addresses

### Problem: BLE won't connect
- Check TX/RX connections
- Verify firmware
- Check pairing code
- Restart Pi

### Problem: Self-cleaning not working
- Reapply TiO2 coating
- Check fluoropolymer layer
- Ensure surface is clean
- Test hydrophobicity

---

## CARE & MAINTENANCE

### Daily Care
- Wipe with soft, dry cloth
- Avoid harsh chemicals
- Remove before showering (if not waterproof)

### Weekly Care
- Clean with isopropyl alcohol
- Check band for wear
- Verify all functions

### Monthly Care
- Reapply fluoropolymer (if needed)
- Calibrate sensors
- Check battery health

### Battery Replacement
1. Open case (UV adhesive)
2. Disconnect old battery
3. Connect new battery
4. Reassemble
5. Recalibrate

---

## SAFETY WARNINGS

1. **Do not** submerge in water deeper than 100m
2. **Do not** expose to temperatures above 200°C
3. **Do not** use if band is damaged
4. **Do not** open case while wearing
5. **Do not** charge overnight unattended
6. **Do not** use if skin irritation occurs
7. **Do not** share with others (hygiene)
8. **Do not** use medical claims without FDA approval

---

## NEXT STEPS

After assembly:
1. Download companion app (see MANUAL.md)
2. Pair with phone via BLE
3. Set up health monitoring
4. Customize display face
5. Join community forum

---

**Document**: 05_ASSEMBLY.md
**Vehicle**: PHI BIO-SKIN WATCH
**Status**: BUILDABLE ✓
**Time**: 4-5 hours
**Difficulty**: Intermediate (soldering required)
