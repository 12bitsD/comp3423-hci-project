"""Prepare dated Class/Exam/Notice SVGs from already archived native evidence.

This only writes local design sources and an unconfigured connection plan. It
does not operate PolyULife/Figma or add native executions or mapped Figma nodes.
Requires Pillow. Optional --render-dir additionally requires resvg_py.
"""
from pathlib import Path
from copy import deepcopy
from datetime import datetime, timezone
import argparse
import base64
import hashlib
import json
import xml.etree.ElementTree as E

from PIL import Image, ImageDraw

R = Path(__file__).resolve().parents[2]
D = R / 'design/polyulife'
P = R / 'evidence/2026-10-02-native-calendar-resume'
NS = 'http://www.w3.org/2000/svg'
XL = 'http://www.w3.org/1999/xlink'
E.register_namespace('', NS)
E.register_namespace('xlink', XL)
SID = 'S-NATIVE-OCT2-'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
tag = lambda n: '{' + NS + '}' + n


def node(name, **attrs):
    return E.Element(tag(name), {k.replace('_', '-'): str(v) for k, v in attrs.items()})


def find(root, ident):
    return next(n for n in root.iter() if n.get('id') == ident)


def label(parent, x, y, value, size=22, color='#404040', **attrs):
    t = node('text', x=x, y=y, font_family='sans-serif', font_size=size,
             fill=color, **attrs)
    t.text = value
    parent.append(t)
    return t


def group(parent, name):
    g = node('g', id=name)
    parent.append(g)
    return g


def rect(parent, x, y, w, h, fill, **attrs):
    parent.append(node('rect', x=x, y=y, width=w, height=h, fill=fill, **attrs))


def path(parent, d, stroke='#404040', width=3, **attrs):
    parent.append(node('path', d=d, fill='none', stroke=stroke,
                       stroke_width=width, **attrs))


def hit(parent, x, y, w, h):
    rect(parent, x, y, w, h, '#FFFFFF', fill_opacity='0.001')


def image(parent, asset, x, y, w, h):
    n = node('image', x=x, y=y, width=w, height=h)
    n.set('{' + XL + '}href', 'data:image/png;base64,' +
          base64.b64encode(asset.read_bytes()).decode())
    parent.append(n)


def titled(root, title):
    root.find(tag('title')).text = title
    root.find(tag('desc')).text = (
        'Fixed Oct2 native fullscreen sample normalized to 576x1024. '
        'Private values are synthetic DEMO and personal date markers omitted. '
        'Editable chrome is approximate; map and loading mark are documented raster crops. '
        'Local design source only: not imported, connected or replayed in Figma. '
        'Unknown outcomes and complete application fidelity remain unverified.')
    return root


def calendar(applied, draft=None):
    root = E.parse(D / ('calendar-oct2-all-demo.svg' if applied == 'class'
                       else 'calendar-oct2-none.svg')).getroot()
    if applied != 'none':
        find(root, 'CalendarCategory').find(tag('text')).text = applied.capitalize()
    filt = find(root, 'Filter')
    filt.find(tag('rect')).set('fill', '#FFFFFF')
    filt.find(tag('path')).set('fill', '#E59B7B')
    if applied == 'class':
        # The three tiny dots are visible; a transparent target keeps them selectable.
        hit(find(root, 'DemoEventEllipsis'), 502, 633, 43, 46)
    if draft:
        panel = deepcopy(find(E.parse(D / 'calendar-filter-none.svg').getroot(), 'FilterOverlay'))
        find(panel, 'FilterBackdrop').set('height', '1024')
        if draft != 'none':
            row = find(panel, draft.capitalize())
            circle = row.find(tag('circle'))
            circle.set('stroke', '#F39772')
            cy = float(circle.get('cy'))
            # Check geometry is an editable approximation of the observed native mark.
            path(row, f'M169 {cy}L175 {cy+5}L190 {cy-10}', '#F39772', 3.5,
                 stroke_linecap='round', stroke_linejoin='round')
        root.append(panel)
    return titled(root, f'Oct2 Calendar applied {applied}; draft {draft or "closed"}')


