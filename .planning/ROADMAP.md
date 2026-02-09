# Roadmap: PSP Inspektions-Flowchart

## Overview

This roadmap delivers a single German-language flowchart showing playground inspection obligations per SN EN 1176-7. Phase 1 defines the flowchart content and structure as structured text. Phase 2 translates that content into valid, rendering Mermaid syntax. Phase 3 researches export options and produces editable formats for customer handover.

## Phases

**Phase Numbering:**
- Integer phases (1, 2): Planned milestone work
- Decimal phases (1.1, 1.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [x] **Phase 1: Content & Logic** - Define flowchart nodes, edges, decision points, and footnotes
- [x] **Phase 2: Mermaid Implementation** - Translate content into valid Mermaid syntax
- [x] **Phase 3: Export & Distribution** - Research export formats and produce editable customer deliverables

## Phase Details

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

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Content & Logic | 1/1 | Complete | 2026-02-09 |
| 2. Mermaid Implementation | 1/1 | Complete | 2026-02-09 |
| 3. Export & Distribution | 2/2 | Complete | 2026-02-09 |
