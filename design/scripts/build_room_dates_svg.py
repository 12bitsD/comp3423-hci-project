"""Build editable September 30 Room snapshots from native evidence.

Only recorded date/filter combinations are represented. Today ALL combines its
observed top and bottom; Thursday/Friday ALL retain only the observed viewport.
The SVGs do not themselves implement Figma scrolling, loading or free input.
"""
from pathlib import Path
import copy, json, hashlib, xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[2]; D=R/'design/polyulife'; E=R/'evidence/2026-09-30-room-dates'
NS='http://www.w3.org/2000/svg'; ET.register_namespace('',NS)
def q(t):return '{'+NS+'}'+t
def el(t,**kw):return ET.Element(q(t),{k.replace('_','-'):str(v) for k,v in kw.items()})
def txt(x,y,s,size=17,color='#404040',anchor='middle',weight=400):
 n=el('text',x=x,y=y,fill=color,font_family='sans-serif',font_size=size,text_anchor=anchor,font_weight=weight);n.text=s;return n
def rect(x,y,w,h,fill,**kw):return el('rect',x=x,y=y,width=w,height=h,fill=fill,**kw)
def find(r,id):return r.find(".//*[@id='"+id+"']")
slots={'Today':[690,840,1290,1320], 'Thu':[], 'Fri':list(range(510,750,30))+[1290,1320], 'Sat':list(range(750,930,30)), 'Sun':[], 'Mon':[690,720,1290,1320], 'Tue':[510,540,690,720,1290,1320]}
days=[('Today','30-Sep'),('Thu','01-Oct'),('Fri','02-Oct'),('Sat','03-Oct'),('Sun','04-Oct'),('Mon','05-Oct'),('Tue','06-Oct')]
rows=[('today-all','S-ALL',0,'Today','all',0,0),('today-available','S-AVAILABLE',3,'Today','available',0,0),('thursday-available','S-ROOM-DATE-THU-AVAILABLE',4,'Thu','available',0,0),('thursday-all','S-ROOM-DATE-THU-ALL',5,'Thu','all',0,0),('friday-all','S-ROOM-DATE-FRI-ALL',6,'Fri','all',0,0),('friday-available','S-ROOM-DATE-FRI-AVAILABLE',7,'Fri','available',0,0),('saturday-available','S-ROOM-DATE-SAT-AVAILABLE',8,'Sat','available',0,0),('sunday-available','S-SUNEMPTY',9,'Sun','available',0,0),('monday-available','S-ROOM-DATE-MON-AVAILABLE',10,'Mon','available',-142,0),('tuesday-available','S-ROOM-DATE-TUE-AVAILABLE',11,'Tue','available',-142,0),('tuesday-reversed','S-ROOM-DATE-TUE-AVAILABLE',12,'Tue','available',0,0),('today-bottom','S-ROOM-DATE-TODAY-BOTTOM',15,'Today','all',0,-396)]
m=json.loads((E/'manifest.json').read_text());old=json.loads((D/'room-dates-sources.json').read_text()) if (D/'room-dates-sources.json').exists() else {'frames':[]};prior={v['file']:v for v in old['frames']};out=[]
for label,state,idx,day,mode,shift,offset in rows:
 root=ET.parse(D/'room-available.svg').getroot();root.set('height','1026');root.set('viewBox','0 0 576 1026');find(root,'ScreenBackground').set('height','1026')
 header=find(root,'Header');back=find(root,'Back');header.remove(back);bg=el('g',id='Back');bg.append(rect(12,36,52,54,'#FFFFFF',fill_opacity='0.001'));back.attrib.pop('id');bg.append(back);header.insert(1,bg)
 dates=find(root,'Dates');dates.clear();dates.set('id','DatesObserved20260930');dates.set('clip-path','url(#DatesViewport)')
 for i,(wd,date) in enumerate(days):
  x=70+i*(280/3)+shift;g=el('g',id='Date-'+wd);g.append(rect(x-40,112,80,67,'#54B39F' if wd==day else '#FFFFFF',rx=9));c='#FFFFFF' if wd==day else '#404040';g.extend([txt(x,140,wd,color=c,weight=600 if wd==day else 400),txt(x,163,date,color=c,weight=600 if wd==day else 400)]);dates.append(g)
 result=find(root,'ResultDate');result.find(q('text')).text=dict(days)[day]+' ('+day+')'
 if day=='Today':
  for n in list(result)[:-1]:n.set('transform','translate(-18,0)')
  result.find(q('text')).set('font-size','15')
 if mode=='all':
  for fid,sel in [('Filter-All',True),('Filter-Available',False)]:
   g=find(root,fid);g.find(q('rect')).set('fill','#54B39F' if sel else '#FFFFFF');g.find(q('rect')).set('stroke','#DCDCDC');g.find(q('text')).set('fill','#FFFFFF' if sel else '#090909');g.find(q('text')).set('font-weight','600' if sel else '400')
 results=find(root,'Results');results.remove(find(root,'Slots'))
 if mode=='available' and not slots[day]:
  g=el('g',id='NoAvailableRoom');g.append(el('path',d='M269 674L308 713M308 674L269 713',stroke='#319987',stroke_width=10,stroke_linecap='round'));g.extend([txt(288,768,'No available room',24,'#555555',weight=700),txt(288,800,'Please search another room.',21,'#A1B2BA',weight=500)]);results.append(g)
 else:
  minutes=slots[day] if mode=='available' else list(range(510,1350 if day=='Today' else 990,30))
  cp=el('clipPath',id='SlotsViewportClip');cp.append(rect(26,426,524,600,'#FFFFFF'));root.find(q('defs')).append(cp)
  vp=el('g',id='SlotsObservedViewport',clip_path='url(#SlotsViewportClip)');g=el('g',id='SlotsObservedContent',transform=f'translate(0,{offset})');g.append(rect(26,426,524,996 if day=='Today' and mode=='all' else max(0,((len(minutes)+1)//2)*70),'#FFFFFF'))
  for i,t in enumerate(minutes):
   x=27 if i%2==0 else 295;y=434+(i//2)*70;green=t in slots[day];end=t+30;v=f'{t//60:02d}:{t%60:02d}-{end//60:02d}:{end%60:02d}';s=el('g',id='Slot-'+v.replace(':',''));s.append(rect(x,y,255,55,'#E6F6DB' if green else '#FFD0D2',rx=8,stroke='#DDDFDC',stroke_width=1.5));s.append(el('circle',cx=x+67,cy=y+27.5,r=4.7,fill='#79AC4E' if green else '#BA3D24'));s.append(txt(x+83,y+34,v,17,'#080808','start'));g.append(s)
  if mode=='all' and day!='Today':
   for x in [27,295]:g.append(rect(x,994,255,32,'#FFD0D2',rx=8,stroke='#DDDFDC',stroke_width=1.5))
  vp.append(g);results.append(vp)
 root.find(q('title')).text='Room September30 — '+label;root.find(q('desc')).text='Editable native snapshot; 576x1026 viewport. Fixed AG206 date/filter and historical data. Fonts/icons approximate; cursor omitted. Today ALL combines observed top and bottom; other ALL lists stop at observed partial row. Scrolling and prototype controls require separate Figma UI configuration; no free input/live data or loading measurement.'
 file='room-dates-'+label+'.svg';p=D/file;ET.ElementTree(root).write(p,encoding='unicode');img=m['images'][idx];sources=[img]
 if mode=='all' and day=='Today':sources=[m['images'][2],m['images'][15]]
 o={'file':file,'state_id':state,'context_variant':'20260930-'+label,'source_evidence_ids':['E-ROOM-DATES-'+str(m['images'].index(v)).zfill(2) for v in sources],'source_evidence_paths':['evidence/2026-09-30-room-dates/'+v['file'] for v in sources],'source_evidence_sha256':[v['sha256'] for v in sources],'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'dimensions':[576,1026],'figma_node_id':prior.get(file,{}).get('figma_node_id'),'status':prior.get(file,{}).get('status','source_only_not_imported'),'label':label,'date':dict(days)[day],'filter':mode,'date_strip_offset':shift,'list_offset':offset};out.append(o)
(D/'room-dates-sources.json').write_text(json.dumps({'status':old.get('status','source_preparation_full_scope_incomplete'),'frames':out},ensure_ascii=False,indent=2)+'\n');print('Prepared',len(out),'editable sources; no Figma completion claim.')
