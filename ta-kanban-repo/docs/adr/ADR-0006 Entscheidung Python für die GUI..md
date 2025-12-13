# ADR <Nummer>: <Titel der Entscheidung>

*Status:* Proposed / Accepted / Rejected / Superseded  
*Datum:* YYYY-MM-DD  
*Autor:* <Name / Team>  
*Betroffene Bereiche:* Architektur / Security / Performance / Datenschutz / UX / etc.

---

## 🎯 1. Kontext

Für das Projekt „Zero Trace“ wird eine grafische Benutzeroberfläche benötigt, die folgende Anforderungen erfüllt:

•	schnelle Entwicklung und iterative Anpassungen

•	moderne, benutzerfreundliche Oberfläche

•	geringer Ressourcenbedarf

•	einfache Installation und Nutzung auf Windows-Systemen

•	langfristige Erweiterbarkeit (Scanner, Reports, Logging, DSG-Konformität)

Im Vergleich zu komplexeren Frameworks (C#, Web-UI) soll die Technologie leichtgewichtig, flexibel und kosteneffizient sein.

---

## ⚖️ 2. Entscheidung

Die GUI wird mit Python und dem integrierten GUI-Framework Tkinter entwickelt.

Vorteile:

•	sehr geringe Einstiegshürde für Entwickler

•	schneller Entwicklungszyklus

•	keine komplizierten Build-Prozesse

•	einfache Testing-Umgebung

Damit entfallen:

•	externe Installationspakete

•	Lizenzkosten

Multi-Platform Support ohne Mehraufwand:

Ohne Anpassung läuft die GUI auf:

•	Windows

•	Linux

•	macOS

Einfache Erstellung eines .exe-Pakets für Endanwender:

Mit pyinstaller können wir aus der GUI exe erstellen:

•	ohne Installation von Python

•	ohne technische Kenntnisse des Users

•	ideal für Endanwender in Firmen

---

## 🧠 3. Begründung

Warum ist diese Entscheidung richtig?

Gründe für Python sind:

•	Python ist schnell und kosteneffizient entwickelbar

•	Python ermöglicht schnelle Iterationen.

Gründe für Tkinter ist:

•	bereits in jeder Standard-Python-Installation enthalten

•	sehr ressourcenschonend

•	auf Windows gut integriert

•	zuverlässig und bewährt seit vielen Jahren

## 🔁 4. Alternativen (evaluierte Optionen)

---

**C#**

•	professionelles Windows-Ui

•	sehr viel Entwicklungsaufwand

•	nur Windows

•	komplexere Build-Umgebungen

**Electron / Web-GUI**

•	sehr modern

•	extrem hoher Ressourcenverbrauch

•	100–300 MB Runtime

## 📊 5. Auswirkungen

### Positiv
•	schnelle Weiterentwicklung

•	modernisierbare Oberfläche

•	kompatibel mit zukünftiger Scan-Engine

•	einfaches Deployment

•	minimaler Ressourcenverbrauch

•	hohe Wartbarkeit

### Negativ / Risiken

  •	Tkinter ist funktional, aber visuell weniger modern als Qt/Electron 

  •	für extrem komplexe GUIs weniger geeignet

### Offene Punkte
- Keine

---

## 🔎 6. Entscheidung gültig für

Python + Tkinter ist die gewählte Technologie für die Zero-Trace-GUI,
basierend auf:

•	Entwicklungs¬geschwindigkeit

•	Flexibilität

•	Ressourceneffizienz

•	einfacher Distribution

•	Kompatibilität mit Netzwerk und Security-Modulen

•	DSG-konformer Integrationsfähigkeit


