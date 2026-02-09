# PSP Inspektions-Flowchart

## Inhalt

Dieses Paket enthält ein vollständiges Ablaufdiagramm für Spielplatz-Inspektionen gemäss der Schweizer Norm **SN EN 1176-7:2020** – Anleitung für Installation, Inspektion, Wartung und Betrieb.

Das Flowchart unterstützt Spielplatzbetreiber, Gemeinden und Eigentümer bei der Erfüllung ihrer Sorgfaltspflicht nach Art. 58 OR (Werkeigentümerhaftung). Es zeigt den vollständigen Inspektionsprozess für neue und bestehende Spielplätze, von der Bauabnahme über die regelmässigen Kontrollen bis zur Mängelbehebung.

## Dateien

| Datei | Format | Verwendung |
|-------|--------|------------|
| Inspektionsablauf.drawio | draw.io | Editierbares Diagramm — Knoten verschieben, Farben ändern, Text bearbeiten |
| Inspektionsablauf.svg | SVG | Druckversion / Web-Einbettung — nicht editierbar |
| Inspektionsablauf.md | Mermaid | Quellcode des Diagramms — für technische Nutzer |
| README.md | Markdown | Diese Anleitung |

## Bearbeitung mit draw.io

### Datei öffnen

**Option 1: Online (keine Installation nötig)**
1. Besuchen Sie https://app.diagrams.net
2. Klicken Sie auf "Open Existing Diagram"
3. Wählen Sie die Datei `Inspektionsablauf.drawio`
4. Das Diagramm wird im Browser geladen

**Option 2: Desktop-App (empfohlen für regelmässige Nutzung)**
1. Laden Sie draw.io Desktop herunter: https://github.com/jgraph/drawio-desktop/releases
2. Installieren Sie die App für Ihr Betriebssystem (Windows, macOS, Linux)
3. Öffnen Sie `Inspektionsablauf.drawio` mit draw.io Desktop

### Diagramm bearbeiten

**Text ändern:**
- Doppelklicken Sie auf einen Knoten, um den Text zu bearbeiten
- Drücken Sie Enter, um die Änderung zu speichern

**Knoten verschieben:**
- Klicken und ziehen Sie einen Knoten an eine neue Position
- Verbindungslinien folgen automatisch (wenn "orthogonal" aktiviert ist)

**Farben ändern:**
1. Wählen Sie einen Knoten aus (einfacher Klick)
2. Rechts im Panel finden Sie "Fill" (Füllung) und "Stroke" (Rahmen)
3. Klicken Sie auf die Farbfelder, um neue Farben zu wählen

**Neue Knoten hinzufügen:**
1. Ziehen Sie eine Form aus der linken Bibliothek auf die Zeichenfläche
2. Das Diagramm verwendet diese Formen:
   - **Rechteck** = Prozessschritt / Aktion
   - **Raute** = Entscheidungspunkt
   - **Abgerundetes Rechteck** = Start / Ende
   - **Parallelogramm** = Dokument / Bericht

