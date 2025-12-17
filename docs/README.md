# 📁 Dokumentationsverzeichnis – Übersicht & Beschreibung

Dieses Dokument beschreibt die Struktur des Ordners `docs/` und erläutert den Zweck jedes enthaltenen Verzeichnisses und jeder wichtigen Datei.  
Es dient zur Orientierung für Entwickler, Prüfer und Projektbeteiligte.

---

## 📌 Hauptdokument

### `README.md`
Startpunkt der Dokumentation. Hier sollte eine kurze Einführung stehen sowie Hinweise, welche Dokumententeile für wen relevant sind und in welcher Reihenfolge sie gelesen werden sollten.

---

## 🧩 Einleitung

### `introduction/`
Beinhaltet grundlegende Informationen über das Projekt.

| Datei | Beschreibung |
|-------|--------------|
| `problem-statement.md` | Definiert das zentrale Problem und die Zielsetzung des Projekts. |
| `scope.md` | Definiert den Projektumfang – was enthalten ist und was bewusst nicht. |
| `glossary.md` | Erklärt wichtige Fachbegriffe, Systembegriffe und Projektspezifika. |

---

## 🏛 Architektur

### `architecture/`
Dokumentiert die technische Struktur und den Aufbau des Systems.

| Datei | Beschreibung |
|-------|--------------|
| `system-overview.md` | Überblick über das System und die architektonischen Ziele. |
| `context-diagram.md` | Darstellung der Systemumgebung und externen Interaktionen. |
| `component-diagram.md` | Übersicht über die Softwarekomponenten und Module. |
| `data-flow.md` | Beschreibung des Datenflusses – insbesondere relevant für Zero Trace. |
| `sequence-diagrams.md` | Ablaufdiagramme einzelner Use Cases (z. B. „Start Session“). |
| `gui-design.md` | Darstellung der GUI-Konzeption inkl. Screenshots. |
| `concurrency-and-security.md` | Dokumentation von Zugriffskonzepten, Datenschutz und parallelen Abläufen. |

---

## 🔐 Datenschutz & Compliance

### `privacy-and-compliance/`
Behandelt Datenschutz, Sicherheitsaspekte und gesetzliche Anforderungen (z. B. DSGVO).

| Datei | Beschreibung |
|-------|--------------|
| `zero-trace-concept.md` | Erläuterung, wie das System ohne dauerhafte Datenspeicherung arbeitet. |
| `data-lifecycle.md` | Darstellung des Lebenszyklus von Daten (Entstehung, Nutzung, Vernichtung). |
| `risk-analysis.md` | Analyse möglicher Risiken im Kontext von Datenschutz und Sicherheit. |
| `gdpr-analysis.md` | Abgleich mit DSGVO-Vorgaben (z. B. Rechte, Aufbewahrung, Löschung). |
| `secure-deletion.md` | Konzept zum sicheren Löschen von Daten (auch temporär). |

---

## 🧠 Architekturentscheidungen

### `adr/` – *Architecture Decision Records*
Dient zur Dokumentation wesentlicher Architekturentscheidungen.

| Datei | Beschreibung |
|-------|--------------|
| `0001-zero-trace-strategy.md` | Entscheidung für das Zero-Trace-Konzept. |
| `0002-storage-model.md` | Entscheidung über die Speicherstrategie (RAM-only). |
| `TEMPLATE.md` | Vorlage zur Erstellung weiterer ADRs. |

---

## 📌 Anforderungen

### `requirements/`
Dokumentiert Anforderungen an das System.

| Datei | Beschreibung |
|-------|--------------|
| `functional-requirements.md` | Funktionale Anforderungen – was die Anwendung leisten muss. |
| `non-functional-requirements.md` | Anforderungen an Sicherheit, Performance und Datenschutz. |
| `use-cases.md` | Use-Case-Beschreibungen und Diagramme. |
| `acceptance-criteria.md` | Kriterien zur Abnahme bzw. Bewertung des Projekts. |

---

## 🧪 Testdokumentation

### `testing/`
Beinhaltet Informationen zur Teststrategie und zur Testdurchführung.

| Datei | Beschreibung |
|-------|--------------|
| `test-strategy.md` | Vorgehensweise beim Testen. |
| `test-cases.md` | Auflistung der durchgeführten Testfälle. |
| `test-report.md` | Dokumentation der Testergebnisse. |
| `coverage-report.md` | Testabdeckungsbericht (ggf. mit IDE-Screenshots). |

---

## 👤 Benutzerdokumentation

### `user-guide/`
Dient Endbenutzern und Prüfern zur Nutzung der Anwendung.

| Datei | Beschreibung |
|-------|--------------|
| `installation.md` | Anleitung zur Einrichtung / Installation. |
| `gui-usage.md` | Bedienungsanleitung inkl. Screenshots. |
| `troubleshooting.md` | Hilfestellungen bei Fehlerszenarien. |

---

## 🎤 Präsentation

### `presentation/`
Unterstützt die Vorbereitung der Abschlusspräsentation.

| Datei | Beschreibung |
|-------|--------------|
| `pitch-outline.md` | Struktur und Ablauf der Präsentation. |
| `summary-handout.md` | Zusammenfassung zentraler Inhalte für Prüfer. |
| `poster-design.md` | Optionales Poster / Infografik, falls gefordert. |

---

## 📍 Empfohlene Lesereihenfolge für Prüfer

1. `introduction/problem-statement.md`
2. `requirements/functional-requirements.md`
3. `architecture/system-overview.md`
4. `privacy-and-compliance/zero-trace-concept.md`
5. `adr/0001-zero-trace-strategy.md`
6. `testing/test-strategy.md`
7. `presentation/pitch-outline.md`

---

## 📅 Letzte Aktualisierung

*22.11.2025*  
👤 Verantwortlich: *Thines Rasiah*

---

## 🟢 Fazit

Die Dokumentation ist so strukturiert, dass sie:

✔ technisch klare Architektur vermittelt  
✔ das Zero-Trace-Konzept nachvollziehbar erklärt  
✔ Bewertungskriterien direkt unterstützt  
✔ Benutzerfreundlichkeit & Präsentation integriert

---