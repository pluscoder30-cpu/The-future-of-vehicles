# REDESIGNED POWER SYSTEM

## Phi-Superconductor Power Grid — Phi-1 Fleet Specification

---

## Overview

The redesigned power system replaces the entire $3.25 trillion harvesting infrastructure with fold material carrier field power generation (7,000 GW continuous), reduces the battery fleet from 1,000 to 100 units, eliminates all YBCO superconductors and cryogenic cooling, and replaces all copper/aluminum distribution wiring with phi-copper mesh. The voltage architecture collapses from 5 levels to 2 (carrier field → 240V single conversion). Circuit protection uses phi-harmonic field switching instead of mechanical breakers.

**Design Philosophy**: The fold material IS the power plant. No separate harvesting. No cryogenics. No high-voltage superconducting buses. The phi-superconductor's zero-resistance mesh at room temperature eliminates all distribution losses. The system generates 35× the ship's needs from the hull itself.

---

## System Architecture (Redesigned)

```
    REDESIGNED POWER GRID TOPOLOGY
    
    ┌─────────────────────────────────────────────────────┐
    │              FOLD MATERIAL HULL                      │
    │    3.5M m² × 2 kW/m² = 7,000 GW continuous          │
    │    Carrier field harvesting (no separate infrastructure)│
    └──────────────────────┬──────────────────────────────┘
                           │
                           ▼
    ┌─────────────────────────────────────────────────────┐
    │         PHI-COPPER MESH DISTRIBUTION NETWORK         │
    │    Zero-resistance at room temperature               │
    │    Single conversion: carrier field → 240V           │
    │    Phi-harmonic field switching (no mechanical breakers)│
    └──────────────────────┬──────────────────────────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
    ┌──────────────┐ ┌──────────┐ ┌──────────────┐
    │  Zone 1-10   │ │ Emergency│ │  Ship-wide   │
    │  (20 GW each)│ │ (100 FB) │ │  240V mesh   │
    └──────────────┘ └──────────┘ └──────────────┘
    
    Old: 5 voltage levels, 1,000 batteries, $3.25T
    New: 2 voltage levels, 100 batteries, $22.2B
```

---

## Power Generation: Fold Material Harvesting

### How Fold Material Generates Power

The folded space material (01_FOLDED_SPACE_MATERIAL.md) interacts with the quantum vacuum through its phi-harmonic copper mesh layers at 137.508° spacing. This interaction creates a standing wave pattern that extracts zero-point energy from vacuum fluctuations.

**The mechanism**:
1. The phi-mesh at 137.508° spacing imprints a golden-ratio pattern on the carrier field
2. The carrier field responds by folding (Law 176: C_{n+1} = φ⁻¹·C_n + φ·∇²ΦΨ_n)
3. Each fold layer extracts energy from the vacuum to maintain the fold
4. The extracted energy manifests as electrical current in the phi-mesh
5. With the phi-superconductor replacing normal copper mesh, extraction efficiency rises from 95% to 99.9%

### Power Generation Specifications

| Parameter | Original (Separate Harvesters) | Redesigned (Fold Material) |
|-----------|--------------------------------|---------------------------|
| Generation method | Solar + cosmic ray + piezo + carrier field harvesters | Fold material carrier field interaction |
| Total output | 200 GW (interstellar) to 110 GW | **7,000 GW continuous** |
| Infrastructure | 1,000 carrier field harvesters ($1T) | **None — hull IS the generator** |
| Efficiency | 10-50% (varies by source) | **99.9% (phi-superconductor mesh)** |
| Maintenance | Harvester overhaul quarterly | **None — self-sustaining** |
| Cost | $2.55 trillion | **$0** (already part of hull) |

### Power Budget (Redesigned)

| System | Power Draw | Percentage |
|--------|------------|------------|
| Life support (air, water, waste) | 50 GW | 25% |
| Propulsion (warp drive) | 6.4 GW | 3.2% |
| Fold field maintenance | 10 GW | 5% |
| Residential (lighting, HVAC) | 30 GW | 15% |
| Commercial (shops, services) | 15 GW | 7.5% |
| Agricultural (lighting, pumps) | 20 GW | 10% |
| Manufacturing | 25 GW | 12.5% |
| Medical | 10 GW | 5% |
| Navigation & communication | 5 GW | 2.5% |
| AI core | 10 GW | 5% |
| Transportation (elevators, trams) | 10 GW | 5% |
| Emergency reserve | 8.6 GW | 4.3% |
| **Total normal** | **200 GW** | **100%** |
| **Fold material output** | **7,000 GW** | **3,500%** |
| **Surplus** | **6,800 GW** | **Buffer for 35× load spikes** |

