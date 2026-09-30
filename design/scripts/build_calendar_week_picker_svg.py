"""Build public observed selector states with an explicitly synthetic timetable."""
from pathlib import Path
import hashlib
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / 'design/polyulife'
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)
tag = lambda name: f'{{{NS}}}{name}'

def element(name, **attrs):
    return ET.Element(tag(name), {k.replace('_', '-'): str(v) for k, v in attrs.items()})

def text(parent, value, x, y, size=23, color='#505050'):
    node = element('text', x=x, y=y, fill=color, font_family='sans-serif',
                   font_size=size, text_anchor='middle')
    node.text = value
    parent.append(node)

records = []
for variant, values, source, eid in [
    ('picker', ['Week 4', 'Week 5', 'Week 6'], 'calendar-174230-week-selector-only.png', 'E-CALENDAR-WEEK-PICKER-HEADER'),
    ('wheel-scrolled', ['Week 12', 'Week 13'], 'calendar-174300-selector-thirteen-header-five-only.png', 'E-CALENDAR-WEEK-WHEEL-SCROLLED'),
]:
    root = ET.parse(DEST / 'calendar-week-demo.svg').getroot()
    root.find(tag('title')).text = f'Calendar — Week 5 selector {variant} — DEMO'
    root.find(tag('desc')).text = (
        f'Public native source {source}, header/picker/day strip only. Editable vector/text approximation; '
        'cursor/shadow omitted. Lower timetable is synthetic DEMO copied from calendar-week-demo.svg '
        'and shifted by 186px; this is not observed private body content. Header remains Week 5 in both '
        'states. Two discrete prototype states; no continuous wheel, bounds, arbitrary week selection, '
        'semester switching or successful different-week application. Figma input proxy configured separately.')
    content = root.find(tag('g'))
    children = list(content)
    start = next(i for i, c in enumerate(children) if c.tag == tag('rect') and c.get('y') == '123')
    end = next(i for i, c in enumerate(children) if c.get('id') == 'BottomNavigation')
    defs = root.find(tag('defs'))
    clip = element('clipPath', id='SyntheticExpandedBodyClip')
    clip.append(element('rect', x=0, y=309, width=576, height=611))
    defs.append(clip)
    body_clip = element('g', clip_path='url(#SyntheticExpandedBodyClip)')
    body = element('g', id='SyntheticExpandedTimetable', transform='translate(0 186)')
    for child in children[start:end]:
        content.remove(child)
        body.append(child)
    body_clip.append(body)
    content.insert(start, body_clip)
    heading = next(c for c in content if c.get('id') == 'WeekSelector')
    heading.insert(0, element('rect', x=220, y=38, width=135, height=45, fill='#FFFFFF', fill_opacity=0))
    heading.find(tag('path')).set('d', 'M331 65H346L338 57Z')
    wheel = element('g', id='WeekWheelInputProxy')
    wheel.append(element('rect', x=103, y=113, width=448, height=185, fill='#FFFFFF'))
    for y in [175, 238]:
        wheel.append(element('path', d=f'M103 {y}H448', stroke='#D3D3D3', stroke_width=1))
    wheel.append(element('path', d='M11 298H551', stroke='#D3D3D3', stroke_width=1))
    for label, y in zip(['2025-26 Sem 3', '2026-27 Sem 1', '2026-27 Sem 2'], [151, 214, 274]):
        text(wheel, label, 215, y, 23 if y == 214 else 20, '#171717' if y == 214 else '#505050')
    for label, y in zip(values, [151, 214, 274]):
        text(wheel, label, 400, y, 23 if y == 214 else 20, '#171717' if y == 214 else '#505050')
    content.insert(start, wheel)
    output = DEST / f'calendar-week-{variant}-demo.svg'
    ET.ElementTree(root).write(output, encoding='unicode')
    source_path = ROOT / 'evidence/2026-09-28-full-audit' / source
    records.append({'variant': variant, 'source_evidence_id': eid, 'source_path': str(source_path.relative_to(ROOT)),
                    'source_sha256': hashlib.sha256(source_path.read_bytes()).hexdigest(),
                    'source_crop_size': [576, 384], 'output': output.name,
                    'output_sha256': hashlib.sha256(output.read_bytes()).hexdigest(),
                    'private_content': 'No private course pixels/text; lower body wholly synthetic DEMO.',
                    'limits': 'Observed header/wheel/day strip only; fonts/icons approximate; pointer omitted.'})
(DEST / 'calendar-week-picker-assets.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
