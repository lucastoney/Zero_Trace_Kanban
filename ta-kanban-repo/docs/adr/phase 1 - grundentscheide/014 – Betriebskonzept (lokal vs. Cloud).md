# ADR <Nummer>: <Titel der Entscheidung>

*Status:* Proposed / Accepted / Rejected / Superseded  
*Datum:* YYYY-MM-DD  
*Autor:* <Name / Team>  
*Betroffene Bereiche:* Architektur / Security / Performance / Datenschutz / UX / etc.

---

## 🎯 1. Kontext

🎯 Kontext

ZeroTrace ist ein Sicherheits-Scanner für KMUs, der Schwachstellen in lokalen Netzwerken erkennen soll.
Die Verarbeitung umfasst:

- Netzwerkscans (Ports, Services, Versionen)
- Host- und OS-Erkennung
- Risiko-Bewertung
- Reporting (HTML/PDF)
- Diese Daten können personenbezogene oder unternehmenssensible Informationen enthalten, beispielsweise:
- IP-Adressen / Hostnamen
- Service-Informationen
- Software-Versionen
- Infrastruktur-Details

Daher ist die Frage zentral, ob die Software lokal beim Kunden oder in einer Cloud-Umgebung betrieben werden soll.

---

## ⚖️ 2. Entscheidung

ZeroTrace wird ausschliesslich lokal beim Kunden ausgeführt.
Es erfolgt keine Übertragung von Daten in eine Cloud und keine externe Analyse.
Alle Scanresultate, Logs und Reports verbleiben auf dem System des Anwenders.

Dies schliesst Cloud-Backend-Infrastrukturen wie AWS, Azure oder SaaS-Plattformen bewusst aus.

---

## 🧠 3. Begründung


| Entscheidung    | Beschreibung                                                                                                                                                                                                           |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lokaler Betrieb | DSVGO / Datenschutz /Complience<br/>- Netzwerk- und Portdaten gelten potenziell als personenbezogen (IP-Adressen, Nutzersysteme)<br/>-DSGVO Art. 5, 6, 32 → Schutzbedarf sehr hoch                                     |
| vs Cloud        | Cloud-Verarbeitung würde:<br/>-Auftragsverarbeitungsverträge erfordern (Art. 28)<br/>-Risiken zur Datenübertragung ins Ausland beinhalten (Art. 44ff)<br/>-zusätzliche organisatorische Sicherheitsmaßnahmen verlangen | 
|                 | Lokaler Betrieb eliminiert diese Risiken nahezu vollständig.                                                                                                                                                           |
| Sicherheit      | Lokaler Betrieb reduziert den Angriffsvektor auf den Arbeitsplatz / Server des Kunden.                                                                                                                                 |

