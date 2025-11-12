#!/usr/bin/env python3
import os, csv, sys, json, argparse, re
import requests

PRIO_MAP = {"H":"prio:high","M":"prio:med","L":"prio:low"}
STATUS_MAP = {"offen":"status:open","kritisch":"status:critical","erledigt":"status:done","info":"status:info"}
CAT_PREFIX = "cat:"

def gh(api, method="GET", json_data=None):
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN not set")
    headers = {"Authorization": f"Bearer {token}","Accept":"application/vnd.github+json"}
    url = f"https://api.github.com{api}"
    r = requests.request(method, url, headers=headers, json=json_data)
    if r.status_code >= 300:
        raise SystemExit(f"GitHub API error {r.status_code}: {r.text}")
    return r.json() if r.text else {}

def ensure_label(owner, repo, name, color="0b76d9", description=""):
    try:
        gh(f"/repos/{owner}/{repo}/labels/{name}")
    except SystemExit:
        gh(f"/repos/{owner}/{repo}/labels", "POST", {"name":name,"color":color,"description":description})

def ensure_milestone(owner, repo, title):
    ms = gh(f"/repos/{owner}/{repo}/milestones?state=all")
    for m in ms:
        if m["title"] == title:
            return m["number"]
    m = gh(f"/repos/{owner}/{repo}/milestones","POST",{"title":title})
    return m["number"]

def upsert_issue(owner, repo, issue_title, body, labels, assignees, milestone, id_key):
    q = f'repo:{owner}/{repo} "{id_key}" in:title'
    res = gh(f"/search/issues?q={requests.utils.quote(q)}")
    issue = None
    for item in res.get("items", []):
        if item["title"].startswith(id_key):
            issue = item
            break
    payload = {"title":issue_title, "body":body, "labels":labels}
    if assignees: payload["assignees"] = assignees
    if milestone: payload["milestone"] = milestone
    if issue:
        gh(f"/repos/{owner}/{repo}/issues/{issue['number']}", "PATCH", payload)
    else:
        gh(f"/repos/{owner}/{repo}/issues","POST",payload)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--repo", required=True, help="owner/repo")
    p.add_argument("--tasks", default="tasks.csv")
    p.add_argument("--team", default="team.json")
    args = p.parse_args()
    owner, repo = args.repo.split("/",1)

    with open("labels.json","r",encoding="utf-8") as lf:
        for L in json.load(lf):
            ensure_label(owner, repo, L["name"], L.get("color","0b76d9"), L.get("description",""))
    team = json.load(open(args.team, "r", encoding="utf-8"))
    assignee_by_kurz = {k: v.get("github","") for k,v in team.items() if v.get("github")}

    with open(args.tasks, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            id_ = row["id"].strip()
            kategorie = row["kategorie"].strip()
            task = row["task"].strip()
            kommentar = row["kommentar"].strip()
            verantw = row["verantw"].strip()
            kw = row["faelligkeit_kw"].strip()
            prio = PRIO_MAP.get(row["prioritaet"].strip(), "prio:med")
            status = STATUS_MAP.get(row["status"].strip(), "status:open")
            bezug = row["bezug_ta"].strip()

            labels = [prio, status, f"{CAT_PREFIX}{kategorie}"]
            assignees = []
            if verantw and verantw in assignee_by_kurz:
                assignees = [assignee_by_kurz[verantw]]

            milestone = None
            # Accept "KW 47", "47", "46 / 12.11.25", "KW 17 (2025)", "laufend"
            m = re.search(r"(?:KW\s*)?(\d{1,2})", kw)
            if m and kw.lower() != "laufend":
                title = f"KW {m.group(1)}"
                milestone = ensure_milestone(owner, repo, title)

            title_prefix = f"[{id_}] "
            issue_title = f"{title_prefix}{task}"
            body = (
                f"**Kategorie:** {kategorie}\n"
                f"**Kommentar:** {kommentar}\n\n"
                f"**Zuständig:** {verantw or '-'}\n"
                f"**Fälligkeit:** {kw or '-'}\n"
                f"**Bezug TA:** {bezug or '-'}\n\n"
                f"---\n"
                f"_Automatisch aus tasks.csv synchronisiert._"
            )
            upsert_issue(owner, repo, issue_title, body, labels, assignees, milestone, title_prefix)

if __name__ == "__main__":
    main()
