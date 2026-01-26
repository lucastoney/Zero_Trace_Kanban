# ADR-0007: Port-Risikostufen

*Status:* Accepted  
*Datum:* 09.12.2025  
*Autor:* Sag / Team  
*Betroffene Bereiche:* Architektur  

---

## 1. Ausgangslage

Wir definieren die Risiken der offenen Ports.
Für den MVP ist es wichtig, dass wir uns auf die wichtigsten Ports fokusieren und diese effizient erkennen.

---

## 2. Entscheidung

Die Ports werden wie folgt definiert und eingestuft:  

| Port | Protokoll | Risiko    | Kategorie / Dienst                 | Kurzbegründung                                                                 |
|------|-----------|-----------|------------------------------------|--------------------------------------------------------------------------------|
| 21   | TCP       | Critical  | FTP                                | Dateiübertragung im Klartext, oft schwache Logins, häufig falsch konfiguriert |
| 22   | TCP       | Critical  | SSH                                | Direkter Administrationszugang, beliebtes Ziel für Brute-Force-Angriffe       |
| 23   | TCP       | Critical  | Telnet                             | Veraltetes Remote-Protokoll im Klartext, sehr unsicher                         |
| 25   | TCP       | Critical  | SMTP                               | Mail-Server; offenes Relay kann für Spam/Phishing missbraucht werden          |
| 135  | TCP       | Critical  | Microsoft RPC                      | Windows-RPC-Dienst, oft Startpunkt für Würmer & Exploits                       |
| 139  | TCP       | Critical  | NetBIOS                            | Alter Windows-Filesharing-/Namensdienst, angreifbar                            |
| 445  | TCP       | Critical  | SMB                                | Windows-Freigaben (SMB), häufiges Ziel von Ransomware und Würmern             |
| 1433 | TCP       | Critical  | Microsoft SQL Server               | Datenbank-Port; bei Exponierung hohes Risiko für Datenabzug                   |
| 3306 | TCP       | Critical  | MySQL                              | Datenbank-Port; Standardziel bei schwachen Passwörtern                        |
| 3389 | TCP       | Critical  | RDP (Remote Desktop)               | Direkter Remote-Zugang zum Desktop, hohes Angriffsziel                        |
| 5900 | TCP       | Critical  | VNC                                | Remote-Desktop-Lösung, oft schwach gesichert                                  |
| 53   | TCP/UDP   | Mid       | DNS                                | Namensauflösung; Fehlkonfiguration kann zu DNS-Angriffen genutzt werden       |
| 80   | TCP       | Mid       | HTTP                               | Webserver; Angriffsfläche über unsichere Webanwendungen                       |
| 110  | TCP       | Mid       | POP3                               | Mailabruf im Klartext (Passwörter unverschlüsselt)                             |
| 143  | TCP       | Mid       | IMAP                               | Mailabruf; ohne TLS potenziell unsicher                                       |
| 993  | TCP       | Mid       | IMAPS                              | IMAP über TLS; sicherer, aber bei Fehlkonfiguration Angriffsfläche            |
| 995  | TCP       | Mid       | POP3S                              | POP3 über TLS; sicherer als 110, jedoch relevanter Dienst                     |
| 8080 | TCP       | Mid       | HTTP-Proxy / Alternativ-HTTP      | Oft als Proxy oder Test-HTTP-Port genutzt, wird gerne „vergessen“ abgesichert |

**Low Risk:**
- Alle weiteren Ports, die offen sind, aber nicht in der Liste der Critical- oder Mid-Ports stehen, werden in ZeroTrace als Low markiert.
- Das bedeutet nicht, dass sie sicher sind – nur, dass sie aus Sicht des MVP-Risikomodells geringer priorisiert werden.

In der GUI & im PDF werden die Ports wie folgt dargestellt:

| Risiko | Symbol |
|--------|--------|
| High   | ■      |
| Mid    | ▣      |
| Low    | □      |


[Siehe Begründung ADR-0007](Begründung-ADR.md#adr-0007)