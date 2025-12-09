# ADR <Nummer>: <Titel der Entscheidung>

*Status:* Proposed / Accepted / Rejected / Superseded  
*Datum:* 03.12.2025
*Autor:* Sag / Alle  
*Betroffene Bereiche:* Architektur Performance / Datenschutz / UI

---

## 🎯 1. Kontext

Wir definieren die Anforderungen an das GUI gemäss den Entscheiden bis heute und den Anforderungen als User im zuzug mit dem DSVGO Gestez. 

Folgende Anforderungen wurden in der Gruppe definiert. 
- Der Scan darf nur ausführbar sein wenn wir manuell ein kästchen abhacken in dem wir bestätigen zum Scannen berechtigt zu sein.
  - Aussehen könnte das etwa so: "ich bin gemäss DSVG Arikel XY berechtigt diese Aktion auszuführen"
- Es werden beide Scans die für den MVP definiert wurden eingebettet und werden auswählbar sein(Netzwerk-, Portscan) ausserdem lassen sich die beiden auch Kombinieren
- Der Startbrron für den ausgewählten Scan verändert sich gemäss den ausgewählten Möglichkeiten
- Es muss sichtbar sein das ein Scan läuft.
- Nach dem Scan soll man sehen das er erfolgreich war oder eben nicht
- Anchlissend soll man auswählen können ob man den Scan direkt exportieren will und wenn ja in welches PDF Format (in dem Dashboard sieht man die Resultate immer)
- Die Scanergebnisse sollen wie folgt Aufgelistet werden:

| Host (IP-Adresse) | Offene Ports | Risklvl General |   |
|-------------------|--------------|-----------------|---|

- Die Offenen Ports werden farblich untermahlt gem. Definition Grün=Low, Gelb=Mid (Attention needed), Rot=HIGH (Critical) sowohl im PDF-Report als auch im Dashboard
-

---

## ⚖️ 2. Entscheidung

Wit entscheiden uns gemäss der oben erwähnten Anforderungen mit der GUI-Entwicklung zu starten, wir wählen den experimentellen Ansatz. 

---

## 🧠 3. Begründung

Warum ist diese Entscheidung richtig?

| Argument        | Beschreibung                                                                                                                                          |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| GUI Entwicklung | Das GUI bietet uns eine Basis, es muss in erster Linie nicht perfekt sein, allerdings kann man ohne überhaupt etwas nichts definieren oder ableiten.  |
                                                                                                                                                     |
---

