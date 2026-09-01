# PHI GARBAGE DRONE — CONTROL SYSTEM

## Avionics and Autonomy

---

## FLIGHT MODES

| Mode | Description | Speed |
|------|-------------|-------|
| COLLECT | Hover and pick | 0 km/h |
| PATROL | Grid search | 15 km/h |
| SORT | Sort collected items | 0 km/h |
| RTH | Return home | 20 km/h |

---

## COLLECTION AUTONOMY

```
AUTO-COLLECTION MISSION:
═══════════════════════════════════════════════════════════════

  1. Navigate to littered area
  2. Scan with camera for trash
  3. For each trash item:
     a. Approach item
     b. Apply sorting frequencies
     c. Activate robotic arm
     d. Pick up item
     e. Identify material
     f. Sort into correct bin
  4. When bins full, return to base
  5. Deposit sorted materials
  6. Return to area
```

---

## SAFETY INTERLOCKS

| Interlock | Condition | Action |
|-----------|-----------|--------|
| Sharp detected | Metal + shape | Skip item |
| Heavy item | > 200g | Skip item |
| Battery < 30% | Low voltage | Return to base |
| Bins full | All > 80% | Return to base |
| Arm jam | Stall detected | Release and retry |
