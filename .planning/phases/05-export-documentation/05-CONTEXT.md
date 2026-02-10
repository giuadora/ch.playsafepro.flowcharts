# Phase 5: Export and Documentation - Context

**Gathered:** 2026-02-10
**Status:** Ready for planning

<domain>
## Phase Boundary

Update all deliverables (SVG, Mermaid, README) to match the A4 layout from Phase 4. Rename folder and files for GitHub publishing. No new flowchart content or structural changes beyond what Phase 4 already established.

</domain>

<decisions>
## Implementation Decisions

### SVG export quality
- Reference system fonts (Helvetica/Arial) — no font embedding
- Optimize for dual use: print (A4) AND web display (GitHub/browser preview)
- Use draw.io's built-in export for SVG generation
- Background/page border handling: Claude's discretion (balance print clarity with web cleanliness)

### Mermaid sync scope
- Sync structure to match Phase 4 changes (simplified post-inspection flow: 10 nodes removed, 3-step linear path)
- Prioritize visual similarity to draw.io layout as closely as Mermaid allows
- Include footnotes in Mermaid source (as notes or comments)
- Must render correctly in GitHub's Mermaid preview — test before shipping

### README content
- Full refresh of entire README to reflect v1.1 changes
- Language: German only
- Update color scheme section to match actual current draw.io colors
- Contact info: E-Mail: info@psp.live, Website: https://www.playsafepro.ch (remove phone line)
- License: CC BY-NC 4.0
- Update version to 1.1

### Folder and file renaming
- Rename delivery folder from `PSP-Inspektions-Flowchart` to `Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden` (hyphenated, no umlauts)
- Rename all files from `Inspektionsablauf.*` to `Spielplatzinspektionen.*` (.drawio, .svg, .md)
- README.md stays as README.md
- Handle as part of this phase (rename first, then generate exports with new names)
- GitHub remote: `https://github.com/giuadora/ch.playsafepro.flowcharts`
- Local project folder name to match repo name

### Claude's Discretion
- SVG background choice (page border vs transparent) for print+web dual use
- README structure and section ordering during full refresh
- Mermaid footnote format (notes vs comments vs subgraph)

</decisions>

<specifics>
## Specific Ideas

- GitHub repo URL is `https://github.com/giuadora/ch.playsafepro.flowcharts` — naming and structure should be professional for public publishing
- File naming `Spielplatzinspektionen` chosen for clarity and brevity
- Folder name avoids umlauts for filesystem/URL compatibility while keeping German terminology

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope

</deferred>

---

*Phase: 05-export-documentation*
*Context gathered: 2026-02-10*