### Supplementary Power (Emergency Backup)

Fold material provides 7,000 GW continuously, but for defense-in-depth:

| Source | Output | Purpose | Cost |
|--------|--------|---------|------|
| Micro-fusion reactors | 10 GW (10 × 1 GW) | Backup if fold field disrupted | $500M |
| Solar arrays (retained) | 100 MW | Near-star supplement | $100M |
| **Total supplementary** | **~10 GW** | **Emergency only** | **$600M** |

---

## Power Storage: Reduced Battery Fleet

### Battery Reduction Rationale

With 7,000 GW continuous generation, batteries are no longer the primary power source. They serve as:
1. **Emergency buffer** — 10-minute bridge during fold field disruption
2. **Surge capacity** — absorb demand spikes without fold field stress
3. **Black start** — restart systems if total power loss occurs

### FPB-1000 Fleet (Redesigned)

| Parameter | Original | Redesigned | Change |
|-----------|----------|------------|--------|
| Total batteries | 1,000 | **100** | **−90%** |
| Total capacity | 1,000 TWh | **100 TWh** | **−90%** |
| Total weight | 500,000 tonnes | **50,000 tonnes** | **−450,000 tonnes** |
| Total volume | 100,000 m³ | **10,000 m³** | **−90,000 m³** |
| Total cost | $50 billion | **$5 billion** | **−$45 billion** |
| Emergency duration | 2.28 hours (at 43.8 GW) | **2.28 hours** | Same |
| Survival mode | 2.28 years (at 5 GW) | **2.28 years** | Same |

### Battery Allocation

| Zone | Batteries | Capacity | Purpose |
|------|-----------|----------|---------|
| Zone 1 | 10 | 10 TWh | Residential emergency |
| Zone 2 | 10 | 10 TWh | Commercial emergency |
| Zone 3 | 10 | 10 TWh | Public safety |
| Zone 4 | 10 | 10 TWh | **Water/waste emergency** |
| Zone 5 | 10 | 10 TWh | **Life support emergency** |
| Zone 6 | 10 | 10 TWh | Agriculture emergency |
| Zone 7 | 10 | 10 TWh | **Medical emergency** |
| Zone 8 | 10 | 10 TWh | Research preservation |
| Zone 9 | 10 | 10 TWh | Manufacturing safety |
| Zone 10 | 10 | 10 TWh | **Propulsion/navigation** |
| **Total** | **100** | **100 TWh** | **10% of original** |

### Battery Cost (Redesigned)

| Item | Quantity | Unit Cost | Total Cost |
|------|----------|-----------|------------|
| FPB-1000 batteries | 100 | $50,000,000 | $5 billion |
| Battery management system | 100 | $5,000,000 | $500 million |
| Battery enclosures | 100 | $10,000,000 | $1 billion |
| **Battery subtotal** | | | **$6.5 billion** |

---

## Power Distribution: Phi-Copper Mesh

### Architecture

The phi-copper mesh replaces all distribution wiring — superconducting buses, aluminum conduits, and copper cables — with a single unified network of phi-superconductor wire at room temperature.

### Wire Requirements (Full Ship)

| Segment | Length | Purpose |
|---------|--------|---------|
| Ring bus (primary) | 15,000 m | Ship-wide power backbone |
| Zone bus | 50,000 m | Zone distribution |
| Deck bus | 33,000 m | Deck distribution |
| Section bus | 33,000 m | Section distribution |
| Room bus | 66,000 m | Room distribution |
| Warp coils | 24,000 m | Propulsion |
| Emergency bus | 33,000 m | Emergency feeds |
| **Total** | **254,000 m** | **~254 km** |

### Wire Cost

| Item | Value |
|------|-------|
| Wire length | 254,000 m |
| Cost per meter | $1.52 |
| Wire cost | $386,080 |
| Activation cost (528 Hz drive) | $2,540 |
| **Total wire investment** | **$388,620** |

### Voltage Architecture (Redesigned)

