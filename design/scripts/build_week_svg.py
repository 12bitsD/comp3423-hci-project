"""Editable observed weekly-calendar geometry with wholly synthetic coursework."""
from build_study_svg import rect, text, group, line, screen, bottom_nav, demo_badge

body = rect(0, 0, 576, 113, '#FFFFFF')
body += group('WeekSelector', text(275, 70, 'Week 5', 26, 700, anchor='middle') + '<path d="M331 60H346L338 68Z" fill="#565656"/>')
body += text(288, 101, 'Sep-Oct | 2026-27 Semester 1', 19, 700, '#505050', 'middle')
body += group('MonthView', rect(500, 47, 76, 54, '#E4A17D', 12) + '<rect x="514" y="62" width="28" height="26" rx="2" stroke="white" stroke-width="3"/><path d="M520 56V66M536 56V66M514 70H542M519 76H537M519 82H537" stroke="white" stroke-width="3"/>')
body += demo_badge()
body += rect(82, 123, 494, 74, '#D2EF41', 14)
for i, (d, n) in enumerate([('Mon','28'),('Tue','29'),('Wed','30'),('Thu','01'),('Fri','02'),('Sat','03')]):
    x = 82 + 87*i
    body += group('WeekDay'+d, text(x+43, 149, d, 19, color='#52652A', anchor='middle') + text(x+43, 185, n, 29, color='#52652A', anchor='middle'))
for i in range(9):
    y = 287 + 87*i
    body += line(82, y, 576, y, '#F0F0F0', 1) + text(60, y+6, f'{8+i:02d}:30', 14, anchor='end')
for x in range(82, 577, 87):
    body += line(x, 197, x, 920, '#EFEFEF', 1)
# These are invented layout samples, not copied course names, enrolments or slots.
for gid, x, y, h, code, kind, room in [
    ('DemoClass1', 169, 374, 174, 'EXM101', 'DEMO', 'ROOM A'),
    ('DemoClass2', 430, 548, 174, 'EXM202', 'DEMO', 'ROOM B'),
]:
    content = rect(x, y, 86, h, '#F4FBED', 6)
    for j, value in enumerate([code, kind, room]):
        content += text(x+8, y+24+j*18, value, 13 if j<2 else 11)
    body += group(gid, content)
body += rect(82, 838, 494, 53, '#FFF6DE', 6) + text(329, 870, 'Synthetic timetable · DEMO', 19, 700, '#775313', 'middle')
body += bottom_nav('Calendar')
screen('calendar-week-demo.svg', 'Calendar — Week 5 — DEMO',
       'calendar-174154-week-five-header-only.png; native Home Calendar recheck on 2026-09-29', body,
       'Week/day/header and weekly-grid geometry follow the observed native screen. All timetable blocks and their count, placement, duration, codes and rooms are synthetic. No real coursework pixels or private body text are included. The native Home Calendar entry reached this weekly view on the recheck; it did not reach the month-view sample. Week selection and month switching are not implemented by this static source.', True)
print('Built calendar-week-demo.svg with synthetic timetable data.')
