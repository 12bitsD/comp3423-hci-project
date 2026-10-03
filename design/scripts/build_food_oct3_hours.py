"""Prepare four finite hours-expanded Food viewports from public evidence.

Reuses editable venue rows from the frozen current list; no app or Figma input.
These are sampled viewports, not complete scrolling or navigation models.
"""
from pathlib import Path
import copy, hashlib, json, re, xml.etree.ElementTree as E
from PIL import Image
from build_calendar_class_exam_oct2 import node, group, rect, label, path, image
from build_food_oct3_details import header

R = Path(__file__).resolve().parents[2]
D = R / 'design/polyulife'
P = R / 'evidence/2026-10-03-food-reverse-controls'
# Pin the source used for the actual hours imports. The hours variant already
# applies its own Online Order centering correction; a moving base could double it.
BASE = D / 'food-oct3-full-list-pre-menu-alignment.svg'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

SAMPLES = [
    dict(key='blocky', state='S-FOOD-OCT3-BLOCKY-HOURS', eid='04',
         source='04-blocky-hours-expand.png', sheet_top=354, viewport_top=387,
         rows=[(1, 387), (2, 674), (3, 890)], expanded_row=1, extra=69,
         hours=[('Mon - Fri:', '08:00 - 20:00'), ('Sat:', '09:00 - 18:00'),
                ('Sun, public holiday:', 'Closed')]),
    dict(key='hcafe', state='S-FOOD-OCT3-HCAFE-HOURS', eid='08',
         source='08-hcafe-hours-expand.png', sheet_top=114, viewport_top=147,
         rows=[(4, 73), (5, 289), (6, 605), (7, 792)], expanded_row=5, extra=69,
         hours=[('Mon - Fri:', '08:00 - 22:00'), ('Sat:', '08:00 - 18:00'),
                ('Sun, public holiday:', '10:00 - 18:00')]),
    dict(key='va210', state='S-FOOD-OCT3-VA210-HOURS', eid='14',
         source='14-va210-hours-expand.png', sheet_top=114, viewport_top=154,
         rows=[(18, 154), (19, 341), (20, 528), (21, 754), (22, 890)],
         expanded_row=20, extra=39,
         hours=[('Mon - Sun, public holiday:', '00:00 - 23:59')]),
    dict(key='gourmet', state='S-FOOD-OCT3-GOURMET-HOURS', eid='19',
         source='19-gourmet-information-expand.png', sheet_top=114, viewport_top=147,
         rows=[(25, 131), (26, 356), (27, 572), (28, 737)],
         expanded_row=28, extra=42,
         hours=[('Mon - Fri:', '08:00 - 19:30'), ('Sat - Sun, public holiday:', 'Closed')]),
]

def child(g, ident):
    return next(n for n in g.iter() if n.get('id') == ident)

def expand_row(g, i, sample):
    extra = sample['extra']
    bg = child(g, 'RowBackground%02d' % i)
    old_height = float(bg.get('height'))
    bg.set('height', str(int(old_height + extra)))
    badge = child(g, 'OpeningHours%02d' % i)
    badge_top = float(next(iter(badge)).get('y'))
    # This is a reconstructed upward arrow, not a claim about native icon pixels.
    arrow = next(n for n in badge if n.tag.endswith('path'))
    ax = float(re.match(r'M([\d.]+)', arrow.get('d')).group(1))
    arrow.set('d', f'M{ax} {badge_top+19}L{ax+6} {badge_top+12}L{ax+12} {badge_top+19}Z')
    h = group(g, 'ExpandedHours%02d' % i)
    cy = badge_top + 54
    h.append(node('circle', cx=131, cy=cy, r=9, fill='none', stroke='#858585', stroke_width=2.5))
    path(h, f'M131 {cy-5}V{cy}L135 {cy+3}', '#858585', 2, stroke_linecap='round')
    for n, (day, time) in enumerate(sample['hours']):
        label(h, 151, badge_top+52+n*21, day, 14, '#555555')
        label(h, 328, badge_top+52+n*21, time, 14, '#555555')
    for ident in ['TagsViewport%02d' % i, 'OnlineOrder%02d' % i]:
        matches = [n for n in g if n.get('id') == ident]
        if matches:
            matches[0].set('transform', f'translate(0 {extra})')
    # Existing list source omits Online Order's60px when centering the ellipsis.
    # Correct that only in these new variants; existing Figma list remains pending.
    menu = child(g, 'VenueMenu%02d' % i)
    menu_shift = extra / 2 + (30 if i in [5, 10] else 0)
    menu.set('transform', f'translate(0 {menu_shift})')
    separator = [n for n in g if n.tag.endswith('path')][-1]
    separator.set('d', f'M0 {old_height+extra}H576')

