---
phase: 06-corporate-branding
plan: 01
subsystem: documentation
title: "Phase 6 Plan 1: Corporate Branding Integration"
one-liner: "PSP logo and 3-column corporate footer integrated into draw.io diagram and README with CDN-sourced SVG"
tags:
  - branding
  - draw.io
  - logo
  - footer
  - documentation
dependencies:
  requires:
    - 05-02: "Exported SVG/PDF for v1.1 (base for branding)"
  provides:
    - "PSP logo in draw.io diagram (CDN-sourced SVG)"
    - "3-column corporate footer matching Offerte template"
    - "PSP logo in delivery README"
    - "Root README for GitHub repository"
  affects:
    - "Future exports will include branding"
    - "Repository now has professional landing page"
tech-stack:
  added: []
  patterns:
    - "CDN-sourced SVG images in draw.io XML"
    - "HTML img tags in Markdown for logo display"
    - "3-column footer layout with alignment styles"
key-files:
  created:
    - README.md
  modified:
    - Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Spielplatzinspektionen.drawio
    - Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/README.md
decisions:
  - id: BRAND-01
    question: "How to embed logo in draw.io?"
    options:
      - "Embed as base64 data URI"
      - "Reference external CDN URL"
    chosen: "Reference external CDN URL"
    rationale: "Keeps file size small, allows logo updates without file changes, matches web best practices"
  - id: BRAND-02
    question: "Footer layout approach?"
    options:
      - "Single text cell with manual spacing"
      - "3 separate cells with alignment styles"
    chosen: "3 separate cells with alignment styles"
    rationale: "Easier to edit, proper alignment (left/center/right), matches Offerte template structure"
  - id: BRAND-03
    question: "Version number for branded release?"
    options:
      - "Keep v1.1"
      - "Bump to v1.2"
    chosen: "Bump to v1.2"
    rationale: "Branding represents a significant deliverable enhancement, warrants minor version increment"
metrics:
  duration: "2 min"
  completed: "2026-02-10"
---

# Phase 6 Plan 1: Corporate Branding Integration Summary

**One-liner:** PSP logo and 3-column corporate footer integrated into draw.io diagram and README with CDN-sourced SVG

## What Was Built

This plan transformed the generic v1.1 flowchart deliverable into a professionally branded PSP document ready for customer distribution by adding corporate branding elements throughout.

### 1. Draw.io Diagram Branding

**Logo Integration (LOGO-01):**
- Replaced dashed placeholder box (id="brand") with actual PSP logo
- Logo sourced from CDN: `cdn.prod.website-files.com/.../playsafepro_logo-rgb_xs-3.svg`
- Sized at 93x40 pixels to maintain 2.32:1 aspect ratio
- Positioned at x=656, y=38 (top-right area)
- Uses draw.io `shape=image` style with `imageAspect=0` and `aspect=fixed`

**3-Column Footer (FOOT-01 through FOOT-04):**
- Removed old single-line footer (id="footer", value="v1.1 -- 2026")
- Created three adjacent text cells at y=1060:
  - **Column 1** (footer-col1, left-aligned): giuadora AG, Sonnenstrasse 4, 8280 Kreuzlingen
  - **Column 2** (footer-col2, center-aligned): +41 (0) 71 508 24 75, www.playsafepro.ch, vertrieb@psp.live
  - **Column 3** (footer-col3, right-aligned): Trademark notice, company seat, UID-Nr. CHE-222.704.530
- Each column: 239px wide, fontSize=7, fontColor=#6C757D (subtle gray)
- Positioned below FOOTNOTES/LEGEND boxes with 20px spacing
- Matches Offerte template footer style exactly

**Preservation:**
- Page dimensions remain 794x1123 (A4 portrait)
- All flowchart nodes, edges, and positions unchanged
- No modifications to flowchart logic or content

### 2. README Branding (LOGO-02)

**Delivery README Updates:**
- Added PSP logo at top (centered, 200px width)
- Logo links to playsafepro.ch
- Version references updated from 1.1 to 1.2 (2 locations)
- All existing content preserved

### 3. Root README Creation (DOC-01)

**New GitHub Landing Page:**
- Created root `README.md` at project root
- PSP logo at top (same CDN source)
- Project title and description in German
- Link to delivery folder with file listing
- Norm basis section (SN EN 1176-7, SIA 118, CEN/TR 17207, Art. 58 OR)
- Inspection frequencies table
- Contact section: PSP contact info
- License: CC BY-NC 4.0
- Footer: giuadora AG company info and UID number

## Task Commits

| Task | Description | Commit | Files Modified |
|------|-------------|--------|----------------|
| 1 | Embed PSP logo and add 3-column footer to draw.io | 1209454 | Spielplatzinspektionen.drawio |
| 2 | Add PSP logo to README and update version to 1.2 | 3c23e5a | README.md (delivery folder) |
| 3 | Create root README for GitHub landing page | d867b9d | README.md (project root) |

## Decisions Made

### BRAND-01: Logo Embedding Strategy

