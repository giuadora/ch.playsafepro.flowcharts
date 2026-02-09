# Spielplatz-Inspektionen: Ablaufdiagramm

**Grundlage:** SN EN 1176-7:2020, Anleitung für Installation, Inspektion, Wartung und Betrieb

**Zweck:** Dieses Flowchart zeigt die Inspektionspflichten für neue und bestehende Spielplätze gemäss SN EN 1176-7. Es unterstützt Betreiber, Gemeinden und Eigentümer bei der Erfüllung ihrer Sorgfaltspflicht nach Art. 58 OR (Werkeigentümerhaftung).

---

## Node Definitions

### Starting Fork

| Node ID | Label | Shape | Footnote |
|---------|-------|-------|----------|
| START | Spielplatz-Inspektionen | rounded-rect (start) | — |
| D01 | Neuer oder bestehender Spielplatz? | diamond | — |

### Neuer Spielplatz Path

| Node ID | Label | Shape | Footnote |
|---------|-------|-------|----------|
| N01 | Bauabnahme nach SIA 118 (vertragliche Abnahme durch Architekt/Bauleiter) | rectangle | [1] |
| N02 | Inspektion nach Installation: Sicherheitsprüfung aller installierten Geräte durch zertifizierte Fachperson | rectangle | [2] |
| D02 | Mängel festgestellt? | diamond | — |
| N03 | Mängel an Ersteller/Hersteller zurück zur Behebung | rectangle | — |
| N04 | Spielplatz eröffnen (Übergang zu Bestandsinspektion) | rounded-rect | — |

### Bestehender Spielplatz Path - Inspection Branches (Parallel)

| Node ID | Label | Shape | Footnote |
|---------|-------|-------|----------|
| E00 | Inspektionszyklus beginnen | rounded-rect | — |
| E01 | Visuelle Routineinspektion (1-3x pro Woche): Sichtprüfung auf offensichtliche Gefahren | rectangle | [3] |
| E02 | Operative Inspektion (alle 1-3 Monate): Funktionsprüfung, Verschleiss, Stabilität | rectangle | [4] |
| E03 | Jährliche Hauptinspektion: Umfassende Prüfung durch zertifizierte, unabhängige Fachperson | rectangle | [5] |
| E04 | Inspektionsbericht erstellen | parallelogram | — |

### Post-Inspection Process

| Node ID | Label | Shape | Footnote |
|---------|-------|-------|----------|
| P01 | Bericht archivieren | rectangle | [6] |
| D03 | Mängel festgestellt? | diamond | — |
| P02 | Mängel nach CEN/TR 17207 klassifizieren | rectangle | [7] |
| D04 | Schweregrad? (Konform / Empfohlen / Wichtig / Dringend) | diamond | — |
| P03 | Konform: Keine Massnahme, nur Dokumentation | rectangle | — |
| P04 | Gerät sperren (sofortige Sperrung bei sicherheitskritischen Mängeln) | rectangle | [8] |
| P05 | Massnahmenkatalog erstellen: Priorisierung, Zuweisung, Terminierung | rectangle | — |
| D05 | Entscheidung: Budget, intern vs. extern, Priorisierung | diamond | — |
| P06 | Massnahmen umsetzen (Reparaturen/Korrekturen ausführen) | rectangle | — |
| P07 | Dokumentation bestehender Mängel: Nachverfolgung, Wiedervorlage | parallelogram | — |
| D06 | Mängel behoben? | diamond | — |
| END | Nächster Inspektionszyklus gemäss Zeitplan (siehe Inspektionsplan SN EN 1176-7, 6.2.4) | rounded-rect (end) | [9] |

---

## Edge Definitions

### Starting Fork to Paths

| From | To | Label |
|------|-----|-------|
| START | D01 | — |
| D01 | N01 | Neuer Spielplatz |
| D01 | E00 | Bestehender Spielplatz |

### Neuer Spielplatz Path Flow

| From | To | Label |
|------|-----|-------|
| N01 | N02 | — |
| N02 | D02 | — |
| D02 | N03 | Ja (Mängel festgestellt) |
| D02 | N04 | Nein (keine Mängel oder Mängel behoben) |
| N03 | N02 | Nachbesserung abgeschlossen, erneute Prüfung |
| N04 | E00 | Spielplatz in Betrieb |

### Bestehender Spielplatz - Parallel Inspection Branches

| From | To | Label |
|------|-----|-------|
| E00 | E01 | Branch: Visuelle Inspektion |
| E00 | E02 | Branch: Operative Inspektion |
| E00 | E03 | Branch: Hauptinspektion |
| E01 | E04 | Merge |
| E02 | E04 | Merge |
| E03 | E04 | Merge |

### Post-Inspection Process Flow

