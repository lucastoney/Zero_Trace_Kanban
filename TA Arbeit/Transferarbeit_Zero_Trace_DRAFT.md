
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

## 1.2 Zielsetzung

Das übergeordnete Ziel dieser Transferarbeit ist die Entwicklung eines Minimal Viable Product (MVP) des Tools „Zero Trace". Der MVP soll innerhalb der verfügbaren Zeit und Ressourcen so weit umgesetzt werden, dass die wichtigsten Funktionen eines lokal laufenden Schwachstellen-Scanners verständlich gezeigt werden können. Im Vordergrund steht dabei nicht eine komplett fertige Software, sondern der Nachweis, dass das Konzept grundsätzlich funktioniert, sowie eine saubere technische Umsetzung mit klarer Verfolgbarkeit zum jetzigen IST-Zustand. Der Prototyp soll über ein GUI bedienbar sein und die wichtigsten Funktionen abdecken: Scan starten, Scanstatus anzeigen und Ergebnisse darstellen.

Inhaltlich konzentriert sich der MVP auf die wichtigsten Funktionen:

Lokale Scans sollen in einem klar definierten und berechtigten Rahmen möglich sein und die Ergebnisse sollen strukturiert erfasst werden. Im Sinne des Zero-Trust-Gedankens werden die Resultate so aufbereitet, dass der aktuelle Zustand der Netzwerkumgebung regelmässig und nachvollziehbar überprüft werden kann. Zusätzlich sollen die Scanresultate passend für verschiedene Zielgruppen dargestellt werden, nämlich als technische Sicht für IT-Fachpersonen und als Managementsicht zur Priorisierung von Risiken und Massnahmen. Für den MVP wird die Einordnung der Ergebnisse bewusst vereinfacht, indem offene Ports anhand einer definierten Portliste in Risikostufen (Low,Mid,High) klassifiziert werden, damit Resultate konsistent dargestellt und verglichen werden können.

Gleichzeitig werden die wichtigsten Architekturentscheidungen mittels ADRs dokumentiert. Auch die dazugehörigen Diskussionen und Abwägungen, die sich im Unterricht ergeben haben werden darin festgehalten. Dadurch bleibt die Umsetzung begründet und der MVP kann später sinvoll erweitert werden.

---

Ich finde das Kapitel 2 ist ein zu grosser Mischmasch an eigentlich allem was sortiert in den Bericht gehören würde, 
Aktuell ist es mehr eine Auflistung und eine Rechtfertigung, die Rechtfertigung resp. die Erklärung würde ich in dem Kapitel 
Disskusion erarbeiten ausserdem gehört viel aktuell davon in den BEreich lesson learnd. Ich schreibe hier meinen kurzen Vorschlag dafür:


# 2. Vorgehen

Die Umsetzung des Projekts erfolgte grösstenteils iterativ, praxisorientiert und experimentell mit dem Ziel, innerhalb des gegebenen Zeitrahmens einen funktionsfähigen Minimum Viable Product (MVP) zu entwickeln.
Der Fokus lag dabei auf der schrittweisen technischen Validierung des Konzepts sowie auf einer engen Abstimmung innerhalb des Projektteams.

## 2.1 Entwicklungsansatz

Die Entwicklung erfolgte überwiegend iterativ und experimentell.
Zu Projektbeginn bestanden Unsicherheiten hinsichtlich der technischen Umsetzbarkeit, insbesondere in Bezug auf die Kombination von Netzwerk Scanning, grafischer Benutzeroberfläche und Reporting. Da im Projektteam nur begrenzte Erfahrung mit der Entwicklung komplexerer Software vorhanden war, wurde bewusst auf ein strikt lineares Vorgehensmodell verzichtet. Stattdessen wurde ein explorativer und iterativer Entwicklungsansatz gewählt, der eine schrittweise Validierung technischer Annahmen ermöglichte.

Funktionen wurden zunächst prototypisch umgesetzt, anschliessend ¨bewertet und danach weiterentwickelt oder angepasst. Der Fokus lag darauf, technische Annahmen früh zu überprüfen und Risiken möglichst früh sichtbar zu machen.