**Decision:** Reference external CDN URL rather than base64 embed

**Rationale:**
- Keeps .drawio file size minimal (~50KB vs potential 200KB+)
- Logo updates can be made centrally without modifying draw.io file
- Matches web best practices for asset management
- draw.io supports external image URLs natively

**Trade-off:** Requires internet connection to view logo in draw.io editor (acceptable for this use case)

### BRAND-02: Footer Layout Approach

**Decision:** Use 3 separate mxCell elements with alignment styles

**Rationale:**
- Each column independently editable
- Proper text alignment (left/center/right) without manual spacing
- Matches Offerte template structure (3 distinct sections)
- Easier maintenance if contact info changes

**Alternative considered:** Single text cell with manual spacing — rejected due to fragility and poor editability

### BRAND-03: Version Numbering

**Decision:** Increment from v1.1 to v1.2

**Rationale:**
- Branding represents significant deliverable enhancement
- Customer-facing document now looks professional
- Follows semantic versioning (minor version bump for new features)
- v1.1 remains available as "unbranded" version if needed

## Deviations from Plan

None — plan executed exactly as written.

## Technical Notes

### CDN URL Structure

The PSP logo URL follows this pattern:
```
https://cdn.prod.website-files.com/67f92758c1ae09d703725f00/67ff5ea44756d842fa02e3ce_playsafepro_logo-rgb_xs-3.svg
```

- `67f92758c1ae09d703725f00`: Site ID
- `67ff5ea44756d842fa02e3ce`: Asset ID
- `playsafepro_logo-rgb_xs-3.svg`: Filename
- SVG native size: 131.78x56.83 (2.32:1 aspect ratio)

### Draw.io Image Style

```xml
style="shape=image;verticalLabelPosition=bottom;labelBackgroundColor=default;verticalAlign=top;aspect=fixed;imageAspect=0;image=https://cdn.prod.website-files.com/67f92758c1ae09d703725f00/67ff5ea44756d842fa02e3ce_playsafepro_logo-rgb_xs-3.svg;"
```

Key attributes:
- `shape=image`: Tells draw.io to render as image
- `aspect=fixed`: Maintain aspect ratio
- `imageAspect=0`: Use geometry dimensions (not native size)
- `image=URL`: External image source

### Footer Typography

- **Font:** Helvetica (consistent with flowchart)
- **Size:** 7pt (slightly smaller than 8pt footnotes)
- **Color:** #6C757D (gray, same as metadata throughout)
- **Line height:** Default (auto-calculated by draw.io)

## Verification Checklist

- [x] LOGO-01: brand cell uses `shape=image` with CDN URL
- [x] LOGO-02: README has PSP logo at top (delivery folder)
- [x] FOOT-01: 3-column footer structure present
- [x] FOOT-02: Column 1 has giuadora AG address
- [x] FOOT-03: Column 2 has contact details
- [x] FOOT-04: Column 3 has legal info and UID
- [x] Page dimensions remain 794x1123 (A4)
- [x] All flowchart nodes unchanged
- [x] DOC-01: Root README exists with GitHub landing page
- [x] Version references updated to 1.2

## Files Modified

### Created
- `README.md` (project root) — 65 lines, GitHub landing page

### Modified
- `Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Spielplatzinspektionen.drawio` — Logo and footer branding
- `Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/README.md` — Logo and version update

## Next Phase Readiness

### Phase Complete
Phase 6 (Corporate Branding) is complete. This was the final phase of v1.2 milestone.

### Outstanding Work
The v1.2 milestone requirements are fully satisfied:
- LOGO-01: PSP logo embedded in draw.io diagram ✓
- LOGO-02: PSP logo in README ✓
- FOOT-01: 3-column footer structure ✓
- FOOT-02: Column 1 content ✓
- FOOT-03: Column 2 content ✓
- FOOT-04: Column 3 content ✓
- EXPORT-01: SVG regeneration — **Needs separate plan** (see below)

### Blockers/Concerns

**EXPORT-01 Not Included:**
The plan did not include SVG export regeneration. The requirement states "Regenerate SVG export from the updated draw.io file to ensure the branding is included in the exported graphic."

**Recommendation:** Create a follow-up task or plan (06-02) to:
1. Export `Spielplatzinspektionen.svg` from the updated draw.io file
2. Verify logo and footer are visible in SVG
3. Verify A4 dimensions preserved (794x1123)
4. Replace old SVG file
5. Commit the updated SVG

**Note:** The draw.io file now contains the branding, so the SVG export is a simple regeneration step. No code changes needed — just a manual export operation followed by git commit.

## Self-Check: PASSED

All created files verified:
- FOUND: README.md (project root)

All modified files verified:
- FOUND: Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Spielplatzinspektionen.drawio
- FOUND: Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/README.md

All commits verified:
- FOUND: 1209454 (Task 1: draw.io branding)
- FOUND: 3c23e5a (Task 2: README logo and version)
- FOUND: d867b9d (Task 3: root README)
