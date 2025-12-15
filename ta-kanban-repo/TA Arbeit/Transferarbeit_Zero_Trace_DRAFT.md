
# Projektbericht Zero Trace

## Inhaltsverzeichnis

- [Einleitung](#1-einleitung)
- [Ausgangslage und Problemstellung](#11-ausgangslage-und-problemstellung)
- [Zielsetzung](#12-zielsetzung)
- [Vorgehen](#2-vorgehen)
- [Ergebnisse](#3-ergebnisse)
- [Diskussion](#4-diskussion)
- [Empfehlung und Ausblick](#5-empfehlung-und-ausblick)
- [Verzeichnisse](#6-verzeichnisse)

---

# Identifikation

Dokumentencode  
**Projektbericht_Zero_Trace.md**

Projektname  
**Bericht | Gruppenarbeit Software Architektur**

Schule  
TEKO Schweizerische Fachschule Bern  
Belpstrasse 37  
3007 Bern

---

# Dokumentenhistorie

| Revision | Datum       | Autor | Bemerkungen           |
|---------|-------------|-------|------------------------|
| 0.1     | 24.11.2025  | xxxx  | Status = Erstellung    |
| 0.2     | xx.xx.xxxx  | xxxx  | Status = Überarbeitung |
| 1.0     | xx.xx.xxxx  | xxxx  | Status = Abgabe        |

---

# 1 Einleitung

## 1.1 Ausgangslage und Problemstellung

Im Modul «Software- und Plattform-Architektur» wurden verschiedene Projektpitches vorgestellt und anschliessend darüber 
abgestimmt, welche Projekte weiterverfolgt werden. Unsere Transferarbeit basiert auf dem Pitch von Manuel und Yves.
Diese präsentierten die Idee eines leicht bedienbaren, modernen Schwachstellen-Scanners, der nach Abschluss eines Scans
zwei unterschiedliche Berichte generiert, einen für IT-Spezialisten und einen für das Management. Auf diese Weise soll
sowohl eine technische als auch eine verständlich formulierte Managementsicht entstehen, damit alle Beteiligten(Stakeholder) ein gemeinsames Verständnis über die aktuelle IT-Sicherheitslage erhalten. Während der technische Bericht konkret aufzeigt, wo akuter Handlungsbedarf besteht, soll der Management-Report als Entscheidungsgrundlage dienen, um Risiken gezielt zu priorisieren. (vgl. ADR-0001)

Der Pitch überzeugte die Klasse durch seine hohe Praxisrelevanz, den Bezug zu aktuellen Sicherheitsthemen und die Anforderungen moderner Datenschutzgesetze wie der DSGVO, die seit dem 25. Mai 2018 gilt, sowie dem revidierten Schweizer Datenschutzgesetz, das am 1. September 2023 in Kraft trat, insbesondere vor dem Hintergrund immer komplexerer und stärker vernetzter IT-Systeme.

Zudem sahen wir einen grossen Mehrwert unser Wissen in diesem Fachgebiet zu erweitern. Im Sinne des Zero-Trust-Modells «Never Trust, Always Verify» sehen wir es als notwendig an, IT-Infrastrukturen regelmässig und nachvollziehbar zu überprüfen, damit Sicherheitsrisiken frühzeitig erkannt und adressiert werden können.

Trotz der Verfügbarkeit von Tools wie Nmap fehlen vielen Organisationen ein Werkzeug, dass:

- Lokale Scans ohne Expertenwissen ermöglicht  
- Ein verständliches GUI bietet  
- Strukturierte technische und nicht-technische Reports daraus erzeugen kann (vgl. ADR-0005)

Zwar existieren Netzwerk-Scanner bereits, diese sind jedoch häufig komplex, überdimensioniert oder nicht konsequent auf eine einfache Grundanalyse im KMU-Umfeld ausgerichtet.

Daraus ergibt sich die zentrale Problemstellung dieser Transferarbeit:

**Wie können wir als Gruppe ein schlankes und intuitiv bedienbares Tool entwickeln, das regelmässige lokale Schwachstellenanalysen im eigenen, autorisierten System ermöglicht und gleichzeitig den Zero-Trust-Ansatz nachvollziehbar vermittelt?** (vgl. ADR-0004)

Um diese Problemstellung schrittweise zu bearbeiten, soll ein MVP (Minimal Viable Product) erstellt werden. Ziel ist eine stabile Grundlage, die spätere Erweiterungen ermöglicht, ohne bereits in den ersten Versionen ein überdimensioniertes System zu bauen.

---

# 1.2 Zielsetzung

Das übergeordnete Ziel dieser Transferarbeit ist die Entwicklung eines Minimal Viable Product (MVP) des Tools „Zero Trace". Der MVP soll innerhalb der verfügbaren Zeit und Ressourcen so weit wie umgesetzt werden, dass die wichtigsten Funktionen eines lokal laufenden Schwachstellen-Scanners verständlich gezeigt werden können. Im Vordergrund steht dabei nicht eine komplett fertige Software, sondern der Nachweis, dass das Konzept grundsätzlich funktioniert, sowie eine saubere technische Umsetzung mit klarer Verfolgbarkeit zum jetzigen IST-Zustand. Der Prototyp soll über ein GUI bedienbar sein und die wichtigsten Funktionen abdecken: Scan starten, Scanstatus anzeigen und Ergebnisse darstellen.

Inhaltlich konzentriert sich der MVP auf die wichtigsten Funktionen:

Lokale Scans sollen in einem klar definierten und berechtigten Rahmen möglich sein und die Ergebnisse sollen strukturiert erfasst werden. Im Sinne des Zero-Trust-Gedankens werden die Resultate so aufbereitet, dass der aktuelle Zustand der Netzwerkumgebung regelmässig und nachvollziehbar überprüft werden kann. Zusätzlich sollen die Scanresultate passend für verschiedene Zielgruppen dargestellt werden, nämlich als technische Sicht für IT-Fachpersonen und als Managementsicht zur Priorisierung von Risiken und Massnahmen. Für den MVP wird die Einordnung der Ergebnisse bewusst vereinfacht, indem offene Ports anhand einer definierten Portliste in Risikostufen (Low,Mid,High) klassifiziert werden, damit Resultate konsistent dargestellt und verglichen werden können.

Gleichzeitig werden die wichtigsten Architekturentscheidungen mittels ADRs dokumentiert. Auch die dazugehörigen Diskussionen und Abwägungen, die sich im Unterricht ergeben haben werden darin festgehalten. Dadurch bleibt die Umsetzung begründet und der MVP kann später sinvoll erweitert werden.

---

# 2 Vorgehen

(Platzhalter – noch zu ergänzen)

---

# 3 Ergebnisse

(Platzhalter – noch zu ergänzen)

---

# 4 Diskussion

Hier wird auf die Punkte aus **1.2 Zielsetzung** eingegangen.

---

# 5 Empfehlung und Ausblick

(Platzhalter – noch zu ergänzen)

---

# 6 Verzeichnisse

## Abbildungsverzeichnis
Es konnten keine Einträge gefunden werden.

## Tabellenverzeichnis
Es konnten keine Einträge gefunden werden.

---

Projektbericht_Zero_Trace.docx | 03.12.2025  
© TEKO Schweizerische Fachschule 2025
