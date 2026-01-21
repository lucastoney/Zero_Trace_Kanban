# ADR 0004: Betriebskonzept Lokal

*Status:* Accepted
*Datum:* 12.11.2025
*Autor:* Team   
*Betroffene Bereiche:* Architektur

---

##  1. Kontext

### Beschreibung

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

##  2. Entscheidung

- ZeroTrace wird ausschliesslich lokal beim Kunden ausgeführt.
- Es erfolgt keine Übertragung von Daten in eine Cloud und keine externe Analyse.
- Alle Scanresultate, Logs und Reports verbleiben auf dem System des Anwenders.

Dieser Entscheid schliesst Cloud-Backend-Infrastrukturen wie AWS, Azure oder SaaS-Plattformen bewusst aus.
