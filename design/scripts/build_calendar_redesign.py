"""Build the optimized Calendar redesign SVGs for the COMP3423 team file.

Design-only source generation: no user research data or live app claims.
All event/course values are explicitly synthetic DEMO values.
"""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parents[1] / "polyulife" / "redesign-calendar"
OUT.mkdir(parents=True, exist_ok=True)
W, H = 390, 844
C = {
    "bg": "#F7F8F4", "card": "#FFFFFF", "ink": "#17201B", "muted": "#66736A",
    "line": "#E2E7DF", "green": "#2F8F78", "green_dark": "#237460",
    "green_soft": "#E7F3ED", "lime": "#DDF26A", "lime_soft": "#F4F9D9",
    "shadow": "#000000", "white": "#FFFFFF", "overlay": "#17201B",
}

def text(x, y, s, size=16, fill=None, weight=400, anchor=None, family="Inter, 'Noto Sans SC', sans-serif"):
    a = f' text-anchor="{anchor}"' if anchor else ""
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{fill or C["ink"]}"{a}>{escape(str(s))}</text>'

def rect(x, y, w, h, fill, rx=0, stroke=None, sw=1, opacity=None):
    op = f' opacity="{opacity}"' if opacity is not None else ""
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{st}{op}/>'

def circle(cx, cy, r, fill, stroke=None, sw=1):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{st}/>'

def line(x1, y1, x2, y2, stroke, sw=1.5, cap="round"):
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}"/>'

def base(title, back="‹ Home", subtitle="2026–27 · Semester 1"):
    s = [rect(0, 0, W, H, C["bg"])]
    s += [text(16, 24, "09:41", 12, C["muted"], 600),
          rect(300, 8, 82, 22, C["lime_soft"], 6), text(341, 23, "DEMO DATA", 9, C["muted"], 700, "middle")]
    if back:
        s += [f'<g id="HomeBack">{text(16, 52, back, 16, C["green_dark"], 600)}</g>']
    s += [text(195, 53, title, 24, C["ink"], 750, "middle"), text(195, 82, subtitle, 13, C["muted"], 500, "middle")]
    return s

def month(selected=2):
    s = [rect(16, 104, 358, 304, C["card"], 18, C["line"]),
         f'<g id="PreviousMonth">{text(34, 140, "‹", 28, C["green_dark"], 500)}</g>',
         text(195, 139, "October 2026", 19, C["ink"], 700, "middle"),
         f'<g id="NextMonth">{text(352, 140, "›", 28, C["green_dark"], 500)}</g>']
    weekdays = ["M", "T", "W", "T", "F", "S", "S"]
    for i, d in enumerate(weekdays):
        s.append(text(46 + i*50, 169, d, 12, C["muted"], 650, "middle"))
    days = [[28,29,30,1,2,3,4],[5,6,7,8,9,10,11],[12,13,14,15,16,17,18],[19,20,21,22,23,24,25],[26,27,28,29,30,31,1]]
    for r, row in enumerate(days):
        for col, day in enumerate(row):
            x, y = 46 + col*50, 202 + r*43
            muted = (r == 0 and col < 3) or (r == 4 and col == 6)
            if day == selected and not muted:
                s += [f'<g id="Day{day}">', circle(x, y-7, 17, C["green"]), text(x, y, day, 14, C["white"], 700, "middle"), '</g>']
            else:
                s += [f'<g id="Day{day}_{r}_{col}">', text(x, y, day, 14, "#B0B8B1" if muted else C["ink"], 500, "middle")]
                if day in (2, 3, 9) and not muted:
                    s.append(circle(x, y+9, 2.4, C["green"]))
                s.append('</g>')
    return s

