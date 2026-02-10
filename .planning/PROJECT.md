# PSP Inspektions-Flowchart

## What This Is

A customer-facing flowchart (in German) that explains the inspection obligations for playground owners/operators according to SN EN 1176/1177. It covers both new and existing playgrounds, focusing specifically on the topic of inspections. Delivered as an editable draw.io diagram, SVG vector export, and Mermaid source with German documentation — ready for visual designer handover and customer distribution.

## Core Value

Give playground owners a clear, norm-based understanding of what inspections are required, when, by whom, and what to do with the results — so they can fulfill their duty of care (Werkeigentumerhaftung, Art. 58 OR).

## Current Milestone: v1.1 Print-Ready A4

**Goal:** Optimize the existing flowchart for professional DIN A4 portrait printout with polished typography.

**Target improvements:**
- Reformat draw.io layout to fit single A4 portrait page
- Professional font choices, size hierarchy, and spacing
- Print-optimized colors and contrast
- Regenerate SVG export

## Current State

**Shipped:** v1 (2026-02-09)

Delivery package at `PSP-Inspektions-Flowchart/`:
- Inspektionsablauf.drawio (21 KB) — Editable diagram for draw.io/Visio
- Inspektionsablauf.svg (15 KB) — Vector export for print/web
- Inspektionsablauf.md (5.5 KB) — Mermaid source for technical users
- README.md (7.1 KB) — German instructions for editing/import

## Requirements

### Validated

- Two entry paths on one flowchart: Neuer Spielplatz and Bestehender Spielplatz — v1
- New playground path: Bauabnahme (SIA 118) > Inspektion nach Installation (SN EN 1176-7, 6.1 a) > Defects back to builder > Opening — v1
- Existing playground path: 3 parallel inspection branches (visuell, operativ, Hauptinspektion) — v1
- Post-inspection flow: Dokumentation > Archivierung > Maengelverarbeitung > Massnahmenkatalog > Entscheidung > Dokumentation bestehender Maengel — v1
- Safety-critical defects trigger immediate device lockout (Geraet sperren, SN EN 1176-7, 6.2.1) — v1
- Cycle loops back from defect documentation to next inspection round — v1
- New playground path transitions into existing playground inspection cycle after opening — v1
- Norm clause references as footnotes (not inline) — v1
- Language: German, using correct norm terminology — v1
- Output format: Mermaid diagram that renders correctly, suitable for handover to visual designer — v1
- Neutral/educational tone — no PSP branding or service references — v1
- Valid Mermaid syntax that renders without errors — v1
- Clear enough for a visual designer to recreate without domain expertise — v1
- No emojis, no special characters that break Mermaid rendering — v1
- SVG export for print/web use — v1
- draw.io export for customer editing — v1
- Editable source importable into Visio — v1

### Active

- [ ] draw.io diagram fits on single DIN A4 portrait page (210 × 297 mm)
- [ ] Professional typography — proper font choices, size hierarchy, consistent spacing
- [ ] Print-optimized layout — compact nodes, efficient use of page area
- [ ] Updated SVG export matching new A4 layout
- [ ] Updated README reflecting new print-ready format

### Out of Scope

- PSP service/product references — designer adds branding later
- Other lifecycle topics beyond inspections (Wartung details, Fallschutz-Pruefung EN 1177, Bestandsschutz assessment) — separate flowcharts
- Interactive web tool — PDF/print focus for now
- English version — German only for v1
- Specific checklists for each inspection type — flowchart shows the process, not the content of each check

## Context

### Norm Basis

- **SN EN 1176-7:2020** — Anleitung fuer Installation, Inspektion, Wartung und Betrieb
  - 4 inspection types defined in 6.1: a) nach Installation, b) visuell, c) operativ, d) jaehrliche Hauptinspektion
  - Inspektionsplan required per 6.2.4
  - Immediate lockout for safety-critical defects per 6.2.1
  - Independent qualified person required for Hauptinspektion and post-installation inspection per 6.2.2
  - Stossdaempfende Boeden need special attention per 6.2.3
  - Documentation requirements per 8.2.2

- **SIA 118** — Bauabnahme is a contractual construction acceptance, NOT a safety inspection. Does not replace the Inspektion nach Installation.

- **Art. 58 OR** — Werkeigentumerhaftung: Owner liable for damages from defective construction or maintenance. SN EN 1176 is applied by courts as "Stand der Technik."

- **Beiblatt 1** — Kein genereller Bestandsschutz for playground equipment. Older devices may need to be assessed against current norms.

- **CEN/TR 17207** — Four-level defect severity classification (Konform/Empfohlen/Wichtig/Dringend) used in post-inspection defect handling.

### Target Audience

Decision-makers: municipal leaders, property managers, facility owners who approve budgets and contracts. Not the Hauswart doing daily checks — this is about understanding the system, not performing inspections.

### PSP Context

PlaySafePro (playsafepro.ch) provides playground inspection, safety management, and consulting services in Switzerland. This flowchart supports their sales process by educating customers on their obligations, naturally surfacing gaps that PSP can fill.

## Constraints

- **Format**: Mermaid flowchart — must actually render without errors. Avoid emojis, special characters, complex subgraph nesting.
- **Language**: German with correct SN EN 1176 terminology
- **Audience**: Non-technical decision-makers — clear, simple language, no jargon beyond what the norm requires
- **Handover**: Must be clear enough for a visual designer to recreate in a design tool without playground safety expertise

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| One flowchart with two entry paths (new + existing) | Customer may have both situations; shows the full picture | Good |
| 3 inspection types as parallel branches (not sequential) | They run independently at different frequencies, not as a sequence | Good |
| Simple split for defect handling (critical vs. non-critical) | Detailed repair/replacement decisions belong on a separate flowchart | Good |
| Norm references as footnotes, not inline | Keeps flowchart clean for decision-makers; traceability preserved separately | Good |
| Bauabnahme (SIA 118) explicitly shown as separate from Inspektion nach Installation | Key misunderstanding among customers; high educational value | Good |
| Defects at installation go back to builder, not into regular Maengel process | Different contractual/legal situation before opening vs. during operation | Good |
| Fork-join pattern for parallel inspection branches | Clear entry/exit points for 3 inspection types | Good |
| Renamed inspection terms (Sichtkontrolle, Funktionskontrolle, Jahreshauptinspektion) with original norm terms in footnotes | More accessible for decision-makers while preserving norm traceability | Good |
| CEN/TR 17207 four-level severity classification | Industry-standard defect classification (Konform/Empfohlen/Wichtig/Dringend) | Good |
| draw.io as primary editable format | Native XML, Visio-importable, free tool, widely used | Good |
| SVG with polygon-based parallelograms | True skewed rectangles for document nodes | Good |
| German README for delivery package | Matches diagram language for Swiss/German customers | Good |

| A4 portrait orientation for single-page print | Flowchart flows top-to-bottom naturally; portrait maximizes vertical space | — Pending |

---
*Last updated: 2026-02-10 after v1.1 milestone start*
