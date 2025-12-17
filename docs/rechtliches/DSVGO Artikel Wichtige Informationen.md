DSVGO

Das wichtigste!

|Artikel|Thema| Kurzbeschreibung                                                                                                                |
|---|---|---------------------------------------------------------------------------------------------------------------------------------|
|**Art. 4** – Begriffsbestimmungen|Definiert zentrale Begriffe wie „personenbezogene Daten“, „Verarbeitung“, „Verantwortlicher“. ([Datenschutz-Grundverordnung (DSGVO)](https://dsgvo-gesetz.de/art-4-dsgvo/?utm_source=chatgpt.com "Art. 4 DSGVO – Begriffsbestimmungen"))| Wichtig, damit  erkennt: Was gilt als „Daten“, wenn wir z. B. IP-Adressen oder Logs verarbeiten wollen.                         |
|**Art. 5** – Grundsätze der Verarbeitung|Regeln wie Rechtmässigkeit, Zweckbindung, Datenminimierung, Speicherbegrenzung, Integrität und Vertraulichkeit. ([Datenschutz-Grundverordnung (DSGVO)](https://dsgvo-gesetz.de/art-5-dsgvo/?utm_source=chatgpt.com "Grundsätze für die Verarbeitung personenbezogener Daten"))| Die Software darf nur so viele Daten erheben und verarbeiten wie nötig, muss sicher sein und nachvollziehbar.                   |
|**Art. 6** – Rechtmässigkeit der Verarbeitung|Legt fest, unter welchen Bedingungen Daten verarbeitet werden dürfen (z. B. Einwilligung, Vertragserfüllung, berechtigtes Interesse). ([Steiger Legal](https://steigerlegal.ch/dsgvo/dsgvo-6/?utm_source=chatgpt.com "Art. 6 DSGVO – Rechtmässigkeit der Verarbeitung"))| Wir müssen klären, auf welcher Rechtsgrundlage wir Daten erheben oder verarbeiten (z. B. Logs von Systemen, Scans über Geräte). |
|**Art. 9** – Verarbeitung besonderer Kategorien personenbezogener Daten|Regelt besonders schützenswerte Daten (z. B. Gesundheits-, biometrische Daten) mit erhöhtem Schutz. ([datenschutzstelle.li](https://www.datenschutzstelle.li/datenschutz/themen-z/art-9_u_art-10-dsgvo?utm_source=chatgpt.com "Besondere Kategorien personenbezogener Daten (Art. 9 ..."))| Nur relevant, wenn wir z. B. Gesundheitsdaten oder biometrische Daten verarbeiten                                               |
|**Art. 30** – Verzeichnis von Verarbeitungstätigkeiten|Verantwortliche müssen ein Verzeichnis führen, wenn bestimmte Voraussetzungen erfüllt sind. ([onetrust.com](https://www.onetrust.com/blog/gdpr-compliance/?utm_source=chatgpt.com "Your complete guide to General Data Protection Regulation (GDPR ..."))| Wir sollten dokumentieren: Welche Daten wir verarbeiten, wozu, wie lange, wer Zugriff hat.                                      |
|**Art. 32** – Sicherheit der Verarbeitung|Technische und organisatorische Massnahmen zur Sicherheit personenbezogener Daten.| Wichtig bei eurer Lösung: Logfiles, Scan-Daten, Reports müssen sicher verarbeitet und gespeichert werden.                       |
|**Art. 33** – Meldung von Verletzungen des Schutzes personenbezogener Daten|Datenpannen müssen ggf. an die Aufsichtsbehörde gemeldet werden.| Falls eure Software Daten verarbeitet und z. B. unbefugt darauf zugegriffen wird — u. U. relevant.                              |
|**Art. 44 ff.** – Datenübermittlungen in Drittländer|Wenn personenbezogene Daten ausserhalb der EU übertragen werden, gelten besondere Regeln.| Relevant, wenn euer Produkt das Ausland einbindet (z. B. Cloud, Drittanbieter).                                                 |
|**Art. 82** – Anspruch auf Schadensersatz|Betroffene haben Anspruch auf Entschädigung bei Datenschutzverletzungen.| Ein Risiko für euch: Wenn ihr nicht sauber arbeitet, kann Haftung entstehen.                                                    |

**Speziell wichtiges für unser Szenario**

- Wenn die Software **nur lokal** läuft und **keine persönlichen Daten** (z. B. von natürlichen Personen) erhebt oder speichert, ist vieles einfacher.

- Wenn aber z. B. Logs mit IP-Adressen, Domainnamen, Nutzer-IDs oder Daten von Mitarbeitern/Kunden verarbeitet, dann gilt DSGVO automatisch.

- Beispiel: Erfassung von IP-Adressen oder Hostnamen kann **personenbezogene Daten** sein, wenn diese Rückschlüsse auf eine Person erlauben. → Art. 4 definieren.

- Wir müssen sicherstellen: minimal notwendige Daten (Art. 5 Datenminimierung), klare Rechtsgrundlage (Art. 6) und angemessene Sicherheit (Art. 32).

- Falls personenbezogene Daten an Drittanbieter gehen (z. B. externes Reporting, Cloud), dann Vertrags- und Übermittlungs-Pflichten (Art. 28 ff., Art. 44 ff.).

- wir sollten ein Verzeichnis der Verarbeitungstätigkeiten führen (Art. 30) und überlegen, ob eine **Datenschutzfolgeabschätzung (DSFA / DPIA)** nötig ist (bei hohen Risiken).

- Auch wenn wir sagen „nur lokale Installation“, müssen wir dokumentieren, **wo Daten sind**, wer Zugriff hat, wie lange gespeichert wird (Art. 5 Speicherbegrenzung).


Muss Soll Kann

## 🧩 **ZeroTrace DSGVO-Checkliste (Schul-/Startup-Projekt)**

### 🟥 **MUSS (gesetzlich verpflichtend)**

|Thema|DSGVO-Artikel|Beschreibung|Umsetzung / Maßnahme|
|---|---|---|---|
|**Datenminimierung**|Art. 5 Abs. 1 c|Nur Daten verarbeiten, die für den Scan nötig sind.|Keine personenbezogenen Daten speichern. IPs ggf. anonymisieren oder nur temporär im RAM.|
|**Zweckbindung & Transparenz**|Art. 5 Abs. 1 a,b|Daten nur zum definierten Zweck „Sicherheitsanalyse im eigenen Netzwerk“.|Zweck in der App-Info / Datenschutzerklärung klar beschreiben.|
|**Rechtmäßigkeit der Verarbeitung**|Art. 6 Abs. 1 f|Datenverarbeitung erlaubt, wenn „berechtigtes Interesse“ (eigene IT-Sicherheit).|Im Projekt dokumentieren: Verarbeitung erfolgt im Rahmen Sicherheitsprüfung eigener Systeme.|
|**Integrität & Vertraulichkeit (Sicherheit)**|Art. 32|Technische und organisatorische Maßnahmen (TOM) zum Schutz der Daten.|Lokale Speicherung verschlüsseln (SQLite-Verschlüsselung / AES). Keine Übertragung ins Internet.|
|**Protokollierung & Zugriffsbeschränkung**|Art. 32 Abs. 1 b|Nur autorisierte Nutzer dürfen Zugriff auf Scan-Daten haben.|Passwortgeschütztes UI / nur lokale Benutzer (Admin).|
|**Speicherbegrenzung**|Art. 5 Abs. 1 e|Daten nur solange aufbewahren, wie nötig.|Reports nach x Tagen automatisch löschen.|
|**Dokumentation der Verarbeitung**|Art. 30|Verzeichnis der Verarbeitungstätigkeiten (wer, was, wozu, wie lange).|Kurze Tabelle im Projekt-Wiki (Datenarten, Speicherort, Verantwortlicher).|

---

### 🟧 **SOLL (empfohlen, erhöht Vertrauen & Nachvollziehbarkeit)**

|Thema|DSGVO-Artikel|Beschreibung|Umsetzung / Maßnahme|
|---|---|---|---|
|**Privacy by Design / Default**|Art. 25|Datenschutz in die Architektur eingebaut.|Voreinstellung: keine Cloud-Verbindungen, lokale Logs, manuelle Zustimmung für Scans.|
|**Anonymisierung / Pseudonymisierung**|Art. 32 Abs. 1 a|Reduziert Risiko, wenn Daten verloren gehen.|IPs in Reports maskieren (z. B. `192.168.x.x`).|
|**Informationspflichten**|Art. 13–14|Betroffene informieren, wenn Daten Dritter berührt werden.|In Schulumgebung reicht: schriftliche Zustimmung der IT oder Lehrkraft für Testnetz.|
|**Auftragsverarbeitung (falls Cloud / extern)**|Art. 28|Wenn Daten bei einem Dienstleister verarbeitet werden.|Nicht nötig beim lokalen MVP – später bei Cloud-Variante wichtig.|
|**Datenpannen-Prozess**|Art. 33|Vorgabe, was bei Datenverlust passiert.|Schulisch reicht: dokumentieren, an wen ihr das melden würdet (z. B. Lehrer / Datenschutzbeauftragter).|

---

### 🟩 **KANN (gute Praxis, stärkt Vertrauen & Marktwert)**

| Thema                                         | DSGVO-Artikel   | Beschreibung                                     | Umsetzung / Maßnahme                                              |
| --------------------------------------------- | --------------- | ------------------------------------------------ | ----------------------------------------------------------------- |
| **Einwilligungsdialog**                       | Art. 7          | Nutzer bestätigt Nutzung auf eigenes Netzwerk.   | „Ich bestätige, dass ich befugt bin, diesen Scan auszuführen.“    |
| **Log-Anonymisierung**                        | Art. 5 Abs. 1 c | Noch weniger personenbezogene Daten.             | Ergebnisse ohne Hostnamen/IPs speichern.                          |
| **Audit-Trail / Nachvollziehbarkeit**         | Art. 5 Abs. 2   | Zeigt Verantwortlichkeit und Professionalität.   | Logbuch: wer wann gescannt hat (lokal).                           |
| **DSFA (Datenschutz-Folgenabschätzung)**      | Art. 35         | Risikoanalyse bei hohem Risiko für Betroffene.   | Nicht nötig im MVP, aber später für Produkt gut zu erwähnen.      |
| **Datenschutzbeauftragter / Ansprechpartner** | Art. 37         | Pflicht ab 20 Personen in der Datenverarbeitung. | Für MVP nicht nötig – in Zukunft bei Kundenorganisation relevant. |
|                                               |                 |                                                  |                                                                   |