def filter_row(mode="All", count=1):
    label = {"All":"All events", "Class":"Class", "Exam":"Exam"}[mode]
    noun = "event" if count == 1 else "events"
    s = [text(16, 440, "Fri, Oct 2", 23, C["ink"], 750),
         f'<g id="FilterButton">{rect(278, 414, 96, 44, C["green_soft"], 12), text(326, 442, "Filter", 15, C["green_dark"], 700, "middle")}</g>',
         f'<g id="ActiveFilter">{rect(16, 462, 104 if mode != "All" else 112, 34, C["green_soft"] if mode != "All" else C["lime_soft"], 10), text(68 if mode != "All" else 72, 485, label + (" ✓" if mode != "All" else ""), 13, C["green_dark"], 650, "middle")}</g>',
         text(136, 485, f"{count} {noun} on this date", 13, C["muted"], 500)]
    if mode != "All":
        s += [f'<g id="ClearFilter">{text(342, 485, "Clear", 13, C["green_dark"], 650, "end")}</g>']
    return s

def event_card(y=530):
    return [f'<g id="ClassCard">{rect(16, y, 358, 152, C["card"], 16, C["line"])}',
            rect(32, y+18, 52, 52, C["green_soft"], 14), text(58, y+52, "CL", 18, C["green_dark"], 750, "middle"),
            text(100, y+35, "EXM2001 · DEMO CLASS", 15, C["ink"], 750),
            text(100, y+61, "Synthetic course event", 14, C["muted"], 500),
            line(32, y+84, 358, y+84, C["line"], 1),
            text(32, y+111, "09:00–10:00", 14, C["ink"], 600),
            text(170, y+111, "EXAMPLE ROOM", 13, C["muted"], 500),
            text(32, y+137, "Class", 12, C["green_dark"], 650),
            text(354, y+76, "›", 26, C["green_dark"], 500, "end"), '</g>']

def bottom_nav(active="Calendar"):
    s = [rect(0, 784, 390, 60, C["card"], 0, C["line"]),
         f'<g id="NavHome">{text(58, 813, "⌂", 23, C["muted"], 500, "middle"), text(58, 833, "Home", 10, C["muted"], 500, "middle")}</g>',
         f'<g id="NavCalendar">{circle(140, 807, 16, C["lime_soft"]), text(140, 813, "▦", 19, C["green_dark"], 600, "middle"), text(140, 833, "Calendar", 10, C["green_dark"], 650, "middle")}</g>',
         text(238, 815, "▢", 22, C["muted"], 500, "middle"), text(238, 833, "QR", 10, C["muted"], 500, "middle"),
         text(326, 815, "•••", 19, C["muted"], 600, "middle"), text(326, 833, "More", 10, C["muted"], 500, "middle")]
    return s

def main_screen(mode="All"):
    s = base("Calendar") + month() + filter_row(mode, 1 if mode != "Exam" else 0)
    if mode == "Exam":
        s += [rect(16, 528, 358, 218, C["card"], 16, C["line"]),
              circle(195, 584, 28, C["green_soft"]), text(195, 592, "▦", 27, C["green_dark"], 600, "middle"),
              text(195, 636, "No exams on this date", 20, C["ink"], 750, "middle"),
              text(195, 666, "Try another date, or show all events for Oct 2.", 13, C["muted"], 400, "middle"),
              f'<g id="ShowAllEvents">{rect(91, 692, 208, 46, C["green"], 12), text(195, 721, "Show all events", 15, C["white"], 700, "middle")}</g>']
    else:
        s += event_card(530)
    return s + bottom_nav()

