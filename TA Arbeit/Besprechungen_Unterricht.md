# Unterrichtsnotizen (Mi, 08:15–11:45) — Beginn 05.11.2025

> Pro Termin kurz festhalten: **Themen**, **wichtigste Punkte**, **Entscheide**.

---

## 2025-11-05 (Mi)
**Themen:**  
- Gruppen wurden anhand der Abstimmungen eingeteilt.
- Erste gemeinsame Besprechung zur TA „Zero-Trace“.
- Gedanken zu Basis/Kernfunktionen und Rahmenbedingungen wurden von Yves & Manuel vorgestellt (ohne aktive Beeinflussung, um weitere Ideen/Ansätze offen zu lassen).
- Erste Tool-Definition und Start eines Projektplans in OneNote.

**Wichtigste Punkte:**  
- Kernfunktionen und Rahmenbedingungen festgelegt.
- Erste Tool-Auswahl getroffen.
- Grobe Arbeitseinteilung (noch ohne Verbindlichkeit).

**Entscheide:**  
- Gruppen gemäss Abstimmung fix. (Manuel,Yves, Luca, Roman, Giovanni und Thines) 
- Fokus: Zero-Trace MVP (Kernfunktionen).
- Erste Tool-Auswahl als Start gesetzt. (OneNote, Teams, Word für TA-Arbeit) 
- OneNote als zentrale Planung/Notizen.  
- Ansatz offen lassen (Varianten möglich).
- Arbeit grob verteilt, Details später.



---

## 2025-11-12 (Mi)
**Themen:**
- Tasks gemeinsam erarbeiten.
- Gemeinsame Ideeneinbringung und Erstellung eines Miroboards (siehe „ZeroTrace_Miroboard.jpg“).
- Zusammenfassung der Möglichkeiten erstellen bzw. eine grobe Struktur darstellen, damit diese den anderen Gruppen vorgestellt werden kann.
- GitHub und PyCharm einrichten (statt der bereits definierten Tool-Auswahl vom 2025-11-05).

**Wichtigste Punkte:**
- Ideeneinbringung von allen und gemeinsames Festhalten der Ergebnisse.
- Grobstruktur sowie Einteilung der Funktionen in Muss-/Kann-Kriterien.
- Task-Verteilung gemäss Grundlage OneNote.

**Entscheide:**
- Für den MVP werden die definierten Muss-Kriterien (bspw. Python, Nmap und PDF-Export) umgesetzt. Damit soll sichergestellt werden, dass wir eine Lösung erarbeiten, die man auch zeigen kann und nicht nur theoretisch bleibt.
- Statt die definierte Tool-Auswahl soll GitHub und PyCharm für die Versionsverwaltung eingesetzt werden.
- Die Aufgabenverteilung ist wie folgt:
  - Git-Aufbau und -Struktur sowie ADR: Luca und Thines
  - Nmap und Python: Yves und Manuel
  - DSGVO-Rahmenbedingungen: Manuel
  - Context Map und BPMN: Roman
  - Python-PDF-Export sowie Skizze der GUI: Giovanni

---

## 2025-11-19 (Mi)
**Themen:**  
- MVP-Umfang festlegen (Muss/Kann nochmals durchgehen).  
- Erste Tests mit Nmap machen und anschauen, welche Resultate wir brauchen.
- GitHub und PyCharm bei allen einrichten (als Standard für die Zusammenarbeit).
- Erste GitHub/Ordnerstruktur erstellen sowie Syntax definieren.
- Erste ADRs starten (wichtige Entscheide kurz festhalten).   
- Context Map und BPMN: grober Ablauf zeichnen (Scan → Bewertung → Report).  
- GUI: erste Skizze, wie die App aussehen könnte.  

**Wichtigste Punkte:**  
- MVP soll: Ziel eingeben → Scan → Resultate → PDF.  
- Nmap-Output analysieren wie wir ihn weiterverarbeiten können.   
- Alle mussten GitHub und PyCharm sauber einrichten, damit wir gemeinsam arbeiten können.  
- Statt der ursprünglichen Tool-Auswahl wird GitHub + PyCharm fix für die Versionsverwaltung genutzt.  

**Entscheide:**   
- ADRs werden ab jetzt laufend ergänzt, sobald wir etwas fix entscheiden und anschliessend gemeinsam kurz besprochen.  
- Scans nur in erlaubten Umgebungen; im Report keine sensiblen Daten speichern.  
- GitHub und PyCharm sind ab jetzt Standard (Versionsverwaltung über GitHub und PyCharm statt der vorher definierten Tool-Auswahl).
- OneNote Projektorganisation wird in GitHub nun als Kanban geführt.

---

## 2025-11-26 (Mi)
**Themen:**  
- Feedback zur Ordnerstruktur (zu komplex).  
- Ordnerstruktur überarbeiten und vereinfachen.  
- Crashkurs in PyCharm: Git-Workflow und wichtige Funktionen (Commit, Push, Pull, Branches, Konflikte).  
- Abgleich, wie wir künftig gemeinsam sauber mit GitHub arbeiten (Regeln/Best Practices).
- Weiterführung und Überarbeitung der ADRs, inkl. kurzer Abstimmung zu den Fortschritten, damit alle auf dem gleichen Stand sind und vom Gleichen sprechen.