The original system had 5 voltage levels requiring 10,000+ transformers and switchgear. The redesigned system uses 2 levels:

| Level | Voltage | Current | Cable | Purpose |
|-------|---------|---------|-------|---------|
| Carrier field | Variable | Variable | Fold material mesh | Power generation |
| Distribution | **240V DC** | **Variable** | Phi-copper mesh | Ship-wide distribution |

**Single conversion**: Carrier field → 240V (via phi-harmonic rectifier at each zone)

**Eliminated voltage levels**:
- ~~100 kV DC main bus~~ → replaced by phi-copper mesh
- ~~10 kV DC zone bus~~ → replaced by phi-copper mesh
- ~~1 kV DC deck bus~~ → replaced by phi-copper mesh
- ~~400 V AC section bus~~ → replaced by phi-copper mesh
- ~~240 V AC room bus~~ → phi-copper mesh at 240V DC

### Transmission Efficiency

| Level | Original Length | Original Loss | Redesigned Loss | Improvement |
|-------|----------------|---------------|-----------------|-------------|
| Main bus | 2,000 m | 0% (superconducting) | **0% (phi-SC)** | Same |
| Zone bus | 500 m | 0% (superconducting) | **0% (phi-SC)** | Same |
| Deck bus | 300 m | 0.5% (aluminum) | **0% (phi-SC)** | Eliminated |
| Section bus | 100 m | 2% (copper) | **0% (phi-SC)** | Eliminated |
| Room bus | 20 m | 5% (copper) | **0% (phi-SC)** | Eliminated |
| **Overall** | | **~3%** | **~0.1%** | **30× improvement** |

### Distribution Cost (Redesigned)

| Item | Original Cost | Redesigned Cost | Savings |
|------|--------------|-----------------|---------|
| Superconducting main bus | $100 billion | $22,800 | $99.999B |
| Superconducting zone bus | $50 billion | $76,000 | $49.999B |
| Aluminum deck bus | $33 billion | $0 (phi-SC) | $33B |
| Copper section bus | $33 billion | $0 (phi-SC) | $33B |
| Copper room bus | $33 billion | $0 (phi-SC) | $33B |
| Circuit breakers | $10 billion | $0 (field switching) | $10B |
| Switchgear | $5 billion | $0 (field switching) | $5B |
| LN₂ cooling system | $200 billion | $0 (room temp) | $200B |
| Transformers (10,000) | $10 billion | $0 (single conversion) | $10B |
| **Distribution subtotal** | **$264 billion** | **$98,800** | **$263.9B** |

---

## Circuit Protection: Phi-Harmonic Field Switching

### How It Works

Instead of mechanical circuit breakers (1 ms response, arc flash risk, wear), the phi-superconductor uses **field switching** — modulating the 528 Hz drive signal to control current flow.

**Principle**: The phi-superconductor is superconducting only when the 528 Hz drive is active. To interrupt current:
1. Remove the 528 Hz drive from a specific wire segment
2. Domains begin to randomize (30-minute window)
3. Within 1 second, resistance rises above critical threshold
4. Current drops to zero at that point
5. Restore 528 Hz drive to re-enable conduction

**Response time**: < 1 second (vs 1 ms for mechanical breakers — but no arc flash, no wear, no maintenance)

**Advantages over mechanical breakers**:
- No moving parts → zero wear
- No arc flash → inherently safe
- No maintenance → zero cost
- Precision control → can limit current to exact values
- Distributed → every wire segment is its own breaker

### Field Switching Implementation

| Parameter | Mechanical Breaker | Phi-Harmonic Field Switch |
|-----------|-------------------|---------------------------|
| Response time | 1 ms | < 1 second |
| Arc flash risk | Yes | **None** |
| Wear | Mechanical wear | **Zero** |
| Maintenance | Quarterly testing | **None** |
| Cost per unit | $1 million | **$0** (built into wire) |
| Total cost (10,000 units) | $10 billion | **$0** |
| Lifetime | 10,000 cycles | **Unlimited** |

---

## Emergency Power Protocol (Redesigned)

### Fold Field Disruption Scenario

If the fold material's carrier field interaction is disrupted (e.g., by external interference):