| From | To | Label |
|------|-----|-------|
| E04 | P01 | — |
| P01 | D03 | — |
| D03 | END | Nein (keine Mängel) |
| D03 | P02 | Ja (Mängel festgestellt) |
| P02 | D04 | — |
| D04 | P03 | Konform |
| D04 | P05 | Empfohlen |
| D04 | P05 | Wichtig |
| D04 | P04 | Dringend |
| P03 | END | — |
| P04 | P05 | Nach Sperrung |
| P05 | D05 | — |
| D05 | P06 | Entscheidung getroffen |
| P06 | P07 | — |
| P07 | D06 | — |
| D06 | END | Ja (Mängel behoben) |
| D06 | P07 | Nein (noch offene Mängel: Wiedervorlage zur nächsten Inspektion) |

---

## Footnotes

[1] **SIA 118** — Allgemeine Bedingungen für Bauarbeiten. Die Bauabnahme ist eine vertragliche Abnahme zwischen Bauherrschaft und Ersteller. Sie ersetzt NICHT die sicherheitstechnische Inspektion nach Installation.

[2] **SN EN 1176-7:2020, 6.1 a** — Inspektion nach Installation: Sicherheitsprüfung durch eine zertifizierte, unabhängige Fachperson vor der ersten Nutzung. Prüft normgerechte Installation, Aufstellflächen, Fallschutz und Gerätefunktion.

[3] **SN EN 1176-7:2020, 6.1 b** — Visuelle Routineinspektion: Sichtprüfung zur Erkennung offensichtlicher Gefahren (z.B. Vandalismus, Verschmutzung, grobe Schäden). Häufigkeit: 1-3x pro Woche, je nach Nutzungsintensität.

[4] **SN EN 1176-7:2020, 6.1 c** — Operative Inspektion: Funktionsprüfung aller beweglichen Teile, Verschleissbeurteilung, Stabilitätsprüfung, Prüfung von Verbindungselementen. Häufigkeit: alle 1-3 Monate durch geschultes Fachpersonal.

[5] **SN EN 1176-7:2020, 6.1 d** — Jährliche Hauptinspektion: Umfassende Sicherheitsprüfung durch eine zertifizierte, unabhängige Fachperson. Detaillierte Beurteilung aller sicherheitsrelevanten Aspekte inkl. Fallschutz, Fundamente, Korrosion, Materialermüdung.

[6] **SN EN 1176-7:2020, 8.2.2** — Dokumentation: Inspektionsberichte müssen aufbewahrt werden. Sie dienen als Nachweis der Sorgfaltspflicht und als Grundlage für Wartungsentscheidungen.

[7] **CEN/TR 17207** — Technischer Bericht zur Risikobewertung und Mängelklassifizierung auf Spielplätzen. Definiert vier Schweregrade basierend auf Eintrittswahrscheinlichkeit und Schadensausmass: Konform, Empfohlen, Wichtig, Dringend.

[8] **SN EN 1176-7:2020, 6.2.1** — Sofortmassnahmen: Sicherheitskritische Mängel (Schweregrad "Dringend") erfordern sofortige Sperrung des betroffenen Geräts bis zur vollständigen Behebung. Gerät darf erst nach Freigabe durch Fachperson wieder genutzt werden.

[9] **SN EN 1176-7:2020, 6.2.4** — Inspektionsplan: Betreiber muss einen Plan erstellen, der festlegt: WAS wird geprüft (Inventar), WANN (Frequenzen), WIE (Checklisten/Verfahren), WER (Zuständigkeiten). Dieser Plan ist Grundlage für den wiederkehrenden Inspektionszyklus.

---

## Shape Legend

| Form | Bedeutung | Verwendung im Flowchart |
|------|-----------|-------------------------|
| **Rechteck** | Prozessschritt / Aktion | Inspektionen durchführen, Massnahmen umsetzen, Klassifizieren |
| **Raute (Diamant)** | Entscheidungspunkt | Fragen mit Ja/Nein oder mehreren Auswahlmöglichkeiten (z.B. Schweregrade) |
| **Abgerundetes Rechteck** | Start / Ende / Übergang | Einstiegspunkte, Abschlusspunkte, Übergänge zwischen Pfaden |
| **Parallelogramm** | Dokument / Bericht | Inspektionsberichte, Dokumentation bestehender Mängel |

**Farbcodierung (für Phase 2 - Mermaid-Implementierung):**
- Neue Spielplätze: Blautöne
- Inspektionen: Grüntöne
- Mängel/Massnahmen: Gelb/Orange
- Kritische Sperrung: Rot
- Start/Ende: Neutralgrau

---

## Node Count Verification

**Total nodes:** 29
- Starting fork: 2 nodes
- Neuer Spielplatz path: 4 nodes
- Bestehender Spielplatz inspection branches: 5 nodes
- Post-inspection process: 12 nodes
- Decisions: 6 nodes

**Total edges:** 31 (including parallel branches and loops)
