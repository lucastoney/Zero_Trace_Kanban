
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

Im Rahmen der Transferarbeit des Moduls «Software- und Plattform-Architektur» wurden zunächst verschiedene Projektpitches vorgestellt. Anschliessend wurde darüber abgestimmt, welche Projekte weiterverfolgt werden sollen. Nach der Abstimmung stellte unser Dozent (Fabian Hirter), der in diesem Projekt künftig die Rolle des fachlichen Vorgesetzten übernimmt, die Projektgruppen anhand der Interessen der Studierenden zusammen. Unsere Gruppe wurde aus sechs Studierenden zusammengestellt: Giovanni Cardillo, Manuel Sager, Roman Nemchenko, Thines Rasiah, Yves Weber und Luca Steiner. Wir alle verfügen über sehr unterschiedliche berufliche Hintergründe und hatten zum Projektbeginn nur geringe Erfahrung mit den in der Software- und Plattform-Architektur eingesetzten Werkzeugen und Methoden.

Die von uns gewählte Transferarbeit basiert auf dem Pitch von Manuel und Yves.
Sie präsentierten die Idee eines leicht bedienbaren, modernen Netzwerk Schwachstellen-Scanners, der nach Abschluss eines Scans zwei unterschiedliche Berichte generiert, einen für IT-Spezialisten und einen für das Management. Auf diese Weise soll sowohl eine technische als auch eine verständlich formulierte Managementsicht entstehen, damit alle Beteiligten (Stakeholder) ein gemeinsames Verständnis über die aktuelle IT-Sicherheitslage erhalten. Während der technische Bericht konkret aufzeigt, wo Handlungsbedarf besteht, soll der Management-Report als Entscheidungsgrundlage dienen, um Risiken gezielt zu priorisieren. Diese unterschiedliche Aufbereitung soll die Kommunikationsstruktur zwischen Techniker und Management (gemäss Conways Law) des Unternehmens vereinfachen und somit verbessern.

Der Pitch überzeugte die Klasse, weil er sehr praxisnah ist und aktuelle Sicherheitsthemen aufgreift. Zudem berücksichtigt er immer wichtiger werdende Datenschutzgesetze wie die DSGVO (seit 25. Mai 2018) und das revidierte Schweizer Datenschutzgesetz (seit 1. September 2023), insbesondere vor dem Hintergrund stetig wachsender Komplexität und Vernetzung unserer IT-Systeme.

Zudem sahen wir einen grossen Mehrwert unser Wissen in diesem Fachgebiet zu erweitern. Im Sinne des Zero-Trust-Modells «Never Trust, Always Verify» sehen wir es als notwendig an, IT-Infrastrukturen regelmässig und nachvollziehbar zu überprüfen, damit Sicherheitsrisiken frühzeitig erkannt und adressiert werden können.

Trotz der Verfügbarkeit von Tools wie Nmap fehlen vielen Organisationen ein Werkzeug, dass:

- Lokale Scans ohne Expertenwissen ermöglicht  
- Ein verständliches GUI bietet  
- Strukturierte technische und nicht-technische Reports daraus erzeugen kann 

Zwar existieren Netzwerk-Scanner bereits, diese sind jedoch häufig komplex, überdimensioniert oder nicht konsequent auf eine einfache Grundanalyse im KMU-Umfeld ausgerichtet.

Daraus ergibt sich die zentrale Problemstellung dieser Transferarbeit:

**Wie können wir als Gruppe mit geringen Vorkenntnissen, ein schlankes und intuitiv bedienbares Tool entwickeln, das regelmässige lokale Schwachstellenanalysen im eigenen, autorisierten System ermöglicht und gleichzeitig den Zero-Trust-Ansatz nachvollziehbar vermittelt?** 

Um diese Problemstellung schrittweise zu bearbeiten, soll ein MVP (Minimal Viable Product) erstellt werden. Ziel ist die Entwicklung einer Grundlage, die spätere Erweiterungen ermöglicht, ohne bereits in den ersten Versionen ein überdimensioniertes System zu bauen.

Eine weitere Herausforderung und Frage die sich uns stellte ist, wie organisieren wir uns, wer hat wo seine Stärken und Interessen? Zudem wie Konsolidieren wir unser wissen, damit jeder das selbe Verständnis über das Projekt verfügt trotz Arbeitsaufteilung?


---

# 1.2 Zielsetzung

Das übergeordnete Ziel dieser Transferarbeit ist die Entwicklung eines Minimal Viable Product (MVP) des Tools „Zero Trace". Der MVP soll innerhalb der verfügbaren Zeit und Ressourcen so weit wie umgesetzt werden, dass die wichtigsten Funktionen eines lokal laufenden Schwachstellen-Scanners verständlich gezeigt werden können. Im Vordergrund steht dabei nicht eine komplett fertige Software, sondern der Nachweis, dass das Konzept grundsätzlich funktioniert, sowie eine saubere technische Umsetzung mit klarer Verfolgbarkeit zum jetzigen IST-Zustand. Der Prototyp soll über ein GUI bedienbar sein und die wichtigsten Funktionen abdecken: Scan starten, Scanstatus anzeigen und Ergebnisse darstellen.

Inhaltlich konzentriert sich der MVP auf die wichtigsten Funktionen:

