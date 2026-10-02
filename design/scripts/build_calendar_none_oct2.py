"""Build the Oct2 native empty-filter branch as editable SVGs.
Fullscreen native sample is normalized to576x1024. Private event values/markers
are synthetic or omitted. Import/replay in Figma is a separate acceptance step.
"""
from pathlib import Path
from copy import deepcopy
import xml.etree.ElementTree as E
import json,hashlib
D=Path(__file__).resolve().parents[1]/'polyulife';N='http://www.w3.org/2000/svg';E.register_namespace('',N)
T=lambda n:'{'+N+'}'+n
get=lambda r,id:next(x for x in r.iter() if x.get('id')==id)
base=E.parse(D/'calendar-oct1.svg').getroot();base.set('height','1024');base.set('viewBox','0 0 576 1024');get(base,'ScreenBackground').set('height','1024')
base.remove(get(base,'EventCard'))
# Academic markers are removed too: these sources represent a public synthetic
# all-category backdrop and the native marker-free none result, not private dots.
grid=get(base,'CalendarGrid')
for g in grid:
 if g.get('id','').startswith('Day'):
  for c in list(g):
   if c.tag in [T('circle'),T('rect')]:g.remove(c)
  for text in g.findall(T('text')):text.set('fill','#4A4A4A');text.set('font-weight','400')
for text in grid.iter(T('text')):
 if text.get('y')=='215.0' and text.get('x') in ['68','141.5','215']:text.set('fill','#D6DBDF')
day=get(base,'Day2');day.insert(0,E.Element(T('rect'),{'x':'338.5','y':'176','width':'47','height':'47','rx':'16','fill':'#31917D'}));day.find(T('text')).set('fill','#FFFFFF');day.find(T('text')).set('font-weight','500')
sel=deepcopy(get(E.parse(D/'calendar-default-demo.svg').getroot(),'SelectedDay'))
sel.find(T('text')).text='Friday, October 2'
base.remove(get(base,'SelectedDay'));base.insert(6,sel)
nav=get(base,'BottomNavigation');nav.find(T('rect')).set('height','104')
for id,x,label in [('NavHome',58,'Home'),('NavCalendar',173,'Calendar'),('NavNotification',403,'Notification'),('NavMore',518,'More')]:
 E.SubElement(get(base,id),T('text'),{'x':str(x),'y':'989','fill':'#9FAFB9','font-family':'sans-serif','font-size':'14','text-anchor':'middle'}).text=label
card=deepcopy(get(E.parse(D/'calendar-default-demo.svg').getroot(),'SyntheticClassEvent'))
for image in list(card.findall(T('image'))):card.remove(image)
# Editable approximation of the generic classroom glyph; no embedded private asset.
g=E.Element(T('g'),{'id':'ClassGlyphApproximation'})
for tag,attrs in [('rect',{'x':'61','y':'630','width':'55','height':'36','rx':'3','fill':'#9FAFB9'}),('rect',{'x':'68','y':'637','width':'40','height':'22','fill':'#F5FCF0'}),('circle',{'cx':'58','cy':'652','r':'10','fill':'#9FAFB9'}),('rect',{'x':'42','y':'666','width':'33','height':'16','rx':'8','fill':'#9FAFB9'})]:E.SubElement(g,T(tag),attrs)
card.insert(1,g)
badge=deepcopy(get(E.parse(D/'calendar-default-demo.svg').getroot(),'DemoBadge'))
none=deepcopy(get(E.parse(D/'calendar-sep28.svg').getroot(),'NoEvent'))
for c in list(none):
 if c.tag==T('rect') and c.get('x')=='559':none.remove(c)
records=[]
for name,bg,draft,state,eids in [
 ('calendar-oct2-all-demo.svg','all',None,'S-NATIVE-OCT2-ALL',['E-NATIVE-OCT2-03']),
 ('calendar-oct2-draft-all-all.svg','all','all','S-NATIVE-OCT2-DRAFT-ALL-ALL',['E-NATIVE-OCT2-04']),
 ('calendar-oct2-draft-none-all.svg','all','none','S-NATIVE-OCT2-DRAFT-NONE-ALL',['E-NATIVE-OCT2-05','E-NATIVE-OCT2-08']),
 ('calendar-oct2-none.svg','none',None,'S-NATIVE-OCT2-NONE',['E-NATIVE-OCT2-09']),
 ('calendar-oct2-draft-none-none.svg','none','none','S-NATIVE-OCT2-DRAFT-NONE-NONE',['E-NATIVE-OCT2-10'])]:
 r=deepcopy(base); r.find(T('title')).text=f'Oct2 Calendar {bg}; draft {draft or "closed"}'
 r.find(T('desc')).text='Native Oct2 fullscreen filter sample. Historical fixed date. Editable geometry/icons/text approximate; private course values are DEMO and event dots omitted. Native X cancels none draft over all, none Apply removes all categories, reopen retains none. Other combinations and callers are unverified; full app not complete.'
 if bg=='all':r.insert(-1,deepcopy(card));r.append(deepcopy(badge))
 else:
  get(r,'CalendarCategory').find(T('text')).text='No Selected Event'
  filt=get(r,'Filter');filt.find(T('rect')).set('fill','#FFFFFF');filt.find(T('path')).set('fill','#E59B7B')
  r.insert(-1,deepcopy(none))
 if draft:
  panel=deepcopy(get(E.parse(D/f'calendar-filter-{draft}.svg').getroot(),'FilterOverlay'))
  get(panel,'FilterBackdrop').set('height','1024');r.append(panel)
 path=D/name;E.ElementTree(r).write(path,encoding='unicode')
 records.append({'file':name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'dimensions':[576,1024],
  'state_id':state,'source_evidence_ids':eids,'applied_background':bg,'draft':draft,'status':'prepared_not_imported',
  'limits':['Synthetic class values and no private markers.','Fullscreen native reference; not phone fidelity.','Finite None branch only; other filters, dates, main callers and data bounds incomplete.']})
(D/'calendar-oct2-none-sources.json').write_text(json.dumps({'sources':records},ensure_ascii=False,indent=2)+'\n')