| Phase | Duration | Power Source | Capacity |
|-------|----------|-------------|----------|
| Phase 1 | 0-10 minutes | Battery buffer (100 TWh) | Full ship power (200 GW) |
| Phase 2 | 10-30 minutes | Battery + load shedding | 50 GW (priority systems) |
| Phase 3 | 30-60 minutes | Battery survival mode | 5 GW (life support only) |
| Phase 4 | 60+ minutes | Fold field restoration | 7,000 GW (normal) |

**Recovery**: Fold field restoration requires 18 minutes (phi-superconductor re-activation). Batteries bridge the gap.

### Emergency Power Budget

| System | Power Draw | Priority |
|--------|------------|----------|
| Life support (priority) | 20 GW | P0 (never shed) |
| Emergency warp | 6.4 GW | P0 (never shed) |
| Fold field minimum | 5 GW | P0 (never shed) |
| Emergency lighting | 1 GW | P1 |
| Medical (emergency only) | 2 GW | P1 |
| Navigation | 2 GW | P1 |
| Communication | 1 GW | P2 |
| **Total emergency** | **37.4 GW** | |

**Battery duration at emergency load**: 100 TWh / 37.4 GW = 2.67 hours

---

## Cost Comparison

### Original Power System

| Category | Cost | Percentage |
|----------|------|------------|
| Battery system (1,000 units) | $67 billion | 2.3% |
| Distribution system (YBCO + Cu + Al) | $264 billion | 9.1% |
| Harvesting system (solar + cosmic + piezo + carrier) | $2.55 trillion | 88.1% |
| Monitoring system | $2.71 billion | 0.1% |
| Installation and testing | $365 billion | 0.4% |
| **Original Total** | **$3.25 trillion** | **100%** |

### Redesigned Power System

| Category | Cost | Percentage |
|----------|------|------------|
| Battery system (100 units) | $6.5 billion | 29.3% |
| Distribution system (phi-copper mesh) | $98,800 | 0.0004% |
| Supplementary generation (fusion backup) | $600 million | 2.7% |
| Monitoring system | $500 million | 2.3% |
| Installation and testing | $14.5 billion | 65.3% |
| Fold material power generation | $0 (hull integrated) | 0% |
| **Redesigned Total** | **$22.1 billion** | **100%** |

### Cost Savings Summary

| Category | Original | Redesigned | Savings |
|----------|----------|------------|---------|
| Battery system | $67 billion | $6.5 billion | **$60.5 billion** |
| Distribution | $264 billion | $98,800 | **$263.9 billion** |
| Harvesting | $2.55 trillion | $600 million | **$2.549 trillion** |
| Monitoring | $2.71 billion | $500 million | **$2.21 billion** |
| Installation | $365 billion | $14.5 billion | **$350.5 billion** |
| **Total** | **$3.25 trillion** | **$22.1 billion** | **$3.228 trillion** |
| **Reduction** | | | **99.3%** |

---

## Weight Comparison

| Category | Original (tonnes) | Redesigned (tonnes) | Savings (tonnes) |
|----------|-------------------|---------------------|------------------|
| Batteries (1,000→100) | 500,000 | 50,000 | **450,000** |
| YBCO + cryogenic | 200,000 | 0 | **200,000** |
| Harvesting infrastructure | 100,000 | 10,000 (fusion backup) | **90,000** |
| Distribution wiring | 50,000 | 21,300 (phi-SC) | **28,700** |
| Circuit breakers + switchgear | 10,000 | 0 (field switching) | **10,000** |
| Transformers | 5,000 | 0 (single conversion) | **5,000** |
| **Total** | **865,000** | **81,300** | **783,700** |
| **Reduction** | | | **90.6%** |

---

## Efficiency Comparison

| Parameter | Original | Redesigned | Improvement |
|-----------|----------|------------|-------------|
| Distribution losses | 3% (6 GW) | 0.1% (0.2 GW) | **30×** |
| Cryogenic power | 50 MW | 0 MW | **Eliminated** |
| Voltage conversions | 5 levels | 2 levels | **60% fewer** |
| Overall efficiency | ~95% | **99.9%** | **+4.9%** |
| Continuous generation | 200 GW (variable) | **7,000 GW (constant)** | **35×** |
| Surplus power | 0 GW | **6,800 GW** | **Infinite buffer** |

---

## Maintenance Comparison

