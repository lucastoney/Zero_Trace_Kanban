# ADR <Nummer>: <Titel der Entscheidung>

*Status:* Proposed / Accepted / Rejected / Superseded  
*Datum:* 09.12.2025
*Autor:* Sag / Team  
*Betroffene Bereiche:* Performance 

---

## 🎯 1. Kontext

Wir definieren hier wie die Tests aussehen sollen und wo sie wie abgelget werden. 
Vorschlag: 
Test Benennung: TC - xy /
docs > TDD Tests 
Kritische Funktionen.md 
- her werden wir alle kritischen Funktionen erfassen und dazu Unit Tests erstellen
- die Tests werden abgehandlet beim Coden und laufend sinvoll selbstständig erweitert
Manuelle Systemtests.md 
- hier werden wir Systemtests definiert welche durch Personen welche nicht mit dem Coden beschäftigt waren ausgeführt werden. 
- diese werden immer auf der Fertigen Anwendung durchgeführt, Kürzel soll die durchführende Person kennzeichnen falls es Rückfragen gibt

---

## ⚖️ 2. Entscheidung

Wir haben den Vorschlag einstimmig angenommen und werden das so durchziehen. 
Die für die Systemtests verantwortliche Person wird noch definiert in der Zukunft. 

---

## 🧠 3. Begründung

Warum ist diese Entscheidung richtig?

| Argument                  | Beschreibung                                                                                                                                                                                  |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Einheitliche Namensgebung | Erleichtert die Dokumentation und die Wiedererkennung                                                                                                                                         |
| Aufteilung der Tests      | Auch wenn eine saubere Dokumentation nicht erwünscht ist, so müssen wir diese Unterteilung machen um Aufgabengebiete sauber trennen zu können und den proggramieren die Arbeit zu erleichtern |
                                                                                                                                                                                         |
---

