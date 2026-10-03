"""Editable finite Sept28 PQ query samples from public native evidence.

Generates files only. No native executions, Figma mutations or full-app claim.
"""
from pathlib import Path
import xml.etree.ElementTree as E
import json, hashlib
R=Path(__file__).resolve().parents[2];D=R/'design/polyulife';P=R/'evidence/2026-09-28-full-audit'
NS='http://www.w3.org/2000/svg';E.register_namespace('',NS);tag=lambda n:f'{{{NS}}}{n}'
find=lambda r,i:next(n for n in r.iter() if n.get('id')==i)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def el(parent,n,attrs,txt=None):
 e=E.SubElement(parent,tag(n),{k:str(v) for k,v in attrs.items()});e.text=txt;return e

def build(kind,value,tue,focused):
 r=E.parse(D/'room-empty.svg').getroot()
 h=find(r,'Header');old=find(r,'Back');h.remove(old)
 g=el(h,'g',{'id':'Back'});el(g,'rect',{'x':8,'y':35,'width':50,'height':60,'fill':'#FFFFFF','opacity':'0.001'});old.attrib.pop('id');g.append(old)
 dates=find(r,'Dates');find(r,'SelectedDate').set('x','126' if tue else '30')
 for child in dates:
  if child.tag!=tag('g'): continue
  sel=child.get('id')==('Date-Tue-29-Sep' if tue else 'Date-Mon-28-Sep')
  for t in child:
   t.set('fill','#FFFFFF' if sel else '#404040');t.set('font-weight','600' if sel else '400')
  if child.get('id')=='Date-Tue-29-Sep':
   el(child,'rect',{'x':126,'y':112,'width':80,'height':67,'fill':'#FFFFFF','opacity':'0.001'})
 search=find(r,'Search')
 if kind=='initial':
  search.remove(find(r,'SearchButton'))
  for child in list(dates):
   if child.get('id') in ['Date-Thu-01-Oct','Date-Fri-02-Oct','Date-Sat-03-Oct']:dates.remove(child)
 if value: el(search,'text',{'id':'QueryText','x':122,'y':233,'fill':'#090909','font-family':'sans-serif','font-size':22},value)
 if focused:
  x=208 if value else 116
  el(search,'path',{'id':'InputCaret','d':f'M{x} 209V237','stroke':'#2876E6','stroke-width':2})
  if value:
   el(search,'path',{'d':'M417 215L432 230M432 215L417 230','stroke':'#9CAFB9','stroke-width':3})
 if kind not in ['initial','typed']:
  empty=find(r,'EmptyState');empty.clear();empty.set('id','NoResultState')
  el(empty,'path',{'d':'M270 411L306 447M306 411L270 447','stroke':'#31917D','stroke-width':8,'stroke-linecap':'round'})
  el(empty,'text',{'x':288,'y':498,'fill':'#575757','font-family':'sans-serif','font-size':25,'font-weight':600,'text-anchor':'middle'},'No room found')
  el(empty,'text',{'x':288,'y':530,'fill':'#9CAFB9','font-family':'sans-serif','font-size':23,'font-weight':500,'text-anchor':'middle'},'Please search another room.')
 r.find(tag('title')).text='Room Finder — Sept28 PQ sample '+kind
 r.find(tag('desc')).text=('Editable finite reconstruction from public native source; fonts/icons/geometry approximate. Pointer/halo omitted. Initial 1060×1898 source uniformly scaled to576 width and lower blank61.37px clipped; other sources576×970. Keyboard P/B/BackSpace are prototype fixed-input proxies, not arbitrary native input. Initial three dates/no search retained; capture dimension difference does not prove asynchronous cause.')
 return r

specs=[('initial','',False,False,'S-EMPTY','E-EMPTY','room-134522-empty.png'),('typed','PQ604',False,False,'S-PQ','E-PQ','room-135053-pq604-input.png'),('none','PQ604',False,False,'S-PQNONE','E-PQNONE','room-135149-pq604-no-room.png'),('b-focused','PQ604B',False,True,'S-PQB','E-PQB','room-135252-pq604b-input.png'),('b-none','PQ604B',False,False,'S-PQBNONE','E-PQBNONE','room-135331-pq604b-no-room.png'),('tue','PQ604B',True,False,'S-TUE','E-TUE','room-135352-next-date.png'),('cleared','',True,True,'S-CLEARED','E-CLEARED','room-135506-input-cleared.png')]
record_path=D/'room-pq-query-sources.json'
old={v['file']:v for v in json.loads(record_path.read_text()).get('sources',[])} if record_path.exists() else {}
records=[]
for kind,val,tue,focused,state,eid,source in specs:
 file='room-pq-'+kind+'.svg';E.ElementTree(build(kind,val,tue,focused)).write(D/file,encoding='unicode',xml_declaration=True)
 records.append({'file':file,'sha256':sha(D/file),'state_id':state,'source_evidence_ids':[eid],'source_file':str((P/source).relative_to(R)),'source_sha256':sha(P/source),'dimensions':[576,970],'status':'prepared_not_imported_not_replayed','context_variant':'20260928-tuesday-cleared-stale' if state=='S-CLEARED' else '20260928-pq-query'})
for record in records:
 previous=old.get(record['file'])
 if previous and previous['sha256']==record['sha256']:record.update(previous)
record_path.write_text(json.dumps({'sources':records,'limits':['Historical September28/29 date context, finite inputs only; complete app not_verified.','Initial source scaled and blank lower portion clipped; no claim of responsive layout or loading cause.','Editable vectors approximate native fonts/icons; pointer/halo omitted; bottom capture fringe omitted.']},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'prepared_sources':len(records),'figma_mutations':0,'native_executions':0}))