Dieses Vorgehen entspricht einem inkrementellen MVP Ansatz, bei dem der Funktionsumfang bewusst auf einen stabilen Kern reduziert wurde. Ziel war nicht die Entwicklung eines vollständigen Produkts, sondern eines funktionsfähigen und demonstrierbaren Prototyps.

Konkret bedeutete dies:

- Definition der zwingend notwendigen Kernfunktionen
- bewusste Zurückstellung zusätzlicher oder optionaler Features
- Fokus auf Funktion und Präsentierbarkeit

Der Kernumfang des MVP umfasste:

- Durchführung eines Netzwerk/Port-Scans
- Steuerung über einer intuitiven grafische Benutzeroberfläche
- verständliche Aufbereitung der Ergebnisse in Form von Reports (PDF)

Weiterführende Funktionen wurden bewusst zurückgestellt.


## 2.2 Einfluss von Teamstruktur nach Conway

Die Struktur der Anwendung wurde wesentlich durch die Organisation des Projektteams geprägt.
Gemäss Conway spiegeln Softwaresysteme häufig die Kommunikationsstrukturen der Organisation wieder, die sie entwickeln.

Im Projekt zeigte sich dieser Zusammenhang deutlich. Aufgrund der Teamgrösse wurde die Arbeit in mehrere Teilbereiche aufgeteilt, die parallel bearbeitet wurden:

- Scan Logik, Reporting
- GUI Entwicklung
- Bildnerische Darstellungen, Diagramme
- Dokumentation

Wir nutzten die Zeit welche wir im Unterricht erhielten um die jeweiligen Arbeitsfortschritte und Äderungsvorschläge jeweils in der Gruppe Wöchentlich zu dikutieren und zu verfeinern. 
So konnten wir sicherstellen, dass jeder seine Meinung einbringen kann .

## 2.3 Domänenorientierte Strukturierung

Ein vollständiger Domain Driven Design Prozess wurde im Projekt nicht umgesetzt. Dennoch erfolgte die Strukturierung der Anwendung bewusst entlang ihrer fachlichen Domäne.
Die zentrale Domäne des Projekts ist das Scannen und Bewerten von Netzwerk Expositionen. Daraus ergaben sich natürliche fachliche Teilbereiche:
- Durchführung von Scans
- Interpretation der Ergebnisse
- Aufbereitung für unterschiedliche Zielgruppen

Diese domänenorientierte Aufteilung unterstützte sowohl die technische Strukturierung der Anwendung als auch die Aufgabenverteilung im Team.

## 2.4 Projektphasen

Die Entwicklung des Prototyps lässt sich in mehrere aufeinander aufbauende Phasen gliedern.

**Phase 1 Anforderungsdefinition** 

Zu Beginn wurden Zielsetzung und Rahmenbedingungen des Projekts festgelegt. Dabei wurde definiert, welche Funktionen für den MVP zwingend erforderlich sind und welche bewusst zurückgestellt werden.

**Phase 2 Architektur und Technologiefestlegung** 

Anschliessend wurde eine grundlegende technische Struktur definiert. Zentrale Entscheidung war die Umsetzung der Scan Funktionalität auf Basis von Nmap sowie die Bereitstellung über eine Python basierte Desktop Anwendung.

**Architecture Decision Records (ADRs)**

Für unser Projekt haben wir Architecture Decision Records eingeführt, um zentrale Architekturentscheidungen klar, strukturiert und dauerhaft festzuhalten. Gerade bei technischen Grundsatzfragen ist es entscheidend, nicht nur Ergebnisse zu dokumentieren, sondern auch den jeweiligen Kontext nachvollziehbar zu machen.

