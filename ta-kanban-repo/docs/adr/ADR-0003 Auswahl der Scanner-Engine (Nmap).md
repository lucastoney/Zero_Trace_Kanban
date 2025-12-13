# ADR 013: Auswahl Scanner-Engine

*Status:* Accepted 
*Datum:* 05.11.2025
*Autor:* Sam / Team  
*Betroffene Bereiche:* Gesamtes Projekt

---

##  1. Kontext

### Nutzung
Wir brauchen eine Engine die wir ins Backend integrieren können, welche die Scans ausführen kann. Der User wird die verschiedenen Scans über das GUI ausführen.

### Folgende Scans möchten wir anbieten: 
Muss enthalten sein für den MVP:

| Funktion          | Nmap-Flag       | Grund                   |
| ----------------- | --------------- | ----------------------- |
| Portscan (TCP)    | `-sT`           | zuverlässig, ohne Admin |
| Service & Version | `-sV`           | nötig für CVE-Mapping   |
| OS Detection      | `-O` (optional) | zusätzlicher Kontext    |
| Host Discovery    | `-sn`           | Netzwerkübersicht       |
| No-Ping Modus     | `-Pn`           | typische KMU-Netze      |

Sollte enthalten sein für spätere Erweiterung:

| Option          | Flag               | Mehrwert                    |
| --------------- | ------------------ | --------------------------- |
| SYN Scan        | `-sS`              | schneller, stealthy         |
| UDP Scan        | `-sU`              | DNS/SNMP prüfen             |
| Aggressive Scan | `-A`               | umfassende Analyse          |
| NSE-Scripts     | `--script=*`       | echte Schwachstellenprüfung |
| TLS/SSL Checks  | `ssl-enum-ciphers` | Kryptosicherheit            |

Achtung: Die Scans und deren Priorität können im Laufe der Entwicklung angepasst werden!!! 

---

##  2. Entscheidung

**Wir entscheiden uns für:**  
Für das Tool NMAP als Scanner-Engine.  

---

##  3. Begründung


| Entscheid               | Begründung                                                                                                                                                                             |     
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NMAP als Scanner-Engine | - Einfach in Phyton zu integrieren<br/>- Deckt alle der benötigten Scans ab welche für MVP benötigt werden<br/>- extrem Stabil<br/>- seit 20 Jahren erfolgreich der Standard für Scans |
                                                                  |
---
