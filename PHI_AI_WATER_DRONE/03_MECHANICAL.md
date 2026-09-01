# PHI AI WATER DRONE — MECHANICAL DESIGN

## Frame Design (AI-Enhanced)

---

## FRAME OVERVIEW

450mm frame with filtration system and AI processor mounting.

```
FRAME TOP VIEW:
═══════════════════════════════════════════════════════════════

         450mm
  ←─────────────────────→
  ┌──────────────────────┐  ─┬─
  │    ╔══╗        ╔══╗  │   │
  │    ║M1║        ║M2║  │   │
  │    ╚══╝        ╚══╝  │   │
  │   ┌──────────────┐   │   │ 278mm
  │   │   CENTER     │   │   │ (450/phi)
  │   │   BODY       │   │   │
  │   │  ┌────┐      │   │   │
  │   │  │ AI │      │   │   │
  │   │  └────┘      │   │   │
  │   │  ┌────────┐  │   │   │
  │   │  │FILTER  │  │   │   │
  │   │  │SYSTEM  │  │   │   │
  │   │  └────────┘  │   │   │
  │   └──────────────┘   │   │
  │    ╔══╗        ╔══╗  │   │
  │    ║M3║        ║M4║  │   │
  │    ╚══╝        ╚══╝  │   │
  └──────────────────────┘  ─┴─
```

---

## FILTRATION SYSTEM MOUNTING

```
3-STAGE FILTRATION:
═══════════════════════════════════════════════════════════════

  Water In → [Sediment] → [Carbon] → [UV/Sterilize] → Clean Out

  ┌──────────────────────────────────────┐
  │   INTAKE                             │
  │   ┌──────────┐                       │
  │   │ Screen   │ ← Prevents debris    │
  │   └────┬─────┘                       │
  │        │                             │
  │   ┌────┴─────┐                       │
  │   │ STAGE 1  │ ← Sediment filter    │
  │   │ (10μm)   │   Removes particles  │
  │   └────┬─────┘                       │
  │        │                             │
  │   ┌────┴─────┐                       │
  │   │ STAGE 2  │ ← Carbon filter      │
  │   │ (GAC)    │   Removes chemicals  │
  │   └────┬─────┘                       │
  │        │                             │
  │   ┌────┴─────┐                       │
  │   │ STAGE 3  │ ← Polish filter      │
  │   │ (1μm)    │   Final cleaning     │
  │   └────┬─────┘                       │
  │        │                             │
  │   OUTPUT: Clean water                │
  └──────────────────────────────────────┘
```

---

## WEIGHT CHECKLIST

| Component | Target Weight |
|-----------|---------------|
| Frame | 350g |
| Motors (4x) | 220g |
| ESCs (4x) | 80g |
| Propellers (4x) | 50g |
| Battery (FPB-5) | 850g |
| Arduino + sensors | 60g |
| Raspberry Pi + Camera | 15g |
| Filtration System | 200g |
| Water Sensors | 50g |
| Frequency generator | 50g |
| Wiring and hardware | 75g |
| **Total** | **2,000g** |

**Target: Under 2,500g (5.5 lbs)**
