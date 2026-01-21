# ADR-0005: GUI Anforderungen

*Status:* Accepted
*Datum:* 03.12.2025
*Autor:* Cag / Team   
*Betroffene Bereiche:* UI

---

## 1. Kontext

### Beschreibung

Wir definieren die Anforderungen an das GUI gemäss den Entscheiden und den Anforderungen als User im beizug mit dem DSVGO Gesetz. 

Folgende Anforderungen wurden in der Gruppe definiert. 
- Der Scan darf nur ausführbar sein wenn wir manuell ein kästchen abhacken in dem wir bestätigen zum Scannen berechtigt zu sein.
- Aussehen könnte das etwa so: "ich bin gemäss DSVGO Arikel XY berechtigt diese Aktion auszuführen"
- Es werden beide Scans die für den MVP definiert wurden eingebettet und werden auswählbar sein(Netzwerk-, Portscan) ausserdem lassen sich die beiden auch Kombinieren
- Der Startbutton für den ausgewählten Scan verändert sich gemäss den ausgewählten Möglichkeiten
- Es muss sichtbar sein das ein Scan läuft.
- Nach dem Scan soll man sehen das er erfolgreich war oder nicht
- Anschliessend soll man auswählen können ob man den Scan direkt exportieren will und wenn ja in welches PDF Format
- Die Scanergebnisse sollen wie folgt Aufgelistet werden:

| Host (IP-Adresse) | Offene Ports | Risk-LVL General |
|-------------------|--------------|------------------|

- Die Offenen Ports werden mit Icons hervorgehoben. Definition Low, Mid (Attention needed), High (Critical) sowohl im PDF-Report als auch im Dashboard

---

## 2. Entscheidung

Wit entscheiden uns gemäss der oben erwähnten Anforderungen mit der GUI-Entwicklung zu starten, wir wählen den experimentellen Ansatz.