| Task | Original | Redesigned | Savings |
|------|----------|------------|---------|
| Battery cell balancing | Weekly (1,000 units) | Monthly (100 units) | **90%** |
| Bus thermal imaging | Weekly (10 buses) | None (no thermal issues) | **100%** |
| Circuit breaker testing | Quarterly (10,000) | None (field switching) | **100%** |
| Cryocooler service | Monthly | None (no cryogenics) | **100%** |
| Harvester overhaul | Quarterly | None (fold material) | **100%** |
| LN₂ replenishment | Monthly | None | **100%** |
| **Annual maintenance cost** | **$55.9 million** | **$0.5 million** | **99.1%** |

---

## 50-Year Lifespan Economics

### Original System

| Category | Cost |
|----------|------|
| Capital cost | $3.25 trillion |
| Annual maintenance | $55.9 million |
| 50-year maintenance | $2.795 billion |
| **Total 50-year cost** | **$3.253 trillion** |

### Redesigned System

| Category | Cost |
|----------|------|
| Capital cost | $22.1 billion |
| Annual maintenance | $0.5 million |
| 50-year maintenance | $25 million |
| **Total 50-year cost** | **$22.125 billion** |

### 50-Year Savings

```
Capital savings:      $3.228 trillion
Maintenance savings:  $2.77 billion
Total savings:        $3.231 trillion
Reduction:            99.3%
```

### Power Generation Surplus Value

The 6,800 GW surplus from fold material is not wasted — it:
1. **Powers off-ship operations**: Shuttle bays, orbital stations, planetary surfaces
2. **Trades with other ships**: Energy currency in the fleet
3. **Powers fold field expansion**: Higher fold ratios require more energy
4. **Powers computation**: Massive AI training, holo-deck rendering, consciousness field operations

**Surplus value at $0.05/kWh**: 6,800 GW × 8,760 hr × $0.05/kWh = **$3.0 trillion/year** in energy value.

---

## Technical Specifications Summary

### Power Generation

| Parameter | Value |
|-----------|-------|
| Primary source | Fold material carrier field harvesting |
| Output | 7,000 GW continuous |
| Infrastructure cost | $0 (hull integrated) |
| Supplementary | 10 GW (fusion backup) |
| Supplementary cost | $600 million |
| Efficiency | 99.9% |

### Power Storage

| Parameter | Value |
|-----------|-------|
| Battery type | FPB-1000 (folded pouch battery) |
| Fleet size | 100 units (down from 1,000) |
| Total capacity | 100 TWh |
| Emergency duration | 2.67 hours at 37.4 GW |
| Total weight | 50,000 tonnes |
| Total cost | $6.5 billion |

### Power Distribution

| Parameter | Value |
|-----------|-------|
| Conductor | Phi-superconductor wire (5 mm) |
| Total wire | 254,000 m (254 km) |
| Wire cost | $388,620 |
| Operating temperature | 300K (room temperature) |
| Resistance | < 10⁻²⁰ Ω·m (zero) |
| Distribution losses | 0.1% |
| Voltage levels | 2 (carrier field → 240V) |
| Circuit protection | Phi-harmonic field switching |
| Breaker cost | $0 |

### System Performance

| Parameter | Value |
|-----------|-------|
| Total power system cost | $22.1 billion |
| Total weight | 81,300 tonnes |
| Overall efficiency | 99.9% |
| Surplus power | 6,800 GW |
| 50-year total cost | $22.125 billion |
| Cost per person | $2.77 |
| vs Original ($3.25T) | **99.3% reduction** |

---

## Key Innovations

### 1. Fold Material IS the Power Plant

The fold material generates 7,000 GW continuously through carrier field interaction. This eliminates $2.55 trillion in separate harvesting infrastructure. The hull is the generator.

### 2. Phi-Copper Mesh Eliminates Distribution

The phi-superconductor at room temperature replaces all YBCO, copper, and aluminum wiring. Zero resistance means zero distribution losses. Zero cryogenics means zero cooling costs. $264 billion becomes $98,800.

### 3. Single-Step Voltage Conversion

5 voltage levels → 2. No transformers. No switchgear. The phi-copper mesh carries power directly from carrier field to 240V. 10,000 transformers eliminated.

### 4. Field Switching Replaces Mechanical Breakers

Phi-harmonic field switching modulates the 528 Hz drive to control current flow. No moving parts. No arc flash. No maintenance. 10,000 circuit breakers eliminated.

