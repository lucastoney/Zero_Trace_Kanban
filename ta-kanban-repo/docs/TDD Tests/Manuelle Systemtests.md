# Systemtests ZeroTrace (End-to-End)

Diese Datei enthält die vollständige Systemtest-Tabelle für ZeroTrace.  
Die Tests prüfen das gesamte System (GUI ↔ Backend ↔ Nmap ↔ PDF).
---
## Übersicht

- Testebene: **Systemtest (E2E)**
- Ziel: Sicherstellen, dass ZeroTrace als vollständige Anwendung korrekt funktioniert.
- Besonderheit: Systemtests können nicht vollständig automatisiert werden (Nmap + GUI), daher manuell und sie sollen von einer "externen Person" durchgeführt werden.
---

## Hinweise zur Durchführung

- Die hier aufgeführten Tests sollten nach "grossen Änderungen" stehts wiederholt werden
- Ergebnisse dokumentieren (✓/✗) und ggf. Screenshots anhängen.
- Kritische Fehler (Nmap-Aufruf, PDF-Report, falsche Ergebnisse) immer sofort beheben!!
---
## Abschluss

Mit dieser Systemtest-Suite kann ZeroTrace vollständig bewertet werden:

- technische Funktionalität  
- Benutzerführung  
- Stabilität  
- Datenschutzrelevante Mechanismen  

Sie ergänzt die Unit- und Integrationstests und bildet das „große Bild“ der Anwendung ab.


# Systemtests Zero Trace Tests 

| TS-ID     | Bereich            | Beschreibung                         | Vorbedingungen        | Schritte                       | Erwartetes Ergebnis                                                   | Erledigt | Verantwortlich |
| --------- | ------------------ |--------------------------------------| --------------------- | ------------------------------ | --------------------------------------------------------------------- | -------- | -------------- |
| **TS-01** | Startverhalten     | GUI startet fehlerfrei               | App + venv            | Starten                        | Oberfläche lädt komplett                                              | ☐        |                |
| **TS-02** | DSG-Validierung    | Scans ohne DSG komplett blockiert    | GUI gestartet         | Net-Scan wählen → Start        | Meldung: „Bitte bestätigen…“                                          | ☐        |                |
| **TS-03** | Netzwerkscan E2E   | Host(s) werden gefunden              | Nmap & Testnetz       | Netz eingeben → Start          | Tabelle enthält aktive Hosts                                          | ☐        |                |
| **TS-04** | Netzwerkscan leer  | Keine Hosts im Netz                  | leeres Testnetz       | Netz eingeben → Start          | Meldung: „Keine passenden Hosts gefunden“                             | ☐        |                |
| **TS-05** | Portscan E2E       | Offener Port erkannt                 | Testhost mit Port 80  | IP eingeben → Portscan → Start | Spalte „Offene Ports“ zeigt „80“                                      | ☐        |                |
| **TS-06** | Custom Scan        | Netzwerk + Port kombiniert           | beide Scanarten aktiv | Start                          | Ports + Netzwerkdaten sinnvoll gemerged                               | ☐        |                |
| **TS-07** | Fortschritts-Popup | „Scan läuft“-Popup erscheint         | Scan starten          | Scan auslösen                  | Popup erscheint, blockiert Eingaben, verschwindet nach Fertigstellung | ☐        |                |
| **TS-08** | Validierung        | Portscan ohne Ports                  | Ports leer            | Start                          | Warnung angezeigt                                                     | ☐        |                |
| **TS-09** | Nmap-Fehler        | Nmap fehlt                           | Nmap umbenannt        | Start                          | Meldung: „Nmap wurde nicht gefunden…“                                 | ☐        |                |
| **TS-10** | PDF-Export         | PDF korrekt generiert                | Scan abgeschlossen    | „PDF-Report erstellen“         | PDF enthält richtige Daten                                            | ☐        |                |
| **TS-11** | PDF-Dateiname      | Automatisch generierter Name korrekt | Scan abgeschlossen    | PDF speichern                  | `Netzwerkscan_YYYYMMDD_HHMMSS.pdf`                                    | ☐        |                |
| **TS-12** | Tabelleninhalt     | GUI zeigt Daten korrekt              | Scan abgeschlossen    | Tabelle prüfen                 | IP, Hostname, Ports, Kommentar korrekt                                | ☐        |                |
| **TS-13** | UX Logik           | Buttons korrekt disabled             | Startzustand          | DSG nicht aktiv                | Scan-Button disabled                                                  | ☐        |                |
| **TS-14** | Stabilität         | App crasht bei Fehlinput nicht       | ungültige Eingaben    | z. B. CIDR „abc“ → Scan        | Fehlermeldung statt Crash                                             | ☐        |                |
