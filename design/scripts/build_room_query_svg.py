"""Build editable Room query states from the 2026-09-29 native recheck.
No Figma import, prototype connection, or visual acceptance is implied.
"""
from pathlib import Path
import copy
import hashlib
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
DESIGN = ROOT / 'design/polyulife'
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)

def tag(name):
    return '{' + NS + '}' + name

def node(name, **attrs):
    return ET.Element(tag(name), {k.replace('_', '-'): str(v) for k, v in attrs.items()})

def text(x, y, value, size=17, color='#404040', anchor='middle', **attrs):
    e = node('text', x=x, y=y, fill=color, font_family='sans-serif', font_size=size,
             text_anchor=anchor, **attrs)
    e.text = value
    return e

def find(root, ident):
    return root.find(".//*[@id='" + ident + "']")

def replace_dates(root, sunday):
    old = find(root, 'DatesShifted') if sunday and find(root, 'DatesShifted') is not None else find(root, 'Dates')
    index = list(root).index(old)
    root.remove(old)
    g = node('g', id='DatesObserved20260929', clip_path='url(#DatesViewport)')
    days = [('Today', '29-Sep'), ('Wed', '30-Sep'), ('Thu', '01-Oct'),
            ('Fri', '02-Oct'), ('Sat', '03-Oct'), ('Sun', '04-Oct'), ('Mon', '05-Oct')]
    xs = [-70, 23, 117, 210, 303, 397, 490] if sunday else [70, 166, 259, 352, 445, 539, 633]
    selected = 5 if sunday else 0
    for i, ((day, date), x) in enumerate(zip(days, xs)):
        row = node('g', id='Date-' + day)
        row.append(node('rect', x=x-40, y=112, width=80, height=67, rx=9,
                        fill='#54B39F' if i == selected else '#FFFFFF'))
        for y, value in [(140, day), (163, date)]:
            row.append(text(x, y, value, color='#FFFFFF' if i == selected else '#404040',
                            font_weight='600' if i == selected else '400'))
        g.append(row)
    root.insert(index, g)

def input_value(root, value, focused=False, clear=False):
    search = find(root, 'Search')
    old = find(root, 'RoomInputValue')
    if old is not None:
        search.remove(old)
    if value:
        search.append(text(122, 233, value, 22, '#090909', 'start', id='RoomInputValue'))
    if clear:
        g = node('g', id='ClearInput')
        g.append(node('rect', x=402, y=201, width=44, height=44, fill='#FFFFFF', fill_opacity='0.001'))
        g.append(node('path', d='M416 216L432 232M432 216L416 232', stroke='#9CAFB9', stroke_width=3))
        search.append(g)
    if focused:
        # Observed caret only; a fixed snapshot does not simulate editable text.
        cx = 122 if not value else 234
        search.append(node('path', id='ObservedCaret', d=f'M{cx} 207V239', stroke='#1684EC', stroke_width=2))

def no_result(root):
    old = find(root, 'EmptyState')
    root.remove(old)
    g = node('g', id='NoRoomFound')
    g.append(node('path', d='M270 411L306 447M306 411L270 447', stroke='#319987',
                  stroke_width=9, stroke_linecap='round'))
    g.append(text(288, 498, 'No room found', 25, '#575757', font_weight='600'))
    g.append(text(288, 530, 'Please search another room.', 23, '#9CAFB9', font_weight='500'))
    root.append(g)

empty = ET.parse(DESIGN/'room-empty.svg').getroot()
rows = [
    ('ag206-suggestion', 'S-ROOM-QUERY-AG206', '02-query-filled', False, 'AG206', False, True),
    ('dirty-results', 'S-ROOM-QUERY-DIRTY', '12-unmatched-query', True, 'ZZZZ9999', True, True),
    ('no-result', 'S-ROOM-QUERY-NONE', '13-unmatched-search', True, 'ZZZZ9999', False, False),
    ('cleared-stale', 'S-CLEARED', '15-cleared-stale-empty', True, '', True, True),
    ('empty-sunday', 'S-EMPTYQUERY', '16-empty-search', True, '', False, False),
]
manifest = []
for label, state, evidence, sunday, value, focus, clear in rows:
    root = ET.parse(DESIGN/'room-sunday-all.svg').getroot() if label == 'dirty-results' else copy.deepcopy(empty)
    replace_dates(root, sunday)
    input_value(root, value, focus, clear)
    if label in ['no-result', 'cleared-stale']:
        no_result(root)
    if label == 'ag206-suggestion':
        g = node('g', id='AG206Suggestion')
        g.append(node('rect', x=105.5, y=257, width=348, height=63, rx=9,
                      fill='#FFFFFF', stroke='#DCDCDC', stroke_width=1.5))
        g.append(text(122, 298, 'AG206', 22, '#090909', 'start'))
        root.append(g)
    if label == 'dirty-results':
        slots = find(root, 'SlotsScrollContent')
        results = find(root, 'Results')
        results.remove(slots)
        cp = node('clipPath', id='ObservedListViewport')
        cp.append(node('rect', x=26, y=426, width=524, height=544))
        root.find(tag('defs')).append(cp)
        viewport = node('g', id='ObservedListOffset', clip_path='url(#ObservedListViewport)')
        slots.set('transform', 'translate(0,-396)')
        viewport.append(slots)
        results.append(viewport)
    root.find(tag('title')).text = 'Room query — ' + label
    root.find(tag('desc')).text = (
        'Editable source from native room-recheck-' + evidence + '.png. Fixed observed date and input; '
        'not yet imported into Figma. Fonts and icons approximate. Cursor and macOS input fringe omitted. '
        'No live availability, free input, delay or unobserved query behavior is implemented. '
        'Dirty-results uses a fixed observed list offset; true list end and scrollbar fidelity unverified.')
    path = DESIGN/('room-query-' + label + '.svg')
    ET.ElementTree(root).write(path, encoding='unicode')
    src = ROOT/'evidence/2026-09-28-full-audit'/('room-recheck-'+evidence+'.png')
    manifest.append({'file':path.name, 'state_id':state, 'figma_node_id':None,
                     'status':'source_only_not_imported', 'source_evidence_path':str(src.relative_to(ROOT)),
                     'source_evidence_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
                     'sha256':hashlib.sha256(path.read_bytes()).hexdigest(), 'dimensions':[576,970]})
(DESIGN/'room-query-sources.json').write_text(json.dumps({'status':'source_only_not_imported',
    'frames':manifest, 'native_reference':'docs/polyulife/room-recheck-20260929.json',
    'remaining':['Import via Figma UI and verify native layers', 'Connect observed query/clear/search transitions with explicit input limitations',
                 'Replay from correct date context', 'Compare rendered geometry and text against native evidence']},ensure_ascii=False,indent=2)+'\n')
print('Built five editable Room query SVG sources; no Figma coverage increment.')
