# Requirements: PSP Inspektions-Flowchart

**Defined:** 2026-02-09
**Core Value:** Give playground owners a clear, norm-based understanding of inspection obligations per SN EN 1176-7

## v1 Requirements

### Flowchart Structure

- [x] **FLOW-01**: Single flowchart with entry point that splits into "Neuer Spielplatz" and "Bestehender Spielplatz"
- [x] **FLOW-02**: New playground path ends by transitioning into existing playground inspection cycle
- [x] **FLOW-03**: Existing playground path loops back to inspections after defect handling
- [x] **FLOW-04**: All norm references collected as numbered footnotes, not inline

### Neuer Spielplatz Path

- [x] ~~**NEW-01**: Planung node~~ — Removed: locked decision says path starts at installation, not earlier planning steps
- [x] ~~**NEW-02**: Bau node~~ — Removed: locked decision says path starts at installation, not earlier planning steps
- [x] **NEW-03**: Bauabnahme nach SIA 118 -- contractual construction acceptance by architect/Bauleiter
- [x] **NEW-04**: Inspektion nach Installation (SN EN 1176-7, 6.1 a) -- safety inspection by certified specialist
- [x] **NEW-05**: Defect decision: findings go back to builder/manufacturer for correction before opening
- [x] **NEW-06**: No defects or defects resolved -- Spielplatz eroeffnen -- transition to existing path

### Inspektionsarten

- [x] **INSP-01**: Three parallel branches for the 3 inspection types
- [x] **INSP-02**: Visuelle Routineinspektion -- frequency set by operator (daily/weekly), SN EN 1176-7, 6.1 b
- [x] **INSP-03**: Operative Inspektion -- every 1-3 months, SN EN 1176-7, 6.1 c
- [x] **INSP-04**: Jaehrliche Hauptinspektion -- by certified independent person, SN EN 1176-7, 6.1 d
- [x] **INSP-05**: All three branches merge into documentation flow

### Post-Inspection Process

- [x] **POST-01**: Dokumentation -- inspection report created
- [x] **POST-02**: Bericht archivieren
- [x] **POST-03**: Festgestellte Maengel verarbeiten with severity split
- [x] **POST-04**: Safety-critical defects -- immediate device lockout (Geraet sperren)
- [x] **POST-05**: Massnahmenkatalog erstellen
- [x] **POST-06**: Entscheidung -- budget, intern vs. extern, prioritization
- [x] **POST-07**: Dokumentation bestehender Maengel (tracking/follow-up)
- [x] **POST-08**: Loop back to inspection cycle

### Format and Quality

- [ ] **FMT-01**: Valid Mermaid syntax that renders without errors
- [ ] **FMT-02**: German language with correct SN EN 1176 terminology
- [ ] **FMT-03**: Clear enough for a visual designer to recreate without domain expertise
- [ ] **FMT-04**: No emojis, no special characters that break Mermaid rendering

### Export and Distribution

- [ ] **EXP-01**: Research available export formats (draw.io, SVG, Visio, PDF, etc.) and document pros/cons
- [ ] **EXP-02**: Export flowchart as SVG for print/web use
- [ ] **EXP-03**: Export flowchart as draw.io (.drawio) for customer editing
- [ ] **EXP-04**: Provide editable source that customers can import into their preferred tool (e.g. Visio)

## v2 Requirements

### Additional Flowcharts

- **V2-01**: Separate flowchart for Wartung (maintenance lifecycle)
- **V2-02**: Separate flowchart for Fallschutzpruefung (EN 1177)
- **V2-03**: Separate flowchart for Bestandsschutz assessment
- **V2-04**: Interactive web version for playsafepro.ch
- **V2-05**: English translation

### Enhancements

- **V2-06**: PSP service touchpoints marked at each gap
- **V2-07**: Specific checklists per inspection type
- **V2-08**: Hinweisschild requirements (SN EN 1176-7, 8.2.3)
- **V2-09**: Unfallmeldeverfahren (SN EN 1176-7, 8.2.4)

## Out of Scope

| Feature | Reason |
|---------|--------|
| PSP branding/service references | Designer adds branding later |
| Maintenance details beyond defect handling | Separate flowchart topic |
| EN 1177 Fallschutz testing specifics | Separate flowchart topic |
| Specific inspection checklists | Flowchart shows process, not content of checks |
| Bestandsschutz/grandfathering assessment | Separate flowchart topic |
| Interactive web tool | PDF/print focus for v1 |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| FLOW-01 | Phase 1 | Complete |
| FLOW-02 | Phase 1 | Complete |
| FLOW-03 | Phase 1 | Complete |
| FLOW-04 | Phase 1 | Complete |
| NEW-01 | Phase 1 | Removed (locked decision) |
| NEW-02 | Phase 1 | Removed (locked decision) |
| NEW-03 | Phase 1 | Complete |
| NEW-04 | Phase 1 | Complete |
| NEW-05 | Phase 1 | Complete |
| NEW-06 | Phase 1 | Complete |
| INSP-01 | Phase 1 | Complete |
| INSP-02 | Phase 1 | Complete |
| INSP-03 | Phase 1 | Complete |
| INSP-04 | Phase 1 | Complete |
| INSP-05 | Phase 1 | Complete |
| POST-01 | Phase 1 | Complete |
| POST-02 | Phase 1 | Complete |
| POST-03 | Phase 1 | Complete |
| POST-04 | Phase 1 | Complete |
| POST-05 | Phase 1 | Complete |
| POST-06 | Phase 1 | Complete |
| POST-07 | Phase 1 | Complete |
| POST-08 | Phase 1 | Complete |
| FMT-01 | Phase 2 | Pending |
| FMT-02 | Phase 2 | Pending |
| FMT-03 | Phase 2 | Pending |
| FMT-04 | Phase 2 | Pending |
| EXP-01 | Phase 3 | Pending |
| EXP-02 | Phase 3 | Pending |
| EXP-03 | Phase 3 | Pending |
| EXP-04 | Phase 3 | Pending |

**Coverage:**
- v1 requirements: 31 total
- Mapped to phases: 31
- Unmapped: 0

---
*Requirements defined: 2026-02-09*
*Last updated: 2026-02-09 after Phase 1 completion*
