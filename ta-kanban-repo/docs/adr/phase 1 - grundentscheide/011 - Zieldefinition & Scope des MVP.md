# ADR 011: Zieldefiniton und Scope des MVP

*Status:* Accepted 
*Datum:* 05.11.2025
*Autor:* Sam / Team  
*Betroffene Bereiche:* Gesamtes Projekt

---

## 🎯 1. Kontext

### Pitch
Wir wollen mit ZeroTrace ein Tool bereitstellen welches KMU unterstützt die eigenen Netzwerke und Umgebungen  zu schützen. 
Das Ziel soll eine einfach zu bedienende Software sein welche Lokal bei den Benutzern läuft und selbstständig bedient werden kann. 
Wir orientieren uns stark am DSVGO und wollen uns vorallem im Bereich schützenswerte Daten und hohe Sicherheit etablieren.
Es soll für Techniker und Management gleich einfach sein zu bedienen, auch die Reports sollen in zwei entsprehcneden Versionen bereitgestellt werden.

### MVP
Für den MVP werden wir ein GUI erstellen und uns forerst auf den Scan des Netzwerks fokusieren.
Das ganze soll stark Skalierbar sein und ständig erweitert werden können.

### Wichtigste Rahmenbedinungen 
- Zerotrace läuft 100% Lokal
- Reports werden in 2 Fassungen bereit gestellt, eine für Management und eine für Techniker (IT-Provider)
- Starke Orientierung an DSVGO (Muss,Soll,Kann)
- 

---

## ⚖️ 2. Entscheidung

**Wir entscheiden uns für:**  
- Entwicklungsumgebung "Pycharm"
- Versionsverlauf und Ablage "Github"
- Dokumentationen und Berichte im .md Format zu erfassen
- ZeroTrace wird 100% Lokal funktionieren
- Für MVP Betriebssystem Windows als Einstieg 


---

## 🧠 3. Begründung


| Entscheid   | Begründung                                                 |     
|-------------|------------------------------------------------------------|
| PyCharm     | Der Entscheid für PyCharm basiert auf allgemeiner Kenntnis |
| ✓ Vorteil 2 | …                                                          |
| ⚠ Nachteil  | …                                                          |
| 🔄 Abwägung | …                                                          |

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
