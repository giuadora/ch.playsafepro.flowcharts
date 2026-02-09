# Phase 1: Content & Logic - Context

**Gathered:** 2026-02-09
**Status:** Ready for planning

<domain>
## Phase Boundary

Define the complete flowchart content and logic structure as structured text. One unified diagram with a starting fork (Neuer/Bestehender Spielplatz). Covers: new playground path (from installation through Bauabnahme), existing playground inspection cycle (three parallel inspection types), and post-inspection defect processing with severity-based routing. Output is a single structured text file that Phase 2 translates directly into Mermaid.

</domain>

<decisions>
## Implementation Decisions

### Content depth & granularity
- Node labels: action + brief context (e.g. "Bauabnahme (SIA 118)")
- Actions only — no responsible parties on nodes
- Single unified diagram with a starting fork: "Neuer oder bestehender Spielplatz?"
- Inspection nodes include frequency + scope (e.g. "Visuelle Inspektion (1-3x/Woche): Sichtprüfung auf offensichtliche Gefahren")
- Defect processing: detailed steps (documentation, prioritization, assignment, follow-up verification)
- Include a legend explaining node shapes (rectangles, diamonds, rounded, etc.)
- New playground path starts at installation (not earlier planning/procurement steps)
- Target audience: broader (facility managers, municipal administrators) — language must be accessible without deep norm knowledge
- Use official norm terminology (Hauptinspektion, Bauabnahme) with footnotes explaining meaning
- Defect severity per CEN/TR 17207 risk assessment: Konform, Empfohlen, Wichtig, Dringend
  - Konform: no action, documentation only
  - Empfohlen, Wichtig, Dringend: feed into Massnahmenkatalog
  - Dringend: triggers "Gerät sperren" immediately

### Decision point logic
- Branch style (binary vs multi-path): Claude's discretion per decision point
- Parallel inspection representation (fork/join vs subgraph): Claude's discretion
- No separate Freigabe gate for new playgrounds — defect-free after Bauabnahme flows naturally to opening
- Unresolved defects: loop back with re-check at next inspection (no escalation path)
- Cycle closure: end node with periodicity note ("Nächster Inspektionszyklus gemäss Zeitplan"), not an explicit loop arrow

### Footnote & norm referencing
- Numbered footnotes (superscript numbers on nodes, footnote list below chart)
- Only nodes where a specific norm clause prescribes the action — not every node
- Footnote content: clause number + key obligation (e.g. "SN EN 1176-7:2020, 8.2 — Hauptinspektion mind. 1x/Jahr durch sachkundige Person")
- Art. 58 OR: footnote only, no special framing at top of chart
- Relevant norms: SN EN 1176-7, SIA 118, Art. 58 OR, CEN/TR 17207

### Structured text format
- Single file covering entire flowchart
- Direct flow to Phase 2 (no review gate between phases)

### Claude's Discretion
- Structured text format choice (Markdown, YAML, or hybrid)
- Whether to include node IDs for traceability
- Branch style per decision point (binary vs multi-path)
- Parallel inspection visual representation
- Exact node wording and label length

</decisions>

<specifics>
## Specific Ideas

- Defect classification follows CEN/TR 17207 risk assessment methodology: "Jeder Befund wird einer der folgenden fünf Kategorien zugeordnet" — four severity levels (Konform, Empfohlen, Wichtig, Dringend) drive follow-up actions
- Inspection reports state: "Die Inspektion erfolgt auf Grundlage der Normenreihe SN EN 1176 sowie einer professionellen Risikobewertung, wie sie im europäischen technischen Bericht CEN/TR 17207 empfohlen wird"
- Defects can be found and documented on all inspection types — classification by inspector determines follow-up, not the inspection type

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope

</deferred>

---

*Phase: 01-content-logic*
*Context gathered: 2026-02-09*
