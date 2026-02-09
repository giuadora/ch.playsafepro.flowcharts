# Phase 3: Export & Distribution - Context

**Gathered:** 2026-02-09
**Status:** Ready for planning

<domain>
## Phase Boundary

Research export formats and produce editable deliverables from the existing Mermaid flowchart. Customers receive files they can import into draw.io or Visio and modify. The Mermaid diagram content and logic are fixed from Phase 2 — this phase focuses on conversion and packaging.

</domain>

<decisions>
## Implementation Decisions

### Format priorities
- Primary format: draw.io (.drawio) — gold standard deliverable
- Secondary format: SVG — for print/web/fallback use
- Mermaid source (.md) included as bonus for tech-savvy customers
- Primary use case is customer editing, not just viewing
- Customers use both draw.io and Visio — draw.io chosen because it's also importable into Visio

### Editability depth
- Full editing: customers must be able to move, resize, recolor, delete, and add nodes
- Connections (arrows) must be linked to nodes — arrows follow when nodes are dragged
- Footnotes and legend entries are individual editable elements, not grouped blocks
- Include a style library/templates so new nodes automatically match existing styling (colors, fonts, shapes)

### Delivery packaging
- Deliverable is a folder containing: draw.io file, SVG, Mermaid source, and README
- German naming convention: folder "PSP-Inspektions-Flowchart/" with files like Inspektionsablauf.drawio, Inspektionsablauf.svg
- README in German — matches diagram language for Swiss/German customers
- README explains how to open and edit the files

### Styling fidelity
- Colors: improved palette — Claude refines colors for better print/screen quality while keeping the same semantic meaning (blue=new, green=inspection, yellow=post, red=critical)
- Shapes: use draw.io's native flowchart shapes — may differ slightly from Mermaid but more polished
- Layout: top-to-bottom flow direction matching the Mermaid structure
- Include a branding area (header/corner) with space for PSP logo — customer can add their own

### Claude's Discretion
- Exact hex values for the improved color palette
- draw.io XML structure and connector routing
- SVG generation method (Mermaid CLI, draw.io export, or manual)
- README content and structure
- Exact file naming within German naming convention
- Style library implementation approach in draw.io

</decisions>

<specifics>
## Specific Ideas

- draw.io file must be a true native diagram (XML with individual shapes and connectors), not an embedded image
- Visio compatibility via draw.io import path — no need for a separate .vsdx file
- Branding area should be easy for the customer to customize with their own logo

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope

</deferred>

---

*Phase: 03-export-distribution*
*Context gathered: 2026-02-09*
