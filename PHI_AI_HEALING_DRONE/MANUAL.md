# PHI AI HEALING DRONE — Operations Manual

## AI-Powered Medical Drone Operations

---

## WHAT IS THE PHI AI HEALING DRONE?

The PHI AI Healing Drone is a flying robot with AI that helps sick people! It can fly to someone who needs help, use its camera and sensors to figure out what's wrong, recommend the right treatment, and deliver medicine. It costs less than $350 to build!

```
 ┌──────────────────────────────────────────────────────┐
 │              PHI AI HEALING DRONE                     │
 │                                                       │
 │           ╔══╗              ╔══╗                      │
 │           ║M1║              ║M2║                      │
 │           ╚══╝              ╚══╝                      │
 │                                                       │
 │     ╔══════════════════════════════════╗              │
 │     ║                                  ║              │
 │     ║    ┌────────────────────────┐    ║              │
 │     ║    │    AI + MEDICAL        │    ║              │
 │     ║    │  Camera: sees wounds   │    ║              │
 │     ║    │  AI: figures out help  │    ║              │
 │     ║    │  Meds: delivers pills  │    ║              │
 │     ║    │  Freq: healing sounds  │    ║              │
 │     ║    └────────────────────────┘    ║              │
 │     ║                                  ║              │
 │     ╚══════════════════════════════════╝              │
 │                                                       │
 │           ╔══╗              ╔══╗                      │
 │           ║M3║              ║M4║                      │
 │           ╚══╝              ╚══╝                      │
 │                                                       │
 │  Cost: $348   Weight: 1.9 kg   Flies: 4 hours       │
 │  AI: Raspberry Pi Zero 2W + Camera                   │
 └──────────────────────────────────────────────────────┘
```

### How Does It Help People?

The drone has FOUR ways to help:

1. **SEES INJURIES** — AI camera looks at wounds and figures out what happened
2. **CHECKS VITAL SIGNS** — Measures heart rate, blood oxygen, and temperature
3. **RECOMMENDS TREATMENT** — AI suggests the best way to help
4. **DELIVERS MEDICINE** — Flies bandages, pills, and cream to patients

**IMPORTANT: The AI only suggests — a human always decides!**

---

## How to Use the AI Features

### Starting an AI Mission

```
AI MISSION START:
═══════════════════════════════════════════════════════════════

  1. Turn on the drone
  2. Wait for AI to boot (blue LED on Pi Zero)
  3. Connect phone to drone WiFi
  4. Open drone app
  5. Type patient location
  6. Press "AI DIAGNOSE" button
  7. Drone flies to patient
  8. AI camera looks at patient
  9. AI checks vital signs
  10. AI suggests what to do
  11. You approve or change the plan
  12. Drone does the approved treatment
```

### What the AI Sees

```
AI DIAGNOSIS SCREEN:
═══════════════════════════════════════════════════════════════

  ┌──────────────────────────────────────┐
  │  AI IS LOOKING...                    │
  │                                      │
  │  Camera sees: Small cut on arm       │
  │  AI thinks: Minor wound (87% sure)   │
  │                                      │
  │  Vitals:                             │
  │  Heart: 75 BPM (normal)             │
  │  Oxygen: 98% (normal)               │
  │  Temp: 98.6°F (normal)              │
  │                                      │
  │  AI SAYS: "Apply bandage + play     │
  │  432Hz healing sound for 5 min"     │
  │                                      │
  │  Your choice:                        │
  │  [APPROVE] [CHANGE] [DO NOTHING]    │
  │                                      │
  └──────────────────────────────────────┘
```

### Overriding the AI

```
HUMAN OVERRIDE:
═══════════════════════════════════════════════════════════════

  You can ALWAYS override the AI:

  In the app:
  ├── "OVERRIDE AI" button
  ├── "MANUAL MODE" button
  └── "EMERGENCY STOP" button

  On the controller:
  ├── Switch to "MANUAL" mode
  └── Hold emergency button 3 seconds

  Remember: The AI is your helper, not your boss!
```

---

## Safety Rules

```
╔═══════════════════════════════════════════════════════════╗
║            AI DRONE SAFETY RULES                          ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  AI SAFETY:                                               ║
║  ✓ AI only SUGGESTS — you DECIDE                        ║
║  ✓ Always check what the AI recommends                   ║
║  ✓ If something seems wrong, override the AI            ║
║  ✓ AI can make mistakes — trust your judgment           ║
║                                                           ║
║  DRONE SAFETY:                                            ║
║  ✓ Have an adult help you build and fly                  ║
║  ✓ Fly in open fields (no people nearby)                 ║
║  ✓ Check the weather before flying                       ║
║  ✓ Keep propellers away from everyone                    ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

---

## Quick Reference Card

```
╔═══════════════════════════════════════════════════╗
║   PHI AI HEALING DRONE — QUICK CARD              ║
╠═══════════════════════════════════════════════════╣
║                                                   ║
║  STARTUP:                                         ║
║  1. Turn on battery                               ║
║  2. Wait for AI blue LED (10 seconds)            ║
║  3. Connect phone to WiFi                         ║
║  4. Open drone app                                ║
║  5. Press "ARM" to start motors                   ║
║  6. Press "AI DIAGNOSE" to fly to patient         ║
║                                                   ║
║  AI MISSION:                                      ║
║  1. Type patient location                         ║
║  2. Press "AI DIAGNOSE"                           ║
║  3. Wait for AI assessment (30 seconds)           ║
║  4. Read AI recommendation                        ║
║  5. Press "APPROVE" or "OVERRIDE"                 ║
║  6. Watch drone treat patient                     ║
║                                                   ║
║  OVERRIDING AI:                                   ║
║  • Press "OVERRIDE AI" anytime                    ║
║  • Switch to "MANUAL MODE"                        ║
║  • Hold emergency button 3 seconds                ║
║                                                   ║
║  LIMITS:                                          ║
║  • Max speed: 40 km/h (22 mph)                   ║
║  • Max height: 120m (400 ft)                     ║
║  • Flight time: 4 hours                          ║
║  • Max payload: 500g (1.1 lbs)                   ║
║  • AI accuracy: ~85% (always double-check!)      ║
║                                                   ║
╚═══════════════════════════════════════════════════╝
```

---

## Congratulations!

You built a medical drone with AI! It can fly to sick people, look at their injuries with a camera, figure out what's wrong, recommend treatment, check their heart rate and temperature, and deliver medicine. The AI makes it smarter, but YOU are always in charge.

**Now go help someone!**

---

*This manual was written for builders age 12 and up, with adult supervision. Always follow local drone regulations. Never fly without proper training. Safety is YOUR responsibility. The AI is a tool — you are the decision maker.*
