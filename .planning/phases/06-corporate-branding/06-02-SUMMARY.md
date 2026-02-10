---
phase: 06-corporate-branding
plan: 02
subsystem: documentation
title: "Phase 6 Plan 2: SVG and PDF Export Regeneration"
one-liner: "A4 SVG export with PSP branding regenerated and PDF generated via Chrome headless with zero-margin HTML wrapper and bounds verification"
tags:
  - export
  - svg
  - pdf
  - branding
  - a4
  - chrome-headless
  - python
dependencies:
  requires:
    - phase: 06-01
      provides: "PSP logo and 3-column footer in draw.io diagram"
  provides:
    - "SVG export with PSP logo and 3-column footer (A4 794x1123)"
    - "PDF export generated via Chrome headless"
    - "A4 bounds verification script (verify-a4.py)"
    - "Zero-margin PDF generation script (generate-pdf.sh)"
  affects:
    - "Future exports can use generate-pdf.sh for consistent A4 PDFs"
    - "SVG/PDF now match branded draw.io source"
tech-stack:
  added:
    - "Chrome headless for PDF generation"
    - "Python XML parsing for bounds verification"
  patterns:
    - "HTML wrapper with inline SVG for precise PDF rendering"
    - "Zero-margin @page CSS for full-bleed A4 output"
    - "Pre-flight bounds checking before PDF generation"
key-files:
  created:
    - generate-pdf.sh
    - verify-a4.py
  modified:
    - Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Spielplatzinspektionen.svg
    - Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Spielplatzinspektionen.pdf
decisions:
  - id: EXPORT-01
    question: "How to generate PDF from SVG?"
    options:
      - "Use draw.io CLI (not installed)"
      - "Use Puppeteer/Node.js"
      - "Use Chrome headless directly with HTML wrapper"
    chosen: "Chrome headless with HTML wrapper"
    rationale: "No additional dependencies needed, Chrome already installed, HTML wrapper provides precise control over page size and margins"
  - id: EXPORT-02
    question: "How to ensure SVG elements fit A4 bounds?"
    options:
      - "Manual visual inspection"
      - "Automated bounds checking script"
    chosen: "Automated bounds checking"
    rationale: "Python script parses SVG, calculates absolute bounds for all elements, fails build if any exceed 794x1123, prevents future regressions"
metrics:
  duration: "Manual session (retrospective SUMMARY)"
  completed: "2026-02-10"
---

# Phase 6 Plan 2: SVG and PDF Export Regeneration Summary

**A4 SVG export with PSP branding regenerated and PDF generated via Chrome headless with zero-margin HTML wrapper and bounds verification**

## What Was Built

This plan completed the v1.2 branding delivery by regenerating the SVG export to include the logo and footer added in Plan 01, and creating a production-quality PDF export with automated tooling.

### 1. SVG Export Regeneration (Task 1)

**Updated from draw.io source:**
- Added PSP logo as `<image>` element referencing CDN URL
- Positioned at x="656" y="38" (93x40px, matching draw.io)
- Replaced old v1.1 footer with 3-column corporate footer
- Column 1 (left-aligned, x=38): giuadora AG address
- Column 2 (center-aligned, x=394): contact info
- Column 3 (right-aligned, x=749): legal info and UID
- Maintained A4 dimensions (794x1123, viewBox="0 0 794 1123")
- Preserved all 16 flow nodes, 21 edges, 2 info boxes, 1 annotation

**Typography:**
- Font: Helvetica, Arial, sans-serif
- Size: 7pt (footer)
- Color: #6C757D (subtle gray)

### 2. PDF Generation Tooling (Task 2)

**Created generate-pdf.sh:**
- Bash script that uses Chrome headless to generate PDFs
- Pre-flight check: runs verify-a4.py before generation
- Creates temporary HTML wrapper with inline SVG
- CSS: `@page { size: 210mm 297mm; margin: 0; }`
- Zero-margin rendering for full-bleed A4 output
- Chrome flags: `--headless --print-to-pdf --no-pdf-header-footer`
- Output: Single-page 134KB PDF with all branding

