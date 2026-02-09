# PSP Inspektions-Flowchart

## What This Is

A customer-facing flowchart (in German) that explains the inspection obligations for playground owners/operators according to SN EN 1176/1177. It covers both new and existing playgrounds, focusing specifically on the topic of inspections. The flowchart is designed for decision-makers (budget holders, municipal leaders, property owners) and will be handed to a visual designer for branding and embedding into a PDF.

## Core Value

Give playground owners a clear, norm-based understanding of what inspections are required, when, by whom, and what to do with the results — so they can fulfill their duty of care (Werkeigentumerhaftung, Art. 58 OR).

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] Two entry paths on one flowchart: Neuer Spielplatz and Bestehender Spielplatz
- [ ] New playground path: Planung > Bau > Bauabnahme (SIA 118) > Inspektion nach Installation (SN EN 1176-7, 6.1 a) > Defects back to builder > Opening
- [ ] Existing playground path: 3 parallel inspection branches (visuell, operativ, Hauptinspektion)
- [ ] Post-inspection flow: Dokumentation > Archivierung > Maengelverarbeitung > Massnahmenkatalog > Entscheidung (Budget, intern/extern) > Dokumentation bestehender Maengel
- [ ] Safety-critical defects trigger immediate device lockout (Geraet sperren, SN EN 1176-7, 6.2.1)
- [ ] Cycle loops back from defect documentation to next inspection round
- [ ] New playground path transitions into existing playground inspection cycle after opening
- [ ] Norm clause references as footnotes (not inline)
- [ ] Language: German, using correct norm terminology
- [ ] Output format: Mermaid diagram that renders correctly, suitable for handover to visual designer
- [ ] Decision-tree level of detail for each inspection type
- [ ] Neutral/educational tone — no PSP branding or service references

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
| One flowchart with two entry paths (new + existing) | Customer may have both situations; shows the full picture | -- Pending |
| 3 inspection types as parallel branches (not sequential) | They run independently at different frequencies, not as a sequence | -- Pending |
| Simple split for defect handling (critical vs. non-critical) | Detailed repair/replacement decisions belong on a separate flowchart | -- Pending |
| Norm references as footnotes, not inline | Keeps flowchart clean for decision-makers; traceability preserved separately | -- Pending |
| Bauabnahme (SIA 118) explicitly shown as separate from Inspektion nach Installation | Key misunderstanding among customers; high educational value | -- Pending |
| Defects at installation go back to builder, not into regular Maengel process | Different contractual/legal situation before opening vs. during operation | -- Pending |

---
*Last updated: 2026-02-09 after initialization*
