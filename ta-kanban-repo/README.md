# TA – MVP Schwachstellen-Scanner · Kanban

Repo zum Verwalten der Aufgaben für die Transferarbeit (Zero Trust · Nmap/Python GUI · Reporting).
**Kanban** erfolgt über GitHub Issues + Labels + (optional) GitHub Projects Board.

## Schnellstart
1. Erstelle ein neues leeres GitHub-Repository und lade diesen Inhalt hoch.
2. Synchronisiere Labels und Issues lokal:
   ```bash
   # Voraussetzung: Python 3.10+, GitHub-Token mit 'repo' Rechten
   export GITHUB_TOKEN=YOUR_TOKEN
   pip install -r requirements.txt
   python scripts/sync_issues.py --repo <owner>/<repo>
   ```
3. (Optional) Erzeuge ein GitHub Project (Kanban) und aktiviere Auto-Add für Issues.
4. Arbeite im Board mit Labels/Assignees. Status wird über **Status-Labels** gepflegt.

## Labels
- **status:open** 🟨 – offen
- **status:critical** 🟥 – kritisch
- **status:done** 🟩 – erledigt
- **status:info** ⚪ – Info
- **prio:high** 🔴, **prio:med** 🟡, **prio:low** 🟢
- **cat:<Kategorie>** (Dokumentation, Konzept, Technik, Tests, Evaluation, Organisation, Reflexion, Diverses)

## Felder-Mapping (aus `tasks.csv`)
- `id` → Issue-Nummer (als Präfix im Titel)
- `kategorie` → Label `cat:<kategorie>`
- `task` → Titel
- `kommentar` → Body (inkl. Bezug TA, Fälligkeit, Ampel)
- `verantw` → Assignee (Kürzel → Mapping in `team.json`)
- `faelligkeit_kw` → Milestone `KW <num>` (wird automatisch erzeugt)
- `prioritaet` → Label `prio:*`
- `status` → Label `status:*`
- `bezug_ta` → Body-Section

## Team-Kürzel
- Stl: Luca Steiner
- Ner: Roman Nemchenko
- Wey: Yves Weber
- Sam: Manuel Sager
- Cag: Giovanni Cardillo
- Rat: Thines Rasiah

---

### Dateien
- `tasks.csv` – Alle Aufgaben (können in Excel/Sheets gepflegt werden)
- `team.json` – Mapping Kürzel → GitHub-User (nachtragen)
- `scripts/sync_issues.py` – Erstellt/aktualisiert Labels, Milestones und Issues anhand `tasks.csv`
- `.github/ISSUE_TEMPLATE/task.yml` – Issue-Vorlage für neue Tasks
- `labels.json` – Standard-Labels
- `requirements.txt` – Python Abhängigkeiten

> Hinweis: Der Sync ist idempotent. Wird `tasks.csv` geändert, aktualisiert der Script die Issues anhand der `id`.
