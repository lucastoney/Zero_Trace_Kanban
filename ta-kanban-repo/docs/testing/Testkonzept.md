# ADR <Nummer>: <Titel der Entscheidung>

*Status:* Proposed / Accepted / Rejected / Superseded  
*Datum:* 03.12.2025
*Autor:* Sag / Alle 
*Betroffene Bereiche:* Security / Performance 

---

## 🎯 1. Kontext

Wir müssen verschiedene Test schreiben sowohl für GUI als auch für das Backend. Wir werden nach TDD vorgehen. 
Testing des GUI:
- Logik
- Vernetzung mit Backend 
- UI, Usability, Durability 
- Anzeigen und Ladeanzeigen
BAckend: 
- Logik
- Funktionen
- PDF Export erst einfach dann Auswahl 

TDD Vorgehensvorschlag: 

RED – Wir schreiben zuerst den Test (z. B. test_run_network_scan_parses_single_up_host)
→ Er schlägt fehl, weil run_network_scan noch nicht (oder nicht korrekt) implementiert ist.

GREEN – Wir implementieren gerade so viel Logik, dass der Test grün wird
→ z. B. XML parsen, ScanResult erzeugen.

REFACTOR – Wir räumen Code auf, ohne das Verhalten zu ändern
→ Tests bleiben grün und dienen als Sicherheitsnetz.

Genauso für die GUI:
Erst Test schreiben, der erwartet, dass btn_scan bei Net+Port „Benutzerdefinierter Scan…“ anzeigt.
Dann _update_scan_button_state so implementieren, bis der Test grün ist.

---

## ⚖️ 2. Entscheidung

Wir entscheiden uns, das ganze wie oben erwähnt umzusetzten, resp. werden wir 2 Dateien für die Testproggramierung anlegen, und 2 welche den fertigen Code enthalten werden.
Es wird aber bei beiden optimiert und getestet, da es Funktionen geben wird die nicht automatisierbar sind oder besser welche nur in der echten Umgebung getestet werden können.
---

## 🧠 3. Begründung

Warum ist diese Entscheidung richtig?

| Argument           | Beschreibung                                                                                                                                                                                                           |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TDD Vorgehensweise | Da wir diese im Buch gelesen haben und es als Sinvoll erscheint werden wir nach dieser Strategie arbeiten. <br/> Da wir das Gui vorbereitet haben ist dies jetzt auch möglich und wir können verbesserungen vornehmen. |
| TDD Nachteile      | Extrem Komplex den überblick zu erhalten wenn man neu ins Projekt kommt, schwierig alle Personen zu involvieren. Wir werden aufteilen müssen.                                                                          |
                                                                                                                                                                                                                  |

---

