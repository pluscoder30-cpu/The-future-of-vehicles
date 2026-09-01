# FTL Vehicle Documentation Fixes — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Fix critical documentation gaps across all FTL vehicles: missing parts list, FPB battery substitution notes, warp system BOM entries, and BOM subtotal mismatches.

**Architecture:** Create missing documentation files, add standardized notes across 6 FTL vehicles, add estimated costs for integrated warp components, and correct all BOM grand totals.

**Tech Stack:** Markdown documentation

**Complexity Target:** Documentation updates across 6 vehicle directories with consistent formatting

---

## Files to Modify/Create

| Vehicle | Files to Modify | Files to Create |
|---------|----------------|-----------------|
| PHI_FTL_SHUTTLE | 02_FPB100_BATTERY.md | 01_PARTS_LIST.md |
| PHI_FTL_FREIGHT | 10_COMPLETE_BOM.md, 01_PARTS_LIST.md | — |
| PHI_FTL_CAR | 10_COMPLETE_BOM.md, 01_PARTS_LIST.md | — |
| PHI_FTL_TRUCK | 10_COMPLETE_BOM.md, 01_PARTS_LIST.md | — |
| PHI_FTL_VAN | 10_COMPLETE_BOM.md, 01_PARTS_LIST.md | — |
| PHI_FTL_CARGO_TRUCK | 10_COMPLETE_BOM.md, 01_PARTS_LIST.md | — |

---

## Task 1: Create PHI_FTL_SHUTTLE 01_PARTS_LIST.md

**Files:**
- Create: `PHI_FTL_SHUTTLE/01_PARTS_LIST.md`

**Content:** Full BOM based on existing vehicle specs (4× FPB-100, warp coils, structural, electrical, passenger systems)

---

## Task 2: Add FPB Battery Substitution Notes

**Files:**
- Modify: `PHI_FTL_SHUTTLE/02_FPB100_BATTERY.md`
- Modify: `PHI_FTL_FREIGHT/01_PARTS_LIST.md`
- Modify: `PHI_FTL_CAR/01_PARTS_LIST.md`
- Modify: `PHI_FTL_TRUCK/01_PARTS_LIST.md`
- Modify: `PHI_FTL_VAN/01_PARTS_LIST.md`
- Modify: `PHI_FTL_CARGO_TRUCK/01_PARTS_LIST.md`

**Standard Note:**
```
> **FPB Substitution Note:** FPB (Field Plasma Battery) is a phi-harmonic energy storage device. For build purposes, substitute with: [LiFePO4 battery pack equivalent voltage/capacity]. The phi-harmonic enhancement provides 2× energy density but is not required for basic operation.
```

---

## Task 3: Add Warp System BOM Costs

**Files:** All 10_COMPLETE_BOM.md and 01_PARTS_LIST.md files

**Estimated Costs (per unit):**
| Component | Unit Cost |
|-----------|-----------|
| Warp coil array (per coil) | $2,500 |
| Resonance stabilizer | $3,500 |
| Dimensional tuner | $4,000 |
| Field emitter node (per node) | $800 |
| Navigation display (HUD) | $2,200 |

---

## Task 4: Fix BOM Subtotal Mismatches

**Actual Calculated Totals vs Listed Grand Totals:**

| Vehicle | Calculated | Listed | Delta |
|---------|------------|--------|-------|
| PHI_FTL_FREIGHT | $37,007 | $25,000 | +$12,007 |
| PHI_FTL_CAR | $17,750 | $12,000 | +$5,750 |
| PHI_FTL_TRUCK | $22,261 | $15,000 | +$7,261 |
| PHI_FTL_VAN | $19,560 | $14,000 | +$5,560 |
| PHI_FTL_CARGO_TRUCK | $28,362 | $20,000 | +$8,362 |

**Resolution:** Update GRAND TOTAL rows to match sum of subtotals.

---

## Task 5: Add Warp Costs to Parts Lists

**Files:** All 01_PARTS_LIST.md files

Update "Source" column from "Integrated" to show estimated costs.

---

## Verification

After all changes:
1. Verify each 10_COMPLETE_BOM.md grand total matches sum of subtotals
2. Verify each 01_PARTS_LIST.md has FPB substitution note
3. Verify PHI_FTL_SHUTTLE has 01_PARTS_LIST.md
4. Verify warp system components have estimated costs