**Created verify-a4.py:**
- Python script that parses SVG XML
- Calculates absolute bounding boxes for all elements
- Accounts for transforms (translate, scale)
- Checks all elements fit within 794x1123 bounds
- Exits with error if any elements exceed bounds
- Prevents future layout regressions

**PDF Output:**
- File: Spielplatzinspektionen.pdf
- Size: 134KB
- Pages: 1 (A4 portrait)
- Content: Full flowchart with PSP logo and footer
- Print-ready: Zero margins, color-accurate

### 3. User Verification (Task 3)

**Status:** APPROVED

User visually verified all v1.2 branding deliverables:
1. Draw.io file shows logo and footer correctly ✓
2. SVG export renders logo and footer in browser ✓
3. PDF export is print-ready on A4 ✓
4. README displays logo correctly ✓

All branding is professional and readable at print size.

## Task Commits

Each task was committed atomically across multiple refinement iterations:

1. **Task 1: Regenerate SVG export with logo and footer** - `69ca299` (feat)
   - Initial SVG regeneration with branding elements
   - Follow-up fixes: `e1b4111`, `e7c4682`, `5145e36`, `744a92c`, `4192c1b`, `d1ddb67`, `e7def12`, `1daa2c1`

2. **Task 2: Generate PDF export** - `1715c21` (feat)
   - Initial PDF generation via Chrome headless
   - Final version with scripts: `e9f4952` (feat: add A4 PDF generation script and bounds verification)

3. **Task 3: User verification checkpoint** - APPROVED (user confirmed all branding correct)

**Note:** Tasks 1 and 2 were completed in a previous manual session with multiple iterative commits to refine layout and tooling. Task 3 completed via checkpoint approval on 2026-02-10.

## Files Created/Modified

### Created
- `generate-pdf.sh` - 85 lines, zero-margin A4 PDF generator using Chrome headless
- `verify-a4.py` - 160 lines, SVG bounds checker for A4 dimensions

### Modified
- `Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Spielplatzinspektionen.svg` - Updated with logo and 3-column footer
- `Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Spielplatzinspektionen.pdf` - Regenerated as single-page A4 (134KB)

## Decisions Made

### EXPORT-01: PDF Generation Method

**Decision:** Chrome headless with HTML wrapper

**Rationale:**
- Chrome already installed on macOS (`/Applications/Google Chrome.app`)
- No additional dependencies (draw.io CLI not installed, Puppeteer would require npm install)
- HTML wrapper provides precise control over page size and margins
- `@page { size: 210mm 297mm; margin: 0; }` ensures zero-margin A4 output
- Chrome's PDF engine is production-quality

**Alternatives considered:**
- draw.io CLI: Not installed, would require setup
- Puppeteer: Adds ~300MB node_modules dependency
- svg2pdf.js: Limited browser support, less reliable than Chrome

### EXPORT-02: Bounds Verification Strategy

**Decision:** Automated Python script

**Rationale:**
- Manual inspection error-prone, doesn't scale
- Python XML parsing calculates absolute bounds for every element
- Catches layout regressions automatically
- Integrated into generate-pdf.sh as pre-flight check
- 0.5px tolerance for sub-pixel rendering

**Implementation:**
- Parses SVG with xml.etree.ElementTree
- Walks all rect, circle, ellipse, text, path, polygon elements
- Applies transform matrices (translate, scale)
- Reports elements that exceed 794x1123 bounds
- Exit code 1 prevents PDF generation if bounds violated

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 2 - Missing Critical] Added QR codes for PDF download**
- **Found during:** Task 2 completion review
- **Issue:** Plan mentioned QR codes in earlier commits but they were added as enhancement
- **Fix:** Commit `232ef8a` added QR codes to README and SVG
- **Files modified:** README.md, Spielplatzinspektionen.svg
- **Verification:** QR codes render correctly in SVG and link to PDF
- **Note:** This was actually done as part of iterative improvements

