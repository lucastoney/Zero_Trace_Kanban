# Begründung der ADR

## ADR-0001
| Entscheid                     | Begründung                                                                                                                                                           |     
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PyCharm                       | Der Entscheid für PyCharm basiert auf allgemeiner Kenntnis der Software und auf Empfehlung unseres Lehrers                                                           |
| Github                        | Github wurde auf drängen uneres Lehrers gewählt, durchaus sinnvoll, es muss jedoch damit gerechnet werden einiges an Zeig aufzuwenden für den Aufbau und die Kenntnis |
| .md Format                    | Gemäss gelesenem haben wir uns dazu entschidene, da sich die Dateien überall leicht integrieren lassen                                                               |
| Lokale Funktion von ZeroTrace | Wurde im Pitch so vorgestellt und einstimmig zugestimmt. Sinnvoll, da einfacher DSVGO konform aufzubauen                                                             |
| Wahl des Betriebssystem       | Wir alle sind Windows User und müssen uns aufgrund der Zeitvorgabe erstmal auf ein OS beschränken                                                                    | 

---

## ADR-0002
| Entscheid               | Begründung                                                                                                                                                                                                                      |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Python als Programmiersprache | - Schnell iterierbar: ideal für MVP, viele libraries (nmap, XML, DB, Reports).<br/> - Cross-Platform: Windows/Linux/macOS, später leicht erweiterbar <br/> - Einfache Synthax im Vergleich zu anderen Programmiersprachen <br/> |

---

##  ADR-0003
| Entscheid               | Begründung                                                                                                                                                                             |     
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NMAP als Scanner-Engine | - Einfach in Phyton zu integrieren<br/>- Deckt alle der benötigten Scans ab welche für MVP benötigt werden<br/>- extrem Stabil<br/>- seit 20 Jahren erfolgreich der Standard für Scans |
                                                                  |
---


##  ADR-0004
| Entscheid    | Begründung                                                                                                                                                                                                            |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lokaler Betrieb | DSVGO / Datenschutz /Complience<br/>- Netzwerk- und Portdaten gelten potenziell als personenbezogen (IP-Adressen, Nutzersysteme)<br/>-DSGVO Art. 5, 6, 32 → Schutzbedarf sehr hoch                                    |
| vs Cloud     | Cloud-Verarbeitung würde:<br/>-Auftragsverarbeitungsverträge erfordern (Art. 28)<br/>-Risiken zur Datenübertragung ins Ausland beinhalten (Art. 44ff)<br/>-zusätzliche organisatorische Sicherheitsmaßnahmen verlangen|
| Sicherheit   | Lokaler Betrieb reduziert den Angriffsvektor auf den Arbeitsplatz / Server des Kunden.                                                                                                                                |

---

## ADR-0005
| Entscheid       | Begründung                                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| GUI Entwicklung | - Das GUI bietet uns eine Basis.<br/> - Ohne ein GUI ist die Bedienung mühsam und kompliziert.<br/> - Es entsteht ein Mehrwert für Kunden |

---

## ADR-0007

Warum ist diese Entscheidung richtig?

| Entscheid         | Begründung                                                    |
|-------------------|---------------------------------------------------------------|
| Menge der Ports   | Ist so Ideal um den Überblick zu behalten                     |
| Auswahl der Ports | Viele davon sind leicht zu aktivieren und somit nachzustellen |


---

## ADR-0008

| Entscheid | Begründung                                                                                                                                                                                                    |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DSGVO und DSG Komform| - Erhebung nur technisch notwendiger Daten <br/> - Speicherung von Scan‑ und Logdaten nur für die notwendige Dauer <br/> - Zugriff auf Daten ist rollenbasiert und auf autorisierte Personen beschränkt <br/> - Lokale Datenverarbeitung ohne Cloud‑Übertragung|