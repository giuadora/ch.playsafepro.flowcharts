# Phase 4: A4 Layout and Typography - Context

**Gathered:** 2026-02-10
**Status:** Ready for planning

<domain>
## Phase Boundary

Reformat the existing draw.io flowchart to fit cleanly on a single DIN A4 portrait page (210x297mm) with professional typography. Same content and logic — no structural changes to the flowchart. Optimized layout, fonts, and visual styling for print.

</domain>

<decisions>
## Implementation Decisions

### Spatial reorganization
- Claude decides the best arrangement to fit A4 portrait — compact vertical, two-column, or hybrid
- The three inspection types (Sichtkontrolle, Funktionskontrolle, Jahreshauptinspektion) must remain as three separate boxes — do not merge them
- Footnotes and legend both stay on the same A4 page (smaller text acceptable)
- PSP Logo placeholder area stays in the layout

### Page structure
- Document title at the top: "Inspektion von Spielplatzgeräten und Spielplatzböden nach SN EN 1176/1177:"
- Title style: ~11-12pt bold (present but not dominating, saves vertical space)
- Footer with version and date (e.g., "v1.1 — 2026")
- Print margins: Claude decides (balance between safety and usable space)

### Typography
- Font family: Helvetica
- Minimum font size: 8pt (for smallest text: footnotes, edge labels)
- Consistent text weight across all node types — no bold/regular differentiation between decisions and process nodes (diamond shape already distinguishes)

### Color and print optimization
- Dual approach: keep color fills AND ensure readability in black & white
- Choose colors with good grayscale contrast so sections remain distinguishable in B&W print
- Edge/arrow lines: medium weight (1.5-2pt) for clear flow visibility
- "Gerät sperren" critical node: same visual treatment as other nodes (no extra emphasis)

### Claude's Discretion
- Exact spatial arrangement strategy (compact vertical vs two-column vs hybrid)
- Print margin sizes
- B&W differentiation approach (grayscale shades, patterns, or other)
- Node sizing and spacing ratios
- How to handle edge label placement at smaller scale
- Loading skeleton for footnotes/legend area compression

</decisions>

<specifics>
## Specific Ideas

- Title text is specifically: "Inspektion von Spielplatzgeräten und Spielplatzböden nach SN EN 1176/1177:"
- Current diagram is 1400x2800px — needs significant compression to fit 210x297mm
- The flowchart has ~30 nodes across 4 color-coded sections (blue/green/yellow/red) plus gray start/end
- 9 footnotes referencing SN EN 1176-7 and CEN/TR 17207 sections — these are legal references and must be preserved exactly

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope

</deferred>

---

*Phase: 04-a4-layout-typography*
*Context gathered: 2026-02-10*
