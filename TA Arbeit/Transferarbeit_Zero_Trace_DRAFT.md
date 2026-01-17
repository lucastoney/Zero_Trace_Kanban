
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

Im Rahmen der Transferarbeit des Moduls «Software- und Plattform-Architektur» wurden zunächst verschiedene Projektideen in Form von Projektpitches vorgestellt. Anschliessend wurde darüber abgestimmt, welche Projekte weiterverfolgt werden sollen. Nach der Abstimmung stellte unser Dozent (Fabian Hirter), der in diesem Projekt künftig die Rolle des fachlichen Vorgesetzten übernimmt, die Projektgruppen anhand der Interessen der Studierenden zusammen. Unsere Gruppe wurde aus sechs Studierenden zusammengestellt: Giovanni Cardillo, Manuel Sager, Roman Nemchenko, Thines Rasiah, Yves Weber und Luca Steiner. Wir alle verfügen über sehr unterschiedliche berufliche Hintergründe und hatten zum Projektbeginn nur geringe Erfahrung mit den in der Software- und Plattform-Architektur eingesetzten Werkzeugen und Methoden.

Die von uns gewählte Transferarbeit basiert auf dem Pitch von Manuel und Yves.
Sie präsentierten die Idee eines leicht bedienbaren, modernen Netzwerkschwachstellen-Scanners, der nach Abschluss eines Scans zwei unterschiedliche Berichte generiert, einen für IT-Spezialisten und einen für das Management. Auf diese Weise soll sowohl eine technische als auch eine verständlich formulierte Managementsicht entstehen, damit alle Beteiligten (Stakeholder) ein gemeinsames Verständnis über die aktuelle IT-Sicherheitslage erhalten. Während der technische Bericht konkret aufzeigt, wo Handlungsbedarf besteht, soll der Management-Report als Entscheidungsgrundlage dienen, um Risiken gezielt zu priorisieren. Diese unterschiedliche Aufbereitung soll die Kommunikationsstruktur zwischen Techniker und Management (gemäss Conways Law) des Unternehmens vereinfachen und somit verbessern.

Der Pitch überzeugte die Klasse, weil er sehr praxisnah ist und aktuelle Sicherheitsthemen aufgreift. Zudem berücksichtigt er immer wichtiger werdende Datenschutzgesetze wie die DSGVO (seit 25. Mai 2018) und das revidierte Schweizer Datenschutzgesetz (seit 1. September 2023), insbesondere vor dem Hintergrund stetig wachsender Komplexität und Vernetzung unserer IT-Systeme.

Zudem sahen wir einen grossen Mehrwert unser Wissen in diesem Fachgebiet zu erweitern. Im Sinne des Zero-Trust-Modells «Never Trust, Always Verify» sehen wir es als notwendig an, IT-Infrastrukturen regelmässig und nachvollziehbar zu überprüfen, damit Sicherheitsrisiken frühzeitig erkannt und adressiert werden können.

Trotz der Verfügbarkeit von Scanner-Tools wie Nmap fehlen vielen Organisationen ein Werkzeug, das:

- Lokale Scans ohne Expertenwissen ermöglicht  
- Eine verständliche Benutzeroberfläche (GUI) bietet  
- Strukturierte technische und nicht-technische Berichte daraus erzeugen kann 

Zwar existieren Netzwerk-Scanner bereits, diese sind jedoch häufig komplex, teuer, überdimensioniert oder nicht konsequent auf eine einfache Grundanalyse im KMU-Umfeld ausgerichtet. Zusätzlich können Scanresultate sensible Infrastrukturinformationen enthalten (z.B. IP-Adressen, Hostnamen, Port- und Serviceinformationen). Daher wurde bereits bei der Vorstellung der Projektidee früh festgelegt, dass Zero Trace ausschliesslich lokal betrieben wird und keine Daten in eine Cloud übertragen werden. 

Daraus ergibt sich die zentrale Problemstellung dieser Transferarbeit:

**Wie können wir als Gruppe mit geringen Vorkenntnissen ein schlankes und intuitiv bedienbares Tool entwickeln, das regelmässige lokale Schwachstellenanalysen im eigenen, autorisierten System ermöglicht und gleichzeitig den Zero-Trust-Ansatz nachvollziehbar vermittelt?** 