def filter_screen(selected="Class"):
    s = base("Calendar", back="") + month()
    s += [rect(0, 0, 390, 844, C["overlay"], opacity=0.34),
          rect(0, 288, 390, 556, C["card"], 24),
          rect(174, 304, 42, 5, C["line"], 3),
          text(24, 350, "Filter events", 23, C["ink"], 750),
          f'<g id="CloseFilter">{text(354, 350, "×", 28, C["muted"], 500, "end")}</g>',
          text(24, 380, "Draft selection is kept until you apply or close.", 13, C["muted"], 400)]
    options = [("Select All", False), ("Class", selected == "Class"), ("Exam", selected == "Exam"), ("Payment", False), ("Acad calendar", False)]
    for i, (label, checked) in enumerate(options):
        y = 416 + i*58
        s += [f'<g id="FilterOption_{label.replace(" ", "")}">', rect(16, y, 358, 50, C["green_soft"] if checked else C["card"], 12, C["green"] if checked else C["line"]),
              circle(42, y+25, 11, C["green"] if checked else C["card"], C["green"] if checked else "#AAB3AC", 1.5),
              text(42, y+30, "✓" if checked else "", 13, C["white"], 700, "middle"),
              text(68, y+31, label, 16, C["ink"], 600), '</g>']
    s += [f'<g id="ResetFilter">{text(28, 766, "Reset", 16, C["green_dark"], 650)}</g>',
          f'<g id="ApplyFilter">{rect(196, 730, 178, 52, C["green"], 14), text(285, 762, "Apply", 17, C["white"], 700, "middle")}</g>']
    return s

def detail_screen():
    s = base("Class details", back="‹ Classes", subtitle="EXM2001 · DEMO CLASS")
    s += [text(24, 128, "Synthetic course event", 23, C["ink"], 750),
          rect(24, 148, 166, 26, C["lime_soft"], 7), text(107, 166, "DEMO COURSE INFO", 10, C["muted"], 700, "middle"),
          rect(16, 202, 358, 330, C["card"], 16, C["line"])]
    rows = [("Class type", "LEC+TUT/LAB"), ("Time", "09:00–10:00"), ("Location", "EXAMPLE ROOM"), ("Instructor", "DEMO instructor"), ("Source", "#Canvas")]
    for i, (k, v) in enumerate(rows):
        y = 238 + i*62
        s += [text(34, y, k, 13, C["muted"], 500), text(34, y+25, v, 16, C["ink"], 650)]
        if i < len(rows)-1:
            s.append(line(34, y+43, 356, y+43, C["line"], 1))
    s += [f'<g id="ClassNotice">{rect(16, 554, 358, 72, C["green_soft"], 14), text(34, 584, "Class Notice", 16, C["green_dark"], 700), text(34, 607, "Course updates and attachments", 12, C["muted"], 400), text(352, 594, "›", 24, C["green_dark"], 500, "end")}</g>',
          f'<g id="BackToClasses">{rect(16, 680, 358, 52, C["green"], 14), text(195, 712, "Back to classes", 16, C["white"], 700, "middle")}</g>']
    return s + bottom_nav()

def svg(name, body, desc):
    source = f'''<svg xmlns="http://www.w3.org/2000/svg" width="390" height="844" viewBox="0 0 390 844" fill="none"><title>{escape(name)}</title><desc>{escape(desc)}</desc>{''.join(body)}</svg>'''
    (OUT / (name + ".svg")).write_text(source, encoding="utf-8")

DESC = "Optimized Calendar redesign; synthetic DEMO values only. Theory-driven design, not yet validated by new participants."
svg("C01-Calendar-All", main_screen("All"), DESC + " All events with visible filter and selected date.")
svg("C02-Calendar-Filter-Class", filter_screen("Class"), DESC + " Class draft with explicit Apply/Reset/Close.")
svg("C03-Calendar-Class-Only", main_screen("Class"), DESC + " Applied Class filter with visible status and Clear.")
svg("C04-Calendar-Class-Detail", detail_screen(), DESC + " Class detail with consistent return path.")
svg("C05-Calendar-Filter-Exam", filter_screen("Exam"), DESC + " Exam draft with explicit Apply/Reset/Close.")
svg("C06-Calendar-Exam-Empty", main_screen("Exam"), DESC + " Recoverable empty state with Show all events.")
print("Wrote 6 SVGs to", OUT)
