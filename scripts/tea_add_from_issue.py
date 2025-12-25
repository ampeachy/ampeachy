import json, os, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "tea_guestbook.json"

def main():
    event = json.loads(pathlib.Path(os.environ["GITHUB_EVENT_PATH"]).read_text(encoding="utf-8"))
    issue = event["issue"]

    login = issue["user"]["login"]
    created_at = issue.get("created_at") or datetime.datetime.utcnow().isoformat() + "Z"
    date = created_at[:10]
    note = (issue.get("body") or "").strip()[:240]

    payload = json.loads(DATA.read_text(encoding="utf-8"))
    payload.setdefault("mugs", []).append({
        "login": login,
        "date": date,
        "note": note,
    })

    DATA.write_text(json.dumps(payload, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main()
