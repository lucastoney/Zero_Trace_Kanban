# ADR <Nummer>: <Titel der Entscheidung>

*Status:* Proposed / Accepted / Rejected / Superseded  
*Datum:* YYYY-MM-DD  
*Autor:* <Name / Team>  
*Betroffene Bereiche:* Architektur / Security / Performance / Datenschutz / UX / etc.

---

## 🎯 1. Kontext

Beschreibe hier die Ausgangssituation:

- Welches Problem gibt es?
- Welche Anforderungen / Rahmenbedingungen spielen eine Rolle?
- Warum musste eine Entscheidung getroffen werden?
- Welche Risiken oder Einschränkungen bestehen (z. B. DSGVO, Zero Trace, lokale Anwendung)?

Beispiele:
- *„Unsere Anwendung darf keine Nutzerdaten speichern, benötigt aber temporäre Verarbeitung.“*
- *„Python wird verwendet, GUI muss lokal laufen.“*

---

## ⚖️ 2. Entscheidung

🟩 **Wir entscheiden uns für:**  
> *<Klar und prägnant formulierte Entscheidung – 1 Satz>*

Beispiel:
> *„Sensible Daten werden ausschliesslich im RAM gespeichert (RAM-Only Storage) und nicht persistent abgelegt.“*

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
