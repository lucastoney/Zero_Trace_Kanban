Ich finde das Kapitel 2 ist ein zu grosser Mischmasch an eigentlich allem was sortiert in den Bericht gehören würde, 
Aktuell ist es mehr eine Auflistung und eine Rechtfertigung, die Rechtfertigung resp. die Erklärung würde ich in dem Kapitel 
Disskusion erarbeiten ausserdem gehört viel aktuell davon in den BEreich lesson learnd. Ich schreibe hier meinen kurzen Vorschlag dafür:


## 2. Vorgehen

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

Die eigentliche Entwicklung erfolgte schrittweise in konstater Überarbeitung.

Umsetzung eines Konsolen Prototyps zur Validierung der Scan Funktionalität,
Entwicklung einer grafischen Benutzeroberfläche zur Steuerung des Scanners,
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
