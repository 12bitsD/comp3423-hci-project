"""Redact an existing native Calendar capture and prepare editable DEMO structure.

No new native actions. Real event text and personal date-marker patterns are never
copied to the SVG. Requires Pillow for redaction; SVG construction uses stdlib.
"""
from pathlib import Path
from PIL import Image,ImageDraw,ImageChops
import hashlib,json,base64,xml.etree.ElementTree as E
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[2];D=R/'design/polyulife';P=R/'evidence/2026-10-02-calendar-default-source';P.mkdir(exist_ok=True)
raw=R/'evidence/raw/2026-09-28-full-audit/2026-09-28T15-50-57-332Z-02-71640203a330.jpg'
im=Image.open(raw).convert('RGB');assert im.size==(576,1082);im=im.crop((0,112,576,1082))
masks=[{'xyxy':[31,177,546,199],'fill':'#FFFFFF'},{'xyxy':[31,234,546,252],'fill':'#FFFFFF'},{'xyxy':[31,291,546,312],'fill':'#FFFFFF'},{'xyxy':[31,348,546,369],'fill':'#FFFFFF'},{'xyxy':[106,405,546,428],'fill':'#FFFFFF'},{'xyxy':[141,615,506,705],'fill':'#242424'}]
dr=ImageDraw.Draw(im)
for m in masks:
 x0,y0,x1,y1=m['xyxy'];dr.rectangle((x0,y0,x1-1,y1-1),fill=m['fill'])
source=P/'native-calendar-default-redacted.png';im.save(source)
assert ImageChops.difference(im,Image.open(source).convert('RGB')).getbbox() is None
# Public generic UI glyph crop excludes the redacted values.
icon=D/'assets/calendar-default-class-icon.png';im.crop((45,627,126,689)).save(icon)
ns='http://www.w3.org/2000/svg';xl='http://www.w3.org/1999/xlink';E.register_namespace('',ns);E.register_namespace('xlink',xl)
root=E.parse(D/'calendar-sep28.svg').getroot();tag=lambda n:'{'+ns+'}'+n
root.find(tag('title')).text='Calendar — September28 all categories — DEMO event'
root.find(tag('desc')).text='Historical native default month capture, prepared after redaction. Editable chrome reused from public academic month; native all-category filter styling and generic card geometry reconstructed. Private event values and date-marker patterns omitted. One synthetic sample is not a native event count. Approximate fonts/vectors. No new native observation, detail route or arbitrary filter behavior established.'
grid=next(g for g in root if g.attrib.get('id')=='CalendarGrid')
for g in grid.iter():
 for c in list(g):
  if c.tag==tag('circle'):g.remove(c)
selected=next(g for g in root if g.attrib.get('id')=='SelectedDay')
for e in selected.iter():
 if e.tag==tag('text') and e.text=='Acad calendar':e.text='Class | Exam | Payment | Acad calendar';e.set('font-size','17.5')
filterg=next(g for g in selected if g.attrib.get('id')=='Filter')
for e in filterg:
 if e.tag==tag('rect'):e.set('fill','#E59B7B')
 if e.tag==tag('path'):e.set('fill','#FFFFFF')
empty=next(g for g in root if g.attrib.get('id')=='NoEvent');idx=list(root).index(empty);root.remove(empty)
card=E.fromstring(f'''<g xmlns="{ns}" xmlns:xlink="{xl}" id="SyntheticClassEvent"><rect x="26" y="596" width="525" height="123" rx="11" fill="#F5FCF0"/><image x="45" y="627" width="81" height="62" xlink:href="data:image/png;base64,{base64.b64encode(icon.read_bytes()).decode()}"/><text x="148" y="641" font-family="Roboto" font-size="18.5" font-weight="700" fill="#141414">EXM2001 · DEMO CLASS</text><text x="148" y="665" font-family="Roboto" font-size="18.5" font-weight="700" fill="#141414">Synthetic course event</text><text x="148" y="691" font-family="Roboto" font-size="18.5" fill="#494949">09:00–10:00 | EXAMPLE ROOM</text><g id="DemoEventEllipsis"><circle cx="512" cy="657" r="3" fill="#A4B5BE"/><circle cx="521" cy="657" r="3" fill="#A4B5BE"/><circle cx="530" cy="657" r="3" fill="#A4B5BE"/></g></g>''')
root.insert(idx,card)
badge=E.fromstring(f'<g xmlns="{ns}" id="DemoBadge"><rect x="440" y="8" width="128" height="20" rx="3" fill="#FBF2D9"/><text x="504" y="22" text-anchor="middle" font-family="Roboto" font-size="10" fill="#66512C">DEMO EVENT VALUES</text></g>');root.append(badge)
svg=D/'calendar-default-demo.svg';E.ElementTree(root).write(svg,encoding='unicode');svg.write_text(svg.read_text()+'\n')
hf=lambda q:hashlib.sha256(q.read_bytes()).hexdigest();now=datetime.now(timezone.utc).isoformat()
item={'file':source.name,'sha256':hf(source),'dimensions':[576,970],'captured_at_utc':'2026-09-28T15:50:57.332Z','prepared_at_utc':now,'source':'Previously captured native Computer Use JPEG; historical redaction, not a new native execution.','description':'Default all-category month chrome; event values and personal date-marker patterns masked. Visible sample does not establish complete event/list bounds.','redaction':{'crop_xyxy':[0,112,576,1082],'opaque_masks':masks,'raw_file_ignored':str(raw.relative_to(R)),'raw_sha256':hf(raw)}}
sheet=Image.new('RGB',(576,1000),'#EEE');sheet.paste(im,(0,30));ImageDraw.Draw(sheet).text((8,8),'Historical native capture; private values/patterns redacted',fill='#111');q=P/'contact-sheet.png';sheet.save(q)
(P/'manifest.json').write_text(json.dumps({'kind':'historical_native_calendar_source_preparation','images':[item],'contact_sheet':{'file':q.name,'sha256':hf(q),'dimensions':list(sheet.size)},'scope':'Existing native state enriched; no new native observation. Public source is masked, SVG uses synthetic event values.'},ensure_ascii=False,indent=2)+'\n')
(D/'calendar-default-source.json').write_text(json.dumps({'state_id':'S-CALENDAR-DEFAULT','native_source':item,'design_source':'calendar-default-demo.svg','design_sha256':hf(svg),'reused_public_chrome':'calendar-sep28.svg','reused_public_chrome_sha256':hf(D/'calendar-sep28.svg'),'generic_icon':{'file':'assets/'+icon.name,'sha256':hf(icon),'dimensions':[81,62],'crop_xyxy':[45,627,126,689]},'status':'prepared_not_imported_not_replayed','limits':['Synthetic event values/count, not a copy of the private timetable.','Personal date-marker patterns omitted; no exact all-filter visual acceptance.','Class-card ellipsis destination not observed; no invented details.','No new native input; Mac currently locked.']},ensure_ascii=False,indent=2)+'\n')
print('Prepared redacted source and editable DEMO SVG.')
