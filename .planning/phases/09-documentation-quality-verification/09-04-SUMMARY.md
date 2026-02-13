---
phase: 09-documentation-quality-verification
plan: 04
subsystem: svg-export, mermaid-diagrams
tags: [gap-closure, uat, subprocess-rendering, mermaid-syntax]
dependency-graph:
  requires: [09-03-gap-closure]
  provides: [corrected-subprocess-rendering, mermaid-subprocess-syntax]
  affects: [FC1-exports, FC2-exports, uat-results]
tech-stack:
  added: []
  patterns: [vertical-line-subprocess-border, mermaid-subprocess-syntax]
key-files:
  created: []
  modified:
    - Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Neuer-Spielplatz.svg
    - Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Bestehender-Spielplatz.svg
    - Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Neuer-Spielplatz.pdf
    - Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Bestehender-Spielplatz.pdf
    - Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Neuer-Spielplatz.md
    - Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Bestehender-Spielplatz.md
decisions: []
metrics:
  duration: 113s
  completed: 2026-02-13T08:09:25Z
---

# Phase 9 Plan 4: UAT Gap Closure for Subprocess Rendering and Mermaid Syntax Summary

**One-liner:** Fixed subprocess double-border rendering in SVGs using vertical lines and corrected Mermaid subprocess node syntax.

## What Was Delivered

**Objective:** Close the final two UAT failures by (1) fixing subprocess double-border rendering in SVG exports to use vertical lines instead of inner rectangles, and (2) adding subprocess `[["text"]]` syntax to Mermaid nodes matching draw.io `shape=process` designations.

**Output:** All 7 UAT tests now pass with corrected SVG subprocess rendering and Mermaid subprocess syntax.

## Tasks Completed

### Task 1: Fix subprocess double-border in both SVGs and regenerate PDFs
**Commit:** 77a14f6
- Fixed Neuer-Spielplatz.svg IPLAN node: replaced inner rect with two vertical lines at x=307 and x=487
- Fixed Bestehender-Spielplatz.svg IHM node: replaced inner rect with two vertical lines at x=327 and x=467
- Vertical lines are 10px inset from left/right edges, spanning full node height
- Regenerated both PDFs from corrected SVGs
- Pattern matches reference Spielplatzinspektionen.svg subprocess rendering

### Task 2: Fix Mermaid subprocess syntax for IPLAN and IHM nodes
**Commit:** 6d458ce
- Neuer-Spielplatz.md: Changed IPLAN from `["text"]` to `[["text"]]` subprocess syntax
- Bestehender-Spielplatz.md: Changed IHM from `["text"]` to `[["text"]]` subprocess syntax
- Only these two nodes changed (matching draw.io shape=process attribute)
- Both Mermaid files remain valid with proper code blocks

## Deviations from Plan

None - plan executed exactly as written.

## Verification Results

All verification steps passed:
- Both SVG subprocess nodes use vertical `<line>` elements (not inner `<rect>`)
- Both Mermaid subprocess nodes use `[["text"]]` syntax
- Both PDFs regenerated successfully (126K and 137K, both > 50KB)
- Both SVGs are valid XML (parsed successfully)
- No regressions: all other nodes, edges, footnotes, legends, QR codes, and footer content unchanged
- UAT Test 1 (FC1 SVG Export Visual Match): subprocess double-border on IPLAN renders correctly with vertical lines
- UAT Test 5 (Mermaid Flowcharts): IPLAN uses `[["text"]]` in FC1 Mermaid, IHM uses `[["text"]]` in FC2 Mermaid

## Success Criteria Met

- [x] Both SVG subprocess nodes render with two vertical lines (10px inset from left/right edges, full height)
- [x] Both Mermaid subprocess nodes use `[["text"]]` syntax matching draw.io `shape=process` attribute
- [x] Both PDFs regenerated from corrected SVGs with file size > 50KB
- [x] All SVGs are valid XML
- [x] No regressions on other flowchart elements
- [x] All 7 UAT tests pass (closed final two gaps)

## Files Modified

**SVG Exports (4 files):**
- Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Neuer-Spielplatz.svg
- Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Bestehender-Spielplatz.svg
- Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Neuer-Spielplatz.pdf
- Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Bestehender-Spielplatz.pdf

**Mermaid Diagrams (2 files):**
- Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Neuer-Spielplatz.md
- Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Bestehender-Spielplatz.md

## Technical Notes

**Subprocess Double-Border Rendering Pattern:**
The correct subprocess rendering (matching reference Spielplatzinspektionen.svg) uses two vertical `<line>` elements instead of an inner rectangle:
- Lines positioned 10px inset from left and right edges of outer rectangle
- Lines span full height of outer rectangle
- Example: outer rect x=297, width=200 → left line at x=307, right line at x=487

**Mermaid Subprocess Syntax:**
Mermaid uses `[["text"]]` syntax for subprocess nodes (matching Flowchart.js "subroutine" type). Only nodes with `shape=process` in draw.io sources should use this syntax.

## Dependencies

**Required:**
- 09-03-gap-closure (SVG and Mermaid files existed from previous plan)

**Provides:**
- Corrected subprocess rendering for both flowcharts
- Mermaid subprocess syntax matching draw.io structure
- Complete UAT pass (all 7 tests)

## Impact

**Immediate:**
- UAT Test 1 now passes (subprocess rendering correct)
- UAT Test 5 now passes (Mermaid subprocess syntax correct)
- v2.0 Flowchart Split milestone fully validated and ready for release

**Future:**
- Establishes subprocess rendering pattern for future flowchart exports
- Mermaid syntax conventions documented for consistency

## Self-Check: PASSED

**Created files:**
None (all modifications)

**Modified files verified:**
- [FOUND] Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Neuer-Spielplatz.svg
- [FOUND] Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Bestehender-Spielplatz.svg
- [FOUND] Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Neuer-Spielplatz.pdf
- [FOUND] Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Bestehender-Spielplatz.pdf
- [FOUND] Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Neuer-Spielplatz.md
- [FOUND] Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Bestehender-Spielplatz.md

**Commits verified:**
- [FOUND] 77a14f6: fix(09-04): replace inner rect with vertical lines for subprocess double-border
- [FOUND] 6d458ce: fix(09-04): add subprocess syntax to IPLAN and IHM Mermaid nodes