Unsere ADRs folgen einem einheitlichen Aufbau: Jede Entscheidung erhält eine eindeutige Nummer, einen Titel, Status, Datum, verantwortliche Personen sowie die betroffenen Bereiche. Dadurch bleibt ersichtlich, wann, von wem und in welchem Umfang eine Entscheidung getroffen wurde.
Inhaltlich gliedert sich jedes Dokument in die Abschnitte Ausgangslage und Entscheidung. Zunächst wird der Rahmen beschrieben, in dem die Wahl getroffen wird (inklusive relevanter Anforderungen und Randbedingungen). Anschließend wird die konkret gewählte Lösung präzise festgehalten. Die ausführliche Begründung wurde bewusst in ein separates Markdown-Dokument ausgelagert. So bleibt das ADR übersichtlich, während die Argumentation vertieft dargestellt werden kann.

ADRs sind für uns nicht nur Dokumentation, sondern ein Instrument zur Qualitätssteigerung im gesamten Entwicklungsprozess.

**Phase 3 Iterative Umsetzung** 

Die eigentliche Entwicklung erfolgte schrittweise in konstanter Überarbeitung.

Entwicklung einer grafischen Benutzeroberfläche zur Steuerung des Scanners, einbetten der Logik, 
Erweiterung um strukturierte Reporting Funktionen

Zwischen den Umsetzungsschritten erfolgten regelmässige Abstimmungen und Anpassungen des Funktionsumfangs.

## 2.5 Zusammenarbeit und Werkzeuge

Aufgrund der parallelen Bearbeitung der Teilbereiche war eine strukturierte Zusammenarbeit erforderlich.

Zur Unterstützung wurden eingesetzt:

- ADRs für eine saubere Nachvollziehbarkeit der Entscheide.  
- GitHub zur Versionsverwaltung und Nachverfolgung von Änderungen
- PyCharm als gemeinsame Entwicklungsumgebung
- Python mit Tkinter, Socket und Nmap Bindings zur technischen Umsetzung

Die Nutzung gemeinsamer Werkzeuge unterstützte die Koordination und Integration der einzelnen Komponenten.


## 2.6 Qualitätssicherung und Tests

Die Qualitätssicherung erfolgte durch kontinuierliche manuelle Tests während der Entwicklung.

Geprüft wurden insbesondere:
- korrekte Durchführung der Scans
- stabile Interaktion zwischen Scan Logik und GUI
- nachvollziehbare Darstellung der Ergebnisse im Reporting

Erkannte Probleme wurden fortlaufend behoben und in die weitere Entwicklung integriert.

# *Hier könnte man noch einen Link in die Docs auf die Tests vereweisen? Oder zu rechtfertigend? 

## 2.7 Reflexion des Vorgehens (nicht sicher ob wir die Reflexion des Vorgehens in die Diskusion packen sollen oder hier belassen! )

Im Projekt zeigte sich, dass insbesondere die Integration der verschiedenen Teilbereiche sowie die Priorisierung des MVP Umfangs zentrale Herausforderungen darstellten.
Wir hatten auch mühe das fehlende Know-how zu kompensieren und uns den ständig wechselnden Rahmenbedinungen kontinuierlich anzupassen.

Mehrfach wurde entschieden, den Funktionsumfang bewusst zu reduzieren, um einen stabilen und präsentierbaren Kern zu gewährleisten. Das iterative Vorgehen erwies sich dabei als entscheidend, um technische Risiken früh zu erkennen und den Projektumfang an die verfügbaren Ressourcen anzupassen.

Die gewonnenen Erfahrungen trugen wesentlich zum Verständnis von Zusammenarbeit, Strukturierung und Entscheidungsfindung in Softwareprojekten bei.

# 3 Ergebnisse

### 3.1 Evaluierte Prototyp-Funktionen (Miroboard)

Zu Projektbeginn wurde während der Lektion gemeinsam ein Miroboard erstellt, um mögliche Funktionen und Themenfelder für **ZeroTrace** zu sammeln und in einer gemeinsamen Übersicht zu festzuhalten. Das Board diente ergänzend zum Projektpitch als Ideengebung der einzelnen Projektbeteiligten und schlussendlich als Orientierung, um den potenziellen Funktionsumfang sichtbar zu machen und erste grobe Zusammenhänge zwischen Scanning, Benutzeroberfläche, Reporting, Datenschutz und Qualitätssicherung zu erkennen. In erster Linie ging es ein gemeinsames Verständnis für unseren Schwachstellen-Scanner zu erarbeiten.

