# Requirements: PSP Inspektions-Flowchart

**Defined:** 2026-02-10
**Core Value:** Give playground owners a clear, norm-based understanding of inspection obligations per SN EN 1176-7, so they can fulfill their duty of care (Werkeigentumerhaftung, Art. 58 OR)

## v1.1 Requirements

Requirements for print-ready A4 optimization. Each maps to roadmap phases.

### Layout

- [x] **LAYOUT-01**: draw.io page set to exact DIN A4 portrait dimensions (210 x 297 mm)
- [x] **LAYOUT-02**: All nodes reorganized and resized to fit within A4 with proper print margins
- [x] **LAYOUT-03**: Flowchart content fully visible without clipping on A4 printout

### Typography

- [x] **TYPO-01**: All nodes use a professional sans-serif font (Helvetica/Arial family) consistently

### Export

- [ ] **EXPORT-01**: SVG export regenerated matching new A4 layout
- [ ] **EXPORT-02**: Mermaid source updated to reflect any structural changes from reorganization

### Documentation

- [ ] **DOC-01**: README updated to reflect A4 print-ready format

## Future Requirements

Deferred to later milestones. Tracked but not in current roadmap.

### Visual Polish

- **TYPO-02**: Clear font size hierarchy (title > section headers > node text > footnotes)
- **TYPO-03**: Consistent padding inside nodes and gaps between elements
- **LAYOUT-04**: Print margins defined (e.g. 10mm) to prevent edge clipping

### Additional Flowcharts

- **FLOW-01**: Wartung (maintenance) flowchart
- **FLOW-02**: Fallschutzpruefung (impact attenuation testing) flowchart

### Branding

- **BRAND-01**: PSP service touchpoints integrated into flowchart

### Interactive

- **INTER-01**: Interactive web version of flowchart

## Out of Scope

| Feature | Reason |
|---------|--------|
| Color palette changes | Current color scheme works well; optimize only if print contrast is poor |
| Content changes | Same flowchart content as v1 -- only layout/typography changes |
| Multi-page PDF | User explicitly chose single A4 page |
| Landscape orientation | User explicitly chose portrait |
| English version | German only per v1 scope |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
|-------------|-------|--------|
| LAYOUT-01 | Phase 4 | Complete |
| LAYOUT-02 | Phase 4 | Complete |
| LAYOUT-03 | Phase 4 | Complete |
| TYPO-01 | Phase 4 | Complete |
| EXPORT-01 | Phase 5 | Pending |
| EXPORT-02 | Phase 5 | Pending |
| DOC-01 | Phase 5 | Pending |

**Coverage:**
- v1.1 requirements: 7 total
- Mapped to phases: 7
- Unmapped: 0

---
*Requirements defined: 2026-02-10*
*Last updated: 2026-02-10 after roadmap creation*
