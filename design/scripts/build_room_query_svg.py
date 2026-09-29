"""Build editable Room query states from the 2026-09-29 native recheck.

The manifest separates native source evidence from recorded Figma sample replays.
Sample navigation does not establish full visual acceptance or application coverage.
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
    ('today-all', 'S-ALL', '04-today-all', False, 'AG206', False, False),
    ('dirty-results', 'S-ROOM-QUERY-DIRTY', '12-unmatched-query', True, 'ZZZZ9999', True, True),
    ('no-result', 'S-ROOM-QUERY-NONE', '13-unmatched-search', True, 'ZZZZ9999', False, False),
    ('focused-no-result', 'S-ROOM-QUERY-NONE', '14-clear-query', True, 'ZZZZ9999', True, True),
    ('cleared-stale', 'S-CLEARED', '15-cleared-stale-empty', True, '', True, True),
    ('empty-sunday', 'S-EMPTYQUERY', '16-empty-search', True, '', False, False),
]
figma_node_ids = {
    'ag206-suggestion': '381:265',
    'today-all': '396:19',
    'dirty-results': '381:72',
    'no-result': '381:19',
    'focused-no-result': '383:19',
    'cleared-stale': '381:327',
    'empty-sunday': '381:383',
}
manifest = []
for label, state, evidence, sunday, value, focus, clear in rows:
    root = (ET.parse(DESIGN/'room-sunday-all.svg').getroot() if label == 'dirty-results'
            else ET.parse(DESIGN/'room-all.svg').getroot() if label == 'today-all'
            else copy.deepcopy(empty))
    replace_dates(root, sunday)
    input_value(root, value, focus, clear)
    if label == 'today-all':
        result_date = find(root, 'ResultDate')
        for icon_part in list(result_date)[:-1]:
            icon_part.set('transform', 'translate(-18,0)')
        result_date_label = result_date.find(tag('text'))
        result_date_label.text = '29-Sep (Today)'
        result_date_label.set('x', '426')
        result_date_label.set('text-anchor', 'start')
        result_date_label.set('font-size', '15')
    if label in ['no-result', 'focused-no-result', 'cleared-stale']:
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
        'Fonts and icons approximate. Cursor and macOS input fringe omitted. '
        'No live availability, free input, delay or unobserved query behavior is implemented. '
        'Dirty-results uses a fixed observed list offset; true list end and scrollbar fidelity unverified. '
        'For focused-no-result, the clear icon shape is inferred from the adjacent focused input states; '
        'the E14 screenshot confirms caret and unchanged query but its pointer obscures the icon.')
    path = DESIGN/('room-query-' + label + '.svg')
    ET.ElementTree(root).write(path, encoding='unicode')
    src = ROOT/'evidence/2026-09-28-full-audit'/('room-recheck-'+evidence+'.png')
    figma_node_id = figma_node_ids.get(label)
    manifest.append({'file':path.name, 'state_id':state, 'figma_node_id':figma_node_id,
                     'status':'sample_present_replayed_partial_fidelity',
                     'source_evidence_path':str(src.relative_to(ROOT)),
                     'source_evidence_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
                     'sha256':hashlib.sha256(path.read_bytes()).hexdigest(), 'dimensions':[576,970]})
(DESIGN/'room-query-sources.json').write_text(json.dumps({'status':'figma_query_samples_replayed_full_scope_incomplete',
    'frames':manifest, 'native_reference':'docs/polyulife/room-recheck-20260929.json',
    'figma_file_url':'https://www.figma.com/design/ulBuuteCRdzdBsHAaiqyUr/',
    'figma_page_id':'12:104',
    'coverage_ledger_status':'archived_in_docs/polyulife/coverage.json; native observations unchanged',
    'prototype_replay_evidence_manifest':'evidence/2026-09-30-room-query-replay/manifest.json',
    'prototype_replays':[
        {'id':'PROTO-ROOM-QUERY-AG206-001','flow_name':'Room · AG206 suggestion to Today ALL',
         'start_node_id':'381:265','observed_node_sequence':['381:265','396:19'],
         'result':'sample_navigation_passed; Today 29-Sep sample only'},
        {'id':'PROTO-ROOM-QUERY-UNMATCHED-001','flow_name':'Room · unmatched search, clear, retry',
         'start_node_id':'381:72','observed_node_sequence':['381:72','381:19','383:19','381:327','381:383'],
         'result':'sample_navigation_passed; static query text and click/focus proxy only'}],
    'connections_editor_verified':[
        {'source_node_id':'381:323', 'trigger':'On click', 'action':'Navigate to', 'destination_node_id':'396:19',
         'native_evidence':'E-ROOM-RECHECK-03', 'prototype_run_id':'PROTO-ROOM-QUERY-AG206-001'},
        {'source_node_id':'381:113', 'trigger':'On click', 'action':'Navigate to', 'destination_node_id':'381:19', 'native_evidence':'E-ROOM-RECHECK-13', 'prototype_run_id':'PROTO-ROOM-QUERY-UNMATCHED-001'},
        {'source_node_id':'381:60', 'trigger':'On click', 'action':'Navigate to', 'destination_node_id':'383:19', 'native_evidence':'E-ROOM-RECHECK-14', 'prototype_run_id':'PROTO-ROOM-QUERY-UNMATCHED-001', 'native_action_id':None, 'fidelity':'click/focus proxy; native E14 was an unsuccessful clear-coordinate attempt'},
        {'source_node_id':'383:67', 'trigger':'On click', 'action':'Navigate to', 'destination_node_id':'381:327', 'native_evidence':'E-ROOM-RECHECK-15', 'prototype_run_id':'PROTO-ROOM-QUERY-UNMATCHED-001'},
        {'source_node_id':'381:369', 'trigger':'On click', 'action':'Navigate to', 'destination_node_id':'381:383', 'native_evidence':'E-ROOM-RECHECK-16', 'prototype_run_id':'PROTO-ROOM-QUERY-UNMATCHED-001'},
    ],
    'local_render_review':{
        'renderer':'resvg-py0.5.0; local system fonts',
        'comparison_path':'assets/room-query-source-comparison.png',
        'sha256':'5ec5a0aeddd8a6e8fed743d76ad3188ceedaf1fe120d6fd3c15472ba7bf511d1',
        'dimensions':[1440,1010],
        'result':'Five initial sources rendered and compared side by side with native evidence. Focused no-result and Today ALL sources rendered separately. Font weight/metrics, exact icon shapes and scrollbar remain deviations. This review predates the separately recorded Figma Present replay.'
    },
    'remaining':['Implement real text input, suggestion timing, other query strings and branches',
                 'Observe and reproduce remaining dates, availability cases and return paths',
                 'Compare native and Figma typography/icons and full bounds beyond these samples',
                 'Complete the rest of PolyULife; current Room query samples do not establish full application coverage']},ensure_ascii=False,indent=2)+'\n')
print('Built seven editable Room query SVG sources; Figma mapping is tracked separately.')