**Farb-Schema des Diagramms:**
- **Blau** (#BBDEFB / #1565C0): Neuer Spielplatz-Pfad
- **Grün** (#C8E6C9 / #2E7D32): Inspektionen
- **Gelb** (#FFF9C4 / #F9A825): Mängel / Massnahmen
- **Rot** (#FFCDD2 / #C62828): Kritische Sperrung
- **Grau** (#F5F5F5 / #9E9E9E): Start / Ende

**Firmenlogo einfügen:**
1. Klicken Sie auf den "PSP Logo" Platzhalter (gestrichelte Box oben rechts)
2. Löschen Sie den Platzhalter-Text
3. Menü: Arrange → Insert → Image
4. Wählen Sie Ihr Firmenlogo (PNG, JPG oder SVG)
5. Positionieren Sie das Logo in der Box

### Exportieren

**Als PDF exportieren:**
1. Menü: File → Export as → PDF
2. Wählen Sie die gewünschten Optionen (z.B. "Selection only" für nur einen Teil)
3. Klicken Sie auf "Export"

**Als PNG exportieren:**
1. Menü: File → Export as → PNG
2. Wählen Sie die Auflösung (z.B. 300 DPI für Druck, 100 DPI für Web)
3. Klicken Sie auf "Export"

**Als neues SVG exportieren:**
1. Menü: File → Export as → SVG
2. Aktivieren Sie "Include a copy of my diagram" falls Sie es später wieder bearbeiten möchten
3. Klicken Sie auf "Export"

## Import in Microsoft Visio

### Direkt-Import (empfohlene Methode)

Microsoft Visio kann draw.io-Dateien direkt importieren:

1. Öffnen Sie Microsoft Visio
2. Menü: Datei → Öffnen
3. Wählen Sie "Alle Dateien (*.*)" im Dateityp-Filter
4. Navigieren Sie zu `Inspektionsablauf.drawio`
5. Klicken Sie auf "Öffnen"
6. Visio importiert das Diagramm automatisch

**Hinweis:** Der Import funktioniert ab Visio 2013. Bei älteren Versionen verwenden Sie die Alternative unten.

### Alternative: Über SVG

Falls der Direkt-Import nicht funktioniert:

1. Öffnen Sie `Inspektionsablauf.drawio` in draw.io (siehe oben)
2. Exportieren Sie als SVG: File → Export as → SVG
3. Öffnen Sie Visio
4. Menü: Datei → Öffnen → wählen Sie die SVG-Datei
5. Visio konvertiert das SVG automatisch in Visio-Shapes

**Tipp:** Nach dem Import in Visio können Sie die Shapes weiterbearbeiten. Bei SVG-Import sind einige Shapes möglicherweise gruppiert — verwenden Sie "Gruppierung aufheben" um einzelne Elemente zu bearbeiten.

## Grundlage

Dieses Flowchart basiert auf folgenden Normen und Rechtsgrundlagen:

- **SN EN 1176-7:2020** — Spielplatzgeräte und Spielplatzböden, Teil 7: Anleitung für Installation, Inspektion, Wartung und Betrieb
- **SIA 118** — Allgemeine Bedingungen für Bauarbeiten (Bauabnahme)
- **CEN/TR 17207** — Technischer Report zur Mängelklassifizierung
- **Art. 58 OR** — Werkeigentümerhaftung (Schweizer Obligationenrecht)

### Inspektionsfrequenzen gemäss SN EN 1176-7

| Inspektionstyp | Frequenz | Norm-Referenz |
|----------------|----------|---------------|
| **Sichtkontrolle** (Visuelle Routineinspektion) | Wöchentlich | SN EN 1176-7, 6.1b |
| **Funktionskontrolle** (Operative Inspektion) | Pro Quartal (alle 3 Monate) | SN EN 1176-7, 6.1c |
| **Jahreshauptinspektion** | Jährlich | SN EN 1176-7, 6.1d |
| **Inspektion nach Installation** | Bei neuen Spielplätzen | SN EN 1176-7, 6.1a |

### Schweregrade für Mängel

Gemäss CEN/TR 17207:

- **Konform** — Keine Massnahme nötig, nur Dokumentation
- **Empfohlen** — Reparatur empfohlen, aber keine unmittelbare Gefahr
- **Wichtig** — Reparatur innerhalb einer angemessenen Frist erforderlich
- **Dringend** — Sofortige Sperrung, unmittelbare Gefahr für Benutzer

## Technische Hinweise

### Mermaid-Datei (für Entwickler)

Die Datei `Inspektionsablauf.md` enthält den Quellcode des Diagramms im Mermaid-Format. Mermaid ist eine Markup-Sprache für Diagramme, die in vielen technischen Dokumentationen verwendet wird.

**Verwendung:**
- Einbetten in Markdown-Dokumentationen (GitHub, GitLab, Confluence, etc.)
- Rendern mit Mermaid CLI: `mmdc -i Inspektionsablauf.md -o output.svg`
- Live-Editor: https://mermaid.live

**Hinweis:** Die Mermaid-Datei ist vor allem für technische Nutzer gedacht, die das Diagramm in ihre Dokumentation einbetten oder programmatisch verarbeiten möchten. Für normale Bearbeitungen verwenden Sie bitte die draw.io-Datei.

### SVG-Datei

Die SVG-Datei ist eine Vektor-Grafik, die in jedem modernen Browser geöffnet werden kann:

- **Im Browser öffnen:** Doppelklicken Sie auf `Inspektionsablauf.svg`
- **In Dokumente einfügen:** Drag & Drop in Word, PowerPoint, InDesign, etc.
- **Drucken:** SVG ist verlustfrei skalierbar — ideal für Poster und Drucke in beliebiger Grösse

**Limitation:** SVG ist nicht direkt editierbar. Für Änderungen verwenden Sie die draw.io-Datei und exportieren Sie neu.

## Kontakt

**PSP — Playground Safety Partner**

Für Fragen zur Anwendung dieses Flowcharts oder zu Spielplatz-Inspektionen wenden Sie sich bitte an:

- E-Mail: [Ihre Kontakt-E-Mail]
- Telefon: [Ihre Kontakt-Telefonnummer]
- Website: [Ihre Website]

---

**Letzte Aktualisierung:** Februar 2026
**Version:** 1.0
**Lizenz:** [Ihre Lizenzinformationen]