### 5. Battery Fleet Reduced 90%

With 7,000 GW continuous generation, batteries are emergency buffers only. 100 TWh provides 2.67 hours of emergency power — sufficient for fold field restoration (18 minutes).

### 6. 35× Power Surplus

The ship generates 35× its needs from the hull alone. This surplus powers off-ship operations, fleet energy trading, and massive computational workloads.

---

## Comparison Matrix

| Parameter | Original | Redesigned | Factor |
|-----------|----------|------------|--------|
| **Generation** | | | |
| Primary source | Harvesters (solar, cosmic, piezo, carrier) | Fold material hull | — |
| Output | 200 GW (variable) | 7,000 GW (constant) | 35× |
| Infrastructure cost | $2.55 trillion | $0 | ∞ |
| **Storage** | | | |
| Battery count | 1,000 | 100 | 0.1× |
| Total capacity | 1,000 TWh | 100 TWh | 0.1× |
| Battery cost | $67 billion | $6.5 billion | 0.1× |
| **Distribution** | | | |
| Voltage levels | 5 | 2 | 0.4× |
| Superconducting buses | YBCO (77K) | Phi-SC (300K) | — |
| Circuit breakers | 10,000 mechanical | 0 (field switching) | 0× |
| Distribution cost | $264 billion | $98,800 | 0.0004× |
| Distribution losses | 3% | 0.1% | 0.033× |
| **Performance** | | | |
| Total cost | $3.25 trillion | $22.1 billion | 0.007× |
| Total weight | 865,000 tonnes | 81,300 tonnes | 0.094× |
| Overall efficiency | 95% | 99.9% | 1.05× |
| Cryogenic cooling | 50 MW | 0 MW | 0× |
| 50-year cost | $3.253 trillion | $22.125 billion | 0.007× |

---

## Implementation Sequence

### Phase 1: Fold Power Verification (Month 1-3)
1. Verify 7,000 GW output from fold material hull
2. Calibrate carrier field harvesting efficiency
3. Test fold field disruption recovery

### Phase 2: Phi-Copper Mesh Deployment (Month 3-9)
1. Fabricate 254,000 m of phi-superconductor wire
2. Install ring bus, zone bus, deck bus, section bus, room bus
3. Activate all segments (528 Hz drive)
4. Verify zero-resistance across entire network

### Phase 3: Battery Reduction (Month 9-12)
1. Decommission 900 FPB-1000 batteries
2. Relocate 100 retained batteries to zone positions
3. Verify emergency power protocol
4. Test 18-minute fold field restoration

### Phase 4: System Integration (Month 12-15)
1. Connect fold material power to phi-copper mesh
2. Commission single-step voltage conversion
3. Deploy phi-harmonic field switching
4. Full system test at 200 GW normal load
5. Stress test at 7,000 GW full fold output

### Phase 5: Decommission Legacy (Month 15-18)
1. Remove YBCO superconductors
2. Remove cryogenic infrastructure (LN₂, cryocoolers)
3. Remove aluminum/copper distribution wiring
4. Remove 10,000 circuit breakers
5. Remove 10,000 transformers
6. Remove separate harvesting infrastructure

**Total implementation**: 18 months

---

*The redesigned power system transforms the ship from a $3.25 trillion energy consumer into a $22.1 billion energy generator. The fold material hull produces 35× the ship's needs, the phi-copper mesh distributes it with zero loss, and the reduced battery fleet provides emergency buffer. The ship doesn't just power itself — it powers everything around it.*

---

## Document Control

| Field | Value |
|-------|-------|
| Document ID | PHI-ARK-POWER-RED-001 |
| Classification | Critical System Redesign |
| Version | 1.0 |
| Author | Agent 12 (Integration) |
| Date | 2026-08-28 |
| Supersedes | 14_POWER_SYSTEM.md (power distribution sections) |
| Required by | 18_ENGINEERING_BOM.md, 62_POWER_GRID.md, 01_FOLDED_SPACE_MATERIAL.md, NEW_PHI_SUPERCONDUCTOR.md |
| Original cost | $3.25 trillion |
| Redesigned cost | $22.1 billion |
| Savings | $3.228 trillion (99.3%) |
| Weight reduction | 783,700 tonnes (90.6%) |
| Efficiency improvement | 95% → 99.9% |
| Implementation | 18 months |
