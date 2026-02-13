# Bestehender Spielplatz: Ablaufdiagramm

**Grundlage:** SN EN 1176-7:2020 – Anleitung für Installation, Inspektion, Wartung und Betrieb

**Zweck:** Dieses Flowchart zeigt den wiederkehrenden Inspektionszyklus für bestehende Spielplätze gemäss SN EN 1176-7. Es umfasst die drei Inspektionstypen, Berichterstattung, Archivierung und Instandhaltungs-Management.

---

```mermaid
flowchart TD
    %% === INSPECTION CYCLE (GREEN) ===
    E00(["Inspektionszyklus<br/>beginnen"])
    E01["Visuelle Routine-Inspektion³<br/>- Sichtprüfung auf<br/>offensichtliche Gefahren"]
    E02["Operative Inspektion⁴<br/>- Funktionsprüfung,<br/>Verschleiss, Stabilität"]
    E03["Jährliche Hauptinspektion⁵<br/>- Umfassende Prüfung durch<br/>zertifizierte Fachperson"]
    E04[/"Inspektionsbericht<br/>erstellen"/]

    E00 -->|"wöchentlich"| E01
    E00 -->|"quartalsweise"| E02
    E00 -->|"jährlich"| E03
    E01 --> E04
    E02 --> E04
    E03 --> E04

    %% NOTE: CEN/TR 17207 annotation (not rendered as node, for documentation only)
    %% "Festgestellte Mängel sind im Bericht nach CEN/TR 17207⁷ zu klassifizieren"
    %% Connected to E04 via dashed line in draw.io

    %% === POST-INSPECTION PROCESS ===
    P01["Bericht archivieren⁶"]
    IHM[["Instandhaltungs-Management"]]

    E04 --> P01
    P01 --> IHM

    %% === END (GRAY) ===
    END(["Nächster Inspektionszyklus<br/>gemäss Zeitplan⁸"])

    IHM --> END
    END -.-> E00

    %% === STYLING ===
    classDef startend fill:#E9ECEF,stroke:#6C757D,color:#495057
    classDef inspection fill:#DFF0D8,stroke:#3C763D,color:#3C763D

    class END startend
    class E00,E01,E02,E03,E04,P01,IHM inspection
```

---

## Fussnoten

**³ SN EN 1176-7, 6.1b** — Visuelle Routineinspektion

**⁴ SN EN 1176-7, 6.1c** — Operative Inspektion

**⁵ SN EN 1176-7, 6.1d** — Jährliche Hauptinspektion

**⁶ SN EN 1176-7, 8.2.2** — Dokumentationspflicht

**⁷ CEN/TR 17207** — Mängelklassifizierung (im Inspektionsbericht anzuwenden)

**⁸ SN EN 1176-7, 6.2.4** — Inspektionsplan

---

## Verwendung

Dieses Mermaid-Diagramm kann mit [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli) in andere Formate konvertiert werden:

```bash
mmdc -i Bestehender-Spielplatz.md -o Bestehender-Spielplatz-mermaid.svg
mmdc -i Bestehender-Spielplatz.md -o Bestehender-Spielplatz-mermaid.png
```

Oder direkt in Markdown-Viewer mit Mermaid-Support (GitHub, GitLab, Obsidian, etc.) anzeigen.
