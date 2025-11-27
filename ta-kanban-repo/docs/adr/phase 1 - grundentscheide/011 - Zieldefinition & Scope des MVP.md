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


| Entscheid                     | Begründung                                                                                                                                                           |     
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PyCharm                       | Der Entscheid für PyCharm basiert auf allgemeiner Kenntnis der Software und auf Empfehlung unseres Lehrers                                                           |
| Github                        | Github wurde auf drängen uneres Lehrers gewählt, durchaus sinnvoll, es muss jedoch damit gerechnet werden einiges an Zeig aufzuwenden für den Aufbau und die Kenntnis |
| .md Format                    | Gemäss gelesenem haben wir uns dazu entschidene, da sich die Dateien überall leicht integrieren lassen                                                               |
| Lokale Funktion von ZeroTrace | Wurde im Pitch so vorgestellt und einstimmig zugestimmt. Sinnvoll, da einfacher DSVGO konform aufzubauen                                                             |
| Wahl des Betriebssystem       | Wir alle sind Windows User und müssen uns aufgrund der Zeitvorgabe erstmal auf ein OS beschränken                                                                    | 

---