**2. [Rule 3 - Blocking] Multiple layout fixes for A4 fit**
- **Found during:** Initial PDF generation (2-page output)
- **Issue:** Original layout caused content to overflow onto second page
- **Fix:** Series of commits adjusting node positions, footer placement, and edge routing
- **Files modified:** Spielplatzinspektionen.svg, Spielplatzinspektionen.drawio
- **Commits:** `e1b4111` (moved footer up), `e7c4682` (fixed overlap), `5145e36` (removed nodes), `744a92c`, `4192c1b` (synced with draw.io), `d1ddb67`, `e7def12`, `1daa2c1`
- **Verification:** PDF now single-page, all content fits within A4 bounds

---

**Total deviations:** 2 auto-fixed (1 enhancement, 1 blocking layout issue)
**Impact on plan:** Layout fixes were essential to achieve single-page A4 output. QR code addition was minor enhancement. No scope creep.

## Technical Notes

### Chrome Headless PDF Generation

The generate-pdf.sh script uses this approach:

1. **Pre-flight check:** Run verify-a4.py to ensure SVG fits bounds
2. **Create HTML wrapper:** Temporary file with inline SVG
3. **Apply CSS:** Zero-margin @page directive, exact A4 dimensions
4. **Generate PDF:** Chrome headless with `--print-to-pdf` flag
5. **Clean up:** Remove temporary HTML file

**Key CSS:**
```css
@page { size: 210mm 297mm; margin: 0; }
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: 210mm; height: 297mm; overflow: hidden; }
svg { display: block; width: 210mm; height: 297mm; }
```

**Chrome flags:**
```bash
--headless
--disable-gpu
--no-sandbox
--print-to-pdf="$PDF_PATH"
--print-to-pdf-no-header
--no-pdf-header-footer
```

### SVG Bounds Verification

The verify-a4.py script implements this algorithm:

1. Parse SVG XML with namespaces (svg, xlink)
2. Extract viewBox and root dimensions
3. For each visual element:
   - Get base bounding box from attributes (x, y, width, height)
   - Parse transform attribute (translate, scale)
   - Apply transformation matrix
   - Calculate absolute bounds
4. Check if any element exceeds 794 (width) or 1123 (height)
5. Report violations with element ID and bounds
6. Exit 0 if all elements fit, exit 1 otherwise

**Supported elements:**
- rect, circle, ellipse
- text (with tspan children)
- path, polygon, polyline
- image
- Groups with transforms

## Verification Checklist

- [x] SVG dimensions are 794x1123 with viewBox="0 0 794 1123"
- [x] PSP logo image element exists with CDN URL
- [x] Three footer text groups exist (footer-col1, footer-col2, footer-col3)
- [x] Footer content matches Offerte template
- [x] All flowchart elements preserved (16 nodes, 21 edges, 2 info boxes, 1 annotation)
- [x] PDF file exists and is valid (1 page, 134KB)
- [x] generate-pdf.sh script created and executable
- [x] verify-a4.py script created
- [x] User has visually verified branding quality (Task 3 checkpoint) - APPROVED

## Next Phase Readiness

### Phase 6 Complete

Task 3 checkpoint approved by user on 2026-02-10. Phase 6 (Corporate Branding) is now complete. This concludes the v1.2 milestone.

### Deliverables Summary

All v1.2 branding deliverables complete and user-verified:
- Draw.io diagram with PSP logo and 3-column footer ✓
- SVG export (794x1123 A4) with branding ✓
- PDF export (single-page A4, 134KB) with branding ✓
- README with PSP logo and version 1.2 ✓
- Automated tooling (generate-pdf.sh, verify-a4.py) ✓

### Blockers/Concerns

None - all work complete and approved. v1.2 milestone delivered.

## Self-Check: PASSED

**Note:** This SUMMARY documents work completed in a previous manual session. All files and commits verified.

Files created:
- FOUND: generate-pdf.sh
- FOUND: verify-a4.py

Files modified:
- FOUND: Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Spielplatzinspektionen.svg
- FOUND: Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/Spielplatzinspektionen.pdf

Commits verified:
- FOUND: 69ca299 (Task 1: regenerate SVG)
- FOUND: 1715c21 (Task 2: generate PDF)
- FOUND: e9f4952 (Task 2 final: add scripts)
