---
phase: 04-a4-layout-typography
plan: 01
subsystem: diagram-layout
tags: [drawio, A4, layout, spatial-reorganization]
requires: [03-02]
provides: [a4-page-setup, compact-layout]
affects: [04-02, 05-01]
tech-stack:
  added: []
  patterns: [compact-flowchart-layout]
key-files:
  created: []
  modified:
    - PSP-Inspektions-Flowchart/Inspektionsablauf.drawio
decisions:
  - id: DEC-04-01-001
    what: A4 portrait page dimensions
    why: DIN A4 (210x297mm) is standard print format in Europe
    alternatives: [A4 landscape, Letter format]
    chosen: A4 portrait at 794x1123px (96 DPI)
  - id: DEC-04-01-002
    what: Compression strategy - manual repositioning vs proportional scaling
    why: Manual repositioning allows optimal readability at smaller scale; proportional scaling would create awkward spacing
    alternatives: [proportional-scale, auto-layout]
    chosen: Manual repositioning with ~0.5x horizontal, ~0.35x vertical compression
  - id: DEC-04-01-003
    what: Node sizing for minimum readability
    why: Text must remain readable when printed; 8-10pt font requires nodes sized 100-120px wide
    alternatives: [smaller-nodes, multi-page]
    chosen: 100-120px wide boxes with 8-10pt text
metrics:
  duration: 368s
  completed: 2026-02-10
---

# Phase 04 Plan 01: A4 page setup and spatial reorganization Summary

**One-liner:** Reformatted flowchart from 1400x2800px to DIN A4 portrait (794x1123px) with complete node repositioning and compact layout.

## What Was Built

**Objective:** Reformat the existing draw.io flowchart to fit on a single DIN A4 portrait page with all content visible.

**Deliverables:**
- A4 page dimensions set (210x297mm = 794x1123px at 96 DPI)
- Title added at top: "Inspektion von Spielplatzgeraeten und Spielplatzboeden nach SN EN 1176/1177:"
- Footer added at bottom: "v1.1 -- 2026"
- Logo placeholder repositioned to top-right (100x40px)
- All ~30 flowchart nodes repositioned within A4 boundaries
- Compact vertical layout: START at y=85 to END at y=930 (bottom=965)
- Footnotes and legend positioned at bottom (y=985, bottom=1075)
- All edges updated with simplified routing

**Spatial reorganization:**
- Compression ratios: ~0.5x horizontal, ~0.35x vertical from original 1400x2800px layout
- Node sizes reduced: standard boxes 100-120x40-55px, decisions 100-110x50-70px
- Font sizes reduced to 8-10pt for compact readability
- Three inspection types (E01, E02, E03) maintained as separate boxes per user decision
- "Gerät sperren" (P04) uses standard styling (no bold) per user decision

## Task Commits

| Task | Commit | Description | Files Modified |
|------|--------|-------------|----------------|
| 1 | 5070cbe | Set A4 page dimensions and add title/footer | Inspektionsablauf.drawio |
| 2 | e6538c4 | Reposition and resize all flowchart nodes for A4 | Inspektionsablauf.drawio |

## Key Technical Details

**Layout strategy:**
- Usable area with 10mm margins: 718x1047px (x: 38-756, y: 38-1085)
- Vertical sections:
  - Title area: y=38-80
  - START and decision fork: y=85-210
  - New playground path (left): y=240-505
  - Inspektionszyklus beginnen: y=525-560
  - Three inspection branches: y=590-645 (spread horizontally)
  - Post-inspection linear chain: y=665-965
  - Footnotes and legend: y=985-1075

**Edge routing:**
- Removed most explicit waypoint arrays for cleaner auto-routing
- Kept waypoints only for:
  - Long "Bestehender Spielplatz" route (e3)
  - "Nachbesserung" loop-back (e8)
  - "Nein: Wiedervorlage" loop-back (e32)
  - Complex multi-target routes from D04 (e23, e24, e26)

**Node count:** 26 flowchart nodes + 3 metadata elements (title, footer, brand) + 2 info boxes (footnotes, legend) = 31 total elements

## Decisions Made

See frontmatter for decision IDs DEC-04-01-001 through DEC-04-01-003.

Key decision: Manual repositioning chosen over proportional scaling to maintain optimal readability at the smaller A4 scale. Proportional scaling would have created awkward spacing and potentially illegible text.

## Deviations from Plan

None - plan executed exactly as written.

## Next Phase Readiness

**Blocks:** None

**Enables:**
- Phase 04 Plan 02: Typography and print-optimized colors can proceed
- Phase 05 Plan 01: SVG export will reflect new A4 layout

**Open Questions:** None

**Risks:** None identified

## Performance Notes

**Duration:** 368 seconds (6.1 minutes)

**Complexity factors:**
- 26 flowchart nodes required manual repositioning
- 32 edges needed routing updates
- Multiple iterations to compress layout within A4 boundaries
- Careful verification of all coordinates within margins

## Self-Check: PASSED

**Files created:** None (plan only modified existing file)

**Files modified:**
- PSP-Inspektions-Flowchart/Inspektionsablauf.drawio ✓ exists

**Commits:**
- 5070cbe ✓ exists
- e6538c4 ✓ exists

**Verification results:**
- Page dimensions: 794x1123 ✓
- All nodes within bounds (38-756 x 38-1085) ✓
- Three inspection types as separate boxes ✓
- All 32 edges reference valid node IDs ✓
- No overlapping nodes ✓
- Title, footer, logo present ✓