Um diese Problemstellung schrittweise zu bearbeiten, soll ein MVP (Minimal Viable Product) erstellt werden. Ziel ist die Entwicklung einer Grundlage, die spätere Erweiterungen ermöglicht, ohne bereits in den ersten Versionen ein überdimensioniertes System zu bauen.

Neben der technischen Fragestellung ergaben sich zu Projektbeginn zusätzliche organisatorische Fragen, die im Projektverlauf beantwortet werden müssen: 

Wie organisieren wir die Zusammenarbeit in der Gruppe mit unterschiedlichen Stärken und Interessen, und wie stellen wir sicher, dass trotz Aufgabenteilung ein gemeinsames Verständnis über das gesamte Projekt vorhanden ist?

Insgesamt beschreibt dieser Projektbericht die Transferarbeit «Zero Trace» von der Ausgangslage bis hin zu unserer Empfehlung und dem Ausblick zu dieser Thematik. Er soll das Vorgehen unserer Gruppe nachvollziehbar darstellen sowie die erzielten Resultate und gewonnenen Erkenntnisse zusammenfassen, einschliesslich der gelesenen Buchabschnitte von David Farley («Modern Software Engineering») und Vaughn Vernon («Strategic Monoliths and Microservices»).

---

# 1.2 Zielsetzung

Das übergeordnete Ziel dieser Transferarbeit ist die Entwicklung eines Minimal Viable Product (MVP) des Tools „Zero Trace". Der MVP soll innerhalb der verfügbaren Zeit und Ressourcen so weit umgesetzt werden, dass die wichtigsten Funktionen eines lokal laufenden Schwachstellen-Scanners verständlich gezeigt werden können. Im Vordergrund steht dabei nicht eine komplett fertige Software, sondern der Nachweis, dass das Konzept grundsätzlich funktioniert, sowie eine saubere technische Umsetzung mit klarer Verfolgbarkeit zum jetzigen IST-Zustand. Der Prototyp soll über ein GUI bedienbar sein und die wichtigsten Funktionen abdecken: Scan starten, Scanstatus anzeigen und Ergebnisse darstellen.

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

### 2.3 Technische Konzeption

Ein klassischer A/B-Vergleich zwischen mehreren gleichwertigen Lösungsansätzen fand im Projektverlauf nicht statt. Bereits zu Beginn stand fest, dass die Port-Scan-Funktionalität auf Basis von Nmap realisiert und über eine grafische Benutzeroberfläche zugänglich gemacht werden soll.

Die zentrale Unsicherheit lag weniger in der Auswahl alternativer Technologien, sondern vielmehr in der Frage, ob sich die gewünschte Scan-Funktionalität stabil und praktikabel mit einer GUI kombinieren lässt. Die Entwicklung diente daher in erster Linie der technischen Validierung dieses Ansatzes.

Alternative Scan-Engines auf Basis direkter Socket-Programmierung wurden im Projektverlauf nicht weiter in Betracht gezogen, da der Fokus klar auf der Nutzung der etablierten Nmap-Funktionalität lag. **--> Bei diesem Punkt bin ich mir nicht sicher ob das stimmt? wenn nicht kannst du das rauslöschen :)**


Im Bereich der grafischen Benutzeroberfläche wurden hingegen verschiedene Frameworks diskutiert. Die Entscheidung fiel auf Tkinter, da dieses Framework eine geringe Einstiegshürde, eine schnelle Umsetzung sowie eine nahtlose Integration in Python ermöglicht.


### 2.4 Iterative Prototypenentwicklung

Die Entwicklung des Prototyps erfolgte iterativ, um die technische Umsetzbarkeit des festgelegten Konzepts schrittweise zu überprüfen und abzusichern:

1. **Iteration 1:** Umsetzung der grundlegenden Scan-Funktionalität auf Basis von Nmap, um die prinzipielle Funktionsfähigkeit zu validieren.  
2. **Iteration 2:** Entwicklung und Integration einer einfachen grafischen Benutzeroberfläche zur Steuerung des Scan-Vorgangs.  
3. **Iteration 3:** Erweiterung um strukturierte Report-Funktionen für technische Anwender sowie für das Management.

