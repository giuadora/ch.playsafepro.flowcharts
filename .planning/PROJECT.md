# PSP Inspektions-Flowchart

## What This Is

A customer-facing flowchart (in German) that explains the inspection obligations for playground owners/operators according to SN EN 1176/1177. Covers both new and existing playgrounds, focusing on inspections. Delivered as a print-ready DIN A4 draw.io diagram, SVG vector export, and Mermaid source with German documentation — ready for visual designer handover and customer distribution.

## Core Value

Give playground owners a clear, norm-based understanding of what inspections are required, when, by whom, and what to do with the results — so they can fulfill their duty of care (Werkeigentumerhaftung, Art. 58 OR).

## Current State

**Shipped:** v1.1 Print-Ready A4 (2026-02-10)

Delivery package at `Inspektion-von-Spielplatzgeraeten-und-Spielplatzboeden/`:
- Spielplatzinspektionen.drawio (21 KB) — A4 portrait editable diagram for draw.io/Visio
- Spielplatzinspektionen.svg (15 KB) — A4 vector export for print/web
- Spielplatzinspektionen.md (5.5 KB) — Mermaid source (16 nodes, 20 edges, 8 footnotes)
- README.md (7.1 KB) — German instructions, CC BY-NC 4.0 license

**Key facts:**
- 16 flow nodes, simplified post-inspection path (3 steps)
- DIN A4 portrait (794x1123px), Helvetica typography
- 5 color sections (gray/blue/green/yellow + info)
- CEN/TR 17207 severity classification as annotation
- 8 norm footnotes (SN EN 1176-7, SIA 118, CEN/TR 17207, Art. 58 OR)

## Requirements

### Validated

- ✓ Two entry paths on one flowchart: Neuer Spielplatz and Bestehender Spielplatz — v1.0
- ✓ New playground path: Bauabnahme > Inspektion nach Installation > Defects back to builder > Opening — v1.0
- ✓ Existing playground path: 3 parallel inspection branches — v1.0
- ✓ Post-inspection flow: Dokumentation > Archivierung > Maengelverarbeitung > Massnahmenkatalog > Entscheidung > Dokumentation bestehender Maengel — v1.0
- ✓ Safety-critical defects trigger immediate device lockout — v1.0
- ✓ Cycle loops back from defect documentation to next inspection round — v1.0
- ✓ New playground path transitions into existing playground inspection cycle after opening — v1.0
- ✓ Norm clause references as footnotes — v1.0
- ✓ Language: German, using correct norm terminology — v1.0
- ✓ Mermaid diagram that renders correctly — v1.0
- ✓ Neutral/educational tone — v1.0
- ✓ Valid Mermaid syntax — v1.0
- ✓ Clear enough for visual designer to recreate — v1.0
- ✓ No emojis/special characters that break rendering — v1.0
- ✓ SVG export for print/web — v1.0
- ✓ draw.io export for customer editing — v1.0
- ✓ Editable source importable into Visio — v1.0
- ✓ draw.io diagram fits on single DIN A4 portrait page (210 x 297 mm) — v1.1
- ✓ Professional typography — Helvetica, consistent sizing and spacing — v1.1
- ✓ Print-optimized layout — compact nodes, efficient use of page area — v1.1
- ✓ Updated SVG export matching A4 layout — v1.1
- ✓ Updated README reflecting print-ready format, CC BY-NC 4.0 — v1.1

### Active

(None — no active milestone)

### Out of Scope

- PSP service/product references — designer adds branding later
- Other lifecycle topics beyond inspections (Wartung, Fallschutz-Pruefung, Bestandsschutz) — separate flowcharts
- Interactive web tool — PDF/print focus for now
- English version — German only
- Specific checklists for each inspection type — flowchart shows process, not content
- Color palette changes — current B&W-contrast scheme works well for print
- Multi-page PDF — user chose single A4 page
- Landscape orientation — user chose portrait

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

- **CEN/TR 17207** — Four-level defect severity classification (Konform/Empfohlen/Wichtig/Dringend) used in post-inspection defect handling. Shown as annotation in flowchart.

### Target Audience

Decision-makers: municipal leaders, property managers, facility owners who approve budgets and contracts. Not the Hauswart doing daily checks — this is about understanding the system, not performing inspections.

### PSP Context

PlaySafePro (playsafepro.ch) provides playground inspection, safety management, and consulting services in Switzerland. This flowchart supports their sales process by educating customers on their obligations, naturally surfacing gaps that PSP can fill.

## Constraints

- **Format**: Mermaid flowchart + draw.io editable + SVG export — A4 portrait print-ready
- **Language**: German with correct SN EN 1176 terminology
- **Audience**: Non-technical decision-makers — clear, simple language
- **Handover**: Must be clear enough for a visual designer to recreate without playground safety expertise
- **License**: CC BY-NC 4.0

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| One flowchart with two entry paths (new + existing) | Customer may have both situations | ✓ Good |
| 3 inspection types as parallel branches | They run independently at different frequencies | ✓ Good |
| Simple split for defect handling (critical vs. non-critical) | Detailed repair decisions belong on separate flowchart | ✓ Good |
| Norm references as footnotes, not inline | Keeps flowchart clean for decision-makers | ✓ Good |
| Bauabnahme (SIA 118) explicitly shown as separate from Inspektion | Key customer misunderstanding; high educational value | ✓ Good |
| Defects at installation go back to builder | Different contractual situation before opening | ✓ Good |
| Fork-join pattern for parallel inspection branches | Clear entry/exit points for 3 types | ✓ Good |
| Renamed inspection terms with original in footnotes | More accessible while preserving traceability | ✓ Good |
| CEN/TR 17207 as annotation instead of process step | Classification is part of report, not a separate action | ✓ Good |
| draw.io as primary editable format | Native XML, Visio-importable, free tool | ✓ Good |
| SVG with polygon-based parallelograms | True skewed rectangles for document nodes | ✓ Good |
| German README for delivery package | Matches diagram language for Swiss/German customers | ✓ Good |
| A4 portrait orientation for single-page print | Flowchart flows top-to-bottom naturally | ✓ Good |
| Manual repositioning over proportional scaling | Optimal readability at A4 scale | ✓ Good |
| Simplified post-inspection flow (10 nodes → 3) | User found complex section unreadable; linear path clearer | ✓ Good |
| Footnote renumbering after P04 removal | Clean sequential numbering (8 footnotes) | ✓ Good |

---
*Last updated: 2026-02-10 after v1.1 milestone*