Lokale Scans sollen in einem klar definierten und berechtigten Rahmen möglich sein und die Ergebnisse sollen strukturiert erfasst werden. Im Sinne des Zero-Trust-Gedankens werden die Resultate so aufbereitet, dass der aktuelle Zustand der Netzwerkumgebung regelmässig und nachvollziehbar überprüft werden kann. Zusätzlich sollen die Scanresultate passend für verschiedene Zielgruppen dargestellt werden, nämlich als technische Sicht für IT-Fachpersonen und als Managementsicht zur Priorisierung von Risiken und Massnahmen. Für den MVP wird die Einordnung der Ergebnisse bewusst vereinfacht, indem offene Ports anhand einer definierten Portliste in Risikostufen (Low,Mid,High) klassifiziert werden, damit Resultate konsistent dargestellt und verglichen werden können.

Gleichzeitig werden die wichtigsten Architekturentscheidungen mittels ADRs dokumentiert. Auch die dazugehörigen Diskussionen und Abwägungen, die sich im Unterricht ergeben haben werden darin festgehalten. Dadurch bleibt die Umsetzung begründet und der MVP kann später sinvoll erweitert werden.

---

# 2 Vorgehen

Die Umsetzung des Projekts erfolgte in mehreren strukturierten Schritten, um eine nachvollziehbare und methodische Entwicklung des MVP **„Zero Trace“** sicherzustellen. Im Folgenden wird beschrieben, welche Werkzeuge, Konzepte und Vorgehensweisen angewendet wurden.

### 2.1 Eingesetzte Tools, Frameworks und Konzepte

Für die Entwicklung des Prototyps wurden folgende Technologien und Konzepte verwendet:

- **Programmiersprache:**  
  Python, aufgrund der breiten Unterstützung für Netzwerk-Scanning und GUI-Entwicklung.

- **Frameworks und Libraries:**  
  - Tkinter für die Erstellung eines einfachen grafischen Benutzerinterfaces (GUI).  
  - Socket und Nmap-Python-Bindings für die Durchführung von Port-Scans.

- **Versionsverwaltung:**  
  GitHub zur kollaborativen Entwicklung und zur Nachverfolgbarkeit von Änderungen.

- **Projektmanagement:**  
  Agile Ansätze mit iterativen Sprints, um den MVP schrittweise zu erweitern.

- **Architekturprinzipien:**  
  Orientierung am Zero-Trust-Modell („Never Trust, Always Verify“) sowie Modularität für spätere Erweiterungen.

### 2.2 Architekturentscheidungen

Die Architektur wurde bewusst schlank gehalten, um den MVP innerhalb der gegebenen Zeit umsetzbar zu machen:

- **Client-seitige Anwendung:**  
  Der Scanner läuft lokal auf dem autorisierten System, um Datenschutz- und Sicherheitsanforderungen zu erfüllen.

- **Modularer Aufbau:**  
  Trennung von Scan-Logik, GUI und Reporting, um spätere Anpassungen zu erleichtern.

- **Reporting-Konzept:**  
  Zwei Ausgabemodi – ein technischer Bericht für IT-Spezialisten und ein vereinfachter Management-Report.

- **ADR-Dokumentation:**  
  Alle Architekturentscheidungen wurden in Architecture Decision Records (ADRs) festgehalten (z. B. ADR-0001 bis ADR-0005).

### 2.3 Variantenvergleich (A/B-Vergleich)

Zu Beginn wurden verschiedene Ansätze für die GUI und die Scan-Engine verglichen:

- **GUI:**  
  Entscheidung zwischen Tkinter und PyQt. Aufgrund der geringeren Komplexität und der schnelleren Umsetzung fiel die Wahl auf Tkinter.

- **Scan-Engine:**  
  Vergleich zwischen direkter Socket-Programmierung und der Nutzung von Nmap-Bindings. Für den MVP wurde die Socket-Variante gewählt, um die Abhängigkeit von externen Tools zu minimieren.

### 2.4 Iterative Prototypenentwicklung

Die Entwicklung erfolgte in mehreren Iterationen:

1. **Iteration 1:** Implementierung der Kernfunktionalität (Port-Scan über eine definierte Portliste).  
2. **Iteration 2:** Aufbau einer einfachen GUI zur Steuerung des Scans.  
3. **Iteration 3:** Generierung von strukturierten Reports (technisch und Management).

Jede Iteration wurde nach Fertigstellung getestet und dokumentiert, bevor die nächste begann.

### 2.5 Herausforderungen

Während der Umsetzung traten folgende Herausforderungen auf:

- **GUI-Integration:**  
  Die Synchronisation zwischen Scan-Prozess und GUI-Statusanzeige erforderte zusätzliche Logik.

- **Performance:**  
  Optimierung der Scan-Geschwindigkeit bei größeren Portlisten.

- **Risikoklassifizierung:**  
  Definition einer konsistenten Port-Risikostufe (Low, Mid, High) für den Management-Report.

### 2.6 Testmethoden

Die Tests wurden manuell durchgeführt:

- **Funktionstests:**  
  Überprüfung der Scan-Funktionalität auf verschiedenen Testsystemen.

- **GUI-Tests:**  
  Sicherstellung der korrekten Anzeige von Scanstatus und Ergebnissen.

- **Report-Validierung:**  
  Kontrolle der strukturierten Ausgabe für beide Zielgruppen.

### 2.7 Dokumentation

Die gesamte Umsetzung wurde kontinuierlich dokumentiert:

- **ADRs:** Architekturentscheidungen und deren Begründungen.  
- **GitHub-Repository:** Versionshistorie und Code-Dokumentation.  
- **Protokolle:** Besprechungen und Entscheidungen im Projektteam.  

**Transferbericht:** Zusammenfassung des Vorgehens und der angewandten Methoden.


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