Nach jeder Iteration wurden die Ergebnisse überprüft und dokumentiert, bevor der nächste Entwicklungsschritt umgesetzt wurde. **  --> Bei diesem Punkt bin ich mir nicht sicher ob das stimmt?**


### 2.5 Herausforderungen

### 2.5 Herausforderungen

Während der Umsetzung des Projekts traten sowohl technische als auch organisatorische Herausforderungen auf, die den Projektverlauf massgeblich beeinflussten und zu mehreren Anpassungen im Vorgehen führten.

**Technische Integration von Scan-Logik und GUI:**  
Eine zentrale Herausforderung bestand in der Integration der Scan-Funktionalität in eine grafische Benutzeroberfläche. Die Kopplung des laufenden Scan-Prozesses mit einer stabilen Status- und Ergebnisanzeige erforderte zusätzliche Abstimmungen sowie eine klare Trennung zwischen Backend-Logik und GUI-Komponenten. Insbesondere zeigte sich, dass eine zu enge Verzahnung die Wartbarkeit und Fehlersuche erschwerte, weshalb Anpassungen am Aufbau vorgenommen wurden.

**Darstellung und Klassifizierung von Risiken:**  
Für den Management-Report musste eine konsistente und zugleich verständliche Risikoklassifizierung definiert werden. Die Einteilung offener Ports in die Kategorien Low, Medium und High stellte sich als anspruchsvoll heraus, da technische Genauigkeit und Verständlichkeit für nicht-technische Zielgruppen in Einklang gebracht werden mussten. Zudem zeigte sich im Verlauf der Umsetzung, dass die ursprünglich geplante farbliche Kennzeichnung einzelner Ports technisch nicht zuverlässig umsetzbar war. Infolgedessen wurde die Darstellung angepasst und durch standardisierte Risikostufen-Symbole ersetzt.

**Tool- und Workflow-Umstellung im Projektverlauf:**  
Zu Beginn des Projekts wurden verschiedene Tools zur Organisation und Zusammenarbeit genutzt. Im weiteren Verlauf stellte sich jedoch heraus, dass eine einheitliche Entwicklungsumgebung notwendig ist, um effizient zusammenarbeiten zu können. Die Umstellung auf GitHub und PyCharm als zentrale Werkzeuge für Versionsverwaltung und Entwicklung erforderte eine kurze Einarbeitungsphase sowie die Definition gemeinsamer Regeln für Commits, Ordnerstrukturen und Dokumentation.

**Koordination und Priorisierung im Team:**  
Die parallele Bearbeitung unterschiedlicher Teilbereiche (z. B. Scan-Logik, GUI, Reporting, Dokumentation) machte eine klare Aufgabenverteilung und regelmässige Abstimmungen notwendig. Insbesondere bei der Festlegung des MVP-Umfangs zeigte sich, dass eine konsequente Priorisierung erforderlich war, um funktionsfähige Ergebnisse zu erzielen. Mehrfach wurde entschieden, den Fokus auf einen stabilen, präsentierbaren Kernumfang zu legen und zusätzliche Funktionen bewusst zurückzustellen.

**Entscheidungsfindung ohne Vorerfahrung in Softwarearchitektur:**  
Eine weitere Herausforderung bestand darin, grundlegende technische und konzeptionelle Entscheidungen zu treffen, obwohl innerhalb der Gruppe keine ausgeprägte Erfahrung mit Softwareprojekten im Bereich der Softwarearchitektur vorhanden war. Dies erforderte eine intensive Auseinandersetzung mit den eingesetzten Technologien, regelmässige Abstimmungen sowie das gemeinsame Abwägen verschiedener Lösungsansätze. Trotz dieser Ausgangslage erwies sich das Projekt als lehrreich und anspruchsvoll, da im Verlauf wichtige Erkenntnisse in den Bereichen Strukturierung, Entscheidungsfindung und Zusammenarbeit in Softwareprojekten gewonnen werden konnten.

Insgesamt trugen diese Herausforderungen dazu bei, das Vorgehen kontinuierlich zu reflektieren und anzupassen. Die daraus gewonnenen Erfahrungen flossen direkt in die weitere Entwicklung des Prototyps sowie in die Projektorganisation ein.


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
