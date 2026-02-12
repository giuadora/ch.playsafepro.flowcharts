---
phase: 07-flowchart-split-file-structure
plan: 01
verified: 2026-02-12T14:30:00Z
status: human_needed
score: 6/6 must-haves verified
human_verification:
  - test: "Visual verification of FC1 (Neuer-Spielplatz.drawio) in draw.io"
    expected: "Flow shows START → Bauabnahme → Inspektion nach Installation → Maengel? → Spielplatz eroeffnen → Inspektionsplan erstellen → Inspektionszyklus beginnen. NO inspection branches. Content centered on A4."
    why_human: "Draw.io visual rendering, layout quality, and flow clarity require human verification"
  - test: "Visual verification of FC2 (Bestehender-Spielplatz.drawio) in draw.io"
    expected: "Flow shows Inspektionszyklus beginnen → three inspection branches → Inspektionsbericht → Bericht archivieren/IHM → Naechster Inspektionszyklus → loop back. NO new playground nodes. Dashed loop-back arrow visible. Content centered on A4."
    why_human: "Draw.io visual rendering, layout quality, loop-back edge visibility, and flow clarity require human verification"
  - test: "A4 fit verification"
    expected: "Both flowcharts fit on A4 page without overflow when opened in draw.io"
    why_human: "Page overflow detection requires visual inspection in draw.io"
---

# Phase 07: Flowchart Split & File Structure Verification Report

**Phase Goal:** Create two independent flowcharts from current single file with correct file names and basic structure

**Verified:** 2026-02-12T14:30:00Z

**Status:** human_needed

**Re-verification:** No — initial verification

## Goal Achievement

### Observable Truths

| #   | Truth                                                                                                                                                                       | Status      | Evidence                                                                    |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | --------------------------------------------------------------------------- |
| 1   | FC1 (Neuer-Spielplatz.drawio) opens in draw.io and shows only the new playground commissioning path from Neuer Spielplatz through Inspektionszyklus beginnen               | ✓ VERIFIED  | File exists, valid XML, contains nodes START, N01, N02, D02, N03, N04, IPLAN, E00 only |
| 2   | FC2 (Bestehender-Spielplatz.drawio) opens in draw.io and shows only the ongoing inspection cycle from Inspektionszyklus beginnen looping back via Naechster Inspektionszyklus | ✓ VERIFIED  | File exists, valid XML, contains nodes E00, E01, E02, E03, E04, P01, IHM, END, NOTE only, loop-back edge verified |
| 3   | FC1 has no inspection branch nodes (E01, E02, E03) and no post-inspection nodes (P01, IHM, END)                                                                             | ✓ VERIFIED  | Grep confirmed E01, E02, E03, P01, IHM, END, NOTE absent from FC1           |
| 4   | FC2 has no new-playground nodes (N01, N02, D02, N03, N04, IPLAN) and no decision diamond D01                                                                                | ✓ VERIFIED  | Grep confirmed START, D01, N01, N02, D02, N03, N04, IPLAN absent from FC2   |
| 5   | Both flowcharts display a subline below the main title — Neuer Spielplatz on FC1, Bestehender Spielplatz on FC2                                                            | ✓ VERIFIED  | FC1 contains "Neuer Spielplatz", FC2 contains "Bestehender Spielplatz", diagram names set correctly |
| 6   | Both flowcharts retain PSP logo and 3-column footer from v1.2                                                                                                               | ✓ VERIFIED  | Both files contain brand, footer-col1, footer-col2, footer-col3 cells       |

**Score:** 6/6 truths verified

### Required Artifacts

| Artifact | Expected | Status | Details |
| -------- | -------- | ------ | ------- |
| `Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Neuer-Spielplatz.drawio` | FC1 new playground commissioning flowchart | ✓ VERIFIED | File exists (19,485 bytes), valid XML, contains "Neuer Spielplatz", diagram name set to "Neuer Spielplatz" |
| `Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Bestehender-Spielplatz.drawio` | FC2 ongoing inspection cycle flowchart | ✓ VERIFIED | File exists (21,674 bytes), valid XML, contains "Bestehender Spielplatz", diagram name set to "Bestehender Spielplatz" |

**Artifact Details:**

**FC1 (Neuer-Spielplatz.drawio):**
- **Exists:** ✓ Yes (19,485 bytes, modified 2026-02-12 13:01)
- **Substantive:** ✓ Valid XML with 108 lines of content
- **Wired:** ✓ Contains FC1 nodes (START, N01, N02, D02, N03, N04, IPLAN, E00)
- **Content exclusions:** ✓ No FC2 nodes (E01, E02, E03, E04, P01, IHM, END, NOTE, D01 all absent)
- **Branding:** ✓ brand, footer-col1, footer-col2, footer-col3 present
- **Footnotes:** ✓ Contains footnotes 1-2 only (SIA 118, SN EN 1176-7 6.1a)
- **Page dimensions:** ✓ A4 portrait (794x1123)

**FC2 (Bestehender-Spielplatz.drawio):**
- **Exists:** ✓ Yes (21,674 bytes, modified 2026-02-12 13:06)
- **Substantive:** ✓ Valid XML with 136 lines of content
- **Wired:** ✓ Contains FC2 nodes (E00, E01, E02, E03, E04, P01, IHM, END, NOTE)
- **Content exclusions:** ✓ No FC1 nodes (START, D01, N01, N02, D02, N03, N04, IPLAN all absent)
- **Branding:** ✓ brand, footer-col1, footer-col2, footer-col3 present
- **Footnotes:** ✓ Contains footnotes 3-8 only (SN EN 1176-7 6.1b/c/d, 8.2.2, 6.2.4, CEN/TR 17207)
- **Page dimensions:** ✓ A4 portrait (794x1123)