def header(root):
    rect(root, 0, 0, 576, 1024, '#FFFFFF', id='ScreenBackground')
    g = group(root, 'DetailHeader')
    rect(g, 0, 0, 576, 100, '#FFFFFF', stroke='#CCCCCC')
    b = group(g, 'Back')
    hit(b, 8, 25, 48, 60)
    path(b, 'M35 54L26 64L35 74', '#242424', 7, stroke_linecap='round')
    label(g, 69, 65, 'EXM2001 · DEMO CLASS', 27, '#242424', font_weight='700')
    label(g, 560, 20, 'SYNTHETIC VALUES', 10, '#876B39', text_anchor='end')


def new_root(title):
    r = node('svg', width=576, height=1024, viewBox='0 0 576 1024')
    r.append(node('title'))
    r.append(node('desc'))
    return titled(r, title)


def detail(map_asset):
    r = new_root('Oct2 Class detail — DEMO')
    header(r)
    rect(r, 18, 100, 539, 924, '#FFFFFF', rx=36, stroke='#C5D0D5')
    label(r, 35, 144, 'Synthetic course event', 28, '#242424', font_weight='700')
    label(r, 35, 182, 'DEMO course information', 22)
    rect(r, 35, 218, 85, 28, '#F0F0F0', rx=14)
    label(r, 43, 239, '#Canvas', 19, '#686868')
    label(r, 35, 274, 'DEMO instructor', 22)
    c = group(r, 'ClassInformation')
    rect(c, 35, 299, 506, 275, '#F6FCF0', rx=23, stroke='#D9DDD5', stroke_width=1.8)
    rect(c, 36, 300, 504, 151, '#EAFBDA', rx=22)
    rect(c, 36, 425, 504, 26, '#EAFBDA')
    path(c, 'M35 451H541M288 451V574', '#D9DDD5', 1.5)
    book = group(c, 'ClassTypeBookApproximation')
    book.append(node('path', d='M158 364Q172 357 182 365Q193 358 205 364V397Q192 390 182 398Q171 390 158 396Z', fill='#8C9382'))
    path(book, 'M182 366V392M188 369H200M188 376H200M188 383H200', '#EAFBDA', 2)
    label(c, 230, 364, 'Class Type', 20)
    label(c, 230, 399, 'LEC+TUT/LAB', 27, '#161616', font_weight='700')
    label(c, 161, 514, '09:00–10:00', 22, text_anchor='middle')
    label(c, 414, 514, 'EXAMPLE ROOM', 20, text_anchor='middle')
    g = group(r, 'ClassNotice')
    rect(g, 35, 606, 214, 51, '#FFFFFF', rx=26, stroke='#DDDDDD', stroke_width=1.8)
    path(g, 'M69 628L64 633Q58 641 65 644Q71 646 77 638M72 633L80 626Q85 619 79 619Q74 618 69 624', '#55B4A6', 3.2, stroke_linecap='round')
    label(g, 91, 640, 'Class Notice', 21, '#5E5E5E')
    path(g, 'M210 628H219V637M210 637L219 628', '#888888', 2.6)
    g = group(r, 'CampusMapRaster')
    image(g, map_asset, 35, 677, 506, 307)
    # The raster contains the native fullscreen control. Recreate editable chrome over
    # it, retaining an unconfigured target instead of inventing an expanded-map outcome.
    f = group(r, 'MapFullscreenUnverified')
    rect(f, 445, 914, 72, 63, '#FFFFFF', rx=14, stroke='#ADBCC4', stroke_width=1.6)
    path(f, 'M481 930H496V945M480 946L495 931M480 959H465V944M481 943L466 958', '#363636', 4, stroke_linejoin='round')
    return r


