# PHI AI FIRE DRONE — SAFETY PROCEDURES

## Safety Guidelines and AI Fire Protocols

---

## SAFETY RATING

**EXPERIMENTAL AI-ASSISTED FIRE SUPPRESSION DRONE**

AI provides fire spread predictions and drop recommendations. Human operator has final authority on all suppression actions.

---

## GENERAL SAFETY RULES

```
╔════════════════════════════════════════════════════════════════╗
║           SAFETY RULES — PHI AI FIRE DRONE                     ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  FIRE SAFETY:                                                  ║
║  ✓ Never fly directly over active fire                        ║
║  ✓ Maintain safe altitude (minimum 10m above flames)          ║
║  ✓ Monitor battery temperature continuously                   ║
║  ✓ Have escape route planned                                  ║
║  ✓ Coordinate with ground fire crews                          ║
║                                                                ║
║  AI SAFETY:                                                    ║
║  ✓ AI recommendations are ADVISORY only                      ║
║  ✓ Human operator approves all retardant drops               ║
║  ✓ Emergency override always available                        ║
║  ✓ AI cannot autonomously deploy retardant                    ║
║                                                                ║
║  FLIGHT SAFETY:                                                ║
║  ✓ No flight in strong winds (>30 km/h)                      ║
║  ✓ No flight in rain or thunderstorms                         ║
║  ✓ Maintain visual line of sight                              ║
║  ✓ Keep away from people and structures                       ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
```

---

## FIRE OPERATIONS SAFETY

### Safe Operating Distances

| Fire Size | Min Altitude | Min Distance | AI Role |
|-----------|-------------|--------------|---------|
| < 1m² | 5m | 3m | Recommend drop |
| 1-5m² | 8m | 5m | Calculate trajectory |
| 5-20m² | 12m | 8m | Coordinate multiple drones |
| > 20m² | DO NOT ENGAGE | — | Alert fire department |

### AI Emergency Procedures

```
AI EMERGENCY PROTOCOLS:
═══════════════════════════════════════════════════════════════

  IF battery < 20%:
  ├── AI alerts operator
  ├── AI recommends immediate RTB
  └── Retardant system disarmed

  IF AI processor crashes:
  ├── Revert to manual fire fighting
  ├── Thermal readings still available (Arduino direct)
  └── Retardant manual control enabled

  IF fire spreads toward drone:
  ├── AI calculates escape route
  ├── AI recommends altitude change
  └── Operator decides action

  IF retardant system fails:
  ├── AI switches to monitoring mode
  ├── AI continues fire tracking
  └── Operator lands for maintenance
```