### Key Link Verification

| From | To | Via | Status | Details |
| ---- | -- | --- | ------ | ------- |
| Neuer-Spielplatz.drawio | node E00 | FC1 terminal node — Inspektionszyklus beginnen is the endpoint | ✓ WIRED | E00 cell with value "Inspektionszyklus beginnen" found in FC1 |
| Bestehender-Spielplatz.drawio | node END | FC2 loop-back — END loops back to E00 conceptually | ✓ WIRED | Loop-back edge (eLOOP) with source="END" target="E00" dashed=1 found in FC2 |

### Requirements Coverage

Phase 7 Requirements from REQUIREMENTS.md:

| Requirement | Status | Evidence |
| ----------- | ------ | -------- |
| SPLIT-01: Single flowchart split into two separate draw.io files | ✓ SATISFIED | Neuer-Spielplatz.drawio and Bestehender-Spielplatz.drawio both exist and valid |
| SPLIT-02: FC1 starts at "Neuer Spielplatz" and ends at "Inspektionszyklus beginnen" | ✓ SATISFIED | FC1 contains START node and E00 terminal node with "Inspektionszyklus beginnen" |
| SPLIT-03: FC2 starts at "Inspektionszyklus beginnen" and loops back via "Nächster Inspektionszyklus" | ✓ SATISFIED | FC2 E00 start node verified, loop-back edge from END to E00 verified |
| SPLIT-04: Both flowcharts have subline below main title | ✓ SATISFIED | "Neuer Spielplatz" in FC1, "Bestehender Spielplatz" in FC2 verified |
| FILE-01: Files renamed to distinguish flows | ✓ SATISFIED | Files named Neuer-Spielplatz.drawio and Bestehender-Spielplatz.drawio |

**Score:** 5/5 requirements satisfied

### Anti-Patterns Found

None detected.

**Checked:**
- TODO/FIXME/placeholder comments: None found in either file
- Empty implementations: N/A (draw.io XML structure)
- Console.log stubs: N/A (draw.io XML structure)

### Human Verification Required

#### 1. Visual verification of FC1 (Neuer-Spielplatz.drawio) in draw.io

**Test:** Open Neuer-Spielplatz.drawio in draw.io (app.diagrams.net or desktop app). Verify:
- Title reads "Inspektion von Spielplatzgeraeten..." with "Neuer Spielplatz" subtitle in blue
- Flow shows: START → Bauabnahme → Inspektion nach Installation → Maengel? → (loop or) Spielplatz eroeffnen → Inspektionsplan erstellen → Inspektionszyklus beginnen
- NO inspection branch nodes (Sichtkontrolle, Funktionskontrolle, Jahreshauptinspektion) appear
- PSP logo in top-right and 3-column footer at bottom
- Footnotes show only footnotes 1 and 2
- Content is reasonably centered on the A4 page

**Expected:** Flow displays correctly with proper layout, no missing nodes, no extra nodes, subtitle visible in blue

**Why human:** Draw.io rendering quality, visual layout, color verification, and content centering require human eyes. XML structure verification cannot confirm visual appearance.

#### 2. Visual verification of FC2 (Bestehender-Spielplatz.drawio) in draw.io

**Test:** Open Bestehender-Spielplatz.drawio in draw.io. Verify:
- Title reads "Inspektion von Spielplatzgeraeten..." with "Bestehender Spielplatz" subtitle in green
- Flow shows: Inspektionszyklus beginnen → three inspection branches (weekly/quarterly/yearly) → Inspektionsbericht → Bericht archivieren / Instandhaltungs-Management → Naechster Inspektionszyklus → (loop back with dashed arrow)
- NO new playground nodes (Bauabnahme, Inspektion nach Installation, Maengel decision) appear
- PSP logo in top-right and 3-column footer at bottom
- Footnotes show only footnotes 3-8
- Content is reasonably centered on the A4 page
- Dashed loop-back arrow from END to E00 is visible and clear

**Expected:** Flow displays correctly with proper layout, no missing nodes, no extra nodes, subtitle visible in green, loop-back edge clearly visible

**Why human:** Draw.io rendering quality, visual layout, color verification, dashed edge visibility, and content centering require human eyes. XML structure verification cannot confirm visual appearance and edge routing quality.

#### 3. A4 fit verification

**Test:** For both flowcharts, check that all content fits within the A4 page bounds (no overflow, no scrolling required to see nodes/edges)

**Expected:** Both flowcharts fit completely on A4 page without overflow

**Why human:** Page overflow and visual fit can only be assessed in draw.io with page view enabled

### Summary

**All automated checks passed.** Both flowcharts:
- Exist with correct file names
- Are valid draw.io XML
- Contain correct node sets (FC1: new playground path only, FC2: inspection cycle only)
- Have correct content exclusions (no overlap between flows)
- Have distinct subtitles ("Neuer Spielplatz" vs "Bestehender Spielplatz")
- Retain PSP branding (logo, 3-column footer)
- Have filtered footnotes (1-2 for FC1, 3-8 for FC2)
- Use A4 portrait dimensions (794x1123)
- Have been committed to git (0e7fab2 for FC1, f523bc9 for FC2)
- FC2 has loop-back edge from END to E00

**Human verification required** for:
1. Visual quality and layout in draw.io
2. Subtitle color rendering (blue for FC1, green for FC2)
3. Loop-back edge visibility and routing in FC2
4. Content centering and A4 page fit

**Phase goal achieved pending human verification.** All programmatically verifiable truths confirmed. Visual verification in draw.io (Task 3 checkpoint) documented in SUMMARY as approved by user, but should be re-confirmed if not already done.

---

_Verified: 2026-02-12T14:30:00Z_
_Verifier: Claude (gsd-verifier)_
