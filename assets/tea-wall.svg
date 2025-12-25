import json, pathlib, datetime, math, hashlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "tea_guestbook.json"
OUT  = ROOT / "assets" / "tea-wall.svg"

MAX_MUGS = 30
COLS = 6

# Tea shades
TEAS = [
  ("matcha", "#8BC34A"),
  ("lavender latte", "#B69CFF"),
  ("chai", "#B07A57"),
]

def pick_tea(login: str):
    h = hashlib.md5(login.encode("utf-8")).hexdigest()
    idx = int(h[:2], 16) % len(TEAS)
    return TEAS[idx]

def mug(x, y, label, tea_color, steam_phase):
    return f"""
    <g transform="translate({x},{y})">
      <rect x="0" y="10" rx="16" ry="16" width="200" height="92"
            fill="#CDBEFF" fill-opacity="0.90"
            stroke="#F6F1FF" stroke-opacity="0.90" stroke-width="2"/>
      <path d="M200 28 C232 28,232 84,200 84" fill="none"
            stroke="#F6F1FF" stroke-opacity="0.90" stroke-width="10" stroke-linecap="round"/>

      <ellipse cx="78" cy="34" rx="56" ry="10" fill="{tea_color}" fill-opacity="0.55"/>
      <ellipse cx="78" cy="33" rx="52" ry="8" fill="{tea_color}" fill-opacity="0.40"/>

      <text x="154" y="72" font-family="system-ui, -apple-system, Segoe UI"
            font-size="22" fill="#5B2EFF" opacity="0.85">♥</text>

      <path d="M42 24 C30 10, 54 6, 44 -6" fill="none"
            stroke="#F6F1FF" stroke-opacity="0.22" stroke-width="4"
            stroke-linecap="round" stroke-dasharray="12 18">
        <animate attributeName="stroke-dashoffset"
                 values="{steam_phase};{steam_phase+30}"
                 dur="2.2s" repeatCount="indefinite"/>
        <animate attributeName="opacity"
                 values="0.16;0.30;0.16" dur="2.2s" repeatCount="indefinite"/>
      </path>

      <path d="M74 24 C62 10, 86 6, 76 -6" fill="none"
            stroke="#F6F1FF" stroke-opacity="0.16" stroke-width="4"
            stroke-linecap="round" stroke-dasharray="10 22">
        <animate attributeName="stroke-dashoffset"
                 values="{steam_phase+8};{steam_phase+38}"
                 dur="2.5s" repeatCount="indefinite"/>
        <animate attributeName="opacity"
                 values="0.10;0.22;0.10" dur="2.5s" repeatCount="indefinite"/>
      </path>

      <text x="100" y="66" text-anchor="middle"
            font-family="system-ui, -apple-system, Segoe UI"
            font-size="18" fill="#1E1B22" opacity="0.95">{label}</text>
    </g>
    """

def main():
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    mugs = payload.get("mugs", [])[-MAX_MUGS:][::-1]

    rows = max(1, math.ceil(len(mugs) / COLS))
    width = 1400
    height = 160 + rows * 120

    svg = [f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <linearGradient id="bg" x1="0" x2="1">
      <stop offset="0" stop-color="#12061C"/>
      <stop offset="1" stop-color="#5B2EFF"/>
    </linearGradient>
    <filter id="soft" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="10"/>
    </filter>
  </defs>

  <rect width="{width}" height="{height}" fill="url(#bg)"/>
  <circle cx="260" cy="70" r="64" fill="#F6F1FF" opacity="0.07" filter="url(#soft)"/>
  <circle cx="1180" cy="88" r="78" fill="#F6F1FF" opacity="0.05" filter="url(#soft)"/>

  <text x="60" y="72" font-family="system-ui, -apple-system, Segoe UI" font-size="34" fill="#F6F1FF" opacity="0.95">☕ Tea Wall</text>
  <text x="60" y="104" font-family="system-ui, -apple-system, Segoe UI" font-size="16" fill="#F6F1FF" opacity="0.75">Thanks for stopping by. Would you like a cup of tea to go?</text>
"""]

    start_x, start_y = 60, 140
    gap_x, gap_y = 220, 120

    for i, m in enumerate(mugs):
        r = i // COLS
        c = i % COLS
        x = start_x + c * gap_x
        y = start_y + r * gap_y

        login = m.get("login","guest")
        label = ("@" + login)[:14]
        _, tea_color = pick_tea(login)

        svg.append(mug(x, y, label, tea_color, steam_phase=i*3))

    svg.append(f"""
  <text x="{width-60}" y="{height-24}" text-anchor="end"
    font-family="system-ui, -apple-system, Segoe UI" font-size="14"
    fill="#F6F1FF" opacity="0.55">Updated {datetime.date.today().isoformat()}</text>
</svg>""")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("".join(svg), encoding="utf-8")

if __name__ == "__main__":
    main()
