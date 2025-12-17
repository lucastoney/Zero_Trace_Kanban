# ADR-0010: GUI-Basisframework für den MVP

**Status:** Proposed  
**Datum:** 2025-12-03  
**Autor(en):** SAG / Alle  
**Betroffene Bereiche:** UI/UX, Architektur, Packaging/Deployment, Wartbarkeit

---

## 🎯 1. Kontext

ZeroTrace benötigt für den MVP eine lokale GUI (vgl. ADR-0005), die folgende Anforderungen erfüllt:
- Scan-Auswahl (Netzwerkscan / Portscan / kombiniert)
- Berechtigungsbestätigung (Checkbox) vor Start
- Statusanzeige „Scan läuft“ + Erfolg/Fehler nach Abschluss
- Tabellarische Ergebnisanzeige (Host, offene Ports, Risk Level)
- Export-Anstoss (z. B. PDF/HTML) über Backend (vgl. ADR-0009)
- Betrieb **lokal** unter Windows (vgl. ADR-0004)

Rahmenbedingungen:
- Programmiersprache Python ist gesetzt (vgl. ADR-0002)
- Zeitlimit im MVP → geringes Setup- und Integrationsrisiko
- Team-Kompetenzen in App-/UI-Entwicklung sind begrenzt → pragmatischer Ansatz nötig

Warum Entscheidung nötig:
- Ein GUI-Framework beeinflusst Umsetzungsgeschwindigkeit, Packaging und Wartbarkeit.
- Es muss ein Framework gewählt werden, das zuverlässig lokal läuft und die MVP-UI-Funktionen abdeckt.

Risiken/Einschränkungen:
- DSGVO-/Security-Kontext: keine Cloud-Dependencies erzwingen, keine unnötige Telemetrie
- Packaging muss später möglich sein (z. B. als ausführbares Paket)

---

## ⚖️ 2. Entscheidung

🟩 **Wir entscheiden uns für:**  
> **Tkinter** als GUI-Basisframework für den MVP (Python Standardbibliothek).

---

## 🧠 3. Begründung

| Argument | Beschreibung |
|----------|--------------|
| ✓ MVP-Tempo | Tkinter ist sofort verfügbar (keine zusätzliche Installation), sehr gut für schnelle MVP-Iteration. |
| ✓ Lokaler Betrieb | Läuft stabil lokal unter Windows; passt zum Betriebskonzept „local-only“. |
| ✓ Einfaches Konzept | Genügend für Formulare, Buttons, Checkbox, Statusanzeigen und Tabellen (z. B. `ttk.Treeview`). |
| ✓ Geringes Projektrisiko | Weniger Abhängigkeiten → weniger Setup-/Packaging-Probleme im MVP. |
| ⚠ Nachteil | Look & Feel wirkt weniger modern; komplexe UI-Patterns sind eingeschränkter als bei PyQt. |
| 🔄 Abwägung | Für MVP zählt Funktionsnachweis (Scan/Resultate/Export). „Polish“ ist nachgelagert und kann später via Framework-Wechsel erfolgen, wenn nötig. |

---

## 🔁 4. Alternativen (evaluierte Optionen)

| Alternative | Warum verworfen? |
|-------------|------------------|
| PyQt / PySide | Mächtiger, aber höherer Setup-/Packaging-Aufwand; potenziell mehr Overhead im MVP. |
| Kivy | Andere UI-Philosophie, zusätzliche Abhängigkeiten; für klassischen Desktop-MVP unnötig komplex. |
| Web-UI lokal (Flask + Browser) | Technisch möglich, aber erhöht Architektur- und Betriebskomplexität (lokaler Server, Browser-Interaktion, Security-Headers etc.). |
| PySimpleGUI | Einfach, aber abhängig von darunterliegendem Framework und Lizenz-/Support-Themen je nach Version; für MVP weniger „Standard“ als Tkinter direkt. |

---

## 📊 5. Auswirkungen

### Positiv
- Schneller Start der GUI-Implementierung (ADR-0005 umsetzbar)
- Weniger Abhängigkeiten im MVP → stabilere Entwicklung
- Gute Passung zur Trennung GUI/Backend (ADR-0009)

### Negativ / Risiken
- UI kann weniger „modern“ wirken
- Bei späteren Anforderungen (z. B. komplexe Layouts, dynamische Filter, Charts) könnte ein Wechsel nötig werden

### Offene Punkte
- Definition der finalen UI-Struktur (Views/Komponenten, Navigation)
- Standardisierung der UI-Elemente (Farblogik + Labels, nicht nur Farbe)
- Packaging-Konzept (z. B. PyInstaller) und Test auf Ziel-Windows

---

## 🔐 6. Sicherheits- & Datenschutzrelevanz

- Tkinter erfordert keine Cloud-Services oder Telemetrie.
- Passt zum „Local-only“-Ansatz (ADR-0004).
- UI soll klar kommunizieren: Berechtigungsbestätigung + Hinweise zu Scan-Verantwortung.

---