### 3.2 GUI-Ergebnisse

### 3.3 GUI-Ergebnisse

#### Beschreibung der grafischen Benutzeroberfläche

ZeroTrace bietet eine grafische Benutzeroberfläche, über die sich Scans konfigurieren, auslösen und die Ergebnisse übersichtlich darstellen lassen. Der Aufbau ist bewusst einfach gehalten und in klar getrennte Bereiche gegliedert, damit die Bedienung auch ohne vertiefte Vorkenntnisse möglich ist.

**Abbildung 2:** GUI – Dashboard / Scan-Ausführung *(Screenshot einfügen: Dashboard-Ansicht mit Scan-Konfiguration und Ergebnis-Tabelle)*

**Abbildung 3:** GUI – Port-Definitionen / Risikokategorien *(Screenshot einfügen: Port-Definitionen mit Tabelle Port/Risikostufe/Erläuterung)*

#### Aufbau der GUI

**Sidebar (links)**  
Die Sidebar zeigt den Namen des Tools **„Zero Trace“** sowie den Menüpunkt **„Dashboard“**. Zusätzlich ist im MVP der Menüpunkt **„Port-Definitionen“** vorhanden, um die im Tool hinterlegten Port-Risikokategorien transparent darzustellen. Weitere Menüpunkte wurden bewusst weggelassen, um die Bedienung schlank zu halten.

**Header (oben)**  
Im Header wird der Titel **„Zero Trace – Lokale Sicherheitsanalyse“** sowie eine kurze Beschreibung angezeigt. Zusätzlich wird der MVP-Charakter über eine Kennzeichnung (**„MVP – Local“**) sichtbar gemacht.

**Scan-Konfiguration (oben, Hauptbereich)**  
Im Bereich **„Scan-Konfiguration“** kann der Benutzer:
- das Zielnetzwerk im CIDR-Format eingeben,
- den Port-Bereich definieren,
- optional nur aktive Hosts anzeigen lassen,
- die Scanart auswählen (Netzwerkscan / Port-Scan).

Zusätzlich muss der Benutzer per Checkbox bestätigen, dass der Scan gemäss DSG (SR 235.1) erfolgt und die Berechtigung vorhanden ist. Erst nach dieser Bestätigung wird der Button zum Starten des Scans aktiviert.

**Risikostufen-Hinweis (Portscan)**  
In der Dashboard-Ansicht wird die Bedeutung der Risikostufen kurz erklärt (Critical/Mid/Low) inklusive Symbolik, damit die Bewertung der offenen Ports direkt verständlich ist.

**Scan-Ergebnisse (unten, rechts)**  
Die Ergebnisse werden tabellarisch dargestellt. Angezeigt werden:
- IP-Adresse  
- Hostname  
- Offene Ports (inkl. Symbol je Risikostufe)  
- Kommentar / Bemerkung  

**PDF-Export (unten rechts)**  
Nach einem erfolgreichen Scan kann ein Report über den Button **„PDF-Report erstellen“** erzeugt werden.

#### Port-Definitionen (separate Ansicht)

In der Ansicht **„Port-Definitionen“** wird eine Liste der im MVP hinterlegten Ports angezeigt. Dazu werden die zugehörige Risikostufe sowie eine kurze Erläuterung aufgeführt. Diese Übersicht dient dazu, die Risikoklassifizierung nachvollziehbar zu machen und auch für Nicht-Techniker verständlich zu erklären, weshalb bestimmte Dienste als kritischer bewertet werden.

#### Statusanzeige

Der jeweilige Systemzustand wird über Rückmeldungen in der Oberfläche sichtbar gemacht (z. B. Aktivierung/Deaktivierung des Scan-Buttons in Abhängigkeit der DSG-Bestätigung sowie Meldungen zum Scanablauf).


### 3.3 Scanner-Engine (Backend)

### 3.4 Risikomodell und Klassifizierung

### 3.5 Reporting-Ergebnisse

### 3.6 Testergebnisse

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
