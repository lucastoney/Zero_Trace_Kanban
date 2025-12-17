# Ubiquitous Language – ZeroTrace

Diese Begriffe werden im Projekt **einheitlich** in Kommunikation, Dokumentation, GUI und Code verwendet.

## Kernbegriffe

| Begriff                         | Bedeutung (einheitlich)                                          | Beispiel im Projekt                            |
| ------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------- |
| **ZeroTrace**                   | Name der Anwendung (lokaler Security-Scanner)                    | „ZeroTrace wird lokal ausgeführt.“             |
| **MVP**                         | Minimaler Funktionsumfang für die TA                             | „Nicht produktiv, aber nachweisbar lauffähig.“ |
| **Scan**                        | Oberbegriff für eine Sicherheitsprüfung (ausgelöst durch Nutzer) | „Scan starten“                                 |
| **Netzwerkscan**                | Erkennung von Hosts im Netz (z. B. „up/down“)                    | „192.168.1.0/24 scannen“                       |
| **Portscan**                    | Erkennung offener Ports pro Host                                 | „Ports 1–1000 prüfen“                          |
| **Custom Scan**                 | Kombination aus Netzwerk + Port (wenn beide gewählt)             | GUI-Buttontext „Benutzerdefinierter Scan“      |
| **Scanlauf** (*ScanRun*)        | Konkrete Ausführung eines Scans (Zeitpunkt + Parameter)          | „Scanlauf vom 09.12.2025, 14:02“               |
| **Scan-Parameter**              | Eingaben/Optionen, die den Scan steuern                          | CIDR, Portbereich, only_up                     |
| **Scanresultat** (*ScanResult*) | Strukturierte Ergebnisse eines Scanlaufs                         | Hosts, Ports, RiskLevel                        |
| **Host**                        | Gescanntes Zielsystem im Netz                                    | IP, optional Hostname                          |
| **IP-Adresse**                  | Identifikation des Hosts                                         | „192.168.1.10“                                 |
| **Hostname**                    | Name des Hosts (falls verfügbar)                                 | „PC-01“                                        |
| **Offene Ports**                | Liste der Ports im Status *open*                                 | „80/tcp, 443/tcp“                              |
| **Risikostufe** (*RiskLevel*)   | Einstufung pro Port gemäss Portliste                             | Low / Mid / Critical                           |
| **Port-Risikomodell**           | Regelwerk zur Port-Einstufung                                    | Liste aus ADR-0008                             |
| **Report**                      | Zusammenfassung der Ergebnisse in einem Dokument                 | technisch / management                         |
| **PDF-Export**                  | Erzeugen eines PDF-Reports aus Scanresultaten                    | „PDF-Report erstellen“                         |
| **Berechtigungsbestätigung**    | Checkbox „ich bin berechtigt zu scannen“ (Gate)                  | Ohne Haken kein Scan                           |
| **Local-only**                  | Keine Cloud, keine Datenübertragung nach extern                  | Ergebnisse bleiben lokal                       |
| **GUI**                         | Bedienoberfläche („Kellner“)                                     | Eingabe, Anzeige                               |
| **Backend**                     | Logik („Koch“)                                                   | Nmap ausführen, XML parsen, Report erstellen   |

---

## UI-Bezeichnungen

Diese Bezeichnungen werden im GUI **genau so** verwendet.

| UI-Element            | Exakte Bezeichnung                                                                 |
| --------------------- | ---------------------------------------------------------------------------------- |
| Checkbox              | „Ich bestätige, dass ich berechtigt bin, diesen Scan auszuführen.“                 |
| Scanarten             | „Netzwerkscan“, „Portscan“, „Benutzerdefinierter Scan“                             |
| Startbutton dynamisch | „Netzwerkscan starten“ / „Portscan starten“ / „Benutzerdefinierter Scan starten“  |
| Status                | „Scan läuft…“ / „Scan abgeschlossen“ / „Scan fehlgeschlagen“                       |
| Export                | „PDF-Report erstellen“                                                             |
| Tabelle Spalten       | „Host (IP-Adresse)“, „Offene Ports“, „Risikostufe (gesamt)“                        |
