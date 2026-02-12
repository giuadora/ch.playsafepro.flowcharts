# Roadmap: PSP Inspektions-Flowchart

## Milestones

- ✅ **v1.0 Inspektions-Flowchart** - Phases 1-3 (shipped 2026-02-09)
- ✅ **v1.1 Print-Ready A4** - Phases 4-5 (shipped 2026-02-10)
- ✅ **v1.2 Branding** - Phase 6 (shipped 2026-02-10)
- 🚧 **v2.0 Flowchart Split** - Phases 7-9 (in progress)

## Phases

<details>
<summary>✅ v1.0 Inspektions-Flowchart (Phases 1-3) - SHIPPED 2026-02-09</summary>

### Phase 1: Content Structure
**Goal**: Define complete flowchart content with norm-compliant nodes and edges
**Plans**: 1 plan

Plans:
- [x] 01-01: Design flowchart structure with SN EN 1176-7 coverage

### Phase 2: Mermaid Diagram
**Goal**: Translate content into rendering Mermaid diagram
**Plans**: 2 plans

Plans:
- [x] 02-01: Create Mermaid flowchart with color-coded sections
- [x] 02-02: Add parallel inspection branches and footnotes

### Phase 3: Delivery Package
**Goal**: Build draw.io XML and generate complete delivery package
**Plans**: 1 plan

Plans:
- [x] 03-01: Create draw.io file and SVG export with German README

</details>

<details>
<summary>✅ v1.1 Print-Ready A4 (Phases 4-5) - SHIPPED 2026-02-10</summary>

### Phase 4: A4 Layout
**Goal**: Reformat flowchart to print-ready DIN A4 portrait
**Plans**: 2 plans

Plans:
- [x] 04-01: Reformat draw.io to A4 with Helvetica typography
- [x] 04-02: Simplify post-inspection flow per user feedback

### Phase 5: Project Structure
**Goal**: Rename project for GitHub publishing and regenerate exports
**Plans**: 2 plans

Plans:
- [x] 05-01: Rename project structure for GitHub
- [x] 05-02: Rewrite Mermaid and regenerate A4 SVG export

</details>

<details>
<summary>✅ v1.2 Branding (Phase 6) - SHIPPED 2026-02-10</summary>

### Phase 6: PSP Branding
**Goal**: Integrate PSP corporate branding and create automated verification tooling
**Plans**: 2 plans

Plans:
- [x] 06-01: Add PSP logo, footer, and PDF generation
- [x] 06-02: Create A4 bounds verification tooling

</details>

### 🚧 v2.0 Flowchart Split (In Progress)

**Milestone Goal:** Split the single inspection flowchart into two separate flowcharts (Neuer Spielplatz + Bestehender Spielplatz) with node corrections, renamed inspection types per SN EN 1176-7, updated footnotes, subprocess symbol, and full quality verification.

#### Phase 7: Flowchart Split & File Structure ✓
**Goal**: Create two independent flowcharts from current single file with correct file names and basic structure
**Depends on**: Phase 6
**Requirements**: SPLIT-01, SPLIT-02, SPLIT-03, SPLIT-04, FILE-01
**Completed**: 2026-02-12
**Plans**: 1 plan

Plans:
- [x] 07-01: Split flowchart into two independent draw.io files (FC1 + FC2) with human verification

#### Phase 8: Node Modifications & Norm Compliance ✓
**Goal**: Apply all node changes and ensure complete norm compliance through footnote audit
**Depends on**: Phase 7
**Requirements**: NODE-01, NODE-02, NODE-03, NODE-04, REF-01, REF-02, REF-03
**Completed**: 2026-02-12
**Plans**: 2 plans

Plans:
- [x] 08-01: FC1 node modifications: green installation inspection, subprocess Inspektionsplan, footnote audit
- [x] 08-02: FC2 node modifications: green Bericht archivieren, SN EN 1176-7 inspection terminology, footnote audit

#### Phase 9: Documentation & Quality Verification
**Goal**: Update all documentation and verify both flowcharts pass quality gates
**Depends on**: Phase 8
**Requirements**: DOC-01, DOC-02, DOC-03, FILE-02, FILE-03, QA-01, QA-02, QA-03, QA-04, QA-05, QA-06
**Success Criteria** (what must be TRUE):
  1. Subprocess symbol appears in legend of both flowcharts
  2. Package README describes both flowcharts (Neuer Spielplatz + Bestehender Spielplatz)
  3. Root README updated with new file listing
  4. Each flowchart's "Als PDF herunterladen" QR points to its own PDF
  5. Both flowcharts' "Als Vorlage herunterladen" QR points to shared README
  6. Both flowcharts pass all quality checks (center alignment, connected arrows, margins, no overlaps, footer, branding)
  7. Complete delivery package exists for both flowcharts (.drawio, .svg, .pdf, .md)
**Plans**: 3 plans

Plans:
- [x] 09-01: Legend subprocess symbol, QR code updates, and README updates (DOC-01, DOC-02, DOC-03, FILE-02, FILE-03)
- [x] 09-02: Automated quality checks and visual verification (QA-01 through QA-06)
- [ ] 09-03: Generate SVG and PDF exports for both split flowcharts (gap closure)

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9

| Phase | Milestone | Plans Complete | Status | Completed |
|-------|-----------|----------------|--------|-----------|
| 1. Content Structure | v1.0 | 1/1 | Complete | 2026-02-09 |
| 2. Mermaid Diagram | v1.0 | 2/2 | Complete | 2026-02-09 |
| 3. Delivery Package | v1.0 | 1/1 | Complete | 2026-02-09 |
| 4. A4 Layout | v1.1 | 2/2 | Complete | 2026-02-10 |
| 5. Project Structure | v1.1 | 2/2 | Complete | 2026-02-10 |
| 6. PSP Branding | v1.2 | 2/2 | Complete | 2026-02-10 |
| 7. Flowchart Split & File Structure | v2.0 | 1/1 | Complete | 2026-02-12 |
| 8. Node Modifications & Norm Compliance | v2.0 | 2/2 | Complete | 2026-02-12 |
| 9. Documentation & Quality Verification | v2.0 | 2/3 | Gap closure | - |
