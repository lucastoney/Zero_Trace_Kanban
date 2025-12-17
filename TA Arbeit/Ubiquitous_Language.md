# Ubiquitous Language – ZeroTrace

Diese Begriffe werden im Projekt einheitlich in Kommunikation, Dokumentation, GUI und Code verwendet.

## Kernbegriffe

| Begriff                          | Bedeutung (einheitlich)                                                           | Beispiel im Projekt                                    |
|----------------------------------|-----------------------------------------------------------------------------------|--------------------------------------------------------|
| **ZeroTrace**                    | Name der Anwendung (lokaler Security-Scanner)                                     | „ZeroTrace wird lokal ausgeführt.“                     |
| **MVP**                          | Minimaler Funktionsumfang für die Transferarbeit                                  | „Nicht vollendet, aber nachweisbar lauffähig.“         |
| **Scan**                         | Oberbegriff für eine Sicherheitsprüfung (ausgelöst durch Nutzer mit Scann-Engine) | „Scan starten“                                         |
| **Netzwerkscan**                 | Erkennung von Hosts im Netz                                                       | „192.168.1.0/24 scannen“                               |
| **Portscan**                     | Erkennung offener Ports pro Host                                                  | „Ports 1–1000 scannen“                                 |
| **Benutzerdefinierter Scan**     | Kombination aus Netzwerk + Port (wenn beide gewählt werden)                       | GUI-Buttontext „Benutzerdefinierter Scan“              |
| **Scanresultat** (*ScanResult*)  | Strukturierte Ergebnisse eines Scanlaufs                                          | Hosts, Ports, Risiko Level                             |
| **Host**                         | Gescanntes Zielsystem im Netz                                                     | IP, optional Hostname                                  |
| **IP-Adresse**                   | Identifikation des Hosts                                                          | „192.168.1.10“                                         |
| **Hostname**                     | Name des Hosts (falls verfügbar)                                                  | „PC-01“                                                |
| **Offene Ports**                 | Liste der Ports im Status *open*                                                  | „80/tcp, 443/tcp“  / ADR 0008                          |
| **Risikostufe** (*RiskLevel*)    | Einstufung pro Port gemäss vordefinierter Portliste                               | □ Low / ▣ Mid / ■ Critical / ADR 0005                  |
| **Port-Risikomodell**            | Regelwerk zur Port-Einstufung                                                     | Ersichtlich in ZeroTrace, Port-Definitionen / ADR 0008 |
| **Report**                       | Zusammenfassung der Ergebnisse in einem Dokument                                  | PDF Verionen: technisch / management                   |
| **PDF-Export**                   | Erzeugen eines PDF-Reports aus Scanresultaten (Dashboard)                         | „PDF-Report erstellen“                                 |
| **DSG Berechtigungsbestätigung** | Checkbox „ich bin berechtigt zu scannen gem. DSG“                                 | Ohne Haken kein Scan! / ADR 0005                       |
| **Local-only**                   | Keine Cloud, keine Datenübertragung nach extern                                   | Ergebnisse bleiben lokal                               |
| **GUI**                          | Bedienoberfläche („Kellner“)                                                      | Eingabe, Anzeige / ADR 0005                            |
| **Backend**                      | Logik („Koch“)                                                                    | Nmap ausführen, XML parsen, Report erstellen /ADR 0007 |

---

## UI-Bezeichnungen

Diese Bezeichnungen werden im GUI **genau so** verwendet.

| UI-Element            | Exakte Bezeichnung                                                               |
| --------------------- |----------------------------------------------------------------------------------|
| Checkbox              | "Ich bestätige, dass der Scan gemäss DSG (SR 235.1) erfolgt und berechtigt bin"  |
| Scanarten             | „Netzwerkscan“, „Portscan“, „Benutzerdefinierter Scan (Beide Scans zeitgleich)“  |
| Status                | „Scan läuft…“ / „Scan abgeschlossen“ / „Scan fehlgeschlagen“ / "Scan abgebrochen" |
| Export                | „PDF-Report erstellen“                                                           |

