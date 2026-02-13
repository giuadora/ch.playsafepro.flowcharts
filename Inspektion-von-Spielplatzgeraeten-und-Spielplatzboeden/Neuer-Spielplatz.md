# Neuer Spielplatz: Ablaufdiagramm

**Grundlage:** SN EN 1176-7:2020 – Anleitung für Installation, Inspektion, Wartung und Betrieb

**Zweck:** Dieses Flowchart zeigt den Ablauf für die Inbetriebnahme eines neuen Spielplatzes gemäss SN EN 1176-7. Es umfasst Bauabnahme, Inspektion nach Installation, Mängelbehandlung und Übergang zum regulären Inspektionszyklus.

---

```mermaid
flowchart TD
    %% === NEUER SPIELPLATZ (BLUE) ===
    START(["Spielplatz-Inspektionen"])
    N01["Bauabnahme nach SIA 118¹<br/>Vertragliche Abnahme<br/>durch Architekt/Bauleiter"]
    N02["Inspektion nach Installation²<br/>Sicherheitsprüfung durch<br/>zertifizierte Fachperson"]
    D02{"Mängel<br/>festgestellt?"}
    N03["Mängel an Ersteller/<br/>Hersteller zurück<br/>zur Behebung"]
    N04(["Spielplatz eröffnen"])
    IPLAN[["Inspektionsplan erstellen³"]]

    START --> N01
    N01 --> N02
    N02 --> D02
    D02 -->|"Ja"| N03
    D02 -->|"Nein"| N04
    N03 -.->|"Nachbesserung"| N02
    N04 -->|"Spielplatz in Betrieb"| IPLAN

    %% === TRANSITION TO INSPECTION CYCLE (GREEN) ===
    E00(["Inspektionszyklus<br/>beginnen"])
    IPLAN --> E00

    %% === STYLING ===
    classDef startend fill:#E9ECEF,stroke:#6C757D,color:#495057
    classDef newpath fill:#D6E4F0,stroke:#2B579A,color:#2B579A
    classDef inspection fill:#DFF0D8,stroke:#3C763D,color:#3C763D
    classDef defect fill:#FFF3CD,stroke:#856404,color:#856404

    class START,N04,E00 startend
    class N01,N02,D02,IPLAN newpath
    class N03 defect
```

---

## Fussnoten

**¹ SIA 118** — Vertragliche Bauabnahme, ersetzt nicht die Sicherheitsinspektion

**² SN EN 1176-7, 6.1a** — Inspektion nach Installation

**³ SN EN 1176-7, 6.2.4** — Inspektionsplan

---

## Verwendung

Dieses Mermaid-Diagramm kann mit [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli) in andere Formate konvertiert werden:

```bash
mmdc -i Neuer-Spielplatz.md -o Neuer-Spielplatz-mermaid.svg
mmdc -i Neuer-Spielplatz.md -o Neuer-Spielplatz-mermaid.png
```

Oder direkt in Markdown-Viewer mit Mermaid-Support (GitHub, GitLab, Obsidian, etc.) anzeigen.
