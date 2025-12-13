# ADR <Nummer>: <Titel der Entscheidung>

*Status:* Proposed / Accepted / Rejected / Superseded  
*Datum:* 03.12.2025  
*Autor:* SAG / Alle
*Betroffene Bereiche:* Architektur / Security / Performance 

---

## 🎯 1. Kontext

Beschreibe hier die Ausgangssituation:

Das Backend soll die Befehle ausführen welche im Gui befohlen werden. 
Wir werden ein Plugin benötigen für Phyton benötigen als Opensource Phyton Bibliothek um PDF's direkt zu erstellen.
Wir werden eine klare trennung Programmieren zwischen GUI und Backend:
- Das GUI ist rein für die Eingabe da, der Kellner und das Backend führt die effektiven Eingaben des GUI aus.
GUI = Kellner
- nimmt Bestellung entgegen
- sagt Bescheid, wenn es fertig ist
- zeigt dir das Essen (Ergebnis)

Backend = Koch
– macht die eigentliche Arbeit
– verarbeitet Rohzutaten (Nmap-Daten)
– liefert fertige Gerichte (ScanResult)

GUI kocht nicht.
Backend serviert nicht.

---

## ⚖️ 2. Entscheidung

Die Zusammenarbeit zwischen GUI und Backend wie oben beschrieben in einem Experimentellen Umfeld zu programmieren. Uns wurden keine Applis zugeteilt, die Kompetenzen sind also dürftig.
Nichts desto trotz, werden wir ein Grundgerüst aufbauen des Backends, welches die Funktionen in sich hat welche durch das GUI ausgeführt werden können.

---

## 🧠 3. Begründung

Warum ist diese Entscheidung richtig?

| Argument               | Beschreibung                                                                                                                                                                                                             |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kellner, Koch          | Nicht nur ist es Verständnis halber einfacher dies so auf zu bauen, Zero Trace soll auch skallierbar sein, das erreichen wir mittels dieser abtrennung und Modularem Code.                                               |
| Kellner, Koch Nachteil | Mit Phyton werden wir in Zukunft an eine grenze stossen, dass ist uns bewusst, auf grund der wenigen PRG. Kompetenzen in der Gruppe und der Beschränkten Zeit bleiben wir jedoch dabei für die Gruppenarbeit und den MVP | |

---
