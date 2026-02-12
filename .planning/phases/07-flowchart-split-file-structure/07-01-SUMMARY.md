---
phase: 07-flowchart-split-file-structure
plan: 01
subsystem: documentation
tags: [drawio, flowchart, xml, documentation, split]

# Dependency graph
requires:
  - phase: 06-corporate-branding
    provides: PSP logo and 3-column footer template
provides:
  - Two independent draw.io flowcharts split by entry path
  - FC1: Neuer-Spielplatz.drawio (new playground commissioning path)
  - FC2: Bestehender-Spielplatz.drawio (ongoing inspection cycle path)
  - Proper subtitle differentiation for each flowchart
  - Footnote filtering (1-2 for FC1, 3-8 for FC2)
affects: [08-node-enhancements, 09-quality-verification]

# Tech tracking
tech-stack:
  added: []
  patterns: [two-file flowchart structure, subtitle differentiation, path-specific footnotes]

key-files:
  created:
    - Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Neuer-Spielplatz.drawio
    - Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Bestehender-Spielplatz.drawio
  modified: []

key-decisions:
  - "Split single flowchart with two entry paths into two focused flowcharts for clarity"
  - "Retained original footnote numbering (3-8 in FC2) rather than renumbering to maintain consistency with node superscripts"
  - "Kept full legend in FC1 despite removing inspection nodes - E00 endpoint is green-styled"
  - "Added dashed loop-back edge in FC2 from END to E00 to emphasize cyclic nature"

patterns-established:
  - "Two-flowchart structure: FC1 for new playground commissioning, FC2 for ongoing inspections"
  - "Subtitle differentiation: blue for FC1 (Neuer Spielplatz), green for FC2 (Bestehender Spielplatz)"
  - "Path-specific footnote filtering while preserving original numbering"

# Metrics
duration: 1 day
completed: 2026-02-12
---

# Phase 07 Plan 01: Flowchart Split & File Structure Summary

**Split single flowchart into two focused draw.io files - FC1 (new playground commissioning) and FC2 (ongoing inspection cycle) with path-specific content, subtitles, and footnotes**

## Performance

- **Duration:** 1 day
- **Started:** 2026-02-12T13:00:00Z
- **Completed:** 2026-02-12T12:22:20Z
- **Tasks:** 3 (2 auto + 1 human-verify checkpoint)
- **Files modified:** 2 created

## Accomplishments
- Created FC1 (Neuer-Spielplatz.drawio) with only new playground commissioning path (START → N01 → N02 → D02 → N03/N04 → IPLAN → E00)
- Created FC2 (Bestehender-Spielplatz.drawio) with only inspection cycle path (E00 → E01/E02/E03 → E04 → P01/IHM → END with loop-back)
- Added distinct subtitles: "Neuer Spielplatz" (blue) for FC1, "Bestehender Spielplatz" (green) for FC2
- Filtered footnotes to show only relevant references (1-2 for FC1, 3-8 for FC2)
- Retained PSP corporate branding (logo, 3-column footer) in both flowcharts
- Both flowcharts verified in draw.io and approved by user

## Task Commits

Each task was committed atomically:

1. **Task 1: Create FC1 Neuer-Spielplatz.drawio from source** - `0e7fab2` (feat)
2. **Task 2: Create FC2 Bestehender-Spielplatz.drawio from source** - `f523bc9` (feat)
3. **Task 3: Verify both flowcharts in draw.io** - No file changes (checkpoint approval)

## Files Created/Modified
- `/Users/jean-pierrekoenig/Documents/Projects/ch.playsafepro.flowcharts/Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Neuer-Spielplatz.drawio` - New playground commissioning flowchart with START through E00 endpoint
- `/Users/jean-pierrekoenig/Documents/Projects/ch.playsafepro.flowcharts/Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Bestehender-Spielplatz.drawio` - Ongoing inspection cycle flowchart with E00 start and loop-back to E00

## Decisions Made
- **Retained original footnote numbering:** FC2 keeps footnotes numbered 3-8 (not renumbered to 1-6) to maintain consistency with existing superscripts on nodes. Renumbering deferred to Phase 9 if needed.
- **Kept full legend in FC1:** Despite removing inspection branch nodes (E01-E03), the legend entry "(Gruen) = Inspektionen" was retained because E00 (Inspektionszyklus beginnen) is green-styled and represents the transition to inspections.
- **Added loop-back edge in FC2:** Inserted a dashed gray edge from END back to E00 to visually emphasize the cyclic nature of ongoing inspections.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

Both flowcharts are ready for Phase 8 (node enhancements):
- FC1 and FC2 have clean, focused content
- Corporate branding (PSP logo, footer) is present in both files
- Footnotes are filtered correctly
- Both files are valid draw.io XML with A4 dimensions
- User has visually verified and approved both flowcharts

No blockers for Phase 8 node modifications (adding REF-01/REF-02/REF-03 footnotes, updating references).

## Self-Check: PASSED

**Files created:**
- FOUND: Neuer-Spielplatz.drawio
- FOUND: Bestehender-Spielplatz.drawio

**Commits verified:**
- FOUND: 0e7fab2 (Task 1 - FC1 creation)
- FOUND: f523bc9 (Task 2 - FC2 creation)

All claims in this summary have been verified.
