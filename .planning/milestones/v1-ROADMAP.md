# Milestone v1: PSP Inspektions-Flowchart

**Status:** SHIPPED 2026-02-09
**Phases:** 1-3
**Total Plans:** 4

## Overview

This roadmap delivered a single German-language flowchart showing playground inspection obligations per SN EN 1176-7. Phase 1 defined the flowchart content and structure as structured text. Phase 2 translated that content into valid, rendering Mermaid syntax. Phase 3 researched export options and produced editable formats for customer handover.

## Phases

### Phase 1: Content & Logic

**Goal**: Define the complete flowchart content and logic structure as structured text

**Depends on**: Nothing (first phase)

**Requirements**: FLOW-01, FLOW-02, FLOW-03, FLOW-04, NEW-03, NEW-04, NEW-05, NEW-06, INSP-01, INSP-02, INSP-03, INSP-04, INSP-05, POST-01, POST-02, POST-03, POST-04, POST-05, POST-06, POST-07, POST-08

**Success Criteria** (what must be TRUE):
  1. Two entry paths (Neuer Spielplatz and Bestehender Spielplatz) are defined with all required nodes
  2. New playground path starts at Bauabnahme (SIA 118) and Inspektion nach Installation (begins at installation, not earlier planning steps), with defects routing back to builder before opening
  3. Existing playground path shows three parallel inspection branches (visuell, operativ, Hauptinspektion) that merge into documentation flow
  4. Post-inspection process includes documentation, archiving, defect processing with safety-critical split (Geraet sperren), Massnahmenkatalog, decision flow, and loop back to inspections
  5. All norm references (SN EN 1176-7 clauses, SIA 118, Art. 58 OR) are collected as numbered footnotes

**Plans**: 1 plan

Plans:
- [x] 01-01-PLAN.md — Create complete flowchart content structure with nodes, edges, footnotes, and legend

**Completed:** 2026-02-09

### Phase 2: Mermaid Implementation

**Goal**: Translate structured flowchart content into valid Mermaid diagram syntax

**Depends on**: Phase 1

**Requirements**: FMT-01, FMT-02, FMT-03, FMT-04

**Success Criteria** (what must be TRUE):
  1. Mermaid diagram renders without errors in standard Mermaid viewers
  2. All German terminology from SN EN 1176-7 is correctly used (Inspektion nach Installation, Bauabnahme, Hauptinspektion, etc.)
  3. Diagram structure is clear enough for a visual designer to recreate without playground safety expertise
  4. No emojis or special characters that break Mermaid rendering

**Plans**: 1 plan

Plans:
- [x] 02-01-PLAN.md — Create complete Mermaid flowchart with nodes, edges, styling, footnotes, and legend

**Completed:** 2026-02-09

### Phase 3: Export & Distribution

**Goal**: Research export formats and produce editable deliverables customers can import into their preferred tools (Visio, draw.io, etc.)

**Depends on**: Phase 2

**Requirements**: EXP-01, EXP-02, EXP-03, EXP-04

**Success Criteria** (what must be TRUE):
  1. Export format options are researched and documented with pros/cons for each
  2. SVG export is generated for print/web use
  3. draw.io (.drawio) export is generated as an editable format
  4. At least one format is confirmed importable into Visio for customer use

**Plans**: 2 plans

Plans:
- [x] 03-01-PLAN.md — Build native draw.io XML file with all nodes, edges, styling, branding, and style library
- [x] 03-02-PLAN.md — Generate SVG, copy Mermaid source, write German README, assemble delivery folder

**Completed:** 2026-02-09

## Progress

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Content & Logic | 1/1 | Complete | 2026-02-09 |
| 2. Mermaid Implementation | 1/1 | Complete | 2026-02-09 |
| 3. Export & Distribution | 2/2 | Complete | 2026-02-09 |

## Milestone Summary

**Key Decisions:**
- Fork-join pattern for parallel inspection branches (clear entry/exit points)
- Parallelogram shape for document nodes (visual distinction)
- Color coding: blue=new, green=inspection, yellow=post, red=critical
- Dotted arrows for loop-back edges (visual distinction for cycles)
- Footnotes/legend as orphan Mermaid nodes (self-contained exportable diagram)
- Improved color palette for draw.io (better print/screen quality)
- Individual text elements for footnotes/legend (enable customer editing)
- SVG parallelogram polygons with 4 points (true skewed rectangles)

**Issues Resolved:**
- SVG parallelogram shapes rendered as hexagons instead of true parallelograms (fixed with 4-point polygons)
- SVG arrow connections not targeting correct node centers after shape fix (corrected)

**Issues Deferred:**
- None

**Technical Debt Incurred:**
- preview-flowchart.html dev artifact in project root (can be removed)
- existing-playground-flowchart.md orphaned pre-project reference file
- README.md contact placeholders not filled (E-Mail, Telefon, Website)

---

_For current project status, see .planning/PROJECT.md_
_Archived: 2026-02-09_
