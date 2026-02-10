# Roadmap: PSP Inspektions-Flowchart

## Milestones

- v1.0 Inspektions-Flowchart - Phases 1-3 (shipped 2026-02-09)
- v1.1 Print-Ready A4 - Phases 4-5 (in progress)

## Phases

<details>
<summary>v1.0 Inspektions-Flowchart (Phases 1-3) - SHIPPED 2026-02-09</summary>

See .planning/MILESTONES.md for v1.0 details.

Phases 1-3 completed: Content structure, Mermaid diagram, draw.io/SVG exports with delivery package.

</details>

### v1.1 Print-Ready A4 (In Progress)

**Milestone Goal:** Optimize the existing flowchart for professional DIN A4 portrait printout -- same content, polished layout and typography, regenerated exports.

- [ ] **Phase 4: A4 Layout and Typography** - Reformat draw.io diagram to fit single A4 portrait page with professional fonts
- [ ] **Phase 5: Export and Documentation** - Regenerate SVG, update Mermaid source, update README

## Phase Details

### Phase 4: A4 Layout and Typography
**Goal**: Flowchart prints cleanly on a single DIN A4 portrait page with professional, readable typography
**Depends on**: Phase 3 (v1 delivery complete)
**Requirements**: LAYOUT-01, LAYOUT-02, LAYOUT-03, TYPO-01
**Success Criteria** (what must be TRUE):
  1. draw.io page dimensions are set to 210 x 297 mm (DIN A4 portrait)
  2. All flowchart nodes, edges, and footnotes are visible within the page area -- nothing is clipped or overflows
  3. All text uses a consistent professional sans-serif font (Helvetica or Arial family)
  4. Flowchart is readable when printed at 100% scale on A4 paper -- no text too small, no overlapping elements
**Plans**: 2 plans

Plans:
- [ ] 04-01-PLAN.md -- A4 page setup and spatial reorganization of all nodes
- [ ] 04-02-PLAN.md -- Typography, print-optimized colors, and visual verification

### Phase 5: Export and Documentation
**Goal**: All deliverables (SVG, Mermaid, README) are updated to match the new A4 layout
**Depends on**: Phase 4
**Requirements**: EXPORT-01, EXPORT-02, DOC-01
**Success Criteria** (what must be TRUE):
  1. SVG export matches the current draw.io layout exactly (same nodes, same arrangement, same fonts)
  2. Mermaid source reflects any structural changes made during layout reorganization
  3. README documents the A4 print-ready format and any new usage instructions
**Plans**: TBD

Plans:
- [ ] 05-01: TBD

## Progress

**Execution Order:** Phase 4 then Phase 5

| Phase | Milestone | Plans Complete | Status | Completed |
|-------|-----------|----------------|--------|-----------|
| 1-3 | v1.0 | 4/4 | Complete | 2026-02-09 |
| 4. A4 Layout and Typography | v1.1 | 0/2 | Not started | - |
| 5. Export and Documentation | v1.1 | 0/TBD | Not started | - |
