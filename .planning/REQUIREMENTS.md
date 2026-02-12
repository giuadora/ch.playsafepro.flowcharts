# Requirements: PSP Inspektions-Flowchart

**Defined:** 2026-02-12
**Core Value:** Give playground owners a clear, norm-based understanding of inspection obligations per SN EN 1176-7, so they can fulfill their duty of care (Werkeigentumerhaftung, Art. 58 OR)

## v2.0 Requirements

Requirements for v2.0 Flowchart Split. Each maps to roadmap phases.

### Flowchart Split

- [ ] **SPLIT-01**: Single flowchart split into two separate draw.io files with matching SVG, PDF, and Mermaid exports
- [ ] **SPLIT-02**: FC1 (Neuer Spielplatz) starts at "Neuer Spielplatz" and ends at "Inspektionszyklus beginnen"
- [ ] **SPLIT-03**: FC2 (Bestehender Spielplatz) starts at "Inspektionszyklus beginnen" and loops back via "Nächster Inspektionszyklus"
- [ ] **SPLIT-04**: Both flowcharts have a subline below the main title — "Neuer Spielplatz" on FC1, "Bestehender Spielplatz" on FC2

### Node Modifications

- [ ] **NODE-01**: FC1 "Inspektion nach Installation" node colored green (inspection activity)
- [ ] **NODE-02**: FC1 "Inspektionsplan erstellen" rendered as subprocess symbol (double-bordered rectangle)
- [ ] **NODE-03**: FC2 new "Bericht archivieren" node as green rectangle (Action) between Inspektionsbericht erstellen and Instandhaltungs-Management
- [ ] **NODE-04**: FC2 inspection types renamed to SN EN 1176-7 terminology: Visuelle Routine-Inspektion, Operative Inspektion, Jährliche Hauptinspektion

### References & Footnotes

- [ ] **REF-01**: All nodes referencing a norm clause carry a footnote superscript
- [ ] **REF-02**: "Inspektionsplan erstellen" audited against SN EN 1176-7 and footnoted if applicable
- [ ] **REF-03**: Each flowchart has its own complete footnote box (only footnotes relevant to that flow)

### Legend & Documentation

- [ ] **DOC-01**: Subprocess symbol added to legend in both flowcharts
- [ ] **DOC-02**: README updated to describe both flowcharts (Neuer Spielplatz + Bestehender Spielplatz)
- [ ] **DOC-03**: Root README updated with new file listing

### File Management & QR

- [ ] **FILE-01**: Files renamed to clearly distinguish the two flows (e.g., Neuer-Spielplatz.* and Bestehender-Spielplatz.*)
- [ ] **FILE-02**: Each flowchart's "Als PDF herunterladen" QR points to its own PDF
- [ ] **FILE-03**: Both flowcharts' "Als Vorlage herunterladen" QR points to the shared README

### Quality Assurance

- [ ] **QA-01**: Both flowcharts pass center alignment verification (vertical + horizontal)
- [ ] **QA-02**: All arrows connected — no dangling edges
- [ ] **QA-03**: Margins maintained on all edges (no content touching page bounds)
- [ ] **QA-04**: No node overlaps
- [ ] **QA-05**: Footer with 3-column corporate layout present on both flowcharts
- [ ] **QA-06**: PSP logo and branding present on both flowcharts

## Future Requirements

### Additional Flowcharts

- **FLOW-01**: Wartung (maintenance) flowchart per SN EN 1176-7
- **FLOW-02**: Fallschutzprüfung (impact attenuation testing) flowchart

### Digital

- **DIGI-01**: Interactive web version of flowcharts

## Out of Scope

| Feature | Reason |
|---------|--------|
| New content/nodes beyond specified changes | v2.0 is structural split + corrections, not content expansion |
| Color palette changes | Current B&W-contrast scheme works well for print |
| Multi-page PDF | Single A4 page per flowchart |
| Landscape orientation | Portrait confirmed in v1.1 |
| English version | German only |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
|-------------|-------|--------|
| SPLIT-01 | Phase 7 | Pending |
| SPLIT-02 | Phase 7 | Pending |
| SPLIT-03 | Phase 7 | Pending |
| SPLIT-04 | Phase 7 | Pending |
| FILE-01 | Phase 7 | Pending |
| NODE-01 | Phase 8 | Pending |
| NODE-02 | Phase 8 | Pending |
| NODE-03 | Phase 8 | Pending |
| NODE-04 | Phase 8 | Pending |
| REF-01 | Phase 8 | Pending |
| REF-02 | Phase 8 | Pending |
| REF-03 | Phase 8 | Pending |
| DOC-01 | Phase 9 | Pending |
| DOC-02 | Phase 9 | Pending |
| DOC-03 | Phase 9 | Pending |
| FILE-02 | Phase 9 | Pending |
| FILE-03 | Phase 9 | Pending |
| QA-01 | Phase 9 | Pending |
| QA-02 | Phase 9 | Pending |
| QA-03 | Phase 9 | Pending |
| QA-04 | Phase 9 | Pending |
| QA-05 | Phase 9 | Pending |
| QA-06 | Phase 9 | Pending |

**Coverage:**
- v2.0 requirements: 19 total
- Mapped to phases: 19
- Unmapped: 0 ✓

---
*Requirements defined: 2026-02-12*
*Last updated: 2026-02-12 after roadmap creation*
