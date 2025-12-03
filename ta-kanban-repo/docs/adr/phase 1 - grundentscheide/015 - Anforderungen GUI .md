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
- Die Offenen Ports werden farblich untermahlt gem. Definition Grün=Low, Gelb=Mid (Attention needed), Rot=HIGH (Critical) sowohl im PDF-Report als auch im Dashboard
- 
- 

| Host (IP-Adresse) | Offene Ports | Risklvl General |   |
|-------------------|--------------|-----------------|---|








Beispiele:
- *„Unsere Anwendung darf keine Nutzerdaten speichern, benötigt aber temporäre Verarbeitung.“*
- *„Python wird verwendet, GUI muss lokal laufen.“*

---

## ⚖️ 2. Entscheidung

🟩 **Wir entscheiden uns für:**  
> *<Klar und prägnant formulierte Entscheidung – 1 Satz>*

Beispiel:
> *„Sensible Daten werden ausschließlich im RAM gespeichert (RAM-Only Storage) und nicht persistent abgelegt.“*

---

## 🧠 3. Begründung

Warum ist diese Entscheidung richtig?

| Argument | Beschreibung |
|----------|--------------|
| ✓ Vorteil 1 | … |
| ✓ Vorteil 2 | … |
| ⚠ Nachteil | … |
| 🔄 Abwägung | … |

---

## 🔁 4. Alternativen (evaluierte Optionen)

| Alternative | Warum verworfen? |
|-------------|------------------|
| Option A | ... |
| Option B | ... |
| Option C | ... |

---

## 📊 5. Auswirkungen

### Positiv
- …

### Negativ / Risiken
- …

### Offene Punkte
- …

---

## 🔐 6. Sicherheits- & Datenschutzrelevanz

> *Nur enthalten, wenn relevant (z. B. Zero Trace, DSGVO, Security)*

- …

---

## 🔎 7. Entscheidung gültig für

🧩 Welche Module oder Bereiche sind betroffen?

```text
z. B. src/security/, src/storage/, GUI, Tests, Dokumentation
