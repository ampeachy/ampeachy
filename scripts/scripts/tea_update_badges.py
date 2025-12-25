import json, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "tea_guestbook.json"

TOTAL_BADGE = ROOT / "data" / "badge_tea_total.json"
TODAY_BADGE = ROOT / "data" / "badge_tea_today.json"

PURPLE = "6A4C93"

def main():
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    mugs = payload.get("mugs", [])

    today = datetime.date.today().isoformat()
    total = len(mugs)
    today_count = sum(1 for m in mugs if m.get("date") == today)

    TOTAL_BADGE.write_text(json.dumps({
        "schemaVersion": 1,
        "label": "Cups of tea served",
        "message": str(total),
        "color": PURPLE
    }, indent=2), encoding="utf-8")

    TODAY_BADGE.write_text(json.dumps({
        "schemaVersion": 1,
        "label": "Cups today",
        "message": str(today_count),
        "color": PURPLE
    }, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main()
