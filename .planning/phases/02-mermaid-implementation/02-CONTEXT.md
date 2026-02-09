# Phase 2: Mermaid Implementation - Context

**Gathered:** 2026-02-09
**Status:** Ready for planning

<domain>
## Phase Boundary

Translate the structured flowchart content from Phase 1 (flowchart-content.md: 29 nodes, 31 edges, 9 footnotes, shape legend) into valid, fully styled Mermaid diagram syntax. The diagram must render without errors, use correct German SN EN 1176-7 terminology, and be self-contained (footnotes + legend inside the diagram) for export in Phase 3.

</domain>

<decisions>
## Implementation Decisions

### Diagram direction & layout
- **Top-to-bottom (TD)** flow direction
- **One continuous diagram** — no subgraphs for sectioning. The parallel inspection branches are the only visual grouping (side-by-side columns)
- **Node labels: title + brief context** — e.g. "Jahreshauptinspektion<br/>durch zertifizierte Fachperson". Not full Phase 1 descriptions, not bare titles
- **Loops must be clearly visible** — labeled back-arrows for defect→fix→re-inspect and unresolved defects→next cycle. Reader must immediately see where the process circles back

### Footnote presentation
- **Superscript notation** on node labels — e.g. "Bauabnahme nach SIA 118¹"
- **Footnotes as a styled Mermaid node/box** at the bottom of the diagram — they must export with the diagram (not separate Markdown below the code block)
- This ensures the complete diagram (flow + footnotes) travels as one unit when exported to SVG/draw.io in Phase 3

### Legend presentation
- **Legend inside the Mermaid diagram** as a styled visual element — same rationale as footnotes: everything exports together as one self-contained image
- Legend explains: node shapes (rectangle, diamond, rounded-rect, parallelogram) and color zones

### Parallel branch rendering
- **Side-by-side columns** — three branches spread horizontally, each flowing down, merging at "Inspektionsbericht erstellen"
- **Single merge node** — one "Inspektionsbericht erstellen" node that all three flow into
- **Edge labels show frequency:**
  - Sichtkontrolle → "wöchentlich"
  - Funktionskontrolle → "pro Quartal"
  - Jahreshauptinspektion → "jährlich"

### Terminology renaming (user decision)
- "Visuelle Routineinspektion" → **Sichtkontrolle**
- "Operative Inspektion" → **Funktionskontrolle**
- "Jährliche Hauptinspektion" → **Jahreshauptinspektion**
- Original norm terms (SN EN 1176-7, 6.1 b/c/d) stay in the footnotes with the official names

### Color & styling
- **Fully styled in Mermaid** — custom CSS classes for each color zone, professional appearance. The Mermaid output itself should look finished
- **PSP brand colors** — extract palette from playsafepro.ch. Reference existing flowchart (existing-playground-flowchart.md) which uses Bootstrap-style alert colors:
  - Yellow/gold (#fff3cd / #856404) — action items
  - Red (#f8d7da / #721c24) — urgent/critical
  - Green (#d4edda / #155724) — OK/complete
  - Blue/teal (#d1ecf1 / #0c5460) — start nodes
  - Lavender/indigo (#e2e3f1 / #383d6e) — link/transition nodes
- Researcher should verify these match the playsafepro.ch website palette and adjust if needed
- **Neutral edges** — all arrows in dark grey/black. Color is only on nodes, not on arrows
- Phase 1 color zones map to: blue=new playground path, green=inspection nodes, yellow/orange=defects/actions, red=critical lockout (Gerät sperren), grey=start/end

### Claude's Discretion
- Exact hex values if website colors diverge from existing flowchart palette
- How to implement superscript in Mermaid (HTML entities, Unicode, or bracket notation — depends on renderer compatibility)
- Footnote box styling and layout within diagram
- Legend box styling and placement
- How to force side-by-side rendering of three inspection branches in Mermaid TD mode
- Node ID naming scheme
- Line break placement within labels for readability

</decisions>

<specifics>
## Specific Ideas

- Existing flowchart (existing-playground-flowchart.md) already uses Mermaid with classDef styling — use as a reference for syntax patterns and color approach
- The existing flowchart uses Bootstrap-style alert colors — maintain consistency since both flowcharts may be used together by PSP customers
- Diagram must be self-contained: flow + footnote box + legend box = one exportable unit
- All three inspection branches must have frequency edge labels: "wöchentlich", "pro Quartal", "jährlich"

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope

</deferred>

---

*Phase: 02-mermaid-implementation*
*Context gathered: 2026-02-09*
