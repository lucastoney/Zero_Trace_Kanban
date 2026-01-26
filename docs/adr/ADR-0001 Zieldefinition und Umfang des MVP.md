# ADR-0001: Zieldefiniton und Umfang des MVP

*Status:* Accepted  
*Datum:* 05.11.2025  
*Autor:* Sam / Team  
*Betroffene Bereiche:* Gesamtes Projekt  

---

##  1. Ausgangslage

### Pitch
Wir wollen mit ZeroTrace ein Tool bereitstellen welches KMU unterstützt die eigenen Netzwerke und Umgebungen zu schützen. 
Das Ziel soll eine einfach zu bedienende Software sein welche Lokal bei den Benutzern läuft und selbstständig bedient werden kann. 
Wir orientieren uns stark am DSVGO und wollen uns vor allem im Bereich schützenswerte Daten und hohe Sicherheit etablieren.
Es soll für Techniker und Management gleich einfach sein zu bedienen, auch die Reports sollen in zwei Versionen bereitgestellt werden.

### MVP
Für den MVP werden wir ein Programm mit GUI erstellen und uns vorerst auf den Scan des Netzwerks fokusieren.
Das ganze soll Skalierbar aufgebaut sein, damit es erweitert werden kann.

### Wichtigste Rahmenbedinungen 
- Zero-Trace läuft 100% Lokal
- Reports werden in 2 Fassungen bereit gestellt, eine für Management und eine für Techniker (IT-Provider)
- Starke Beachtung an DSVGO (Muss,Soll,Kann)

---

##  2. Entscheidung

**Wir entscheiden uns für:**  
- Entwicklungsumgebung "Pycharm"
- Versionsverlauf und Ablage "GitHub"
- Dokumentationen und Berichte im .md Format
- ZeroTrace wird 100% Lokal ausgeführt
- Der MVP wird vorerst auf Windows laufen

[Siehe Begründung ADR-0001](Begründung-ADR.md#adr-0001)