def main():
    base = E.parse(BASE).getroot()
    metadata = D/'food-oct3-hours-sources.json'
    previous = json.loads(metadata.read_text()) if metadata.exists() else {}
    previous_sources = {s['file']: s for s in previous.get('sources', [])}
    sources = []
    for s in SAMPLES:
        r = node('svg', width=576, height=1024, viewBox='0 0 576 1024')
        title = node('title'); title.text = 'Food — '+s['key']+' observed hours expanded'; r.append(title)
        desc = node('desc'); desc.text = 'Finite editable reconstruction from archived native screenshot '+s['source']+'. Public labels/hours retained. Geometry/fonts/icons approximate; public logo/map imagery raster. No scrolling, live status or navigation implemented. Native source normalized to576x1024; exact native viewport extent unknown.'; r.append(desc)
        defs = copy.deepcopy(next(n for n in base if n.tag.endswith('defs')))
        cp = node('clipPath', id='HoursSampleViewport', clipPathUnits='userSpaceOnUse')
        bottom = 1024 if s['key'] == 'blocky' else 954
        # 954 here is only a finite content-visibility mask from these samples;
        # it is not the native scrolling viewport boundary.
        rect(cp, 0, s['viewport_top'], 576, bottom-s['viewport_top'], '#FFFFFF')
        defs.append(cp); r.append(defs)
        rect(r, 0, 0, 576, 1024, '#FFFFFF', id='ScreenBackground')
        assets = []
        if s['key'] == 'blocky':
            f = D / 'assets/food-oct3-blocky-hours-map.png'
            Image.open(P/s['source']).crop((0,100,576,354)).save(f)
            image(group(r, 'PublicHalfSheetMap'), f, 0, 100, 576, 254)
            assets.append(dict(file='assets/'+f.name, source_evidence_id='E-FOOD-REV-'+s['eid'], source_sha256=sha(P/s['source']), crop_xyxy=[0,100,576,354], sha256=sha(f), dimensions=[576,254], limits='Public campus geography only; screenshot raster, not live map'))
        else:
            r.append(copy.deepcopy(child(base, 'PublicMapStrip')))
        sheet = group(r, 'ObservedSheetChrome')
        y = s['sheet_top']
        sheet.append(node('path', d=f'M0 {y+26}Q0 {y} 24 {y}H552Q576 {y} 576 {y+26}V1024H0Z', fill='#FFFFFF'))
        rect(group(sheet, 'PanelHandle'), 238.5, y+16, 100, 7.5, '#31917D', rx=2)
        vp = group(r, 'FiniteObservedVenueViewport'); vp.set('clip-path', 'url(#HoursSampleViewport)')
        for i, top in s['rows']:
            g = copy.deepcopy(child(base, 'VenueRow%02d' % i))
            g.set('transform', f'translate(0 {top})')
            if i == s['expanded_row']:
                expand_row(g, i, s)
            vp.append(g)
        header(r, 'Food')
        f = D / ('food-oct3-'+s['key']+'-hours.svg')
        E.ElementTree(r).write(f, encoding='unicode', xml_declaration=True)
        rec = dict(file=f.name, state_id=s['state'], source_evidence_ids=['E-FOOD-REV-'+s['eid']], sha256=sha(f), dimensions=[576,1024], status='prepared_not_imported_not_replayed', observed_hours=s['hours'], expanded_row=s['expanded_row'], rows=s['rows'], finite_visible_mask=[0,s['viewport_top'],576,bottom], extra_row_height=s['extra'], menu_offset_correction=30 if s['key']=='hcafe' else 0, assets=assets)
        old = previous_sources.get(f.name, {})
        if old.get('sha256') == rec['sha256']:
            for key in ['status', 'figma', 'editor_evidence_ids', 'prototype_run_ids', 'spacing_repair']:
                if key in old:
                    rec[key] = old[key]
        sources.append(rec)
    result = dict(sources=sources, reused_source=dict(file=BASE.name, sha256=sha(BASE)), limits=['Four finite screenshot positions, not the full list or complete scroll geometry.', 'Independent text/vector source; public logos and campus map crops raster.', 'Hours imports retain the frozen pre-menu base and their own centering correction. Current full-list menus were corrected separately; menu interactions remain unconfigured.', 'Gourmet last-row height and954px content mask are reconstruction; clipped lower tags/bottom do not prove native extent.', 'No app input, Figma import, prototype interaction or human evaluation by generator.'])
    if all(previous_sources.get(s['file'], {}).get('sha256') == s['sha256'] for s in sources) and 'import_limits' in previous:
        result['import_limits'] = previous['import_limits']
    if all(previous_sources.get(s['file'], {}).get('sha256') == s['sha256'] for s in sources) and 'subsequent_full_list_alignment' in previous:
        result['subsequent_full_list_alignment'] = previous['subsequent_full_list_alignment']
    metadata.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(dict(sources=len(sources), figma_mutations=0)))

if __name__ == '__main__':
    main()