**Wichtigste Punkte:**  
- Die aktuelle Ordnerstruktur wurde als zu kompliziert bewertet und muss einfacher werden.  
- Ziel: weniger Unterordner, klare Trennung zwischen Code und Doku, gutes Naming.  (bspw. ADR_0000)
- Alle konnten im Crashkurs die wichtigsten Schritte im Git-Workflow üben (Commit → Push → Pull).  
- Einheitliches Vorgehen wurde wichtiger, damit niemand „am Repo vorbei“ arbeitet.  

**Entscheide:**  
- Ordnerstruktur wird reduziert und vereinfacht (weniger Ebenen, klarere Benennung).  
- PyCharm wird als Standard-Tool für Git genutzt (Commit/Push direkt aus PyCharm).  
- Ab jetzt gilt: kleine, saubere Commits mit kurzen Commit-Messages statt seltene „Riesen-Commits“.  
- Änderungen an Struktur/Naming werden dokumentiert (kurzer Hinweis in README oder ADR, falls nötig). 

---

## 2025-12-03 (Mi)
**Themen:**  
- Review der neuen Ordnerstruktur (passt sie jetzt / letzte Anpassungen) – nicht mehr zu viel Zeit mit der Struktur verschwenden.  
- Stand der Teilaufgaben: Nmap/Python, DSGVO, Context Map/BPMN, GUI/PDF, ADRs.  
- Kurze Präsentation des bisherigen Stands und Feedback aus der Klasse.  
- Fokuswechsel: zuerst GUI erstellen, damit man den MVP besser zeigen kann.  
- Risikobewertung: wie sollen die Ports eingestuft werden (z. B. Low/Medium/High) und wie kommt das ins PDF.  
- Report/PDF: Inhalt und Layout grob festlegen (was muss rein, was ist „nice to have“).  
- Nächste Schritte und Zeitplan bis Weihnachten klären.  

**Wichtigste Punkte:**  
- Die vereinfachte Struktur wurde nochmals kurz geprüft und bei Bedarf minimal angepasst.  
- Erste Resultate aus Nmap konnten gelesen/weiterverarbeitet werden (Beispieldaten).  
- Klarheit, welche Infos im Report stehen sollen.  
- Wichtiges Feedback: Backend ist zwar da, aber ohne GUI wirkt es bei einer Demo wenig greifbar → GUI hat Priorität, somit von GUI zu Backend.  

**Entscheide:**   
- GUI wird priorisiert, damit der MVP visuell präsentiert werden kann (Backend wird dafür so weit wie möglich angebunden).  
- Risikostufen werden einfach gehalten und im GUI mit Rot (High), Gelb (Medium), Grün (Low) dargestellt.  
- PDF bekommt eine klare Mindeststruktur (Titel, Ziel, Zusammenfassung, Findings, Empfehlungen).  
- Jeder aktualisiert seinen Teil im Repo bis zur nächsten Sitzung (damit alles zusammengeführt werden kann).

---

## 2025-12-10 (Mi)
**Themen:**  
- Zwischenstand GUI: erste klickbare Oberfläche (Eingaben, Buttons, Navigation).  
- Risikodarstellung in der Ergebnisliste umsetzen (Critical/Mid/Low). Gemeinsame Einstufung der Riskien gemäss Recherche.  
- Backend-Anbindung an die GUI (mindestens „Scan starten“ löst etwas aus).  
- Nmap: Resultate so aufbereiten, dass sie im GUI angezeigt werden können.   
- Kurzer Check ADRs/DSGVO: stimmen die wichtigsten Punkte / fehlt etwas? 

**Wichtigste Punkte:**  
- GUI ist jetzt der Hauptfokus und soll bei einer Demo sauber wirken. 
- Erste Scan-Resultate können im GUI angezeigt werden (mindestens mit Beispieldaten, ideal mit echtem Scan, jedoch nur bewilligt).  
- Es hat sich gezeigt, dass die gewünschte **farbliche Markierung einzelner Ports** in Python/der gewählten Darstellung so nicht sauber möglich ist (entweder alle Ports bekommen eine Farbe oder keine, aber nicht einzeln pro Port wie geplant).  
- Daher wurde die Darstellung angepasst: statt Rot/Gelb/Grün pro Port nutzen wir **Risikostufen-Symbole** (wie im GUI dargestellt) für Critical/Mid/Low.   

**Entscheide:**
- Für die Risikoanzeige werden **Symbole** verwendet (Critical/Mid/Low), nicht die farbliche Markierung einzelner Ports.  
- Für die nächste Demo gilt: lieber ein stabiler Ablauf mit weniger Features als viele halbfertige Funktionen.  
- Minimum bis 17.12: GUI → Scan starten → Resultate anzeigen → PDF erstellen (auch wenn simpel).  
- Ergebnisanzeige wird standardisiert (IP, Hostname, offene Ports, Risikostufe, Kommentar).

---

## 2025-12-17 (Mi)
**Themen:**  
- 

**Wichtigste Punkte:**  
- 

**Entscheide:**  
- 

---

## 2025-12-24 (Mi)
**Themen:**  
- 

**Wichtigste Punkte:**  
- 

**Entscheide:**  
- 
