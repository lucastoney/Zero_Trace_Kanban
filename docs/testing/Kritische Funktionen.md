# Kritische Funktionen in ZeroTrace – Definition

ZeroTrace ist ein lokal ausgeführtes Security-Scanning-Tool.  
Kritische Funktionen sind alle Bestandteile der Anwendung, deren Fehler Auswirkungen auf folgendes haben:

- **Sicherheit**
- **Richtigkeit der Ergebnisse**
- **Datenschutz (DSG / DSGVO)**
- **Benutzervertrauen**
- **Stabilität des Systems**

Die folgenden Funktionsbereiche gelten als kritisch:
---
## 1. Scan-Auslösung & Berechtigung

### 1.1 DSG-Bestätigung
- Der Scan darf nur ausgeführt werden, wenn der Benutzer ausdrücklich bestätigt, dass:
  - die Durchführung berechtigt ist  
  - die gesetzlichen Grundlagen (DSG / DSGVO) eingehalten werden

### 1.2 Auswahl des Scan-Modus
- Netzwerkscan, Port-Scan oder benutzerdefinierter Scan.
- Entscheidung, welche Parameter verwendet werden.
- Fehler führen zu unerwünschten Netzwerkanfragen.
---
## 2. Scan-Durchführung (Backend)

### 2.1 Korrekte Ausführung von Nmap
- Aufruf mit korrekten Parametern.
- Fehlerhafte Parameter → falsche oder "gefährliche" Scans.

### 2.2 Verarbeitung der Nmap-Ergebnisse
- XML parsing für:
  - IP-Adressen
  - Hostnamen
  - Zustand (up/down)
  - Ports (open/closed)
- Parsing-Fehler führen zu falschen Ergebnissen, was sicherheitsrelevant ist.

### 2.3 Handling von Fehlerfällen
- Nmap nicht installiert → klare Fehlermeldung.
- Ungültiges Netzwerkformat → kontrollierter Abbruch.
- Keine Scans ohne gültige Eingabeparameter!!!
---
## 3. Ergebnisdarstellung (GUI)

### 3.1 Darstellung der ScanResult-Daten
- Falsche Abbildung zwischen Backend und GUI führt zu:
  - irreführenden Ergebnissen
  - falscher Risikobewertung

### 3.2 Benutzerfeedback / Status
- Popup „Scan läuft…“ verhindert Fehleingaben.
- Statusbar zeigt die Scanart und Fortschritt an.
- Fehler führen zu unklaren Systemzuständen.
---
## 4. PDF-Report (Exportfunktion erst einzel)

### 4.1 Korrekte Erstellung des Reports
- Exportierte PDF muss alle Informationen richtig abbilden:
  - IP-Adresse
  - Hostname
  - Offene Ports
  - Kommentar
  - Scan-Typ
  - Datum und Kontext

### 4.2 Dateibenennung
- Automatische Erstellung eines nachvollziehbaren Namens:
  - `Netzwerkscan_YYYYMMDD_HHMMSS.pdf`

### 4.3 Fehlerhandling
- Fehlendes Reportlab → verständliche Fehlermeldung.
- Kein Export trotz gültiger Daten darf nicht vorkommen.
---
## 5. Lokalität der Verarbeitung

### 5.1 Keine externen Netzwerkverbindungen
- ZeroTrace MUSS ausschließlich lokal scannen.
- Es dürfen **keine Daten an Cloud oder Externe** gesendet werden.
---
## Zusammenfassung

Die kritischen Funktionen umfassen:
- Scan-Auswahl & Berechtigung
- Durchführung der Scans
- Verarbeitung der Ergebnisse
- Erstellung der Reports
- Wahrung des Datenschutzes
- Keine unerwünschten externen Datenflüsse

Alle diese Bereiche sind durch TDD-Tests, Integrations-Tests und manuelle Systemtests abgesichert.



# Kritische Funktionen in ZeroTrace – Tests

| TC-ID     | Bereich / Funktion             | Beschreibung                               | Vorbedingungen              | Schritte (kurz)                       | Erwartetes Ergebnis                                     | Automatisiert? | Testfunktion                                                    | Erledigt | Verantwortlich |
| --------- | ------------------------------ | ------------------------------------------ | --------------------------- | ------------------------------------- | ------------------------------------------------------- | -------------- | --------------------------------------------------------------- | -------- | -------------- |
| **TC-01** | Netzwerkscan-Parsing           | „up“-Host korrekt aus XML lesen            | Fake-Nmap-XML               | `run_network_scan()` mit only_up=True | 1 Host erkannt, IP/Hostname korrekt, Kommentar sinnvoll | Ja             | `test_run_network_scan_parses_single_up_host`                   | ☐        |                |
| **TC-02** | Netzwerkscan-Filter            | „down“-Hosts werden bei only_up gefiltert  | Fake-XML (state=down)       | `run_network_scan()`                  | Ergebnisliste leer                                      | Ja             | `test_run_network_scan_filters_down_hosts`                      | ☐        |                |
| **TC-03** | Portscan-Parsing               | Offene Ports korrekt aggregiert            | Fake-XML Ports: 80/443 open | `run_port_scan()`                     | „80/tcp, 443/tcp“ in open_ports                         | Ja             | `test_run_port_scan_collects_open_ports`                        | ☐        |                |
| **TC-04** | PDF-Export                     | PDF-Datei wird erzeugt                     | reportlab installiert       | `export_results_to_pdf()`             | PDF existiert, >0 Bytes                                 | Ja             | `test_export_results_to_pdf_creates_file`                       | ☐        |                |
| **TC-05** | PDF-Fehlerhandling             | Fehler wenn reportlab fehlt                | reportlab entfernen/mocken  | `export_results_to_pdf()`             | Aussagekräftige Fehlermeldung                           | Optional       | (noch offen)                                                    | ☐        |                |
| **TC-06** | GUI-Logik – Netzwerkscan       | Button wird korrekt aktiviert              | GUI gestartet               | Netzwerk-Scan aktiv + DSG             | Button aktiv + Text = „Netzwerkscan starten“            | Ja             | `test_update_scan_button_state_enables_button_for_network_scan` | ☐        |                |
| **TC-07** | GUI-Logik – Custom Scan        | Kombi Netzwerk+Port → richtiger Buttontext | beide Checkboxen aktiv      | `_update_scan_button_state()`         | Button zeigt „Benutzerdefinierter Scan“                 | Ja             | `test_update_scan_button_state_custom_scan_text`                | ☐        |                |
| **TC-08** | Scan-Ablauf (Integration Mock) | GUI ruft Backend richtig auf               | Backend gemockt             | `_run_scan()`                         | Fake-Network + Fake-Portscan jeweils 1× aufgerufen      | Ja             | `test_run_scan_calls_backend_functions`                         | ☐        |                |
| **TC-09** | Validierung DSG                | Kein Scan ohne Berechtigung                | DSG = False                 | Start drücken                         | Warnung erscheint, Button disabled                      | Teilweise      | (GUI Test manuell)                                              | ☐        |                |
| **TC-10** | Validierung Ports              | Portscan ohne Portbereich                  | Ports leer                  | `_run_scan()`                         | Warnung erscheint, kein Scan                            | Manuell/TDD    | (offen)                                                         | ☐        |                |

