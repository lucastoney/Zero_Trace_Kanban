# 📁 Projektstruktur – Zero Trace App

Dieses Dokument beschreibt die Ordnerstruktur des Projekts und erläutert den Zweck jedes Verzeichnisses.  
Es dient der Orientierung für Entwickler, Prüfer und alle Projektbeteiligten.

---

## 📦 Hauptverzeichnisse

| Ordner | Beschreibung |
|--------|--------------|
| `src/` | Haupt-Quellcode der Anwendung. Enthält die komplette Implementierung der Zero Trace Applikation. |
| `tests/` | Testcode zur Verifikation der Funktionalitäten und Sicherheitsanforderungen. |
| `docs/` | Technische und fachliche Projektdokumentation, inkl. Architektur, Anforderungen, Datenschutz und Präsentation. |
| `config/` | Konfigurationsdateien (nicht sensibel), z. B. Entwicklungs- oder Produktionsprofile. |
| `scripts/` | Hilfsskripte für Entwicklung, Test und Bereinigung (z. B. Zero Trace Clean-Up). |
| `.env.example` | Vorlage für Umgebungsvariablen (z. B. Laufzeitkonfigurationen – ohne sensible Daten). |
| `pyproject.toml` / `setup.cfg` | Konfigurationsdateien für Build- und Projektmanagement in Python. |
| `README.md` | Einstiegspunkt für Entwickler (z. B. wie man das Projekt startet). |
| `LICENSE` | Lizenzdokument (optional, falls benötigt). |

---

## 📂 `src/zerotrace_app/` – Hauptanwendung

| Unterordner / Datei | Zweck |
|--------------------|-------|
| `main.py` | Einstiegspunkt der Anwendung (Start der GUI). |
| `gui/` | Grafische Benutzeroberfläche der Applikation. Enthält Views (Fenster), Controller (Logik) und Widgets. |
| `core/` | Kernlogik / Geschäftslogik, z. B. Models, Services und Privacy-Policies. |
| `security/` | Implementierung von Sicherheits- und Datenschutzfunktionen (z. B. Verschlüsselung, Wipe). |
| `storage/` | Zero Trace Speicherstrategien (RAM-only, temporäre Dateien, Konfigurationsspeicher). |
| `config/` | Zentrale Konfiguration der Anwendung inkl. Profile (secure/debug) und Default-Werte. |
| `utils/` | Hilfsfunktionen wie Pfade oder Logging-Stub (kein Logging in Produktivbetrieb). |

---

## 🧠 Detail: Wichtige Module

### 🔐 `security/`
| Datei | Zweck |
|------|-------|
| `crypto.py` | Verschlüsselung & Schlüsselverwaltung. |
| `wiping.py` | Sicheres Löschen (z. B. Überschreiben temporärer Daten). |
| `audit.py` | Minimaler Audit-Mechanismus (in-memory, optional). |

### 💾 `storage/`
| Datei | Zweck |
|------|-------|
| `in_memory_store.py` | Speichert Daten ausschließlich im RAM. |
| `temp_store.py` | Optional temporäre Speicherung (z. B. bei Verarbeitung), wird beim Beenden gelöscht. |
| `config_store.py` | Lesen von Konfiguration (keine sensiblen Inhalte). |

---

## 🧪 `tests/`

Dieser Ordner enthält automatisierte Tests und ist nach Funktionalität der Anwendung gegliedert:

| Unterordner | Beschreibung |
|-------------|--------------|
| `test_gui/` | Tests der Benutzeroberfläche. |
| `test_core/` | Tests der Geschäftslogik. |
| `test_security/` | Tests der Sicherheits- und Zero-Trace-Funktionen. |
| `test_storage/` | Tests zur Datenhaltung (RAM-only & Clean-Up). |

---

## 📚 `docs/` – Dokumentation

Strukturiert nach Themenbereichen für Transparenz bei der Bewertung.

| Unterordner | Inhalt |
|-------------|--------|
| `introduction/` | Problemdefinition, Projektscope und Glossar. |
| `architecture/` | Gesamtarchitektur, Systemkontext, Komponenten, Datenfluss und Sequenzdiagramme. |
| `privacy-and-compliance/` | Zero Trace Konzept, DSGVO-Analyse, Datenlebenszyklus, Risikobewertung, sicheres Löschen. |
| `adr/` | Architekturentscheidungen (z. B. Zero Trace Strategie). |
| `requirements/` | Funktionale & nicht-funktionale Anforderungen, Use Cases, Abnahmekriterien. |
| `testing/` | Teststrategie, Testfälle, Ergebnisse und Coverage. |
| `user-guide/` | Installations- und Benutzeranleitung, Troubleshooting. |
| `presentation/` | Inhalte für Abschlusspräsentation (Pitch, Handout, Poster). |

---

## ⚙ `config/`

| Datei | Beschreibung |
|-------|--------------|
| `dev.yml` | Konfiguration für Entwicklungsmodus. |
| `prod.yml` | Produktiv-Konfiguration (ohne Debug-Funktionen). |
| `logging-dev.yml` | Logging-Einstellungen für Entwicklung (nicht für Produktion). |

---

## ▶ `scripts/`

| Datei | Beschreibung |
|-------|--------------|
| `run_dev.sh` | Startet Anwendung im Entwicklungsmodus. |
| `run_tests.sh` | Führt automatisierte Tests aus. |
| `clean_temp.py` | Löscht potenzielle Rückstände (Zero Trace Clean-Up). |

---

## 🔍 Bewertungshinweise

| Prüfkriterium | Nachweis (Ort) |
|---------------|----------------|
| Problemverständnis | `docs/introduction/problem-statement.md` |
| Technische Architektur | `docs/architecture/system-overview.md` |
| Zero Trace Umsetzung | `docs/privacy-and-compliance/zero-trace-concept.md`, `src/storage/`, `src/security/` |
| Architekturentscheidungen | `docs/adr/0001-zero-trace-strategy.md` |
| Testnachweise | `docs/testing/`, `tests/` |
| Benutzererfahrung | `docs/user-guide/gui-usage.md`, Screenshots |
| Präsentationsvorbereitung | `docs/presentation/` |

---

## 📌 Letzte Aktualisierung

`22.11.2025`  
👤 *Erstellt von:* `Thines Rasiah`

---

## 🎯 Empfehlung

- Bei Änderungen an der Struktur **dieses Dokument ebenfalls aktualisieren**.
- Prüfer sollten mit diesem Dokument beginnen, bevor sie Code oder restliche Dokumentation sichten.
---
