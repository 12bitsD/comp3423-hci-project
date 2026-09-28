"""Preserve the Home scrolling reconstruction as editable SVG sources.

Combines existing public/synthetic designs; no app, private data or network reads.
SVGs describe content and clipping only. Figma scrolling and constraints must be
configured separately using home-scroll-layout.json and the recorded walkthrough.
"""
import json
import xml.etree.ElementTree as ET
from pathlib import Path

from build_study_svg import home_features

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'design/polyulife'
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')


def build():
    for day, source in [('monday', 'top'), ('tuesday', 'tuesday')]:
        tree = ET.parse(OUT / f'home-demo-{source}.svg')
        svg = tree.getroot()
        svg.find(f'{{{NS}}}title').text = f'Home — DEMO — {day.title()} — Scroll content'
        svg.find(f'{{{NS}}}desc').text = (
            'Editable reconstruction; all personal agenda, counts, times, rooms, subjects and exams are synthetic DEMO. '
            'Public date/navigation evidence follows the existing Home sources. '
            'Continuous content combines top and features samples using a 353-unit offset; this is inferred geometry, '
            'not proof of native full scrolling extent. Frame viewport 576x970; body viewport x0 y100 w576 h735; '
            'body content extends to y1187 in root coordinates, allowing 352 units of vertical scroll. '
            'Header, bottom sheet preview and bottom navigation remain outside the scrolling frame. '
            'SVG itself has no scrolling/navigation. In Figma convert the body clip group to a Frame, remove its old mask, '
            'keep Clip content, set vertical overflow, and constrain body children Top instead of Scale. '
            'Original fixed-position SVG samples remain historical references. Fonts/icons approximate the UI. '
            'Sheet expansion, other dates, card details and native complete content boundary remain unverified.'
        )
        viewport = svg.find(f'.//{{{NS}}}clipPath[@id="HomeContentClip"]/{{{NS}}}rect')
        viewport.set('height', '735')
        content = next(e for e in svg.iter() if e.get('clip-path') == 'url(#HomeContentClip)')
        content.set('id', 'HomeScrollViewport')
        features = ET.fromstring(f'<g xmlns="{NS}" transform="translate(0,353)">{home_features()}</g>')
        content.append(features)
        tree.write(OUT / f'home-demo-{day}-scroll.svg', encoding='unicode', xml_declaration=False)
    layout = {
        'revision_id': 'FIGMA-HOME-CONTINUOUS-SCROLL',
        'root_size': [576, 970],
        'viewport': {'position': [0, 100], 'size': [576, 735], 'clip_content': True, 'overflow': 'Vertical'},
        'children_vertical_constraint': 'Top',
        'features_in_viewport': {'position': [78, 909], 'size': [454, 178]},
        'inferred_scroll_range': [0, 352],
        'native_full_extent_verified': False,
        'fixed_outside_viewport': ['Header', 'BottomSheet', 'BottomNavigation'],
        'frames': [
            {'day': 'Monday', 'root_node_id': '67:569', 'viewport_node_id': '67:654',
             'features_node_id': '113:57', 'source': 'home-demo-monday-scroll.svg'},
            {'day': 'Tuesday', 'root_node_id': '67:694', 'viewport_node_id': '67:780',
             'features_node_id': '113:12', 'source': 'home-demo-tuesday-scroll.svg'}
        ],
        'limitations': [
            'Range and spacing derived from two samples, not a newly observed native endpoint.',
            'Private agenda content is synthetic, with approximate geometry.',
            'Feature links copied from existing Home sample; only Apps direct-entry returns replayed in this batch.',
            'Apps Back is history Back for direct Home entries only; category detours are not covered.',
            'Other source returns and native full application remain incomplete.'
        ]
    }
    (OUT / 'home-scroll-layout.json').write_text(json.dumps(layout, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    build()
    print('Built two Home scroll content SVGs and Figma layout metadata.')