def notice(kind, loading_asset):
    r = new_root('Class Notice — ' + kind)
    header(r)
    g = group(r, 'NoticeWebview')
    rect(g, 8, 77, 561, 947, '#F6F8F5', rx=23, stroke='#C9CBC9')
    rect(g, 9, 151, 559, 728, '#FFFFFF')
    rect(g, 9, 141, 559, 11, '#DEDEDE')
    close = group(g, 'CloseNotice')
    hit(close, 15, 87, 52, 49)
    path(close, 'M32 104L52 125M52 104L32 125', '#454B4A', 3.5, stroke_linecap='round')
    more = group(g, 'NoticeMore')
    hit(more, 496, 87, 63, 49)
    for x in (515, 528, 541):
        more.append(node('circle', cx=x, cy=114, r=4, fill='#424645'))
    if kind == 'loading':
        image(group(g, 'LoadingMarkRaster'), loading_asset, 260, 532, 59, 60)
    footer = group(g, 'BrowserFooter')
    rect(footer, 0, 879, 576, 145, '#F6F8F5')
    path(footer, 'M8 879H568', '#C5C5C5', 1)
    path(footer, 'M56 910L42 925L56 940M110 910L124 925L110 940', '#BABEBD', 3.5)
    rect(footer, 150, 894, 388, 62, '#FFFFFF', rx=13, stroke='#AAAAAA')
    path(footer, 'M177 924V922Q177 914 182 914Q187 914 187 922V924', '#444444', 2.5)
    rect(footer, 176, 923, 12, 11, '#444444', rx=1.5)
    label(footer, 200, 934, 'www.polyu.edu.hk/ar/do...', 20, '#888888')
    rel = group(footer, 'NoticeReloadUnverified')
    hit(rel, 488, 900, 43, 47)
    path(rel, 'M518 921A13 13 0 1 0 523 930M511 912L519 920L510 925', '#444444', 2.8)
    if kind == 'menu':
        menu = group(r, 'NoticeMenuOverlay')
        rect(menu, 0, 0, 576, 1024, '#000000', fill_opacity='.7')
        rect(menu, 18, 639, 540, 258, '#FFFFFF', rx=20)
        for name, text, y in [('SystemBrowserUnverified', 'Open in system browser', 683),
                              ('ShareUnverified', 'Share via...', 769),
                              ('CopyUnverified', 'Copy link', 855)]:
            item = group(menu, name)
            hit(item, 18, y-44, 540, 86)
            label(item, 288, y+10, text, 27, '#000000', text_anchor='middle')
        path(menu, 'M19 725H557M19 810H557', '#E7E7E7', 1)
        cancel = group(menu, 'CancelNoticeMenu')
        rect(cancel, 18, 909, 540, 86, '#FFFFFF', rx=20)
        label(cancel, 288, 962, 'Cancel', 27, '#FF0000', text_anchor='middle')
    return r


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--render-dir', type=Path)
    args = ap.parse_args()
    target = D / 'calendar-oct2-class-exam-sources.json'
    if target.exists():
        existing = json.loads(target.read_text())
        assert all(x['status'] == 'prepared_not_imported_not_replayed' for x in existing['sources']), 'Do not overwrite imported-source bookkeeping'
    coverage = json.loads((R / 'docs/polyulife/coverage.json').read_text())
    evidence = {e['id']: e for e in coverage['evidence']}
    assets = []
    for name, source, box, eid in [
        ('calendar-class-campus.png', '13-class-ellipsis-detail.png', (35, 677, 541, 984), 'E-NATIVE-OCT2-13'),
        ('calendar-notice-loading-mark.png', '14-class-notice-open.png', (260, 532, 319, 592), 'E-NATIVE-OCT2-14')]:
        source_path = P / source
        assert sha(source_path) == evidence[eid]['sha256']
        dest = D / 'assets' / name
        Image.open(source_path).crop(box).save(dest)
        assets.append({'file': 'assets/' + name, 'sha256': sha(dest),
                       'source_evidence_id': eid, 'source_sha256': sha(source_path),
                       'crop_xyxy': list(box), 'dimensions': list(Image.open(dest).size),
                       'source': 'Crop of an already redacted native screenshot; not a live map or vector logo'})
    map_asset, loading_asset = [D / a['file'] for a in assets]
    # Native map contains its fullscreen control. It is covered with recreated editable
    # chrome above. The geography/labels and attribution remain raster pixels.
    specs = [
        ('draft-class-none', 'DRAFT-CLASS-NONE', [11], calendar('none', 'class'), 'none', 'class'),
        ('class', 'CLASS', [12, 19], calendar('class'), 'class', None),
        ('class-detail', 'CLASS-DETAIL', [13, 18], detail(map_asset), None, None),
        ('notice-loading', 'NOTICE-LOADING', [14], notice('loading', loading_asset), None, None),
        ('notice-blank', 'NOTICE-BLANK', [15, 17], notice('blank', loading_asset), None, None),
        ('notice-menu', 'NOTICE-MENU', [16], notice('menu', loading_asset), None, None),
        ('draft-class-class', 'DRAFT-CLASS-CLASS', [20], calendar('class', 'class'), 'class', 'class'),
        ('draft-none-class', 'DRAFT-NONE-CLASS', [21], calendar('class', 'none'), 'class', 'none'),
        ('draft-exam-class', 'DRAFT-EXAM-CLASS', [22], calendar('class', 'exam'), 'class', 'exam'),
        ('exam', 'EXAM', [23], calendar('exam'), 'exam', None),
        ('draft-exam-exam', 'DRAFT-EXAM-EXAM', [24], calendar('exam', 'exam'), 'exam', 'exam'),
        ('draft-none-exam', 'DRAFT-NONE-EXAM', [25], calendar('exam', 'none'), 'exam', 'none'),
        ('draft-payment-exam', 'DRAFT-PAYMENT-EXAM', [26], calendar('exam', 'payment'), 'exam', 'payment'),
    ]
    sources = []
    for key, state, steps, root, applied, draft in specs:
        eids = [f'E-NATIVE-OCT2-{n:02d}' for n in steps]
        assert all(SID + state in evidence[e]['state_ids'] for e in eids)
        p = D / f'calendar-oct2-{key}.svg'
        E.ElementTree(root).write(p, encoding='unicode')
        p.write_text(p.read_text().rstrip() + '\n')
        ids = [n.get('id') for n in root.iter() if n.get('id')]
        assert len(ids) == len(set(ids)), p
        sources.append({'file': p.name, 'sha256': sha(p), 'dimensions': [576, 1024],
                        'state_id': SID + state, 'source_evidence_ids': eids,
                        'source_evidence_sha256': {e: evidence[e]['sha256'] for e in eids},
                        'applied_background': applied, 'draft': draft,
                        'editable_group_ids': ids,
                        'status': 'prepared_not_imported_not_replayed'})
    controls = {11: 'Class', 12: 'Apply', 13: 'DemoEventEllipsis', 14: 'ClassNotice',
                16: 'NoticeMore', 17: 'CancelNoticeMenu', 18: 'CloseNotice', 19: 'Back',
                20: 'Filter', 21: 'Class', 22: 'Exam', 23: 'Apply', 24: 'Filter',
                25: 'Exam', 26: 'Payment'}
    roots = {s['state_id']: set(s['editable_group_ids']) for s in sources}
    roots[SID + 'DRAFT-NONE-NONE'] = {n.get('id') for n in E.parse(D / 'calendar-oct2-draft-none-none.svg').getroot().iter()}
    edges = []
    for step, control in controls.items():
        a = next(a for a in coverage['actions'] if a['id'] == f'A-NATIVE-OCT2-{step:02d}')
        assert a['status'] == 'observed' and control in roots[a['from_state_id']]
        assert a['target_state_id'] in roots
        edges.append({'action_id': a['id'], 'from_state_id': a['from_state_id'],
                      'target_state_id': a['target_state_id'], 'trigger_group': control,
                      'trigger': 'On click', 'proposed_behavior': 'Navigate to',
                      'status': 'planned_not_configured', 'native_source_evidence_ids': a['evidence_ids']})
    edges.append({'action_id': None, 'from_state_id': SID + 'NOTICE-LOADING',
                  'target_state_id': SID + 'NOTICE-BLANK', 'trigger_group': None,
                  'trigger': 'After delay', 'delay_ms': 800, 'proposed_behavior': 'Navigate to',
                  'status': 'planned_not_configured',
                  'native_source_evidence_ids': ['E-NATIVE-OCT2-14', 'E-NATIVE-OCT2-15'],
                  'inference': 'A proposed demo delay between successive recorded states; not measured native latency or proof of successful webpage load.'})
    limits = [
        'Not imported, connected or replayed in Figma; native and Figma coverage counts stay unchanged.',
        'Private values are DEMO, private date markers omitted, geometry and generic icons approximate.',
        'Campus map is raster with editable fullscreen chrome; live map/gestures/outcomes unverified.',
        'Notice blank is an observed snapshot, not a successfully loaded document.',
        'Native Payment Apply outcome unknown: no result frame or Apply connection is invented.',
        'Proposed Navigate-to composite frames preserve this finite reference context only; main Home/More callers need integration.',
        'Other draft combinations, X exits, map actions, Reload and browser menu results still require observation.',
    ]
    plan = {'kind': 'unconfigured_figma_connection_plan', 'status': 'planned_not_configured',
            'existing_entry': {'state_id': SID + 'DRAFT-NONE-NONE', 'node_id': '791:873',
                               'node_id_source': 'Previously verified mapping; re-read live editor before editing'},
            'connections': edges, 'limits': limits}
    (D / 'calendar-oct2-class-exam-plan.json').write_text(json.dumps(plan, ensure_ascii=False, indent=2) + '\n')
    result = {'sources': sources, 'assets': assets, 'limits': limits}
    if args.render_dir:
        import resvg_py
        out = args.render_dir.resolve()
        out.mkdir(parents=True, exist_ok=True)
        now = datetime.now(timezone.utc).isoformat()
        manifest = {'kind': 'local_design_source_render_not_figma_or_native_capture',
                    'session_id': None, 'renderer': 'resvg_py ' + resvg_py.__version__,
                    'images': []}
        sheet = Image.new('RGB', (1728, 1596), '#E8E8E8')
        draw = ImageDraw.Draw(sheet)
        for i, s in enumerate(sources):
            p = out / Path(s['file']).with_suffix('.png').name
            p.write_bytes(resvg_py.svg_to_bytes(svg_path=str(D / s['file'])))
            im = Image.open(p).convert('RGB')
            assert im.size == (576, 1024)
            manifest['images'].append({'file': p.name, 'sha256': sha(p), 'dimensions': list(im.size),
                                       'prepared_at_utc': now, 'state_id': s['state_id'],
                                       'source': 'Local SVG render; NOT Figma replay or new native evidence',
                                       'svg_file': s['file'], 'svg_sha256': s['sha256']})
            x, y = (i % 6) * 288, (i // 6) * 532
            sheet.paste(im.resize((270, 480)), (x+9, y+39))
            draw.text((x+8, y+5), s['file'].removeprefix('calendar-oct2-'), fill='#111111')
            draw.text((x+8, y+21), 'LOCAL SOURCE / NOT IMPORTED', fill='#765519')
        p = out / 'contact-sheet.png'
        sheet.save(p)
        manifest['contact_sheet'] = {'file': p.name, 'sha256': sha(p), 'dimensions': list(sheet.size),
                                      'source': 'Contact sheet of local SVG renders'}
        (out / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
        result['local_render_manifest'] = str((out / 'manifest.json').relative_to(R))
        result['local_render_review'] = 'Prepared; manual review required. Not Figma acceptance.'
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'prepared_sources': len(sources), 'planned_connections': len(edges),
                      'figma_mutations': 0, 'native_executions': 0}, indent=2))


if __name__ == '__main__':
    main()
